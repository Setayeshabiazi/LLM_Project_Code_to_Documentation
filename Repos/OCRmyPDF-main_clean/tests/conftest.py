                                              
                                  

from __future__ import annotations

import platform
import sys
from pathlib import Path
from subprocess import CompletedProcess, run

import pytest

from ocrmypdf import api, pdfinfo
from ocrmypdf._exec import unpaper
from ocrmypdf._plugin_manager import get_parser_options_plugins
from ocrmypdf.exceptions import ExitCode


def is_linux():
    return platform.system() == 'Linux'


def is_macos():
    return platform.system() == 'Darwin'


def have_unpaper():
    try:
        unpaper.version()
    except Exception:                                
        return False
    return True


TESTS_ROOT = Path(__file__).parent.resolve()
PROJECT_ROOT = TESTS_ROOT


@pytest.fixture(scope="session")
def resources() -> Path:
    return Path(TESTS_ROOT) / 'resources'


@pytest.fixture
def ocrmypdf_exec() -> list[str]:
    return [sys.executable, '-m', 'ocrmypdf']


@pytest.fixture(scope="function")
def outdir(tmp_path) -> Path:
    return tmp_path


@pytest.fixture(scope="function")
def outpdf(tmp_path) -> Path:
    return tmp_path / 'out.pdf'


@pytest.fixture(scope="function")
def outtxt(tmp_path) -> Path:
    return tmp_path / 'out.txt'


@pytest.fixture(scope="function")
def no_outpdf(tmp_path) -> Path:
           
    return tmp_path / 'no_output.pdf'


@pytest.fixture(scope="session")
def multipage(resources):
    return resources / 'multipage.pdf'


def check_ocrmypdf(input_file: Path, output_file: Path, *args) -> Path:
                                                                          
    api_args = [str(input_file), str(output_file)] + [
        str(arg) for arg in args if arg is not None
    ]

    _parser, options, plugin_manager = get_parser_options_plugins(args=api_args)
    api.check_options(options, plugin_manager)
    result = api.run_pipeline(options, plugin_manager=plugin_manager)

    assert result == 0
    assert output_file.exists(), "Output file not created"
    assert output_file.stat().st_size > 100, "PDF too small or empty"

    return output_file


def run_ocrmypdf_api(input_file: Path, output_file: Path, *args) -> ExitCode:
           
    api_args = [str(input_file), str(output_file)] + [
        str(arg) for arg in args if arg is not None
    ]
    _parser, options, plugin_manager = get_parser_options_plugins(args=api_args)

    api.check_options(options, plugin_manager)
    return api.run_pipeline_cli(options, plugin_manager=plugin_manager)


def run_ocrmypdf(
    input_file: Path, output_file: Path, *args, text: bool = True
) -> CompletedProcess:
           
    p_args = (
        [sys.executable, '-m', 'ocrmypdf']
        + [str(arg) for arg in args if arg is not None]
        + [str(input_file), str(output_file)]
    )

    p = run(
        p_args,
        capture_output=True,
        text=text,
        check=False,
    )
                     
    return p


def first_page_dimensions(pdf: Path):
    info = pdfinfo.PdfInfo(pdf)
    page0 = info[0]
    return (page0.width_inches, page0.height_inches)


def pytest_addoption(parser):
    parser.addoption(
        "--runslow",
        action="store_true",
        default=False,
        help=(
            "run slow tests only useful for development (unlikely to be "
            "useful for downstream packagers)"
        ),
    )


def pytest_collection_modifyitems(config, items):
    if config.getoption("--runslow"):
                                                        
        return
    skip_slow = pytest.mark.skip(reason="need --runslow option to run")
    for item in items:
        if "slow" in item.keywords:
            item.add_marker(skip_slow)
