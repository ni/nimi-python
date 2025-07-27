import array
import hightime
import nirfsg
import numpy as np
import os
import pathlib
import pytest
import sys
import time


sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent / 'shared'))
import system_test_utilities  # noqa: E402

# Set up global information we need
test_files_base_dir = os.path.join(os.path.dirname(__file__))
use_simulated_session = True
real_hw_resource_name = '5841'


def get_test_file_path(file_name):
    return os.path.join(test_files_base_dir, file_name)


sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent / 'generated/nirfsg'))


class SystemTests:
    @pytest.fixture(scope='function')
    def rfsg_device_session(self, session_creation_kwargs):
        if use_simulated_session:
            with nirfsg.Session("5841sim", options="Simulate=1, DriverSetup=Model:5841", **session_creation_kwargs) as sim_5841_session:
                yield sim_5841_session
        else:
            with nirfsg.Session(real_hw_resource_name, **session_creation_kwargs) as real_rfsg_device_session:
                yield real_rfsg_device_session

    @pytest.fixture(scope='function')
    def simulated_5831_device_session(self, session_creation_kwargs):
        with nirfsg.Session("5831sim", options="Simulate=1, DriverSetup=Model:5831", **session_creation_kwargs) as sim_5831_session:
            yield sim_5831_session

# Attribute set and get related tests
    def test_get_float_attribute(self, rfsg_device_session):
        value = rfsg_device_session.power_level
        assert isinstance(value, float)

    def test_set_float_attribute(self, rfsg_device_session):
        rfsg_device_session.power_level = -3.0
        assert rfsg_device_session.power_level == -3.0

    def test_get_string_attribute(self, rfsg_device_session):
        model = rfsg_device_session.instrument_model
        assert model == "NI PXIe-5841"

    def test_set_string_attribute(self, rfsg_device_session):
        rfsg_device_session.selected_script = "myScript"
        assert rfsg_device_session.selected_script == "myScript"

    def test_get_int32_attribute(self, rfsg_device_session):
        value = rfsg_device_session.external_calibration_recommended_interval
        assert isinstance(value, int)

    def test_set_int32_enum_attribute(self, rfsg_device_session):
        rfsg_device_session.frequency_settling_units = nirfsg.FrequencySettlingUnits.TIME_AFTER_LOCK
        assert rfsg_device_session.frequency_settling_units == nirfsg.FrequencySettlingUnits.TIME_AFTER_LOCK

    def test_set_invalid_attribute_raises(self, rfsg_device_session):
        with pytest.raises(AttributeError):
            rfsg_device_session.non_existent_attribute = 123

# Multi-threading related tests
    def test_multi_threading_lock_unlock(self, rfsg_device_session):
        system_test_utilities.impl_test_multi_threading_lock_unlock(rfsg_device_session)

    def test_multi_threading_ivi_synchronized_wrapper_releases_lock(self, rfsg_device_session):
        system_test_utilities.impl_test_multi_threading_ivi_synchronized_wrapper_releases_lock(rfsg_device_session.abort)

# Error handling related tests
    def test_error_message(self, session_creation_kwargs):
        try:
            with nirfsg.Session(resource_name="invalid_model", id_query=False, reset_device=False, options="Simulate=1, DriverSetup=Model:invalid_model", **session_creation_kwargs):
                assert False
        except nirfsg.Error as e:
            assert e.code == -1074135025
            assert "Invalid model in DriverSetup string" in e.description

    def test_get_error(self, rfsg_device_session):
        try:
            rfsg_device_session.instrument_model = ''
            assert False
        except nirfsg.Error as e:
            assert e.code == -1074135027
            assert "Attribute is read-only" in e.description

