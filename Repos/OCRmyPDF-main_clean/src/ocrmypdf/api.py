                                              
                                  

"""Functions for using ocrmypdf as an API."""

from __future__ import annotations

import logging
import os
import sys
import threading
from argparse import Namespace
from collections.abc import Iterable, Sequence
from enum import IntEnum
from io import IOBase
from pathlib import Path
from typing import BinaryIO
from warnings import warn

import pluggy

from ocrmypdf._logging import PageNumberFilter
from ocrmypdf._pipelines.hocr_to_ocr_pdf import run_hocr_to_ocr_pdf_pipeline
from ocrmypdf._pipelines.ocr import run_pipeline, run_pipeline_cli
from ocrmypdf._pipelines.pdf_to_hocr import run_hocr_pipeline
from ocrmypdf._plugin_manager import get_plugin_manager
from ocrmypdf._validation import check_options
from ocrmypdf.cli import ArgumentParser, get_parser
from ocrmypdf.helpers import is_iterable_notstr

StrPath = Path | str | bytes
PathOrIO = BinaryIO | StrPath

                                                                        
                                                                      
                           
_api_lock = threading.Lock()


class Verbosity(IntEnum):
                                                

                                  
    quiet = -1                           
    default = 0                             
    debug = 1                                   
    debug_all = 2                                                                


def configure_logging(
    verbosity: Verbosity,
    *,
    progress_bar_friendly: bool = True,
    manage_root_logger: bool = False,
    plugin_manager: pluggy.PluginManager | None = None,
):
           
    prefix = '' if manage_root_logger else 'ocrmypdf'

    log = logging.getLogger(prefix)
    log.setLevel(logging.DEBUG)

    console = None
    if plugin_manager and progress_bar_friendly:
        console = plugin_manager.hook.get_logging_console()

    if not console:
        console = logging.StreamHandler(stream=sys.stderr)

    if verbosity < 0:
        console.setLevel(logging.ERROR)
    elif verbosity >= 1:
        console.setLevel(logging.DEBUG)
    else:
        console.setLevel(logging.INFO)

    console.addFilter(PageNumberFilter())

    if verbosity >= 2:
        fmt = '%(levelname)7s %(name)s -%(pageno)s %(message)s'
    else:
        fmt = '%(pageno)s%(message)s'

    formatter = None

    if not formatter:
        formatter = logging.Formatter(fmt=fmt)

    console.setFormatter(formatter)
    log.addHandler(console)

    if verbosity <= 1:
        pdfminer_log = logging.getLogger('pdfminer')
        pdfminer_log.setLevel(logging.ERROR)
        pil_log = logging.getLogger('PIL')
        pil_log.setLevel(logging.INFO)

    if manage_root_logger:
        logging.captureWarnings(True)

    return log


def _kwargs_to_cmdline(
    *, defer_kwargs: set[str], **kwargs
) -> tuple[list[str | bytes], dict[str, str | bytes]]:
                                                   
    cmdline: list[str | bytes] = []
    deferred = {}
    for arg, val in kwargs.items():
        if val is None:
            continue

                                                   
        if arg in defer_kwargs:
            deferred[arg] = val
            continue

        cmd_style_arg = arg.replace('_', '-')

                                                                
        if isinstance(val, bool):
            if val:
                cmdline.append(f"--{cmd_style_arg}")
            continue

        if is_iterable_notstr(val):
            for elem in val:
                cmdline.append(f"--{cmd_style_arg}")
                cmdline.append(elem)
            continue

                             
        cmdline.append(f"--{cmd_style_arg}")
        if isinstance(val, int | float):
            cmdline.append(str(val))
        elif isinstance(val, str):
            cmdline.append(val)
        elif isinstance(val, Path):
            cmdline.append(str(val))
        else:
            raise TypeError(f"{arg}: {val} ({type(val)})")
    return cmdline, deferred


