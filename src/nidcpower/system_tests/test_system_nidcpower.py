import hightime
import nidcpower
import os
import pytest
import tempfile


def pytest_generate_tests(metafunc):
    """Parametrizes the "session" fixture by examining the the markers set for a test.

    By default, the session fixture is parametrized so each test runs once with an Independent
    Channels session. To also run a test with a legacy Synchronized Channels session, decorate the
    test with the custom marker @pytest.mark.include_legacy_session. To run a test with only a
    legacy session, decorate the test with @pytest.mark.legacy_session_only.
    """

    if 'session' in metafunc.fixturenames:
        # fixtures can't be parametrized more than once. this approach prevents exclusive
        # markers from being set on the same test

        legacy_session_only = metafunc.definition.get_closest_marker('legacy_session_only')
        include_legacy_session = metafunc.definition.get_closest_marker('include_legacy_session')

        if legacy_session_only:
            metafunc.parametrize('session', [False], indirect=True)
        if include_legacy_session:
            metafunc.parametrize('session', [True, False], indirect=True)
        if not legacy_session_only and not include_legacy_session:
            metafunc.parametrize('session', [True], indirect=True)


@pytest.fixture(scope='function')
def session(request):
    """Creates an NI-DCPower Session.

    Markers can be used to override the default initializer arguments. For example,
    @pytest.mark.resource_name('4162/0') will override the default resource name.

    Available markers include:
        @pytest.mark.resource_name
        @pytest.mark.channels
        @pytest.mark.reset
        @pytest.mark.options
        @pytest.mark.independent_channels

    By default, all dependent tests will run once with an Independent Channels session. Dependent
    tests can override this behavior by using custom markers. Refer to the documentation in
    pytest_generate_tests for more information.
    """

    # set default values
    init_args = {
        'resource_name': '4162',
        'channels': '',
        'reset': False,
        'options': 'Simulate=1, DriverSetup=Model:4162; BoardType:PXIe',
        'independent_channels': request.param
    }

    # iterate through markers and update arguments
    for marker in request.node.iter_markers():
        if marker.name in init_args:  # only look at markers with valid argument names
            init_args[marker.name] = marker.args[0]  # assume single parameter in marker

    # initialize and yield session
    with nidcpower.Session(**init_args) as simulated_session:
        yield simulated_session


def test_self_test(session):
    session.self_test()


# Workaround for driver runtime bug. See issue #1798 for details.
@pytest.mark.legacy_session_only
def test_self_cal(session):
    session.self_cal()


def test_get_channel_name(session):
    name = session.get_channel_name(1)
    assert name == '4162/0'


def test_get_channel_names(session):
    expected_string = ['4162/{0}'.format(x) for x in range(12)]
    channel_indices = ['0-1, 2, 3:4', 5, (6, 7), range(8, 10), slice(10, 12)]
    assert session.get_channel_names(channel_indices) == expected_string


@pytest.mark.resource_name('Dev1/0-5,Dev2/0-5')
def test_get_channel_names_multiple_instruments(session):
    expected_string = ['{0}/{1}'.format(name, channel) for name in ['Dev1', 'Dev2'] for channel in range(6)]
    channel_indices = ['0-1, 2, 3:4', 5, (6, 7), range(8, 10), slice(10, 12)]
    assert session.get_channel_names(channel_indices) == expected_string


def test_get_attribute_string(session):
    model = session.instrument_model
    assert model == 'NI PXIe-4162'


def test_error_message():
    with pytest.raises(nidcpower.Error) as e:
        # We pass in an invalid model name to force going to error_message
        with nidcpower.Session('4162', [0, 1], False, 'Simulate=1, DriverSetup=Model:invalid_model; BoardType:PXIe'):
            pass
    assert e.value.code == -1074134964
    # The option string parameter contains an entry with an unknown option value.


def test_get_error(session):
    with pytest.raises(nidcpower.Error) as e:
        session.instrument_model = ''
    assert e.value.code == -1074135027
    # Error Description: Attribute is read-only.


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


def test_disable(session):
    channel = session.channels['0']
    assert channel.output_enabled is True
    session.disable()
    assert channel.output_enabled is False


@pytest.mark.channels('0')
def test_measure(session):
    session.source_mode = nidcpower.SourceMode.SINGLE_POINT
    session.output_function = nidcpower.OutputFunction.DC_VOLTAGE
    session.voltage_level_range = 6
    session.voltage_level = 2
    with session.initiate():
        reading = session.measure(nidcpower.MeasurementTypes.VOLTAGE)
        assert session.query_in_compliance() is False
    assert reading == 2


@pytest.mark.channels('0')
def test_query_output_state(session):
    with session.initiate():
        assert session.query_output_state(nidcpower.OutputStates.VOLTAGE) is True   # since default function is DCVolt when initiated output state for DC Volt\DC current should be True and False respectively
        assert session.query_output_state(nidcpower.OutputStates.CURRENT) is False


@pytest.mark.channels('0')
def test_config_aperture_time(session):
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


@pytest.mark.channels('0')
def test_fetch_multiple(session):
    session.source_mode = nidcpower.SourceMode.SINGLE_POINT
    session.configure_aperture_time(0, nidcpower.ApertureTimeUnits.SECONDS)
    session.voltage_level = 1
    count = 10
    session.measure_when = nidcpower.MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE
    with session.initiate():
        measurements = session.fetch_multiple(count)
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


