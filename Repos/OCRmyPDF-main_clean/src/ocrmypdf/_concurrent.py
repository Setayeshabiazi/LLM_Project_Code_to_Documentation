                                              
                                  

"""OCRmyPDF concurrency abstractions."""

from __future__ import annotations

import threading
from abc import ABC, abstractmethod
from collections.abc import Callable, Iterable
from typing import Any, TypeVar

from ocrmypdf._progressbar import NullProgressBar, ProgressBar

T = TypeVar('T')


def _task_noop(*_args, **_kwargs):
    return


def _task_finished_noop(_result: Any, pbar: ProgressBar):
    pbar.update()


class Executor(ABC):
                                       

    pool_lock = threading.Lock()
    pbar_class = NullProgressBar

    def __init__(self, *, pbar_class=None):
        if pbar_class:
            self.pbar_class = pbar_class

    def __call__(
        self,
        *,
        use_threads: bool,
        max_workers: int,
        progress_kwargs: dict,
        worker_initializer: Callable | None = None,
        task: Callable[..., T] | None = None,
        task_arguments: Iterable | None = None,
        task_finished: Callable[[T, ProgressBar], None] | None = None,
    ) -> None:
                   
        if not task_arguments:
            return                  
        if not worker_initializer:
            worker_initializer = _task_noop
        if not task_finished:
            task_finished = _task_finished_noop
        if not task:
            task = _task_noop

        with self.pool_lock:
            self._execute(
                use_threads=use_threads,
                max_workers=max_workers,
                progress_kwargs=progress_kwargs,
                worker_initializer=worker_initializer,
                task=task,
                task_arguments=task_arguments,
                task_finished=task_finished,
            )

    @abstractmethod
    def _execute(
        self,
        *,
        use_threads: bool,
        max_workers: int,
        progress_kwargs: dict,
        worker_initializer: Callable,
        task: Callable,
        task_arguments: Iterable,
        task_finished: Callable,
    ):
                                                           


def setup_executor(plugin_manager) -> Executor:
    pbar_class = plugin_manager.hook.get_progressbar_class()
    return plugin_manager.hook.get_executor(progressbar_class=pbar_class)


class SerialExecutor(Executor):
           

    def _execute(
        self,
        *,
        use_threads: bool,
        max_workers: int,
        progress_kwargs: dict,
        worker_initializer: Callable,
        task: Callable,
        task_arguments: Iterable,
        task_finished: Callable,
    ):                                   
        with self.pbar_class(**progress_kwargs) as pbar:
            for args in task_arguments:
                result = task(*args)
                task_finished(result, pbar)