def create_options(
    *, input_file: PathOrIO, output_file: PathOrIO, parser: ArgumentParser, **kwargs
) -> Namespace:
           
    cmdline, deferred = _kwargs_to_cmdline(
        defer_kwargs={'progress_bar', 'plugins', 'parser', 'input_file', 'output_file'},
        **kwargs,
    )
    if isinstance(input_file, BinaryIO | IOBase):
        cmdline.append('stream://input_file')
    else:
        cmdline.append(os.fspath(input_file))
    if isinstance(output_file, BinaryIO | IOBase):
        cmdline.append('stream://output_file')
    else:
        cmdline.append(os.fspath(output_file))
    if 'sidecar' in kwargs and isinstance(kwargs['sidecar'], BinaryIO | IOBase):
        cmdline.append('--sidecar')
        cmdline.append('stream://sidecar')

    parser.enable_api_mode()
    options = parser.parse_args(cmdline)
    for keyword, val in deferred.items():
        setattr(options, keyword, val)

    if options.input_file == 'stream://input_file':
        options.input_file = input_file
    if options.output_file == 'stream://output_file':
        options.output_file = output_file
    if options.sidecar == 'stream://sidecar':
        options.sidecar = kwargs['sidecar']

    return options


def ocr(              
    input_file: PathOrIO,
    output_file: PathOrIO,
    *,
    language: Iterable[str] | None = None,
    image_dpi: int | None = None,
    output_type: str | None = None,
    sidecar: PathOrIO | None = None,
    jobs: int | None = None,
    use_threads: bool | None = None,
    title: str | None = None,
    author: str | None = None,
    subject: str | None = None,
    keywords: str | None = None,
    rotate_pages: bool | None = None,
    remove_background: bool | None = None,
    deskew: bool | None = None,
    clean: bool | None = None,
    clean_final: bool | None = None,
    unpaper_args: str | None = None,
    oversample: int | None = None,
    remove_vectors: bool | None = None,
    force_ocr: bool | None = None,
    skip_text: bool | None = None,
    redo_ocr: bool | None = None,
    skip_big: float | None = None,
    optimize: int | None = None,
    jpg_quality: int | None = None,
    png_quality: int | None = None,
    jbig2_lossy: bool | None = None,
    jbig2_page_group_size: int | None = None,
    jbig2_threshold: float | None = None,
    pages: str | None = None,
    max_image_mpixels: float | None = None,
    tesseract_config: Iterable[str] | None = None,
    tesseract_pagesegmode: int | None = None,
    tesseract_oem: int | None = None,
    tesseract_thresholding: int | None = None,
    pdf_renderer: str | None = None,
    tesseract_timeout: float | None = None,
    tesseract_non_ocr_timeout: float | None = None,
    tesseract_downsample_above: int | None = None,
    tesseract_downsample_large_images: bool | None = None,
    rotate_pages_threshold: float | None = None,
    pdfa_image_compression: str | None = None,
    color_conversion_strategy: str | None = None,
    user_words: os.PathLike | None = None,
    user_patterns: os.PathLike | None = None,
    fast_web_view: float | None = None,
    continue_on_soft_render_error: bool | None = None,
    invalidate_digital_signatures: bool | None = None,
    plugins: Iterable[Path | str] | None = None,
    plugin_manager=None,
    keep_temporary_files: bool | None = None,
    progress_bar: bool | None = None,
    **kwargs,
):
           
    if plugins and plugin_manager:
        raise ValueError("plugins= and plugin_manager are mutually exclusive")

    if not plugins:
        plugins = []
    elif isinstance(plugins, str | Path):
        plugins = [plugins]
    else:
        plugins = list(plugins)

                                                                            
    create_options_kwargs = {
        k: v
        for k, v in locals().items()
        if k not in {'input_file', 'output_file', 'kwargs'}
    }
    create_options_kwargs.update(kwargs)

    parser = get_parser()
    with _api_lock:
        if not plugin_manager:
            plugin_manager = get_plugin_manager(plugins)
        plugin_manager.hook.add_options(parser=parser)                             

        if 'verbose' in kwargs:
            warn("ocrmypdf.ocr(verbose=) is ignored. Use ocrmypdf.configure_logging().")

        options = create_options(
            input_file=input_file,
            output_file=output_file,
            parser=parser,
            **create_options_kwargs,
        )
        check_options(options, plugin_manager)
        return run_pipeline(options=options, plugin_manager=plugin_manager)