@pytest.mark.parametrize(
    'resource_name,channels,independent_channels,measurement_channels,expected_measured_channel',
    [
        ('Dev1', '1', False, None, '1'),
        ('Dev1', '2', False, '', '2'),
        ('Dev1', '3', False, ' ', '3'),
        ('Dev1', '4', False, '4', '4'),
        (' Dev1 ', ' 5 ', False, ' 5 ', '5'),
        ('Dev1', '1', True, None, 'Dev1/1'),
        ('Dev1', '2', True, '', 'Dev1/2'),
        ('Dev1', '3', True, ' ', 'Dev1/3'),
        ('Dev1', '4', True, '4', 'Dev1/4'),
        ('Dev1', 'Dev1/5', True, 'Dev1/5', 'Dev1/5'),
        ('Dev1/6', '', True, None, 'Dev1/6'),
        ('Dev1/7', ' ', True, ' ', 'Dev1/7'),
        ('  DEV1 / 8  ', ' ', True, ' dev1  /  8 ', 'DEV1/8')
    ]
)
def test_fetch_multiple_channels(
    resource_name,
    channels,
    independent_channels,
    measurement_channels,
    expected_measured_channel
):
    options = {'Simulate': True, 'DriverSetup': {'Model': '4162', 'BoardType': 'PXIe'}}
    with nidcpower.Session(
        resource_name,
        channels,
        options=options,
        independent_channels=independent_channels
    ) as session:
        session.measure_when = nidcpower.MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE
        count = 10
        with session.initiate():
            if measurement_channels is None:
                measurements = session.fetch_multiple(count)
            else:
                measurements = session.channels[measurement_channels].fetch_multiple(count)
            assert len(measurements) == count
            for measurement in measurements:
                assert measurement.channel == expected_measured_channel


@pytest.mark.parametrize(
    'resource_name,channels,independent_channels,measurement_channels,expected_measured_channels',
    [
        ('Dev1', None, False, None, [str(x) for x in range(12)]),
        ('Dev1', '', False, '', [str(x) for x in range(12)]),
        ('Dev1', ' ', False, ' ', [str(x) for x in range(12)]),
        ('Dev1', '0,2-3,6', False, '2-3,0', ['2', '3', '0']),
        (' DEV1 ', ' 0 , 2 - 3 , 6 ', False, ' 2 - 3 , 0', ['2', '3', '0']),
        ('Dev1', None, True, None, [f'Dev1/{x}' for x in range(12)]),
        ('Dev1', '', True, '', [f'Dev1/{x}' for x in range(12)]),
        ('Dev1', ' ', True, ' ', [f'Dev1/{x}' for x in range(12)]),
        ('Dev1', '0:2,Dev1/4', True, 'Dev1/1:2,0', ['Dev1/1', 'Dev1/2', 'Dev1/0']),
        ('Dev1', 'Dev1/0:2,Dev1/4', True, 'Dev1/1:2,Dev1/0', ['Dev1/1', 'Dev1/2', 'Dev1/0']),
        ('Dev1/1', '', True, None, ['Dev1/1']),
        ('Dev1/1:4', ' ', True, '2:3', ['Dev1/2', 'Dev1/3']),
        ('Dev1/0-1,Dev2/0:2', ' ', True, 'Dev2/0-1,Dev1/0', ['Dev2/0', 'Dev2/1', 'Dev1/0']),
        ('Dev1/1:4,Dev1/6', ' ', True, '6,2-3', ['Dev1/6', 'Dev1/2', 'Dev1/3']),
        (' dev1 / 0 - 1 , DEV2 / 0 : 2 ', ' ', True, ' Dev2 / 0 - 1 , DEV1 / 0 ', ['DEV2/0', 'DEV2/1', 'dev1/0']),
        ('DEV1  /1:4,dev1/  6', ' ', True, ' 6 , 2 - 3 ', ['DEV1/6', 'DEV1/2', 'DEV1/3'])
    ]
)
def test_measure_multiple_channels(
    resource_name,
    channels,
    independent_channels,
    measurement_channels,
    expected_measured_channels
):
    options = {'Simulate': True, 'DriverSetup': {'Model': '4162', 'BoardType': 'PXIe'}}
    with nidcpower.Session(
        resource_name,
        channels,
        options=options,
        independent_channels=independent_channels
    ) as session:
        with session.initiate():
            if measurement_channels is None:
                measurements = session.measure_multiple()
            else:
                measurements = session.channels[measurement_channels].measure_multiple()
            assert [measurement.channel for measurement in measurements] == expected_measured_channels


@pytest.mark.resource_name('Dev1,Dev2')
def test_measure_multiple_channel_ordering(session):
    for instrument in (1, 2):
        for channel in range(12):
            session.channels[f"Dev{instrument}/{channel}"].voltage_level = instrument + channel * 0.01
    with session.initiate():
        measurements = session.channels["Dev2/3-5, Dev1/0, Dev2/7"].measure_multiple()
        expected_measured_voltages_and_channels = (
            (2.03, "Dev2/3"),
            (2.04, "Dev2/4"),
            (2.05, "Dev2/5"),
            (1.00, "Dev1/0"),
            (2.07, "Dev2/7")
        )
        assert len(measurements) == len(expected_measured_voltages_and_channels)
        for measurement, expected_measured_voltage_and_channel in zip(
            measurements,
            expected_measured_voltages_and_channels
        ):
            expected_measured_voltage, expected_channel = expected_measured_voltage_and_channel
            assert measurement.voltage == pytest.approx(expected_measured_voltage)
            assert measurement.channel == expected_channel


