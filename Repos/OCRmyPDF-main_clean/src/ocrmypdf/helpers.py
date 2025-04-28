                                              
                                  

"""Support functions."""

from __future__ import annotations

import logging
import multiprocessing
import os
import shutil
import warnings
from collections.abc import Callable, Iterable, Sequence
from contextlib import suppress
from decimal import Decimal
from io import StringIO
from math import isclose, isfinite
from pathlib import Path
from statistics import harmonic_mean
from typing import (
    Any,
    Generic,
    TypeVar,
)

import img2pdf
import pikepdf
from deprecation import deprecated

log = logging.getLogger(__name__)

IMG2PDF_KWARGS = dict(engine=img2pdf.Engine.pikepdf, rotation=img2pdf.Rotation.ifvalid)


T = TypeVar('T', float, int, Decimal)


class Resolution(Generic[T]):
           

    x: T
    y: T

    __slots__ = ('x', 'y')

    def __init__(self, x: T, y: T):
                                            
        self.x = x
        self.y = y

                                                                      
                                                    
    CONVERSION_ERROR = 0.002

    def round(self, ndigits: int) -> Resolution:
                                                       
        return Resolution(round(self.x, ndigits), round(self.y, ndigits))

    def to_int(self) -> Resolution[int]:
                                       
        return Resolution(int(round(self.x)), int(round(self.y)))

    @classmethod
    def _isclose(cls, a, b):
        return isclose(a, b, rel_tol=cls.CONVERSION_ERROR)

    @property
    def is_square(self) -> bool:
                                                        
        return self._isclose(self.x, self.y)

    @property
    def is_finite(self) -> bool:
                                                      
        return isfinite(self.x) and isfinite(self.y)

    def to_scalar(self) -> float:
                   
        return harmonic_mean([float(self.x), float(self.y)])

    def _take_minmax(
        self, vals: Iterable[Any], yvals: Iterable[Any] | None, cmp: Callable
    ) -> Resolution:
                                                                                   
        if yvals is not None:
            return Resolution(cmp(self.x, *vals), cmp(self.y, *yvals))
        cmp_x, cmp_y = self.x, self.y
        for x, y in vals:
            cmp_x = cmp(x, cmp_x)
            cmp_y = cmp(y, cmp_y)
        return Resolution(cmp_x, cmp_y)

    def take_max(
        self, vals: Iterable[Any], yvals: Iterable[Any] | None = None
    ) -> Resolution:
                                                                                   
        return self._take_minmax(vals, yvals, max)

    def take_min(
        self, vals: Iterable[Any], yvals: Iterable[Any] | None = None
    ) -> Resolution:
                                                                                   
        return self._take_minmax(vals, yvals, min)

    def flip_axis(self) -> Resolution[T]:
                                                                  
        return Resolution(self.y, self.x)

    def __getitem__(self, idx: int | slice) -> T:
                                           
        return (self.x, self.y)[idx]

    def __str__(self):
                                                               
        return f"{self.x:f}×{self.y:f}"

    def __repr__(self):                    
                                                
        return f"Resolution({self.x!r}, {self.y!r})"

    def __eq__(self, other):
                                                                           
        if isinstance(other, tuple) and len(other) == 2:
            other = Resolution(*other)
        if not isinstance(other, Resolution):
            return NotImplemented
        return self._isclose(self.x, other.x) and self._isclose(self.y, other.y)


@deprecated(deprecated_in='15.4.0')
class NeverRaise(Exception):
                                            


