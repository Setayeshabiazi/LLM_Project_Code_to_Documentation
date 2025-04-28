                      

                                              
                                  
"""Extract information about the content of a PDF."""

from __future__ import annotations

import atexit
import logging
import re
import statistics
from collections import defaultdict
from collections.abc import Callable, Container, Iterable, Iterator, Mapping, Sequence
from contextlib import contextmanager, nullcontext
from decimal import Decimal
from enum import Enum, auto
from functools import partial
from math import hypot, inf, isclose
from os import PathLike
from pathlib import Path
from typing import NamedTuple
from warnings import warn

from pdfminer.layout import LTPage, LTTextBox
from pikepdf import (
    Dictionary,
    Matrix,
    Name,
    Object,
    Page,
    Pdf,
    PdfImage,
    PdfInlineImage,
    Stream,
    UnsupportedImageTypeError,
    parse_content_stream,
)

from ocrmypdf._concurrent import Executor, SerialExecutor
from ocrmypdf._progressbar import ProgressBar
from ocrmypdf.exceptions import EncryptedPdfError, InputFileError
from ocrmypdf.helpers import Resolution, available_cpu_count, pikepdf_enable_mmap
from ocrmypdf.pdfinfo.layout import (
    LTStateAwareChar,
    PdfMinerState,
    get_page_analysis,
    get_text_boxes,
)

logger = logging.getLogger()


class Colorspace(Enum):
                                                           

                                  
    gray = auto()
    rgb = auto()
    cmyk = auto()
    lab = auto()
    icc = auto()
    index = auto()
    sep = auto()
    devn = auto()
    pattern = auto()
    jpeg2000 = auto()


class Encoding(Enum):
                                                         

                                  
    ccitt = auto()
    jpeg = auto()
    jpeg2000 = auto()
    jbig2 = auto()
    asciihex = auto()
    ascii85 = auto()
    lzw = auto()
    flate = auto()
    runlength = auto()


FloatRect = tuple[float, float, float, float]

FRIENDLY_COLORSPACE: dict[str, Colorspace] = {
    '/DeviceGray': Colorspace.gray,
    '/CalGray': Colorspace.gray,
    '/DeviceRGB': Colorspace.rgb,
    '/CalRGB': Colorspace.rgb,
    '/DeviceCMYK': Colorspace.cmyk,
    '/Lab': Colorspace.lab,
    '/ICCBased': Colorspace.icc,
    '/Indexed': Colorspace.index,
    '/Separation': Colorspace.sep,
    '/DeviceN': Colorspace.devn,
    '/Pattern': Colorspace.pattern,
    '/G': Colorspace.gray,                                            
    '/RGB': Colorspace.rgb,
    '/CMYK': Colorspace.cmyk,
    '/I': Colorspace.index,
}

FRIENDLY_ENCODING: dict[str, Encoding] = {
    '/CCITTFaxDecode': Encoding.ccitt,
    '/DCTDecode': Encoding.jpeg,
    '/JPXDecode': Encoding.jpeg2000,
    '/JBIG2Decode': Encoding.jbig2,
    '/CCF': Encoding.ccitt,                                            
    '/DCT': Encoding.jpeg,
    '/AHx': Encoding.asciihex,
    '/A85': Encoding.ascii85,
    '/LZW': Encoding.lzw,
    '/Fl': Encoding.flate,
    '/RL': Encoding.runlength,
}

FRIENDLY_COMP: dict[Colorspace, int] = {
    Colorspace.gray: 1,
    Colorspace.rgb: 3,
    Colorspace.cmyk: 4,
    Colorspace.lab: 3,
    Colorspace.index: 1,
}


UNIT_SQUARE = (1.0, 0.0, 0.0, 1.0, 0.0, 0.0)


def _is_unit_square(shorthand):
    values = map(float, shorthand)
    pairwise = zip(values, UNIT_SQUARE)
    return all(isclose(a, b, rel_tol=1e-3) for a, b in pairwise)


class XobjectSettings(NamedTuple):
                                               

    name: str
    shorthand: tuple[float, float, float, float, float, float]
    stack_depth: int


class InlineSettings(NamedTuple):
                                                    

    iimage: PdfInlineImage
    shorthand: tuple[float, float, float, float, float, float]
    stack_depth: int


class ContentsInfo(NamedTuple):
                                                    

    xobject_settings: list[XobjectSettings]
    inline_images: list[InlineSettings]
    found_vector: bool
    found_text: bool
    name_index: Mapping[str, list[XobjectSettings]]


