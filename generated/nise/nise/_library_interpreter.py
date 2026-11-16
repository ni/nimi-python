# -*- coding: utf-8 -*-
# This file was generated

import array
import ctypes
import hightime  # noqa: F401
import nise._library_singleton as _library_singleton
import nise._visatype as _visatype
import nise.enums as enums  # noqa: F401
import nise.errors as errors


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
            returned_error_code, error_string = self.get_error([1024])
            if returned_error_code == error_code:
                return error_string
        except errors.Error:
            pass
        return "Failed to retrieve error description."

    def close_session(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niSE_CloseSession(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def connect(self, connect_spec, multiconnect_mode, wait_for_debounce):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        connect_spec_ctype = ctypes.create_string_buffer(connect_spec.encode(self._encoding))  # case C020
        multiconnect_mode_ctype = _visatype.ViInt32(multiconnect_mode.value)  # case S130
        wait_for_debounce_ctype = _visatype.ViBoolean(wait_for_debounce)  # case S150
        error_code = self._library.niSE_Connect(vi_ctype, connect_spec_ctype, multiconnect_mode_ctype, wait_for_debounce_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def connect_and_disconnect(self, connect_spec, disconnect_spec, multiconnect_mode, operation_order, wait_for_debounce):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        connect_spec_ctype = ctypes.create_string_buffer(connect_spec.encode(self._encoding))  # case C020
        disconnect_spec_ctype = ctypes.create_string_buffer(disconnect_spec.encode(self._encoding))  # case C020
        multiconnect_mode_ctype = _visatype.ViInt32(multiconnect_mode.value)  # case S130
        operation_order_ctype = _visatype.ViInt32(operation_order.value)  # case S130
        wait_for_debounce_ctype = _visatype.ViBoolean(wait_for_debounce)  # case S150
        error_code = self._library.niSE_ConnectAndDisconnect(vi_ctype, connect_spec_ctype, disconnect_spec_ctype, multiconnect_mode_ctype, operation_order_ctype, wait_for_debounce_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disconnect(self, disconnect_spec):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        disconnect_spec_ctype = ctypes.create_string_buffer(disconnect_spec.encode(self._encoding))  # case C020
        error_code = self._library.niSE_Disconnect(vi_ctype, disconnect_spec_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disconnect_all(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niSE_DisconnectAll(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def expand_route_spec(self, route_spec, expand_action, expanded_route_spec_size):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        route_spec_ctype = ctypes.create_string_buffer(route_spec.encode(self._encoding))  # case C020
        expand_action_ctype = _visatype.ViInt32(expand_action.value)  # case S130
        expanded_route_spec_ctype = (_visatype.ViChar * expanded_route_spec_size[0])()  # case C080
        expanded_route_spec_size_ctype = _get_ctypes_pointer_for_buffer(value=expanded_route_spec_size, library_type=_visatype.ViInt32)  # case B550
        error_code = self._library.niSE_ExpandRouteSpec(vi_ctype, route_spec_ctype, expand_action_ctype, expanded_route_spec_ctype, expanded_route_spec_size_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return expanded_route_spec_ctype.value.decode(self._encoding)

    def find_route(self, channel1, channel2, route_spec_size):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel1_ctype = ctypes.create_string_buffer(channel1.encode(self._encoding))  # case C020
        channel2_ctype = ctypes.create_string_buffer(channel2.encode(self._encoding))  # case C020
        route_spec_ctype = (_visatype.ViChar * route_spec_size[0])()  # case C080
        route_spec_size_ctype = _get_ctypes_pointer_for_buffer(value=route_spec_size, library_type=_visatype.ViInt32)  # case B550
        path_capability_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niSE_FindRoute(vi_ctype, channel1_ctype, channel2_ctype, route_spec_ctype, route_spec_size_ctype, None if path_capability_ctype is None else (ctypes.pointer(path_capability_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return route_spec_ctype.value.decode(self._encoding), enums.PathCapability(path_capability_ctype.value)

    def get_all_connections(self, route_spec_size):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        route_spec_ctype = (_visatype.ViChar * route_spec_size[0])()  # case C080
        route_spec_size_ctype = _get_ctypes_pointer_for_buffer(value=route_spec_size, library_type=_visatype.ViInt32)  # case B550
        error_code = self._library.niSE_GetAllConnections(vi_ctype, route_spec_ctype, route_spec_size_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return route_spec_ctype.value.decode(self._encoding)

    def get_error(self, error_description_size):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_number_ctype = _visatype.ViInt32()  # case S220
        error_description_ctype = (_visatype.ViChar * error_description_size[0])()  # case C080
        error_description_size_ctype = _get_ctypes_pointer_for_buffer(value=error_description_size, library_type=_visatype.ViInt32)  # case B550
        error_code = self._library.niSE_GetError(vi_ctype, None if error_number_ctype is None else (ctypes.pointer(error_number_ctype)), error_description_ctype, error_description_size_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return int(error_number_ctype.value), error_description_ctype.value.decode(self._encoding)

    def is_connected(self, route_spec):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        route_spec_ctype = ctypes.create_string_buffer(route_spec.encode(self._encoding))  # case C020
        is_connected_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niSE_IsConnected(vi_ctype, route_spec_ctype, None if is_connected_ctype is None else (ctypes.pointer(is_connected_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(is_connected_ctype.value)

    def is_debounced(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        is_debounced_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niSE_IsDebounced(vi_ctype, None if is_debounced_ctype is None else (ctypes.pointer(is_debounced_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(is_debounced_ctype.value)

    def open_session(self, virtual_device_name, option_string):  # noqa: N802
        virtual_device_name_ctype = ctypes.create_string_buffer(virtual_device_name.encode(self._encoding))  # case C020
        option_string_ctype = ctypes.create_string_buffer(option_string.encode(self._encoding))  # case C020
        vi_ctype = _visatype.ViSession()  # case S220
        error_code = self._library.niSE_OpenSession(virtual_device_name_ctype, option_string_ctype, None if vi_ctype is None else (ctypes.pointer(vi_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(vi_ctype.value)

    def wait_for_debounce(self, maximum_time_ms):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        maximum_time_ms_ctype = _visatype.ViInt32(maximum_time_ms)  # case S150
        error_code = self._library.niSE_WaitForDebounce(vi_ctype, maximum_time_ms_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return
