# -*- coding: utf-8 -*-
# This file was generated

import ctypes
import threading

from nifake._visatype import *  # noqa: F403,H303

import nifake.custom_struct as custom_struct  # noqa: F401


class Library(object):
    '''Library

    Wrapper around driver library.
    Class will setup the correct ctypes information for every function on first call.
    '''

    def __init__(self, ctypes_library):
        self._func_lock = threading.Lock()
        self._library = ctypes_library
        # We cache the cfunc object from the ctypes.CDLL object
        self.niFake_Abort_cfunc = None
        self.niFake_AcceptListOfDurationsInSeconds_cfunc = None
        self.niFake_BoolArrayOutputFunction_cfunc = None
        self.niFake_DoubleAllTheNums_cfunc = None
        self.niFake_EnumArrayOutputFunction_cfunc = None
        self.niFake_EnumInputFunctionWithDefaults_cfunc = None
        self.niFake_ExportAttributeConfigurationBuffer_cfunc = None
        self.niFake_FetchWaveform_cfunc = None
        self.niFake_GetABoolean_cfunc = None
        self.niFake_GetANumber_cfunc = None
        self.niFake_GetAStringOfFixedMaximumSize_cfunc = None
        self.niFake_GetAStringUsingPythonCode_cfunc = None
        self.niFake_GetAnIviDanceString_cfunc = None
        self.niFake_GetAnIviDanceWithATwistString_cfunc = None
        self.niFake_GetArrayForPythonCodeCustomType_cfunc = None
        self.niFake_GetArrayForPythonCodeDouble_cfunc = None
        self.niFake_GetArraySizeForPythonCode_cfunc = None
        self.niFake_GetArrayUsingIviDance_cfunc = None
        self.niFake_GetAttributeViBoolean_cfunc = None
        self.niFake_GetAttributeViInt32_cfunc = None
        self.niFake_GetAttributeViInt64_cfunc = None
        self.niFake_GetAttributeViReal64_cfunc = None
        self.niFake_GetAttributeViString_cfunc = None
        self.niFake_GetCalDateAndTime_cfunc = None
        self.niFake_GetCalInterval_cfunc = None
        self.niFake_GetCustomType_cfunc = None
        self.niFake_GetCustomTypeArray_cfunc = None
        self.niFake_GetEnumValue_cfunc = None
        self.niFake_GetError_cfunc = None
        self.niFake_ImportAttributeConfigurationBuffer_cfunc = None
        self.niFake_InitWithOptions_cfunc = None
        self.niFake_Initiate_cfunc = None
        self.niFake_LockSession_cfunc = None
        self.niFake_MultipleArrayTypes_cfunc = None
        self.niFake_MultipleArraysSameSize_cfunc = None
        self.niFake_OneInputFunction_cfunc = None
        self.niFake_ParametersAreMultipleTypes_cfunc = None
        self.niFake_PoorlyNamedSimpleFunction_cfunc = None
        self.niFake_Read_cfunc = None
        self.niFake_ReadFromChannel_cfunc = None
        self.niFake_ReturnANumberAndAString_cfunc = None
        self.niFake_ReturnDurationInSeconds_cfunc = None
        self.niFake_ReturnListOfDurationsInSeconds_cfunc = None
        self.niFake_ReturnMultipleTypes_cfunc = None
        self.niFake_SetAttributeViBoolean_cfunc = None
        self.niFake_SetAttributeViInt32_cfunc = None
        self.niFake_SetAttributeViInt64_cfunc = None
        self.niFake_SetAttributeViReal64_cfunc = None
        self.niFake_SetAttributeViString_cfunc = None
        self.niFake_SetCustomType_cfunc = None
        self.niFake_SetCustomTypeArray_cfunc = None
        self.niFake_StringValuedEnumInputFunctionWithDefaults_cfunc = None
        self.niFake_TwoInputFunction_cfunc = None
        self.niFake_UnlockSession_cfunc = None
        self.niFake_Use64BitNumber_cfunc = None
        self.niFake_WriteWaveform_cfunc = None
        self.niFake_close_cfunc = None
        self.niFake_error_message_cfunc = None
        self.niFake_self_test_cfunc = None

    def niFake_Abort(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFake_Abort_cfunc is None:
                try:
                    self.niFake_Abort_cfunc = self._library.niFake_Abort
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_Abort_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFake_Abort_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_Abort_cfunc(vi)

    def niFake_AcceptListOfDurationsInSeconds(self, vi, count, delays):  # noqa: N802
        with self._func_lock:
            if self.niFake_AcceptListOfDurationsInSeconds_cfunc is None:
                try:
                    self.niFake_AcceptListOfDurationsInSeconds_cfunc = self._library.niFake_AcceptListOfDurationsInSeconds
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_AcceptListOfDurationsInSeconds_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFake_AcceptListOfDurationsInSeconds_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_AcceptListOfDurationsInSeconds_cfunc(vi, count, delays)

    def niFake_BoolArrayOutputFunction(self, vi, number_of_elements, an_array):  # noqa: N802
        with self._func_lock:
            if self.niFake_BoolArrayOutputFunction_cfunc is None:
                try:
                    self.niFake_BoolArrayOutputFunction_cfunc = self._library.niFake_BoolArrayOutputFunction
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_BoolArrayOutputFunction_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niFake_BoolArrayOutputFunction_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_BoolArrayOutputFunction_cfunc(vi, number_of_elements, an_array)

    def niFake_DoubleAllTheNums(self, vi, number_count, numbers):  # noqa: N802
        with self._func_lock:
            if self.niFake_DoubleAllTheNums_cfunc is None:
                try:
                    self.niFake_DoubleAllTheNums_cfunc = self._library.niFake_DoubleAllTheNums
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_DoubleAllTheNums_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFake_DoubleAllTheNums_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_DoubleAllTheNums_cfunc(vi, number_count, numbers)

    def niFake_EnumArrayOutputFunction(self, vi, number_of_elements, an_array):  # noqa: N802
        with self._func_lock:
            if self.niFake_EnumArrayOutputFunction_cfunc is None:
                try:
                    self.niFake_EnumArrayOutputFunction_cfunc = self._library.niFake_EnumArrayOutputFunction
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_EnumArrayOutputFunction_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt16)]  # noqa: F405
                self.niFake_EnumArrayOutputFunction_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_EnumArrayOutputFunction_cfunc(vi, number_of_elements, an_array)

    def niFake_EnumInputFunctionWithDefaults(self, vi, a_turtle):  # noqa: N802
        with self._func_lock:
            if self.niFake_EnumInputFunctionWithDefaults_cfunc is None:
                try:
                    self.niFake_EnumInputFunctionWithDefaults_cfunc = self._library.niFake_EnumInputFunctionWithDefaults
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_EnumInputFunctionWithDefaults_cfunc.argtypes = [ViSession, ViInt16]  # noqa: F405
                self.niFake_EnumInputFunctionWithDefaults_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_EnumInputFunctionWithDefaults_cfunc(vi, a_turtle)

    def niFake_ExportAttributeConfigurationBuffer(self, vi, size_in_bytes, configuration):  # noqa: N802
        with self._func_lock:
            if self.niFake_ExportAttributeConfigurationBuffer_cfunc is None:
                try:
                    self.niFake_ExportAttributeConfigurationBuffer_cfunc = self._library.niFake_ExportAttributeConfigurationBuffer
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_ExportAttributeConfigurationBuffer_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt8)]  # noqa: F405
                self.niFake_ExportAttributeConfigurationBuffer_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_ExportAttributeConfigurationBuffer_cfunc(vi, size_in_bytes, configuration)

    def niFake_FetchWaveform(self, vi, number_of_samples, waveform_data, actual_number_of_samples):  # noqa: N802
        with self._func_lock:
            if self.niFake_FetchWaveform_cfunc is None:
                try:
                    self.niFake_FetchWaveform_cfunc = self._library.niFake_FetchWaveform
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_FetchWaveform_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFake_FetchWaveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_FetchWaveform_cfunc(vi, number_of_samples, waveform_data, actual_number_of_samples)

    def niFake_GetABoolean(self, vi, a_boolean):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetABoolean_cfunc is None:
                try:
                    self.niFake_GetABoolean_cfunc = self._library.niFake_GetABoolean
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_GetABoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niFake_GetABoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_GetABoolean_cfunc(vi, a_boolean)

    def niFake_GetANumber(self, vi, a_number):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetANumber_cfunc is None:
                try:
                    self.niFake_GetANumber_cfunc = self._library.niFake_GetANumber
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_GetANumber_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt16)]  # noqa: F405
                self.niFake_GetANumber_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_GetANumber_cfunc(vi, a_number)

    def niFake_GetAStringOfFixedMaximumSize(self, vi, a_string):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetAStringOfFixedMaximumSize_cfunc is None:
                try:
                    self.niFake_GetAStringOfFixedMaximumSize_cfunc = self._library.niFake_GetAStringOfFixedMaximumSize
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_GetAStringOfFixedMaximumSize_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFake_GetAStringOfFixedMaximumSize_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_GetAStringOfFixedMaximumSize_cfunc(vi, a_string)

    def niFake_GetAStringUsingPythonCode(self, vi, a_number, a_string):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetAStringUsingPythonCode_cfunc is None:
                try:
                    self.niFake_GetAStringUsingPythonCode_cfunc = self._library.niFake_GetAStringUsingPythonCode
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_GetAStringUsingPythonCode_cfunc.argtypes = [ViSession, ViInt16, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFake_GetAStringUsingPythonCode_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_GetAStringUsingPythonCode_cfunc(vi, a_number, a_string)

    def niFake_GetAnIviDanceString(self, vi, buffer_size, a_string):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetAnIviDanceString_cfunc is None:
                try:
                    self.niFake_GetAnIviDanceString_cfunc = self._library.niFake_GetAnIviDanceString
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_GetAnIviDanceString_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFake_GetAnIviDanceString_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_GetAnIviDanceString_cfunc(vi, buffer_size, a_string)

    def niFake_GetAnIviDanceWithATwistString(self, vi, buffer_size, a_string, actual_size):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetAnIviDanceWithATwistString_cfunc is None:
                try:
                    self.niFake_GetAnIviDanceWithATwistString_cfunc = self._library.niFake_GetAnIviDanceWithATwistString
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_GetAnIviDanceWithATwistString_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViChar), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFake_GetAnIviDanceWithATwistString_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_GetAnIviDanceWithATwistString_cfunc(vi, buffer_size, a_string, actual_size)

    def niFake_GetArrayForPythonCodeCustomType(self, vi, number_of_elements, array_out):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetArrayForPythonCodeCustomType_cfunc is None:
                try:
                    self.niFake_GetArrayForPythonCodeCustomType_cfunc = self._library.niFake_GetArrayForPythonCodeCustomType
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_GetArrayForPythonCodeCustomType_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(custom_struct.struct_CustomStruct)]  # noqa: F405
                self.niFake_GetArrayForPythonCodeCustomType_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_GetArrayForPythonCodeCustomType_cfunc(vi, number_of_elements, array_out)

    def niFake_GetArrayForPythonCodeDouble(self, vi, number_of_elements, array_out):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetArrayForPythonCodeDouble_cfunc is None:
                try:
                    self.niFake_GetArrayForPythonCodeDouble_cfunc = self._library.niFake_GetArrayForPythonCodeDouble
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_GetArrayForPythonCodeDouble_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFake_GetArrayForPythonCodeDouble_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_GetArrayForPythonCodeDouble_cfunc(vi, number_of_elements, array_out)

    def niFake_GetArraySizeForPythonCode(self, vi, size_out):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetArraySizeForPythonCode_cfunc is None:
                try:
                    self.niFake_GetArraySizeForPythonCode_cfunc = self._library.niFake_GetArraySizeForPythonCode
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_GetArraySizeForPythonCode_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFake_GetArraySizeForPythonCode_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_GetArraySizeForPythonCode_cfunc(vi, size_out)

    def niFake_GetArrayUsingIviDance(self, vi, array_size, array_out):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetArrayUsingIviDance_cfunc is None:
                try:
                    self.niFake_GetArrayUsingIviDance_cfunc = self._library.niFake_GetArrayUsingIviDance
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_GetArrayUsingIviDance_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFake_GetArrayUsingIviDance_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_GetArrayUsingIviDance_cfunc(vi, array_size, array_out)

    def niFake_GetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetAttributeViBoolean_cfunc is None:
                try:
                    self.niFake_GetAttributeViBoolean_cfunc = self._library.niFake_GetAttributeViBoolean
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_GetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niFake_GetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_GetAttributeViBoolean_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFake_GetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetAttributeViInt32_cfunc is None:
                try:
                    self.niFake_GetAttributeViInt32_cfunc = self._library.niFake_GetAttributeViInt32
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_GetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFake_GetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_GetAttributeViInt32_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFake_GetAttributeViInt64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetAttributeViInt64_cfunc is None:
                try:
                    self.niFake_GetAttributeViInt64_cfunc = self._library.niFake_GetAttributeViInt64
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_GetAttributeViInt64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViInt64)]  # noqa: F405
                self.niFake_GetAttributeViInt64_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_GetAttributeViInt64_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFake_GetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetAttributeViReal64_cfunc is None:
                try:
                    self.niFake_GetAttributeViReal64_cfunc = self._library.niFake_GetAttributeViReal64
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_GetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFake_GetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_GetAttributeViReal64_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFake_GetAttributeViString(self, vi, channel_name, attribute_id, buffer_size, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetAttributeViString_cfunc is None:
                try:
                    self.niFake_GetAttributeViString_cfunc = self._library.niFake_GetAttributeViString
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_GetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFake_GetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_GetAttributeViString_cfunc(vi, channel_name, attribute_id, buffer_size, attribute_value)

    def niFake_GetCalDateAndTime(self, vi, cal_type, month, day, year, hour, minute):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetCalDateAndTime_cfunc is None:
                try:
                    self.niFake_GetCalDateAndTime_cfunc = self._library.niFake_GetCalDateAndTime
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_GetCalDateAndTime_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFake_GetCalDateAndTime_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_GetCalDateAndTime_cfunc(vi, cal_type, month, day, year, hour, minute)

    def niFake_GetCalInterval(self, vi, months):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetCalInterval_cfunc is None:
                try:
                    self.niFake_GetCalInterval_cfunc = self._library.niFake_GetCalInterval
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_GetCalInterval_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFake_GetCalInterval_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_GetCalInterval_cfunc(vi, months)

    def niFake_GetCustomType(self, vi, cs):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetCustomType_cfunc is None:
                try:
                    self.niFake_GetCustomType_cfunc = self._library.niFake_GetCustomType
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_GetCustomType_cfunc.argtypes = [ViSession, ctypes.POINTER(custom_struct.struct_CustomStruct)]  # noqa: F405
                self.niFake_GetCustomType_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_GetCustomType_cfunc(vi, cs)

    def niFake_GetCustomTypeArray(self, vi, number_of_elements, cs):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetCustomTypeArray_cfunc is None:
                try:
                    self.niFake_GetCustomTypeArray_cfunc = self._library.niFake_GetCustomTypeArray
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_GetCustomTypeArray_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(custom_struct.struct_CustomStruct)]  # noqa: F405
                self.niFake_GetCustomTypeArray_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_GetCustomTypeArray_cfunc(vi, number_of_elements, cs)

    def niFake_GetEnumValue(self, vi, a_quantity, a_turtle):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetEnumValue_cfunc is None:
                try:
                    self.niFake_GetEnumValue_cfunc = self._library.niFake_GetEnumValue
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_GetEnumValue_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt16)]  # noqa: F405
                self.niFake_GetEnumValue_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_GetEnumValue_cfunc(vi, a_quantity, a_turtle)

    def niFake_GetError(self, vi, error_code, buffer_size, description):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetError_cfunc is None:
                try:
                    self.niFake_GetError_cfunc = self._library.niFake_GetError
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_GetError_cfunc.argtypes = [ViSession, ctypes.POINTER(ViStatus), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFake_GetError_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_GetError_cfunc(vi, error_code, buffer_size, description)

    def niFake_ImportAttributeConfigurationBuffer(self, vi, size_in_bytes, configuration):  # noqa: N802
        with self._func_lock:
            if self.niFake_ImportAttributeConfigurationBuffer_cfunc is None:
                try:
                    self.niFake_ImportAttributeConfigurationBuffer_cfunc = self._library.niFake_ImportAttributeConfigurationBuffer
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_ImportAttributeConfigurationBuffer_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt8)]  # noqa: F405
                self.niFake_ImportAttributeConfigurationBuffer_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_ImportAttributeConfigurationBuffer_cfunc(vi, size_in_bytes, configuration)

    def niFake_InitWithOptions(self, resource_name, id_query, reset_device, option_string, vi):  # noqa: N802
        with self._func_lock:
            if self.niFake_InitWithOptions_cfunc is None:
                try:
                    self.niFake_InitWithOptions_cfunc = self._library.niFake_InitWithOptions
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_InitWithOptions_cfunc.argtypes = [ctypes.POINTER(ViChar), ViBoolean, ViBoolean, ctypes.POINTER(ViChar), ctypes.POINTER(ViSession)]  # noqa: F405
                self.niFake_InitWithOptions_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_InitWithOptions_cfunc(resource_name, id_query, reset_device, option_string, vi)

    def niFake_Initiate(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFake_Initiate_cfunc is None:
                try:
                    self.niFake_Initiate_cfunc = self._library.niFake_Initiate
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_Initiate_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFake_Initiate_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_Initiate_cfunc(vi)

    def niFake_LockSession(self, vi, caller_has_lock):  # noqa: N802
        with self._func_lock:
            if self.niFake_LockSession_cfunc is None:
                try:
                    self.niFake_LockSession_cfunc = self._library.niFake_LockSession
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_LockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niFake_LockSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_LockSession_cfunc(vi, caller_has_lock)

    def niFake_MultipleArrayTypes(self, vi, output_array_size, output_array, output_array_of_fixed_length, input_array_sizes, input_array_of_floats, input_array_of_integers):  # noqa: N802
        with self._func_lock:
            if self.niFake_MultipleArrayTypes_cfunc is None:
                try:
                    self.niFake_MultipleArrayTypes_cfunc = self._library.niFake_MultipleArrayTypes
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_MultipleArrayTypes_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt16)]  # noqa: F405
                self.niFake_MultipleArrayTypes_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_MultipleArrayTypes_cfunc(vi, output_array_size, output_array, output_array_of_fixed_length, input_array_sizes, input_array_of_floats, input_array_of_integers)

    def niFake_MultipleArraysSameSize(self, vi, values1, values2, values3, values4, size):  # noqa: N802
        with self._func_lock:
            if self.niFake_MultipleArraysSameSize_cfunc is None:
                try:
                    self.niFake_MultipleArraysSameSize_cfunc = self._library.niFake_MultipleArraysSameSize
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_MultipleArraysSameSize_cfunc.argtypes = [ViSession, ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ViInt32]  # noqa: F405
                self.niFake_MultipleArraysSameSize_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_MultipleArraysSameSize_cfunc(vi, values1, values2, values3, values4, size)

    def niFake_OneInputFunction(self, vi, a_number):  # noqa: N802
        with self._func_lock:
            if self.niFake_OneInputFunction_cfunc is None:
                try:
                    self.niFake_OneInputFunction_cfunc = self._library.niFake_OneInputFunction
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_OneInputFunction_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niFake_OneInputFunction_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_OneInputFunction_cfunc(vi, a_number)

    def niFake_ParametersAreMultipleTypes(self, vi, a_boolean, an_int32, an_int64, an_int_enum, a_float, a_float_enum, string_size, a_string):  # noqa: N802
        with self._func_lock:
            if self.niFake_ParametersAreMultipleTypes_cfunc is None:
                try:
                    self.niFake_ParametersAreMultipleTypes_cfunc = self._library.niFake_ParametersAreMultipleTypes
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_ParametersAreMultipleTypes_cfunc.argtypes = [ViSession, ViBoolean, ViInt32, ViInt64, ViInt16, ViReal64, ViReal64, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFake_ParametersAreMultipleTypes_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_ParametersAreMultipleTypes_cfunc(vi, a_boolean, an_int32, an_int64, an_int_enum, a_float, a_float_enum, string_size, a_string)

    def niFake_PoorlyNamedSimpleFunction(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFake_PoorlyNamedSimpleFunction_cfunc is None:
                try:
                    self.niFake_PoorlyNamedSimpleFunction_cfunc = self._library.niFake_PoorlyNamedSimpleFunction
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_PoorlyNamedSimpleFunction_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFake_PoorlyNamedSimpleFunction_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_PoorlyNamedSimpleFunction_cfunc(vi)

    def niFake_Read(self, vi, maximum_time, reading):  # noqa: N802
        with self._func_lock:
            if self.niFake_Read_cfunc is None:
                try:
                    self.niFake_Read_cfunc = self._library.niFake_Read
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_Read_cfunc.argtypes = [ViSession, ViReal64, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFake_Read_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_Read_cfunc(vi, maximum_time, reading)

    def niFake_ReadFromChannel(self, vi, channel_name, maximum_time, reading):  # noqa: N802
        with self._func_lock:
            if self.niFake_ReadFromChannel_cfunc is None:
                try:
                    self.niFake_ReadFromChannel_cfunc = self._library.niFake_ReadFromChannel
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_ReadFromChannel_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFake_ReadFromChannel_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_ReadFromChannel_cfunc(vi, channel_name, maximum_time, reading)

    def niFake_ReturnANumberAndAString(self, vi, a_number, a_string):  # noqa: N802
        with self._func_lock:
            if self.niFake_ReturnANumberAndAString_cfunc is None:
                try:
                    self.niFake_ReturnANumberAndAString_cfunc = self._library.niFake_ReturnANumberAndAString
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_ReturnANumberAndAString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt16), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFake_ReturnANumberAndAString_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_ReturnANumberAndAString_cfunc(vi, a_number, a_string)

    def niFake_ReturnDurationInSeconds(self, vi, timedelta):  # noqa: N802
        with self._func_lock:
            if self.niFake_ReturnDurationInSeconds_cfunc is None:
                try:
                    self.niFake_ReturnDurationInSeconds_cfunc = self._library.niFake_ReturnDurationInSeconds
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_ReturnDurationInSeconds_cfunc.argtypes = [ViSession, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFake_ReturnDurationInSeconds_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_ReturnDurationInSeconds_cfunc(vi, timedelta)

    def niFake_ReturnListOfDurationsInSeconds(self, vi, number_of_elements, timedeltas):  # noqa: N802
        with self._func_lock:
            if self.niFake_ReturnListOfDurationsInSeconds_cfunc is None:
                try:
                    self.niFake_ReturnListOfDurationsInSeconds_cfunc = self._library.niFake_ReturnListOfDurationsInSeconds
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_ReturnListOfDurationsInSeconds_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFake_ReturnListOfDurationsInSeconds_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_ReturnListOfDurationsInSeconds_cfunc(vi, number_of_elements, timedeltas)

    def niFake_ReturnMultipleTypes(self, vi, a_boolean, an_int32, an_int64, an_int_enum, a_float, a_float_enum, array_size, an_array, string_size, a_string):  # noqa: N802
        with self._func_lock:
            if self.niFake_ReturnMultipleTypes_cfunc is None:
                try:
                    self.niFake_ReturnMultipleTypes_cfunc = self._library.niFake_ReturnMultipleTypes
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_ReturnMultipleTypes_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt64), ctypes.POINTER(ViInt16), ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ViInt32, ctypes.POINTER(ViReal64), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFake_ReturnMultipleTypes_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_ReturnMultipleTypes_cfunc(vi, a_boolean, an_int32, an_int64, an_int_enum, a_float, a_float_enum, array_size, an_array, string_size, a_string)

    def niFake_SetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFake_SetAttributeViBoolean_cfunc is None:
                try:
                    self.niFake_SetAttributeViBoolean_cfunc = self._library.niFake_SetAttributeViBoolean
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_SetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViBoolean]  # noqa: F405
                self.niFake_SetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_SetAttributeViBoolean_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFake_SetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFake_SetAttributeViInt32_cfunc is None:
                try:
                    self.niFake_SetAttributeViInt32_cfunc = self._library.niFake_SetAttributeViInt32
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_SetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32]  # noqa: F405
                self.niFake_SetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_SetAttributeViInt32_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFake_SetAttributeViInt64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFake_SetAttributeViInt64_cfunc is None:
                try:
                    self.niFake_SetAttributeViInt64_cfunc = self._library.niFake_SetAttributeViInt64
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_SetAttributeViInt64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt64]  # noqa: F405
                self.niFake_SetAttributeViInt64_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_SetAttributeViInt64_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFake_SetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFake_SetAttributeViReal64_cfunc is None:
                try:
                    self.niFake_SetAttributeViReal64_cfunc = self._library.niFake_SetAttributeViReal64
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_SetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViReal64]  # noqa: F405
                self.niFake_SetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_SetAttributeViReal64_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFake_SetAttributeViString(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFake_SetAttributeViString_cfunc is None:
                try:
                    self.niFake_SetAttributeViString_cfunc = self._library.niFake_SetAttributeViString
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_SetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFake_SetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_SetAttributeViString_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFake_SetCustomType(self, vi, cs):  # noqa: N802
        with self._func_lock:
            if self.niFake_SetCustomType_cfunc is None:
                try:
                    self.niFake_SetCustomType_cfunc = self._library.niFake_SetCustomType
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_SetCustomType_cfunc.argtypes = [ViSession, custom_struct.struct_CustomStruct]  # noqa: F405
                self.niFake_SetCustomType_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_SetCustomType_cfunc(vi, cs)

    def niFake_SetCustomTypeArray(self, vi, number_of_elements, cs):  # noqa: N802
        with self._func_lock:
            if self.niFake_SetCustomTypeArray_cfunc is None:
                try:
                    self.niFake_SetCustomTypeArray_cfunc = self._library.niFake_SetCustomTypeArray
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_SetCustomTypeArray_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(custom_struct.struct_CustomStruct)]  # noqa: F405
                self.niFake_SetCustomTypeArray_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_SetCustomTypeArray_cfunc(vi, number_of_elements, cs)

    def niFake_StringValuedEnumInputFunctionWithDefaults(self, vi, a_mobile_os_name):  # noqa: N802
        with self._func_lock:
            if self.niFake_StringValuedEnumInputFunctionWithDefaults_cfunc is None:
                try:
                    self.niFake_StringValuedEnumInputFunctionWithDefaults_cfunc = self._library.niFake_StringValuedEnumInputFunctionWithDefaults
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_StringValuedEnumInputFunctionWithDefaults_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFake_StringValuedEnumInputFunctionWithDefaults_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_StringValuedEnumInputFunctionWithDefaults_cfunc(vi, a_mobile_os_name)

    def niFake_TwoInputFunction(self, vi, a_number, a_string):  # noqa: N802
        with self._func_lock:
            if self.niFake_TwoInputFunction_cfunc is None:
                try:
                    self.niFake_TwoInputFunction_cfunc = self._library.niFake_TwoInputFunction
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_TwoInputFunction_cfunc.argtypes = [ViSession, ViReal64, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFake_TwoInputFunction_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_TwoInputFunction_cfunc(vi, a_number, a_string)

    def niFake_UnlockSession(self, vi, caller_has_lock):  # noqa: N802
        with self._func_lock:
            if self.niFake_UnlockSession_cfunc is None:
                try:
                    self.niFake_UnlockSession_cfunc = self._library.niFake_UnlockSession
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_UnlockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niFake_UnlockSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_UnlockSession_cfunc(vi, caller_has_lock)

    def niFake_Use64BitNumber(self, vi, input, output):  # noqa: N802
        with self._func_lock:
            if self.niFake_Use64BitNumber_cfunc is None:
                try:
                    self.niFake_Use64BitNumber_cfunc = self._library.niFake_Use64BitNumber
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_Use64BitNumber_cfunc.argtypes = [ViSession, ViInt64, ctypes.POINTER(ViInt64)]  # noqa: F405
                self.niFake_Use64BitNumber_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_Use64BitNumber_cfunc(vi, input, output)

    def niFake_WriteWaveform(self, vi, number_of_samples, waveform):  # noqa: N802
        with self._func_lock:
            if self.niFake_WriteWaveform_cfunc is None:
                try:
                    self.niFake_WriteWaveform_cfunc = self._library.niFake_WriteWaveform
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_WriteWaveform_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFake_WriteWaveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_WriteWaveform_cfunc(vi, number_of_samples, waveform)

    def niFake_close(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFake_close_cfunc is None:
                try:
                    self.niFake_close_cfunc = self._library.niFake_close
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_close_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFake_close_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_close_cfunc(vi)

    def niFake_error_message(self, vi, error_code, error_message):  # noqa: N802
        with self._func_lock:
            if self.niFake_error_message_cfunc is None:
                try:
                    self.niFake_error_message_cfunc = self._library.niFake_error_message
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_error_message_cfunc.argtypes = [ViSession, ViStatus, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFake_error_message_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_error_message_cfunc(vi, error_code, error_message)

    def niFake_self_test(self, vi, self_test_result, self_test_message):  # noqa: N802
        with self._func_lock:
            if self.niFake_self_test_cfunc is None:
                try:
                    self.niFake_self_test_cfunc = self._library.niFake_self_test
                except AttributeError as e:
                    raise AttributeError("A required function was not found in the instrument driver DLL. This might "
                                         "be an indication that the version of the instrument driver is too old for "
                                         "this version of the python API. Upgrade your instrument driver.") from e
                self.niFake_self_test_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt16), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFake_self_test_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_self_test_cfunc(vi, self_test_result, self_test_message)
