import datetime
import nidcpower
import pytest


@pytest.fixture(scope='function')
def session():
    with nidcpower.Session('4162', '', False, 'Simulate=1, DriverSetup=Model:4162; BoardType:PXIe') as simulated_session:
        yield simulated_session


@pytest.fixture(scope='function')
def single_channel_session():
    with nidcpower.Session('4162', '0', False, 'Simulate=1, DriverSetup=Model:4162; BoardType:PXIe') as simulated_session:
        yield simulated_session


@pytest.fixture(scope='function')
def multiple_channel_session():
    with nidcpower.Session('4162', [0, 1], False, 'Simulate=1, DriverSetup=Model:4162; BoardType:PXIe') as simulated_session:
        yield simulated_session


def test_self_test():
    # TODO(frank): self_test does not work with simulated PXIe-4162 modules due to internal NI bug.
    # Update to use the session created with 'session' function above after internal NI bug is fixed.
    with nidcpower.Session('', '', False, 'Simulate=1, DriverSetup=Model:4143; BoardType:PXIe') as session:
        # We should not get an assert if self_test passes
        session.self_test()


def test_self_cal(session):
    session.self_cal()


def test_get_channel_name(session):
    name = session.get_channel_name(1)
    assert name == '0'


def test_get_attribute_string(session):
    model = session.instrument_model
    assert model == 'NI PXIe-4162'


def test_error_message():
    try:
        # We pass in an invalid model name to force going to error_message
        with nidcpower.Session('4162', [0, 1], False, 'Simulate=1, DriverSetup=Model:invalid_model; BoardType:PXIe'):
            assert False
    except nidcpower.Error as e:
        assert e.code == -1074134964
        assert e.description.find('The option string parameter contains an entry with an unknown option value.') != -1


def test_get_error(session):
    try:
        session.instrument_model = ''
        assert False
    except nidcpower.Error as e:
        assert e.code == -1074135027  # Error : Attribute is read-only.
        assert e.description.find('Attribute is read-only.') != -1


def test_get_self_cal_last_date_and_time(session):
    last_cal = session.get_self_cal_last_date_and_time()
    assert last_cal.year == 1940
    assert last_cal.month == 3
    assert last_cal.day == 1
    assert last_cal.hour == 0
    assert last_cal.minute == 0


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
        channel = session.channels['0']
        default_output_function = channel.output_function
        assert default_output_function == nidcpower.OutputFunction.DC_VOLTAGE
        channel.output_function = nidcpower.OutputFunction.DC_CURRENT
        session.reset_device()
        function_after_reset = channel.output_function
        assert function_after_reset == default_output_function


def test_reset_with_default(session):
    channel = session.channels['0']
    assert channel.aperture_time_units == nidcpower.ApertureTimeUnits.SECONDS
    channel.aperture_time_units == nidcpower.ApertureTimeUnits.POWER_LINE_CYCLES
    session.reset_with_defaults()
    assert channel.aperture_time_units == nidcpower.ApertureTimeUnits.SECONDS


def test_reset(session):
    channel = session.channels['0']
    assert channel.output_enabled is True
    channel.output_enabled = False
    session.reset()
    assert channel.output_enabled is True


def test_disable(session):
    channel = session.channels['0']
    assert channel.output_enabled is True
    session.disable()
    assert channel.output_enabled is False


def test_measure(single_channel_session):
    single_channel_session.source_mode = nidcpower.SourceMode.SINGLE_POINT
    single_channel_session.output_function = nidcpower.OutputFunction.DC_VOLTAGE
    single_channel_session.voltage_level_range = 6
    single_channel_session.voltage_level = 2
    with single_channel_session.initiate():
        reading = single_channel_session.measure(nidcpower.MeasurementTypes.VOLTAGE)
        assert single_channel_session.query_in_compliance() is False
    assert reading == 2


def test_query_output_state(single_channel_session):
    with single_channel_session.initiate():
        assert single_channel_session.query_output_state(nidcpower.OutputStates.VOLTAGE) is True   # since default function is DCVolt when initiated output state for DC Volt\DC current should be True and False respectively
        assert single_channel_session.query_output_state(nidcpower.OutputStates.CURRENT) is False


