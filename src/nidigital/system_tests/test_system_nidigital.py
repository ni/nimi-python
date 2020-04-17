import array
import collections
import datetime
import os

import numpy
import pytest

import nidigital
from nidigital.enums import PinState
from nidigital.history_ram_cycle_information import HistoryRAMCycleInformation

instruments = ['PXI1Slot2', 'PXI1Slot5']
test_files_base_dir = os.path.join(os.path.dirname(__file__), 'test_files')


@pytest.fixture(scope='function')
def multi_instrument_session():
    with nidigital.Session(resource_name=','.join(instruments), options='Simulate=1, DriverSetup=Model:6570') as simulated_session:
        yield simulated_session


def test_reset(multi_instrument_session):
    multi_instrument_session.selected_function = nidigital.SelectedFunction.PPMU
    assert multi_instrument_session.selected_function == nidigital.SelectedFunction.PPMU
    multi_instrument_session.reset()
    assert multi_instrument_session.selected_function == nidigital.SelectedFunction.DISCONNECT


def test_reset_device(multi_instrument_session):
    multi_instrument_session.selected_function = nidigital.SelectedFunction.PPMU
    assert multi_instrument_session.selected_function == nidigital.SelectedFunction.PPMU
    multi_instrument_session.reset_device()
    assert multi_instrument_session.selected_function == nidigital.SelectedFunction.DISCONNECT


def test_self_test(multi_instrument_session):
    multi_instrument_session.self_test()


def test_get_error(multi_instrument_session):
    try:
        multi_instrument_session.supported_instrument_models = ''
        assert False
    except nidigital.Error as e:
        assert e.code == -1074135027
        assert e.description.find('Attribute is read-only.') != -1


def test_self_calibrate(multi_instrument_session):
    multi_instrument_session.self_calibrate()


def test_pins_rep_cap(multi_instrument_session):
    multi_instrument_session.load_pin_map(os.path.join(test_files_base_dir, "pin_map.pinmap"))

    # Channel-based properties
    multi_instrument_session.vil = 1
    multi_instrument_session.pins['PinA', 'PinB', 'PinC'].vil = 2
    assert multi_instrument_session.pins['DutPins'].vil == pytest.approx(2, abs=1e-3)
    assert multi_instrument_session.pins['SysPins'].vil == pytest.approx(1, abs=1e-3)

    # Methods that accept channel_list parameter
    states = multi_instrument_session.pins['PinA', 'PinB'].read_static()
    assert len(states) == 4    # 2 sites per pin

    # Methods that accept pin_list parameter
    multi_instrument_session.create_time_set('t0')
    multi_instrument_session.pins['PinA', 'PinB'].configure_time_set_drive_format(
        time_set_name='t0',
        drive_format=nidigital.DriveFormat.RL)
    drive_format = multi_instrument_session.pins['PinA', 'PinB'].get_time_set_drive_format(time_set_name='t0')
    assert drive_format == nidigital.DriveFormat.RL


def test_instruments_rep_cap(multi_instrument_session):
    multi_instrument_session.timing_absolute_delay_enabled = True
    delay0 = datetime.timedelta(microseconds=5e-3)
    delay1 = datetime.timedelta(microseconds=-5e-3)
    multi_instrument_session.instruments[instruments[0]].timing_absolute_delay = delay0
    multi_instrument_session.instruments[instruments[1]].timing_absolute_delay = delay1
    assert multi_instrument_session.instruments[instruments[0]].timing_absolute_delay == delay0
    assert multi_instrument_session.instruments[instruments[1]].timing_absolute_delay == delay1

    for instrument in instruments:
        assert multi_instrument_session.instruments[instrument].serial_number == '0'

    for instrument in instruments:
        assert multi_instrument_session.instruments[instrument].instrument_firmware_revision == '0.0.0d0'


def test_property_boolean(multi_instrument_session):
    channel = multi_instrument_session.get_channel_name(index=42)
    multi_instrument_session.channels[channel].ppmu_allow_extended_voltage_range = True
    assert multi_instrument_session.channels[channel].ppmu_allow_extended_voltage_range is True


def test_property_int32(multi_instrument_session):
    channel = multi_instrument_session.get_channel_name(index=42)
    multi_instrument_session.channels[channel].termination_mode = nidigital.TerminationMode.HIGH_Z
    assert multi_instrument_session.channels[channel].termination_mode == nidigital.TerminationMode.HIGH_Z


