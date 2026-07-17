import time


def pytest_sessionfinish(session, exitstatus):
    time.sleep(5)