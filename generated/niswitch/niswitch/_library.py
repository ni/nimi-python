# -*- coding: utf-8 -*-
# This file was generated

import array  # noqa: F401
import ctypes
import hightime
import niswitch._converters as _converters
import niswitch._visatype as _visatype
import niswitch.enums as enums
import niswitch.errors as errors
import threading

from niswitch._visatype import *  # noqa: F403,H303


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
        self.niSwitch_AbortScan_cfunc = None
        self.niSwitch_CanConnect_cfunc = None
        self.niSwitch_Commit_cfunc = None
        self.niSwitch_Connect_cfunc = None
        self.niSwitch_ConnectMultiple_cfunc = None
        self.niSwitch_Disable_cfunc = None
        self.niSwitch_Disconnect_cfunc = None
        self.niSwitch_DisconnectAll_cfunc = None
        self.niSwitch_DisconnectMultiple_cfunc = None
        self.niSwitch_GetAttributeViBoolean_cfunc = None
        self.niSwitch_GetAttributeViInt32_cfunc = None
        self.niSwitch_GetAttributeViReal64_cfunc = None
        self.niSwitch_GetAttributeViString_cfunc = None
        self.niSwitch_GetChannelName_cfunc = None
        self.niSwitch_GetError_cfunc = None
        self.niSwitch_GetPath_cfunc = None
        self.niSwitch_GetRelayCount_cfunc = None
        self.niSwitch_GetRelayName_cfunc = None
        self.niSwitch_GetRelayPosition_cfunc = None
        self.niSwitch_InitWithTopology_cfunc = None
        self.niSwitch_InitiateScan_cfunc = None
        self.niSwitch_LockSession_cfunc = None
        self.niSwitch_RelayControl_cfunc = None
        self.niSwitch_ResetWithDefaults_cfunc = None
        self.niSwitch_RouteScanAdvancedOutput_cfunc = None
        self.niSwitch_RouteTriggerInput_cfunc = None
        self.niSwitch_SendSoftwareTrigger_cfunc = None
        self.niSwitch_SetAttributeViBoolean_cfunc = None
        self.niSwitch_SetAttributeViInt32_cfunc = None
        self.niSwitch_SetAttributeViReal64_cfunc = None
        self.niSwitch_SetAttributeViString_cfunc = None
        self.niSwitch_SetPath_cfunc = None
        self.niSwitch_UnlockSession_cfunc = None
        self.niSwitch_WaitForDebounce_cfunc = None
        self.niSwitch_WaitForScanComplete_cfunc = None
        self.niSwitch_close_cfunc = None
        self.niSwitch_error_message_cfunc = None
        self.niSwitch_reset_cfunc = None
        self.niSwitch_self_test_cfunc = None

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

    def abort(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niSwitch_AbortScan_cfunc is None:
                self.niSwitch_AbortScan_cfunc = self._get_library_function('niSwitch_AbortScan')
                self.niSwitch_AbortScan_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSwitch_AbortScan_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSwitch_AbortScan_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def can_connect(self, session, channel1, channel2):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel1_ctype = ctypes.create_string_buffer(channel1.encode(session._encoding))  # case C020
        channel2_ctype = ctypes.create_string_buffer(channel2.encode(session._encoding))  # case C020
        path_capability_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niSwitch_CanConnect_cfunc is None:
                self.niSwitch_CanConnect_cfunc = self._get_library_function('niSwitch_CanConnect')
                self.niSwitch_CanConnect_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niSwitch_CanConnect_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSwitch_CanConnect_cfunc(vi_ctype, channel1_ctype, channel2_ctype, None if path_capability_ctype is None else (ctypes.pointer(path_capability_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return enums.PathCapability(path_capability_ctype.value)

    def commit(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niSwitch_Commit_cfunc is None:
                self.niSwitch_Commit_cfunc = self._get_library_function('niSwitch_Commit')
                self.niSwitch_Commit_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSwitch_Commit_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSwitch_Commit_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def connect(self, session, channel1, channel2):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel1_ctype = ctypes.create_string_buffer(channel1.encode(session._encoding))  # case C020
        channel2_ctype = ctypes.create_string_buffer(channel2.encode(session._encoding))  # case C020
        with self._func_lock:
            if self.niSwitch_Connect_cfunc is None:
                self.niSwitch_Connect_cfunc = self._get_library_function('niSwitch_Connect')
                self.niSwitch_Connect_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSwitch_Connect_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSwitch_Connect_cfunc(vi_ctype, channel1_ctype, channel2_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def connect_multiple(self, session, connection_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        connection_list_ctype = ctypes.create_string_buffer(connection_list.encode(session._encoding))  # case C020
        with self._func_lock:
            if self.niSwitch_ConnectMultiple_cfunc is None:
                self.niSwitch_ConnectMultiple_cfunc = self._get_library_function('niSwitch_ConnectMultiple')
                self.niSwitch_ConnectMultiple_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSwitch_ConnectMultiple_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSwitch_ConnectMultiple_cfunc(vi_ctype, connection_list_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disable(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niSwitch_Disable_cfunc is None:
                self.niSwitch_Disable_cfunc = self._get_library_function('niSwitch_Disable')
                self.niSwitch_Disable_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSwitch_Disable_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSwitch_Disable_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disconnect(self, session, channel1, channel2):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel1_ctype = ctypes.create_string_buffer(channel1.encode(session._encoding))  # case C020
        channel2_ctype = ctypes.create_string_buffer(channel2.encode(session._encoding))  # case C020
        with self._func_lock:
            if self.niSwitch_Disconnect_cfunc is None:
                self.niSwitch_Disconnect_cfunc = self._get_library_function('niSwitch_Disconnect')
                self.niSwitch_Disconnect_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSwitch_Disconnect_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSwitch_Disconnect_cfunc(vi_ctype, channel1_ctype, channel2_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disconnect_all(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niSwitch_DisconnectAll_cfunc is None:
                self.niSwitch_DisconnectAll_cfunc = self._get_library_function('niSwitch_DisconnectAll')
                self.niSwitch_DisconnectAll_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSwitch_DisconnectAll_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSwitch_DisconnectAll_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disconnect_multiple(self, session, disconnection_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        disconnection_list_ctype = ctypes.create_string_buffer(disconnection_list.encode(session._encoding))  # case C020
        with self._func_lock:
            if self.niSwitch_DisconnectMultiple_cfunc is None:
                self.niSwitch_DisconnectMultiple_cfunc = self._get_library_function('niSwitch_DisconnectMultiple')
                self.niSwitch_DisconnectMultiple_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSwitch_DisconnectMultiple_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSwitch_DisconnectMultiple_cfunc(vi_ctype, disconnection_list_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _get_attribute_vi_boolean(self, session, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViBoolean()  # case S220
        with self._func_lock:
            if self.niSwitch_GetAttributeViBoolean_cfunc is None:
                self.niSwitch_GetAttributeViBoolean_cfunc = self._get_library_function('niSwitch_GetAttributeViBoolean')
                self.niSwitch_GetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niSwitch_GetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSwitch_GetAttributeViBoolean_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(attribute_value_ctype.value)

    def _get_attribute_vi_int32(self, session, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niSwitch_GetAttributeViInt32_cfunc is None:
                self.niSwitch_GetAttributeViInt32_cfunc = self._get_library_function('niSwitch_GetAttributeViInt32')
                self.niSwitch_GetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niSwitch_GetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSwitch_GetAttributeViInt32_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(attribute_value_ctype.value)

    def _get_attribute_vi_real64(self, session, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViReal64()  # case S220
        with self._func_lock:
            if self.niSwitch_GetAttributeViReal64_cfunc is None:
                self.niSwitch_GetAttributeViReal64_cfunc = self._get_library_function('niSwitch_GetAttributeViReal64')
                self.niSwitch_GetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niSwitch_GetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSwitch_GetAttributeViReal64_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return float(attribute_value_ctype.value)

    def _get_attribute_vi_string(self, session, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        array_size_ctype = _visatype.ViInt32()  # case S170
        attribute_value_ctype = None  # case C050
        with self._func_lock:
            if self.niSwitch_GetAttributeViString_cfunc is None:
                self.niSwitch_GetAttributeViString_cfunc = self._get_library_function('niSwitch_GetAttributeViString')
                self.niSwitch_GetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSwitch_GetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSwitch_GetAttributeViString_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, array_size_ctype, attribute_value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=False)
        array_size_ctype = _visatype.ViInt32(error_code)  # case S180
        attribute_value_ctype = (_visatype.ViChar * array_size_ctype.value)()  # case C060
        error_code = self.niSwitch_GetAttributeViString_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, array_size_ctype, attribute_value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return attribute_value_ctype.value.decode(session._encoding)

    def get_channel_name(self, session, index):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        index_ctype = _visatype.ViInt32(index)  # case S150
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        channel_name_buffer_ctype = None  # case C050
        with self._func_lock:
            if self.niSwitch_GetChannelName_cfunc is None:
                self.niSwitch_GetChannelName_cfunc = self._get_library_function('niSwitch_GetChannelName')
                self.niSwitch_GetChannelName_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSwitch_GetChannelName_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSwitch_GetChannelName_cfunc(vi_ctype, index_ctype, buffer_size_ctype, channel_name_buffer_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        channel_name_buffer_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self.niSwitch_GetChannelName_cfunc(vi_ctype, index_ctype, buffer_size_ctype, channel_name_buffer_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return channel_name_buffer_ctype.value.decode(session._encoding)

    def _get_error(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        code_ctype = _visatype.ViStatus()  # case S220
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        description_ctype = None  # case C050
        with self._func_lock:
            if self.niSwitch_GetError_cfunc is None:
                self.niSwitch_GetError_cfunc = self._get_library_function('niSwitch_GetError')
                self.niSwitch_GetError_cfunc.argtypes = [ViSession, ctypes.POINTER(ViStatus), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSwitch_GetError_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSwitch_GetError_cfunc(vi_ctype, None if code_ctype is None else (ctypes.pointer(code_ctype)), buffer_size_ctype, description_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=True)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        description_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self.niSwitch_GetError_cfunc(vi_ctype, None if code_ctype is None else (ctypes.pointer(code_ctype)), buffer_size_ctype, description_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=True)
        return int(code_ctype.value), description_ctype.value.decode(session._encoding)

    def get_path(self, session, channel1, channel2):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel1_ctype = ctypes.create_string_buffer(channel1.encode(session._encoding))  # case C020
        channel2_ctype = ctypes.create_string_buffer(channel2.encode(session._encoding))  # case C020
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        path_ctype = None  # case C050
        with self._func_lock:
            if self.niSwitch_GetPath_cfunc is None:
                self.niSwitch_GetPath_cfunc = self._get_library_function('niSwitch_GetPath')
                self.niSwitch_GetPath_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSwitch_GetPath_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSwitch_GetPath_cfunc(vi_ctype, channel1_ctype, channel2_ctype, buffer_size_ctype, path_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        path_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self.niSwitch_GetPath_cfunc(vi_ctype, channel1_ctype, channel2_ctype, buffer_size_ctype, path_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return path_ctype.value.decode(session._encoding)

    def get_relay_count(self, session, relay_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        relay_name_ctype = ctypes.create_string_buffer(relay_name.encode(session._encoding))  # case C020
        relay_count_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niSwitch_GetRelayCount_cfunc is None:
                self.niSwitch_GetRelayCount_cfunc = self._get_library_function('niSwitch_GetRelayCount')
                self.niSwitch_GetRelayCount_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niSwitch_GetRelayCount_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSwitch_GetRelayCount_cfunc(vi_ctype, relay_name_ctype, None if relay_count_ctype is None else (ctypes.pointer(relay_count_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(relay_count_ctype.value)

    def get_relay_name(self, session, index):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        index_ctype = _visatype.ViInt32(index)  # case S150
        relay_name_buffer_size_ctype = _visatype.ViInt32()  # case S170
        relay_name_buffer_ctype = None  # case C050
        with self._func_lock:
            if self.niSwitch_GetRelayName_cfunc is None:
                self.niSwitch_GetRelayName_cfunc = self._get_library_function('niSwitch_GetRelayName')
                self.niSwitch_GetRelayName_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSwitch_GetRelayName_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSwitch_GetRelayName_cfunc(vi_ctype, index_ctype, relay_name_buffer_size_ctype, relay_name_buffer_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=False)
        relay_name_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        relay_name_buffer_ctype = (_visatype.ViChar * relay_name_buffer_size_ctype.value)()  # case C060
        error_code = self.niSwitch_GetRelayName_cfunc(vi_ctype, index_ctype, relay_name_buffer_size_ctype, relay_name_buffer_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return relay_name_buffer_ctype.value.decode(session._encoding)

    def get_relay_position(self, session, relay_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        relay_name_ctype = ctypes.create_string_buffer(relay_name.encode(session._encoding))  # case C020
        relay_position_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niSwitch_GetRelayPosition_cfunc is None:
                self.niSwitch_GetRelayPosition_cfunc = self._get_library_function('niSwitch_GetRelayPosition')
                self.niSwitch_GetRelayPosition_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niSwitch_GetRelayPosition_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSwitch_GetRelayPosition_cfunc(vi_ctype, relay_name_ctype, None if relay_position_ctype is None else (ctypes.pointer(relay_position_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return enums.RelayPosition(relay_position_ctype.value)

    def _init_with_topology(self, session, resource_name, topology="Configured Topology", simulate=False, reset_device=False):  # noqa: N802
        resource_name_ctype = ctypes.create_string_buffer(resource_name.encode(session._encoding))  # case C020
        topology_ctype = ctypes.create_string_buffer(topology.encode(session._encoding))  # case C020
        simulate_ctype = _visatype.ViBoolean(simulate)  # case S150
        reset_device_ctype = _visatype.ViBoolean(reset_device)  # case S150
        vi_ctype = _visatype.ViSession()  # case S220
        with self._func_lock:
            if self.niSwitch_InitWithTopology_cfunc is None:
                self.niSwitch_InitWithTopology_cfunc = self._get_library_function('niSwitch_InitWithTopology')
                self.niSwitch_InitWithTopology_cfunc.argtypes = [ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViBoolean, ViBoolean, ctypes.POINTER(ViSession)]  # noqa: F405
                self.niSwitch_InitWithTopology_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSwitch_InitWithTopology_cfunc(resource_name_ctype, topology_ctype, simulate_ctype, reset_device_ctype, None if vi_ctype is None else (ctypes.pointer(vi_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(vi_ctype.value)

    def _initiate_scan(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niSwitch_InitiateScan_cfunc is None:
                self.niSwitch_InitiateScan_cfunc = self._get_library_function('niSwitch_InitiateScan')
                self.niSwitch_InitiateScan_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSwitch_InitiateScan_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSwitch_InitiateScan_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def lock(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        caller_has_lock_ctype = _visatype.ViBoolean()  # case S220
        with self._func_lock:
            if self.niSwitch_LockSession_cfunc is None:
                self.niSwitch_LockSession_cfunc = self._get_library_function('niSwitch_LockSession')
                self.niSwitch_LockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niSwitch_LockSession_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSwitch_LockSession_cfunc(vi_ctype, None if caller_has_lock_ctype is None else (ctypes.pointer(caller_has_lock_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(caller_has_lock_ctype.value)

    def relay_control(self, session, relay_name, relay_action):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        relay_name_ctype = ctypes.create_string_buffer(relay_name.encode(session._encoding))  # case C020
        relay_action_ctype = _visatype.ViInt32(relay_action.value)  # case S130
        with self._func_lock:
            if self.niSwitch_RelayControl_cfunc is None:
                self.niSwitch_RelayControl_cfunc = self._get_library_function('niSwitch_RelayControl')
                self.niSwitch_RelayControl_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niSwitch_RelayControl_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSwitch_RelayControl_cfunc(vi_ctype, relay_name_ctype, relay_action_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def reset_with_defaults(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niSwitch_ResetWithDefaults_cfunc is None:
                self.niSwitch_ResetWithDefaults_cfunc = self._get_library_function('niSwitch_ResetWithDefaults')
                self.niSwitch_ResetWithDefaults_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSwitch_ResetWithDefaults_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSwitch_ResetWithDefaults_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def route_scan_advanced_output(self, session, scan_advanced_output_connector, scan_advanced_output_bus_line, invert=False):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        scan_advanced_output_connector_ctype = _visatype.ViInt32(scan_advanced_output_connector.value)  # case S130
        scan_advanced_output_bus_line_ctype = _visatype.ViInt32(scan_advanced_output_bus_line.value)  # case S130
        invert_ctype = _visatype.ViBoolean(invert)  # case S150
        with self._func_lock:
            if self.niSwitch_RouteScanAdvancedOutput_cfunc is None:
                self.niSwitch_RouteScanAdvancedOutput_cfunc = self._get_library_function('niSwitch_RouteScanAdvancedOutput')
                self.niSwitch_RouteScanAdvancedOutput_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ViBoolean]  # noqa: F405
                self.niSwitch_RouteScanAdvancedOutput_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSwitch_RouteScanAdvancedOutput_cfunc(vi_ctype, scan_advanced_output_connector_ctype, scan_advanced_output_bus_line_ctype, invert_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def route_trigger_input(self, session, trigger_input_connector, trigger_input_bus_line, invert=False):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        trigger_input_connector_ctype = _visatype.ViInt32(trigger_input_connector.value)  # case S130
        trigger_input_bus_line_ctype = _visatype.ViInt32(trigger_input_bus_line.value)  # case S130
        invert_ctype = _visatype.ViBoolean(invert)  # case S150
        with self._func_lock:
            if self.niSwitch_RouteTriggerInput_cfunc is None:
                self.niSwitch_RouteTriggerInput_cfunc = self._get_library_function('niSwitch_RouteTriggerInput')
                self.niSwitch_RouteTriggerInput_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ViBoolean]  # noqa: F405
                self.niSwitch_RouteTriggerInput_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSwitch_RouteTriggerInput_cfunc(vi_ctype, trigger_input_connector_ctype, trigger_input_bus_line_ctype, invert_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def send_software_trigger(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niSwitch_SendSoftwareTrigger_cfunc is None:
                self.niSwitch_SendSoftwareTrigger_cfunc = self._get_library_function('niSwitch_SendSoftwareTrigger')
                self.niSwitch_SendSoftwareTrigger_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSwitch_SendSoftwareTrigger_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSwitch_SendSoftwareTrigger_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_boolean(self, session, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViBoolean(attribute_value)  # case S150
        with self._func_lock:
            if self.niSwitch_SetAttributeViBoolean_cfunc is None:
                self.niSwitch_SetAttributeViBoolean_cfunc = self._get_library_function('niSwitch_SetAttributeViBoolean')
                self.niSwitch_SetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViBoolean]  # noqa: F405
                self.niSwitch_SetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSwitch_SetAttributeViBoolean_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_int32(self, session, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt32(attribute_value)  # case S150
        with self._func_lock:
            if self.niSwitch_SetAttributeViInt32_cfunc is None:
                self.niSwitch_SetAttributeViInt32_cfunc = self._get_library_function('niSwitch_SetAttributeViInt32')
                self.niSwitch_SetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32]  # noqa: F405
                self.niSwitch_SetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSwitch_SetAttributeViInt32_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_real64(self, session, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViReal64(attribute_value)  # case S150
        with self._func_lock:
            if self.niSwitch_SetAttributeViReal64_cfunc is None:
                self.niSwitch_SetAttributeViReal64_cfunc = self._get_library_function('niSwitch_SetAttributeViReal64')
                self.niSwitch_SetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViReal64]  # noqa: F405
                self.niSwitch_SetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSwitch_SetAttributeViReal64_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_string(self, session, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = ctypes.create_string_buffer(attribute_value.encode(session._encoding))  # case C020
        with self._func_lock:
            if self.niSwitch_SetAttributeViString_cfunc is None:
                self.niSwitch_SetAttributeViString_cfunc = self._get_library_function('niSwitch_SetAttributeViString')
                self.niSwitch_SetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSwitch_SetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSwitch_SetAttributeViString_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_path(self, session, path_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        path_list_ctype = ctypes.create_string_buffer(path_list.encode(session._encoding))  # case C020
        with self._func_lock:
            if self.niSwitch_SetPath_cfunc is None:
                self.niSwitch_SetPath_cfunc = self._get_library_function('niSwitch_SetPath')
                self.niSwitch_SetPath_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSwitch_SetPath_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSwitch_SetPath_cfunc(vi_ctype, path_list_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def unlock(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        caller_has_lock_ctype = _visatype.ViBoolean()  # case S220
        with self._func_lock:
            if self.niSwitch_UnlockSession_cfunc is None:
                self.niSwitch_UnlockSession_cfunc = self._get_library_function('niSwitch_UnlockSession')
                self.niSwitch_UnlockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niSwitch_UnlockSession_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSwitch_UnlockSession_cfunc(vi_ctype, None if caller_has_lock_ctype is None else (ctypes.pointer(caller_has_lock_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(caller_has_lock_ctype.value)

    def wait_for_debounce(self, session, maximum_time_ms=hightime.timedelta(milliseconds=5000)):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        maximum_time_ms_ctype = _converters.convert_timedelta_to_milliseconds_int32(maximum_time_ms)  # case S140
        with self._func_lock:
            if self.niSwitch_WaitForDebounce_cfunc is None:
                self.niSwitch_WaitForDebounce_cfunc = self._get_library_function('niSwitch_WaitForDebounce')
                self.niSwitch_WaitForDebounce_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niSwitch_WaitForDebounce_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSwitch_WaitForDebounce_cfunc(vi_ctype, maximum_time_ms_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def wait_for_scan_complete(self, session, maximum_time_ms=hightime.timedelta(milliseconds=5000)):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        maximum_time_ms_ctype = _converters.convert_timedelta_to_milliseconds_int32(maximum_time_ms)  # case S140
        with self._func_lock:
            if self.niSwitch_WaitForScanComplete_cfunc is None:
                self.niSwitch_WaitForScanComplete_cfunc = self._get_library_function('niSwitch_WaitForScanComplete')
                self.niSwitch_WaitForScanComplete_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niSwitch_WaitForScanComplete_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSwitch_WaitForScanComplete_cfunc(vi_ctype, maximum_time_ms_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _close(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niSwitch_close_cfunc is None:
                self.niSwitch_close_cfunc = self._get_library_function('niSwitch_close')
                self.niSwitch_close_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSwitch_close_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSwitch_close_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _error_message(self, session, error_code):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        error_code_ctype = _visatype.ViStatus(error_code)  # case S150
        error_message_ctype = (_visatype.ViChar * 256)()  # case C070
        with self._func_lock:
            if self.niSwitch_error_message_cfunc is None:
                self.niSwitch_error_message_cfunc = self._get_library_function('niSwitch_error_message')
                self.niSwitch_error_message_cfunc.argtypes = [ViSession, ViStatus, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSwitch_error_message_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSwitch_error_message_cfunc(vi_ctype, error_code_ctype, error_message_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=True)
        return error_message_ctype.value.decode(session._encoding)

    def reset(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niSwitch_reset_cfunc is None:
                self.niSwitch_reset_cfunc = self._get_library_function('niSwitch_reset')
                self.niSwitch_reset_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSwitch_reset_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSwitch_reset_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _self_test(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        self_test_result_ctype = _visatype.ViInt16()  # case S220
        self_test_message_ctype = (_visatype.ViChar * 256)()  # case C070
        with self._func_lock:
            if self.niSwitch_self_test_cfunc is None:
                self.niSwitch_self_test_cfunc = self._get_library_function('niSwitch_self_test')
                self.niSwitch_self_test_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt16), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSwitch_self_test_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niSwitch_self_test_cfunc(vi_ctype, None if self_test_result_ctype is None else (ctypes.pointer(self_test_result_ctype)), self_test_message_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(self_test_result_ctype.value), self_test_message_ctype.value.decode(session._encoding)