def _pdf_to_hocr(              
    input_pdf: Path,
    output_folder: Path,
    *,
    language: Iterable[str] | None = None,
    image_dpi: int | None = None,
    jobs: int | None = None,
    use_threads: bool | None = None,
    title: str | None = None,
    author: str | None = None,
    subject: str | None = None,
    keywords: str | None = None,
    rotate_pages: bool | None = None,
    remove_background: bool | None = None,
    deskew: bool | None = None,
    clean: bool | None = None,
    clean_final: bool | None = None,
    unpaper_args: str | None = None,
    oversample: int | None = None,
    remove_vectors: bool | None = None,
    force_ocr: bool | None = None,
    skip_text: bool | None = None,
    redo_ocr: bool | None = None,
    skip_big: float | None = None,
    pages: str | None = None,
    max_image_mpixels: float | None = None,
    tesseract_config: Iterable[str] | None = None,
    tesseract_pagesegmode: int | None = None,
    tesseract_oem: int | None = None,
    tesseract_thresholding: int | None = None,
    tesseract_timeout: float | None = None,
    tesseract_non_ocr_timeout: float | None = None,
    tesseract_downsample_above: int | None = None,
    tesseract_downsample_large_images: bool | None = None,
    rotate_pages_threshold: float | None = None,
    user_words: os.PathLike | None = None,
    user_patterns: os.PathLike | None = None,
    continue_on_soft_render_error: bool | None = None,
    invalidate_digital_signatures: bool | None = None,
    plugin_manager=None,
    plugins: Sequence[Path | str] | None = None,
    keep_temporary_files: bool | None = None,
    **kwargs,
):
           
                                                                            
    create_options_kwargs = {
        k: v
        for k, v in locals().items()
        if k not in {'input_pdf', 'output_folder', 'kwargs'}
    }
    create_options_kwargs.update(kwargs)

    parser = get_parser()

    with _api_lock:
        if not plugin_manager:
            plugin_manager = get_plugin_manager(plugins)
        plugin_manager.hook.add_options(parser=parser)                             

        cmdline, deferred = _kwargs_to_cmdline(
            defer_kwargs={'input_pdf', 'output_folder', 'plugins'},
            **create_options_kwargs,
        )
        cmdline.append(str(input_pdf))
        cmdline.append(str(output_folder))
        parser.enable_api_mode()
        options = parser.parse_args(cmdline)
        for keyword, val in deferred.items():
            setattr(options, keyword, val)
        delattr(options, 'output_file')
        setattr(options, 'output_folder', output_folder)

        return run_hocr_pipeline(options=options, plugin_manager=plugin_manager)


def _hocr_to_ocr_pdf(              
    work_folder: Path,
    output_file: Path,
    *,
    jobs: int | None = None,
    use_threads: bool | None = None,
    optimize: int | None = None,
    jpg_quality: int | None = None,
    png_quality: int | None = None,
    jbig2_lossy: bool | None = None,
    jbig2_page_group_size: int | None = None,
    jbig2_threshold: float | None = None,
    pdfa_image_compression: str | None = None,
    color_conversion_strategy: str | None = None,
    fast_web_view: float | None = None,
    plugin_manager=None,
    plugins: Sequence[Path | str] | None = None,
    **kwargs,
):
           
                                                                            
    create_options_kwargs = {
        k: v
        for k, v in locals().items()
        if k not in {'work_folder', 'output_pdf', 'kwargs'}
    }
    create_options_kwargs.update(kwargs)

    parser = get_parser()

    with _api_lock:
        if not plugin_manager:
            plugin_manager = get_plugin_manager(plugins)
        plugin_manager.hook.add_options(parser=parser)                             

        cmdline, deferred = _kwargs_to_cmdline(
            defer_kwargs={'work_folder', 'output_file', 'plugins'},
            **create_options_kwargs,
        )
        cmdline.append(str(work_folder))
        cmdline.append(str(output_file))
        parser.enable_api_mode()
        options = parser.parse_args(cmdline)
        for keyword, val in deferred.items():
            setattr(options, keyword, val)
        delattr(options, 'input_file')
        setattr(options, 'work_folder', work_folder)

        return run_hocr_to_ocr_pdf_pipeline(
            options=options, plugin_manager=plugin_manager
        )


__all__ = [
    'PageNumberFilter',
    'Verbosity',
    'check_options',
    'configure_logging',
    'create_options',
    'get_parser',
    'get_plugin_manager',
    'ocr',
    'run_pipeline',
    'run_pipeline_cli',
]
