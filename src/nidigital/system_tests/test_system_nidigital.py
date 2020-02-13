import array
import collections
import os

import numpy
import pytest

import nidigital
from nidigital.history_ram_cycle_information import HistoryRAMCycleInformation

instr = ['PXI1Slot2', 'PXI1Slot5']
test_files_base_dir = os.path.join(os.path.dirname(__file__), 'test_files')


@pytest.fixture(scope='function')
def multi_instrument_session():
    # with nidigital.Session(resource_name=','.join(instr), options='Simulate=1, DriverSetup=Model:6570') as simulated_session:
    with nidigital.Session(resource_name=','.join(instr), options='') as simulated_session:
        yield simulated_session


def test_pins_rep_cap(multi_instrument_session):
    multi_instrument_session.load_pin_map(os.path.join(test_files_base_dir, "pin_map.pinmap"))

    multi_instrument_session.vil = 1
    multi_instrument_session.pins['PinA', 'PinB', 'PinC'].vil = 2
    assert multi_instrument_session.pins['DutPins'].vil == pytest.approx(2, abs=1e-3)
    assert multi_instrument_session.pins['SysPins'].vil == pytest.approx(1, abs=1e-3)


def test_property_boolean(multi_instrument_session):
    channel = multi_instrument_session.get_channel_name(index=42)
    multi_instrument_session.channels[channel].ppmu_allow_extended_voltage_range = True
    assert multi_instrument_session.channels[channel].ppmu_allow_extended_voltage_range == True


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

    multi_instrument_session.create_source_waveform_parallel(
        pin_list='LowPins',
        waveform_name='src_wfm',
        data_mapping=2600)

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

    multi_instrument_session.create_source_waveform_parallel(
        pin_list='LowPins',
        waveform_name='src_wfm',
        data_mapping=2601)

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

    multi_instrument_session.create_capture_waveform_parallel(pin_list='HighPins', waveform_name='capt_wfm')

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

    multi_instrument_session.create_source_waveform_parallel(
        pin_list='LowPins',
        waveform_name='src_wfm',
        data_mapping=2600)
    source_waveform = [i for i in range(num_samples)]
    multi_instrument_session.write_source_waveform_broadcast(
        waveform_name='src_wfm',
        waveform_data=source_waveform)

    multi_instrument_session.create_capture_waveform_parallel(pin_list='HighPins', waveform_name='capt_wfm')

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

    fully_qualified_channels = [instr[1] + '/0', instr[0] + '/1', instr[1] + '/11']
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
        expected_pin_states=[[1, 1], [2, 2]],
        actual_pin_states=[[3, 3], [4, 4]],
        per_pin_pass_fail=[[True, True], [False, False]])
    recreated_cycle_info = eval(repr(cycle_info))
    assert str(recreated_cycle_info) == str(cycle_info)


