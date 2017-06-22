# This file was generated


import ctypes
import platform

class nidmm_ctypes_library:
    # We cache the cfunc object from the ctypes.CDLL object
    niDMM_init_cfunc = None
    niDMM_InitWithOptions_cfunc = None
    niDMM_close_cfunc = None
    niDMM_GetError_cfunc = None
    niDMM_GetErrorMessage_cfunc = None
    niDMM_ClearError_cfunc = None
    niDMM_reset_cfunc = None
    niDMM_self_test_cfunc = None
    niDMM_SelfCal_cfunc = None
    niDMM_revision_query_cfunc = None
    niDMM_InvalidateAllAttributes_cfunc = None
    niDMM_ResetWithDefaults_cfunc = None
    niDMM_Disable_cfunc = None
    niDMM_GetMeasurementPeriod_cfunc = None
    niDMM_ConfigureTrigger_cfunc = None
    niDMM_Read_cfunc = None
    niDMM_Fetch_cfunc = None
    niDMM_Abort_cfunc = None
    niDMM_Initiate_cfunc = None
    niDMM_IsOverRange_cfunc = None
    niDMM_IsUnderRange_cfunc = None
    niDMM_ConfigureACBandwidth_cfunc = None
    niDMM_ConfigureFrequencyVoltageRange_cfunc = None
    niDMM_ConfigureMeasCompleteDest_cfunc = None
    niDMM_ConfigureMultiPoint_cfunc = None
    niDMM_ReadMultiPoint_cfunc = None
    niDMM_FetchMultiPoint_cfunc = None
    niDMM_ConfigureTriggerSlope_cfunc = None
    niDMM_SendSoftwareTrigger_cfunc = None
    niDMM_GetApertureTimeInfo_cfunc = None
    niDMM_GetAutoRangeValue_cfunc = None
    niDMM_ConfigureAutoZeroMode_cfunc = None
    niDMM_ConfigurePowerLineFrequency_cfunc = None
    niDMM_ConfigureMeasurementDigits_cfunc = None
    niDMM_ConfigureMeasurementAbsolute_cfunc = None
    niDMM_ConfigureMeasCompleteSlope_cfunc = None
    niDMM_ConfigureSampleTriggerSlope_cfunc = None
    niDMM_ReadStatus_cfunc = None
    niDMM_Control_cfunc = None
    niDMM_ConfigureADCCalibration_cfunc = None
    niDMM_ConfigureOffsetCompOhms_cfunc = None
    niDMM_ConfigureCurrentSource_cfunc = None
    niDMM_ConfigureCableCompType_cfunc = None
    niDMM_PerformOpenCableComp_cfunc = None
    niDMM_PerformShortCableComp_cfunc = None
    niDMM_ConfigureOpenCableCompValues_cfunc = None
    niDMM_ConfigureShortCableCompValues_cfunc = None
    niDMM_LockSession_cfunc = None
    niDMM_UnlockSession_cfunc = None
    niDMM_ConfigureWaveformAcquisition_cfunc = None
    niDMM_ConfigureWaveformCoupling_cfunc = None
    niDMM_FetchWaveform_cfunc = None
    niDMM_ReadWaveform_cfunc = None
    niDMM_GetAttributeViInt32_cfunc = None
    niDMM_SetAttributeViInt32_cfunc = None
    niDMM_CheckAttributeViInt32_cfunc = None
    niDMM_GetAttributeViReal64_cfunc = None
    niDMM_SetAttributeViReal64_cfunc = None
    niDMM_CheckAttributeViReal64_cfunc = None
    niDMM_GetAttributeViString_cfunc = None
    niDMM_SetAttributeViString_cfunc = None
    niDMM_CheckAttributeViString_cfunc = None
    niDMM_GetAttributeViSession_cfunc = None
    niDMM_SetAttributeViSession_cfunc = None
    niDMM_CheckAttributeViSession_cfunc = None
    niDMM_GetAttributeViBoolean_cfunc = None
    niDMM_SetAttributeViBoolean_cfunc = None
    niDMM_CheckAttributeViBoolean_cfunc = None
    niDMM_GetNextCoercionRecord_cfunc = None
    niDMM_GetNextInterchangeWarning_cfunc = None
    niDMM_ResetInterchangeCheck_cfunc = None
    niDMM_ClearInterchangeWarnings_cfunc = None
    niDMM_4022Control_cfunc = None
    niDMM_GetChannelName_cfunc = None
    niDMM_InitExtCal_cfunc = None
    niDMM_CloseExtCal_cfunc = None
    niDMM_CalAdjustLinearization_cfunc = None
    niDMM_CalAdjustGain_cfunc = None
    niDMM_CalAdjustOffset_cfunc = None
    niDMM_CalAdjustMisc_cfunc = None
    niDMM_CalAdjustLC_cfunc = None
    niDMM_CalAdjustACFilter_cfunc = None
    niDMM_RestoreLastExtCalConstants_cfunc = None
    niDMM_SetCalPassword_cfunc = None
    niDMM_GetExtCalRecommendedInterval_cfunc = None
    niDMM_SetCalUserDefinedInfo_cfunc = None
    niDMM_GetCalUserDefinedInfoMaxSize_cfunc = None
    niDMM_GetCalUserDefinedInfo_cfunc = None
    niDMM_GetSelfCalSupported_cfunc = None
    niDMM_GetCalDateAndTime_cfunc = None
    niDMM_GetCalCount_cfunc = None
    niDMM_GetLastCalTemp_cfunc = None
    niDMM_GetDevTemp_cfunc = None
    niDMM_ConfigureTransducerType_cfunc = None
    niDMM_ConfigureThermocouple_cfunc = None
    niDMM_ConfigureFixedRefJunction_cfunc = None
    niDMM_ConfigureRTDType_cfunc = None
    niDMM_ConfigureRTDCustom_cfunc = None
    niDMM_ConfigureThermistorType_cfunc = None
    niDMM_ConfigureThermistorCustom_cfunc = None

    def __init__(self, library_name):
        self._cdll = ctypes.CDLL(library_name)


    def niDMM_init(self, resourceName, IDQuery, reset, newVi):
        if self.niDMM_init_cfunc is None:
            self.niDMM_init_cfunc = self._cdll.niDMM_init
            self.niDMM_init_cfunc.argtypes = [ctypes.c_char_p, ctypes.c_ushort, ctypes.c_ushort, ctypes.POINTER(ctypes.c_ulong)]
            self.niDMM_init_cfunc.restype = c_long
        return self.niDMM_init_cfunc(self, resourceName, IDQuery, reset, newVi)

    def niDMM_InitWithOptions(self, resourceName, IDQuery, resetDevice, optionsString, newVi):
        if self.niDMM_InitWithOptions_cfunc is None:
            self.niDMM_InitWithOptions_cfunc = self._cdll.niDMM_InitWithOptions
            self.niDMM_InitWithOptions_cfunc.argtypes = [ctypes.c_char_p, ctypes.c_ushort, ctypes.c_ushort, ctypes.c_char_p, ctypes.POINTER(ctypes.c_ulong)]
            self.niDMM_InitWithOptions_cfunc.restype = c_long
        return self.niDMM_InitWithOptions_cfunc(self, resourceName, IDQuery, resetDevice, optionsString, newVi)

    def niDMM_close(self, vi):
        if self.niDMM_close_cfunc is None:
            self.niDMM_close_cfunc = self._cdll.niDMM_close
            self.niDMM_close_cfunc.argtypes = [ctypes.c_ulong]
            self.niDMM_close_cfunc.restype = c_long
        return self.niDMM_close_cfunc(self, vi)

    def niDMM_GetError(self, vi, errorCode, bufferSize, description):
        if self.niDMM_GetError_cfunc is None:
            self.niDMM_GetError_cfunc = self._cdll.niDMM_GetError
            self.niDMM_GetError_cfunc.argtypes = [ctypes.c_ulong, ctypes.POINTER(ctypes.c_long), ctypes.c_long, ctypes.c_char_p]
            self.niDMM_GetError_cfunc.restype = c_long
        return self.niDMM_GetError_cfunc(self, vi, errorCode, bufferSize, description)

    def niDMM_GetErrorMessage(self, vi, errorCode, bufferSize, errMessage):
        if self.niDMM_GetErrorMessage_cfunc is None:
            self.niDMM_GetErrorMessage_cfunc = self._cdll.niDMM_GetErrorMessage
            self.niDMM_GetErrorMessage_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.c_long, ctypes.c_char_p]
            self.niDMM_GetErrorMessage_cfunc.restype = c_long
        return self.niDMM_GetErrorMessage_cfunc(self, vi, errorCode, bufferSize, errMessage)

    def niDMM_ClearError(self, vi):
        if self.niDMM_ClearError_cfunc is None:
            self.niDMM_ClearError_cfunc = self._cdll.niDMM_ClearError
            self.niDMM_ClearError_cfunc.argtypes = [ctypes.c_ulong]
            self.niDMM_ClearError_cfunc.restype = c_long
        return self.niDMM_ClearError_cfunc(self, vi)

    def niDMM_reset(self, vi):
        if self.niDMM_reset_cfunc is None:
            self.niDMM_reset_cfunc = self._cdll.niDMM_reset
            self.niDMM_reset_cfunc.argtypes = [ctypes.c_ulong]
            self.niDMM_reset_cfunc.restype = c_long
        return self.niDMM_reset_cfunc(self, vi)

    def niDMM_self_test(self, vi, selfTestResult, selfTestMessage):
        if self.niDMM_self_test_cfunc is None:
            self.niDMM_self_test_cfunc = self._cdll.niDMM_self_test
            self.niDMM_self_test_cfunc.argtypes = [ctypes.c_ulong, ctypes.POINTER(ctypes.c_short), ctypes.c_char_p]
            self.niDMM_self_test_cfunc.restype = c_long
        return self.niDMM_self_test_cfunc(self, vi, selfTestResult, selfTestMessage)

    def niDMM_SelfCal(self, vi):
        if self.niDMM_SelfCal_cfunc is None:
            self.niDMM_SelfCal_cfunc = self._cdll.niDMM_SelfCal
            self.niDMM_SelfCal_cfunc.argtypes = [ctypes.c_ulong]
            self.niDMM_SelfCal_cfunc.restype = c_long
        return self.niDMM_SelfCal_cfunc(self, vi)

    def niDMM_revision_query(self, vi, driverRev, instrRev):
        if self.niDMM_revision_query_cfunc is None:
            self.niDMM_revision_query_cfunc = self._cdll.niDMM_revision_query
            self.niDMM_revision_query_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_char_p, ctypes.c_char_p]
            self.niDMM_revision_query_cfunc.restype = c_long
        return self.niDMM_revision_query_cfunc(self, vi, driverRev, instrRev)

    def niDMM_InvalidateAllAttributes(self, vi):
        if self.niDMM_InvalidateAllAttributes_cfunc is None:
            self.niDMM_InvalidateAllAttributes_cfunc = self._cdll.niDMM_InvalidateAllAttributes
            self.niDMM_InvalidateAllAttributes_cfunc.argtypes = [ctypes.c_ulong]
            self.niDMM_InvalidateAllAttributes_cfunc.restype = c_long
        return self.niDMM_InvalidateAllAttributes_cfunc(self, vi)

    def niDMM_ResetWithDefaults(self, vi):
        if self.niDMM_ResetWithDefaults_cfunc is None:
            self.niDMM_ResetWithDefaults_cfunc = self._cdll.niDMM_ResetWithDefaults
            self.niDMM_ResetWithDefaults_cfunc.argtypes = [ctypes.c_ulong]
            self.niDMM_ResetWithDefaults_cfunc.restype = c_long
        return self.niDMM_ResetWithDefaults_cfunc(self, vi)

    def niDMM_Disable(self, vi):
        if self.niDMM_Disable_cfunc is None:
            self.niDMM_Disable_cfunc = self._cdll.niDMM_Disable
            self.niDMM_Disable_cfunc.argtypes = [ctypes.c_ulong]
            self.niDMM_Disable_cfunc.restype = c_long
        return self.niDMM_Disable_cfunc(self, vi)

    def niDMM_GetMeasurementPeriod(self, vi, period):
        if self.niDMM_GetMeasurementPeriod_cfunc is None:
            self.niDMM_GetMeasurementPeriod_cfunc = self._cdll.niDMM_GetMeasurementPeriod
            self.niDMM_GetMeasurementPeriod_cfunc.argtypes = [ctypes.c_ulong, ctypes.POINTER(ctypes.c_double)]
            self.niDMM_GetMeasurementPeriod_cfunc.restype = c_long
        return self.niDMM_GetMeasurementPeriod_cfunc(self, vi, period)

    def niDMM_ConfigureTrigger(self, vi, trigSource, triggerDelay):
        if self.niDMM_ConfigureTrigger_cfunc is None:
            self.niDMM_ConfigureTrigger_cfunc = self._cdll.niDMM_ConfigureTrigger
            self.niDMM_ConfigureTrigger_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.c_double]
            self.niDMM_ConfigureTrigger_cfunc.restype = c_long
        return self.niDMM_ConfigureTrigger_cfunc(self, vi, trigSource, triggerDelay)

    def niDMM_Read(self, vi, maxTime, reading):
        if self.niDMM_Read_cfunc is None:
            self.niDMM_Read_cfunc = self._cdll.niDMM_Read
            self.niDMM_Read_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.POINTER(ctypes.c_double)]
            self.niDMM_Read_cfunc.restype = c_long
        return self.niDMM_Read_cfunc(self, vi, maxTime, reading)

    def niDMM_Fetch(self, vi, maxTime, reading):
        if self.niDMM_Fetch_cfunc is None:
            self.niDMM_Fetch_cfunc = self._cdll.niDMM_Fetch
            self.niDMM_Fetch_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.POINTER(ctypes.c_double)]
            self.niDMM_Fetch_cfunc.restype = c_long
        return self.niDMM_Fetch_cfunc(self, vi, maxTime, reading)

    def niDMM_Abort(self, vi):
        if self.niDMM_Abort_cfunc is None:
            self.niDMM_Abort_cfunc = self._cdll.niDMM_Abort
            self.niDMM_Abort_cfunc.argtypes = [ctypes.c_ulong]
            self.niDMM_Abort_cfunc.restype = c_long
        return self.niDMM_Abort_cfunc(self, vi)

    def niDMM_Initiate(self, vi):
        if self.niDMM_Initiate_cfunc is None:
            self.niDMM_Initiate_cfunc = self._cdll.niDMM_Initiate
            self.niDMM_Initiate_cfunc.argtypes = [ctypes.c_ulong]
            self.niDMM_Initiate_cfunc.restype = c_long
        return self.niDMM_Initiate_cfunc(self, vi)

    def niDMM_IsOverRange(self, vi, measurementValue, isOverRange):
        if self.niDMM_IsOverRange_cfunc is None:
            self.niDMM_IsOverRange_cfunc = self._cdll.niDMM_IsOverRange
            self.niDMM_IsOverRange_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_double, ctypes.POINTER(ctypes.c_ushort)]
            self.niDMM_IsOverRange_cfunc.restype = c_long
        return self.niDMM_IsOverRange_cfunc(self, vi, measurementValue, isOverRange)

    def niDMM_IsUnderRange(self, vi, measurementValue, isUnderRange):
        if self.niDMM_IsUnderRange_cfunc is None:
            self.niDMM_IsUnderRange_cfunc = self._cdll.niDMM_IsUnderRange
            self.niDMM_IsUnderRange_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_double, ctypes.POINTER(ctypes.c_ushort)]
            self.niDMM_IsUnderRange_cfunc.restype = c_long
        return self.niDMM_IsUnderRange_cfunc(self, vi, measurementValue, isUnderRange)

    def niDMM_ConfigureACBandwidth(self, vi, minFreq, maxFreq):
        if self.niDMM_ConfigureACBandwidth_cfunc is None:
            self.niDMM_ConfigureACBandwidth_cfunc = self._cdll.niDMM_ConfigureACBandwidth
            self.niDMM_ConfigureACBandwidth_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_double, ctypes.c_double]
            self.niDMM_ConfigureACBandwidth_cfunc.restype = c_long
        return self.niDMM_ConfigureACBandwidth_cfunc(self, vi, minFreq, maxFreq)

    def niDMM_ConfigureFrequencyVoltageRange(self, vi, frequencyVoltageRange):
        if self.niDMM_ConfigureFrequencyVoltageRange_cfunc is None:
            self.niDMM_ConfigureFrequencyVoltageRange_cfunc = self._cdll.niDMM_ConfigureFrequencyVoltageRange
            self.niDMM_ConfigureFrequencyVoltageRange_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_double]
            self.niDMM_ConfigureFrequencyVoltageRange_cfunc.restype = c_long
        return self.niDMM_ConfigureFrequencyVoltageRange_cfunc(self, vi, frequencyVoltageRange)

    def niDMM_ConfigureMeasCompleteDest(self, vi, destination):
        if self.niDMM_ConfigureMeasCompleteDest_cfunc is None:
            self.niDMM_ConfigureMeasCompleteDest_cfunc = self._cdll.niDMM_ConfigureMeasCompleteDest
            self.niDMM_ConfigureMeasCompleteDest_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_long]
            self.niDMM_ConfigureMeasCompleteDest_cfunc.restype = c_long
        return self.niDMM_ConfigureMeasCompleteDest_cfunc(self, vi, destination)

    def niDMM_ConfigureMultiPoint(self, vi, triggerCount, sampleCount, sampleTrigger, sampleInterval):
        if self.niDMM_ConfigureMultiPoint_cfunc is None:
            self.niDMM_ConfigureMultiPoint_cfunc = self._cdll.niDMM_ConfigureMultiPoint
            self.niDMM_ConfigureMultiPoint_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_double]
            self.niDMM_ConfigureMultiPoint_cfunc.restype = c_long
        return self.niDMM_ConfigureMultiPoint_cfunc(self, vi, triggerCount, sampleCount, sampleTrigger, sampleInterval)

    def niDMM_ReadMultiPoint(self, vi, maxTime, arraySize, readingArray, actualPts):
        if self.niDMM_ReadMultiPoint_cfunc is None:
            self.niDMM_ReadMultiPoint_cfunc = self._cdll.niDMM_ReadMultiPoint
            self.niDMM_ReadMultiPoint_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.c_long, ctypes.c_double, ctypes.POINTER(ctypes.c_long)]
            self.niDMM_ReadMultiPoint_cfunc.restype = c_long
        return self.niDMM_ReadMultiPoint_cfunc(self, vi, maxTime, arraySize, readingArray, actualPts)

    def niDMM_FetchMultiPoint(self, vi, maxTime, arraySize, readingArray, actualPts):
        if self.niDMM_FetchMultiPoint_cfunc is None:
            self.niDMM_FetchMultiPoint_cfunc = self._cdll.niDMM_FetchMultiPoint
            self.niDMM_FetchMultiPoint_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.c_long, ctypes.c_double, ctypes.POINTER(ctypes.c_long)]
            self.niDMM_FetchMultiPoint_cfunc.restype = c_long
        return self.niDMM_FetchMultiPoint_cfunc(self, vi, maxTime, arraySize, readingArray, actualPts)

    def niDMM_ConfigureTriggerSlope(self, vi, polarity):
        if self.niDMM_ConfigureTriggerSlope_cfunc is None:
            self.niDMM_ConfigureTriggerSlope_cfunc = self._cdll.niDMM_ConfigureTriggerSlope
            self.niDMM_ConfigureTriggerSlope_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_long]
            self.niDMM_ConfigureTriggerSlope_cfunc.restype = c_long
        return self.niDMM_ConfigureTriggerSlope_cfunc(self, vi, polarity)

    def niDMM_SendSoftwareTrigger(self, vi):
        if self.niDMM_SendSoftwareTrigger_cfunc is None:
            self.niDMM_SendSoftwareTrigger_cfunc = self._cdll.niDMM_SendSoftwareTrigger
            self.niDMM_SendSoftwareTrigger_cfunc.argtypes = [ctypes.c_ulong]
            self.niDMM_SendSoftwareTrigger_cfunc.restype = c_long
        return self.niDMM_SendSoftwareTrigger_cfunc(self, vi)

    def niDMM_GetApertureTimeInfo(self, vi, apertureTime, apertureTimeUnits):
        if self.niDMM_GetApertureTimeInfo_cfunc is None:
            self.niDMM_GetApertureTimeInfo_cfunc = self._cdll.niDMM_GetApertureTimeInfo
            self.niDMM_GetApertureTimeInfo_cfunc.argtypes = [ctypes.c_ulong, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_long)]
            self.niDMM_GetApertureTimeInfo_cfunc.restype = c_long
        return self.niDMM_GetApertureTimeInfo_cfunc(self, vi, apertureTime, apertureTimeUnits)

    def niDMM_GetAutoRangeValue(self, vi, autoRangeValue):
        if self.niDMM_GetAutoRangeValue_cfunc is None:
            self.niDMM_GetAutoRangeValue_cfunc = self._cdll.niDMM_GetAutoRangeValue
            self.niDMM_GetAutoRangeValue_cfunc.argtypes = [ctypes.c_ulong, ctypes.POINTER(ctypes.c_double)]
            self.niDMM_GetAutoRangeValue_cfunc.restype = c_long
        return self.niDMM_GetAutoRangeValue_cfunc(self, vi, autoRangeValue)

    def niDMM_ConfigureAutoZeroMode(self, vi, autoZeroMode):
        if self.niDMM_ConfigureAutoZeroMode_cfunc is None:
            self.niDMM_ConfigureAutoZeroMode_cfunc = self._cdll.niDMM_ConfigureAutoZeroMode
            self.niDMM_ConfigureAutoZeroMode_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_long]
            self.niDMM_ConfigureAutoZeroMode_cfunc.restype = c_long
        return self.niDMM_ConfigureAutoZeroMode_cfunc(self, vi, autoZeroMode)

    def niDMM_ConfigurePowerLineFrequency(self, vi, frequency):
        if self.niDMM_ConfigurePowerLineFrequency_cfunc is None:
            self.niDMM_ConfigurePowerLineFrequency_cfunc = self._cdll.niDMM_ConfigurePowerLineFrequency
            self.niDMM_ConfigurePowerLineFrequency_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_double]
            self.niDMM_ConfigurePowerLineFrequency_cfunc.restype = c_long
        return self.niDMM_ConfigurePowerLineFrequency_cfunc(self, vi, frequency)

    def niDMM_ConfigureMeasurementDigits(self, vi, measFunction, range, resolutionDigits):
        if self.niDMM_ConfigureMeasurementDigits_cfunc is None:
            self.niDMM_ConfigureMeasurementDigits_cfunc = self._cdll.niDMM_ConfigureMeasurementDigits
            self.niDMM_ConfigureMeasurementDigits_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.c_double, ctypes.c_double]
            self.niDMM_ConfigureMeasurementDigits_cfunc.restype = c_long
        return self.niDMM_ConfigureMeasurementDigits_cfunc(self, vi, measFunction, range, resolutionDigits)

    def niDMM_ConfigureMeasurementAbsolute(self, vi, measFunction, range, resolutionAbsolute):
        if self.niDMM_ConfigureMeasurementAbsolute_cfunc is None:
            self.niDMM_ConfigureMeasurementAbsolute_cfunc = self._cdll.niDMM_ConfigureMeasurementAbsolute
            self.niDMM_ConfigureMeasurementAbsolute_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.c_double, ctypes.c_double]
            self.niDMM_ConfigureMeasurementAbsolute_cfunc.restype = c_long
        return self.niDMM_ConfigureMeasurementAbsolute_cfunc(self, vi, measFunction, range, resolutionAbsolute)

    def niDMM_ConfigureMeasCompleteSlope(self, vi, polarity):
        if self.niDMM_ConfigureMeasCompleteSlope_cfunc is None:
            self.niDMM_ConfigureMeasCompleteSlope_cfunc = self._cdll.niDMM_ConfigureMeasCompleteSlope
            self.niDMM_ConfigureMeasCompleteSlope_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_long]
            self.niDMM_ConfigureMeasCompleteSlope_cfunc.restype = c_long
        return self.niDMM_ConfigureMeasCompleteSlope_cfunc(self, vi, polarity)

    def niDMM_ConfigureSampleTriggerSlope(self, vi, polarity):
        if self.niDMM_ConfigureSampleTriggerSlope_cfunc is None:
            self.niDMM_ConfigureSampleTriggerSlope_cfunc = self._cdll.niDMM_ConfigureSampleTriggerSlope
            self.niDMM_ConfigureSampleTriggerSlope_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_long]
            self.niDMM_ConfigureSampleTriggerSlope_cfunc.restype = c_long
        return self.niDMM_ConfigureSampleTriggerSlope_cfunc(self, vi, polarity)

    def niDMM_ReadStatus(self, vi, acqBacklog, acqDone):
        if self.niDMM_ReadStatus_cfunc is None:
            self.niDMM_ReadStatus_cfunc = self._cdll.niDMM_ReadStatus
            self.niDMM_ReadStatus_cfunc.argtypes = [ctypes.c_ulong, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_short)]
            self.niDMM_ReadStatus_cfunc.restype = c_long
        return self.niDMM_ReadStatus_cfunc(self, vi, acqBacklog, acqDone)

    def niDMM_Control(self, vi, action):
        if self.niDMM_Control_cfunc is None:
            self.niDMM_Control_cfunc = self._cdll.niDMM_Control
            self.niDMM_Control_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_long]
            self.niDMM_Control_cfunc.restype = c_long
        return self.niDMM_Control_cfunc(self, vi, action)

    def niDMM_ConfigureADCCalibration(self, vi, adcGainComp):
        if self.niDMM_ConfigureADCCalibration_cfunc is None:
            self.niDMM_ConfigureADCCalibration_cfunc = self._cdll.niDMM_ConfigureADCCalibration
            self.niDMM_ConfigureADCCalibration_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_long]
            self.niDMM_ConfigureADCCalibration_cfunc.restype = c_long
        return self.niDMM_ConfigureADCCalibration_cfunc(self, vi, adcGainComp)

    def niDMM_ConfigureOffsetCompOhms(self, vi, offsetCompOhms):
        if self.niDMM_ConfigureOffsetCompOhms_cfunc is None:
            self.niDMM_ConfigureOffsetCompOhms_cfunc = self._cdll.niDMM_ConfigureOffsetCompOhms
            self.niDMM_ConfigureOffsetCompOhms_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_long]
            self.niDMM_ConfigureOffsetCompOhms_cfunc.restype = c_long
        return self.niDMM_ConfigureOffsetCompOhms_cfunc(self, vi, offsetCompOhms)

    def niDMM_ConfigureCurrentSource(self, vi, diodeCurrentSrc):
        if self.niDMM_ConfigureCurrentSource_cfunc is None:
            self.niDMM_ConfigureCurrentSource_cfunc = self._cdll.niDMM_ConfigureCurrentSource
            self.niDMM_ConfigureCurrentSource_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_double]
            self.niDMM_ConfigureCurrentSource_cfunc.restype = c_long
        return self.niDMM_ConfigureCurrentSource_cfunc(self, vi, diodeCurrentSrc)

    def niDMM_ConfigureCableCompType(self, vi, typeOfCompensation):
        if self.niDMM_ConfigureCableCompType_cfunc is None:
            self.niDMM_ConfigureCableCompType_cfunc = self._cdll.niDMM_ConfigureCableCompType
            self.niDMM_ConfigureCableCompType_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_long]
            self.niDMM_ConfigureCableCompType_cfunc.restype = c_long
        return self.niDMM_ConfigureCableCompType_cfunc(self, vi, typeOfCompensation)

    def niDMM_PerformOpenCableComp(self, vi, conductance, susceptance):
        if self.niDMM_PerformOpenCableComp_cfunc is None:
            self.niDMM_PerformOpenCableComp_cfunc = self._cdll.niDMM_PerformOpenCableComp
            self.niDMM_PerformOpenCableComp_cfunc.argtypes = [ctypes.c_ulong, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
            self.niDMM_PerformOpenCableComp_cfunc.restype = c_long
        return self.niDMM_PerformOpenCableComp_cfunc(self, vi, conductance, susceptance)

    def niDMM_PerformShortCableComp(self, vi, resistance, reactance):
        if self.niDMM_PerformShortCableComp_cfunc is None:
            self.niDMM_PerformShortCableComp_cfunc = self._cdll.niDMM_PerformShortCableComp
            self.niDMM_PerformShortCableComp_cfunc.argtypes = [ctypes.c_ulong, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
            self.niDMM_PerformShortCableComp_cfunc.restype = c_long
        return self.niDMM_PerformShortCableComp_cfunc(self, vi, resistance, reactance)

    def niDMM_ConfigureOpenCableCompValues(self, vi, conductance, susceptance):
        if self.niDMM_ConfigureOpenCableCompValues_cfunc is None:
            self.niDMM_ConfigureOpenCableCompValues_cfunc = self._cdll.niDMM_ConfigureOpenCableCompValues
            self.niDMM_ConfigureOpenCableCompValues_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_double, ctypes.c_double]
            self.niDMM_ConfigureOpenCableCompValues_cfunc.restype = c_long
        return self.niDMM_ConfigureOpenCableCompValues_cfunc(self, vi, conductance, susceptance)

    def niDMM_ConfigureShortCableCompValues(self, vi, resistance, reactance):
        if self.niDMM_ConfigureShortCableCompValues_cfunc is None:
            self.niDMM_ConfigureShortCableCompValues_cfunc = self._cdll.niDMM_ConfigureShortCableCompValues
            self.niDMM_ConfigureShortCableCompValues_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_double, ctypes.c_double]
            self.niDMM_ConfigureShortCableCompValues_cfunc.restype = c_long
        return self.niDMM_ConfigureShortCableCompValues_cfunc(self, vi, resistance, reactance)

    def niDMM_LockSession(self, vi, callerHasLock):
        if self.niDMM_LockSession_cfunc is None:
            self.niDMM_LockSession_cfunc = self._cdll.niDMM_LockSession
            self.niDMM_LockSession_cfunc.argtypes = [ctypes.c_ulong, ctypes.POINTER(ctypes.c_ushort)]
            self.niDMM_LockSession_cfunc.restype = c_long
        return self.niDMM_LockSession_cfunc(self, vi, callerHasLock)

    def niDMM_UnlockSession(self, vi, callerHasLock):
        if self.niDMM_UnlockSession_cfunc is None:
            self.niDMM_UnlockSession_cfunc = self._cdll.niDMM_UnlockSession
            self.niDMM_UnlockSession_cfunc.argtypes = [ctypes.c_ulong, ctypes.POINTER(ctypes.c_ushort)]
            self.niDMM_UnlockSession_cfunc.restype = c_long
        return self.niDMM_UnlockSession_cfunc(self, vi, callerHasLock)

    def niDMM_ConfigureWaveformAcquisition(self, vi, function, range, rate, waveformPoints):
        if self.niDMM_ConfigureWaveformAcquisition_cfunc is None:
            self.niDMM_ConfigureWaveformAcquisition_cfunc = self._cdll.niDMM_ConfigureWaveformAcquisition
            self.niDMM_ConfigureWaveformAcquisition_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.c_double, ctypes.c_double, ctypes.c_long]
            self.niDMM_ConfigureWaveformAcquisition_cfunc.restype = c_long
        return self.niDMM_ConfigureWaveformAcquisition_cfunc(self, vi, function, range, rate, waveformPoints)

    def niDMM_ConfigureWaveformCoupling(self, vi, coupling):
        if self.niDMM_ConfigureWaveformCoupling_cfunc is None:
            self.niDMM_ConfigureWaveformCoupling_cfunc = self._cdll.niDMM_ConfigureWaveformCoupling
            self.niDMM_ConfigureWaveformCoupling_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_long]
            self.niDMM_ConfigureWaveformCoupling_cfunc.restype = c_long
        return self.niDMM_ConfigureWaveformCoupling_cfunc(self, vi, coupling)

    def niDMM_FetchWaveform(self, vi, maxTime, arraySize, waveformArray, actualPoints):
        if self.niDMM_FetchWaveform_cfunc is None:
            self.niDMM_FetchWaveform_cfunc = self._cdll.niDMM_FetchWaveform
            self.niDMM_FetchWaveform_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.c_long, ctypes.c_double, ctypes.POINTER(ctypes.c_long)]
            self.niDMM_FetchWaveform_cfunc.restype = c_long
        return self.niDMM_FetchWaveform_cfunc(self, vi, maxTime, arraySize, waveformArray, actualPoints)

    def niDMM_ReadWaveform(self, vi, maxTime, arraySize, waveformArray, actualPoints):
        if self.niDMM_ReadWaveform_cfunc is None:
            self.niDMM_ReadWaveform_cfunc = self._cdll.niDMM_ReadWaveform
            self.niDMM_ReadWaveform_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.c_long, ctypes.c_double, ctypes.POINTER(ctypes.c_long)]
            self.niDMM_ReadWaveform_cfunc.restype = c_long
        return self.niDMM_ReadWaveform_cfunc(self, vi, maxTime, arraySize, waveformArray, actualPoints)

    def niDMM_GetAttributeViInt32(self, vi, channelName, attributeId, value):
        if self.niDMM_GetAttributeViInt32_cfunc is None:
            self.niDMM_GetAttributeViInt32_cfunc = self._cdll.niDMM_GetAttributeViInt32
            self.niDMM_GetAttributeViInt32_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_char_p, ctypes.c_long, ctypes.POINTER(ctypes.c_long)]
            self.niDMM_GetAttributeViInt32_cfunc.restype = c_long
        return self.niDMM_GetAttributeViInt32_cfunc(self, vi, channelName, attributeId, value)

    def niDMM_SetAttributeViInt32(self, vi, channelName, attributeId, value):
        if self.niDMM_SetAttributeViInt32_cfunc is None:
            self.niDMM_SetAttributeViInt32_cfunc = self._cdll.niDMM_SetAttributeViInt32
            self.niDMM_SetAttributeViInt32_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_char_p, ctypes.c_long, ctypes.c_long]
            self.niDMM_SetAttributeViInt32_cfunc.restype = c_long
        return self.niDMM_SetAttributeViInt32_cfunc(self, vi, channelName, attributeId, value)

    def niDMM_CheckAttributeViInt32(self, vi, channelName, attributeId, value):
        if self.niDMM_CheckAttributeViInt32_cfunc is None:
            self.niDMM_CheckAttributeViInt32_cfunc = self._cdll.niDMM_CheckAttributeViInt32
            self.niDMM_CheckAttributeViInt32_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_char_p, ctypes.c_long, ctypes.c_long]
            self.niDMM_CheckAttributeViInt32_cfunc.restype = c_long
        return self.niDMM_CheckAttributeViInt32_cfunc(self, vi, channelName, attributeId, value)

    def niDMM_GetAttributeViReal64(self, vi, channelName, attributeId, value):
        if self.niDMM_GetAttributeViReal64_cfunc is None:
            self.niDMM_GetAttributeViReal64_cfunc = self._cdll.niDMM_GetAttributeViReal64
            self.niDMM_GetAttributeViReal64_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_char_p, ctypes.c_long, ctypes.POINTER(ctypes.c_double)]
            self.niDMM_GetAttributeViReal64_cfunc.restype = c_long
        return self.niDMM_GetAttributeViReal64_cfunc(self, vi, channelName, attributeId, value)

    def niDMM_SetAttributeViReal64(self, vi, channelName, attributeId, value):
        if self.niDMM_SetAttributeViReal64_cfunc is None:
            self.niDMM_SetAttributeViReal64_cfunc = self._cdll.niDMM_SetAttributeViReal64
            self.niDMM_SetAttributeViReal64_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_char_p, ctypes.c_long, ctypes.c_double]
            self.niDMM_SetAttributeViReal64_cfunc.restype = c_long
        return self.niDMM_SetAttributeViReal64_cfunc(self, vi, channelName, attributeId, value)

    def niDMM_CheckAttributeViReal64(self, vi, channelName, attributeId, value):
        if self.niDMM_CheckAttributeViReal64_cfunc is None:
            self.niDMM_CheckAttributeViReal64_cfunc = self._cdll.niDMM_CheckAttributeViReal64
            self.niDMM_CheckAttributeViReal64_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_char_p, ctypes.c_long, ctypes.c_double]
            self.niDMM_CheckAttributeViReal64_cfunc.restype = c_long
        return self.niDMM_CheckAttributeViReal64_cfunc(self, vi, channelName, attributeId, value)

    def niDMM_GetAttributeViString(self, vi, channelName, attributeId, bufSize, value):
        if self.niDMM_GetAttributeViString_cfunc is None:
            self.niDMM_GetAttributeViString_cfunc = self._cdll.niDMM_GetAttributeViString
            self.niDMM_GetAttributeViString_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_char_p, ctypes.c_long, ctypes.c_long, ctypes.c_char_p]
            self.niDMM_GetAttributeViString_cfunc.restype = c_long
        return self.niDMM_GetAttributeViString_cfunc(self, vi, channelName, attributeId, bufSize, value)

    def niDMM_SetAttributeViString(self, vi, channelName, attributeId, value):
        if self.niDMM_SetAttributeViString_cfunc is None:
            self.niDMM_SetAttributeViString_cfunc = self._cdll.niDMM_SetAttributeViString
            self.niDMM_SetAttributeViString_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_char_p, ctypes.c_long, ctypes.c_char_p]
            self.niDMM_SetAttributeViString_cfunc.restype = c_long
        return self.niDMM_SetAttributeViString_cfunc(self, vi, channelName, attributeId, value)

    def niDMM_CheckAttributeViString(self, vi, channelName, attributeId, value):
        if self.niDMM_CheckAttributeViString_cfunc is None:
            self.niDMM_CheckAttributeViString_cfunc = self._cdll.niDMM_CheckAttributeViString
            self.niDMM_CheckAttributeViString_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_char_p, ctypes.c_long, ctypes.c_char_p]
            self.niDMM_CheckAttributeViString_cfunc.restype = c_long
        return self.niDMM_CheckAttributeViString_cfunc(self, vi, channelName, attributeId, value)

    def niDMM_GetAttributeViSession(self, vi, channelName, attributeId, value):
        if self.niDMM_GetAttributeViSession_cfunc is None:
            self.niDMM_GetAttributeViSession_cfunc = self._cdll.niDMM_GetAttributeViSession
            self.niDMM_GetAttributeViSession_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_char_p, ctypes.c_long, ctypes.POINTER(ctypes.c_ulong)]
            self.niDMM_GetAttributeViSession_cfunc.restype = c_long
        return self.niDMM_GetAttributeViSession_cfunc(self, vi, channelName, attributeId, value)

    def niDMM_SetAttributeViSession(self, vi, channelName, attributeId, value):
        if self.niDMM_SetAttributeViSession_cfunc is None:
            self.niDMM_SetAttributeViSession_cfunc = self._cdll.niDMM_SetAttributeViSession
            self.niDMM_SetAttributeViSession_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_char_p, ctypes.c_long, ctypes.c_ulong]
            self.niDMM_SetAttributeViSession_cfunc.restype = c_long
        return self.niDMM_SetAttributeViSession_cfunc(self, vi, channelName, attributeId, value)

    def niDMM_CheckAttributeViSession(self, vi, channelName, attributeId, value):
        if self.niDMM_CheckAttributeViSession_cfunc is None:
            self.niDMM_CheckAttributeViSession_cfunc = self._cdll.niDMM_CheckAttributeViSession
            self.niDMM_CheckAttributeViSession_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_char_p, ctypes.c_long, ctypes.c_ulong]
            self.niDMM_CheckAttributeViSession_cfunc.restype = c_long
        return self.niDMM_CheckAttributeViSession_cfunc(self, vi, channelName, attributeId, value)

    def niDMM_GetAttributeViBoolean(self, vi, channelName, attributeId, value):
        if self.niDMM_GetAttributeViBoolean_cfunc is None:
            self.niDMM_GetAttributeViBoolean_cfunc = self._cdll.niDMM_GetAttributeViBoolean
            self.niDMM_GetAttributeViBoolean_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_char_p, ctypes.c_long, ctypes.POINTER(ctypes.c_ushort)]
            self.niDMM_GetAttributeViBoolean_cfunc.restype = c_long
        return self.niDMM_GetAttributeViBoolean_cfunc(self, vi, channelName, attributeId, value)

    def niDMM_SetAttributeViBoolean(self, vi, channelName, attributeId, value):
        if self.niDMM_SetAttributeViBoolean_cfunc is None:
            self.niDMM_SetAttributeViBoolean_cfunc = self._cdll.niDMM_SetAttributeViBoolean
            self.niDMM_SetAttributeViBoolean_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_char_p, ctypes.c_long, ctypes.c_ushort]
            self.niDMM_SetAttributeViBoolean_cfunc.restype = c_long
        return self.niDMM_SetAttributeViBoolean_cfunc(self, vi, channelName, attributeId, value)

    def niDMM_CheckAttributeViBoolean(self, vi, channelName, attributeId, value):
        if self.niDMM_CheckAttributeViBoolean_cfunc is None:
            self.niDMM_CheckAttributeViBoolean_cfunc = self._cdll.niDMM_CheckAttributeViBoolean
            self.niDMM_CheckAttributeViBoolean_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_char_p, ctypes.c_long, ctypes.c_ushort]
            self.niDMM_CheckAttributeViBoolean_cfunc.restype = c_long
        return self.niDMM_CheckAttributeViBoolean_cfunc(self, vi, channelName, attributeId, value)

    def niDMM_GetNextCoercionRecord(self, vi, bufferSize, record):
        if self.niDMM_GetNextCoercionRecord_cfunc is None:
            self.niDMM_GetNextCoercionRecord_cfunc = self._cdll.niDMM_GetNextCoercionRecord
            self.niDMM_GetNextCoercionRecord_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.c_char_p]
            self.niDMM_GetNextCoercionRecord_cfunc.restype = c_long
        return self.niDMM_GetNextCoercionRecord_cfunc(self, vi, bufferSize, record)

    def niDMM_GetNextInterchangeWarning(self, vi, bufferSize, warnString):
        if self.niDMM_GetNextInterchangeWarning_cfunc is None:
            self.niDMM_GetNextInterchangeWarning_cfunc = self._cdll.niDMM_GetNextInterchangeWarning
            self.niDMM_GetNextInterchangeWarning_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.c_char_p]
            self.niDMM_GetNextInterchangeWarning_cfunc.restype = c_long
        return self.niDMM_GetNextInterchangeWarning_cfunc(self, vi, bufferSize, warnString)

    def niDMM_ResetInterchangeCheck(self, vi):
        if self.niDMM_ResetInterchangeCheck_cfunc is None:
            self.niDMM_ResetInterchangeCheck_cfunc = self._cdll.niDMM_ResetInterchangeCheck
            self.niDMM_ResetInterchangeCheck_cfunc.argtypes = [ctypes.c_ulong]
            self.niDMM_ResetInterchangeCheck_cfunc.restype = c_long
        return self.niDMM_ResetInterchangeCheck_cfunc(self, vi)

    def niDMM_ClearInterchangeWarnings(self, vi):
        if self.niDMM_ClearInterchangeWarnings_cfunc is None:
            self.niDMM_ClearInterchangeWarnings_cfunc = self._cdll.niDMM_ClearInterchangeWarnings
            self.niDMM_ClearInterchangeWarnings_cfunc.argtypes = [ctypes.c_ulong]
            self.niDMM_ClearInterchangeWarnings_cfunc.restype = c_long
        return self.niDMM_ClearInterchangeWarnings_cfunc(self, vi)

    def niDMM_4022Control(self, resourceName, configuration):
        if self.niDMM_4022Control_cfunc is None:
            self.niDMM_4022Control_cfunc = self._cdll.niDMM_4022Control
            self.niDMM_4022Control_cfunc.argtypes = [ctypes.c_char_p, ctypes.c_long]
            self.niDMM_4022Control_cfunc.restype = c_long
        return self.niDMM_4022Control_cfunc(self, resourceName, configuration)

    def niDMM_GetChannelName(self, vi, index, bufferSize, name):
        if self.niDMM_GetChannelName_cfunc is None:
            self.niDMM_GetChannelName_cfunc = self._cdll.niDMM_GetChannelName
            self.niDMM_GetChannelName_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.c_long, ctypes.c_char_p]
            self.niDMM_GetChannelName_cfunc.restype = c_long
        return self.niDMM_GetChannelName_cfunc(self, vi, index, bufferSize, name)

    def niDMM_InitExtCal(self, resourceName, password, newVi):
        if self.niDMM_InitExtCal_cfunc is None:
            self.niDMM_InitExtCal_cfunc = self._cdll.niDMM_InitExtCal
            self.niDMM_InitExtCal_cfunc.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_ulong)]
            self.niDMM_InitExtCal_cfunc.restype = c_long
        return self.niDMM_InitExtCal_cfunc(self, resourceName, password, newVi)

    def niDMM_CloseExtCal(self, vi, action):
        if self.niDMM_CloseExtCal_cfunc is None:
            self.niDMM_CloseExtCal_cfunc = self._cdll.niDMM_CloseExtCal
            self.niDMM_CloseExtCal_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_long]
            self.niDMM_CloseExtCal_cfunc.restype = c_long
        return self.niDMM_CloseExtCal_cfunc(self, vi, action)

    def niDMM_CalAdjustLinearization(self, vi, mode, range, inputR, expectedValue):
        if self.niDMM_CalAdjustLinearization_cfunc is None:
            self.niDMM_CalAdjustLinearization_cfunc = self._cdll.niDMM_CalAdjustLinearization
            self.niDMM_CalAdjustLinearization_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.c_double, ctypes.c_double, ctypes.c_double]
            self.niDMM_CalAdjustLinearization_cfunc.restype = c_long
        return self.niDMM_CalAdjustLinearization_cfunc(self, vi, mode, range, inputR, expectedValue)

    def niDMM_CalAdjustGain(self, vi, mode, range, inputR, expectedValue):
        if self.niDMM_CalAdjustGain_cfunc is None:
            self.niDMM_CalAdjustGain_cfunc = self._cdll.niDMM_CalAdjustGain
            self.niDMM_CalAdjustGain_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.c_double, ctypes.c_double, ctypes.c_double]
            self.niDMM_CalAdjustGain_cfunc.restype = c_long
        return self.niDMM_CalAdjustGain_cfunc(self, vi, mode, range, inputR, expectedValue)

    def niDMM_CalAdjustOffset(self, vi, mode, range, inputR):
        if self.niDMM_CalAdjustOffset_cfunc is None:
            self.niDMM_CalAdjustOffset_cfunc = self._cdll.niDMM_CalAdjustOffset
            self.niDMM_CalAdjustOffset_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.c_double, ctypes.c_double]
            self.niDMM_CalAdjustOffset_cfunc.restype = c_long
        return self.niDMM_CalAdjustOffset_cfunc(self, vi, mode, range, inputR)

    def niDMM_CalAdjustMisc(self, vi, type):
        if self.niDMM_CalAdjustMisc_cfunc is None:
            self.niDMM_CalAdjustMisc_cfunc = self._cdll.niDMM_CalAdjustMisc
            self.niDMM_CalAdjustMisc_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_long]
            self.niDMM_CalAdjustMisc_cfunc.restype = c_long
        return self.niDMM_CalAdjustMisc_cfunc(self, vi, type)

    def niDMM_CalAdjustLC(self, vi, type):
        if self.niDMM_CalAdjustLC_cfunc is None:
            self.niDMM_CalAdjustLC_cfunc = self._cdll.niDMM_CalAdjustLC
            self.niDMM_CalAdjustLC_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_long]
            self.niDMM_CalAdjustLC_cfunc.restype = c_long
        return self.niDMM_CalAdjustLC_cfunc(self, vi, type)

    def niDMM_CalAdjustACFilter(self, vi, mode, range, frequency, expectedValue):
        if self.niDMM_CalAdjustACFilter_cfunc is None:
            self.niDMM_CalAdjustACFilter_cfunc = self._cdll.niDMM_CalAdjustACFilter
            self.niDMM_CalAdjustACFilter_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.c_double, ctypes.c_double, ctypes.c_double]
            self.niDMM_CalAdjustACFilter_cfunc.restype = c_long
        return self.niDMM_CalAdjustACFilter_cfunc(self, vi, mode, range, frequency, expectedValue)

    def niDMM_RestoreLastExtCalConstants(self, vi):
        if self.niDMM_RestoreLastExtCalConstants_cfunc is None:
            self.niDMM_RestoreLastExtCalConstants_cfunc = self._cdll.niDMM_RestoreLastExtCalConstants
            self.niDMM_RestoreLastExtCalConstants_cfunc.argtypes = [ctypes.c_ulong]
            self.niDMM_RestoreLastExtCalConstants_cfunc.restype = c_long
        return self.niDMM_RestoreLastExtCalConstants_cfunc(self, vi)

    def niDMM_SetCalPassword(self, vi, oldPassword, newPassword):
        if self.niDMM_SetCalPassword_cfunc is None:
            self.niDMM_SetCalPassword_cfunc = self._cdll.niDMM_SetCalPassword
            self.niDMM_SetCalPassword_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_char_p, ctypes.c_char_p]
            self.niDMM_SetCalPassword_cfunc.restype = c_long
        return self.niDMM_SetCalPassword_cfunc(self, vi, oldPassword, newPassword)

    def niDMM_GetExtCalRecommendedInterval(self, vi, months):
        if self.niDMM_GetExtCalRecommendedInterval_cfunc is None:
            self.niDMM_GetExtCalRecommendedInterval_cfunc = self._cdll.niDMM_GetExtCalRecommendedInterval
            self.niDMM_GetExtCalRecommendedInterval_cfunc.argtypes = [ctypes.c_ulong, ctypes.POINTER(ctypes.c_long)]
            self.niDMM_GetExtCalRecommendedInterval_cfunc.restype = c_long
        return self.niDMM_GetExtCalRecommendedInterval_cfunc(self, vi, months)

    def niDMM_SetCalUserDefinedInfo(self, vi, info):
        if self.niDMM_SetCalUserDefinedInfo_cfunc is None:
            self.niDMM_SetCalUserDefinedInfo_cfunc = self._cdll.niDMM_SetCalUserDefinedInfo
            self.niDMM_SetCalUserDefinedInfo_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_char_p]
            self.niDMM_SetCalUserDefinedInfo_cfunc.restype = c_long
        return self.niDMM_SetCalUserDefinedInfo_cfunc(self, vi, info)

    def niDMM_GetCalUserDefinedInfoMaxSize(self, vi, infoSize):
        if self.niDMM_GetCalUserDefinedInfoMaxSize_cfunc is None:
            self.niDMM_GetCalUserDefinedInfoMaxSize_cfunc = self._cdll.niDMM_GetCalUserDefinedInfoMaxSize
            self.niDMM_GetCalUserDefinedInfoMaxSize_cfunc.argtypes = [ctypes.c_ulong, ctypes.POINTER(ctypes.c_long)]
            self.niDMM_GetCalUserDefinedInfoMaxSize_cfunc.restype = c_long
        return self.niDMM_GetCalUserDefinedInfoMaxSize_cfunc(self, vi, infoSize)

    def niDMM_GetCalUserDefinedInfo(self, vi, bufferSize, info):
        if self.niDMM_GetCalUserDefinedInfo_cfunc is None:
            self.niDMM_GetCalUserDefinedInfo_cfunc = self._cdll.niDMM_GetCalUserDefinedInfo
            self.niDMM_GetCalUserDefinedInfo_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.c_char_p]
            self.niDMM_GetCalUserDefinedInfo_cfunc.restype = c_long
        return self.niDMM_GetCalUserDefinedInfo_cfunc(self, vi, bufferSize, info)

    def niDMM_GetSelfCalSupported(self, vi, selfCalSupported):
        if self.niDMM_GetSelfCalSupported_cfunc is None:
            self.niDMM_GetSelfCalSupported_cfunc = self._cdll.niDMM_GetSelfCalSupported
            self.niDMM_GetSelfCalSupported_cfunc.argtypes = [ctypes.c_ulong, ctypes.POINTER(ctypes.c_ushort)]
            self.niDMM_GetSelfCalSupported_cfunc.restype = c_long
        return self.niDMM_GetSelfCalSupported_cfunc(self, vi, selfCalSupported)

    def niDMM_GetCalDateAndTime(self, vi, calType, month, day, year, hour, minute):
        if self.niDMM_GetCalDateAndTime_cfunc is None:
            self.niDMM_GetCalDateAndTime_cfunc = self._cdll.niDMM_GetCalDateAndTime
            self.niDMM_GetCalDateAndTime_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)]
            self.niDMM_GetCalDateAndTime_cfunc.restype = c_long
        return self.niDMM_GetCalDateAndTime_cfunc(self, vi, calType, month, day, year, hour, minute)

    def niDMM_GetCalCount(self, vi, calType, count):
        if self.niDMM_GetCalCount_cfunc is None:
            self.niDMM_GetCalCount_cfunc = self._cdll.niDMM_GetCalCount
            self.niDMM_GetCalCount_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.POINTER(ctypes.c_long)]
            self.niDMM_GetCalCount_cfunc.restype = c_long
        return self.niDMM_GetCalCount_cfunc(self, vi, calType, count)

    def niDMM_GetLastCalTemp(self, vi, calType, temperature):
        if self.niDMM_GetLastCalTemp_cfunc is None:
            self.niDMM_GetLastCalTemp_cfunc = self._cdll.niDMM_GetLastCalTemp
            self.niDMM_GetLastCalTemp_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.POINTER(ctypes.c_double)]
            self.niDMM_GetLastCalTemp_cfunc.restype = c_long
        return self.niDMM_GetLastCalTemp_cfunc(self, vi, calType, temperature)

    def niDMM_GetDevTemp(self, vi, reserved, temperature):
        if self.niDMM_GetDevTemp_cfunc is None:
            self.niDMM_GetDevTemp_cfunc = self._cdll.niDMM_GetDevTemp
            self.niDMM_GetDevTemp_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
            self.niDMM_GetDevTemp_cfunc.restype = c_long
        return self.niDMM_GetDevTemp_cfunc(self, vi, reserved, temperature)

    def niDMM_ConfigureTransducerType(self, vi, transducerType):
        if self.niDMM_ConfigureTransducerType_cfunc is None:
            self.niDMM_ConfigureTransducerType_cfunc = self._cdll.niDMM_ConfigureTransducerType
            self.niDMM_ConfigureTransducerType_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_long]
            self.niDMM_ConfigureTransducerType_cfunc.restype = c_long
        return self.niDMM_ConfigureTransducerType_cfunc(self, vi, transducerType)

    def niDMM_ConfigureThermocouple(self, vi, thermocoupleType, refJunctionType):
        if self.niDMM_ConfigureThermocouple_cfunc is None:
            self.niDMM_ConfigureThermocouple_cfunc = self._cdll.niDMM_ConfigureThermocouple
            self.niDMM_ConfigureThermocouple_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.c_long]
            self.niDMM_ConfigureThermocouple_cfunc.restype = c_long
        return self.niDMM_ConfigureThermocouple_cfunc(self, vi, thermocoupleType, refJunctionType)

    def niDMM_ConfigureFixedRefJunction(self, vi, fixedRefJunction):
        if self.niDMM_ConfigureFixedRefJunction_cfunc is None:
            self.niDMM_ConfigureFixedRefJunction_cfunc = self._cdll.niDMM_ConfigureFixedRefJunction
            self.niDMM_ConfigureFixedRefJunction_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_double]
            self.niDMM_ConfigureFixedRefJunction_cfunc.restype = c_long
        return self.niDMM_ConfigureFixedRefJunction_cfunc(self, vi, fixedRefJunction)

    def niDMM_ConfigureRTDType(self, vi, rtdType, resistance):
        if self.niDMM_ConfigureRTDType_cfunc is None:
            self.niDMM_ConfigureRTDType_cfunc = self._cdll.niDMM_ConfigureRTDType
            self.niDMM_ConfigureRTDType_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.c_double]
            self.niDMM_ConfigureRTDType_cfunc.restype = c_long
        return self.niDMM_ConfigureRTDType_cfunc(self, vi, rtdType, resistance)

    def niDMM_ConfigureRTDCustom(self, vi, a, b, c):
        if self.niDMM_ConfigureRTDCustom_cfunc is None:
            self.niDMM_ConfigureRTDCustom_cfunc = self._cdll.niDMM_ConfigureRTDCustom
            self.niDMM_ConfigureRTDCustom_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_double, ctypes.c_double, ctypes.c_double]
            self.niDMM_ConfigureRTDCustom_cfunc.restype = c_long
        return self.niDMM_ConfigureRTDCustom_cfunc(self, vi, a, b, c)

    def niDMM_ConfigureThermistorType(self, vi, thermistorType):
        if self.niDMM_ConfigureThermistorType_cfunc is None:
            self.niDMM_ConfigureThermistorType_cfunc = self._cdll.niDMM_ConfigureThermistorType
            self.niDMM_ConfigureThermistorType_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_long]
            self.niDMM_ConfigureThermistorType_cfunc.restype = c_long
        return self.niDMM_ConfigureThermistorType_cfunc(self, vi, thermistorType)

    def niDMM_ConfigureThermistorCustom(self, vi, a, b, c):
        if self.niDMM_ConfigureThermistorCustom_cfunc is None:
            self.niDMM_ConfigureThermistorCustom_cfunc = self._cdll.niDMM_ConfigureThermistorCustom
            self.niDMM_ConfigureThermistorCustom_cfunc.argtypes = [ctypes.c_ulong, ctypes.c_double, ctypes.c_double, ctypes.c_double]
            self.niDMM_ConfigureThermistorCustom_cfunc.restype = c_long
        return self.niDMM_ConfigureThermistorCustom_cfunc(self, vi, a, b, c)


