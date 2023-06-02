# -*- coding: utf-8 -*-
# This file was generated

import grpc
import hightime  # noqa: F401
import threading
import warnings

from . import enums as enums  # noqa: F401
from . import errors as errors
from . import nifgen_pb2 as grpc_types
from . import nifgen_pb2_grpc as nifgen_grpc
from . import session_pb2 as session_grpc_types


class GrpcStubInterpreter(object):
    '''Interpreter for interacting with a gRPC Stub class'''

    def __init__(self, grpc_options):
        self._grpc_options = grpc_options
        self._lock = threading.RLock()
        self._client = nifgen_grpc.NiFgenStub(grpc_options.grpc_channel)
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
            self._client.AbortGeneration,
            grpc_types.AbortGenerationRequest(vi=self._vi),
        )

    def allocate_named_waveform(self, channel_name, waveform_name, waveform_size):  # noqa: N802
        self._invoke(
            self._client.AllocateNamedWaveform,
            grpc_types.AllocateNamedWaveformRequest(vi=self._vi, channel_name=channel_name, waveform_name=waveform_name, waveform_size=waveform_size),
        )

    def allocate_waveform(self, channel_name, waveform_size):  # noqa: N802
        response = self._invoke(
            self._client.AllocateWaveform,
            grpc_types.AllocateWaveformRequest(vi=self._vi, channel_name=channel_name, waveform_size=waveform_size),
        )
        return response.waveform_handle

    def clear_arb_memory(self):  # noqa: N802
        self._invoke(
            self._client.ClearArbMemory,
            grpc_types.ClearArbMemoryRequest(vi=self._vi),
        )

    def clear_arb_sequence(self, sequence_handle):  # noqa: N802
        self._invoke(
            self._client.ClearArbSequence,
            grpc_types.ClearArbSequenceRequest(vi=self._vi, sequence_handle_raw=sequence_handle),
        )

    def clear_arb_waveform(self, waveform_handle):  # noqa: N802
        self._invoke(
            self._client.ClearArbWaveform,
            grpc_types.ClearArbWaveformRequest(vi=self._vi, waveform_handle_raw=waveform_handle),
        )

    def clear_freq_list(self, frequency_list_handle):  # noqa: N802
        self._invoke(
            self._client.ClearFreqList,
            grpc_types.ClearFreqListRequest(vi=self._vi, frequency_list_handle_raw=frequency_list_handle),
        )

    def clear_user_standard_waveform(self, channel_name):  # noqa: N802
        self._invoke(
            self._client.ClearUserStandardWaveform,
            grpc_types.ClearUserStandardWaveformRequest(vi=self._vi, channel_name=channel_name),
        )

    def commit(self):  # noqa: N802
        self._invoke(
            self._client.Commit,
            grpc_types.CommitRequest(vi=self._vi),
        )

    def configure_arb_sequence(self, channel_name, sequence_handle, gain, offset):  # noqa: N802
        self._invoke(
            self._client.ConfigureArbSequence,
            grpc_types.ConfigureArbSequenceRequest(vi=self._vi, channel_name=channel_name, sequence_handle=sequence_handle, gain=gain, offset=offset),
        )

    def configure_arb_waveform(self, channel_name, waveform_handle, gain, offset):  # noqa: N802
        self._invoke(
            self._client.ConfigureArbWaveform,
            grpc_types.ConfigureArbWaveformRequest(vi=self._vi, channel_name=channel_name, waveform_handle=waveform_handle, gain=gain, offset=offset),
        )

    def configure_freq_list(self, channel_name, frequency_list_handle, amplitude, dc_offset, start_phase):  # noqa: N802
        self._invoke(
            self._client.ConfigureFreqList,
            grpc_types.ConfigureFreqListRequest(vi=self._vi, channel_name=channel_name, frequency_list_handle=frequency_list_handle, amplitude=amplitude, dc_offset=dc_offset, start_phase=start_phase),
        )

    def configure_standard_waveform(self, channel_name, waveform, amplitude, dc_offset, frequency, start_phase):  # noqa: N802
        self._invoke(
            self._client.ConfigureStandardWaveform,
            grpc_types.ConfigureStandardWaveformRequest(vi=self._vi, channel_name=channel_name, waveform_raw=waveform.value, amplitude=amplitude, dc_offset=dc_offset, frequency=frequency, start_phase=start_phase),
        )

    def create_advanced_arb_sequence(self, waveform_handles_array, loop_counts_array, sample_counts_array, marker_location_array):  # noqa: N802
        response = self._invoke(
            self._client.CreateAdvancedArbSequence,
            grpc_types.CreateAdvancedArbSequenceRequest(vi=self._vi, waveform_handles_array=waveform_handles_array, loop_counts_array=loop_counts_array, sample_counts_array=sample_counts_array, marker_location_array=marker_location_array),
        )
        return response.coerced_markers_array, response.sequence_handle

    def create_arb_sequence(self, waveform_handles_array, loop_counts_array):  # noqa: N802
        response = self._invoke(
            self._client.CreateArbSequence,
            grpc_types.CreateArbSequenceRequest(vi=self._vi, waveform_handles_array=waveform_handles_array, loop_counts_array=loop_counts_array),
        )
        return response.sequence_handle

    def create_freq_list(self, waveform, frequency_array, duration_array):  # noqa: N802
        response = self._invoke(
            self._client.CreateFreqList,
            grpc_types.CreateFreqListRequest(vi=self._vi, waveform_raw=waveform.value, frequency_array=frequency_array, duration_array=duration_array),
        )
        return response.frequency_list_handle

    def create_waveform_f64(self, channel_name, waveform_data_array):  # noqa: N802
        response = self._invoke(
            self._client.CreateWaveformF64,
            grpc_types.CreateWaveformF64Request(vi=self._vi, channel_name=channel_name, waveform_data_array=waveform_data_array),
        )
        return response.waveform_handle

    def create_waveform_f64_numpy(self, channel_name, waveform_data_array):  # noqa: N802
        raise NotImplementedError('numpy-specific methods are not supported over gRPC')

    def create_waveform_from_file_f64(self, channel_name, file_name, byte_order):  # noqa: N802
        response = self._invoke(
            self._client.CreateWaveformFromFileF64,
            grpc_types.CreateWaveformFromFileF64Request(vi=self._vi, channel_name=channel_name, file_name=file_name, byte_order_raw=byte_order.value),
        )
        return response.waveform_handle

    def create_waveform_from_file_i16(self, channel_name, file_name, byte_order):  # noqa: N802
        response = self._invoke(
            self._client.CreateWaveformFromFileI16,
            grpc_types.CreateWaveformFromFileI16Request(vi=self._vi, channel_name=channel_name, file_name=file_name, byte_order_raw=byte_order.value),
        )
        return response.waveform_handle

    def create_waveform_i16_numpy(self, channel_name, waveform_data_array):  # noqa: N802
        raise NotImplementedError('numpy-specific methods are not supported over gRPC')

    def define_user_standard_waveform(self, channel_name, waveform_data_array):  # noqa: N802
        self._invoke(
            self._client.DefineUserStandardWaveform,
            grpc_types.DefineUserStandardWaveformRequest(vi=self._vi, channel_name=channel_name, waveform_data_array=waveform_data_array),
        )

    def delete_named_waveform(self, channel_name, waveform_name):  # noqa: N802
        self._invoke(
            self._client.DeleteNamedWaveform,
            grpc_types.DeleteNamedWaveformRequest(vi=self._vi, channel_name=channel_name, waveform_name=waveform_name),
        )

    def delete_script(self, channel_name, script_name):  # noqa: N802
        self._invoke(
            self._client.DeleteScript,
            grpc_types.DeleteScriptRequest(vi=self._vi, channel_name=channel_name, script_name=script_name),
        )

    def disable(self):  # noqa: N802
        self._invoke(
            self._client.Disable,
            grpc_types.DisableRequest(vi=self._vi),
        )

    def export_attribute_configuration_buffer(self):  # noqa: N802
        response = self._invoke(
            self._client.ExportAttributeConfigurationBuffer,
            grpc_types.ExportAttributeConfigurationBufferRequest(vi=self._vi),
        )
        return response.configuration

    def export_attribute_configuration_file(self, file_path):  # noqa: N802
        self._invoke(
            self._client.ExportAttributeConfigurationFile,
            grpc_types.ExportAttributeConfigurationFileRequest(vi=self._vi, file_path=file_path),
        )

    def get_attribute_vi_boolean(self, channel_name, attribute_id):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViBoolean,
            grpc_types.GetAttributeViBooleanRequest(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id),
        )
        return response.attribute_value

    def get_attribute_vi_int32(self, channel_name, attribute_id):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViInt32,
            grpc_types.GetAttributeViInt32Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id),
        )
        return response.attribute_value

    def get_attribute_vi_real64(self, channel_name, attribute_id):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViReal64,
            grpc_types.GetAttributeViReal64Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id),
        )
        return response.attribute_value

    def get_attribute_vi_string(self, channel_name, attribute_id):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViString,
            grpc_types.GetAttributeViStringRequest(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id),
        )
        return response.attribute_value

    def get_channel_name(self, index):  # noqa: N802
        response = self._invoke(
            self._client.GetChannelName,
            grpc_types.GetChannelNameRequest(vi=self._vi, index=index),
        )
        return response.channel_string

    def get_error(self):  # noqa: N802
        response = self._invoke(
            self._client.GetError,
            grpc_types.GetErrorRequest(vi=self._vi),
        )
        return response.error_code, response.error_description

    def get_ext_cal_last_date_and_time(self):  # noqa: N802
        response = self._invoke(
            self._client.GetExtCalLastDateAndTime,
            grpc_types.GetExtCalLastDateAndTimeRequest(vi=self._vi),
        )
        return response.year, response.month, response.day, response.hour, response.minute

    def get_ext_cal_last_temp(self):  # noqa: N802
        response = self._invoke(
            self._client.GetExtCalLastTemp,
            grpc_types.GetExtCalLastTempRequest(vi=self._vi),
        )
        return response.temperature

    def get_ext_cal_recommended_interval(self):  # noqa: N802
        response = self._invoke(
            self._client.GetExtCalRecommendedInterval,
            grpc_types.GetExtCalRecommendedIntervalRequest(vi=self._vi),
        )
        return response.months

    def get_hardware_state(self):  # noqa: N802
        response = self._invoke(
            self._client.GetHardwareState,
            grpc_types.GetHardwareStateRequest(vi=self._vi),
        )
        return enums.HardwareState(response.state_raw)

    def get_self_cal_last_date_and_time(self):  # noqa: N802
        response = self._invoke(
            self._client.GetSelfCalLastDateAndTime,
            grpc_types.GetSelfCalLastDateAndTimeRequest(vi=self._vi),
        )
        return response.year, response.month, response.day, response.hour, response.minute

    def get_self_cal_last_temp(self):  # noqa: N802
        response = self._invoke(
            self._client.GetSelfCalLastTemp,
            grpc_types.GetSelfCalLastTempRequest(vi=self._vi),
        )
        return response.temperature

    def get_self_cal_supported(self):  # noqa: N802
        response = self._invoke(
            self._client.GetSelfCalSupported,
            grpc_types.GetSelfCalSupportedRequest(vi=self._vi),
        )
        return response.self_cal_supported

    def import_attribute_configuration_buffer(self, configuration):  # noqa: N802
        self._invoke(
            self._client.ImportAttributeConfigurationBuffer,
            grpc_types.ImportAttributeConfigurationBufferRequest(vi=self._vi, configuration=configuration),
        )

    def import_attribute_configuration_file(self, file_path):  # noqa: N802
        self._invoke(
            self._client.ImportAttributeConfigurationFile,
            grpc_types.ImportAttributeConfigurationFileRequest(vi=self._vi, file_path=file_path),
        )

    def initialize_with_channels(self, resource_name, channel_name, reset_device, option_string):  # noqa: N802
        metadata = (
            ('ni-api-key', self._grpc_options.api_key),
        )
        response = self._invoke(
            self._client.InitializeWithChannels,
            grpc_types.InitializeWithChannelsRequest(resource_name=resource_name, channel_name=channel_name, reset_device=reset_device, option_string=option_string, session_name=self._grpc_options.session_name, initialization_behavior=self._grpc_options.initialization_behavior),
            metadata=metadata,
        )
        self._close_on_exit = response.new_session_initialized
        return response.vi

    def initiate_generation(self):  # noqa: N802
        self._invoke(
            self._client.InitiateGeneration,
            grpc_types.InitiateGenerationRequest(vi=self._vi),
        )

    def is_done(self):  # noqa: N802
        response = self._invoke(
            self._client.IsDone,
            grpc_types.IsDoneRequest(vi=self._vi),
        )
        return response.done

    def lock(self):  # noqa: N802
        self._lock.acquire()

    def query_arb_seq_capabilities(self):  # noqa: N802
        response = self._invoke(
            self._client.QueryArbSeqCapabilities,
            grpc_types.QueryArbSeqCapabilitiesRequest(vi=self._vi),
        )
        return response.maximum_number_of_sequences, response.minimum_sequence_length, response.maximum_sequence_length, response.maximum_loop_count

    def query_arb_wfm_capabilities(self):  # noqa: N802
        response = self._invoke(
            self._client.QueryArbWfmCapabilities,
            grpc_types.QueryArbWfmCapabilitiesRequest(vi=self._vi),
        )
        return response.maximum_number_of_waveforms, response.waveform_quantum, response.minimum_waveform_size, response.maximum_waveform_size

    def query_freq_list_capabilities(self):  # noqa: N802
        response = self._invoke(
            self._client.QueryFreqListCapabilities,
            grpc_types.QueryFreqListCapabilitiesRequest(vi=self._vi),
        )
        return response.maximum_number_of_freq_lists, response.minimum_frequency_list_length, response.maximum_frequency_list_length, response.minimum_frequency_list_duration, response.maximum_frequency_list_duration, response.frequency_list_duration_quantum

    def read_current_temperature(self):  # noqa: N802
        response = self._invoke(
            self._client.ReadCurrentTemperature,
            grpc_types.ReadCurrentTemperatureRequest(vi=self._vi),
        )
        return response.temperature

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

    def self_cal(self):  # noqa: N802
        self._invoke(
            self._client.SelfCal,
            grpc_types.SelfCalRequest(vi=self._vi),
        )

    def send_software_edge_trigger(self, trigger, trigger_id):  # noqa: N802
        self._invoke(
            self._client.SendSoftwareEdgeTrigger,
            grpc_types.SendSoftwareEdgeTriggerRequest(vi=self._vi, trigger_raw=trigger.value, trigger_id=trigger_id),
        )

    def set_attribute_vi_boolean(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViBoolean,
            grpc_types.SetAttributeViBooleanRequest(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id, attribute_value=attribute_value),
        )

    def set_attribute_vi_int32(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViInt32,
            grpc_types.SetAttributeViInt32Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id, attribute_value_raw=attribute_value),
        )

    def set_attribute_vi_real64(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViReal64,
            grpc_types.SetAttributeViReal64Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id, attribute_value_raw=attribute_value),
        )

    def set_attribute_vi_string(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViString,
            grpc_types.SetAttributeViStringRequest(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id, attribute_value_raw=attribute_value),
        )

    def set_named_waveform_next_write_position(self, channel_name, waveform_name, relative_to, offset):  # noqa: N802
        self._invoke(
            self._client.SetNamedWaveformNextWritePosition,
            grpc_types.SetNamedWaveformNextWritePositionRequest(vi=self._vi, channel_name=channel_name, waveform_name=waveform_name, relative_to_raw=relative_to.value, offset=offset),
        )

    def set_runtime_environment(self, environment, environment_version, reserved1, reserved2):  # noqa: N802
        raise NotImplementedError('set_runtime_environment is not supported over gRPC')

    def set_waveform_next_write_position(self, channel_name, waveform_handle, relative_to, offset):  # noqa: N802
        self._invoke(
            self._client.SetWaveformNextWritePosition,
            grpc_types.SetWaveformNextWritePositionRequest(vi=self._vi, channel_name=channel_name, waveform_handle=waveform_handle, relative_to_raw=relative_to.value, offset=offset),
        )

    def unlock(self):  # noqa: N802
        self._lock.release()

    def wait_until_done(self, max_time):  # noqa: N802
        self._invoke(
            self._client.WaitUntilDone,
            grpc_types.WaitUntilDoneRequest(vi=self._vi, max_time=max_time),
        )

    def write_binary16_waveform_numpy(self, channel_name, waveform_handle, data):  # noqa: N802
        raise NotImplementedError('numpy-specific methods are not supported over gRPC')

    def write_named_waveform_f64(self, channel_name, waveform_name, data):  # noqa: N802
        self._invoke(
            self._client.WriteNamedWaveformF64,
            grpc_types.WriteNamedWaveformF64Request(vi=self._vi, channel_name=channel_name, waveform_name=waveform_name, data=data),
        )

    def write_named_waveform_f64_numpy(self, channel_name, waveform_name, data):  # noqa: N802
        raise NotImplementedError('numpy-specific methods are not supported over gRPC')

    def write_named_waveform_i16_numpy(self, channel_name, waveform_name, data):  # noqa: N802
        raise NotImplementedError('numpy-specific methods are not supported over gRPC')

    def write_script(self, channel_name, script):  # noqa: N802
        self._invoke(
            self._client.WriteScript,
            grpc_types.WriteScriptRequest(vi=self._vi, channel_name=channel_name, script=script),
        )

    def write_waveform(self, channel_name, waveform_handle, data):  # noqa: N802
        self._invoke(
            self._client.WriteWaveform,
            grpc_types.WriteWaveformRequest(vi=self._vi, channel_name=channel_name, waveform_handle=waveform_handle, data=data),
        )

    def write_waveform_numpy(self, channel_name, waveform_handle, data):  # noqa: N802
        raise NotImplementedError('numpy-specific methods are not supported over gRPC')

    def close(self):  # noqa: N802
        self._invoke(
            self._client.Close,
            grpc_types.CloseRequest(vi=self._vi),
        )

    def error_message(self, error_code):  # noqa: N802
        response = self._invoke(
            self._client.ErrorMessage,
            grpc_types.ErrorMessageRequest(vi=self._vi, error_code=error_code),
        )
        return response.error_message

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
