import array
import collections
import os

import numpy
import pytest

import nidigital
from nidigital.enums import DigitalState
from nidigital.history_ram_cycle_information import HistoryRAMCycleInformation

instruments = ['PXI1Slot2', 'PXI1Slot5']
test_files_base_dir = os.path.join(os.path.dirname(__file__), 'test_files')


@pytest.fixture(scope='function')
def multi_instrument_session():
    with nidigital.Session(resource_name=','.join(instruments), options='') as simulated_session:
        yield simulated_session


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
    multi_instrument_session.pins['PinA', 'PinB'].configure_time_set_drive_format('t0', 1501)
    drive_format = multi_instrument_session.pins['PinA', 'PinB'].get_time_set_drive_format('t0')
    assert drive_format == 1501


def test_instruments_rep_cap(multi_instrument_session):
    # fw_rev = multi_instrument_session.channels[instruments[1]].channel_count
    # print(fw_rev)
    # value = multi_instrument_session.channels[instruments[1]].channel_count
    # print(value)
    val2 = multi_instrument_session.channel_count
    print(val2)


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


def test_source_waveform_parallel_broadcast(multi_instrument_session):
    test_name = test_source_waveform_parallel_broadcast.__name__
    configure_session(multi_instrument_session, test_name)

    multi_instrument_session.load_pattern(get_test_file_path(test_name, 'pattern.digipat'))

    multi_instrument_session.pins['LowPins'].create_source_waveform_parallel(waveform_name='src_wfm', data_mapping=2600)

    multi_instrument_session.write_source_waveform_broadcast(
        waveform_name='src_wfm',
        waveform_data=[i for i in range(4)])

    multi_instrument_session.burst_pattern(
        site_list='',
        start_label='new_pattern',
        select_digital_function=True,
        wait_until_done=True,
        timeout=5)

    pass_fail = multi_instrument_session.get_site_pass_fail(site_list='')
    assert pass_fail == [True, True]


def configure_session(session, test_name):
    session.load_pin_map(get_test_file_path(test_name, 'pin_map.pinmap'))

    session.load_specifications(get_test_file_path(test_name, 'specifications.specs'))
    session.load_levels(get_test_file_path(test_name, 'pin_levels.digilevels'))
    session.load_timing(get_test_file_path(test_name, 'timing.digitiming'))
    session.apply_levels_and_timing(
        site_list='',
        levels_sheet='pin_levels',
        timing_sheet='timing',
        initial_state_high_pins='',
        initial_state_low_pins='',
        initial_state_tristate_pins='')


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
    multi_instrument_session.write_sequencer_register(reg='reg0', value=num_samples)

    multi_instrument_session.pins['LowPins'].create_source_waveform_parallel(waveform_name='src_wfm', data_mapping=2601)

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

    multi_instrument_session.burst_pattern(
        site_list='',
        start_label='new_pattern',
        select_digital_function=True,
        wait_until_done=True,
        timeout=5)

    # Pattern burst is configured to fetch num_samples samples
    fetched_waveforms = multi_instrument_session.fetch_capture_waveform(
        site_list='',
        waveform_name='capt_wfm',
        samples_to_read=num_samples,
        timeout=10.0)

    assert sorted(fetched_waveforms.keys()) == sorted([0, 1])
    assert all(len(fetched_waveforms[site]) == num_samples for site in fetched_waveforms)


