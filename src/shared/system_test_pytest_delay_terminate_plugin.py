import time


def pytest_sessionfinish(session, exitstatus):
    # Work around a race condition that can cause a crash during process termination.
    time.sleep(5)