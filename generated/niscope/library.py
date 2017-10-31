# This file was generated

import ctypes
import threading

from niscope.visatype import *  # noqa: F403,H303


class Library(object):
    '''Library

    Wrapper around driver library.
    Class will setup the correct ctypes information for every function on first call.
    '''

    def __init__(self, library_name, library_type):
        self._func_lock = threading.Lock()
        # We cache the cfunc object from the ctypes.CDLL object
        self.niScope_Abort_cfunc = None
        self.niScope_AcquisitionStatus_cfunc = None
        self.niScope_ActualMeasWfmSize_cfunc = None
        self.niScope_ActualNumWfms_cfunc = None
        self.niScope_ActualRecordLength_cfunc = None
        self.niScope_AddWaveformProcessing_cfunc = None
        self.niScope_AdjustSampleClockRelativeDelay_cfunc = None
        self.niScope_AutoSetup_cfunc = None
        self.niScope_CalSelfCalibrate_cfunc = None
        self.niScope_CheckAttributeViBoolean_cfunc = None
        self.niScope_CheckAttributeViInt32_cfunc = None
        self.niScope_CheckAttributeViInt64_cfunc = None
        self.niScope_CheckAttributeViReal64_cfunc = None
        self.niScope_CheckAttributeViSession_cfunc = None
        self.niScope_CheckAttributeViString_cfunc = None
        self.niScope_ClearWaveformMeasurementStats_cfunc = None
        self.niScope_ClearWaveformProcessing_cfunc = None
        self.niScope_Commit_cfunc = None
        self.niScope_ConfigureAcquisition_cfunc = None
        self.niScope_ConfigureAcquisitionRecord_cfunc = None
        self.niScope_ConfigureChanCharacteristics_cfunc = None
        self.niScope_ConfigureChannel_cfunc = None
        self.niScope_ConfigureClock_cfunc = None
        self.niScope_ConfigureEdgeTriggerSource_cfunc = None
        self.niScope_ConfigureEqualizationFilterCoefficients_cfunc = None
        self.niScope_ConfigureHorizontalTiming_cfunc = None
        self.niScope_ConfigureRefLevels_cfunc = None
        self.niScope_ConfigureTVTriggerLineNumber_cfunc = None
        self.niScope_ConfigureTVTriggerSource_cfunc = None
        self.niScope_ConfigureTrigger_cfunc = None
        self.niScope_ConfigureTriggerCoupling_cfunc = None
        self.niScope_ConfigureTriggerDigital_cfunc = None
        self.niScope_ConfigureTriggerEdge_cfunc = None
        self.niScope_ConfigureTriggerHysteresis_cfunc = None
        self.niScope_ConfigureTriggerImmediate_cfunc = None
        self.niScope_ConfigureTriggerOutput_cfunc = None
        self.niScope_ConfigureTriggerSoftware_cfunc = None
        self.niScope_ConfigureTriggerVideo_cfunc = None
        self.niScope_ConfigureTriggerWindow_cfunc = None
        self.niScope_ConfigureVertical_cfunc = None
        self.niScope_Disable_cfunc = None
        self.niScope_ExportSignal_cfunc = None
        self.niScope_FetchMeasurement_cfunc = None
        self.niScope_FetchMeasurementStats_cfunc = None
        self.niScope_FetchWaveform_cfunc = None
        self.niScope_FetchWaveformMeasurement_cfunc = None
        self.niScope_GetAttributeViBoolean_cfunc = None
        self.niScope_GetAttributeViInt32_cfunc = None
        self.niScope_GetAttributeViInt64_cfunc = None
        self.niScope_GetAttributeViReal64_cfunc = None
        self.niScope_GetAttributeViString_cfunc = None
        self.niScope_GetChannelName_cfunc = None
        self.niScope_GetEqualizationFilterCoefficients_cfunc = None
        self.niScope_GetError_cfunc = None
        self.niScope_GetErrorMessage_cfunc = None
        self.niScope_GetFrequencyResponse_cfunc = None
        self.niScope_GetStreamEndpointHandle_cfunc = None
        self.niScope_InitWithOptions_cfunc = None
        self.niScope_InitiateAcquisition_cfunc = None
        self.niScope_IsDeviceReady_cfunc = None
        self.niScope_IsInvalidWfmElement_cfunc = None
        self.niScope_ProbeCompensationSignalStart_cfunc = None
        self.niScope_ProbeCompensationSignalStop_cfunc = None
        self.niScope_ReadMeasurement_cfunc = None
        self.niScope_ReadWaveform_cfunc = None
        self.niScope_ReadWaveformMeasurement_cfunc = None
        self.niScope_ResetDevice_cfunc = None
        self.niScope_ResetWithDefaults_cfunc = None
        self.niScope_SampleRate_cfunc = None
        self.niScope_SendSWTrigger_cfunc = None
        self.niScope_SendSoftwareTriggerEdge_cfunc = None
        self.niScope_SetAttributeViBoolean_cfunc = None
        self.niScope_SetAttributeViInt32_cfunc = None
        self.niScope_SetAttributeViInt64_cfunc = None
        self.niScope_SetAttributeViReal64_cfunc = None
        self.niScope_SetAttributeViString_cfunc = None
        self.niScope_close_cfunc = None
        self.niScope_errorHandler_cfunc = None
        self.niScope_reset_cfunc = None
        self.niScope_self_test_cfunc = None

        if library_type == 'windll':
            self._library = ctypes.WinDLL(library_name)
        else:  # pragma: no cover
            assert library_type == 'cdll'
            self._library = ctypes.CDLL(library_name)

    def niScope_Abort(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niScope_Abort_cfunc is None:
                self.niScope_Abort_cfunc = self._library.niScope_Abort
                self.niScope_Abort_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_Abort_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_Abort_cfunc(vi)

    def niScope_AcquisitionStatus(self, vi, acquisition_status):  # noqa: N802
        with self._func_lock:
            if self.niScope_AcquisitionStatus_cfunc is None:
                self.niScope_AcquisitionStatus_cfunc = self._library.niScope_AcquisitionStatus
                self.niScope_AcquisitionStatus_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niScope_AcquisitionStatus_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_AcquisitionStatus_cfunc(vi, acquisition_status)

    def niScope_ActualMeasWfmSize(self, vi, array_meas_function, meas_waveform_size):  # noqa: N802
        with self._func_lock:
            if self.niScope_ActualMeasWfmSize_cfunc is None:
                self.niScope_ActualMeasWfmSize_cfunc = self._library.niScope_ActualMeasWfmSize
                self.niScope_ActualMeasWfmSize_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niScope_ActualMeasWfmSize_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ActualMeasWfmSize_cfunc(vi, array_meas_function, meas_waveform_size)

    def niScope_ActualNumWfms(self, vi, channel_list, num_wfms):  # noqa: N802
        with self._func_lock:
            if self.niScope_ActualNumWfms_cfunc is None:
                self.niScope_ActualNumWfms_cfunc = self._library.niScope_ActualNumWfms
                self.niScope_ActualNumWfms_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niScope_ActualNumWfms_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ActualNumWfms_cfunc(vi, channel_list, num_wfms)

    def niScope_ActualRecordLength(self, vi, record_length):  # noqa: N802
        with self._func_lock:
            if self.niScope_ActualRecordLength_cfunc is None:
                self.niScope_ActualRecordLength_cfunc = self._library.niScope_ActualRecordLength
                self.niScope_ActualRecordLength_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niScope_ActualRecordLength_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ActualRecordLength_cfunc(vi, record_length)

    def niScope_AddWaveformProcessing(self, vi, channel_list, meas_function):  # noqa: N802
        with self._func_lock:
            if self.niScope_AddWaveformProcessing_cfunc is None:
                self.niScope_AddWaveformProcessing_cfunc = self._library.niScope_AddWaveformProcessing
                self.niScope_AddWaveformProcessing_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niScope_AddWaveformProcessing_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_AddWaveformProcessing_cfunc(vi, channel_list, meas_function)

    def niScope_AdjustSampleClockRelativeDelay(self, vi, delay):  # noqa: N802
        with self._func_lock:
            if self.niScope_AdjustSampleClockRelativeDelay_cfunc is None:
                self.niScope_AdjustSampleClockRelativeDelay_cfunc = self._library.niScope_AdjustSampleClockRelativeDelay
                self.niScope_AdjustSampleClockRelativeDelay_cfunc.argtypes = [ViSession, ViReal64]  # noqa: F405
                self.niScope_AdjustSampleClockRelativeDelay_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_AdjustSampleClockRelativeDelay_cfunc(vi, delay)

    def niScope_AutoSetup(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niScope_AutoSetup_cfunc is None:
                self.niScope_AutoSetup_cfunc = self._library.niScope_AutoSetup
                self.niScope_AutoSetup_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_AutoSetup_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_AutoSetup_cfunc(vi)

    def niScope_CalSelfCalibrate(self, vi, channel_list, option):  # noqa: N802
        with self._func_lock:
            if self.niScope_CalSelfCalibrate_cfunc is None:
                self.niScope_CalSelfCalibrate_cfunc = self._library.niScope_CalSelfCalibrate
                self.niScope_CalSelfCalibrate_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niScope_CalSelfCalibrate_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_CalSelfCalibrate_cfunc(vi, channel_list, option)

    def niScope_CheckAttributeViBoolean(self, vi, channel_list, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niScope_CheckAttributeViBoolean_cfunc is None:
                self.niScope_CheckAttributeViBoolean_cfunc = self._library.niScope_CheckAttributeViBoolean
                self.niScope_CheckAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViBoolean]  # noqa: F405
                self.niScope_CheckAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_CheckAttributeViBoolean_cfunc(vi, channel_list, attribute_id, value)

    def niScope_CheckAttributeViInt32(self, vi, channel_list, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niScope_CheckAttributeViInt32_cfunc is None:
                self.niScope_CheckAttributeViInt32_cfunc = self._library.niScope_CheckAttributeViInt32
                self.niScope_CheckAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32]  # noqa: F405
                self.niScope_CheckAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_CheckAttributeViInt32_cfunc(vi, channel_list, attribute_id, value)

    def niScope_CheckAttributeViInt64(self, vi, channel_list, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niScope_CheckAttributeViInt64_cfunc is None:
                self.niScope_CheckAttributeViInt64_cfunc = self._library.niScope_CheckAttributeViInt64
                self.niScope_CheckAttributeViInt64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt64]  # noqa: F405
                self.niScope_CheckAttributeViInt64_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_CheckAttributeViInt64_cfunc(vi, channel_list, attribute_id, value)

    def niScope_CheckAttributeViReal64(self, vi, channel_list, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niScope_CheckAttributeViReal64_cfunc is None:
                self.niScope_CheckAttributeViReal64_cfunc = self._library.niScope_CheckAttributeViReal64
                self.niScope_CheckAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViReal64]  # noqa: F405
                self.niScope_CheckAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_CheckAttributeViReal64_cfunc(vi, channel_list, attribute_id, value)

    def niScope_CheckAttributeViSession(self, vi, channel_list, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niScope_CheckAttributeViSession_cfunc is None:
                self.niScope_CheckAttributeViSession_cfunc = self._library.niScope_CheckAttributeViSession
                self.niScope_CheckAttributeViSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViSession]  # noqa: F405
                self.niScope_CheckAttributeViSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_CheckAttributeViSession_cfunc(vi, channel_list, attribute_id, value)

    def niScope_CheckAttributeViString(self, vi, channel_list, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niScope_CheckAttributeViString_cfunc is None:
                self.niScope_CheckAttributeViString_cfunc = self._library.niScope_CheckAttributeViString
                self.niScope_CheckAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niScope_CheckAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_CheckAttributeViString_cfunc(vi, channel_list, attribute_id, value)

    def niScope_ClearWaveformMeasurementStats(self, vi, channel_list, clearable_measurement_function):  # noqa: N802
        with self._func_lock:
            if self.niScope_ClearWaveformMeasurementStats_cfunc is None:
                self.niScope_ClearWaveformMeasurementStats_cfunc = self._library.niScope_ClearWaveformMeasurementStats
                self.niScope_ClearWaveformMeasurementStats_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niScope_ClearWaveformMeasurementStats_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ClearWaveformMeasurementStats_cfunc(vi, channel_list, clearable_measurement_function)

    def niScope_ClearWaveformProcessing(self, vi, channel_list):  # noqa: N802
        with self._func_lock:
            if self.niScope_ClearWaveformProcessing_cfunc is None:
                self.niScope_ClearWaveformProcessing_cfunc = self._library.niScope_ClearWaveformProcessing
                self.niScope_ClearWaveformProcessing_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niScope_ClearWaveformProcessing_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ClearWaveformProcessing_cfunc(vi, channel_list)

    def niScope_Commit(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niScope_Commit_cfunc is None:
                self.niScope_Commit_cfunc = self._library.niScope_Commit
                self.niScope_Commit_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_Commit_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_Commit_cfunc(vi)

    def niScope_ConfigureAcquisition(self, vi, acquisition_type):  # noqa: N802
        with self._func_lock:
            if self.niScope_ConfigureAcquisition_cfunc is None:
                self.niScope_ConfigureAcquisition_cfunc = self._library.niScope_ConfigureAcquisition
                self.niScope_ConfigureAcquisition_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niScope_ConfigureAcquisition_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ConfigureAcquisition_cfunc(vi, acquisition_type)

    def niScope_ConfigureAcquisitionRecord(self, vi, time_per_record, min_num_points, acquisition_start_time):  # noqa: N802
        with self._func_lock:
            if self.niScope_ConfigureAcquisitionRecord_cfunc is None:
                self.niScope_ConfigureAcquisitionRecord_cfunc = self._library.niScope_ConfigureAcquisitionRecord
                self.niScope_ConfigureAcquisitionRecord_cfunc.argtypes = [ViSession, ViReal64, ViInt32, ViReal64]  # noqa: F405
                self.niScope_ConfigureAcquisitionRecord_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ConfigureAcquisitionRecord_cfunc(vi, time_per_record, min_num_points, acquisition_start_time)

    def niScope_ConfigureChanCharacteristics(self, vi, channel_list, input_impedance, max_input_frequency):  # noqa: N802
        with self._func_lock:
            if self.niScope_ConfigureChanCharacteristics_cfunc is None:
                self.niScope_ConfigureChanCharacteristics_cfunc = self._library.niScope_ConfigureChanCharacteristics
                self.niScope_ConfigureChanCharacteristics_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViReal64]  # noqa: F405
                self.niScope_ConfigureChanCharacteristics_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ConfigureChanCharacteristics_cfunc(vi, channel_list, input_impedance, max_input_frequency)

    def niScope_ConfigureChannel(self, vi, channel, range, offset, coupling, probe_attenuation, enabled):  # noqa: N802
        with self._func_lock:
            if self.niScope_ConfigureChannel_cfunc is None:
                self.niScope_ConfigureChannel_cfunc = self._library.niScope_ConfigureChannel
                self.niScope_ConfigureChannel_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViReal64, ViInt32, ViReal64, ViBoolean]  # noqa: F405
                self.niScope_ConfigureChannel_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ConfigureChannel_cfunc(vi, channel, range, offset, coupling, probe_attenuation, enabled)

    def niScope_ConfigureClock(self, vi, input_clock_source, output_clock_source, clock_sync_pulse_source, master_enabled):  # noqa: N802
        with self._func_lock:
            if self.niScope_ConfigureClock_cfunc is None:
                self.niScope_ConfigureClock_cfunc = self._library.niScope_ConfigureClock
                self.niScope_ConfigureClock_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViBoolean]  # noqa: F405
                self.niScope_ConfigureClock_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ConfigureClock_cfunc(vi, input_clock_source, output_clock_source, clock_sync_pulse_source, master_enabled)

    def niScope_ConfigureEdgeTriggerSource(self, vi, source, level, slope):  # noqa: N802
        with self._func_lock:
            if self.niScope_ConfigureEdgeTriggerSource_cfunc is None:
                self.niScope_ConfigureEdgeTriggerSource_cfunc = self._library.niScope_ConfigureEdgeTriggerSource
                self.niScope_ConfigureEdgeTriggerSource_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViInt32]  # noqa: F405
                self.niScope_ConfigureEdgeTriggerSource_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ConfigureEdgeTriggerSource_cfunc(vi, source, level, slope)

    def niScope_ConfigureEqualizationFilterCoefficients(self, vi, channel_list, number_of_coefficients, coefficients):  # noqa: N802
        with self._func_lock:
            if self.niScope_ConfigureEqualizationFilterCoefficients_cfunc is None:
                self.niScope_ConfigureEqualizationFilterCoefficients_cfunc = self._library.niScope_ConfigureEqualizationFilterCoefficients
                self.niScope_ConfigureEqualizationFilterCoefficients_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niScope_ConfigureEqualizationFilterCoefficients_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ConfigureEqualizationFilterCoefficients_cfunc(vi, channel_list, number_of_coefficients, coefficients)

    def niScope_ConfigureHorizontalTiming(self, vi, min_sample_rate, min_num_pts, ref_position, num_records, enforce_realtime):  # noqa: N802
        with self._func_lock:
            if self.niScope_ConfigureHorizontalTiming_cfunc is None:
                self.niScope_ConfigureHorizontalTiming_cfunc = self._library.niScope_ConfigureHorizontalTiming
                self.niScope_ConfigureHorizontalTiming_cfunc.argtypes = [ViSession, ViReal64, ViInt32, ViReal64, ViInt32, ViBoolean]  # noqa: F405
                self.niScope_ConfigureHorizontalTiming_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ConfigureHorizontalTiming_cfunc(vi, min_sample_rate, min_num_pts, ref_position, num_records, enforce_realtime)

    def niScope_ConfigureRefLevels(self, vi, low, mid, high):  # noqa: N802
        with self._func_lock:
            if self.niScope_ConfigureRefLevels_cfunc is None:
                self.niScope_ConfigureRefLevels_cfunc = self._library.niScope_ConfigureRefLevels
                self.niScope_ConfigureRefLevels_cfunc.argtypes = [ViSession, ViReal64, ViReal64, ViReal64]  # noqa: F405
                self.niScope_ConfigureRefLevels_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ConfigureRefLevels_cfunc(vi, low, mid, high)

    def niScope_ConfigureTVTriggerLineNumber(self, vi, line_number):  # noqa: N802
        with self._func_lock:
            if self.niScope_ConfigureTVTriggerLineNumber_cfunc is None:
                self.niScope_ConfigureTVTriggerLineNumber_cfunc = self._library.niScope_ConfigureTVTriggerLineNumber
                self.niScope_ConfigureTVTriggerLineNumber_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niScope_ConfigureTVTriggerLineNumber_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ConfigureTVTriggerLineNumber_cfunc(vi, line_number)

    def niScope_ConfigureTVTriggerSource(self, vi, source, signal_format, event, polarity):  # noqa: N802
        with self._func_lock:
            if self.niScope_ConfigureTVTriggerSource_cfunc is None:
                self.niScope_ConfigureTVTriggerSource_cfunc = self._library.niScope_ConfigureTVTriggerSource
                self.niScope_ConfigureTVTriggerSource_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViInt32, ViInt32]  # noqa: F405
                self.niScope_ConfigureTVTriggerSource_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ConfigureTVTriggerSource_cfunc(vi, source, signal_format, event, polarity)

    def niScope_ConfigureTrigger(self, vi, trigger_type, holdoff):  # noqa: N802
        with self._func_lock:
            if self.niScope_ConfigureTrigger_cfunc is None:
                self.niScope_ConfigureTrigger_cfunc = self._library.niScope_ConfigureTrigger
                self.niScope_ConfigureTrigger_cfunc.argtypes = [ViSession, ViInt32, ViReal64]  # noqa: F405
                self.niScope_ConfigureTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ConfigureTrigger_cfunc(vi, trigger_type, holdoff)

    def niScope_ConfigureTriggerCoupling(self, vi, coupling):  # noqa: N802
        with self._func_lock:
            if self.niScope_ConfigureTriggerCoupling_cfunc is None:
                self.niScope_ConfigureTriggerCoupling_cfunc = self._library.niScope_ConfigureTriggerCoupling
                self.niScope_ConfigureTriggerCoupling_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niScope_ConfigureTriggerCoupling_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ConfigureTriggerCoupling_cfunc(vi, coupling)

    def niScope_ConfigureTriggerDigital(self, vi, trigger_source, slope, holdoff, delay):  # noqa: N802
        with self._func_lock:
            if self.niScope_ConfigureTriggerDigital_cfunc is None:
                self.niScope_ConfigureTriggerDigital_cfunc = self._library.niScope_ConfigureTriggerDigital
                self.niScope_ConfigureTriggerDigital_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViReal64, ViReal64]  # noqa: F405
                self.niScope_ConfigureTriggerDigital_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ConfigureTriggerDigital_cfunc(vi, trigger_source, slope, holdoff, delay)

    def niScope_ConfigureTriggerEdge(self, vi, trigger_source, level, slope, trigger_coupling, holdoff, delay):  # noqa: N802
        with self._func_lock:
            if self.niScope_ConfigureTriggerEdge_cfunc is None:
                self.niScope_ConfigureTriggerEdge_cfunc = self._library.niScope_ConfigureTriggerEdge
                self.niScope_ConfigureTriggerEdge_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViInt32, ViInt32, ViReal64, ViReal64]  # noqa: F405
                self.niScope_ConfigureTriggerEdge_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ConfigureTriggerEdge_cfunc(vi, trigger_source, level, slope, trigger_coupling, holdoff, delay)

    def niScope_ConfigureTriggerHysteresis(self, vi, trigger_source, level, hysteresis, slope, trigger_coupling, holdoff, delay):  # noqa: N802
        with self._func_lock:
            if self.niScope_ConfigureTriggerHysteresis_cfunc is None:
                self.niScope_ConfigureTriggerHysteresis_cfunc = self._library.niScope_ConfigureTriggerHysteresis
                self.niScope_ConfigureTriggerHysteresis_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViReal64, ViInt32, ViInt32, ViReal64, ViReal64]  # noqa: F405
                self.niScope_ConfigureTriggerHysteresis_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ConfigureTriggerHysteresis_cfunc(vi, trigger_source, level, hysteresis, slope, trigger_coupling, holdoff, delay)

    def niScope_ConfigureTriggerImmediate(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niScope_ConfigureTriggerImmediate_cfunc is None:
                self.niScope_ConfigureTriggerImmediate_cfunc = self._library.niScope_ConfigureTriggerImmediate
                self.niScope_ConfigureTriggerImmediate_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_ConfigureTriggerImmediate_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ConfigureTriggerImmediate_cfunc(vi)

    def niScope_ConfigureTriggerOutput(self, vi, trigger_event, trigger_output):  # noqa: N802
        with self._func_lock:
            if self.niScope_ConfigureTriggerOutput_cfunc is None:
                self.niScope_ConfigureTriggerOutput_cfunc = self._library.niScope_ConfigureTriggerOutput
                self.niScope_ConfigureTriggerOutput_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niScope_ConfigureTriggerOutput_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ConfigureTriggerOutput_cfunc(vi, trigger_event, trigger_output)

    def niScope_ConfigureTriggerSoftware(self, vi, holdoff, delay):  # noqa: N802
        with self._func_lock:
            if self.niScope_ConfigureTriggerSoftware_cfunc is None:
                self.niScope_ConfigureTriggerSoftware_cfunc = self._library.niScope_ConfigureTriggerSoftware
                self.niScope_ConfigureTriggerSoftware_cfunc.argtypes = [ViSession, ViReal64, ViReal64]  # noqa: F405
                self.niScope_ConfigureTriggerSoftware_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ConfigureTriggerSoftware_cfunc(vi, holdoff, delay)

    def niScope_ConfigureTriggerVideo(self, vi, trigger_source, enable_dc_restore, signal_format, event, line_number, polarity, trigger_coupling, holdoff, delay):  # noqa: N802
        with self._func_lock:
            if self.niScope_ConfigureTriggerVideo_cfunc is None:
                self.niScope_ConfigureTriggerVideo_cfunc = self._library.niScope_ConfigureTriggerVideo
                self.niScope_ConfigureTriggerVideo_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViBoolean, ViInt32, ViInt32, ViInt32, ViInt32, ViInt32, ViReal64, ViReal64]  # noqa: F405
                self.niScope_ConfigureTriggerVideo_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ConfigureTriggerVideo_cfunc(vi, trigger_source, enable_dc_restore, signal_format, event, line_number, polarity, trigger_coupling, holdoff, delay)

    def niScope_ConfigureTriggerWindow(self, vi, trigger_source, low_level, high_level, window_mode, trigger_coupling, holdoff, delay):  # noqa: N802
        with self._func_lock:
            if self.niScope_ConfigureTriggerWindow_cfunc is None:
                self.niScope_ConfigureTriggerWindow_cfunc = self._library.niScope_ConfigureTriggerWindow
                self.niScope_ConfigureTriggerWindow_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViReal64, ViInt32, ViInt32, ViReal64, ViReal64]  # noqa: F405
                self.niScope_ConfigureTriggerWindow_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ConfigureTriggerWindow_cfunc(vi, trigger_source, low_level, high_level, window_mode, trigger_coupling, holdoff, delay)

    def niScope_ConfigureVertical(self, vi, channel_list, range, offset, coupling, probe_attenuation, enabled):  # noqa: N802
        with self._func_lock:
            if self.niScope_ConfigureVertical_cfunc is None:
                self.niScope_ConfigureVertical_cfunc = self._library.niScope_ConfigureVertical
                self.niScope_ConfigureVertical_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViReal64, ViInt32, ViReal64, ViBoolean]  # noqa: F405
                self.niScope_ConfigureVertical_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ConfigureVertical_cfunc(vi, channel_list, range, offset, coupling, probe_attenuation, enabled)

    def niScope_Disable(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niScope_Disable_cfunc is None:
                self.niScope_Disable_cfunc = self._library.niScope_Disable
                self.niScope_Disable_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_Disable_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_Disable_cfunc(vi)

    def niScope_ExportSignal(self, vi, signal, signal_identifier, output_terminal):  # noqa: N802
        with self._func_lock:
            if self.niScope_ExportSignal_cfunc is None:
                self.niScope_ExportSignal_cfunc = self._library.niScope_ExportSignal
                self.niScope_ExportSignal_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niScope_ExportSignal_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ExportSignal_cfunc(vi, signal, signal_identifier, output_terminal)

    def niScope_FetchMeasurement(self, vi, channel_list, timeout, scalar_meas_function, result):  # noqa: N802
        with self._func_lock:
            if self.niScope_FetchMeasurement_cfunc is None:
                self.niScope_FetchMeasurement_cfunc = self._library.niScope_FetchMeasurement
                self.niScope_FetchMeasurement_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niScope_FetchMeasurement_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_FetchMeasurement_cfunc(vi, channel_list, timeout, scalar_meas_function, result)

    def niScope_FetchMeasurementStats(self, vi, channel_list, timeout, scalar_meas_function, result, mean, stdev, min, max, num_in_stats):  # noqa: N802
        with self._func_lock:
            if self.niScope_FetchMeasurementStats_cfunc is None:
                self.niScope_FetchMeasurementStats_cfunc = self._library.niScope_FetchMeasurementStats
                self.niScope_FetchMeasurementStats_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niScope_FetchMeasurementStats_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_FetchMeasurementStats_cfunc(vi, channel_list, timeout, scalar_meas_function, result, mean, stdev, min, max, num_in_stats)

    def niScope_FetchWaveform(self, vi, channel, waveform_size, waveform, actual_points, initial_x, x_increment):  # noqa: N802
        with self._func_lock:
            if self.niScope_FetchWaveform_cfunc is None:
                self.niScope_FetchWaveform_cfunc = self._library.niScope_FetchWaveform
                self.niScope_FetchWaveform_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32), ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niScope_FetchWaveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_FetchWaveform_cfunc(vi, channel, waveform_size, waveform, actual_points, initial_x, x_increment)

    def niScope_FetchWaveformMeasurement(self, vi, channel, meas_function, measurement):  # noqa: N802
        with self._func_lock:
            if self.niScope_FetchWaveformMeasurement_cfunc is None:
                self.niScope_FetchWaveformMeasurement_cfunc = self._library.niScope_FetchWaveformMeasurement
                self.niScope_FetchWaveformMeasurement_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niScope_FetchWaveformMeasurement_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_FetchWaveformMeasurement_cfunc(vi, channel, meas_function, measurement)

    def niScope_GetAttributeViBoolean(self, vi, channel_list, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niScope_GetAttributeViBoolean_cfunc is None:
                self.niScope_GetAttributeViBoolean_cfunc = self._library.niScope_GetAttributeViBoolean
                self.niScope_GetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niScope_GetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_GetAttributeViBoolean_cfunc(vi, channel_list, attribute_id, value)

    def niScope_GetAttributeViInt32(self, vi, channel_list, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niScope_GetAttributeViInt32_cfunc is None:
                self.niScope_GetAttributeViInt32_cfunc = self._library.niScope_GetAttributeViInt32
                self.niScope_GetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niScope_GetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_GetAttributeViInt32_cfunc(vi, channel_list, attribute_id, value)

    def niScope_GetAttributeViInt64(self, vi, channel_list, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niScope_GetAttributeViInt64_cfunc is None:
                self.niScope_GetAttributeViInt64_cfunc = self._library.niScope_GetAttributeViInt64
                self.niScope_GetAttributeViInt64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViInt64)]  # noqa: F405
                self.niScope_GetAttributeViInt64_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_GetAttributeViInt64_cfunc(vi, channel_list, attribute_id, value)

    def niScope_GetAttributeViReal64(self, vi, channel_list, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niScope_GetAttributeViReal64_cfunc is None:
                self.niScope_GetAttributeViReal64_cfunc = self._library.niScope_GetAttributeViReal64
                self.niScope_GetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niScope_GetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_GetAttributeViReal64_cfunc(vi, channel_list, attribute_id, value)

    def niScope_GetAttributeViString(self, vi, channel_list, attribute_id, buf_size, value):  # noqa: N802
        with self._func_lock:
            if self.niScope_GetAttributeViString_cfunc is None:
                self.niScope_GetAttributeViString_cfunc = self._library.niScope_GetAttributeViString
                self.niScope_GetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niScope_GetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_GetAttributeViString_cfunc(vi, channel_list, attribute_id, buf_size, value)

    def niScope_GetChannelName(self, vi, index, buffer_size, channel_string):  # noqa: N802
        with self._func_lock:
            if self.niScope_GetChannelName_cfunc is None:
                self.niScope_GetChannelName_cfunc = self._library.niScope_GetChannelName
                self.niScope_GetChannelName_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niScope_GetChannelName_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_GetChannelName_cfunc(vi, index, buffer_size, channel_string)

    def niScope_GetEqualizationFilterCoefficients(self, vi, channel, number_of_coefficients, coefficients):  # noqa: N802
        with self._func_lock:
            if self.niScope_GetEqualizationFilterCoefficients_cfunc is None:
                self.niScope_GetEqualizationFilterCoefficients_cfunc = self._library.niScope_GetEqualizationFilterCoefficients
                self.niScope_GetEqualizationFilterCoefficients_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niScope_GetEqualizationFilterCoefficients_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_GetEqualizationFilterCoefficients_cfunc(vi, channel, number_of_coefficients, coefficients)

    def niScope_GetError(self, vi, error_code, buffer_size, description):  # noqa: N802
        with self._func_lock:
            if self.niScope_GetError_cfunc is None:
                self.niScope_GetError_cfunc = self._library.niScope_GetError
                self.niScope_GetError_cfunc.argtypes = [ViSession, ctypes.POINTER(ViStatus), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niScope_GetError_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_GetError_cfunc(vi, error_code, buffer_size, description)

    def niScope_GetErrorMessage(self, vi, error_code, buffer__size, error_message):  # noqa: N802
        with self._func_lock:
            if self.niScope_GetErrorMessage_cfunc is None:
                self.niScope_GetErrorMessage_cfunc = self._library.niScope_GetErrorMessage
                self.niScope_GetErrorMessage_cfunc.argtypes = [ViSession, ViStatus, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niScope_GetErrorMessage_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_GetErrorMessage_cfunc(vi, error_code, buffer__size, error_message)

    def niScope_GetFrequencyResponse(self, vi, channel, buffer_size, frequencies, amplitudes, phases, number_of_frequencies):  # noqa: N802
        with self._func_lock:
            if self.niScope_GetFrequencyResponse_cfunc is None:
                self.niScope_GetFrequencyResponse_cfunc = self._library.niScope_GetFrequencyResponse
                self.niScope_GetFrequencyResponse_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niScope_GetFrequencyResponse_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_GetFrequencyResponse_cfunc(vi, channel, buffer_size, frequencies, amplitudes, phases, number_of_frequencies)

    def niScope_GetStreamEndpointHandle(self, vi, stream_name, writer_handle):  # noqa: N802
        with self._func_lock:
            if self.niScope_GetStreamEndpointHandle_cfunc is None:
                self.niScope_GetStreamEndpointHandle_cfunc = self._library.niScope_GetStreamEndpointHandle
                self.niScope_GetStreamEndpointHandle_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViUInt32)]  # noqa: F405
                self.niScope_GetStreamEndpointHandle_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_GetStreamEndpointHandle_cfunc(vi, stream_name, writer_handle)

    def niScope_InitWithOptions(self, resource_name, id_query, reset_device, option_string, vi):  # noqa: N802
        with self._func_lock:
            if self.niScope_InitWithOptions_cfunc is None:
                self.niScope_InitWithOptions_cfunc = self._library.niScope_InitWithOptions
                self.niScope_InitWithOptions_cfunc.argtypes = [ctypes.POINTER(ViChar), ViBoolean, ViBoolean, ctypes.POINTER(ViChar), ctypes.POINTER(ViSession)]  # noqa: F405
                self.niScope_InitWithOptions_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_InitWithOptions_cfunc(resource_name, id_query, reset_device, option_string, vi)

    def niScope_InitiateAcquisition(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niScope_InitiateAcquisition_cfunc is None:
                self.niScope_InitiateAcquisition_cfunc = self._library.niScope_InitiateAcquisition
                self.niScope_InitiateAcquisition_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_InitiateAcquisition_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_InitiateAcquisition_cfunc(vi)

    def niScope_IsDeviceReady(self, resource_name, channel_list, device_ready):  # noqa: N802
        with self._func_lock:
            if self.niScope_IsDeviceReady_cfunc is None:
                self.niScope_IsDeviceReady_cfunc = self._library.niScope_IsDeviceReady
                self.niScope_IsDeviceReady_cfunc.argtypes = [ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niScope_IsDeviceReady_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_IsDeviceReady_cfunc(resource_name, channel_list, device_ready)

    def niScope_IsInvalidWfmElement(self, vi, element_value, is_invalid):  # noqa: N802
        with self._func_lock:
            if self.niScope_IsInvalidWfmElement_cfunc is None:
                self.niScope_IsInvalidWfmElement_cfunc = self._library.niScope_IsInvalidWfmElement
                self.niScope_IsInvalidWfmElement_cfunc.argtypes = [ViSession, ViReal64, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niScope_IsInvalidWfmElement_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_IsInvalidWfmElement_cfunc(vi, element_value, is_invalid)

    def niScope_ProbeCompensationSignalStart(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niScope_ProbeCompensationSignalStart_cfunc is None:
                self.niScope_ProbeCompensationSignalStart_cfunc = self._library.niScope_ProbeCompensationSignalStart
                self.niScope_ProbeCompensationSignalStart_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_ProbeCompensationSignalStart_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ProbeCompensationSignalStart_cfunc(vi)

    def niScope_ProbeCompensationSignalStop(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niScope_ProbeCompensationSignalStop_cfunc is None:
                self.niScope_ProbeCompensationSignalStop_cfunc = self._library.niScope_ProbeCompensationSignalStop
                self.niScope_ProbeCompensationSignalStop_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_ProbeCompensationSignalStop_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ProbeCompensationSignalStop_cfunc(vi)

    def niScope_ReadMeasurement(self, vi, channel_list, timeout, scalar_meas_function, result):  # noqa: N802
        with self._func_lock:
            if self.niScope_ReadMeasurement_cfunc is None:
                self.niScope_ReadMeasurement_cfunc = self._library.niScope_ReadMeasurement
                self.niScope_ReadMeasurement_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niScope_ReadMeasurement_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ReadMeasurement_cfunc(vi, channel_list, timeout, scalar_meas_function, result)

    def niScope_ReadWaveform(self, vi, channel, waveform_size, max_time, waveform, actual_points, initial_x, x_increment):  # noqa: N802
        with self._func_lock:
            if self.niScope_ReadWaveform_cfunc is None:
                self.niScope_ReadWaveform_cfunc = self._library.niScope_ReadWaveform
                self.niScope_ReadWaveform_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32), ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niScope_ReadWaveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ReadWaveform_cfunc(vi, channel, waveform_size, max_time, waveform, actual_points, initial_x, x_increment)

    def niScope_ReadWaveformMeasurement(self, vi, channel, meas_function, max_time, measurement):  # noqa: N802
        with self._func_lock:
            if self.niScope_ReadWaveformMeasurement_cfunc is None:
                self.niScope_ReadWaveformMeasurement_cfunc = self._library.niScope_ReadWaveformMeasurement
                self.niScope_ReadWaveformMeasurement_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niScope_ReadWaveformMeasurement_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ReadWaveformMeasurement_cfunc(vi, channel, meas_function, max_time, measurement)

    def niScope_ResetDevice(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niScope_ResetDevice_cfunc is None:
                self.niScope_ResetDevice_cfunc = self._library.niScope_ResetDevice
                self.niScope_ResetDevice_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_ResetDevice_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ResetDevice_cfunc(vi)

    def niScope_ResetWithDefaults(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niScope_ResetWithDefaults_cfunc is None:
                self.niScope_ResetWithDefaults_cfunc = self._library.niScope_ResetWithDefaults
                self.niScope_ResetWithDefaults_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_ResetWithDefaults_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ResetWithDefaults_cfunc(vi)

    def niScope_SampleRate(self, vi, sample_rate):  # noqa: N802
        with self._func_lock:
            if self.niScope_SampleRate_cfunc is None:
                self.niScope_SampleRate_cfunc = self._library.niScope_SampleRate
                self.niScope_SampleRate_cfunc.argtypes = [ViSession, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niScope_SampleRate_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_SampleRate_cfunc(vi, sample_rate)

    def niScope_SendSWTrigger(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niScope_SendSWTrigger_cfunc is None:
                self.niScope_SendSWTrigger_cfunc = self._library.niScope_SendSWTrigger
                self.niScope_SendSWTrigger_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_SendSWTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_SendSWTrigger_cfunc(vi)

    def niScope_SendSoftwareTriggerEdge(self, vi, which_trigger):  # noqa: N802
        with self._func_lock:
            if self.niScope_SendSoftwareTriggerEdge_cfunc is None:
                self.niScope_SendSoftwareTriggerEdge_cfunc = self._library.niScope_SendSoftwareTriggerEdge
                self.niScope_SendSoftwareTriggerEdge_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niScope_SendSoftwareTriggerEdge_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_SendSoftwareTriggerEdge_cfunc(vi, which_trigger)

    def niScope_SetAttributeViBoolean(self, vi, channel_list, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niScope_SetAttributeViBoolean_cfunc is None:
                self.niScope_SetAttributeViBoolean_cfunc = self._library.niScope_SetAttributeViBoolean
                self.niScope_SetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViBoolean]  # noqa: F405
                self.niScope_SetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_SetAttributeViBoolean_cfunc(vi, channel_list, attribute_id, value)

    def niScope_SetAttributeViInt32(self, vi, channel_list, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niScope_SetAttributeViInt32_cfunc is None:
                self.niScope_SetAttributeViInt32_cfunc = self._library.niScope_SetAttributeViInt32
                self.niScope_SetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32]  # noqa: F405
                self.niScope_SetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_SetAttributeViInt32_cfunc(vi, channel_list, attribute_id, value)

    def niScope_SetAttributeViInt64(self, vi, channel_list, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niScope_SetAttributeViInt64_cfunc is None:
                self.niScope_SetAttributeViInt64_cfunc = self._library.niScope_SetAttributeViInt64
                self.niScope_SetAttributeViInt64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt64]  # noqa: F405
                self.niScope_SetAttributeViInt64_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_SetAttributeViInt64_cfunc(vi, channel_list, attribute_id, value)

    def niScope_SetAttributeViReal64(self, vi, channel_list, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niScope_SetAttributeViReal64_cfunc is None:
                self.niScope_SetAttributeViReal64_cfunc = self._library.niScope_SetAttributeViReal64
                self.niScope_SetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViReal64]  # noqa: F405
                self.niScope_SetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_SetAttributeViReal64_cfunc(vi, channel_list, attribute_id, value)

    def niScope_SetAttributeViString(self, vi, channel_list, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niScope_SetAttributeViString_cfunc is None:
                self.niScope_SetAttributeViString_cfunc = self._library.niScope_SetAttributeViString
                self.niScope_SetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niScope_SetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_SetAttributeViString_cfunc(vi, channel_list, attribute_id, value)

    def niScope_close(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niScope_close_cfunc is None:
                self.niScope_close_cfunc = self._library.niScope_close
                self.niScope_close_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_close_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_close_cfunc(vi)

    def niScope_errorHandler(self, vi, error_code, error_source, error_description):  # noqa: N802
        with self._func_lock:
            if self.niScope_errorHandler_cfunc is None:
                self.niScope_errorHandler_cfunc = self._library.niScope_errorHandler
                self.niScope_errorHandler_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niScope_errorHandler_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_errorHandler_cfunc(vi, error_code, error_source, error_description)

    def niScope_reset(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niScope_reset_cfunc is None:
                self.niScope_reset_cfunc = self._library.niScope_reset
                self.niScope_reset_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_reset_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_reset_cfunc(vi)

    def niScope_self_test(self, vi, self_test_result, self_test_message):  # noqa: N802
        with self._func_lock:
            if self.niScope_self_test_cfunc is None:
                self.niScope_self_test_cfunc = self._library.niScope_self_test
                self.niScope_self_test_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt16), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niScope_self_test_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_self_test_cfunc(vi, self_test_result, self_test_message)