def test_fetch_capture_waveform(multi_instrument_session):
    test_name = test_fetch_capture_waveform.__name__
    configure_session(multi_instrument_session, test_name)

    multi_instrument_session.load_pattern(get_test_file_path(test_name, 'pattern.digipat'))

    num_samples = 256
    multi_instrument_session.write_sequencer_register(reg='reg0', value=num_samples)

    multi_instrument_session.pins['LowPins'].create_source_waveform_parallel(waveform_name='src_wfm', data_mapping=2600)
    source_waveform = [i for i in range(num_samples)]
    multi_instrument_session.write_source_waveform_broadcast(waveform_name='src_wfm', waveform_data=source_waveform)

    multi_instrument_session.pins['HighPins'].create_capture_waveform_parallel(waveform_name='capt_wfm')

    multi_instrument_session.burst_pattern(
        site_list='',
        start_label='new_pattern',
        select_digital_function=True,
        wait_until_done=True,
        timeout=5)

    # Pattern burst is configured to fetch num_samples samples
    samples_per_fetch = 8
    waveforms = collections.defaultdict(list)
    for i in range(num_samples // samples_per_fetch):
        fetched_waveform = multi_instrument_session.fetch_capture_waveform(
            site_list='site1,site0',
            waveform_name='capt_wfm',
            samples_to_read=samples_per_fetch,
            timeout=10.0)
        for site in fetched_waveform:
            waveforms[site] += fetched_waveform[site]

    assert sorted(waveforms.keys()) == sorted([0, 1])
    assert all(len(waveforms[site]) == num_samples for site in waveforms)

    # Burst on subset of sites and verify fetch_capture_waveform()
    multi_instrument_session.burst_pattern(
        site_list='site1',
        start_label='new_pattern',
        select_digital_function=True,
        wait_until_done=True,
        timeout=5)
    fetched_waveform = multi_instrument_session.fetch_capture_waveform(
        site_list='',
        waveform_name='capt_wfm',
        samples_to_read=num_samples,
        timeout=10.0)

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
        expected_pin_states=[[DigitalState.D, DigitalState.D], [DigitalState.V, DigitalState.V]],
        actual_pin_states=[[DigitalState.PIN_STATE_NOT_ACQUIRED, DigitalState.PIN_STATE_NOT_ACQUIRED], [DigitalState.NOT_A_PIN_STATE, DigitalState.NOT_A_PIN_STATE]],
        per_pin_pass_fail=[[True, True], [False, False]])
    recreated_cycle_info = eval(repr(cycle_info))
    assert str(recreated_cycle_info) == str(cycle_info)


@pytest.mark.skip(reason="TODO(sbethur): Enable running on simulated session. GitHub issue #1273")
def test_fetch_history_ram_cycle_information_position_negative(multi_instrument_session):
    configure_for_history_ram_test(multi_instrument_session)

    with pytest.raises(ValueError, match='position should be greater than or equal to 0.'):
        multi_instrument_session.fetch_history_ram_cycle_information(
            site='site1',
            position=-1,
            samples_to_read=-1)


def configure_for_history_ram_test(session):
    test_files_folder = 'test_fetch_history_ram_cycle_information'
    configure_session(session, test_files_folder)

    session.load_pattern(get_test_file_path(test_files_folder, 'pattern.digipat'))

    session.history_ram_trigger_type = 2200
    session.history_ram_cycles_to_acquire = 2304
    session.history_ram_pretrigger_samples = 0
    session.history_ram_number_of_samples_is_finite = True

    session.burst_pattern(
        site_list='site1',
        start_label='new_pattern',
        select_digital_function=True,
        wait_until_done=True,
        timeout=5)


@pytest.mark.skip(reason="TODO(sbethur): Enable running on simulated session. GitHub issue #1273")
def test_fetch_history_ram_cycle_information_position_out_of_bound(multi_instrument_session):
    configure_for_history_ram_test(multi_instrument_session)

    with pytest.raises(ValueError, match='position: Specified value = 7, Maximum value = 6.'):
        multi_instrument_session.fetch_history_ram_cycle_information(
            site='site1',
            position=7,
            samples_to_read=-1)


@pytest.mark.skip(reason="TODO(sbethur): Enable running on simulated session. GitHub issue #1273")
def test_fetch_history_ram_cycle_information_position_last(multi_instrument_session):
    configure_for_history_ram_test(multi_instrument_session)

    history_ram_cycle_info = multi_instrument_session.fetch_history_ram_cycle_information(
        site='site1',
        position=6,
        samples_to_read=-1)

    assert len(history_ram_cycle_info) == 1
    assert history_ram_cycle_info[0].vector_number == 9
    assert history_ram_cycle_info[0].cycle_number == 11


