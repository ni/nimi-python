import hightime
import nirfsa
import numpy as np
import os
import pathlib
import pytest
import sys
import time

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent / 'shared'))
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent / 'generated/nirfsa'))

import system_test_utilities  # noqa: E402

test_files_base_dir = os.path.join(os.path.dirname(__file__))
use_simulated_session = True
real_hw_resource_name = '5841'


def get_test_file_path(file_name):
    return os.path.join(test_files_base_dir, file_name)


class SystemTests:
    @pytest.fixture(scope='function')
    def rfsa_device_session(self, session_creation_kwargs):
        if use_simulated_session:
            with nirfsa.Session("5841sim", id_query=False, reset_device=False, options="Simulate=1, DriverSetup=Model:5841", **session_creation_kwargs) as sim_5841_session:
                yield sim_5841_session
        else:
            with nirfsa.Session(real_hw_resource_name, id_query=False, reset_device=False, **session_creation_kwargs) as real_rfsa_device_session:
                yield real_rfsa_device_session

    @pytest.fixture(scope='function')
    def simulated_5831_device_session(self, session_creation_kwargs):
        with nirfsa.Session("5831sim", id_query=False, reset_device=False, options="Simulate=1, DriverSetup=Model:5831", **session_creation_kwargs) as sim_5831_session:
            yield sim_5831_session

    @pytest.fixture(scope='function')
    def simulated_5668_device_session(self, session_creation_kwargs):
        with nirfsa.Session("5668sim", id_query=False, reset_device=False, options="Simulate=1, DriverSetup=Model:5668R", **session_creation_kwargs) as sim_5668_session:
            yield sim_5668_session

# Attribute set and get related tests
    def test_get_float_attribute(self, rfsa_device_session):
        value = rfsa_device_session.reference_level
        assert isinstance(value, float)

    def test_set_float_attribute(self, rfsa_device_session):
        rfsa_device_session.reference_level = -1.0
        assert rfsa_device_session.reference_level == -1.0

    def test_get_int64_attribute(self, rfsa_device_session):
        value = rfsa_device_session.fetch_offset
        assert isinstance(value, int)

    def test_set_int64_attribute(self, rfsa_device_session):
        rfsa_device_session.fetch_offset = 5
        assert rfsa_device_session.fetch_offset == 5

    def test_set_int32_enum_attribute(self, rfsa_device_session):
        rfsa_device_session.acquisition_type = nirfsa.AcquisitionType.SPECTRUM
        assert rfsa_device_session.acquisition_type == nirfsa.AcquisitionType.SPECTRUM

    def test_get_bool_attribute(self, rfsa_device_session):
        value = rfsa_device_session.allow_more_records_than_memory
        assert isinstance(value, bool)

    def test_set_bool_attribute(self, rfsa_device_session):
        rfsa_device_session.allow_more_records_than_memory = True
        assert rfsa_device_session.allow_more_records_than_memory is True

    def test_get_string_attribute(self, rfsa_device_session):
        value = rfsa_device_session.serial_number
        assert isinstance(value, str)

    def test_get_list_of_strings_attribute(self, rfsa_device_session):
        models = rfsa_device_session.supported_instrument_models
        assert isinstance(models, list) and all(isinstance(model, str) for model in models)
        assert "NI PXIe-5841" in models

    def test_get_timedelta_attribute(self, rfsa_device_session):
        value = rfsa_device_session.absolute_delay
        assert isinstance(value, hightime.timedelta)

    def test_set_invalid_attribute_raises(self, rfsa_device_session):
        with pytest.raises(AttributeError):
            rfsa_device_session.non_existent_attribute = 123

# Multi-threading related tests
    def test_multi_threading_lock_unlock(self, rfsa_device_session):
        system_test_utilities.impl_test_multi_threading_lock_unlock(rfsa_device_session)

    def test_multi_threading_ivi_synchronized_wrapper_releases_lock(self, rfsa_device_session):
        system_test_utilities.impl_test_multi_threading_ivi_synchronized_wrapper_releases_lock(rfsa_device_session.abort)

# Error handling related tests
    def test_error_message(self, session_creation_kwargs):
        try:
            with nirfsa.Session(resource_name="invalid_model", id_query=False, reset_device=False, options="Simulate=1, DriverSetup=Model:invalid_model", **session_creation_kwargs):
                assert False
        except nirfsa.Error as e:
            assert e.code == -1074135025  # IVI_ERROR_INVALID_PARAMETER
            assert "Invalid model in DriverSetup string" in e.description

    def test_get_error(self, rfsa_device_session):
        try:
            rfsa_device_session.instrument_model = ''
            assert False
        except nirfsa.Error as e:
            assert e.code == -1074135027  # IVI_ERROR_IVI_ATTR_NOT_WRITABLE
            assert "Attribute is read-only" in e.description

    def test_save_load_configuration(self, rfsa_device_session):
        rfsa_device_session.iq_carrier_frequency = 2.4e9
        rfsa_device_session.reference_level = -5.0
        rfsa_device_session.save_configurations_to_file(get_test_file_path('tempConfiguration.json'))
        assert os.path.exists(get_test_file_path('tempConfiguration.json'))
        rfsa_device_session.iq_carrier_frequency = 1e9
        rfsa_device_session.reference_level = -10.0
        assert rfsa_device_session.iq_carrier_frequency == 1e9
        assert rfsa_device_session.reference_level == -10.0
        rfsa_device_session.load_configurations_from_file(get_test_file_path('tempConfiguration.json'))
        assert rfsa_device_session.iq_carrier_frequency == 2.4e9
        assert rfsa_device_session.reference_level == -5.0
        os.remove(get_test_file_path('tempConfiguration.json'))