def test_config_aperture_time(single_channel_session):
    expected_default_aperture_time = 0.01666
    default_aperture_time = single_channel_session.aperture_time
    assert single_channel_session.aperture_time_units == nidcpower.ApertureTimeUnits.SECONDS
    default_aperture_time_in_range = abs(default_aperture_time - expected_default_aperture_time) <= max(1e-09 * max(abs(default_aperture_time), abs(expected_default_aperture_time)), 0.0)  # https://stackoverflow.com/questions/5595425/what-is-the-best-way-to-compare-floats-for-almost-equality-in-python
    assert default_aperture_time_in_range is True
    single_channel_session.configure_aperture_time(5, nidcpower.ApertureTimeUnits.POWER_LINE_CYCLES)
    assert single_channel_session.aperture_time_units == nidcpower.ApertureTimeUnits.POWER_LINE_CYCLES
    aperture_time = single_channel_session.aperture_time
    expected_aperture_time = 5
    aperture_time_in_range = abs(aperture_time - expected_aperture_time) <= max(1e-09 * max(abs(aperture_time), abs(expected_aperture_time)), 0.0)  # https://stackoverflow.com/questions/5595425/what-is-the-best-way-to-compare-floats-for-almost-equality-in-python
    assert aperture_time_in_range is True


def test_fetch_multiple(single_channel_session):
    single_channel_session.source_mode = nidcpower.SourceMode.SINGLE_POINT
    single_channel_session.configure_aperture_time(0, nidcpower.ApertureTimeUnits.SECONDS)
    single_channel_session.voltage_level = 1
    count = 10
    single_channel_session.measure_when = nidcpower.MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE
    with single_channel_session.initiate():
        measurements = single_channel_session.fetch_multiple(count)
        assert len(measurements) == count
        assert isinstance(measurements[1].voltage, float)
        assert isinstance(measurements[1].current, float)
        assert measurements[1].in_compliance in [True, False]
        assert measurements[1].voltage == 1.0
        assert measurements[1].current == 0.00001


def test_measure_multiple(session):
    with session.initiate():
        # session is open to all 12 channels on the device
        measurements = session.measure_multiple()
        assert len(measurements) == 12
        assert measurements[1].in_compliance is None
        assert measurements[1].voltage == 0.0
        assert measurements[1].current == 0.00001
        # now a subset of the channels
        measurements = session.channels[range(4)].measure_multiple()
        assert len(measurements) == 4
        assert measurements[1].in_compliance is None
        assert measurements[1].voltage == 0.0
        assert measurements[1].current == 0.00001


def test_query_max_current_limit(single_channel_session):
    max_current_limit = single_channel_session.query_max_current_limit(6)
    expected_max_current_limit = 0.06  # for a simulated 4162 max current limit should be 0.06 for 6V Voltage level
    max_current_limit_in_range = abs(max_current_limit - expected_max_current_limit) <= max(1e-09 * max(abs(max_current_limit), abs(expected_max_current_limit)), 0.0)  # https://stackoverflow.com/questions/5595425/what-is-the-best-way-to-compare-floats-for-almost-equality-in-python
    assert max_current_limit_in_range is True


def test_query_max_voltage_level(single_channel_session):
        max_voltage_level = single_channel_session.query_max_voltage_level(0.03)
        expected_max_voltage_level = 24  # for a simulated 4162 max voltage level should be 24V for 30mA current limit
        max_voltage_level_in_range = abs(max_voltage_level - expected_max_voltage_level) <= max(1e-09 * max(abs(max_voltage_level), abs(expected_max_voltage_level)), 0.0)  # https://stackoverflow.com/questions/5595425/what-is-the-best-way-to-compare-floats-for-almost-equality-in-python
        assert max_voltage_level_in_range is True


def test_query_min_current_limit(single_channel_session):
    min_current_limit = single_channel_session.query_min_current_limit(0.03)
    expected_min_current_limit = 0.0000001  # for a simulated 4162 min_current_limit should be 1uA for 6V voltage level
    min_current_limit_in_range = abs(min_current_limit - expected_min_current_limit) <= max(1e-09 * max(abs(min_current_limit), abs(expected_min_current_limit)), 0.0)  # https://stackoverflow.com/questions/5595425/what-is-the-best-way-to-compare-floats-for-almost-equality-in-python
    assert min_current_limit_in_range is True


