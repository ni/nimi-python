# This file was generated


import ctypes
from unittest.mock import DEFAULT
import pprint
from ctypes import *
pp = pprint.PrettyPrinter(indent=4)

# Create side effect functions for all entry points that take byref/pointer parameters

def niDMM_init_side_effect(resourceName, IDQuery, reset, newVi):
    newVi.contents.value = 42
    return DEFAULT

def niDMM_InitWithOptions_side_effect(resourceName, IDQuery, resetDevice, optionsString, newVi):
    newVi.contents.value = 42
    return DEFAULT

def niDMM_GetError_side_effect(vi, errorCode, bufferSize, description):
    errorCode.contents.value = -1
    return DEFAULT

def niDMM_self_test_side_effect(vi, selfTestResult, selfTestMessage):
    selfTestResult.contents.value = 42
    return DEFAULT

def niDMM_GetMeasurementPeriod_side_effect(vi, period):
    period.contents.value = 42.2
    return DEFAULT

def niDMM_Read_side_effect(vi, maxTime, reading):
    reading.contents.value = 4.2
    return DEFAULT

def niDMM_Fetch_side_effect(vi, maxTime, reading):
    reading.contents.value = 4.2
    return DEFAULT

def niDMM_IsOverRange_side_effect(vi, measurementValue, isOverRange):
    isOverRange.contents.value = 1
    return DEFAULT

def niDMM_IsUnderRange_side_effect(vi, measurementValue, isUnderRange):
    isUnderRange.contents.value = 1
    return DEFAULT

def niDMM_ReadMultiPoint_side_effect(vi, maxTime, arraySize, readingArray, actualPts):
    actualPts.contents.value = 42
    return DEFAULT

def niDMM_FetchMultiPoint_side_effect(vi, maxTime, arraySize, readingArray, actualPts):
    actualPts.contents.value = 42
    return DEFAULT

def niDMM_GetApertureTimeInfo_side_effect(vi, apertureTime, apertureTimeUnits):
    apertureTime.contents.value = 42.2
    apertureTimeUnits.contents.value = 0
    return DEFAULT

def niDMM_GetAutoRangeValue_side_effect(vi, autoRangeValue):
    autoRangeValue.contents.value = 10
    return DEFAULT

def niDMM_ReadStatus_side_effect(vi, acqBacklog, acqDone):
    acqBacklog.contents.value = 1
    acqDone.contents.value = 1
    return DEFAULT

def niDMM_PerformOpenCableComp_side_effect(vi, conductance, susceptance):
    conductance.contents.value = 400.1
    susceptance.contents.value = 400.2
    return DEFAULT

def niDMM_PerformShortCableComp_side_effect(vi, resistance, reactance):
    resistance.contents.value = 10000
    reactance.contents.value = 10000.1
    return DEFAULT

def niDMM_LockSession_side_effect(vi, callerHasLock):
    callerHasLock.contents.value = 1
    return DEFAULT

def niDMM_UnlockSession_side_effect(vi, callerHasLock):
    callerHasLock.contents.value = 0
    return DEFAULT

def niDMM_FetchWaveform_side_effect(vi, maxTime, arraySize, waveformArray, actualPoints):
    actualPoints.contents.value = 5
    return DEFAULT

def niDMM_ReadWaveform_side_effect(vi, maxTime, arraySize, waveformArray, actualPoints):
    actualPoints.contents.value = 5
    return DEFAULT

def niDMM_GetAttributeViInt32_side_effect(vi, channelName, attributeId, value):
    value.contents.value = 42
    return DEFAULT

def niDMM_GetAttributeViReal64_side_effect(vi, channelName, attributeId, value):
    value.contents.value = 42.2
    return DEFAULT

def niDMM_GetAttributeViSession_side_effect(vi, channelName, attributeId, value):
    value.contents.value = 42
    return DEFAULT

def niDMM_GetAttributeViBoolean_side_effect(vi, channelName, attributeId, value):
    value.contents.value = 1
    return DEFAULT

def niDMM_InitExtCal_side_effect(resourceName, password, newVi):
    newVi.contents.value = 43
    return DEFAULT

def niDMM_GetExtCalRecommendedInterval_side_effect(vi, months):
    months.contents.value = 360
    return DEFAULT