# Utility method tests
    def test_reset(self, rfsa_device_session):
        default_reference_level = rfsa_device_session.reference_level
        rfsa_device_session.reference_level = default_reference_level + 1.0
        assert rfsa_device_session.reference_level == default_reference_level + 1.0
        rfsa_device_session.reset()
        assert rfsa_device_session.reference_level == default_reference_level

    def test_reset_with_options(self, rfsa_device_session):
        frequencies = np.array([1e9, 2e9, 3e9], dtype=np.float64)
        sparameter_tables = np.array([[[1 + 1j, 2 + 2j], [3 + 3j, 4 + 4j]], [[5 + 5j, 6 + 6j], [7 + 7j, 8 + 8j]], [[9 + 9j, 10 + 10j], [11 + 11j, 12 + 12j]]], dtype=np.complex128)
        rfsa_device_session.create_deembedding_sparameter_table_array('', 'myTable1', frequencies, sparameter_tables, nirfsa.SparameterOrientation.PORT2_TOWARDS_DUT)
        default_reference_level = rfsa_device_session.reference_level
        rfsa_device_session.reference_level = default_reference_level + 1.0
        assert rfsa_device_session.reference_level == default_reference_level + 1.0
        steps_to_omit_with_deembedding_tables = nirfsa.ResetWithOptionsStepsToOmit.DEEMBEDDING_TABLES
        steps_to_omit_none = nirfsa.ResetWithOptionsStepsToOmit.NONE

        # Reset all properties but omit deleting de-embedding tables.
        rfsa_device_session.reset_with_options(steps_to_omit_with_deembedding_tables)
        assert rfsa_device_session.reference_level == default_reference_level

        rfsa_device_session.ports[''].deembedding_selected_table = 'myTable1'
        rfsa_device_session.commit()

        # Reset with no omitted steps deletes the de-embedding tables.
        rfsa_device_session.reset_with_options(steps_to_omit_none)
        rfsa_device_session.ports[''].deembedding_selected_table = 'myTable1'
        try:
            rfsa_device_session.commit()
            assert False
        except nirfsa.Error as e:
            assert e.code == -1074097772
            assert 'de-embedding table cannot be found' in e.description

    def test_self_test(self, rfsa_device_session):
        # We should not get an assert if self_test passes
        rfsa_device_session.self_test()

    @pytest.mark.skipif(use_simulated_session is False, reason="Takes long time on real device")
    def test_self_cal_range(self, rfsa_device_session):
        steps_to_omit = nirfsa.SelfCalibrateRangeStepsToOmit.DIGITIZER_SELF_CAL | nirfsa.SelfCalibrateRangeStepsToOmit.LO_SELF_CAL
        rfsa_device_session.self_calibrate_range(steps_to_omit, 1e9, 2e9, -20, 0)

    def test_clear_self_calibrate_range(self, rfsa_device_session):
        rfsa_device_session.clear_self_calibrate_range()

    @pytest.mark.skipif(use_simulated_session is True, reason="Bad date returned by driver for simulated device")
    def test_get_ext_cal_last_date_and_time(self, rfsa_device_session):
        dt = rfsa_device_session.get_ext_cal_last_date_and_time()
        assert isinstance(dt, hightime.datetime)

    def test_get_ext_cal_recommended_interval(self, rfsa_device_session):
        interval = rfsa_device_session.get_ext_cal_recommended_interval()
        assert isinstance(interval, hightime.timedelta)

    def test_get_terminal_name(self, rfsa_device_session):
        terminal_name = rfsa_device_session.get_terminal_name(nirfsa.Signal.REF_TRIGGER, '')
        assert '/ai/0/ReferenceTrigger' in terminal_name

    def test_abort(self, rfsa_device_session):
        rfsa_device_session.iq_carrier_frequency = 2.4e9
        rfsa_device_session.initiate()
        rfsa_device_session.check_acquisition_status()
        rfsa_device_session.abort()

    @pytest.mark.skipif(use_simulated_session is True, reason="is_done is always True on simulated device")
    def test_abort_with_status(self, rfsa_device_session):
        rfsa_device_session.acquisition_type = nirfsa.AcquisitionType.IQ
        rfsa_device_session.iq_carrier_frequency = 2.4e9
        rfsa_device_session.reference_level = 0.0
        rfsa_device_session.iq_rate = 1e6
        rfsa_device_session.number_of_samples_is_finite = False
        with rfsa_device_session.initiate():
            assert rfsa_device_session.check_acquisition_status() is False  # is_done never True for continuous acquisition
        assert rfsa_device_session.check_acquisition_status() is True  # is_done True after abort

    @pytest.mark.skipif(use_simulated_session is True, reason="Bad date returned by driver for simulated device")
    def test_get_self_cal_last_date_and_time(self, rfsa_device_session):
        dt = rfsa_device_session.get_self_cal_last_date_and_time(nirfsa.SelfCalibrationStep.IMAGE_SUPPRESSION)
        assert isinstance(dt, hightime.datetime)

    @pytest.mark.skipif(use_simulated_session is True, reason="Calibration step temperature may be unsupported or unreliable on simulated RFSA")
    def test_get_self_calibration_temperature(self, rfsa_device_session):
        temperature = rfsa_device_session.get_self_calibration_temperature(nirfsa.SelfCalibrationStep.IMAGE_SUPPRESSION)
        assert isinstance(temperature, float)

    @pytest.mark.skipif(use_simulated_session is True, reason="Thermal correction is unsupported on simulated RFSA")
    def test_perform_thermal_correction(self, rfsa_device_session):
        rfsa_device_session.number_of_samples_is_finite = False
        rfsa_device_session.acquisition_type = nirfsa.AcquisitionType.IQ
        rfsa_device_session.iq_rate = 1e6
        with rfsa_device_session.initiate():
            rfsa_device_session.perform_thermal_correction()

    def test_get_scaling_coefficients(self, rfsa_device_session):
        coefficient_info = rfsa_device_session.get_scaling_coefficients()
        assert isinstance(coefficient_info, list)
        assert len(coefficient_info) > 0
        for info in coefficient_info:
            assert hasattr(info, 'offset')
            assert hasattr(info, 'gain')

    @pytest.mark.skipif(use_simulated_session is True, reason="Fetch backlog behavior differs on simulated RFSA")
    def test_get_fetch_backlog(self, rfsa_device_session):
        rfsa_device_session.acquisition_type = nirfsa.AcquisitionType.IQ
        rfsa_device_session.reference_level = 0.0
        rfsa_device_session.iq_rate = 1e6
        rfsa_device_session.number_of_samples = 2000
        rfsa_device_session.fetch_relative_to = nirfsa.FetchRelativeTo.REFERENCE_TRIGGER
        with rfsa_device_session.initiate():
            time.sleep(3)
            backlog = rfsa_device_session.get_fetch_backlog(0)
        assert backlog == rfsa_device_session.number_of_samples

