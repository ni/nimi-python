# -*- coding: utf-8 -*-
# This file was generated

import grpc
import hightime  # noqa: F401
import threading
import warnings

from . import enums as enums  # noqa: F401
from . import errors as errors
from . import niscope_pb2 as grpc_types
from . import niscope_pb2_grpc as niscope_grpc
from . import session_pb2 as session_grpc_types

from . import waveform_info as waveform_info  # noqa: F401

from . import measurement_stats as measurement_stats  # noqa: F401


class GrpcStubInterpreter(object):
    '''Interpreter for interacting with a gRPC Stub class'''

    def __init__(self, grpc_options):
        self._grpc_options = grpc_options
        self._lock = threading.RLock()
        self._client = niscope_grpc.NiScopeStub(grpc_options.grpc_channel)
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

    def acquisition_status(self):  # noqa: N802
        response = self._invoke(
            self._client.AcquisitionStatus,
            grpc_types.AcquisitionStatusRequest(vi=self._vi),
        )
        return enums.AcquisitionStatus(response.acquisition_status_raw)

    def actual_meas_wfm_size(self, array_meas_function):  # noqa: N802
        response = self._invoke(
            self._client.ActualMeasWfmSize,
            grpc_types.ActualMeasWfmSizeRequest(vi=self._vi, array_meas_function_raw=array_meas_function.value),
        )
        return response.meas_waveform_size

    def actual_num_wfms(self, channel_list):  # noqa: N802
        response = self._invoke(
            self._client.ActualNumWfms,
            grpc_types.ActualNumWfmsRequest(vi=self._vi, channel_list=channel_list),
        )
        return response.num_wfms

    def add_waveform_processing(self, channel_list, meas_function):  # noqa: N802
        self._invoke(
            self._client.AddWaveformProcessing,
            grpc_types.AddWaveformProcessingRequest(vi=self._vi, channel_list=channel_list, meas_function_raw=meas_function.value),
        )

    def auto_setup(self):  # noqa: N802
        self._invoke(
            self._client.AutoSetup,
            grpc_types.AutoSetupRequest(vi=self._vi),
        )

    def cal_fetch_date(self, which_one):  # noqa: N802
        response = self._invoke(
            self._client.CalFetchDate,
            grpc_types.CalFetchDateRequest(vi=self._vi, which_one_raw=which_one.value),
        )
        return response.year, response.month, response.day

    def cal_fetch_temperature(self, which_one):  # noqa: N802
        response = self._invoke(
            self._client.CalFetchTemperature,
            grpc_types.CalFetchTemperatureRequest(vi=self._vi, which_one_raw=which_one),
        )
        return response.temperature

    def self_cal(self, channel_list, option):  # noqa: N802
        self._invoke(
            self._client.CalSelfCalibrate,
            grpc_types.CalSelfCalibrateRequest(vi=self._vi, channel_list=channel_list, option_raw=option.value),
        )

    def clear_waveform_measurement_stats(self, channel_list, clearable_measurement_function):  # noqa: N802
        self._invoke(
            self._client.ClearWaveformMeasurementStats,
            grpc_types.ClearWaveformMeasurementStatsRequest(vi=self._vi, channel_list=channel_list, clearable_measurement_function_raw=clearable_measurement_function.value),
        )

    def clear_waveform_processing(self, channel_list):  # noqa: N802
        self._invoke(
            self._client.ClearWaveformProcessing,
            grpc_types.ClearWaveformProcessingRequest(vi=self._vi, channel_list=channel_list),
        )

    def commit(self):  # noqa: N802
        self._invoke(
            self._client.Commit,
            grpc_types.CommitRequest(vi=self._vi),
        )

    def configure_chan_characteristics(self, channel_list, input_impedance, max_input_frequency):  # noqa: N802
        self._invoke(
            self._client.ConfigureChanCharacteristics,
            grpc_types.ConfigureChanCharacteristicsRequest(vi=self._vi, channel_list=channel_list, input_impedance=input_impedance, max_input_frequency=max_input_frequency),
        )

    def configure_equalization_filter_coefficients(self, channel_list, coefficients):  # noqa: N802
        self._invoke(
            self._client.ConfigureEqualizationFilterCoefficients,
            grpc_types.ConfigureEqualizationFilterCoefficientsRequest(vi=self._vi, channel_list=channel_list, coefficients=coefficients),
        )

    def configure_horizontal_timing(self, min_sample_rate, min_num_pts, ref_position, num_records, enforce_realtime):  # noqa: N802
        self._invoke(
            self._client.ConfigureHorizontalTiming,
            grpc_types.ConfigureHorizontalTimingRequest(vi=self._vi, min_sample_rate=min_sample_rate, min_num_pts=min_num_pts, ref_position=ref_position, num_records=num_records, enforce_realtime=enforce_realtime),
        )

    def configure_ref_levels(self, low, mid, high):  # noqa: N802
        raise NotImplementedError('configure_ref_levels is not supported over gRPC')

    def configure_trigger_digital(self, trigger_source, slope, holdoff, delay):  # noqa: N802
        self._invoke(
            self._client.ConfigureTriggerDigital,
            grpc_types.ConfigureTriggerDigitalRequest(vi=self._vi, trigger_source=trigger_source, slope_raw=slope.value, holdoff=holdoff, delay=delay),
        )

    def configure_trigger_edge(self, trigger_source, level, slope, trigger_coupling, holdoff, delay):  # noqa: N802
        self._invoke(
            self._client.ConfigureTriggerEdge,
            grpc_types.ConfigureTriggerEdgeRequest(vi=self._vi, trigger_source=trigger_source, level=level, slope_raw=slope.value, trigger_coupling_raw=trigger_coupling.value, holdoff=holdoff, delay=delay),
        )

    def configure_trigger_hysteresis(self, trigger_source, level, hysteresis, slope, trigger_coupling, holdoff, delay):  # noqa: N802
        self._invoke(
            self._client.ConfigureTriggerHysteresis,
            grpc_types.ConfigureTriggerHysteresisRequest(vi=self._vi, trigger_source=trigger_source, level=level, hysteresis=hysteresis, slope_raw=slope.value, trigger_coupling_raw=trigger_coupling.value, holdoff=holdoff, delay=delay),
        )

    def configure_trigger_immediate(self):  # noqa: N802
        self._invoke(
            self._client.ConfigureTriggerImmediate,
            grpc_types.ConfigureTriggerImmediateRequest(vi=self._vi),
        )

    def configure_trigger_software(self, holdoff, delay):  # noqa: N802
        self._invoke(
            self._client.ConfigureTriggerSoftware,
            grpc_types.ConfigureTriggerSoftwareRequest(vi=self._vi, holdoff=holdoff, delay=delay),
        )

    def configure_trigger_video(self, trigger_source, enable_dc_restore, signal_format, event, line_number, polarity, trigger_coupling, holdoff, delay):  # noqa: N802
        self._invoke(
            self._client.ConfigureTriggerVideo,
            grpc_types.ConfigureTriggerVideoRequest(vi=self._vi, trigger_source=trigger_source, enable_dc_restore=enable_dc_restore, signal_format_raw=signal_format.value, event_raw=event.value, line_number=line_number, polarity_raw=polarity.value, trigger_coupling_raw=trigger_coupling.value, holdoff=holdoff, delay=delay),
        )

    def configure_trigger_window(self, trigger_source, low_level, high_level, window_mode, trigger_coupling, holdoff, delay):  # noqa: N802
        self._invoke(
            self._client.ConfigureTriggerWindow,
            grpc_types.ConfigureTriggerWindowRequest(vi=self._vi, trigger_source=trigger_source, low_level=low_level, high_level=high_level, window_mode_raw=window_mode.value, trigger_coupling_raw=trigger_coupling.value, holdoff=holdoff, delay=delay),
        )

    def configure_vertical(self, channel_list, range, offset, coupling, probe_attenuation, enabled):  # noqa: N802
        self._invoke(
            self._client.ConfigureVertical,
            grpc_types.ConfigureVerticalRequest(vi=self._vi, channel_list=channel_list, range=range, offset=offset, coupling_raw=coupling.value, probe_attenuation=probe_attenuation, enabled=enabled),
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

    def fetch(self, channel_list, timeout, num_samples):  # noqa: N802
        response = self._invoke(
            self._client.Fetch,
            grpc_types.FetchRequest(vi=self._vi, channel_list=channel_list, timeout=timeout, num_samples=num_samples),
        )
        return response.waveform, [waveform_info.WaveformInfo(x) for x in response.wfm_info]

    def fetch_into_numpy(self, channel_list, timeout, num_samples):  # noqa: N802
        raise NotImplementedError('numpy-specific methods are not supported over gRPC')

    def fetch_array_measurement(self, channel_list, timeout, array_meas_function, measurement_waveform_size):  # noqa: N802
        response = self._invoke(
            self._client.FetchArrayMeasurement,
            grpc_types.FetchArrayMeasurementRequest(vi=self._vi, channel_list=channel_list, timeout=timeout, array_meas_function_raw=array_meas_function.value, meas_wfm_size=measurement_waveform_size),
        )
        return response.meas_wfm, [waveform_info.WaveformInfo(x) for x in response.wfm_info]

    def fetch_binary16_into_numpy(self, channel_list, timeout, num_samples):  # noqa: N802
        raise NotImplementedError('numpy-specific methods are not supported over gRPC')

    def fetch_binary32_into_numpy(self, channel_list, timeout, num_samples):  # noqa: N802
        raise NotImplementedError('numpy-specific methods are not supported over gRPC')

    def fetch_binary8_into_numpy(self, channel_list, timeout, num_samples):  # noqa: N802
        raise NotImplementedError('numpy-specific methods are not supported over gRPC')

    def fetch_measurement_stats(self, channel_list, timeout, scalar_meas_function):  # noqa: N802
        response = self._invoke(
            self._client.FetchMeasurementStats,
            grpc_types.FetchMeasurementStatsRequest(vi=self._vi, channel_list=channel_list, timeout=timeout, scalar_meas_function_raw=scalar_meas_function.value),
        )
        return response.result, response.mean, response.stdev, response.min, response.max, response.num_in_stats

    def get_attribute_vi_boolean(self, channel_list, attribute_id):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViBoolean,
            grpc_types.GetAttributeViBooleanRequest(vi=self._vi, channel_list=channel_list, attribute_id=attribute_id),
        )
        return response.value

    def get_attribute_vi_int32(self, channel_list, attribute_id):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViInt32,
            grpc_types.GetAttributeViInt32Request(vi=self._vi, channel_list=channel_list, attribute_id=attribute_id),
        )
        return response.value

    def get_attribute_vi_int64(self, channel_list, attribute_id):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViInt64,
            grpc_types.GetAttributeViInt64Request(vi=self._vi, channel_list=channel_list, attribute_id=attribute_id),
        )
        return response.value

    def get_attribute_vi_real64(self, channel_list, attribute_id):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViReal64,
            grpc_types.GetAttributeViReal64Request(vi=self._vi, channel_list=channel_list, attribute_id=attribute_id),
        )
        return response.value

    def get_attribute_vi_string(self, channel_list, attribute_id):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViString,
            grpc_types.GetAttributeViStringRequest(vi=self._vi, channel_list=channel_list, attribute_id=attribute_id),
        )
        return response.value

    def get_channel_names(self, indices):  # noqa: N802
        response = self._invoke(
            self._client.GetChannelNameFromString,
            grpc_types.GetChannelNameFromStringRequest(vi=self._vi, index=indices),
        )
        return response.name

    def get_equalization_filter_coefficients(self, channel, number_of_coefficients):  # noqa: N802
        response = self._invoke(
            self._client.GetEqualizationFilterCoefficients,
            grpc_types.GetEqualizationFilterCoefficientsRequest(vi=self._vi, channel=channel, number_of_coefficients=number_of_coefficients),
        )
        return response.coefficients

    def get_error(self):  # noqa: N802
        response = self._invoke(
            self._client.GetError,
            grpc_types.GetErrorRequest(vi=self._vi),
        )
        return response.error_code, response.description

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

    def initiate_acquisition(self):  # noqa: N802
        self._invoke(
            self._client.InitiateAcquisition,
            grpc_types.InitiateAcquisitionRequest(vi=self._vi),
        )

    def lock(self):  # noqa: N802
        self._lock.acquire()

    def probe_compensation_signal_start(self):  # noqa: N802
        self._invoke(
            self._client.ProbeCompensationSignalStart,
            grpc_types.ProbeCompensationSignalStartRequest(vi=self._vi),
        )

    def probe_compensation_signal_stop(self):  # noqa: N802
        self._invoke(
            self._client.ProbeCompensationSignalStop,
            grpc_types.ProbeCompensationSignalStopRequest(vi=self._vi),
        )

    def read(self, channel_list, timeout, num_samples):  # noqa: N802
        response = self._invoke(
            self._client.Read,
            grpc_types.ReadRequest(vi=self._vi, channel_list=channel_list, timeout=timeout, num_samples=num_samples),
        )
        return response.waveform, [waveform_info.WaveformInfo(x) for x in response.wfm_info]

    def reset_device(self):  # noqa: N802
        self._invoke(
            self._client.ResetDevice,
            grpc_types.ResetDeviceRequest(vi=self._vi),
        )

    def reset_with_defaults(self):  # noqa: N802
        raise NotImplementedError('reset_with_defaults is not supported over gRPC')

    def send_software_trigger_edge(self, which_trigger):  # noqa: N802
        self._invoke(
            self._client.SendSoftwareTriggerEdge,
            grpc_types.SendSoftwareTriggerEdgeRequest(vi=self._vi, which_trigger_raw=which_trigger.value),
        )

    def set_attribute_vi_boolean(self, channel_list, attribute_id, value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViBoolean,
            grpc_types.SetAttributeViBooleanRequest(vi=self._vi, channel_list=channel_list, attribute_id=attribute_id, value=value),
        )

    def set_attribute_vi_int32(self, channel_list, attribute_id, value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViInt32,
            grpc_types.SetAttributeViInt32Request(vi=self._vi, channel_list=channel_list, attribute_id=attribute_id, value_raw=value),
        )

    def set_attribute_vi_int64(self, channel_list, attribute_id, value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViInt64,
            grpc_types.SetAttributeViInt64Request(vi=self._vi, channel_list=channel_list, attribute_id=attribute_id, value_raw=value),
        )

    def set_attribute_vi_real64(self, channel_list, attribute_id, value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViReal64,
            grpc_types.SetAttributeViReal64Request(vi=self._vi, channel_list=channel_list, attribute_id=attribute_id, value_raw=value),
        )

    def set_attribute_vi_string(self, channel_list, attribute_id, value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViString,
            grpc_types.SetAttributeViStringRequest(vi=self._vi, channel_list=channel_list, attribute_id=attribute_id, value_raw=value),
        )

    def set_runtime_environment(self, environment, environment_version, reserved1, reserved2):  # noqa: N802
        raise NotImplementedError('set_runtime_environment is not supported over gRPC')

    def unlock(self):  # noqa: N802
        self._lock.release()

    def close(self):  # noqa: N802
        self._invoke(
            self._client.Close,
            grpc_types.CloseRequest(vi=self._vi),
        )

    def error_message(self, error_code):  # noqa: N802
        response = self._invoke(
            self._client.GetErrorMessage,
            grpc_types.GetErrorMessageRequest(vi=self._vi, error_code=error_code),
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
