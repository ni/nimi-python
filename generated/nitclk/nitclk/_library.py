# -*- coding: utf-8 -*-
# This file was generated

import array  # noqa: F401
import ctypes
import nitclk._converters as _converters
import nitclk._visatype as _visatype
import nitclk.errors as errors
import threading

from nitclk._visatype import *  # noqa: F403,H303


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
        self.niTClk_ConfigureForHomogeneousTriggers_cfunc = None
        self.niTClk_FinishSyncPulseSenderSynchronize_cfunc = None
        self.niTClk_GetAttributeViReal64_cfunc = None
        self.niTClk_GetAttributeViSession_cfunc = None
        self.niTClk_GetAttributeViString_cfunc = None
        self.niTClk_GetExtendedErrorInfo_cfunc = None
        self.niTClk_Initiate_cfunc = None
        self.niTClk_IsDone_cfunc = None
        self.niTClk_SetAttributeViReal64_cfunc = None
        self.niTClk_SetAttributeViSession_cfunc = None
        self.niTClk_SetAttributeViString_cfunc = None
        self.niTClk_SetupForSyncPulseSenderSynchronize_cfunc = None
        self.niTClk_Synchronize_cfunc = None
        self.niTClk_SynchronizeToSyncPulseSender_cfunc = None
        self.niTClk_WaitUntilDone_cfunc = None

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
            '''
            It is expected for _get_error to raise when the session is invalid
            (IVI spec requires GetError to fail).
            Use _error_message instead. It doesn't require a session.
            '''
            error_string = self._get_extended_error_info(session)
            return error_string
        except errors.Error:
            return "Failed to retrieve error description."

    def configure_for_homogeneous_triggers(self, session, sessions):  # noqa: N802
        session_count_ctype = _visatype.ViUInt32(0 if sessions is None else len(sessions))  # case S160
        sessions_converted = _converters.convert_to_nitclk_session_number_list(sessions)  # case B520
        sessions_ctype = get_ctypes_pointer_for_buffer(value=sessions_converted, library_type=_visatype.ViSession)  # case B520
        with self._func_lock:
            if self.niTClk_ConfigureForHomogeneousTriggers_cfunc is None:
                self.niTClk_ConfigureForHomogeneousTriggers_cfunc = self._get_library_function('niTClk_ConfigureForHomogeneousTriggers')
                self.niTClk_ConfigureForHomogeneousTriggers_cfunc.argtypes = [ViUInt32, ctypes.POINTER(ViSession)]  # noqa: F405
                self.niTClk_ConfigureForHomogeneousTriggers_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niTClk_ConfigureForHomogeneousTriggers_cfunc(session_count_ctype, sessions_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def finish_sync_pulse_sender_synchronize(self, session, sessions, min_time):  # noqa: N802
        session_count_ctype = _visatype.ViUInt32(0 if sessions is None else len(sessions))  # case S160
        sessions_converted = _converters.convert_to_nitclk_session_number_list(sessions)  # case B520
        sessions_ctype = get_ctypes_pointer_for_buffer(value=sessions_converted, library_type=_visatype.ViSession)  # case B520
        min_time_ctype = _converters.convert_timedelta_to_seconds_real64(min_time)  # case S140
        with self._func_lock:
            if self.niTClk_FinishSyncPulseSenderSynchronize_cfunc is None:
                self.niTClk_FinishSyncPulseSenderSynchronize_cfunc = self._get_library_function('niTClk_FinishSyncPulseSenderSynchronize')
                self.niTClk_FinishSyncPulseSenderSynchronize_cfunc.argtypes = [ViUInt32, ctypes.POINTER(ViSession), ViReal64]  # noqa: F405
                self.niTClk_FinishSyncPulseSenderSynchronize_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niTClk_FinishSyncPulseSenderSynchronize_cfunc(session_count_ctype, sessions_ctype, min_time_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _get_attribute_vi_real64(self, session, channel_name, attribute_id):  # noqa: N802
        session_ctype = _visatype.ViSession(session._session_number)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViReal64()  # case S220
        with self._func_lock:
            if self.niTClk_GetAttributeViReal64_cfunc is None:
                self.niTClk_GetAttributeViReal64_cfunc = self._get_library_function('niTClk_GetAttributeViReal64')
                self.niTClk_GetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niTClk_GetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niTClk_GetAttributeViReal64_cfunc(session_ctype, channel_name_ctype, attribute_id_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return float(value_ctype.value)

    def _get_attribute_vi_session(self, session, channel_name, attribute_id):  # noqa: N802
        session_ctype = _visatype.ViSession(session._session_number)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViSession()  # case S220
        with self._func_lock:
            if self.niTClk_GetAttributeViSession_cfunc is None:
                self.niTClk_GetAttributeViSession_cfunc = self._get_library_function('niTClk_GetAttributeViSession')
                self.niTClk_GetAttributeViSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViSession)]  # noqa: F405
                self.niTClk_GetAttributeViSession_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niTClk_GetAttributeViSession_cfunc(session_ctype, channel_name_ctype, attribute_id_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(value_ctype.value)

    def _get_attribute_vi_string(self, session, channel_name, attribute_id):  # noqa: N802
        session_ctype = _visatype.ViSession(session._session_number)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        buf_size_ctype = _visatype.ViInt32()  # case S170
        value_ctype = None  # case C050
        with self._func_lock:
            if self.niTClk_GetAttributeViString_cfunc is None:
                self.niTClk_GetAttributeViString_cfunc = self._get_library_function('niTClk_GetAttributeViString')
                self.niTClk_GetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niTClk_GetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niTClk_GetAttributeViString_cfunc(session_ctype, channel_name_ctype, attribute_id_ctype, buf_size_ctype, value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=False)
        buf_size_ctype = _visatype.ViInt32(error_code)  # case S180
        value_ctype = (_visatype.ViChar * buf_size_ctype.value)()  # case C060
        error_code = self.niTClk_GetAttributeViString_cfunc(session_ctype, channel_name_ctype, attribute_id_ctype, buf_size_ctype, value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return value_ctype.value.decode(session._encoding)

    def _get_extended_error_info(self, session):  # noqa: N802
        error_string_ctype = None  # case C050
        error_string_size_ctype = _visatype.ViUInt32()  # case S170
        with self._func_lock:
            if self.niTClk_GetExtendedErrorInfo_cfunc is None:
                self.niTClk_GetExtendedErrorInfo_cfunc = self._get_library_function('niTClk_GetExtendedErrorInfo')
                self.niTClk_GetExtendedErrorInfo_cfunc.argtypes = [ctypes.POINTER(ViChar), ViUInt32]  # noqa: F405
                self.niTClk_GetExtendedErrorInfo_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niTClk_GetExtendedErrorInfo_cfunc(error_string_ctype, error_string_size_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=True)
        error_string_size_ctype = _visatype.ViUInt32(error_code)  # case S180
        error_string_ctype = (_visatype.ViChar * error_string_size_ctype.value)()  # case C060
        error_code = self.niTClk_GetExtendedErrorInfo_cfunc(error_string_ctype, error_string_size_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=True)
        return error_string_ctype.value.decode(session._encoding)

    def initiate(self, session, sessions):  # noqa: N802
        session_count_ctype = _visatype.ViUInt32(0 if sessions is None else len(sessions))  # case S160
        sessions_converted = _converters.convert_to_nitclk_session_number_list(sessions)  # case B520
        sessions_ctype = get_ctypes_pointer_for_buffer(value=sessions_converted, library_type=_visatype.ViSession)  # case B520
        with self._func_lock:
            if self.niTClk_Initiate_cfunc is None:
                self.niTClk_Initiate_cfunc = self._get_library_function('niTClk_Initiate')
                self.niTClk_Initiate_cfunc.argtypes = [ViUInt32, ctypes.POINTER(ViSession)]  # noqa: F405
                self.niTClk_Initiate_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niTClk_Initiate_cfunc(session_count_ctype, sessions_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def is_done(self, session, sessions):  # noqa: N802
        session_count_ctype = _visatype.ViUInt32(0 if sessions is None else len(sessions))  # case S160
        sessions_converted = _converters.convert_to_nitclk_session_number_list(sessions)  # case B520
        sessions_ctype = get_ctypes_pointer_for_buffer(value=sessions_converted, library_type=_visatype.ViSession)  # case B520
        done_ctype = _visatype.ViBoolean()  # case S220
        with self._func_lock:
            if self.niTClk_IsDone_cfunc is None:
                self.niTClk_IsDone_cfunc = self._get_library_function('niTClk_IsDone')
                self.niTClk_IsDone_cfunc.argtypes = [ViUInt32, ctypes.POINTER(ViSession), ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niTClk_IsDone_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niTClk_IsDone_cfunc(session_count_ctype, sessions_ctype, None if done_ctype is None else (ctypes.pointer(done_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(done_ctype.value)

    def _set_attribute_vi_real64(self, session, channel_name, attribute_id, value):  # noqa: N802
        session_ctype = _visatype.ViSession(session._session_number)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViReal64(value)  # case S150
        with self._func_lock:
            if self.niTClk_SetAttributeViReal64_cfunc is None:
                self.niTClk_SetAttributeViReal64_cfunc = self._get_library_function('niTClk_SetAttributeViReal64')
                self.niTClk_SetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViReal64]  # noqa: F405
                self.niTClk_SetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niTClk_SetAttributeViReal64_cfunc(session_ctype, channel_name_ctype, attribute_id_ctype, value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_session(self, session, channel_name, attribute_id, value):  # noqa: N802
        session_ctype = _visatype.ViSession(session._session_number)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViSession(value)  # case S150
        with self._func_lock:
            if self.niTClk_SetAttributeViSession_cfunc is None:
                self.niTClk_SetAttributeViSession_cfunc = self._get_library_function('niTClk_SetAttributeViSession')
                self.niTClk_SetAttributeViSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViSession]  # noqa: F405
                self.niTClk_SetAttributeViSession_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niTClk_SetAttributeViSession_cfunc(session_ctype, channel_name_ctype, attribute_id_ctype, value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_string(self, session, channel_name, attribute_id, value):  # noqa: N802
        session_ctype = _visatype.ViSession(session._session_number)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = ctypes.create_string_buffer(value.encode(session._encoding))  # case C020
        with self._func_lock:
            if self.niTClk_SetAttributeViString_cfunc is None:
                self.niTClk_SetAttributeViString_cfunc = self._get_library_function('niTClk_SetAttributeViString')
                self.niTClk_SetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niTClk_SetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niTClk_SetAttributeViString_cfunc(session_ctype, channel_name_ctype, attribute_id_ctype, value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def setup_for_sync_pulse_sender_synchronize(self, session, sessions, min_time):  # noqa: N802
        session_count_ctype = _visatype.ViUInt32(0 if sessions is None else len(sessions))  # case S160
        sessions_converted = _converters.convert_to_nitclk_session_number_list(sessions)  # case B520
        sessions_ctype = get_ctypes_pointer_for_buffer(value=sessions_converted, library_type=_visatype.ViSession)  # case B520
        min_time_ctype = _converters.convert_timedelta_to_seconds_real64(min_time)  # case S140
        with self._func_lock:
            if self.niTClk_SetupForSyncPulseSenderSynchronize_cfunc is None:
                self.niTClk_SetupForSyncPulseSenderSynchronize_cfunc = self._get_library_function('niTClk_SetupForSyncPulseSenderSynchronize')
                self.niTClk_SetupForSyncPulseSenderSynchronize_cfunc.argtypes = [ViUInt32, ctypes.POINTER(ViSession), ViReal64]  # noqa: F405
                self.niTClk_SetupForSyncPulseSenderSynchronize_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niTClk_SetupForSyncPulseSenderSynchronize_cfunc(session_count_ctype, sessions_ctype, min_time_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def synchronize(self, session, sessions, min_tclk_period):  # noqa: N802
        session_count_ctype = _visatype.ViUInt32(0 if sessions is None else len(sessions))  # case S160
        sessions_converted = _converters.convert_to_nitclk_session_number_list(sessions)  # case B520
        sessions_ctype = get_ctypes_pointer_for_buffer(value=sessions_converted, library_type=_visatype.ViSession)  # case B520
        min_tclk_period_ctype = _converters.convert_timedelta_to_seconds_real64(min_tclk_period)  # case S140
        with self._func_lock:
            if self.niTClk_Synchronize_cfunc is None:
                self.niTClk_Synchronize_cfunc = self._get_library_function('niTClk_Synchronize')
                self.niTClk_Synchronize_cfunc.argtypes = [ViUInt32, ctypes.POINTER(ViSession), ViReal64]  # noqa: F405
                self.niTClk_Synchronize_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niTClk_Synchronize_cfunc(session_count_ctype, sessions_ctype, min_tclk_period_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def synchronize_to_sync_pulse_sender(self, session, sessions, min_time):  # noqa: N802
        session_count_ctype = _visatype.ViUInt32(0 if sessions is None else len(sessions))  # case S160
        sessions_converted = _converters.convert_to_nitclk_session_number_list(sessions)  # case B520
        sessions_ctype = get_ctypes_pointer_for_buffer(value=sessions_converted, library_type=_visatype.ViSession)  # case B520
        min_time_ctype = _converters.convert_timedelta_to_seconds_real64(min_time)  # case S140
        with self._func_lock:
            if self.niTClk_SynchronizeToSyncPulseSender_cfunc is None:
                self.niTClk_SynchronizeToSyncPulseSender_cfunc = self._get_library_function('niTClk_SynchronizeToSyncPulseSender')
                self.niTClk_SynchronizeToSyncPulseSender_cfunc.argtypes = [ViUInt32, ctypes.POINTER(ViSession), ViReal64]  # noqa: F405
                self.niTClk_SynchronizeToSyncPulseSender_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niTClk_SynchronizeToSyncPulseSender_cfunc(session_count_ctype, sessions_ctype, min_time_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def wait_until_done(self, session, sessions, timeout):  # noqa: N802
        session_count_ctype = _visatype.ViUInt32(0 if sessions is None else len(sessions))  # case S160
        sessions_converted = _converters.convert_to_nitclk_session_number_list(sessions)  # case B520
        sessions_ctype = get_ctypes_pointer_for_buffer(value=sessions_converted, library_type=_visatype.ViSession)  # case B520
        timeout_ctype = _converters.convert_timedelta_to_seconds_real64(timeout)  # case S140
        with self._func_lock:
            if self.niTClk_WaitUntilDone_cfunc is None:
                self.niTClk_WaitUntilDone_cfunc = self._get_library_function('niTClk_WaitUntilDone')
                self.niTClk_WaitUntilDone_cfunc.argtypes = [ViUInt32, ctypes.POINTER(ViSession), ViReal64]  # noqa: F405
                self.niTClk_WaitUntilDone_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niTClk_WaitUntilDone_cfunc(session_count_ctype, sessions_ctype, timeout_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return
