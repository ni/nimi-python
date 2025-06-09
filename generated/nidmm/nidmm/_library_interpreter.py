# -*- coding: utf-8 -*-
# This file was generated

import array
import ctypes
import hightime  # noqa: F401
import platform

import nidmm._library_singleton as _library_singleton
import nidmm._visatype as _visatype
import nidmm.enums as enums  # noqa: F401
import nidmm.errors as errors


_was_runtime_environment_set = None


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
        global _was_runtime_environment_set
        if _was_runtime_environment_set is None:
            try:
                runtime_env = platform.python_implementation()
                version = platform.python_version()
                self.set_runtime_environment(
                    runtime_env,
                    version,
                    '',
                    ''
                )
            except errors.DriverTooOldError:
                pass
            finally:
                _was_runtime_environment_set = True
        # Initialize _vi to 0 for now.
        # Session will directly update it once the driver runtime init function has been called and
        # we have a valid session handle.
        self.set_session_handle()

    def set_session_handle(self, value=0):
        self._vi = value

    def get_session_handle(self):
        return self._vi

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
        error_code = self._library.niDMM_Abort(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_measurement_absolute(self, measurement_function, range, resolution_absolute):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        measurement_function_ctype = _visatype.ViInt32(measurement_function.value)  # case S130
        range_ctype = _visatype.ViReal64(range)  # case S150
        resolution_absolute_ctype = _visatype.ViReal64(resolution_absolute)  # case S150
        error_code = self._library.niDMM_ConfigureMeasurementAbsolute(vi_ctype, measurement_function_ctype, range_ctype, resolution_absolute_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_measurement_digits(self, measurement_function, range, resolution_digits):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        measurement_function_ctype = _visatype.ViInt32(measurement_function.value)  # case S130
        range_ctype = _visatype.ViReal64(range)  # case S150
        resolution_digits_ctype = _visatype.ViReal64(resolution_digits)  # case S150
        error_code = self._library.niDMM_ConfigureMeasurementDigits(vi_ctype, measurement_function_ctype, range_ctype, resolution_digits_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_multi_point(self, trigger_count, sample_count, sample_trigger, sample_interval):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        trigger_count_ctype = _visatype.ViInt32(trigger_count)  # case S150
        sample_count_ctype = _visatype.ViInt32(sample_count)  # case S150
        sample_trigger_ctype = _visatype.ViInt32(sample_trigger.value)  # case S130
        sample_interval_ctype = _visatype.ViReal64(sample_interval)  # case S150
        error_code = self._library.niDMM_ConfigureMultiPoint(vi_ctype, trigger_count_ctype, sample_count_ctype, sample_trigger_ctype, sample_interval_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_rtd_custom(self, rtd_a, rtd_b, rtd_c):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        rtd_a_ctype = _visatype.ViReal64(rtd_a)  # case S150
        rtd_b_ctype = _visatype.ViReal64(rtd_b)  # case S150
        rtd_c_ctype = _visatype.ViReal64(rtd_c)  # case S150
        error_code = self._library.niDMM_ConfigureRTDCustom(vi_ctype, rtd_a_ctype, rtd_b_ctype, rtd_c_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_rtd_type(self, rtd_type, rtd_resistance):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        rtd_type_ctype = _visatype.ViInt32(rtd_type.value)  # case S130
        rtd_resistance_ctype = _visatype.ViReal64(rtd_resistance)  # case S150
        error_code = self._library.niDMM_ConfigureRTDType(vi_ctype, rtd_type_ctype, rtd_resistance_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_thermistor_custom(self, thermistor_a, thermistor_b, thermistor_c):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        thermistor_a_ctype = _visatype.ViReal64(thermistor_a)  # case S150
        thermistor_b_ctype = _visatype.ViReal64(thermistor_b)  # case S150
        thermistor_c_ctype = _visatype.ViReal64(thermistor_c)  # case S150
        error_code = self._library.niDMM_ConfigureThermistorCustom(vi_ctype, thermistor_a_ctype, thermistor_b_ctype, thermistor_c_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_thermocouple(self, thermocouple_type, reference_junction_type):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        thermocouple_type_ctype = _visatype.ViInt32(thermocouple_type.value)  # case S130
        reference_junction_type_ctype = _visatype.ViInt32(reference_junction_type.value)  # case S130
        error_code = self._library.niDMM_ConfigureThermocouple(vi_ctype, thermocouple_type_ctype, reference_junction_type_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_trigger(self, trigger_source, trigger_delay):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        trigger_source_ctype = _visatype.ViInt32(trigger_source.value)  # case S130
        trigger_delay_ctype = _visatype.ViReal64(trigger_delay)  # case S150
        error_code = self._library.niDMM_ConfigureTrigger(vi_ctype, trigger_source_ctype, trigger_delay_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_waveform_acquisition(self, measurement_function, range, rate, waveform_points):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        measurement_function_ctype = _visatype.ViInt32(measurement_function.value)  # case S130
        range_ctype = _visatype.ViReal64(range)  # case S150
        rate_ctype = _visatype.ViReal64(rate)  # case S150
        waveform_points_ctype = _visatype.ViInt32(waveform_points)  # case S150
        error_code = self._library.niDMM_ConfigureWaveformAcquisition(vi_ctype, measurement_function_ctype, range_ctype, rate_ctype, waveform_points_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disable(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDMM_Disable(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def export_attribute_configuration_buffer(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        size_ctype = _visatype.ViInt32()  # case S170
        configuration_ctype = None  # case B580
        error_code = self._library.niDMM_ExportAttributeConfigurationBuffer(vi_ctype, size_ctype, configuration_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        size_ctype = _visatype.ViInt32(error_code)  # case S180
        configuration_size = size_ctype.value  # case B590
        configuration_array = array.array("b", [0]) * configuration_size  # case B590
        configuration_ctype = _get_ctypes_pointer_for_buffer(value=configuration_array, library_type=_visatype.ViInt8)  # case B590
        error_code = self._library.niDMM_ExportAttributeConfigurationBuffer(vi_ctype, size_ctype, configuration_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return configuration_array

    def export_attribute_configuration_file(self, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.niDMM_ExportAttributeConfigurationFile(vi_ctype, file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def fetch(self, maximum_time):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        maximum_time_ctype = _visatype.ViInt32(maximum_time)  # case S150
        reading_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDMM_Fetch(vi_ctype, maximum_time_ctype, None if reading_ctype is None else (ctypes.pointer(reading_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(reading_ctype.value)

    def fetch_multi_point(self, maximum_time, array_size):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        maximum_time_ctype = _visatype.ViInt32(maximum_time)  # case S150
        array_size_ctype = _visatype.ViInt32(array_size)  # case S210
        reading_array_size = array_size  # case B600
        reading_array_array = array.array("d", [0]) * reading_array_size  # case B600
        reading_array_ctype = _get_ctypes_pointer_for_buffer(value=reading_array_array, library_type=_visatype.ViReal64)  # case B600
        actual_number_of_points_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDMM_FetchMultiPoint(vi_ctype, maximum_time_ctype, array_size_ctype, reading_array_ctype, None if actual_number_of_points_ctype is None else (ctypes.pointer(actual_number_of_points_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return reading_array_array

    def fetch_waveform(self, maximum_time, array_size):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        maximum_time_ctype = _visatype.ViInt32(maximum_time)  # case S150
        array_size_ctype = _visatype.ViInt32(array_size)  # case S210
        waveform_array_size = array_size  # case B600
        waveform_array_array = array.array("d", [0]) * waveform_array_size  # case B600
        waveform_array_ctype = _get_ctypes_pointer_for_buffer(value=waveform_array_array, library_type=_visatype.ViReal64)  # case B600
        actual_number_of_points_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDMM_FetchWaveform(vi_ctype, maximum_time_ctype, array_size_ctype, waveform_array_ctype, None if actual_number_of_points_ctype is None else (ctypes.pointer(actual_number_of_points_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return waveform_array_array

    def fetch_waveform_into(self, waveform_array, maximum_time):  # noqa: N802
        array_size = len(waveform_array)
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        maximum_time_ctype = _visatype.ViInt32(maximum_time)  # case S150
        array_size_ctype = _visatype.ViInt32(array_size)  # case S210
        waveform_array_ctype = _get_ctypes_pointer_for_buffer(value=waveform_array)  # case B510
        actual_number_of_points_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDMM_FetchWaveform(vi_ctype, maximum_time_ctype, array_size_ctype, waveform_array_ctype, None if actual_number_of_points_ctype is None else (ctypes.pointer(actual_number_of_points_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def get_attribute_vi_boolean(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niDMM_GetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(attribute_value_ctype.value)

    def get_attribute_vi_int32(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDMM_GetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(attribute_value_ctype.value)

    def get_attribute_vi_real64(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDMM_GetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(attribute_value_ctype.value)

    def get_attribute_vi_string(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        attribute_value_ctype = None  # case C050
        error_code = self._library.niDMM_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, buffer_size_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        attribute_value_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niDMM_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, buffer_size_ctype, attribute_value_ctype)
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
        error_code = self._library.niDMM_GetCalDateAndTime(vi_ctype, cal_type_ctype, None if month_ctype is None else (ctypes.pointer(month_ctype)), None if day_ctype is None else (ctypes.pointer(day_ctype)), None if year_ctype is None else (ctypes.pointer(year_ctype)), None if hour_ctype is None else (ctypes.pointer(hour_ctype)), None if minute_ctype is None else (ctypes.pointer(minute_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(month_ctype.value), int(day_ctype.value), int(year_ctype.value), int(hour_ctype.value), int(minute_ctype.value)

    def get_dev_temp(self, options):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        options_ctype = ctypes.create_string_buffer(options.encode(self._encoding))  # case C020
        temperature_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDMM_GetDevTemp(vi_ctype, options_ctype, None if temperature_ctype is None else (ctypes.pointer(temperature_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

    def get_error(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code_ctype = _visatype.ViStatus()  # case S220
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        description_ctype = None  # case C050
        error_code = self._library.niDMM_GetError(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), buffer_size_ctype, description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=True)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        description_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niDMM_GetError(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), buffer_size_ctype, description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return int(error_code_ctype.value), description_ctype.value.decode(self._encoding)

    def get_ext_cal_recommended_interval(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        months_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDMM_GetExtCalRecommendedInterval(vi_ctype, None if months_ctype is None else (ctypes.pointer(months_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(months_ctype.value)

    def get_last_cal_temp(self, cal_type):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        cal_type_ctype = _visatype.ViInt32(cal_type)  # case S150
        temperature_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDMM_GetLastCalTemp(vi_ctype, cal_type_ctype, None if temperature_ctype is None else (ctypes.pointer(temperature_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

    def get_self_cal_supported(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        self_cal_supported_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niDMM_GetSelfCalSupported(vi_ctype, None if self_cal_supported_ctype is None else (ctypes.pointer(self_cal_supported_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(self_cal_supported_ctype.value)

    def import_attribute_configuration_buffer(self, configuration):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        size_ctype = _visatype.ViInt32(0 if configuration is None else len(configuration))  # case S160
        configuration_ctype = _get_ctypes_pointer_for_buffer(value=configuration, library_type=_visatype.ViInt8)  # case B550
        error_code = self._library.niDMM_ImportAttributeConfigurationBuffer(vi_ctype, size_ctype, configuration_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def import_attribute_configuration_file(self, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.niDMM_ImportAttributeConfigurationFile(vi_ctype, file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def init_with_options(self, resource_name, id_query, reset_device, option_string):  # noqa: N802
        resource_name_ctype = ctypes.create_string_buffer(resource_name.encode(self._encoding))  # case C020
        id_query_ctype = _visatype.ViBoolean(id_query)  # case S150
        reset_device_ctype = _visatype.ViBoolean(reset_device)  # case S150
        option_string_ctype = ctypes.create_string_buffer(option_string.encode(self._encoding))  # case C020
        vi_ctype = _visatype.ViSession()  # case S220
        error_code = self._library.niDMM_InitWithOptions(resource_name_ctype, id_query_ctype, reset_device_ctype, option_string_ctype, None if vi_ctype is None else (ctypes.pointer(vi_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        self._close_on_exit = True
        return int(vi_ctype.value)

    def initiate(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDMM_Initiate(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def lock(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDMM_LockSession(vi_ctype, None)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def perform_open_cable_comp(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        conductance_ctype = _visatype.ViReal64()  # case S220
        susceptance_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDMM_PerformOpenCableComp(vi_ctype, None if conductance_ctype is None else (ctypes.pointer(conductance_ctype)), None if susceptance_ctype is None else (ctypes.pointer(susceptance_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(conductance_ctype.value), float(susceptance_ctype.value)

    def perform_short_cable_comp(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        resistance_ctype = _visatype.ViReal64()  # case S220
        reactance_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDMM_PerformShortCableComp(vi_ctype, None if resistance_ctype is None else (ctypes.pointer(resistance_ctype)), None if reactance_ctype is None else (ctypes.pointer(reactance_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(resistance_ctype.value), float(reactance_ctype.value)

    def read(self, maximum_time):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        maximum_time_ctype = _visatype.ViInt32(maximum_time)  # case S150
        reading_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDMM_Read(vi_ctype, maximum_time_ctype, None if reading_ctype is None else (ctypes.pointer(reading_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(reading_ctype.value)

    def read_multi_point(self, maximum_time, array_size):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        maximum_time_ctype = _visatype.ViInt32(maximum_time)  # case S150
        array_size_ctype = _visatype.ViInt32(array_size)  # case S210
        reading_array_size = array_size  # case B600
        reading_array_array = array.array("d", [0]) * reading_array_size  # case B600
        reading_array_ctype = _get_ctypes_pointer_for_buffer(value=reading_array_array, library_type=_visatype.ViReal64)  # case B600
        actual_number_of_points_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDMM_ReadMultiPoint(vi_ctype, maximum_time_ctype, array_size_ctype, reading_array_ctype, None if actual_number_of_points_ctype is None else (ctypes.pointer(actual_number_of_points_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return reading_array_array

    def read_status(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        acquisition_backlog_ctype = _visatype.ViInt32()  # case S220
        acquisition_status_ctype = _visatype.ViInt16()  # case S220
        error_code = self._library.niDMM_ReadStatus(vi_ctype, None if acquisition_backlog_ctype is None else (ctypes.pointer(acquisition_backlog_ctype)), None if acquisition_status_ctype is None else (ctypes.pointer(acquisition_status_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(acquisition_backlog_ctype.value), enums.AcquisitionStatus(acquisition_status_ctype.value)

    def read_waveform(self, maximum_time, array_size):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        maximum_time_ctype = _visatype.ViInt32(maximum_time)  # case S150
        array_size_ctype = _visatype.ViInt32(array_size)  # case S210
        waveform_array_size = array_size  # case B600
        waveform_array_array = array.array("d", [0]) * waveform_array_size  # case B600
        waveform_array_ctype = _get_ctypes_pointer_for_buffer(value=waveform_array_array, library_type=_visatype.ViReal64)  # case B600
        actual_number_of_points_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDMM_ReadWaveform(vi_ctype, maximum_time_ctype, array_size_ctype, waveform_array_ctype, None if actual_number_of_points_ctype is None else (ctypes.pointer(actual_number_of_points_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return waveform_array_array

    def reset_with_defaults(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDMM_ResetWithDefaults(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def self_cal(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDMM_SelfCal(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def send_software_trigger(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDMM_SendSoftwareTrigger(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_boolean(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViBoolean(attribute_value)  # case S150
        error_code = self._library.niDMM_SetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_int32(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt32(attribute_value)  # case S150
        error_code = self._library.niDMM_SetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_real64(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViReal64(attribute_value)  # case S150
        error_code = self._library.niDMM_SetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_string(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = ctypes.create_string_buffer(attribute_value.encode(self._encoding))  # case C020
        error_code = self._library.niDMM_SetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_runtime_environment(self, environment, environment_version, reserved1, reserved2):  # noqa: N802
        environment_ctype = ctypes.create_string_buffer(environment.encode(self._encoding))  # case C020
        environment_version_ctype = ctypes.create_string_buffer(environment_version.encode(self._encoding))  # case C020
        reserved1_ctype = ctypes.create_string_buffer(reserved1.encode(self._encoding))  # case C020
        reserved2_ctype = ctypes.create_string_buffer(reserved2.encode(self._encoding))  # case C020
        error_code = self._library.niDMM_SetRuntimeEnvironment(environment_ctype, environment_version_ctype, reserved1_ctype, reserved2_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def unlock(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDMM_UnlockSession(vi_ctype, None)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def close(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDMM_close(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def error_message(self, error_code):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code_ctype = _visatype.ViStatus(error_code)  # case S150
        error_message_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library.niDMM_error_message(vi_ctype, error_code_ctype, error_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return error_message_ctype.value.decode(self._encoding)

    def reset(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDMM_reset(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def self_test(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        self_test_result_ctype = _visatype.ViInt16()  # case S220
        self_test_message_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library.niDMM_self_test(vi_ctype, None if self_test_result_ctype is None else (ctypes.pointer(self_test_result_ctype)), self_test_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(self_test_result_ctype.value), self_test_message_ctype.value.decode(self._encoding)
