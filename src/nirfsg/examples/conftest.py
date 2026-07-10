import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent / 'shared'))
import system_test_utilities  # noqa: E402

_session_exitstatus = {}


def pytest_sessionfinish(session, exitstatus):
    '''Capture the pytest result code for use during unconfigure.'''
    _session_exitstatus['code'] = int(exitstatus)


def pytest_unconfigure(config):
    '''Hard-exit after all reporting is done to skip the py3.10 native abort.'''
    system_test_utilities.finalize_test_process(_session_exitstatus.get('code', 0))
