                                              
                                  

"""Post-processing image optimization of OCR PDFs."""

from __future__ import annotations

import logging
import sys
import tempfile
import threading
from collections import defaultdict
from collections.abc import Callable, Iterator, MutableSet, Sequence
from os import fspath
from pathlib import Path
from typing import Any, NamedTuple, NewType
from zlib import compress

import img2pdf
from pikepdf import (
    Dictionary,
    Name,
    Object,
    ObjectStreamMode,
    Pdf,
    PdfError,
    PdfImage,
    Stream,
    UnsupportedImageTypeError,
)
from pikepdf.models.image import HifiPrintImageNotTranscodableError
from PIL import Image

from ocrmypdf._concurrent import Executor, SerialExecutor
from ocrmypdf._exec import jbig2enc, pngquant
from ocrmypdf._jobcontext import PdfContext
from ocrmypdf._progressbar import ProgressBar
from ocrmypdf.exceptions import OutputFileAccessError
from ocrmypdf.helpers import IMG2PDF_KWARGS, safe_symlink

log = logging.getLogger(__name__)

DEFAULT_JPEG_QUALITY = 75
DEFAULT_PNG_QUALITY = 70


Xref = NewType('Xref', int)


class XrefExt(NamedTuple):
                                              

    xref: Xref
    ext: str


def img_name(root: Path, xref: Xref, ext: str) -> Path:
                                                                          
    return root / f'{xref:08d}{ext}'


def png_name(root: Path, xref: Xref) -> Path:
                                                         
    return img_name(root, xref, '.png')


def jpg_name(root: Path, xref: Xref) -> Path:
                                                          
    return img_name(root, xref, '.jpg')


def extract_image_filter(
    image: Stream, xref: Xref
) -> tuple[PdfImage, tuple[Name, Object]] | None:
                                               
    if image.Subtype != Name.Image:
        return None
    if not isinstance(image.Length, int) or image.Length < 100:
        log.debug(f"xref {xref}: skipping image with small stream size")
        return None
    if (
        not isinstance(image.Width, int)
        or not isinstance(image.Height, int)
        or image.Width < 8
        or image.Height < 8
    ):             
        log.debug(f"xref {xref}: skipping image with unusually small dimensions")
        return None

    pim = PdfImage(image)

    if len(pim.filter_decodeparms) > 1:
        first_filtdp = pim.filter_decodeparms[0]
        second_filtdp = pim.filter_decodeparms[1]
        if (
            len(pim.filter_decodeparms) == 2
            and first_filtdp[0] == Name.FlateDecode
            and first_filtdp[1] is not None
            and first_filtdp[1].get(Name.Predictor, 1) == 1
            and second_filtdp[0] == Name.DCTDecode
            and not second_filtdp[1]
        ):
            log.debug(
                f"xref {xref}: found image compressed as /FlateDecode /DCTDecode, "
                "marked for JPEG optimization"
            )
            filtdp = pim.filter_decodeparms[1]
        else:
            log.debug(f"xref {xref}: skipping image with multiple compression filters")
            return None
    else:
        filtdp = pim.filter_decodeparms[0]

    if pim.bits_per_component > 8:
        log.debug(f"xref {xref}: skipping wide gamut image")
        return None                                     

    if filtdp[0] == Name.JPXDecode:
        log.debug(f"xref {xref}: skipping JPEG2000 image")
        return None                     

    if filtdp[0] == Name.CCITTFaxDecode and filtdp[1].get('/K', 0) >= 0:
        log.debug(f"xref {xref}: skipping CCITT Group 3 image")
        return None                                       

    if Name.Decode in image:
        log.debug(f"xref {xref}: skipping image with Decode table")
        return None                                        

    return pim, filtdp


def extract_image_jbig2(
    *, pdf: Pdf, root: Path, image: Stream, xref: Xref, options
) -> XrefExt | None:
                                                      
    del options              

    result = extract_image_filter(image, xref)
    if result is None:
        return None
    pim, filtdp = result

    if (
        pim.bits_per_component == 1
        and filtdp[0] != Name.JBIG2Decode
        and jbig2enc.available()
    ):
                                                                   
                                                                      
                                                                         
                                                                          
                           
        colorspace = pim.obj.get(Name.ColorSpace, None)
        if colorspace is not None or pim.image_mask:
            try:
                                                                     
                pim.obj.ColorSpace = Name.DeviceGray
                imgname = root / f'{xref:08d}'
                with imgname.open('wb') as f:
                    ext = pim.extract_to(stream=f)
                                                                   
                                                                      
                                                        
                imgname.rename(imgname.with_suffix(".prejbig2" + ext))
            except NotImplementedError as e:
                if '/Decode' in str(e):
                    log.debug(
                        f"xref {xref}: skipping image with unsupported Decode table"
                    )
                    return None
                raise
            except UnsupportedImageTypeError:
                return None
            finally:
                                                                                     
                if colorspace is not None:
                    pim.obj.ColorSpace = colorspace
                else:
                    del pim.obj.ColorSpace
            return XrefExt(xref, ".prejbig2" + ext)
    return None