# Repeated capability tests
    def test_ports_rep_cap(self, simulated_5831_device_session):
        requested_deembedding_type = nirfsa.DeembeddingType.SCALAR
        simulated_5831_device_session.ports['if1'].deembedding_type = requested_deembedding_type
        assert simulated_5831_device_session.ports['if1'].deembedding_type == requested_deembedding_type

    def test_los_rep_cap(self, simulated_5831_device_session):
        requested_lo_source = nirfsa.LoSource.LO_SOURCE_SG_SA_SHARED
        simulated_5831_device_session.los[2].lo_source = requested_lo_source
        assert simulated_5831_device_session.los[2].lo_source == requested_lo_source

    def test_device_temperatures_rep_cap(self, rfsa_device_session):
        temperature = rfsa_device_session.device_temperatures['0'].device_temperature
        assert isinstance(temperature, float)

# Trigger configuration tests
    def test_configure_spectrum_frequency_center_span(self, rfsa_device_session):
        rfsa_device_session.acquisition_type = nirfsa.AcquisitionType.SPECTRUM
        requested_center_frequency = 2.4e9
        requested_span = 20e6
        rfsa_device_session.configure_spectrum_frequency(center_frequency=requested_center_frequency, span=requested_span)
        center_frequency_diff = abs(rfsa_device_session.center_frequency - requested_center_frequency)
        span_diff = abs(rfsa_device_session.spectrum_span - requested_span)
        assert center_frequency_diff < 1
        assert span_diff < 1e5  # tolerance chosen as 100k to account for the coercions done by driver while planning the spectrum

    def test_configure_spectrum_frequency_start_stop(self, rfsa_device_session):
        rfsa_device_session.acquisition_type = nirfsa.AcquisitionType.SPECTRUM
        requested_start_frequency = 2.39e9
        requested_stop_frequency = 2.41e9
        rfsa_device_session.configure_spectrum_frequency(start_frequency=requested_start_frequency, stop_frequency=requested_stop_frequency)
        expected_center_frequency = requested_start_frequency + (requested_stop_frequency - requested_start_frequency) / 2
        center_frequency_diff = abs(rfsa_device_session.center_frequency - expected_center_frequency)
        expected_span = requested_stop_frequency - requested_start_frequency
        span_diff = abs(rfsa_device_session.spectrum_span - expected_span)
        assert center_frequency_diff < 1
        assert span_diff < 1e5  # tolerance chosen as 100k to account for the coercions done by driver while planning the spectrum

    def test_configure_spectrum_frequency_wrong_parameter_error(self, rfsa_device_session):
        rfsa_device_session.acquisition_type = nirfsa.AcquisitionType.SPECTRUM
        expected_error = "Provide either (center_frequency & span) or (start_frequency & stop_frequency)"

        with pytest.raises(ValueError) as exc_info:
            rfsa_device_session.configure_spectrum_frequency(center_frequency=2.4e9)
        assert str(exc_info.value) == expected_error

        with pytest.raises(ValueError) as exc_info:
            rfsa_device_session.configure_spectrum_frequency(span=20e6)
        assert str(exc_info.value) == expected_error

        with pytest.raises(ValueError) as exc_info:
            rfsa_device_session.configure_spectrum_frequency(center_frequency=2.4e9, stop_frequency=2.41e9)
        assert str(exc_info.value) == expected_error

        with pytest.raises(ValueError) as exc_info:
            rfsa_device_session.configure_spectrum_frequency()
        assert str(exc_info.value) == expected_error

    def test_configure_digital_edge_advance_trigger(self, rfsa_device_session):
        rfsa_device_session.configure_digital_edge_advance_trigger('PXI_Trig1', nirfsa.AdvanceTriggerDigitalEdgeEdge.RISING)
        assert rfsa_device_session.advance_trigger_type == nirfsa.AdvanceTriggerType.DIGITAL_EDGE
        assert rfsa_device_session.digital_edge_advance_trigger_source == 'PXI_Trig1'

    def test_disable_advance_trigger(self, rfsa_device_session):
        rfsa_device_session.configure_digital_edge_advance_trigger('PXI_Trig1', nirfsa.AdvanceTriggerDigitalEdgeEdge.RISING)
        assert rfsa_device_session.advance_trigger_type == nirfsa.AdvanceTriggerType.DIGITAL_EDGE
        rfsa_device_session.disable_advance_trigger()
        assert rfsa_device_session.advance_trigger_type == nirfsa.AdvanceTriggerType.NONE

    def test_configure_digital_edge_ref_trigger(self, rfsa_device_session):
        rfsa_device_session.configure_digital_edge_ref_trigger('PXI_Trig1', nirfsa.ReferenceTriggerDigitalEdgeEdge.RISING)
        assert rfsa_device_session.ref_trigger_type == nirfsa.ReferenceTriggerType.DIGITAL_EDGE
        assert rfsa_device_session.digital_edge_ref_trigger_source == 'PXI_Trig1'
        assert rfsa_device_session.digital_edge_ref_trigger_edge == nirfsa.ReferenceTriggerDigitalEdgeEdge.RISING

    def test_disable_ref_trigger(self, rfsa_device_session):
        rfsa_device_session.configure_digital_edge_ref_trigger('PXI_Trig1', nirfsa.ReferenceTriggerDigitalEdgeEdge.RISING)
        assert rfsa_device_session.ref_trigger_type == nirfsa.ReferenceTriggerType.DIGITAL_EDGE
        rfsa_device_session.disable_ref_trigger()
        assert rfsa_device_session.ref_trigger_type == nirfsa.ReferenceTriggerType.NONE

    def test_configure_iq_power_edge_ref_trigger(self, rfsa_device_session):
        rfsa_device_session.configure_iq_power_edge_ref_trigger('0', -20.0, nirfsa.ReferenceTriggerIqPowerEdgeSlope.FALLING, pretrigger_samples=32)
        assert rfsa_device_session.ref_trigger_type == nirfsa.ReferenceTriggerType.IQ_POWER_EDGE
        assert rfsa_device_session.iq_power_edge_ref_trigger_source == '0'
        assert abs(rfsa_device_session.iq_power_edge_ref_trigger_level - (-20.0)) < 1
        assert rfsa_device_session.iq_power_edge_ref_trigger_slope == nirfsa.ReferenceTriggerIqPowerEdgeSlope.FALLING
        assert rfsa_device_session.ref_trigger_pretrigger_samples == 32

    def test_configure_digital_edge_start_trigger(self, rfsa_device_session):
        rfsa_device_session.configure_digital_edge_start_trigger('PXI_Trig1', nirfsa.StartTriggerDigitalEdgeEdge.RISING)
        assert rfsa_device_session.start_trigger_type == nirfsa.StartTriggerType.DIGITAL_EDGE
        assert rfsa_device_session.digital_edge_start_trigger_source == 'PXI_Trig1'
        assert rfsa_device_session.digital_edge_start_trigger_edge == nirfsa.StartTriggerDigitalEdgeEdge.RISING

    def test_disable_start_trigger(self, rfsa_device_session):
        rfsa_device_session.configure_digital_edge_start_trigger('PXI_Trig1', nirfsa.StartTriggerDigitalEdgeEdge.RISING)
        assert rfsa_device_session.start_trigger_type == nirfsa.StartTriggerType.DIGITAL_EDGE
        rfsa_device_session.disable_start_trigger()
        assert rfsa_device_session.start_trigger_type == nirfsa.StartTriggerType.NONE

    def test_configure_software_edge_advance_trigger(self, rfsa_device_session):
        rfsa_device_session.configure_software_edge_advance_trigger()
        assert rfsa_device_session.advance_trigger_type == nirfsa.AdvanceTriggerType.SOFTWARE_EDGE

    def test_configure_software_edge_ref_trigger(self, rfsa_device_session):
        rfsa_device_session.configure_software_edge_ref_trigger(pretrigger_samples=32)
        assert rfsa_device_session.ref_trigger_type == nirfsa.ReferenceTriggerType.SOFTWARE_EDGE
        assert rfsa_device_session.ref_trigger_pretrigger_samples == 32

    def test_configure_software_edge_start_trigger(self, rfsa_device_session):
        rfsa_device_session.configure_software_edge_start_trigger()
        assert rfsa_device_session.start_trigger_type == nirfsa.StartTriggerType.SOFTWARE_EDGE

    @pytest.mark.skipif(use_simulated_session is True, reason="check_acquisition_status always returns True on simulated device")
    def test_send_software_edge_trigger_configured_with_ref_trigger(self, rfsa_device_session):
        rfsa_device_session.acquisition_type = nirfsa.AcquisitionType.IQ
        rfsa_device_session.iq_rate = 1e6
        rfsa_device_session.configure_software_edge_ref_trigger()
        with rfsa_device_session.initiate():
            assert rfsa_device_session.check_acquisition_status() is False
            rfsa_device_session.send_software_edge_trigger(nirfsa.SoftwareTriggerType.REF, '')
            time.sleep(3)
            assert rfsa_device_session.check_acquisition_status() is True

    @pytest.mark.skipif(use_simulated_session is True, reason="check_acquisition_status always returns True on simulated device")
    def test_send_software_edge_trigger_configured_with_start_trigger(self, rfsa_device_session):
        rfsa_device_session.acquisition_type = nirfsa.AcquisitionType.IQ
        rfsa_device_session.iq_rate = 1e6
        rfsa_device_session.configure_software_edge_start_trigger()
        with rfsa_device_session.initiate():
            assert rfsa_device_session.check_acquisition_status() is False
            rfsa_device_session.send_software_edge_trigger(nirfsa.SoftwareTriggerType.START, '')
            time.sleep(3)
            assert rfsa_device_session.check_acquisition_status() is True

