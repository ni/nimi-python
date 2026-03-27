# -*- coding: utf-8 -*-
# This file was generated

import grpc
import hightime  # noqa: F401
import threading
import warnings

from . import enums as enums  # noqa: F401
from . import errors as errors
from . import nidevice_pb2 as grpc_complex_types  # noqa: F401
from . import nirfsg_pb2 as grpc_types
from . import nirfsg_pb2_grpc as nirfsg_grpc
from . import session_pb2 as session_grpc_types


class GrpcStubInterpreter(object):
    '''Interpreter for interacting with a gRPC Stub class'''

    def __init__(self, grpc_options):
        self._grpc_options = grpc_options
        self._lock = threading.RLock()
        self._client = nirfsg_grpc.NiRFSGStub(grpc_options.grpc_channel)
        self.set_session_handle()

    def set_session_handle(self, value=session_grpc_types.Session()):
        self._vi = value

    def get_session_handle(self):
        return self._vi

    def _invoke(self, func, request, metadata=None):
        try:
            response = func(request, metadata=metadata)
            error_code = response.status
            error_message = ''
        except grpc.RpcError as rpc_error:
            error_code = None
            error_message = rpc_error.details()
            for entry in rpc_error.trailing_metadata() or []:
                if entry.key == 'ni-error':
                    value = entry.value if isinstance(entry.value, str) else entry.value.decode('utf-8')
                    try:
                        error_code = int(value)
                    except ValueError:
                        error_message += f'\nError status: {value}'

            grpc_error = rpc_error.code()
            if grpc_error == grpc.StatusCode.NOT_FOUND:
                raise errors.DriverTooOldError() from None
            elif grpc_error == grpc.StatusCode.INVALID_ARGUMENT:
                raise ValueError(error_message) from None
            elif grpc_error == grpc.StatusCode.UNAVAILABLE:
                error_message = 'Failed to connect to server'
            elif grpc_error == grpc.StatusCode.UNIMPLEMENTED:
                error_message = (
                    'This operation is not supported by the NI gRPC Device Server being used. Upgrade NI gRPC Device Server.'
                )

            if error_code is None:
                raise errors.RpcError(grpc_error, error_message) from None

        if error_code < 0:
            raise errors.DriverError(error_code, error_message)
        elif error_code > 0:
            if not error_message:
                try:
                    error_message = self.error_message(error_code)
                except errors.Error:
                    error_message = 'Failed to retrieve error description.'
            warnings.warn(errors.DriverWarning(error_code, error_message))
        return response

    def abort(self):  # noqa: N802
        self._invoke(
            self._client.Abort,
            grpc_types.AbortRequest(vi=self._vi),
        )

    def allocate_arb_waveform(self, waveform_name, size_in_samples):  # noqa: N802
        self._invoke(
            self._client.AllocateArbWaveform,
            grpc_types.AllocateArbWaveformRequest(vi=self._vi, waveform_name=waveform_name, size_in_samples=size_in_samples),
        )

    def change_external_calibration_password(self, old_password, new_password):  # noqa: N802
        self._invoke(
            self._client.ChangeExternalCalibrationPassword,
            grpc_types.ChangeExternalCalibrationPasswordRequest(vi=self._vi, old_password=old_password, new_password=new_password),
        )

    def check_generation_status(self):  # noqa: N802
        response = self._invoke(
            self._client.CheckGenerationStatus,
            grpc_types.CheckGenerationStatusRequest(vi=self._vi),
        )
        return response.is_done

    def check_if_script_exists(self, script_name):  # noqa: N802
        response = self._invoke(
            self._client.CheckIfScriptExists,
            grpc_types.CheckIfScriptExistsRequest(vi=self._vi, script_name=script_name),
        )
        return response.script_exists

    def check_if_waveform_exists(self, waveform_name):  # noqa: N802
        response = self._invoke(
            self._client.CheckIfWaveformExists,
            grpc_types.CheckIfWaveformExistsRequest(vi=self._vi, waveform_name=waveform_name),
        )
        return response.waveform_exists

    def clear_all_arb_waveforms(self):  # noqa: N802
        self._invoke(
            self._client.ClearAllArbWaveforms,
            grpc_types.ClearAllArbWaveformsRequest(vi=self._vi),
        )

    def clear_arb_waveform(self, waveform_name):  # noqa: N802
        self._invoke(
            self._client.ClearArbWaveform,
            grpc_types.ClearArbWaveformRequest(vi=self._vi, name=waveform_name),
        )

    def clear_self_calibrate_range(self):  # noqa: N802
        self._invoke(
            self._client.ClearSelfCalibrateRange,
            grpc_types.ClearSelfCalibrateRangeRequest(vi=self._vi),
        )

    def commit(self):  # noqa: N802
        self._invoke(
            self._client.Commit,
            grpc_types.CommitRequest(vi=self._vi),
        )

    def configure_deembedding_table_interpolation_linear(self, port, table_name, format):  # noqa: N802
        self._invoke(
            self._client.ConfigureDeembeddingTableInterpolationLinear,
            grpc_types.ConfigureDeembeddingTableInterpolationLinearRequest(vi=self._vi, port=port, table_name=table_name, format_raw=format.value),
        )

    def configure_deembedding_table_interpolation_nearest(self, port, table_name):  # noqa: N802
        self._invoke(
            self._client.ConfigureDeembeddingTableInterpolationNearest,
            grpc_types.ConfigureDeembeddingTableInterpolationNearestRequest(vi=self._vi, port=port, table_name=table_name),
        )

    def configure_deembedding_table_interpolation_spline(self, port, table_name):  # noqa: N802
        self._invoke(
            self._client.ConfigureDeembeddingTableInterpolationSpline,
            grpc_types.ConfigureDeembeddingTableInterpolationSplineRequest(vi=self._vi, port=port, table_name=table_name),
        )

    def configure_digital_edge_script_trigger(self, trigger_id, source, edge):  # noqa: N802
        self._invoke(
            self._client.ConfigureDigitalEdgeScriptTrigger,
            grpc_types.ConfigureDigitalEdgeScriptTriggerRequest(vi=self._vi, trigger_id_raw=trigger_id, source_raw=source, edge_raw=edge.value),
        )

    def configure_digital_edge_start_trigger(self, source, edge):  # noqa: N802
        self._invoke(
            self._client.ConfigureDigitalEdgeStartTrigger,
            grpc_types.ConfigureDigitalEdgeStartTriggerRequest(vi=self._vi, source_raw=source, edge_raw=edge.value),
        )

    def configure_digital_level_script_trigger(self, trigger_id, source, level):  # noqa: N802
        self._invoke(
            self._client.ConfigureDigitalLevelScriptTrigger,
            grpc_types.ConfigureDigitalLevelScriptTriggerRequest(vi=self._vi, trigger_id_raw=trigger_id, source=source, level=level),
        )

    def configure_rf(self, frequency, power_level):  # noqa: N802
        self._invoke(
            self._client.ConfigureRF,
            grpc_types.ConfigureRFRequest(vi=self._vi, frequency=frequency, power_level=power_level),
        )

    def configure_ref_clock(self, ref_clock_source, ref_clock_rate):  # noqa: N802
        self._invoke(
            self._client.ConfigureRefClock,
            grpc_types.ConfigureRefClockRequest(vi=self._vi, ref_clock_source=ref_clock_source, ref_clock_rate=ref_clock_rate),
        )

    def configure_software_script_trigger(self, trigger_id):  # noqa: N802
        self._invoke(
            self._client.ConfigureSoftwareScriptTrigger,
            grpc_types.ConfigureSoftwareScriptTriggerRequest(vi=self._vi, trigger_id_raw=trigger_id),
        )

    def configure_software_start_trigger(self):  # noqa: N802
        self._invoke(
            self._client.ConfigureSoftwareStartTrigger,
            grpc_types.ConfigureSoftwareStartTriggerRequest(vi=self._vi),
        )

    def create_deembedding_sparameter_table_array(self, port, table_name, frequencies, sparameter_table, number_of_ports, sparameter_orientation):  # noqa: N802
        # Use ravel() so that gRPC always receives a flat numpy array, regardless of input dimensions.
        sparameter_table_list = [
            grpc_complex_types.NIComplexNumber(real=val.real, imaginary=val.imag)
            for val in sparameter_table.ravel()
        ]
        self._invoke(
            self._client.CreateDeembeddingSparameterTableArray,
            grpc_types.CreateDeembeddingSparameterTableArrayRequest(vi=self._vi, port=port, table_name=table_name, frequencies=frequencies, sparameter_table=sparameter_table_list, number_of_ports=number_of_ports, sparameter_orientation_raw=sparameter_orientation.value),
        )

    def create_deembedding_sparameter_table_s2p_file(self, port, table_name, s2p_file_path, sparameter_orientation):  # noqa: N802
        self._invoke(
            self._client.CreateDeembeddingSparameterTableS2PFile,
            grpc_types.CreateDeembeddingSparameterTableS2PFileRequest(vi=self._vi, port=port, table_name=table_name, s2p_file_path=s2p_file_path, sparameter_orientation_raw=sparameter_orientation.value),
        )

    def delete_all_deembedding_tables(self):  # noqa: N802
        self._invoke(
            self._client.DeleteAllDeembeddingTables,
            grpc_types.DeleteAllDeembeddingTablesRequest(vi=self._vi),
        )

    def delete_deembedding_table(self, port, table_name):  # noqa: N802
        self._invoke(
            self._client.DeleteDeembeddingTable,
            grpc_types.DeleteDeembeddingTableRequest(vi=self._vi, port=port, table_name=table_name),
        )

    def delete_script(self, script_name):  # noqa: N802
        self._invoke(
            self._client.DeleteScript,
            grpc_types.DeleteScriptRequest(vi=self._vi, script_name=script_name),
        )

    def disable_script_trigger(self, trigger_id):  # noqa: N802
        self._invoke(
            self._client.DisableScriptTrigger,
            grpc_types.DisableScriptTriggerRequest(vi=self._vi, trigger_id_raw=trigger_id),
        )

    def disable_start_trigger(self):  # noqa: N802
        self._invoke(
            self._client.DisableStartTrigger,
            grpc_types.DisableStartTriggerRequest(vi=self._vi),
        )

    def error_message(self, error_code, error_message):  # noqa: N802
        self._invoke(
            self._client.ErrorMessage,
            grpc_types.ErrorMessageRequest(vi=self._vi, error_code=error_code, error_message=error_message),
        )

    def get_all_named_waveform_names(self):  # noqa: N802
        response = self._invoke(
            self._client.GetAllNamedWaveformNames,
            grpc_types.GetAllNamedWaveformNamesRequest(vi=self._vi),
        )
        return response.waveform_names

    def get_all_script_names(self):  # noqa: N802
        response = self._invoke(
            self._client.GetAllScriptNames,
            grpc_types.GetAllScriptNamesRequest(vi=self._vi),
        )
        return response.script_names

    def get_attribute_vi_boolean(self, channel_name, attribute):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViBoolean,
            grpc_types.GetAttributeViBooleanRequest(vi=self._vi, channel_name=channel_name, attribute_id=attribute),
        )
        return response.value

    def get_attribute_vi_int32(self, channel_name, attribute):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViInt32,
            grpc_types.GetAttributeViInt32Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute),
        )
        return response.value

    def get_attribute_vi_int64(self, channel_name, attribute):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViInt64,
            grpc_types.GetAttributeViInt64Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute),
        )
        return response.value

    def get_attribute_vi_real64(self, channel_name, attribute):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViReal64,
            grpc_types.GetAttributeViReal64Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute),
        )
        return response.value

    def get_attribute_vi_session(self, channel_name, attribute):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViSession,
            grpc_types.GetAttributeViSessionRequest(vi=self._vi, channel_name=channel_name, attribute_id=attribute),
        )
        return response.value

    def get_attribute_vi_string(self, channel_name, attribute):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViString,
            grpc_types.GetAttributeViStringRequest(vi=self._vi, channel_name=channel_name, attribute_id=attribute),
        )
        return response.value

    def get_deembedding_sparameters(self):
        import numpy as np
        response = self._invoke(
            self._client.GetDeembeddingSparameters,
            grpc_types.GetDeembeddingSparametersRequest(vi=self._vi),
        )
        number_of_ports = response.number_of_ports
        sparameters = np.array([c.real + 1j * c.imaginary for c in response.sparameters], dtype=np.complex128)
        sparameters = sparameters.reshape((number_of_ports, number_of_ports))
        return sparameters

    def get_deembedding_table_number_of_ports(self):  # noqa: N802
        response = self._invoke(
            self._client.GetDeembeddingTableNumberOfPorts,
            grpc_types.GetDeembeddingTableNumberOfPortsRequest(vi=self._vi),
        )
        return response.number_of_ports

    def get_error(self):  # noqa: N802
        response = self._invoke(
            self._client.GetError,
            grpc_types.GetErrorRequest(vi=self._vi),
        )
        return response.error_code, response.error_description

    def get_external_calibration_last_date_and_time(self):  # noqa: N802
        response = self._invoke(
            self._client.GetExternalCalibrationLastDateAndTime,
            grpc_types.GetExternalCalibrationLastDateAndTimeRequest(vi=self._vi),
        )
        return response.year, response.month, response.day, response.hour, response.minute, response.second

    def get_max_settable_power(self):  # noqa: N802
        response = self._invoke(
            self._client.GetMaxSettablePower,
            grpc_types.GetMaxSettablePowerRequest(vi=self._vi),
        )
        return response.value

    def get_script(self, script_name):  # noqa: N802
        response = self._invoke(
            self._client.GetScript,
            grpc_types.GetScriptRequest(vi=self._vi, script_name=script_name),
        )
        return response.script

    def get_self_calibration_date_and_time(self, module):  # noqa: N802
        response = self._invoke(
            self._client.GetSelfCalibrationDateAndTime,
            grpc_types.GetSelfCalibrationDateAndTimeRequest(vi=self._vi, module=module.value),
        )
        return response.year, response.month, response.day, response.hour, response.minute, response.second

    def get_self_calibration_temperature(self, module):  # noqa: N802
        response = self._invoke(
            self._client.GetSelfCalibrationTemperature,
            grpc_types.GetSelfCalibrationTemperatureRequest(vi=self._vi, module_raw=module.value),
        )
        return response.temperature

    def get_terminal_name(self, signal, signal_identifier):  # noqa: N802
        response = self._invoke(
            self._client.GetTerminalName,
            grpc_types.GetTerminalNameRequest(vi=self._vi, signal_raw=signal.value, signal_identifier_raw=signal_identifier),
        )
        return response.terminal_name

    def get_waveform_burst_start_locations(self, channel_name):  # noqa: N802
        response = self._invoke(
            self._client.GetWaveformBurstStartLocations,
            grpc_types.GetWaveformBurstStartLocationsRequest(vi=self._vi, channel_name=channel_name),
        )
        return response.locations

    def get_waveform_burst_stop_locations(self, channel_name):  # noqa: N802
        response = self._invoke(
            self._client.GetWaveformBurstStopLocations,
            grpc_types.GetWaveformBurstStopLocationsRequest(vi=self._vi, channel_name=channel_name),
        )
        return response.locations

    def get_waveform_marker_event_locations(self, channel_name):  # noqa: N802
        response = self._invoke(
            self._client.GetWaveformMarkerEventLocations,
            grpc_types.GetWaveformMarkerEventLocationsRequest(vi=self._vi, channel_name=channel_name),
        )
        return response.locations

    def init_with_options(self, resource_name, id_query, reset_device, option_string):  # noqa: N802
        metadata = (
            ('ni-api-key', self._grpc_options.api_key),
        )
        response = self._invoke(
            self._client.InitWithOptions,
            grpc_types.InitWithOptionsRequest(resource_name=resource_name, id_query=id_query, reset_device=reset_device, option_string=option_string, session_name=self._grpc_options.session_name, initialization_behavior=self._grpc_options.initialization_behavior),
            metadata=metadata,
        )
        self._close_on_exit = response.new_session_initialized
        return response.vi

    def initiate(self):  # noqa: N802
        self._invoke(
            self._client.Initiate,
            grpc_types.InitiateRequest(vi=self._vi),
        )

    def load_configurations_from_file(self, channel_name, file_path):  # noqa: N802
        self._invoke(
            self._client.LoadConfigurationsFromFile,
            grpc_types.LoadConfigurationsFromFileRequest(vi=self._vi, channel_name=channel_name, file_path=file_path),
        )

    def lock(self):  # noqa: N802
        self._lock.acquire()

    def perform_power_search(self):  # noqa: N802
        self._invoke(
            self._client.PerformPowerSearch,
            grpc_types.PerformPowerSearchRequest(vi=self._vi),
        )

    def perform_thermal_correction(self):  # noqa: N802
        self._invoke(
            self._client.PerformThermalCorrection,
            grpc_types.PerformThermalCorrectionRequest(vi=self._vi),
        )

    def query_arb_waveform_capabilities(self):  # noqa: N802
        response = self._invoke(
            self._client.QueryArbWaveformCapabilities,
            grpc_types.QueryArbWaveformCapabilitiesRequest(vi=self._vi),
        )
        return response.max_number_waveforms, response.waveform_quantum, response.min_waveform_size, response.max_waveform_size

    def read_and_download_waveform_from_file_tdms(self, waveform_name, file_path, waveform_index):  # noqa: N802
        self._invoke(
            self._client.ReadAndDownloadWaveformFromFileTDMS,
            grpc_types.ReadAndDownloadWaveformFromFileTDMSRequest(vi=self._vi, waveform_name=waveform_name, file_path=file_path, waveform_index=waveform_index),
        )

    def reset_device(self):  # noqa: N802
        self._invoke(
            self._client.ResetDevice,
            grpc_types.ResetDeviceRequest(vi=self._vi),
        )

    def reset_with_defaults(self):  # noqa: N802
        self._invoke(
            self._client.ResetWithDefaults,
            grpc_types.ResetWithDefaultsRequest(vi=self._vi),
        )

    def reset_with_options(self, steps_to_omit):  # noqa: N802
        self._invoke(
            self._client.ResetWithOptions,
            grpc_types.ResetWithOptionsRequest(vi=self._vi, steps_to_omit_raw=steps_to_omit.value),
        )

    def save_configurations_to_file(self, channel_name, file_path):  # noqa: N802
        self._invoke(
            self._client.SaveConfigurationsToFile,
            grpc_types.SaveConfigurationsToFileRequest(vi=self._vi, channel_name=channel_name, file_path=file_path),
        )

    def select_arb_waveform(self, waveform_name):  # noqa: N802
        self._invoke(
            self._client.SelectArbWaveform,
            grpc_types.SelectArbWaveformRequest(vi=self._vi, name=waveform_name),
        )

    def self_cal(self):  # noqa: N802
        self._invoke(
            self._client.SelfCal,
            grpc_types.SelfCalRequest(vi=self._vi),
        )

    def self_calibrate_range(self, steps_to_omit, min_frequency, max_frequency, min_power_level, max_power_level):  # noqa: N802
        self._invoke(
            self._client.SelfCalibrateRange,
            grpc_types.SelfCalibrateRangeRequest(vi=self._vi, steps_to_omit_raw=steps_to_omit.value, min_frequency=min_frequency, max_frequency=max_frequency, min_power_level=min_power_level, max_power_level=max_power_level),
        )

    def send_software_edge_trigger(self, trigger, trigger_identifier):  # noqa: N802
        self._invoke(
            self._client.SendSoftwareEdgeTrigger,
            grpc_types.SendSoftwareEdgeTriggerRequest(vi=self._vi, trigger_raw=trigger.value, trigger_identifier_raw=trigger_identifier.value),
        )

    def set_arb_waveform_next_write_position(self, waveform_name, relative_to, offset):  # noqa: N802
        self._invoke(
            self._client.SetArbWaveformNextWritePosition,
            grpc_types.SetArbWaveformNextWritePositionRequest(vi=self._vi, waveform_name=waveform_name, relative_to_raw=relative_to.value, offset=offset),
        )

    def set_attribute_vi_boolean(self, channel_name, attribute, value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViBoolean,
            grpc_types.SetAttributeViBooleanRequest(vi=self._vi, channel_name=channel_name, attribute_id=attribute, value=value),
        )

    def set_attribute_vi_int32(self, channel_name, attribute, value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViInt32,
            grpc_types.SetAttributeViInt32Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute, value_raw=value),
        )

    def set_attribute_vi_int64(self, channel_name, attribute, value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViInt64,
            grpc_types.SetAttributeViInt64Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute, value_raw=value),
        )

    def set_attribute_vi_real64(self, channel_name, attribute, value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViReal64,
            grpc_types.SetAttributeViReal64Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute, value_raw=value),
        )

    def set_attribute_vi_session(self, channel_name, attribute):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViSession,
            grpc_types.SetAttributeViSessionRequest(vi=self._vi, channel_name=channel_name, attribute_id=attribute, value=self._vi),
        )

    def set_attribute_vi_string(self, channel_name, attribute, value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViString,
            grpc_types.SetAttributeViStringRequest(vi=self._vi, channel_name=channel_name, attribute_id=attribute, value_raw=value),
        )

    def set_waveform_burst_start_locations(self, channel_name, locations):  # noqa: N802
        self._invoke(
            self._client.SetWaveformBurstStartLocations,
            grpc_types.SetWaveformBurstStartLocationsRequest(vi=self._vi, channel_name=channel_name, locations=locations),
        )

    def set_waveform_burst_stop_locations(self, channel_name, locations):  # noqa: N802
        self._invoke(
            self._client.SetWaveformBurstStopLocations,
            grpc_types.SetWaveformBurstStopLocationsRequest(vi=self._vi, channel_name=channel_name, locations=locations),
        )

    def set_waveform_marker_event_locations(self, channel_name, locations):  # noqa: N802
        self._invoke(
            self._client.SetWaveformMarkerEventLocations,
            grpc_types.SetWaveformMarkerEventLocationsRequest(vi=self._vi, channel_name=channel_name, locations=locations),
        )

    def unlock(self):  # noqa: N802
        self._lock.release()

    def wait_until_settled(self, max_time_milliseconds):  # noqa: N802
        self._invoke(
            self._client.WaitUntilSettled,
            grpc_types.WaitUntilSettledRequest(vi=self._vi, max_time_milliseconds=max_time_milliseconds),
        )

    def write_arb_waveform_complex_f32(self, waveform_name, waveform_data_array, more_data_pending):  # noqa: N802
        # Use ravel() so that gRPC always receives a flat numpy array, regardless of input dimensions.
        waveform_data_array_list = [
            grpc_complex_types.NIComplexNumberF32(real=val.real, imaginary=val.imag)
            for val in waveform_data_array.ravel()
        ]
        self._invoke(
            self._client.WriteArbWaveformComplexF32,
            grpc_types.WriteArbWaveformComplexF32Request(vi=self._vi, waveform_name=waveform_name, wfm_data=waveform_data_array_list, more_data_pending=more_data_pending),
        )

    def write_arb_waveform_complex_f64(self, waveform_name, waveform_data_array, more_data_pending):  # noqa: N802
        # Use ravel() so that gRPC always receives a flat numpy array, regardless of input dimensions.
        waveform_data_array_list = [
            grpc_complex_types.NIComplexNumber(real=val.real, imaginary=val.imag)
            for val in waveform_data_array.ravel()
        ]
        self._invoke(
            self._client.WriteArbWaveformComplexF64,
            grpc_types.WriteArbWaveformComplexF64Request(vi=self._vi, waveform_name=waveform_name, wfm_data=waveform_data_array_list, more_data_pending=more_data_pending),
        )

    def write_arb_waveform_complex_i16(self, waveform_name, waveform_data_array):  # noqa: N802
        # Use ravel() so that gRPC always receives a flat numpy array, regardless of input dimensions.
        arr = waveform_data_array.ravel()
        if arr.size % 2 != 0:
            raise ValueError("Interleaved int16 array must have even length (real/imag pairs)")
        arr_pairs = arr.reshape(-1, 2)
        waveform_data_array_list = [
            grpc_complex_types.NIComplexI16(real=int(pair[0]), imaginary=int(pair[1]))
            for pair in arr_pairs
        ]
        self._invoke(
            self._client.WriteArbWaveformComplexI16,
            grpc_types.WriteArbWaveformComplexI16Request(vi=self._vi, waveform_name=waveform_name, wfm_data=waveform_data_array_list),
        )

    def write_script(self, script):  # noqa: N802
        self._invoke(
            self._client.WriteScript,
            grpc_types.WriteScriptRequest(vi=self._vi, script=script),
        )

    def close(self):  # noqa: N802
        self._invoke(
            self._client.Close,
            grpc_types.CloseRequest(vi=self._vi),
        )

    def reset(self):  # noqa: N802
        self._invoke(
            self._client.Reset,
            grpc_types.ResetRequest(vi=self._vi),
        )

    def self_test(self):  # noqa: N802
        response = self._invoke(
            self._client.SelfTest,
            grpc_types.SelfTestRequest(vi=self._vi),
        )
        return response.self_test_result, response.self_test_message
