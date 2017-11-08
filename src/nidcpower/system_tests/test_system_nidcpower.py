import nidcpower
import pytest


@pytest.fixture(scope='function')
def session():
    with nidcpower.Session('', '', False, 'Simulate=1, DriverSetup=Model:4162; BoardType:PXIe') as simulated_session:
        yield simulated_session


def test_self_test():
    # TODO(frank): self_test does not work with simulated PXIe-4162 modules due to internal NI bug.
    # Update to use the session created with 'session' function above after internal NI bug is fixed.
    with nidcpower.Session('', '', False, 'Simulate=1, DriverSetup=Model:4143; BoardType:PXIe') as session:
        result, message = session.self_test()
        assert result == 0
        assert message == 'Self test passed'


def test_get_channel_name(session):
    name = session.get_channel_name(1)
    assert name == '0'


def test_get_attribute_string(session):
    model = session.instrument_model
    assert model == 'NI PXIe-4162'


def test_error_message(session):
    # Calling the private function directly, as _get_error_message() only gets called when you have an invalid session,
    # and there is no good way for us to invalidate a simulated session.
    message = session._error_message(-1074135027)
    assert message.find('Attribute is read-only.') != -1


def test_get_error(session):
    try:
        session.instrument_model = ''
        assert False
    except nidcpower.Error as e:
        assert e.code == -1074135027  # Error : Attribute is read-only.
        assert e.description.find('Attribute is read-only.') != -1


def test_get_self_cal_last_date_and_time(session):
    year, month, day, hour, minute = session.get_self_cal_last_date_and_time()
    assert year == 1940
    assert month == 3
    assert day == 1
    assert hour == 0
    assert minute == 0


def test_get_self_cal_last_temp(session):
    temperature = session.get_self_cal_last_temp()
    assert temperature == 25.0


def test_read_current_temperature(session):
    temperature = session.read_current_temperature()
    assert temperature == 25.0


def test_reset_device():
    # TODO(frank): reset_device does not work with simulated PXIe-4162 modules due to internal NI bug.
    # Update to use the session created with 'session' function above after internal NI bug is fixed.
    with nidcpower.Session('', '', False, 'Simulate=1, DriverSetup=Model:4143; BoardType:PXIe') as session:
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


def test_measure():
    with nidcpower.Session('', '0', False, 'Simulate=1, DriverSetup=Model:4162; BoardType:PXIe') as session:
        session.source_mode = nidcpower.SourceMode.SINGLE_POINT
        session.output_function = nidcpower.OutputFunction.DC_VOLTAGE
        session.voltage_level_range = 6
        session.voltage_level = 2
        with session.initiate():
            reading = session.measure(nidcpower.MeasurementTypes.MEASURE_VOLTAGE)
            assert session.query_in_compliance() is False
        assert reading == 2


def test_query_output_state():
    with nidcpower.Session('', '0', False, 'Simulate=1, DriverSetup=Model:4162; BoardType:PXIe') as session:
        with session.initiate():
            assert session.query_output_state(nidcpower.OutputStates.OUTPUT_CONSTANT_VOLTAGE) is True   # since default function is DCVolt when initiated output state for DC Volt\DC current should be True and False respectively
            assert session.query_output_state(nidcpower.OutputStates.OUTPUT_CONSTANT_CURRENT) is False


def test_config_aperture_time():
    with nidcpower.Session('', '0', False, 'Simulate=1, DriverSetup=Model:4162; BoardType:PXIe') as session:
        expected_default_aperture_time = 0.01666
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


def test_fetch_multiple():
    with nidcpower.Session('', '0', False, 'Simulate=1, DriverSetup=Model:4162; BoardType:PXIe') as session:
        session.source_mode = nidcpower.SourceMode.SINGLE_POINT
        session.configure_aperture_time(0, nidcpower.ApertureTimeUnits.SECONDS)
        session.voltage_level = 1
        count = 10
        session.measure_when = nidcpower.MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE
        with session.initiate():
            voltage_measurements, current_measurements, in_compliance, actual_count = session.fetch_multiple(count)
            assert len(voltage_measurements) == count
            assert len(current_measurements) == count
            assert len(in_compliance) == count
            assert actual_count == count
            assert isinstance(voltage_measurements[1], float)
            assert isinstance(current_measurements[1], float)
            assert in_compliance[1] in [True, False]
            assert voltage_measurements[1] == 1.0
            assert current_measurements[1] == 0.00001


'''
TODO: (Jaleel) Python Crashes when running these examples : Issue#444
def test_measure_multiple(session):
    session.source_mode = nidcpower.SourceMode.SINGLE_POINT
    session.configure_aperture_time(0, nidcpower.ApertureTimeUnits.SECONDS)
    #session.voltage_level = 1
    count = 10
    session.measure_when = nidcpower.MeasureWhen.ON_DEMAND
    with session.initiate():
        voltage_measurements, current_measurements = session.measure_multiple()
    assert len(voltage_measurements) == 4   # measuremultiple will return a reading for all channel , since 4162 has 4 channel expecting 4 readings
    assert len(current_measurements) == 4
    assert isinstance(voltage_measurements[1], float)
    assert isinstance(current_measurements[1], float)
'''


