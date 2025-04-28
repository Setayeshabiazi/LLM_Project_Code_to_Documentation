                                              
                                  
"""Detailed text position and layout analysis, building on pdfminer.six."""

from __future__ import annotations

import re
from collections.abc import Iterator, Mapping
from contextlib import contextmanager
from math import copysign
from os import PathLike
from pathlib import Path
from typing import Any
from unittest.mock import patch

import pdfminer
import pdfminer.encodingdb
import pdfminer.pdfdevice
import pdfminer.pdfinterp
import pdfminer.psparser
from deprecation import deprecated
from pdfminer.converter import PDFLayoutAnalyzer
from pdfminer.layout import LAParams, LTChar, LTPage, LTTextBox
from pdfminer.pdfcolor import PDFColorSpace
from pdfminer.pdfdevice import PDFTextSeq
from pdfminer.pdfdocument import PDFTextExtractionNotAllowed
from pdfminer.pdffont import FontWidthDict, PDFFont, PDFSimpleFont, PDFUnicodeNotDefined
from pdfminer.pdfinterp import PDFGraphicState, PDFResourceManager, PDFTextState
from pdfminer.pdfpage import PDFPage
from pdfminer.utils import Matrix, bbox2str, matrix2str

from ocrmypdf.exceptions import EncryptedPdfError, InputFileError

STRIP_NAME = re.compile(r'[0-9]+')


original_pdfsimplefont_init = PDFSimpleFont.__init__


def pdfsimplefont__init__(
    self,
    descriptor: Mapping[str, Any],
    widths: FontWidthDict,
    spec: Mapping[str, Any],
) -> None:
           
                                                    
                                                      
                      
    original_pdfsimplefont_init(self, descriptor, widths, spec)
    if not self.unicode_map and 'Encoding' not in spec:
        self.cid2unicode = {}
    return


setattr(PDFSimpleFont, '__init__', pdfsimplefont__init__)

                                
                                                                                   
                                                                                  
pdfminer.psparser.PSBaseParser.BUFSIZ = 256 * 1024 * 1024


def pdftype3font__pscript5_get_height(self):
           
    h = self.bbox[3] - self.bbox[1]
    if h == 0:
        h = self.ascent - self.descent
    return h * copysign(1.0, self.vscale)


def pdftype3font__pscript5_get_descent(self):
           
    return self.descent * copysign(1.0, self.vscale)


def pdftype3font__pscript5_get_ascent(self):
           
    return self.ascent * copysign(1.0, self.vscale)


def _is_undefined_char(s: str) -> bool:
                                                      
    return s.startswith('(cid:') and s.endswith(')')


class LTStateAwareChar(LTChar):
                                                                               

    __slots__ = (
        'rendermode',
        '_text',
        'matrix',
        'fontname',
        'adv',
        'upright',
        'size',
        'width',
        'height',
        'bbox',
        'x0',
        'x1',
        'y0',
        'y1',
    )

    def __init__(
        self,
        matrix: Matrix,
        font: PDFFont,
        fontsize: float,
        scaling: float,
        rise: float,
        text: str,
        textwidth: float,
        textdisp: float | tuple[float | None, float],
        ncs: PDFColorSpace,
        graphicstate: PDFGraphicState,
        textstate: PDFTextState,
    ) -> None:
                         
        super().__init__(
            matrix,
            font,
            fontsize,
            scaling,
            rise,
            text,
            textwidth,
            textdisp,
            ncs,
            graphicstate,
        )
        self.rendermode = textstate.render

    def is_compatible(self, obj: object) -> bool:
                   
                                          
        if not isinstance(obj, LTStateAwareChar):
            return False
        both_unicode_mapped = not _is_undefined_char(
            self._text
        ) and not _is_undefined_char(obj._text)
        if both_unicode_mapped:
            return self.rendermode == obj.rendermode
        return self.fontname == obj.fontname and self.rendermode == obj.rendermode

    def get_text(self) -> str:
                                           
        if _is_undefined_char(self._text):
            return '\ufffd'                             
        return self._text

    def __repr__(self) -> str:
                                                            
        return (
            f"<{self.__class__.__name__} "
            f"{bbox2str(self.bbox)} "
            f"matrix={matrix2str(self.matrix)} "
            f"rendermode={self.rendermode!r} "
            f"font={self.fontname!r} "
            f"adv={self.adv} "
            f"text={self.get_text()!r}>"
        )


