                                              
                                  

from __future__ import annotations

from math import isclose

import pytest
from PIL import Image

from ocrmypdf._exec import ghostscript, tesseract
from ocrmypdf.exceptions import ExitCode
from ocrmypdf.helpers import Resolution
from ocrmypdf.pdfinfo import PdfInfo

from .conftest import check_ocrmypdf, have_unpaper, run_ocrmypdf

RENDERERS = ['hocr', 'sandwich']


def test_deskew(resources, outdir):
                     
    deskewed_pdf = check_ocrmypdf(resources / 'skew.pdf', outdir / 'skew.pdf', '-d')

                                     
    deskewed_png = outdir / 'deskewed.png'

    ghostscript.rasterize_pdf(
        deskewed_pdf,
        deskewed_png,
        raster_device='pngmono',
        raster_dpi=Resolution(150, 150),
        pageno=1,
    )

                                                                               
    skew_angle = tesseract.get_deskew(deskewed_png, [], None, 5.0)
    print(skew_angle)
    assert -0.5 < skew_angle < 0.5, "Deskewing failed"


def test_deskew_blank_page(resources, outpdf):
                                                                       
    check_ocrmypdf(resources / 'blank.pdf', outpdf, '--deskew')


@pytest.mark.xfail(reason="remove background disabled")
def test_remove_background(resources, outdir):
                                                              
    with Image.open(resources / 'baiona_color.jpg') as im:
        assert im.getextrema() != ((0, 255), (0, 255), (0, 255))

    output_pdf = check_ocrmypdf(
        resources / 'baiona_color.jpg',
        outdir / 'test_remove_bg.pdf',
        '--remove-background',
        '--image-dpi',
        '150',
        '--plugin',
        'tests/plugins/tesseract_noop.py',
    )

    output_png = outdir / 'remove_bg.png'

    ghostscript.rasterize_pdf(
        output_pdf,
        output_png,
        raster_device='png16m',
        raster_dpi=Resolution(100, 100),
        pageno=1,
    )

                                                          
    with Image.open(output_png) as im:
        assert im.getextrema() == ((0, 255), (0, 255), (0, 255))


                                         
@pytest.mark.parametrize(
    "pdf", ['palette.pdf', 'cmyk.pdf', 'ccitt.pdf', 'jbig2.pdf', 'lichtenstein.pdf']
)
@pytest.mark.parametrize("renderer", ['sandwich', 'hocr'])
@pytest.mark.parametrize("output_type", ['pdf', 'pdfa'])
def test_exotic_image(pdf, renderer, output_type, resources, outdir):
    outfile = outdir / f'test_{pdf}_{renderer}.pdf'
    check_ocrmypdf(
        resources / pdf,
        outfile,
        '-dc' if have_unpaper() else '-d',
        '-v',
        '1',
        '--output-type',
        output_type,
        '--sidecar',
        '--skip-text',
        '--pdf-renderer',
        renderer,
        '--plugin',
        'tests/plugins/tesseract_cache.py',
    )

    assert outfile.with_suffix('.pdf.txt').exists()


@pytest.mark.parametrize('renderer', RENDERERS)
def test_non_square_resolution(renderer, resources, outpdf):
                                                  
    in_pageinfo = PdfInfo(resources / 'aspect.pdf')
    assert in_pageinfo[0].dpi.x != in_pageinfo[0].dpi.y

    proc = run_ocrmypdf(
        resources / 'aspect.pdf',
        outpdf,
        '--pdf-renderer',
        renderer,
        '--plugin',
        'tests/plugins/tesseract_cache.py',
    )
                                                                                   
                            
    if proc.returncode != ExitCode.pdfa_conversion_failed:
        proc.check_returncode()

    out_pageinfo = PdfInfo(outpdf)

                                          
    assert in_pageinfo[0].dpi == out_pageinfo[0].dpi


@pytest.mark.parametrize('renderer', RENDERERS)
def test_convert_to_square_resolution(renderer, resources, outpdf):
                                                  
    in_pageinfo = PdfInfo(resources / 'aspect.pdf')
    assert in_pageinfo[0].dpi.x != in_pageinfo[0].dpi.y

                                                                       
    check_ocrmypdf(
        resources / 'aspect.pdf',
        outpdf,
        '--force-ocr',
        '--pdf-renderer',
        renderer,
        '--plugin',
        'tests/plugins/tesseract_cache.py',
    )

    out_pageinfo = PdfInfo(outpdf)

    in_p0, out_p0 = in_pageinfo[0], out_pageinfo[0]

                                  
    assert out_p0.dpi.x == out_p0.dpi.y

                                            
    assert isclose(in_p0.width_inches, out_p0.width_inches)
    assert isclose(in_p0.height_inches, out_p0.height_inches)

                                                                             
                     
    out_im_w = out_p0.images[0].width / out_p0.images[0].dpi.x
    out_im_h = out_p0.images[0].height / out_p0.images[0].dpi.y
    assert isclose(out_p0.width_inches, out_im_w)
    assert isclose(out_p0.height_inches, out_im_h)
