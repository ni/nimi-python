# -*- coding: utf-8 -*-
# This file was generated

import grpc
import hightime  # noqa: F401
import threading
import warnings

from . import enums as enums  # noqa: F401
from . import errors as errors
from . import niswitch_pb2 as grpc_types
from . import niswitch_pb2_grpc as niswitch_grpc
from . import session_pb2 as session_grpc_types


class GrpcStubInterpreter(object):
    '''Interpreter for interacting with a gRPC Stub class'''

    def __init__(self, grpc_options):
        self._grpc_options = grpc_options
        self._lock = threading.RLock()
        self._client = niswitch_grpc.NiSwitchStub(grpc_options.grpc_channel)
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
            self._client.AbortScan,
            grpc_types.AbortScanRequest(vi=self._vi),
        )

    def can_connect(self, channel1, channel2):  # noqa: N802
        response = self._invoke(
            self._client.CanConnect,
            grpc_types.CanConnectRequest(vi=self._vi, channel1=channel1, channel2=channel2),
        )
        return enums.PathCapability(response.path_capability_raw)

    def commit(self):  # noqa: N802
        self._invoke(
            self._client.Commit,
            grpc_types.CommitRequest(vi=self._vi),
        )

    def connect(self, channel1, channel2):  # noqa: N802
        self._invoke(
            self._client.Connect,
            grpc_types.ConnectRequest(vi=self._vi, channel1=channel1, channel2=channel2),
        )

    def connect_multiple(self, connection_list):  # noqa: N802
        self._invoke(
            self._client.ConnectMultiple,
            grpc_types.ConnectMultipleRequest(vi=self._vi, connection_list=connection_list),
        )

    def disable(self):  # noqa: N802
        self._invoke(
            self._client.Disable,
            grpc_types.DisableRequest(vi=self._vi),
        )

    def disconnect(self, channel1, channel2):  # noqa: N802
        self._invoke(
            self._client.Disconnect,
            grpc_types.DisconnectRequest(vi=self._vi, channel1=channel1, channel2=channel2),
        )

    def disconnect_all(self):  # noqa: N802
        self._invoke(
            self._client.DisconnectAll,
            grpc_types.DisconnectAllRequest(vi=self._vi),
        )

    def disconnect_multiple(self, disconnection_list):  # noqa: N802
        self._invoke(
            self._client.DisconnectMultiple,
            grpc_types.DisconnectMultipleRequest(vi=self._vi, disconnection_list=disconnection_list),
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
        return response.channel_name_buffer

    def get_error(self):  # noqa: N802
        response = self._invoke(
            self._client.GetError,
            grpc_types.GetErrorRequest(vi=self._vi),
        )
        return response.code, response.description

    def get_path(self, channel1, channel2):  # noqa: N802
        response = self._invoke(
            self._client.GetPath,
            grpc_types.GetPathRequest(vi=self._vi, channel1=channel1, channel2=channel2),
        )
        return response.path

    def get_relay_count(self, relay_name):  # noqa: N802
        response = self._invoke(
            self._client.GetRelayCount,
            grpc_types.GetRelayCountRequest(vi=self._vi, relay_name=relay_name),
        )
        return response.relay_count

    def get_relay_name(self, index):  # noqa: N802
        response = self._invoke(
            self._client.GetRelayName,
            grpc_types.GetRelayNameRequest(vi=self._vi, index=index),
        )
        return response.relay_name_buffer

    def get_relay_position(self, relay_name):  # noqa: N802
        response = self._invoke(
            self._client.GetRelayPosition,
            grpc_types.GetRelayPositionRequest(vi=self._vi, relay_name=relay_name),
        )
        return enums.RelayPosition(response.relay_position_raw)

    def init_with_topology(self, resource_name, topology, simulate, reset_device):  # noqa: N802
        metadata = (
            ('ni-api-key', self._grpc_options.api_key),
        )
        response = self._invoke(
            self._client.InitWithTopology,
            grpc_types.InitWithTopologyRequest(resource_name=resource_name, topology=topology, simulate=simulate, reset_device=reset_device, session_name=self._grpc_options.session_name, initialization_behavior=self._grpc_options.initialization_behavior),
            metadata=metadata,
        )
        self._close_on_exit = response.new_session_initialized
        return response.vi

    def initiate_scan(self):  # noqa: N802
        self._invoke(
            self._client.InitiateScan,
            grpc_types.InitiateScanRequest(vi=self._vi),
        )

    def lock(self):  # noqa: N802
        self._lock.acquire()

    def relay_control(self, relay_name, relay_action):  # noqa: N802
        self._invoke(
            self._client.RelayControl,
            grpc_types.RelayControlRequest(vi=self._vi, relay_name=relay_name, relay_action_raw=relay_action.value),
        )

    def reset_with_defaults(self):  # noqa: N802
        self._invoke(
            self._client.ResetWithDefaults,
            grpc_types.ResetWithDefaultsRequest(vi=self._vi),
        )

    def route_scan_advanced_output(self, scan_advanced_output_connector, scan_advanced_output_bus_line, invert):  # noqa: N802
        self._invoke(
            self._client.RouteScanAdvancedOutput,
            grpc_types.RouteScanAdvancedOutputRequest(vi=self._vi, scan_advanced_output_connector_raw=scan_advanced_output_connector.value, scan_advanced_output_bus_line_raw=scan_advanced_output_bus_line.value, invert=invert),
        )

    def route_trigger_input(self, trigger_input_connector, trigger_input_bus_line, invert):  # noqa: N802
        self._invoke(
            self._client.RouteTriggerInput,
            grpc_types.RouteTriggerInputRequest(vi=self._vi, trigger_input_connector_raw=trigger_input_connector.value, trigger_input_bus_line_raw=trigger_input_bus_line.value, invert=invert),
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

    def set_path(self, path_list):  # noqa: N802
        self._invoke(
            self._client.SetPath,
            grpc_types.SetPathRequest(vi=self._vi, path_list=path_list),
        )

    def set_runtime_environment(self, environment, environment_version, reserved1, reserved2):  # noqa: N802
        raise NotImplementedError('set_runtime_environment is not supported over gRPC')

    def unlock(self):  # noqa: N802
        self._lock.release()

    def wait_for_debounce(self, maximum_time_ms):  # noqa: N802
        self._invoke(
            self._client.WaitForDebounce,
            grpc_types.WaitForDebounceRequest(vi=self._vi, maximum_time_ms=maximum_time_ms),
        )

    def wait_for_scan_complete(self, maximum_time_ms):  # noqa: N802
        self._invoke(
            self._client.WaitForScanComplete,
            grpc_types.WaitForScanCompleteRequest(vi=self._vi, maximum_time_ms=maximum_time_ms),
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