def extract_image_generic(
    *, pdf: Pdf, root: Path, image: Stream, xref: Xref, options
) -> XrefExt | None:
                                   
    result = extract_image_filter(image, xref)
    if result is None:
        return None
    pim, filtdp = result

                                                                        
    if pim.bits_per_component == 1:
        return None

    if filtdp[0] == Name.DCTDecode and options.optimize >= 2:
                                                                              
                                                                          
                                                                             
                   
                                                          
                                                                    
                                        
                         
        try:
            imgname = root / f'{xref:08d}'
            with imgname.open('wb') as f:
                ext = pim.extract_to(stream=f)
            imgname.rename(imgname.with_suffix(ext))
        except (UnsupportedImageTypeError, HifiPrintImageNotTranscodableError):
            return None
        return XrefExt(xref, ext)
    elif (
        pim.indexed
        and pim.colorspace in pim.SIMPLE_COLORSPACES
        and options.optimize >= 3
    ):
                                                                           
                             
        pim.as_pil_image().save(png_name(root, xref))
        return XrefExt(xref, '.png')
    elif not pim.indexed and pim.colorspace in pim.SIMPLE_COLORSPACES:
                                                                            
                                               
        try:
            pim.as_pil_image().save(png_name(root, xref))
        except NotImplementedError:
            log.warning("PDF contains an atypical image that cannot be optimized.")
            return None
        return XrefExt(xref, '.png')
    elif (
        not pim.indexed
        and pim.colorspace == Name.ICCBased
        and pim.bits_per_component == 1
        and not options.jbig2_lossy
    ):
                                                                           
                                                                           
                     
        pim.as_pil_image().save(png_name(root, xref))
        return XrefExt(xref, '.png')

    return None


def _find_image_xrefs_container(
    pdf: Pdf,
    container: Object,
    pageno: int,
    include_xrefs: MutableSet[Xref],
    exclude_xrefs: MutableSet[Xref],
    pageno_for_xref: dict[Xref, int],
    depth: int = 0,
):
                                                                                   
    if depth > 10:
        log.warning("Recursion depth exceeded in _find_image_xrefs_page")
        return
    try:
        xobjs = container.Resources.XObject
    except AttributeError:
        return
    for _imname, image in dict(xobjs).items():
        if image.objgen[1] != 0:
            continue                                       
        xref = Xref(image.objgen[0])
        if xref in include_xrefs or xref in exclude_xrefs:
            continue                     
        if Name.Subtype in image and image.Subtype == Name.Form:
                                        
            log.debug(f"Recursing into Form XObject {_imname} in page {pageno}")
            _find_image_xrefs_container(
                pdf,
                image,
                pageno,
                include_xrefs,
                exclude_xrefs,
                pageno_for_xref,
                depth + 1,
            )
            continue
        if Name.SMask in image:
                               
            smask_xref = Xref(image.SMask.objgen[0])
            exclude_xrefs.add(smask_xref)
            log.debug(f"xref {smask_xref}: skipping image because it is an SMask")
        include_xrefs.add(xref)
        log.debug(f"xref {xref}: treating as an optimization candidate")
        if xref not in pageno_for_xref:
            pageno_for_xref[xref] = pageno


def _find_image_xrefs(pdf: Pdf):
    include_xrefs: MutableSet[Xref] = set()
    exclude_xrefs: MutableSet[Xref] = set()
    pageno_for_xref: dict[Xref, int] = {}

    for pageno, page in enumerate(pdf.pages):
        _find_image_xrefs_container(
            pdf, page.obj, pageno, include_xrefs, exclude_xrefs, pageno_for_xref
        )

    working_xrefs = include_xrefs - exclude_xrefs
    return working_xrefs, pageno_for_xref