def niDMM_GetCalUserDefinedInfoMaxSize_side_effect(vi, infoSize):
    infoSize.contents.value = 4
    return DEFAULT

def niDMM_GetSelfCalSupported_side_effect(vi, selfCalSupported):
    selfCalSupported.contents.value = 1
    return DEFAULT

def niDMM_GetCalDateAndTime_side_effect(vi, calType, month, day, year, hour, minute):
    month.contents.value = 40
    day.contents.value = 41
    year.contents.value = 42
    hour.contents.value = 43
    minute.contents.value = 44
    return DEFAULT

def niDMM_GetCalCount_side_effect(vi, calType, count):
    count.contents.value = 42
    return DEFAULT

def niDMM_GetLastCalTemp_side_effect(vi, calType, temperature):
    temperature.contents.value = 42.2
    return DEFAULT

def niDMM_GetDevTemp_side_effect(vi, reserved, temperature):
    temperature.contents.value = 41.2
    return DEFAULT

# Helper function to setup Mock object with default side affects and return values
def set_side_effects_and_return_values(mock_library):
    mock_library.niDMM_init.side_effect = niDMM_init_side_effect
    mock_library.niDMM_init.return_value = 0
    mock_library.niDMM_InitWithOptions.side_effect = niDMM_InitWithOptions_side_effect
    mock_library.niDMM_InitWithOptions.return_value = 0
    mock_library.niDMM_close.return_value = 0
    mock_library.niDMM_GetError.side_effect = niDMM_GetError_side_effect
    mock_library.niDMM_GetError.return_value = 0
    mock_library.niDMM_GetErrorMessage.return_value = 0
    mock_library.niDMM_ClearError.return_value = 0
    mock_library.niDMM_reset.return_value = 0
    mock_library.niDMM_self_test.side_effect = niDMM_self_test_side_effect
    mock_library.niDMM_self_test.return_value = 0
    mock_library.niDMM_SelfCal.return_value = 0
    mock_library.niDMM_revision_query.return_value = 0
    mock_library.niDMM_InvalidateAllAttributes.return_value = 0
    mock_library.niDMM_ResetWithDefaults.return_value = 0
    mock_library.niDMM_Disable.return_value = 0
    mock_library.niDMM_GetMeasurementPeriod.side_effect = niDMM_GetMeasurementPeriod_side_effect
    mock_library.niDMM_GetMeasurementPeriod.return_value = 0
    mock_library.niDMM_ConfigureTrigger.return_value = 0
    mock_library.niDMM_Read.side_effect = niDMM_Read_side_effect
    mock_library.niDMM_Read.return_value = 0
    mock_library.niDMM_Fetch.side_effect = niDMM_Fetch_side_effect
    mock_library.niDMM_Fetch.return_value = 0
    mock_library.niDMM_Abort.return_value = 0
    mock_library.niDMM_Initiate.return_value = 0
    mock_library.niDMM_IsOverRange.side_effect = niDMM_IsOverRange_side_effect
    mock_library.niDMM_IsOverRange.return_value = 0
    mock_library.niDMM_IsUnderRange.side_effect = niDMM_IsUnderRange_side_effect
    mock_library.niDMM_IsUnderRange.return_value = 0
    mock_library.niDMM_ConfigureACBandwidth.return_value = 0
    mock_library.niDMM_ConfigureFrequencyVoltageRange.return_value = 0
    mock_library.niDMM_ConfigureMeasCompleteDest.return_value = 0
    mock_library.niDMM_ConfigureMultiPoint.return_value = 0
    mock_library.niDMM_ReadMultiPoint.side_effect = niDMM_ReadMultiPoint_side_effect
    mock_library.niDMM_ReadMultiPoint.return_value = 0
    mock_library.niDMM_FetchMultiPoint.side_effect = niDMM_FetchMultiPoint_side_effect
    mock_library.niDMM_FetchMultiPoint.return_value = 0
    mock_library.niDMM_ConfigureTriggerSlope.return_value = 0
    mock_library.niDMM_SendSoftwareTrigger.return_value = 0
    mock_library.niDMM_GetApertureTimeInfo.side_effect = niDMM_GetApertureTimeInfo_side_effect
    mock_library.niDMM_GetApertureTimeInfo.return_value = 0
    mock_library.niDMM_GetAutoRangeValue.side_effect = niDMM_GetAutoRangeValue_side_effect
    mock_library.niDMM_GetAutoRangeValue.return_value = 0
    mock_library.niDMM_ConfigureAutoZeroMode.return_value = 0
    mock_library.niDMM_ConfigurePowerLineFrequency.return_value = 0
    mock_library.niDMM_ConfigureMeasurementDigits.return_value = 0
    mock_library.niDMM_ConfigureMeasurementAbsolute.return_value = 0
    mock_library.niDMM_ConfigureMeasCompleteSlope.return_value = 0
    mock_library.niDMM_ConfigureSampleTriggerSlope.return_value = 0
    mock_library.niDMM_ReadStatus.side_effect = niDMM_ReadStatus_side_effect
    mock_library.niDMM_ReadStatus.return_value = 0
    mock_library.niDMM_Control.return_value = 0
    mock_library.niDMM_ConfigureADCCalibration.return_value = 0
    mock_library.niDMM_ConfigureOffsetCompOhms.return_value = 0
    mock_library.niDMM_ConfigureCurrentSource.return_value = 0
    mock_library.niDMM_ConfigureCableCompType.return_value = 0
    mock_library.niDMM_PerformOpenCableComp.side_effect = niDMM_PerformOpenCableComp_side_effect
    mock_library.niDMM_PerformOpenCableComp.return_value = 0
    mock_library.niDMM_PerformShortCableComp.side_effect = niDMM_PerformShortCableComp_side_effect
    mock_library.niDMM_PerformShortCableComp.return_value = 0
    mock_library.niDMM_ConfigureOpenCableCompValues.return_value = 0
    mock_library.niDMM_ConfigureShortCableCompValues.return_value = 0
    mock_library.niDMM_LockSession.side_effect = niDMM_LockSession_side_effect
    mock_library.niDMM_LockSession.return_value = 0
    mock_library.niDMM_UnlockSession.side_effect = niDMM_UnlockSession_side_effect
    mock_library.niDMM_UnlockSession.return_value = 0
    mock_library.niDMM_ConfigureWaveformAcquisition.return_value = 0
    mock_library.niDMM_ConfigureWaveformCoupling.return_value = 0
    mock_library.niDMM_FetchWaveform.side_effect = niDMM_FetchWaveform_side_effect
    mock_library.niDMM_FetchWaveform.return_value = 0
    mock_library.niDMM_ReadWaveform.side_effect = niDMM_ReadWaveform_side_effect
    mock_library.niDMM_ReadWaveform.return_value = 0
    mock_library.niDMM_GetAttributeViInt32.side_effect = niDMM_GetAttributeViInt32_side_effect
    mock_library.niDMM_GetAttributeViInt32.return_value = 0
    mock_library.niDMM_SetAttributeViInt32.return_value = 0
    mock_library.niDMM_CheckAttributeViInt32.return_value = 0
    mock_library.niDMM_GetAttributeViReal64.side_effect = niDMM_GetAttributeViReal64_side_effect
    mock_library.niDMM_GetAttributeViReal64.return_value = 0
    mock_library.niDMM_SetAttributeViReal64.return_value = 0
    mock_library.niDMM_CheckAttributeViReal64.return_value = 0
    mock_library.niDMM_GetAttributeViString.return_value = 0
    mock_library.niDMM_SetAttributeViString.return_value = 0
    mock_library.niDMM_CheckAttributeViString.return_value = 0
    mock_library.niDMM_GetAttributeViSession.side_effect = niDMM_GetAttributeViSession_side_effect
    mock_library.niDMM_GetAttributeViSession.return_value = 0
    mock_library.niDMM_SetAttributeViSession.return_value = 0
    mock_library.niDMM_CheckAttributeViSession.return_value = 0
    mock_library.niDMM_GetAttributeViBoolean.side_effect = niDMM_GetAttributeViBoolean_side_effect
    mock_library.niDMM_GetAttributeViBoolean.return_value = 0
    mock_library.niDMM_SetAttributeViBoolean.return_value = 0
    mock_library.niDMM_CheckAttributeViBoolean.return_value = 0
    mock_library.niDMM_GetNextCoercionRecord.return_value = 0
    mock_library.niDMM_GetNextInterchangeWarning.return_value = 0
    mock_library.niDMM_ResetInterchangeCheck.return_value = 0
    mock_library.niDMM_ClearInterchangeWarnings.return_value = 0
    mock_library.niDMM_4022Control.return_value = 0
    mock_library.niDMM_GetChannelName.return_value = 0
    mock_library.niDMM_InitExtCal.side_effect = niDMM_InitExtCal_side_effect
    mock_library.niDMM_InitExtCal.return_value = 0
    mock_library.niDMM_CloseExtCal.return_value = 0
    mock_library.niDMM_CalAdjustLinearization.return_value = 0
    mock_library.niDMM_CalAdjustGain.return_value = 0
    mock_library.niDMM_CalAdjustOffset.return_value = 0
    mock_library.niDMM_CalAdjustMisc.return_value = 0
    mock_library.niDMM_CalAdjustLC.return_value = 0
    mock_library.niDMM_CalAdjustACFilter.return_value = 0
    mock_library.niDMM_RestoreLastExtCalConstants.return_value = 0
    mock_library.niDMM_SetCalPassword.return_value = 0
    mock_library.niDMM_GetExtCalRecommendedInterval.side_effect = niDMM_GetExtCalRecommendedInterval_side_effect
    mock_library.niDMM_GetExtCalRecommendedInterval.return_value = 0
    mock_library.niDMM_SetCalUserDefinedInfo.return_value = 0
    mock_library.niDMM_GetCalUserDefinedInfoMaxSize.side_effect = niDMM_GetCalUserDefinedInfoMaxSize_side_effect
    mock_library.niDMM_GetCalUserDefinedInfoMaxSize.return_value = 0
    mock_library.niDMM_GetCalUserDefinedInfo.return_value = 0
    mock_library.niDMM_GetSelfCalSupported.side_effect = niDMM_GetSelfCalSupported_side_effect
    mock_library.niDMM_GetSelfCalSupported.return_value = 0
    mock_library.niDMM_GetCalDateAndTime.side_effect = niDMM_GetCalDateAndTime_side_effect
    mock_library.niDMM_GetCalDateAndTime.return_value = 0
    mock_library.niDMM_GetCalCount.side_effect = niDMM_GetCalCount_side_effect
    mock_library.niDMM_GetCalCount.return_value = 0
    mock_library.niDMM_GetLastCalTemp.side_effect = niDMM_GetLastCalTemp_side_effect
    mock_library.niDMM_GetLastCalTemp.return_value = 0
    mock_library.niDMM_GetDevTemp.side_effect = niDMM_GetDevTemp_side_effect
    mock_library.niDMM_GetDevTemp.return_value = 0
    mock_library.niDMM_ConfigureTransducerType.return_value = 0
    mock_library.niDMM_ConfigureThermocouple.return_value = 0
    mock_library.niDMM_ConfigureFixedRefJunction.return_value = 0
    mock_library.niDMM_ConfigureRTDType.return_value = 0
    mock_library.niDMM_ConfigureRTDCustom.return_value = 0
    mock_library.niDMM_ConfigureThermistorType.return_value = 0
    mock_library.niDMM_ConfigureThermistorCustom.return_value = 0

