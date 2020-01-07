import array
import collections
import os
import sys

import numpy
import pytest

import nidigital


instr = ['PXI1Slot2', 'PXI1Slot5']
test_files_base_dir = os.path.join(os.getcwd(), 'src', 'nidigital', 'system_tests', 'test_files')


@pytest.fixture(scope='function')
def multi_instrument_session():
    with nidigital.Session(resource_name=','.join(instr), options='Simulate=1, DriverSetup=Model:6570') as simulated_session:
        yield simulated_session


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


def test_get_pin_results_pin_information(multi_instrument_session):
    pass


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
        select_digital_function=False,
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
        select_digital_function=False,
        wait_until_done=False,
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
        select_digital_function=False,
        wait_until_done=False,
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
        select_digital_function=False,
        wait_until_done=False,
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