@pytest.mark.independent_channels(False)
def test_measure_multiple_channel_ordering_non_independent_channels(session):
    for channel in range(12):
        session.channels[f"{channel}"].voltage_level = channel * 0.01
    with session.initiate():
        measurements = session.channels["3-4, 0, 7, 1"].measure_multiple()
        expected_measured_voltages_and_channels = (
            (0.03, "3"),
            (0.04, "4"),
            (0.00, "0"),
            (0.07, "7"),
            (0.01, "1")
        )
        assert len(measurements) == len(expected_measured_voltages_and_channels)
        for measurement, expected_measured_voltage_and_channel in zip(
            measurements,
            expected_measured_voltages_and_channels
        ):
            expected_measured_voltage, expected_channel = expected_measured_voltage_and_channel
            assert measurement.voltage == pytest.approx(expected_measured_voltage)
            assert measurement.channel == expected_channel


@pytest.mark.parametrize(
    'resource_name,measurement_channels',
    [
        ('Dev1/0:1,Dev2/2:3', 'Dev1/0,2'),
        ('Dev1/0:1,Dev2/0:1', '2,3'),
        ('Dev1/0, Dev1/1, Dev2/2', '0, Dev1/1')
    ]
)
def test_measure_multiple_error_invalid_channels(resource_name, measurement_channels):
    options = {'Simulate': True, 'DriverSetup': {'Model': '4162', 'BoardType': 'PXIe'}}
    with nidcpower.Session(
        resource_name,
        channels=' ',
        options=options,
        independent_channels=True
    ) as session:
        with session.initiate():
            with pytest.raises(nidcpower.errors.DriverError) as e:
                session.channels[measurement_channels].measure_multiple()
            assert e.value.code == -1074135008
            assert 'Unknown channel or repeated capability name.' in e.value.description


@pytest.mark.channels('0')
def test_query_max_current_limit(session):
    max_current_limit = session.query_max_current_limit(6)
    assert max_current_limit == pytest.approx(0.1, 1e-9)  # for a simulated 4162 max current limit should be 0.1 for 6V Voltage level


@pytest.mark.channels('0')
def test_query_max_voltage_level(session):
    max_voltage_level = session.query_max_voltage_level(0.03)
    assert max_voltage_level == pytest.approx(24, 1e-9)  # for a simulated 4162 max voltage level should be 24V for 30mA current limit


@pytest.mark.channels('0')
def test_query_min_current_limit(session):
    min_current_limit = session.query_min_current_limit(0.03)
    assert min_current_limit == pytest.approx(0.1e-6, 1e-9)  # for a simulated 4162 min_current_limit should be 0.1uA for 30mV voltage level


@pytest.mark.channels('0')
def test_set_sequence_with_source_delays(session):
    session.set_sequence([0.1, 0.2, 0.3], [0.001, 0.002, 0.003])


@pytest.mark.channels('0')
def test_set_sequence_with_too_many_source_delays(session):
    with pytest.raises(ValueError):
        session.set_sequence([0.1, 0.2, 0.3], [0.001, 0.002, 0.003, 0.004])


@pytest.mark.channels('0')
def test_set_sequence_with_too_few_source_delays(session):
    with pytest.raises(ValueError):
        session.set_sequence([0.1, 0.2, 0.3, 0.4], [0.001, 0.002])


@pytest.mark.channels('0')
def test_wait_for_event_default_timeout(session):
    with session.initiate():
        session.wait_for_event(nidcpower.Event.SOURCE_COMPLETE)


@pytest.mark.channels('0')
def test_wait_for_event_with_timeout(session):
    with session.initiate():
        session.wait_for_event(nidcpower.Event.SOURCE_COMPLETE, hightime.timedelta(seconds=0.5))


@pytest.mark.channels('0')
def test_commit(session):
    non_default_current_limit = 0.00021
    session.current_limit = non_default_current_limit
    session.commit()


@pytest.mark.channels('0')
def test_import_export_buffer(session):
    test_value_1 = 1
    test_value_2 = 2
    session.voltage_level = test_value_1
    assert session.voltage_level == test_value_1
    buffer = session.export_attribute_configuration_buffer()
    session.voltage_level = test_value_2
    assert session.voltage_level == test_value_2
    session.import_attribute_configuration_buffer(buffer)
    assert session.voltage_level == test_value_1


@pytest.mark.channels('0')
def test_import_export_file(session):
    test_value_1 = 1
    test_value_2 = 2
    temp_file = tempfile.NamedTemporaryFile(suffix='.txt', delete=False)
    # NamedTemporaryFile() returns the file already opened, so we need to close it before we can use it
    temp_file.close()
    path = temp_file.name
    session.voltage_level = test_value_1
    assert session.voltage_level == test_value_1
    session.export_attribute_configuration_file(path)
    session.voltage_level = test_value_2
    assert session.voltage_level == test_value_2
    session.import_attribute_configuration_file(path)
    assert session.voltage_level == test_value_1
    os.remove(path)


@pytest.mark.channels('0')
def test_create_and_delete_advanced_sequence(session):
    properties_used = ['output_function', 'voltage_level']
    sequence_name = 'my_sequence'
    session.source_mode = nidcpower.SourceMode.SEQUENCE
    session.create_advanced_sequence(sequence_name=sequence_name, property_names=properties_used, set_as_active_sequence=True)
    session.create_advanced_sequence_step(set_as_active_step=True)
    assert session.active_advanced_sequence == sequence_name
    session.output_function = nidcpower.OutputFunction.DC_VOLTAGE
    session.voltage_level = 1
    session.delete_advanced_sequence(sequence_name=sequence_name)
    with pytest.raises(nidcpower.errors.DriverError):
        session.active_advanced_sequence = sequence_name


