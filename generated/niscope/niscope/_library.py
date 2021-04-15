# -*- coding: utf-8 -*-
# This file was generated

import ctypes
import niscope.errors as errors
import threading

from niscope._visatype import *  # noqa: F403,H303

import niscope.waveform_info as waveform_info  # noqa: F401

import niscope.measurement_stats as measurement_stats  # noqa: F401


class Library(object):
    '''Library

    Wrapper around driver library.
    Class will setup the correct ctypes information for every function on first call.
    '''

    def __init__(self, ctypes_library):
        self._func_lock = threading.Lock()
        self._library = ctypes_library
        # We cache the cfunc object from the ctypes.CDLL object
        self.niScope_Abort_cfunc = None
        self.niScope_AcquisitionStatus_cfunc = None
        self.niScope_ActualMeasWfmSize_cfunc = None
        self.niScope_ActualNumWfms_cfunc = None
        self.niScope_AddWaveformProcessing_cfunc = None
        self.niScope_AutoSetup_cfunc = None
        self.niScope_CalFetchDate_cfunc = None
        self.niScope_CalFetchTemperature_cfunc = None
        self.niScope_CalSelfCalibrate_cfunc = None
        self.niScope_ClearWaveformMeasurementStats_cfunc = None
        self.niScope_ClearWaveformProcessing_cfunc = None
        self.niScope_Commit_cfunc = None
        self.niScope_ConfigureChanCharacteristics_cfunc = None
        self.niScope_ConfigureEqualizationFilterCoefficients_cfunc = None
        self.niScope_ConfigureHorizontalTiming_cfunc = None
        self.niScope_ConfigureRefLevels_cfunc = None
        self.niScope_ConfigureTriggerDigital_cfunc = None
        self.niScope_ConfigureTriggerEdge_cfunc = None
        self.niScope_ConfigureTriggerHysteresis_cfunc = None
        self.niScope_ConfigureTriggerImmediate_cfunc = None
        self.niScope_ConfigureTriggerSoftware_cfunc = None
        self.niScope_ConfigureTriggerVideo_cfunc = None
        self.niScope_ConfigureTriggerWindow_cfunc = None
        self.niScope_ConfigureVertical_cfunc = None
        self.niScope_Disable_cfunc = None
        self.niScope_ExportAttributeConfigurationBuffer_cfunc = None
        self.niScope_ExportAttributeConfigurationFile_cfunc = None
        self.niScope_Fetch_cfunc = None
        self.niScope_FetchArrayMeasurement_cfunc = None
        self.niScope_FetchBinary16_cfunc = None
        self.niScope_FetchBinary32_cfunc = None
        self.niScope_FetchBinary8_cfunc = None
        self.niScope_FetchMeasurementStats_cfunc = None
        self.niScope_GetAttributeViBoolean_cfunc = None
        self.niScope_GetAttributeViInt32_cfunc = None
        self.niScope_GetAttributeViInt64_cfunc = None
        self.niScope_GetAttributeViReal64_cfunc = None
        self.niScope_GetAttributeViString_cfunc = None
        self.niScope_GetEqualizationFilterCoefficients_cfunc = None
        self.niScope_GetError_cfunc = None
        self.niScope_ImportAttributeConfigurationBuffer_cfunc = None
        self.niScope_ImportAttributeConfigurationFile_cfunc = None
        self.niScope_InitWithOptions_cfunc = None
        self.niScope_InitiateAcquisition_cfunc = None
        self.niScope_LockSession_cfunc = None
        self.niScope_ProbeCompensationSignalStart_cfunc = None
        self.niScope_ProbeCompensationSignalStop_cfunc = None
        self.niScope_Read_cfunc = None
        self.niScope_ResetDevice_cfunc = None
        self.niScope_ResetWithDefaults_cfunc = None
        self.niScope_SendSoftwareTriggerEdge_cfunc = None
        self.niScope_SetAttributeViBoolean_cfunc = None
        self.niScope_SetAttributeViInt32_cfunc = None
        self.niScope_SetAttributeViInt64_cfunc = None
        self.niScope_SetAttributeViReal64_cfunc = None
        self.niScope_SetAttributeViString_cfunc = None
        self.niScope_UnlockSession_cfunc = None
        self.niScope_close_cfunc = None
        self.niScope_error_message_cfunc = None
        self.niScope_reset_cfunc = None
        self.niScope_self_test_cfunc = None

    def _get_library_function(self, name):
        try:
            function = getattr(self._library, name)
        except AttributeError as e:
            raise errors.DriverTooOldError() from e
        return function

    def niScope_Abort(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niScope_Abort_cfunc is None:
                self.niScope_Abort_cfunc = self._get_library_function('niScope_Abort')
                self.niScope_Abort_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_Abort_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_Abort_cfunc(vi)

    def niScope_AcquisitionStatus(self, vi, acquisition_status):  # noqa: N802
        with self._func_lock:
            if self.niScope_AcquisitionStatus_cfunc is None:
                self.niScope_AcquisitionStatus_cfunc = self._get_library_function('niScope_AcquisitionStatus')
                self.niScope_AcquisitionStatus_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niScope_AcquisitionStatus_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_AcquisitionStatus_cfunc(vi, acquisition_status)

    def niScope_ActualMeasWfmSize(self, vi, array_meas_function, meas_waveform_size):  # noqa: N802
        with self._func_lock:
            if self.niScope_ActualMeasWfmSize_cfunc is None:
                self.niScope_ActualMeasWfmSize_cfunc = self._get_library_function('niScope_ActualMeasWfmSize')
                self.niScope_ActualMeasWfmSize_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niScope_ActualMeasWfmSize_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ActualMeasWfmSize_cfunc(vi, array_meas_function, meas_waveform_size)

    def niScope_ActualNumWfms(self, vi, channel_list, num_wfms):  # noqa: N802
        with self._func_lock:
            if self.niScope_ActualNumWfms_cfunc is None:
                self.niScope_ActualNumWfms_cfunc = self._get_library_function('niScope_ActualNumWfms')
                self.niScope_ActualNumWfms_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niScope_ActualNumWfms_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ActualNumWfms_cfunc(vi, channel_list, num_wfms)

    def niScope_AddWaveformProcessing(self, vi, channel_list, meas_function):  # noqa: N802
        with self._func_lock:
            if self.niScope_AddWaveformProcessing_cfunc is None:
                self.niScope_AddWaveformProcessing_cfunc = self._get_library_function('niScope_AddWaveformProcessing')
                self.niScope_AddWaveformProcessing_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niScope_AddWaveformProcessing_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_AddWaveformProcessing_cfunc(vi, channel_list, meas_function)

    def niScope_AutoSetup(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niScope_AutoSetup_cfunc is None:
                self.niScope_AutoSetup_cfunc = self._get_library_function('niScope_AutoSetup')
                self.niScope_AutoSetup_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_AutoSetup_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_AutoSetup_cfunc(vi)

    def niScope_CalFetchDate(self, vi, which_one, year, month, day):  # noqa: N802
        with self._func_lock:
            if self.niScope_CalFetchDate_cfunc is None:
                self.niScope_CalFetchDate_cfunc = self._get_library_function('niScope_CalFetchDate')
                self.niScope_CalFetchDate_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niScope_CalFetchDate_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_CalFetchDate_cfunc(vi, which_one, year, month, day)

    def niScope_CalFetchTemperature(self, vi, which_one, temperature):  # noqa: N802
        with self._func_lock:
            if self.niScope_CalFetchTemperature_cfunc is None:
                self.niScope_CalFetchTemperature_cfunc = self._get_library_function('niScope_CalFetchTemperature')
                self.niScope_CalFetchTemperature_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niScope_CalFetchTemperature_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_CalFetchTemperature_cfunc(vi, which_one, temperature)

    def niScope_CalSelfCalibrate(self, vi, channel_list, option):  # noqa: N802
        with self._func_lock:
            if self.niScope_CalSelfCalibrate_cfunc is None:
                self.niScope_CalSelfCalibrate_cfunc = self._get_library_function('niScope_CalSelfCalibrate')
                self.niScope_CalSelfCalibrate_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niScope_CalSelfCalibrate_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_CalSelfCalibrate_cfunc(vi, channel_list, option)

    def niScope_ClearWaveformMeasurementStats(self, vi, channel_list, clearable_measurement_function):  # noqa: N802
        with self._func_lock:
            if self.niScope_ClearWaveformMeasurementStats_cfunc is None:
                self.niScope_ClearWaveformMeasurementStats_cfunc = self._get_library_function('niScope_ClearWaveformMeasurementStats')
                self.niScope_ClearWaveformMeasurementStats_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niScope_ClearWaveformMeasurementStats_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ClearWaveformMeasurementStats_cfunc(vi, channel_list, clearable_measurement_function)

    def niScope_ClearWaveformProcessing(self, vi, channel_list):  # noqa: N802
        with self._func_lock:
            if self.niScope_ClearWaveformProcessing_cfunc is None:
                self.niScope_ClearWaveformProcessing_cfunc = self._get_library_function('niScope_ClearWaveformProcessing')
                self.niScope_ClearWaveformProcessing_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niScope_ClearWaveformProcessing_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ClearWaveformProcessing_cfunc(vi, channel_list)

    def niScope_Commit(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niScope_Commit_cfunc is None:
                self.niScope_Commit_cfunc = self._get_library_function('niScope_Commit')
                self.niScope_Commit_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_Commit_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_Commit_cfunc(vi)

    def niScope_ConfigureChanCharacteristics(self, vi, channel_list, input_impedance, max_input_frequency):  # noqa: N802
        with self._func_lock:
            if self.niScope_ConfigureChanCharacteristics_cfunc is None:
                self.niScope_ConfigureChanCharacteristics_cfunc = self._get_library_function('niScope_ConfigureChanCharacteristics')
                self.niScope_ConfigureChanCharacteristics_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViReal64]  # noqa: F405
                self.niScope_ConfigureChanCharacteristics_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ConfigureChanCharacteristics_cfunc(vi, channel_list, input_impedance, max_input_frequency)

    def niScope_ConfigureEqualizationFilterCoefficients(self, vi, channel_list, number_of_coefficients, coefficients):  # noqa: N802
        with self._func_lock:
            if self.niScope_ConfigureEqualizationFilterCoefficients_cfunc is None:
                self.niScope_ConfigureEqualizationFilterCoefficients_cfunc = self._get_library_function('niScope_ConfigureEqualizationFilterCoefficients')
                self.niScope_ConfigureEqualizationFilterCoefficients_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niScope_ConfigureEqualizationFilterCoefficients_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ConfigureEqualizationFilterCoefficients_cfunc(vi, channel_list, number_of_coefficients, coefficients)

    def niScope_ConfigureHorizontalTiming(self, vi, min_sample_rate, min_num_pts, ref_position, num_records, enforce_realtime):  # noqa: N802
        with self._func_lock:
            if self.niScope_ConfigureHorizontalTiming_cfunc is None:
                self.niScope_ConfigureHorizontalTiming_cfunc = self._get_library_function('niScope_ConfigureHorizontalTiming')
                self.niScope_ConfigureHorizontalTiming_cfunc.argtypes = [ViSession, ViReal64, ViInt32, ViReal64, ViInt32, ViBoolean]  # noqa: F405
                self.niScope_ConfigureHorizontalTiming_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ConfigureHorizontalTiming_cfunc(vi, min_sample_rate, min_num_pts, ref_position, num_records, enforce_realtime)

    def niScope_ConfigureRefLevels(self, vi, low, mid, high):  # noqa: N802
        with self._func_lock:
            if self.niScope_ConfigureRefLevels_cfunc is None:
                self.niScope_ConfigureRefLevels_cfunc = self._get_library_function('niScope_ConfigureRefLevels')
                self.niScope_ConfigureRefLevels_cfunc.argtypes = [ViSession, ViReal64, ViReal64, ViReal64]  # noqa: F405
                self.niScope_ConfigureRefLevels_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ConfigureRefLevels_cfunc(vi, low, mid, high)

    def niScope_ConfigureTriggerDigital(self, vi, trigger_source, slope, holdoff, delay):  # noqa: N802
        with self._func_lock:
            if self.niScope_ConfigureTriggerDigital_cfunc is None:
                self.niScope_ConfigureTriggerDigital_cfunc = self._get_library_function('niScope_ConfigureTriggerDigital')
                self.niScope_ConfigureTriggerDigital_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViReal64, ViReal64]  # noqa: F405
                self.niScope_ConfigureTriggerDigital_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ConfigureTriggerDigital_cfunc(vi, trigger_source, slope, holdoff, delay)

    def niScope_ConfigureTriggerEdge(self, vi, trigger_source, level, slope, trigger_coupling, holdoff, delay):  # noqa: N802
        with self._func_lock:
            if self.niScope_ConfigureTriggerEdge_cfunc is None:
                self.niScope_ConfigureTriggerEdge_cfunc = self._get_library_function('niScope_ConfigureTriggerEdge')
                self.niScope_ConfigureTriggerEdge_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViInt32, ViInt32, ViReal64, ViReal64]  # noqa: F405
                self.niScope_ConfigureTriggerEdge_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ConfigureTriggerEdge_cfunc(vi, trigger_source, level, slope, trigger_coupling, holdoff, delay)

    def niScope_ConfigureTriggerHysteresis(self, vi, trigger_source, level, hysteresis, slope, trigger_coupling, holdoff, delay):  # noqa: N802
        with self._func_lock:
            if self.niScope_ConfigureTriggerHysteresis_cfunc is None:
                self.niScope_ConfigureTriggerHysteresis_cfunc = self._get_library_function('niScope_ConfigureTriggerHysteresis')
                self.niScope_ConfigureTriggerHysteresis_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViReal64, ViInt32, ViInt32, ViReal64, ViReal64]  # noqa: F405
                self.niScope_ConfigureTriggerHysteresis_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ConfigureTriggerHysteresis_cfunc(vi, trigger_source, level, hysteresis, slope, trigger_coupling, holdoff, delay)

    def niScope_ConfigureTriggerImmediate(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niScope_ConfigureTriggerImmediate_cfunc is None:
                self.niScope_ConfigureTriggerImmediate_cfunc = self._get_library_function('niScope_ConfigureTriggerImmediate')
                self.niScope_ConfigureTriggerImmediate_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_ConfigureTriggerImmediate_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ConfigureTriggerImmediate_cfunc(vi)

    def niScope_ConfigureTriggerSoftware(self, vi, holdoff, delay):  # noqa: N802
        with self._func_lock:
            if self.niScope_ConfigureTriggerSoftware_cfunc is None:
                self.niScope_ConfigureTriggerSoftware_cfunc = self._get_library_function('niScope_ConfigureTriggerSoftware')
                self.niScope_ConfigureTriggerSoftware_cfunc.argtypes = [ViSession, ViReal64, ViReal64]  # noqa: F405
                self.niScope_ConfigureTriggerSoftware_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ConfigureTriggerSoftware_cfunc(vi, holdoff, delay)

    def niScope_ConfigureTriggerVideo(self, vi, trigger_source, enable_dc_restore, signal_format, event, line_number, polarity, trigger_coupling, holdoff, delay):  # noqa: N802
        with self._func_lock:
            if self.niScope_ConfigureTriggerVideo_cfunc is None:
                self.niScope_ConfigureTriggerVideo_cfunc = self._get_library_function('niScope_ConfigureTriggerVideo')
                self.niScope_ConfigureTriggerVideo_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViBoolean, ViInt32, ViInt32, ViInt32, ViInt32, ViInt32, ViReal64, ViReal64]  # noqa: F405
                self.niScope_ConfigureTriggerVideo_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ConfigureTriggerVideo_cfunc(vi, trigger_source, enable_dc_restore, signal_format, event, line_number, polarity, trigger_coupling, holdoff, delay)

    def niScope_ConfigureTriggerWindow(self, vi, trigger_source, low_level, high_level, window_mode, trigger_coupling, holdoff, delay):  # noqa: N802
        with self._func_lock:
            if self.niScope_ConfigureTriggerWindow_cfunc is None:
                self.niScope_ConfigureTriggerWindow_cfunc = self._get_library_function('niScope_ConfigureTriggerWindow')
                self.niScope_ConfigureTriggerWindow_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViReal64, ViInt32, ViInt32, ViReal64, ViReal64]  # noqa: F405
                self.niScope_ConfigureTriggerWindow_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ConfigureTriggerWindow_cfunc(vi, trigger_source, low_level, high_level, window_mode, trigger_coupling, holdoff, delay)

    def niScope_ConfigureVertical(self, vi, channel_list, range, offset, coupling, probe_attenuation, enabled):  # noqa: N802
        with self._func_lock:
            if self.niScope_ConfigureVertical_cfunc is None:
                self.niScope_ConfigureVertical_cfunc = self._get_library_function('niScope_ConfigureVertical')
                self.niScope_ConfigureVertical_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViReal64, ViInt32, ViReal64, ViBoolean]  # noqa: F405
                self.niScope_ConfigureVertical_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ConfigureVertical_cfunc(vi, channel_list, range, offset, coupling, probe_attenuation, enabled)

    def niScope_Disable(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niScope_Disable_cfunc is None:
                self.niScope_Disable_cfunc = self._get_library_function('niScope_Disable')
                self.niScope_Disable_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_Disable_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_Disable_cfunc(vi)

    def niScope_ExportAttributeConfigurationBuffer(self, vi, size_in_bytes, configuration):  # noqa: N802
        with self._func_lock:
            if self.niScope_ExportAttributeConfigurationBuffer_cfunc is None:
                self.niScope_ExportAttributeConfigurationBuffer_cfunc = self._get_library_function('niScope_ExportAttributeConfigurationBuffer')
                self.niScope_ExportAttributeConfigurationBuffer_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt8)]  # noqa: F405
                self.niScope_ExportAttributeConfigurationBuffer_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ExportAttributeConfigurationBuffer_cfunc(vi, size_in_bytes, configuration)

    def niScope_ExportAttributeConfigurationFile(self, vi, file_path):  # noqa: N802
        with self._func_lock:
            if self.niScope_ExportAttributeConfigurationFile_cfunc is None:
                self.niScope_ExportAttributeConfigurationFile_cfunc = self._get_library_function('niScope_ExportAttributeConfigurationFile')
                self.niScope_ExportAttributeConfigurationFile_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niScope_ExportAttributeConfigurationFile_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ExportAttributeConfigurationFile_cfunc(vi, file_path)

    def niScope_Fetch(self, vi, channel_list, timeout, num_samples, waveform, wfm_info):  # noqa: N802
        with self._func_lock:
            if self.niScope_Fetch_cfunc is None:
                self.niScope_Fetch_cfunc = self._get_library_function('niScope_Fetch')
                self.niScope_Fetch_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(waveform_info.struct_niScope_wfmInfo)]  # noqa: F405
                self.niScope_Fetch_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_Fetch_cfunc(vi, channel_list, timeout, num_samples, waveform, wfm_info)

    def niScope_FetchArrayMeasurement(self, vi, channel_list, timeout, array_meas_function, measurement_waveform_size, meas_wfm, wfm_info):  # noqa: N802
        with self._func_lock:
            if self.niScope_FetchArrayMeasurement_cfunc is None:
                self.niScope_FetchArrayMeasurement_cfunc = self._get_library_function('niScope_FetchArrayMeasurement')
                self.niScope_FetchArrayMeasurement_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViInt32, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(waveform_info.struct_niScope_wfmInfo)]  # noqa: F405
                self.niScope_FetchArrayMeasurement_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_FetchArrayMeasurement_cfunc(vi, channel_list, timeout, array_meas_function, measurement_waveform_size, meas_wfm, wfm_info)

    def niScope_FetchBinary16(self, vi, channel_list, timeout, num_samples, waveform, wfm_info):  # noqa: N802
        with self._func_lock:
            if self.niScope_FetchBinary16_cfunc is None:
                self.niScope_FetchBinary16_cfunc = self._get_library_function('niScope_FetchBinary16')
                self.niScope_FetchBinary16_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViInt32, ctypes.POINTER(ViInt16), ctypes.POINTER(waveform_info.struct_niScope_wfmInfo)]  # noqa: F405
                self.niScope_FetchBinary16_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_FetchBinary16_cfunc(vi, channel_list, timeout, num_samples, waveform, wfm_info)

    def niScope_FetchBinary32(self, vi, channel_list, timeout, num_samples, waveform, wfm_info):  # noqa: N802
        with self._func_lock:
            if self.niScope_FetchBinary32_cfunc is None:
                self.niScope_FetchBinary32_cfunc = self._get_library_function('niScope_FetchBinary32')
                self.niScope_FetchBinary32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViInt32, ctypes.POINTER(ViInt32), ctypes.POINTER(waveform_info.struct_niScope_wfmInfo)]  # noqa: F405
                self.niScope_FetchBinary32_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_FetchBinary32_cfunc(vi, channel_list, timeout, num_samples, waveform, wfm_info)

    def niScope_FetchBinary8(self, vi, channel_list, timeout, num_samples, waveform, wfm_info):  # noqa: N802
        with self._func_lock:
            if self.niScope_FetchBinary8_cfunc is None:
                self.niScope_FetchBinary8_cfunc = self._get_library_function('niScope_FetchBinary8')
                self.niScope_FetchBinary8_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViInt32, ctypes.POINTER(ViInt8), ctypes.POINTER(waveform_info.struct_niScope_wfmInfo)]  # noqa: F405
                self.niScope_FetchBinary8_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_FetchBinary8_cfunc(vi, channel_list, timeout, num_samples, waveform, wfm_info)

    def niScope_FetchMeasurementStats(self, vi, channel_list, timeout, scalar_meas_function, result, mean, stdev, min, max, num_in_stats):  # noqa: N802
        with self._func_lock:
            if self.niScope_FetchMeasurementStats_cfunc is None:
                self.niScope_FetchMeasurementStats_cfunc = self._get_library_function('niScope_FetchMeasurementStats')
                self.niScope_FetchMeasurementStats_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niScope_FetchMeasurementStats_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_FetchMeasurementStats_cfunc(vi, channel_list, timeout, scalar_meas_function, result, mean, stdev, min, max, num_in_stats)

    def niScope_GetAttributeViBoolean(self, vi, channel_list, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niScope_GetAttributeViBoolean_cfunc is None:
                self.niScope_GetAttributeViBoolean_cfunc = self._get_library_function('niScope_GetAttributeViBoolean')
                self.niScope_GetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niScope_GetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_GetAttributeViBoolean_cfunc(vi, channel_list, attribute_id, value)

    def niScope_GetAttributeViInt32(self, vi, channel_list, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niScope_GetAttributeViInt32_cfunc is None:
                self.niScope_GetAttributeViInt32_cfunc = self._get_library_function('niScope_GetAttributeViInt32')
                self.niScope_GetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niScope_GetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_GetAttributeViInt32_cfunc(vi, channel_list, attribute_id, value)

    def niScope_GetAttributeViInt64(self, vi, channel_list, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niScope_GetAttributeViInt64_cfunc is None:
                self.niScope_GetAttributeViInt64_cfunc = self._get_library_function('niScope_GetAttributeViInt64')
                self.niScope_GetAttributeViInt64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViInt64)]  # noqa: F405
                self.niScope_GetAttributeViInt64_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_GetAttributeViInt64_cfunc(vi, channel_list, attribute_id, value)

    def niScope_GetAttributeViReal64(self, vi, channel_list, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niScope_GetAttributeViReal64_cfunc is None:
                self.niScope_GetAttributeViReal64_cfunc = self._get_library_function('niScope_GetAttributeViReal64')
                self.niScope_GetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niScope_GetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_GetAttributeViReal64_cfunc(vi, channel_list, attribute_id, value)

    def niScope_GetAttributeViString(self, vi, channel_list, attribute_id, buf_size, value):  # noqa: N802
        with self._func_lock:
            if self.niScope_GetAttributeViString_cfunc is None:
                self.niScope_GetAttributeViString_cfunc = self._get_library_function('niScope_GetAttributeViString')
                self.niScope_GetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niScope_GetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_GetAttributeViString_cfunc(vi, channel_list, attribute_id, buf_size, value)

    def niScope_GetEqualizationFilterCoefficients(self, vi, channel, number_of_coefficients, coefficients):  # noqa: N802
        with self._func_lock:
            if self.niScope_GetEqualizationFilterCoefficients_cfunc is None:
                self.niScope_GetEqualizationFilterCoefficients_cfunc = self._get_library_function('niScope_GetEqualizationFilterCoefficients')
                self.niScope_GetEqualizationFilterCoefficients_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niScope_GetEqualizationFilterCoefficients_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_GetEqualizationFilterCoefficients_cfunc(vi, channel, number_of_coefficients, coefficients)

    def niScope_GetError(self, vi, error_code, buffer_size, description):  # noqa: N802
        with self._func_lock:
            if self.niScope_GetError_cfunc is None:
                self.niScope_GetError_cfunc = self._get_library_function('niScope_GetError')
                self.niScope_GetError_cfunc.argtypes = [ViSession, ctypes.POINTER(ViStatus), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niScope_GetError_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_GetError_cfunc(vi, error_code, buffer_size, description)

    def niScope_ImportAttributeConfigurationBuffer(self, vi, size_in_bytes, configuration):  # noqa: N802
        with self._func_lock:
            if self.niScope_ImportAttributeConfigurationBuffer_cfunc is None:
                self.niScope_ImportAttributeConfigurationBuffer_cfunc = self._get_library_function('niScope_ImportAttributeConfigurationBuffer')
                self.niScope_ImportAttributeConfigurationBuffer_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt8)]  # noqa: F405
                self.niScope_ImportAttributeConfigurationBuffer_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ImportAttributeConfigurationBuffer_cfunc(vi, size_in_bytes, configuration)

    def niScope_ImportAttributeConfigurationFile(self, vi, file_path):  # noqa: N802
        with self._func_lock:
            if self.niScope_ImportAttributeConfigurationFile_cfunc is None:
                self.niScope_ImportAttributeConfigurationFile_cfunc = self._get_library_function('niScope_ImportAttributeConfigurationFile')
                self.niScope_ImportAttributeConfigurationFile_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niScope_ImportAttributeConfigurationFile_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ImportAttributeConfigurationFile_cfunc(vi, file_path)

    def niScope_InitWithOptions(self, resource_name, id_query, reset_device, option_string, vi):  # noqa: N802
        with self._func_lock:
            if self.niScope_InitWithOptions_cfunc is None:
                self.niScope_InitWithOptions_cfunc = self._get_library_function('niScope_InitWithOptions')
                self.niScope_InitWithOptions_cfunc.argtypes = [ctypes.POINTER(ViChar), ViBoolean, ViBoolean, ctypes.POINTER(ViChar), ctypes.POINTER(ViSession)]  # noqa: F405
                self.niScope_InitWithOptions_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_InitWithOptions_cfunc(resource_name, id_query, reset_device, option_string, vi)

    def niScope_InitiateAcquisition(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niScope_InitiateAcquisition_cfunc is None:
                self.niScope_InitiateAcquisition_cfunc = self._get_library_function('niScope_InitiateAcquisition')
                self.niScope_InitiateAcquisition_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_InitiateAcquisition_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_InitiateAcquisition_cfunc(vi)

    def niScope_LockSession(self, vi, caller_has_lock):  # noqa: N802
        with self._func_lock:
            if self.niScope_LockSession_cfunc is None:
                self.niScope_LockSession_cfunc = self._get_library_function('niScope_LockSession')
                self.niScope_LockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niScope_LockSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_LockSession_cfunc(vi, caller_has_lock)

    def niScope_ProbeCompensationSignalStart(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niScope_ProbeCompensationSignalStart_cfunc is None:
                self.niScope_ProbeCompensationSignalStart_cfunc = self._get_library_function('niScope_ProbeCompensationSignalStart')
                self.niScope_ProbeCompensationSignalStart_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_ProbeCompensationSignalStart_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ProbeCompensationSignalStart_cfunc(vi)

    def niScope_ProbeCompensationSignalStop(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niScope_ProbeCompensationSignalStop_cfunc is None:
                self.niScope_ProbeCompensationSignalStop_cfunc = self._get_library_function('niScope_ProbeCompensationSignalStop')
                self.niScope_ProbeCompensationSignalStop_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_ProbeCompensationSignalStop_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ProbeCompensationSignalStop_cfunc(vi)

    def niScope_Read(self, vi, channel_list, timeout, num_samples, waveform, wfm_info):  # noqa: N802
        with self._func_lock:
            if self.niScope_Read_cfunc is None:
                self.niScope_Read_cfunc = self._get_library_function('niScope_Read')
                self.niScope_Read_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(waveform_info.struct_niScope_wfmInfo)]  # noqa: F405
                self.niScope_Read_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_Read_cfunc(vi, channel_list, timeout, num_samples, waveform, wfm_info)

    def niScope_ResetDevice(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niScope_ResetDevice_cfunc is None:
                self.niScope_ResetDevice_cfunc = self._get_library_function('niScope_ResetDevice')
                self.niScope_ResetDevice_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_ResetDevice_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ResetDevice_cfunc(vi)

    def niScope_ResetWithDefaults(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niScope_ResetWithDefaults_cfunc is None:
                self.niScope_ResetWithDefaults_cfunc = self._get_library_function('niScope_ResetWithDefaults')
                self.niScope_ResetWithDefaults_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_ResetWithDefaults_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ResetWithDefaults_cfunc(vi)

    def niScope_SendSoftwareTriggerEdge(self, vi, which_trigger):  # noqa: N802
        with self._func_lock:
            if self.niScope_SendSoftwareTriggerEdge_cfunc is None:
                self.niScope_SendSoftwareTriggerEdge_cfunc = self._get_library_function('niScope_SendSoftwareTriggerEdge')
                self.niScope_SendSoftwareTriggerEdge_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niScope_SendSoftwareTriggerEdge_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_SendSoftwareTriggerEdge_cfunc(vi, which_trigger)

    def niScope_SetAttributeViBoolean(self, vi, channel_list, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niScope_SetAttributeViBoolean_cfunc is None:
                self.niScope_SetAttributeViBoolean_cfunc = self._get_library_function('niScope_SetAttributeViBoolean')
                self.niScope_SetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViBoolean]  # noqa: F405
                self.niScope_SetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_SetAttributeViBoolean_cfunc(vi, channel_list, attribute_id, value)

    def niScope_SetAttributeViInt32(self, vi, channel_list, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niScope_SetAttributeViInt32_cfunc is None:
                self.niScope_SetAttributeViInt32_cfunc = self._get_library_function('niScope_SetAttributeViInt32')
                self.niScope_SetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32]  # noqa: F405
                self.niScope_SetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_SetAttributeViInt32_cfunc(vi, channel_list, attribute_id, value)

    def niScope_SetAttributeViInt64(self, vi, channel_list, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niScope_SetAttributeViInt64_cfunc is None:
                self.niScope_SetAttributeViInt64_cfunc = self._get_library_function('niScope_SetAttributeViInt64')
                self.niScope_SetAttributeViInt64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt64]  # noqa: F405
                self.niScope_SetAttributeViInt64_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_SetAttributeViInt64_cfunc(vi, channel_list, attribute_id, value)

    def niScope_SetAttributeViReal64(self, vi, channel_list, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niScope_SetAttributeViReal64_cfunc is None:
                self.niScope_SetAttributeViReal64_cfunc = self._get_library_function('niScope_SetAttributeViReal64')
                self.niScope_SetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViReal64]  # noqa: F405
                self.niScope_SetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_SetAttributeViReal64_cfunc(vi, channel_list, attribute_id, value)

    def niScope_SetAttributeViString(self, vi, channel_list, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niScope_SetAttributeViString_cfunc is None:
                self.niScope_SetAttributeViString_cfunc = self._get_library_function('niScope_SetAttributeViString')
                self.niScope_SetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niScope_SetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_SetAttributeViString_cfunc(vi, channel_list, attribute_id, value)

    def niScope_UnlockSession(self, vi, caller_has_lock):  # noqa: N802
        with self._func_lock:
            if self.niScope_UnlockSession_cfunc is None:
                self.niScope_UnlockSession_cfunc = self._get_library_function('niScope_UnlockSession')
                self.niScope_UnlockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niScope_UnlockSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_UnlockSession_cfunc(vi, caller_has_lock)

    def niScope_close(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niScope_close_cfunc is None:
                self.niScope_close_cfunc = self._get_library_function('niScope_close')
                self.niScope_close_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_close_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_close_cfunc(vi)

    def niScope_error_message(self, vi, error_code, error_message):  # noqa: N802
        with self._func_lock:
            if self.niScope_error_message_cfunc is None:
                self.niScope_error_message_cfunc = self._get_library_function('niScope_error_message')
                self.niScope_error_message_cfunc.argtypes = [ViSession, ViStatus, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niScope_error_message_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_error_message_cfunc(vi, error_code, error_message)

    def niScope_reset(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niScope_reset_cfunc is None:
                self.niScope_reset_cfunc = self._get_library_function('niScope_reset')
                self.niScope_reset_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_reset_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_reset_cfunc(vi)

    def niScope_self_test(self, vi, self_test_result, self_test_message):  # noqa: N802
        with self._func_lock:
            if self.niScope_self_test_cfunc is None:
                self.niScope_self_test_cfunc = self._get_library_function('niScope_self_test')
                self.niScope_self_test_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt16), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niScope_self_test_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_self_test_cfunc(vi, self_test_result, self_test_message)