def extract_images(
    pdf: Pdf,
    root: Path,
    options,
    extract_fn: Callable[..., XrefExt | None],
) -> Iterator[tuple[int, XrefExt]]:
           
    errors = 0
    working_xrefs, pageno_for_xref = _find_image_xrefs(pdf)
    for xref in working_xrefs:
        image = pdf.get_object((xref, 0))
        try:
            result = extract_fn(
                pdf=pdf, root=root, image=image, xref=xref, options=options
            )
        except Exception:                                
            log.exception(
                f"xref {xref}: While extracting this image, an error occurred"
            )
            errors += 1
        else:
            if result:
                _, ext = result
                yield pageno_for_xref[xref], XrefExt(xref, ext)


def extract_images_generic(
    pdf: Pdf, root: Path, options
) -> tuple[list[Xref], list[Xref]]:
                                                           
    jpegs = []
    pngs = []
    for _, xref_ext in extract_images(pdf, root, options, extract_image_generic):
        log.debug('%s', xref_ext)
        if xref_ext.ext == '.png':
            pngs.append(xref_ext.xref)
        elif xref_ext.ext == '.jpg':
            jpegs.append(xref_ext.xref)
    log.debug(f"Optimizable images: JPEGs: {len(jpegs)} PNGs: {len(pngs)}")
    return jpegs, pngs


def extract_images_jbig2(pdf: Pdf, root: Path, options) -> dict[int, list[XrefExt]]:
                                                                          
    jbig2_groups = defaultdict(list)
    for pageno, xref_ext in extract_images(pdf, root, options, extract_image_jbig2):
        group = pageno // options.jbig2_page_group_size
        jbig2_groups[group].append(xref_ext)

    log.debug(f"Optimizable images: JBIG2 groups: {len(jbig2_groups)}")
    return jbig2_groups


def _produce_jbig2_images(
    jbig2_groups: dict[int, list[XrefExt]], root: Path, options, executor: Executor
) -> None:
                                                 

    def jbig2_group_args(root: Path, groups: dict[int, list[XrefExt]]):
        for group, xref_exts in groups.items():
            prefix = f'group{group:08d}'
            yield (
                fspath(root),        
                (img_name(root, xref, ext) for xref, ext in xref_exts),            
                prefix,               
                options.jbig2_threshold,
            )

    def jbig2_single_args(root: Path, groups: dict[int, list[XrefExt]]):
        for group, xref_exts in groups.items():
            prefix = f'group{group:08d}'
                                                                            
            for n, xref_ext in enumerate(xref_exts):
                xref, ext = xref_ext
                yield (
                    fspath(root),
                    img_name(root, xref, ext),
                    root / f'{prefix}.{n:04d}',
                    options.jbig2_threshold,
                )

    if options.jbig2_page_group_size > 1:
        jbig2_args = jbig2_group_args
        jbig2_convert = jbig2enc.convert_group
    else:
        jbig2_args = jbig2_single_args
        jbig2_convert = jbig2enc.convert_single

    executor(
        use_threads=True,
        max_workers=options.jobs,
        progress_kwargs=dict(
            total=len(jbig2_groups),
            desc="JBIG2",
            unit='item',
            disable=not options.progress_bar,
        ),
        task=jbig2_convert,
        task_arguments=jbig2_args(root, jbig2_groups),
    )


def convert_to_jbig2(
    pdf: Pdf,
    jbig2_groups: dict[int, list[XrefExt]],
    root: Path,
    options,
    executor: Executor,
) -> None:
           
    jbig2_globals_dict: Dictionary | None

    _produce_jbig2_images(jbig2_groups, root, options, executor)

    for group, xref_exts in jbig2_groups.items():
        prefix = f'group{group:08d}'
        jbig2_symfile = root / (prefix + '.sym')
        if jbig2_symfile.exists():
            jbig2_globals_data = jbig2_symfile.read_bytes()
            jbig2_globals = Stream(pdf, jbig2_globals_data)
            jbig2_globals_dict = Dictionary(JBIG2Globals=jbig2_globals)
        elif options.jbig2_page_group_size == 1:
            jbig2_globals_dict = None
        else:
            raise FileNotFoundError(jbig2_symfile)

        for n, xref_ext in enumerate(xref_exts):
            xref, _ = xref_ext
            jbig2_im_file = root / (prefix + f'.{n:04d}')
            jbig2_im_data = jbig2_im_file.read_bytes()
            im_obj = pdf.get_object(xref, 0)
            im_obj.write(
                jbig2_im_data, filter=Name.JBIG2Decode, decode_parms=jbig2_globals_dict
            )


def _optimize_jpeg(
    xref: Xref, in_jpg: Path, opt_jpg: Path, jpeg_quality: int
) -> tuple[Xref, Path | None]:
    with Image.open(in_jpg) as im:
        im.save(opt_jpg, optimize=True, quality=jpeg_quality)

    if opt_jpg.stat().st_size > in_jpg.stat().st_size:
        log.debug(f"xref {xref}, jpeg, made larger - skip")
        opt_jpg.unlink()
        return xref, None
    return xref, opt_jpg


