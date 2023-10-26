# -*- coding: utf-8 -*-
# This file was generated

import grpc
import hightime  # noqa: F401
import threading
import warnings

from . import enums as enums  # noqa: F401
from . import errors as errors
from . import nidcpower_pb2 as grpc_types
from . import nidcpower_pb2_grpc as nidcpower_grpc
from . import session_pb2 as session_grpc_types

from . import lcr_measurement as lcr_measurement  # noqa: F401

from . import lcr_load_compensation_spot as lcr_load_compensation_spot  # noqa: F401


class GrpcStubInterpreter(object):
    '''Interpreter for interacting with a gRPC Stub class'''

    def __init__(self, grpc_options):
        self._grpc_options = grpc_options
        self._lock = threading.RLock()
        self._client = nidcpower_grpc.NiDCPowerStub(grpc_options.grpc_channel)
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

    def abort(self, channel_name):  # noqa: N802
        self._invoke(
            self._client.AbortWithChannels,
            grpc_types.AbortWithChannelsRequest(vi=self._vi, channel_name=channel_name),
        )

    def self_cal(self, channel_name):  # noqa: N802
        self._invoke(
            self._client.CalSelfCalibrate,
            grpc_types.CalSelfCalibrateRequest(vi=self._vi, channel_name=channel_name),
        )

    def clear_latched_output_cutoff_state(self, channel_name, output_cutoff_reason):  # noqa: N802
        self._invoke(
            self._client.ClearLatchedOutputCutoffState,
            grpc_types.ClearLatchedOutputCutoffStateRequest(vi=self._vi, channel_name=channel_name, output_cutoff_reason_raw=output_cutoff_reason.value),
        )

    def commit(self, channel_name):  # noqa: N802
        self._invoke(
            self._client.CommitWithChannels,
            grpc_types.CommitWithChannelsRequest(vi=self._vi, channel_name=channel_name),
        )

    def configure_aperture_time(self, channel_name, aperture_time, units):  # noqa: N802
        self._invoke(
            self._client.ConfigureApertureTime,
            grpc_types.ConfigureApertureTimeRequest(vi=self._vi, channel_name=channel_name, aperture_time=aperture_time, units_raw=units.value),
        )

    def configure_lcr_compensation(self, channel_name, compensation_data):  # noqa: N802
        raise NotImplementedError('configure_lcr_compensation is not supported over gRPC')

    def configure_lcr_custom_cable_compensation(self, channel_name, custom_cable_compensation_data):  # noqa: N802
        self._invoke(
            self._client.ConfigureLCRCustomCableCompensation,
            grpc_types.ConfigureLCRCustomCableCompensationRequest(vi=self._vi, channel_name=channel_name, custom_cable_compensation_data=custom_cable_compensation_data),
        )

    def create_advanced_sequence_commit_step(self, channel_name, set_as_active_step):  # noqa: N802
        self._invoke(
            self._client.CreateAdvancedSequenceCommitStepWithChannels,
            grpc_types.CreateAdvancedSequenceCommitStepWithChannelsRequest(vi=self._vi, channel_name=channel_name, set_as_active_step=set_as_active_step),
        )

    def create_advanced_sequence_step(self, channel_name, set_as_active_step):  # noqa: N802
        self._invoke(
            self._client.CreateAdvancedSequenceStepWithChannels,
            grpc_types.CreateAdvancedSequenceStepWithChannelsRequest(vi=self._vi, channel_name=channel_name, set_as_active_step=set_as_active_step),
        )

    def create_advanced_sequence_with_channels(self, channel_name, sequence_name, attribute_ids, set_as_active_sequence):  # noqa: N802
        self._invoke(
            self._client.CreateAdvancedSequenceWithChannels,
            grpc_types.CreateAdvancedSequenceWithChannelsRequest(vi=self._vi, channel_name=channel_name, sequence_name=sequence_name, attribute_ids=attribute_ids, set_as_active_sequence=set_as_active_sequence),
        )

    def delete_advanced_sequence(self, channel_name, sequence_name):  # noqa: N802
        self._invoke(
            self._client.DeleteAdvancedSequenceWithChannels,
            grpc_types.DeleteAdvancedSequenceWithChannelsRequest(vi=self._vi, channel_name=channel_name, sequence_name=sequence_name),
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

    def fancy_initialize(self, resource_name, channels, reset, option_string, independent_channels):  # noqa: N802
        response = self._invoke(
            self._client.FancyInitialize,
            grpc_types.FancyInitializeRequest(resource_name=resource_name, channels=channels, reset=reset, option_string=option_string, independent_channels=independent_channels),
        )
        return response.vi

    def fetch_multiple(self, channel_name, timeout, count):  # noqa: N802
        response = self._invoke(
            self._client.FetchMultiple,
            grpc_types.FetchMultipleRequest(vi=self._vi, channel_name=channel_name, timeout=timeout, count=count),
        )
        return response.voltage_measurements, response.current_measurements, response.in_compliance

    def fetch_multiple_lcr(self, channel_name, timeout, count):  # noqa: N802
        response = self._invoke(
            self._client.FetchMultipleLCR,
            grpc_types.FetchMultipleLCRRequest(vi=self._vi, channel_name=channel_name, timeout=timeout, count=count),
        )
        return [lcr_measurement.LCRMeasurement(x) for x in response.measurements]

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

    def get_attribute_vi_int64(self, channel_name, attribute_id):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViInt64,
            grpc_types.GetAttributeViInt64Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id),
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
        return response.channel_name

    def get_channel_names(self, indices):  # noqa: N802
        response = self._invoke(
            self._client.GetChannelNameFromString,
            grpc_types.GetChannelNameFromStringRequest(vi=self._vi, index=indices),
        )
        return response.channel_name

    def get_error(self):  # noqa: N802
        response = self._invoke(
            self._client.GetError,
            grpc_types.GetErrorRequest(vi=self._vi),
        )
        return response.code, response.description

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

    def get_lcr_compensation_data(self, channel_name):  # noqa: N802
        raise NotImplementedError('get_lcr_compensation_data is not supported over gRPC')

    def get_lcr_compensation_last_date_and_time(self, channel_name, compensation_type):  # noqa: N802
        response = self._invoke(
            self._client.GetLCRCompensationLastDateAndTime,
            grpc_types.GetLCRCompensationLastDateAndTimeRequest(vi=self._vi, channel_name=channel_name, compensation_type_raw=compensation_type.value),
        )
        return response.year, response.month, response.day, response.hour, response.minute

    def get_lcr_custom_cable_compensation_data(self, channel_name):  # noqa: N802
        response = self._invoke(
            self._client.GetLCRCustomCableCompensationData,
            grpc_types.GetLCRCustomCableCompensationDataRequest(vi=self._vi, channel_name=channel_name),
        )
        return response.custom_cable_compensation_data

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

    def initialize_with_channels(self, resource_name, channels, reset, option_string):  # noqa: N802
        metadata = (
            ('ni-api-key', self._grpc_options.api_key),
        )
        response = self._invoke(
            self._client.InitializeWithChannels,
            grpc_types.InitializeWithChannelsRequest(resource_name=resource_name, channels=channels, reset=reset, option_string=option_string, session_name=self._grpc_options.session_name, initialization_behavior=self._grpc_options.initialization_behavior),
            metadata=metadata,
        )
        self._close_on_exit = response.new_session_initialized
        return response.vi

    def initialize_with_independent_channels(self, resource_name, reset, option_string):  # noqa: N802
        metadata = (
            ('ni-api-key', self._grpc_options.api_key),
        )
        response = self._invoke(
            self._client.InitializeWithIndependentChannels,
            grpc_types.InitializeWithIndependentChannelsRequest(resource_name=resource_name, reset=reset, option_string=option_string, session_name=self._grpc_options.session_name, initialization_behavior=self._grpc_options.initialization_behavior),
            metadata=metadata,
        )
        self._close_on_exit = response.new_session_initialized
        return response.vi

    def initiate_with_channels(self, channel_name):  # noqa: N802
        self._invoke(
            self._client.InitiateWithChannels,
            grpc_types.InitiateWithChannelsRequest(vi=self._vi, channel_name=channel_name),
        )

    def lock(self):  # noqa: N802
        self._lock.acquire()

    def measure(self, channel_name, measurement_type):  # noqa: N802
        response = self._invoke(
            self._client.Measure,
            grpc_types.MeasureRequest(vi=self._vi, channel_name=channel_name, measurement_type_raw=measurement_type.value),
        )
        return response.measurement

    def measure_multiple(self, channel_name):  # noqa: N802
        response = self._invoke(
            self._client.MeasureMultiple,
            grpc_types.MeasureMultipleRequest(vi=self._vi, channel_name=channel_name),
        )
        return response.voltage_measurements, response.current_measurements

    def measure_multiple_lcr(self, channel_name):  # noqa: N802
        response = self._invoke(
            self._client.MeasureMultipleLCR,
            grpc_types.MeasureMultipleLCRRequest(vi=self._vi, channel_name=channel_name),
        )
        return [lcr_measurement.LCRMeasurement(x) for x in response.measurements]

    def parse_channel_count(self, channels_string):  # noqa: N802
        raise NotImplementedError('parse_channel_count is not supported over gRPC')

    def perform_lcr_load_compensation(self, channel_name, compensation_spots):  # noqa: N802
        self._invoke(
            self._client.PerformLCRLoadCompensation,
            grpc_types.PerformLCRLoadCompensationRequest(vi=self._vi, channel_name=channel_name, compensation_spots=compensation_spots and [x._create_copy(grpc_types.NILCRLoadCompensationSpot) for x in compensation_spots]),
        )

    def perform_lcr_open_compensation(self, channel_name, additional_frequencies):  # noqa: N802
        self._invoke(
            self._client.PerformLCROpenCompensation,
            grpc_types.PerformLCROpenCompensationRequest(vi=self._vi, channel_name=channel_name, additional_frequencies=additional_frequencies),
        )

    def perform_lcr_open_custom_cable_compensation(self, channel_name):  # noqa: N802
        self._invoke(
            self._client.PerformLCROpenCustomCableCompensation,
            grpc_types.PerformLCROpenCustomCableCompensationRequest(vi=self._vi, channel_name=channel_name),
        )

    def perform_lcr_short_compensation(self, channel_name, additional_frequencies):  # noqa: N802
        self._invoke(
            self._client.PerformLCRShortCompensation,
            grpc_types.PerformLCRShortCompensationRequest(vi=self._vi, channel_name=channel_name, additional_frequencies=additional_frequencies),
        )

    def perform_lcr_short_custom_cable_compensation(self, channel_name):  # noqa: N802
        self._invoke(
            self._client.PerformLCRShortCustomCableCompensation,
            grpc_types.PerformLCRShortCustomCableCompensationRequest(vi=self._vi, channel_name=channel_name),
        )

    def query_in_compliance(self, channel_name):  # noqa: N802
        response = self._invoke(
            self._client.QueryInCompliance,
            grpc_types.QueryInComplianceRequest(vi=self._vi, channel_name=channel_name),
        )
        return response.in_compliance

    def query_latched_output_cutoff_state(self, channel_name, output_cutoff_reason):  # noqa: N802
        response = self._invoke(
            self._client.QueryLatchedOutputCutoffState,
            grpc_types.QueryLatchedOutputCutoffStateRequest(vi=self._vi, channel_name=channel_name, output_cutoff_reason_raw=output_cutoff_reason.value),
        )
        return response.output_cutoff_state

    def query_max_current_limit(self, channel_name, voltage_level):  # noqa: N802
        response = self._invoke(
            self._client.QueryMaxCurrentLimit,
            grpc_types.QueryMaxCurrentLimitRequest(vi=self._vi, channel_name=channel_name, voltage_level=voltage_level),
        )
        return response.max_current_limit

    def query_max_voltage_level(self, channel_name, current_limit):  # noqa: N802
        response = self._invoke(
            self._client.QueryMaxVoltageLevel,
            grpc_types.QueryMaxVoltageLevelRequest(vi=self._vi, channel_name=channel_name, current_limit=current_limit),
        )
        return response.max_voltage_level

    def query_min_current_limit(self, channel_name, voltage_level):  # noqa: N802
        response = self._invoke(
            self._client.QueryMinCurrentLimit,
            grpc_types.QueryMinCurrentLimitRequest(vi=self._vi, channel_name=channel_name, voltage_level=voltage_level),
        )
        return response.min_current_limit

    def query_output_state(self, channel_name, output_state):  # noqa: N802
        response = self._invoke(
            self._client.QueryOutputState,
            grpc_types.QueryOutputStateRequest(vi=self._vi, channel_name=channel_name, output_state_raw=output_state.value),
        )
        return response.in_state

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

    def reset(self, channel_name):  # noqa: N802
        self._invoke(
            self._client.ResetWithChannels,
            grpc_types.ResetWithChannelsRequest(vi=self._vi, channel_name=channel_name),
        )

    def reset_with_defaults(self):  # noqa: N802
        self._invoke(
            self._client.ResetWithDefaults,
            grpc_types.ResetWithDefaultsRequest(vi=self._vi),
        )

    def send_software_edge_trigger(self, channel_name, trigger):  # noqa: N802
        self._invoke(
            self._client.SendSoftwareEdgeTriggerWithChannels,
            grpc_types.SendSoftwareEdgeTriggerWithChannelsRequest(vi=self._vi, channel_name=channel_name, trigger_raw=trigger.value),
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

    def set_attribute_vi_int64(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViInt64,
            grpc_types.SetAttributeViInt64Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id, attribute_value_raw=attribute_value),
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

    def set_sequence(self, channel_name, values, source_delays):  # noqa: N802
        self._invoke(
            self._client.SetSequence,
            grpc_types.SetSequenceRequest(vi=self._vi, channel_name=channel_name, values=values, source_delays=source_delays),
        )

    def unlock(self):  # noqa: N802
        self._lock.release()

    def wait_for_event(self, channel_name, event_id, timeout):  # noqa: N802
        self._invoke(
            self._client.WaitForEventWithChannels,
            grpc_types.WaitForEventWithChannelsRequest(vi=self._vi, channel_name=channel_name, event_id_raw=event_id.value, timeout=timeout),
        )

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

    def self_test(self):  # noqa: N802
        response = self._invoke(
            self._client.SelfTest,
            grpc_types.SelfTestRequest(vi=self._vi),
        )
        return response.self_test_result, response.self_test_message
