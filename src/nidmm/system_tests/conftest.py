import pytest


def pytest_addoption(parser):
    parser.addoption("--name", action="store", default="Dev1", help="Device name for opening a session.")


@pytest.fixture
def name(request):
    return request.config.getoption("--name")

