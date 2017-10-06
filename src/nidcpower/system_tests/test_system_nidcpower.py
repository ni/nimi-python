import nidcpower
import pytest


@pytest.fixture(scope='function')
def session():
    with nidcpower.Session('FakeDevice', '', False, 'Simulate=1, DriverSetup=Model:4143; BoardType:PXIe') as simulated_session:
        yield simulated_session


def test_self_test(session):
    result, message = session.self_test()
    assert result == 0
    assert message == 'Self test passed'


def test_revision_query(session):
    driver_revision, firmware_revision = session.revision_query()
    assert driver_revision == '17.1.0'
    assert firmware_revision == 'Not Available'


def test_get_channel_name(session):
    name = session.get_channel_name(1)
    assert name == '0'


def test_get_attribute_string(session):
    model = session.instrument_model
    assert model == 'NI PXIe-4143'


def test_error_message(session):
    # Testing a private function, as there is no way to natively get to this function on a simulated session.
    message = session._error_message(-1074135027)
    assert message == 'IVI:  (Hex 0xBFFA000D) Attribute is read-only.'


def test_get_error(session):
    try:
        session.instrument_model = 'Potato'
        assert False
    except nidcpower.Error as e:
        assert e.code == -1074135027  # Error : Attribute is read-only.
        assert e.description == 'IVI:  (Hex 0xBFFA000D) Attribute is read-only.\n\nAttribute: IVI_ATTR_INSTRUMENT_MODEL'