# Class with all required entry points - used as a spec when mocking the ctypes.CDLL
#   dynamically created object
class mock_library():
   def niDMM_init(self, resourceName, IDQuery, reset, newVi):
       pass

   def niDMM_InitWithOptions(self, resourceName, IDQuery, resetDevice, optionsString, newVi):
       pass

   def niDMM_close(self, vi):
       pass

   def niDMM_GetError(self, vi, errorCode, bufferSize, description):
       pass

   def niDMM_GetErrorMessage(self, vi, errorCode, bufferSize, errMessage):
       pass

   def niDMM_ClearError(self, vi):
       pass

   def niDMM_reset(self, vi):
       pass

   def niDMM_self_test(self, vi, selfTestResult, selfTestMessage):
       pass

   def niDMM_SelfCal(self, vi):
       pass

   def niDMM_revision_query(self, vi, driverRev, instrRev):
       pass

   def niDMM_InvalidateAllAttributes(self, vi):
       pass

   def niDMM_ResetWithDefaults(self, vi):
       pass

   def niDMM_Disable(self, vi):
       pass

   def niDMM_GetMeasurementPeriod(self, vi, period):
       pass

   def niDMM_ConfigureTrigger(self, vi, trigSource, triggerDelay):
       pass

   def niDMM_Read(self, vi, maxTime, reading):
       pass

   def niDMM_Fetch(self, vi, maxTime, reading):
       pass

   def niDMM_Abort(self, vi):
       pass

   def niDMM_Initiate(self, vi):
       pass

   def niDMM_IsOverRange(self, vi, measurementValue, isOverRange):
       pass

   def niDMM_IsUnderRange(self, vi, measurementValue, isUnderRange):
       pass

   def niDMM_ConfigureACBandwidth(self, vi, minFreq, maxFreq):
       pass

   def niDMM_ConfigureFrequencyVoltageRange(self, vi, frequencyVoltageRange):
       pass

   def niDMM_ConfigureMeasCompleteDest(self, vi, destination):
       pass

   def niDMM_ConfigureMultiPoint(self, vi, triggerCount, sampleCount, sampleTrigger, sampleInterval):
       pass

   def niDMM_ReadMultiPoint(self, vi, maxTime, arraySize, readingArray, actualPts):
       pass

   def niDMM_FetchMultiPoint(self, vi, maxTime, arraySize, readingArray, actualPts):
       pass

   def niDMM_ConfigureTriggerSlope(self, vi, polarity):
       pass

   def niDMM_SendSoftwareTrigger(self, vi):
       pass

   def niDMM_GetApertureTimeInfo(self, vi, apertureTime, apertureTimeUnits):
       pass

   def niDMM_GetAutoRangeValue(self, vi, autoRangeValue):
       pass

   def niDMM_ConfigureAutoZeroMode(self, vi, autoZeroMode):
       pass

   def niDMM_ConfigurePowerLineFrequency(self, vi, frequency):
       pass

   def niDMM_ConfigureMeasurementDigits(self, vi, measFunction, range, resolutionDigits):
       pass

   def niDMM_ConfigureMeasurementAbsolute(self, vi, measFunction, range, resolutionAbsolute):
       pass

   def niDMM_ConfigureMeasCompleteSlope(self, vi, polarity):
       pass

   def niDMM_ConfigureSampleTriggerSlope(self, vi, polarity):
       pass

   def niDMM_ReadStatus(self, vi, acqBacklog, acqDone):
       pass

   def niDMM_Control(self, vi, action):
       pass

   def niDMM_ConfigureADCCalibration(self, vi, adcGainComp):
       pass

   def niDMM_ConfigureOffsetCompOhms(self, vi, offsetCompOhms):
       pass

   def niDMM_ConfigureCurrentSource(self, vi, diodeCurrentSrc):
       pass

   def niDMM_ConfigureCableCompType(self, vi, typeOfCompensation):
       pass

   def niDMM_PerformOpenCableComp(self, vi, conductance, susceptance):
       pass

   def niDMM_PerformShortCableComp(self, vi, resistance, reactance):
       pass

   def niDMM_ConfigureOpenCableCompValues(self, vi, conductance, susceptance):
       pass

   def niDMM_ConfigureShortCableCompValues(self, vi, resistance, reactance):
       pass

   def niDMM_LockSession(self, vi, callerHasLock):
       pass

   def niDMM_UnlockSession(self, vi, callerHasLock):
       pass

   def niDMM_ConfigureWaveformAcquisition(self, vi, function, range, rate, waveformPoints):
       pass

   def niDMM_ConfigureWaveformCoupling(self, vi, coupling):
       pass

   def niDMM_FetchWaveform(self, vi, maxTime, arraySize, waveformArray, actualPoints):
       pass

   def niDMM_ReadWaveform(self, vi, maxTime, arraySize, waveformArray, actualPoints):
       pass

   def niDMM_GetAttributeViInt32(self, vi, channelName, attributeId, value):
       pass

   def niDMM_SetAttributeViInt32(self, vi, channelName, attributeId, value):
       pass

   def niDMM_CheckAttributeViInt32(self, vi, channelName, attributeId, value):
       pass

   def niDMM_GetAttributeViReal64(self, vi, channelName, attributeId, value):
       pass

   def niDMM_SetAttributeViReal64(self, vi, channelName, attributeId, value):
       pass

   def niDMM_CheckAttributeViReal64(self, vi, channelName, attributeId, value):
       pass

   def niDMM_GetAttributeViString(self, vi, channelName, attributeId, bufSize, value):
       pass

   def niDMM_SetAttributeViString(self, vi, channelName, attributeId, value):
       pass

   def niDMM_CheckAttributeViString(self, vi, channelName, attributeId, value):
       pass

   def niDMM_GetAttributeViSession(self, vi, channelName, attributeId, value):
       pass

   def niDMM_SetAttributeViSession(self, vi, channelName, attributeId, value):
       pass

   def niDMM_CheckAttributeViSession(self, vi, channelName, attributeId, value):
       pass

   def niDMM_GetAttributeViBoolean(self, vi, channelName, attributeId, value):
       pass

   def niDMM_SetAttributeViBoolean(self, vi, channelName, attributeId, value):
       pass

   def niDMM_CheckAttributeViBoolean(self, vi, channelName, attributeId, value):
       pass

   def niDMM_GetNextCoercionRecord(self, vi, bufferSize, record):
       pass

   def niDMM_GetNextInterchangeWarning(self, vi, bufferSize, warnString):
       pass

   def niDMM_ResetInterchangeCheck(self, vi):
       pass

   def niDMM_ClearInterchangeWarnings(self, vi):
       pass

   def niDMM_4022Control(self, resourceName, configuration):
       pass

   def niDMM_GetChannelName(self, vi, index, bufferSize, name):
       pass

   def niDMM_InitExtCal(self, resourceName, password, newVi):
       pass

   def niDMM_CloseExtCal(self, vi, action):
       pass

   def niDMM_CalAdjustLinearization(self, vi, mode, range, inputR, expectedValue):
       pass

   def niDMM_CalAdjustGain(self, vi, mode, range, inputR, expectedValue):
       pass

   def niDMM_CalAdjustOffset(self, vi, mode, range, inputR):
       pass

   def niDMM_CalAdjustMisc(self, vi, type):
       pass

   def niDMM_CalAdjustLC(self, vi, type):
       pass

   def niDMM_CalAdjustACFilter(self, vi, mode, range, frequency, expectedValue):
       pass

   def niDMM_RestoreLastExtCalConstants(self, vi):
       pass

   def niDMM_SetCalPassword(self, vi, oldPassword, newPassword):
       pass

   def niDMM_GetExtCalRecommendedInterval(self, vi, months):
       pass

   def niDMM_SetCalUserDefinedInfo(self, vi, info):
       pass

   def niDMM_GetCalUserDefinedInfoMaxSize(self, vi, infoSize):
       pass

   def niDMM_GetCalUserDefinedInfo(self, vi, bufferSize, info):
       pass

   def niDMM_GetSelfCalSupported(self, vi, selfCalSupported):
       pass

   def niDMM_GetCalDateAndTime(self, vi, calType, month, day, year, hour, minute):
       pass

   def niDMM_GetCalCount(self, vi, calType, count):
       pass

   def niDMM_GetLastCalTemp(self, vi, calType, temperature):
       pass

   def niDMM_GetDevTemp(self, vi, reserved, temperature):
       pass

   def niDMM_ConfigureTransducerType(self, vi, transducerType):
       pass

   def niDMM_ConfigureThermocouple(self, vi, thermocoupleType, refJunctionType):
       pass

   def niDMM_ConfigureFixedRefJunction(self, vi, fixedRefJunction):
       pass

   def niDMM_ConfigureRTDType(self, vi, rtdType, resistance):
       pass

   def niDMM_ConfigureRTDCustom(self, vi, a, b, c):
       pass

   def niDMM_ConfigureThermistorType(self, vi, thermistorType):
       pass

   def niDMM_ConfigureThermistorCustom(self, vi, a, b, c):
       pass