class TextboxInfo(NamedTuple):
                                               

    bbox: tuple[float, float, float, float]
    is_visible: bool
    is_corrupt: bool


class VectorMarker:
                                                                             


class TextMarker:
                                                                           


def _normalize_stack(graphobjs):
                                                                  
    for operands, operator in graphobjs:
        operator = str(operator)
        if re.match(r'Q*q+$', operator):                                 
            for char in operator:                         
                yield ([], char)                    
        else:
            yield (operands, operator)


def _interpret_contents(contentstream: Object, initial_shorthand=UNIT_SQUARE):
           
    stack = []
    ctm = Matrix(initial_shorthand)
    xobject_settings: list[XobjectSettings] = []
    inline_images: list[InlineSettings] = []
    name_index = defaultdict(lambda: [])
    found_vector = False
    found_text = False
    vector_ops = set('S s f F f* B B* b b*'.split())
    text_showing_ops = set("""TJ Tj " '""".split())
    image_ops = set('BI ID EI q Q Do cm'.split())
    operator_whitelist = ' '.join(vector_ops | text_showing_ops | image_ops)

    for n, graphobj in enumerate(
        _normalize_stack(parse_content_stream(contentstream, operator_whitelist))
    ):
        operands, operator = graphobj
        if operator == 'q':
            stack.append(ctm)
            if len(stack) > 32:                 
                if len(stack) > 128:
                    raise RuntimeError(
                        f"PDF graphics stack overflowed hard limit at operator {n}"
                    )
                warn("PDF graphics stack overflowed spec limit")
        elif operator == 'Q':
            try:
                ctm = stack.pop()
            except IndexError:
                                                                              
                                                                               
                warn("PDF graphics stack underflowed - PDF may be malformed")
        elif operator == 'cm':
            try:
                ctm = Matrix(operands) @ ctm
            except ValueError:
                raise InputFileError(
                    "PDF content stream is corrupt - this PDF is malformed. "
                    "Use a PDF editor that is capable of visually inspecting the PDF."
                )
        elif operator == 'Do':
            image_name = operands[0]
            settings = XobjectSettings(
                name=image_name, shorthand=ctm.shorthand, stack_depth=len(stack)
            )
            xobject_settings.append(settings)
            name_index[str(image_name)].append(settings)
        elif operator == 'INLINE IMAGE':                                  
            iimage = operands[0]
            inline = InlineSettings(
                iimage=iimage, shorthand=ctm.shorthand, stack_depth=len(stack)
            )
            inline_images.append(inline)
        elif operator in vector_ops:
            found_vector = True
        elif operator in text_showing_ops:
            found_text = True

    return ContentsInfo(
        xobject_settings=xobject_settings,
        inline_images=inline_images,
        found_vector=found_vector,
        found_text=found_text,
        name_index=name_index,
    )


def _get_dpi(ctm_shorthand, image_size) -> Resolution:
           
    a, b, c, d, _, _ = ctm_shorthand                                

                                                              
    image_drawn = hypot(a, b), hypot(c, d)

    def calc(drawn, pixels, inches_per_pt=72.0):
                                                                                 
        scale = pixels / drawn if drawn != 0 else inf
        dpi = scale * inches_per_pt
        return dpi

    dpi_w, dpi_h = (calc(image_drawn[n], image_size[n]) for n in range(2))
    return Resolution(dpi_w, dpi_h)


