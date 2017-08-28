import pytest


def pytest_addoption(parser):
   parser.addoption("--family", action="store", default="nidmm", help="Device family name for opening an NI-ModInst session.")

@pytest.fixture
def family(request):
    return request.config.getoption("--family")

