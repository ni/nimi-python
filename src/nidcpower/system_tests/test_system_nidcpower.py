import hightime
import nidcpower
import os
import pytest
import tempfile


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


@pytest.fixture(scope='function')
def independent_channel_session():
    with nidcpower.Session(['4162/0', '4162/1'], False, 'Simulate=1, DriverSetup=Model:4162; BoardType:PXIe') as simulated_session:
        yield simulated_session


# this fixture can be used to test with different types of sessions
@pytest.fixture(scope='function', params=[('4162', '', false), ('4162', [0, 1], false), (('4162/0', '4162/1'), '', true)])
def sessions(request):
    with nidcpower.Session(request.param[0], request.param[1], False,
                           'Simulate=1, DriverSetup=Model:4162; BoardType:PXIe',
                           independent_channels=request.param[2]) as simulated_session:
        yield simulated_session


def test_self_test(sessions):
    sessions.self_test()


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


def test_reset_device(session):
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
    channel.aperture_time_units = nidcpower.ApertureTimeUnits.POWER_LINE_CYCLES
    session.reset_with_defaults()
    assert channel.aperture_time_units == nidcpower.ApertureTimeUnits.SECONDS


def test_reset(session):
    channel = session.channels['0']
    assert channel.output_enabled is True
    channel.output_enabled = False
    session.reset()
    assert channel.output_enabled is True


def test_reset_rep_cap_all(independent_channel_session):
    assert independent_channel_session.channels['4162/0', '4162/1'].output_enabled is True
    independent_channel_session.channels['4162/0', '4162/1'].output_enabled = False
    independent_channel_session.channels['4162/0', '4162/1'].reset()
    assert independent_channel_session.channels['4162/0'].output_enabled is True
    assert independent_channel_session.channels['4162/1'].output_enabled is True
    assert independent_channel_session.channels['4162/0', '4162/1'].output_enabled is True


def test_reset_rep_cap_subset(independent_channel_session):
    assert independent_channel_session.channels['4162/0'].output_enabled is True
    assert independent_channel_session.channels['4162/1'].output_enabled is True
    independent_channel_session.channels['4162/0'].output_enabled = False
    independent_channel_session.channels['4162/1'].output_enabled = False
    independent_channel_session.channels['4162/0'].reset()
    assert independent_channel_session.channels['4162/0'].output_enabled is True
    assert independent_channel_session.channels['4162/1'].output_enabled is False


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
    expected_max_current_limit = 0.1  # for a simulated 4162 max current limit should be 0.1 for 6V Voltage level
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
        single_channel_session.wait_for_event(nidcpower.Event.SOURCE_COMPLETE, hightime.timedelta(seconds=0.5))


def test_commit(single_channel_session):
    non_default_current_limit = 0.00021
    single_channel_session.current_limit = non_default_current_limit
    single_channel_session.commit()


def test_commit_rep_cap(independent_channel_session):
    non_default_current_limit = 0.00021
    independent_channel_session['4162/1'].current_limit = non_default_current_limit
    independent_channel_session['4162/1'].commit()


def test_import_export_buffer(single_channel_session):
    test_value_1 = 1
    test_value_2 = 2
    single_channel_session.voltage_level = test_value_1
    assert single_channel_session.voltage_level == test_value_1
    buffer = single_channel_session.export_attribute_configuration_buffer()
    single_channel_session.voltage_level = test_value_2
    assert single_channel_session.voltage_level == test_value_2
    single_channel_session.import_attribute_configuration_buffer(buffer)
    assert single_channel_session.voltage_level == test_value_1


def test_import_export_file(single_channel_session):
    test_value_1 = 1
    test_value_2 = 2
    temp_file = tempfile.NamedTemporaryFile(suffix='.txt', delete=False)
    # NamedTemporaryFile() returns the file already opened, so we need to close it before we can use it
    temp_file.close()
    path = temp_file.name
    single_channel_session.voltage_level = test_value_1
    assert single_channel_session.voltage_level == test_value_1
    single_channel_session.export_attribute_configuration_file(path)
    single_channel_session.voltage_level = test_value_2
    assert single_channel_session.voltage_level == test_value_2
    single_channel_session.import_attribute_configuration_file(path)
    assert single_channel_session.voltage_level == test_value_1
    os.remove(path)