def test_property_int64(multi_instrument_session):
    multi_instrument_session.cycle_number_history_ram_trigger_cycle_number = 42
    assert multi_instrument_session.cycle_number_history_ram_trigger_cycle_number == 42


def test_property_real64(multi_instrument_session):
    channel = multi_instrument_session.get_channel_name(index=42)
    multi_instrument_session.channels[channel].ppmu_voltage_level = 4
    assert multi_instrument_session.channels[channel].ppmu_voltage_level == pytest.approx(4, rel=1e-3)


def test_property_string(multi_instrument_session):
    multi_instrument_session.start_label = 'foo'
    assert multi_instrument_session.start_label == 'foo'


def test_tdr_all_channels(multi_instrument_session):
    applied_offsets = multi_instrument_session.tdr(apply_offsets=False)
    assert len(applied_offsets) == multi_instrument_session.channel_count

    multi_instrument_session.apply_tdr_offsets(applied_offsets)

    channels = [multi_instrument_session.get_channel_name(i) for i in
                range(1, multi_instrument_session.channel_count + 1)]
    fetched_offsets = [multi_instrument_session.channels[i].tdr_offset for i in channels]
    assert fetched_offsets == applied_offsets


def test_tdr_some_channels(multi_instrument_session):
    channels = [multi_instrument_session.get_channel_name(i) for i in [64, 1, 50, 25]]
    applied_offsets = multi_instrument_session.channels[channels].tdr(apply_offsets=False)
    assert len(applied_offsets) == len(channels)

    multi_instrument_session.channels[channels].apply_tdr_offsets(applied_offsets)

    fetched_offsets = [multi_instrument_session.channels[i].tdr_offset for i in channels]
    assert fetched_offsets == applied_offsets


def test_burst_pattern_burst_only(multi_instrument_session):
    test_files_folder = 'simple_pattern'
    configure_session(multi_instrument_session, test_files_folder)

    multi_instrument_session.load_pattern(get_test_file_path(test_files_folder, 'pattern.digipat'))

    result = multi_instrument_session.burst_pattern(start_label='new_pattern', wait_until_done=False)
    assert result is None


def test_burst_pattern_pass_fail(multi_instrument_session):
    test_files_folder = 'simple_pattern'
    configure_session(multi_instrument_session, test_files_folder)

    multi_instrument_session.load_pattern(get_test_file_path(test_files_folder, 'pattern.digipat'))

    result = multi_instrument_session.burst_pattern(start_label='new_pattern', wait_until_done=True)
    assert result == {0: True, 1: True, 2: True, 3: True}


def test_source_waveform_parallel_broadcast(multi_instrument_session):
    test_name = test_source_waveform_parallel_broadcast.__name__
    configure_session(multi_instrument_session, test_name)

    multi_instrument_session.load_pattern(get_test_file_path(test_name, 'pattern.digipat'))

    multi_instrument_session.pins['LowPins'].create_source_waveform_parallel(
        waveform_name='src_wfm',
        data_mapping=nidigital.SourceDataMapping.BROADCAST)

    multi_instrument_session.write_source_waveform_broadcast(
        waveform_name='src_wfm',
        waveform_data=[i for i in range(4)])

    pass_fail = multi_instrument_session.burst_pattern(start_label='new_pattern')
    assert pass_fail == {0: True, 1: True}


def configure_session(session, test_name):
    session.load_pin_map(get_test_file_path(test_name, 'pin_map.pinmap'))

    session.load_specifications_levels_and_timing(
        specifications_file_paths=get_test_file_path(test_name, 'specifications.specs'),
        levels_file_paths=get_test_file_path(test_name, 'pin_levels.digilevels'),
        timing_file_paths=get_test_file_path(test_name, 'timing.digitiming'))
    session.apply_levels_and_timing(levels_sheet='pin_levels', timing_sheet='timing')


def get_test_file_path(test_name, file_name):
    return os.path.join(test_files_base_dir, test_name, file_name)


@pytest.fixture(params=[array.array, numpy.array, list])
def source_waveform_type(request):
    return request.param