class ImageInfo:
           

    DPI_PREC = Decimal('1.000')

    _comp: int | None
    _name: str

    def __init__(
        self,
        *,
        name='',
        pdfimage: Object | None = None,
        inline: PdfInlineImage | None = None,
        shorthand=None,
    ):
                                      
        self._name = str(name)
        self._shorthand = shorthand

        pim: PdfInlineImage | PdfImage

        if inline is not None:
            self._origin = 'inline'
            pim = inline
        elif pdfimage is not None and isinstance(pdfimage, Stream):
            self._origin = 'xobject'
            pim = PdfImage(pdfimage)
        else:
            raise ValueError("Either pdfimage or inline must be set")

        self._width = pim.width
        self._height = pim.height
        if (smask := pim.obj.get(Name.SMask, None)) is not None:
                                                                             
                                                                     
                                                                             
                                                                           
                                                
            if isinstance(smask, Stream | Dictionary):
                self._width = max(smask.get(Name.Width, 0), self._width)
                self._height = max(smask.get(Name.Height, 0), self._height)
        if (mask := pim.obj.get(Name.Mask, None)) is not None:
                                                                      
                                                                  
                                                                         
                      
            if isinstance(mask, Stream | Dictionary):
                self._width = max(mask.get(Name.Width, 0), self._width)
                self._height = max(mask.get(Name.Height, 0), self._height)

                                                                  
                                                                           
                                                                         
        if pim.image_mask:
            self._type = 'stencil'
        else:
            self._type = 'image'

        self._bpc = int(pim.bits_per_component)
        try:
            self._enc = FRIENDLY_ENCODING.get(pim.filters[0])
        except IndexError:
            self._enc = None

        try:
            self._color = FRIENDLY_COLORSPACE.get(pim.colorspace or '')
        except NotImplementedError:
            self._color = None
        if self._enc == Encoding.jpeg2000:
            self._color = Colorspace.jpeg2000

        self._comp = None
        if self._color == Colorspace.icc and isinstance(pim, PdfImage):
            self._comp = self._init_icc(pim)
        else:
            if isinstance(self._color, Colorspace):
                self._comp = FRIENDLY_COMP.get(self._color)
                                                                              
                                                    
            if self._comp is None and self._enc in (Encoding.ccitt, Encoding.jbig2):
                self._comp = FRIENDLY_COMP[Colorspace.gray]

    def _init_icc(self, pim: PdfImage):
        try:
            icc = pim.icc
        except UnsupportedImageTypeError as e:
            logger.warning(
                f"An image with a corrupt or unreadable ICC profile was found. "
                f"Output PDF may not match the input PDF visually: {e}. {self}"
            )
            return None
                                                              
        if icc is None or not hasattr(icc, 'profile'):
            logger.warning(
                f"An image with an ICC profile but no ICC profile data was found. "
                f"The output PDF may not match the input PDF visually. {self}"
            )
            return None
        try:
            if icc.profile.xcolor_space == 'GRAY':
                return 1
            elif icc.profile.xcolor_space == 'CMYK':
                return 4
            else:
                return 3
        except AttributeError:
            return None

    @property
    def name(self):
                                                         
        return self._name

    @property
    def type_(self):
                                                         
        return self._type

    @property
    def width(self) -> int:
                                           
        return self._width

    @property
    def height(self) -> int:
                                            
        return self._height

    @property
    def bpc(self):
                                 
        return self._bpc

    @property
    def color(self):
                                      
        return self._color if self._color is not None else '?'

    @property
    def comp(self):
                                                         
        return self._comp if self._comp is not None else '?'

    @property
    def enc(self):
                                    
        return self._enc if self._enc is not None else 'image'

    @property
    def renderable(self) -> bool:
                   
        return (
            self.dpi.is_finite
            and self.width >= 0
            and self.height >= 0
            and self.type_ != 'stencil'
        )

    @property
    def dpi(self) -> Resolution:
                   
        return _get_dpi(self._shorthand, (self._width, self._height))

    @property
    def printed_area(self) -> float:
                                                          
        if not self.renderable:
            return 0.0
        return float((self.width / self.dpi.x) * (self.height / self.dpi.y))

    def __repr__(self):
                                                          
        return (
            f"<ImageInfo '{self.name}' {self.type_} {self.width}×{self.height} "
            f"{self.color} {self.comp} {self.bpc} {self.enc} {self.dpi}>"
        )


def _find_inline_images(contentsinfo: ContentsInfo) -> Iterator[ImageInfo]:
                                                  
    for n, inline in enumerate(contentsinfo.inline_images):
        yield ImageInfo(
            name=f'inline-{n:02d}', shorthand=inline.shorthand, inline=inline.iimage
        )


def _image_xobjects(container) -> Iterator[tuple[Object, str]]:
           
    if Name.Resources not in container:
        return
    resources = container[Name.Resources]
    if Name.XObject not in resources:
        return
    for key, candidate in resources[Name.XObject].items():
        if candidate is None or Name.Subtype not in candidate:
            continue
        if candidate[Name.Subtype] == Name.Image:
            pdfimage = candidate
            yield (pdfimage, key)


