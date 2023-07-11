# -*- coding: utf-8 -*-
# This file was generated

import array
import ctypes
import hightime  # noqa: F401
import platform

import niswitch._library_singleton as _library_singleton
import niswitch._visatype as _visatype
import niswitch.enums as enums  # noqa: F401
import niswitch.errors as errors


_was_runtime_environment_set = None


# Helper functions for creating ctypes needed for calling into the driver DLL
def _get_ctypes_pointer_for_buffer(value=None, library_type=None, size=None):
    if isinstance(value, array.array):
        assert library_type is not None, 'library_type is required for array.array'
        addr, _ = value.buffer_info()
        return ctypes.cast(addr, ctypes.POINTER(library_type))
    elif str(type(value)).find("'numpy.ndarray'") != -1:
        import numpy
        return numpy.ctypeslib.as_ctypes(value)
    elif isinstance(value, bytes):
        return ctypes.cast(value, ctypes.POINTER(library_type))
    elif isinstance(value, list):
        assert library_type is not None, 'library_type is required for list'
        return (library_type * len(value))(*value)
    else:
        if library_type is not None and size is not None:
            return (library_type * size)()
        else:
            return None


def _convert_to_array(value, array_type):
    if value is not None:
        if isinstance(value, array.array):
            value_array = value
        else:
            value_array = array.array(array_type, value)
    else:
        value_array = None

    return value_array


