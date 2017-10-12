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


def test_get_channel_name(session):
    name = session.get_channel_name(1)
    assert name == '0'


def test_get_attribute_string(session):
    model = session.instrument_model
    assert model == 'NI PXIe-4143'


def test_error_message(session):
    # Calling the private function directly, as _get_error_message() only gets called when you have an invalid session,
    # and there is no good way for us to invalidate a simulated session.
    message = session._error_message(-1074135027)
    assert message.find('Attribute is read-only.') != -1


def test_get_error(session):
    try:
        session.instrument_model = 'Potato'
        assert False
    except nidcpower.Error as e:
        assert e.code == -1074135027  # Error : Attribute is read-only.
        assert e.description.find('Attribute is read-only.') != -1


def test_commit_after_initiate(session):
    try:
        with session.initiate():
            session.commit()
    except nidcpower.Error as e:
        assert False


def test_get_self_cal_last_date_and_time(session):
    try:
        session.get_self_cal_last_date_and_time()
        assert False
    except nidcpower.Error as e:
        assert e.code == -1074118643  # This operation is invalid on a simulated device.


def test_get_self_cal_last_temp(session):
    try:
        session.get_self_cal_last_temp()
        assert False
    except nidcpower.Error as e:
        assert e.code == -1074118643  # This operation is invalid on a simulated device.


def test_read_current_temperature(session):
    try:
        session.read_current_temperature()
        assert False
    except nidcpower.Error as e:
        assert e.code == -1074118643  # This operation is invalid on a simulated device.


def test_reset_device(session):
    channel = session['0']
    default_output_function = channel.output_function
    assert default_output_function == nidcpower.OutputFunction.DC_VOLTAGE
    channel.output_function = nidcpower.OutputFunction.DC_CURRENT
    session.reset_device()
    function_after_reset = channel.output_function
    assert function_after_reset == default_output_function


def test_reset_with_default(session):
    channel = session['0']
    assert channel.aperture_time_units == nidcpower.ApertureTimeUnits.SECONDS
    channel.aperture_time_units == nidcpower.ApertureTimeUnits.POWER_LINE_CYCLES
    session.reset_with_defaults()
    assert channel.aperture_time_units == nidcpower.ApertureTimeUnits.SECONDS


def test_reset(session):
    channel = session['0']
    assert channel.output_enabled is True
    channel.output_enabled = False
    session.reset()
    assert channel.output_enabled is True


def test_disable(session):
    channel = session['0']
    assert channel.output_enabled is True
    session.disable()
    assert channel.output_enabled is False