class TextPositionTracker(PDFLayoutAnalyzer):
                                                                        

    textstate: PDFTextState

    def __init__(
        self,
        rsrcmgr: PDFResourceManager,
        pageno: int = 1,
        laparams: LAParams | None = None,
    ):
                                             
        super().__init__(rsrcmgr, pageno, laparams)
        self.result: LTPage | None = None

    def begin_page(self, page: PDFPage, ctm: Matrix) -> None:
                                         
        super().begin_page(page, ctm)
        self.cur_item = LTPage(self.pageno, page.mediabox)

    def end_page(self, page: PDFPage) -> None:
                                       
        assert not self._stack, str(len(self._stack))
        assert isinstance(self.cur_item, LTPage), str(type(self.cur_item))
        if self.laparams is not None:
            self.cur_item.analyze(self.laparams)
        self.pageno += 1
        self.receive_layout(self.cur_item)

    def render_string(
        self,
        textstate: PDFTextState,
        seq: PDFTextSeq,
        ncs: PDFColorSpace,
        graphicstate: PDFGraphicState,
    ) -> None:
                                                                    
        self.textstate = textstate.copy()
        super().render_string(self.textstate, seq, ncs, graphicstate)

    def render_char(
        self,
        matrix: Matrix,
        font: PDFFont,
        fontsize: float,
        scaling: float,
        rise: float,
        cid: int,
        ncs: PDFColorSpace,
        graphicstate: PDFGraphicState,
    ) -> float:
                                                                  
        try:
            text = font.to_unichr(cid)
            assert isinstance(text, str), str(type(text))
        except PDFUnicodeNotDefined:
            text = self.handle_undefined_char(font, cid)
        textwidth = font.char_width(cid)
        textdisp = font.char_disp(cid)
        item = LTStateAwareChar(
            matrix,
            font,
            fontsize,
            scaling,
            rise,
            text,
            textwidth,
            textdisp,
            ncs,
            graphicstate,
            self.textstate,
        )
        self.cur_item.add(item)
        return item.adv

    def receive_layout(self, ltpage: LTPage) -> None:
                                     
        self.result = ltpage

    def get_result(self) -> LTPage | None:
                                             
        return self.result


@contextmanager
def patch_pdfminer(pscript5_mode: bool):
                                                                             
    if pscript5_mode:
        with patch.multiple(
            'pdfminer.pdffont.PDFType3Font',
            spec=True,
            get_ascent=pdftype3font__pscript5_get_ascent,
            get_descent=pdftype3font__pscript5_get_descent,
            get_height=pdftype3font__pscript5_get_height,
        ):
            yield
    else:
        yield


@deprecated(deprecated_in='16.6.0', details='Use PdfMinerState instead.')
def get_page_analysis(
    infile: PathLike, pageno: int, pscript5_mode: bool
) -> LTPage | None:
                                                 
    rman = pdfminer.pdfinterp.PDFResourceManager(caching=True)
    disable_boxes_flow = None
    dev = TextPositionTracker(
        rman,
        laparams=LAParams(
            all_texts=True, detect_vertical=True, boxes_flow=disable_boxes_flow
        ),
    )
    interp = pdfminer.pdfinterp.PDFPageInterpreter(rman, dev)

    with patch_pdfminer(pscript5_mode):
        try:
            with Path(infile).open('rb') as f:
                page_iter = PDFPage.get_pages(f, pagenos=[pageno], maxpages=0)
                page = next(page_iter, None)
                if page is None:
                    raise InputFileError(
                        f"pdfminer could not process page {pageno} (counting from 0)."
                    )
                interp.process_page(page)
        except PDFTextExtractionNotAllowed as e:
            raise EncryptedPdfError() from e

    return dev.get_result()


class PdfMinerState:
           

    def __init__(self, infile: Path, pscript5_mode: bool) -> None:
                   
        self.infile = infile
        self.rman = pdfminer.pdfinterp.PDFResourceManager(caching=True)
        self.disable_boxes_flow = None
        self.page_iter = None
        self.page_cache: list[PDFPage] = []
        self.pscript5_mode = pscript5_mode
        self.file = None

    def __enter__(self):
                                        
        self.file = Path(self.infile).open('rb')
        self.page_iter = PDFPage.get_pages(self.file)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
                                       
        if self.file:
            self.file.close()
        return True

    def get_page_analysis(self, pageno: int):
                                                     
        while len(self.page_cache) <= pageno:
            try:
                self.page_cache.append(next(self.page_iter))
            except StopIteration:
                raise InputFileError(
                    f"pdfminer did not find page {pageno} in the input file."
                )
        page = self.page_cache[pageno]
        if not page:
            raise InputFileError(
                f"pdfminer could not process page {pageno} (counting from 0)."
            )
        dev = TextPositionTracker(
            self.rman,
            laparams=LAParams(
                all_texts=True, detect_vertical=True, boxes_flow=self.disable_boxes_flow
            ),
        )
        interp = pdfminer.pdfinterp.PDFPageInterpreter(self.rman, dev)

        with patch_pdfminer(self.pscript5_mode):
            interp.process_page(page)

        return dev.get_result()


def get_text_boxes(obj) -> Iterator[LTTextBox]:
                                                          
    for child in obj:
        if isinstance(child, (LTTextBox)):
            yield child
        else:
            try:
                yield from get_text_boxes(child)
            except TypeError:
                continue
