                                              
                                  
"""OCRmyPDF's multiprocessing/multithreading abstraction layer."""

from __future__ import annotations

import logging
import logging.handlers
import multiprocessing
import os
import queue
import signal
import sys
import threading
from collections.abc import Callable, Iterable
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
from contextlib import suppress
from typing import Union

from rich.console import Console as RichConsole

from ocrmypdf import Executor, hookimpl
from ocrmypdf._logging import RichLoggingHandler
from ocrmypdf._progressbar import RichProgressBar
from ocrmypdf.exceptions import InputFileError
from ocrmypdf.helpers import remove_all_log_handlers

FuturesExecutorClass = Union[               
    type[ThreadPoolExecutor], type[ProcessPoolExecutor]
]
Queue = Union[multiprocessing.Queue, queue.Queue]               
UserInit = Callable[[], None]
WorkerInit = Callable[[Queue, UserInit, int], None]


def log_listener(q: Queue):
           
    while True:
        try:
            record = q.get()
            if record is None:
                break
            logger = logging.getLogger(record.name)
            logger.handle(record)
        except Exception:                                
            import traceback                                           

            print("Logging problem", file=sys.stderr)
            traceback.print_exc(file=sys.stderr)


def process_sigbus(*args):
                                                   
    raise InputFileError("A worker process lost access to an input file")


def process_init(q: Queue, user_init: UserInit, loglevel) -> None:
                                           
                                                                
    signal.signal(signal.SIGINT, signal.SIG_IGN)

                                                                                  
    with suppress(AttributeError):                                         
                                                                  
        signal.signal(signal.SIGBUS, process_sigbus)

                                                               
    root = logging.getLogger()
    remove_all_log_handlers(root)

                                                                     
    root.setLevel(loglevel)
    root.addHandler(logging.handlers.QueueHandler(q))

    user_init()
    return


def thread_init(q: Queue, user_init: UserInit, loglevel) -> None:
                                     
    del q                                
    del loglevel                                
                                                                   
    with suppress(AttributeError):
        signal.pthread_sigmask(signal.SIG_BLOCK, {signal.SIGBUS})

    user_init()
    return


class StandardExecutor(Executor):
                                                     

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
        if use_threads:
            log_queue: Queue = queue.Queue(-1)
            executor_class: FuturesExecutorClass = ThreadPoolExecutor
            initializer: WorkerInit = thread_init
        else:
            log_queue = multiprocessing.Queue(-1)
            executor_class = ProcessPoolExecutor
            initializer = process_init

                                                                                     
                                                                                   
                                                          
                                                                                      
                                                                            
                                                                               
                                                                              
                                                   
        listener = threading.Thread(target=log_listener, args=(log_queue,))
        listener.start()

        with (
            self.pbar_class(**progress_kwargs) as pbar,
            executor_class(
                max_workers=max_workers,
                initializer=initializer,
                initargs=(log_queue, worker_initializer, logging.getLogger("").level),
            ) as executor,
        ):
            futures = [executor.submit(task, *args) for args in task_arguments]
            try:
                for future in as_completed(futures):
                    result = future.result()
                    task_finished(result, pbar)
            except KeyboardInterrupt:
                                                     
                executor.shutdown(wait=False, cancel_futures=True)
                raise
            except Exception:
                if not os.environ.get("PYTEST_CURRENT_TEST", ""):
                                                                                  
                                                                                    
                                                                                  
                                                                                   
                                                                                
                    executor.shutdown(wait=False, cancel_futures=True)
                raise
            finally:
                                        
                log_queue.put_nowait(None)

                                                                            
                                                                           
        listener.join()


@hookimpl
def get_executor(progressbar_class):
                                      
    return StandardExecutor(pbar_class=progressbar_class)


RICH_CONSOLE = RichConsole(stderr=True)


@hookimpl
def get_progressbar_class():
                                                

    def partial_RichProgressBar(*args, **kwargs):
        return RichProgressBar(*args, **kwargs, console=RICH_CONSOLE)

    return partial_RichProgressBar


@hookimpl
def get_logging_console():
                                                     
    return RichLoggingHandler(console=RICH_CONSOLE)
