import nidcpower
import pytest


@pytest.fixture(scope='function')
def session():
    with nidcpower.Session('FakeDevice', False, True, 'Simulate=1, DriverSetup=Model:4143; BoardType:PXIe') as simulated_session:
        yield simulated_session


def test_need_to_write_all():
    pass
