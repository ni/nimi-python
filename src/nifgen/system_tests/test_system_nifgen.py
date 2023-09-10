import os
import pathlib
import sys
import tempfile
import warnings

import grpc
import hightime
import numpy
import pytest

import nifgen

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent / 'shared'))
import system_test_utilities  # noqa: E402


# Set up global information we need
test_files_base_dir = os.path.join(os.path.dirname(__file__))


def get_test_file_path(file_name):
    return os.path.join(test_files_base_dir, file_name)


invalid_waveforms = ['Not waveform data',
                     numpy.zeros(100, dtype=numpy.uint16),
                     numpy.zeros(100, dtype=numpy.float32),
                     42,
                     3.14159, ]


class SystemTests:
    @pytest.fixture(scope='function')
    def session(self, session_creation_kwargs):
        with nifgen.Session('', '0', False, 'Simulate=1, DriverSetup=Model:5433 (2CH);BoardType:PXIe', **session_creation_kwargs) as simulated_session:
            yield simulated_session

    def test_self_test(self, session):
        # We should not get an assert if self_test passes
        session.self_test()

    def test_get_attribute_string(self, session):
        model = session.instrument_model
        assert model == 'NI PXIe-5433 (2CH)'

    def test_error_message(self, session_creation_kwargs):
        try:
            # We pass in an invalid model name to force going to error_message
            with nifgen.Session('', '0', False, 'Simulate=1, DriverSetup=Model:invalid_model (2CH);BoardType:PXIe', **session_creation_kwargs):
                assert False
        except nifgen.Error as e:
            # The returned error has changed over time, so accept multiple error codes, descriptions.
            # Users should generally not look for specific error codes and should instead correct their code if they hit an error.
            assert e.code in [-1074134944, -1074134964]
            assert any(
                [
                    e.description.find('Insufficient location information or resource not present in the system.') != -1,
                    e.description.find('The option string parameter contains an entry with an unknown option value.') != -1,
                ]
            )

    def test_get_error(self, session):
        try:
            session.instrument_model = ''
            assert False
        except nifgen.Error as e:
            assert e.code == -1074135027  # Error : Attribute is read-only.
            assert e.description.find('Attribute is read-only.') != -1

    def test_method_get_self_cal_supported(self, session):
        assert session.get_self_cal_supported() in [True, False]

    def test_get_self_cal_last_date_and_time(self, session):
        try:
            session.get_self_cal_last_date_and_time()
            assert False
        except nifgen.Error as e:
            assert e.code == -1074118632  # This operation is not supported for simulated device

    def test_self_cal(self, session):
        session.self_cal()

    def test_channels_rep_cap(self):
        with nifgen.Session('', '', False, 'Simulate=1, DriverSetup=Model:5433 (2CH);BoardType:PXIe') as session:
            session.func_amplitude = 0.5
            assert session.channels[0:1].func_amplitude == 0.5

            session.channels[0].func_amplitude = 1
            assert session.channels[0].func_amplitude == 1
            assert session.channels[1].func_amplitude == 0.5

    def test_markers_rep_cap(self, session):
        assert '' == session.markers[0].marker_event_output_terminal

        requested_terminal_name = '/Dev1/PXI_Trig0'
        session.markers[0].marker_event_output_terminal = requested_terminal_name
        assert requested_terminal_name == session.markers[0].marker_event_output_terminal

    def test_data_markers_rep_cap(self, session):
        assert nifgen.DataMarkerEventLevelPolarity.HIGH == session.data_markers[0].data_marker_event_level_polarity

        requested_polarity = nifgen.DataMarkerEventLevelPolarity.LOW
        session.data_markers[0].data_marker_event_level_polarity = requested_polarity
        assert requested_polarity == session.data_markers[0].data_marker_event_level_polarity

    def test_script_triggers_rep_cap(self, session):
        assert '' == session.script_triggers[0].exported_script_trigger_output_terminal

        requested_terminal_name = '/Dev1/PXI_Trig0'
        session.script_triggers[0].exported_script_trigger_output_terminal = requested_terminal_name
        assert requested_terminal_name == session.script_triggers[0].exported_script_trigger_output_terminal

    def test_standard_waveform(self, session):
        session.output_mode = nifgen.OutputMode.FUNC
        session.configure_standard_waveform(nifgen.Waveform.SINE, 2.0, 2000000, 1.0, 0.0)
        expected_frequency = 2000000
        with session.initiate():
            assert session.func_amplitude == 2.0
            assert session.func_waveform == nifgen.Waveform.SINE
            actual_frequency = session.func_frequency
            in_range = abs(actual_frequency - expected_frequency) <= max(1e-09 * max(abs(actual_frequency), abs(expected_frequency)), 0.0)   # https://stackoverflow.com/questions/5595425/what-is-the-best-way-to-compare-floats-for-almost-equality-in-python
            assert in_range is True
            assert session.func_dc_offset == 1.0
            assert session.func_start_phase == 0.0
            assert session.is_done() is False

    def test_frequency_list(self, session):
        session.output_mode = nifgen.OutputMode.FREQ_LIST
        duration_array = [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]
        frequency_array = [1000, 100900, 200800, 300700, 400600, 500500, 600400, 700300, 800200, 900100]
        waveform_handle = session.create_freq_list(nifgen.Waveform.SQUARE, frequency_array, duration_array)
        session.configure_freq_list(waveform_handle, 2.0, 0, 0)
        session.trigger_mode = nifgen.TriggerMode.CONTINUOUS
        session.output_enabled = True
        assert session.func_waveform == nifgen.Waveform.SQUARE
        assert session.func_amplitude == 2.0

    def test_clear_freq_list(self, session):
        session.clear_freq_list(-1)

    def test_create_waveform_from_list(self, session):
        data = [0.1] * 10000
        assert type(session.create_waveform(data)) is int

    def test_configure_arb_waveform(self, session):
        waveform_data = [x * (1.0 / 256.0) for x in range(256)]
        session.output_mode = nifgen.OutputMode.ARB
        session.configure_arb_waveform(session.create_waveform(waveform_data), 1.0, 0.0)

    def test_disable(self, session):
        channel = session.channels['0']
        assert channel.output_enabled is True
        session.disable()
        assert channel.output_enabled is False

    def test_get_ext_cal_last_date_and_time(self, session):
        try:
            session.get_ext_cal_last_date_and_time()
            assert False, "If we hit this, it means a simulated 5433 now works properly for this. You can now remove the check for -1074135040"
        except nifgen.Error as e:
            assert e.code == -1074118632 or e.code == -1074135040  # This operation is not supported for simulated device or Unrecoverable Failure

    def test_get_ext_cal_last_temp(self, session):
        try:
            session.get_ext_cal_last_temp()
        except nifgen.Error as e:
            assert e.code == -1074135023  # Function or method not supported for 5413/23/33 and not supported on any other FGen when simulated

    def test_get_ext_cal_recommended_interval(self, session):
        interval = session.get_ext_cal_recommended_interval()
        assert interval.days == 730  # recommended external cal interval is 24 months

    def test_get_hardware_state(self, session):
        assert session.get_hardware_state() == nifgen.HardwareState.IDLE

    def test_get_self_cal_last_temp(self, session):
        assert session.get_self_cal_last_temp() == 0.0  # returns 0.0 for a simulated 5433

    def test_query_arb_wfm_capabilities(self, session):
        max_number_of_waveform, waveform_quantum, minimum_waveform_size, maximum_waveform_size = session.query_arb_wfm_capabilities()
        assert max_number_of_waveform == 4194304  # default values for max_number_of_waveform, waveform_quantum, minimum_waveform_size, maximum_waveform_size for a simulated 5433 is 4194304, 1, 4, 268435456 respectively
        assert waveform_quantum == 1
        assert minimum_waveform_size == 4
        assert maximum_waveform_size == 268435456

    def test_query_freq_list_capabilities(self, session):
        maximum_number_of_freq_lists, minimum_frequency_list_length, maximum_frequency_list_length, minimum_frequency_list_duration, maximum_frequency_list_duration, frequency_list_duration_quantum = session.query_freq_list_capabilities()  # comparing with default values for simulated 5433
        assert maximum_number_of_freq_lists == 9999
        assert minimum_frequency_list_length == 1
        assert maximum_frequency_list_length == 1024
        assert minimum_frequency_list_duration == 1e-08
        assert maximum_frequency_list_duration == 2814749.76711
        assert frequency_list_duration_quantum == 1e-08

    def test_read_current_temperature(self, session):
        assert session.read_current_temperature() > 25.0

    def test_allocate_waveform(self, session):
        handles = [session.allocate_waveform(100) in range(10)]
        assert len(handles) == len(set(handles)), "Failed, waveform handles aren't unique."
        try:
            session.allocate_waveform(2000000000)
            assert False
        except nifgen.Error as e:
            assert e.code == -1074101596  # Such a big waveform doesn't fit!

    def test_clear_waveform_memory(self, session):
        session.clear_arb_memory()
        session.clear_user_standard_waveform()
        session.configure_arb_sequence(0, 1.0, 0)
        session.clear_arb_sequence(-1)
        session.delete_waveform(-1)

    def test_query_arb_seq_capabilities(self, session):
        maximum_number_of_sequences, minimum_sequence_length, maximum_sequence_length, maximum_loop_count = session.query_arb_seq_capabilities()
        assert maximum_number_of_sequences == 65535
        assert minimum_sequence_length == 1
        assert maximum_sequence_length == 65535
        assert maximum_loop_count == 16777215

    def test_create_arb_sequence(self, session):
        waveform_data = [x * (1.0 / 256.0) for x in range(256)]
        waveform_handles_array = [session.create_waveform(waveform_data)]
        # This relies on value of sequence handles starting at 0 and incrementing, not ideal but true for now.
        assert 0 == session.create_arb_sequence(waveform_handles_array, [10])
        assert 1 == session.create_arb_sequence(waveform_handles_array, [10])

    def test_create_advanced_arb_sequence(self, session):
        seq_handle_base = 100000  # This is not necessary on 5433 because handles start at 0.
        waveform_data = [x * (1.0 / 256.0) for x in range(256)]
        waveform_handles_array = [session.create_waveform(waveform_data), session.create_waveform(waveform_data), session.create_waveform(waveform_data)]
        marker_location_array = [0, 16, 32]
        sample_counts_array = [256, 128, 64]
        loop_counts_array = [10, 20, 30]
        session.output_mode = nifgen.OutputMode.SEQ
        # Test relies on value of sequence handles starting at a known value and incrementing sequentially. Hardly ideal.
        assert ([], seq_handle_base + 0) == session.create_advanced_arb_sequence(waveform_handles_array, loop_counts_array=loop_counts_array)
        assert ([], seq_handle_base + 1) == session.create_advanced_arb_sequence(waveform_handles_array, loop_counts_array=loop_counts_array, sample_counts_array=sample_counts_array)
        assert (marker_location_array, seq_handle_base + 2) == session.create_advanced_arb_sequence(waveform_handles_array, loop_counts_array=loop_counts_array, marker_location_array=marker_location_array)
        assert (marker_location_array, seq_handle_base + 3) == session.create_advanced_arb_sequence(waveform_handles_array, loop_counts_array=loop_counts_array, sample_counts_array=sample_counts_array, marker_location_array=marker_location_array)

    def test_arb_script(self, session):
        waveform_data = [x * (1.0 / 256.0) for x in range(256)]
        session.output_mode = nifgen.OutputMode.SCRIPT
        session.script_triggers[0].digital_edge_script_trigger_source = 'PFI0'
        session.script_triggers[0].digital_edge_script_trigger_edge = nifgen.ScriptTriggerDigitalEdgeEdge.RISING
        session.write_waveform('wfmSine', waveform_data)
        session.arb_sample_rate = 10000000
        script = '''script myScript0
        repeat 3
        Generate wfmSine
        end repeat
        end script'''
        session.write_script(script)
        session.script_to_generate = 'myScript0'
        session.commit()
        session.delete_script('myScript0')
        actual_sample_rate = session.arb_sample_rate
        in_range = abs(actual_sample_rate - 10000000) <= max(1e-09 * max(abs(actual_sample_rate), abs(10000000)), 0.0)   # https://stackoverflow.com/questions/5595425/what-is-the-best-way-to-compare-floats-for-almost-equality-in-python
        assert in_range is True

    def test_reset(self, session):
        default_output_mode = session.output_mode
        assert default_output_mode == nifgen.OutputMode.ARB
        session.output_mode = nifgen.OutputMode.SEQ
        assert session.output_mode == nifgen.OutputMode.SEQ
        session.reset()
        assert session.output_mode == nifgen.OutputMode.ARB

    def test_reset_device(self, session):
        default_trigger_mode = session.trigger_mode
        assert default_trigger_mode == nifgen.TriggerMode.CONTINUOUS
        session.trigger_mode = nifgen.TriggerMode.STEPPED
        non_default_trigger_mode = nifgen.TriggerMode.STEPPED
        assert non_default_trigger_mode == nifgen.TriggerMode.STEPPED
        session.reset_device()
        assert session.trigger_mode == nifgen.TriggerMode.CONTINUOUS

    def test_reset_with_default(self, session):
        default_sample_rate = session.arb_sample_rate
        assert default_sample_rate == 250000000.0
        session.arb_sample_rate = 100000000.0
        non_default_arb_sample_rate = session.arb_sample_rate
        assert non_default_arb_sample_rate == 100000000.0
        session.reset_with_defaults()
        assert session.arb_sample_rate == 250000000.0

    def test_write_waveform_from_list(self, session):
        data = [0.1] * 10000
        session.write_waveform(session.allocate_waveform(len(data)), data)

    def test_write_named_waveform_from_list(self, session):
        data = [0.1] * 10000
        session.allocate_named_waveform('foo', len(data))
        session.write_waveform('foo', data)

    def test_write_waveform_wrong_type(self, session):
        waveform_handle = session.allocate_waveform(100)
        for data in invalid_waveforms:
            try:
                session.write_waveform(waveform_handle, data)
                assert False
            except (TypeError, ValueError):
                pass

    def test_set_waveform_next_write_position(self, session):
        session.set_next_write_position(session.allocate_waveform(10), nifgen.RelativeTo.START, 5)

    def test_write_waveform_from_filei64(self, session):
        session.create_waveform_from_file_i16(get_test_file_path('SineI16BigEndian_1000.bin'), nifgen.ByteOrder.BIG)

    def test_named_waveform_operations(self, session):
        waveform_name = 'Waveform'
        waveform_size = 4096
        write_offset = 0
        waveform_data_1 = [x * (1.0 / 256.0) for x in range(256)]
        waveform_data_2 = [x * (-1.0 / 256.0) for x in range(256)]
        session.allocate_named_waveform(waveform_name, waveform_size)
        session.set_next_write_position(waveform_name, nifgen.RelativeTo.START, write_offset)
        session.write_waveform(waveform_name, waveform_data_1)
        session.write_waveform(waveform_name, waveform_data_2)
        session.delete_waveform(waveform_name)

    def test_handle_waveform_operations(self, session):
        waveform_data = [x * (1.0 / 256.0) for x in range(256)]
        waveform_handle = session.create_waveform(waveform_data_array=waveform_data)
        session.delete_waveform(waveform_handle)

    def test_write_waveform_from_file_f64(self, session):
        try:
            session.create_waveform_from_file_f64(get_test_file_path('SineI16BigEndian_1000.bin'), nifgen.ByteOrder.BIG)
        except nifgen.Error as e:
            assert e.code == -1074135024  # Expecting error since loading an I16 file when f64 is expected.

    def test_wait_until_done(self, session):
        session.wait_until_done(hightime.timedelta(milliseconds=20))

    def test_user_standard_waveform(self, session):
        wfm_points = [1] * 8192
        session.output_mode = nifgen.OutputMode.FUNC
        session.configure_standard_waveform(nifgen.Waveform.USER, 1.0, 2000000, 1.0, 0.0)
        session.define_user_standard_waveform(wfm_points)
        session.clear_user_standard_waveform()

    ''' Removed due to OSP disabled - #891
    def test_fir_filter_coefficients(self, session_creation_kwargs):
        with nifgen.Session('', '0', False, 'Simulate=1, DriverSetup=Model:5441;BoardType:PXI', **session_creation_kwargs) as session:
            coeff_array = [0 for i in range(95)]
            coeff_array[0] = -1.0
            coeff_array[2] = 1.0
            session.configure_custom_fir_filter_coefficients(coeff_array)
            session.commit()
            array = session.get_fir_filter_coefficients()
            assert len(array) == len(coeff_array)
            assert array == coeff_array
    '''

    def test_send_software_edge_trigger_start_deprecated(self, session):
        warnings.filterwarnings("always", category=DeprecationWarning)

        waveform_data = [x * (1.0 / 256.0) for x in range(256)]
        session.create_waveform(waveform_data)
        with session.initiate():
            with warnings.catch_warnings(record=True) as w:
                session.send_software_edge_trigger()
                assert len(w) == 1
                assert issubclass(w[0].category, DeprecationWarning)

    def test_send_software_edge_trigger_script_deprecated(self, session):
        warnings.filterwarnings("always", category=DeprecationWarning)

        waveform_data = [x * (1.0 / 256.0) for x in range(256)]
        session.create_waveform(waveform_data)
        session.output_mode = nifgen.OutputMode.SCRIPT
        session.script_triggers[0].digital_edge_script_trigger_source = 'PFI0'
        session.script_triggers[0].digital_edge_script_trigger_edge = nifgen.ScriptTriggerDigitalEdgeEdge.RISING
        with session.initiate():
            with warnings.catch_warnings(record=True) as w:
                session.script_triggers[0].send_software_edge_trigger()
                assert len(w) == 1
                assert issubclass(w[0].category, DeprecationWarning)

    def test_send_software_edge_trigger_start(self, session):
        waveform_data = [x * (1.0 / 256.0) for x in range(256)]
        session.create_waveform(waveform_data)
        with session.initiate():
            session.send_software_edge_trigger(nifgen.Trigger.START, 'None')

    def test_send_software_edge_trigger_script(self, session):
        waveform_data = [x * (1.0 / 256.0) for x in range(256)]
        session.create_waveform(waveform_data)
        session.output_mode = nifgen.OutputMode.SCRIPT
        session.script_triggers[0].digital_edge_script_trigger_source = 'PFI0'
        session.script_triggers[0].digital_edge_script_trigger_edge = nifgen.ScriptTriggerDigitalEdgeEdge.RISING
        with session.initiate():
            session.send_software_edge_trigger(nifgen.Trigger.SCRIPT, 'ScriptTrigger0')

    def test_channel_format_types(self, session_creation_kwargs):
        with nifgen.Session('', [0, 1], False, 'Simulate=1, DriverSetup=Model:5433 (2CH);BoardType:PXIe', **session_creation_kwargs) as simulated_session:
            assert simulated_session.channel_count == 2
        with nifgen.Session('', range(2), False, 'Simulate=1, DriverSetup=Model:5433 (2CH);BoardType:PXIe', **session_creation_kwargs) as simulated_session:
            assert simulated_session.channel_count == 2
        with nifgen.Session('', '0,1', False, 'Simulate=1, DriverSetup=Model:5433 (2CH);BoardType:PXIe', **session_creation_kwargs) as simulated_session:
            assert simulated_session.channel_count == 2
        with nifgen.Session('', None, False, 'Simulate=1, DriverSetup=Model:5433 (2CH); BoardType:PXIe', **session_creation_kwargs) as simulated_session:
            assert simulated_session.channel_count == 2
        with nifgen.Session(resource_name='', reset_device=False, options='Simulate=1, DriverSetup=Model:5433 (2CH); BoardType:PXIe', **session_creation_kwargs) as simulated_session:
            assert simulated_session.channel_count == 2

    def test_import_export_buffer(self, session):
        test_value_1 = 1.0
        test_value_2 = 2.0
        session.arb_gain = test_value_1
        assert session.arb_gain == test_value_1
        buffer = session.export_attribute_configuration_buffer()
        session.arb_gain = test_value_2
        assert session.arb_gain == test_value_2
        session.import_attribute_configuration_buffer(buffer)
        assert session.arb_gain == test_value_1

    def test_import_export_file(self, session):
        test_value_1 = 2.0
        test_value_2 = 3.0
        temp_file = tempfile.NamedTemporaryFile(suffix='.txt', delete=False)
        # NamedTemporaryFile() returns the file already opened, so we need to close it before we can use it
        temp_file.close()
        path = temp_file.name
        session.arb_gain = test_value_1
        assert session.arb_gain == test_value_1
        session.export_attribute_configuration_file(path)
        session.arb_gain = test_value_2
        assert session.arb_gain == test_value_2
        session.import_attribute_configuration_file(path)
        assert session.arb_gain == test_value_1
        os.remove(path)

    def test_get_channel_name(self, session):
        name = session.get_channel_name(1)
        assert name == '0'

    def test_create_waveform_wrong_type(self, session):
        for data in invalid_waveforms:
            try:
                session.create_waveform(data)
                assert False
            except (TypeError, ValueError):
                pass

    def test_create_advanced_arb_sequence_wrong_size(self, session):
        waveform_data = [x * (1.0 / 256.0) for x in range(256)]
        waveform_handles_array = [session.create_waveform(waveform_data), session.create_waveform(waveform_data), session.create_waveform(waveform_data)]
        marker_location_array = [0, 16]
        loop_counts_array = [10, 20, 30]
        session.output_mode = nifgen.OutputMode.SEQ
        # Test relies on value of sequence handles starting at a known value and incrementing sequentially. Hardly ideal.
        with pytest.raises(ValueError) as exc_info:
            session.create_advanced_arb_sequence(waveform_handles_array, loop_counts_array=loop_counts_array, marker_location_array=marker_location_array)
        assert exc_info.value.args[0] == 'Length of marker_location_array and waveform_handles_array parameters do not match.'
        assert str(exc_info.value) == 'Length of marker_location_array and waveform_handles_array parameters do not match.'

    # Multi-Threading tests
    def test_multi_threading_lock_unlock(self, session):
        system_test_utilities.impl_test_multi_threading_lock_unlock(session)

    def test_multi_threading_ivi_synchronized_wrapper_releases_lock(self, session):
        system_test_utilities.impl_test_multi_threading_ivi_synchronized_wrapper_releases_lock(
            session.abort)


