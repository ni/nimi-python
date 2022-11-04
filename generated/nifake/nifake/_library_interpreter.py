# -*- coding: utf-8 -*-
# This file was generated

import array
import ctypes
import hightime  # noqa: F401
import nifake._library_singleton as _library_singleton
import nifake._visatype as _visatype
import nifake.enums as enums  # noqa: F401
import nifake.errors as errors

import nifake.custom_struct as custom_struct  # noqa: F401

import nifake.custom_struct_nested_typedef as custom_struct_nested_typedef  # noqa: F401

import nifake.custom_struct_typedef as custom_struct_typedef  # noqa: F401


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
        self._vi = 0

    def get_error_description(self, error_code):
        '''get_error_description

        Returns the error description.
        '''
        try:
            returned_error_code, error_string = self.get_error()
            if returned_error_code == error_code:
                return error_string
        except errors.Error:
            pass

        try:
            '''
            It is expected for get_error to raise when the session is invalid
            (IVI spec requires GetError to fail).
            Use error_message instead. It doesn't require a session.
            '''
            error_string = self.error_message(error_code)
            return error_string
        except errors.Error:
            pass
        return "Failed to retrieve error description."

    def abort(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFake_Abort(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def accept_list_of_durations_in_seconds(self, delays):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        count_ctype = _visatype.ViInt32(0 if delays is None else len(delays))  # case S160
        delays_ctype = _get_ctypes_pointer_for_buffer(value=delays, library_type=_visatype.ViReal64)  # case B550
        error_code = self._library.niFake_AcceptListOfDurationsInSeconds(vi_ctype, count_ctype, delays_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def bool_array_output_function(self, number_of_elements):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        number_of_elements_ctype = _visatype.ViInt32(number_of_elements)  # case S210
        an_array_size = number_of_elements  # case B600
        an_array_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViBoolean, size=an_array_size)  # case B600
        error_code = self._library.niFake_BoolArrayOutputFunction(vi_ctype, number_of_elements_ctype, an_array_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [bool(an_array_ctype[i]) for i in range(number_of_elements_ctype.value)]

    def custom_nested_struct_roundtrip(self, nested_custom_type_in):  # noqa: N802
        nested_custom_type_in_ctype = custom_struct_nested_typedef.struct_CustomStructNestedTypedef(nested_custom_type_in)  # case S150
        nested_custom_type_out_ctype = custom_struct_nested_typedef.struct_CustomStructNestedTypedef()  # case S220
        error_code = self._library.niFake_CustomNestedStructRoundtrip(nested_custom_type_in_ctype, None if nested_custom_type_out_ctype is None else (ctypes.pointer(nested_custom_type_out_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return custom_struct_nested_typedef.CustomStructNestedTypedef(nested_custom_type_out_ctype)

    def double_all_the_nums(self, numbers):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        number_count_ctype = _visatype.ViInt32(0 if numbers is None else len(numbers))  # case S160
        numbers_ctype = _get_ctypes_pointer_for_buffer(value=numbers, library_type=_visatype.ViReal64)  # case B550
        error_code = self._library.niFake_DoubleAllTheNums(vi_ctype, number_count_ctype, numbers_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def enum_array_output_function(self, number_of_elements):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        number_of_elements_ctype = _visatype.ViInt32(number_of_elements)  # case S210
        an_array_size = number_of_elements  # case B600
        an_array_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViInt16, size=an_array_size)  # case B600
        error_code = self._library.niFake_EnumArrayOutputFunction(vi_ctype, number_of_elements_ctype, an_array_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [enums.Turtle(an_array_ctype[i]) for i in range(number_of_elements_ctype.value)]

    def enum_input_function_with_defaults(self, a_turtle):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        a_turtle_ctype = _visatype.ViInt16(a_turtle.value)  # case S130
        error_code = self._library.niFake_EnumInputFunctionWithDefaults(vi_ctype, a_turtle_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def export_attribute_configuration_buffer(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        size_in_bytes_ctype = _visatype.ViInt32()  # case S170
        configuration_ctype = None  # case B580
        error_code = self._library.niFake_ExportAttributeConfigurationBuffer(vi_ctype, size_in_bytes_ctype, configuration_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        size_in_bytes_ctype = _visatype.ViInt32(error_code)  # case S180
        configuration_size = size_in_bytes_ctype.value  # case B590
        configuration_array = array.array("b", [0] * configuration_size)  # case B590
        configuration_ctype = _get_ctypes_pointer_for_buffer(value=configuration_array, library_type=_visatype.ViInt8)  # case B590
        error_code = self._library.niFake_ExportAttributeConfigurationBuffer(vi_ctype, size_in_bytes_ctype, configuration_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return configuration_array

    def fetch_waveform(self, number_of_samples):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        number_of_samples_ctype = _visatype.ViInt32(number_of_samples)  # case S210
        waveform_data_size = number_of_samples  # case B600
        waveform_data_array = array.array("d", [0] * waveform_data_size)  # case B600
        waveform_data_ctype = _get_ctypes_pointer_for_buffer(value=waveform_data_array, library_type=_visatype.ViReal64)  # case B600
        actual_number_of_samples_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFake_FetchWaveform(vi_ctype, number_of_samples_ctype, waveform_data_ctype, None if actual_number_of_samples_ctype is None else (ctypes.pointer(actual_number_of_samples_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return waveform_data_array

    def fetch_waveform_into(self, waveform_data):  # noqa: N802
        number_of_samples = len(waveform_data)
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        number_of_samples_ctype = _visatype.ViInt32(number_of_samples)  # case S210
        waveform_data_ctype = _get_ctypes_pointer_for_buffer(value=waveform_data)  # case B510
        actual_number_of_samples_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFake_FetchWaveform(vi_ctype, number_of_samples_ctype, waveform_data_ctype, None if actual_number_of_samples_ctype is None else (ctypes.pointer(actual_number_of_samples_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def function_with_repeated_capability_type(self, site_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(site_list.encode(self._encoding))  # case C010
        error_code = self._library.niFake_FunctionWithRepeatedCapabilityType(vi_ctype, site_list_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def get_a_boolean(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        a_boolean_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niFake_GetABoolean(vi_ctype, None if a_boolean_ctype is None else (ctypes.pointer(a_boolean_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(a_boolean_ctype.value)

    def get_a_number(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        a_number_ctype = _visatype.ViInt16()  # case S220
        error_code = self._library.niFake_GetANumber(vi_ctype, None if a_number_ctype is None else (ctypes.pointer(a_number_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(a_number_ctype.value)

    def get_a_string_of_fixed_maximum_size(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        a_string_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library.niFake_GetAStringOfFixedMaximumSize(vi_ctype, a_string_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return a_string_ctype.value.decode(self._encoding)

    def get_a_string_using_python_code(self, a_number):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        a_number_ctype = _visatype.ViInt16(a_number)  # case S150
        a_string_ctype = (_visatype.ViChar * a_number)()  # case C080
        error_code = self._library.niFake_GetAStringUsingPythonCode(vi_ctype, a_number_ctype, a_string_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return a_string_ctype.value.decode(self._encoding)

    def get_an_ivi_dance_string(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        a_string_ctype = None  # case C050
        error_code = self._library.niFake_GetAnIviDanceString(vi_ctype, buffer_size_ctype, a_string_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        a_string_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niFake_GetAnIviDanceString(vi_ctype, buffer_size_ctype, a_string_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return a_string_ctype.value.decode(self._encoding)

    def get_an_ivi_dance_with_a_twist_string(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        a_string_ctype = None  # case C090
        actual_size_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFake_GetAnIviDanceWithATwistString(vi_ctype, buffer_size_ctype, a_string_ctype, None if actual_size_ctype is None else (ctypes.pointer(actual_size_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(actual_size_ctype.value)  # case S200
        a_string_ctype = (_visatype.ViChar * actual_size_ctype.value)()  # case C100
        error_code = self._library.niFake_GetAnIviDanceWithATwistString(vi_ctype, buffer_size_ctype, a_string_ctype, None if actual_size_ctype is None else (ctypes.pointer(actual_size_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return a_string_ctype.value.decode(self._encoding)

    def get_array_for_python_code_custom_type(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        number_of_elements_ctype = _visatype.ViInt32(self.get_array_size_for_python_code())  # case S120
        array_out_size = self.get_array_size_for_python_code()  # case B560
        array_out_ctype = _get_ctypes_pointer_for_buffer(library_type=custom_struct.struct_CustomStruct, size=array_out_size)  # case B560
        error_code = self._library.niFake_GetArrayForPythonCodeCustomType(vi_ctype, number_of_elements_ctype, array_out_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [custom_struct.CustomStruct(array_out_ctype[i]) for i in range(self.get_array_size_for_python_code())]

    def get_array_for_python_code_double(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        number_of_elements_ctype = _visatype.ViInt32(self.get_array_size_for_python_code())  # case S120
        array_out_size = self.get_array_size_for_python_code()  # case B560
        array_out_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=array_out_size)  # case B560
        error_code = self._library.niFake_GetArrayForPythonCodeDouble(vi_ctype, number_of_elements_ctype, array_out_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(array_out_ctype[i]) for i in range(self.get_array_size_for_python_code())]

    def get_array_size_for_python_code(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        size_out_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFake_GetArraySizeForPythonCode(vi_ctype, None if size_out_ctype is None else (ctypes.pointer(size_out_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(size_out_ctype.value)

    def get_array_using_ivi_dance(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        array_size_ctype = _visatype.ViInt32()  # case S170
        array_out_ctype = None  # case B580
        error_code = self._library.niFake_GetArrayUsingIviDance(vi_ctype, array_size_ctype, array_out_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        array_size_ctype = _visatype.ViInt32(error_code)  # case S180
        array_out_size = array_size_ctype.value  # case B590
        array_out_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=array_out_size)  # case B590
        error_code = self._library.niFake_GetArrayUsingIviDance(vi_ctype, array_size_ctype, array_out_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(array_out_ctype[i]) for i in range(array_size_ctype.value)]

    def get_attribute_vi_boolean(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niFake_GetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(attribute_value_ctype.value)

    def get_attribute_vi_int32(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFake_GetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(attribute_value_ctype.value)

    def get_attribute_vi_int64(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt64()  # case S220
        error_code = self._library.niFake_GetAttributeViInt64(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(attribute_value_ctype.value)

    def get_attribute_vi_real64(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niFake_GetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(attribute_value_ctype.value)

    def get_attribute_vi_string(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        attribute_value_ctype = None  # case C050
        error_code = self._library.niFake_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, buffer_size_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        attribute_value_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niFake_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, buffer_size_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return attribute_value_ctype.value.decode(self._encoding)

    def get_cal_date_and_time(self, cal_type):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        cal_type_ctype = _visatype.ViInt32(cal_type)  # case S150
        month_ctype = _visatype.ViInt32()  # case S220
        day_ctype = _visatype.ViInt32()  # case S220
        year_ctype = _visatype.ViInt32()  # case S220
        hour_ctype = _visatype.ViInt32()  # case S220
        minute_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFake_GetCalDateAndTime(vi_ctype, cal_type_ctype, None if month_ctype is None else (ctypes.pointer(month_ctype)), None if day_ctype is None else (ctypes.pointer(day_ctype)), None if year_ctype is None else (ctypes.pointer(year_ctype)), None if hour_ctype is None else (ctypes.pointer(hour_ctype)), None if minute_ctype is None else (ctypes.pointer(minute_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(month_ctype.value), int(day_ctype.value), int(year_ctype.value), int(hour_ctype.value), int(minute_ctype.value)

    def get_cal_interval(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        months_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFake_GetCalInterval(vi_ctype, None if months_ctype is None else (ctypes.pointer(months_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(months_ctype.value)

    def get_channel_names(self, indices):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        indices_ctype = ctypes.create_string_buffer(indices.encode(self._encoding))  # case C020
        name_size_ctype = _visatype.ViInt32()  # case S170
        names_ctype = None  # case C050
        error_code = self._library.niFake_GetChannelNames(vi_ctype, indices_ctype, name_size_ctype, names_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        name_size_ctype = _visatype.ViInt32(error_code)  # case S180
        names_ctype = (_visatype.ViChar * name_size_ctype.value)()  # case C060
        error_code = self._library.niFake_GetChannelNames(vi_ctype, indices_ctype, name_size_ctype, names_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return names_ctype.value.decode(self._encoding)

    def get_custom_type(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        cs_ctype = custom_struct.struct_CustomStruct()  # case S220
        error_code = self._library.niFake_GetCustomType(vi_ctype, None if cs_ctype is None else (ctypes.pointer(cs_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return custom_struct.CustomStruct(cs_ctype)

    def get_custom_type_array(self, number_of_elements):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        number_of_elements_ctype = _visatype.ViInt32(number_of_elements)  # case S210
        cs_size = number_of_elements  # case B600
        cs_ctype = _get_ctypes_pointer_for_buffer(library_type=custom_struct.struct_CustomStruct, size=cs_size)  # case B600
        error_code = self._library.niFake_GetCustomTypeArray(vi_ctype, number_of_elements_ctype, cs_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [custom_struct.CustomStruct(cs_ctype[i]) for i in range(number_of_elements_ctype.value)]

    def get_custom_type_typedef(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        cst_ctype = custom_struct_typedef.struct_CustomStructTypedef()  # case S220
        csnt_ctype = custom_struct_nested_typedef.struct_CustomStructNestedTypedef()  # case S220
        error_code = self._library.niFake_GetCustomTypeTypedef(vi_ctype, None if cst_ctype is None else (ctypes.pointer(cst_ctype)), None if csnt_ctype is None else (ctypes.pointer(csnt_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return custom_struct_typedef.CustomStructTypedef(cst_ctype), custom_struct_nested_typedef.CustomStructNestedTypedef(csnt_ctype)

    def get_enum_value(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        a_quantity_ctype = _visatype.ViInt32()  # case S220
        a_turtle_ctype = _visatype.ViInt16()  # case S220
        error_code = self._library.niFake_GetEnumValue(vi_ctype, None if a_quantity_ctype is None else (ctypes.pointer(a_quantity_ctype)), None if a_turtle_ctype is None else (ctypes.pointer(a_turtle_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(a_quantity_ctype.value), enums.Turtle(a_turtle_ctype.value)

    def get_error(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code_ctype = _visatype.ViStatus()  # case S220
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        description_ctype = None  # case C050
        error_code = self._library.niFake_GetError(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), buffer_size_ctype, description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=True)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        description_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niFake_GetError(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), buffer_size_ctype, description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return int(error_code_ctype.value), description_ctype.value.decode(self._encoding)

    def import_attribute_configuration_buffer(self, configuration):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        size_in_bytes_ctype = _visatype.ViInt32(0 if configuration is None else len(configuration))  # case S160
        configuration_ctype = _get_ctypes_pointer_for_buffer(value=configuration, library_type=_visatype.ViInt8)  # case B550
        error_code = self._library.niFake_ImportAttributeConfigurationBuffer(vi_ctype, size_in_bytes_ctype, configuration_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def init_with_options(self, resource_name, id_query, reset_device, option_string):  # noqa: N802
        resource_name_ctype = ctypes.create_string_buffer(resource_name.encode(self._encoding))  # case C020
        id_query_ctype = _visatype.ViBoolean(id_query)  # case S150
        reset_device_ctype = _visatype.ViBoolean(reset_device)  # case S150
        option_string_ctype = ctypes.create_string_buffer(option_string.encode(self._encoding))  # case C020
        vi_ctype = _visatype.ViSession()  # case S220
        error_code = self._library.niFake_InitWithOptions(resource_name_ctype, id_query_ctype, reset_device_ctype, option_string_ctype, None if vi_ctype is None else (ctypes.pointer(vi_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        self._close_on_exit = True
        return int(vi_ctype.value)

    def initiate(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFake_Initiate(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def lock(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        caller_has_lock_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niFake_LockSession(vi_ctype, None if caller_has_lock_ctype is None else (ctypes.pointer(caller_has_lock_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(caller_has_lock_ctype.value)

    def method_using_whole_and_fractional_numbers(self):  # noqa: N802
        whole_number_ctype = _visatype.ViInt32()  # case S220
        fractional_number_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niFake_MethodUsingWholeAndFractionalNumbers(None if whole_number_ctype is None else (ctypes.pointer(whole_number_ctype)), None if fractional_number_ctype is None else (ctypes.pointer(fractional_number_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(whole_number_ctype.value), float(fractional_number_ctype.value)

    def method_with_grpc_only_param(self, simple_param):  # noqa: N802
        simple_param_ctype = _visatype.ViInt32(simple_param)  # case S150
        error_code = self._library.niFake_MethodWithGrpcOnlyParam(simple_param_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def method_with_proto_only_parameter(self, attribute_value):  # noqa: N802
        attribute_value_ctype = _visatype.ViInt32(attribute_value)  # case S150
        error_code = self._library.niFake_MethodWithProtoOnlyParameter(attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def multiple_array_types(self, output_array_size, input_array_of_floats, input_array_of_integers):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        output_array_size_ctype = _visatype.ViInt32(output_array_size)  # case S210
        output_array_size = output_array_size  # case B600
        output_array_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=output_array_size)  # case B600
        output_array_of_fixed_length_size = 3  # case B570
        output_array_of_fixed_length_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=output_array_of_fixed_length_size)  # case B570
        input_array_sizes_ctype = _visatype.ViInt32(0 if input_array_of_floats is None else len(input_array_of_floats))  # case S160
        if input_array_of_integers is not None and len(input_array_of_integers) != len(input_array_of_floats):  # case S160
            raise ValueError("Length of input_array_of_integers and input_array_of_floats parameters do not match.")  # case S160
        input_array_of_floats_ctype = _get_ctypes_pointer_for_buffer(value=input_array_of_floats, library_type=_visatype.ViReal64)  # case B550
        input_array_of_integers_ctype = _get_ctypes_pointer_for_buffer(value=input_array_of_integers, library_type=_visatype.ViInt16)  # case B550
        error_code = self._library.niFake_MultipleArrayTypes(vi_ctype, output_array_size_ctype, output_array_ctype, output_array_of_fixed_length_ctype, input_array_sizes_ctype, input_array_of_floats_ctype, input_array_of_integers_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(output_array_ctype[i]) for i in range(output_array_size_ctype.value)], [float(output_array_of_fixed_length_ctype[i]) for i in range(3)]

    def multiple_arrays_same_size(self, values1, values2, values3, values4):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        values1_ctype = _get_ctypes_pointer_for_buffer(value=values1, library_type=_visatype.ViReal64)  # case B550
        values2_ctype = _get_ctypes_pointer_for_buffer(value=values2, library_type=_visatype.ViReal64)  # case B550
        values3_ctype = _get_ctypes_pointer_for_buffer(value=values3, library_type=_visatype.ViReal64)  # case B550
        values4_ctype = _get_ctypes_pointer_for_buffer(value=values4, library_type=_visatype.ViReal64)  # case B550
        size_ctype = _visatype.ViInt32(0 if values1 is None else len(values1))  # case S160
        if values2 is not None and len(values2) != len(values1):  # case S160
            raise ValueError("Length of values2 and values1 parameters do not match.")  # case S160
        if values3 is not None and len(values3) != len(values1):  # case S160
            raise ValueError("Length of values3 and values1 parameters do not match.")  # case S160
        if values4 is not None and len(values4) != len(values1):  # case S160
            raise ValueError("Length of values4 and values1 parameters do not match.")  # case S160
        error_code = self._library.niFake_MultipleArraysSameSize(vi_ctype, values1_ctype, values2_ctype, values3_ctype, values4_ctype, size_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def one_input_function(self, a_number):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        a_number_ctype = _visatype.ViInt32(a_number)  # case S150
        error_code = self._library.niFake_OneInputFunction(vi_ctype, a_number_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def parameters_are_multiple_types(self, a_boolean, an_int32, an_int64, an_int_enum, a_float, a_float_enum, string_size, a_string):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        a_boolean_ctype = _visatype.ViBoolean(a_boolean)  # case S150
        an_int32_ctype = _visatype.ViInt32(an_int32)  # case S150
        an_int64_ctype = _visatype.ViInt64(an_int64)  # case S150
        an_int_enum_ctype = _visatype.ViInt16(an_int_enum.value)  # case S130
        a_float_ctype = _visatype.ViReal64(a_float)  # case S150
        a_float_enum_ctype = _visatype.ViReal64(a_float_enum.value)  # case S130
        string_size_ctype = _visatype.ViInt32(string_size)  # case S150
        a_string_ctype = ctypes.create_string_buffer(a_string.encode(self._encoding))  # case C020
        error_code = self._library.niFake_ParametersAreMultipleTypes(vi_ctype, a_boolean_ctype, an_int32_ctype, an_int64_ctype, an_int_enum_ctype, a_float_ctype, a_float_enum_ctype, string_size_ctype, a_string_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def simple_function(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFake_PoorlyNamedSimpleFunction(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def read(self, maximum_time):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        maximum_time_ctype = _visatype.ViReal64(maximum_time)  # case S150
        reading_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niFake_Read(vi_ctype, maximum_time_ctype, None if reading_ctype is None else (ctypes.pointer(reading_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(reading_ctype.value)

    def read_from_channel(self, channel_name, maximum_time):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        maximum_time_ctype = _visatype.ViInt32(maximum_time)  # case S150
        reading_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niFake_ReadFromChannel(vi_ctype, channel_name_ctype, maximum_time_ctype, None if reading_ctype is None else (ctypes.pointer(reading_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(reading_ctype.value)

    def return_a_number_and_a_string(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        a_number_ctype = _visatype.ViInt16()  # case S220
        a_string_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library.niFake_ReturnANumberAndAString(vi_ctype, None if a_number_ctype is None else (ctypes.pointer(a_number_ctype)), a_string_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(a_number_ctype.value), a_string_ctype.value.decode(self._encoding)

    def return_duration_in_seconds(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        timedelta_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niFake_ReturnDurationInSeconds(vi_ctype, None if timedelta_ctype is None else (ctypes.pointer(timedelta_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(timedelta_ctype.value)

    def return_list_of_durations_in_seconds(self, number_of_elements):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        number_of_elements_ctype = _visatype.ViInt32(number_of_elements)  # case S210
        timedeltas_size = number_of_elements  # case B600
        timedeltas_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=timedeltas_size)  # case B600
        error_code = self._library.niFake_ReturnListOfDurationsInSeconds(vi_ctype, number_of_elements_ctype, timedeltas_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(timedeltas_ctype[i]) for i in range(number_of_elements_ctype.value)]

    def return_multiple_types(self, array_size):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        a_boolean_ctype = _visatype.ViBoolean()  # case S220
        an_int32_ctype = _visatype.ViInt32()  # case S220
        an_int64_ctype = _visatype.ViInt64()  # case S220
        an_int_enum_ctype = _visatype.ViInt16()  # case S220
        a_float_ctype = _visatype.ViReal64()  # case S220
        a_float_enum_ctype = _visatype.ViReal64()  # case S220
        array_size_ctype = _visatype.ViInt32(array_size)  # case S210
        an_array_size = array_size  # case B600
        an_array_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=an_array_size)  # case B600
        string_size_ctype = _visatype.ViInt32()  # case S170
        a_string_ctype = None  # case C050
        error_code = self._library.niFake_ReturnMultipleTypes(vi_ctype, None if a_boolean_ctype is None else (ctypes.pointer(a_boolean_ctype)), None if an_int32_ctype is None else (ctypes.pointer(an_int32_ctype)), None if an_int64_ctype is None else (ctypes.pointer(an_int64_ctype)), None if an_int_enum_ctype is None else (ctypes.pointer(an_int_enum_ctype)), None if a_float_ctype is None else (ctypes.pointer(a_float_ctype)), None if a_float_enum_ctype is None else (ctypes.pointer(a_float_enum_ctype)), array_size_ctype, an_array_ctype, string_size_ctype, a_string_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        string_size_ctype = _visatype.ViInt32(error_code)  # case S180
        a_string_ctype = (_visatype.ViChar * string_size_ctype.value)()  # case C060
        error_code = self._library.niFake_ReturnMultipleTypes(vi_ctype, None if a_boolean_ctype is None else (ctypes.pointer(a_boolean_ctype)), None if an_int32_ctype is None else (ctypes.pointer(an_int32_ctype)), None if an_int64_ctype is None else (ctypes.pointer(an_int64_ctype)), None if an_int_enum_ctype is None else (ctypes.pointer(an_int_enum_ctype)), None if a_float_ctype is None else (ctypes.pointer(a_float_ctype)), None if a_float_enum_ctype is None else (ctypes.pointer(a_float_enum_ctype)), array_size_ctype, an_array_ctype, string_size_ctype, a_string_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(a_boolean_ctype.value), int(an_int32_ctype.value), int(an_int64_ctype.value), enums.Turtle(an_int_enum_ctype.value), float(a_float_ctype.value), enums.FloatEnum(a_float_enum_ctype.value), [float(an_array_ctype[i]) for i in range(array_size_ctype.value)], a_string_ctype.value.decode(self._encoding)

    def set_attribute_vi_boolean(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViBoolean(attribute_value)  # case S150
        error_code = self._library.niFake_SetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_int32(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt32(attribute_value)  # case S150
        error_code = self._library.niFake_SetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_int64(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt64(attribute_value)  # case S150
        error_code = self._library.niFake_SetAttributeViInt64(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_real64(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViReal64(attribute_value)  # case S150
        error_code = self._library.niFake_SetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_string(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = ctypes.create_string_buffer(attribute_value.encode(self._encoding))  # case C020
        error_code = self._library.niFake_SetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_custom_type(self, cs):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        cs_ctype = custom_struct.struct_CustomStruct(cs)  # case S150
        error_code = self._library.niFake_SetCustomType(vi_ctype, cs_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_custom_type_array(self, cs):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        number_of_elements_ctype = _visatype.ViInt32(0 if cs is None else len(cs))  # case S160
        cs_ctype = _get_ctypes_pointer_for_buffer([custom_struct.struct_CustomStruct(c) for c in cs], library_type=custom_struct.struct_CustomStruct)  # case B540
        error_code = self._library.niFake_SetCustomTypeArray(vi_ctype, number_of_elements_ctype, cs_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def string_valued_enum_input_function_with_defaults(self, a_mobile_os_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        a_mobile_os_name_ctype = ctypes.create_string_buffer(a_mobile_os_name.value.encode(self._encoding))  # case C030
        error_code = self._library.niFake_StringValuedEnumInputFunctionWithDefaults(vi_ctype, a_mobile_os_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def two_input_function(self, a_number, a_string):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        a_number_ctype = _visatype.ViReal64(a_number)  # case S150
        a_string_ctype = ctypes.create_string_buffer(a_string.encode(self._encoding))  # case C020
        error_code = self._library.niFake_TwoInputFunction(vi_ctype, a_number_ctype, a_string_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def unlock(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        caller_has_lock_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niFake_UnlockSession(vi_ctype, None if caller_has_lock_ctype is None else (ctypes.pointer(caller_has_lock_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(caller_has_lock_ctype.value)

    def use64_bit_number(self, input):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        input_ctype = _visatype.ViInt64(input)  # case S150
        output_ctype = _visatype.ViInt64()  # case S220
        error_code = self._library.niFake_Use64BitNumber(vi_ctype, input_ctype, None if output_ctype is None else (ctypes.pointer(output_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(output_ctype.value)

    def write_waveform(self, waveform):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        number_of_samples_ctype = _visatype.ViInt32(0 if waveform is None else len(waveform))  # case S160
        waveform_array = _convert_to_array(value=waveform, array_type="d")  # case B550
        waveform_ctype = _get_ctypes_pointer_for_buffer(value=waveform_array, library_type=_visatype.ViReal64)  # case B550
        error_code = self._library.niFake_WriteWaveform(vi_ctype, number_of_samples_ctype, waveform_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def write_waveform_numpy(self, waveform):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        number_of_samples_ctype = _visatype.ViInt32(0 if waveform is None else len(waveform))  # case S160
        waveform_ctype = _get_ctypes_pointer_for_buffer(value=waveform)  # case B510
        error_code = self._library.niFake_WriteWaveform(vi_ctype, number_of_samples_ctype, waveform_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def close(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFake_close(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def error_message(self, error_code):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code_ctype = _visatype.ViStatus(error_code)  # case S150
        error_message_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library.niFake_error_message(vi_ctype, error_code_ctype, error_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return error_message_ctype.value.decode(self._encoding)

    def self_test(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        self_test_result_ctype = _visatype.ViInt16()  # case S220
        self_test_message_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library.niFake_self_test(vi_ctype, None if self_test_result_ctype is None else (ctypes.pointer(self_test_result_ctype)), self_test_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(self_test_result_ctype.value), self_test_message_ctype.value.decode(self._encoding)
