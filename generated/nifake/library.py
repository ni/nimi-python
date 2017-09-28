# This file was generated

import ctypes
import threading

from nifake.ctypes_types import *  # noqa: F403,H303
import nifake.python_types


class Library(object):
    '''Library

    Wrapper around driver library.
    Class will setup the correct ctypes information for every function on first call.
    '''

    def __init__(self, library_name, library_type):
        self._func_lock = threading.Lock()
        # We cache the cfunc object from the ctypes.CDLL object
        self.niFake_Abort_cfunc = None
        self.niFake_GetABoolean_cfunc = None
        self.niFake_GetANumber_cfunc = None
        self.niFake_GetAStringOfFixedMaximumSize_cfunc = None
        self.niFake_GetAStringWithSpecifiedMaximumSize_cfunc = None
        self.niFake_GetAttributeViBoolean_cfunc = None
        self.niFake_GetAttributeViInt32_cfunc = None
        self.niFake_GetAttributeViReal64_cfunc = None
        self.niFake_GetAttributeViSession_cfunc = None
        self.niFake_GetAttributeViString_cfunc = None
        self.niFake_GetEnumValue_cfunc = None
        self.niFake_GetError_cfunc = None
        self.niFake_GetErrorMessage_cfunc = None
        self.niFake_InitWithOptions_cfunc = None
        self.niFake_Initiate_cfunc = None
        self.niFake_OneInputFunction_cfunc = None
        self.niFake_Read_cfunc = None
        self.niFake_ReadFromChannel_cfunc = None
        self.niFake_ReadMultiPoint_cfunc = None
        self.niFake_ReturnANumberAndAString_cfunc = None
        self.niFake_SetAttributeViBoolean_cfunc = None
        self.niFake_SetAttributeViInt32_cfunc = None
        self.niFake_SetAttributeViReal64_cfunc = None
        self.niFake_SetAttributeViSession_cfunc = None
        self.niFake_SetAttributeViString_cfunc = None
        self.niFake_SimpleFunction_cfunc = None
        self.niFake_TwoInputFunction_cfunc = None
        self.niFake_close_cfunc = None

        if library_type == 'windll':
            self._library = ctypes.WinDLL(library_name)
        else:  # pragma: no cover
            assert library_type == 'cdll'
            self._library = ctypes.CDLL(library_name)

    def niFake_Abort(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFake_Abort_cfunc is None:
                self.niFake_Abort_cfunc = self._library.niFake_Abort
                self.niFake_Abort_cfunc.argtypes = [ViSession_ctype]  # noqa: F405
                self.niFake_Abort_cfunc.restype = nifake.python_types.ViStatus
        return self.niFake_Abort_cfunc(vi)

    def niFake_GetABoolean(self, vi, a_boolean):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetABoolean_cfunc is None:
                self.niFake_GetABoolean_cfunc = self._library.niFake_GetABoolean
                self.niFake_GetABoolean_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViBoolean_ctype)]  # noqa: F405
                self.niFake_GetABoolean_cfunc.restype = nifake.python_types.ViStatus
        return self.niFake_GetABoolean_cfunc(vi, a_boolean)

    def niFake_GetANumber(self, vi, a_number):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetANumber_cfunc is None:
                self.niFake_GetANumber_cfunc = self._library.niFake_GetANumber
                self.niFake_GetANumber_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViInt16_ctype)]  # noqa: F405
                self.niFake_GetANumber_cfunc.restype = nifake.python_types.ViStatus
        return self.niFake_GetANumber_cfunc(vi, a_number)

    def niFake_GetAStringOfFixedMaximumSize(self, vi, a_string):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetAStringOfFixedMaximumSize_cfunc is None:
                self.niFake_GetAStringOfFixedMaximumSize_cfunc = self._library.niFake_GetAStringOfFixedMaximumSize
                self.niFake_GetAStringOfFixedMaximumSize_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViChar_ctype)]  # noqa: F405
                self.niFake_GetAStringOfFixedMaximumSize_cfunc.restype = nifake.python_types.ViStatus
        return self.niFake_GetAStringOfFixedMaximumSize_cfunc(vi, a_string)

    def niFake_GetAStringWithSpecifiedMaximumSize(self, vi, a_string, buffer_size):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetAStringWithSpecifiedMaximumSize_cfunc is None:
                self.niFake_GetAStringWithSpecifiedMaximumSize_cfunc = self._library.niFake_GetAStringWithSpecifiedMaximumSize
                self.niFake_GetAStringWithSpecifiedMaximumSize_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViChar_ctype), ViInt32_ctype]  # noqa: F405
                self.niFake_GetAStringWithSpecifiedMaximumSize_cfunc.restype = nifake.python_types.ViStatus
        return self.niFake_GetAStringWithSpecifiedMaximumSize_cfunc(vi, a_string, buffer_size)

    def niFake_GetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetAttributeViBoolean_cfunc is None:
                self.niFake_GetAttributeViBoolean_cfunc = self._library.niFake_GetAttributeViBoolean
                self.niFake_GetAttributeViBoolean_cfunc.argtypes = [ViSession_ctype, ViConstString_ctype, ViAttr_ctype, ctypes.POINTER(ViBoolean_ctype)]  # noqa: F405
                self.niFake_GetAttributeViBoolean_cfunc.restype = nifake.python_types.ViStatus
        return self.niFake_GetAttributeViBoolean_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFake_GetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetAttributeViInt32_cfunc is None:
                self.niFake_GetAttributeViInt32_cfunc = self._library.niFake_GetAttributeViInt32
                self.niFake_GetAttributeViInt32_cfunc.argtypes = [ViSession_ctype, ViConstString_ctype, ViAttr_ctype, ctypes.POINTER(ViInt32_ctype)]  # noqa: F405
                self.niFake_GetAttributeViInt32_cfunc.restype = nifake.python_types.ViStatus
        return self.niFake_GetAttributeViInt32_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFake_GetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetAttributeViReal64_cfunc is None:
                self.niFake_GetAttributeViReal64_cfunc = self._library.niFake_GetAttributeViReal64
                self.niFake_GetAttributeViReal64_cfunc.argtypes = [ViSession_ctype, ViConstString_ctype, ViAttr_ctype, ctypes.POINTER(ViReal64_ctype)]  # noqa: F405
                self.niFake_GetAttributeViReal64_cfunc.restype = nifake.python_types.ViStatus
        return self.niFake_GetAttributeViReal64_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFake_GetAttributeViSession(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetAttributeViSession_cfunc is None:
                self.niFake_GetAttributeViSession_cfunc = self._library.niFake_GetAttributeViSession
                self.niFake_GetAttributeViSession_cfunc.argtypes = [ViSession_ctype, ViConstString_ctype, ViAttr_ctype, ctypes.POINTER(ViSession_ctype)]  # noqa: F405
                self.niFake_GetAttributeViSession_cfunc.restype = nifake.python_types.ViStatus
        return self.niFake_GetAttributeViSession_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFake_GetAttributeViString(self, vi, channel_name, attribute_id, buffer_size, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetAttributeViString_cfunc is None:
                self.niFake_GetAttributeViString_cfunc = self._library.niFake_GetAttributeViString
                self.niFake_GetAttributeViString_cfunc.argtypes = [ViSession_ctype, ViConstString_ctype, ViAttr_ctype, ViInt32_ctype, ViString_ctype]  # noqa: F405
                self.niFake_GetAttributeViString_cfunc.restype = nifake.python_types.ViStatus
        return self.niFake_GetAttributeViString_cfunc(vi, channel_name, attribute_id, buffer_size, attribute_value)

    def niFake_GetEnumValue(self, vi, a_quantity, a_turtle):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetEnumValue_cfunc is None:
                self.niFake_GetEnumValue_cfunc = self._library.niFake_GetEnumValue
                self.niFake_GetEnumValue_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViInt32_ctype), ctypes.POINTER(ViInt16_ctype)]  # noqa: F405
                self.niFake_GetEnumValue_cfunc.restype = nifake.python_types.ViStatus
        return self.niFake_GetEnumValue_cfunc(vi, a_quantity, a_turtle)

    def niFake_GetError(self, vi, error_code, buffer_size, description):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetError_cfunc is None:
                self.niFake_GetError_cfunc = self._library.niFake_GetError
                self.niFake_GetError_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViStatus_ctype), ViInt32_ctype, ViString_ctype]  # noqa: F405
                self.niFake_GetError_cfunc.restype = nifake.python_types.ViStatus
        return self.niFake_GetError_cfunc(vi, error_code, buffer_size, description)

    def niFake_GetErrorMessage(self, vi, error_code, buffer_size, error_message):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetErrorMessage_cfunc is None:
                self.niFake_GetErrorMessage_cfunc = self._library.niFake_GetErrorMessage
                self.niFake_GetErrorMessage_cfunc.argtypes = [ViSession_ctype, ViStatus_ctype, ViInt32_ctype, ViString_ctype]  # noqa: F405
                self.niFake_GetErrorMessage_cfunc.restype = nifake.python_types.ViStatus
        return self.niFake_GetErrorMessage_cfunc(vi, error_code, buffer_size, error_message)

    def niFake_InitWithOptions(self, resource_name, id_query, reset_device, option_string, vi):  # noqa: N802
        with self._func_lock:
            if self.niFake_InitWithOptions_cfunc is None:
                self.niFake_InitWithOptions_cfunc = self._library.niFake_InitWithOptions
                self.niFake_InitWithOptions_cfunc.argtypes = [ViString_ctype, ViBoolean_ctype, ViBoolean_ctype, ViString_ctype, ctypes.POINTER(ViSession_ctype)]  # noqa: F405
                self.niFake_InitWithOptions_cfunc.restype = nifake.python_types.ViStatus
        return self.niFake_InitWithOptions_cfunc(resource_name, id_query, reset_device, option_string, vi)

    def niFake_Initiate(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFake_Initiate_cfunc is None:
                self.niFake_Initiate_cfunc = self._library.niFake_Initiate
                self.niFake_Initiate_cfunc.argtypes = [ViSession_ctype]  # noqa: F405
                self.niFake_Initiate_cfunc.restype = nifake.python_types.ViStatus
        return self.niFake_Initiate_cfunc(vi)

    def niFake_OneInputFunction(self, vi, a_number):  # noqa: N802
        with self._func_lock:
            if self.niFake_OneInputFunction_cfunc is None:
                self.niFake_OneInputFunction_cfunc = self._library.niFake_OneInputFunction
                self.niFake_OneInputFunction_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype]  # noqa: F405
                self.niFake_OneInputFunction_cfunc.restype = nifake.python_types.ViStatus
        return self.niFake_OneInputFunction_cfunc(vi, a_number)

    def niFake_Read(self, vi, maximum_time, reading):  # noqa: N802
        with self._func_lock:
            if self.niFake_Read_cfunc is None:
                self.niFake_Read_cfunc = self._library.niFake_Read
                self.niFake_Read_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ctypes.POINTER(ViReal64_ctype)]  # noqa: F405
                self.niFake_Read_cfunc.restype = nifake.python_types.ViStatus
        return self.niFake_Read_cfunc(vi, maximum_time, reading)

    def niFake_ReadFromChannel(self, vi, channel_name, maximum_time, reading):  # noqa: N802
        with self._func_lock:
            if self.niFake_ReadFromChannel_cfunc is None:
                self.niFake_ReadFromChannel_cfunc = self._library.niFake_ReadFromChannel
                self.niFake_ReadFromChannel_cfunc.argtypes = [ViSession_ctype, ViConstString_ctype, ViInt32_ctype, ctypes.POINTER(ViReal64_ctype)]  # noqa: F405
                self.niFake_ReadFromChannel_cfunc.restype = nifake.python_types.ViStatus
        return self.niFake_ReadFromChannel_cfunc(vi, channel_name, maximum_time, reading)

    def niFake_ReadMultiPoint(self, vi, maximum_time, array_size, reading_array, actual_number_of_points):  # noqa: N802
        with self._func_lock:
            if self.niFake_ReadMultiPoint_cfunc is None:
                self.niFake_ReadMultiPoint_cfunc = self._library.niFake_ReadMultiPoint
                self.niFake_ReadMultiPoint_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViInt32_ctype, ctypes.POINTER(ViReal64_ctype), ctypes.POINTER(ViInt32_ctype)]  # noqa: F405
                self.niFake_ReadMultiPoint_cfunc.restype = nifake.python_types.ViStatus
        return self.niFake_ReadMultiPoint_cfunc(vi, maximum_time, array_size, reading_array, actual_number_of_points)

    def niFake_ReturnANumberAndAString(self, vi, a_number, a_string):  # noqa: N802
        with self._func_lock:
            if self.niFake_ReturnANumberAndAString_cfunc is None:
                self.niFake_ReturnANumberAndAString_cfunc = self._library.niFake_ReturnANumberAndAString
                self.niFake_ReturnANumberAndAString_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViInt16_ctype), ctypes.POINTER(ViChar_ctype)]  # noqa: F405
                self.niFake_ReturnANumberAndAString_cfunc.restype = nifake.python_types.ViStatus
        return self.niFake_ReturnANumberAndAString_cfunc(vi, a_number, a_string)

    def niFake_SetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFake_SetAttributeViBoolean_cfunc is None:
                self.niFake_SetAttributeViBoolean_cfunc = self._library.niFake_SetAttributeViBoolean
                self.niFake_SetAttributeViBoolean_cfunc.argtypes = [ViSession_ctype, ViConstString_ctype, ViAttr_ctype, ViBoolean_ctype]  # noqa: F405
                self.niFake_SetAttributeViBoolean_cfunc.restype = nifake.python_types.ViStatus
        return self.niFake_SetAttributeViBoolean_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFake_SetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFake_SetAttributeViInt32_cfunc is None:
                self.niFake_SetAttributeViInt32_cfunc = self._library.niFake_SetAttributeViInt32
                self.niFake_SetAttributeViInt32_cfunc.argtypes = [ViSession_ctype, ViConstString_ctype, ViAttr_ctype, ViInt32_ctype]  # noqa: F405
                self.niFake_SetAttributeViInt32_cfunc.restype = nifake.python_types.ViStatus
        return self.niFake_SetAttributeViInt32_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFake_SetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFake_SetAttributeViReal64_cfunc is None:
                self.niFake_SetAttributeViReal64_cfunc = self._library.niFake_SetAttributeViReal64
                self.niFake_SetAttributeViReal64_cfunc.argtypes = [ViSession_ctype, ViConstString_ctype, ViAttr_ctype, ViReal64_ctype]  # noqa: F405
                self.niFake_SetAttributeViReal64_cfunc.restype = nifake.python_types.ViStatus
        return self.niFake_SetAttributeViReal64_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFake_SetAttributeViSession(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFake_SetAttributeViSession_cfunc is None:
                self.niFake_SetAttributeViSession_cfunc = self._library.niFake_SetAttributeViSession
                self.niFake_SetAttributeViSession_cfunc.argtypes = [ViSession_ctype, ViConstString_ctype, ViAttr_ctype, ViSession_ctype]  # noqa: F405
                self.niFake_SetAttributeViSession_cfunc.restype = nifake.python_types.ViStatus
        return self.niFake_SetAttributeViSession_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFake_SetAttributeViString(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFake_SetAttributeViString_cfunc is None:
                self.niFake_SetAttributeViString_cfunc = self._library.niFake_SetAttributeViString
                self.niFake_SetAttributeViString_cfunc.argtypes = [ViSession_ctype, ViConstString_ctype, ViAttr_ctype, ViString_ctype]  # noqa: F405
                self.niFake_SetAttributeViString_cfunc.restype = nifake.python_types.ViStatus
        return self.niFake_SetAttributeViString_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFake_SimpleFunction(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFake_SimpleFunction_cfunc is None:
                self.niFake_SimpleFunction_cfunc = self._library.niFake_SimpleFunction
                self.niFake_SimpleFunction_cfunc.argtypes = [ViSession_ctype]  # noqa: F405
                self.niFake_SimpleFunction_cfunc.restype = nifake.python_types.ViStatus
        return self.niFake_SimpleFunction_cfunc(vi)

    def niFake_TwoInputFunction(self, vi, a_number, a_string):  # noqa: N802
        with self._func_lock:
            if self.niFake_TwoInputFunction_cfunc is None:
                self.niFake_TwoInputFunction_cfunc = self._library.niFake_TwoInputFunction
                self.niFake_TwoInputFunction_cfunc.argtypes = [ViSession_ctype, ViReal64_ctype, ViChar_ctype]  # noqa: F405
                self.niFake_TwoInputFunction_cfunc.restype = nifake.python_types.ViStatus
        return self.niFake_TwoInputFunction_cfunc(vi, a_number, a_string)

    def niFake_close(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFake_close_cfunc is None:
                self.niFake_close_cfunc = self._library.niFake_close
                self.niFake_close_cfunc.argtypes = [ViSession_ctype]  # noqa: F405
                self.niFake_close_cfunc.restype = nifake.python_types.ViStatus
        return self.niFake_close_cfunc(vi)
