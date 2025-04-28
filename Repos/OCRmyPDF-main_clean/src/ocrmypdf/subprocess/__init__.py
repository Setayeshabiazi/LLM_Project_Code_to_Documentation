                                              
                                  
"""Wrappers to manage subprocess calls."""

from __future__ import annotations

import logging
import os
import re
import sys
from collections.abc import Callable, Mapping, Sequence
from contextlib import suppress
from pathlib import Path
from subprocess import PIPE, STDOUT, CalledProcessError, CompletedProcess, Popen
from subprocess import run as subprocess_run

from packaging.version import Version

from ocrmypdf.exceptions import MissingDependencyError

                                              

log = logging.getLogger(__name__)

Args = Sequence[Path | str]
OsEnviron = os._Environ                                    


def run(
    args: Args,
    *,
    env: OsEnviron | None = None,
    logs_errors_to_stdout: bool = False,
    check: bool = False,
    **kwargs,
) -> CompletedProcess:
           
    args, env, process_log, _text = _fix_process_args(args, env, kwargs)

    stderr = None
    stderr_name = 'stderr' if not logs_errors_to_stdout else 'stdout'
    try:
        proc = subprocess_run(args, env=env, check=check, **kwargs)
    except CalledProcessError as e:
        stderr = getattr(e, stderr_name, None)
        raise
    else:
        stderr = getattr(proc, stderr_name, None)
    finally:
        if process_log.isEnabledFor(logging.DEBUG) and stderr:
            with suppress(AttributeError, UnicodeDecodeError):
                stderr = stderr.decode('utf-8', 'replace')
            if logs_errors_to_stdout:
                process_log.debug("stdout/stderr = %s", stderr)
            else:
                process_log.debug("stderr = %s", stderr)
    return proc


def run_polling_stderr(
    args: Args,
    *,
    callback: Callable[[str], None],
    check: bool = False,
    env: OsEnviron | None = None,
    **kwargs,
) -> CompletedProcess:
           
    args, env, process_log, text = _fix_process_args(args, env, kwargs)
    assert text, "Must use text=True"

    with Popen(args, env=env, **kwargs) as proc:
        lines = []
        while proc.poll() is None:
            if proc.stderr is None:
                continue
            for msg in iter(proc.stderr.readline, ''):
                if process_log.isEnabledFor(logging.DEBUG):
                    process_log.debug(msg.strip())
                callback(msg)
                lines.append(msg)
        stderr = ''.join(lines)

        if check and proc.returncode != 0:
            raise CalledProcessError(proc.returncode, args, output=None, stderr=stderr)
        return CompletedProcess(args, proc.returncode, None, stderr=stderr)


def _fix_process_args(
    args: Args, env: OsEnviron | None, kwargs
) -> tuple[Args, OsEnviron, logging.Logger, bool]:
    if not env:
        env = os.environ

                                       
    program = str(args[0])

    if sys.platform == 'win32':
                                                 
        from ocrmypdf.subprocess._windows import fix_windows_args

        args = fix_windows_args(program, args, env)

    log.debug("Running: %s", args)
    process_log = log.getChild(os.path.basename(program))
    text = bool(kwargs.get('text', False))

    return args, env, process_log, text


def get_version(
    program: str,
    *,
    version_arg: str = '--version',
    regex=r'(\d+(\.\d+)*)',
    env: OsEnviron | None = None,
) -> str:
           
    args_prog = [program, version_arg]
    try:
        proc = run(
            args_prog,
            close_fds=True,
            text=True,
            stdout=PIPE,
            stderr=STDOUT,
            check=True,
            env=env,
        )
        output: str = proc.stdout
    except FileNotFoundError as e:
        raise MissingDependencyError(
            f"Could not find program '{program}' on the PATH"
        ) from e
    except CalledProcessError as e:
        if e.returncode != 0:
            log.exception(e)
            raise MissingDependencyError(
                f"Ran program '{program}' but it exited with an error:\n{e.output}"
            ) from e
        raise MissingDependencyError(
            f"Could not find program '{program}' on the PATH"
        ) from e

    match = re.match(regex, output.strip())
    if not match:
        raise MissingDependencyError(
            f"The program '{program}' did not report its version. "
            f"Message was:\n{output}"
        )
    version = match.group(1)

    return version