def test_fetch_history_ram_cycle_information_position_negative(multi_instrument_session):
    configure_for_history_ram_test(multi_instrument_session)

    with pytest.raises(ValueError, match='position should be greater than or equal to 0.'):
        multi_instrument_session.fetch_history_ram_cycle_information(
            site='site1',
            pin_list='',
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


def test_fetch_history_ram_cycle_information_position_out_of_bound(multi_instrument_session):
    configure_for_history_ram_test(multi_instrument_session)

    with pytest.raises(ValueError, match='position: Specified value = 7, Maximum value = 6.'):
        multi_instrument_session.fetch_history_ram_cycle_information(
            site='site1',
            pin_list='',
            position=7,
            samples_to_read=-1)


def test_fetch_history_ram_cycle_information_position_last(multi_instrument_session):
    configure_for_history_ram_test(multi_instrument_session)

    history_ram_cycle_info = multi_instrument_session.fetch_history_ram_cycle_information(
        site='site1',
        pin_list='',
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
        multi_instrument_session.fetch_history_ram_cycle_information(
            site='site1',
            pin_list='',
            position=0,
            samples_to_read=-1)


def test_fetch_history_ram_cycle_information_samples_to_read_too_much(multi_instrument_session):
    configure_for_history_ram_test(multi_instrument_session)

    expected_error_description = (
        'position: Specified value = 1, samples_to_read: Specified value = 7; Samples available = 7.')
    with pytest.raises(ValueError, match=expected_error_description):
        multi_instrument_session.fetch_history_ram_cycle_information(
            site='site1',
            pin_list='',
            position=1,
            samples_to_read=7)


def test_fetch_history_ram_cycle_information_samples_to_read_negative(multi_instrument_session):
    configure_for_history_ram_test(multi_instrument_session)

    with pytest.raises(ValueError, match='samples_to_read should be greater than or equal to -1.'):
        multi_instrument_session.fetch_history_ram_cycle_information(
            site='site1',
            pin_list='',
            position=0,
            samples_to_read=-2)


def test_fetch_history_ram_cycle_information_samples_to_read_zero(multi_instrument_session):
    configure_for_history_ram_test(multi_instrument_session)

    history_ram_cycle_info = multi_instrument_session.fetch_history_ram_cycle_information(
        site='site1',
        pin_list='',
        position=0,
        samples_to_read=0)

    assert len(history_ram_cycle_info) == 0


def test_fetch_history_ram_cycle_information_samples_to_read_all(multi_instrument_session):
    configure_for_history_ram_test(multi_instrument_session)

    history_ram_cycle_info = multi_instrument_session.fetch_history_ram_cycle_information(
        site='site1',
        pin_list='',
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

    pin_names = multi_instrument_session.get_pattern_pin_list('new_pattern')
    assert pin_names == 'LO0, LO1, LO2, LO3, HI0, HI1, HI2, HI3'

    expected_pin_states = [i.expected_pin_states for i in history_ram_cycle_info]
    assert expected_pin_states == [
        [[0, 4, 5, 5, 4, 0, 5, 5]],
        [[5, 5, 0, 1, 5, 5, 3, 4]],
        [[5, 5, 1, 0, 5, 5, 4, 3]],
        [[1, 1, 5, 5, 4, 4, 5, 5], [0, 0, 5, 5, 3, 3, 5, 5]],
        [[1, 1, 5, 5, 4, 4, 5, 5], [0, 0, 5, 5, 3, 3, 5, 5]],
        [[0, 1, 5, 5, 3, 4, 5, 5], [1, 0, 5, 5, 4, 3, 5, 5]],
        [[5, 5, 5, 5, 5, 5, 5, 5]]
    ]

    # If test expects actual pin state to be 'X', then value returned by the returned can be anything.
    # So, need to skip those pin states while comparing.
    actual_pin_states = [i.actual_pin_states for i in history_ram_cycle_info]
    actual_pin_states_expected_by_test = [
        [[3, 3, 5, 5, 3, 3, 5, 5]],
        [[5, 5, 3, 4, 5, 5, 3, 4]],
        [[5, 5, 4, 3, 5, 5, 4, 3]],
        [[4, 4, 5, 5, 4, 4, 5, 5], [3, 3, 5, 5, 3, 3, 5, 5]],
        [[4, 4, 5, 5, 4, 4, 5, 5], [3, 3, 5, 5, 3, 3, 5, 5]],
        [[3, 4, 5, 5, 3, 4, 5, 5], [4, 3, 5, 5, 4, 3, 5, 5]],
        [[5, 5, 5, 5, 5, 5, 5, 5]]
    ]
    assert len(actual_pin_states) == len(actual_pin_states_expected_by_test)
    for vector_pin_states, vector_pin_states_expected_by_test in zip(actual_pin_states, actual_pin_states_expected_by_test):
        for cycle_pin_states, cycle_pin_states_expected_by_test in zip(vector_pin_states, vector_pin_states_expected_by_test):
            for pin_state, pin_state_expected_by_test in zip(cycle_pin_states, cycle_pin_states_expected_by_test):
                if pin_state_expected_by_test is not 5:
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

