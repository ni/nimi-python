# -*- coding: utf-8 -*-
# This file was generated

import array  # noqa: F401
import ctypes
import hightime
import nifake._converters as _converters
import nifake._visatype as _visatype
import nifake.enums as enums
import nifake.errors as errors
import threading

from nifake._visatype import *  # noqa: F403,H303

import nifake.custom_struct as custom_struct  # noqa: F401

import nifake.custom_struct_nested_typedef as custom_struct_nested_typedef  # noqa: F401

import nifake.custom_struct_typedef as custom_struct_typedef  # noqa: F401


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
        self.niFake_Abort_cfunc = None
        self.niFake_AcceptListOfDurationsInSeconds_cfunc = None
        self.niFake_BoolArrayOutputFunction_cfunc = None
        self.niFake_DoubleAllTheNums_cfunc = None
        self.niFake_EnumArrayOutputFunction_cfunc = None
        self.niFake_EnumInputFunctionWithDefaults_cfunc = None
        self.niFake_ExportAttributeConfigurationBuffer_cfunc = None
        self.niFake_FetchWaveform_cfunc = None
        self.niFake_FunctionWithRepeatedCapabilityType_cfunc = None
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
        self.niFake_GetChannelNames_cfunc = None
        self.niFake_GetCustomType_cfunc = None
        self.niFake_GetCustomTypeArray_cfunc = None
        self.niFake_GetCustomTypeTypedef_cfunc = None
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
            if self.niFake_Abort_cfunc is None:
                self.niFake_Abort_cfunc = self._get_library_function('niFake_Abort')
                self.niFake_Abort_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFake_Abort_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_Abort_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def accept_list_of_durations_in_seconds(self, session, delays):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        count_ctype = _visatype.ViInt32(0 if delays is None else len(delays))  # case S160
        delays_converted = _converters.convert_timedeltas_to_seconds_real64(delays)  # case B520
        delays_ctype = get_ctypes_pointer_for_buffer(value=delays_converted, library_type=_visatype.ViReal64)  # case B520
        with self._func_lock:
            if self.niFake_AcceptListOfDurationsInSeconds_cfunc is None:
                self.niFake_AcceptListOfDurationsInSeconds_cfunc = self._get_library_function('niFake_AcceptListOfDurationsInSeconds')
                self.niFake_AcceptListOfDurationsInSeconds_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFake_AcceptListOfDurationsInSeconds_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_AcceptListOfDurationsInSeconds_cfunc(vi_ctype, count_ctype, delays_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def bool_array_output_function(self, session, number_of_elements):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        number_of_elements_ctype = _visatype.ViInt32(number_of_elements)  # case S210
        an_array_size = number_of_elements  # case B600
        an_array_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViBoolean, size=an_array_size)  # case B600
        with self._func_lock:
            if self.niFake_BoolArrayOutputFunction_cfunc is None:
                self.niFake_BoolArrayOutputFunction_cfunc = self._get_library_function('niFake_BoolArrayOutputFunction')
                self.niFake_BoolArrayOutputFunction_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niFake_BoolArrayOutputFunction_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_BoolArrayOutputFunction_cfunc(vi_ctype, number_of_elements_ctype, an_array_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return [bool(an_array_ctype[i]) for i in range(number_of_elements_ctype.value)]

    def double_all_the_nums(self, session, numbers):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        number_count_ctype = _visatype.ViInt32(0 if numbers is None else len(numbers))  # case S160
        numbers_converted = _converters.convert_double_each_element(numbers)  # case B520
        numbers_ctype = get_ctypes_pointer_for_buffer(value=numbers_converted, library_type=_visatype.ViReal64)  # case B520
        with self._func_lock:
            if self.niFake_DoubleAllTheNums_cfunc is None:
                self.niFake_DoubleAllTheNums_cfunc = self._get_library_function('niFake_DoubleAllTheNums')
                self.niFake_DoubleAllTheNums_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFake_DoubleAllTheNums_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_DoubleAllTheNums_cfunc(vi_ctype, number_count_ctype, numbers_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def enum_array_output_function(self, session, number_of_elements):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        number_of_elements_ctype = _visatype.ViInt32(number_of_elements)  # case S210
        an_array_size = number_of_elements  # case B600
        an_array_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViInt16, size=an_array_size)  # case B600
        with self._func_lock:
            if self.niFake_EnumArrayOutputFunction_cfunc is None:
                self.niFake_EnumArrayOutputFunction_cfunc = self._get_library_function('niFake_EnumArrayOutputFunction')
                self.niFake_EnumArrayOutputFunction_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt16)]  # noqa: F405
                self.niFake_EnumArrayOutputFunction_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_EnumArrayOutputFunction_cfunc(vi_ctype, number_of_elements_ctype, an_array_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return [enums.Turtle(an_array_ctype[i]) for i in range(number_of_elements_ctype.value)]

    def enum_input_function_with_defaults(self, session, a_turtle=enums.Turtle.LEONARDO):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        a_turtle_ctype = _visatype.ViInt16(a_turtle.value)  # case S130
        with self._func_lock:
            if self.niFake_EnumInputFunctionWithDefaults_cfunc is None:
                self.niFake_EnumInputFunctionWithDefaults_cfunc = self._get_library_function('niFake_EnumInputFunctionWithDefaults')
                self.niFake_EnumInputFunctionWithDefaults_cfunc.argtypes = [ViSession, ViInt16]  # noqa: F405
                self.niFake_EnumInputFunctionWithDefaults_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_EnumInputFunctionWithDefaults_cfunc(vi_ctype, a_turtle_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def export_attribute_configuration_buffer(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        size_in_bytes_ctype = _visatype.ViInt32()  # case S170
        configuration_ctype = None  # case B580
        with self._func_lock:
            if self.niFake_ExportAttributeConfigurationBuffer_cfunc is None:
                self.niFake_ExportAttributeConfigurationBuffer_cfunc = self._get_library_function('niFake_ExportAttributeConfigurationBuffer')
                self.niFake_ExportAttributeConfigurationBuffer_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt8)]  # noqa: F405
                self.niFake_ExportAttributeConfigurationBuffer_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_ExportAttributeConfigurationBuffer_cfunc(vi_ctype, size_in_bytes_ctype, configuration_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=False)
        size_in_bytes_ctype = _visatype.ViInt32(error_code)  # case S180
        configuration_size = size_in_bytes_ctype.value  # case B590
        configuration_array = array.array("b", [0] * configuration_size)  # case B590
        configuration_ctype = get_ctypes_pointer_for_buffer(value=configuration_array, library_type=_visatype.ViInt8)  # case B590
        error_code = self.niFake_ExportAttributeConfigurationBuffer_cfunc(vi_ctype, size_in_bytes_ctype, configuration_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return _converters.convert_to_bytes(configuration_array)

    def fetch_waveform(self, session, number_of_samples):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        number_of_samples_ctype = _visatype.ViInt32(number_of_samples)  # case S210
        waveform_data_size = number_of_samples  # case B600
        waveform_data_array = array.array("d", [0] * waveform_data_size)  # case B600
        waveform_data_ctype = get_ctypes_pointer_for_buffer(value=waveform_data_array, library_type=_visatype.ViReal64)  # case B600
        actual_number_of_samples_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niFake_FetchWaveform_cfunc is None:
                self.niFake_FetchWaveform_cfunc = self._get_library_function('niFake_FetchWaveform')
                self.niFake_FetchWaveform_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFake_FetchWaveform_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_FetchWaveform_cfunc(vi_ctype, number_of_samples_ctype, waveform_data_ctype, None if actual_number_of_samples_ctype is None else (ctypes.pointer(actual_number_of_samples_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return waveform_data_array

    def fetch_waveform_into(self, session, waveform_data):  # noqa: N802
        number_of_samples = len(waveform_data)
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        number_of_samples_ctype = _visatype.ViInt32(number_of_samples)  # case S210
        waveform_data_ctype = get_ctypes_pointer_for_buffer(value=waveform_data)  # case B510
        actual_number_of_samples_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niFake_FetchWaveform_cfunc is None:
                self.niFake_FetchWaveform_cfunc = self._get_library_function('niFake_FetchWaveform')
                self.niFake_FetchWaveform_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFake_FetchWaveform_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_FetchWaveform_cfunc(vi_ctype, number_of_samples_ctype, waveform_data_ctype, None if actual_number_of_samples_ctype is None else (ctypes.pointer(actual_number_of_samples_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def function_with_repeated_capability_type(self, session, site_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(site_list.encode(session._encoding))  # case C010
        with self._func_lock:
            if self.niFake_FunctionWithRepeatedCapabilityType_cfunc is None:
                self.niFake_FunctionWithRepeatedCapabilityType_cfunc = self._get_library_function('niFake_FunctionWithRepeatedCapabilityType')
                self.niFake_FunctionWithRepeatedCapabilityType_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFake_FunctionWithRepeatedCapabilityType_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_FunctionWithRepeatedCapabilityType_cfunc(vi_ctype, site_list_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def get_a_boolean(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        a_boolean_ctype = _visatype.ViBoolean()  # case S220
        with self._func_lock:
            if self.niFake_GetABoolean_cfunc is None:
                self.niFake_GetABoolean_cfunc = self._get_library_function('niFake_GetABoolean')
                self.niFake_GetABoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niFake_GetABoolean_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_GetABoolean_cfunc(vi_ctype, None if a_boolean_ctype is None else (ctypes.pointer(a_boolean_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(a_boolean_ctype.value)

    def get_a_number(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        a_number_ctype = _visatype.ViInt16()  # case S220
        with self._func_lock:
            if self.niFake_GetANumber_cfunc is None:
                self.niFake_GetANumber_cfunc = self._get_library_function('niFake_GetANumber')
                self.niFake_GetANumber_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt16)]  # noqa: F405
                self.niFake_GetANumber_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_GetANumber_cfunc(vi_ctype, None if a_number_ctype is None else (ctypes.pointer(a_number_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(a_number_ctype.value)

    def get_a_string_of_fixed_maximum_size(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        a_string_ctype = (_visatype.ViChar * 256)()  # case C070
        with self._func_lock:
            if self.niFake_GetAStringOfFixedMaximumSize_cfunc is None:
                self.niFake_GetAStringOfFixedMaximumSize_cfunc = self._get_library_function('niFake_GetAStringOfFixedMaximumSize')
                self.niFake_GetAStringOfFixedMaximumSize_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFake_GetAStringOfFixedMaximumSize_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_GetAStringOfFixedMaximumSize_cfunc(vi_ctype, a_string_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return a_string_ctype.value.decode(session._encoding)

    def get_a_string_using_python_code(self, session, a_number):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        a_number_ctype = _visatype.ViInt16(a_number)  # case S150
        a_string_ctype = (_visatype.ViChar * a_number)()  # case C080
        with self._func_lock:
            if self.niFake_GetAStringUsingPythonCode_cfunc is None:
                self.niFake_GetAStringUsingPythonCode_cfunc = self._get_library_function('niFake_GetAStringUsingPythonCode')
                self.niFake_GetAStringUsingPythonCode_cfunc.argtypes = [ViSession, ViInt16, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFake_GetAStringUsingPythonCode_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_GetAStringUsingPythonCode_cfunc(vi_ctype, a_number_ctype, a_string_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return a_string_ctype.value.decode(session._encoding)

    def get_an_ivi_dance_string(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        a_string_ctype = None  # case C050
        with self._func_lock:
            if self.niFake_GetAnIviDanceString_cfunc is None:
                self.niFake_GetAnIviDanceString_cfunc = self._get_library_function('niFake_GetAnIviDanceString')
                self.niFake_GetAnIviDanceString_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFake_GetAnIviDanceString_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_GetAnIviDanceString_cfunc(vi_ctype, buffer_size_ctype, a_string_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        a_string_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self.niFake_GetAnIviDanceString_cfunc(vi_ctype, buffer_size_ctype, a_string_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return a_string_ctype.value.decode(session._encoding)

    def get_an_ivi_dance_with_a_twist_string(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        a_string_ctype = None  # case C090
        actual_size_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niFake_GetAnIviDanceWithATwistString_cfunc is None:
                self.niFake_GetAnIviDanceWithATwistString_cfunc = self._get_library_function('niFake_GetAnIviDanceWithATwistString')
                self.niFake_GetAnIviDanceWithATwistString_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViChar), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFake_GetAnIviDanceWithATwistString_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_GetAnIviDanceWithATwistString_cfunc(vi_ctype, buffer_size_ctype, a_string_ctype, None if actual_size_ctype is None else (ctypes.pointer(actual_size_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(actual_size_ctype.value)  # case S200
        a_string_ctype = (_visatype.ViChar * actual_size_ctype.value)()  # case C100
        error_code = self.niFake_GetAnIviDanceWithATwistString_cfunc(vi_ctype, buffer_size_ctype, a_string_ctype, None if actual_size_ctype is None else (ctypes.pointer(actual_size_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return a_string_ctype.value.decode(session._encoding)

    def get_array_for_python_code_custom_type(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        number_of_elements_ctype = _visatype.ViInt32(self.get_array_size_for_python_code(session))  # case S120
        array_out_size = self.get_array_size_for_python_code(session)  # case B560
        array_out_ctype = get_ctypes_pointer_for_buffer(library_type=custom_struct.struct_CustomStruct, size=array_out_size)  # case B560
        with self._func_lock:
            if self.niFake_GetArrayForPythonCodeCustomType_cfunc is None:
                self.niFake_GetArrayForPythonCodeCustomType_cfunc = self._get_library_function('niFake_GetArrayForPythonCodeCustomType')
                self.niFake_GetArrayForPythonCodeCustomType_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(custom_struct.struct_CustomStruct)]  # noqa: F405
                self.niFake_GetArrayForPythonCodeCustomType_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_GetArrayForPythonCodeCustomType_cfunc(vi_ctype, number_of_elements_ctype, array_out_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return [custom_struct.CustomStruct(array_out_ctype[i]) for i in range(self.get_array_size_for_python_code(session))]

    def get_array_for_python_code_double(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        number_of_elements_ctype = _visatype.ViInt32(self.get_array_size_for_python_code(session))  # case S120
        array_out_size = self.get_array_size_for_python_code(session)  # case B560
        array_out_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=array_out_size)  # case B560
        with self._func_lock:
            if self.niFake_GetArrayForPythonCodeDouble_cfunc is None:
                self.niFake_GetArrayForPythonCodeDouble_cfunc = self._get_library_function('niFake_GetArrayForPythonCodeDouble')
                self.niFake_GetArrayForPythonCodeDouble_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFake_GetArrayForPythonCodeDouble_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_GetArrayForPythonCodeDouble_cfunc(vi_ctype, number_of_elements_ctype, array_out_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(array_out_ctype[i]) for i in range(self.get_array_size_for_python_code(session))]

    def get_array_size_for_python_code(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        size_out_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niFake_GetArraySizeForPythonCode_cfunc is None:
                self.niFake_GetArraySizeForPythonCode_cfunc = self._get_library_function('niFake_GetArraySizeForPythonCode')
                self.niFake_GetArraySizeForPythonCode_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFake_GetArraySizeForPythonCode_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_GetArraySizeForPythonCode_cfunc(vi_ctype, None if size_out_ctype is None else (ctypes.pointer(size_out_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(size_out_ctype.value)

    def get_array_using_ivi_dance(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        array_size_ctype = _visatype.ViInt32()  # case S170
        array_out_ctype = None  # case B580
        with self._func_lock:
            if self.niFake_GetArrayUsingIviDance_cfunc is None:
                self.niFake_GetArrayUsingIviDance_cfunc = self._get_library_function('niFake_GetArrayUsingIviDance')
                self.niFake_GetArrayUsingIviDance_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFake_GetArrayUsingIviDance_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_GetArrayUsingIviDance_cfunc(vi_ctype, array_size_ctype, array_out_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=False)
        array_size_ctype = _visatype.ViInt32(error_code)  # case S180
        array_out_size = array_size_ctype.value  # case B590
        array_out_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=array_out_size)  # case B590
        error_code = self.niFake_GetArrayUsingIviDance_cfunc(vi_ctype, array_size_ctype, array_out_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(array_out_ctype[i]) for i in range(array_size_ctype.value)]

    def _get_attribute_vi_boolean(self, session, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViBoolean()  # case S220
        with self._func_lock:
            if self.niFake_GetAttributeViBoolean_cfunc is None:
                self.niFake_GetAttributeViBoolean_cfunc = self._get_library_function('niFake_GetAttributeViBoolean')
                self.niFake_GetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niFake_GetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_GetAttributeViBoolean_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(attribute_value_ctype.value)

    def _get_attribute_vi_int32(self, session, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niFake_GetAttributeViInt32_cfunc is None:
                self.niFake_GetAttributeViInt32_cfunc = self._get_library_function('niFake_GetAttributeViInt32')
                self.niFake_GetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFake_GetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_GetAttributeViInt32_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(attribute_value_ctype.value)

    def _get_attribute_vi_int64(self, session, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt64()  # case S220
        with self._func_lock:
            if self.niFake_GetAttributeViInt64_cfunc is None:
                self.niFake_GetAttributeViInt64_cfunc = self._get_library_function('niFake_GetAttributeViInt64')
                self.niFake_GetAttributeViInt64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViInt64)]  # noqa: F405
                self.niFake_GetAttributeViInt64_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_GetAttributeViInt64_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(attribute_value_ctype.value)

    def _get_attribute_vi_real64(self, session, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViReal64()  # case S220
        with self._func_lock:
            if self.niFake_GetAttributeViReal64_cfunc is None:
                self.niFake_GetAttributeViReal64_cfunc = self._get_library_function('niFake_GetAttributeViReal64')
                self.niFake_GetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFake_GetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_GetAttributeViReal64_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return float(attribute_value_ctype.value)

    def _get_attribute_vi_string(self, session, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        attribute_value_ctype = None  # case C050
        with self._func_lock:
            if self.niFake_GetAttributeViString_cfunc is None:
                self.niFake_GetAttributeViString_cfunc = self._get_library_function('niFake_GetAttributeViString')
                self.niFake_GetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFake_GetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_GetAttributeViString_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, buffer_size_ctype, attribute_value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        attribute_value_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self.niFake_GetAttributeViString_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, buffer_size_ctype, attribute_value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return attribute_value_ctype.value.decode(session._encoding)

    def _get_cal_date_and_time(self, session, cal_type):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        cal_type_ctype = _visatype.ViInt32(cal_type)  # case S150
        month_ctype = _visatype.ViInt32()  # case S220
        day_ctype = _visatype.ViInt32()  # case S220
        year_ctype = _visatype.ViInt32()  # case S220
        hour_ctype = _visatype.ViInt32()  # case S220
        minute_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niFake_GetCalDateAndTime_cfunc is None:
                self.niFake_GetCalDateAndTime_cfunc = self._get_library_function('niFake_GetCalDateAndTime')
                self.niFake_GetCalDateAndTime_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFake_GetCalDateAndTime_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_GetCalDateAndTime_cfunc(vi_ctype, cal_type_ctype, None if month_ctype is None else (ctypes.pointer(month_ctype)), None if day_ctype is None else (ctypes.pointer(day_ctype)), None if year_ctype is None else (ctypes.pointer(year_ctype)), None if hour_ctype is None else (ctypes.pointer(hour_ctype)), None if minute_ctype is None else (ctypes.pointer(minute_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(month_ctype.value), int(day_ctype.value), int(year_ctype.value), int(hour_ctype.value), int(minute_ctype.value)

    def get_cal_interval(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        months_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niFake_GetCalInterval_cfunc is None:
                self.niFake_GetCalInterval_cfunc = self._get_library_function('niFake_GetCalInterval')
                self.niFake_GetCalInterval_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFake_GetCalInterval_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_GetCalInterval_cfunc(vi_ctype, None if months_ctype is None else (ctypes.pointer(months_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return _converters.convert_month_to_timedelta(int(months_ctype.value))

    def _get_channel_names(self, session, indices):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        indices_ctype = ctypes.create_string_buffer(_converters.convert_repeated_capabilities_without_prefix(indices).encode(session._encoding))  # case C040
        name_size_ctype = _visatype.ViInt32()  # case S170
        names_ctype = None  # case C050
        with self._func_lock:
            if self.niFake_GetChannelNames_cfunc is None:
                self.niFake_GetChannelNames_cfunc = self._get_library_function('niFake_GetChannelNames')
                self.niFake_GetChannelNames_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFake_GetChannelNames_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_GetChannelNames_cfunc(vi_ctype, indices_ctype, name_size_ctype, names_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=False)
        name_size_ctype = _visatype.ViInt32(error_code)  # case S180
        names_ctype = (_visatype.ViChar * name_size_ctype.value)()  # case C060
        error_code = self.niFake_GetChannelNames_cfunc(vi_ctype, indices_ctype, name_size_ctype, names_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return _converters.convert_comma_separated_string_to_list(names_ctype.value.decode(session._encoding))

    def get_custom_type(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        cs_ctype = custom_struct.struct_CustomStruct()  # case S220
        with self._func_lock:
            if self.niFake_GetCustomType_cfunc is None:
                self.niFake_GetCustomType_cfunc = self._get_library_function('niFake_GetCustomType')
                self.niFake_GetCustomType_cfunc.argtypes = [ViSession, ctypes.POINTER(custom_struct.struct_CustomStruct)]  # noqa: F405
                self.niFake_GetCustomType_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_GetCustomType_cfunc(vi_ctype, None if cs_ctype is None else (ctypes.pointer(cs_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return custom_struct.CustomStruct(cs_ctype)

    def get_custom_type_array(self, session, number_of_elements):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        number_of_elements_ctype = _visatype.ViInt32(number_of_elements)  # case S210
        cs_size = number_of_elements  # case B600
        cs_ctype = get_ctypes_pointer_for_buffer(library_type=custom_struct.struct_CustomStruct, size=cs_size)  # case B600
        with self._func_lock:
            if self.niFake_GetCustomTypeArray_cfunc is None:
                self.niFake_GetCustomTypeArray_cfunc = self._get_library_function('niFake_GetCustomTypeArray')
                self.niFake_GetCustomTypeArray_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(custom_struct.struct_CustomStruct)]  # noqa: F405
                self.niFake_GetCustomTypeArray_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_GetCustomTypeArray_cfunc(vi_ctype, number_of_elements_ctype, cs_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return [custom_struct.CustomStruct(cs_ctype[i]) for i in range(number_of_elements_ctype.value)]

    def get_custom_type_typedef(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        cst_ctype = custom_struct_typedef.struct_CustomStructTypedef()  # case S220
        csnt_ctype = custom_struct_nested_typedef.struct_CustomStructNestedTypedef()  # case S220
        with self._func_lock:
            if self.niFake_GetCustomTypeTypedef_cfunc is None:
                self.niFake_GetCustomTypeTypedef_cfunc = self._get_library_function('niFake_GetCustomTypeTypedef')
                self.niFake_GetCustomTypeTypedef_cfunc.argtypes = [ViSession, ctypes.POINTER(custom_struct_typedef.struct_CustomStructTypedef), ctypes.POINTER(custom_struct_nested_typedef.struct_CustomStructNestedTypedef)]  # noqa: F405
                self.niFake_GetCustomTypeTypedef_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_GetCustomTypeTypedef_cfunc(vi_ctype, None if cst_ctype is None else (ctypes.pointer(cst_ctype)), None if csnt_ctype is None else (ctypes.pointer(csnt_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return custom_struct_typedef.CustomStructTypedef(cst_ctype), custom_struct_nested_typedef.CustomStructNestedTypedef(csnt_ctype)

    def get_enum_value(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        a_quantity_ctype = _visatype.ViInt32()  # case S220
        a_turtle_ctype = _visatype.ViInt16()  # case S220
        with self._func_lock:
            if self.niFake_GetEnumValue_cfunc is None:
                self.niFake_GetEnumValue_cfunc = self._get_library_function('niFake_GetEnumValue')
                self.niFake_GetEnumValue_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt16)]  # noqa: F405
                self.niFake_GetEnumValue_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_GetEnumValue_cfunc(vi_ctype, None if a_quantity_ctype is None else (ctypes.pointer(a_quantity_ctype)), None if a_turtle_ctype is None else (ctypes.pointer(a_turtle_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(a_quantity_ctype.value), enums.Turtle(a_turtle_ctype.value)

    def _get_error(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        error_code_ctype = _visatype.ViStatus()  # case S220
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        description_ctype = None  # case C050
        with self._func_lock:
            if self.niFake_GetError_cfunc is None:
                self.niFake_GetError_cfunc = self._get_library_function('niFake_GetError')
                self.niFake_GetError_cfunc.argtypes = [ViSession, ctypes.POINTER(ViStatus), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFake_GetError_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_GetError_cfunc(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), buffer_size_ctype, description_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=True)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        description_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self.niFake_GetError_cfunc(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), buffer_size_ctype, description_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=True)
        return int(error_code_ctype.value), description_ctype.value.decode(session._encoding)

    def import_attribute_configuration_buffer(self, session, configuration):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        size_in_bytes_ctype = _visatype.ViInt32(0 if configuration is None else len(configuration))  # case S160
        configuration_converted = _converters.convert_to_bytes(configuration)  # case B520
        configuration_ctype = get_ctypes_pointer_for_buffer(value=configuration_converted, library_type=_visatype.ViInt8)  # case B520
        with self._func_lock:
            if self.niFake_ImportAttributeConfigurationBuffer_cfunc is None:
                self.niFake_ImportAttributeConfigurationBuffer_cfunc = self._get_library_function('niFake_ImportAttributeConfigurationBuffer')
                self.niFake_ImportAttributeConfigurationBuffer_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt8)]  # noqa: F405
                self.niFake_ImportAttributeConfigurationBuffer_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_ImportAttributeConfigurationBuffer_cfunc(vi_ctype, size_in_bytes_ctype, configuration_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _init_with_options(self, session, resource_name, option_string, id_query=False, reset_device=False):  # noqa: N802
        resource_name_ctype = ctypes.create_string_buffer(resource_name.encode(session._encoding))  # case C020
        id_query_ctype = _visatype.ViBoolean(id_query)  # case S150
        reset_device_ctype = _visatype.ViBoolean(reset_device)  # case S150
        option_string_ctype = ctypes.create_string_buffer(_converters.convert_init_with_options_dictionary(option_string).encode(session._encoding))  # case C040
        vi_ctype = _visatype.ViSession()  # case S220
        with self._func_lock:
            if self.niFake_InitWithOptions_cfunc is None:
                self.niFake_InitWithOptions_cfunc = self._get_library_function('niFake_InitWithOptions')
                self.niFake_InitWithOptions_cfunc.argtypes = [ctypes.POINTER(ViChar), ViBoolean, ViBoolean, ctypes.POINTER(ViChar), ctypes.POINTER(ViSession)]  # noqa: F405
                self.niFake_InitWithOptions_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_InitWithOptions_cfunc(resource_name_ctype, id_query_ctype, reset_device_ctype, option_string_ctype, None if vi_ctype is None else (ctypes.pointer(vi_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(vi_ctype.value)

    def _initiate(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niFake_Initiate_cfunc is None:
                self.niFake_Initiate_cfunc = self._get_library_function('niFake_Initiate')
                self.niFake_Initiate_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFake_Initiate_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_Initiate_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def lock(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        caller_has_lock_ctype = _visatype.ViBoolean()  # case S220
        with self._func_lock:
            if self.niFake_LockSession_cfunc is None:
                self.niFake_LockSession_cfunc = self._get_library_function('niFake_LockSession')
                self.niFake_LockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niFake_LockSession_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_LockSession_cfunc(vi_ctype, None if caller_has_lock_ctype is None else (ctypes.pointer(caller_has_lock_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(caller_has_lock_ctype.value)

    def multiple_array_types(self, session, output_array_size, input_array_of_floats, input_array_of_integers=None):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        output_array_size_ctype = _visatype.ViInt32(output_array_size)  # case S210
        output_array_size = output_array_size  # case B600
        output_array_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=output_array_size)  # case B600
        output_array_of_fixed_length_size = 3  # case B570
        output_array_of_fixed_length_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=output_array_of_fixed_length_size)  # case B570
        input_array_sizes_ctype = _visatype.ViInt32(0 if input_array_of_floats is None else len(input_array_of_floats))  # case S160
        if input_array_of_integers is not None and len(input_array_of_integers) != len(input_array_of_floats):  # case S160
            raise ValueError("Length of input_array_of_integers and input_array_of_floats parameters do not match.")  # case S160
        input_array_of_floats_ctype = get_ctypes_pointer_for_buffer(value=input_array_of_floats, library_type=_visatype.ViReal64)  # case B550
        input_array_of_integers_ctype = get_ctypes_pointer_for_buffer(value=input_array_of_integers, library_type=_visatype.ViInt16)  # case B550
        with self._func_lock:
            if self.niFake_MultipleArrayTypes_cfunc is None:
                self.niFake_MultipleArrayTypes_cfunc = self._get_library_function('niFake_MultipleArrayTypes')
                self.niFake_MultipleArrayTypes_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt16)]  # noqa: F405
                self.niFake_MultipleArrayTypes_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_MultipleArrayTypes_cfunc(vi_ctype, output_array_size_ctype, output_array_ctype, output_array_of_fixed_length_ctype, input_array_sizes_ctype, input_array_of_floats_ctype, input_array_of_integers_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(output_array_ctype[i]) for i in range(output_array_size_ctype.value)], [float(output_array_of_fixed_length_ctype[i]) for i in range(3)]

    def multiple_arrays_same_size(self, session, values1, values2, values3, values4):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        values1_ctype = get_ctypes_pointer_for_buffer(value=values1, library_type=_visatype.ViReal64)  # case B550
        values2_ctype = get_ctypes_pointer_for_buffer(value=values2, library_type=_visatype.ViReal64)  # case B550
        values3_ctype = get_ctypes_pointer_for_buffer(value=values3, library_type=_visatype.ViReal64)  # case B550
        values4_ctype = get_ctypes_pointer_for_buffer(value=values4, library_type=_visatype.ViReal64)  # case B550
        size_ctype = _visatype.ViInt32(0 if values1 is None else len(values1))  # case S160
        if values2 is not None and len(values2) != len(values1):  # case S160
            raise ValueError("Length of values2 and values1 parameters do not match.")  # case S160
        if values3 is not None and len(values3) != len(values1):  # case S160
            raise ValueError("Length of values3 and values1 parameters do not match.")  # case S160
        if values4 is not None and len(values4) != len(values1):  # case S160
            raise ValueError("Length of values4 and values1 parameters do not match.")  # case S160
        with self._func_lock:
            if self.niFake_MultipleArraysSameSize_cfunc is None:
                self.niFake_MultipleArraysSameSize_cfunc = self._get_library_function('niFake_MultipleArraysSameSize')
                self.niFake_MultipleArraysSameSize_cfunc.argtypes = [ViSession, ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ViInt32]  # noqa: F405
                self.niFake_MultipleArraysSameSize_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_MultipleArraysSameSize_cfunc(vi_ctype, values1_ctype, values2_ctype, values3_ctype, values4_ctype, size_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def one_input_function(self, session, a_number):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        a_number_ctype = _visatype.ViInt32(a_number)  # case S150
        with self._func_lock:
            if self.niFake_OneInputFunction_cfunc is None:
                self.niFake_OneInputFunction_cfunc = self._get_library_function('niFake_OneInputFunction')
                self.niFake_OneInputFunction_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niFake_OneInputFunction_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_OneInputFunction_cfunc(vi_ctype, a_number_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def parameters_are_multiple_types(self, session, a_boolean, an_int32, an_int64, an_int_enum, a_float, a_float_enum, a_string):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        a_boolean_ctype = _visatype.ViBoolean(a_boolean)  # case S150
        an_int32_ctype = _visatype.ViInt32(an_int32)  # case S150
        an_int64_ctype = _visatype.ViInt64(an_int64)  # case S150
        an_int_enum_ctype = _visatype.ViInt16(an_int_enum.value)  # case S130
        a_float_ctype = _visatype.ViReal64(a_float)  # case S150
        a_float_enum_ctype = _visatype.ViReal64(a_float_enum.value)  # case S130
        string_size_ctype = _visatype.ViInt32(0 if a_string is None else len(a_string))  # case S160
        a_string_ctype = ctypes.create_string_buffer(a_string.encode(session._encoding))  # case C020
        with self._func_lock:
            if self.niFake_ParametersAreMultipleTypes_cfunc is None:
                self.niFake_ParametersAreMultipleTypes_cfunc = self._get_library_function('niFake_ParametersAreMultipleTypes')
                self.niFake_ParametersAreMultipleTypes_cfunc.argtypes = [ViSession, ViBoolean, ViInt32, ViInt64, ViInt16, ViReal64, ViReal64, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFake_ParametersAreMultipleTypes_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_ParametersAreMultipleTypes_cfunc(vi_ctype, a_boolean_ctype, an_int32_ctype, an_int64_ctype, an_int_enum_ctype, a_float_ctype, a_float_enum_ctype, string_size_ctype, a_string_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def simple_function(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niFake_PoorlyNamedSimpleFunction_cfunc is None:
                self.niFake_PoorlyNamedSimpleFunction_cfunc = self._get_library_function('niFake_PoorlyNamedSimpleFunction')
                self.niFake_PoorlyNamedSimpleFunction_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFake_PoorlyNamedSimpleFunction_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_PoorlyNamedSimpleFunction_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def read(self, session, maximum_time):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        maximum_time_ctype = _converters.convert_timedelta_to_seconds_real64(maximum_time)  # case S140
        reading_ctype = _visatype.ViReal64()  # case S220
        with self._func_lock:
            if self.niFake_Read_cfunc is None:
                self.niFake_Read_cfunc = self._get_library_function('niFake_Read')
                self.niFake_Read_cfunc.argtypes = [ViSession, ViReal64, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFake_Read_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_Read_cfunc(vi_ctype, maximum_time_ctype, None if reading_ctype is None else (ctypes.pointer(reading_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return float(reading_ctype.value)

    def read_from_channel(self, session, channel_name, maximum_time):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        maximum_time_ctype = _converters.convert_timedelta_to_milliseconds_int32(maximum_time)  # case S140
        reading_ctype = _visatype.ViReal64()  # case S220
        with self._func_lock:
            if self.niFake_ReadFromChannel_cfunc is None:
                self.niFake_ReadFromChannel_cfunc = self._get_library_function('niFake_ReadFromChannel')
                self.niFake_ReadFromChannel_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFake_ReadFromChannel_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_ReadFromChannel_cfunc(vi_ctype, channel_name_ctype, maximum_time_ctype, None if reading_ctype is None else (ctypes.pointer(reading_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return float(reading_ctype.value)

    def return_a_number_and_a_string(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        a_number_ctype = _visatype.ViInt16()  # case S220
        a_string_ctype = (_visatype.ViChar * 256)()  # case C070
        with self._func_lock:
            if self.niFake_ReturnANumberAndAString_cfunc is None:
                self.niFake_ReturnANumberAndAString_cfunc = self._get_library_function('niFake_ReturnANumberAndAString')
                self.niFake_ReturnANumberAndAString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt16), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFake_ReturnANumberAndAString_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_ReturnANumberAndAString_cfunc(vi_ctype, None if a_number_ctype is None else (ctypes.pointer(a_number_ctype)), a_string_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(a_number_ctype.value), a_string_ctype.value.decode(session._encoding)

    def return_duration_in_seconds(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        timedelta_ctype = _visatype.ViReal64()  # case S220
        with self._func_lock:
            if self.niFake_ReturnDurationInSeconds_cfunc is None:
                self.niFake_ReturnDurationInSeconds_cfunc = self._get_library_function('niFake_ReturnDurationInSeconds')
                self.niFake_ReturnDurationInSeconds_cfunc.argtypes = [ViSession, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFake_ReturnDurationInSeconds_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_ReturnDurationInSeconds_cfunc(vi_ctype, None if timedelta_ctype is None else (ctypes.pointer(timedelta_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return _converters.convert_seconds_real64_to_timedelta(float(timedelta_ctype.value))

    def return_list_of_durations_in_seconds(self, session, number_of_elements):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        number_of_elements_ctype = _visatype.ViInt32(number_of_elements)  # case S210
        timedeltas_size = number_of_elements  # case B600
        timedeltas_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=timedeltas_size)  # case B600
        with self._func_lock:
            if self.niFake_ReturnListOfDurationsInSeconds_cfunc is None:
                self.niFake_ReturnListOfDurationsInSeconds_cfunc = self._get_library_function('niFake_ReturnListOfDurationsInSeconds')
                self.niFake_ReturnListOfDurationsInSeconds_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFake_ReturnListOfDurationsInSeconds_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_ReturnListOfDurationsInSeconds_cfunc(vi_ctype, number_of_elements_ctype, timedeltas_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return _converters.convert_seconds_real64_to_timedeltas([float(timedeltas_ctype[i]) for i in range(number_of_elements_ctype.value)])

    def return_multiple_types(self, session, array_size):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        a_boolean_ctype = _visatype.ViBoolean()  # case S220
        an_int32_ctype = _visatype.ViInt32()  # case S220
        an_int64_ctype = _visatype.ViInt64()  # case S220
        an_int_enum_ctype = _visatype.ViInt16()  # case S220
        a_float_ctype = _visatype.ViReal64()  # case S220
        a_float_enum_ctype = _visatype.ViReal64()  # case S220
        array_size_ctype = _visatype.ViInt32(array_size)  # case S210
        an_array_size = array_size  # case B600
        an_array_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=an_array_size)  # case B600
        string_size_ctype = _visatype.ViInt32()  # case S170
        a_string_ctype = None  # case C050
        with self._func_lock:
            if self.niFake_ReturnMultipleTypes_cfunc is None:
                self.niFake_ReturnMultipleTypes_cfunc = self._get_library_function('niFake_ReturnMultipleTypes')
                self.niFake_ReturnMultipleTypes_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt64), ctypes.POINTER(ViInt16), ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ViInt32, ctypes.POINTER(ViReal64), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFake_ReturnMultipleTypes_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_ReturnMultipleTypes_cfunc(vi_ctype, None if a_boolean_ctype is None else (ctypes.pointer(a_boolean_ctype)), None if an_int32_ctype is None else (ctypes.pointer(an_int32_ctype)), None if an_int64_ctype is None else (ctypes.pointer(an_int64_ctype)), None if an_int_enum_ctype is None else (ctypes.pointer(an_int_enum_ctype)), None if a_float_ctype is None else (ctypes.pointer(a_float_ctype)), None if a_float_enum_ctype is None else (ctypes.pointer(a_float_enum_ctype)), array_size_ctype, an_array_ctype, string_size_ctype, a_string_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=False)
        string_size_ctype = _visatype.ViInt32(error_code)  # case S180
        a_string_ctype = (_visatype.ViChar * string_size_ctype.value)()  # case C060
        error_code = self.niFake_ReturnMultipleTypes_cfunc(vi_ctype, None if a_boolean_ctype is None else (ctypes.pointer(a_boolean_ctype)), None if an_int32_ctype is None else (ctypes.pointer(an_int32_ctype)), None if an_int64_ctype is None else (ctypes.pointer(an_int64_ctype)), None if an_int_enum_ctype is None else (ctypes.pointer(an_int_enum_ctype)), None if a_float_ctype is None else (ctypes.pointer(a_float_ctype)), None if a_float_enum_ctype is None else (ctypes.pointer(a_float_enum_ctype)), array_size_ctype, an_array_ctype, string_size_ctype, a_string_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(a_boolean_ctype.value), int(an_int32_ctype.value), int(an_int64_ctype.value), enums.Turtle(an_int_enum_ctype.value), float(a_float_ctype.value), enums.FloatEnum(a_float_enum_ctype.value), [float(an_array_ctype[i]) for i in range(array_size_ctype.value)], a_string_ctype.value.decode(session._encoding)

    def _set_attribute_vi_boolean(self, session, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViBoolean(attribute_value)  # case S150
        with self._func_lock:
            if self.niFake_SetAttributeViBoolean_cfunc is None:
                self.niFake_SetAttributeViBoolean_cfunc = self._get_library_function('niFake_SetAttributeViBoolean')
                self.niFake_SetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViBoolean]  # noqa: F405
                self.niFake_SetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_SetAttributeViBoolean_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_int32(self, session, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt32(attribute_value)  # case S150
        with self._func_lock:
            if self.niFake_SetAttributeViInt32_cfunc is None:
                self.niFake_SetAttributeViInt32_cfunc = self._get_library_function('niFake_SetAttributeViInt32')
                self.niFake_SetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32]  # noqa: F405
                self.niFake_SetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_SetAttributeViInt32_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_int64(self, session, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt64(attribute_value)  # case S150
        with self._func_lock:
            if self.niFake_SetAttributeViInt64_cfunc is None:
                self.niFake_SetAttributeViInt64_cfunc = self._get_library_function('niFake_SetAttributeViInt64')
                self.niFake_SetAttributeViInt64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt64]  # noqa: F405
                self.niFake_SetAttributeViInt64_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_SetAttributeViInt64_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_real64(self, session, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViReal64(attribute_value)  # case S150
        with self._func_lock:
            if self.niFake_SetAttributeViReal64_cfunc is None:
                self.niFake_SetAttributeViReal64_cfunc = self._get_library_function('niFake_SetAttributeViReal64')
                self.niFake_SetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViReal64]  # noqa: F405
                self.niFake_SetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_SetAttributeViReal64_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_string(self, session, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = ctypes.create_string_buffer(attribute_value.encode(session._encoding))  # case C020
        with self._func_lock:
            if self.niFake_SetAttributeViString_cfunc is None:
                self.niFake_SetAttributeViString_cfunc = self._get_library_function('niFake_SetAttributeViString')
                self.niFake_SetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFake_SetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_SetAttributeViString_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_custom_type(self, session, cs):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        cs_ctype = custom_struct.struct_CustomStruct(cs)  # case S150
        with self._func_lock:
            if self.niFake_SetCustomType_cfunc is None:
                self.niFake_SetCustomType_cfunc = self._get_library_function('niFake_SetCustomType')
                self.niFake_SetCustomType_cfunc.argtypes = [ViSession, custom_struct.struct_CustomStruct]  # noqa: F405
                self.niFake_SetCustomType_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_SetCustomType_cfunc(vi_ctype, cs_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_custom_type_array(self, session, cs):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        number_of_elements_ctype = _visatype.ViInt32(0 if cs is None else len(cs))  # case S160
        cs_ctype = get_ctypes_pointer_for_buffer([custom_struct.struct_CustomStruct(c) for c in cs], library_type=custom_struct.struct_CustomStruct)  # case B540
        with self._func_lock:
            if self.niFake_SetCustomTypeArray_cfunc is None:
                self.niFake_SetCustomTypeArray_cfunc = self._get_library_function('niFake_SetCustomTypeArray')
                self.niFake_SetCustomTypeArray_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(custom_struct.struct_CustomStruct)]  # noqa: F405
                self.niFake_SetCustomTypeArray_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_SetCustomTypeArray_cfunc(vi_ctype, number_of_elements_ctype, cs_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def string_valued_enum_input_function_with_defaults(self, session, a_mobile_os_name=enums.MobileOSNames.ANDROID):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        a_mobile_os_name_ctype = ctypes.create_string_buffer(a_mobile_os_name.value.encode(session._encoding))  # case C030
        with self._func_lock:
            if self.niFake_StringValuedEnumInputFunctionWithDefaults_cfunc is None:
                self.niFake_StringValuedEnumInputFunctionWithDefaults_cfunc = self._get_library_function('niFake_StringValuedEnumInputFunctionWithDefaults')
                self.niFake_StringValuedEnumInputFunctionWithDefaults_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFake_StringValuedEnumInputFunctionWithDefaults_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_StringValuedEnumInputFunctionWithDefaults_cfunc(vi_ctype, a_mobile_os_name_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def two_input_function(self, session, a_number, a_string):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        a_number_ctype = _visatype.ViReal64(a_number)  # case S150
        a_string_ctype = ctypes.create_string_buffer(a_string.encode(session._encoding))  # case C020
        with self._func_lock:
            if self.niFake_TwoInputFunction_cfunc is None:
                self.niFake_TwoInputFunction_cfunc = self._get_library_function('niFake_TwoInputFunction')
                self.niFake_TwoInputFunction_cfunc.argtypes = [ViSession, ViReal64, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFake_TwoInputFunction_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_TwoInputFunction_cfunc(vi_ctype, a_number_ctype, a_string_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def unlock(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        caller_has_lock_ctype = _visatype.ViBoolean()  # case S220
        with self._func_lock:
            if self.niFake_UnlockSession_cfunc is None:
                self.niFake_UnlockSession_cfunc = self._get_library_function('niFake_UnlockSession')
                self.niFake_UnlockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niFake_UnlockSession_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_UnlockSession_cfunc(vi_ctype, None if caller_has_lock_ctype is None else (ctypes.pointer(caller_has_lock_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(caller_has_lock_ctype.value)

    def use64_bit_number(self, session, input):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        input_ctype = _visatype.ViInt64(input)  # case S150
        output_ctype = _visatype.ViInt64()  # case S220
        with self._func_lock:
            if self.niFake_Use64BitNumber_cfunc is None:
                self.niFake_Use64BitNumber_cfunc = self._get_library_function('niFake_Use64BitNumber')
                self.niFake_Use64BitNumber_cfunc.argtypes = [ViSession, ViInt64, ctypes.POINTER(ViInt64)]  # noqa: F405
                self.niFake_Use64BitNumber_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_Use64BitNumber_cfunc(vi_ctype, input_ctype, None if output_ctype is None else (ctypes.pointer(output_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(output_ctype.value)

    def write_waveform(self, session, waveform):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        number_of_samples_ctype = _visatype.ViInt32(0 if waveform is None else len(waveform))  # case S160
        waveform_array = get_ctypes_and_array(value=waveform, array_type="d")  # case B550
        waveform_ctype = get_ctypes_pointer_for_buffer(value=waveform_array, library_type=_visatype.ViReal64)  # case B550
        with self._func_lock:
            if self.niFake_WriteWaveform_cfunc is None:
                self.niFake_WriteWaveform_cfunc = self._get_library_function('niFake_WriteWaveform')
                self.niFake_WriteWaveform_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFake_WriteWaveform_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_WriteWaveform_cfunc(vi_ctype, number_of_samples_ctype, waveform_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def write_waveform_numpy(self, session, waveform):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        number_of_samples_ctype = _visatype.ViInt32(0 if waveform is None else len(waveform))  # case S160
        waveform_ctype = get_ctypes_pointer_for_buffer(value=waveform)  # case B510
        with self._func_lock:
            if self.niFake_WriteWaveform_cfunc is None:
                self.niFake_WriteWaveform_cfunc = self._get_library_function('niFake_WriteWaveform')
                self.niFake_WriteWaveform_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFake_WriteWaveform_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_WriteWaveform_cfunc(vi_ctype, number_of_samples_ctype, waveform_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _close(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niFake_close_cfunc is None:
                self.niFake_close_cfunc = self._get_library_function('niFake_close')
                self.niFake_close_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFake_close_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_close_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _error_message(self, session, error_code):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        error_code_ctype = _visatype.ViStatus(error_code)  # case S150
        error_message_ctype = (_visatype.ViChar * 256)()  # case C070
        with self._func_lock:
            if self.niFake_error_message_cfunc is None:
                self.niFake_error_message_cfunc = self._get_library_function('niFake_error_message')
                self.niFake_error_message_cfunc.argtypes = [ViSession, ViStatus, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFake_error_message_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_error_message_cfunc(vi_ctype, error_code_ctype, error_message_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=True)
        return error_message_ctype.value.decode(session._encoding)

    def _self_test(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        self_test_result_ctype = _visatype.ViInt16()  # case S220
        self_test_message_ctype = (_visatype.ViChar * 256)()  # case C070
        with self._func_lock:
            if self.niFake_self_test_cfunc is None:
                self.niFake_self_test_cfunc = self._get_library_function('niFake_self_test')
                self.niFake_self_test_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt16), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFake_self_test_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFake_self_test_cfunc(vi_ctype, None if self_test_result_ctype is None else (ctypes.pointer(self_test_result_ctype)), self_test_message_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(self_test_result_ctype.value), self_test_message_ctype.value.decode(session._encoding)
