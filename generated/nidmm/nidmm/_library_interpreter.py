# -*- coding: utf-8 -*-
# This file was generated

import array
import ctypes
import hightime  # noqa: F401
import nidmm._converters as _converters  # noqa: F401
import nidmm._library_singleton as _library_singleton
import nidmm._visatype as _visatype
import nidmm.enums as enums
import nidmm.errors as errors


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


class LibraryInterpreter(object):
    '''Library C<->Python interpreter.'''

    def __init__(self, encoding):
        self._encoding = encoding
        self._library = _library_singleton.get()

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
        error_code = self._library.abort(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_measurement_absolute(self, session, measurement_function, range, resolution_absolute):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        measurement_function_ctype = _visatype.ViInt32(measurement_function.value)  # case S130
        range_ctype = _visatype.ViReal64(range)  # case S150
        resolution_absolute_ctype = _visatype.ViReal64(resolution_absolute)  # case S150
        error_code = self._library.configure_measurement_absolute(vi_ctype, measurement_function_ctype, range_ctype, resolution_absolute_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_measurement_digits(self, session, measurement_function, range, resolution_digits):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        measurement_function_ctype = _visatype.ViInt32(measurement_function.value)  # case S130
        range_ctype = _visatype.ViReal64(range)  # case S150
        resolution_digits_ctype = _visatype.ViReal64(resolution_digits)  # case S150
        error_code = self._library.configure_measurement_digits(vi_ctype, measurement_function_ctype, range_ctype, resolution_digits_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_multi_point(self, session, trigger_count, sample_count, sample_trigger=enums.SampleTrigger.IMMEDIATE, sample_interval=hightime.timedelta(seconds=-1)):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        trigger_count_ctype = _visatype.ViInt32(trigger_count)  # case S150
        sample_count_ctype = _visatype.ViInt32(sample_count)  # case S150
        sample_trigger_ctype = _visatype.ViInt32(sample_trigger.value)  # case S130
        sample_interval_ctype = _converters.convert_timedelta_to_seconds_real64(sample_interval)  # case S140
        error_code = self._library.configure_multi_point(vi_ctype, trigger_count_ctype, sample_count_ctype, sample_trigger_ctype, sample_interval_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_rtd_custom(self, session, rtd_a, rtd_b, rtd_c):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        rtd_a_ctype = _visatype.ViReal64(rtd_a)  # case S150
        rtd_b_ctype = _visatype.ViReal64(rtd_b)  # case S150
        rtd_c_ctype = _visatype.ViReal64(rtd_c)  # case S150
        error_code = self._library.configure_rtd_custom(vi_ctype, rtd_a_ctype, rtd_b_ctype, rtd_c_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_rtd_type(self, session, rtd_type, rtd_resistance):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        rtd_type_ctype = _visatype.ViInt32(rtd_type.value)  # case S130
        rtd_resistance_ctype = _visatype.ViReal64(rtd_resistance)  # case S150
        error_code = self._library.configure_rtd_type(vi_ctype, rtd_type_ctype, rtd_resistance_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_thermistor_custom(self, session, thermistor_a, thermistor_b, thermistor_c):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        thermistor_a_ctype = _visatype.ViReal64(thermistor_a)  # case S150
        thermistor_b_ctype = _visatype.ViReal64(thermistor_b)  # case S150
        thermistor_c_ctype = _visatype.ViReal64(thermistor_c)  # case S150
        error_code = self._library.configure_thermistor_custom(vi_ctype, thermistor_a_ctype, thermistor_b_ctype, thermistor_c_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_thermocouple(self, session, thermocouple_type, reference_junction_type=enums.ThermocoupleReferenceJunctionType.FIXED):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        thermocouple_type_ctype = _visatype.ViInt32(thermocouple_type.value)  # case S130
        reference_junction_type_ctype = _visatype.ViInt32(reference_junction_type.value)  # case S130
        error_code = self._library.configure_thermocouple(vi_ctype, thermocouple_type_ctype, reference_junction_type_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_trigger(self, session, trigger_source, trigger_delay=hightime.timedelta(seconds=-1)):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        trigger_source_ctype = _visatype.ViInt32(trigger_source.value)  # case S130
        trigger_delay_ctype = _converters.convert_timedelta_to_seconds_real64(trigger_delay)  # case S140
        error_code = self._library.configure_trigger(vi_ctype, trigger_source_ctype, trigger_delay_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_waveform_acquisition(self, session, measurement_function, range, rate, waveform_points):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        measurement_function_ctype = _visatype.ViInt32(measurement_function.value)  # case S130
        range_ctype = _visatype.ViReal64(range)  # case S150
        rate_ctype = _visatype.ViReal64(rate)  # case S150
        waveform_points_ctype = _visatype.ViInt32(waveform_points)  # case S150
        error_code = self._library.configure_waveform_acquisition(vi_ctype, measurement_function_ctype, range_ctype, rate_ctype, waveform_points_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disable(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        error_code = self._library.disable(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def export_attribute_configuration_buffer(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        size_ctype = _visatype.ViInt32()  # case S170
        configuration_ctype = None  # case B580
        error_code = self._library.export_attribute_configuration_buffer(vi_ctype, size_ctype, configuration_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=False)
        size_ctype = _visatype.ViInt32(error_code)  # case S180
        configuration_size = size_ctype.value  # case B590
        configuration_array = array.array("b", [0] * configuration_size)  # case B590
        configuration_ctype = get_ctypes_pointer_for_buffer(value=configuration_array, library_type=_visatype.ViInt8)  # case B590
        error_code = self._library.export_attribute_configuration_buffer(vi_ctype, size_ctype, configuration_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return _converters.convert_to_bytes(configuration_array)

    def export_attribute_configuration_file(self, session, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.export_attribute_configuration_file(vi_ctype, file_path_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def fetch(self, session, maximum_time=hightime.timedelta(milliseconds=-1)):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        maximum_time_ctype = _converters.convert_timedelta_to_milliseconds_int32(maximum_time)  # case S140
        reading_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.fetch(vi_ctype, maximum_time_ctype, None if reading_ctype is None else (ctypes.pointer(reading_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return float(reading_ctype.value)

    def fetch_multi_point(self, session, array_size, maximum_time=hightime.timedelta(milliseconds=-1)):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        maximum_time_ctype = _converters.convert_timedelta_to_milliseconds_int32(maximum_time)  # case S140
        array_size_ctype = _visatype.ViInt32(array_size)  # case S210
        reading_array_size = array_size  # case B600
        reading_array_array = array.array("d", [0] * reading_array_size)  # case B600
        reading_array_ctype = get_ctypes_pointer_for_buffer(value=reading_array_array, library_type=_visatype.ViReal64)  # case B600
        actual_number_of_points_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.fetch_multi_point(vi_ctype, maximum_time_ctype, array_size_ctype, reading_array_ctype, None if actual_number_of_points_ctype is None else (ctypes.pointer(actual_number_of_points_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return reading_array_array

    def fetch_waveform(self, session, array_size, maximum_time=hightime.timedelta(milliseconds=-1)):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        maximum_time_ctype = _converters.convert_timedelta_to_milliseconds_int32(maximum_time)  # case S140
        array_size_ctype = _visatype.ViInt32(array_size)  # case S210
        waveform_array_size = array_size  # case B600
        waveform_array_array = array.array("d", [0] * waveform_array_size)  # case B600
        waveform_array_ctype = get_ctypes_pointer_for_buffer(value=waveform_array_array, library_type=_visatype.ViReal64)  # case B600
        actual_number_of_points_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.fetch_waveform(vi_ctype, maximum_time_ctype, array_size_ctype, waveform_array_ctype, None if actual_number_of_points_ctype is None else (ctypes.pointer(actual_number_of_points_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return waveform_array_array

    def fetch_waveform_into(self, session, waveform_array, maximum_time):  # noqa: N802
        array_size = len(waveform_array)
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        maximum_time_ctype = _converters.convert_timedelta_to_milliseconds_int32(maximum_time)  # case S140
        array_size_ctype = _visatype.ViInt32(array_size)  # case S210
        waveform_array_ctype = get_ctypes_pointer_for_buffer(value=waveform_array)  # case B510
        actual_number_of_points_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.fetch_waveform(vi_ctype, maximum_time_ctype, array_size_ctype, waveform_array_ctype, None if actual_number_of_points_ctype is None else (ctypes.pointer(actual_number_of_points_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _get_attribute_vi_boolean(self, session, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library._get_attribute_vi_boolean(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(attribute_value_ctype.value)

    def _get_attribute_vi_int32(self, session, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library._get_attribute_vi_int32(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(attribute_value_ctype.value)

    def _get_attribute_vi_real64(self, session, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library._get_attribute_vi_real64(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return float(attribute_value_ctype.value)

    def _get_attribute_vi_string(self, session, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        attribute_value_ctype = None  # case C050
        error_code = self._library._get_attribute_vi_string(vi_ctype, channel_name_ctype, attribute_id_ctype, buffer_size_ctype, attribute_value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        attribute_value_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library._get_attribute_vi_string(vi_ctype, channel_name_ctype, attribute_id_ctype, buffer_size_ctype, attribute_value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return attribute_value_ctype.value.decode(self._encoding)

    def _get_cal_date_and_time(self, session, cal_type):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        cal_type_ctype = _visatype.ViInt32(cal_type)  # case S150
        month_ctype = _visatype.ViInt32()  # case S220
        day_ctype = _visatype.ViInt32()  # case S220
        year_ctype = _visatype.ViInt32()  # case S220
        hour_ctype = _visatype.ViInt32()  # case S220
        minute_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library._get_cal_date_and_time(vi_ctype, cal_type_ctype, None if month_ctype is None else (ctypes.pointer(month_ctype)), None if day_ctype is None else (ctypes.pointer(day_ctype)), None if year_ctype is None else (ctypes.pointer(year_ctype)), None if hour_ctype is None else (ctypes.pointer(hour_ctype)), None if minute_ctype is None else (ctypes.pointer(minute_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(month_ctype.value), int(day_ctype.value), int(year_ctype.value), int(hour_ctype.value), int(minute_ctype.value)

    def get_dev_temp(self, session, options=""):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        options_ctype = ctypes.create_string_buffer(options.encode(self._encoding))  # case C020
        temperature_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.get_dev_temp(vi_ctype, options_ctype, None if temperature_ctype is None else (ctypes.pointer(temperature_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

    def _get_error(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        error_code_ctype = _visatype.ViStatus()  # case S220
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        description_ctype = None  # case C050
        error_code = self._library._get_error(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), buffer_size_ctype, description_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=True)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        description_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library._get_error(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), buffer_size_ctype, description_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=True)
        return int(error_code_ctype.value), description_ctype.value.decode(self._encoding)

    def get_ext_cal_recommended_interval(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        months_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.get_ext_cal_recommended_interval(vi_ctype, None if months_ctype is None else (ctypes.pointer(months_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return _converters.convert_month_to_timedelta(int(months_ctype.value))

    def get_last_cal_temp(self, session, cal_type):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        cal_type_ctype = _visatype.ViInt32(cal_type)  # case S150
        temperature_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.get_last_cal_temp(vi_ctype, cal_type_ctype, None if temperature_ctype is None else (ctypes.pointer(temperature_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

    def get_self_cal_supported(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        self_cal_supported_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.get_self_cal_supported(vi_ctype, None if self_cal_supported_ctype is None else (ctypes.pointer(self_cal_supported_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(self_cal_supported_ctype.value)

    def import_attribute_configuration_buffer(self, session, configuration):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        size_ctype = _visatype.ViInt32(0 if configuration is None else len(configuration))  # case S160
        configuration_converted = _converters.convert_to_bytes(configuration)  # case B520
        configuration_ctype = get_ctypes_pointer_for_buffer(value=configuration_converted, library_type=_visatype.ViInt8)  # case B520
        error_code = self._library.import_attribute_configuration_buffer(vi_ctype, size_ctype, configuration_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def import_attribute_configuration_file(self, session, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.import_attribute_configuration_file(vi_ctype, file_path_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _init_with_options(self, session, resource_name, id_query=False, reset_device=False, option_string=""):  # noqa: N802
        resource_name_ctype = ctypes.create_string_buffer(resource_name.encode(self._encoding))  # case C020
        id_query_ctype = _visatype.ViBoolean(id_query)  # case S150
        reset_device_ctype = _visatype.ViBoolean(reset_device)  # case S150
        option_string_ctype = ctypes.create_string_buffer(_converters.convert_init_with_options_dictionary(option_string).encode(self._encoding))  # case C040
        vi_ctype = _visatype.ViSession()  # case S220
        error_code = self._library._init_with_options(resource_name_ctype, id_query_ctype, reset_device_ctype, option_string_ctype, None if vi_ctype is None else (ctypes.pointer(vi_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(vi_ctype.value)

    def _initiate(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        error_code = self._library._initiate(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def lock(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        caller_has_lock_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.lock(vi_ctype, None if caller_has_lock_ctype is None else (ctypes.pointer(caller_has_lock_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(caller_has_lock_ctype.value)

    def perform_open_cable_comp(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        conductance_ctype = _visatype.ViReal64()  # case S220
        susceptance_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.perform_open_cable_comp(vi_ctype, None if conductance_ctype is None else (ctypes.pointer(conductance_ctype)), None if susceptance_ctype is None else (ctypes.pointer(susceptance_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return float(conductance_ctype.value), float(susceptance_ctype.value)

    def perform_short_cable_comp(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        resistance_ctype = _visatype.ViReal64()  # case S220
        reactance_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.perform_short_cable_comp(vi_ctype, None if resistance_ctype is None else (ctypes.pointer(resistance_ctype)), None if reactance_ctype is None else (ctypes.pointer(reactance_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return float(resistance_ctype.value), float(reactance_ctype.value)

    def read(self, session, maximum_time=hightime.timedelta(milliseconds=-1)):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        maximum_time_ctype = _converters.convert_timedelta_to_milliseconds_int32(maximum_time)  # case S140
        reading_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.read(vi_ctype, maximum_time_ctype, None if reading_ctype is None else (ctypes.pointer(reading_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return float(reading_ctype.value)

    def read_multi_point(self, session, array_size, maximum_time=hightime.timedelta(milliseconds=-1)):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        maximum_time_ctype = _converters.convert_timedelta_to_milliseconds_int32(maximum_time)  # case S140
        array_size_ctype = _visatype.ViInt32(array_size)  # case S210
        reading_array_size = array_size  # case B600
        reading_array_array = array.array("d", [0] * reading_array_size)  # case B600
        reading_array_ctype = get_ctypes_pointer_for_buffer(value=reading_array_array, library_type=_visatype.ViReal64)  # case B600
        actual_number_of_points_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.read_multi_point(vi_ctype, maximum_time_ctype, array_size_ctype, reading_array_ctype, None if actual_number_of_points_ctype is None else (ctypes.pointer(actual_number_of_points_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return reading_array_array

    def read_status(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        acquisition_backlog_ctype = _visatype.ViInt32()  # case S220
        acquisition_status_ctype = _visatype.ViInt16()  # case S220
        error_code = self._library.read_status(vi_ctype, None if acquisition_backlog_ctype is None else (ctypes.pointer(acquisition_backlog_ctype)), None if acquisition_status_ctype is None else (ctypes.pointer(acquisition_status_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(acquisition_backlog_ctype.value), enums.AcquisitionStatus(acquisition_status_ctype.value)

    def read_waveform(self, session, array_size, maximum_time=hightime.timedelta(milliseconds=-1)):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        maximum_time_ctype = _converters.convert_timedelta_to_milliseconds_int32(maximum_time)  # case S140
        array_size_ctype = _visatype.ViInt32(array_size)  # case S210
        waveform_array_size = array_size  # case B600
        waveform_array_array = array.array("d", [0] * waveform_array_size)  # case B600
        waveform_array_ctype = get_ctypes_pointer_for_buffer(value=waveform_array_array, library_type=_visatype.ViReal64)  # case B600
        actual_number_of_points_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.read_waveform(vi_ctype, maximum_time_ctype, array_size_ctype, waveform_array_ctype, None if actual_number_of_points_ctype is None else (ctypes.pointer(actual_number_of_points_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return waveform_array_array

    def reset_with_defaults(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        error_code = self._library.reset_with_defaults(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def self_cal(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        error_code = self._library.self_cal(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def send_software_trigger(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        error_code = self._library.send_software_trigger(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_boolean(self, session, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViBoolean(attribute_value)  # case S150
        error_code = self._library._set_attribute_vi_boolean(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_int32(self, session, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt32(attribute_value)  # case S150
        error_code = self._library._set_attribute_vi_int32(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_real64(self, session, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViReal64(attribute_value)  # case S150
        error_code = self._library._set_attribute_vi_real64(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_string(self, session, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = ctypes.create_string_buffer(attribute_value.encode(self._encoding))  # case C020
        error_code = self._library._set_attribute_vi_string(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def unlock(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        caller_has_lock_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.unlock(vi_ctype, None if caller_has_lock_ctype is None else (ctypes.pointer(caller_has_lock_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(caller_has_lock_ctype.value)

    def _close(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        error_code = self._library._close(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _error_message(self, session, error_code):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        error_code_ctype = _visatype.ViStatus(error_code)  # case S150
        error_message_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library._error_message(vi_ctype, error_code_ctype, error_message_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=True)
        return error_message_ctype.value.decode(self._encoding)

    def reset(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        error_code = self._library.reset(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _self_test(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        self_test_result_ctype = _visatype.ViInt16()  # case S220
        self_test_message_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library._self_test(vi_ctype, None if self_test_result_ctype is None else (ctypes.pointer(self_test_result_ctype)), self_test_message_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(self_test_result_ctype.value), self_test_message_ctype.value.decode(self._encoding)