def test_source_waveform_parallel_site_unique(multi_instrument_session, source_waveform_type):
    test_name = test_source_waveform_parallel_site_unique.__name__
    configure_session(multi_instrument_session, test_name)

    multi_instrument_session.load_pattern(get_test_file_path(test_name, 'pattern.digipat'))

    num_samples = 256
    multi_instrument_session.write_sequencer_register(reg=nidigital.SequencerRegister.REGISTER0, value=num_samples)

    multi_instrument_session.pins['LowPins'].create_source_waveform_parallel(
        waveform_name='src_wfm',
        data_mapping=nidigital.SourceDataMapping.SITE_UNIQUE)

    if source_waveform_type == array.array:
        source_waveform = {
            1: array.array('L', [i for i in range(num_samples)]),
            0: array.array('L', [i for i in reversed(range(num_samples))])}
    elif source_waveform_type == numpy.array:
        source_waveform = {
            1: numpy.array([i for i in range(num_samples)], dtype=numpy.uint32),
            0: numpy.array([i for i in reversed(range(num_samples))], dtype=numpy.uint32)}
    elif source_waveform_type == list:
        source_waveform = {
            1: [i for i in range(num_samples)],
            0: [i for i in reversed(range(num_samples))]}
    else:
        assert False, "Invalid source waveform data type: {}".format(source_waveform_type)

    multi_instrument_session.write_source_waveform_site_unique(
        waveform_name='src_wfm',
        waveform_data=source_waveform)

    multi_instrument_session.pins['HighPins'].create_capture_waveform_parallel(waveform_name='capt_wfm')

    multi_instrument_session.burst_pattern(start_label='new_pattern')

    # Pattern burst is configured to fetch num_samples samples
    fetched_waveforms = multi_instrument_session.fetch_capture_waveform(
        waveform_name='capt_wfm',
        samples_to_read=num_samples)

    assert sorted(fetched_waveforms.keys()) == sorted([0, 1])
    assert all(len(fetched_waveforms[site]) == num_samples for site in fetched_waveforms)