def _find_regular_images(
    container: Object, contentsinfo: ContentsInfo
) -> Iterator[ImageInfo]:
           
    for pdfimage, xobj in _image_xobjects(container):
        if xobj not in contentsinfo.name_index:
            continue
        for draw in contentsinfo.name_index[xobj]:
            if draw.stack_depth == 0 and _is_unit_square(draw.shorthand):
                                                                              
                                                                            
                                                                      
                                                                             
                                                              
                continue

            yield ImageInfo(name=draw.name, pdfimage=pdfimage, shorthand=draw.shorthand)


def _find_form_xobject_images(pdf: Pdf, container: Object, contentsinfo: ContentsInfo):
           
    if Name.Resources not in container:
        return
    resources = container[Name.Resources]
    if Name.XObject not in resources:
        return
    xobjs = resources[Name.XObject].as_dict()
    for xobj in xobjs:
        candidate = xobjs[xobj]
        if candidate is None or candidate.get(Name.Subtype) != Name.Form:
            continue

        form_xobject = candidate
        for settings in contentsinfo.xobject_settings:
            if settings.name != xobj:
                continue

                                                                        
                                                                          
                                                                            
                                             
            ctm_shorthand = settings.shorthand
            yield from _process_content_streams(
                pdf=pdf, container=form_xobject, shorthand=ctm_shorthand
            )


def _process_content_streams(
    *, pdf: Pdf, container: Object, shorthand=None
) -> Iterator[VectorMarker | TextMarker | ImageInfo]:
           
    if container.get(Name.Type) == Name.Page and Name.Contents in container:
        initial_shorthand = shorthand or UNIT_SQUARE
    elif (
        container.get(Name.Type) == Name.XObject
        and container[Name.Subtype] == Name.Form
    ):
                                                                    
                                                                       
        ctm = Matrix(shorthand) if shorthand else Matrix()

                                                                          
                                            
        form_shorthand = container.get(Name.Matrix, Matrix())
        form_matrix = Matrix(form_shorthand)

                                                                       
                                              
        ctm = form_matrix @ ctm
        initial_shorthand = ctm.shorthand
    else:
        return

    contentsinfo = _interpret_contents(container, initial_shorthand)

    if contentsinfo.found_vector:
        yield VectorMarker()
    if contentsinfo.found_text:
        yield TextMarker()
    yield from _find_inline_images(contentsinfo)
    yield from _find_regular_images(container, contentsinfo)
    yield from _find_form_xobject_images(pdf, container, contentsinfo)


def _page_has_text(text_blocks: Iterable[FloatRect], page_width, page_height) -> bool:
                                                              
    pw, ph = float(page_width), float(page_height)                                

    margin_ratio = 0.125
    interior_bbox = (
        margin_ratio * pw,        
        (1 - margin_ratio) * ph,       
        (1 - margin_ratio) * pw,         
        margin_ratio * ph,                                          
    )

    def rects_intersect(a: FloatRect, b: FloatRect) -> bool:
                   
        return a[0] < b[2] and a[2] > b[0] and a[1] > b[3] and a[3] < b[1]

    has_text = False
    for bbox in text_blocks:
        if rects_intersect(bbox, interior_bbox):
            has_text = True
            break
    return has_text


def simplify_textboxes(
    miner_page: LTPage, textbox_getter: Callable[[LTPage], Iterator[LTTextBox]]
) -> Iterator[TextboxInfo]:
           
    for box in textbox_getter(miner_page):
        first_line = box._objs[0]                                    
        first_char = first_line._objs[0]                                    
        if not isinstance(first_char, LTStateAwareChar):
            continue
        visible = first_char.rendermode != 3
        corrupt = first_char.get_text() == '\ufffd'
        yield TextboxInfo(box.bbox, visible, corrupt)


worker_pdf = None                                


def _pdf_pageinfo_sync_init(pdf: Pdf, infile: Path, pdfminer_loglevel):
    global worker_pdf                                                 
    pikepdf_enable_mmap()

    logging.getLogger('pdfminer').setLevel(pdfminer_loglevel)

                                                                         
    if pdf is None:
        worker_pdf = Pdf.open(infile)

        def on_process_close():
            worker_pdf.close()

                                       
        atexit.register(on_process_close)


@contextmanager
def _pdf_pageinfo_sync_pdf(thread_pdf: Pdf | None, infile: Path):
    if thread_pdf is not None:
        yield thread_pdf
    elif worker_pdf is not None:
        yield worker_pdf
    else:
        with Pdf.open(infile) as pdf:
            yield pdf


