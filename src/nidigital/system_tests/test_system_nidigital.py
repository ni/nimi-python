import array
import collections
import os
import pathlib
import subprocess
import time

import grpc
import hightime
import numpy
import pytest

import nidigital

instruments = ['PXI1Slot2', 'PXI1Slot5']
test_files_base_dir = os.path.join(os.path.dirname(__file__), 'test_files')


class SystemTests:
    def test_reset(self, multi_instrument_session):
        multi_instrument_session.selected_function = nidigital.SelectedFunction.PPMU
        assert multi_instrument_session.selected_function == nidigital.SelectedFunction.PPMU
        multi_instrument_session.reset()
        assert multi_instrument_session.selected_function == nidigital.SelectedFunction.DISCONNECT

    def test_reset_device(self, multi_instrument_session):
        multi_instrument_session.selected_function = nidigital.SelectedFunction.PPMU
        assert multi_instrument_session.selected_function == nidigital.SelectedFunction.PPMU
        multi_instrument_session.reset_device()
        assert multi_instrument_session.selected_function == nidigital.SelectedFunction.DISCONNECT

    def test_self_test(self, multi_instrument_session):
        multi_instrument_session.self_test()

    def test_get_error(self, multi_instrument_session):
        try:
            multi_instrument_session.supported_instrument_models = ''
            assert False
        except nidigital.Error as e:
            assert e.code == -1074135027
            assert e.description.find('Attribute is read-only.') != -1

    def test_self_calibrate(self, multi_instrument_session):
        multi_instrument_session.self_calibrate()

    def test_channels_rep_cap(self, multi_instrument_session):
        multi_instrument_session.load_pin_map(os.path.join(test_files_base_dir, "pin_map.pinmap"))

        multi_instrument_session.vil = 1
        ch_0_63 = multi_instrument_session.get_channel_names(indices=[0, 63])
        multi_instrument_session.channels[ch_0_63].vil = 2
        assert multi_instrument_session.pins[ch_0_63].vil == pytest.approx(2, abs=1e-3)
        ch_1 = multi_instrument_session.get_channel_names(indices=1)
        assert multi_instrument_session.pins[ch_1].vil == pytest.approx(1, abs=1e-3)

    def test_sites_rep_cap(self, multi_instrument_session):
        multi_instrument_session.load_pin_map(os.path.join(test_files_base_dir, "pin_map.pinmap"))

        assert multi_instrument_session.sites[0].is_site_enabled()
        assert multi_instrument_session.sites[1].is_site_enabled()

        multi_instrument_session.sites[0, 1].disable_sites()
        assert not multi_instrument_session.sites[0].is_site_enabled()
        assert not multi_instrument_session.sites[1].is_site_enabled()

    def test_pins_rep_cap(self, multi_instrument_session):
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

    def test_chained_sites_pins_rep_cap(self, multi_instrument_session):
        multi_instrument_session.load_pin_map(os.path.join(test_files_base_dir, "pin_map.pinmap"))

        multi_instrument_session.vil = 1
        multi_instrument_session.sites[0, 1].pins['PinA', 'PinB', 'PinC'].vil = 2
        assert multi_instrument_session.sites[0].pins['DutPins'].vil == pytest.approx(2, abs=1e-3)
        assert multi_instrument_session.sites[1].pins['DutPins'].vil == pytest.approx(2, abs=1e-3)

    def test_instruments_rep_cap(self, multi_instrument_session):
        multi_instrument_session.timing_absolute_delay_enabled = True
        delay0 = hightime.timedelta(microseconds=5e-3)
        delay1 = hightime.timedelta(microseconds=-5e-3)
        multi_instrument_session.instruments[instruments[0]].timing_absolute_delay = delay0
        multi_instrument_session.instruments[instruments[1]].timing_absolute_delay = delay1
        assert multi_instrument_session.instruments[instruments[0]].timing_absolute_delay == delay0
        assert multi_instrument_session.instruments[instruments[1]].timing_absolute_delay == delay1

        for instrument in instruments:
            assert multi_instrument_session.instruments[instrument].serial_number == '0'

        for instrument in instruments:
            assert multi_instrument_session.instruments[instrument].instrument_firmware_revision == '0.0.0d0'

    def test_pattern_opcode_events_rep_cap(self, multi_instrument_session):
        assert '' == multi_instrument_session.pattern_opcode_events[3].exported_pattern_opcode_event_output_terminal

        requested_terminal_name = '/Dev1/PXI_Trig0'
        multi_instrument_session.pattern_opcode_events[3].exported_pattern_opcode_event_output_terminal = requested_terminal_name
        assert requested_terminal_name == multi_instrument_session.pattern_opcode_events[3].exported_pattern_opcode_event_output_terminal

    def test_conditional_jump_triggers_rep_cap(self, multi_instrument_session):
        assert nidigital.TriggerType.NONE == multi_instrument_session.conditional_jump_triggers[3].conditional_jump_trigger_type

        requested_trigger_type = nidigital.TriggerType.DIGITAL_EDGE
        multi_instrument_session.conditional_jump_triggers[3].conditional_jump_trigger_type = requested_trigger_type
        assert requested_trigger_type == multi_instrument_session.conditional_jump_triggers[3].conditional_jump_trigger_type

    def test_rio_events_rep_cap(self, single_instrument_session):
        assert '' == single_instrument_session.rio_events[3].exported_rio_event_output_terminal

        requested_terminal_name = '/Dev1/PXI_Trig0'
        single_instrument_session.rio_events[3].exported_rio_event_output_terminal = requested_terminal_name
        assert requested_terminal_name == single_instrument_session.rio_events[3].exported_rio_event_output_terminal

    def test_rio_triggers_rep_cap(self, single_instrument_session):
        assert nidigital.TriggerType.NONE == single_instrument_session.rio_triggers[3].rio_trigger_type

        requested_trigger_type = nidigital.TriggerType.DIGITAL_EDGE
        single_instrument_session.rio_triggers[3].rio_trigger_type = requested_trigger_type
        assert requested_trigger_type == single_instrument_session.rio_triggers[3].rio_trigger_type

    def test_property_boolean(self, multi_instrument_session):
        channel = multi_instrument_session.get_channel_names(indices=42)
        multi_instrument_session.channels[channel].ppmu_allow_extended_voltage_range = True
        assert multi_instrument_session.channels[channel].ppmu_allow_extended_voltage_range is True

    def test_property_int32(self, multi_instrument_session):
        channel = multi_instrument_session.get_channel_names(indices=42)
        multi_instrument_session.channels[channel].termination_mode = nidigital.TerminationMode.HIGH_Z
        assert multi_instrument_session.channels[channel].termination_mode == nidigital.TerminationMode.HIGH_Z

    def test_property_int64(self, multi_instrument_session):
        multi_instrument_session.cycle_number_history_ram_trigger_cycle_number = 42
        assert multi_instrument_session.cycle_number_history_ram_trigger_cycle_number == 42

    def test_property_real64(self, multi_instrument_session):
        channel = multi_instrument_session.get_channel_names(indices=42)
        multi_instrument_session.channels[channel].ppmu_voltage_level = 4
        assert multi_instrument_session.channels[channel].ppmu_voltage_level == pytest.approx(4, rel=1e-3)

    def test_property_string(self, multi_instrument_session):
        multi_instrument_session.start_label = 'foo'
        assert multi_instrument_session.start_label == 'foo'

    def test_get_channel_names(self, multi_instrument_session):
        expected_string = ['{0}/{1}'.format(instruments[0], x) for x in range(12)]
        # Sanity test few different types of input. No need for test to be exhaustive
        # since all the various types are covered by converter unit tests.
        channel_indices = ['0-1, 2, 3:4', 5, (6, 7), range(8, 10), slice(10, 12)]
        assert multi_instrument_session.get_channel_names(indices=channel_indices) == expected_string

    def test_tdr_all_channels(self, multi_instrument_session):
        applied_offsets = multi_instrument_session.tdr(apply_offsets=False)
        assert len(applied_offsets) == multi_instrument_session.channel_count

        multi_instrument_session.apply_tdr_offsets(applied_offsets)

        channels = multi_instrument_session.get_channel_names(range(0, multi_instrument_session.channel_count))
        fetched_offsets = [multi_instrument_session.channels[i].tdr_offset for i in channels]
        assert fetched_offsets == applied_offsets

    def test_tdr_some_channels(self, multi_instrument_session):
        channels = multi_instrument_session.get_channel_names([63, 0, 49, 24])
        applied_offsets = multi_instrument_session.channels[channels].tdr(apply_offsets=False)
        assert len(applied_offsets) == len(channels)

        multi_instrument_session.channels[channels].apply_tdr_offsets(applied_offsets)

        fetched_offsets = [multi_instrument_session.channels[i].tdr_offset for i in channels]
        assert fetched_offsets == applied_offsets

    def test_burst_pattern_burst_only(self, multi_instrument_session):
        test_files_folder = 'simple_pattern'
        self.configure_session(multi_instrument_session, test_files_folder)

        multi_instrument_session.load_pattern(self.get_test_file_path(test_files_folder, 'pattern.digipat'))

        result = multi_instrument_session.burst_pattern(start_label='new_pattern', wait_until_done=False)
        assert result is None

    def test_burst_pattern_pass_fail(self, multi_instrument_session):
        test_files_folder = 'simple_pattern'
        self.configure_session(multi_instrument_session, test_files_folder)

        multi_instrument_session.load_pattern(self.get_test_file_path(test_files_folder, 'pattern.digipat'))

        result = multi_instrument_session.burst_pattern(start_label='new_pattern', wait_until_done=True)
        assert result == {0: True, 1: True, 2: True, 3: True}

    def test_source_waveform_parallel_broadcast(self, multi_instrument_session):
        '''Test methods for using source waveform with parallel sourcing and broadcast data mapping.

        - create_source_waveform_parallel
        - write_source_waveform_broadcast
        '''
        test_name = self.test_source_waveform_parallel_broadcast.__name__
        self.configure_session(multi_instrument_session, test_name)

        multi_instrument_session.load_pattern(self.get_test_file_path(test_name, 'pattern.digipat'))

        multi_instrument_session.pins['LowPins'].create_source_waveform_parallel(
            waveform_name='src_wfm',
            data_mapping=nidigital.SourceDataMapping.BROADCAST)

        multi_instrument_session.write_source_waveform_broadcast(
            waveform_name='src_wfm',
            waveform_data=[i for i in range(4)])

        pass_fail = multi_instrument_session.burst_pattern(start_label='new_pattern')
        assert pass_fail == {0: True, 1: True}

    def configure_session(self, session, test_name):
        session.load_pin_map(self.get_test_file_path(test_name, 'pin_map.pinmap'))

        session.load_specifications_levels_and_timing(
            specifications_file_paths=self.get_test_file_path(test_name, 'specifications.specs'),
            levels_file_paths=self.get_test_file_path(test_name, 'pin_levels.digilevels'),
            timing_file_paths=self.get_test_file_path(test_name, 'timing.digitiming'))
        session.apply_levels_and_timing(levels_sheet='pin_levels', timing_sheet='timing')

    def get_test_file_path(self, test_name, file_name):
        return os.path.join(test_files_base_dir, test_name, file_name)

    @pytest.fixture(params=[array.array, numpy.array, list])
    def source_waveform_type(self, request):
        return request.param

    def test_source_waveform_parallel_site_unique(self, multi_instrument_session, source_waveform_type):
        '''Test methods for using source waveform with parallel sourcing and site-unique data mapping.

        - create_source_waveform_parallel
        - write_source_waveform_site_unique
        '''
        test_name = self.test_source_waveform_parallel_site_unique.__name__
        self.configure_session(multi_instrument_session, test_name)

        multi_instrument_session.load_pattern(self.get_test_file_path(test_name, 'pattern.digipat'))

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

    @pytest.fixture(params=[tuple, int, str])
    def source_waveform_wrong_type(self, request):
        return request.param

    def test_source_waveform_parallel_site_unique_wrong_type(self, multi_instrument_session, source_waveform_wrong_type):
        '''Test methods for passing wrong types write_source_waveform_site_unique .

        - create_source_waveform_parallel
        - write_source_waveform_site_unique
        '''
        test_name = self.test_source_waveform_parallel_site_unique.__name__
        self.configure_session(multi_instrument_session, test_name)

        multi_instrument_session.load_pattern(self.get_test_file_path(test_name, 'pattern.digipat'))

        num_samples = 256
        multi_instrument_session.write_sequencer_register(reg=nidigital.SequencerRegister.REGISTER0, value=num_samples)

        multi_instrument_session.pins['LowPins'].create_source_waveform_parallel(
            waveform_name='src_wfm',
            data_mapping=nidigital.SourceDataMapping.SITE_UNIQUE)

        if source_waveform_wrong_type == tuple:
            source_waveform = ([i for i in range(num_samples)], [i for i in reversed(range(num_samples))])
        elif source_waveform_wrong_type == int:
            source_waveform = num_samples
        elif source_waveform_wrong_type == str:
            source_waveform = {
                str(1): [str(i) for i in range(num_samples)],
                str(0): [str(i) for i in reversed(range(num_samples))]}
        else:
            assert False, "Invalid source waveform data type: {}".format(source_waveform_wrong_type)

        with pytest.raises(TypeError):
            multi_instrument_session.write_source_waveform_site_unique(
                waveform_name='src_wfm',
                waveform_data=source_waveform)

    def test_fetch_capture_waveform_parallel(self, multi_instrument_session):
        '''Test methods for using capture waveform with parallel acquisition.

        - create_capture_waveform_parallel
        - fetch_capture_waveform
        '''
        test_name = self.test_fetch_capture_waveform_parallel.__name__
        self.configure_session(multi_instrument_session, test_name)

        multi_instrument_session.load_pattern(self.get_test_file_path(test_name, 'pattern.digipat'))

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

    def test_get_pin_results_pin_information(self, multi_instrument_session):
        # Also tests load_pin_map
        multi_instrument_session.load_pin_map(os.path.join(test_files_base_dir, "pin_map.pinmap"))

        fully_qualified_channels = [instruments[1] + '/0', instruments[0] + '/1', instruments[1] + '/11']
        pin_info = multi_instrument_session.channels[fully_qualified_channels].get_pin_results_pin_information()

        pins = [i.pin_name for i in pin_info]
        sites = [i.site_number for i in pin_info]
        channels = [i.channel_name for i in pin_info]

        assert pins == ['PinA', 'PinB', '']
        assert sites == [1, 0, -1]
        assert channels == fully_qualified_channels

    def test_history_ram_cycle_information_representation(self):
        cycle_info = nidigital.HistoryRAMCycleInformation(
            pattern_name='pat',
            time_set_name='t0',
            vector_number=42,
            cycle_number=999,
            scan_cycle_number=13,
            expected_pin_states=[[nidigital.PinState.D, nidigital.PinState.D], [nidigital.PinState.V, nidigital.PinState.V]],
            actual_pin_states=[[nidigital.PinState.PIN_STATE_NOT_ACQUIRED, nidigital.PinState.PIN_STATE_NOT_ACQUIRED],
                               [nidigital.PinState.NOT_A_PIN_STATE, nidigital.PinState.NOT_A_PIN_STATE]],
            per_pin_pass_fail=[[True, True], [False, False]])
        recreated_cycle_info = eval(repr(cycle_info))
        assert str(recreated_cycle_info) == str(cycle_info)

    def test_history_ram_cycle_information_string(self):
        cycle_info = nidigital.HistoryRAMCycleInformation(
            pattern_name='pat',
            time_set_name='t0',
            vector_number=42,
            cycle_number=999,
            scan_cycle_number=13,
            expected_pin_states=[[nidigital.PinState.D, nidigital.PinState.V], [nidigital.PinState.V, nidigital.PinState.D]],
            actual_pin_states=[[nidigital.PinState.PIN_STATE_NOT_ACQUIRED, nidigital.PinState.NOT_A_PIN_STATE], [nidigital.PinState.ZERO, nidigital.PinState.ONE]],
            per_pin_pass_fail=[[True, True], [False, False]])
        print(cycle_info)
        expected_string = '''Pattern Name        : pat
Time Set Name       : t0
Vector Number       : 42
Cycle Number        : 999
Scan Cycle Number   : 13
Expected Pin States : [[D, V], [V, D]]
Actual Pin States   : [[Pin State Not Acquired, Not a Pin State], [0, 1]]
Per Pin Pass Fail   : [[True, True], [False, False]]
'''
        assert str(cycle_info) == expected_string

    def test_fetch_history_ram_cycle_information_without_site(self, multi_instrument_session):
        self.configure_for_history_ram_test(multi_instrument_session)

        with pytest.raises(ValueError, match='Site number on which to retrieve pattern information must be specified via sites repeated capability.'):
            multi_instrument_session.fetch_history_ram_cycle_information(position=-1, samples_to_read=-1)

    def test_fetch_history_ram_cycle_information_position_negative(self, multi_instrument_session):
        self.configure_for_history_ram_test(multi_instrument_session)

        with pytest.raises(ValueError, match='position should be greater than or equal to 0.'):
            multi_instrument_session.sites[1].fetch_history_ram_cycle_information(position=-1, samples_to_read=-1)

    def configure_for_history_ram_test(self, session):
        test_files_folder = 'test_fetch_history_ram_cycle_information'
        self.configure_session(session, test_files_folder)

        session.load_pattern(self.get_test_file_path(test_files_folder, 'pattern.digipat'))

        session.history_ram_trigger_type = nidigital.HistoryRAMTriggerType.FIRST_FAILURE
        session.history_ram_cycles_to_acquire = nidigital.HistoryRAMCyclesToAcquire.ALL
        session.history_ram_pretrigger_samples = 0
        session.history_ram_number_of_samples_is_finite = True

        session.sites[1].burst_pattern(start_label='new_pattern')

    @pytest.mark.skip(reason="TODO(sbethur): Enable running on simulated session. GitHub issue #1273")
    def test_fetch_history_ram_cycle_information_position_out_of_bound(self, multi_instrument_session):
        self.configure_for_history_ram_test(multi_instrument_session)

        with pytest.raises(ValueError, match='position: Specified value = 8, Maximum value = 6.'):
            multi_instrument_session.sites[1].fetch_history_ram_cycle_information(position=8, samples_to_read=-1)

    @pytest.mark.skip(reason="TODO(sbethur): Enable running on simulated session. GitHub issue #1273")
    def test_fetch_history_ram_cycle_information_position_last(self, multi_instrument_session):
        self.configure_for_history_ram_test(multi_instrument_session)

        history_ram_cycle_info = multi_instrument_session.sites[1].fetch_history_ram_cycle_information(
            position=6,
            samples_to_read=-1)

        assert len(history_ram_cycle_info) == 1
        assert history_ram_cycle_info[0].vector_number == 9
        assert history_ram_cycle_info[0].cycle_number == 11

    def test_fetch_history_ram_cycle_information_is_finite_invalid(self, multi_instrument_session):
        self.configure_for_history_ram_test(multi_instrument_session)
        multi_instrument_session.history_ram_number_of_samples_is_finite = False

        expected_error_description = (
            'Specifying -1 to fetch all History RAM samples is not supported when the digital pattern instrument '
            'is configured for continuous History RAM acquisition. You must specify an exact number of samples to fetch.')
        with pytest.raises(RuntimeError, match=expected_error_description):
            multi_instrument_session.sites[1].fetch_history_ram_cycle_information(position=0, samples_to_read=-1)

    @pytest.mark.skip(reason="TODO(sbethur): Enable running on simulated session. GitHub issue #1273")
    def test_fetch_history_ram_cycle_information_samples_to_read_too_much(self, multi_instrument_session):
        self.configure_for_history_ram_test(multi_instrument_session)

        assert multi_instrument_session.sites[1].get_history_ram_sample_count() == 7

        multi_instrument_session.sites[1].fetch_history_ram_cycle_information(position=0, samples_to_read=3)

        expected_error_description = (
            'position: Specified value = 3, samples_to_read: Specified value = 5; Samples available = 4.')
        with pytest.raises(ValueError, match=expected_error_description):
            multi_instrument_session.sites[1].fetch_history_ram_cycle_information(position=3, samples_to_read=5)

    def test_fetch_history_ram_cycle_information_samples_to_read_negative(self, multi_instrument_session):
        self.configure_for_history_ram_test(multi_instrument_session)

        with pytest.raises(ValueError, match='samples_to_read should be greater than or equal to -1.'):
            multi_instrument_session.sites[1].fetch_history_ram_cycle_information(position=0, samples_to_read=-2)

    def test_fetch_history_ram_cycle_information_samples_to_read_zero(self, multi_instrument_session):
        self.configure_for_history_ram_test(multi_instrument_session)

        history_ram_cycle_info = multi_instrument_session.sites[1].fetch_history_ram_cycle_information(
            position=0,
            samples_to_read=0)

        assert len(history_ram_cycle_info) == 0

    @pytest.mark.skip(reason="TODO(sbethur): Enable running on simulated session. GitHub issue #1273")
    def test_fetch_history_ram_cycle_information_samples_to_read_all(self, multi_instrument_session):
        self.configure_for_history_ram_test(multi_instrument_session)

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
            [[nidigital.PinState.ZERO, nidigital.PinState.H, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.H, nidigital.PinState.ZERO, nidigital.PinState.X, nidigital.PinState.X]],
            [[nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.ZERO, nidigital.PinState.ONE, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.L, nidigital.PinState.H]],
            [[nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.ONE, nidigital.PinState.ZERO, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.H, nidigital.PinState.L]],
            [[nidigital.PinState.ONE, nidigital.PinState.ONE, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.H, nidigital.PinState.H, nidigital.PinState.X, nidigital.PinState.X], [nidigital.PinState.ZERO, nidigital.PinState.ZERO, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.L, nidigital.PinState.L, nidigital.PinState.X, nidigital.PinState.X]],
            [[nidigital.PinState.ONE, nidigital.PinState.ONE, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.H, nidigital.PinState.H, nidigital.PinState.X, nidigital.PinState.X], [nidigital.PinState.ZERO, nidigital.PinState.ZERO, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.L, nidigital.PinState.L, nidigital.PinState.X, nidigital.PinState.X]],
            [[nidigital.PinState.ZERO, nidigital.PinState.ONE, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.L, nidigital.PinState.H, nidigital.PinState.X, nidigital.PinState.X], [nidigital.PinState.ONE, nidigital.PinState.ZERO, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.H, nidigital.PinState.L, nidigital.PinState.X, nidigital.PinState.X]],
            [[nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.X]]
        ]

        # If test expects actual pin state to be 'X', then value returned by the returned can be anything.
        # So, need to skip those pin states while comparing.
        actual_pin_states = [i.actual_pin_states for i in history_ram_cycle_info]
        actual_pin_states_expected_by_test = [
            [[nidigital.PinState.L, nidigital.PinState.L, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.L, nidigital.PinState.L, nidigital.PinState.X, nidigital.PinState.X]],
            [[nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.L, nidigital.PinState.H, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.L, nidigital.PinState.H]],
            [[nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.H, nidigital.PinState.L, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.H, nidigital.PinState.L]],
            [[nidigital.PinState.H, nidigital.PinState.H, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.H, nidigital.PinState.H, nidigital.PinState.X, nidigital.PinState.X], [nidigital.PinState.L, nidigital.PinState.L, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.L, nidigital.PinState.L, nidigital.PinState.X, nidigital.PinState.X]],
            [[nidigital.PinState.H, nidigital.PinState.H, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.H, nidigital.PinState.H, nidigital.PinState.X, nidigital.PinState.X], [nidigital.PinState.L, nidigital.PinState.L, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.L, nidigital.PinState.L, nidigital.PinState.X, nidigital.PinState.X]],
            [[nidigital.PinState.L, nidigital.PinState.H, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.L, nidigital.PinState.H, nidigital.PinState.X, nidigital.PinState.X], [nidigital.PinState.H, nidigital.PinState.L, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.H, nidigital.PinState.L, nidigital.PinState.X, nidigital.PinState.X]],
            [[nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.X]]
        ]
        assert len(actual_pin_states) == len(actual_pin_states_expected_by_test)
        for vector_pin_states, vector_pin_states_expected_by_test in zip(actual_pin_states, actual_pin_states_expected_by_test):
            for cycle_pin_states, cycle_pin_states_expected_by_test in zip(vector_pin_states, vector_pin_states_expected_by_test):
                for pin_state, pin_state_expected_by_test in zip(cycle_pin_states, cycle_pin_states_expected_by_test):
                    if pin_state_expected_by_test is not nidigital.PinState.X:
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

    def test_fetch_history_ram_cycle_information_no_failures(self, multi_instrument_session):
        test_name = 'simple_pattern'
        self.configure_session(multi_instrument_session, test_name)
        multi_instrument_session.load_pattern(self.get_test_file_path(test_name, 'pattern.digipat'))
        multi_instrument_session.burst_pattern(start_label='new_pattern')

        history_ram_cycle_info = multi_instrument_session.sites[0].fetch_history_ram_cycle_information(
            position=0,
            samples_to_read=-1)
        assert len(history_ram_cycle_info) == 0

        history_ram_cycle_info = multi_instrument_session.sites[0].fetch_history_ram_cycle_information(
            position=0,
            samples_to_read=0)
        assert len(history_ram_cycle_info) == 0

    def test_get_pattern_pin_names(self, multi_instrument_session):
        # Also tests load_pattern
        test_name = 'simple_pattern'
        self.configure_session(multi_instrument_session, test_name)

        multi_instrument_session.load_pattern(self.get_test_file_path(test_name, 'pattern.digipat'))

        pattern_pin_names = multi_instrument_session.get_pattern_pin_names(start_label='new_pattern')

        assert pattern_pin_names == ['LO' + str(i) for i in range(4)] + ['HI' + str(i) for i in range(4)]

    def test_get_site_pass_fail(self, multi_instrument_session):
        test_files_folder = 'simple_pattern'
        self.configure_session(multi_instrument_session, test_files_folder)

        multi_instrument_session.load_pattern(self.get_test_file_path(test_files_folder, 'pattern.digipat'))

        multi_instrument_session.burst_pattern(start_label='new_pattern')

        pass_fail = multi_instrument_session.get_site_pass_fail()
        assert pass_fail == {0: True, 1: True, 2: True, 3: True}

        pass_fail = multi_instrument_session.sites[3, 0].get_site_pass_fail()
        assert pass_fail == {3: True, 0: True}

    def test_get_fail_count(self, multi_instrument_session):
        test_files_folder = 'simple_pattern'
        self.configure_session(multi_instrument_session, test_files_folder)
        multi_instrument_session.load_pattern(self.get_test_file_path(test_files_folder, 'pattern.digipat'))
        multi_instrument_session.burst_pattern(start_label='new_pattern')

        fail_count = multi_instrument_session.get_fail_count()
        assert fail_count == [0] * multi_instrument_session.channel_count

        fail_count = multi_instrument_session.pins['site0/LO0', 'site0/HI1', 'site2/HI3'].get_fail_count()
        assert fail_count == [0] * 3

    def test_ppmu_measure(self, multi_instrument_session):
        test_name = 'simple_pattern'
        self.configure_session(multi_instrument_session, test_name)

        voltage_measurements = multi_instrument_session.pins['site0/LO0', 'site1/HI0'].ppmu_measure(
            nidigital.PPMUMeasurementType.VOLTAGE)

        assert len(voltage_measurements) == 2

    def test_ppmu_source(self, multi_instrument_session):
        test_name = 'simple_pattern'
        self.configure_session(multi_instrument_session, test_name)

        multi_instrument_session.pins['site0/LO0', 'site1/HI0'].ppmu_source()

    def test_read_static(self, multi_instrument_session):
        test_name = 'simple_pattern'
        self.configure_session(multi_instrument_session, test_name)

        pin_states = multi_instrument_session.pins['site0/LO0', 'site1/HI0'].read_static()

        assert pin_states == [nidigital.PinState.L] * 2

    def test_write_static(self, multi_instrument_session):
        test_name = 'simple_pattern'
        self.configure_session(multi_instrument_session, test_name)

        multi_instrument_session.pins['site0/LO0', 'site1/HI0'].write_static(
            nidigital.WriteStaticPinState.ONE)

    def test_read_sequencer_flag(self, multi_instrument_session):
        flag_state = multi_instrument_session.read_sequencer_flag(nidigital.SequencerFlag.FLAG1)
        assert flag_state is False

    def test_write_sequencer_flag(self, multi_instrument_session):
        multi_instrument_session.write_sequencer_flag(nidigital.SequencerFlag.FLAG2, True)

    def test_read_sequencer_register(self, multi_instrument_session):
        register_value = multi_instrument_session.read_sequencer_register(
            nidigital.SequencerRegister.REGISTER10)
        assert register_value == 0

    def test_write_sequencer_register(self, multi_instrument_session):
        multi_instrument_session.write_sequencer_register(
            nidigital.SequencerRegister.REGISTER15,
            65535)

    def test_configure_voltage_levels(self, multi_instrument_session):
        assert multi_instrument_session.vil == pytest.approx(0.0, abs=1e-4)
        assert multi_instrument_session.vih == pytest.approx(3.3, rel=1e-3)
        assert multi_instrument_session.vol == pytest.approx(1.6, rel=1e-3)
        assert multi_instrument_session.voh == pytest.approx(1.7, rel=1e-3)
        assert multi_instrument_session.vterm == pytest.approx(2.0, rel=1e-3)
        multi_instrument_session.load_pin_map(os.path.join(test_files_base_dir, "pin_map.pinmap"))
        multi_instrument_session.pins['site0/PinA', 'site1/PinC'].configure_voltage_levels(
            vil=1.0,
            vih=2.0,
            vol=3.0,
            voh=4.0,
            vterm=5.0)
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].vil == pytest.approx(1.0, rel=1e-3)
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].vih == pytest.approx(2.0, rel=1e-3)
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].vol == pytest.approx(3.0, rel=1e-3)
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].voh == pytest.approx(4.0, rel=1e-3)
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].vterm == pytest.approx(5.0, rel=1e-3)

    def test_configure_active_load_levels(self, multi_instrument_session):
        assert multi_instrument_session.active_load_iol == pytest.approx(0.0015, rel=1e-3)
        assert multi_instrument_session.active_load_ioh == pytest.approx(-0.0015, rel=1e-3)
        assert multi_instrument_session.active_load_vcom == pytest.approx(2.0, rel=1e-3)
        multi_instrument_session.load_pin_map(os.path.join(test_files_base_dir, "pin_map.pinmap"))
        multi_instrument_session.pins['site0/PinA', 'site1/PinC'].configure_active_load_levels(
            iol=0.024,
            ioh=-0.024,
            vcom=3.0)
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].active_load_iol == pytest.approx(0.024, rel=1e-3)
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].active_load_ioh == pytest.approx(-0.024, rel=1e-3)
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].active_load_vcom == pytest.approx(3.0, rel=1e-3)

    def test_clock_generator_abort(self, multi_instrument_session):
        multi_instrument_session.load_pin_map(os.path.join(test_files_base_dir, "pin_map.pinmap"))
        multi_instrument_session.pins['site0/PinA', 'site1/PinC'].clock_generator_abort()

    def test_clock_generator_generate_clock(self, multi_instrument_session):
        multi_instrument_session.load_pin_map(os.path.join(test_files_base_dir, "pin_map.pinmap"))
        multi_instrument_session.pins['site0/PinA', 'site1/PinC'].clock_generator_generate_clock(
            1e6,
            True)

    def test_frequency_counter_measure_frequency(self, multi_instrument_session):
        multi_instrument_session.load_pin_map(os.path.join(test_files_base_dir, "pin_map.pinmap"))
        multi_instrument_session.pins['site0/PinA', 'site1/PinC'].selected_function = nidigital.SelectedFunction.DIGITAL
        multi_instrument_session.pins['site0/PinA', 'site1/PinC'].frequency_counter_measurement_time = hightime.timedelta(milliseconds=5)
        frequencies = multi_instrument_session.pins['site0/PinA', 'site1/PinC'].frequency_counter_measure_frequency()
        assert frequencies == [0] * 2

    def test_create_get_delete_time_sets(self, multi_instrument_session):
        '''Test basic time set methods.

        - create_time_set
        - delete_all_time_sets
        '''
        time_set_a = 'time_set_abc'
        time_set_b = 'time_set_123'
        multi_instrument_session.load_pin_map(os.path.join(test_files_base_dir, "pin_map.pinmap"))

        multi_instrument_session.create_time_set(time_set_a)
        multi_instrument_session.create_time_set(time_set_b)
        multi_instrument_session.delete_all_time_sets()

    def test_configure_get_time_set_period(self, multi_instrument_session):
        '''Test time set period methods.

        - configure_time_set_period
        - get_time_set_period
        '''
        time_set_name = 'time_set_abc'
        time_set_period = hightime.timedelta(microseconds=10)
        multi_instrument_session.load_pin_map(os.path.join(test_files_base_dir, "pin_map.pinmap"))

        multi_instrument_session.create_time_set(time_set_name)
        assert multi_instrument_session.get_time_set_period(time_set_name) == hightime.timedelta(microseconds=1)
        multi_instrument_session.configure_time_set_period(time_set_name, time_set_period)
        assert multi_instrument_session.get_time_set_period(time_set_name) == time_set_period

    def test_configure_get_time_set_drive_format(self, multi_instrument_session):
        '''Test time set drive format methods.

        - configure_time_set_drive_format
        - get_time_set_drive_format
        '''
        time_set_name = 'time_set_abc'
        time_set_drive_format = nidigital.DriveFormat.SBC
        multi_instrument_session.load_pin_map(os.path.join(test_files_base_dir, "pin_map.pinmap"))

        multi_instrument_session.create_time_set(time_set_name)
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].get_time_set_drive_format(time_set_name) == nidigital.DriveFormat.NR
        multi_instrument_session.pins['site0/PinA', 'site1/PinC'].configure_time_set_drive_format(time_set_name, time_set_drive_format)
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].get_time_set_drive_format(time_set_name) == time_set_drive_format

    def test_configure_get_time_set_edge(self, multi_instrument_session):
        '''Test time set individual edge methods.

        - configure_time_set_edge
        - get_time_set_edge
        '''
        time_set_name = 'time_set_abc'
        time_set_period = hightime.timedelta(microseconds=10)
        time_set_drive_on = time_set_period * 0.5
        multi_instrument_session.load_pin_map(os.path.join(test_files_base_dir, "pin_map.pinmap"))

        multi_instrument_session.create_time_set(time_set_name)
        multi_instrument_session.configure_time_set_period(time_set_name, time_set_period)
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].get_time_set_edge(
            time_set_name,
            nidigital.TimeSetEdgeType.DRIVE_ON) == hightime.timedelta(seconds=0)
        multi_instrument_session.pins['site0/PinA', 'site1/PinC'].configure_time_set_edge(
            time_set_name,
            nidigital.TimeSetEdgeType.DRIVE_ON,
            time_set_drive_on)
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].get_time_set_edge(
            time_set_name,
            nidigital.TimeSetEdgeType.DRIVE_ON) == time_set_drive_on

    def test_configure_time_set_drive_edges(self, multi_instrument_session):
        time_set_name = 'time_set_abc'
        time_set_period = hightime.timedelta(microseconds=10)
        time_set_drive_format = nidigital.DriveFormat.RL
        time_set_drive_on = time_set_period * 0.1
        time_set_drive_data = time_set_period * 0.2
        time_set_drive_return = time_set_period * 0.8
        time_set_drive_off = time_set_period * 0.9

        multi_instrument_session.load_pin_map(os.path.join(test_files_base_dir, "pin_map.pinmap"))
        multi_instrument_session.create_time_set(time_set_name)
        multi_instrument_session.configure_time_set_period(time_set_name, time_set_period)

        multi_instrument_session.pins['site0/PinA', 'site1/PinC'].configure_time_set_drive_edges(
            time_set_name,
            time_set_drive_format,
            time_set_drive_on,
            time_set_drive_data,
            time_set_drive_return,
            time_set_drive_off)
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].get_time_set_drive_format(time_set_name) == time_set_drive_format
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].get_time_set_edge(
            time_set_name,
            nidigital.TimeSetEdgeType.DRIVE_ON) == time_set_drive_on
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].get_time_set_edge(
            time_set_name,
            nidigital.TimeSetEdgeType.DRIVE_DATA) == time_set_drive_data
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].get_time_set_edge(
            time_set_name,
            nidigital.TimeSetEdgeType.DRIVE_RETURN) == time_set_drive_return
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].get_time_set_edge(
            time_set_name,
            nidigital.TimeSetEdgeType.DRIVE_OFF) == time_set_drive_off

    def test_configure_time_set_compare_edges_strobe(self, multi_instrument_session):
        time_set_name = 'time_set_abc'
        time_set_period = hightime.timedelta(microseconds=10)
        time_set_strobe = time_set_period * 0.5

        multi_instrument_session.load_pin_map(os.path.join(test_files_base_dir, "pin_map.pinmap"))
        multi_instrument_session.create_time_set(time_set_name)
        multi_instrument_session.configure_time_set_period(time_set_name, time_set_period)

        multi_instrument_session.pins['site0/PinA', 'site1/PinC'].configure_time_set_compare_edges_strobe(
            time_set_name,
            time_set_strobe)
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].get_time_set_edge(
            time_set_name,
            nidigital.TimeSetEdgeType.COMPARE_STROBE) == time_set_strobe

    def test_configure_get_time_set_edge_multiplier(self, multi_instrument_session):
        '''Test time set edge multiplier methods.

        - configure_time_set_edge_multiplier
        - get_time_set_edge_multiplier
        '''
        time_set_name = 'time_set_abc'
        time_set_period = hightime.timedelta(microseconds=10)
        time_set_edge_multiplier = 2

        multi_instrument_session.load_pin_map(os.path.join(test_files_base_dir, "pin_map.pinmap"))
        multi_instrument_session.create_time_set(time_set_name)
        multi_instrument_session.configure_time_set_period(time_set_name, time_set_period)

        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].get_time_set_edge_multiplier(time_set_name) == 1
        multi_instrument_session.pins['site0/PinA', 'site1/PinC'].configure_time_set_edge_multiplier(time_set_name, time_set_edge_multiplier)
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].get_time_set_edge_multiplier(time_set_name) == time_set_edge_multiplier

    def test_configure_time_set_drive_edges2x(self, multi_instrument_session):
        time_set_name = 'time_set_abc'
        time_set_period = hightime.timedelta(microseconds=10)
        time_set_drive_format = nidigital.DriveFormat.RL
        time_set_drive_on = time_set_period * 0.1
        time_set_drive_data = time_set_period * 0.2
        time_set_drive_return = time_set_period * 0.5
        time_set_drive_data2 = time_set_period * 0.7
        time_set_drive_return2 = time_set_period * 0.9
        time_set_drive_off = time_set_period * 0.9

        multi_instrument_session.load_pin_map(os.path.join(test_files_base_dir, "pin_map.pinmap"))
        multi_instrument_session.create_time_set(time_set_name)
        multi_instrument_session.configure_time_set_period(time_set_name, time_set_period)
        multi_instrument_session.pins['site0/PinA', 'site1/PinC'].configure_time_set_edge_multiplier(time_set_name, 2)

        multi_instrument_session.pins['site0/PinA', 'site1/PinC'].configure_time_set_drive_edges2x(
            time_set_name,
            time_set_drive_format,
            time_set_drive_on,
            time_set_drive_data,
            time_set_drive_return,
            time_set_drive_off,
            time_set_drive_data2,
            time_set_drive_return2)
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].get_time_set_drive_format(time_set_name) == time_set_drive_format
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].get_time_set_edge(
            time_set_name,
            nidigital.TimeSetEdgeType.DRIVE_ON) == time_set_drive_on
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].get_time_set_edge(
            time_set_name,
            nidigital.TimeSetEdgeType.DRIVE_DATA) == time_set_drive_data
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].get_time_set_edge(
            time_set_name,
            nidigital.TimeSetEdgeType.DRIVE_RETURN) == time_set_drive_return
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].get_time_set_edge(
            time_set_name,
            nidigital.TimeSetEdgeType.DRIVE_OFF) == time_set_drive_off
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].get_time_set_edge(
            time_set_name,
            nidigital.TimeSetEdgeType.DRIVE_DATA2) == time_set_drive_data2
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].get_time_set_edge(
            time_set_name,
            nidigital.TimeSetEdgeType.DRIVE_RETURN2) == time_set_drive_return2

    def test_configure_time_set_compare_edges_strobe2x(self, multi_instrument_session):
        time_set_name = 'time_set_abc'
        time_set_period = hightime.timedelta(microseconds=10)
        time_set_strobe = time_set_period * 0.4
        time_set_strobe2 = time_set_period * 0.8

        multi_instrument_session.load_pin_map(os.path.join(test_files_base_dir, "pin_map.pinmap"))
        multi_instrument_session.create_time_set(time_set_name)
        multi_instrument_session.configure_time_set_period(time_set_name, time_set_period)
        multi_instrument_session.pins['site0/PinA', 'site1/PinC'].configure_time_set_edge_multiplier(time_set_name, 2)

        multi_instrument_session.pins['site0/PinA', 'site1/PinC'].configure_time_set_compare_edges_strobe2x(
            time_set_name,
            time_set_strobe,
            time_set_strobe2)
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].get_time_set_edge(
            time_set_name,
            nidigital.TimeSetEdgeType.COMPARE_STROBE) == time_set_strobe
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].get_time_set_edge(
            time_set_name,
            nidigital.TimeSetEdgeType.COMPARE_STROBE2) == time_set_strobe2

    def test_enable_disable_sites_single(self, multi_instrument_session):
        '''Test methods for single site enable configuration.

        - enable_sites
        - disable_sites
        - is_site_enabled
        '''
        multi_instrument_session.load_pin_map(os.path.join(test_files_base_dir, "pin_map.pinmap"))
        assert multi_instrument_session.sites[1].is_site_enabled()

        # Single site configuration
        multi_instrument_session.sites[1].disable_sites()
        assert not multi_instrument_session.sites[1].is_site_enabled()
        multi_instrument_session.sites[1].enable_sites()
        assert multi_instrument_session.sites[1].is_site_enabled()

    def test_enable_disable_sites_multiple(self, multi_instrument_session):
        '''Test methods for multiple site enable configuration.

        - enable_sites
        - disable_sites
        - is_site_enabled
        '''
        multi_instrument_session.load_pin_map(os.path.join(test_files_base_dir, "pin_map.pinmap"))
        assert multi_instrument_session.sites[0].is_site_enabled()
        assert multi_instrument_session.sites[1].is_site_enabled()

        # Multiple site configuration
        multi_instrument_session.sites[0, 1].disable_sites()
        assert not multi_instrument_session.sites[0].is_site_enabled()
        assert not multi_instrument_session.sites[1].is_site_enabled()
        multi_instrument_session.sites[0, 1].enable_sites()
        assert multi_instrument_session.sites[0].is_site_enabled()
        assert multi_instrument_session.sites[1].is_site_enabled()

        # All site configuration
        multi_instrument_session.disable_sites()
        assert not multi_instrument_session.sites[0].is_site_enabled()
        assert not multi_instrument_session.sites[1].is_site_enabled()
        multi_instrument_session.enable_sites()
        assert multi_instrument_session.sites[0].is_site_enabled()
        assert multi_instrument_session.sites[1].is_site_enabled()

    def test_load_get_unload_patterns(self, multi_instrument_session):
        '''Test basic pattern methods.

        - load_pattern
        - unload_all_patterns
        '''
        test_name = 'multiple_patterns'
        multi_instrument_session.load_pin_map(self.get_test_file_path(test_name, 'pin_map.pinmap'))

        multi_instrument_session.load_pattern(self.get_test_file_path(test_name, 'pattern_a.digipat'))
        multi_instrument_session.load_pattern(self.get_test_file_path(test_name, 'pattern_b.digipat'))

        multi_instrument_session.unload_all_patterns(unload_keep_alive_pattern=True)

    def test_configure_pattern_burst_sites(self, multi_instrument_session):
        # Also tests initiate
        test_name = 'multiple_patterns'
        self.configure_session(multi_instrument_session, test_name)
        multi_instrument_session.load_pattern(self.get_test_file_path(test_name, 'pattern_b.digipat'))
        multi_instrument_session.start_label = 'second_pattern'
        multi_instrument_session.selected_function = nidigital.SelectedFunction.DIGITAL

        multi_instrument_session.sites[0, 2, 3].configure_pattern_burst_sites()

        multi_instrument_session.initiate()
        multi_instrument_session.wait_until_done(timeout=hightime.timedelta(seconds=5.0))
        result = multi_instrument_session.sites[0, 1, 3].get_site_pass_fail()
        assert result == {0: True, 3: True}

    def test_commit(self, multi_instrument_session):
        multi_instrument_session.cycle_number_history_ram_trigger_cycle_number = 42
        multi_instrument_session.commit()
        assert multi_instrument_session.cycle_number_history_ram_trigger_cycle_number == 42

    def test_initiate_context_manager_and_wait_until_done(self, multi_instrument_session):
        '''Test initiate's context manager and pattern completion methods.

        - with initiate
        - wait_until_done
        - is_done
        '''
        test_name = 'simple_pattern'
        self.configure_session(multi_instrument_session, test_name)
        multi_instrument_session.load_pattern(self.get_test_file_path(test_name, 'pattern.digipat'))
        multi_instrument_session.start_label = 'new_pattern'
        multi_instrument_session.selected_function = nidigital.SelectedFunction.DIGITAL

        with multi_instrument_session.initiate():
            # note that wait_until_done will return immediately with simulated hardware
            multi_instrument_session.wait_until_done(timeout=hightime.timedelta(seconds=5.0))
        assert multi_instrument_session.is_done()

    def test_abort(self, multi_instrument_session):
        test_name = 'simple_pattern'
        self.configure_session(multi_instrument_session, test_name)
        multi_instrument_session.load_pattern(self.get_test_file_path(test_name, 'pattern.digipat'))
        multi_instrument_session.start_label = 'new_pattern'
        multi_instrument_session.selected_function = nidigital.SelectedFunction.DIGITAL
        multi_instrument_session.initiate()

        multi_instrument_session.abort()

    def test_abort_keep_alive(self, multi_instrument_session):
        test_name = 'simple_pattern'
        self.configure_session(multi_instrument_session, test_name)
        multi_instrument_session.load_pattern(self.get_test_file_path(test_name, 'pattern.digipat'))
        multi_instrument_session.start_label = 'new_pattern'
        multi_instrument_session.selected_function = nidigital.SelectedFunction.DIGITAL
        multi_instrument_session.initiate()

        multi_instrument_session.abort_keep_alive()

    def test_create_source_waveform_serial(self, multi_instrument_session):
        test_name = 'test_create_source_waveform_serial'
        self.configure_session(multi_instrument_session, test_name)
        multi_instrument_session.load_pattern(self.get_test_file_path(test_name, 'pattern.digipat'))

        multi_instrument_session.pins['LO0'].create_source_waveform_serial(
            waveform_name='src_wfm',
            data_mapping=nidigital.SourceDataMapping.BROADCAST,
            sample_width=2,
            bit_order=nidigital.BitOrder.LSB)

        # load and burst the waveform to confirm that configuration went okay
        multi_instrument_session.write_source_waveform_broadcast(
            waveform_name='src_wfm',
            waveform_data=[1, 2])
        pass_fail = multi_instrument_session.burst_pattern(start_label='new_pattern')
        assert pass_fail == {0: True, 1: True}

    def test_create_source_waveform_from_file_tdms(self, multi_instrument_session):
        test_name = 'test_source_waveform_parallel_broadcast'
        self.configure_session(multi_instrument_session, test_name)
        multi_instrument_session.load_pattern(self.get_test_file_path(test_name, 'pattern.digipat'))

        multi_instrument_session.create_source_waveform_from_file_tdms(
            waveform_name='src_wfm',
            waveform_file_path=self.get_test_file_path(test_name, 'source_waveform.tdms'),
            write_waveform_data=True)

        # burst the waveform to confirm that configuration and loading went okay
        pass_fail = multi_instrument_session.burst_pattern(start_label='new_pattern')
        assert pass_fail == {0: True, 1: True}

    def test_write_source_waveform_data_from_file_tdms(self, multi_instrument_session):
        test_name = 'test_source_waveform_parallel_broadcast'
        self.configure_session(multi_instrument_session, test_name)
        multi_instrument_session.load_pattern(self.get_test_file_path(test_name, 'pattern.digipat'))

        multi_instrument_session.create_source_waveform_from_file_tdms(
            waveform_name='src_wfm',
            waveform_file_path=self.get_test_file_path(test_name, 'source_waveform.tdms'),
            write_waveform_data=False)
        try:  # confirm that the waveform is not yet loaded
            multi_instrument_session.burst_pattern(start_label='new_pattern')
            assert False
        except nidigital.Error as e:
            assert e.code == -1074118614
            assert e.description.find('The source waveform(s) used in the pattern(s) to be burst have not been written to source memory.'
                                      ' Ensure that you write source waveforms with niDigital Write Source Waveform.') != -1

        multi_instrument_session.write_source_waveform_data_from_file_tdms(
            waveform_name='src_wfm',
            waveform_file_path=self.get_test_file_path(test_name, 'source_waveform.tdms'))

        # burst the waveform to confirm that configuration and loading went okay
        pass_fail = multi_instrument_session.burst_pattern(start_label='new_pattern')
        assert pass_fail == {0: True, 1: True}

    def test_create_capture_waveform_serial(self, multi_instrument_session):
        test_name = 'test_create_capture_waveform_serial'
        self.configure_session(multi_instrument_session, test_name)
        multi_instrument_session.load_pattern(self.get_test_file_path(test_name, 'pattern.digipat'))
        num_samples = 2

        multi_instrument_session.pins['HI0'].create_capture_waveform_serial(
            waveform_name='capt_wfm',
            sample_width=2,
            bit_order=nidigital.BitOrder.LSB)

        # The pattern references a wfm 'src_wfm', so we have to load it before we can burst
        multi_instrument_session.pins['LO0'].create_source_waveform_serial(
            waveform_name='src_wfm',
            data_mapping=nidigital.SourceDataMapping.BROADCAST,
            sample_width=2,
            bit_order=nidigital.BitOrder.LSB)
        multi_instrument_session.write_source_waveform_broadcast(
            waveform_name='src_wfm',
            waveform_data=[1, 2])
        multi_instrument_session.burst_pattern(start_label='new_pattern')

        # Fetch to confirm that configuration went okay
        fetched_waveforms = multi_instrument_session.sites[1, 0].fetch_capture_waveform(
            waveform_name='capt_wfm',
            samples_to_read=num_samples)
        assert sorted(fetched_waveforms.keys()) == sorted([0, 1])
        assert all(len(fetched_waveforms[site]) == num_samples for site in fetched_waveforms)

    def test_create_capture_waveform_from_file_digicapture(self, multi_instrument_session):
        test_name = 'test_create_capture_waveform_serial'
        self.configure_session(multi_instrument_session, test_name)
        multi_instrument_session.load_pattern(self.get_test_file_path(test_name, 'pattern.digipat'))
        num_samples = 2

        multi_instrument_session.create_capture_waveform_from_file_digicapture(
            waveform_name='capt_wfm',
            waveform_file_path=self.get_test_file_path(test_name, 'capture_waveform.digicapture'))

        # The pattern references a wfm 'src_wfm', so we have to load it before we can burst
        multi_instrument_session.create_source_waveform_from_file_tdms(
            waveform_name='src_wfm',
            waveform_file_path=self.get_test_file_path(test_name, 'source_waveform.tdms'),
            write_waveform_data=True)
        multi_instrument_session.burst_pattern(start_label='new_pattern')

        # Fetch to confirm that configuration went okay
        fetched_waveforms = multi_instrument_session.sites[1, 0].fetch_capture_waveform(
            waveform_name='capt_wfm',
            samples_to_read=num_samples)
        assert sorted(fetched_waveforms.keys()) == sorted([0, 1])
        assert all(len(fetched_waveforms[site]) == num_samples for site in fetched_waveforms)

    def test_send_software_edge_trigger(self, multi_instrument_session):
        test_files_folder = 'simple_pattern'
        self.configure_session(multi_instrument_session, test_files_folder)
        multi_instrument_session.load_pattern(self.get_test_file_path(test_files_folder, 'pattern.digipat'))

        multi_instrument_session.start_trigger_type = nidigital.TriggerType.SOFTWARE
        multi_instrument_session.burst_pattern(start_label='new_pattern', wait_until_done=False)
        multi_instrument_session.send_software_edge_trigger(
            trigger=nidigital.SoftwareTrigger.START,
            trigger_identifier='')

        # We shouldn't time out, having sent the trigger, though in simulation it might complete, anyway
        multi_instrument_session.wait_until_done(timeout=hightime.timedelta(seconds=5.0))

    def test_specifications_levels_and_timing_single(self, multi_instrument_session):
        '''Test methods for loading, applying and unloading specifications, levels, and timing files.

        - apply_levels_and_timing
        - load_specifications_levels_and_timing
        - unload_specifications
        '''
        pinmap = self.get_test_file_path('specifications_levels_and_timing_single', 'pin_map.pinmap')
        specs = self.get_test_file_path('specifications_levels_and_timing_single', 'specs.specs')
        # Levels and timing files contain references to variables in specs1
        levels = self.get_test_file_path('specifications_levels_and_timing_single', 'levels.digilevels')
        timing = self.get_test_file_path('specifications_levels_and_timing_single', 'timing.digitiming')

        multi_instrument_session.load_pin_map(file_path=pinmap)
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

    def test_specifications_levels_and_timing_multiple(self, multi_instrument_session):
        '''Test methods for loading, applying and unloading multiple specifications, levels, and timing files.

        - apply_levels_and_timing
        - load_specifications_levels_and_timing
        - unload_specifications
        '''
        pinmap = self.get_test_file_path('specifications_levels_and_timing_multiple', 'pin_map.pinmap')

        specs1 = self.get_test_file_path('specifications_levels_and_timing_multiple', 'specs1.specs')
        # Contains reference to variables in specs1
        specs2 = self.get_test_file_path('specifications_levels_and_timing_multiple', 'specs2.specs')

        # All levels and timing files contain references to variables in specs1 and specs2
        levels1 = self.get_test_file_path('specifications_levels_and_timing_multiple', 'levels1.digilevels')
        levels2 = self.get_test_file_path('specifications_levels_and_timing_multiple', 'levels2.digilevels')
        timing1 = self.get_test_file_path('specifications_levels_and_timing_multiple', 'timing1.digitiming')
        timing2 = self.get_test_file_path('specifications_levels_and_timing_multiple', 'timing2.digitiming')

        multi_instrument_session.load_pin_map(file_path=pinmap)
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

    def test_specifications_levels_and_timing_load_sequentially(self, multi_instrument_session):
        '''Test methods for separately loading, applying and unloading multiple specifications, levels, and timing files.

        - apply_levels_and_timing
        - load_specifications_levels_and_timing
        - unload_specifications
        '''
        pinmap = self.get_test_file_path('specifications_levels_and_timing_multiple', 'pin_map.pinmap')

        specs1 = self.get_test_file_path('specifications_levels_and_timing_multiple', 'specs1.specs')
        # Contains reference to variables in specs1
        specs2 = self.get_test_file_path('specifications_levels_and_timing_multiple', 'specs2.specs')

        # All levels and timing files contain references to variables in specs1 and specs2
        levels1 = self.get_test_file_path('specifications_levels_and_timing_multiple', 'levels1.digilevels')
        levels2 = self.get_test_file_path('specifications_levels_and_timing_multiple', 'levels2.digilevels')
        timing1 = self.get_test_file_path('specifications_levels_and_timing_multiple', 'timing1.digitiming')
        timing2 = self.get_test_file_path('specifications_levels_and_timing_multiple', 'timing2.digitiming')

        multi_instrument_session.load_pin_map(file_path=pinmap)

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

    def test_apply_levels_and_timing_initial_states(self, multi_instrument_session):
        self.configure_session(multi_instrument_session, 'simple_pattern')
        multi_instrument_session.sites[0, 2].apply_levels_and_timing(
            levels_sheet='pin_levels',
            timing_sheet='timing',
            initial_state_high_pins=['HI0', 'LowPins'],
            initial_state_tristate_pins='HI1, HI2')