def transcode_jpegs(
    pdf: Pdf, jpegs: Sequence[Xref], root: Path, options, executor: Executor
) -> None:
                                                            

    def jpeg_args() -> Iterator[tuple[Xref, Path, Path, int]]:
        for xref in jpegs:
            in_jpg = jpg_name(root, xref)
            opt_jpg = in_jpg.with_suffix('.opt.jpg')
            yield xref, in_jpg, opt_jpg, options.jpeg_quality

    def finish_jpeg(result: tuple[Xref, Path | None], pbar: ProgressBar):
        xref, opt_jpg = result
        if opt_jpg:
            compdata = opt_jpg.read_bytes()                                    
            im_obj = pdf.get_object(xref, 0)
            im_obj.write(compdata, filter=Name.DCTDecode)
        pbar.update()

    executor(
        use_threads=True,                                                   
        max_workers=options.jobs,
        progress_kwargs=dict(
            desc="Recompressing JPEGs",
            total=len(jpegs),
            unit='image',
            disable=not options.progress_bar,
        ),
        task=_optimize_jpeg,
        task_arguments=jpeg_args(),
        task_finished=finish_jpeg,
    )


def _find_deflatable_jpeg(
    *, pdf: Pdf, root: Path, image: Stream, xref: Xref, options
) -> XrefExt | None:
    result = extract_image_filter(image, xref)
    if result is None:
        return None
    _pim, filtdp = result

    if filtdp[0] == Name.DCTDecode and not filtdp[1] and options.optimize >= 1:
        return XrefExt(xref, '.memory')

    return None


def _deflate_jpeg(
    pdf: Pdf, lock: threading.Lock, xref: Xref, complevel: int
) -> tuple[Xref, bytes]:
    with lock:
        xobj = pdf.get_object(xref, 0)
        try:
            data = xobj.read_raw_bytes()
        except PdfError:
            return xref, b''
    compdata = compress(data, complevel)
    if len(compdata) >= len(data):
        return xref, b''
    return xref, compdata


def deflate_jpegs(pdf: Pdf, root: Path, options, executor: Executor) -> None:
           
    jpegs = []
    for _pageno, xref_ext in extract_images(pdf, root, options, _find_deflatable_jpeg):
        xref = xref_ext.xref
        log.debug(f'xref {xref}: marking this JPEG as deflatable')
        jpegs.append(xref)

    complevel = 9 if options.optimize == 3 else 6

                                                             
    lock = threading.Lock()

    def deflate_args() -> Iterator:
        for xref in jpegs:
            yield pdf, lock, xref, complevel

    def finish(result: tuple[Xref, bytes], pbar: ProgressBar):
        xref, compdata = result
        if len(compdata) > 0:
            with lock:
                xobj = pdf.get_object(xref, 0)
                xobj.write(compdata, filter=[Name.FlateDecode, Name.DCTDecode])
        pbar.update()

    executor(
        use_threads=True,                                                    
        max_workers=options.jobs,
        progress_kwargs=dict(
            desc="Deflating JPEGs",
            total=len(jpegs),
            unit='image',
            disable=not options.progress_bar,
        ),
        task=_deflate_jpeg,
        task_arguments=deflate_args(),
        task_finished=finish,
    )


def _transcode_png(pdf: Pdf, filename: Path, xref: Xref) -> bool:
    output = filename.with_suffix('.png.pdf')
    with output.open('wb') as f:
        img2pdf.convert(fspath(filename), outputstream=f, **IMG2PDF_KWARGS)

    with Pdf.open(output) as pdf_image:
        foreign_image = next(iter(pdf_image.pages[0].images.values()))
        local_image = pdf.copy_foreign(foreign_image)

        im_obj = pdf.get_object(xref, 0)
        im_obj.write(
            local_image.read_raw_bytes(),
            filter=local_image.Filter,
            decode_parms=local_image.DecodeParms,
        )

                                               
        del_keys = set(im_obj.keys()) - set(local_image.keys())
                                                                          
                                                                          
                                                                         
        keep_fields = {
            '/ID',
            '/Intent',
            '/Interpolate',
            '/Mask',
            '/Metadata',
            '/OC',
            '/OPI',
            '/SMask',
            '/StructParent',
        }
        del_keys -= keep_fields
        for key in local_image.keys():
            if key != Name.Length and str(key) not in keep_fields:
                im_obj[key] = local_image[key]
        for key in del_keys:
            del im_obj[key]
    return True