@pytest.mark.channels('0')
def test_create_advanced_sequence_commit_step(session):
    properties_used = ['output_function', 'voltage_level']
    sequence_name = 'my_sequence'
    session.source_mode = nidcpower.SourceMode.SEQUENCE
    session.create_advanced_sequence(sequence_name=sequence_name, property_names=properties_used, set_as_active_sequence=True)
    with pytest.raises(nidcpower.Error) as e:
        session.create_advanced_sequence_commit_step(set_as_active_step=True)
    assert e.value.code == -1074118619
    # Error Description: This device does not support the requested operation. Refer to the device
    # documentation to determine which operations it supports.


@pytest.mark.channels('0')
def test_create_and_delete_advanced_sequence_bad_name(session):
    properties_used = ['output_function_bad', 'voltage_level']
    sequence_name = 'my_sequence'
    session.source_mode = nidcpower.SourceMode.SEQUENCE
    with pytest.raises(KeyError):
        session.create_advanced_sequence(sequence_name=sequence_name, property_names=properties_used, set_as_active_sequence=True)


@pytest.mark.channels('0')
def test_create_and_delete_advanced_sequence_bad_type(session):
    properties_used = ['unlock', 'voltage_level']
    sequence_name = 'my_sequence'
    session.source_mode = nidcpower.SourceMode.SEQUENCE
    with pytest.raises(TypeError):
        session.create_advanced_sequence(sequence_name=sequence_name, property_names=properties_used, set_as_active_sequence=True)


@pytest.mark.resource_name("4190/0")
@pytest.mark.options("Simulate=1, DriverSetup=Model:4190; BoardType:PXIe")
def test_create_and_delete_advanced_sequence_attribute_enum_with_converter(session):
    properties_used = ['lcr_measurement_time']
    sequence_name = 'my_sequence'
    session.source_mode = nidcpower.SourceMode.SEQUENCE
    session.create_advanced_sequence(
        sequence_name=sequence_name,
        property_names=properties_used,
        set_as_active_sequence=True
    )
    session.create_advanced_sequence_step(set_as_active_step=True)
    assert session.active_advanced_sequence == sequence_name
    session.lcr_measurement_time = nidcpower.LCRMeasurementTime.SHORT
    session.delete_advanced_sequence(sequence_name=sequence_name)
    with pytest.raises(nidcpower.errors.DriverError):
        session.active_advanced_sequence = sequence_name


@pytest.mark.legacy_session_only
def test_send_software_edge_trigger_error(session):
    with pytest.raises(nidcpower.Error) as e:
        session.send_software_edge_trigger(nidcpower.SendSoftwareEdgeTriggerType.START)
    assert e.value.code == -1074118587
    # Error Description: The requested function is not available when multiple channels are present in the same session.


def test_get_ext_cal_last_date_and_time(session):
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


@pytest.mark.parametrize(
    'channels,expected_channel_count',
    [
        ([0, 1], 2),
        (range(2), 2),
        ('0,1', 2),
        (None, 12)
    ]
)
def test_channels_argument_format(channels, expected_channel_count):
    with nidcpower.Session('4162', channels, False, 'Simulate=1, DriverSetup=Model:4162; BoardType:PXIe') as simulated_session:
        assert simulated_session.channel_count == expected_channel_count


def test_default_channels_argument():
    with nidcpower.Session(resource_name='4162', reset=False, options='Simulate=1, DriverSetup=Model:4162; BoardType:PXIe') as simulated_session:
        assert simulated_session.channel_count == 12


@pytest.mark.parametrize(
    'resource_name,channels,independent_channels',
    [
        ('Dev1', None, False),
        ('Dev1', '', False),
        ('Dev1', '0', False),
        ('Dev1', '0', True)
    ]
)
def test_init_issues_deprecation_warnings(resource_name, channels, independent_channels):
    """Tests for deprecation warnings for legacy initialization options.

    A deprecation warning should occur any time independent_channels is False or a channels
    argument is supplied.
    """
    options = {'Simulate': True, 'DriverSetup': {'Model': '4162', 'BoardType': 'PXIe'}}
    with pytest.deprecated_call() as dc:
        with nidcpower.Session(resource_name, channels, options=options, independent_channels=independent_channels):
            pass
    assert len(dc.list) == 1  # assert only 1 deprecation warning was thrown
    message = dc.list[0].message.args[0]  # grabs the deprecation warning message
    if not independent_channels:
        assert message.find('Initializing session without independent channels enabled.') != -1
    if channels and independent_channels:
        assert message.find('Attempting to initialize an independent channels session with a channels argument.') != -1


@pytest.mark.parametrize(
    'resource_name,channels',
    [
        ('Dev1', None),
        ('Dev1', ''),
        ('Dev1', '0'),
        ('Dev1', '0,1'),
        (['Dev1'], [0, 1]),
        (('Dev1',), (0, 1)),
        ('Dev1', range(2))
    ]
)
def test_init_backwards_compatibility_with_initialize_with_channels(resource_name, channels):
    """Tests that legacy sessions open without exception for valid arguments."""
    options = {'Simulate': True, 'DriverSetup': {'Model': '4162', 'BoardType': 'PXIe'}}
    with nidcpower.Session(resource_name, channels, options=options, independent_channels=False):
        pass


