import niscope
import pytest


@pytest.fixture(scope='function')
def session():
    with niscope.Session('FakeDevice', False, True, 'Simulate=1, DriverSetup=Model:5164; BoardType:PXIe') as simulated_session:
        yield simulated_session


# Basic usability tests
def test_load_session(session):
    pass