# Utility method tests
    def test_reset(self, rfsg_device_session):
        default_power_level = rfsg_device_session.power_level
        rfsg_device_session.power_level = default_power_level + 1.0
        assert rfsg_device_session.power_level == default_power_level + 1.0
        rfsg_device_session.reset()
        assert rfsg_device_session.power_level == default_power_level

    def test_reset_with_options(self, rfsg_device_session):
        rfsg_device_session.generation_mode = nirfsg.GenerationMode.ARB_WAVEFORM
        waveform_data = np.full(1000, 1 + 0j, dtype=np.complex128)
        rfsg_device_session.write_arb_waveform('mywaveform', waveform_data, False)
        default_power_level = rfsg_device_session.power_level
        rfsg_device_session.power_level = default_power_level + 1.0
        assert rfsg_device_session.power_level == default_power_level + 1.0
        steps_to_omit_without_waveforms = nirfsg.ResetWithOptionsStepsToOmit.ROUTES
        steps_to_omit_with_waveforms = nirfsg.ResetWithOptionsStepsToOmit.WAVEFORMS | nirfsg.ResetWithOptionsStepsToOmit.ROUTES
        rfsg_device_session.reset_with_options(steps_to_omit_with_waveforms)
        assert rfsg_device_session.power_level == default_power_level
        waveform_exists = rfsg_device_session.check_if_waveform_exists('mywaveform')
        assert waveform_exists is True
        rfsg_device_session.reset_with_options(steps_to_omit_without_waveforms)
        waveform_exists = rfsg_device_session.check_if_waveform_exists('mywaveform')
        assert waveform_exists is False

    @pytest.mark.skipif(use_simulated_session is False, reason="Takes long time in real device")
    def test_self_cal(self, rfsg_device_session):
        rfsg_device_session.self_cal()

    @pytest.mark.skipif(use_simulated_session is False, reason="Takes long time in real device")
    def test_self_cal_range(self, rfsg_device_session):
        steps_to_omit = nirfsg.SelfCalibrateRangeStepsToOmit.LO_SELF_CAL | nirfsg.SelfCalibrateRangeStepsToOmit.IMAGE_SUPPRESSION
        rfsg_device_session.self_calibrate_range(steps_to_omit, 1e9, 2e9, -20, 0)

    def test_clear_self_calibrate_range(self, rfsg_device_session):
        rfsg_device_session.clear_self_calibrate_range()

    @pytest.mark.skipif(use_simulated_session is True, reason="Bad date returned by driver for simulated device")
    def test_get_external_calibration_last_date_and_time(self, rfsg_device_session):
        dt = rfsg_device_session.get_external_calibration_last_date_and_time()
        assert isinstance(dt, hightime.datetime)

    @pytest.mark.skipif(use_simulated_session is True, reason="Bad date returned by driver for simulated device")
    def test_get_self_calibration_last_date_and_time(self, rfsg_device_session):
        dt = rfsg_device_session.get_self_calibration_last_date_and_time(nirfsg.Module.PRIMARY_MODULE)
        assert isinstance(dt, hightime.datetime)

    def test_get_terminal_name(self, rfsg_device_session):
        terminal_name = rfsg_device_session.get_terminal_name(nirfsg.Signal.MARKER_EVENT, 'marker3')
        assert '/ao/0/Marker3Event' in terminal_name

    def test_query_arb_waveform_capabilities(self, rfsg_device_session):
        max_number_waveforms, waveform_quantum, min_waveform_size, max_waveform_size = rfsg_device_session.query_arb_waveform_capabilities()
        assert max_number_waveforms == 67108864
        assert waveform_quantum == 1
        assert min_waveform_size == 8
        assert max_waveform_size == 536870912

# Repeated capability tests
    def test_markers_rep_cap(self, rfsg_device_session):
        marker = rfsg_device_session.markers[0]
        requested_terminal_name = '/Dev0/PXI_Trig0'
        marker.exported_marker_event_output_terminal = requested_terminal_name
        assert marker.exported_marker_event_output_terminal == requested_terminal_name

    def test_script_triggers_rep_cap(self, rfsg_device_session):
        trigger = rfsg_device_session.script_triggers[0]
        requested_terminal_name = '/Dev0/PXI_Trig0'
        trigger.exported_script_trigger_output_terminal = requested_terminal_name
        assert trigger.exported_script_trigger_output_terminal == requested_terminal_name

    def test_waveforms_rep_cap(self, rfsg_device_session):
        rfsg_device_session.generation_mode = nirfsg.GenerationMode.ARB_WAVEFORM
        waveform_data = np.full(1000, 1 + 0j, dtype=np.complex128)
        rfsg_device_session.write_arb_waveform('mywaveform', waveform_data, False)
        requested_waveform_iq_rate = 1e6
        rfsg_device_session.waveforms['mywaveform'].waveform_iq_rate = requested_waveform_iq_rate
        assert rfsg_device_session.waveforms['mywaveform'].waveform_iq_rate == requested_waveform_iq_rate

    def test_ports_rep_cap(self, simulated_5831_device_session):
        requested_deembedding_type = nirfsg.DeembeddingType.SCALAR
        simulated_5831_device_session.ports['if1'].deembedding_type = requested_deembedding_type
        assert simulated_5831_device_session.ports['if1'].deembedding_type == requested_deembedding_type

    def test_los_rep_cap(self, simulated_5831_device_session):
        requested_lo_source = "SG_SA_Shared"
        simulated_5831_device_session.los[2].lo_source = requested_lo_source
        assert simulated_5831_device_session.los[2].lo_source == requested_lo_source