def safe_symlink(input_file: os.PathLike, soft_link_name: os.PathLike) -> None:
           
    input_file = os.fspath(input_file)
    soft_link_name = os.fspath(soft_link_name)

                                           
    if input_file == soft_link_name:
        log.warning(
            "No symbolic link created. You are using the original data directory "
            "as the working directory."
        )
        return

                                                  
    if os.path.lexists(soft_link_name):
                                                              
        if not os.path.islink(soft_link_name):
            raise FileExistsError(f"{soft_link_name} exists and is not a link")
        os.unlink(soft_link_name)

    if not os.path.exists(input_file):
        raise FileNotFoundError(f"trying to create a broken symlink to {input_file}")

    if os.name == 'nt':
                                                                         
        shutil.copyfile(input_file, soft_link_name)
        return

    log.debug("os.symlink(%s, %s)", input_file, soft_link_name)

                                              
    os.symlink(os.path.abspath(input_file), soft_link_name)


def samefile(file1: os.PathLike, file2: os.PathLike) -> bool:
           
    if os.name == 'nt':
        return file1 == file2
    else:
        return os.path.samefile(file1, file2)


def is_iterable_notstr(thing: Any) -> bool:
                                                           
    return isinstance(thing, Iterable) and not isinstance(thing, str)


def monotonic(seq: Sequence) -> bool:
                                                    
    return all(b > a for a, b in zip(seq, seq[1:]))


def page_number(input_file: os.PathLike) -> int:
                                                                          
    return int(os.path.basename(os.fspath(input_file))[0:6])


def available_cpu_count() -> int:
                                               
    try:
        return multiprocessing.cpu_count()
    except NotImplementedError:
        pass
    warnings.warn(
        "Could not get CPU count. Assuming one (1) CPU. Use -j N to set manually."
    )
    return 1


def is_file_writable(test_file: os.PathLike) -> bool:
           
    try:
        p = Path(test_file)
        if p.is_symlink():
            p = p.resolve(strict=False)

                                                       
        if p.exists() and (p.is_file() or p.samefile(os.devnull)):
            return os.access(
                os.fspath(p),
                os.W_OK,
                effective_ids=(os.access in os.supports_effective_ids),
            )

        try:
            fp = p.open('wb')
        except OSError:
            return False
        else:
            fp.close()
            with suppress(OSError):
                p.unlink()
        return True
    except (OSError, RuntimeError) as e:
        log.debug(e)
        log.error(str(e))
        return False


def check_pdf(input_file: Path) -> bool:
           
    try:
        pdf = pikepdf.open(input_file)
    except pikepdf.PdfError as e:
        log.error(e)
        return False
    else:
        with pdf:
            with warnings.catch_warnings():
                warnings.filterwarnings('ignore', message=r'pikepdf.*JBIG2.*')
                messages = pdf.check()
            success = True
            for msg in messages:
                if 'error' in msg.lower():
                    log.error(msg)
                    success = False
                elif (
                    "/DecodeParms: operation for dictionary attempted on object "
                    "of type null" in msg
                ):
                    pass                           
                else:
                    log.warning(msg)
                    success = False

            sio = StringIO()
            linearize_msgs = ''
            try:
                                                                                 
                                                                     
                pdf.check_linearization(sio)
            except (RuntimeError, pikepdf.ForeignObjectError):
                pass
            else:
                linearize_msgs = sio.getvalue()
                if linearize_msgs:
                    log.warning(linearize_msgs)

            if success and not linearize_msgs:
                return True
            return False


def clamp(n: T, smallest: T, largest: T) -> T:
                                                                            
    return max(smallest, min(n, largest))


def remove_all_log_handlers(logger: logging.Logger) -> None:
           
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
        handler.close()                                                         


def pikepdf_enable_mmap() -> None:
                                        
    try:
        pikepdf._core.set_access_default_mmap(True)
        log.debug(
            "pikepdf mmap "
            + (
                'enabled'
                if pikepdf._core.get_access_default_mmap()                              
                else 'disabled'
            )
        )
    except AttributeError:
        log.debug("pikepdf mmap not available")


def running_in_docker() -> bool:
                                                                      
    return Path('/.dockerenv').exists()


def running_in_snap() -> bool:
                                                                    
    try:
        cgroup_text = Path('/proc/self/cgroup').read_text()
        return 'snap.ocrmypdf' in cgroup_text
    except FileNotFoundError:
        return False
