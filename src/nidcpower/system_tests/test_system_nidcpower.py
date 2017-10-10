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
    # Testing a private function, as there is no way to natively get to this function on a simulated session.
    message = session._error_message(-1074135027)
    assert message.find('Attribute is read-only.') != -1


def test_get_error(session):
    try:
        session.instrument_model = 'Potato'
        assert False
    except nidcpower.Error as e:
        assert e.code == -1074135027  # Error : Attribute is read-only.
        assert e.description.find('Attribute is read-only.') != -1


'''
TODO: (Jaleel) Dependent on PR#439 and Issue $428,#371 : Error -1074134972  (Hex 0xBFFA0044) Channel or or repeated capability name required
def test_config_aperture_time(session):
    session.configure_aperture_time(2, nidcpower.ApertureTimeUnits.POWER_LINE_CYCLES)
    session.configure_aperture_time(0.01666, nidcpower.ApertureTimeUnits.SECONDS)
    assert session.aperture_time_units == nidcpower.ApertureTimeUnits.SECONDS
    assert session.aperture_time == 0.01666


TODO: (Jaleel) Dependent on PR#439 and Issue $428,#371 : Error -1074134972  (Hex 0xBFFA0044) Channel or or repeated capability name required
def test_fetch_multiple(session):
    session.source_mode = nidcpower.SourceMode.SINGLE_POINT
    session.configure_aperture_time(0, nidcpower.ApertureTimeUnits.SECONDS)
    session.voltage_level = 1
    count = 10
    session.measure_when = nidcpower.MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE
    with session.initiate():
        voltage_measurements, current_measurements, in_compliance, actual_count = session.fetch_multiple(-1, count)
        assert len(voltage_measurements) == count
        assert len(current_measurements) == count
        assert len(in_compliance) == count
        assert actual_count == count
        assert isinstance(voltage_measurement[1], float)
        assert isinstance(current_measurements[1], float)
        assert in_compliance[1] in [True, False]


TODO:(Jaleel) Check after #444 fixed
def test_measure_multiple(session):
    session.source_mode = nidcpower.SourceMode.SINGLE_POINT
    session.configure_aperture_time(0, nidcpower.ApertureTimeUnits.SECONDS)
    #session.voltage_level = 1
    count = 10
    session.measure_when = nidcpower.MeasureWhen.ON_DEMAND
    with session.initiate():
        voltage_measurements, current_measurements = session.measure_multiple()
    assert len(voltage_measurements) == 4   # measuremultiple will return a reading for all channel , since 4143 has 4 channel expecting 4 readings
    assert len(current_measurements) == 4
    assert isinstance(voltage_measurement[1], float)
    assert isinstance(current_measurements[1], float)


TODO: (Jaleel) Following tests need to be validated once issue $428,#371 fixed : Error -1074134972  (Hex 0xBFFA0044) Channel or or repeated capability name required
def test_measure(session):
    session.source_mode = nidcpower.SourceMode.SINGLE_POINT
    session.output_function = nidcpower.OutputFunction.DC_VOLTAGE
    session.voltage_level_range = 6
    session.voltage_level = 2
    with session.initiate():
        reading = session.measure(1) ## enum missing from enum.py. Shouldn't be an enum ?
    assert session.query_in_compliance(1) is False
    assert reading == 2


def test_query_max_current_limit(session):
    max_current_limit = session.query_max_current_limit(6)
    assert max_current_limit == 0.150000  # for a simulated 4143 max current limit should be 0.150000 for 6V Voltage level


def test_query_max_voltage_level(session):
    max_voltage_level = session.query_max_voltage_level(0.03)
    assert max_voltage_level == 24  # for a simulated 4143 max voltage level should be 24V for 30mA current limit


def test_query_min_current_limit(session):
    min_current_limit = session.query_min_current_limit(0.03)
    assert min_current_limit ==  0.0000001  # for a simulated 4143 min_current_limit should be 1uA for 6V voltage level


def test_query_output_state(session):
    with session.initiate():
        assert session.query_output_state(0) is True   # since default function is DCVolt when initiated output state for DC Volt\DC current should be True and False respectively
        assert session.query_output_state(1) is False
'''
