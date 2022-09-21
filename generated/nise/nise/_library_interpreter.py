# -*- coding: utf-8 -*-
# This file was generated

import array
import ctypes
import hightime  # noqa: F401
import nise._converters as _converters  # noqa: F401
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

    def __init__(self):
        self._library = _library_singleton.get()

    def get_error_description(self, session_handle, encoding, error_code):
        '''get_error_description

        Returns the error description.
        '''
        try:
            _, error_string = self.get_error(session_handle, encoding, [1024])
            return error_string
        except errors.Error:
            return "Failed to retrieve error description."

    def close_session(self, session_handle, encoding):  # noqa: N802
        vi_ctype = _visatype.ViSession(session_handle)  # case S110
        error_code = self._library.niSE_CloseSession(vi_ctype)
        errors.handle_error(self, session_handle, encoding, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def connect(self, session_handle, encoding, connect_spec, multiconnect_mode, wait_for_debounce):  # noqa: N802
        vi_ctype = _visatype.ViSession(session_handle)  # case S110
        connect_spec_ctype = ctypes.create_string_buffer(connect_spec.encode(encoding))  # case C020
        multiconnect_mode_ctype = _visatype.ViInt32(multiconnect_mode.value)  # case S130
        wait_for_debounce_ctype = _visatype.ViBoolean(wait_for_debounce)  # case S150
        error_code = self._library.niSE_Connect(vi_ctype, connect_spec_ctype, multiconnect_mode_ctype, wait_for_debounce_ctype)
        errors.handle_error(self, session_handle, encoding, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def connect_and_disconnect(self, session_handle, encoding, connect_spec, disconnect_spec, multiconnect_mode, operation_order, wait_for_debounce):  # noqa: N802
        vi_ctype = _visatype.ViSession(session_handle)  # case S110
        connect_spec_ctype = ctypes.create_string_buffer(connect_spec.encode(encoding))  # case C020
        disconnect_spec_ctype = ctypes.create_string_buffer(disconnect_spec.encode(encoding))  # case C020
        multiconnect_mode_ctype = _visatype.ViInt32(multiconnect_mode.value)  # case S130
        operation_order_ctype = _visatype.ViInt32(operation_order.value)  # case S130
        wait_for_debounce_ctype = _visatype.ViBoolean(wait_for_debounce)  # case S150
        error_code = self._library.niSE_ConnectAndDisconnect(vi_ctype, connect_spec_ctype, disconnect_spec_ctype, multiconnect_mode_ctype, operation_order_ctype, wait_for_debounce_ctype)
        errors.handle_error(self, session_handle, encoding, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disconnect(self, session_handle, encoding, disconnect_spec):  # noqa: N802
        vi_ctype = _visatype.ViSession(session_handle)  # case S110
        disconnect_spec_ctype = ctypes.create_string_buffer(disconnect_spec.encode(encoding))  # case C020
        error_code = self._library.niSE_Disconnect(vi_ctype, disconnect_spec_ctype)
        errors.handle_error(self, session_handle, encoding, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disconnect_all(self, session_handle, encoding):  # noqa: N802
        vi_ctype = _visatype.ViSession(session_handle)  # case S110
        error_code = self._library.niSE_DisconnectAll(vi_ctype)
        errors.handle_error(self, session_handle, encoding, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def expand_route_spec(self, session_handle, encoding, route_spec, expand_action, expanded_route_spec_size):  # noqa: N802
        vi_ctype = _visatype.ViSession(session_handle)  # case S110
        route_spec_ctype = ctypes.create_string_buffer(route_spec.encode(encoding))  # case C020
        expand_action_ctype = _visatype.ViInt32(expand_action.value)  # case S130
        expanded_route_spec_ctype = (_visatype.ViChar * expanded_route_spec_size[0])()  # case C080
        expanded_route_spec_size_ctype = _get_ctypes_pointer_for_buffer(value=expanded_route_spec_size, library_type=_visatype.ViInt32)  # case B550
        error_code = self._library.niSE_ExpandRouteSpec(vi_ctype, route_spec_ctype, expand_action_ctype, expanded_route_spec_ctype, expanded_route_spec_size_ctype)
        errors.handle_error(self, session_handle, encoding, error_code, ignore_warnings=False, is_error_handling=False)
        return expanded_route_spec_ctype.value.decode(encoding)

    def find_route(self, session_handle, encoding, channel1, channel2, route_spec_size):  # noqa: N802
        vi_ctype = _visatype.ViSession(session_handle)  # case S110
        channel1_ctype = ctypes.create_string_buffer(channel1.encode(encoding))  # case C020
        channel2_ctype = ctypes.create_string_buffer(channel2.encode(encoding))  # case C020
        route_spec_ctype = (_visatype.ViChar * route_spec_size[0])()  # case C080
        route_spec_size_ctype = _get_ctypes_pointer_for_buffer(value=route_spec_size, library_type=_visatype.ViInt32)  # case B550
        path_capability_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niSE_FindRoute(vi_ctype, channel1_ctype, channel2_ctype, route_spec_ctype, route_spec_size_ctype, None if path_capability_ctype is None else (ctypes.pointer(path_capability_ctype)))
        errors.handle_error(self, session_handle, encoding, error_code, ignore_warnings=False, is_error_handling=False)
        return route_spec_ctype.value.decode(encoding), enums.PathCapability(path_capability_ctype.value)

    def get_all_connections(self, session_handle, encoding, route_spec_size):  # noqa: N802
        vi_ctype = _visatype.ViSession(session_handle)  # case S110
        route_spec_ctype = (_visatype.ViChar * route_spec_size[0])()  # case C080
        route_spec_size_ctype = _get_ctypes_pointer_for_buffer(value=route_spec_size, library_type=_visatype.ViInt32)  # case B550
        error_code = self._library.niSE_GetAllConnections(vi_ctype, route_spec_ctype, route_spec_size_ctype)
        errors.handle_error(self, session_handle, encoding, error_code, ignore_warnings=False, is_error_handling=False)
        return route_spec_ctype.value.decode(encoding)

    def get_error(self, session_handle, encoding, error_description_size):  # noqa: N802
        vi_ctype = _visatype.ViSession(session_handle)  # case S110
        error_number_ctype = _visatype.ViInt32()  # case S220
        error_description_ctype = (_visatype.ViChar * error_description_size[0])()  # case C080
        error_description_size_ctype = _get_ctypes_pointer_for_buffer(value=error_description_size, library_type=_visatype.ViInt32)  # case B550
        error_code = self._library.niSE_GetError(vi_ctype, None if error_number_ctype is None else (ctypes.pointer(error_number_ctype)), error_description_ctype, error_description_size_ctype)
        errors.handle_error(self, session_handle, encoding, error_code, ignore_warnings=False, is_error_handling=True)
        return int(error_number_ctype.value), error_description_ctype.value.decode(encoding)

    def is_connected(self, session_handle, encoding, route_spec):  # noqa: N802
        vi_ctype = _visatype.ViSession(session_handle)  # case S110
        route_spec_ctype = ctypes.create_string_buffer(route_spec.encode(encoding))  # case C020
        is_connected_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niSE_IsConnected(vi_ctype, route_spec_ctype, None if is_connected_ctype is None else (ctypes.pointer(is_connected_ctype)))
        errors.handle_error(self, session_handle, encoding, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(is_connected_ctype.value)

    def is_debounced(self, session_handle, encoding):  # noqa: N802
        vi_ctype = _visatype.ViSession(session_handle)  # case S110
        is_debounced_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niSE_IsDebounced(vi_ctype, None if is_debounced_ctype is None else (ctypes.pointer(is_debounced_ctype)))
        errors.handle_error(self, session_handle, encoding, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(is_debounced_ctype.value)

    def open_session(self, session_handle, encoding, virtual_device_name, option_string):  # noqa: N802
        virtual_device_name_ctype = ctypes.create_string_buffer(virtual_device_name.encode(encoding))  # case C020
        option_string_ctype = ctypes.create_string_buffer(_converters.convert_init_with_options_dictionary(option_string).encode(encoding))  # case C040
        vi_ctype = _visatype.ViSession()  # case S220
        error_code = self._library.niSE_OpenSession(virtual_device_name_ctype, option_string_ctype, None if vi_ctype is None else (ctypes.pointer(vi_ctype)))
        errors.handle_error(self, session_handle, encoding, error_code, ignore_warnings=False, is_error_handling=False)
        return int(vi_ctype.value)

    def wait_for_debounce(self, session_handle, encoding, maximum_time_ms):  # noqa: N802
        vi_ctype = _visatype.ViSession(session_handle)  # case S110
        maximum_time_ms_ctype = _converters.convert_timedelta_to_milliseconds_int32(maximum_time_ms)  # case S140
        error_code = self._library.niSE_WaitForDebounce(vi_ctype, maximum_time_ms_ctype)
        errors.handle_error(self, session_handle, encoding, error_code, ignore_warnings=False, is_error_handling=False)
        return