@pytest.mark.parametrize(
    'resource_name,channels',
    [
        ('Dev1', None),
        ('Dev1', ''),
        ('Dev1', '0'),  # backwards compatibility check
        ('Dev1', '0,1'),  # backwards compatibility check
        ('Dev1/0', None),
        ('Dev1/0', ''),
        ('Dev1/0,Dev1/1', None),
        ('Dev1/0,Dev2/1', None),
        ('Dev1/0,Dev2/1', ''),
        (['Dev1/0', 'Dev1/1'], ''),  # construct with list
        (('Dev1/0', 'Dev1/1'), ''),  # construct with tuple
        ('Dev1/0-3', None),
        ('Dev1/0:3', None)
    ]
)
def test_init_with_independent_channels(resource_name, channels):
    """Tests that independent channels sessions open without exception for valid arguments."""
    options = {'Simulate': True, 'DriverSetup': {'Model': '4162', 'BoardType': 'PXIe'}}
    with nidcpower.Session(resource_name, channels, options=options, independent_channels=True):
        pass


def test_init_raises_value_error_for_multi_instrument_resource_name_and_channels_argument():
    """Combining channels with multiple instruments is invalid.

    Tests that a value error is thrown when a multi-instrument resource name is provided with
    a channels argument. How to combine the two arguments is undefined.
    """
    options = {'Simulate': True, 'DriverSetup': {'Model': '4162', 'BoardType': 'PXIe'}}
    with pytest.raises(ValueError):
        with nidcpower.Session("Dev1,Dev2", "0", options=options, independent_channels=True):
            pass


@pytest.mark.parametrize(
    'resource_name,channels',
    [
        ('Dev1/0', '0'),  # combines to 'Dev1/0/0'
        ('Dev1/0', '0,1'),  # combines to 'Dev1/0/0,1'
        ('Dev1/0', '0:3'),  # combines to 'Dev1/0/0:3'
        ('Dev1/0', '0-3'),  # combines to 'Dev1/0/0-3'
        ('Dev1/0', range(4))  # combines to 'Dev1/0/0-3'
    ]
)
def test_init_raises_driver_errors_for_invalid_arguments(resource_name, channels):
    """Tests for driver errors that should occur for invalid initialization arguments."""
    options = {'Simulate': True, 'DriverSetup': {'Model': '4162', 'BoardType': 'PXIe'}}
    with pytest.raises(nidcpower.errors.DriverError) as e:
        with nidcpower.Session(resource_name, channels, options=options):
            pass
    assert e.value.code == -1074097793
    # Error Description: The specified device cannot be found.


@pytest.mark.parametrize(
    'resource_name,channels',
    [
        ('Dev1/0', None),
        ('Dev1/0', 'Dev1/0'),
        ('Dev1/0,Dev2/0', 'Dev1/0'),
        ('Dev1,Dev2', '')
    ]
)
def test_init_raises_driver_errors_for_invalid_arguments_legacy_session(resource_name, channels):
    """Tests invalid initializer arguments for legacy initialize with channels sessions.

    Multi-instrument resource names are valid for simulated initialize with channels sessions. So,
    we attempt to initialize a true session and assert an unsupported device exception is raised.
    """

    with pytest.raises(nidcpower.errors.DriverError) as e:
        with nidcpower.Session(resource_name, channels, independent_channels=False):
            pass
    assert e.value.code == -1074118656
    # Error Description: Device was not recognized. The device is not supported with this driver or version.


@pytest.mark.include_legacy_session
def test_repeated_capabilities_on_method_when_all_channels_are_specified(session):
    """Sessions should not error when specifying all channels by number."""
    assert session.channels['0'].output_enabled is True
    session.channels['0'].output_enabled = False
    session.channels['0-11'].reset()
    assert session.channels['0'].output_enabled is True


@pytest.mark.legacy_session_only
def test_error_channel_name_not_allowed_in_legacy_session(session):
    with pytest.raises(nidcpower.Error) as e:
        session.channels['0'].reset()
    assert e.value.code == -1074118494
    # Error Description: The channel name string must represent all channels in the session because
    # the session was not initialized with independent channels. To specify a subset of channels
    # for this function, first initialize the session with independent channels.


@pytest.mark.legacy_session_only
def test_error_channel_name_not_allowed(session):
    with pytest.raises(nidcpower.Error) as e:
        session.channels['0'].instrument_model
    assert e.value.code == -1074134971
    # Error Description: The channel or repeated capability name is not allowed.


@pytest.mark.resource_name('Dev1,Dev2')
@pytest.mark.parametrize(
    'channels',
    [
        'Dev1/0-11,Dev2/0-11',
        'Dev1/2:5,Dev2/4:7',
        'Dev1/10,Dev2/11',
        'Dev1/3,Dev2/0:11'
    ]
)
def test_repeated_capabilities_with_initiate_multi_instrument_session(session, channels):
    session.channels[channels].initiate()


@pytest.mark.resource_name('Dev1')
@pytest.mark.parametrize('channels', ['Dev1/0', 'Dev1/9-11', '', '0', '4:6', '2-10', '0-11'])
def test_repeated_capabilities_with_initiate_single_instrument_session(session, channels):
    session.channels[channels].initiate()


@pytest.mark.legacy_session_only
@pytest.mark.parametrize('channels', ['', '0-11'])
def test_repeated_capabilities_with_initiate_legacy_session(session, channels):
    """Initiate should work on legacy sessions when all channels are specified."""
    session.channels[channels].initiate()