# Fetch tests
    def test_fetch_iq_single_record_with_samples_passed_as_none(self, rfsa_device_session):
        rfsa_device_session.acquisition_type = nirfsa.AcquisitionType.IQ
        rfsa_device_session.iq_rate = 1e6

        iq_data_array = np.zeros(64, dtype=np.complex128)
        with rfsa_device_session.initiate():
            wfm_info = rfsa_device_session.fetch_iq_single_record_into(iq_data_array)
        assert len(wfm_info.samples) == wfm_info.actual_samples
        assert np.asarray(wfm_info.samples).dtype == np.complex128

    def test_fetch_iq_single_record_subset(self, rfsa_device_session):
        rfsa_device_session.acquisition_type = nirfsa.AcquisitionType.IQ
        rfsa_device_session.iq_rate = 1e6
        rfsa_device_session.number_of_samples = 1024

        iq_data_array = np.zeros(1024, dtype=np.complex64)
        with rfsa_device_session.initiate():
            wfm_info = rfsa_device_session.fetch_iq_single_record_into(iq_data_array, number_of_samples=128)
        assert len(wfm_info.samples) == wfm_info.actual_samples
        assert np.asarray(wfm_info.samples).dtype == np.complex64

    def test_fetch_iq_single_record_grow_with_smaller_buffer(self, rfsa_device_session):
        rfsa_device_session.acquisition_type = nirfsa.AcquisitionType.IQ
        rfsa_device_session.iq_rate = 1e6
        rfsa_device_session.number_of_samples = 1024

        iq_data_array = np.zeros(64, dtype=np.complex128)
        with rfsa_device_session.initiate():
            wfm_info = rfsa_device_session.fetch_iq_single_record_into(iq_data_array, number_of_samples=rfsa_device_session.number_of_samples)
        assert len(wfm_info.samples) == wfm_info.actual_samples
        assert np.asarray(wfm_info.samples).dtype == np.complex128

    def test_fetch_iq_single_record_check_view_with_larger_buffer(self, rfsa_device_session):
        rfsa_device_session.acquisition_type = nirfsa.AcquisitionType.IQ
        rfsa_device_session.number_of_samples = 1024

        iq_data_array = np.zeros(512, dtype=np.complex128)
        with rfsa_device_session.initiate():
            wfm_info = rfsa_device_session.fetch_iq_single_record_into(iq_data_array, number_of_samples=rfsa_device_session.number_of_samples)
        assert len(wfm_info.samples) == wfm_info.actual_samples
        assert len(iq_data_array) == rfsa_device_session.number_of_samples
        assert np.asarray(wfm_info.samples).dtype == np.complex128

    def test_fetch_iq_single_record_complex_i16(self, rfsa_device_session):
        rfsa_device_session.acquisition_type = nirfsa.AcquisitionType.IQ
        rfsa_device_session.number_of_samples = 1024

        iq_data_array = np.zeros(64, dtype=np.int16)
        with rfsa_device_session.initiate():
            wfm_info = rfsa_device_session.fetch_iq_single_record_into(
                iq_data_array,
                number_of_samples=rfsa_device_session.number_of_samples,
            )
        assert np.asarray(wfm_info.samples).dtype == np.int16
        assert len(wfm_info.samples) == wfm_info.actual_samples

    def test_fetch_iq_multi_record_with_records_passed_as_none(self, rfsa_device_session):
        rfsa_device_session.acquisition_type = nirfsa.AcquisitionType.IQ
        rfsa_device_session.number_of_samples = 64

        iq_data_arrays = np.zeros((2, 64), dtype=np.complex128)
        with rfsa_device_session.initiate():
            wfm_info = rfsa_device_session.fetch_iq_multi_record_into(iq_data_arrays, number_of_samples=rfsa_device_session.number_of_samples)

        assert len(wfm_info) == rfsa_device_session.number_of_records
        for i in range(len(wfm_info)):
            if isinstance(wfm_info[i], nirfsa.WaveformInfo):
                assert np.asarray(wfm_info[i].samples).dtype == np.complex128
                assert len(wfm_info[i].samples) == rfsa_device_session.number_of_samples

    def test_fetch_iq_multi_record_with_samples_passed_as_none(self, rfsa_device_session):
        rfsa_device_session.acquisition_type = nirfsa.AcquisitionType.IQ
        rfsa_device_session.number_of_records = 2

        iq_data_arrays = np.zeros((2, 64), dtype=np.complex128)
        with rfsa_device_session.initiate():
            wfm_info = rfsa_device_session.fetch_iq_multi_record_into(iq_data_arrays, number_of_records=rfsa_device_session.number_of_records)

        assert len(wfm_info) == rfsa_device_session.number_of_records
        for i in range(len(wfm_info)):
            if isinstance(wfm_info[i], nirfsa.WaveformInfo):
                assert np.asarray(wfm_info[i].samples).dtype == np.complex128
                assert len(wfm_info[i].samples) == rfsa_device_session.number_of_samples

    def test_fetch_iq_multi_record_grow_with_smaller_column_size(self, rfsa_device_session):
        rfsa_device_session.acquisition_type = nirfsa.AcquisitionType.IQ
        rfsa_device_session.number_of_records = 2
        rfsa_device_session.number_of_samples = 1024

        iq_data_arrays = np.zeros((2, 64), dtype=np.complex128)
        with rfsa_device_session.initiate():
            wfm_info = rfsa_device_session.fetch_iq_multi_record_into(iq_data_arrays, number_of_records=rfsa_device_session.number_of_records, number_of_samples=rfsa_device_session.number_of_samples)

        assert len(wfm_info) == rfsa_device_session.number_of_records
        for i in range(len(wfm_info)):
            if isinstance(wfm_info[i], nirfsa.WaveformInfo):
                assert np.asarray(wfm_info[i].samples).dtype == np.complex128
                assert len(wfm_info[i].samples) == rfsa_device_session.number_of_samples

    def test_fetch_iq_multi_record_with_smaller_row_size_error_case(self, rfsa_device_session):
        rfsa_device_session.acquisition_type = nirfsa.AcquisitionType.IQ
        rfsa_device_session.number_of_records = 2

        iq_data_arrays = np.zeros((1, 64), dtype=np.complex128)
        with rfsa_device_session.initiate():
            with pytest.raises(ValueError) as exc_info:
                rfsa_device_session.fetch_iq_multi_record_into(iq_data_arrays, number_of_records=rfsa_device_session.number_of_records, number_of_samples=rfsa_device_session.number_of_samples)
        assert str(exc_info.value) == "iq_data_arrays must have at least 2 rows (number_of_records), but has 1"

    def test_fetch_iq_multi_record_subset(self, rfsa_device_session):
        rfsa_device_session.acquisition_type = nirfsa.AcquisitionType.IQ
        rfsa_device_session.number_of_samples = 1024
        rfsa_device_session.number_of_records = 2

        iq_data_arrays = np.zeros((2, 64), dtype=np.complex64)
        with rfsa_device_session.initiate():
            wfm_info = rfsa_device_session.fetch_iq_multi_record_into(iq_data_arrays, number_of_records=rfsa_device_session.number_of_records, number_of_samples=rfsa_device_session.number_of_samples)

        assert len(wfm_info) == rfsa_device_session.number_of_records
        for i in range(len(wfm_info)):
            if isinstance(wfm_info[i], nirfsa.WaveformInfo):
                assert np.asarray(wfm_info[i].samples).dtype == np.complex64
                assert len(wfm_info[i].samples) == rfsa_device_session.number_of_samples

    def test_fetch_iq_multi_record_complex_i16(self, rfsa_device_session):
        rfsa_device_session.acquisition_type = nirfsa.AcquisitionType.IQ
        rfsa_device_session.number_of_records = 2
        rfsa_device_session.number_of_samples = 1024

        iq_data_arrays = np.zeros((2, 64), dtype=np.int16)
        with rfsa_device_session.initiate():
            wfm_info = rfsa_device_session.fetch_iq_multi_record_into(
                iq_data_arrays,
                starting_record=0,
                number_of_records=rfsa_device_session.number_of_records,
                number_of_samples=rfsa_device_session.number_of_samples,
                timeout=10.0,
            )

        assert len(wfm_info) == rfsa_device_session.number_of_records
        for i in range(len(wfm_info)):
            if isinstance(wfm_info[i], nirfsa.WaveformInfo):
                assert np.asarray(wfm_info[i].samples).dtype == np.int16
                assert len(wfm_info[i].samples) == rfsa_device_session.number_of_samples

    def test_read_iq_single_record_grow_with_smaller_buffer(self, rfsa_device_session):
        rfsa_device_session.acquisition_type = nirfsa.AcquisitionType.IQ
        rfsa_device_session.number_of_samples = 1024

        iq_data_array = np.zeros(64, dtype=np.complex128)
        wfm_info = rfsa_device_session.read_iq_single_record_into(iq_data_array)
        assert len(wfm_info.samples) == wfm_info.actual_samples
        assert np.asarray(wfm_info.samples).dtype == np.complex128

    def test_read_power_spectrum_grow_with_smaller_buffer(self, rfsa_device_session):
        rfsa_device_session.acquisition_type = nirfsa.AcquisitionType.SPECTRUM
        rfsa_device_session.number_of_spectral_lines = 1024

        power_spectrum_data_array = np.zeros(512, dtype=np.float64)
        spectrum_info = rfsa_device_session.read_power_spectrum_into(power_spectrum_data_array, rfsa_device_session.number_of_spectral_lines)
        assert len(spectrum_info.samples) == rfsa_device_session.number_of_spectral_lines
        assert np.asarray(spectrum_info.samples).dtype == np.float64

    def test_read_power_spectrum_check_view_with_larger_buffer(self, rfsa_device_session):
        rfsa_device_session.acquisition_type = nirfsa.AcquisitionType.SPECTRUM
        rfsa_device_session.number_of_spectral_lines = 512

        power_spectrum_data_array = np.zeros(1024, dtype=np.float64)
        spectrum_info = rfsa_device_session.read_power_spectrum_into(power_spectrum_data_array, rfsa_device_session.number_of_spectral_lines)
        assert len(spectrum_info.samples) == rfsa_device_session.number_of_spectral_lines
        assert np.asarray(spectrum_info.samples).dtype == np.float64
        assert len(power_spectrum_data_array) == 1024

    def test_read_power_spectrum_with_data_array_size_passed_as_none(self, rfsa_device_session):
        rfsa_device_session.acquisition_type = nirfsa.AcquisitionType.SPECTRUM
        rfsa_device_session.number_of_spectral_lines = 1024

        power_spectrum_data_array = np.zeros(512, dtype=np.float64)
        spectrum_info = rfsa_device_session.read_power_spectrum_into(power_spectrum_data_array)
        assert len(spectrum_info.samples) == rfsa_device_session.number_of_spectral_lines
        assert np.asarray(spectrum_info.samples).dtype == np.float64

