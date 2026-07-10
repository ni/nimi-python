import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent / 'shared'))
import system_test_utilities  # noqa: E402


def pytest_configure(config):
    '''Enable fatal-signal tracebacks for the nirfsg examples process.'''
    system_test_utilities.enable_native_teardown_diagnostics()


def pytest_sessionfinish(session, exitstatus):
    '''Force a deterministic teardown once the nirfsg examples finish.'''
    system_test_utilities.finalize_test_process(exitstatus)