class TestLibrary(SystemTests):
    @pytest.fixture(scope='class')
    def session_creation_kwargs(self):
        return {}

    # Test doesn't run over gRPC because numpy isn't supported by gRPC.
    def test_create_waveform_from_numpy_array_float64(self, session):
        data = numpy.ndarray(10000, dtype=numpy.float64)
        data.fill(0.5)
        assert type(session.create_waveform(data)) is int

    # Test doesn't run over gRPC because numpy isn't supported by gRPC.
    def test_create_waveform_numpy_array_int16(self, session):
        data = numpy.ndarray(10000, dtype=numpy.int16)
        data.fill(256)
        assert type(session.create_waveform(data)) is int

    # Test doesn't run over gRPC because numpy isn't supported by gRPC.
    def test_write_waveform_from_numpy_array_float64(self, session):
        data = numpy.ndarray(10000, dtype=numpy.float64)
        data.fill(0.5)
        session.write_waveform(session.allocate_waveform(len(data)), data)

    # Test doesn't run over gRPC because numpy isn't supported by gRPC.
    def test_write_waveform_numpy_array_int16(self, session):
        data = numpy.ndarray(10000, dtype=numpy.int16)
        data.fill(256)
        session.write_waveform(session.allocate_waveform(len(data)), data)

    # Test doesn't run over gRPC because numpy isn't supported by gRPC.
    def test_write_named_waveform_from_numpy_array_float64(self, session):
        data = numpy.ndarray(10000, dtype=numpy.float64)
        data.fill(0.5)
        session.allocate_named_waveform('foo', len(data))
        session.write_waveform('foo', data)

    # Test doesn't run over gRPC because numpy isn't supported by gRPC.
    def test_write_named_waveform_numpy_array_int16(self, session):
        data = numpy.ndarray(10000, dtype=numpy.int16)
        data.fill(256)
        session.allocate_named_waveform('foo', len(data))
        session.write_waveform('foo', data)


class TestGrpc(SystemTests):
    @pytest.fixture(scope='class')
    def grpc_channel(self):
        with system_test_utilities.GrpcServerProcess() as proc:
            channel = grpc.insecure_channel(f"localhost:{proc.server_port}")
            yield channel

    @pytest.fixture(scope='class')
    def session_creation_kwargs(self, grpc_channel):
        grpc_options = nifgen.GrpcSessionOptions(grpc_channel, '')
        return {'grpc_options': grpc_options}