MISSING_PROGRAM = '''
The program '{program}' could not be executed or was not found on your
system PATH.
'''

MISSING_OPTIONAL_PROGRAM = '''
The program '{program}' could not be executed or was not found on your
system PATH.  This program is required when you use the
{required_for} arguments.  You could try omitting these arguments, or install
the package.
'''

MISSING_RECOMMEND_PROGRAM = '''
The program '{program}' could not be executed or was not found on your
system PATH.  This program is recommended when using the {required_for} arguments,
but not required, so we will proceed.  For best results, install the program.
'''

OLD_VERSION = '''
OCRmyPDF requires '{program}' {need_version} or higher.  Your system appears
to have {found_version}.  Please update this program.
'''

OLD_VERSION_REQUIRED_FOR = '''
OCRmyPDF requires '{program}' {need_version} or higher when run with the
{required_for} arguments.  {program} {found_version} is installed.

If you omit these arguments, OCRmyPDF may be able to
proceed.  For best results, update the program.
'''

OSX_INSTALL_ADVICE = '''
If you have homebrew installed, try these command to install the missing
package:
    brew install {package}
'''

LINUX_INSTALL_ADVICE = '''
On systems with the aptitude package manager (Debian, Ubuntu), try these
commands:
    sudo apt update
    sudo apt install {package}

On RPM-based systems (Red Hat, Fedora), try this command:
    sudo dnf install {package}
'''

WINDOWS_INSTALL_ADVICE = '''
If not already installed, install the Chocolatey package manager. Then use
a command prompt to install the missing package:
    choco install {package}
'''


def _get_platform() -> str:
    if sys.platform.startswith('freebsd'):
        return 'freebsd'
    elif sys.platform.startswith('linux'):
        return 'linux'
    elif sys.platform.startswith('win'):
        return 'windows'
    return sys.platform


def _error_trailer(program: str, package: str | Mapping[str, str], **kwargs) -> None:
    del kwargs
    if isinstance(package, Mapping):
        package = package.get(_get_platform(), program)

    if _get_platform() == 'darwin':
        log.info(OSX_INSTALL_ADVICE.format(**locals()))
    elif _get_platform() == 'linux':
        log.info(LINUX_INSTALL_ADVICE.format(**locals()))
    elif _get_platform() == 'windows':
        log.info(WINDOWS_INSTALL_ADVICE.format(**locals()))


def _error_missing_program(
    program: str, package: str, required_for: str | None, recommended: bool
) -> None:
                                     
    if recommended:
        log.warning(MISSING_RECOMMEND_PROGRAM.format(**locals()))
    elif required_for:
        log.error(MISSING_OPTIONAL_PROGRAM.format(**locals()))
    else:
        log.error(MISSING_PROGRAM.format(**locals()))
    _error_trailer(**locals())


def _error_old_version(
    program: str,
    package: str,
    need_version: str,
    found_version: str,
    required_for: str | None,
) -> None:
                                     
    if required_for:
        log.error(OLD_VERSION_REQUIRED_FOR.format(**locals()))
    else:
        log.error(OLD_VERSION.format(**locals()))
    _error_trailer(**locals())


def check_external_program(
    *,
    program: str,
    package: str,
    version_checker: Callable[[], Version],
    need_version: str | Version,
    required_for: str | None = None,
    recommended: bool = False,
    version_parser: type[Version] = Version,
) -> None:
           
    if not isinstance(need_version, Version):
        need_version = version_parser(need_version)
    try:
        found_version = version_checker()
    except (CalledProcessError, FileNotFoundError) as e:
        _error_missing_program(program, package, required_for, recommended)
        if not recommended:
            raise MissingDependencyError(program) from e
        return
    except MissingDependencyError:
        _error_missing_program(program, package, required_for, recommended)
        if not recommended:
            raise
        return

    if found_version and found_version < need_version:
        _error_old_version(
            program, package, str(need_version), str(found_version), required_for
        )
        if not recommended:
            raise MissingDependencyError(program)

    log.debug('Found %s %s', program, found_version)
