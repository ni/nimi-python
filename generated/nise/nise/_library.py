# -*- coding: utf-8 -*-
# This file was generated

import array  # noqa: F401
import ctypes
import hightime
import nise._converters as _converters
import nise._visatype as _visatype
import nise.enums as enums
import nise.errors as errors
import threading

from nise._visatype import *  # noqa: F403,H303


# Helper functions for creating ctypes needed for calling into the driver DLL
def get_ctypes_pointer_for_buffer(value=None, library_type=None, size=None):
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


def get_ctypes_and_array(value, array_type):
    if value is not None:
        if isinstance(value, array.array):
            value_array = value
        else:
            value_array = array.array(array_type, value)
    else:
        value_array = None

    return value_array


class Library(object):
    '''Library

    Wrapper around driver library.
    Class will setup the correct ctypes information for every function on first call.
    '''

    def __init__(self, ctypes_library):
        self._func_lock = threading.Lock()
        self._library = ctypes_library
        # We cache the cfunc object from the ctypes.CDLL object
        self.niSE_CloseSession_cfunc = None
        self.niSE_Connect_cfunc = None
        self.niSE_ConnectAndDisconnect_cfunc = None
        self.niSE_Disconnect_cfunc = None
        self.niSE_DisconnectAll_cfunc = None
        self.niSE_ExpandRouteSpec_cfunc = None
        self.niSE_FindRoute_cfunc = None
        self.niSE_GetAllConnections_cfunc = None
        self.niSE_GetError_cfunc = None
        self.niSE_IsConnected_cfunc = None
        self.niSE_IsDebounced_cfunc = None
        self.niSE_OpenSession_cfunc = None
        self.niSE_WaitForDebounce_cfunc = None

    def _get_library_function(self, name):
        try:
            function = getattr(self._library, name)
        except AttributeError as e:
            raise errors.DriverTooOldError() from e
        return function

    def _get_error_description(self, session, error_code):
        '''_get_error_description

        Returns the error description.
        '''
        try:
            _, error_string = self._get_error(session)
            return error_string
        except errors.Error:
            pass

        try:
            '''
            It is expected for _get_error to raise when the session is invalid
            (IVI spec requires GetError to fail).
            Use _error_message instead. It doesn't require a session.
            '''
            error_string = self._error_message(session, error_code)
            return error_string
        except errors.Error:
            return "Failed to retrieve error description."

    def _close_session(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niSE_CloseSession_cfunc is None:
                self.niSE_CloseSession_cfunc = self._get_library_function('niSE_CloseSession')
                self.niSE_CloseSession_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSE_CloseSession_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSE_CloseSession_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def connect(self, session, connect_spec, multiconnect_mode=enums.MulticonnectMode.DEFAULT, wait_for_debounce=True):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        connect_spec_ctype = ctypes.create_string_buffer(connect_spec.encode(session._encoding))  # case C020
        multiconnect_mode_ctype = _visatype.ViInt32(multiconnect_mode.value)  # case S130
        wait_for_debounce_ctype = _visatype.ViBoolean(wait_for_debounce)  # case S150
        with self._func_lock:
            if self.niSE_Connect_cfunc is None:
                self.niSE_Connect_cfunc = self._get_library_function('niSE_Connect')
                self.niSE_Connect_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViBoolean]  # noqa: F405
                self.niSE_Connect_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSE_Connect_cfunc(vi_ctype, connect_spec_ctype, multiconnect_mode_ctype, wait_for_debounce_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def connect_and_disconnect(self, session, connect_spec, disconnect_spec, multiconnect_mode=enums.MulticonnectMode.DEFAULT, operation_order=enums.OperationOrder.AFTER, wait_for_debounce=True):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        connect_spec_ctype = ctypes.create_string_buffer(connect_spec.encode(session._encoding))  # case C020
        disconnect_spec_ctype = ctypes.create_string_buffer(disconnect_spec.encode(session._encoding))  # case C020
        multiconnect_mode_ctype = _visatype.ViInt32(multiconnect_mode.value)  # case S130
        operation_order_ctype = _visatype.ViInt32(operation_order.value)  # case S130
        wait_for_debounce_ctype = _visatype.ViBoolean(wait_for_debounce)  # case S150
        with self._func_lock:
            if self.niSE_ConnectAndDisconnect_cfunc is None:
                self.niSE_ConnectAndDisconnect_cfunc = self._get_library_function('niSE_ConnectAndDisconnect')
                self.niSE_ConnectAndDisconnect_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ViInt32, ViBoolean]  # noqa: F405
                self.niSE_ConnectAndDisconnect_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSE_ConnectAndDisconnect_cfunc(vi_ctype, connect_spec_ctype, disconnect_spec_ctype, multiconnect_mode_ctype, operation_order_ctype, wait_for_debounce_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disconnect(self, session, disconnect_spec):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        disconnect_spec_ctype = ctypes.create_string_buffer(disconnect_spec.encode(session._encoding))  # case C020
        with self._func_lock:
            if self.niSE_Disconnect_cfunc is None:
                self.niSE_Disconnect_cfunc = self._get_library_function('niSE_Disconnect')
                self.niSE_Disconnect_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSE_Disconnect_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSE_Disconnect_cfunc(vi_ctype, disconnect_spec_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disconnect_all(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niSE_DisconnectAll_cfunc is None:
                self.niSE_DisconnectAll_cfunc = self._get_library_function('niSE_DisconnectAll')
                self.niSE_DisconnectAll_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSE_DisconnectAll_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSE_DisconnectAll_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def expand_route_spec(self, session, route_spec, expand_action=enums.ExpandAction.ROUTES, expanded_route_spec_size=[1024]):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        route_spec_ctype = ctypes.create_string_buffer(route_spec.encode(session._encoding))  # case C020
        expand_action_ctype = _visatype.ViInt32(expand_action.value)  # case S130
        expanded_route_spec_ctype = (_visatype.ViChar * expanded_route_spec_size[0])()  # case C080
        expanded_route_spec_size_ctype = get_ctypes_pointer_for_buffer(value=expanded_route_spec_size, library_type=_visatype.ViInt32)  # case B550
        with self._func_lock:
            if self.niSE_ExpandRouteSpec_cfunc is None:
                self.niSE_ExpandRouteSpec_cfunc = self._get_library_function('niSE_ExpandRouteSpec')
                self.niSE_ExpandRouteSpec_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViChar), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niSE_ExpandRouteSpec_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSE_ExpandRouteSpec_cfunc(vi_ctype, route_spec_ctype, expand_action_ctype, expanded_route_spec_ctype, expanded_route_spec_size_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return expanded_route_spec_ctype.value.decode(session._encoding)

    def find_route(self, session, channel1, channel2, route_spec_size=[1024]):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel1_ctype = ctypes.create_string_buffer(channel1.encode(session._encoding))  # case C020
        channel2_ctype = ctypes.create_string_buffer(channel2.encode(session._encoding))  # case C020
        route_spec_ctype = (_visatype.ViChar * route_spec_size[0])()  # case C080
        route_spec_size_ctype = get_ctypes_pointer_for_buffer(value=route_spec_size, library_type=_visatype.ViInt32)  # case B550
        path_capability_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niSE_FindRoute_cfunc is None:
                self.niSE_FindRoute_cfunc = self._get_library_function('niSE_FindRoute')
                self.niSE_FindRoute_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niSE_FindRoute_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSE_FindRoute_cfunc(vi_ctype, channel1_ctype, channel2_ctype, route_spec_ctype, route_spec_size_ctype, None if path_capability_ctype is None else (ctypes.pointer(path_capability_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return route_spec_ctype.value.decode(session._encoding), enums.PathCapability(path_capability_ctype.value)

    def get_all_connections(self, session, route_spec_size=[1024]):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        route_spec_ctype = (_visatype.ViChar * route_spec_size[0])()  # case C080
        route_spec_size_ctype = get_ctypes_pointer_for_buffer(value=route_spec_size, library_type=_visatype.ViInt32)  # case B550
        with self._func_lock:
            if self.niSE_GetAllConnections_cfunc is None:
                self.niSE_GetAllConnections_cfunc = self._get_library_function('niSE_GetAllConnections')
                self.niSE_GetAllConnections_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niSE_GetAllConnections_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSE_GetAllConnections_cfunc(vi_ctype, route_spec_ctype, route_spec_size_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return route_spec_ctype.value.decode(session._encoding)

    def _get_error(self, session, error_description_size=[1024]):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        error_number_ctype = _visatype.ViInt32()  # case S220
        error_description_ctype = (_visatype.ViChar * error_description_size[0])()  # case C080
        error_description_size_ctype = get_ctypes_pointer_for_buffer(value=error_description_size, library_type=_visatype.ViInt32)  # case B550
        with self._func_lock:
            if self.niSE_GetError_cfunc is None:
                self.niSE_GetError_cfunc = self._get_library_function('niSE_GetError')
                self.niSE_GetError_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32), ctypes.POINTER(ViChar), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niSE_GetError_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSE_GetError_cfunc(vi_ctype, None if error_number_ctype is None else (ctypes.pointer(error_number_ctype)), error_description_ctype, error_description_size_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=True)
        return int(error_number_ctype.value), error_description_ctype.value.decode(session._encoding)

    def is_connected(self, session, route_spec):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        route_spec_ctype = ctypes.create_string_buffer(route_spec.encode(session._encoding))  # case C020
        is_connected_ctype = _visatype.ViBoolean()  # case S220
        with self._func_lock:
            if self.niSE_IsConnected_cfunc is None:
                self.niSE_IsConnected_cfunc = self._get_library_function('niSE_IsConnected')
                self.niSE_IsConnected_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niSE_IsConnected_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSE_IsConnected_cfunc(vi_ctype, route_spec_ctype, None if is_connected_ctype is None else (ctypes.pointer(is_connected_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(is_connected_ctype.value)

    def is_debounced(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        is_debounced_ctype = _visatype.ViBoolean()  # case S220
        with self._func_lock:
            if self.niSE_IsDebounced_cfunc is None:
                self.niSE_IsDebounced_cfunc = self._get_library_function('niSE_IsDebounced')
                self.niSE_IsDebounced_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niSE_IsDebounced_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSE_IsDebounced_cfunc(vi_ctype, None if is_debounced_ctype is None else (ctypes.pointer(is_debounced_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(is_debounced_ctype.value)

    def _open_session(self, session, virtual_device_name, option_string=""):  # noqa: N802
        virtual_device_name_ctype = ctypes.create_string_buffer(virtual_device_name.encode(session._encoding))  # case C020
        option_string_ctype = ctypes.create_string_buffer(_converters.convert_init_with_options_dictionary(option_string).encode(session._encoding))  # case C040
        vi_ctype = _visatype.ViSession()  # case S220
        with self._func_lock:
            if self.niSE_OpenSession_cfunc is None:
                self.niSE_OpenSession_cfunc = self._get_library_function('niSE_OpenSession')
                self.niSE_OpenSession_cfunc.argtypes = [ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViSession)]  # noqa: F405
                self.niSE_OpenSession_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSE_OpenSession_cfunc(virtual_device_name_ctype, option_string_ctype, None if vi_ctype is None else (ctypes.pointer(vi_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(vi_ctype.value)

    def wait_for_debounce(self, session, maximum_time_ms=hightime.timedelta(milliseconds=-1)):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        maximum_time_ms_ctype = _converters.convert_timedelta_to_milliseconds_int32(maximum_time_ms)  # case S140
        with self._func_lock:
            if self.niSE_WaitForDebounce_cfunc is None:
                self.niSE_WaitForDebounce_cfunc = self._get_library_function('niSE_WaitForDebounce')
                self.niSE_WaitForDebounce_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niSE_WaitForDebounce_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSE_WaitForDebounce_cfunc(vi_ctype, maximum_time_ms_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return