@pytest.mark.skip(reason="TODO(sbethur): Enable running on simulated session. GitHub issue #1273")
def test_fetch_history_ram_cycle_information_is_finite_invalid(multi_instrument_session):
    configure_for_history_ram_test(multi_instrument_session)
    multi_instrument_session.history_ram_number_of_samples_is_finite = False

    expected_error_description = (
        'Specifying -1 to fetch all History RAM samples is not supported when the digital pattern instrument '
        'is configured for continuous History RAM acquisition. You must specify an exact number of samples to fetch.')
    with pytest.raises(RuntimeError, match=expected_error_description):
        multi_instrument_session.fetch_history_ram_cycle_information(
            site='site1',
            position=0,
            samples_to_read=-1)


@pytest.mark.skip(reason="TODO(sbethur): Enable running on simulated session. GitHub issue #1273")
def test_fetch_history_ram_cycle_information_samples_to_read_too_much(multi_instrument_session):
    configure_for_history_ram_test(multi_instrument_session)

    site = 'site1'
    assert multi_instrument_session.get_history_ram_sample_count(site) == 7

    multi_instrument_session.fetch_history_ram_cycle_information(
        site=site,
        position=0,
        samples_to_read=3)

    expected_error_description = (
        'position: Specified value = 3, samples_to_read: Specified value = 5; Samples available = 4.')
    with pytest.raises(ValueError, match=expected_error_description):
        multi_instrument_session.fetch_history_ram_cycle_information(
            site=site,
            position=3,
            samples_to_read=5)


def test_fetch_history_ram_cycle_information_samples_to_read_negative(multi_instrument_session):
    configure_for_history_ram_test(multi_instrument_session)

    with pytest.raises(ValueError, match='samples_to_read should be greater than or equal to -1.'):
        multi_instrument_session.fetch_history_ram_cycle_information(
            site='site1',
            position=0,
            samples_to_read=-2)


@pytest.mark.skip(reason="TODO(sbethur): Enable running on simulated session. GitHub issue #1273")
def test_fetch_history_ram_cycle_information_samples_to_read_zero(multi_instrument_session):
    configure_for_history_ram_test(multi_instrument_session)

    history_ram_cycle_info = multi_instrument_session.fetch_history_ram_cycle_information(
        site='site1',
        position=0,
        samples_to_read=0)

    assert len(history_ram_cycle_info) == 0