def test_query_max_current_limit():
    with nidcpower.Session('', '0', False, 'Simulate=1, DriverSetup=Model:4162; BoardType:PXIe') as session:
        max_current_limit = session.query_max_current_limit(6)
        expected_max_current_limit = 0.06  # for a simulated 4162 max current limit should be 0.06 for 6V Voltage level
        max_current_limit_in_range = abs(max_current_limit - expected_max_current_limit) <= max(1e-09 * max(abs(max_current_limit), abs(expected_max_current_limit)), 0.0)  # https://stackoverflow.com/questions/5595425/what-is-the-best-way-to-compare-floats-for-almost-equality-in-python
        assert max_current_limit_in_range is True


def test_query_max_voltage_level():
    with nidcpower.Session('', '0', False, 'Simulate=1, DriverSetup=Model:4162; BoardType:PXIe') as session:
        max_voltage_level = session.query_max_voltage_level(0.03)
        expected_max_voltage_level = 24  # for a simulated 4162 max voltage level should be 24V for 30mA current limit
        max_voltage_level_in_range = abs(max_voltage_level - expected_max_voltage_level) <= max(1e-09 * max(abs(max_voltage_level), abs(expected_max_voltage_level)), 0.0)  # https://stackoverflow.com/questions/5595425/what-is-the-best-way-to-compare-floats-for-almost-equality-in-python
        assert max_voltage_level_in_range is True


def test_query_min_current_limit():
    with nidcpower.Session('', '0', False, 'Simulate=1, DriverSetup=Model:4162; BoardType:PXIe') as session:
        min_current_limit = session.query_min_current_limit(0.03)
        expected_min_current_limit = 0.0000001  # for a simulated 4162 min_current_limit should be 1uA for 6V voltage level
        min_current_limit_in_range = abs(min_current_limit - expected_min_current_limit) <= max(1e-09 * max(abs(min_current_limit), abs(expected_min_current_limit)), 0.0)  # https://stackoverflow.com/questions/5595425/what-is-the-best-way-to-compare-floats-for-almost-equality-in-python
        assert min_current_limit_in_range is True


def test_create_advanced_sequence():
    with nidcpower.Session('', '0', False, 'Simulate=1, DriverSetup=Model:4162; BoardType:PXIe') as session:
        ids = [1150008, 1250001, 1150009]  # work around #507
        session.create_advanced_sequence(sequence_name='my_sequence', attribute_ids=ids, set_as_active_sequence=True)


# TODO(marcoskirsch): Doesn't work, issue #515
'''
def test_set_sequence_default_source_delays():
    with nidcpower.Session('', '0', False, 'Simulate=1, DriverSetup=Model:4162; BoardType:PXIe') as session:
        session.set_sequence([0.1, 0.2, 0.3])
'''


# TODO(marcoskirsch): Should raise because arrays are different size, or maybe treat [] same as None? See issue #515
'''
def test_set_sequence_no_source_delays():
    with nidcpower.Session('', '0', False, 'Simulate=1, DriverSetup=Model:4162; BoardType:PXIe') as session:
        session.set_sequence([0.1, 0.2, 0.3], [])
'''


def test_set_sequence_with_source_delays():
    with nidcpower.Session('', '0', False, 'Simulate=1, DriverSetup=Model:4162; BoardType:PXIe') as session:
        session.set_sequence([0.1, 0.2, 0.3], [0.001, 0.002, 0.003])


# TODO(marcoskirsch): Should raise because arrays are different size. See issue #515
def test_set_sequence_with_too_many_source_delays():
    with nidcpower.Session('', '0', False, 'Simulate=1, DriverSetup=Model:4162; BoardType:PXIe') as session:
        session.set_sequence([0.1, 0.2, 0.3], [0.001, 0.002, 0.003, 0.004])


# TODO(marcoskirsch): Should raise because arrays are different size. See issue #515
def test_set_sequence_with_too_few_source_delays():
    with nidcpower.Session('', '0', False, 'Simulate=1, DriverSetup=Model:4162; BoardType:PXIe') as session:
        session.set_sequence([0.1, 0.2, 0.3, 0.4], [0.001, 0.002, 0.003, 0.004])


def test_wait_for_event_default_timeout():
    with nidcpower.Session('', '0', False, 'Simulate=1, DriverSetup=Model:4162; BoardType:PXIe') as session:
        with session.initiate():
            session.wait_for_event(nidcpower.Event.SOURCE_COMPLETE)


def test_wait_for_event_with_timeout():
    with nidcpower.Session('', '0', False, 'Simulate=1, DriverSetup=Model:4162; BoardType:PXIe') as session:
        with session.initiate():
            session.wait_for_event(nidcpower.Event.SOURCE_COMPLETE, 0.5)


def test_wait_for_event_with_timeout():
    pass