@pytest.mark.resource_name('Dev1/0-3,Dev2/0,Dev3/0:3')
@pytest.mark.parametrize('indices', ('0:8', range(9)))
def test_repeated_capabilities_with_initiate_and_get_channel_names(session, indices):
    session.channels[session.get_channel_names(indices)].initiate()


@pytest.mark.resource_name('Dev1/0')
@pytest.mark.parametrize('channels', ('1', '0-1', 1))
def test_invalid_channels_repeated_capabilities(session, channels):
    with pytest.raises(nidcpower.Error) as e:
        session.channels[channels].output_function = nidcpower.OutputFunction.DC_VOLTAGE
    assert e.value.code == -1074135008
    # Error Description: Unknown channel or repeated capability name.


@pytest.mark.resource_name('Dev1,Dev2,Dev3')
@pytest.mark.parametrize(
    'device_name',
    [
        'Dev1',
        'Dev2',
        'Dev3',
        'Dev1,Dev2',
        'Dev1,Dev2,Dev3',
        ''
    ]
)
def test_instruments_repeated_capability(session, device_name):
    assert session.instruments[device_name].instrument_model == 'NI PXIe-4162'


@pytest.mark.resource_name('Dev1/0:3, Dev2/0:3')
@pytest.mark.parametrize(
    'channels',
    [
        'Dev1/0',
        'Dev1/0-3',
        'Dev2/0',
        'Dev2/0:3',
        'Dev1/0,Dev2/0',
        'Dev1/0:1,Dev2/2-3',
        'Dev1/3,Dev2/0-3'
    ]
)
def test_create_and_delete_advanced_sequence_repeated_capabilities(session, channels):
    channels_session = session.channels[channels]
    properties_used = ['output_function', 'voltage_level']
    sequence_name = 'my_sequence'
    channels_session.source_mode = nidcpower.SourceMode.SEQUENCE
    channels_session.create_advanced_sequence(sequence_name=sequence_name, property_names=properties_used, set_as_active_sequence=True)
    channels_session.create_advanced_sequence_step(set_as_active_step=True)
    assert channels_session.active_advanced_sequence == sequence_name
    channels_session.output_function = nidcpower.OutputFunction.DC_VOLTAGE
    channels_session.voltage_level = 1
    channels_session.delete_advanced_sequence(sequence_name=sequence_name)
    with pytest.raises(nidcpower.errors.DriverError):
        channels_session.active_advanced_sequence = sequence_name


@pytest.mark.resource_name('Dev1/0, Dev2/0')
@pytest.mark.parametrize('channels', ('Dev1/0', 'Dev2/0', 'Dev1/0,Dev2/0'))
def test_create_advanced_sequence_commit_step_repeated_capabilities(session, channels):
    channels_session = session.channels[channels]
    properties_used = ['output_function', 'voltage_level']
    sequence_name = 'my_sequence'
    channels_session.source_mode = nidcpower.SourceMode.SEQUENCE
    channels_session.create_advanced_sequence(sequence_name=sequence_name, property_names=properties_used, set_as_active_sequence=True)
    with pytest.raises(nidcpower.Error) as e:
        channels_session.create_advanced_sequence_commit_step(set_as_active_step=True)
    assert e.value.code == -1074118619
    # Error Description: This device does not support the requested operation. Refer to the device
    # documentation to determine which operations it supports.


@pytest.mark.resource_name('Dev1/0:3, Dev2/0:3')
@pytest.mark.parametrize('method', ['abort', 'commit', 'reset'])
@pytest.mark.parametrize(
    'channels',
    [
        'Dev1/0',
        'Dev1/0-3',
        'Dev2/0',
        'Dev2/0:3',
        'Dev1/0,Dev2/0',
        'Dev1/0:1,Dev2/2-3',
        'Dev1/3,Dev2/0-3'
    ]
)
def test_repeated_capabilities_parameterless_methods(session, channels, method):
    """Double parametrize markers of this method results in nested parameterization of the test."""
    getattr(session.channels[channels], method)()  # get method by name then invoke it


@pytest.mark.resource_name('Dev1/0:3, Dev2/0:3')
@pytest.mark.parametrize(
    'channels',
    [
        'Dev1/0',
        'Dev1/0-3',
        'Dev2/0',
        'Dev2/0:3',
        'Dev1/0,Dev2/0',
        'Dev1/0:1,Dev2/2-3',
        'Dev1/3,Dev2/0-3'
    ]
)
def test_send_software_edge_trigger_repeated_capabilities(session, channels):
    channels_session = session.channels[channels]
    channels_session.initiate()
    channels_session.send_software_edge_trigger(nidcpower.SendSoftwareEdgeTriggerType.START)


@pytest.mark.resource_name('Dev1/0:3, Dev2/0:3')
@pytest.mark.parametrize(
    'channels',
    [
        'Dev1/0',
        'Dev1/0-3',
        'Dev2/0',
        'Dev2/0:3',
        'Dev1/0,Dev2/0',
        'Dev1/0:1,Dev2/2-3',
        'Dev1/3,Dev2/0-3'
    ]
)
def test_wait_for_event_repeated_capabilities(session, channels):
    channels_session = session.channels[channels]
    with channels_session.initiate():
        channels_session.wait_for_event(nidcpower.Event.SOURCE_COMPLETE)