def test_fetch_capture_waveform(multi_instrument_session):
    test_name = test_fetch_capture_waveform.__name__
    configure_session(multi_instrument_session, test_name)

    multi_instrument_session.load_pattern(get_test_file_path(test_name, 'pattern.digipat'))

    num_samples = 256
    multi_instrument_session.write_sequencer_register(reg=nidigital.SequencerRegister.REGISTER0, value=num_samples)

    multi_instrument_session.pins['LowPins'].create_source_waveform_parallel(
        waveform_name='src_wfm',
        data_mapping=nidigital.SourceDataMapping.BROADCAST)
    source_waveform = [i for i in range(num_samples)]
    multi_instrument_session.write_source_waveform_broadcast(waveform_name='src_wfm', waveform_data=source_waveform)

    multi_instrument_session.pins['HighPins'].create_capture_waveform_parallel(waveform_name='capt_wfm')

    multi_instrument_session.burst_pattern(start_label='new_pattern')

    # Pattern burst is configured to fetch num_samples samples
    samples_per_fetch = 8
    waveforms = collections.defaultdict(list)
    for i in range(num_samples // samples_per_fetch):
        fetched_waveform = multi_instrument_session.sites[1, 0].fetch_capture_waveform(
            waveform_name='capt_wfm',
            samples_to_read=samples_per_fetch)
        for site in fetched_waveform:
            waveforms[site] += fetched_waveform[site]

    assert sorted(waveforms.keys()) == sorted([0, 1])
    assert all(len(waveforms[site]) == num_samples for site in waveforms)

    # Burst on subset of sites and verify fetch_capture_waveform()
    multi_instrument_session.sites[1].burst_pattern(start_label='new_pattern')
    fetched_waveform = multi_instrument_session.fetch_capture_waveform(
        waveform_name='capt_wfm',
        samples_to_read=num_samples)

    assert len(fetched_waveform) == 1
    fetched_site = next(iter(fetched_waveform))
    assert fetched_site == 1
    assert len(fetched_waveform[fetched_site]) == num_samples


def test_get_pin_results_pin_information(multi_instrument_session):
    multi_instrument_session.load_pin_map(os.path.join(test_files_base_dir, "pin_map.pinmap"))

    fully_qualified_channels = [instruments[1] + '/0', instruments[0] + '/1', instruments[1] + '/11']
    pin_info = multi_instrument_session.channels[fully_qualified_channels].get_pin_results_pin_information()

    pins = [i.pin_name for i in pin_info]
    sites = [i.site_number for i in pin_info]
    channels = [i.channel_name for i in pin_info]

    assert pins == ['PinA', 'PinB', '']
    assert sites == [1, 0, -1]
    assert channels == fully_qualified_channels


def test_history_ram_cycle_information_representation():
    cycle_info = HistoryRAMCycleInformation(
        pattern_name='pat',
        time_set_name='t0',
        vector_number=42,
        cycle_number=999,
        scan_cycle_number=13,
        expected_pin_states=[[PinState.D, PinState.D], [PinState.V, PinState.V]],
        actual_pin_states=[[PinState.PIN_STATE_NOT_ACQUIRED, PinState.PIN_STATE_NOT_ACQUIRED], [PinState.NOT_A_PIN_STATE, PinState.NOT_A_PIN_STATE]],
        per_pin_pass_fail=[[True, True], [False, False]])
    recreated_cycle_info = eval(repr(cycle_info))
    assert str(recreated_cycle_info) == str(cycle_info)


def test_history_ram_cycle_information_string():
    cycle_info = HistoryRAMCycleInformation(
        pattern_name='pat',
        time_set_name='t0',
        vector_number=42,
        cycle_number=999,
        scan_cycle_number=13,
        expected_pin_states=[[PinState.D, PinState.V], [PinState.V, PinState.D]],
        actual_pin_states=[[PinState.PIN_STATE_NOT_ACQUIRED, PinState.PIN_STATE_NOT_ACQUIRED], [PinState.ZERO, PinState.ONE]],
        per_pin_pass_fail=[[True, True], [False, False]])
    print(cycle_info)
    expected_string = '''Pattern Name        : pat
Time Set Name       : t0
Vector Number       : 42
Cycle Number        : 999
Scan Cycle Number   : 13
Expected Pin States : [[D, V], [V, D]]
Actual Pin States   : [[PIN_STATE_NOT_ACQUIRED, PIN_STATE_NOT_ACQUIRED], [ZERO, ONE]]
Per Pin Pass Fail   : [[True, True], [False, False]]
'''
    assert str(cycle_info) == expected_string


def test_fetch_history_ram_cycle_information_without_site(multi_instrument_session):
    configure_for_history_ram_test(multi_instrument_session)

    with pytest.raises(ValueError, match='Site number on which to retrieve pattern information must be specified via sites repeated capability.'):
        multi_instrument_session.fetch_history_ram_cycle_information(position=-1, samples_to_read=-1)


def test_fetch_history_ram_cycle_information_position_negative(multi_instrument_session):
    configure_for_history_ram_test(multi_instrument_session)

    with pytest.raises(ValueError, match='position should be greater than or equal to 0.'):
        multi_instrument_session.sites[1].fetch_history_ram_cycle_information(position=-1, samples_to_read=-1)


def configure_for_history_ram_test(session):
    test_files_folder = 'test_fetch_history_ram_cycle_information'
    configure_session(session, test_files_folder)

    session.load_pattern(get_test_file_path(test_files_folder, 'pattern.digipat'))

    session.history_ram_trigger_type = nidigital.HistoryRAMTriggerType.FIRST_FAILURE
    session.history_ram_cycles_to_acquire = nidigital.HistoryRAMCyclesToAcquire.ALL
    session.history_ram_pretrigger_samples = 0
    session.history_ram_number_of_samples_is_finite = True

    session.sites[1].burst_pattern(start_label='new_pattern')


@pytest.mark.skip(reason="TODO(sbethur): Enable running on simulated session. GitHub issue #1273")
def test_fetch_history_ram_cycle_information_position_out_of_bound(multi_instrument_session):
    configure_for_history_ram_test(multi_instrument_session)

    with pytest.raises(ValueError, match='position: Specified value = 8, Maximum value = 6.'):
        multi_instrument_session.sites[1].fetch_history_ram_cycle_information(position=8, samples_to_read=-1)


@pytest.mark.skip(reason="TODO(sbethur): Enable running on simulated session. GitHub issue #1273")
def test_fetch_history_ram_cycle_information_position_last(multi_instrument_session):
    configure_for_history_ram_test(multi_instrument_session)

    history_ram_cycle_info = multi_instrument_session.sites[1].fetch_history_ram_cycle_information(
        position=6,
        samples_to_read=-1)

    assert len(history_ram_cycle_info) == 1
    assert history_ram_cycle_info[0].vector_number == 9
    assert history_ram_cycle_info[0].cycle_number == 11


def test_fetch_history_ram_cycle_information_is_finite_invalid(multi_instrument_session):
    configure_for_history_ram_test(multi_instrument_session)
    multi_instrument_session.history_ram_number_of_samples_is_finite = False

    expected_error_description = (
        'Specifying -1 to fetch all History RAM samples is not supported when the digital pattern instrument '
        'is configured for continuous History RAM acquisition. You must specify an exact number of samples to fetch.')
    with pytest.raises(RuntimeError, match=expected_error_description):
        multi_instrument_session.sites[1].fetch_history_ram_cycle_information(position=0, samples_to_read=-1)


@pytest.mark.skip(reason="TODO(sbethur): Enable running on simulated session. GitHub issue #1273")
def test_fetch_history_ram_cycle_information_samples_to_read_too_much(multi_instrument_session):
    configure_for_history_ram_test(multi_instrument_session)

    assert multi_instrument_session.sites[1].get_history_ram_sample_count() == 7

    multi_instrument_session.sites[1].fetch_history_ram_cycle_information(position=0, samples_to_read=3)

    expected_error_description = (
        'position: Specified value = 3, samples_to_read: Specified value = 5; Samples available = 4.')
    with pytest.raises(ValueError, match=expected_error_description):
        multi_instrument_session.sites[1].fetch_history_ram_cycle_information(position=3, samples_to_read=5)


def test_fetch_history_ram_cycle_information_samples_to_read_negative(multi_instrument_session):
    configure_for_history_ram_test(multi_instrument_session)

    with pytest.raises(ValueError, match='samples_to_read should be greater than or equal to -1.'):
        multi_instrument_session.sites[1].fetch_history_ram_cycle_information(position=0, samples_to_read=-2)


def test_fetch_history_ram_cycle_information_samples_to_read_zero(multi_instrument_session):
    configure_for_history_ram_test(multi_instrument_session)

    history_ram_cycle_info = multi_instrument_session.sites[1].fetch_history_ram_cycle_information(
        position=0,
        samples_to_read=0)

    assert len(history_ram_cycle_info) == 0


@pytest.mark.skip(reason="TODO(sbethur): Enable running on simulated session. GitHub issue #1273")
def test_fetch_history_ram_cycle_information_samples_to_read_all(multi_instrument_session):
    configure_for_history_ram_test(multi_instrument_session)

    history_ram_cycle_info = multi_instrument_session.sites[1].fetch_history_ram_cycle_information(
        position=0,
        samples_to_read=-1)

    assert len(history_ram_cycle_info) == 7
    assert all([i.pattern_name == 'new_pattern' for i in history_ram_cycle_info])

    time_set_names = [i.time_set_name for i in history_ram_cycle_info]
    assert time_set_names == ['t0', 'tScan', 'tScan', 't2X', 't2X', 't2X', 't0']

    vector_numbers = [i.vector_number for i in history_ram_cycle_info]
    assert vector_numbers == [5, 6, 6, 7, 7, 8, 9]

    cycle_numbers = [i.cycle_number for i in history_ram_cycle_info]
    assert cycle_numbers == list(range(5, 12))

    scan_cycle_numbers = [i.scan_cycle_number for i in history_ram_cycle_info]
    assert scan_cycle_numbers == [-1, 0, 1, -1, -1, -1, -1]

    pin_names = multi_instrument_session.get_pattern_pin_names('new_pattern')
    assert pin_names == ['LO' + str(i) for i in range(4)] + ['HI' + str(i) for i in range(4)]

    expected_pin_states = [i.expected_pin_states for i in history_ram_cycle_info]
    assert expected_pin_states == [
        [[PinState.ZERO, PinState.H, PinState.X, PinState.X, PinState.H, PinState.ZERO, PinState.X, PinState.X]],
        [[PinState.X, PinState.X, PinState.ZERO, PinState.ONE, PinState.X, PinState.X, PinState.L, PinState.H]],
        [[PinState.X, PinState.X, PinState.ONE, PinState.ZERO, PinState.X, PinState.X, PinState.H, PinState.L]],
        [[PinState.ONE, PinState.ONE, PinState.X, PinState.X, PinState.H, PinState.H, PinState.X, PinState.X], [PinState.ZERO, PinState.ZERO, PinState.X, PinState.X, PinState.L, PinState.L, PinState.X, PinState.X]],
        [[PinState.ONE, PinState.ONE, PinState.X, PinState.X, PinState.H, PinState.H, PinState.X, PinState.X], [PinState.ZERO, PinState.ZERO, PinState.X, PinState.X, PinState.L, PinState.L, PinState.X, PinState.X]],
        [[PinState.ZERO, PinState.ONE, PinState.X, PinState.X, PinState.L, PinState.H, PinState.X, PinState.X], [PinState.ONE, PinState.ZERO, PinState.X, PinState.X, PinState.H, PinState.L, PinState.X, PinState.X]],
        [[PinState.X, PinState.X, PinState.X, PinState.X, PinState.X, PinState.X, PinState.X, PinState.X]]
    ]

    # If test expects actual pin state to be 'X', then value returned by the returned can be anything.
    # So, need to skip those pin states while comparing.
    actual_pin_states = [i.actual_pin_states for i in history_ram_cycle_info]
    actual_pin_states_expected_by_test = [
        [[PinState.L, PinState.L, PinState.X, PinState.X, PinState.L, PinState.L, PinState.X, PinState.X]],
        [[PinState.X, PinState.X, PinState.L, PinState.H, PinState.X, PinState.X, PinState.L, PinState.H]],
        [[PinState.X, PinState.X, PinState.H, PinState.L, PinState.X, PinState.X, PinState.H, PinState.L]],
        [[PinState.H, PinState.H, PinState.X, PinState.X, PinState.H, PinState.H, PinState.X, PinState.X], [PinState.L, PinState.L, PinState.X, PinState.X, PinState.L, PinState.L, PinState.X, PinState.X]],
        [[PinState.H, PinState.H, PinState.X, PinState.X, PinState.H, PinState.H, PinState.X, PinState.X], [PinState.L, PinState.L, PinState.X, PinState.X, PinState.L, PinState.L, PinState.X, PinState.X]],
        [[PinState.L, PinState.H, PinState.X, PinState.X, PinState.L, PinState.H, PinState.X, PinState.X], [PinState.H, PinState.L, PinState.X, PinState.X, PinState.H, PinState.L, PinState.X, PinState.X]],
        [[PinState.X, PinState.X, PinState.X, PinState.X, PinState.X, PinState.X, PinState.X, PinState.X]]
    ]
    assert len(actual_pin_states) == len(actual_pin_states_expected_by_test)
    for vector_pin_states, vector_pin_states_expected_by_test in zip(actual_pin_states, actual_pin_states_expected_by_test):
        for cycle_pin_states, cycle_pin_states_expected_by_test in zip(vector_pin_states, vector_pin_states_expected_by_test):
            for pin_state, pin_state_expected_by_test in zip(cycle_pin_states, cycle_pin_states_expected_by_test):
                if pin_state_expected_by_test is not PinState.X:
                    assert pin_state == pin_state_expected_by_test

    # Only the first cycle returned is expected to have failures
    per_pin_pass_fail = [i.per_pin_pass_fail for i in history_ram_cycle_info]
    assert per_pin_pass_fail == [
        [[True, False, True, True, False, True, True, True]],
        [[True, True, True, True, True, True, True, True]],
        [[True, True, True, True, True, True, True, True]],
        [[True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True]],
        [[True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True]],
        [[True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True]],
        [[True, True, True, True, True, True, True, True]],
    ]


def test_fetch_history_ram_cycle_information_no_failures(multi_instrument_session):
    test_name = 'simple_pattern'
    configure_session(multi_instrument_session, test_name)
    multi_instrument_session.load_pattern(get_test_file_path(test_name, 'pattern.digipat'))
    multi_instrument_session.burst_pattern(start_label='new_pattern')

    history_ram_cycle_info = multi_instrument_session.sites[0].fetch_history_ram_cycle_information(
        position=0,
        samples_to_read=-1)
    assert len(history_ram_cycle_info) == 0

    history_ram_cycle_info = multi_instrument_session.sites[0].fetch_history_ram_cycle_information(
        position=0,
        samples_to_read=0)
    assert len(history_ram_cycle_info) == 0


def test_get_pattern_pin_names(multi_instrument_session):
    test_name = 'simple_pattern'
    configure_session(multi_instrument_session, test_name)

    multi_instrument_session.load_pattern(get_test_file_path(test_name, 'pattern.digipat'))

    pattern_pin_names = multi_instrument_session.get_pattern_pin_names(start_label='new_pattern')

    assert pattern_pin_names == ['LO' + str(i) for i in range(4)] + ['HI' + str(i) for i in range(4)]


def test_get_site_pass_fail(multi_instrument_session):
    test_files_folder = 'simple_pattern'
    configure_session(multi_instrument_session, test_files_folder)

    multi_instrument_session.load_pattern(get_test_file_path(test_files_folder, 'pattern.digipat'))

    multi_instrument_session.burst_pattern(start_label='new_pattern')

    pass_fail = multi_instrument_session.get_site_pass_fail()
    assert pass_fail == {0: True, 1: True, 2: True, 3: True}

    pass_fail = multi_instrument_session.sites[3, 0].get_site_pass_fail()
    assert pass_fail == {3: True, 0: True}


def test_ppmu_measure(multi_instrument_session):
    test_name = 'simple_pattern'
    configure_session(multi_instrument_session, test_name)

    voltage_measurements = multi_instrument_session.pins['site0/LO0', 'site1/HI0'].ppmu_measure(
        nidigital.enums.PPMUMeasurementType.VOLTAGE)

    assert len(voltage_measurements) == 2


def test_ppmu_source(multi_instrument_session):
    test_name = 'simple_pattern'
    configure_session(multi_instrument_session, test_name)

    multi_instrument_session.pins['site0/LO0', 'site1/HI0'].ppmu_source()


def test_read_static(multi_instrument_session):
    test_name = 'simple_pattern'
    configure_session(multi_instrument_session, test_name)

    pin_states = multi_instrument_session.pins['site0/LO0', 'site1/HI0'].read_static()

    assert pin_states == [nidigital.PinState.L] * 2


def test_write_static(multi_instrument_session):
    test_name = 'simple_pattern'
    configure_session(multi_instrument_session, test_name)

    multi_instrument_session.pins['site0/LO0', 'site1/HI0'].write_static(
        nidigital.WriteStaticPinState.ONE)


def test_read_sequencer_flag(multi_instrument_session):
    flag_state = multi_instrument_session.read_sequencer_flag(nidigital.SequencerFlag.FLAG1)
    assert flag_state is False


def test_write_sequencer_flag(multi_instrument_session):
    multi_instrument_session.write_sequencer_flag(nidigital.SequencerFlag.FLAG2, True)


def test_read_sequencer_register(multi_instrument_session):
    register_value = multi_instrument_session.read_sequencer_register(
        nidigital.SequencerRegister.REGISTER10)
    assert register_value == 0


def test_write_sequencer_register(multi_instrument_session):
    multi_instrument_session.write_sequencer_register(
        nidigital.SequencerRegister.REGISTER15,
        65535)


def test_specifications_levels_and_timing_single(multi_instrument_session):
    pinmap = get_test_file_path('specifications_levels_and_timing_single', 'pin_map.pinmap')
    specs = get_test_file_path('specifications_levels_and_timing_single', 'specs.specs')
    # Levels and timing files contain references to variables in specs1
    levels = get_test_file_path('specifications_levels_and_timing_single', 'levels.digilevels')
    timing = get_test_file_path('specifications_levels_and_timing_single', 'timing.digitiming')

    multi_instrument_session.load_pin_map(pin_map_file_path=pinmap)
    multi_instrument_session.load_specifications_levels_and_timing(
        specifications_file_paths=specs,
        levels_file_paths=levels,
        timing_file_paths=timing)

    # Verify the loaded levels and timing sheets can be applied to hardware
    multi_instrument_session.apply_levels_and_timing(levels_sheet='levels', timing_sheet='timing')

    multi_instrument_session.unload_specifications(file_paths=specs)

    # Verify reapplying the loaded levels and timing sheets throws
    try:
        multi_instrument_session.apply_levels_and_timing(levels_sheet='levels', timing_sheet='timing')
        assert False
    except nidigital.Error as e:
        assert e.code == -1074118494
        assert e.description.find('An error occurred while getting values from a levels sheet.') != -1


def test_specifications_levels_and_timing_multiple(multi_instrument_session):
    pinmap = get_test_file_path('specifications_levels_and_timing_multiple', 'pin_map.pinmap')

    specs1 = get_test_file_path('specifications_levels_and_timing_multiple', 'specs1.specs')
    # Contains reference to variables in specs1
    specs2 = get_test_file_path('specifications_levels_and_timing_multiple', 'specs2.specs')

    # All levels and timing files contain references to variables in specs1 and specs2
    levels1 = get_test_file_path('specifications_levels_and_timing_multiple', 'levels1.digilevels')
    levels2 = get_test_file_path('specifications_levels_and_timing_multiple', 'levels2.digilevels')
    timing1 = get_test_file_path('specifications_levels_and_timing_multiple', 'timing1.digitiming')
    timing2 = get_test_file_path('specifications_levels_and_timing_multiple', 'timing2.digitiming')

    multi_instrument_session.load_pin_map(pin_map_file_path=pinmap)
    multi_instrument_session.load_specifications_levels_and_timing(
        specifications_file_paths=[specs1, specs2],  # list
        levels_file_paths=(levels1, levels2),  # tuple
        timing_file_paths=[timing1, timing2])

    # Verify the loaded levels and timing sheets can be applied to hardware
    multi_instrument_session.apply_levels_and_timing(levels_sheet='levels1', timing_sheet='timing2')
    multi_instrument_session.apply_levels_and_timing(levels_sheet='levels2', timing_sheet='timing1')

    multi_instrument_session.unload_specifications(file_paths=[specs1, specs2])

    # Verify reapplying the loaded levels and timing sheets throws
    try:
        multi_instrument_session.apply_levels_and_timing(levels_sheet='levels1', timing_sheet='timing2')
        assert False
    except nidigital.Error as e:
        assert e.code == -1074118494
        assert e.description.find('An error occurred while getting values from a levels sheet.') != -1


def test_specifications_levels_and_timing_load_sequentially(multi_instrument_session):
    pinmap = get_test_file_path('specifications_levels_and_timing_multiple', 'pin_map.pinmap')

    specs1 = get_test_file_path('specifications_levels_and_timing_multiple', 'specs1.specs')
    # Contains reference to variables in specs1
    specs2 = get_test_file_path('specifications_levels_and_timing_multiple', 'specs2.specs')

    # All levels and timing files contain references to variables in specs1 and specs2
    levels1 = get_test_file_path('specifications_levels_and_timing_multiple', 'levels1.digilevels')
    levels2 = get_test_file_path('specifications_levels_and_timing_multiple', 'levels2.digilevels')
    timing1 = get_test_file_path('specifications_levels_and_timing_multiple', 'timing1.digitiming')
    timing2 = get_test_file_path('specifications_levels_and_timing_multiple', 'timing2.digitiming')

    multi_instrument_session.load_pin_map(pin_map_file_path=pinmap)

    # Load just the specs files first, in two separate calls
    multi_instrument_session.load_specifications_levels_and_timing(specifications_file_paths=specs1)
    multi_instrument_session.load_specifications_levels_and_timing(specifications_file_paths=[specs2])

    # Then load both the levels together
    multi_instrument_session.load_specifications_levels_and_timing(levels_file_paths=[levels2, levels1])

    # Then load the two timing files in two separate calls
    multi_instrument_session.load_specifications_levels_and_timing(timing_file_paths=[timing2])
    multi_instrument_session.load_specifications_levels_and_timing(timing_file_paths=[timing1])

    # Verify the loaded levels and timing sheets can be applied to hardware
    multi_instrument_session.apply_levels_and_timing(levels_sheet='levels1', timing_sheet='timing2')
    multi_instrument_session.apply_levels_and_timing(levels_sheet='levels2', timing_sheet='timing1')

    multi_instrument_session.unload_specifications(file_paths=specs1)
    multi_instrument_session.unload_specifications(file_paths=(specs2))

    # Verify reapplying the loaded levels and timing sheets throws
    try:
        multi_instrument_session.apply_levels_and_timing(levels_sheet='levels1', timing_sheet='timing2')
        assert False
    except nidigital.Error as e:
        assert e.code == -1074118494
        assert e.description.find('An error occurred while getting values from a levels sheet.') != -1