class TestLibrary(SystemTests):
    @pytest.fixture(scope='function')
    def multi_instrument_session(self):
        with nidigital.Session(resource_name=','.join(instruments), options='Simulate=1, DriverSetup=Model:6570') as simulated_session:
            yield simulated_session

    @pytest.fixture(scope='function')
    def single_instrument_session(self):
        with nidigital.Session(resource_name=instruments[0], options='Simulate=1, DriverSetup=Model:6570') as simulated_session:
            yield simulated_session

    def test_close(self):
        session = nidigital.Session(resource_name=','.join(instruments), options='Simulate=1, DriverSetup=Model:6570')
        session.vil = 1
        session.close()
        try:
            session.vil = 1
            assert False
        except nidigital.Error as e:
            assert e.code == -1074130544


class TestGrpc(SystemTests):
    server_address = "localhost"
    server_port = "31763"

    def _get_grpc_server_exe(self):
        if os.name != "nt":
            pytest.skip("Only supported on Windows")
        import winreg
        try:
            reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
            read64key = winreg.KEY_READ | winreg.KEY_WOW64_64KEY
            with winreg.OpenKey(reg, r"SOFTWARE\National Instruments\Common\Installer", access=read64key) as key:
                shared_dir, _ = winreg.QueryValueEx(key, "NISHAREDDIR64")
        except OSError:
            pytest.skip("NI gRPC Device Server not installed")
        server_exe = pathlib.Path(shared_dir) / "NI gRPC Device Server" / "ni_grpc_device_server.exe"
        if not server_exe.exists():
            pytest.skip("NI gRPC Device Server not installed")
        return server_exe

    @pytest.fixture(scope='class')
    def grpc_channel(self):
        server_exe = self._get_grpc_server_exe()
        proc = subprocess.Popen([str(server_exe)])
        time.sleep(3)
        try:
            channel = grpc.insecure_channel(f"{self.server_address}:{self.server_port}")
            yield channel
        finally:
            proc.kill()

    @pytest.fixture(scope='function')
    def multi_instrument_session(self, grpc_channel):
        grpc_options = nidigital.GrpcSessionOptions(grpc_channel, '')
        with nidigital.Session(resource_name=','.join(instruments), options='Simulate=1, DriverSetup=Model:6570', _grpc_options=grpc_options) as simulated_session:
            yield simulated_session

    @pytest.fixture(scope='function')
    def single_instrument_session(self, grpc_channel):
        grpc_options = nidigital.GrpcSessionOptions(grpc_channel, '')
        with nidigital.Session(resource_name=instruments[0], options='Simulate=1, DriverSetup=Model:6570', _grpc_options=grpc_options) as simulated_session:
            yield simulated_session

    def test_close(self, grpc_channel):
        grpc_options = nidigital.GrpcSessionOptions(grpc_channel, '')
        session = nidigital.Session(resource_name=','.join(instruments), options='Simulate=1, DriverSetup=Model:6570', _grpc_options=grpc_options)
        session.vil = 1
        session.close()
        try:
            session.vil = 1
            assert False
        except nidigital.Error as e:
            assert e.code == -1074130544
