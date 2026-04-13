# -*- coding: utf-8 -*-
# This file was generated

import grpc
import hightime  # noqa: F401
import threading
import warnings

from . import enums as enums  # noqa: F401
from . import errors as errors
from . import nidmm_pb2 as grpc_types
from . import nidmm_pb2_grpc as nidmm_grpc
from . import session_pb2 as session_grpc_types


class GrpcStubInterpreter(object):
    '''Interpreter for interacting with a gRPC Stub class'''

    def __init__(self, grpc_options):
        self._grpc_options = grpc_options
        self._lock = threading.RLock()
        self._client = nidmm_grpc.NiDmmStub(grpc_options.grpc_channel)
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

    def configure_measurement_absolute(self, measurement_function, range, resolution_absolute):  # noqa: N802
        self._invoke(
            self._client.ConfigureMeasurementAbsolute,
            grpc_types.ConfigureMeasurementAbsoluteRequest(vi=self._vi, measurement_function_raw=measurement_function.value, range=range, resolution_absolute=resolution_absolute),
        )

    def configure_measurement_digits(self, measurement_function, range, resolution_digits):  # noqa: N802
        self._invoke(
            self._client.ConfigureMeasurementDigits,
            grpc_types.ConfigureMeasurementDigitsRequest(vi=self._vi, measurement_function_raw=measurement_function.value, range=range, resolution_digits=resolution_digits),
        )

    def configure_multi_point(self, trigger_count, sample_count, sample_trigger, sample_interval):  # noqa: N802
        self._invoke(
            self._client.ConfigureMultiPoint,
            grpc_types.ConfigureMultiPointRequest(vi=self._vi, trigger_count_raw=trigger_count, sample_count_raw=sample_count, sample_trigger_raw=sample_trigger.value, sample_interval_raw=sample_interval),
        )

    def configure_rtd_custom(self, rtd_a, rtd_b, rtd_c):  # noqa: N802
        self._invoke(
            self._client.ConfigureRTDCustom,
            grpc_types.ConfigureRTDCustomRequest(vi=self._vi, rtd_a=rtd_a, rtd_b=rtd_b, rtd_c=rtd_c),
        )

    def configure_rtd_type(self, rtd_type, rtd_resistance):  # noqa: N802
        self._invoke(
            self._client.ConfigureRTDType,
            grpc_types.ConfigureRTDTypeRequest(vi=self._vi, rtd_type_raw=rtd_type.value, rtd_resistance=rtd_resistance),
        )

    def configure_thermistor_custom(self, thermistor_a, thermistor_b, thermistor_c):  # noqa: N802
        self._invoke(
            self._client.ConfigureThermistorCustom,
            grpc_types.ConfigureThermistorCustomRequest(vi=self._vi, thermistor_a=thermistor_a, thermistor_b=thermistor_b, thermistor_c=thermistor_c),
        )

    def configure_thermocouple(self, thermocouple_type, reference_junction_type):  # noqa: N802
        self._invoke(
            self._client.ConfigureThermocouple,
            grpc_types.ConfigureThermocoupleRequest(vi=self._vi, thermocouple_type_raw=thermocouple_type.value, reference_junction_type_raw=reference_junction_type.value),
        )

    def configure_trigger(self, trigger_source, trigger_delay):  # noqa: N802
        self._invoke(
            self._client.ConfigureTrigger,
            grpc_types.ConfigureTriggerRequest(vi=self._vi, trigger_source_raw=trigger_source.value, trigger_delay_raw=trigger_delay),
        )

    def configure_waveform_acquisition(self, measurement_function, range, rate, waveform_points):  # noqa: N802
        self._invoke(
            self._client.ConfigureWaveformAcquisition,
            grpc_types.ConfigureWaveformAcquisitionRequest(vi=self._vi, measurement_function_raw=measurement_function.value, range=range, rate=rate, waveform_points=waveform_points),
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

    def fetch(self, maximum_time):  # noqa: N802
        response = self._invoke(
            self._client.Fetch,
            grpc_types.FetchRequest(vi=self._vi, maximum_time_raw=maximum_time),
        )
        return response.reading

    def fetch_multi_point(self, maximum_time, array_size):  # noqa: N802
        response = self._invoke(
            self._client.FetchMultiPoint,
            grpc_types.FetchMultiPointRequest(vi=self._vi, maximum_time_raw=maximum_time, array_size=array_size),
        )
        return response.reading_array

    def fetch_waveform(self, maximum_time, array_size):  # noqa: N802
        response = self._invoke(
            self._client.FetchWaveform,
            grpc_types.FetchWaveformRequest(vi=self._vi, maximum_time_raw=maximum_time, array_size=array_size),
        )
        return response.waveform_array

    def fetch_waveform_into(self, maximum_time, array_size):  # noqa: N802
        raise NotImplementedError('numpy-specific methods are not supported over gRPC')

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

    def get_cal_date_and_time(self, cal_type):  # noqa: N802
        response = self._invoke(
            self._client.GetCalDateAndTime,
            grpc_types.GetCalDateAndTimeRequest(vi=self._vi, cal_type=cal_type),
        )
        return response.month, response.day, response.year, response.hour, response.minute

    def get_dev_temp(self, options):  # noqa: N802
        response = self._invoke(
            self._client.GetDevTemp,
            grpc_types.GetDevTempRequest(vi=self._vi, options=options),
        )
        return response.temperature

    def get_error(self):  # noqa: N802
        response = self._invoke(
            self._client.GetError,
            grpc_types.GetErrorRequest(vi=self._vi),
        )
        return response.error_code, response.description

    def get_ext_cal_recommended_interval(self):  # noqa: N802
        response = self._invoke(
            self._client.GetExtCalRecommendedInterval,
            grpc_types.GetExtCalRecommendedIntervalRequest(vi=self._vi),
        )
        return response.months

    def get_last_cal_temp(self, cal_type):  # noqa: N802
        response = self._invoke(
            self._client.GetLastCalTemp,
            grpc_types.GetLastCalTempRequest(vi=self._vi, cal_type=cal_type),
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

    def lock(self):  # noqa: N802
        self._lock.acquire()

    def perform_open_cable_comp(self):  # noqa: N802
        response = self._invoke(
            self._client.PerformOpenCableComp,
            grpc_types.PerformOpenCableCompRequest(vi=self._vi),
        )
        return response.conductance, response.susceptance

    def perform_short_cable_comp(self):  # noqa: N802
        response = self._invoke(
            self._client.PerformShortCableComp,
            grpc_types.PerformShortCableCompRequest(vi=self._vi),
        )
        return response.resistance, response.reactance

    def read(self, maximum_time):  # noqa: N802
        response = self._invoke(
            self._client.Read,
            grpc_types.ReadRequest(vi=self._vi, maximum_time_raw=maximum_time),
        )
        return response.reading

    def read_multi_point(self, maximum_time, array_size):  # noqa: N802
        response = self._invoke(
            self._client.ReadMultiPoint,
            grpc_types.ReadMultiPointRequest(vi=self._vi, maximum_time_raw=maximum_time, array_size=array_size),
        )
        return response.reading_array

    def read_status(self):  # noqa: N802
        response = self._invoke(
            self._client.ReadStatus,
            grpc_types.ReadStatusRequest(vi=self._vi),
        )
        return response.acquisition_backlog, enums.AcquisitionStatus(response.acquisition_status_raw)

    def read_waveform(self, maximum_time, array_size):  # noqa: N802
        response = self._invoke(
            self._client.ReadWaveform,
            grpc_types.ReadWaveformRequest(vi=self._vi, maximum_time_raw=maximum_time, array_size=array_size),
        )
        return response.waveform_array

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

    def send_software_trigger(self):  # noqa: N802
        self._invoke(
            self._client.SendSoftwareTrigger,
            grpc_types.SendSoftwareTriggerRequest(vi=self._vi),
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