def test_create_advanced_sequence(single_channel_session):
    ids = [1150008, 1250001, 1150009]  # work around #507
    single_channel_session._create_advanced_sequence(sequence_name='my_sequence', attribute_ids=ids, set_as_active_sequence=True)


def test_set_sequence_with_source_delays(single_channel_session):
    single_channel_session.set_sequence([0.1, 0.2, 0.3], [0.001, 0.002, 0.003])


def test_set_sequence_with_too_many_source_delays(single_channel_session):
    try:
        single_channel_session.set_sequence([0.1, 0.2, 0.3], [0.001, 0.002, 0.003, 0.004])
        assert False
    except ValueError:
        pass


def test_set_sequence_with_too_few_source_delays(single_channel_session):
    try:
        single_channel_session.set_sequence([0.1, 0.2, 0.3, 0.4], [0.001, 0.002])
        assert False
    except ValueError:
        pass


def test_wait_for_event_default_timeout(single_channel_session):
    with single_channel_session.initiate():
        single_channel_session.wait_for_event(nidcpower.Event.SOURCE_COMPLETE)


def test_wait_for_event_with_timeout(single_channel_session):
    with single_channel_session.initiate():
        single_channel_session.wait_for_event(nidcpower.Event.SOURCE_COMPLETE, datetime.timedelta(seconds=0.5))


def test_commit(single_channel_session):
    non_default_current_limit = 0.00021
    single_channel_session.current_limit = non_default_current_limit
    single_channel_session.commit()


def test_create_and_delete_advanced_sequence_step(single_channel_session):
    ids = [1250001]  # work around #507
    single_channel_session.source_mode = nidcpower.SourceMode.SEQUENCE
    single_channel_session._create_advanced_sequence(sequence_name='my_sequence', attribute_ids=ids, set_as_active_sequence=True)
    single_channel_session._create_advanced_sequence_step(set_as_active_step=True)
    single_channel_session.voltage_level = 1
    single_channel_session._delete_advanced_sequence(sequence_name='my_sequence')


def test_send_software_edge_trigger_error(session):
    try:
        session.send_software_edge_trigger(nidcpower.SendSoftwareEdgeTriggerType.START)
        assert False
    except nidcpower.Error as e:
        assert e.code == -1074118587  # Error : Function not available in multichannel session
        assert e.description.find('The requested function is not available when multiple channels are present in the same session.') != -1


def test_get_ext_cal_last_date_and_time(session):
    print(type(session))
    last_cal = session.get_ext_cal_last_date_and_time()
    assert last_cal.year == 1940
    assert last_cal.month == 3
    assert last_cal.day == 1
    assert last_cal.hour == 0
    assert last_cal.minute == 0


def test_get_ext_cal_last_temp(session):
    temperature = session.get_ext_cal_last_temp()
    assert temperature == 25.0


def test_get_ext_cal_recommended_interval(session):
    interval = session.get_ext_cal_recommended_interval()
    assert interval.days == 365


def test_set_get_vi_int_64_attribute(session):
    session.channels['0']._active_advanced_sequence_step = 1
    read_advanced_sequence_step = session.channels['0']._active_advanced_sequence_step
    assert read_advanced_sequence_step == 1


def test_channel_format_types():
    with nidcpower.Session('4162', [0, 1], False, 'Simulate=1, DriverSetup=Model:4162; BoardType:PXIe') as simulated_session:
        assert simulated_session.channel_count == 2
    with nidcpower.Session('4162', range(2), False, 'Simulate=1, DriverSetup=Model:4162; BoardType:PXIe') as simulated_session:
        assert simulated_session.channel_count == 2
    with nidcpower.Session('4162', '0,1', False, 'Simulate=1, DriverSetup=Model:4162; BoardType:PXIe') as simulated_session:
        assert simulated_session.channel_count == 2
    with nidcpower.Session('4162', None, False, 'Simulate=1, DriverSetup=Model:4162; BoardType:PXIe') as simulated_session:
        assert simulated_session.channel_count == 12
    with nidcpower.Session(resource_name='4162', reset=False, options='Simulate=1, DriverSetup=Model:4162; BoardType:PXIe') as simulated_session:
        assert simulated_session.channel_count == 12