class LibraryInterpreter(object):
    '''Library C<->Python interpreter.

    This class is responsible for interpreting the Library's C API. It is responsible for:
    * Converting ctypes to native Python types.
    * Dealing with string encoding.
    * Allocating memory.
    * Converting errors returned by Library into Python exceptions.
    '''

    def __init__(self, encoding):
        self._encoding = encoding
        self._library = _library_singleton.get()
        global _was_runtime_environment_set
        if _was_runtime_environment_set is None:
            try:
                runtime_env = platform.python_implementation()
                version = platform.python_version()
                self.set_runtime_environment(
                    runtime_env,
                    version,
                    '',
                    ''
                )
            except errors.DriverTooOldError:
                pass
            finally:
                _was_runtime_environment_set = True
        # Initialize _vi to 0 for now.
        # Session will directly update it once the driver runtime init function has been called and
        # we have a valid session handle.
        self.set_session_handle()

    def set_session_handle(self, value=0):
        self._vi = value

    def get_session_handle(self):
        return self._vi

    def get_error_description(self, error_code):
        '''get_error_description

        Returns the error description.
        '''
        try:
            returned_error_code, error_string = self.get_error()
            if returned_error_code == error_code:
                return error_string
        except errors.Error:
            pass

        try:
            '''
            It is expected for get_error to raise when the session is invalid
            (IVI spec requires GetError to fail).
            Use error_message instead. It doesn't require a session.
            '''
            error_string = self.error_message(error_code)
            return error_string
        except errors.Error:
            pass
        return "Failed to retrieve error description."

    def abort(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niSwitch_AbortScan(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def can_connect(self, channel1, channel2):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel1_ctype = ctypes.create_string_buffer(channel1.encode(self._encoding))  # case C020
        channel2_ctype = ctypes.create_string_buffer(channel2.encode(self._encoding))  # case C020
        path_capability_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niSwitch_CanConnect(vi_ctype, channel1_ctype, channel2_ctype, None if path_capability_ctype is None else (ctypes.pointer(path_capability_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return enums.PathCapability(path_capability_ctype.value)

    def commit(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niSwitch_Commit(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def connect(self, channel1, channel2):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel1_ctype = ctypes.create_string_buffer(channel1.encode(self._encoding))  # case C020
        channel2_ctype = ctypes.create_string_buffer(channel2.encode(self._encoding))  # case C020
        error_code = self._library.niSwitch_Connect(vi_ctype, channel1_ctype, channel2_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def connect_multiple(self, connection_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        connection_list_ctype = ctypes.create_string_buffer(connection_list.encode(self._encoding))  # case C020
        error_code = self._library.niSwitch_ConnectMultiple(vi_ctype, connection_list_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disable(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niSwitch_Disable(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disconnect(self, channel1, channel2):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel1_ctype = ctypes.create_string_buffer(channel1.encode(self._encoding))  # case C020
        channel2_ctype = ctypes.create_string_buffer(channel2.encode(self._encoding))  # case C020
        error_code = self._library.niSwitch_Disconnect(vi_ctype, channel1_ctype, channel2_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disconnect_all(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niSwitch_DisconnectAll(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disconnect_multiple(self, disconnection_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        disconnection_list_ctype = ctypes.create_string_buffer(disconnection_list.encode(self._encoding))  # case C020
        error_code = self._library.niSwitch_DisconnectMultiple(vi_ctype, disconnection_list_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def get_attribute_vi_boolean(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niSwitch_GetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(attribute_value_ctype.value)

    def get_attribute_vi_int32(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niSwitch_GetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(attribute_value_ctype.value)

    def get_attribute_vi_real64(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niSwitch_GetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(attribute_value_ctype.value)

    def get_attribute_vi_string(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        array_size_ctype = _visatype.ViInt32()  # case S170
        attribute_value_ctype = None  # case C050
        error_code = self._library.niSwitch_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, array_size_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        array_size_ctype = _visatype.ViInt32(error_code)  # case S180
        attribute_value_ctype = (_visatype.ViChar * array_size_ctype.value)()  # case C060
        error_code = self._library.niSwitch_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, array_size_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return attribute_value_ctype.value.decode(self._encoding)

    def get_channel_name(self, index):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        index_ctype = _visatype.ViInt32(index)  # case S150
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        channel_name_buffer_ctype = None  # case C050
        error_code = self._library.niSwitch_GetChannelName(vi_ctype, index_ctype, buffer_size_ctype, channel_name_buffer_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        channel_name_buffer_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niSwitch_GetChannelName(vi_ctype, index_ctype, buffer_size_ctype, channel_name_buffer_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return channel_name_buffer_ctype.value.decode(self._encoding)

    def get_error(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code_ctype = _visatype.ViStatus()  # case S220
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        description_ctype = None  # case C050
        error_code = self._library.niSwitch_GetError(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), buffer_size_ctype, description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=True)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        description_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niSwitch_GetError(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), buffer_size_ctype, description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return int(error_code_ctype.value), description_ctype.value.decode(self._encoding)

    def get_path(self, channel1, channel2):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel1_ctype = ctypes.create_string_buffer(channel1.encode(self._encoding))  # case C020
        channel2_ctype = ctypes.create_string_buffer(channel2.encode(self._encoding))  # case C020
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        path_ctype = None  # case C050
        error_code = self._library.niSwitch_GetPath(vi_ctype, channel1_ctype, channel2_ctype, buffer_size_ctype, path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        path_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niSwitch_GetPath(vi_ctype, channel1_ctype, channel2_ctype, buffer_size_ctype, path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return path_ctype.value.decode(self._encoding)

    def get_relay_count(self, relay_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        relay_name_ctype = ctypes.create_string_buffer(relay_name.encode(self._encoding))  # case C020
        relay_count_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niSwitch_GetRelayCount(vi_ctype, relay_name_ctype, None if relay_count_ctype is None else (ctypes.pointer(relay_count_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(relay_count_ctype.value)

    def get_relay_name(self, index):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        index_ctype = _visatype.ViInt32(index)  # case S150
        relay_name_buffer_size_ctype = _visatype.ViInt32()  # case S170
        relay_name_buffer_ctype = None  # case C050
        error_code = self._library.niSwitch_GetRelayName(vi_ctype, index_ctype, relay_name_buffer_size_ctype, relay_name_buffer_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        relay_name_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        relay_name_buffer_ctype = (_visatype.ViChar * relay_name_buffer_size_ctype.value)()  # case C060
        error_code = self._library.niSwitch_GetRelayName(vi_ctype, index_ctype, relay_name_buffer_size_ctype, relay_name_buffer_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return relay_name_buffer_ctype.value.decode(self._encoding)

    def get_relay_position(self, relay_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        relay_name_ctype = ctypes.create_string_buffer(relay_name.encode(self._encoding))  # case C020
        relay_position_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niSwitch_GetRelayPosition(vi_ctype, relay_name_ctype, None if relay_position_ctype is None else (ctypes.pointer(relay_position_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return enums.RelayPosition(relay_position_ctype.value)

    def init_with_topology(self, resource_name, topology, simulate, reset_device):  # noqa: N802
        resource_name_ctype = ctypes.create_string_buffer(resource_name.encode(self._encoding))  # case C020
        topology_ctype = ctypes.create_string_buffer(topology.encode(self._encoding))  # case C020
        simulate_ctype = _visatype.ViBoolean(simulate)  # case S150
        reset_device_ctype = _visatype.ViBoolean(reset_device)  # case S150
        vi_ctype = _visatype.ViSession()  # case S220
        error_code = self._library.niSwitch_InitWithTopology(resource_name_ctype, topology_ctype, simulate_ctype, reset_device_ctype, None if vi_ctype is None else (ctypes.pointer(vi_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        self._close_on_exit = True
        return int(vi_ctype.value)

    def initiate_scan(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niSwitch_InitiateScan(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def lock(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niSwitch_LockSession(vi_ctype, None)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def relay_control(self, relay_name, relay_action):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        relay_name_ctype = ctypes.create_string_buffer(relay_name.encode(self._encoding))  # case C020
        relay_action_ctype = _visatype.ViInt32(relay_action.value)  # case S130
        error_code = self._library.niSwitch_RelayControl(vi_ctype, relay_name_ctype, relay_action_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def reset_with_defaults(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niSwitch_ResetWithDefaults(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def route_scan_advanced_output(self, scan_advanced_output_connector, scan_advanced_output_bus_line, invert):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        scan_advanced_output_connector_ctype = _visatype.ViInt32(scan_advanced_output_connector.value)  # case S130
        scan_advanced_output_bus_line_ctype = _visatype.ViInt32(scan_advanced_output_bus_line.value)  # case S130
        invert_ctype = _visatype.ViBoolean(invert)  # case S150
        error_code = self._library.niSwitch_RouteScanAdvancedOutput(vi_ctype, scan_advanced_output_connector_ctype, scan_advanced_output_bus_line_ctype, invert_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def route_trigger_input(self, trigger_input_connector, trigger_input_bus_line, invert):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        trigger_input_connector_ctype = _visatype.ViInt32(trigger_input_connector.value)  # case S130
        trigger_input_bus_line_ctype = _visatype.ViInt32(trigger_input_bus_line.value)  # case S130
        invert_ctype = _visatype.ViBoolean(invert)  # case S150
        error_code = self._library.niSwitch_RouteTriggerInput(vi_ctype, trigger_input_connector_ctype, trigger_input_bus_line_ctype, invert_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def send_software_trigger(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niSwitch_SendSoftwareTrigger(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_boolean(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViBoolean(attribute_value)  # case S150
        error_code = self._library.niSwitch_SetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_int32(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt32(attribute_value)  # case S150
        error_code = self._library.niSwitch_SetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_real64(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViReal64(attribute_value)  # case S150
        error_code = self._library.niSwitch_SetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_string(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = ctypes.create_string_buffer(attribute_value.encode(self._encoding))  # case C020
        error_code = self._library.niSwitch_SetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_path(self, path_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        path_list_ctype = ctypes.create_string_buffer(path_list.encode(self._encoding))  # case C020
        error_code = self._library.niSwitch_SetPath(vi_ctype, path_list_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_runtime_environment(self, environment, environment_version, reserved1, reserved2):  # noqa: N802
        environment_ctype = ctypes.create_string_buffer(environment.encode(self._encoding))  # case C020
        environment_version_ctype = ctypes.create_string_buffer(environment_version.encode(self._encoding))  # case C020
        reserved1_ctype = ctypes.create_string_buffer(reserved1.encode(self._encoding))  # case C020
        reserved2_ctype = ctypes.create_string_buffer(reserved2.encode(self._encoding))  # case C020
        error_code = self._library.niSwitch_SetRuntimeEnvironment(environment_ctype, environment_version_ctype, reserved1_ctype, reserved2_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def unlock(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niSwitch_UnlockSession(vi_ctype, None)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def wait_for_debounce(self, maximum_time_ms):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        maximum_time_ms_ctype = _visatype.ViInt32(maximum_time_ms)  # case S150
        error_code = self._library.niSwitch_WaitForDebounce(vi_ctype, maximum_time_ms_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def wait_for_scan_complete(self, maximum_time_ms):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        maximum_time_ms_ctype = _visatype.ViInt32(maximum_time_ms)  # case S150
        error_code = self._library.niSwitch_WaitForScanComplete(vi_ctype, maximum_time_ms_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def close(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niSwitch_close(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def error_message(self, error_code):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code_ctype = _visatype.ViStatus(error_code)  # case S150
        error_message_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library.niSwitch_error_message(vi_ctype, error_code_ctype, error_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return error_message_ctype.value.decode(self._encoding)

    def reset(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niSwitch_reset(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def self_test(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        self_test_result_ctype = _visatype.ViInt16()  # case S220
        self_test_message_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library.niSwitch_self_test(vi_ctype, None if self_test_result_ctype is None else (ctypes.pointer(self_test_result_ctype)), self_test_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(self_test_result_ctype.value), self_test_message_ctype.value.decode(self._encoding)
