                                              
                                  

"""OCRmyPDF pluggy plugin specification."""

from __future__ import annotations

from abc import ABC, abstractmethod
from argparse import ArgumentParser, Namespace
from collections.abc import Sequence, Set
from logging import Handler
from pathlib import Path
from typing import TYPE_CHECKING, NamedTuple

import pluggy

from ocrmypdf import Executor, PdfContext
from ocrmypdf._progressbar import ProgressBar
from ocrmypdf.helpers import Resolution

if TYPE_CHECKING:
    from PIL import Image

                                       
    from ocrmypdf._jobcontext import PageContext
    from ocrmypdf.pdfinfo import PdfInfo

                                      

hookspec = pluggy.HookspecMarker('ocrmypdf')

                                 
                                     


@hookspec(firstresult=True)
def get_logging_console() -> Handler:
           


@hookspec
def initialize(plugin_manager: pluggy.PluginManager) -> None:
           


@hookspec
def add_options(parser: ArgumentParser) -> None:
           


@hookspec
def check_options(options: Namespace) -> None:
           


@hookspec(firstresult=True)
def get_executor(progressbar_class: type[ProgressBar]) -> Executor:
           


@hookspec(firstresult=True)
def get_progressbar_class() -> type[ProgressBar]:
           


@hookspec
def validate(pdfinfo: PdfInfo, options: Namespace) -> None:
           


@hookspec(firstresult=True)
def rasterize_pdf_page(
    input_file: Path,
    output_file: Path,
    raster_device: str,
    raster_dpi: Resolution,
    pageno: int,
    page_dpi: Resolution | None,
    rotation: int | None,
    filter_vector: bool,
    stop_on_soft_error: bool,
) -> Path:
           


@hookspec(firstresult=True)
def filter_ocr_image(page: PageContext, image: Image.Image) -> Image.Image:
           


@hookspec(firstresult=True)
def filter_page_image(page: PageContext, image_filename: Path) -> Path:
           


@hookspec(firstresult=True)
def filter_pdf_page(page: PageContext, image_filename: Path, output_pdf: Path) -> Path:
           


class OrientationConfidence(NamedTuple):
           

    angle: int
    confidence: float


class OcrEngine(ABC):
           

    @staticmethod
    @abstractmethod
    def version() -> str:
                                                    

    @staticmethod
    @abstractmethod
    def creator_tag(options: Namespace) -> str:
                   

    @abstractmethod
    def __str__(self):
                   

    @staticmethod
    @abstractmethod
    def languages(options: Namespace) -> Set[str]:
                   

    @staticmethod
    @abstractmethod
    def get_orientation(input_file: Path, options: Namespace) -> OrientationConfidence:
                                                   

    @staticmethod
    def get_deskew(input_file: Path, options: Namespace) -> float:
                                                                
        return 0.0

    @staticmethod
    @abstractmethod
    def generate_hocr(
        input_file: Path, output_hocr: Path, output_text: Path, options: Namespace
    ) -> None:
                   

    @staticmethod
    @abstractmethod
    def generate_pdf(
        input_file: Path, output_pdf: Path, output_text: Path, options: Namespace
    ) -> None:
                   


@hookspec(firstresult=True)
def get_ocr_engine() -> OcrEngine:
           


@hookspec(firstresult=True)
def generate_pdfa(
    pdf_pages: list[Path],
    pdfmark: Path,
    output_file: Path,
    context: PdfContext,
    pdf_version: str,
    pdfa_part: str,
    progressbar_class: type[ProgressBar] | None,
    stop_on_soft_error: bool,
) -> Path:
           


@hookspec(firstresult=True)
def optimize_pdf(
    input_pdf: Path,
    output_pdf: Path,
    context: PdfContext,
    executor: Executor,
    linearize: bool,
) -> tuple[Path, Sequence[str]]:
           


@hookspec(firstresult=True)
def is_optimization_enabled(context: PdfContext) -> bool:
           
