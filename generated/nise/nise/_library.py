# -*- coding: utf-8 -*-
# This file was generated

import ctypes
import nise.errors as errors
import threading

from nise._visatype import *  # noqa: F403,H303


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

    def niSE_CloseSession(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niSE_CloseSession_cfunc is None:
                self.niSE_CloseSession_cfunc = self._get_library_function('niSE_CloseSession')
                self.niSE_CloseSession_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSE_CloseSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niSE_CloseSession_cfunc(vi)

    def niSE_Connect(self, vi, connect_spec, multiconnect_mode, wait_for_debounce):  # noqa: N802
        with self._func_lock:
            if self.niSE_Connect_cfunc is None:
                self.niSE_Connect_cfunc = self._get_library_function('niSE_Connect')
                self.niSE_Connect_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViBoolean]  # noqa: F405
                self.niSE_Connect_cfunc.restype = ViStatus  # noqa: F405
        return self.niSE_Connect_cfunc(vi, connect_spec, multiconnect_mode, wait_for_debounce)

    def niSE_ConnectAndDisconnect(self, vi, connect_spec, disconnect_spec, multiconnect_mode, operation_order, wait_for_debounce):  # noqa: N802
        with self._func_lock:
            if self.niSE_ConnectAndDisconnect_cfunc is None:
                self.niSE_ConnectAndDisconnect_cfunc = self._get_library_function('niSE_ConnectAndDisconnect')
                self.niSE_ConnectAndDisconnect_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ViInt32, ViBoolean]  # noqa: F405
                self.niSE_ConnectAndDisconnect_cfunc.restype = ViStatus  # noqa: F405
        return self.niSE_ConnectAndDisconnect_cfunc(vi, connect_spec, disconnect_spec, multiconnect_mode, operation_order, wait_for_debounce)

    def niSE_Disconnect(self, vi, disconnect_spec):  # noqa: N802
        with self._func_lock:
            if self.niSE_Disconnect_cfunc is None:
                self.niSE_Disconnect_cfunc = self._get_library_function('niSE_Disconnect')
                self.niSE_Disconnect_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSE_Disconnect_cfunc.restype = ViStatus  # noqa: F405
        return self.niSE_Disconnect_cfunc(vi, disconnect_spec)

    def niSE_DisconnectAll(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niSE_DisconnectAll_cfunc is None:
                self.niSE_DisconnectAll_cfunc = self._get_library_function('niSE_DisconnectAll')
                self.niSE_DisconnectAll_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSE_DisconnectAll_cfunc.restype = ViStatus  # noqa: F405
        return self.niSE_DisconnectAll_cfunc(vi)

    def niSE_ExpandRouteSpec(self, vi, route_spec, expand_action, expanded_route_spec, expanded_route_spec_size):  # noqa: N802
        with self._func_lock:
            if self.niSE_ExpandRouteSpec_cfunc is None:
                self.niSE_ExpandRouteSpec_cfunc = self._get_library_function('niSE_ExpandRouteSpec')
                self.niSE_ExpandRouteSpec_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViChar), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niSE_ExpandRouteSpec_cfunc.restype = ViStatus  # noqa: F405
        return self.niSE_ExpandRouteSpec_cfunc(vi, route_spec, expand_action, expanded_route_spec, expanded_route_spec_size)

    def niSE_FindRoute(self, vi, channel1, channel2, route_spec, route_spec_size, path_capability):  # noqa: N802
        with self._func_lock:
            if self.niSE_FindRoute_cfunc is None:
                self.niSE_FindRoute_cfunc = self._get_library_function('niSE_FindRoute')
                self.niSE_FindRoute_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niSE_FindRoute_cfunc.restype = ViStatus  # noqa: F405
        return self.niSE_FindRoute_cfunc(vi, channel1, channel2, route_spec, route_spec_size, path_capability)

    def niSE_GetAllConnections(self, vi, route_spec, route_spec_size):  # noqa: N802
        with self._func_lock:
            if self.niSE_GetAllConnections_cfunc is None:
                self.niSE_GetAllConnections_cfunc = self._get_library_function('niSE_GetAllConnections')
                self.niSE_GetAllConnections_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niSE_GetAllConnections_cfunc.restype = ViStatus  # noqa: F405
        return self.niSE_GetAllConnections_cfunc(vi, route_spec, route_spec_size)

    def niSE_GetError(self, vi, error_number, error_description, error_description_size):  # noqa: N802
        with self._func_lock:
            if self.niSE_GetError_cfunc is None:
                self.niSE_GetError_cfunc = self._get_library_function('niSE_GetError')
                self.niSE_GetError_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32), ctypes.POINTER(ViChar), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niSE_GetError_cfunc.restype = ViStatus  # noqa: F405
        return self.niSE_GetError_cfunc(vi, error_number, error_description, error_description_size)

    def niSE_IsConnected(self, vi, route_spec, is_connected):  # noqa: N802
        with self._func_lock:
            if self.niSE_IsConnected_cfunc is None:
                self.niSE_IsConnected_cfunc = self._get_library_function('niSE_IsConnected')
                self.niSE_IsConnected_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niSE_IsConnected_cfunc.restype = ViStatus  # noqa: F405
        return self.niSE_IsConnected_cfunc(vi, route_spec, is_connected)

    def niSE_IsDebounced(self, vi, is_debounced):  # noqa: N802
        with self._func_lock:
            if self.niSE_IsDebounced_cfunc is None:
                self.niSE_IsDebounced_cfunc = self._get_library_function('niSE_IsDebounced')
                self.niSE_IsDebounced_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niSE_IsDebounced_cfunc.restype = ViStatus  # noqa: F405
        return self.niSE_IsDebounced_cfunc(vi, is_debounced)

    def niSE_OpenSession(self, virtual_device_name, option_string, vi):  # noqa: N802
        with self._func_lock:
            if self.niSE_OpenSession_cfunc is None:
                self.niSE_OpenSession_cfunc = self._get_library_function('niSE_OpenSession')
                self.niSE_OpenSession_cfunc.argtypes = [ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViSession)]  # noqa: F405
                self.niSE_OpenSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niSE_OpenSession_cfunc(virtual_device_name, option_string, vi)

    def niSE_WaitForDebounce(self, vi, maximum_time_ms):  # noqa: N802
        with self._func_lock:
            if self.niSE_WaitForDebounce_cfunc is None:
                self.niSE_WaitForDebounce_cfunc = self._get_library_function('niSE_WaitForDebounce')
                self.niSE_WaitForDebounce_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niSE_WaitForDebounce_cfunc.restype = ViStatus  # noqa: F405
        return self.niSE_WaitForDebounce_cfunc(vi, maximum_time_ms)
