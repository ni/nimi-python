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


def test_measure(session):
    with nidcpower.Session('FakeDevice', '0', False, 'Simulate=1, DriverSetup=Model:4143; BoardType:PXIe') as session:
        session.source_mode = nidcpower.SourceMode.SINGLE_POINT
        session.output_function = nidcpower.OutputFunction.DC_VOLTAGE
        session.voltage_level_range = 6
        session.voltage_level = 2
        with session.initiate():
            reading = session.measure(nidcpower.MeasurementTypes.MEASURE_VOLTAGE)
            assert session.query_in_compliance() is False
        assert reading == 2


def test_query_output_state(session):
    with nidcpower.Session('FakeDevice', '0', False, 'Simulate=1, DriverSetup=Model:4143; BoardType:PXIe') as session:
        with session.initiate():
            assert session.query_output_state(nidcpower.OutputStates.OUTPUT_CONSTANT_VOLTAGE) is True   # since default function is DCVolt when initiated output state for DC Volt\DC current should be True and False respectively
            assert session.query_output_state(nidcpower.OutputStates.OUTPUT_CONSTANT_CURRENT) is False
