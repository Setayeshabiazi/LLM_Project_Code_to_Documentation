                                              
                                  

"""Interface to Ghostscript executable."""

from __future__ import annotations

import logging
import os
import re
from collections import deque
from io import BytesIO
from os import fspath
from pathlib import Path
from subprocess import PIPE, CalledProcessError

from packaging.version import Version
from PIL import Image, UnidentifiedImageError

from ocrmypdf.exceptions import (
    ColorConversionNeededError,
    InputFileError,
    SubprocessOutputError,
)
from ocrmypdf.helpers import Resolution
from ocrmypdf.subprocess import get_version, run, run_polling_stderr

COLOR_CONVERSION_STRATEGIES = frozenset(
    [
        'CMYK',
        'Gray',
        'LeaveColorUnchanged',
        'RGB',
        'UseDeviceIndependentColor',
    ]
)
                                                    
GS = 'gswin64c' if os.name == 'nt' else 'gs'


log = logging.getLogger(__name__)


class DuplicateFilter(logging.Filter):
           

    def __init__(self, logger: logging.Logger, context_window=5):
        self.window: deque[str] = deque([], maxlen=context_window)
        self.logger = logger
        self.levelno = logging.DEBUG
        self.count = 0

    def filter(self, record):
        if record.msg in self.window:
            self.count += 1
            self.levelno = record.levelno
            return False
        else:
            if self.count >= 1:
                rep_msg = f"(suppressed {self.count} repeated lines)"
                self.count = 0                            
                self.logger.log(self.levelno, rep_msg)
                self.window.clear()
            self.window.append(record.msg)
            return True


log.addFilter(DuplicateFilter(log))


def version() -> Version:
    return Version(get_version(GS))


def _gs_error_reported(stream) -> bool:
    match = re.search(r'error', stream, flags=re.IGNORECASE)
    return bool(match)


def _gs_devicen_reported(stream) -> bool:
           
    match = re.search(
        r'DeviceN.*inappropriate alternate',
        stream,
        flags=re.IGNORECASE | re.MULTILINE,
    )
    return bool(match)


def rasterize_pdf(
    input_file: os.PathLike,
    output_file: os.PathLike,
    *,
    raster_device: str,
    raster_dpi: Resolution,
    pageno: int = 1,
    page_dpi: Resolution | None = None,
    rotation: int | None = None,
    filter_vector: bool = False,
    stop_on_error: bool = False,
):
                                                                               
    raster_dpi = raster_dpi.round(6)
    if not page_dpi:
        page_dpi = raster_dpi

    args_gs = (
        [
            GS,
            '-dSAFER',
            '-dBATCH',
            '-dNOPAUSE',
            '-dInterpolateControl=-1',
            f'-sDEVICE={raster_device}',
            f'-dFirstPage={pageno}',
            f'-dLastPage={pageno}',
            f'-r{raster_dpi.x:f}x{raster_dpi.y:f}',
        ]
        + (['-dFILTERVECTOR'] if filter_vector else [])
        + (['-dPDFSTOPONERROR'] if stop_on_error else [])
        + [
            '-o',
            fspath(output_file),
            '-sstdout=%stderr',                                        
            '-dAutoRotatePages=/None',                                    
            '-f',
            fspath(input_file),
        ]
    )

    try:
        p = run(args_gs, stdout=PIPE, stderr=PIPE, check=True)
    except CalledProcessError as e:
        log.error(e.stderr.decode(errors='replace'))
        Path(output_file).unlink(missing_ok=True)
        raise SubprocessOutputError("Ghostscript rasterizing failed") from e

    stderr = p.stderr.decode(errors='replace')
    if _gs_error_reported(stderr):
        log.error(stderr)
        if stop_on_error and "recoverable image error" in stderr:
            Path(output_file).unlink(missing_ok=True)
            raise InputFileError(
                "Ghostscript rasterizing failed. The input file contains errors that "
                "cause PDF viewers to interpret it differently and incorrectly. "
                "Try using --continue-on-soft-render-error and manually inspect the "
                "input and output files to check for visual differences or errors."
            )

    try:
        with Image.open(output_file) as im:
            if rotation is not None:
                log.debug("Rotating output by %i", rotation)
                                                                     
                                                                   
                if rotation == 90:
                    im = im.transpose(Image.Transpose.ROTATE_90)
                elif rotation == 180:
                    im = im.transpose(Image.Transpose.ROTATE_180)
                elif rotation == 270:
                    im = im.transpose(Image.Transpose.ROTATE_270)
                if rotation % 180 == 90:
                    page_dpi = page_dpi.flip_axis()
            im.save(output_file, dpi=page_dpi)
    except UnidentifiedImageError:
        log.error(
            f"Ghostscript (using {raster_device} at {raster_dpi} dpi) produced "
            "an invalid page image file."
        )
        raise
    except OSError as e:
        log.error(
            f"Ghostscript (using {raster_device} at {raster_dpi} dpi) produced "
            "an invalid page image file."
        )
        raise UnidentifiedImageError() from e