@pytest.mark.resource_name("4190/0")
@pytest.mark.options("Simulate=1, DriverSetup=Model:4190; BoardType:PXIe")
def test_fetch_multiple_lcr(session):
    session.measure_when = nidcpower.MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE
    session.instrument_mode = nidcpower.InstrumentMode.LCR
    session.lcr_stimulus_function = nidcpower.LCRStimulusFunction.VOLTAGE
    session.lcr_voltage_amplitude = 0.7
    session.lcr_frequency = 10_000.0
    session.lcr_dc_bias_source = nidcpower.LCRDCBiasSource.VOLTAGE
    session.lcr_dc_bias_voltage_level = 1.0
    count = 3
    with session.initiate():
        measurements = session.fetch_multiple_lcr(count)
        assert len(measurements) == count
        for measurement in measurements:
            assert measurement.vdc == pytest.approx(session.lcr_dc_bias_voltage_level, 1e-9)
            assert measurement.stimulus_frequency == pytest.approx(session.lcr_frequency, 1e-9)
            assert measurement.ac_voltage.real == pytest.approx(session.lcr_voltage_amplitude, 1e-9)
            assert measurement.ac_voltage.imag == pytest.approx(0.0, 1e-9)
            assert measurement.measurement_mode == nidcpower.InstrumentMode.LCR
            assert not measurement.dc_in_compliance
            assert not measurement.ac_in_compliance
            assert not measurement.unbalanced


@pytest.mark.resource_name("4190/0")
@pytest.mark.options("Simulate=1, DriverSetup=Model:4190; BoardType:PXIe")
def test_measure_multiple_lcr(session):
    session.instrument_mode = nidcpower.InstrumentMode.LCR
    session.lcr_stimulus_function = nidcpower.LCRStimulusFunction.CURRENT
    session.lcr_current_amplitude = 700.0e-6
    session.lcr_frequency = 10_000.0
    session.lcr_dc_bias_source = nidcpower.LCRDCBiasSource.CURRENT
    session.lcr_dc_bias_current_level = 1.0e-6
    with session.initiate():
        measurements = session.measure_multiple_lcr()
        assert measurements[0].idc == pytest.approx(session.lcr_dc_bias_current_level, 1e-9)
        assert measurements[0].stimulus_frequency == pytest.approx(session.lcr_frequency, 1e-9)
        assert measurements[0].ac_current.real == pytest.approx(session.lcr_current_amplitude, 1e-9)
        assert measurements[0].ac_current.imag == pytest.approx(0.0, 1e-9)
        assert measurements[0].measurement_mode == nidcpower.InstrumentMode.LCR
        assert not measurements[0].dc_in_compliance
        assert not measurements[0].ac_in_compliance
        assert not measurements[0].unbalanced


@pytest.mark.parametrize(
    'resource_name,channels,independent_channels,measurement_channels,expected_measured_channel',
    [
        ('Dev1', None, False, None, '0'),
        ('Dev1', '', False, '', '0'),
        ('Dev1', ' ', False, ' ', '0'),
        (' Dev1 ', ' 0 ', False, ' 0 ', '0'),
        ('Dev1', None, True, None, 'Dev1/0'),
        ('Dev1', '', True, '', 'Dev1/0'),
        ('Dev1', ' ', True, ' ', 'Dev1/0'),
        ('Dev1', '0', True, '0', 'Dev1/0'),
        ('Dev1', 'Dev1/0', True, 'Dev1/0', 'Dev1/0'),
        ('Dev1/0', '', True, None, 'Dev1/0'),
        ('Dev1/0', ' ', True, ' ', 'Dev1/0'),
        ('  DEV1 / 0  ', ' ', True, ' dev1  /  0 ', 'DEV1/0'),
    ]
)
def test_fetch_multiple_lcr_channels(
    resource_name,
    channels,
    independent_channels,
    measurement_channels,
    expected_measured_channel
):
    options = {'Simulate': True, 'DriverSetup': {'Model': '4190', 'BoardType': 'PXIe'}}
    with nidcpower.Session(
        resource_name,
        channels,
        options=options,
        independent_channels=independent_channels
    ) as session:
        session.instrument_mode = nidcpower.InstrumentMode.LCR
        session.measure_when = nidcpower.MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE
        count = 10
        with session.initiate():
            if measurement_channels is None:
                lcr_measurements = session.fetch_multiple_lcr(count)
            else:
                lcr_measurements = session.channels[measurement_channels].fetch_multiple_lcr(count)
            assert len(lcr_measurements) == count
            for lcr_measurement_object in lcr_measurements:
                assert lcr_measurement_object.channel == expected_measured_channel


@pytest.mark.parametrize(
    'resource_name,channels,independent_channels,measurement_channels,expected_measured_channels',
    [
        ('Dev1', None, False, None, ['0']),
        ('Dev1', '', False, '', ['0']),
        ('Dev1', ' ', False, ' ', ['0']),
        (' DEV1 ', ' 0 ', False, ' 0 ', ['0']),
        ('Dev1', None, True, None, ['Dev1/0']),
        ('Dev1', '', True, '', ['Dev1/0']),
        ('Dev1', ' ', True, ' ', ['Dev1/0']),
        ('Dev1', '0', True, 'Dev1/0', ['Dev1/0']),
        ('Dev1', 'Dev1/0', True, '0', ['Dev1/0']),
        ('Dev1/0', '', True, None, ['Dev1/0']),
        ('Dev1/0', ' ', True, ' ', ['Dev1/0']),
        ('Dev1,Dev2', ' ', True, 'Dev2/0,Dev1/0', ['Dev2/0', 'Dev1/0']),
        (' DEV1 / 0 , dev2 / 0 ', ' ', True, 'dev1  /0,DEV2/  0', ['DEV1/0', 'dev2/0']),
    ]
)
def test_measure_multiple_lcr_channels(
    resource_name,
    channels,
    independent_channels,
    measurement_channels,
    expected_measured_channels
):
    options = {'Simulate': True, 'DriverSetup': {'Model': '4190', 'BoardType': 'PXIe'}}
    with nidcpower.Session(
        resource_name,
        channels,
        options=options,
        independent_channels=independent_channels
    ) as session:
        session.instrument_mode = nidcpower.InstrumentMode.LCR
        with session.initiate():
            if measurement_channels is None:
                lcr_measurements = session.measure_multiple_lcr()
            else:
                lcr_measurements = session.channels[measurement_channels].measure_multiple_lcr()
            assert [
                lcr_measurement_object.channel for lcr_measurement_object in lcr_measurements
            ] == expected_measured_channels


