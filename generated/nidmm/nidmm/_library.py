# -*- coding: utf-8 -*-
# This file was generated

import array  # noqa: F401
import ctypes
import hightime
import nidmm._converters as _converters
import nidmm._visatype as _visatype
import nidmm.enums as enums
import nidmm.errors as errors
import threading

from nidmm._visatype import *  # noqa: F403,H303


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
        self.niDMM_Abort_cfunc = None
        self.niDMM_ConfigureMeasurementAbsolute_cfunc = None
        self.niDMM_ConfigureMeasurementDigits_cfunc = None
        self.niDMM_ConfigureMultiPoint_cfunc = None
        self.niDMM_ConfigureRTDCustom_cfunc = None
        self.niDMM_ConfigureRTDType_cfunc = None
        self.niDMM_ConfigureThermistorCustom_cfunc = None
        self.niDMM_ConfigureThermocouple_cfunc = None
        self.niDMM_ConfigureTrigger_cfunc = None
        self.niDMM_ConfigureWaveformAcquisition_cfunc = None
        self.niDMM_Disable_cfunc = None
        self.niDMM_ExportAttributeConfigurationBuffer_cfunc = None
        self.niDMM_ExportAttributeConfigurationFile_cfunc = None
        self.niDMM_Fetch_cfunc = None
        self.niDMM_FetchMultiPoint_cfunc = None
        self.niDMM_FetchWaveform_cfunc = None
        self.niDMM_GetAttributeViBoolean_cfunc = None
        self.niDMM_GetAttributeViInt32_cfunc = None
        self.niDMM_GetAttributeViReal64_cfunc = None
        self.niDMM_GetAttributeViString_cfunc = None
        self.niDMM_GetCalDateAndTime_cfunc = None
        self.niDMM_GetDevTemp_cfunc = None
        self.niDMM_GetError_cfunc = None
        self.niDMM_GetExtCalRecommendedInterval_cfunc = None
        self.niDMM_GetLastCalTemp_cfunc = None
        self.niDMM_GetSelfCalSupported_cfunc = None
        self.niDMM_ImportAttributeConfigurationBuffer_cfunc = None
        self.niDMM_ImportAttributeConfigurationFile_cfunc = None
        self.niDMM_InitWithOptions_cfunc = None
        self.niDMM_Initiate_cfunc = None
        self.niDMM_LockSession_cfunc = None
        self.niDMM_PerformOpenCableComp_cfunc = None
        self.niDMM_PerformShortCableComp_cfunc = None
        self.niDMM_Read_cfunc = None
        self.niDMM_ReadMultiPoint_cfunc = None
        self.niDMM_ReadStatus_cfunc = None
        self.niDMM_ReadWaveform_cfunc = None
        self.niDMM_ResetWithDefaults_cfunc = None
        self.niDMM_SelfCal_cfunc = None
        self.niDMM_SendSoftwareTrigger_cfunc = None
        self.niDMM_SetAttributeViBoolean_cfunc = None
        self.niDMM_SetAttributeViInt32_cfunc = None
        self.niDMM_SetAttributeViReal64_cfunc = None
        self.niDMM_SetAttributeViString_cfunc = None
        self.niDMM_UnlockSession_cfunc = None
        self.niDMM_close_cfunc = None
        self.niDMM_error_message_cfunc = None
        self.niDMM_reset_cfunc = None
        self.niDMM_self_test_cfunc = None

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
            if self.niDMM_Abort_cfunc is None:
                self.niDMM_Abort_cfunc = self._get_library_function('niDMM_Abort')
                self.niDMM_Abort_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDMM_Abort_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_Abort_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_measurement_absolute(self, session, measurement_function, range, resolution_absolute):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        measurement_function_ctype = _visatype.ViInt32(measurement_function.value)  # case S130
        range_ctype = _visatype.ViReal64(range)  # case S150
        resolution_absolute_ctype = _visatype.ViReal64(resolution_absolute)  # case S150
        with self._func_lock:
            if self.niDMM_ConfigureMeasurementAbsolute_cfunc is None:
                self.niDMM_ConfigureMeasurementAbsolute_cfunc = self._get_library_function('niDMM_ConfigureMeasurementAbsolute')
                self.niDMM_ConfigureMeasurementAbsolute_cfunc.argtypes = [ViSession, ViInt32, ViReal64, ViReal64]  # noqa: F405
                self.niDMM_ConfigureMeasurementAbsolute_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_ConfigureMeasurementAbsolute_cfunc(vi_ctype, measurement_function_ctype, range_ctype, resolution_absolute_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_measurement_digits(self, session, measurement_function, range, resolution_digits):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        measurement_function_ctype = _visatype.ViInt32(measurement_function.value)  # case S130
        range_ctype = _visatype.ViReal64(range)  # case S150
        resolution_digits_ctype = _visatype.ViReal64(resolution_digits)  # case S150
        with self._func_lock:
            if self.niDMM_ConfigureMeasurementDigits_cfunc is None:
                self.niDMM_ConfigureMeasurementDigits_cfunc = self._get_library_function('niDMM_ConfigureMeasurementDigits')
                self.niDMM_ConfigureMeasurementDigits_cfunc.argtypes = [ViSession, ViInt32, ViReal64, ViReal64]  # noqa: F405
                self.niDMM_ConfigureMeasurementDigits_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_ConfigureMeasurementDigits_cfunc(vi_ctype, measurement_function_ctype, range_ctype, resolution_digits_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_multi_point(self, session, trigger_count, sample_count, sample_trigger=enums.SampleTrigger.IMMEDIATE, sample_interval=hightime.timedelta(seconds=-1)):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        trigger_count_ctype = _visatype.ViInt32(trigger_count)  # case S150
        sample_count_ctype = _visatype.ViInt32(sample_count)  # case S150
        sample_trigger_ctype = _visatype.ViInt32(sample_trigger.value)  # case S130
        sample_interval_ctype = _converters.convert_timedelta_to_seconds_real64(sample_interval)  # case S140
        with self._func_lock:
            if self.niDMM_ConfigureMultiPoint_cfunc is None:
                self.niDMM_ConfigureMultiPoint_cfunc = self._get_library_function('niDMM_ConfigureMultiPoint')
                self.niDMM_ConfigureMultiPoint_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ViInt32, ViReal64]  # noqa: F405
                self.niDMM_ConfigureMultiPoint_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_ConfigureMultiPoint_cfunc(vi_ctype, trigger_count_ctype, sample_count_ctype, sample_trigger_ctype, sample_interval_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_rtd_custom(self, session, rtd_a, rtd_b, rtd_c):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        rtd_a_ctype = _visatype.ViReal64(rtd_a)  # case S150
        rtd_b_ctype = _visatype.ViReal64(rtd_b)  # case S150
        rtd_c_ctype = _visatype.ViReal64(rtd_c)  # case S150
        with self._func_lock:
            if self.niDMM_ConfigureRTDCustom_cfunc is None:
                self.niDMM_ConfigureRTDCustom_cfunc = self._get_library_function('niDMM_ConfigureRTDCustom')
                self.niDMM_ConfigureRTDCustom_cfunc.argtypes = [ViSession, ViReal64, ViReal64, ViReal64]  # noqa: F405
                self.niDMM_ConfigureRTDCustom_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_ConfigureRTDCustom_cfunc(vi_ctype, rtd_a_ctype, rtd_b_ctype, rtd_c_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_rtd_type(self, session, rtd_type, rtd_resistance):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        rtd_type_ctype = _visatype.ViInt32(rtd_type.value)  # case S130
        rtd_resistance_ctype = _visatype.ViReal64(rtd_resistance)  # case S150
        with self._func_lock:
            if self.niDMM_ConfigureRTDType_cfunc is None:
                self.niDMM_ConfigureRTDType_cfunc = self._get_library_function('niDMM_ConfigureRTDType')
                self.niDMM_ConfigureRTDType_cfunc.argtypes = [ViSession, ViInt32, ViReal64]  # noqa: F405
                self.niDMM_ConfigureRTDType_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_ConfigureRTDType_cfunc(vi_ctype, rtd_type_ctype, rtd_resistance_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_thermistor_custom(self, session, thermistor_a, thermistor_b, thermistor_c):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        thermistor_a_ctype = _visatype.ViReal64(thermistor_a)  # case S150
        thermistor_b_ctype = _visatype.ViReal64(thermistor_b)  # case S150
        thermistor_c_ctype = _visatype.ViReal64(thermistor_c)  # case S150
        with self._func_lock:
            if self.niDMM_ConfigureThermistorCustom_cfunc is None:
                self.niDMM_ConfigureThermistorCustom_cfunc = self._get_library_function('niDMM_ConfigureThermistorCustom')
                self.niDMM_ConfigureThermistorCustom_cfunc.argtypes = [ViSession, ViReal64, ViReal64, ViReal64]  # noqa: F405
                self.niDMM_ConfigureThermistorCustom_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_ConfigureThermistorCustom_cfunc(vi_ctype, thermistor_a_ctype, thermistor_b_ctype, thermistor_c_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_thermocouple(self, session, thermocouple_type, reference_junction_type=enums.ThermocoupleReferenceJunctionType.FIXED):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        thermocouple_type_ctype = _visatype.ViInt32(thermocouple_type.value)  # case S130
        reference_junction_type_ctype = _visatype.ViInt32(reference_junction_type.value)  # case S130
        with self._func_lock:
            if self.niDMM_ConfigureThermocouple_cfunc is None:
                self.niDMM_ConfigureThermocouple_cfunc = self._get_library_function('niDMM_ConfigureThermocouple')
                self.niDMM_ConfigureThermocouple_cfunc.argtypes = [ViSession, ViInt32, ViInt32]  # noqa: F405
                self.niDMM_ConfigureThermocouple_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_ConfigureThermocouple_cfunc(vi_ctype, thermocouple_type_ctype, reference_junction_type_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_trigger(self, session, trigger_source, trigger_delay=hightime.timedelta(seconds=-1)):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        trigger_source_ctype = _visatype.ViInt32(trigger_source.value)  # case S130
        trigger_delay_ctype = _converters.convert_timedelta_to_seconds_real64(trigger_delay)  # case S140
        with self._func_lock:
            if self.niDMM_ConfigureTrigger_cfunc is None:
                self.niDMM_ConfigureTrigger_cfunc = self._get_library_function('niDMM_ConfigureTrigger')
                self.niDMM_ConfigureTrigger_cfunc.argtypes = [ViSession, ViInt32, ViReal64]  # noqa: F405
                self.niDMM_ConfigureTrigger_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_ConfigureTrigger_cfunc(vi_ctype, trigger_source_ctype, trigger_delay_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_waveform_acquisition(self, session, measurement_function, range, rate, waveform_points):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        measurement_function_ctype = _visatype.ViInt32(measurement_function.value)  # case S130
        range_ctype = _visatype.ViReal64(range)  # case S150
        rate_ctype = _visatype.ViReal64(rate)  # case S150
        waveform_points_ctype = _visatype.ViInt32(waveform_points)  # case S150
        with self._func_lock:
            if self.niDMM_ConfigureWaveformAcquisition_cfunc is None:
                self.niDMM_ConfigureWaveformAcquisition_cfunc = self._get_library_function('niDMM_ConfigureWaveformAcquisition')
                self.niDMM_ConfigureWaveformAcquisition_cfunc.argtypes = [ViSession, ViInt32, ViReal64, ViReal64, ViInt32]  # noqa: F405
                self.niDMM_ConfigureWaveformAcquisition_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_ConfigureWaveformAcquisition_cfunc(vi_ctype, measurement_function_ctype, range_ctype, rate_ctype, waveform_points_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disable(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niDMM_Disable_cfunc is None:
                self.niDMM_Disable_cfunc = self._get_library_function('niDMM_Disable')
                self.niDMM_Disable_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDMM_Disable_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_Disable_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def export_attribute_configuration_buffer(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        size_ctype = _visatype.ViInt32()  # case S170
        configuration_ctype = None  # case B580
        with self._func_lock:
            if self.niDMM_ExportAttributeConfigurationBuffer_cfunc is None:
                self.niDMM_ExportAttributeConfigurationBuffer_cfunc = self._get_library_function('niDMM_ExportAttributeConfigurationBuffer')
                self.niDMM_ExportAttributeConfigurationBuffer_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt8)]  # noqa: F405
                self.niDMM_ExportAttributeConfigurationBuffer_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_ExportAttributeConfigurationBuffer_cfunc(vi_ctype, size_ctype, configuration_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=False)
        size_ctype = _visatype.ViInt32(error_code)  # case S180
        configuration_size = size_ctype.value  # case B590
        configuration_array = array.array("b", [0] * configuration_size)  # case B590
        configuration_ctype = get_ctypes_pointer_for_buffer(value=configuration_array, library_type=_visatype.ViInt8)  # case B590
        error_code = self.niDMM_ExportAttributeConfigurationBuffer_cfunc(vi_ctype, size_ctype, configuration_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return _converters.convert_to_bytes(configuration_array)

    def export_attribute_configuration_file(self, session, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(session._encoding))  # case C020
        with self._func_lock:
            if self.niDMM_ExportAttributeConfigurationFile_cfunc is None:
                self.niDMM_ExportAttributeConfigurationFile_cfunc = self._get_library_function('niDMM_ExportAttributeConfigurationFile')
                self.niDMM_ExportAttributeConfigurationFile_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDMM_ExportAttributeConfigurationFile_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_ExportAttributeConfigurationFile_cfunc(vi_ctype, file_path_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def fetch(self, session, maximum_time=hightime.timedelta(milliseconds=-1)):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        maximum_time_ctype = _converters.convert_timedelta_to_milliseconds_int32(maximum_time)  # case S140
        reading_ctype = _visatype.ViReal64()  # case S220
        with self._func_lock:
            if self.niDMM_Fetch_cfunc is None:
                self.niDMM_Fetch_cfunc = self._get_library_function('niDMM_Fetch')
                self.niDMM_Fetch_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDMM_Fetch_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_Fetch_cfunc(vi_ctype, maximum_time_ctype, None if reading_ctype is None else (ctypes.pointer(reading_ctype)))
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
        with self._func_lock:
            if self.niDMM_FetchMultiPoint_cfunc is None:
                self.niDMM_FetchMultiPoint_cfunc = self._get_library_function('niDMM_FetchMultiPoint')
                self.niDMM_FetchMultiPoint_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDMM_FetchMultiPoint_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_FetchMultiPoint_cfunc(vi_ctype, maximum_time_ctype, array_size_ctype, reading_array_ctype, None if actual_number_of_points_ctype is None else (ctypes.pointer(actual_number_of_points_ctype)))
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
        with self._func_lock:
            if self.niDMM_FetchWaveform_cfunc is None:
                self.niDMM_FetchWaveform_cfunc = self._get_library_function('niDMM_FetchWaveform')
                self.niDMM_FetchWaveform_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDMM_FetchWaveform_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_FetchWaveform_cfunc(vi_ctype, maximum_time_ctype, array_size_ctype, waveform_array_ctype, None if actual_number_of_points_ctype is None else (ctypes.pointer(actual_number_of_points_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return waveform_array_array

    def fetch_waveform_into(self, session, waveform_array, maximum_time):  # noqa: N802
        array_size = len(waveform_array)
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        maximum_time_ctype = _converters.convert_timedelta_to_milliseconds_int32(maximum_time)  # case S140
        array_size_ctype = _visatype.ViInt32(array_size)  # case S210
        waveform_array_ctype = get_ctypes_pointer_for_buffer(value=waveform_array)  # case B510
        actual_number_of_points_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niDMM_FetchWaveform_cfunc is None:
                self.niDMM_FetchWaveform_cfunc = self._get_library_function('niDMM_FetchWaveform')
                self.niDMM_FetchWaveform_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDMM_FetchWaveform_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_FetchWaveform_cfunc(vi_ctype, maximum_time_ctype, array_size_ctype, waveform_array_ctype, None if actual_number_of_points_ctype is None else (ctypes.pointer(actual_number_of_points_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _get_attribute_vi_boolean(self, session, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViBoolean()  # case S220
        with self._func_lock:
            if self.niDMM_GetAttributeViBoolean_cfunc is None:
                self.niDMM_GetAttributeViBoolean_cfunc = self._get_library_function('niDMM_GetAttributeViBoolean')
                self.niDMM_GetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niDMM_GetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_GetAttributeViBoolean_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(attribute_value_ctype.value)

    def _get_attribute_vi_int32(self, session, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niDMM_GetAttributeViInt32_cfunc is None:
                self.niDMM_GetAttributeViInt32_cfunc = self._get_library_function('niDMM_GetAttributeViInt32')
                self.niDMM_GetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDMM_GetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_GetAttributeViInt32_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(attribute_value_ctype.value)

    def _get_attribute_vi_real64(self, session, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViReal64()  # case S220
        with self._func_lock:
            if self.niDMM_GetAttributeViReal64_cfunc is None:
                self.niDMM_GetAttributeViReal64_cfunc = self._get_library_function('niDMM_GetAttributeViReal64')
                self.niDMM_GetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDMM_GetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_GetAttributeViReal64_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return float(attribute_value_ctype.value)

    def _get_attribute_vi_string(self, session, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        attribute_value_ctype = None  # case C050
        with self._func_lock:
            if self.niDMM_GetAttributeViString_cfunc is None:
                self.niDMM_GetAttributeViString_cfunc = self._get_library_function('niDMM_GetAttributeViString')
                self.niDMM_GetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDMM_GetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_GetAttributeViString_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, buffer_size_ctype, attribute_value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        attribute_value_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self.niDMM_GetAttributeViString_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, buffer_size_ctype, attribute_value_ctype)
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
            if self.niDMM_GetCalDateAndTime_cfunc is None:
                self.niDMM_GetCalDateAndTime_cfunc = self._get_library_function('niDMM_GetCalDateAndTime')
                self.niDMM_GetCalDateAndTime_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDMM_GetCalDateAndTime_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_GetCalDateAndTime_cfunc(vi_ctype, cal_type_ctype, None if month_ctype is None else (ctypes.pointer(month_ctype)), None if day_ctype is None else (ctypes.pointer(day_ctype)), None if year_ctype is None else (ctypes.pointer(year_ctype)), None if hour_ctype is None else (ctypes.pointer(hour_ctype)), None if minute_ctype is None else (ctypes.pointer(minute_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(month_ctype.value), int(day_ctype.value), int(year_ctype.value), int(hour_ctype.value), int(minute_ctype.value)

    def get_dev_temp(self, session, options=""):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        options_ctype = ctypes.create_string_buffer(options.encode(session._encoding))  # case C020
        temperature_ctype = _visatype.ViReal64()  # case S220
        with self._func_lock:
            if self.niDMM_GetDevTemp_cfunc is None:
                self.niDMM_GetDevTemp_cfunc = self._get_library_function('niDMM_GetDevTemp')
                self.niDMM_GetDevTemp_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDMM_GetDevTemp_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_GetDevTemp_cfunc(vi_ctype, options_ctype, None if temperature_ctype is None else (ctypes.pointer(temperature_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

    def _get_error(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        error_code_ctype = _visatype.ViStatus()  # case S220
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        description_ctype = None  # case C050
        with self._func_lock:
            if self.niDMM_GetError_cfunc is None:
                self.niDMM_GetError_cfunc = self._get_library_function('niDMM_GetError')
                self.niDMM_GetError_cfunc.argtypes = [ViSession, ctypes.POINTER(ViStatus), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDMM_GetError_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_GetError_cfunc(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), buffer_size_ctype, description_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=True)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        description_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self.niDMM_GetError_cfunc(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), buffer_size_ctype, description_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=True)
        return int(error_code_ctype.value), description_ctype.value.decode(session._encoding)

    def get_ext_cal_recommended_interval(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        months_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niDMM_GetExtCalRecommendedInterval_cfunc is None:
                self.niDMM_GetExtCalRecommendedInterval_cfunc = self._get_library_function('niDMM_GetExtCalRecommendedInterval')
                self.niDMM_GetExtCalRecommendedInterval_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDMM_GetExtCalRecommendedInterval_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_GetExtCalRecommendedInterval_cfunc(vi_ctype, None if months_ctype is None else (ctypes.pointer(months_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return _converters.convert_month_to_timedelta(int(months_ctype.value))

    def get_last_cal_temp(self, session, cal_type):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        cal_type_ctype = _visatype.ViInt32(cal_type)  # case S150
        temperature_ctype = _visatype.ViReal64()  # case S220
        with self._func_lock:
            if self.niDMM_GetLastCalTemp_cfunc is None:
                self.niDMM_GetLastCalTemp_cfunc = self._get_library_function('niDMM_GetLastCalTemp')
                self.niDMM_GetLastCalTemp_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDMM_GetLastCalTemp_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_GetLastCalTemp_cfunc(vi_ctype, cal_type_ctype, None if temperature_ctype is None else (ctypes.pointer(temperature_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

    def get_self_cal_supported(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        self_cal_supported_ctype = _visatype.ViBoolean()  # case S220
        with self._func_lock:
            if self.niDMM_GetSelfCalSupported_cfunc is None:
                self.niDMM_GetSelfCalSupported_cfunc = self._get_library_function('niDMM_GetSelfCalSupported')
                self.niDMM_GetSelfCalSupported_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niDMM_GetSelfCalSupported_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_GetSelfCalSupported_cfunc(vi_ctype, None if self_cal_supported_ctype is None else (ctypes.pointer(self_cal_supported_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(self_cal_supported_ctype.value)

    def import_attribute_configuration_buffer(self, session, configuration):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        size_ctype = _visatype.ViInt32(0 if configuration is None else len(configuration))  # case S160
        configuration_converted = _converters.convert_to_bytes(configuration)  # case B520
        configuration_ctype = get_ctypes_pointer_for_buffer(value=configuration_converted, library_type=_visatype.ViInt8)  # case B520
        with self._func_lock:
            if self.niDMM_ImportAttributeConfigurationBuffer_cfunc is None:
                self.niDMM_ImportAttributeConfigurationBuffer_cfunc = self._get_library_function('niDMM_ImportAttributeConfigurationBuffer')
                self.niDMM_ImportAttributeConfigurationBuffer_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt8)]  # noqa: F405
                self.niDMM_ImportAttributeConfigurationBuffer_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_ImportAttributeConfigurationBuffer_cfunc(vi_ctype, size_ctype, configuration_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def import_attribute_configuration_file(self, session, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(session._encoding))  # case C020
        with self._func_lock:
            if self.niDMM_ImportAttributeConfigurationFile_cfunc is None:
                self.niDMM_ImportAttributeConfigurationFile_cfunc = self._get_library_function('niDMM_ImportAttributeConfigurationFile')
                self.niDMM_ImportAttributeConfigurationFile_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDMM_ImportAttributeConfigurationFile_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_ImportAttributeConfigurationFile_cfunc(vi_ctype, file_path_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _init_with_options(self, session, resource_name, id_query=False, reset_device=False, option_string=""):  # noqa: N802
        resource_name_ctype = ctypes.create_string_buffer(resource_name.encode(session._encoding))  # case C020
        id_query_ctype = _visatype.ViBoolean(id_query)  # case S150
        reset_device_ctype = _visatype.ViBoolean(reset_device)  # case S150
        option_string_ctype = ctypes.create_string_buffer(_converters.convert_init_with_options_dictionary(option_string).encode(session._encoding))  # case C040
        vi_ctype = _visatype.ViSession()  # case S220
        with self._func_lock:
            if self.niDMM_InitWithOptions_cfunc is None:
                self.niDMM_InitWithOptions_cfunc = self._get_library_function('niDMM_InitWithOptions')
                self.niDMM_InitWithOptions_cfunc.argtypes = [ctypes.POINTER(ViChar), ViBoolean, ViBoolean, ctypes.POINTER(ViChar), ctypes.POINTER(ViSession)]  # noqa: F405
                self.niDMM_InitWithOptions_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_InitWithOptions_cfunc(resource_name_ctype, id_query_ctype, reset_device_ctype, option_string_ctype, None if vi_ctype is None else (ctypes.pointer(vi_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(vi_ctype.value)

    def _initiate(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niDMM_Initiate_cfunc is None:
                self.niDMM_Initiate_cfunc = self._get_library_function('niDMM_Initiate')
                self.niDMM_Initiate_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDMM_Initiate_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_Initiate_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def lock(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        caller_has_lock_ctype = _visatype.ViBoolean()  # case S220
        with self._func_lock:
            if self.niDMM_LockSession_cfunc is None:
                self.niDMM_LockSession_cfunc = self._get_library_function('niDMM_LockSession')
                self.niDMM_LockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niDMM_LockSession_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_LockSession_cfunc(vi_ctype, None if caller_has_lock_ctype is None else (ctypes.pointer(caller_has_lock_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(caller_has_lock_ctype.value)

    def perform_open_cable_comp(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        conductance_ctype = _visatype.ViReal64()  # case S220
        susceptance_ctype = _visatype.ViReal64()  # case S220
        with self._func_lock:
            if self.niDMM_PerformOpenCableComp_cfunc is None:
                self.niDMM_PerformOpenCableComp_cfunc = self._get_library_function('niDMM_PerformOpenCableComp')
                self.niDMM_PerformOpenCableComp_cfunc.argtypes = [ViSession, ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDMM_PerformOpenCableComp_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_PerformOpenCableComp_cfunc(vi_ctype, None if conductance_ctype is None else (ctypes.pointer(conductance_ctype)), None if susceptance_ctype is None else (ctypes.pointer(susceptance_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return float(conductance_ctype.value), float(susceptance_ctype.value)

    def perform_short_cable_comp(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        resistance_ctype = _visatype.ViReal64()  # case S220
        reactance_ctype = _visatype.ViReal64()  # case S220
        with self._func_lock:
            if self.niDMM_PerformShortCableComp_cfunc is None:
                self.niDMM_PerformShortCableComp_cfunc = self._get_library_function('niDMM_PerformShortCableComp')
                self.niDMM_PerformShortCableComp_cfunc.argtypes = [ViSession, ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDMM_PerformShortCableComp_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_PerformShortCableComp_cfunc(vi_ctype, None if resistance_ctype is None else (ctypes.pointer(resistance_ctype)), None if reactance_ctype is None else (ctypes.pointer(reactance_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return float(resistance_ctype.value), float(reactance_ctype.value)

    def read(self, session, maximum_time=hightime.timedelta(milliseconds=-1)):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        maximum_time_ctype = _converters.convert_timedelta_to_milliseconds_int32(maximum_time)  # case S140
        reading_ctype = _visatype.ViReal64()  # case S220
        with self._func_lock:
            if self.niDMM_Read_cfunc is None:
                self.niDMM_Read_cfunc = self._get_library_function('niDMM_Read')
                self.niDMM_Read_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDMM_Read_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_Read_cfunc(vi_ctype, maximum_time_ctype, None if reading_ctype is None else (ctypes.pointer(reading_ctype)))
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
        with self._func_lock:
            if self.niDMM_ReadMultiPoint_cfunc is None:
                self.niDMM_ReadMultiPoint_cfunc = self._get_library_function('niDMM_ReadMultiPoint')
                self.niDMM_ReadMultiPoint_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDMM_ReadMultiPoint_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_ReadMultiPoint_cfunc(vi_ctype, maximum_time_ctype, array_size_ctype, reading_array_ctype, None if actual_number_of_points_ctype is None else (ctypes.pointer(actual_number_of_points_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return reading_array_array

    def read_status(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        acquisition_backlog_ctype = _visatype.ViInt32()  # case S220
        acquisition_status_ctype = _visatype.ViInt16()  # case S220
        with self._func_lock:
            if self.niDMM_ReadStatus_cfunc is None:
                self.niDMM_ReadStatus_cfunc = self._get_library_function('niDMM_ReadStatus')
                self.niDMM_ReadStatus_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt16)]  # noqa: F405
                self.niDMM_ReadStatus_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_ReadStatus_cfunc(vi_ctype, None if acquisition_backlog_ctype is None else (ctypes.pointer(acquisition_backlog_ctype)), None if acquisition_status_ctype is None else (ctypes.pointer(acquisition_status_ctype)))
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
        with self._func_lock:
            if self.niDMM_ReadWaveform_cfunc is None:
                self.niDMM_ReadWaveform_cfunc = self._get_library_function('niDMM_ReadWaveform')
                self.niDMM_ReadWaveform_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDMM_ReadWaveform_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_ReadWaveform_cfunc(vi_ctype, maximum_time_ctype, array_size_ctype, waveform_array_ctype, None if actual_number_of_points_ctype is None else (ctypes.pointer(actual_number_of_points_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return waveform_array_array

    def reset_with_defaults(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niDMM_ResetWithDefaults_cfunc is None:
                self.niDMM_ResetWithDefaults_cfunc = self._get_library_function('niDMM_ResetWithDefaults')
                self.niDMM_ResetWithDefaults_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDMM_ResetWithDefaults_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_ResetWithDefaults_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def self_cal(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niDMM_SelfCal_cfunc is None:
                self.niDMM_SelfCal_cfunc = self._get_library_function('niDMM_SelfCal')
                self.niDMM_SelfCal_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDMM_SelfCal_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_SelfCal_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def send_software_trigger(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niDMM_SendSoftwareTrigger_cfunc is None:
                self.niDMM_SendSoftwareTrigger_cfunc = self._get_library_function('niDMM_SendSoftwareTrigger')
                self.niDMM_SendSoftwareTrigger_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDMM_SendSoftwareTrigger_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_SendSoftwareTrigger_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_boolean(self, session, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViBoolean(attribute_value)  # case S150
        with self._func_lock:
            if self.niDMM_SetAttributeViBoolean_cfunc is None:
                self.niDMM_SetAttributeViBoolean_cfunc = self._get_library_function('niDMM_SetAttributeViBoolean')
                self.niDMM_SetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViBoolean]  # noqa: F405
                self.niDMM_SetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_SetAttributeViBoolean_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_int32(self, session, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt32(attribute_value)  # case S150
        with self._func_lock:
            if self.niDMM_SetAttributeViInt32_cfunc is None:
                self.niDMM_SetAttributeViInt32_cfunc = self._get_library_function('niDMM_SetAttributeViInt32')
                self.niDMM_SetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32]  # noqa: F405
                self.niDMM_SetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_SetAttributeViInt32_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_real64(self, session, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViReal64(attribute_value)  # case S150
        with self._func_lock:
            if self.niDMM_SetAttributeViReal64_cfunc is None:
                self.niDMM_SetAttributeViReal64_cfunc = self._get_library_function('niDMM_SetAttributeViReal64')
                self.niDMM_SetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViReal64]  # noqa: F405
                self.niDMM_SetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_SetAttributeViReal64_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_string(self, session, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = ctypes.create_string_buffer(attribute_value.encode(session._encoding))  # case C020
        with self._func_lock:
            if self.niDMM_SetAttributeViString_cfunc is None:
                self.niDMM_SetAttributeViString_cfunc = self._get_library_function('niDMM_SetAttributeViString')
                self.niDMM_SetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDMM_SetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_SetAttributeViString_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def unlock(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        caller_has_lock_ctype = _visatype.ViBoolean()  # case S220
        with self._func_lock:
            if self.niDMM_UnlockSession_cfunc is None:
                self.niDMM_UnlockSession_cfunc = self._get_library_function('niDMM_UnlockSession')
                self.niDMM_UnlockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niDMM_UnlockSession_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_UnlockSession_cfunc(vi_ctype, None if caller_has_lock_ctype is None else (ctypes.pointer(caller_has_lock_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(caller_has_lock_ctype.value)

    def _close(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niDMM_close_cfunc is None:
                self.niDMM_close_cfunc = self._get_library_function('niDMM_close')
                self.niDMM_close_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDMM_close_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_close_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _error_message(self, session, error_code):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        error_code_ctype = _visatype.ViStatus(error_code)  # case S150
        error_message_ctype = (_visatype.ViChar * 256)()  # case C070
        with self._func_lock:
            if self.niDMM_error_message_cfunc is None:
                self.niDMM_error_message_cfunc = self._get_library_function('niDMM_error_message')
                self.niDMM_error_message_cfunc.argtypes = [ViSession, ViStatus, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDMM_error_message_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_error_message_cfunc(vi_ctype, error_code_ctype, error_message_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=True)
        return error_message_ctype.value.decode(session._encoding)

    def reset(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niDMM_reset_cfunc is None:
                self.niDMM_reset_cfunc = self._get_library_function('niDMM_reset')
                self.niDMM_reset_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDMM_reset_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_reset_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _self_test(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        self_test_result_ctype = _visatype.ViInt16()  # case S220
        self_test_message_ctype = (_visatype.ViChar * 256)()  # case C070
        with self._func_lock:
            if self.niDMM_self_test_cfunc is None:
                self.niDMM_self_test_cfunc = self._get_library_function('niDMM_self_test')
                self.niDMM_self_test_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt16), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDMM_self_test_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDMM_self_test_cfunc(vi_ctype, None if self_test_result_ctype is None else (ctypes.pointer(self_test_result_ctype)), self_test_message_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(self_test_result_ctype.value), self_test_message_ctype.value.decode(session._encoding)
