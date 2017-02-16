import asyncio
import json

from .errors import HassbianError


CMD = ['sudo', 'hassbian-config']


@asyncio.coroutine
def _run_command(action, *, loop):
    process = yield from asyncio.create_subprocess_exec(
        *CMD, *action,
        loop=loop,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.DEVNULL
    )
    stdout, _ = yield from process.communicate()
    return str(stdout, 'utf-8')


@asyncio.coroutine
def get_status(*, loop=None):
    """Get status."""
    if loop is None:
        loop = asyncio.get_event_loop()

    response = yield from _run_command(['status'], loop=loop)
    try:
        return json.loads(response)
    except ValueError:
        raise HassbianError('Unable to parse JSON')


def install_suite(suite, *, loop=None):
    """Install a suite."""
    if loop is None:
        loop = asyncio.get_event_loop()

    return _run_command(['install'], loop=loop)
