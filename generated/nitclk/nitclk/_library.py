# -*- coding: utf-8 -*-
# This file was generated

import ctypes
import threading

from nitclk._visatype import *  # noqa: F403,H303


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

    def niTClk_ConfigureForHomogeneousTriggers(self, session_count, sessions):  # noqa: N802
        with self._func_lock:
            if self.niTClk_ConfigureForHomogeneousTriggers_cfunc is None:
                self.niTClk_ConfigureForHomogeneousTriggers_cfunc = self._library.niTClk_ConfigureForHomogeneousTriggers
                self.niTClk_ConfigureForHomogeneousTriggers_cfunc.argtypes = [ViUInt32, ctypes.POINTER(ViSession)]  # noqa: F405
                self.niTClk_ConfigureForHomogeneousTriggers_cfunc.restype = ViStatus  # noqa: F405
        return self.niTClk_ConfigureForHomogeneousTriggers_cfunc(session_count, sessions)

    def niTClk_FinishSyncPulseSenderSynchronize(self, session_count, sessions, min_time):  # noqa: N802
        with self._func_lock:
            if self.niTClk_FinishSyncPulseSenderSynchronize_cfunc is None:
                self.niTClk_FinishSyncPulseSenderSynchronize_cfunc = self._library.niTClk_FinishSyncPulseSenderSynchronize
                self.niTClk_FinishSyncPulseSenderSynchronize_cfunc.argtypes = [ViUInt32, ctypes.POINTER(ViSession), ViReal64]  # noqa: F405
                self.niTClk_FinishSyncPulseSenderSynchronize_cfunc.restype = ViStatus  # noqa: F405
        return self.niTClk_FinishSyncPulseSenderSynchronize_cfunc(session_count, sessions, min_time)

    def niTClk_GetAttributeViReal64(self, session, channel_name, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niTClk_GetAttributeViReal64_cfunc is None:
                self.niTClk_GetAttributeViReal64_cfunc = self._library.niTClk_GetAttributeViReal64
                self.niTClk_GetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niTClk_GetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niTClk_GetAttributeViReal64_cfunc(session, channel_name, attribute_id, value)

    def niTClk_GetAttributeViSession(self, session, channel_name, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niTClk_GetAttributeViSession_cfunc is None:
                self.niTClk_GetAttributeViSession_cfunc = self._library.niTClk_GetAttributeViSession
                self.niTClk_GetAttributeViSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViSession)]  # noqa: F405
                self.niTClk_GetAttributeViSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niTClk_GetAttributeViSession_cfunc(session, channel_name, attribute_id, value)

    def niTClk_GetAttributeViString(self, session, channel_name, attribute_id, buf_size, value):  # noqa: N802
        with self._func_lock:
            if self.niTClk_GetAttributeViString_cfunc is None:
                self.niTClk_GetAttributeViString_cfunc = self._library.niTClk_GetAttributeViString
                self.niTClk_GetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niTClk_GetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niTClk_GetAttributeViString_cfunc(session, channel_name, attribute_id, buf_size, value)

    def niTClk_GetExtendedErrorInfo(self, error_string, error_string_size):  # noqa: N802
        with self._func_lock:
            if self.niTClk_GetExtendedErrorInfo_cfunc is None:
                self.niTClk_GetExtendedErrorInfo_cfunc = self._library.niTClk_GetExtendedErrorInfo
                self.niTClk_GetExtendedErrorInfo_cfunc.argtypes = [ctypes.POINTER(ViChar), ViUInt32]  # noqa: F405
                self.niTClk_GetExtendedErrorInfo_cfunc.restype = ViStatus  # noqa: F405
        return self.niTClk_GetExtendedErrorInfo_cfunc(error_string, error_string_size)

    def niTClk_Initiate(self, session_count, sessions):  # noqa: N802
        with self._func_lock:
            if self.niTClk_Initiate_cfunc is None:
                self.niTClk_Initiate_cfunc = self._library.niTClk_Initiate
                self.niTClk_Initiate_cfunc.argtypes = [ViUInt32, ctypes.POINTER(ViSession)]  # noqa: F405
                self.niTClk_Initiate_cfunc.restype = ViStatus  # noqa: F405
        return self.niTClk_Initiate_cfunc(session_count, sessions)

    def niTClk_IsDone(self, session_count, sessions, done):  # noqa: N802
        with self._func_lock:
            if self.niTClk_IsDone_cfunc is None:
                self.niTClk_IsDone_cfunc = self._library.niTClk_IsDone
                self.niTClk_IsDone_cfunc.argtypes = [ViUInt32, ctypes.POINTER(ViSession), ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niTClk_IsDone_cfunc.restype = ViStatus  # noqa: F405
        return self.niTClk_IsDone_cfunc(session_count, sessions, done)

    def niTClk_SetAttributeViReal64(self, session, channel_name, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niTClk_SetAttributeViReal64_cfunc is None:
                self.niTClk_SetAttributeViReal64_cfunc = self._library.niTClk_SetAttributeViReal64
                self.niTClk_SetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViReal64]  # noqa: F405
                self.niTClk_SetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niTClk_SetAttributeViReal64_cfunc(session, channel_name, attribute_id, value)

    def niTClk_SetAttributeViSession(self, session, channel_name, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niTClk_SetAttributeViSession_cfunc is None:
                self.niTClk_SetAttributeViSession_cfunc = self._library.niTClk_SetAttributeViSession
                self.niTClk_SetAttributeViSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViSession]  # noqa: F405
                self.niTClk_SetAttributeViSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niTClk_SetAttributeViSession_cfunc(session, channel_name, attribute_id, value)

    def niTClk_SetAttributeViString(self, session, channel_name, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niTClk_SetAttributeViString_cfunc is None:
                self.niTClk_SetAttributeViString_cfunc = self._library.niTClk_SetAttributeViString
                self.niTClk_SetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niTClk_SetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niTClk_SetAttributeViString_cfunc(session, channel_name, attribute_id, value)

    def niTClk_SetupForSyncPulseSenderSynchronize(self, session_count, sessions, min_time):  # noqa: N802
        with self._func_lock:
            if self.niTClk_SetupForSyncPulseSenderSynchronize_cfunc is None:
                self.niTClk_SetupForSyncPulseSenderSynchronize_cfunc = self._library.niTClk_SetupForSyncPulseSenderSynchronize
                self.niTClk_SetupForSyncPulseSenderSynchronize_cfunc.argtypes = [ViUInt32, ctypes.POINTER(ViSession), ViReal64]  # noqa: F405
                self.niTClk_SetupForSyncPulseSenderSynchronize_cfunc.restype = ViStatus  # noqa: F405
        return self.niTClk_SetupForSyncPulseSenderSynchronize_cfunc(session_count, sessions, min_time)

    def niTClk_Synchronize(self, session_count, sessions, min_tclk_period):  # noqa: N802
        with self._func_lock:
            if self.niTClk_Synchronize_cfunc is None:
                self.niTClk_Synchronize_cfunc = self._library.niTClk_Synchronize
                self.niTClk_Synchronize_cfunc.argtypes = [ViUInt32, ctypes.POINTER(ViSession), ViReal64]  # noqa: F405
                self.niTClk_Synchronize_cfunc.restype = ViStatus  # noqa: F405
        return self.niTClk_Synchronize_cfunc(session_count, sessions, min_tclk_period)

    def niTClk_SynchronizeToSyncPulseSender(self, session_count, sessions, min_time):  # noqa: N802
        with self._func_lock:
            if self.niTClk_SynchronizeToSyncPulseSender_cfunc is None:
                self.niTClk_SynchronizeToSyncPulseSender_cfunc = self._library.niTClk_SynchronizeToSyncPulseSender
                self.niTClk_SynchronizeToSyncPulseSender_cfunc.argtypes = [ViUInt32, ctypes.POINTER(ViSession), ViReal64]  # noqa: F405
                self.niTClk_SynchronizeToSyncPulseSender_cfunc.restype = ViStatus  # noqa: F405
        return self.niTClk_SynchronizeToSyncPulseSender_cfunc(session_count, sessions, min_time)

    def niTClk_WaitUntilDone(self, session_count, sessions, timeout):  # noqa: N802
        with self._func_lock:
            if self.niTClk_WaitUntilDone_cfunc is None:
                self.niTClk_WaitUntilDone_cfunc = self._library.niTClk_WaitUntilDone
                self.niTClk_WaitUntilDone_cfunc.argtypes = [ViUInt32, ctypes.POINTER(ViSession), ViReal64]  # noqa: F405
                self.niTClk_WaitUntilDone_cfunc.restype = ViStatus  # noqa: F405
        return self.niTClk_WaitUntilDone_cfunc(session_count, sessions, timeout)