def _pdf_pageinfo_sync(
    pageno: int,
    thread_pdf: Pdf | None,
    infile: Path,
    check_pages: Container[int],
    detailed_analysis: bool,
    miner_state: PdfMinerState | None,
) -> PageInfo:
    with _pdf_pageinfo_sync_pdf(thread_pdf, infile) as pdf:
        return PageInfo(
            pdf, pageno, infile, check_pages, detailed_analysis, miner_state
        )


def _pdf_pageinfo_concurrent(
    pdf,
    executor: Executor,
    max_workers: int,
    use_threads: bool,
    infile,
    progbar,
    check_pages,
    detailed_analysis: bool = False,
    miner_state: PdfMinerState | None = None,
) -> Sequence[PageInfo | None]:
    pages: list[PageInfo | None] = [None] * len(pdf.pages)

    def update_pageinfo(page: PageInfo, pbar: ProgressBar):
        if not page:
            raise InputFileError("Could read a page in the PDF")
        pages[page.pageno] = page
        pbar.update()

    if max_workers is None:
        max_workers = available_cpu_count()

    total = len(pdf.pages)

    n_workers = min(1 + len(pages) // 4, max_workers)
    if n_workers == 1:
                                                                      
                             
        use_threads = True

    if use_threads and n_workers > 1:
                                                                           
                                                            
        n_workers = 1

                                                                          
                                                                                   
         
    initial_pdf = pdf if use_threads else None

    contexts = (
        (n, initial_pdf, infile, check_pages, detailed_analysis, miner_state)
        for n in range(total)
    )
    assert n_workers == 1 if use_threads else n_workers >= 1, "Not multithreadable"
    logger.debug(
        f"Gathering info with {n_workers} "
        + ('thread' if use_threads else 'process')
        + " workers"
    )
    executor(
        use_threads=use_threads,
        max_workers=n_workers,
        progress_kwargs=dict(
            total=total, desc="Scanning contents", unit='page', disable=not progbar
        ),
        worker_initializer=partial(
            _pdf_pageinfo_sync_init,
            initial_pdf,
            infile,
            logging.getLogger('pdfminer').level,
        ),
        task=_pdf_pageinfo_sync,
        task_arguments=contexts,
        task_finished=update_pageinfo,
    )
    return pages


class PageResolutionProfile(NamedTuple):
                                                      

    weighted_dpi: float
    """The weighted average DPI of the page, weighted by the area of each image."""

    max_dpi: float
    """The maximum DPI of an image on the page."""

    average_to_max_dpi_ratio: float
    """The average DPI of the page divided by the maximum DPI of the page.

    This indicates the intensity of the resolution variation on the page.

    If the average is 1.0 or close to 1.0, has all of its content at a uniform
    resolution. If the average is much lower than 1.0, some content is at a
    higher resolution than the rest of the page.
    """

    area_ratio: float
    """The maximum-DPI area of the page divided by the total drawn area.

    This indicates the prevalence of high-resolution content on the page.
    """


class PageInfo:
                                                                   

    _has_text: bool | None
    _has_vector: bool | None
    _images: list[ImageInfo] = []

    def __init__(
        self,
        pdf: Pdf,
        pageno: int,
        infile: PathLike,
        check_pages: Container[int],
        detailed_analysis: bool = False,
        miner_state: PdfMinerState | None = None,
    ):
                                           
        self._pageno = pageno
        self._infile = infile
        self._detailed_analysis = detailed_analysis
        self._gather_pageinfo(
            pdf, pageno, infile, check_pages, detailed_analysis, miner_state
        )

    def _gather_pageinfo(
        self,
        pdf: Pdf,
        pageno: int,
        infile: PathLike,
        check_pages: Container[int],
        detailed_analysis: bool,
        miner_state: PdfMinerState | None,
    ):
        page: Page = pdf.pages[pageno]
        mediabox = [Decimal(d) for d in page.mediabox.as_list()]
        width_pt = mediabox[2] - mediabox[0]
        height_pt = mediabox[3] - mediabox[1]

                                                                  
                                                                      
        self._cropbox = [float(d) for d in page.cropbox.as_list()]
        self._mediabox = [float(d) for d in page.mediabox.as_list()]
        self._trimbox = [float(d) for d in page.trimbox.as_list()]

        check_this_page = pageno in check_pages

        if check_this_page and detailed_analysis:
            page_analysis = miner_state.get_page_analysis(pageno)
            if page_analysis is not None:
                self._textboxes = list(
                    simplify_textboxes(page_analysis, get_text_boxes)
                )
            else:
                self._textboxes = []
            bboxes = (box.bbox for box in self._textboxes)

            self._has_text = _page_has_text(bboxes, width_pt, height_pt)
        else:
            self._textboxes = []
            self._has_text = None                         

        userunit = page.get(Name.UserUnit, Decimal(1.0))
        if not isinstance(userunit, Decimal):
            userunit = Decimal(userunit)
        self._userunit = userunit
        self._width_inches = width_pt * userunit / Decimal(72.0)
        self._height_inches = height_pt * userunit / Decimal(72.0)
        self._rotate = int(getattr(page.obj, 'Rotate', 0))

        userunit_shorthand = (userunit, 0, 0, userunit, 0, 0)

        if check_this_page:
            self._has_vector = False
            self._has_text = False
            self._images = []
            for info in _process_content_streams(
                pdf=pdf, container=page, shorthand=userunit_shorthand
            ):
                if isinstance(info, VectorMarker):
                    self._has_vector = True
                elif isinstance(info, TextMarker):
                    self._has_text = True
                elif isinstance(info, ImageInfo):
                    self._images.append(info)
                else:
                    raise NotImplementedError()
        else:
            self._has_vector = None                         
            self._has_text = None
            self._images = []

        self._dpi = None
        if self._images:
            dpi = Resolution(0.0, 0.0).take_max(
                image.dpi for image in self._images if image.renderable
            )
            self._dpi = dpi
            self._width_pixels = int(round(dpi.x * float(self._width_inches)))
            self._height_pixels = int(round(dpi.y * float(self._height_inches)))

    @property
    def pageno(self) -> int:
                                           
        return self._pageno

    @property
    def has_text(self) -> bool:
                                                                    
        return bool(self._has_text)

    @property
    def has_corrupt_text(self) -> bool:
                                                                            
        if not self._detailed_analysis:
            raise NotImplementedError('Did not do detailed analysis')
        return any(tbox.is_corrupt for tbox in self._textboxes)

    @property
    def has_vector(self) -> bool:
                   
        return bool(self._has_vector)

    @property
    def width_inches(self) -> Decimal:
                                             
        return self._width_inches

    @property
    def height_inches(self) -> Decimal:
                                              
        return self._height_inches

    @property
    def width_pixels(self) -> int:
                                             
        return int(round(float(self.width_inches) * self.dpi.x))

    @property
    def height_pixels(self) -> int:
                                              
        return int(round(float(self.height_inches) * self.dpi.y))

    @property
    def rotation(self) -> int:
                   
        return self._rotate

    @rotation.setter
    def rotation(self, value):
        if value in (0, 90, 180, 270, 360, -90, -180, -270):
            self._rotate = value
        else:
            raise ValueError("rotation must be a cardinal angle")

    @property
    def cropbox(self) -> FloatRect:
                                                        
        return self._cropbox

    @property
    def mediabox(self) -> FloatRect:
                                                         
        return self._mediabox

    @property
    def trimbox(self) -> FloatRect:
                                                        
        return self._trimbox

    @property
    def images(self) -> list[ImageInfo]:
                            
        return self._images

    def get_textareas(self, visible: bool | None = None, corrupt: bool | None = None):
                                                                             

        def predicate(
            obj: TextboxInfo, want_visible: bool | None, want_corrupt: bool | None
        ) -> bool:
            result = True
            if want_visible is not None:
                if obj.is_visible != want_visible:
                    result = False
            if want_corrupt is not None:
                if obj.is_corrupt != want_corrupt:
                    result = False
            return result

        if not self._textboxes:
            if visible is not None and corrupt is not None:
                raise NotImplementedError('Incomplete information on textboxes')
            return self._textboxes

        return (obj.bbox for obj in self._textboxes if predicate(obj, visible, corrupt))

    @property
    def dpi(self) -> Resolution:
                                                                 
        if self._dpi is None:
            return Resolution(0.0, 0.0)
        return self._dpi

    @property
    def userunit(self) -> Decimal:
                                       
        return self._userunit

    @property
    def min_version(self) -> str:
                                                                    
        if self.userunit is not None:
            return '1.6'
        else:
            return '1.5'

    def page_dpi_profile(self) -> PageResolutionProfile | None:
                   
        image_dpis = []
        image_areas = []
        for image in self._images:
            if not image.renderable:
                continue
            image_dpis.append(image.dpi.to_scalar())
            image_areas.append(image.printed_area)

        total_drawn_area = sum(image_areas)
        if total_drawn_area == 0:
            return None

        weights = [area / total_drawn_area for area in image_areas]
                                                          
        weighted_dpi = statistics.harmonic_mean(image_dpis, weights)
        max_dpi = max(image_dpis)
        dpi_average_max_ratio = weighted_dpi / max_dpi

        arg_max_dpi = image_dpis.index(max_dpi)
        max_area_ratio = image_areas[arg_max_dpi] / total_drawn_area
        return PageResolutionProfile(
            weighted_dpi,
            max_dpi,
            dpi_average_max_ratio,
            max_area_ratio,
        )

    def __repr__(self):
                                           
        return (
            f'<PageInfo '
            f'pageno={self.pageno} {self.width_inches}"x{self.height_inches}" '
            f'rotation={self.rotation} dpi={self.dpi} has_text={self.has_text}>'
        )


DEFAULT_EXECUTOR = SerialExecutor()


class PdfInfo:
           

    _has_acroform: bool = False
    _has_signature: bool = False
    _needs_rendering: bool = False

    def __init__(
        self,
        infile: Path,
        *,
        detailed_analysis: bool = False,
        progbar: bool = False,
        max_workers: int | None = None,
        use_threads: bool = True,
        check_pages=None,
        executor: Executor = DEFAULT_EXECUTOR,
    ):
                         
        self._infile = infile
        if check_pages is None:
            check_pages = range(0, 1_000_000_000)

        with Pdf.open(infile) as pdf:
            if pdf.is_encrypted:
                raise EncryptedPdfError()                                             
            pscript5_mode = str(pdf.docinfo.get(Name.Creator, "")).startswith(
                'PScript5'
            )
            self._miner_state = (
                PdfMinerState(infile, pscript5_mode)
                if detailed_analysis
                else nullcontext()
            )
            with self._miner_state as miner_state:
                self._pages = _pdf_pageinfo_concurrent(
                    pdf,
                    executor,
                    max_workers,
                    use_threads,
                    infile,
                    progbar,
                    check_pages=check_pages,
                    detailed_analysis=detailed_analysis,
                    miner_state=miner_state,
                )
            self._needs_rendering = pdf.Root.get(Name.NeedsRendering, False)
            if Name.AcroForm in pdf.Root:
                if len(pdf.Root.AcroForm.get(Name.Fields, [])) > 0:
                    self._has_acroform = True
                elif Name.XFA in pdf.Root.AcroForm:
                    self._has_acroform = True
                self._has_signature = bool(pdf.Root.AcroForm.get(Name.SigFlags, 0) & 1)
            self._is_tagged = bool(
                pdf.Root.get(Name.MarkInfo, {}).get(Name.Marked, False)
            )

    @property
    def pages(self) -> Sequence[PageInfo | None]:
                                                                       
        return self._pages

    @property
    def min_version(self) -> str:
                                                                   
                                                                               
        return max(page.min_version for page in self.pages if page)

    @property
    def has_userunit(self) -> bool:
                                                      
        return any(page.userunit != 1.0 for page in self.pages if page)

    @property
    def has_acroform(self) -> bool:
                                                                  
        return self._has_acroform

    @property
    def has_signature(self) -> bool:
                                                                              
        return self._has_signature

    @property
    def is_tagged(self) -> bool:
                                                                                 
        return self._is_tagged

    @property
    def filename(self) -> str | Path:
                                     
        if not isinstance(self._infile, str | Path):
            raise NotImplementedError("can't get filename from stream")
        return self._infile

    @property
    def needs_rendering(self) -> bool:
                   
        return self._needs_rendering

    def __getitem__(self, item) -> PageInfo:
                                                            
        return self._pages[item]

    def __len__(self):
                                            
        return len(self._pages)

    def __repr__(self):
                                           
        return f"<PdfInfo('...'), page count={len(self)}>"


def main():                    
                          
    import argparse                                           
    from pprint import pprint                                           

    parser = argparse.ArgumentParser()
    parser.add_argument('infile')
    args = parser.parse_args()
    pdfinfo = PdfInfo(args.infile)

    pprint(pdfinfo)
    for page in pdfinfo.pages:
        pprint(page)
        for im in page.images:
            pprint(im)


if __name__ == '__main__':
    main()
