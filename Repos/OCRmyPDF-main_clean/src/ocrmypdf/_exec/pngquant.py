                                              
                                  

"""Interface to pngquant executable."""

from __future__ import annotations

from pathlib import Path
from subprocess import PIPE

from packaging.version import Version

from ocrmypdf.exceptions import MissingDependencyError
from ocrmypdf.subprocess import get_version, run


def version() -> Version:
    return Version(get_version('pngquant', regex=r'(\d+(\.\d+)*).*'))


def available():
    try:
        version()
    except MissingDependencyError:
        return False
    return True


def quantize(input_file: Path, output_file: Path, quality_min: int, quality_max: int):
           
    with open(input_file, 'rb') as input_stream:
        args = [
            'pngquant',
            '--force',
            '--skip-if-larger',
            '--quality',
            f'{quality_min}-{quality_max}',
            '--',                                       
            '-',                                     
        ]
        result = run(args, stdin=input_stream, stdout=PIPE, stderr=PIPE, check=False)

    if result.returncode == 0:
                                                                            
        output_file.write_bytes(result.stdout)
