                                              
                                  

"""Defines context objects that are passed to child processes/threads."""

from __future__ import annotations

import os
from argparse import Namespace
from collections.abc import Iterator
from copy import copy
from pathlib import Path

from pluggy import PluginManager

from ocrmypdf.pdfinfo import PdfInfo
from ocrmypdf.pdfinfo.info import PageInfo


class PdfContext:
                                                                 

    options: Namespace                                                   
    origin: Path                                             
    pdfinfo: PdfInfo                                
    plugin_manager: PluginManager                                                  

    def __init__(
        self,
        options: Namespace,
        work_folder: Path,
        origin: Path,
        pdfinfo: PdfInfo,
        plugin_manager,
    ):
        self.options = options
        self.work_folder = work_folder
        self.origin = origin
        self.pdfinfo = pdfinfo
        self.plugin_manager = plugin_manager

    def get_path(self, name: str) -> Path:
                   
        return self.work_folder / name

    def get_page_contexts(self) -> Iterator[PageContext]:
                                                   
        npages = len(self.pdfinfo)
        for n in range(npages):
            yield PageContext(self, n)

    def get_page_context_args(self) -> Iterator[tuple[PageContext]]:
                                                                                        
        npages = len(self.pdfinfo)
        for n in range(npages):
            yield (PageContext(self, n),)


class PageContext:
           

    options: Namespace                                                   
    origin: Path                                             
    pageno: int                                   
    pageinfo: PageInfo                              
    plugin_manager: PluginManager                                                  

    def __init__(self, pdf_context: PdfContext, pageno):
        self.work_folder = pdf_context.work_folder
        self.origin = pdf_context.origin
        self.options = pdf_context.options
        self.pageno = pageno
        self.pageinfo = pdf_context.pdfinfo[pageno]
        self.plugin_manager = pdf_context.plugin_manager

    def get_path(self, name: str) -> Path:
                   
        return self.work_folder / f"{(self.pageno + 1):06d}_{name}"

    def __getstate__(self):
        state = self.__dict__.copy()

        state['options'] = copy(self.options)
        if not isinstance(state['options'].input_file, str | bytes | os.PathLike):
            state['options'].input_file = 'stream'
        if not isinstance(state['options'].output_file, str | bytes | os.PathLike):
            state['options'].output_file = 'stream'
        return state