@pytest.mark.skip(reason="TODO(sbethur): Enable running on simulated session. GitHub issue #1273")
def test_fetch_history_ram_cycle_information_samples_to_read_all(multi_instrument_session):
    configure_for_history_ram_test(multi_instrument_session)

    history_ram_cycle_info = multi_instrument_session.fetch_history_ram_cycle_information(
        site='site1',
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
        [[DigitalState.ZERO, DigitalState.H, DigitalState.X, DigitalState.X, DigitalState.H, DigitalState.ZERO, DigitalState.X, DigitalState.X]],
        [[DigitalState.X, DigitalState.X, DigitalState.ZERO, DigitalState.ONE, DigitalState.X, DigitalState.X, DigitalState.L, DigitalState.H]],
        [[DigitalState.X, DigitalState.X, DigitalState.ONE, DigitalState.ZERO, DigitalState.X, DigitalState.X, DigitalState.H, DigitalState.L]],
        [[DigitalState.ONE, DigitalState.ONE, DigitalState.X, DigitalState.X, DigitalState.H, DigitalState.H, DigitalState.X, DigitalState.X], [DigitalState.ZERO, DigitalState.ZERO, DigitalState.X, DigitalState.X, DigitalState.L, DigitalState.L, DigitalState.X, DigitalState.X]],
        [[DigitalState.ONE, DigitalState.ONE, DigitalState.X, DigitalState.X, DigitalState.H, DigitalState.H, DigitalState.X, DigitalState.X], [DigitalState.ZERO, DigitalState.ZERO, DigitalState.X, DigitalState.X, DigitalState.L, DigitalState.L, DigitalState.X, DigitalState.X]],
        [[DigitalState.ZERO, DigitalState.ONE, DigitalState.X, DigitalState.X, DigitalState.L, DigitalState.H, DigitalState.X, DigitalState.X], [DigitalState.ONE, DigitalState.ZERO, DigitalState.X, DigitalState.X, DigitalState.H, DigitalState.L, DigitalState.X, DigitalState.X]],
        [[DigitalState.X, DigitalState.X, DigitalState.X, DigitalState.X, DigitalState.X, DigitalState.X, DigitalState.X, DigitalState.X]]
    ]

    # If test expects actual pin state to be 'X', then value returned by the returned can be anything.
    # So, need to skip those pin states while comparing.
    actual_pin_states = [i.actual_pin_states for i in history_ram_cycle_info]
    actual_pin_states_expected_by_test = [
        [[DigitalState.L, DigitalState.L, DigitalState.X, DigitalState.X, DigitalState.L, DigitalState.L, DigitalState.X, DigitalState.X]],
        [[DigitalState.X, DigitalState.X, DigitalState.L, DigitalState.H, DigitalState.X, DigitalState.X, DigitalState.L, DigitalState.H]],
        [[DigitalState.X, DigitalState.X, DigitalState.H, DigitalState.L, DigitalState.X, DigitalState.X, DigitalState.H, DigitalState.L]],
        [[DigitalState.H, DigitalState.H, DigitalState.X, DigitalState.X, DigitalState.H, DigitalState.H, DigitalState.X, DigitalState.X], [DigitalState.L, DigitalState.L, DigitalState.X, DigitalState.X, DigitalState.L, DigitalState.L, DigitalState.X, DigitalState.X]],
        [[DigitalState.H, DigitalState.H, DigitalState.X, DigitalState.X, DigitalState.H, DigitalState.H, DigitalState.X, DigitalState.X], [DigitalState.L, DigitalState.L, DigitalState.X, DigitalState.X, DigitalState.L, DigitalState.L, DigitalState.X, DigitalState.X]],
        [[DigitalState.L, DigitalState.H, DigitalState.X, DigitalState.X, DigitalState.L, DigitalState.H, DigitalState.X, DigitalState.X], [DigitalState.H, DigitalState.L, DigitalState.X, DigitalState.X, DigitalState.H, DigitalState.L, DigitalState.X, DigitalState.X]],
        [[DigitalState.X, DigitalState.X, DigitalState.X, DigitalState.X, DigitalState.X, DigitalState.X, DigitalState.X, DigitalState.X]]
    ]
    assert len(actual_pin_states) == len(actual_pin_states_expected_by_test)
    for vector_pin_states, vector_pin_states_expected_by_test in zip(actual_pin_states, actual_pin_states_expected_by_test):
        for cycle_pin_states, cycle_pin_states_expected_by_test in zip(vector_pin_states, vector_pin_states_expected_by_test):
            for pin_state, pin_state_expected_by_test in zip(cycle_pin_states, cycle_pin_states_expected_by_test):
                if pin_state_expected_by_test is not DigitalState.X:
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


def test_get_pattern_pin_names(multi_instrument_session):
    test_name = 'simple_pattern'
    configure_session(multi_instrument_session, test_name)

    multi_instrument_session.load_pattern(get_test_file_path(test_name, 'pattern.digipat'))

    pattern_pin_names = multi_instrument_session.get_pattern_pin_names(start_label='new_pattern')

    assert pattern_pin_names == ['LO' + str(i) for i in range(8)] + ['HI' + str(i) for i in range(8)]