@pytest.mark.resource_name("4190/0")
@pytest.mark.options("Simulate=1, DriverSetup=Model:4190; BoardType:PXIe")
@pytest.mark.parametrize("additional_frequencies", [None, [], [9_000.0, 12_345.0, 12_346.0]])
def test_perform_lcr_open_compensation(session, additional_frequencies):
    if additional_frequencies is None:
        nidcpower.Session.perform_lcr_open_compensation(session)
    else:
        nidcpower.Session.perform_lcr_open_compensation(session, additional_frequencies)


@pytest.mark.resource_name("4190/0")
@pytest.mark.options("Simulate=1, DriverSetup=Model:4190; BoardType:PXIe")
@pytest.mark.parametrize("additional_frequencies", [None, [], [9_000.0, 12_345.0, 12_346.0]])
def test_perform_lcr_short_compensation(session, additional_frequencies):
    if additional_frequencies is None:
        nidcpower.Session.perform_lcr_short_compensation(session)
    else:
        nidcpower.Session.perform_lcr_short_compensation(session, additional_frequencies)


@pytest.mark.resource_name("4190/0")
@pytest.mark.options("Simulate=1, DriverSetup=Model:4190; BoardType:PXIe")
def test_perform_lcr_load_compensation(session):
    session.perform_lcr_load_compensation(
        [
            nidcpower.LCRLoadCompensationSpot(
                frequency=100_000.0,
                reference_value_type=nidcpower.LCRReferenceValueType.IMPEDANCE,
                reference_value=complex(100.0, 1000.0)
            ),
            nidcpower.LCRLoadCompensationSpot(
                frequency=200_000.0,
                reference_value_type=nidcpower.LCRReferenceValueType.IDEAL_CAPACITANCE,
                reference_value=300.0e-9
            ),
            nidcpower.LCRLoadCompensationSpot(
                frequency=300_000.0,
                reference_value_type=nidcpower.LCRReferenceValueType.IDEAL_INDUCTANCE,
                reference_value=400.0e-6
            ),
            nidcpower.LCRLoadCompensationSpot(
                frequency=400_000.0,
                reference_value_type=nidcpower.LCRReferenceValueType.IDEAL_RESISTANCE,
                reference_value=200.0
            )
        ]
    )


@pytest.mark.resource_name("4190/0")
@pytest.mark.options("Simulate=1, DriverSetup=Model:4190; BoardType:PXIe")
@pytest.mark.parametrize(
    "compensation_function",
    [
        nidcpower.Session.perform_lcr_open_custom_cable_compensation,
        nidcpower.Session.perform_lcr_short_custom_cable_compensation,
    ],
)
def test_perform_lcr_open_short_custom_cable_compensation(session, compensation_function):
    compensation_function(session)


@pytest.mark.resource_name("4190/0")
@pytest.mark.options("Simulate=1, DriverSetup=Model:4190; BoardType:PXIe")
def test_lcr_custom_cable_compensation_data(session):
    compensation_data = session.get_lcr_custom_cable_compensation_data()
    session.configure_lcr_custom_cable_compensation(compensation_data)

    session.configure_lcr_custom_cable_compensation(list(compensation_data))

    session.configure_lcr_custom_cable_compensation(bytes(compensation_data))

    with tempfile.NamedTemporaryFile(suffix='.bin', delete=False) as temp_file:
        temp_file.write(compensation_data)
    with open(temp_file.name, 'rb') as reopened_temp_file:
        compensation_data_bytes_from_file = reopened_temp_file.read()
    session.configure_lcr_custom_cable_compensation(compensation_data_bytes_from_file)


@pytest.mark.resource_name("4190/0")
@pytest.mark.options("Simulate=1, DriverSetup=Model:4190; BoardType:PXIe")
@pytest.mark.parametrize(
    "compensation_type",
    [
        nidcpower.LCRCompensationType.OPEN_CUSTOM_CABLE,
        nidcpower.LCRCompensationType.SHORT_CUSTOM_CABLE,
        nidcpower.LCRCompensationType.OPEN,
        nidcpower.LCRCompensationType.SHORT,
        nidcpower.LCRCompensationType.LOAD,
    ],
)
def test_get_lcr_compensation_last_date_and_time(session, compensation_type):
    last_compensation_datetime = session.get_lcr_compensation_last_date_and_time(compensation_type)
    assert last_compensation_datetime.year == 1940
    assert last_compensation_datetime.month == 3
    assert last_compensation_datetime.day == 1
    assert last_compensation_datetime.hour == 0
    assert last_compensation_datetime.minute == 0
