# -*- coding: utf-8 -*-
# This file was generated

import ctypes
import nidmm.errors as errors
import threading

from nidmm._visatype import *  # noqa: F403,H303


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

    def niDMM_Abort(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDMM_Abort_cfunc is None:
                self.niDMM_Abort_cfunc = self._get_library_function('niDMM_Abort')
                self.niDMM_Abort_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDMM_Abort_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_Abort_cfunc(vi)

    def niDMM_ConfigureMeasurementAbsolute(self, vi, measurement_function, range, resolution_absolute):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ConfigureMeasurementAbsolute_cfunc is None:
                self.niDMM_ConfigureMeasurementAbsolute_cfunc = self._get_library_function('niDMM_ConfigureMeasurementAbsolute')
                self.niDMM_ConfigureMeasurementAbsolute_cfunc.argtypes = [ViSession, ViInt32, ViReal64, ViReal64]  # noqa: F405
                self.niDMM_ConfigureMeasurementAbsolute_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_ConfigureMeasurementAbsolute_cfunc(vi, measurement_function, range, resolution_absolute)

    def niDMM_ConfigureMeasurementDigits(self, vi, measurement_function, range, resolution_digits):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ConfigureMeasurementDigits_cfunc is None:
                self.niDMM_ConfigureMeasurementDigits_cfunc = self._get_library_function('niDMM_ConfigureMeasurementDigits')
                self.niDMM_ConfigureMeasurementDigits_cfunc.argtypes = [ViSession, ViInt32, ViReal64, ViReal64]  # noqa: F405
                self.niDMM_ConfigureMeasurementDigits_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_ConfigureMeasurementDigits_cfunc(vi, measurement_function, range, resolution_digits)

    def niDMM_ConfigureMultiPoint(self, vi, trigger_count, sample_count, sample_trigger, sample_interval):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ConfigureMultiPoint_cfunc is None:
                self.niDMM_ConfigureMultiPoint_cfunc = self._get_library_function('niDMM_ConfigureMultiPoint')
                self.niDMM_ConfigureMultiPoint_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ViInt32, ViReal64]  # noqa: F405
                self.niDMM_ConfigureMultiPoint_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_ConfigureMultiPoint_cfunc(vi, trigger_count, sample_count, sample_trigger, sample_interval)

    def niDMM_ConfigureRTDCustom(self, vi, rtd_a, rtd_b, rtd_c):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ConfigureRTDCustom_cfunc is None:
                self.niDMM_ConfigureRTDCustom_cfunc = self._get_library_function('niDMM_ConfigureRTDCustom')
                self.niDMM_ConfigureRTDCustom_cfunc.argtypes = [ViSession, ViReal64, ViReal64, ViReal64]  # noqa: F405
                self.niDMM_ConfigureRTDCustom_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_ConfigureRTDCustom_cfunc(vi, rtd_a, rtd_b, rtd_c)

    def niDMM_ConfigureRTDType(self, vi, rtd_type, rtd_resistance):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ConfigureRTDType_cfunc is None:
                self.niDMM_ConfigureRTDType_cfunc = self._get_library_function('niDMM_ConfigureRTDType')
                self.niDMM_ConfigureRTDType_cfunc.argtypes = [ViSession, ViInt32, ViReal64]  # noqa: F405
                self.niDMM_ConfigureRTDType_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_ConfigureRTDType_cfunc(vi, rtd_type, rtd_resistance)

    def niDMM_ConfigureThermistorCustom(self, vi, thermistor_a, thermistor_b, thermistor_c):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ConfigureThermistorCustom_cfunc is None:
                self.niDMM_ConfigureThermistorCustom_cfunc = self._get_library_function('niDMM_ConfigureThermistorCustom')
                self.niDMM_ConfigureThermistorCustom_cfunc.argtypes = [ViSession, ViReal64, ViReal64, ViReal64]  # noqa: F405
                self.niDMM_ConfigureThermistorCustom_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_ConfigureThermistorCustom_cfunc(vi, thermistor_a, thermistor_b, thermistor_c)

    def niDMM_ConfigureThermocouple(self, vi, thermocouple_type, reference_junction_type):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ConfigureThermocouple_cfunc is None:
                self.niDMM_ConfigureThermocouple_cfunc = self._get_library_function('niDMM_ConfigureThermocouple')
                self.niDMM_ConfigureThermocouple_cfunc.argtypes = [ViSession, ViInt32, ViInt32]  # noqa: F405
                self.niDMM_ConfigureThermocouple_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_ConfigureThermocouple_cfunc(vi, thermocouple_type, reference_junction_type)

    def niDMM_ConfigureTrigger(self, vi, trigger_source, trigger_delay):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ConfigureTrigger_cfunc is None:
                self.niDMM_ConfigureTrigger_cfunc = self._get_library_function('niDMM_ConfigureTrigger')
                self.niDMM_ConfigureTrigger_cfunc.argtypes = [ViSession, ViInt32, ViReal64]  # noqa: F405
                self.niDMM_ConfigureTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_ConfigureTrigger_cfunc(vi, trigger_source, trigger_delay)

    def niDMM_ConfigureWaveformAcquisition(self, vi, measurement_function, range, rate, waveform_points):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ConfigureWaveformAcquisition_cfunc is None:
                self.niDMM_ConfigureWaveformAcquisition_cfunc = self._get_library_function('niDMM_ConfigureWaveformAcquisition')
                self.niDMM_ConfigureWaveformAcquisition_cfunc.argtypes = [ViSession, ViInt32, ViReal64, ViReal64, ViInt32]  # noqa: F405
                self.niDMM_ConfigureWaveformAcquisition_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_ConfigureWaveformAcquisition_cfunc(vi, measurement_function, range, rate, waveform_points)

    def niDMM_Disable(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDMM_Disable_cfunc is None:
                self.niDMM_Disable_cfunc = self._get_library_function('niDMM_Disable')
                self.niDMM_Disable_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDMM_Disable_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_Disable_cfunc(vi)

    def niDMM_ExportAttributeConfigurationBuffer(self, vi, size, configuration):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ExportAttributeConfigurationBuffer_cfunc is None:
                self.niDMM_ExportAttributeConfigurationBuffer_cfunc = self._get_library_function('niDMM_ExportAttributeConfigurationBuffer')
                self.niDMM_ExportAttributeConfigurationBuffer_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt8)]  # noqa: F405
                self.niDMM_ExportAttributeConfigurationBuffer_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_ExportAttributeConfigurationBuffer_cfunc(vi, size, configuration)

    def niDMM_ExportAttributeConfigurationFile(self, vi, file_path):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ExportAttributeConfigurationFile_cfunc is None:
                self.niDMM_ExportAttributeConfigurationFile_cfunc = self._get_library_function('niDMM_ExportAttributeConfigurationFile')
                self.niDMM_ExportAttributeConfigurationFile_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDMM_ExportAttributeConfigurationFile_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_ExportAttributeConfigurationFile_cfunc(vi, file_path)

    def niDMM_Fetch(self, vi, maximum_time, reading):  # noqa: N802
        with self._func_lock:
            if self.niDMM_Fetch_cfunc is None:
                self.niDMM_Fetch_cfunc = self._get_library_function('niDMM_Fetch')
                self.niDMM_Fetch_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDMM_Fetch_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_Fetch_cfunc(vi, maximum_time, reading)

    def niDMM_FetchMultiPoint(self, vi, maximum_time, array_size, reading_array, actual_number_of_points):  # noqa: N802
        with self._func_lock:
            if self.niDMM_FetchMultiPoint_cfunc is None:
                self.niDMM_FetchMultiPoint_cfunc = self._get_library_function('niDMM_FetchMultiPoint')
                self.niDMM_FetchMultiPoint_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDMM_FetchMultiPoint_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_FetchMultiPoint_cfunc(vi, maximum_time, array_size, reading_array, actual_number_of_points)

    def niDMM_FetchWaveform(self, vi, maximum_time, array_size, waveform_array, actual_number_of_points):  # noqa: N802
        with self._func_lock:
            if self.niDMM_FetchWaveform_cfunc is None:
                self.niDMM_FetchWaveform_cfunc = self._get_library_function('niDMM_FetchWaveform')
                self.niDMM_FetchWaveform_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDMM_FetchWaveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_FetchWaveform_cfunc(vi, maximum_time, array_size, waveform_array, actual_number_of_points)

    def niDMM_GetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDMM_GetAttributeViBoolean_cfunc is None:
                self.niDMM_GetAttributeViBoolean_cfunc = self._get_library_function('niDMM_GetAttributeViBoolean')
                self.niDMM_GetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niDMM_GetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_GetAttributeViBoolean_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDMM_GetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDMM_GetAttributeViInt32_cfunc is None:
                self.niDMM_GetAttributeViInt32_cfunc = self._get_library_function('niDMM_GetAttributeViInt32')
                self.niDMM_GetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDMM_GetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_GetAttributeViInt32_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDMM_GetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDMM_GetAttributeViReal64_cfunc is None:
                self.niDMM_GetAttributeViReal64_cfunc = self._get_library_function('niDMM_GetAttributeViReal64')
                self.niDMM_GetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDMM_GetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_GetAttributeViReal64_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDMM_GetAttributeViString(self, vi, channel_name, attribute_id, buffer_size, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDMM_GetAttributeViString_cfunc is None:
                self.niDMM_GetAttributeViString_cfunc = self._get_library_function('niDMM_GetAttributeViString')
                self.niDMM_GetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDMM_GetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_GetAttributeViString_cfunc(vi, channel_name, attribute_id, buffer_size, attribute_value)

    def niDMM_GetCalDateAndTime(self, vi, cal_type, month, day, year, hour, minute):  # noqa: N802
        with self._func_lock:
            if self.niDMM_GetCalDateAndTime_cfunc is None:
                self.niDMM_GetCalDateAndTime_cfunc = self._get_library_function('niDMM_GetCalDateAndTime')
                self.niDMM_GetCalDateAndTime_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDMM_GetCalDateAndTime_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_GetCalDateAndTime_cfunc(vi, cal_type, month, day, year, hour, minute)

    def niDMM_GetDevTemp(self, vi, options, temperature):  # noqa: N802
        with self._func_lock:
            if self.niDMM_GetDevTemp_cfunc is None:
                self.niDMM_GetDevTemp_cfunc = self._get_library_function('niDMM_GetDevTemp')
                self.niDMM_GetDevTemp_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDMM_GetDevTemp_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_GetDevTemp_cfunc(vi, options, temperature)

    def niDMM_GetError(self, vi, error_code, buffer_size, description):  # noqa: N802
        with self._func_lock:
            if self.niDMM_GetError_cfunc is None:
                self.niDMM_GetError_cfunc = self._get_library_function('niDMM_GetError')
                self.niDMM_GetError_cfunc.argtypes = [ViSession, ctypes.POINTER(ViStatus), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDMM_GetError_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_GetError_cfunc(vi, error_code, buffer_size, description)

    def niDMM_GetExtCalRecommendedInterval(self, vi, months):  # noqa: N802
        with self._func_lock:
            if self.niDMM_GetExtCalRecommendedInterval_cfunc is None:
                self.niDMM_GetExtCalRecommendedInterval_cfunc = self._get_library_function('niDMM_GetExtCalRecommendedInterval')
                self.niDMM_GetExtCalRecommendedInterval_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDMM_GetExtCalRecommendedInterval_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_GetExtCalRecommendedInterval_cfunc(vi, months)

    def niDMM_GetLastCalTemp(self, vi, cal_type, temperature):  # noqa: N802
        with self._func_lock:
            if self.niDMM_GetLastCalTemp_cfunc is None:
                self.niDMM_GetLastCalTemp_cfunc = self._get_library_function('niDMM_GetLastCalTemp')
                self.niDMM_GetLastCalTemp_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDMM_GetLastCalTemp_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_GetLastCalTemp_cfunc(vi, cal_type, temperature)

    def niDMM_GetSelfCalSupported(self, vi, self_cal_supported):  # noqa: N802
        with self._func_lock:
            if self.niDMM_GetSelfCalSupported_cfunc is None:
                self.niDMM_GetSelfCalSupported_cfunc = self._get_library_function('niDMM_GetSelfCalSupported')
                self.niDMM_GetSelfCalSupported_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niDMM_GetSelfCalSupported_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_GetSelfCalSupported_cfunc(vi, self_cal_supported)

    def niDMM_ImportAttributeConfigurationBuffer(self, vi, size, configuration):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ImportAttributeConfigurationBuffer_cfunc is None:
                self.niDMM_ImportAttributeConfigurationBuffer_cfunc = self._get_library_function('niDMM_ImportAttributeConfigurationBuffer')
                self.niDMM_ImportAttributeConfigurationBuffer_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt8)]  # noqa: F405
                self.niDMM_ImportAttributeConfigurationBuffer_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_ImportAttributeConfigurationBuffer_cfunc(vi, size, configuration)

    def niDMM_ImportAttributeConfigurationFile(self, vi, file_path):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ImportAttributeConfigurationFile_cfunc is None:
                self.niDMM_ImportAttributeConfigurationFile_cfunc = self._get_library_function('niDMM_ImportAttributeConfigurationFile')
                self.niDMM_ImportAttributeConfigurationFile_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDMM_ImportAttributeConfigurationFile_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_ImportAttributeConfigurationFile_cfunc(vi, file_path)

    def niDMM_InitWithOptions(self, resource_name, id_query, reset_device, option_string, vi):  # noqa: N802
        with self._func_lock:
            if self.niDMM_InitWithOptions_cfunc is None:
                self.niDMM_InitWithOptions_cfunc = self._get_library_function('niDMM_InitWithOptions')
                self.niDMM_InitWithOptions_cfunc.argtypes = [ctypes.POINTER(ViChar), ViBoolean, ViBoolean, ctypes.POINTER(ViChar), ctypes.POINTER(ViSession)]  # noqa: F405
                self.niDMM_InitWithOptions_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_InitWithOptions_cfunc(resource_name, id_query, reset_device, option_string, vi)

    def niDMM_Initiate(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDMM_Initiate_cfunc is None:
                self.niDMM_Initiate_cfunc = self._get_library_function('niDMM_Initiate')
                self.niDMM_Initiate_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDMM_Initiate_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_Initiate_cfunc(vi)

    def niDMM_LockSession(self, vi, caller_has_lock):  # noqa: N802
        with self._func_lock:
            if self.niDMM_LockSession_cfunc is None:
                self.niDMM_LockSession_cfunc = self._get_library_function('niDMM_LockSession')
                self.niDMM_LockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niDMM_LockSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_LockSession_cfunc(vi, caller_has_lock)

    def niDMM_PerformOpenCableComp(self, vi, conductance, susceptance):  # noqa: N802
        with self._func_lock:
            if self.niDMM_PerformOpenCableComp_cfunc is None:
                self.niDMM_PerformOpenCableComp_cfunc = self._get_library_function('niDMM_PerformOpenCableComp')
                self.niDMM_PerformOpenCableComp_cfunc.argtypes = [ViSession, ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDMM_PerformOpenCableComp_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_PerformOpenCableComp_cfunc(vi, conductance, susceptance)

    def niDMM_PerformShortCableComp(self, vi, resistance, reactance):  # noqa: N802
        with self._func_lock:
            if self.niDMM_PerformShortCableComp_cfunc is None:
                self.niDMM_PerformShortCableComp_cfunc = self._get_library_function('niDMM_PerformShortCableComp')
                self.niDMM_PerformShortCableComp_cfunc.argtypes = [ViSession, ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDMM_PerformShortCableComp_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_PerformShortCableComp_cfunc(vi, resistance, reactance)

    def niDMM_Read(self, vi, maximum_time, reading):  # noqa: N802
        with self._func_lock:
            if self.niDMM_Read_cfunc is None:
                self.niDMM_Read_cfunc = self._get_library_function('niDMM_Read')
                self.niDMM_Read_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDMM_Read_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_Read_cfunc(vi, maximum_time, reading)

    def niDMM_ReadMultiPoint(self, vi, maximum_time, array_size, reading_array, actual_number_of_points):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ReadMultiPoint_cfunc is None:
                self.niDMM_ReadMultiPoint_cfunc = self._get_library_function('niDMM_ReadMultiPoint')
                self.niDMM_ReadMultiPoint_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDMM_ReadMultiPoint_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_ReadMultiPoint_cfunc(vi, maximum_time, array_size, reading_array, actual_number_of_points)

    def niDMM_ReadStatus(self, vi, acquisition_backlog, acquisition_status):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ReadStatus_cfunc is None:
                self.niDMM_ReadStatus_cfunc = self._get_library_function('niDMM_ReadStatus')
                self.niDMM_ReadStatus_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt16)]  # noqa: F405
                self.niDMM_ReadStatus_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_ReadStatus_cfunc(vi, acquisition_backlog, acquisition_status)

    def niDMM_ReadWaveform(self, vi, maximum_time, array_size, waveform_array, actual_number_of_points):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ReadWaveform_cfunc is None:
                self.niDMM_ReadWaveform_cfunc = self._get_library_function('niDMM_ReadWaveform')
                self.niDMM_ReadWaveform_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDMM_ReadWaveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_ReadWaveform_cfunc(vi, maximum_time, array_size, waveform_array, actual_number_of_points)

    def niDMM_ResetWithDefaults(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ResetWithDefaults_cfunc is None:
                self.niDMM_ResetWithDefaults_cfunc = self._get_library_function('niDMM_ResetWithDefaults')
                self.niDMM_ResetWithDefaults_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDMM_ResetWithDefaults_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_ResetWithDefaults_cfunc(vi)

    def niDMM_SelfCal(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDMM_SelfCal_cfunc is None:
                self.niDMM_SelfCal_cfunc = self._get_library_function('niDMM_SelfCal')
                self.niDMM_SelfCal_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDMM_SelfCal_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_SelfCal_cfunc(vi)

    def niDMM_SendSoftwareTrigger(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDMM_SendSoftwareTrigger_cfunc is None:
                self.niDMM_SendSoftwareTrigger_cfunc = self._get_library_function('niDMM_SendSoftwareTrigger')
                self.niDMM_SendSoftwareTrigger_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDMM_SendSoftwareTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_SendSoftwareTrigger_cfunc(vi)

    def niDMM_SetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDMM_SetAttributeViBoolean_cfunc is None:
                self.niDMM_SetAttributeViBoolean_cfunc = self._get_library_function('niDMM_SetAttributeViBoolean')
                self.niDMM_SetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViBoolean]  # noqa: F405
                self.niDMM_SetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_SetAttributeViBoolean_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDMM_SetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDMM_SetAttributeViInt32_cfunc is None:
                self.niDMM_SetAttributeViInt32_cfunc = self._get_library_function('niDMM_SetAttributeViInt32')
                self.niDMM_SetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32]  # noqa: F405
                self.niDMM_SetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_SetAttributeViInt32_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDMM_SetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDMM_SetAttributeViReal64_cfunc is None:
                self.niDMM_SetAttributeViReal64_cfunc = self._get_library_function('niDMM_SetAttributeViReal64')
                self.niDMM_SetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViReal64]  # noqa: F405
                self.niDMM_SetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_SetAttributeViReal64_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDMM_SetAttributeViString(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDMM_SetAttributeViString_cfunc is None:
                self.niDMM_SetAttributeViString_cfunc = self._get_library_function('niDMM_SetAttributeViString')
                self.niDMM_SetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDMM_SetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_SetAttributeViString_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDMM_UnlockSession(self, vi, caller_has_lock):  # noqa: N802
        with self._func_lock:
            if self.niDMM_UnlockSession_cfunc is None:
                self.niDMM_UnlockSession_cfunc = self._get_library_function('niDMM_UnlockSession')
                self.niDMM_UnlockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niDMM_UnlockSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_UnlockSession_cfunc(vi, caller_has_lock)

    def niDMM_close(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDMM_close_cfunc is None:
                self.niDMM_close_cfunc = self._get_library_function('niDMM_close')
                self.niDMM_close_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDMM_close_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_close_cfunc(vi)

    def niDMM_error_message(self, vi, error_code, error_message):  # noqa: N802
        with self._func_lock:
            if self.niDMM_error_message_cfunc is None:
                self.niDMM_error_message_cfunc = self._get_library_function('niDMM_error_message')
                self.niDMM_error_message_cfunc.argtypes = [ViSession, ViStatus, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDMM_error_message_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_error_message_cfunc(vi, error_code, error_message)

    def niDMM_reset(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDMM_reset_cfunc is None:
                self.niDMM_reset_cfunc = self._get_library_function('niDMM_reset')
                self.niDMM_reset_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDMM_reset_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_reset_cfunc(vi)

    def niDMM_self_test(self, vi, self_test_result, self_test_message):  # noqa: N802
        with self._func_lock:
            if self.niDMM_self_test_cfunc is None:
                self.niDMM_self_test_cfunc = self._get_library_function('niDMM_self_test')
                self.niDMM_self_test_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt16), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDMM_self_test_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_self_test_cfunc(vi, self_test_result, self_test_message)