# Configuration methods related tests
    def test_configure_rf(self, rfsg_device_session):
        rfsg_device_session.configure_rf(2e9, -5.0)
        assert rfsg_device_session.power_level == -5.0
        assert rfsg_device_session.frequency == 2e9

    def test_write_arb_waveform_numpy_complex128(self, rfsg_device_session):
        rfsg_device_session.generation_mode = nirfsg.GenerationMode.ARB_WAVEFORM
        waveform_data = np.full(1000, 1 + 0j, dtype=np.complex128)
        rfsg_device_session.write_arb_waveform('mywaveform1', waveform_data, False)
        waveform_exists = rfsg_device_session.check_if_waveform_exists('mywaveform1')
        assert waveform_exists is True
        waveform_exists = rfsg_device_session.check_if_waveform_exists('mywaveform2')
        assert waveform_exists is False

    def test_write_arb_waveform_numpy_complex64(self, rfsg_device_session):
        rfsg_device_session.generation_mode = nirfsg.GenerationMode.ARB_WAVEFORM
        waveform_data = np.full(1600, 1 + 0j, dtype=np.complex64)
        rfsg_device_session.write_arb_waveform('mywaveform2', waveform_data, False)
        waveform_exists = rfsg_device_session.check_if_waveform_exists('mywaveform2')
        assert waveform_exists is True
        waveform_exists = rfsg_device_session.check_if_waveform_exists('mywaveform3')
        assert waveform_exists is False

    def test_write_arb_waveform_numpy_interleaved_int16(self, rfsg_device_session):
        rfsg_device_session.generation_mode = nirfsg.GenerationMode.ARB_WAVEFORM
        rfsg_device_session.power_level_type = nirfsg.PowerLevelType.PEAK  # Needed for writing unscaled int16 data
        waveform_data = np.array([1, 0] * 3000, dtype=np.int16)
        rfsg_device_session.write_arb_waveform('mywaveform3', waveform_data, False)
        waveform_exists = rfsg_device_session.check_if_waveform_exists('mywaveform3')
        assert waveform_exists is True
        waveform_exists = rfsg_device_session.check_if_waveform_exists('mywaveform1')
        assert waveform_exists is False

    def test_write_arb_waveform_with_wrong_datatype(self, rfsg_device_session):
        rfsg_device_session.generation_mode = nirfsg.GenerationMode.ARB_WAVEFORM
        waveform_data_wrong_numpy_type = np.array([1, 0] * 3000, dtype=np.int32)
        waveform_data_non_numpy_type = array.array('h', [1, 0] * 3000)
        try:
            rfsg_device_session.write_arb_waveform('mywaveform3', waveform_data_wrong_numpy_type, False)
            assert False
        except TypeError:
            pass
        try:
            rfsg_device_session.write_arb_waveform('mywaveform1', waveform_data_non_numpy_type, False)
            assert False
        except TypeError:
            pass

    def test_clear_arb_waveform(self, rfsg_device_session):
        rfsg_device_session.generation_mode = nirfsg.GenerationMode.ARB_WAVEFORM
        waveform_data = np.full(1000, 1 + 0j, dtype=np.complex128)
        rfsg_device_session.write_arb_waveform('mywaveform1', waveform_data, False)
        waveform_exists = rfsg_device_session.check_if_waveform_exists('mywaveform1')
        assert waveform_exists is True
        rfsg_device_session.clear_arb_waveform('mywaveform1')
        waveform_exists = rfsg_device_session.check_if_waveform_exists('mywaveform1')
        assert waveform_exists is False

    def test_clear_all_arb_waveforms(self, rfsg_device_session):
        rfsg_device_session.generation_mode = nirfsg.GenerationMode.ARB_WAVEFORM
        waveform_data = np.full(1000, 1 + 0j, dtype=np.complex128)
        rfsg_device_session.write_arb_waveform('mywaveform1', waveform_data, False)
        rfsg_device_session.write_arb_waveform('mywaveform2', waveform_data, False)
        waveform_exists = rfsg_device_session.check_if_waveform_exists('mywaveform1')
        assert waveform_exists is True
        waveform_exists = rfsg_device_session.check_if_waveform_exists('mywaveform2')
        assert waveform_exists is True
        rfsg_device_session.clear_all_arb_waveforms()
        waveform_exists = rfsg_device_session.check_if_waveform_exists('mywaveform1')
        assert waveform_exists is False
        waveform_exists = rfsg_device_session.check_if_waveform_exists('mywaveform2')
        assert waveform_exists is False

    def test_allocate_arb_waveform(self, rfsg_device_session):
        rfsg_device_session.generation_mode = nirfsg.GenerationMode.ARB_WAVEFORM
        rfsg_device_session.power_level_type = nirfsg.PowerLevelType.PEAK  # To be able to call write multiple times on same waveform
        waveform_data = np.full(1000, 1 + 0j, dtype=np.complex128)
        rfsg_device_session.allocate_arb_waveform('foo', len(waveform_data) * 2)
        rfsg_device_session.write_arb_waveform('foo', waveform_data, True)
        rfsg_device_session.write_arb_waveform('foo', waveform_data, False)

    def test_set_arb_waveform_next_write_position(self, rfsg_device_session):
        rfsg_device_session.generation_mode = nirfsg.GenerationMode.ARB_WAVEFORM
        rfsg_device_session.power_level_type = nirfsg.PowerLevelType.PEAK  # To be able to call write multiple times on same waveform
        waveform_data = np.full(1000, 1 + 0j, dtype=np.complex128)
        rfsg_device_session.write_arb_waveform('mywaveform1', waveform_data, True)
        rfsg_device_session.set_arb_waveform_next_write_position('mywaveform1', nirfsg.RelativeTo.START_OF_WAVEFORM, 500)
        waveform_data_new_second_half = np.full(500, 0 + 1j, dtype=np.complex128)
        rfsg_device_session.write_arb_waveform('mywaveform1', waveform_data_new_second_half, False)

    def test_set_get_burst_start_stop_locations(self, rfsg_device_session):
        rfsg_device_session.generation_mode = nirfsg.GenerationMode.ARB_WAVEFORM
        waveform_data = np.full(1000, 1 + 0j, dtype=np.complex128)
        rfsg_device_session.write_arb_waveform('mywaveform1', waveform_data, False)
        startlocations = [1, 100, 200]
        stoplocations = [50, 175, 750]
        rfsg_device_session.waveforms['mywaveform1'].set_waveform_burst_start_locations(startlocations)
        rfsg_device_session.waveforms['mywaveform1'].set_waveform_burst_stop_locations(stoplocations)
        startlocations_out = rfsg_device_session.waveforms['mywaveform1'].get_waveform_burst_start_locations()
        stoplocations_out = rfsg_device_session.waveforms['mywaveform1'].get_waveform_burst_stop_locations()
        assert startlocations_out == startlocations
        assert stoplocations_out == stoplocations

    def test_set_get_marker_event_locations(self, rfsg_device_session):
        rfsg_device_session.generation_mode = nirfsg.GenerationMode.ARB_WAVEFORM
        waveform_data = np.full(1000, 1 + 0j, dtype=np.complex128)
        rfsg_device_session.write_arb_waveform('mywaveform1', waveform_data, False)
        markerlocations = [1, 100, 200]
        rfsg_device_session.waveforms['mywaveform1'].markers[0].set_waveform_marker_event_locations(markerlocations)
        markerlocations_out = rfsg_device_session.waveforms['mywaveform1'].markers[0].get_waveform_marker_event_locations()
        assert markerlocations_out == markerlocations

    def test_write_script(self, rfsg_device_session):
        rfsg_device_session.generation_mode = nirfsg.GenerationMode.SCRIPT
        waveform_data = np.full(1000, 0.707 + 0.707j, dtype=np.complex64)
        rfsg_device_session.write_arb_waveform('mywaveform1', waveform_data, False)
        script = '''script myScript1
        repeat forever
        generate mywaveform1
        end repeat
        end script'''
        rfsg_device_session.write_script(script)

    @pytest.mark.skipif(use_simulated_session is True, reason="Scripts not compiled on simulated device")
    def test_check_if_script_exists(self, rfsg_device_session):
        rfsg_device_session.generation_mode = nirfsg.GenerationMode.SCRIPT
        waveform_data = np.full(1000, 0.707 + 0.707j, dtype=np.complex64)
        rfsg_device_session.write_arb_waveform('mywaveform1', waveform_data, False)
        script = '''script myScript1
        repeat forever
        generate mywaveform1
        end repeat
        end script'''
        rfsg_device_session.write_script(script)
        script_exists = rfsg_device_session.check_if_script_exists('myScript1')
        assert script_exists is True
        script_exists = rfsg_device_session.check_if_script_exists('myScript2')
        assert script_exists is False

    @pytest.mark.skipif(use_simulated_session is True, reason="Scripts not compiled on simulated device")
    def test_write_script_with_bad_script(self, rfsg_device_session):
        rfsg_device_session.generation_mode = nirfsg.GenerationMode.SCRIPT
        script = '''script myScript1
        repeat forever
        generate mywaveform1
        end repeat
        end script'''
        try:
            rfsg_device_session.write_script(script)
            assert False
        except nirfsg.Error as e:
            assert e.code == -1074101603
            assert "A waveform matching the provided name does not exist in memory" in e.description

    def test_configure_software_trigger(self, rfsg_device_session):
        rfsg_device_session.configure_software_start_trigger()
        assert rfsg_device_session.start_trigger_type == nirfsg.StartTriggerType.SOFTWARE
        rfsg_device_session.script_triggers[0].configure_software_script_trigger()
        assert rfsg_device_session.script_triggers[0].script_trigger_type == nirfsg.ScriptTriggerType.SOFTWARE

    def test_configure_digital_edge_trigger(self, rfsg_device_session):
        rfsg_device_session.configure_digital_edge_start_trigger('PXI_Trig1', nirfsg.StartTriggerDigitalEdgeEdge.RISING)
        rfsg_device_session.script_triggers[1].configure_digital_edge_script_trigger('PXI_Trig2', nirfsg.ScriptTriggerDigitalEdgeEdge.FALLING)
        assert rfsg_device_session.start_trigger_type == nirfsg.StartTriggerType.DIGITAL_EDGE
        assert rfsg_device_session.digital_edge_start_trigger_source == 'PXI_Trig1'
        assert rfsg_device_session.digital_edge_start_trigger_edge == nirfsg.StartTriggerDigitalEdgeEdge.RISING
        assert rfsg_device_session.script_triggers[1].script_trigger_type == nirfsg.ScriptTriggerType.DIGITAL_EDGE
        assert rfsg_device_session.script_triggers[1].digital_edge_script_trigger_source == 'PXI_Trig2'
        assert rfsg_device_session.script_triggers[1].digital_edge_script_trigger_edge == nirfsg.ScriptTriggerDigitalEdgeEdge.FALLING

    def test_disable_trigger(self, rfsg_device_session):
        rfsg_device_session.configure_software_start_trigger()
        assert rfsg_device_session.start_trigger_type == nirfsg.StartTriggerType.SOFTWARE
        rfsg_device_session.disable_start_trigger()
        assert rfsg_device_session.start_trigger_type == nirfsg.StartTriggerType.NONE
        rfsg_device_session.script_triggers[3].configure_software_script_trigger()
        assert rfsg_device_session.script_triggers[3].script_trigger_type == nirfsg.ScriptTriggerType.SOFTWARE
        rfsg_device_session.script_triggers[3].disable_script_trigger()
        assert rfsg_device_session.script_triggers[3].script_trigger_type == nirfsg.ScriptTriggerType.NONE

    @pytest.mark.skipif(use_simulated_session is True, reason="RoCo is not invoked for simulated device")
    def test_export_started_event_with_invalid_terminal(self, rfsg_device_session):
        try:
            rfsg_device_session.exported_started_event_output_terminal = 'InvalidTerminal'
            rfsg_device_session.commit()
            assert False
        except nirfsg.Error as e:
            assert e.code == -1074107490
            assert 'Destination terminal to be routed could not be found on the device' in e.description

    def test_save_load_configuration(self, rfsg_device_session):
        rfsg_device_session.configure_rf(2e9, -5.0)
        rfsg_device_session.iq_rate = 1e6
        rfsg_device_session.save_configurations_to_file(get_test_file_path('tempConfiguration.json'))
        assert os.path.exists(get_test_file_path('tempConfiguration.json'))
        rfsg_device_session.configure_rf(3e9, -15.0)
        rfsg_device_session.iq_rate = 2e6
        assert rfsg_device_session.frequency == 3e9
        assert rfsg_device_session.power_level == -15.0
        assert rfsg_device_session.iq_rate == 2e6
        rfsg_device_session.load_configurations_from_file(get_test_file_path('tempConfiguration.json'))
        assert rfsg_device_session.frequency == 2e9
        assert rfsg_device_session.power_level == -5.0
        assert rfsg_device_session.iq_rate == 1e6
        os.remove(get_test_file_path('tempConfiguration.json'))

