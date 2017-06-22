#!/usr/bin/python
# This file was generated


import ctypes
from nidmm import errors
import platform


def get_library_name():
    try:
        return {'Windows': {'32bit': 'nidmm_32.dll', '64bit': 'nidmm_64.dll'}, 'Linux': {'64bit': 'libnidmm.so'}}[platform.system()][platform.architecture()[0]]
    except KeyError as e:
        raise errors.UnsupportedConfigurationError


def get_library():
    try:
        library = ctypes.CDLL(get_library_name())
    except OSError as e:
        raise errors.DriverNotInstalledError()


    """ Specify required argument types (function prototypes) and Return types.
        https://docs.python.org/3/library/ctypes.html#specifying-the-required-argument-types-function-prototypes
        https://docs.python.org/3/library/ctypes.html#return-types
        This provides some automatic conversion and error checking when calling NI-DMM functions.
        Strictly speaking, this is not necessary if/when we code-generate the calling code.
        It may have some performance impact as well.
    """

    library.niDMM_init.restype = ctypes.c_long
    library.niDMM_init.argtypes = [ctypes.c_char_p, ctypes.c_ushort, ctypes.c_ushort, ctypes.POINTER(ctypes.c_ulong)]

    library.niDMM_InitWithOptions.restype = ctypes.c_long
    library.niDMM_InitWithOptions.argtypes = [ctypes.c_char_p, ctypes.c_ushort, ctypes.c_ushort, ctypes.c_char_p, ctypes.POINTER(ctypes.c_ulong)]

    library.niDMM_close.restype = ctypes.c_long
    library.niDMM_close.argtypes = [ctypes.c_ulong]

    library.niDMM_GetError.restype = ctypes.c_long
    library.niDMM_GetError.argtypes = [ctypes.c_ulong, ctypes.POINTER(ctypes.c_long), ctypes.c_long, ctypes.c_char_p]

    library.niDMM_GetErrorMessage.restype = ctypes.c_long
    library.niDMM_GetErrorMessage.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.c_long, ctypes.c_char_p]

    library.niDMM_ClearError.restype = ctypes.c_long
    library.niDMM_ClearError.argtypes = [ctypes.c_ulong]

    library.niDMM_reset.restype = ctypes.c_long
    library.niDMM_reset.argtypes = [ctypes.c_ulong]

    library.niDMM_self_test.restype = ctypes.c_long
    library.niDMM_self_test.argtypes = [ctypes.c_ulong, ctypes.POINTER(ctypes.c_short), ctypes.c_char_p]

    library.niDMM_SelfCal.restype = ctypes.c_long
    library.niDMM_SelfCal.argtypes = [ctypes.c_ulong]

    library.niDMM_revision_query.restype = ctypes.c_long
    library.niDMM_revision_query.argtypes = [ctypes.c_ulong, ctypes.c_char_p, ctypes.c_char_p]

    library.niDMM_InvalidateAllAttributes.restype = ctypes.c_long
    library.niDMM_InvalidateAllAttributes.argtypes = [ctypes.c_ulong]

    library.niDMM_ResetWithDefaults.restype = ctypes.c_long
    library.niDMM_ResetWithDefaults.argtypes = [ctypes.c_ulong]

    library.niDMM_Disable.restype = ctypes.c_long
    library.niDMM_Disable.argtypes = [ctypes.c_ulong]

    library.niDMM_GetMeasurementPeriod.restype = ctypes.c_long
    library.niDMM_GetMeasurementPeriod.argtypes = [ctypes.c_ulong, ctypes.POINTER(ctypes.c_double)]

    library.niDMM_ConfigureTrigger.restype = ctypes.c_long
    library.niDMM_ConfigureTrigger.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.c_double]

    library.niDMM_Read.restype = ctypes.c_long
    library.niDMM_Read.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.POINTER(ctypes.c_double)]

    library.niDMM_Fetch.restype = ctypes.c_long
    library.niDMM_Fetch.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.POINTER(ctypes.c_double)]

    library.niDMM_Abort.restype = ctypes.c_long
    library.niDMM_Abort.argtypes = [ctypes.c_ulong]

    library.niDMM_Initiate.restype = ctypes.c_long
    library.niDMM_Initiate.argtypes = [ctypes.c_ulong]

    library.niDMM_IsOverRange.restype = ctypes.c_long
    library.niDMM_IsOverRange.argtypes = [ctypes.c_ulong, ctypes.c_double, ctypes.POINTER(ctypes.c_ushort)]

    library.niDMM_IsUnderRange.restype = ctypes.c_long
    library.niDMM_IsUnderRange.argtypes = [ctypes.c_ulong, ctypes.c_double, ctypes.POINTER(ctypes.c_ushort)]

    library.niDMM_ConfigureACBandwidth.restype = ctypes.c_long
    library.niDMM_ConfigureACBandwidth.argtypes = [ctypes.c_ulong, ctypes.c_double, ctypes.c_double]

    library.niDMM_ConfigureFrequencyVoltageRange.restype = ctypes.c_long
    library.niDMM_ConfigureFrequencyVoltageRange.argtypes = [ctypes.c_ulong, ctypes.c_double]

    library.niDMM_ConfigureMeasCompleteDest.restype = ctypes.c_long
    library.niDMM_ConfigureMeasCompleteDest.argtypes = [ctypes.c_ulong, ctypes.c_long]

    library.niDMM_ConfigureMultiPoint.restype = ctypes.c_long
    library.niDMM_ConfigureMultiPoint.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_double]

    library.niDMM_ReadMultiPoint.restype = ctypes.c_long
    library.niDMM_ReadMultiPoint.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.c_long, ctypes.c_double, ctypes.POINTER(ctypes.c_long)]

    library.niDMM_FetchMultiPoint.restype = ctypes.c_long
    library.niDMM_FetchMultiPoint.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.c_long, ctypes.c_double, ctypes.POINTER(ctypes.c_long)]

    library.niDMM_ConfigureTriggerSlope.restype = ctypes.c_long
    library.niDMM_ConfigureTriggerSlope.argtypes = [ctypes.c_ulong, ctypes.c_long]

    library.niDMM_SendSoftwareTrigger.restype = ctypes.c_long
    library.niDMM_SendSoftwareTrigger.argtypes = [ctypes.c_ulong]

    library.niDMM_GetApertureTimeInfo.restype = ctypes.c_long
    library.niDMM_GetApertureTimeInfo.argtypes = [ctypes.c_ulong, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_long)]

    library.niDMM_GetAutoRangeValue.restype = ctypes.c_long
    library.niDMM_GetAutoRangeValue.argtypes = [ctypes.c_ulong, ctypes.POINTER(ctypes.c_double)]

    library.niDMM_ConfigureAutoZeroMode.restype = ctypes.c_long
    library.niDMM_ConfigureAutoZeroMode.argtypes = [ctypes.c_ulong, ctypes.c_long]

    library.niDMM_ConfigurePowerLineFrequency.restype = ctypes.c_long
    library.niDMM_ConfigurePowerLineFrequency.argtypes = [ctypes.c_ulong, ctypes.c_double]

    library.niDMM_ConfigureMeasurementDigits.restype = ctypes.c_long
    library.niDMM_ConfigureMeasurementDigits.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.c_double, ctypes.c_double]

    library.niDMM_ConfigureMeasurementAbsolute.restype = ctypes.c_long
    library.niDMM_ConfigureMeasurementAbsolute.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.c_double, ctypes.c_double]

    library.niDMM_ConfigureMeasCompleteSlope.restype = ctypes.c_long
    library.niDMM_ConfigureMeasCompleteSlope.argtypes = [ctypes.c_ulong, ctypes.c_long]

    library.niDMM_ConfigureSampleTriggerSlope.restype = ctypes.c_long
    library.niDMM_ConfigureSampleTriggerSlope.argtypes = [ctypes.c_ulong, ctypes.c_long]

    library.niDMM_ReadStatus.restype = ctypes.c_long
    library.niDMM_ReadStatus.argtypes = [ctypes.c_ulong, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_short)]

    library.niDMM_Control.restype = ctypes.c_long
    library.niDMM_Control.argtypes = [ctypes.c_ulong, ctypes.c_long]

    library.niDMM_ConfigureADCCalibration.restype = ctypes.c_long
    library.niDMM_ConfigureADCCalibration.argtypes = [ctypes.c_ulong, ctypes.c_long]

    library.niDMM_ConfigureOffsetCompOhms.restype = ctypes.c_long
    library.niDMM_ConfigureOffsetCompOhms.argtypes = [ctypes.c_ulong, ctypes.c_long]

    library.niDMM_ConfigureCurrentSource.restype = ctypes.c_long
    library.niDMM_ConfigureCurrentSource.argtypes = [ctypes.c_ulong, ctypes.c_double]

    library.niDMM_ConfigureCableCompType.restype = ctypes.c_long
    library.niDMM_ConfigureCableCompType.argtypes = [ctypes.c_ulong, ctypes.c_long]

    library.niDMM_PerformOpenCableComp.restype = ctypes.c_long
    library.niDMM_PerformOpenCableComp.argtypes = [ctypes.c_ulong, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]

    library.niDMM_PerformShortCableComp.restype = ctypes.c_long
    library.niDMM_PerformShortCableComp.argtypes = [ctypes.c_ulong, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]

    library.niDMM_ConfigureOpenCableCompValues.restype = ctypes.c_long
    library.niDMM_ConfigureOpenCableCompValues.argtypes = [ctypes.c_ulong, ctypes.c_double, ctypes.c_double]

    library.niDMM_ConfigureShortCableCompValues.restype = ctypes.c_long
    library.niDMM_ConfigureShortCableCompValues.argtypes = [ctypes.c_ulong, ctypes.c_double, ctypes.c_double]

    library.niDMM_LockSession.restype = ctypes.c_long
    library.niDMM_LockSession.argtypes = [ctypes.c_ulong, ctypes.POINTER(ctypes.c_ushort)]

    library.niDMM_UnlockSession.restype = ctypes.c_long
    library.niDMM_UnlockSession.argtypes = [ctypes.c_ulong, ctypes.POINTER(ctypes.c_ushort)]

    library.niDMM_ConfigureWaveformAcquisition.restype = ctypes.c_long
    library.niDMM_ConfigureWaveformAcquisition.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.c_double, ctypes.c_double, ctypes.c_long]

    library.niDMM_ConfigureWaveformCoupling.restype = ctypes.c_long
    library.niDMM_ConfigureWaveformCoupling.argtypes = [ctypes.c_ulong, ctypes.c_long]

    library.niDMM_FetchWaveform.restype = ctypes.c_long
    library.niDMM_FetchWaveform.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.c_long, ctypes.c_double, ctypes.POINTER(ctypes.c_long)]

    library.niDMM_ReadWaveform.restype = ctypes.c_long
    library.niDMM_ReadWaveform.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.c_long, ctypes.c_double, ctypes.POINTER(ctypes.c_long)]

    library.niDMM_GetAttributeViInt32.restype = ctypes.c_long
    library.niDMM_GetAttributeViInt32.argtypes = [ctypes.c_ulong, ctypes.c_char_p, ctypes.c_long, ctypes.POINTER(ctypes.c_long)]

    library.niDMM_SetAttributeViInt32.restype = ctypes.c_long
    library.niDMM_SetAttributeViInt32.argtypes = [ctypes.c_ulong, ctypes.c_char_p, ctypes.c_long, ctypes.c_long]

    library.niDMM_CheckAttributeViInt32.restype = ctypes.c_long
    library.niDMM_CheckAttributeViInt32.argtypes = [ctypes.c_ulong, ctypes.c_char_p, ctypes.c_long, ctypes.c_long]

    library.niDMM_GetAttributeViReal64.restype = ctypes.c_long
    library.niDMM_GetAttributeViReal64.argtypes = [ctypes.c_ulong, ctypes.c_char_p, ctypes.c_long, ctypes.POINTER(ctypes.c_double)]

    library.niDMM_SetAttributeViReal64.restype = ctypes.c_long
    library.niDMM_SetAttributeViReal64.argtypes = [ctypes.c_ulong, ctypes.c_char_p, ctypes.c_long, ctypes.c_double]

    library.niDMM_CheckAttributeViReal64.restype = ctypes.c_long
    library.niDMM_CheckAttributeViReal64.argtypes = [ctypes.c_ulong, ctypes.c_char_p, ctypes.c_long, ctypes.c_double]

    library.niDMM_GetAttributeViString.restype = ctypes.c_long
    library.niDMM_GetAttributeViString.argtypes = [ctypes.c_ulong, ctypes.c_char_p, ctypes.c_long, ctypes.c_long, ctypes.c_char_p]

    library.niDMM_SetAttributeViString.restype = ctypes.c_long
    library.niDMM_SetAttributeViString.argtypes = [ctypes.c_ulong, ctypes.c_char_p, ctypes.c_long, ctypes.c_char_p]

    library.niDMM_CheckAttributeViString.restype = ctypes.c_long
    library.niDMM_CheckAttributeViString.argtypes = [ctypes.c_ulong, ctypes.c_char_p, ctypes.c_long, ctypes.c_char_p]

    library.niDMM_GetAttributeViSession.restype = ctypes.c_long
    library.niDMM_GetAttributeViSession.argtypes = [ctypes.c_ulong, ctypes.c_char_p, ctypes.c_long, ctypes.POINTER(ctypes.c_ulong)]

    library.niDMM_SetAttributeViSession.restype = ctypes.c_long
    library.niDMM_SetAttributeViSession.argtypes = [ctypes.c_ulong, ctypes.c_char_p, ctypes.c_long, ctypes.c_ulong]

    library.niDMM_CheckAttributeViSession.restype = ctypes.c_long
    library.niDMM_CheckAttributeViSession.argtypes = [ctypes.c_ulong, ctypes.c_char_p, ctypes.c_long, ctypes.c_ulong]

    library.niDMM_GetAttributeViBoolean.restype = ctypes.c_long
    library.niDMM_GetAttributeViBoolean.argtypes = [ctypes.c_ulong, ctypes.c_char_p, ctypes.c_long, ctypes.POINTER(ctypes.c_ushort)]

    library.niDMM_SetAttributeViBoolean.restype = ctypes.c_long
    library.niDMM_SetAttributeViBoolean.argtypes = [ctypes.c_ulong, ctypes.c_char_p, ctypes.c_long, ctypes.c_ushort]

    library.niDMM_CheckAttributeViBoolean.restype = ctypes.c_long
    library.niDMM_CheckAttributeViBoolean.argtypes = [ctypes.c_ulong, ctypes.c_char_p, ctypes.c_long, ctypes.c_ushort]

    library.niDMM_GetNextCoercionRecord.restype = ctypes.c_long
    library.niDMM_GetNextCoercionRecord.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.c_char_p]

    library.niDMM_GetNextInterchangeWarning.restype = ctypes.c_long
    library.niDMM_GetNextInterchangeWarning.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.c_char_p]

    library.niDMM_ResetInterchangeCheck.restype = ctypes.c_long
    library.niDMM_ResetInterchangeCheck.argtypes = [ctypes.c_ulong]

    library.niDMM_ClearInterchangeWarnings.restype = ctypes.c_long
    library.niDMM_ClearInterchangeWarnings.argtypes = [ctypes.c_ulong]

    library.niDMM_4022Control.restype = ctypes.c_long
    library.niDMM_4022Control.argtypes = [ctypes.c_char_p, ctypes.c_long]

    library.niDMM_GetChannelName.restype = ctypes.c_long
    library.niDMM_GetChannelName.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.c_long, ctypes.c_char_p]

    library.niDMM_InitExtCal.restype = ctypes.c_long
    library.niDMM_InitExtCal.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_ulong)]

    library.niDMM_CloseExtCal.restype = ctypes.c_long
    library.niDMM_CloseExtCal.argtypes = [ctypes.c_ulong, ctypes.c_long]

    library.niDMM_CalAdjustLinearization.restype = ctypes.c_long
    library.niDMM_CalAdjustLinearization.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.c_double, ctypes.c_double, ctypes.c_double]

    library.niDMM_CalAdjustGain.restype = ctypes.c_long
    library.niDMM_CalAdjustGain.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.c_double, ctypes.c_double, ctypes.c_double]

    library.niDMM_CalAdjustOffset.restype = ctypes.c_long
    library.niDMM_CalAdjustOffset.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.c_double, ctypes.c_double]

    library.niDMM_CalAdjustMisc.restype = ctypes.c_long
    library.niDMM_CalAdjustMisc.argtypes = [ctypes.c_ulong, ctypes.c_long]

    library.niDMM_CalAdjustLC.restype = ctypes.c_long
    library.niDMM_CalAdjustLC.argtypes = [ctypes.c_ulong, ctypes.c_long]

    library.niDMM_CalAdjustACFilter.restype = ctypes.c_long
    library.niDMM_CalAdjustACFilter.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.c_double, ctypes.c_double, ctypes.c_double]

    library.niDMM_RestoreLastExtCalConstants.restype = ctypes.c_long
    library.niDMM_RestoreLastExtCalConstants.argtypes = [ctypes.c_ulong]

    library.niDMM_SetCalPassword.restype = ctypes.c_long
    library.niDMM_SetCalPassword.argtypes = [ctypes.c_ulong, ctypes.c_char_p, ctypes.c_char_p]

    library.niDMM_GetExtCalRecommendedInterval.restype = ctypes.c_long
    library.niDMM_GetExtCalRecommendedInterval.argtypes = [ctypes.c_ulong, ctypes.POINTER(ctypes.c_long)]

    library.niDMM_SetCalUserDefinedInfo.restype = ctypes.c_long
    library.niDMM_SetCalUserDefinedInfo.argtypes = [ctypes.c_ulong, ctypes.c_char_p]

    library.niDMM_GetCalUserDefinedInfoMaxSize.restype = ctypes.c_long
    library.niDMM_GetCalUserDefinedInfoMaxSize.argtypes = [ctypes.c_ulong, ctypes.POINTER(ctypes.c_long)]

    library.niDMM_GetCalUserDefinedInfo.restype = ctypes.c_long
    library.niDMM_GetCalUserDefinedInfo.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.c_char_p]

    library.niDMM_GetSelfCalSupported.restype = ctypes.c_long
    library.niDMM_GetSelfCalSupported.argtypes = [ctypes.c_ulong, ctypes.POINTER(ctypes.c_ushort)]

    library.niDMM_GetCalDateAndTime.restype = ctypes.c_long
    library.niDMM_GetCalDateAndTime.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)]

    library.niDMM_GetCalCount.restype = ctypes.c_long
    library.niDMM_GetCalCount.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.POINTER(ctypes.c_long)]

    library.niDMM_GetLastCalTemp.restype = ctypes.c_long
    library.niDMM_GetLastCalTemp.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.POINTER(ctypes.c_double)]

    library.niDMM_GetDevTemp.restype = ctypes.c_long
    library.niDMM_GetDevTemp.argtypes = [ctypes.c_ulong, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]

    library.niDMM_ConfigureTransducerType.restype = ctypes.c_long
    library.niDMM_ConfigureTransducerType.argtypes = [ctypes.c_ulong, ctypes.c_long]

    library.niDMM_ConfigureThermocouple.restype = ctypes.c_long
    library.niDMM_ConfigureThermocouple.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.c_long]

    library.niDMM_ConfigureFixedRefJunction.restype = ctypes.c_long
    library.niDMM_ConfigureFixedRefJunction.argtypes = [ctypes.c_ulong, ctypes.c_double]

    library.niDMM_ConfigureRTDType.restype = ctypes.c_long
    library.niDMM_ConfigureRTDType.argtypes = [ctypes.c_ulong, ctypes.c_long, ctypes.c_double]

    library.niDMM_ConfigureRTDCustom.restype = ctypes.c_long
    library.niDMM_ConfigureRTDCustom.argtypes = [ctypes.c_ulong, ctypes.c_double, ctypes.c_double, ctypes.c_double]

    library.niDMM_ConfigureThermistorType.restype = ctypes.c_long
    library.niDMM_ConfigureThermistorType.argtypes = [ctypes.c_ulong, ctypes.c_long]

    library.niDMM_ConfigureThermistorCustom.restype = ctypes.c_long
    library.niDMM_ConfigureThermistorCustom.argtypes = [ctypes.c_ulong, ctypes.c_double, ctypes.c_double, ctypes.c_double]

    return library