def transcode_pngs(
    pdf: Pdf,
    images: Sequence[Xref],
    image_name_fn: Callable[[Path, Xref], Path],
    root: Path,
    options,
    executor: Executor,
) -> None:
                                          
    modified: MutableSet[Xref] = set()
    if options.optimize >= 2:
        png_quality = (
            max(10, options.png_quality - 10),
            min(100, options.png_quality + 10),
        )

        def pngquant_args():
            for xref in images:
                log.debug(image_name_fn(root, xref))
                yield (
                    image_name_fn(root, xref),
                    png_name(root, xref),
                    png_quality[0],
                    png_quality[1],
                )
                modified.add(xref)

        executor(
            use_threads=True,
            max_workers=options.jobs,
            progress_kwargs=dict(
                desc="PNGs",
                total=len(images),
                unit='image',
                disable=not options.progress_bar,
            ),
            task=pngquant.quantize,
            task_arguments=pngquant_args(),
        )

    for xref in modified:
        filename = png_name(root, xref)
        _transcode_png(pdf, filename, xref)


DEFAULT_EXECUTOR = SerialExecutor()


def optimize(
    input_file: Path,
    output_file: Path,
    context: PdfContext,
    save_settings: dict[str, Any],
    executor: Executor = DEFAULT_EXECUTOR,
) -> Path:
                                        
    options = context.options
    if options.optimize == 0:
        safe_symlink(input_file, output_file)
        return output_file

    if options.jpeg_quality == 0:
        options.jpeg_quality = DEFAULT_JPEG_QUALITY if options.optimize < 3 else 40
    if options.png_quality == 0:
        options.png_quality = DEFAULT_PNG_QUALITY if options.optimize < 3 else 30
    if options.jbig2_page_group_size == 0:
        options.jbig2_page_group_size = 10 if options.jbig2_lossy else 1

    with Pdf.open(input_file) as pdf:
        root = output_file.parent / 'images'
        root.mkdir(exist_ok=True)

        jpegs, pngs = extract_images_generic(pdf, root, options)
        transcode_jpegs(pdf, jpegs, root, options, executor)
        deflate_jpegs(pdf, root, options, executor)
                                   
                                 
                                                                
        transcode_pngs(pdf, pngs, png_name, root, options, executor)

        jbig2_groups = extract_images_jbig2(pdf, root, options)
        convert_to_jbig2(pdf, jbig2_groups, root, options, executor)

        target_file = output_file.with_suffix('.opt.pdf')
        pdf.remove_unreferenced_resources()
        pdf.save(target_file, **save_settings)

    input_size = input_file.stat().st_size
    output_size = target_file.stat().st_size
    if output_size == 0:
        raise OutputFileAccessError(
            f"Output file not created after optimizing. We probably ran "
            f"out of disk space in the temporary folder: {tempfile.gettempdir()}."
        )
    savings = 1 - output_size / input_size

    if savings < 0:
        log.info(
            "Image optimization did not improve the file - "
            "optimizations will not be used"
        )
                                        
        with Pdf.open(input_file) as pdf:
            pdf.remove_unreferenced_resources()
            pdf.save(output_file, **save_settings)
    else:
        safe_symlink(target_file, output_file)

    return output_file


def main(infile, outfile, level, jobs=1):
                                                        
    from shutil import copy                                           
    from tempfile import TemporaryDirectory                                           

    class OptimizeOptions:
                                         

        def __init__(
            self, input_file, jobs, optimize_, jpeg_quality, png_quality, jb2lossy
        ):
            self.input_file = input_file
            self.jobs = jobs
            self.optimize = optimize_
            self.jpeg_quality = jpeg_quality
            self.png_quality = png_quality
            self.jbig2_page_group_size = 0
            self.jbig2_lossy = jb2lossy
            self.jbig2_threshold = 0.85
            self.quiet = True
            self.progress_bar = False

    infile = Path(infile)
    options = OptimizeOptions(
        input_file=infile,
        jobs=jobs,
        optimize_=int(level),
        jpeg_quality=0,               
        png_quality=0,
        jb2lossy=False,
    )

    with TemporaryDirectory() as tmpdir:
        context = PdfContext(options, tmpdir, infile, None, None)
        tmpout = Path(tmpdir) / 'out.pdf'
        optimize(
            infile,
            tmpout,
            context,
            dict(
                compress_streams=True,
                preserve_pdfa=True,
                object_stream_mode=ObjectStreamMode.generate,
            ),
        )
        copy(fspath(tmpout), fspath(outfile))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
