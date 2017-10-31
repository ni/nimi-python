import nifgen
import pytest


@pytest.fixture(scope='function')
def session():
    with nifgen.Session('', False, 'Simulate=1, DriverSetup=Model:5433 (2CH);BoardType:PXIe') as simulated_session:
        yield simulated_session


def test_self_test(session):
    result, message = session.self_test()
    assert result == 0
    assert message == 'Self test passed'


def test_get_attribute_string(session):
    model = session.instrument_model
    assert model == 'NI PXIe-5433 (2CH)'


def test_error_message(session):
    # Calling the private function directly, as _get_error_message() only gets called when you have an invalid session,
    # and there is no good way for us to invalidate a simulated session.
    message = session._error_message(-1074135027)
    assert message.find('Attribute is read-only.') != -1


def test_get_error(session):
    try:
        session.instrument_model = ''
        assert False
    except nifgen.Error as e:
        assert e.code == -1074135027  # Error : Attribute is read-only.
        assert e.description.find('Attribute is read-only.') != -1


def test_method_get_self_cal_supported(session):
    assert session.get_self_cal_supported() in [True, False]


def test_get_self_cal_last_date_and_time():
    try:
        with nifgen.Session('', False, 'Simulate=1, DriverSetup=Model:5421;BoardType:PXI') as session:
            year, month, day, hour, minute = session.get_self_cal_last_date_and_time()
            assert False
    except nifgen.Error as e:
        assert e.code == -1074118632  # This operation is not supported for simulated device


def test_self_cal(session):
        session.self_cal()
