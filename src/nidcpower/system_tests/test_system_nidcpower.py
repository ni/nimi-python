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


def test_config_aperture_time(session):
    with nidcpower.Session('FakeDevice', '0', False, 'Simulate=1, DriverSetup=Model:4143; BoardType:PXIe') as session:
        expected_default_aperture_time = 0.016666666666666666
        default_aperture_time = session.aperture_time
        assert session.aperture_time_units == nidcpower.ApertureTimeUnits.SECONDS
        default_aperture_time_in_range = abs(default_aperture_time - expected_default_aperture_time) <= max(1e-09 * max(abs(default_aperture_time), abs(expected_default_aperture_time)), 0.0)  # https://stackoverflow.com/questions/5595425/what-is-the-best-way-to-compare-floats-for-almost-equality-in-python
        assert default_aperture_time_in_range is True
        session.configure_aperture_time(5, nidcpower.ApertureTimeUnits.POWER_LINE_CYCLES)
        assert session.aperture_time_units == nidcpower.ApertureTimeUnits.POWER_LINE_CYCLES
        aperture_time = session.aperture_time
        expected_aperture_time = 5
        aperture_time_in_range = abs(aperture_time - expected_aperture_time) <= max(1e-09 * max(abs(aperture_time), abs(expected_aperture_time)), 0.0)  # https://stackoverflow.com/questions/5595425/what-is-the-best-way-to-compare-floats-for-almost-equality-in-python
        assert aperture_time_in_range is True


'''
TODO: (Jaleel) Python Crashes when running these examples : Issue#444,445
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
'''


def test_query_max_current_limit(session):
    with nidcpower.Session('FakeDevice', '0', False, 'Simulate=1, DriverSetup=Model:4143; BoardType:PXIe') as session:
        max_current_limit = session.query_max_current_limit(6)
        expected_max_current_limit = 0.150000  # for a simulated 4143 max current limit should be 0.150000 for 6V Voltage level
        max_current_limit_in_range = abs(max_current_limit - expected_max_current_limit) <= max(1e-09 * max(abs(max_current_limit), abs(expected_max_current_limit)), 0.0)  # https://stackoverflow.com/questions/5595425/what-is-the-best-way-to-compare-floats-for-almost-equality-in-python
        assert max_current_limit_in_range is True


def test_query_max_voltage_level(session):
    with nidcpower.Session('FakeDevice', '0', False, 'Simulate=1, DriverSetup=Model:4143; BoardType:PXIe') as session:
        max_voltage_level = session.query_max_voltage_level(0.03)
        expected_max_voltage_level = 24  # for a simulated 4143 max voltage level should be 24V for 30mA current limit
        max_voltage_level_in_range = abs(max_voltage_level - expected_max_voltage_level) <= max(1e-09 * max(abs(max_voltage_level), abs(expected_max_voltage_level)), 0.0)  # https://stackoverflow.com/questions/5595425/what-is-the-best-way-to-compare-floats-for-almost-equality-in-python
        assert max_voltage_level_in_range is True


def test_query_min_current_limit(session):
    with nidcpower.Session('FakeDevice', '0', False, 'Simulate=1, DriverSetup=Model:4143; BoardType:PXIe') as session:
        min_current_limit = session.query_min_current_limit(0.03)
        expected_min_current_limit = 0.0000001  # for a simulated 4143 min_current_limit should be 1uA for 6V voltage level
        min_current_limit_in_range = abs(min_current_limit - expected_min_current_limit) <= max(1e-09 * max(abs(min_current_limit), abs(expected_min_current_limit)), 0.0)  # https://stackoverflow.com/questions/5595425/what-is-the-best-way-to-compare-floats-for-almost-equality-in-python
        assert min_current_limit_in_range is True