# Basic tests for generation
    @pytest.mark.skipif(use_simulated_session is False, reason="Test executed with status check in real hw")
    def test_cw_generation(self, rfsg_device_session):
        rfsg_device_session.configure_rf(2e9, -5.0)
        with rfsg_device_session.initiate():
            rfsg_device_session.check_generation_status()

    @pytest.mark.skipif(use_simulated_session is True, reason="is_done is always True on simulated device")
    def test_cw_generation_with_status(self, rfsg_device_session):
        rfsg_device_session.configure_rf(2e9, -5.0)
        with rfsg_device_session.initiate():
            is_done = rfsg_device_session.check_generation_status()
            assert is_done is False  # is_done will never be True in CW mode

    def test_abort(self, rfsg_device_session):
        rfsg_device_session.configure_rf(2e9, -5.0)
        rfsg_device_session.initiate()
        rfsg_device_session.check_generation_status()
        rfsg_device_session.abort()

    @pytest.mark.skipif(use_simulated_session is True, reason="is_done is always True on simulated device")
    def test_abort_with_status(self, rfsg_device_session):
        rfsg_device_session.configure_rf(2e9, -5.0)
        with rfsg_device_session.initiate():
            is_done = rfsg_device_session.check_generation_status()
            assert is_done is False  # is_done will never be True in CW mode
        is_done = rfsg_device_session.check_generation_status()
        assert is_done is True  # is_done should now be True after aborting

    @pytest.mark.skipif(use_simulated_session is False, reason="Test executed with status check in real hw")
    def test_multiple_arb_waveform_generation(self, rfsg_device_session):
        rfsg_device_session.generation_mode = nirfsg.GenerationMode.ARB_WAVEFORM
        waveform_data1 = np.full(1000, 1 + 0j, dtype=np.complex128)
        rfsg_device_session.write_arb_waveform('mywaveform1', waveform_data1, False)
        waveform_data2 = np.full(8000, 1 + 0j, dtype=np.complex128)
        rfsg_device_session.write_arb_waveform('mywaveform2', waveform_data2, False)
        rfsg_device_session.arb_selected_waveform = 'mywaveform1'
        with rfsg_device_session.initiate():
            rfsg_device_session.check_generation_status()
        rfsg_device_session.arb_selected_waveform = 'mywaveform2'
        with rfsg_device_session.initiate():
            rfsg_device_session.check_generation_status()

    @pytest.mark.skipif(use_simulated_session is True, reason="is_done is always True on simulated device")
    def test_multiple_arb_waveform_generation_with_status(self, rfsg_device_session):
        rfsg_device_session.generation_mode = nirfsg.GenerationMode.ARB_WAVEFORM
        waveform_data1 = np.full(1000, 1 + 0j, dtype=np.complex128)
        rfsg_device_session.write_arb_waveform('mywaveform1', waveform_data1, False)
        waveform_data2 = np.full(8000, 1 + 0j, dtype=np.complex128)
        rfsg_device_session.write_arb_waveform('mywaveform2', waveform_data2, False)
        rfsg_device_session.arb_selected_waveform = 'mywaveform1'
        with rfsg_device_session.initiate():
            is_done = rfsg_device_session.check_generation_status()
            assert is_done is False  # is_done will never be True since we have not authored waveform_repeat_count
        rfsg_device_session.arb_selected_waveform = 'mywaveform2'
        with rfsg_device_session.initiate():
            is_done = rfsg_device_session.check_generation_status()
            assert is_done is False  # is_done will never be True since we have not authored waveform_repeat_count

    @pytest.mark.skipif(use_simulated_session is False, reason="Test executed with status check in real hw")
    def test_multiple_script_generation(self, rfsg_device_session):
        rfsg_device_session.generation_mode = nirfsg.GenerationMode.SCRIPT
        waveform_data = np.full(2000, 1 + 0j, dtype=np.complex128)
        rfsg_device_session.write_arb_waveform('mywaveform', waveform_data, False)
        script0 = '''script myScript0
        repeat 1
        generate mywaveform
        end repeat
        end script'''
        script1 = '''script myScript1
        repeat forever
        generate mywaveform
        end repeat
        end script'''
        rfsg_device_session.write_script(script0)
        rfsg_device_session.write_script(script1)
        rfsg_device_session.selected_script = 'myScript0'
        with rfsg_device_session.initiate():
            rfsg_device_session.check_generation_status()
        rfsg_device_session.selected_script = 'myScript1'
        with rfsg_device_session.initiate():
            rfsg_device_session.check_generation_status()

    @pytest.mark.skipif(use_simulated_session is True, reason="is_done is always True on simulated device")
    def test_multiple_script_generation_with_status(self, rfsg_device_session):
        rfsg_device_session.generation_mode = nirfsg.GenerationMode.SCRIPT
        waveform_data = np.full(2000, 1 + 0j, dtype=np.complex128)
        rfsg_device_session.write_arb_waveform('mywaveform', waveform_data, False)
        script0 = '''script myScript0
        repeat 1
        generate mywaveform
        end repeat
        end script'''
        script1 = '''script myScript1
        repeat forever
        generate mywaveform
        end repeat
        end script'''
        rfsg_device_session.write_script(script0)
        rfsg_device_session.write_script(script1)
        rfsg_device_session.selected_script = 'myScript0'
        with rfsg_device_session.initiate():
            time.sleep(2)
            is_done = rfsg_device_session.check_generation_status()
            assert is_done is True  # is_done will be True since we are repeating only once
        rfsg_device_session.selected_script = 'myScript1'
        with rfsg_device_session.initiate():
            is_done = rfsg_device_session.check_generation_status()
            assert is_done is False  # is_done will never be True since we are repeating forever

    def test_send_software_edge_trigger(self, rfsg_device_session):
        rfsg_device_session.generation_mode = nirfsg.GenerationMode.SCRIPT
        waveform_data = np.full(2000, 1 + 0j, dtype=np.complex128)
        rfsg_device_session.write_arb_waveform('mywaveform', waveform_data, False)
        script0 = '''script myScript0
        wait until scriptTrigger0
        generate mywaveform
        end script'''
        rfsg_device_session.write_script(script0)
        rfsg_device_session.configure_software_start_trigger()
        rfsg_device_session.script_triggers[0].configure_software_script_trigger()
        with rfsg_device_session.initiate():
            rfsg_device_session.send_software_edge_trigger(nirfsg.SoftwareTriggerType.START, '')
            rfsg_device_session.send_software_edge_trigger(nirfsg.SoftwareTriggerType.SCRIPT, 'scriptTrigger0')

    @pytest.mark.skipif(sys.platform == "linux", reason="Function not supported on Linux OS")
    def test_create_deembedding_sparameter_table_s2p_file(self, rfsg_device_session):
        rfsg_device_session.create_deembedding_sparameter_table_s2p_file('', 'myTable1', get_test_file_path('samples2pfile.s2p'), nirfsg.SparameterOrientation.PORT2_TOWARDS_DUT)
        rfsg_device_session.create_deembedding_sparameter_table_s2p_file('', 'myTable2', get_test_file_path('samples2pfile.s2p'), nirfsg.SparameterOrientation.PORT1_TOWARDS_DUT)
        rfsg_device_session.configure_deembedding_table_interpolation_linear('', 'myTable1', nirfsg.Format.MAGNITUDE_AND_PHASE)
        rfsg_device_session.ports[''].deembedding_selected_table = 'myTable1'
        with rfsg_device_session.initiate():
            rfsg_device_session.check_generation_status()
        rfsg_device_session.delete_deembedding_table('', 'myTable1')
        rfsg_device_session.ports[''].deembedding_selected_table = 'myTable2'
        with rfsg_device_session.initiate():
            rfsg_device_session.check_generation_status()
        rfsg_device_session.delete_all_deembedding_tables()
        try:
            rfsg_device_session.commit()
            assert False
        except nirfsg.Error as e:
            assert e.code == -1074097772
            assert 'The specified de-embedding table cannot be found' in e.description
        rfsg_device_session.ports[''].deembedding_selected_table = ''
        with rfsg_device_session.initiate():
            rfsg_device_session.check_generation_status()

    def test_set_get_deembedding_sparameters(self, rfsg_device_session):
        frequencies = np.array([1e9, 2e9, 3e9], dtype=np.float64)
        sparameter_tables = np.array([[[1 + 1j, 2 + 2j], [3 + 3j, 4 + 4j]], [[5 + 5j, 6 + 6j], [7 + 7j, 8 + 8j]], [[9 + 9j, 10 + 10j], [11 + 11j, 12 + 12j]]], dtype=np.complex128)
        expected_sparameter_table = np.array([[5 + 5j, 6 + 6j], [7 + 7j, 8 + 8j]], dtype=np.complex128)
        rfsg_device_session.create_deembedding_sparameter_table_array('', 'myTable1', frequencies, sparameter_tables, nirfsg.SparameterOrientation.PORT2_TOWARDS_DUT)
        rfsg_device_session.frequency = 2e9
        returned_sparameter_table, number_of_ports = rfsg_device_session.get_deembedding_sparameters()
        assert number_of_ports == 2
        assert returned_sparameter_table.all() == expected_sparameter_table.all()

    def test_create_deembedding_sparameter_table_array_error_cases(self, rfsg_device_session):
        frequencies = np.array([1e9, 2e9, 3e9], dtype=np.float64)
        wrong_number_of_tables = np.full((2, 2, 2), 2.0 + 0.0j, dtype=np.complex128)
        wrong_table_size = np.full((3, 2, 3), 2.0 + 0.0j, dtype=np.complex128)
        wrong_array_dimensions = np.full((3, 2), 2.0 + 0.0j, dtype=np.complex128)
        try:
            rfsg_device_session.create_deembedding_sparameter_table_array('', 'myTable1', frequencies, wrong_number_of_tables, nirfsg.SparameterOrientation.PORT2_TOWARDS_DUT)
            assert False
        except ValueError as e:
            assert str(e) == 'Frequencies count does not match the sparameter table count. Frequencies count is 3 and sparameter table count is 2.'
        try:
            rfsg_device_session.create_deembedding_sparameter_table_array('', 'myTable1', frequencies, wrong_table_size, nirfsg.SparameterOrientation.PORT2_TOWARDS_DUT)
            assert False
        except ValueError as e:
            assert str(e) == 'Row and column count of sparameter table should be equal. Table row count is 2 and column count is 3.'
        try:
            rfsg_device_session.create_deembedding_sparameter_table_array('', 'myTable1', frequencies, wrong_array_dimensions, nirfsg.SparameterOrientation.PORT2_TOWARDS_DUT)
            assert False
        except ValueError as e:
            assert str(e) == 'Unsupported array dimension. Is 2, expected 3'

    def test_read_and_download_waveform_from_file_tdms(self, rfsg_device_session):
        rfsg_device_session.generation_mode = nirfsg.GenerationMode.ARB_WAVEFORM
        rfsg_device_session.read_and_download_waveform_from_file_tdms('mywaveform', get_test_file_path('ValidWaveformTDMSFile.tdms'), 0)
        waveform_exists = rfsg_device_session.check_if_waveform_exists('mywaveform')
        assert waveform_exists is True

    def test_wait_until_settled(self, rfsg_device_session):
        rfsg_device_session.configure_rf(2e9, -5.0)
        with rfsg_device_session.initiate():
            rfsg_device_session.wait_until_settled(15000)


class TestLibrary(SystemTests):
    @pytest.fixture(scope='class')
    def session_creation_kwargs(self):
        return {}