def test_create_and_delete_advanced_sequence(single_channel_session):
    properties_used = ['output_function', 'voltage_level']
    sequence_name = 'my_sequence'
    single_channel_session.source_mode = nidcpower.SourceMode.SEQUENCE
    single_channel_session.create_advanced_sequence(sequence_name=sequence_name, property_names=properties_used, set_as_active_sequence=True)
    single_channel_session.create_advanced_sequence_step(set_as_active_step=True)
    assert single_channel_session.active_advanced_sequence == sequence_name
    single_channel_session.output_function = nidcpower.OutputFunction.DC_VOLTAGE
    single_channel_session.voltage_level = 1
    single_channel_session.delete_advanced_sequence(sequence_name=sequence_name)
    try:
        single_channel_session.active_advanced_sequence = sequence_name
        assert False
    except nidcpower.errors.DriverError:
        pass


def test_create_and_delete_advanced_sequence_rep_cap(independent_channel_session):
    properties_used = ['output_function', 'voltage_level']
    sequence_name = 'my_sequence'
    channel_session = independent_channel_session.channels['4162/0']
    session.source_mode = nidcpower.SourceMode.SEQUENCE
    channel_session.create_advanced_sequence(sequence_name=sequence_name, property_names=properties_used, set_as_active_sequence=True)
    channel_session.create_advanced_sequence_step(set_as_active_step=True)
    assert channel_session.active_advanced_sequence == sequence_name
    channel_session.output_function = nidcpower.OutputFunction.DC_VOLTAGE
    channel_session.voltage_level = 1
    channel_session.delete_advanced_sequence(sequence_name=sequence_name)
    try:
        channel_session.active_advanced_sequence = sequence_name
        assert False
    except nidcpower.errors.DriverError:
        pass


def test_create_and_delete_advanced_sequence_bad_name(single_channel_session):
    properties_used = ['output_function_bad', 'voltage_level']
    sequence_name = 'my_sequence'
    single_channel_session.source_mode = nidcpower.SourceMode.SEQUENCE
    try:
        single_channel_session.create_advanced_sequence(sequence_name=sequence_name, property_names=properties_used, set_as_active_sequence=True)
        assert False
    except KeyError:
        pass


def test_create_and_delete_advanced_sequence_bad_type(single_channel_session):
    properties_used = ['unlock', 'voltage_level']
    sequence_name = 'my_sequence'
    single_channel_session.source_mode = nidcpower.SourceMode.SEQUENCE
    try:
        single_channel_session.create_advanced_sequence(sequence_name=sequence_name, property_names=properties_used, set_as_active_sequence=True)
        assert False
    except TypeError:
        pass


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
    session.channels['0'].active_advanced_sequence_step = 1
    read_advanced_sequence_step = session.channels['0'].active_advanced_sequence_step
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


def test_rep_cap_all_channels(multiple_channel_session):
    # no error for non-independent channel session when specifying all channels by number
    multiple_channel_session.channels['0', '1'].reset()


def test_rep_cap_method_error(multiple_channel_session):
    try:
        multiple_channel_session.channels['0'].reset()
        assert False
    except nidcpower.Error as e:
        assert e.code == -1074118494  # NIDCPOWER_ERROR_CHANNEL_NAME_NOT_ALLOWED_IN_OBSOLETE_SESSION
        assert e.description.find('The channel name string must represent all channels in the session because the session was not initialized with independent channels. To specify a subset of channels for this function, first initialize the session with independent channels.') != -1


def test_rep_cap_attribute_error(multiple_channel_session):
    try:
        multiple_channel_session.channels['0'].instrument_model
        assert False
    except nidcpower.Error as e:
        assert e.code == -1074134971  # IVI_ERROR_CHANNEL_NAME_NOT_ALLOWED
        assert e.description.find('The channel or repeated capability name is not allowed.') != -1