# Deembedding tests
    def test_set_get_deembedding_sparameters(self, rfsa_device_session):
        frequencies = np.array([1e9, 2e9, 3e9], dtype=np.float64)
        sparameter_tables = np.array([[[1 + 1j, 2 + 2j], [3 + 3j, 4 + 4j]], [[5 + 5j, 6 + 6j], [7 + 7j, 8 + 8j]], [[9 + 9j, 10 + 10j], [11 + 11j, 12 + 12j]]], dtype=np.complex128)
        expected_sparameter_table = np.array([[5 + 5j, 6 + 6j], [7 + 7j, 8 + 8j]], dtype=np.complex128)
        rfsa_device_session.create_deembedding_sparameter_table_array('', 'myTable1', frequencies, sparameter_tables, nirfsa.SparameterOrientation.PORT2_TOWARDS_DUT)
        rfsa_device_session.center_frequency = 2e9
        returned_sparameter_table = rfsa_device_session.get_deembedding_sparameters()
        assert returned_sparameter_table.all() == expected_sparameter_table.all()

    def test_configure_deembedding_table_interpolation(self, rfsa_device_session):
        frequencies = np.array([1e9, 2e9, 3e9], dtype=np.float64)
        sparameter_tables = np.array([[[1 + 1j, 2 + 2j], [3 + 3j, 4 + 4j]], [[5 + 5j, 6 + 6j], [7 + 7j, 8 + 8j]], [[9 + 9j, 10 + 10j], [11 + 11j, 12 + 12j]]], dtype=np.complex128)
        rfsa_device_session.create_deembedding_sparameter_table_array('', 'myTable1', frequencies, sparameter_tables, nirfsa.SparameterOrientation.PORT2_TOWARDS_DUT)
        rfsa_device_session.configure_deembedding_table_interpolation_linear('', 'myTable1', nirfsa.LinearInterpolationFormat.MAGNITUDE_AND_PHASE)
        rfsa_device_session.delete_deembedding_table('', 'myTable1')

    @pytest.mark.skipif(sys.platform == "linux", reason="Function not supported on Linux OS")
    def test_create_deembedding_sparameter_table_s2p_file(self, rfsa_device_session):
        rfsa_device_session.create_deembedding_sparameter_table_s2p_file('', 'myTable1', get_test_file_path('samples2pfile.s2p'), nirfsa.SparameterOrientation.PORT2_TOWARDS_DUT)
        rfsa_device_session.create_deembedding_sparameter_table_s2p_file('', 'myTable2', get_test_file_path('samples2pfile.s2p'), nirfsa.SparameterOrientation.PORT1_TOWARDS_DUT)
        rfsa_device_session.configure_deembedding_table_interpolation_linear('', 'myTable1', nirfsa.LinearInterpolationFormat.MAGNITUDE_AND_PHASE)
        rfsa_device_session.ports[''].deembedding_selected_table = 'myTable1'
        with rfsa_device_session.initiate():
            rfsa_device_session.check_acquisition_status()
        rfsa_device_session.delete_deembedding_table('', 'myTable1')
        rfsa_device_session.ports[''].deembedding_selected_table = 'myTable2'
        with rfsa_device_session.initiate():
            rfsa_device_session.check_acquisition_status()
        rfsa_device_session.delete_all_deembedding_tables()
        try:
            rfsa_device_session.commit()
            assert False
        except nirfsa.Error as e:
            assert e.code == -1074097772
            assert 'de-embedding table cannot be found' in e.description
        rfsa_device_session.ports[''].deembedding_selected_table = ''
        with rfsa_device_session.initiate():
            rfsa_device_session.check_acquisition_status()

    def test_create_deembedding_sparameter_table_array_error_cases(self, rfsa_device_session):
        frequencies = np.array([1e9, 2e9, 3e9], dtype=np.float64)
        wrong_number_of_tables = np.full((2, 2, 2), 2.0 + 0.0j, dtype=np.complex128)
        wrong_table_size = np.full((3, 2, 3), 2.0 + 0.0j, dtype=np.complex128)
        wrong_array_dimensions = np.full((3, 2), 2.0 + 0.0j, dtype=np.complex128)
        try:
            rfsa_device_session.create_deembedding_sparameter_table_array('', 'myTable1', frequencies, wrong_number_of_tables, nirfsa.SparameterOrientation.PORT2_TOWARDS_DUT)
            assert False
        except ValueError as e:
            assert str(e) == 'Frequencies count does not match the sparameter table count. Frequencies count is 3 and sparameter table count is 2.'
        try:
            rfsa_device_session.create_deembedding_sparameter_table_array('', 'myTable1', frequencies, wrong_table_size, nirfsa.SparameterOrientation.PORT2_TOWARDS_DUT)
            assert False
        except ValueError as e:
            assert str(e) == 'Row and column count of sparameter table should be equal. Table row count is 2 and column count is 3.'
        try:
            rfsa_device_session.create_deembedding_sparameter_table_array('', 'myTable1', frequencies, wrong_array_dimensions, nirfsa.SparameterOrientation.PORT2_TOWARDS_DUT)
            assert False
        except ValueError as e:
            assert str(e) == 'Unsupported array dimension. Is 2, expected 3'

    def test_delete_all_deembedding_tables(self, rfsa_device_session):
        frequencies = np.array([1e9, 2e9, 3e9], dtype=np.float64)
        sparameter_tables = np.array([[[1 + 1j, 2 + 2j], [3 + 3j, 4 + 4j]], [[5 + 5j, 6 + 6j], [7 + 7j, 8 + 8j]], [[9 + 9j, 10 + 10j], [11 + 11j, 12 + 12j]]], dtype=np.complex128)
        rfsa_device_session.create_deembedding_sparameter_table_array('', 'myTable1', frequencies, sparameter_tables, nirfsa.SparameterOrientation.PORT2_TOWARDS_DUT)
        rfsa_device_session.create_deembedding_sparameter_table_array('', 'myTable2', frequencies, sparameter_tables, nirfsa.SparameterOrientation.PORT2_TOWARDS_DUT)
        rfsa_device_session.delete_all_deembedding_tables()


class TestLibrary(SystemTests):
    @pytest.fixture(scope='class')
    def session_creation_kwargs(self):
        return {}