class GhostscriptFollower:
                                                                                  

    re_process = re.compile(r"Processing pages \d+ through (\d+).")
    re_page = re.compile(r"Page (\d+)")

    def __init__(self, progressbar_class):
        self.count = 0
        self.progressbar_class = progressbar_class
        self.progressbar = None

    def __enter__(self):
                                                                              
                                                                            
                              
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.progressbar:
            return self.progressbar.__exit__(exc_type, exc_value, traceback)
        return False

    def __call__(self, line):
        if not self.progressbar_class:
            return
        if not self.progressbar:
            m = self.re_process.match(line.strip())
            if m:
                self.count = int(m.group(1))
                self.progressbar = self.progressbar_class(
                    total=self.count, desc="PDF/A conversion", unit='page'
                )
                                                                            
                self.progressbar.__enter__()
        else:
            if self.re_page.match(line.strip()):
                self.progressbar.update()


def generate_pdfa(
    pdf_pages,
    output_file: os.PathLike,
    *,
    compression: str,
    color_conversion_strategy: str,
    pdf_version: str = '1.5',
    pdfa_part: str = '2',
    progressbar_class=None,
    stop_on_error: bool = False,
):
                                                                                 
                                                                                 
                                              
    compression_args = []
    if compression == 'jpeg':
        compression_args = [
            "-dAutoFilterColorImages=false",
            "-dColorImageFilter=/DCTEncode",
            "-dAutoFilterGrayImages=false",
            "-dGrayImageFilter=/DCTEncode",
        ]
    elif compression == 'lossless':
        compression_args = [
            "-dAutoFilterColorImages=false",
            "-dColorImageFilter=/FlateEncode",
            "-dAutoFilterGrayImages=false",
            "-dGrayImageFilter=/FlateEncode",
        ]
    else:
        compression_args = [
            "-dAutoFilterColorImages=true",
            "-dAutoFilterGrayImages=true",
        ]

    gs_version = version()
    if gs_version == Version('9.56.0'):
                                                          
                                                             
        compression_args.append('-dNEWPDF=false')

    if os.name == 'nt':
                                                              
        stop_on_error = False

                                                                          
                  
                                                         
    args_gs = (
        [
            GS,
            "-dBATCH",
            "-dNOPAUSE",
            "-dSAFER",
            f"-dCompatibilityLevel={str(pdf_version)}",
            "-sDEVICE=pdfwrite",
            "-dAutoRotatePages=/None",
            f"-sColorConversionStrategy={color_conversion_strategy}",
        ]
        + (['-dPDFSTOPONERROR'] if stop_on_error else [])
        + compression_args
        + [
            "-dJPEGQ=95",
            f"-dPDFA={pdfa_part}",
            "-dPDFACompatibilityPolicy=1",
            "-o",
            fspath(output_file),
            "-sstdout=%stderr",                                        
        ]
    )
    args_gs.extend(fspath(s) for s in pdf_pages)                       
    try:
        with GhostscriptFollower(progressbar_class) as pbar:
            p = run_polling_stderr(
                args_gs,
                stderr=PIPE,
                check=True,
                text=True,
                encoding='utf-8',
                errors='replace',
                callback=pbar,
            )
    except CalledProcessError as e:
                                                                         
                                              
        log.error(e.stderr)
        raise SubprocessOutputError('Ghostscript PDF/A rendering failed') from e
    else:
        stderr = p.stderr
                                                                            
                     
        if _gs_error_reported(stderr):
                                                                           
                                                                             
                                                                           
                                                              
            for part in stderr.split('****'):
                log.error(part)
        if _gs_devicen_reported(stderr):
            raise ColorConversionNeededError()
