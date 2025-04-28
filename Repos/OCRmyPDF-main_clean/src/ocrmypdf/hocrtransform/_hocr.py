                                               
                                                      
                                              
                                             
                              

"""hOCR transform implementation."""

from __future__ import annotations

import logging
import os
import re
import unicodedata
from dataclasses import dataclass
from itertools import pairwise
from math import atan, pi
from pathlib import Path
from xml.etree import ElementTree

from pikepdf import Matrix, Name, Rectangle
from pikepdf.canvas import (
    BLACK,
    BLUE,
    CYAN,
    DARKGREEN,
    GREEN,
    MAGENTA,
    RED,
    Canvas,
    Text,
    TextDirection,
)

from ocrmypdf.hocrtransform._font import EncodableFont as Font
from ocrmypdf.hocrtransform._font import GlyphlessFont

log = logging.getLogger(__name__)

INCH = 72.0

Element = ElementTree.Element


@dataclass
class DebugRenderOptions:
                                                 

    render_paragraph_bbox: bool = False
    render_baseline: bool = False
    render_triangle: bool = False
    render_line_bbox: bool = False
    render_word_bbox: bool = False
    render_space_bbox: bool = False


class HocrTransformError(Exception):
                                              


class HocrTransform:
           

    box_pattern = re.compile(
        r'''
        bbox \s+
        (\d+) \s+   # left: uint
        (\d+) \s+   # top: uint
        (\d+) \s+   # right: uint
        (\d+)       # bottom: uint
        ''',
        re.VERBOSE,
    )
    baseline_pattern = re.compile(
        r'''
        baseline \s+
        ([\-\+]?\d*\.?\d*) \s+  # +/- decimal float
        ([\-\+]?\d+)            # +/- int
        ''',
        re.VERBOSE,
    )
    textangle_pattern = re.compile(
        r'''
        textangle \s+
        ([\-\+]?\d*\.?\d*)  # +/- decimal float
        ''',
        re.VERBOSE,
    )

    def __init__(
        self,
        *,
        hocr_filename: str | Path,
        dpi: float,
        debug: bool = False,
        fontname: Name = Name("/f-0-0"),
        font: Font = GlyphlessFont(),
        debug_render_options: DebugRenderOptions | None = None,
    ):
                                                  
        if debug:
            log.warning("Use debug_render_options instead", DeprecationWarning)
            self.render_options = DebugRenderOptions(
                render_baseline=debug,
                render_triangle=debug,
                render_line_bbox=False,
                render_word_bbox=debug,
                render_paragraph_bbox=False,
                render_space_bbox=False,
            )
        else:
            self.render_options = debug_render_options or DebugRenderOptions()
        self.dpi = dpi
        self.hocr = ElementTree.parse(os.fspath(hocr_filename))
        self._fontname = fontname
        self._font = font

                                                                           
                       
        matches = re.match(r'({.*})html', self.hocr.getroot().tag)
        self.xmlns = ''
        if matches:
            self.xmlns = matches.group(1)

        for div in self.hocr.findall(self._child_xpath('div', 'ocr_page')):
            coords = self.element_coordinates(div)
            if not coords:
                raise HocrTransformError("hocr file is missing page dimensions")
            self.width = (coords.urx - coords.llx) / (self.dpi / INCH)
            self.height = (coords.ury - coords.lly) / (self.dpi / INCH)
                                                            
            break

    def _get_element_text(self, element: Element) -> str:
                                                                         
        text = element.text if element.text is not None else ''
        for child in element:
            text += self._get_element_text(child)
        text += element.tail if element.tail is not None else ''
        return text

    @classmethod
    def element_coordinates(cls, element: Element) -> Rectangle | None:
                                                                    
        matches = cls.box_pattern.search(element.attrib.get('title', ''))
        if not matches:
            return None
        return Rectangle(
            float(matches.group(1)),              
            float(matches.group(2)),             
            float(matches.group(3)),               
            float(matches.group(4)),                
        )

    @classmethod
    def baseline(cls, element: Element) -> tuple[float, float]:
                                                 
        matches = cls.baseline_pattern.search(element.attrib.get('title', ''))
        if not matches:
            return (0.0, 0.0)
        return float(matches.group(1)), int(matches.group(2))

    @classmethod
    def textangle(cls, element: Element) -> float:
                                           
        matches = cls.textangle_pattern.search(element.attrib.get('title', ''))
        if not matches:
            return 0.0
        return float(matches.group(1))

    def _child_xpath(self, html_tag: str, html_class: str | None = None) -> str:
        xpath = f".//{self.xmlns}{html_tag}"
        if html_class:
            xpath += f"[@class='{html_class}']"
        return xpath

    @classmethod
    def normalize_text(cls, s: str) -> str:
                                                                         
        return unicodedata.normalize("NFKC", s)

    def to_pdf(
        self,
        *,
        out_filename: Path,
        image_filename: Path | None = None,
        invisible_text: bool = True,
    ) -> None:
                   
                             
                                        
        canvas = Canvas(page_size=(self.width, self.height))
        canvas.add_font(self._fontname, self._font)
        page_matrix = (
            Matrix()
            .translated(0, self.height)
            .scaled(1, -1)
            .scaled(INCH / self.dpi, INCH / self.dpi)
        )
        log.debug(page_matrix)
        with canvas.do.save_state(cm=page_matrix):
            self._debug_draw_paragraph_boxes(canvas)
            found_lines = False
            for par in self.hocr.iterfind(self._child_xpath('p', 'ocr_par')):
                for line in (
                    element
                    for element in par.iterfind(self._child_xpath('span'))
                    if 'class' in element.attrib
                    and element.attrib['class']
                    in {'ocr_header', 'ocr_line', 'ocr_textfloat', 'ocr_caption'}
                ):
                    found_lines = True
                    direction = self._get_text_direction(par)
                    inject_word_breaks = self._get_inject_word_breaks(par)
                    self._do_line(
                        canvas,
                        line,
                        "ocrx_word",
                        invisible_text,
                        direction,
                        inject_word_breaks,
                    )

            if not found_lines:
                                                                 
                root = self.hocr.find(self._child_xpath('div', 'ocr_page'))
                direction = self._get_text_direction(root)
                self._do_line(
                    canvas,
                    root,
                    "ocrx_word",
                    invisible_text,
                    direction,
                    True,
                )
                                                            
        if image_filename is not None:
            canvas.do.draw_image(
                image_filename, 0, 0, width=self.width, height=self.height
            )

                                        
        canvas.to_pdf().save(out_filename)

    def _get_text_direction(self, par):
                   
        if par is None:
            return TextDirection.LTR
            
        return (
            TextDirection.RTL
            if par.attrib.get('dir', 'ltr') == 'rtl'
            else TextDirection.LTR
        )

    def _get_inject_word_breaks(self, par):
                   
        lang = par.attrib.get('lang', '')
        log.debug(lang)
        if lang in {'chi_sim', 'chi_tra', 'jpn', 'kor'}:
            return False
        return True

    @classmethod
    def polyval(cls, poly, x):                    
                                                             
        return x * poly[0] + poly[1]

    def _do_line(
        self,
        canvas: Canvas,
        line: Element | None,
        elemclass: str,
        invisible_text: bool,
        text_direction: TextDirection,
        inject_word_breaks: bool,
    ):
                   
        if line is None:
            return
                                                                                    
                                                                                 
                                                                              
                                                                                
                                                                                 
                                                                              
                                                     
        line_min_aabb = self.element_coordinates(line)
        if not line_min_aabb:
            return
        if line_min_aabb.ury <= line_min_aabb.lly:
            log.error(
                "line box is invalid so we cannot render it: box=%s text=%s",
                line_min_aabb,
                self._get_element_text(line),
            )
            return
        self._debug_draw_line_bbox(canvas, line_min_aabb)

                                                                             
                                                                            
                                                             
                                                                            
                                              
                                                                           
                                                                  
                                                    
        top_left_corner = (line_min_aabb.llx, line_min_aabb.lly)
        line_size_aabb_matrix = (
            Matrix()
            .translated(*top_left_corner)
                                                                                 
            .rotated(-self.textangle(line))
        )
        line_size_aabb = line_size_aabb_matrix.inverse().transform(line_min_aabb)

        slope, intercept = self.baseline(line)
        if abs(slope) < 0.005:
            slope = 0.0
        slope_angle = atan(slope)

                                                                             
                                                                              
                                                                                   
        baseline_matrix = (
            line_size_aabb_matrix
                                                                                  
                                   
                                                                                  
                                                                                  
            .translated(0, line_size_aabb.height)
            .translated(0, intercept)
            .rotated(slope_angle / pi * 180)
        )

        with canvas.do.save_state(cm=baseline_matrix):
            text = Text(direction=text_direction)
            fontsize = line_size_aabb.height + intercept
            text.font(self._fontname, fontsize)
            text.render_mode(3 if invisible_text else 0)

            self._debug_draw_baseline(
                canvas, baseline_matrix.inverse().transform(line_min_aabb), 0
            )

            canvas.do.fill_color(BLACK)                 
            elements = line.findall(self._child_xpath('span', elemclass))
            for elem, next_elem in pairwise(elements + [None]):
                self._do_line_word(
                    canvas,
                    baseline_matrix,
                    text,
                    fontsize,
                    elem,
                    next_elem,
                    text_direction,
                    inject_word_breaks,
                )
            canvas.do.draw_text(text)

    def _do_line_word(
        self,
        canvas: Canvas,
        line_matrix: Matrix,
        text: Text,
        fontsize: float,
        elem: Element | None,
        next_elem: Element | None,
        text_direction: TextDirection,
        inject_word_breaks: bool,
    ):
                                                
        if elem is None:
            return
        elemtxt = self.normalize_text(self._get_element_text(elem).strip())
        if elemtxt == '':
            return

        hocr_box = self.element_coordinates(elem)
        if hocr_box is None:
            return
        box = line_matrix.inverse().transform(hocr_box)
        font_width = self._font.text_width(elemtxt, fontsize)

                        
        self._debug_draw_word_triangle(canvas, box)
        self._debug_draw_word_bbox(canvas, box)

                                                                                      
        if text_direction == TextDirection.RTL:
            log.info("RTL: %s", elemtxt)
        if font_width > 0:
            if text_direction == TextDirection.LTR:
                text.text_transform(Matrix(1, 0, 0, -1, box.llx, 0))
            elif text_direction == TextDirection.RTL:
                text.text_transform(Matrix(-1, 0, 0, -1, box.llx + box.width, 0))
            text.horiz_scale(100 * box.width / font_width)
            text.show(self._font.text_encode(elemtxt))

                                                            
        hocr_next_box = (
            self.element_coordinates(next_elem) if next_elem is not None else None
        )
        if hocr_next_box is None:
            return
                                                                                      
                                                                             
                                                                     
                                          
        if not inject_word_breaks:
            return
        next_box = line_matrix.inverse().transform(hocr_next_box)
        if text_direction == TextDirection.LTR:
            space_box = Rectangle(box.urx, box.lly, next_box.llx, next_box.ury)
        elif text_direction == TextDirection.RTL:
            space_box = Rectangle(next_box.urx, box.lly, box.llx, next_box.ury)
        self._debug_draw_space_bbox(canvas, space_box)
        space_width = self._font.text_width(' ', fontsize)
        if space_width > 0 and space_box.width > 0:
            if text_direction == TextDirection.LTR:
                text.text_transform(Matrix(1, 0, 0, -1, space_box.llx, 0))
            elif text_direction == TextDirection.RTL:
                text.text_transform(
                    Matrix(-1, 0, 0, -1, space_box.llx + space_box.width, 0)
                )
            text.horiz_scale(100 * space_box.width / space_width)
            text.show(self._font.text_encode(' '))

    def _debug_draw_paragraph_boxes(self, canvas: Canvas, color=CYAN):
                                                           
        if not self.render_options.render_paragraph_bbox:                    
            return
        with canvas.do.save_state():
                                       
            canvas.do.stroke_color(color).line_width(0.1)
            for elem in self.hocr.iterfind(self._child_xpath('p', 'ocr_par')):
                elemtxt = self._get_element_text(elem).strip()
                if len(elemtxt) == 0:
                    continue
                ocr_par = self.element_coordinates(elem)
                if ocr_par is None:
                    continue
                canvas.do.rect(
                    ocr_par.llx, ocr_par.lly, ocr_par.width, ocr_par.height, fill=False
                )

    def _debug_draw_line_bbox(self, canvas: Canvas, line_box: Rectangle, color=BLUE):
                                                     
        if not self.render_options.render_line_bbox:                    
            return
        with canvas.do.save_state():
            canvas.do.stroke_color(color).line_width(0.15).rect(
                line_box.llx, line_box.lly, line_box.width, line_box.height, fill=False
            )

    def _debug_draw_word_triangle(
        self, canvas: Canvas, box: Rectangle, color=RED, line_width=0.1
    ):
                                                                               
        if not self.render_options.render_triangle:                    
            return
        with canvas.do.save_state():
            canvas.do.stroke_color(color).line_width(line_width).line(
                box.llx, box.lly, box.urx, box.lly
            ).line(box.urx, box.lly, box.llx, box.ury).line(
                box.llx, box.lly, box.llx, box.ury
            )

    def _debug_draw_word_bbox(
        self, canvas: Canvas, box: Rectangle, color=GREEN, line_width=0.1
    ):
                                              
        if not self.render_options.render_word_bbox:                    
            return
        with canvas.do.save_state():
            canvas.do.stroke_color(color).line_width(line_width).rect(
                box.llx, box.lly, box.width, box.height, fill=False
            )

    def _debug_draw_space_bbox(
        self, canvas: Canvas, box: Rectangle, color=DARKGREEN, line_width=0.1
    ):
                                                                 
        if not self.render_options.render_space_bbox:                    
            return
        with canvas.do.save_state():
            canvas.do.fill_color(color).line_width(line_width).rect(
                box.llx, box.lly, box.width, box.height, fill=True
            )

    def _debug_draw_baseline(
        self,
        canvas: Canvas,
        line_box: Rectangle,
        baseline_lly,
        color=MAGENTA,
        line_width=0.25,
    ):
                                       
        if not self.render_options.render_baseline:
            return
        with canvas.do.save_state():
            canvas.do.stroke_color(color).line_width(line_width).line(
                line_box.llx,
                baseline_lly,
                line_box.urx,
                baseline_lly,
            )
