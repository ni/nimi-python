# This file was generated

import ctypes
import platform

from nidmm.ctypes_types import *

class nidmm_ctypes_library:

    def __init__(self, library_name):
    # We cache the cfunc object from the ctypes.CDLL object
        self.niDMM_InitWithOptions_cfunc = None
        self.niDMM_close_cfunc = None
        self.niDMM_GetError_cfunc = None
        self.niDMM_GetErrorMessage_cfunc = None
        self.niDMM_ClearError_cfunc = None
        self.niDMM_reset_cfunc = None
        self.niDMM_self_test_cfunc = None
        self.niDMM_SelfCal_cfunc = None
        self.niDMM_revision_query_cfunc = None
        self.niDMM_InvalidateAllAttributes_cfunc = None
        self.niDMM_ResetWithDefaults_cfunc = None
        self.niDMM_Disable_cfunc = None
        self.niDMM_GetMeasurementPeriod_cfunc = None
        self.niDMM_ConfigureTrigger_cfunc = None
        self.niDMM_Read_cfunc = None
        self.niDMM_Fetch_cfunc = None
        self.niDMM_Abort_cfunc = None
        self.niDMM_Initiate_cfunc = None
        self.niDMM_IsOverRange_cfunc = None
        self.niDMM_IsUnderRange_cfunc = None
        self.niDMM_ConfigureACBandwidth_cfunc = None
        self.niDMM_ConfigureFrequencyVoltageRange_cfunc = None
        self.niDMM_ConfigureMeasCompleteDest_cfunc = None
        self.niDMM_ConfigureMultiPoint_cfunc = None
        self.niDMM_ReadMultiPoint_cfunc = None
        self.niDMM_FetchMultiPoint_cfunc = None
        self.niDMM_ConfigureTriggerSlope_cfunc = None
        self.niDMM_SendSoftwareTrigger_cfunc = None
        self.niDMM_GetApertureTimeInfo_cfunc = None
        self.niDMM_GetAutoRangeValue_cfunc = None
        self.niDMM_ConfigureAutoZeroMode_cfunc = None
        self.niDMM_ConfigurePowerLineFrequency_cfunc = None
        self.niDMM_ConfigureMeasurementDigits_cfunc = None
        self.niDMM_ConfigureMeasurementAbsolute_cfunc = None
        self.niDMM_ConfigureMeasCompleteSlope_cfunc = None
        self.niDMM_ConfigureSampleTriggerSlope_cfunc = None
        self.niDMM_ReadStatus_cfunc = None
        self.niDMM_ConfigureADCCalibration_cfunc = None
        self.niDMM_ConfigureOffsetCompOhms_cfunc = None
        self.niDMM_ConfigureCurrentSource_cfunc = None
        self.niDMM_ConfigureCableCompType_cfunc = None
        self.niDMM_PerformOpenCableComp_cfunc = None
        self.niDMM_PerformShortCableComp_cfunc = None
        self.niDMM_ConfigureOpenCableCompValues_cfunc = None
        self.niDMM_ConfigureShortCableCompValues_cfunc = None
        self.niDMM_LockSession_cfunc = None
        self.niDMM_UnlockSession_cfunc = None
        self.niDMM_ConfigureWaveformAcquisition_cfunc = None
        self.niDMM_ConfigureWaveformCoupling_cfunc = None
        self.niDMM_FetchWaveform_cfunc = None
        self.niDMM_ReadWaveform_cfunc = None
        self.niDMM_GetAttributeViInt32_cfunc = None
        self.niDMM_SetAttributeViInt32_cfunc = None
        self.niDMM_GetAttributeViReal64_cfunc = None
        self.niDMM_SetAttributeViReal64_cfunc = None
        self.niDMM_GetAttributeViString_cfunc = None
        self.niDMM_SetAttributeViString_cfunc = None
        self.niDMM_GetAttributeViSession_cfunc = None
        self.niDMM_SetAttributeViSession_cfunc = None
        self.niDMM_GetAttributeViBoolean_cfunc = None
        self.niDMM_SetAttributeViBoolean_cfunc = None
        self.niDMM_GetNextCoercionRecord_cfunc = None
        self.niDMM_GetNextInterchangeWarning_cfunc = None
        self.niDMM_ResetInterchangeCheck_cfunc = None
        self.niDMM_ClearInterchangeWarnings_cfunc = None
        self.niDMM_GetChannelName_cfunc = None
        self.niDMM_GetCalCount_cfunc = None
        self.niDMM_GetLastCalTemp_cfunc = None
        self.niDMM_GetDevTemp_cfunc = None
        self.niDMM_ConfigureTransducerType_cfunc = None
        self.niDMM_ConfigureThermocouple_cfunc = None
        self.niDMM_ConfigureFixedRefJunction_cfunc = None
        self.niDMM_ConfigureRTDType_cfunc = None
        self.niDMM_ConfigureRTDCustom_cfunc = None
        self.niDMM_ConfigureThermistorType_cfunc = None
        self.niDMM_ConfigureThermistorCustom_cfunc = None
        self._cdll = ctypes.WinDLL(library_name)


    def niDMM_InitWithOptions(self, resource_name, id_query, reset_device, options_string, new_vi):
        if self.niDMM_InitWithOptions_cfunc is None:
            self.niDMM_InitWithOptions_cfunc = self._cdll.niDMM_InitWithOptions
            self.niDMM_InitWithOptions_cfunc.argtypes = [ViRsrc_ctype, ViBoolean_ctype, ViBoolean_ctype, ViString_ctype, ctypes.POINTER(ViSession_ctype)]
            self.niDMM_InitWithOptions_cfunc.restype = ViStatus_ctype
        return self.niDMM_InitWithOptions_cfunc(self, resource_name, id_query, reset_device, options_string, new_vi)

    def niDMM_close(self, vi):
        if self.niDMM_close_cfunc is None:
            self.niDMM_close_cfunc = self._cdll.niDMM_close
            self.niDMM_close_cfunc.argtypes = [ViSession_ctype]
            self.niDMM_close_cfunc.restype = ViStatus_ctype
        return self.niDMM_close_cfunc(self, vi)

    def niDMM_GetError(self, vi, error_code, buffer_size, description):
        if self.niDMM_GetError_cfunc is None:
            self.niDMM_GetError_cfunc = self._cdll.niDMM_GetError
            self.niDMM_GetError_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViStatus_ctype), ViInt32_ctype, ViChar_ctype]
            self.niDMM_GetError_cfunc.restype = ViStatus_ctype
        return self.niDMM_GetError_cfunc(self, vi, error_code, buffer_size, description)

    def niDMM_GetErrorMessage(self, vi, error_code, buffer_size, err_message):
        if self.niDMM_GetErrorMessage_cfunc is None:
            self.niDMM_GetErrorMessage_cfunc = self._cdll.niDMM_GetErrorMessage
            self.niDMM_GetErrorMessage_cfunc.argtypes = [ViSession_ctype, ViStatus_ctype, ViInt32_ctype, ViChar_ctype]
            self.niDMM_GetErrorMessage_cfunc.restype = ViStatus_ctype
        return self.niDMM_GetErrorMessage_cfunc(self, vi, error_code, buffer_size, err_message)

    def niDMM_ClearError(self, vi):
        if self.niDMM_ClearError_cfunc is None:
            self.niDMM_ClearError_cfunc = self._cdll.niDMM_ClearError
            self.niDMM_ClearError_cfunc.argtypes = [ViSession_ctype]
            self.niDMM_ClearError_cfunc.restype = ViStatus_ctype
        return self.niDMM_ClearError_cfunc(self, vi)

    def niDMM_reset(self, vi):
        if self.niDMM_reset_cfunc is None:
            self.niDMM_reset_cfunc = self._cdll.niDMM_reset
            self.niDMM_reset_cfunc.argtypes = [ViSession_ctype]
            self.niDMM_reset_cfunc.restype = ViStatus_ctype
        return self.niDMM_reset_cfunc(self, vi)

    def niDMM_self_test(self, vi, self_test_result, self_test_message):
        if self.niDMM_self_test_cfunc is None:
            self.niDMM_self_test_cfunc = self._cdll.niDMM_self_test
            self.niDMM_self_test_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViInt16_ctype), ViChar_ctype]
            self.niDMM_self_test_cfunc.restype = ViStatus_ctype
        return self.niDMM_self_test_cfunc(self, vi, self_test_result, self_test_message)

    def niDMM_SelfCal(self, vi):
        if self.niDMM_SelfCal_cfunc is None:
            self.niDMM_SelfCal_cfunc = self._cdll.niDMM_SelfCal
            self.niDMM_SelfCal_cfunc.argtypes = [ViSession_ctype]
            self.niDMM_SelfCal_cfunc.restype = ViStatus_ctype
        return self.niDMM_SelfCal_cfunc(self, vi)

    def niDMM_revision_query(self, vi, driver_rev, instr_rev):
        if self.niDMM_revision_query_cfunc is None:
            self.niDMM_revision_query_cfunc = self._cdll.niDMM_revision_query
            self.niDMM_revision_query_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViChar_ctype]
            self.niDMM_revision_query_cfunc.restype = ViStatus_ctype
        return self.niDMM_revision_query_cfunc(self, vi, driver_rev, instr_rev)

    def niDMM_InvalidateAllAttributes(self, vi):
        if self.niDMM_InvalidateAllAttributes_cfunc is None:
            self.niDMM_InvalidateAllAttributes_cfunc = self._cdll.niDMM_InvalidateAllAttributes
            self.niDMM_InvalidateAllAttributes_cfunc.argtypes = [ViSession_ctype]
            self.niDMM_InvalidateAllAttributes_cfunc.restype = ViStatus_ctype
        return self.niDMM_InvalidateAllAttributes_cfunc(self, vi)

    def niDMM_ResetWithDefaults(self, vi):
        if self.niDMM_ResetWithDefaults_cfunc is None:
            self.niDMM_ResetWithDefaults_cfunc = self._cdll.niDMM_ResetWithDefaults
            self.niDMM_ResetWithDefaults_cfunc.argtypes = [ViSession_ctype]
            self.niDMM_ResetWithDefaults_cfunc.restype = ViStatus_ctype
        return self.niDMM_ResetWithDefaults_cfunc(self, vi)

    def niDMM_Disable(self, vi):
        if self.niDMM_Disable_cfunc is None:
            self.niDMM_Disable_cfunc = self._cdll.niDMM_Disable
            self.niDMM_Disable_cfunc.argtypes = [ViSession_ctype]
            self.niDMM_Disable_cfunc.restype = ViStatus_ctype
        return self.niDMM_Disable_cfunc(self, vi)

    def niDMM_GetMeasurementPeriod(self, vi, period):
        if self.niDMM_GetMeasurementPeriod_cfunc is None:
            self.niDMM_GetMeasurementPeriod_cfunc = self._cdll.niDMM_GetMeasurementPeriod
            self.niDMM_GetMeasurementPeriod_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViReal64_ctype)]
            self.niDMM_GetMeasurementPeriod_cfunc.restype = ViStatus_ctype
        return self.niDMM_GetMeasurementPeriod_cfunc(self, vi, period)

    def niDMM_ConfigureTrigger(self, vi, trig_source, trigger_delay):
        if self.niDMM_ConfigureTrigger_cfunc is None:
            self.niDMM_ConfigureTrigger_cfunc = self._cdll.niDMM_ConfigureTrigger
            self.niDMM_ConfigureTrigger_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViReal64_ctype]
            self.niDMM_ConfigureTrigger_cfunc.restype = ViStatus_ctype
        return self.niDMM_ConfigureTrigger_cfunc(self, vi, trig_source, trigger_delay)

    def niDMM_Read(self, vi, max_time, reading):
        if self.niDMM_Read_cfunc is None:
            self.niDMM_Read_cfunc = self._cdll.niDMM_Read
            self.niDMM_Read_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ctypes.POINTER(ViReal64_ctype)]
            self.niDMM_Read_cfunc.restype = ViStatus_ctype
        return self.niDMM_Read_cfunc(self, vi, max_time, reading)

    def niDMM_Fetch(self, vi, max_time, reading):
        if self.niDMM_Fetch_cfunc is None:
            self.niDMM_Fetch_cfunc = self._cdll.niDMM_Fetch
            self.niDMM_Fetch_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ctypes.POINTER(ViReal64_ctype)]
            self.niDMM_Fetch_cfunc.restype = ViStatus_ctype
        return self.niDMM_Fetch_cfunc(self, vi, max_time, reading)

    def niDMM_Abort(self, vi):
        if self.niDMM_Abort_cfunc is None:
            self.niDMM_Abort_cfunc = self._cdll.niDMM_Abort
            self.niDMM_Abort_cfunc.argtypes = [ViSession_ctype]
            self.niDMM_Abort_cfunc.restype = ViStatus_ctype
        return self.niDMM_Abort_cfunc(self, vi)

    def niDMM_Initiate(self, vi):
        if self.niDMM_Initiate_cfunc is None:
            self.niDMM_Initiate_cfunc = self._cdll.niDMM_Initiate
            self.niDMM_Initiate_cfunc.argtypes = [ViSession_ctype]
            self.niDMM_Initiate_cfunc.restype = ViStatus_ctype
        return self.niDMM_Initiate_cfunc(self, vi)

    def niDMM_IsOverRange(self, vi, measurement_value, is_over_range):
        if self.niDMM_IsOverRange_cfunc is None:
            self.niDMM_IsOverRange_cfunc = self._cdll.niDMM_IsOverRange
            self.niDMM_IsOverRange_cfunc.argtypes = [ViSession_ctype, ViReal64_ctype, ctypes.POINTER(ViBoolean_ctype)]
            self.niDMM_IsOverRange_cfunc.restype = ViStatus_ctype
        return self.niDMM_IsOverRange_cfunc(self, vi, measurement_value, is_over_range)

    def niDMM_IsUnderRange(self, vi, measurement_value, is_under_range):
        if self.niDMM_IsUnderRange_cfunc is None:
            self.niDMM_IsUnderRange_cfunc = self._cdll.niDMM_IsUnderRange
            self.niDMM_IsUnderRange_cfunc.argtypes = [ViSession_ctype, ViReal64_ctype, ctypes.POINTER(ViBoolean_ctype)]
            self.niDMM_IsUnderRange_cfunc.restype = ViStatus_ctype
        return self.niDMM_IsUnderRange_cfunc(self, vi, measurement_value, is_under_range)

    def niDMM_ConfigureACBandwidth(self, vi, min_freq, max_freq):
        if self.niDMM_ConfigureACBandwidth_cfunc is None:
            self.niDMM_ConfigureACBandwidth_cfunc = self._cdll.niDMM_ConfigureACBandwidth
            self.niDMM_ConfigureACBandwidth_cfunc.argtypes = [ViSession_ctype, ViReal64_ctype, ViReal64_ctype]
            self.niDMM_ConfigureACBandwidth_cfunc.restype = ViStatus_ctype
        return self.niDMM_ConfigureACBandwidth_cfunc(self, vi, min_freq, max_freq)

    def niDMM_ConfigureFrequencyVoltageRange(self, vi, frequency_voltage_range):
        if self.niDMM_ConfigureFrequencyVoltageRange_cfunc is None:
            self.niDMM_ConfigureFrequencyVoltageRange_cfunc = self._cdll.niDMM_ConfigureFrequencyVoltageRange
            self.niDMM_ConfigureFrequencyVoltageRange_cfunc.argtypes = [ViSession_ctype, ViReal64_ctype]
            self.niDMM_ConfigureFrequencyVoltageRange_cfunc.restype = ViStatus_ctype
        return self.niDMM_ConfigureFrequencyVoltageRange_cfunc(self, vi, frequency_voltage_range)

    def niDMM_ConfigureMeasCompleteDest(self, vi, destination):
        if self.niDMM_ConfigureMeasCompleteDest_cfunc is None:
            self.niDMM_ConfigureMeasCompleteDest_cfunc = self._cdll.niDMM_ConfigureMeasCompleteDest
            self.niDMM_ConfigureMeasCompleteDest_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype]
            self.niDMM_ConfigureMeasCompleteDest_cfunc.restype = ViStatus_ctype
        return self.niDMM_ConfigureMeasCompleteDest_cfunc(self, vi, destination)

    def niDMM_ConfigureMultiPoint(self, vi, trigger_count, sample_count, sample_trigger, sample_interval):
        if self.niDMM_ConfigureMultiPoint_cfunc is None:
            self.niDMM_ConfigureMultiPoint_cfunc = self._cdll.niDMM_ConfigureMultiPoint
            self.niDMM_ConfigureMultiPoint_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViInt32_ctype, ViInt32_ctype, ViReal64_ctype]
            self.niDMM_ConfigureMultiPoint_cfunc.restype = ViStatus_ctype
        return self.niDMM_ConfigureMultiPoint_cfunc(self, vi, trigger_count, sample_count, sample_trigger, sample_interval)

    def niDMM_ReadMultiPoint(self, vi, max_time, array_size, reading_array, actual_pts):
        if self.niDMM_ReadMultiPoint_cfunc is None:
            self.niDMM_ReadMultiPoint_cfunc = self._cdll.niDMM_ReadMultiPoint
            self.niDMM_ReadMultiPoint_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViInt32_ctype, ViReal64_ctype, ctypes.POINTER(ViInt32_ctype)]
            self.niDMM_ReadMultiPoint_cfunc.restype = ViStatus_ctype
        return self.niDMM_ReadMultiPoint_cfunc(self, vi, max_time, array_size, reading_array, actual_pts)

    def niDMM_FetchMultiPoint(self, vi, max_time, array_size, reading_array, actual_pts):
        if self.niDMM_FetchMultiPoint_cfunc is None:
            self.niDMM_FetchMultiPoint_cfunc = self._cdll.niDMM_FetchMultiPoint
            self.niDMM_FetchMultiPoint_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViInt32_ctype, ViReal64_ctype, ctypes.POINTER(ViInt32_ctype)]
            self.niDMM_FetchMultiPoint_cfunc.restype = ViStatus_ctype
        return self.niDMM_FetchMultiPoint_cfunc(self, vi, max_time, array_size, reading_array, actual_pts)

    def niDMM_ConfigureTriggerSlope(self, vi, polarity):
        if self.niDMM_ConfigureTriggerSlope_cfunc is None:
            self.niDMM_ConfigureTriggerSlope_cfunc = self._cdll.niDMM_ConfigureTriggerSlope
            self.niDMM_ConfigureTriggerSlope_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype]
            self.niDMM_ConfigureTriggerSlope_cfunc.restype = ViStatus_ctype
        return self.niDMM_ConfigureTriggerSlope_cfunc(self, vi, polarity)

    def niDMM_SendSoftwareTrigger(self, vi):
        if self.niDMM_SendSoftwareTrigger_cfunc is None:
            self.niDMM_SendSoftwareTrigger_cfunc = self._cdll.niDMM_SendSoftwareTrigger
            self.niDMM_SendSoftwareTrigger_cfunc.argtypes = [ViSession_ctype]
            self.niDMM_SendSoftwareTrigger_cfunc.restype = ViStatus_ctype
        return self.niDMM_SendSoftwareTrigger_cfunc(self, vi)

    def niDMM_GetApertureTimeInfo(self, vi, aperture_time, aperture_time_units):
        if self.niDMM_GetApertureTimeInfo_cfunc is None:
            self.niDMM_GetApertureTimeInfo_cfunc = self._cdll.niDMM_GetApertureTimeInfo
            self.niDMM_GetApertureTimeInfo_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViReal64_ctype), ctypes.POINTER(ViInt32_ctype)]
            self.niDMM_GetApertureTimeInfo_cfunc.restype = ViStatus_ctype
        return self.niDMM_GetApertureTimeInfo_cfunc(self, vi, aperture_time, aperture_time_units)

    def niDMM_GetAutoRangeValue(self, vi, auto_range_value):
        if self.niDMM_GetAutoRangeValue_cfunc is None:
            self.niDMM_GetAutoRangeValue_cfunc = self._cdll.niDMM_GetAutoRangeValue
            self.niDMM_GetAutoRangeValue_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViReal64_ctype)]
            self.niDMM_GetAutoRangeValue_cfunc.restype = ViStatus_ctype
        return self.niDMM_GetAutoRangeValue_cfunc(self, vi, auto_range_value)

    def niDMM_ConfigureAutoZeroMode(self, vi, auto_zero_mode):
        if self.niDMM_ConfigureAutoZeroMode_cfunc is None:
            self.niDMM_ConfigureAutoZeroMode_cfunc = self._cdll.niDMM_ConfigureAutoZeroMode
            self.niDMM_ConfigureAutoZeroMode_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype]
            self.niDMM_ConfigureAutoZeroMode_cfunc.restype = ViStatus_ctype
        return self.niDMM_ConfigureAutoZeroMode_cfunc(self, vi, auto_zero_mode)

    def niDMM_ConfigurePowerLineFrequency(self, vi, frequency):
        if self.niDMM_ConfigurePowerLineFrequency_cfunc is None:
            self.niDMM_ConfigurePowerLineFrequency_cfunc = self._cdll.niDMM_ConfigurePowerLineFrequency
            self.niDMM_ConfigurePowerLineFrequency_cfunc.argtypes = [ViSession_ctype, ViReal64_ctype]
            self.niDMM_ConfigurePowerLineFrequency_cfunc.restype = ViStatus_ctype
        return self.niDMM_ConfigurePowerLineFrequency_cfunc(self, vi, frequency)

    def niDMM_ConfigureMeasurementDigits(self, vi, meas_function, range, resolution_digits):
        if self.niDMM_ConfigureMeasurementDigits_cfunc is None:
            self.niDMM_ConfigureMeasurementDigits_cfunc = self._cdll.niDMM_ConfigureMeasurementDigits
            self.niDMM_ConfigureMeasurementDigits_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViReal64_ctype, ViReal64_ctype]
            self.niDMM_ConfigureMeasurementDigits_cfunc.restype = ViStatus_ctype
        return self.niDMM_ConfigureMeasurementDigits_cfunc(self, vi, meas_function, range, resolution_digits)

    def niDMM_ConfigureMeasurementAbsolute(self, vi, meas_function, range, resolution_absolute):
        if self.niDMM_ConfigureMeasurementAbsolute_cfunc is None:
            self.niDMM_ConfigureMeasurementAbsolute_cfunc = self._cdll.niDMM_ConfigureMeasurementAbsolute
            self.niDMM_ConfigureMeasurementAbsolute_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViReal64_ctype, ViReal64_ctype]
            self.niDMM_ConfigureMeasurementAbsolute_cfunc.restype = ViStatus_ctype
        return self.niDMM_ConfigureMeasurementAbsolute_cfunc(self, vi, meas_function, range, resolution_absolute)

    def niDMM_ConfigureMeasCompleteSlope(self, vi, polarity):
        if self.niDMM_ConfigureMeasCompleteSlope_cfunc is None:
            self.niDMM_ConfigureMeasCompleteSlope_cfunc = self._cdll.niDMM_ConfigureMeasCompleteSlope
            self.niDMM_ConfigureMeasCompleteSlope_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype]
            self.niDMM_ConfigureMeasCompleteSlope_cfunc.restype = ViStatus_ctype
        return self.niDMM_ConfigureMeasCompleteSlope_cfunc(self, vi, polarity)

    def niDMM_ConfigureSampleTriggerSlope(self, vi, polarity):
        if self.niDMM_ConfigureSampleTriggerSlope_cfunc is None:
            self.niDMM_ConfigureSampleTriggerSlope_cfunc = self._cdll.niDMM_ConfigureSampleTriggerSlope
            self.niDMM_ConfigureSampleTriggerSlope_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype]
            self.niDMM_ConfigureSampleTriggerSlope_cfunc.restype = ViStatus_ctype
        return self.niDMM_ConfigureSampleTriggerSlope_cfunc(self, vi, polarity)

    def niDMM_ReadStatus(self, vi, acq_backlog, acq_done):
        if self.niDMM_ReadStatus_cfunc is None:
            self.niDMM_ReadStatus_cfunc = self._cdll.niDMM_ReadStatus
            self.niDMM_ReadStatus_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViInt32_ctype), ctypes.POINTER(ViInt16_ctype)]
            self.niDMM_ReadStatus_cfunc.restype = ViStatus_ctype
        return self.niDMM_ReadStatus_cfunc(self, vi, acq_backlog, acq_done)

    def niDMM_ConfigureADCCalibration(self, vi, adc_gain_comp):
        if self.niDMM_ConfigureADCCalibration_cfunc is None:
            self.niDMM_ConfigureADCCalibration_cfunc = self._cdll.niDMM_ConfigureADCCalibration
            self.niDMM_ConfigureADCCalibration_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype]
            self.niDMM_ConfigureADCCalibration_cfunc.restype = ViStatus_ctype
        return self.niDMM_ConfigureADCCalibration_cfunc(self, vi, adc_gain_comp)

    def niDMM_ConfigureOffsetCompOhms(self, vi, offset_comp_ohms):
        if self.niDMM_ConfigureOffsetCompOhms_cfunc is None:
            self.niDMM_ConfigureOffsetCompOhms_cfunc = self._cdll.niDMM_ConfigureOffsetCompOhms
            self.niDMM_ConfigureOffsetCompOhms_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype]
            self.niDMM_ConfigureOffsetCompOhms_cfunc.restype = ViStatus_ctype
        return self.niDMM_ConfigureOffsetCompOhms_cfunc(self, vi, offset_comp_ohms)

    def niDMM_ConfigureCurrentSource(self, vi, diode_current_src):
        if self.niDMM_ConfigureCurrentSource_cfunc is None:
            self.niDMM_ConfigureCurrentSource_cfunc = self._cdll.niDMM_ConfigureCurrentSource
            self.niDMM_ConfigureCurrentSource_cfunc.argtypes = [ViSession_ctype, ViReal64_ctype]
            self.niDMM_ConfigureCurrentSource_cfunc.restype = ViStatus_ctype
        return self.niDMM_ConfigureCurrentSource_cfunc(self, vi, diode_current_src)

    def niDMM_ConfigureCableCompType(self, vi, type_of_compensation):
        if self.niDMM_ConfigureCableCompType_cfunc is None:
            self.niDMM_ConfigureCableCompType_cfunc = self._cdll.niDMM_ConfigureCableCompType
            self.niDMM_ConfigureCableCompType_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype]
            self.niDMM_ConfigureCableCompType_cfunc.restype = ViStatus_ctype
        return self.niDMM_ConfigureCableCompType_cfunc(self, vi, type_of_compensation)

    def niDMM_PerformOpenCableComp(self, vi, conductance, susceptance):
        if self.niDMM_PerformOpenCableComp_cfunc is None:
            self.niDMM_PerformOpenCableComp_cfunc = self._cdll.niDMM_PerformOpenCableComp
            self.niDMM_PerformOpenCableComp_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViReal64_ctype), ctypes.POINTER(ViReal64_ctype)]
            self.niDMM_PerformOpenCableComp_cfunc.restype = ViStatus_ctype
        return self.niDMM_PerformOpenCableComp_cfunc(self, vi, conductance, susceptance)

    def niDMM_PerformShortCableComp(self, vi, resistance, reactance):
        if self.niDMM_PerformShortCableComp_cfunc is None:
            self.niDMM_PerformShortCableComp_cfunc = self._cdll.niDMM_PerformShortCableComp
            self.niDMM_PerformShortCableComp_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViReal64_ctype), ctypes.POINTER(ViReal64_ctype)]
            self.niDMM_PerformShortCableComp_cfunc.restype = ViStatus_ctype
        return self.niDMM_PerformShortCableComp_cfunc(self, vi, resistance, reactance)

    def niDMM_ConfigureOpenCableCompValues(self, vi, conductance, susceptance):
        if self.niDMM_ConfigureOpenCableCompValues_cfunc is None:
            self.niDMM_ConfigureOpenCableCompValues_cfunc = self._cdll.niDMM_ConfigureOpenCableCompValues
            self.niDMM_ConfigureOpenCableCompValues_cfunc.argtypes = [ViSession_ctype, ViReal64_ctype, ViReal64_ctype]
            self.niDMM_ConfigureOpenCableCompValues_cfunc.restype = ViStatus_ctype
        return self.niDMM_ConfigureOpenCableCompValues_cfunc(self, vi, conductance, susceptance)

    def niDMM_ConfigureShortCableCompValues(self, vi, resistance, reactance):
        if self.niDMM_ConfigureShortCableCompValues_cfunc is None:
            self.niDMM_ConfigureShortCableCompValues_cfunc = self._cdll.niDMM_ConfigureShortCableCompValues
            self.niDMM_ConfigureShortCableCompValues_cfunc.argtypes = [ViSession_ctype, ViReal64_ctype, ViReal64_ctype]
            self.niDMM_ConfigureShortCableCompValues_cfunc.restype = ViStatus_ctype
        return self.niDMM_ConfigureShortCableCompValues_cfunc(self, vi, resistance, reactance)

    def niDMM_LockSession(self, vi, caller_has_lock):
        if self.niDMM_LockSession_cfunc is None:
            self.niDMM_LockSession_cfunc = self._cdll.niDMM_LockSession
            self.niDMM_LockSession_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViBoolean_ctype)]
            self.niDMM_LockSession_cfunc.restype = ViStatus_ctype
        return self.niDMM_LockSession_cfunc(self, vi, caller_has_lock)

    def niDMM_UnlockSession(self, vi, caller_has_lock):
        if self.niDMM_UnlockSession_cfunc is None:
            self.niDMM_UnlockSession_cfunc = self._cdll.niDMM_UnlockSession
            self.niDMM_UnlockSession_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViBoolean_ctype)]
            self.niDMM_UnlockSession_cfunc.restype = ViStatus_ctype
        return self.niDMM_UnlockSession_cfunc(self, vi, caller_has_lock)

    def niDMM_ConfigureWaveformAcquisition(self, vi, function, range, rate, waveform_points):
        if self.niDMM_ConfigureWaveformAcquisition_cfunc is None:
            self.niDMM_ConfigureWaveformAcquisition_cfunc = self._cdll.niDMM_ConfigureWaveformAcquisition
            self.niDMM_ConfigureWaveformAcquisition_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViReal64_ctype, ViReal64_ctype, ViInt32_ctype]
            self.niDMM_ConfigureWaveformAcquisition_cfunc.restype = ViStatus_ctype
        return self.niDMM_ConfigureWaveformAcquisition_cfunc(self, vi, function, range, rate, waveform_points)

    def niDMM_ConfigureWaveformCoupling(self, vi, coupling):
        if self.niDMM_ConfigureWaveformCoupling_cfunc is None:
            self.niDMM_ConfigureWaveformCoupling_cfunc = self._cdll.niDMM_ConfigureWaveformCoupling
            self.niDMM_ConfigureWaveformCoupling_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype]
            self.niDMM_ConfigureWaveformCoupling_cfunc.restype = ViStatus_ctype
        return self.niDMM_ConfigureWaveformCoupling_cfunc(self, vi, coupling)

    def niDMM_FetchWaveform(self, vi, max_time, array_size, waveform_array, actual_points):
        if self.niDMM_FetchWaveform_cfunc is None:
            self.niDMM_FetchWaveform_cfunc = self._cdll.niDMM_FetchWaveform
            self.niDMM_FetchWaveform_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViInt32_ctype, ViReal64_ctype, ctypes.POINTER(ViInt32_ctype)]
            self.niDMM_FetchWaveform_cfunc.restype = ViStatus_ctype
        return self.niDMM_FetchWaveform_cfunc(self, vi, max_time, array_size, waveform_array, actual_points)

    def niDMM_ReadWaveform(self, vi, max_time, array_size, waveform_array, actual_points):
        if self.niDMM_ReadWaveform_cfunc is None:
            self.niDMM_ReadWaveform_cfunc = self._cdll.niDMM_ReadWaveform
            self.niDMM_ReadWaveform_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViInt32_ctype, ViReal64_ctype, ctypes.POINTER(ViInt32_ctype)]
            self.niDMM_ReadWaveform_cfunc.restype = ViStatus_ctype
        return self.niDMM_ReadWaveform_cfunc(self, vi, max_time, array_size, waveform_array, actual_points)

    def niDMM_GetAttributeViInt32(self, vi, channel_name, attribute_id, value):
        if self.niDMM_GetAttributeViInt32_cfunc is None:
            self.niDMM_GetAttributeViInt32_cfunc = self._cdll.niDMM_GetAttributeViInt32
            self.niDMM_GetAttributeViInt32_cfunc.argtypes = [ViSession_ctype, ViConstString_ctype, ViAttr_ctype, ctypes.POINTER(ViInt32_ctype)]
            self.niDMM_GetAttributeViInt32_cfunc.restype = ViStatus_ctype
        return self.niDMM_GetAttributeViInt32_cfunc(self, vi, channel_name, attribute_id, value)

    def niDMM_SetAttributeViInt32(self, vi, channel_name, attribute_id, value):
        if self.niDMM_SetAttributeViInt32_cfunc is None:
            self.niDMM_SetAttributeViInt32_cfunc = self._cdll.niDMM_SetAttributeViInt32
            self.niDMM_SetAttributeViInt32_cfunc.argtypes = [ViSession_ctype, ViConstString_ctype, ViAttr_ctype, ViInt32_ctype]
            self.niDMM_SetAttributeViInt32_cfunc.restype = ViStatus_ctype
        return self.niDMM_SetAttributeViInt32_cfunc(self, vi, channel_name, attribute_id, value)

    def niDMM_GetAttributeViReal64(self, vi, channel_name, attribute_id, value):
        if self.niDMM_GetAttributeViReal64_cfunc is None:
            self.niDMM_GetAttributeViReal64_cfunc = self._cdll.niDMM_GetAttributeViReal64
            self.niDMM_GetAttributeViReal64_cfunc.argtypes = [ViSession_ctype, ViConstString_ctype, ViAttr_ctype, ctypes.POINTER(ViReal64_ctype)]
            self.niDMM_GetAttributeViReal64_cfunc.restype = ViStatus_ctype
        return self.niDMM_GetAttributeViReal64_cfunc(self, vi, channel_name, attribute_id, value)

    def niDMM_SetAttributeViReal64(self, vi, channel_name, attribute_id, value):
        if self.niDMM_SetAttributeViReal64_cfunc is None:
            self.niDMM_SetAttributeViReal64_cfunc = self._cdll.niDMM_SetAttributeViReal64
            self.niDMM_SetAttributeViReal64_cfunc.argtypes = [ViSession_ctype, ViConstString_ctype, ViAttr_ctype, ViReal64_ctype]
            self.niDMM_SetAttributeViReal64_cfunc.restype = ViStatus_ctype
        return self.niDMM_SetAttributeViReal64_cfunc(self, vi, channel_name, attribute_id, value)

    def niDMM_GetAttributeViString(self, vi, channel_name, attribute_id, buf_size, value):
        if self.niDMM_GetAttributeViString_cfunc is None:
            self.niDMM_GetAttributeViString_cfunc = self._cdll.niDMM_GetAttributeViString
            self.niDMM_GetAttributeViString_cfunc.argtypes = [ViSession_ctype, ViConstString_ctype, ViAttr_ctype, ViInt32_ctype, ViChar_ctype]
            self.niDMM_GetAttributeViString_cfunc.restype = ViStatus_ctype
        return self.niDMM_GetAttributeViString_cfunc(self, vi, channel_name, attribute_id, buf_size, value)

    def niDMM_SetAttributeViString(self, vi, channel_name, attribute_id, value):
        if self.niDMM_SetAttributeViString_cfunc is None:
            self.niDMM_SetAttributeViString_cfunc = self._cdll.niDMM_SetAttributeViString
            self.niDMM_SetAttributeViString_cfunc.argtypes = [ViSession_ctype, ViConstString_ctype, ViAttr_ctype, ViChar_ctype]
            self.niDMM_SetAttributeViString_cfunc.restype = ViStatus_ctype
        return self.niDMM_SetAttributeViString_cfunc(self, vi, channel_name, attribute_id, value)

    def niDMM_GetAttributeViSession(self, vi, channel_name, attribute_id, value):
        if self.niDMM_GetAttributeViSession_cfunc is None:
            self.niDMM_GetAttributeViSession_cfunc = self._cdll.niDMM_GetAttributeViSession
            self.niDMM_GetAttributeViSession_cfunc.argtypes = [ViSession_ctype, ViConstString_ctype, ViAttr_ctype, ctypes.POINTER(ViSession_ctype)]
            self.niDMM_GetAttributeViSession_cfunc.restype = ViStatus_ctype
        return self.niDMM_GetAttributeViSession_cfunc(self, vi, channel_name, attribute_id, value)

    def niDMM_SetAttributeViSession(self, vi, channel_name, attribute_id, value):
        if self.niDMM_SetAttributeViSession_cfunc is None:
            self.niDMM_SetAttributeViSession_cfunc = self._cdll.niDMM_SetAttributeViSession
            self.niDMM_SetAttributeViSession_cfunc.argtypes = [ViSession_ctype, ViConstString_ctype, ViAttr_ctype, ViSession_ctype]
            self.niDMM_SetAttributeViSession_cfunc.restype = ViStatus_ctype
        return self.niDMM_SetAttributeViSession_cfunc(self, vi, channel_name, attribute_id, value)

    def niDMM_GetAttributeViBoolean(self, vi, channel_name, attribute_id, value):
        if self.niDMM_GetAttributeViBoolean_cfunc is None:
            self.niDMM_GetAttributeViBoolean_cfunc = self._cdll.niDMM_GetAttributeViBoolean
            self.niDMM_GetAttributeViBoolean_cfunc.argtypes = [ViSession_ctype, ViConstString_ctype, ViAttr_ctype, ctypes.POINTER(ViBoolean_ctype)]
            self.niDMM_GetAttributeViBoolean_cfunc.restype = ViStatus_ctype
        return self.niDMM_GetAttributeViBoolean_cfunc(self, vi, channel_name, attribute_id, value)

    def niDMM_SetAttributeViBoolean(self, vi, channel_name, attribute_id, value):
        if self.niDMM_SetAttributeViBoolean_cfunc is None:
            self.niDMM_SetAttributeViBoolean_cfunc = self._cdll.niDMM_SetAttributeViBoolean
            self.niDMM_SetAttributeViBoolean_cfunc.argtypes = [ViSession_ctype, ViConstString_ctype, ViAttr_ctype, ViBoolean_ctype]
            self.niDMM_SetAttributeViBoolean_cfunc.restype = ViStatus_ctype
        return self.niDMM_SetAttributeViBoolean_cfunc(self, vi, channel_name, attribute_id, value)

    def niDMM_GetNextCoercionRecord(self, vi, buffer_size, record):
        if self.niDMM_GetNextCoercionRecord_cfunc is None:
            self.niDMM_GetNextCoercionRecord_cfunc = self._cdll.niDMM_GetNextCoercionRecord
            self.niDMM_GetNextCoercionRecord_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViChar_ctype]
            self.niDMM_GetNextCoercionRecord_cfunc.restype = ViStatus_ctype
        return self.niDMM_GetNextCoercionRecord_cfunc(self, vi, buffer_size, record)

    def niDMM_GetNextInterchangeWarning(self, vi, buffer_size, warn_string):
        if self.niDMM_GetNextInterchangeWarning_cfunc is None:
            self.niDMM_GetNextInterchangeWarning_cfunc = self._cdll.niDMM_GetNextInterchangeWarning
            self.niDMM_GetNextInterchangeWarning_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViChar_ctype]
            self.niDMM_GetNextInterchangeWarning_cfunc.restype = ViStatus_ctype
        return self.niDMM_GetNextInterchangeWarning_cfunc(self, vi, buffer_size, warn_string)

    def niDMM_ResetInterchangeCheck(self, vi):
        if self.niDMM_ResetInterchangeCheck_cfunc is None:
            self.niDMM_ResetInterchangeCheck_cfunc = self._cdll.niDMM_ResetInterchangeCheck
            self.niDMM_ResetInterchangeCheck_cfunc.argtypes = [ViSession_ctype]
            self.niDMM_ResetInterchangeCheck_cfunc.restype = ViStatus_ctype
        return self.niDMM_ResetInterchangeCheck_cfunc(self, vi)

    def niDMM_ClearInterchangeWarnings(self, vi):
        if self.niDMM_ClearInterchangeWarnings_cfunc is None:
            self.niDMM_ClearInterchangeWarnings_cfunc = self._cdll.niDMM_ClearInterchangeWarnings
            self.niDMM_ClearInterchangeWarnings_cfunc.argtypes = [ViSession_ctype]
            self.niDMM_ClearInterchangeWarnings_cfunc.restype = ViStatus_ctype
        return self.niDMM_ClearInterchangeWarnings_cfunc(self, vi)

    def niDMM_GetChannelName(self, vi, index, buffer_size, name):
        if self.niDMM_GetChannelName_cfunc is None:
            self.niDMM_GetChannelName_cfunc = self._cdll.niDMM_GetChannelName
            self.niDMM_GetChannelName_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViInt32_ctype, ViChar_ctype]
            self.niDMM_GetChannelName_cfunc.restype = ViStatus_ctype
        return self.niDMM_GetChannelName_cfunc(self, vi, index, buffer_size, name)

    def niDMM_GetCalCount(self, vi, cal_type, count):
        if self.niDMM_GetCalCount_cfunc is None:
            self.niDMM_GetCalCount_cfunc = self._cdll.niDMM_GetCalCount
            self.niDMM_GetCalCount_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ctypes.POINTER(ViInt32_ctype)]
            self.niDMM_GetCalCount_cfunc.restype = ViStatus_ctype
        return self.niDMM_GetCalCount_cfunc(self, vi, cal_type, count)

    def niDMM_GetLastCalTemp(self, vi, cal_type, temperature):
        if self.niDMM_GetLastCalTemp_cfunc is None:
            self.niDMM_GetLastCalTemp_cfunc = self._cdll.niDMM_GetLastCalTemp
            self.niDMM_GetLastCalTemp_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ctypes.POINTER(ViReal64_ctype)]
            self.niDMM_GetLastCalTemp_cfunc.restype = ViStatus_ctype
        return self.niDMM_GetLastCalTemp_cfunc(self, vi, cal_type, temperature)

    def niDMM_GetDevTemp(self, vi, reserved, temperature):
        if self.niDMM_GetDevTemp_cfunc is None:
            self.niDMM_GetDevTemp_cfunc = self._cdll.niDMM_GetDevTemp
            self.niDMM_GetDevTemp_cfunc.argtypes = [ViSession_ctype, ViString_ctype, ctypes.POINTER(ViReal64_ctype)]
            self.niDMM_GetDevTemp_cfunc.restype = ViStatus_ctype
        return self.niDMM_GetDevTemp_cfunc(self, vi, reserved, temperature)

    def niDMM_ConfigureTransducerType(self, vi, transducer_type):
        if self.niDMM_ConfigureTransducerType_cfunc is None:
            self.niDMM_ConfigureTransducerType_cfunc = self._cdll.niDMM_ConfigureTransducerType
            self.niDMM_ConfigureTransducerType_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype]
            self.niDMM_ConfigureTransducerType_cfunc.restype = ViStatus_ctype
        return self.niDMM_ConfigureTransducerType_cfunc(self, vi, transducer_type)

    def niDMM_ConfigureThermocouple(self, vi, thermocouple_type, ref_junction_type):
        if self.niDMM_ConfigureThermocouple_cfunc is None:
            self.niDMM_ConfigureThermocouple_cfunc = self._cdll.niDMM_ConfigureThermocouple
            self.niDMM_ConfigureThermocouple_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViInt32_ctype]
            self.niDMM_ConfigureThermocouple_cfunc.restype = ViStatus_ctype
        return self.niDMM_ConfigureThermocouple_cfunc(self, vi, thermocouple_type, ref_junction_type)

    def niDMM_ConfigureFixedRefJunction(self, vi, fixed_ref_junction):
        if self.niDMM_ConfigureFixedRefJunction_cfunc is None:
            self.niDMM_ConfigureFixedRefJunction_cfunc = self._cdll.niDMM_ConfigureFixedRefJunction
            self.niDMM_ConfigureFixedRefJunction_cfunc.argtypes = [ViSession_ctype, ViReal64_ctype]
            self.niDMM_ConfigureFixedRefJunction_cfunc.restype = ViStatus_ctype
        return self.niDMM_ConfigureFixedRefJunction_cfunc(self, vi, fixed_ref_junction)

    def niDMM_ConfigureRTDType(self, vi, rtd_type, resistance):
        if self.niDMM_ConfigureRTDType_cfunc is None:
            self.niDMM_ConfigureRTDType_cfunc = self._cdll.niDMM_ConfigureRTDType
            self.niDMM_ConfigureRTDType_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViReal64_ctype]
            self.niDMM_ConfigureRTDType_cfunc.restype = ViStatus_ctype
        return self.niDMM_ConfigureRTDType_cfunc(self, vi, rtd_type, resistance)

    def niDMM_ConfigureRTDCustom(self, vi, a, b, c):
        if self.niDMM_ConfigureRTDCustom_cfunc is None:
            self.niDMM_ConfigureRTDCustom_cfunc = self._cdll.niDMM_ConfigureRTDCustom
            self.niDMM_ConfigureRTDCustom_cfunc.argtypes = [ViSession_ctype, ViReal64_ctype, ViReal64_ctype, ViReal64_ctype]
            self.niDMM_ConfigureRTDCustom_cfunc.restype = ViStatus_ctype
        return self.niDMM_ConfigureRTDCustom_cfunc(self, vi, a, b, c)

    def niDMM_ConfigureThermistorType(self, vi, thermistor_type):
        if self.niDMM_ConfigureThermistorType_cfunc is None:
            self.niDMM_ConfigureThermistorType_cfunc = self._cdll.niDMM_ConfigureThermistorType
            self.niDMM_ConfigureThermistorType_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype]
            self.niDMM_ConfigureThermistorType_cfunc.restype = ViStatus_ctype
        return self.niDMM_ConfigureThermistorType_cfunc(self, vi, thermistor_type)

    def niDMM_ConfigureThermistorCustom(self, vi, a, b, c):
        if self.niDMM_ConfigureThermistorCustom_cfunc is None:
            self.niDMM_ConfigureThermistorCustom_cfunc = self._cdll.niDMM_ConfigureThermistorCustom
            self.niDMM_ConfigureThermistorCustom_cfunc.argtypes = [ViSession_ctype, ViReal64_ctype, ViReal64_ctype, ViReal64_ctype]
            self.niDMM_ConfigureThermistorCustom_cfunc.restype = ViStatus_ctype
        return self.niDMM_ConfigureThermistorCustom_cfunc(self, vi, a, b, c)


