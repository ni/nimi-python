# This file was generated

# Python ctypes wrapper around driver DLL.
# ctypes is a library to manage calling into C/C++ DLLs. It will ensure the correct
#  number and types of parameters are passed into the different entry points

import ctypes

from nidmm.ctypes_types import *  # noqa: F403,H303
import nidmm.python_types


class NidmmCtypesLibrary(object):
    def __init__(self, library_name, library_type):
        # We cache the cfunc object from the ctypes.CDLL object
        self.niDMM_Abort_cfunc = None
        self.niDMM_CalAdjustACFilter_cfunc = None
        self.niDMM_CalAdjustGain_cfunc = None
        self.niDMM_CalAdjustLC_cfunc = None
        self.niDMM_CalAdjustLinearization_cfunc = None
        self.niDMM_CalAdjustMisc_cfunc = None
        self.niDMM_CalAdjustOffset_cfunc = None
        self.niDMM_CheckAttributeViBoolean_cfunc = None
        self.niDMM_CheckAttributeViInt32_cfunc = None
        self.niDMM_CheckAttributeViReal64_cfunc = None
        self.niDMM_CheckAttributeViSession_cfunc = None
        self.niDMM_CheckAttributeViString_cfunc = None
        self.niDMM_ClearError_cfunc = None
        self.niDMM_ClearInterchangeWarnings_cfunc = None
        self.niDMM_CloseExtCal_cfunc = None
        self.niDMM_ConfigureACBandwidth_cfunc = None
        self.niDMM_ConfigureADCCalibration_cfunc = None
        self.niDMM_ConfigureAutoZeroMode_cfunc = None
        self.niDMM_ConfigureCableCompType_cfunc = None
        self.niDMM_ConfigureCurrentSource_cfunc = None
        self.niDMM_ConfigureFixedRefJunction_cfunc = None
        self.niDMM_ConfigureFrequencyVoltageRange_cfunc = None
        self.niDMM_ConfigureMeasCompleteDest_cfunc = None
        self.niDMM_ConfigureMeasCompleteSlope_cfunc = None
        self.niDMM_ConfigureMeasurementAbsolute_cfunc = None
        self.niDMM_ConfigureMeasurementDigits_cfunc = None
        self.niDMM_ConfigureMultiPoint_cfunc = None
        self.niDMM_ConfigureOffsetCompOhms_cfunc = None
        self.niDMM_ConfigureOpenCableCompValues_cfunc = None
        self.niDMM_ConfigurePowerLineFrequency_cfunc = None
        self.niDMM_ConfigureRTDCustom_cfunc = None
        self.niDMM_ConfigureRTDType_cfunc = None
        self.niDMM_ConfigureSampleTriggerSlope_cfunc = None
        self.niDMM_ConfigureShortCableCompValues_cfunc = None
        self.niDMM_ConfigureThermistorCustom_cfunc = None
        self.niDMM_ConfigureThermistorType_cfunc = None
        self.niDMM_ConfigureThermocouple_cfunc = None
        self.niDMM_ConfigureTransducerType_cfunc = None
        self.niDMM_ConfigureTrigger_cfunc = None
        self.niDMM_ConfigureTriggerSlope_cfunc = None
        self.niDMM_ConfigureWaveformAcquisition_cfunc = None
        self.niDMM_ConfigureWaveformCoupling_cfunc = None
        self.niDMM_Control_cfunc = None
        self.niDMM_Disable_cfunc = None
        self.niDMM_Fetch_cfunc = None
        self.niDMM_FetchMultiPoint_cfunc = None
        self.niDMM_FetchWaveform_cfunc = None
        self.niDMM_FormatMeasAbsolute_cfunc = None
        self.niDMM_GetApertureTimeInfo_cfunc = None
        self.niDMM_GetAttributeViBoolean_cfunc = None
        self.niDMM_GetAttributeViInt32_cfunc = None
        self.niDMM_GetAttributeViReal64_cfunc = None
        self.niDMM_GetAttributeViSession_cfunc = None
        self.niDMM_GetAttributeViString_cfunc = None
        self.niDMM_GetAutoRangeValue_cfunc = None
        self.niDMM_GetCalCount_cfunc = None
        self.niDMM_GetCalDateAndTime_cfunc = None
        self.niDMM_GetCalUserDefinedInfo_cfunc = None
        self.niDMM_GetCalUserDefinedInfoMaxSize_cfunc = None
        self.niDMM_GetChannelName_cfunc = None
        self.niDMM_GetDevTemp_cfunc = None
        self.niDMM_GetError_cfunc = None
        self.niDMM_GetErrorMessage_cfunc = None
        self.niDMM_GetExtCalRecommendedInterval_cfunc = None
        self.niDMM_GetLastCalTemp_cfunc = None
        self.niDMM_GetMeasurementPeriod_cfunc = None
        self.niDMM_GetNextCoercionRecord_cfunc = None
        self.niDMM_GetNextInterchangeWarning_cfunc = None
        self.niDMM_GetSelfCalSupported_cfunc = None
        self.niDMM_InitExtCal_cfunc = None
        self.niDMM_InitWithOptions_cfunc = None
        self.niDMM_Initiate_cfunc = None
        self.niDMM_IsOverRange_cfunc = None
        self.niDMM_IsUnderRange_cfunc = None
        self.niDMM_LockSession_cfunc = None
        self.niDMM_PerformOpenCableComp_cfunc = None
        self.niDMM_PerformShortCableComp_cfunc = None
        self.niDMM_Read_cfunc = None
        self.niDMM_ReadMultiPoint_cfunc = None
        self.niDMM_ReadStatus_cfunc = None
        self.niDMM_ReadWaveform_cfunc = None
        self.niDMM_ResetInterchangeCheck_cfunc = None
        self.niDMM_ResetWithDefaults_cfunc = None
        self.niDMM_RestoreLastExtCalConstants_cfunc = None
        self.niDMM_SelfCal_cfunc = None
        self.niDMM_SendSoftwareTrigger_cfunc = None
        self.niDMM_SetAttributeViBoolean_cfunc = None
        self.niDMM_SetAttributeViInt32_cfunc = None
        self.niDMM_SetAttributeViReal64_cfunc = None
        self.niDMM_SetAttributeViSession_cfunc = None
        self.niDMM_SetAttributeViString_cfunc = None
        self.niDMM_SetCalPassword_cfunc = None
        self.niDMM_SetCalUserDefinedInfo_cfunc = None
        self.niDMM_UnlockSession_cfunc = None
        self.niDMM_close_cfunc = None
        self.niDMM_error_message_cfunc = None
        self.niDMM_error_query_cfunc = None
        self.niDMM_init_cfunc = None
        self.niDMM_reset_cfunc = None
        self.niDMM_revision_query_cfunc = None
        self.niDMM_self_test_cfunc = None

        if library_type == 'windll':
            self._library = ctypes.WinDLL(library_name)
        else:
            assert library_type == 'cdll'
            self._library = ctypes.CDLL(library_name)

    def niDMM_Abort(self, vi):  # noqa: N802
        if self.Abort_cfunc is None:
            self.Abort_cfunc = self._library.Abort
            self.Abort_cfunc.argtypes = [ViSession_ctype]  # noqa: F405
            self.Abort_cfunc.restype = nidmm.python_types.ViStatus
        return self.Abort_cfunc(vi)

    def niDMM_CalAdjustACFilter(self, vi, mode, range, frequency, expected_value):  # noqa: N802
        if self.CalAdjustACFilter_cfunc is None:
            self.CalAdjustACFilter_cfunc = self._library.CalAdjustACFilter
            self.CalAdjustACFilter_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViReal64_ctype, ViReal64_ctype, ViReal64_ctype]  # noqa: F405
            self.CalAdjustACFilter_cfunc.restype = nidmm.python_types.ViStatus
        return self.CalAdjustACFilter_cfunc(vi, mode, range, frequency, expected_value)

    def niDMM_CalAdjustGain(self, vi, mode, range, input_resistance, expected_value):  # noqa: N802
        if self.CalAdjustGain_cfunc is None:
            self.CalAdjustGain_cfunc = self._library.CalAdjustGain
            self.CalAdjustGain_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViReal64_ctype, ViReal64_ctype, ViReal64_ctype]  # noqa: F405
            self.CalAdjustGain_cfunc.restype = nidmm.python_types.ViStatus
        return self.CalAdjustGain_cfunc(vi, mode, range, input_resistance, expected_value)

    def niDMM_CalAdjustLC(self, vi, type):  # noqa: N802
        if self.CalAdjustLC_cfunc is None:
            self.CalAdjustLC_cfunc = self._library.CalAdjustLC
            self.CalAdjustLC_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype]  # noqa: F405
            self.CalAdjustLC_cfunc.restype = nidmm.python_types.ViStatus
        return self.CalAdjustLC_cfunc(vi, type)

    def niDMM_CalAdjustLinearization(self, vi, function, range, input_resistance, expected_value):  # noqa: N802
        if self.CalAdjustLinearization_cfunc is None:
            self.CalAdjustLinearization_cfunc = self._library.CalAdjustLinearization
            self.CalAdjustLinearization_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViReal64_ctype, ViReal64_ctype, ViReal64_ctype]  # noqa: F405
            self.CalAdjustLinearization_cfunc.restype = nidmm.python_types.ViStatus
        return self.CalAdjustLinearization_cfunc(vi, function, range, input_resistance, expected_value)

    def niDMM_CalAdjustMisc(self, vi, type):  # noqa: N802
        if self.CalAdjustMisc_cfunc is None:
            self.CalAdjustMisc_cfunc = self._library.CalAdjustMisc
            self.CalAdjustMisc_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype]  # noqa: F405
            self.CalAdjustMisc_cfunc.restype = nidmm.python_types.ViStatus
        return self.CalAdjustMisc_cfunc(vi, type)

    def niDMM_CalAdjustOffset(self, vi, mode, range, input_resistance):  # noqa: N802
        if self.CalAdjustOffset_cfunc is None:
            self.CalAdjustOffset_cfunc = self._library.CalAdjustOffset
            self.CalAdjustOffset_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViReal64_ctype, ViReal64_ctype]  # noqa: F405
            self.CalAdjustOffset_cfunc.restype = nidmm.python_types.ViStatus
        return self.CalAdjustOffset_cfunc(vi, mode, range, input_resistance)

    def niDMM_CheckAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self.CheckAttributeViBoolean_cfunc is None:
            self.CheckAttributeViBoolean_cfunc = self._library.CheckAttributeViBoolean
            self.CheckAttributeViBoolean_cfunc.argtypes = [ViSession_ctype, ViConstString_ctype, ViAttr_ctype, ViBoolean_ctype]  # noqa: F405
            self.CheckAttributeViBoolean_cfunc.restype = nidmm.python_types.ViStatus
        return self.CheckAttributeViBoolean_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDMM_CheckAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self.CheckAttributeViInt32_cfunc is None:
            self.CheckAttributeViInt32_cfunc = self._library.CheckAttributeViInt32
            self.CheckAttributeViInt32_cfunc.argtypes = [ViSession_ctype, ViConstString_ctype, ViAttr_ctype, ViInt32_ctype]  # noqa: F405
            self.CheckAttributeViInt32_cfunc.restype = nidmm.python_types.ViStatus
        return self.CheckAttributeViInt32_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDMM_CheckAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self.CheckAttributeViReal64_cfunc is None:
            self.CheckAttributeViReal64_cfunc = self._library.CheckAttributeViReal64
            self.CheckAttributeViReal64_cfunc.argtypes = [ViSession_ctype, ViConstString_ctype, ViAttr_ctype, ViReal64_ctype]  # noqa: F405
            self.CheckAttributeViReal64_cfunc.restype = nidmm.python_types.ViStatus
        return self.CheckAttributeViReal64_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDMM_CheckAttributeViSession(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self.CheckAttributeViSession_cfunc is None:
            self.CheckAttributeViSession_cfunc = self._library.CheckAttributeViSession
            self.CheckAttributeViSession_cfunc.argtypes = [ViSession_ctype, ViConstString_ctype, ViAttr_ctype, ViSession_ctype]  # noqa: F405
            self.CheckAttributeViSession_cfunc.restype = nidmm.python_types.ViStatus
        return self.CheckAttributeViSession_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDMM_CheckAttributeViString(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self.CheckAttributeViString_cfunc is None:
            self.CheckAttributeViString_cfunc = self._library.CheckAttributeViString
            self.CheckAttributeViString_cfunc.argtypes = [ViSession_ctype, ViConstString_ctype, ViAttr_ctype, ViChar_ctype]  # noqa: F405
            self.CheckAttributeViString_cfunc.restype = nidmm.python_types.ViStatus
        return self.CheckAttributeViString_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDMM_ClearError(self, vi):  # noqa: N802
        if self.ClearError_cfunc is None:
            self.ClearError_cfunc = self._library.ClearError
            self.ClearError_cfunc.argtypes = [ViSession_ctype]  # noqa: F405
            self.ClearError_cfunc.restype = nidmm.python_types.ViStatus
        return self.ClearError_cfunc(vi)

    def niDMM_ClearInterchangeWarnings(self, vi):  # noqa: N802
        if self.ClearInterchangeWarnings_cfunc is None:
            self.ClearInterchangeWarnings_cfunc = self._library.ClearInterchangeWarnings
            self.ClearInterchangeWarnings_cfunc.argtypes = [ViSession_ctype]  # noqa: F405
            self.ClearInterchangeWarnings_cfunc.restype = nidmm.python_types.ViStatus
        return self.ClearInterchangeWarnings_cfunc(vi)

    def niDMM_CloseExtCal(self, vi, action):  # noqa: N802
        if self.CloseExtCal_cfunc is None:
            self.CloseExtCal_cfunc = self._library.CloseExtCal
            self.CloseExtCal_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype]  # noqa: F405
            self.CloseExtCal_cfunc.restype = nidmm.python_types.ViStatus
        return self.CloseExtCal_cfunc(vi, action)

    def niDMM_ConfigureACBandwidth(self, vi, ac_minimum_frequency_hz, ac_maximum_frequency_hz):  # noqa: N802
        if self.ConfigureACBandwidth_cfunc is None:
            self.ConfigureACBandwidth_cfunc = self._library.ConfigureACBandwidth
            self.ConfigureACBandwidth_cfunc.argtypes = [ViSession_ctype, ViReal64_ctype, ViReal64_ctype]  # noqa: F405
            self.ConfigureACBandwidth_cfunc.restype = nidmm.python_types.ViStatus
        return self.ConfigureACBandwidth_cfunc(vi, ac_minimum_frequency_hz, ac_maximum_frequency_hz)

    def niDMM_ConfigureADCCalibration(self, vi, adc_calibration):  # noqa: N802
        if self.ConfigureADCCalibration_cfunc is None:
            self.ConfigureADCCalibration_cfunc = self._library.ConfigureADCCalibration
            self.ConfigureADCCalibration_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype]  # noqa: F405
            self.ConfigureADCCalibration_cfunc.restype = nidmm.python_types.ViStatus
        return self.ConfigureADCCalibration_cfunc(vi, adc_calibration)

    def niDMM_ConfigureAutoZeroMode(self, vi, auto_zero_mode):  # noqa: N802
        if self.ConfigureAutoZeroMode_cfunc is None:
            self.ConfigureAutoZeroMode_cfunc = self._library.ConfigureAutoZeroMode
            self.ConfigureAutoZeroMode_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype]  # noqa: F405
            self.ConfigureAutoZeroMode_cfunc.restype = nidmm.python_types.ViStatus
        return self.ConfigureAutoZeroMode_cfunc(vi, auto_zero_mode)

    def niDMM_ConfigureCableCompType(self, vi, cable_comp_type):  # noqa: N802
        if self.ConfigureCableCompType_cfunc is None:
            self.ConfigureCableCompType_cfunc = self._library.ConfigureCableCompType
            self.ConfigureCableCompType_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype]  # noqa: F405
            self.ConfigureCableCompType_cfunc.restype = nidmm.python_types.ViStatus
        return self.ConfigureCableCompType_cfunc(vi, cable_comp_type)

    def niDMM_ConfigureCurrentSource(self, vi, current_source):  # noqa: N802
        if self.ConfigureCurrentSource_cfunc is None:
            self.ConfigureCurrentSource_cfunc = self._library.ConfigureCurrentSource
            self.ConfigureCurrentSource_cfunc.argtypes = [ViSession_ctype, ViReal64_ctype]  # noqa: F405
            self.ConfigureCurrentSource_cfunc.restype = nidmm.python_types.ViStatus
        return self.ConfigureCurrentSource_cfunc(vi, current_source)

    def niDMM_ConfigureFixedRefJunction(self, vi, fixed_reference_junction):  # noqa: N802
        if self.ConfigureFixedRefJunction_cfunc is None:
            self.ConfigureFixedRefJunction_cfunc = self._library.ConfigureFixedRefJunction
            self.ConfigureFixedRefJunction_cfunc.argtypes = [ViSession_ctype, ViReal64_ctype]  # noqa: F405
            self.ConfigureFixedRefJunction_cfunc.restype = nidmm.python_types.ViStatus
        return self.ConfigureFixedRefJunction_cfunc(vi, fixed_reference_junction)

    def niDMM_ConfigureFrequencyVoltageRange(self, vi, voltage_range):  # noqa: N802
        if self.ConfigureFrequencyVoltageRange_cfunc is None:
            self.ConfigureFrequencyVoltageRange_cfunc = self._library.ConfigureFrequencyVoltageRange
            self.ConfigureFrequencyVoltageRange_cfunc.argtypes = [ViSession_ctype, ViReal64_ctype]  # noqa: F405
            self.ConfigureFrequencyVoltageRange_cfunc.restype = nidmm.python_types.ViStatus
        return self.ConfigureFrequencyVoltageRange_cfunc(vi, voltage_range)

    def niDMM_ConfigureMeasCompleteDest(self, vi, meas_complete_destination):  # noqa: N802
        if self.ConfigureMeasCompleteDest_cfunc is None:
            self.ConfigureMeasCompleteDest_cfunc = self._library.ConfigureMeasCompleteDest
            self.ConfigureMeasCompleteDest_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype]  # noqa: F405
            self.ConfigureMeasCompleteDest_cfunc.restype = nidmm.python_types.ViStatus
        return self.ConfigureMeasCompleteDest_cfunc(vi, meas_complete_destination)

    def niDMM_ConfigureMeasCompleteSlope(self, vi, meas_complete_slope):  # noqa: N802
        if self.ConfigureMeasCompleteSlope_cfunc is None:
            self.ConfigureMeasCompleteSlope_cfunc = self._library.ConfigureMeasCompleteSlope
            self.ConfigureMeasCompleteSlope_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype]  # noqa: F405
            self.ConfigureMeasCompleteSlope_cfunc.restype = nidmm.python_types.ViStatus
        return self.ConfigureMeasCompleteSlope_cfunc(vi, meas_complete_slope)

    def niDMM_ConfigureMeasurementAbsolute(self, vi, measurement_function, range, resolution_absolute):  # noqa: N802
        if self.ConfigureMeasurementAbsolute_cfunc is None:
            self.ConfigureMeasurementAbsolute_cfunc = self._library.ConfigureMeasurementAbsolute
            self.ConfigureMeasurementAbsolute_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViReal64_ctype, ViReal64_ctype]  # noqa: F405
            self.ConfigureMeasurementAbsolute_cfunc.restype = nidmm.python_types.ViStatus
        return self.ConfigureMeasurementAbsolute_cfunc(vi, measurement_function, range, resolution_absolute)

    def niDMM_ConfigureMeasurementDigits(self, vi, measurement_function, range, resolution_digits):  # noqa: N802
        if self.ConfigureMeasurementDigits_cfunc is None:
            self.ConfigureMeasurementDigits_cfunc = self._library.ConfigureMeasurementDigits
            self.ConfigureMeasurementDigits_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViReal64_ctype, ViReal64_ctype]  # noqa: F405
            self.ConfigureMeasurementDigits_cfunc.restype = nidmm.python_types.ViStatus
        return self.ConfigureMeasurementDigits_cfunc(vi, measurement_function, range, resolution_digits)

    def niDMM_ConfigureMultiPoint(self, vi, trigger_count, sample_count, sample_trigger, sample_interval):  # noqa: N802
        if self.ConfigureMultiPoint_cfunc is None:
            self.ConfigureMultiPoint_cfunc = self._library.ConfigureMultiPoint
            self.ConfigureMultiPoint_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViInt32_ctype, ViInt32_ctype, ViReal64_ctype]  # noqa: F405
            self.ConfigureMultiPoint_cfunc.restype = nidmm.python_types.ViStatus
        return self.ConfigureMultiPoint_cfunc(vi, trigger_count, sample_count, sample_trigger, sample_interval)

    def niDMM_ConfigureOffsetCompOhms(self, vi, offset_comp_ohms):  # noqa: N802
        if self.ConfigureOffsetCompOhms_cfunc is None:
            self.ConfigureOffsetCompOhms_cfunc = self._library.ConfigureOffsetCompOhms
            self.ConfigureOffsetCompOhms_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype]  # noqa: F405
            self.ConfigureOffsetCompOhms_cfunc.restype = nidmm.python_types.ViStatus
        return self.ConfigureOffsetCompOhms_cfunc(vi, offset_comp_ohms)

    def niDMM_ConfigureOpenCableCompValues(self, vi, conductance, susceptance):  # noqa: N802
        if self.ConfigureOpenCableCompValues_cfunc is None:
            self.ConfigureOpenCableCompValues_cfunc = self._library.ConfigureOpenCableCompValues
            self.ConfigureOpenCableCompValues_cfunc.argtypes = [ViSession_ctype, ViReal64_ctype, ViReal64_ctype]  # noqa: F405
            self.ConfigureOpenCableCompValues_cfunc.restype = nidmm.python_types.ViStatus
        return self.ConfigureOpenCableCompValues_cfunc(vi, conductance, susceptance)

    def niDMM_ConfigurePowerLineFrequency(self, vi, power_line_frequency_hz):  # noqa: N802
        if self.ConfigurePowerLineFrequency_cfunc is None:
            self.ConfigurePowerLineFrequency_cfunc = self._library.ConfigurePowerLineFrequency
            self.ConfigurePowerLineFrequency_cfunc.argtypes = [ViSession_ctype, ViReal64_ctype]  # noqa: F405
            self.ConfigurePowerLineFrequency_cfunc.restype = nidmm.python_types.ViStatus
        return self.ConfigurePowerLineFrequency_cfunc(vi, power_line_frequency_hz)

    def niDMM_ConfigureRTDCustom(self, vi, rtd_a, rtd_b, rtd_c):  # noqa: N802
        if self.ConfigureRTDCustom_cfunc is None:
            self.ConfigureRTDCustom_cfunc = self._library.ConfigureRTDCustom
            self.ConfigureRTDCustom_cfunc.argtypes = [ViSession_ctype, ViReal64_ctype, ViReal64_ctype, ViReal64_ctype]  # noqa: F405
            self.ConfigureRTDCustom_cfunc.restype = nidmm.python_types.ViStatus
        return self.ConfigureRTDCustom_cfunc(vi, rtd_a, rtd_b, rtd_c)

    def niDMM_ConfigureRTDType(self, vi, rtd_type, rtd_resistance):  # noqa: N802
        if self.ConfigureRTDType_cfunc is None:
            self.ConfigureRTDType_cfunc = self._library.ConfigureRTDType
            self.ConfigureRTDType_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViReal64_ctype]  # noqa: F405
            self.ConfigureRTDType_cfunc.restype = nidmm.python_types.ViStatus
        return self.ConfigureRTDType_cfunc(vi, rtd_type, rtd_resistance)

    def niDMM_ConfigureSampleTriggerSlope(self, vi, sample_trigger_slope):  # noqa: N802
        if self.ConfigureSampleTriggerSlope_cfunc is None:
            self.ConfigureSampleTriggerSlope_cfunc = self._library.ConfigureSampleTriggerSlope
            self.ConfigureSampleTriggerSlope_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype]  # noqa: F405
            self.ConfigureSampleTriggerSlope_cfunc.restype = nidmm.python_types.ViStatus
        return self.ConfigureSampleTriggerSlope_cfunc(vi, sample_trigger_slope)

    def niDMM_ConfigureShortCableCompValues(self, vi, resistance, reactance):  # noqa: N802
        if self.ConfigureShortCableCompValues_cfunc is None:
            self.ConfigureShortCableCompValues_cfunc = self._library.ConfigureShortCableCompValues
            self.ConfigureShortCableCompValues_cfunc.argtypes = [ViSession_ctype, ViReal64_ctype, ViReal64_ctype]  # noqa: F405
            self.ConfigureShortCableCompValues_cfunc.restype = nidmm.python_types.ViStatus
        return self.ConfigureShortCableCompValues_cfunc(vi, resistance, reactance)

    def niDMM_ConfigureThermistorCustom(self, vi, thermistor_a, thermistor_b, thermistor_c):  # noqa: N802
        if self.ConfigureThermistorCustom_cfunc is None:
            self.ConfigureThermistorCustom_cfunc = self._library.ConfigureThermistorCustom
            self.ConfigureThermistorCustom_cfunc.argtypes = [ViSession_ctype, ViReal64_ctype, ViReal64_ctype, ViReal64_ctype]  # noqa: F405
            self.ConfigureThermistorCustom_cfunc.restype = nidmm.python_types.ViStatus
        return self.ConfigureThermistorCustom_cfunc(vi, thermistor_a, thermistor_b, thermistor_c)

    def niDMM_ConfigureThermistorType(self, vi, thermistor_type):  # noqa: N802
        if self.ConfigureThermistorType_cfunc is None:
            self.ConfigureThermistorType_cfunc = self._library.ConfigureThermistorType
            self.ConfigureThermistorType_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype]  # noqa: F405
            self.ConfigureThermistorType_cfunc.restype = nidmm.python_types.ViStatus
        return self.ConfigureThermistorType_cfunc(vi, thermistor_type)

    def niDMM_ConfigureThermocouple(self, vi, thermocouple_type, reference_junction_type):  # noqa: N802
        if self.ConfigureThermocouple_cfunc is None:
            self.ConfigureThermocouple_cfunc = self._library.ConfigureThermocouple
            self.ConfigureThermocouple_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViInt32_ctype]  # noqa: F405
            self.ConfigureThermocouple_cfunc.restype = nidmm.python_types.ViStatus
        return self.ConfigureThermocouple_cfunc(vi, thermocouple_type, reference_junction_type)

    def niDMM_ConfigureTransducerType(self, vi, transducer_type):  # noqa: N802
        if self.ConfigureTransducerType_cfunc is None:
            self.ConfigureTransducerType_cfunc = self._library.ConfigureTransducerType
            self.ConfigureTransducerType_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype]  # noqa: F405
            self.ConfigureTransducerType_cfunc.restype = nidmm.python_types.ViStatus
        return self.ConfigureTransducerType_cfunc(vi, transducer_type)

    def niDMM_ConfigureTrigger(self, vi, trigger_source, trigger_delay):  # noqa: N802
        if self.ConfigureTrigger_cfunc is None:
            self.ConfigureTrigger_cfunc = self._library.ConfigureTrigger
            self.ConfigureTrigger_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViReal64_ctype]  # noqa: F405
            self.ConfigureTrigger_cfunc.restype = nidmm.python_types.ViStatus
        return self.ConfigureTrigger_cfunc(vi, trigger_source, trigger_delay)

    def niDMM_ConfigureTriggerSlope(self, vi, trigger_slope):  # noqa: N802
        if self.ConfigureTriggerSlope_cfunc is None:
            self.ConfigureTriggerSlope_cfunc = self._library.ConfigureTriggerSlope
            self.ConfigureTriggerSlope_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype]  # noqa: F405
            self.ConfigureTriggerSlope_cfunc.restype = nidmm.python_types.ViStatus
        return self.ConfigureTriggerSlope_cfunc(vi, trigger_slope)

    def niDMM_ConfigureWaveformAcquisition(self, vi, measurement_function, range, rate, waveform_points):  # noqa: N802
        if self.ConfigureWaveformAcquisition_cfunc is None:
            self.ConfigureWaveformAcquisition_cfunc = self._library.ConfigureWaveformAcquisition
            self.ConfigureWaveformAcquisition_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViReal64_ctype, ViReal64_ctype, ViInt32_ctype]  # noqa: F405
            self.ConfigureWaveformAcquisition_cfunc.restype = nidmm.python_types.ViStatus
        return self.ConfigureWaveformAcquisition_cfunc(vi, measurement_function, range, rate, waveform_points)

    def niDMM_ConfigureWaveformCoupling(self, vi, waveform_coupling):  # noqa: N802
        if self.ConfigureWaveformCoupling_cfunc is None:
            self.ConfigureWaveformCoupling_cfunc = self._library.ConfigureWaveformCoupling
            self.ConfigureWaveformCoupling_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype]  # noqa: F405
            self.ConfigureWaveformCoupling_cfunc.restype = nidmm.python_types.ViStatus
        return self.ConfigureWaveformCoupling_cfunc(vi, waveform_coupling)

    def niDMM_Control(self, vi, control_action):  # noqa: N802
        if self.Control_cfunc is None:
            self.Control_cfunc = self._library.Control
            self.Control_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype]  # noqa: F405
            self.Control_cfunc.restype = nidmm.python_types.ViStatus
        return self.Control_cfunc(vi, control_action)

    def niDMM_Disable(self, vi):  # noqa: N802
        if self.Disable_cfunc is None:
            self.Disable_cfunc = self._library.Disable
            self.Disable_cfunc.argtypes = [ViSession_ctype]  # noqa: F405
            self.Disable_cfunc.restype = nidmm.python_types.ViStatus
        return self.Disable_cfunc(vi)

    def niDMM_Fetch(self, vi, maximum_time, reading):  # noqa: N802
        if self.Fetch_cfunc is None:
            self.Fetch_cfunc = self._library.Fetch
            self.Fetch_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ctypes.POINTER(ViReal64_ctype)]  # noqa: F405
            self.Fetch_cfunc.restype = nidmm.python_types.ViStatus
        return self.Fetch_cfunc(vi, maximum_time, reading)

    def niDMM_FetchMultiPoint(self, vi, maximum_time, array_size, reading_array, actual_number_of_points):  # noqa: N802
        if self.FetchMultiPoint_cfunc is None:
            self.FetchMultiPoint_cfunc = self._library.FetchMultiPoint
            self.FetchMultiPoint_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViInt32_ctype, ctypes.POINTER(ViReal64_ctype), ctypes.POINTER(ViInt32_ctype)]  # noqa: F405
            self.FetchMultiPoint_cfunc.restype = nidmm.python_types.ViStatus
        return self.FetchMultiPoint_cfunc(vi, maximum_time, array_size, reading_array, actual_number_of_points)

    def niDMM_FetchWaveform(self, vi, maximum_time, array_size, waveform_array, actual_number_of_points):  # noqa: N802
        if self.FetchWaveform_cfunc is None:
            self.FetchWaveform_cfunc = self._library.FetchWaveform
            self.FetchWaveform_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViInt32_ctype, ctypes.POINTER(ViReal64_ctype), ctypes.POINTER(ViInt32_ctype)]  # noqa: F405
            self.FetchWaveform_cfunc.restype = nidmm.python_types.ViStatus
        return self.FetchWaveform_cfunc(vi, maximum_time, array_size, waveform_array, actual_number_of_points)

    def niDMM_FormatMeasAbsolute(self, measurement_function, range, resolution, measurement, mode_string, range_string, data_string):  # noqa: N802
        if self.FormatMeasAbsolute_cfunc is None:
            self.FormatMeasAbsolute_cfunc = self._library.FormatMeasAbsolute
            self.FormatMeasAbsolute_cfunc.argtypes = [ViInt32_ctype, ViReal64_ctype, ViReal64_ctype, ViReal64_ctype, ctypes.POINTER(ViChar_ctype), ctypes.POINTER(ViChar_ctype), ctypes.POINTER(ViChar_ctype)]  # noqa: F405
            self.FormatMeasAbsolute_cfunc.restype = nidmm.python_types.ViStatus
        return self.FormatMeasAbsolute_cfunc(measurement_function, range, resolution, measurement, mode_string, range_string, data_string)

    def niDMM_GetApertureTimeInfo(self, vi, aperture_time, aperture_time_units):  # noqa: N802
        if self.GetApertureTimeInfo_cfunc is None:
            self.GetApertureTimeInfo_cfunc = self._library.GetApertureTimeInfo
            self.GetApertureTimeInfo_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViReal64_ctype), ctypes.POINTER(ViInt32_ctype)]  # noqa: F405
            self.GetApertureTimeInfo_cfunc.restype = nidmm.python_types.ViStatus
        return self.GetApertureTimeInfo_cfunc(vi, aperture_time, aperture_time_units)

    def niDMM_GetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self.GetAttributeViBoolean_cfunc is None:
            self.GetAttributeViBoolean_cfunc = self._library.GetAttributeViBoolean
            self.GetAttributeViBoolean_cfunc.argtypes = [ViSession_ctype, ViConstString_ctype, ViAttr_ctype, ctypes.POINTER(ViBoolean_ctype)]  # noqa: F405
            self.GetAttributeViBoolean_cfunc.restype = nidmm.python_types.ViStatus
        return self.GetAttributeViBoolean_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDMM_GetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self.GetAttributeViInt32_cfunc is None:
            self.GetAttributeViInt32_cfunc = self._library.GetAttributeViInt32
            self.GetAttributeViInt32_cfunc.argtypes = [ViSession_ctype, ViConstString_ctype, ViAttr_ctype, ctypes.POINTER(ViInt32_ctype)]  # noqa: F405
            self.GetAttributeViInt32_cfunc.restype = nidmm.python_types.ViStatus
        return self.GetAttributeViInt32_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDMM_GetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self.GetAttributeViReal64_cfunc is None:
            self.GetAttributeViReal64_cfunc = self._library.GetAttributeViReal64
            self.GetAttributeViReal64_cfunc.argtypes = [ViSession_ctype, ViConstString_ctype, ViAttr_ctype, ctypes.POINTER(ViReal64_ctype)]  # noqa: F405
            self.GetAttributeViReal64_cfunc.restype = nidmm.python_types.ViStatus
        return self.GetAttributeViReal64_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDMM_GetAttributeViSession(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self.GetAttributeViSession_cfunc is None:
            self.GetAttributeViSession_cfunc = self._library.GetAttributeViSession
            self.GetAttributeViSession_cfunc.argtypes = [ViSession_ctype, ViConstString_ctype, ViAttr_ctype, ctypes.POINTER(ViSession_ctype)]  # noqa: F405
            self.GetAttributeViSession_cfunc.restype = nidmm.python_types.ViStatus
        return self.GetAttributeViSession_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDMM_GetAttributeViString(self, vi, channel_name, attribute_id, buffer_size, attribute_value):  # noqa: N802
        if self.GetAttributeViString_cfunc is None:
            self.GetAttributeViString_cfunc = self._library.GetAttributeViString
            self.GetAttributeViString_cfunc.argtypes = [ViSession_ctype, ViConstString_ctype, ViAttr_ctype, ViInt32_ctype, ctypes.POINTER(ViChar_ctype)]  # noqa: F405
            self.GetAttributeViString_cfunc.restype = nidmm.python_types.ViStatus
        return self.GetAttributeViString_cfunc(vi, channel_name, attribute_id, buffer_size, attribute_value)

    def niDMM_GetAutoRangeValue(self, vi, actual_range):  # noqa: N802
        if self.GetAutoRangeValue_cfunc is None:
            self.GetAutoRangeValue_cfunc = self._library.GetAutoRangeValue
            self.GetAutoRangeValue_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViReal64_ctype)]  # noqa: F405
            self.GetAutoRangeValue_cfunc.restype = nidmm.python_types.ViStatus
        return self.GetAutoRangeValue_cfunc(vi, actual_range)

    def niDMM_GetCalCount(self, vi, cal_type, count):  # noqa: N802
        if self.GetCalCount_cfunc is None:
            self.GetCalCount_cfunc = self._library.GetCalCount
            self.GetCalCount_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ctypes.POINTER(ViInt32_ctype)]  # noqa: F405
            self.GetCalCount_cfunc.restype = nidmm.python_types.ViStatus
        return self.GetCalCount_cfunc(vi, cal_type, count)

    def niDMM_GetCalDateAndTime(self, vi, cal_type, month, day, year, hour, minute):  # noqa: N802
        if self.GetCalDateAndTime_cfunc is None:
            self.GetCalDateAndTime_cfunc = self._library.GetCalDateAndTime
            self.GetCalDateAndTime_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ctypes.POINTER(ViInt32_ctype), ctypes.POINTER(ViInt32_ctype), ctypes.POINTER(ViInt32_ctype), ctypes.POINTER(ViInt32_ctype), ctypes.POINTER(ViInt32_ctype)]  # noqa: F405
            self.GetCalDateAndTime_cfunc.restype = nidmm.python_types.ViStatus
        return self.GetCalDateAndTime_cfunc(vi, cal_type, month, day, year, hour, minute)

    def niDMM_GetCalUserDefinedInfo(self, vi, buffer_size, info):  # noqa: N802
        if self.GetCalUserDefinedInfo_cfunc is None:
            self.GetCalUserDefinedInfo_cfunc = self._library.GetCalUserDefinedInfo
            self.GetCalUserDefinedInfo_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ctypes.POINTER(ViChar_ctype)]  # noqa: F405
            self.GetCalUserDefinedInfo_cfunc.restype = nidmm.python_types.ViStatus
        return self.GetCalUserDefinedInfo_cfunc(vi, buffer_size, info)

    def niDMM_GetCalUserDefinedInfoMaxSize(self, vi, info_size):  # noqa: N802
        if self.GetCalUserDefinedInfoMaxSize_cfunc is None:
            self.GetCalUserDefinedInfoMaxSize_cfunc = self._library.GetCalUserDefinedInfoMaxSize
            self.GetCalUserDefinedInfoMaxSize_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViInt32_ctype)]  # noqa: F405
            self.GetCalUserDefinedInfoMaxSize_cfunc.restype = nidmm.python_types.ViStatus
        return self.GetCalUserDefinedInfoMaxSize_cfunc(vi, info_size)

    def niDMM_GetChannelName(self, vi, index, buffer_size, channel_string):  # noqa: N802
        if self.GetChannelName_cfunc is None:
            self.GetChannelName_cfunc = self._library.GetChannelName
            self.GetChannelName_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViInt32_ctype, ctypes.POINTER(ViChar_ctype)]  # noqa: F405
            self.GetChannelName_cfunc.restype = nidmm.python_types.ViStatus
        return self.GetChannelName_cfunc(vi, index, buffer_size, channel_string)

    def niDMM_GetDevTemp(self, vi, options, temperature):  # noqa: N802
        if self.GetDevTemp_cfunc is None:
            self.GetDevTemp_cfunc = self._library.GetDevTemp
            self.GetDevTemp_cfunc.argtypes = [ViSession_ctype, ViString_ctype, ctypes.POINTER(ViReal64_ctype)]  # noqa: F405
            self.GetDevTemp_cfunc.restype = nidmm.python_types.ViStatus
        return self.GetDevTemp_cfunc(vi, options, temperature)

    def niDMM_GetError(self, vi, error_code, buffer_size, description):  # noqa: N802
        if self.GetError_cfunc is None:
            self.GetError_cfunc = self._library.GetError
            self.GetError_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViStatus_ctype), ViInt32_ctype, ctypes.POINTER(ViChar_ctype)]  # noqa: F405
            self.GetError_cfunc.restype = nidmm.python_types.ViStatus
        return self.GetError_cfunc(vi, error_code, buffer_size, description)

    def niDMM_GetErrorMessage(self, vi, error_code, buffer_size, error_message):  # noqa: N802
        if self.GetErrorMessage_cfunc is None:
            self.GetErrorMessage_cfunc = self._library.GetErrorMessage
            self.GetErrorMessage_cfunc.argtypes = [ViSession_ctype, ViStatus_ctype, ViInt32_ctype, ctypes.POINTER(ViChar_ctype)]  # noqa: F405
            self.GetErrorMessage_cfunc.restype = nidmm.python_types.ViStatus
        return self.GetErrorMessage_cfunc(vi, error_code, buffer_size, error_message)

    def niDMM_GetExtCalRecommendedInterval(self, vi, months):  # noqa: N802
        if self.GetExtCalRecommendedInterval_cfunc is None:
            self.GetExtCalRecommendedInterval_cfunc = self._library.GetExtCalRecommendedInterval
            self.GetExtCalRecommendedInterval_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViInt32_ctype)]  # noqa: F405
            self.GetExtCalRecommendedInterval_cfunc.restype = nidmm.python_types.ViStatus
        return self.GetExtCalRecommendedInterval_cfunc(vi, months)

    def niDMM_GetLastCalTemp(self, vi, cal_type, temperature):  # noqa: N802
        if self.GetLastCalTemp_cfunc is None:
            self.GetLastCalTemp_cfunc = self._library.GetLastCalTemp
            self.GetLastCalTemp_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ctypes.POINTER(ViReal64_ctype)]  # noqa: F405
            self.GetLastCalTemp_cfunc.restype = nidmm.python_types.ViStatus
        return self.GetLastCalTemp_cfunc(vi, cal_type, temperature)

    def niDMM_GetMeasurementPeriod(self, vi, period):  # noqa: N802
        if self.GetMeasurementPeriod_cfunc is None:
            self.GetMeasurementPeriod_cfunc = self._library.GetMeasurementPeriod
            self.GetMeasurementPeriod_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViReal64_ctype)]  # noqa: F405
            self.GetMeasurementPeriod_cfunc.restype = nidmm.python_types.ViStatus
        return self.GetMeasurementPeriod_cfunc(vi, period)

    def niDMM_GetNextCoercionRecord(self, vi, buffer_size, coercion_record):  # noqa: N802
        if self.GetNextCoercionRecord_cfunc is None:
            self.GetNextCoercionRecord_cfunc = self._library.GetNextCoercionRecord
            self.GetNextCoercionRecord_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ctypes.POINTER(ViChar_ctype)]  # noqa: F405
            self.GetNextCoercionRecord_cfunc.restype = nidmm.python_types.ViStatus
        return self.GetNextCoercionRecord_cfunc(vi, buffer_size, coercion_record)

    def niDMM_GetNextInterchangeWarning(self, vi, buffer_size, interchange_warning):  # noqa: N802
        if self.GetNextInterchangeWarning_cfunc is None:
            self.GetNextInterchangeWarning_cfunc = self._library.GetNextInterchangeWarning
            self.GetNextInterchangeWarning_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ctypes.POINTER(ViChar_ctype)]  # noqa: F405
            self.GetNextInterchangeWarning_cfunc.restype = nidmm.python_types.ViStatus
        return self.GetNextInterchangeWarning_cfunc(vi, buffer_size, interchange_warning)

    def niDMM_GetSelfCalSupported(self, vi, self_cal_supported):  # noqa: N802
        if self.GetSelfCalSupported_cfunc is None:
            self.GetSelfCalSupported_cfunc = self._library.GetSelfCalSupported
            self.GetSelfCalSupported_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViBoolean_ctype)]  # noqa: F405
            self.GetSelfCalSupported_cfunc.restype = nidmm.python_types.ViStatus
        return self.GetSelfCalSupported_cfunc(vi, self_cal_supported)

    def niDMM_InitExtCal(self, resource_name, calibration_password, vi):  # noqa: N802
        if self.InitExtCal_cfunc is None:
            self.InitExtCal_cfunc = self._library.InitExtCal
            self.InitExtCal_cfunc.argtypes = [ViString_ctype, ViChar_ctype, ctypes.POINTER(ViSession_ctype)]  # noqa: F405
            self.InitExtCal_cfunc.restype = nidmm.python_types.ViStatus
        return self.InitExtCal_cfunc(resource_name, calibration_password, vi)

    def niDMM_InitWithOptions(self, resource_name, id_query, reset_device, option_string, vi):  # noqa: N802
        if self.InitWithOptions_cfunc is None:
            self.InitWithOptions_cfunc = self._library.InitWithOptions
            self.InitWithOptions_cfunc.argtypes = [ViString_ctype, ViBoolean_ctype, ViBoolean_ctype, ViString_ctype, ctypes.POINTER(ViSession_ctype)]  # noqa: F405
            self.InitWithOptions_cfunc.restype = nidmm.python_types.ViStatus
        return self.InitWithOptions_cfunc(resource_name, id_query, reset_device, option_string, vi)

    def niDMM_Initiate(self, vi):  # noqa: N802
        if self.Initiate_cfunc is None:
            self.Initiate_cfunc = self._library.Initiate
            self.Initiate_cfunc.argtypes = [ViSession_ctype]  # noqa: F405
            self.Initiate_cfunc.restype = nidmm.python_types.ViStatus
        return self.Initiate_cfunc(vi)

    def niDMM_IsOverRange(self, vi, measurement_value, is_over_range):  # noqa: N802
        if self.IsOverRange_cfunc is None:
            self.IsOverRange_cfunc = self._library.IsOverRange
            self.IsOverRange_cfunc.argtypes = [ViSession_ctype, ViReal64_ctype, ctypes.POINTER(ViBoolean_ctype)]  # noqa: F405
            self.IsOverRange_cfunc.restype = nidmm.python_types.ViStatus
        return self.IsOverRange_cfunc(vi, measurement_value, is_over_range)

    def niDMM_IsUnderRange(self, vi, measurement_value, is_under_range):  # noqa: N802
        if self.IsUnderRange_cfunc is None:
            self.IsUnderRange_cfunc = self._library.IsUnderRange
            self.IsUnderRange_cfunc.argtypes = [ViSession_ctype, ViReal64_ctype, ctypes.POINTER(ViBoolean_ctype)]  # noqa: F405
            self.IsUnderRange_cfunc.restype = nidmm.python_types.ViStatus
        return self.IsUnderRange_cfunc(vi, measurement_value, is_under_range)

    def niDMM_LockSession(self, vi, caller_has_lock):  # noqa: N802
        if self.LockSession_cfunc is None:
            self.LockSession_cfunc = self._library.LockSession
            self.LockSession_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViBoolean_ctype)]  # noqa: F405
            self.LockSession_cfunc.restype = nidmm.python_types.ViStatus
        return self.LockSession_cfunc(vi, caller_has_lock)

    def niDMM_PerformOpenCableComp(self, vi, conductance, susceptance):  # noqa: N802
        if self.PerformOpenCableComp_cfunc is None:
            self.PerformOpenCableComp_cfunc = self._library.PerformOpenCableComp
            self.PerformOpenCableComp_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViReal64_ctype), ctypes.POINTER(ViReal64_ctype)]  # noqa: F405
            self.PerformOpenCableComp_cfunc.restype = nidmm.python_types.ViStatus
        return self.PerformOpenCableComp_cfunc(vi, conductance, susceptance)

    def niDMM_PerformShortCableComp(self, vi, resistance, reactance):  # noqa: N802
        if self.PerformShortCableComp_cfunc is None:
            self.PerformShortCableComp_cfunc = self._library.PerformShortCableComp
            self.PerformShortCableComp_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViReal64_ctype), ctypes.POINTER(ViReal64_ctype)]  # noqa: F405
            self.PerformShortCableComp_cfunc.restype = nidmm.python_types.ViStatus
        return self.PerformShortCableComp_cfunc(vi, resistance, reactance)

    def niDMM_Read(self, vi, maximum_time, reading):  # noqa: N802
        if self.Read_cfunc is None:
            self.Read_cfunc = self._library.Read
            self.Read_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ctypes.POINTER(ViReal64_ctype)]  # noqa: F405
            self.Read_cfunc.restype = nidmm.python_types.ViStatus
        return self.Read_cfunc(vi, maximum_time, reading)

    def niDMM_ReadMultiPoint(self, vi, maximum_time, array_size, reading_array, actual_number_of_points):  # noqa: N802
        if self.ReadMultiPoint_cfunc is None:
            self.ReadMultiPoint_cfunc = self._library.ReadMultiPoint
            self.ReadMultiPoint_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViInt32_ctype, ctypes.POINTER(ViReal64_ctype), ctypes.POINTER(ViInt32_ctype)]  # noqa: F405
            self.ReadMultiPoint_cfunc.restype = nidmm.python_types.ViStatus
        return self.ReadMultiPoint_cfunc(vi, maximum_time, array_size, reading_array, actual_number_of_points)

    def niDMM_ReadStatus(self, vi, acquisition_backlog, acquisition_status):  # noqa: N802
        if self.ReadStatus_cfunc is None:
            self.ReadStatus_cfunc = self._library.ReadStatus
            self.ReadStatus_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViInt32_ctype), ctypes.POINTER(ViInt16_ctype)]  # noqa: F405
            self.ReadStatus_cfunc.restype = nidmm.python_types.ViStatus
        return self.ReadStatus_cfunc(vi, acquisition_backlog, acquisition_status)

    def niDMM_ReadWaveform(self, vi, maximum_time, array_size, waveform_array, actual_number_of_points):  # noqa: N802
        if self.ReadWaveform_cfunc is None:
            self.ReadWaveform_cfunc = self._library.ReadWaveform
            self.ReadWaveform_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViInt32_ctype, ctypes.POINTER(ViReal64_ctype), ctypes.POINTER(ViInt32_ctype)]  # noqa: F405
            self.ReadWaveform_cfunc.restype = nidmm.python_types.ViStatus
        return self.ReadWaveform_cfunc(vi, maximum_time, array_size, waveform_array, actual_number_of_points)

    def niDMM_ResetInterchangeCheck(self, vi):  # noqa: N802
        if self.ResetInterchangeCheck_cfunc is None:
            self.ResetInterchangeCheck_cfunc = self._library.ResetInterchangeCheck
            self.ResetInterchangeCheck_cfunc.argtypes = [ViSession_ctype]  # noqa: F405
            self.ResetInterchangeCheck_cfunc.restype = nidmm.python_types.ViStatus
        return self.ResetInterchangeCheck_cfunc(vi)

    def niDMM_ResetWithDefaults(self, vi):  # noqa: N802
        if self.ResetWithDefaults_cfunc is None:
            self.ResetWithDefaults_cfunc = self._library.ResetWithDefaults
            self.ResetWithDefaults_cfunc.argtypes = [ViSession_ctype]  # noqa: F405
            self.ResetWithDefaults_cfunc.restype = nidmm.python_types.ViStatus
        return self.ResetWithDefaults_cfunc(vi)

    def niDMM_RestoreLastExtCalConstants(self, vi):  # noqa: N802
        if self.RestoreLastExtCalConstants_cfunc is None:
            self.RestoreLastExtCalConstants_cfunc = self._library.RestoreLastExtCalConstants
            self.RestoreLastExtCalConstants_cfunc.argtypes = [ViSession_ctype]  # noqa: F405
            self.RestoreLastExtCalConstants_cfunc.restype = nidmm.python_types.ViStatus
        return self.RestoreLastExtCalConstants_cfunc(vi)

    def niDMM_SelfCal(self, vi):  # noqa: N802
        if self.SelfCal_cfunc is None:
            self.SelfCal_cfunc = self._library.SelfCal
            self.SelfCal_cfunc.argtypes = [ViSession_ctype]  # noqa: F405
            self.SelfCal_cfunc.restype = nidmm.python_types.ViStatus
        return self.SelfCal_cfunc(vi)

    def niDMM_SendSoftwareTrigger(self, vi):  # noqa: N802
        if self.SendSoftwareTrigger_cfunc is None:
            self.SendSoftwareTrigger_cfunc = self._library.SendSoftwareTrigger
            self.SendSoftwareTrigger_cfunc.argtypes = [ViSession_ctype]  # noqa: F405
            self.SendSoftwareTrigger_cfunc.restype = nidmm.python_types.ViStatus
        return self.SendSoftwareTrigger_cfunc(vi)

    def niDMM_SetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self.SetAttributeViBoolean_cfunc is None:
            self.SetAttributeViBoolean_cfunc = self._library.SetAttributeViBoolean
            self.SetAttributeViBoolean_cfunc.argtypes = [ViSession_ctype, ViConstString_ctype, ViAttr_ctype, ViBoolean_ctype]  # noqa: F405
            self.SetAttributeViBoolean_cfunc.restype = nidmm.python_types.ViStatus
        return self.SetAttributeViBoolean_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDMM_SetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self.SetAttributeViInt32_cfunc is None:
            self.SetAttributeViInt32_cfunc = self._library.SetAttributeViInt32
            self.SetAttributeViInt32_cfunc.argtypes = [ViSession_ctype, ViConstString_ctype, ViAttr_ctype, ViInt32_ctype]  # noqa: F405
            self.SetAttributeViInt32_cfunc.restype = nidmm.python_types.ViStatus
        return self.SetAttributeViInt32_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDMM_SetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self.SetAttributeViReal64_cfunc is None:
            self.SetAttributeViReal64_cfunc = self._library.SetAttributeViReal64
            self.SetAttributeViReal64_cfunc.argtypes = [ViSession_ctype, ViConstString_ctype, ViAttr_ctype, ViReal64_ctype]  # noqa: F405
            self.SetAttributeViReal64_cfunc.restype = nidmm.python_types.ViStatus
        return self.SetAttributeViReal64_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDMM_SetAttributeViSession(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self.SetAttributeViSession_cfunc is None:
            self.SetAttributeViSession_cfunc = self._library.SetAttributeViSession
            self.SetAttributeViSession_cfunc.argtypes = [ViSession_ctype, ViConstString_ctype, ViAttr_ctype, ViSession_ctype]  # noqa: F405
            self.SetAttributeViSession_cfunc.restype = nidmm.python_types.ViStatus
        return self.SetAttributeViSession_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDMM_SetAttributeViString(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self.SetAttributeViString_cfunc is None:
            self.SetAttributeViString_cfunc = self._library.SetAttributeViString
            self.SetAttributeViString_cfunc.argtypes = [ViSession_ctype, ViConstString_ctype, ViAttr_ctype, ViChar_ctype]  # noqa: F405
            self.SetAttributeViString_cfunc.restype = nidmm.python_types.ViStatus
        return self.SetAttributeViString_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDMM_SetCalPassword(self, vi, old_password, new_password):  # noqa: N802
        if self.SetCalPassword_cfunc is None:
            self.SetCalPassword_cfunc = self._library.SetCalPassword
            self.SetCalPassword_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViChar_ctype]  # noqa: F405
            self.SetCalPassword_cfunc.restype = nidmm.python_types.ViStatus
        return self.SetCalPassword_cfunc(vi, old_password, new_password)

    def niDMM_SetCalUserDefinedInfo(self, vi, info):  # noqa: N802
        if self.SetCalUserDefinedInfo_cfunc is None:
            self.SetCalUserDefinedInfo_cfunc = self._library.SetCalUserDefinedInfo
            self.SetCalUserDefinedInfo_cfunc.argtypes = [ViSession_ctype, ViChar_ctype]  # noqa: F405
            self.SetCalUserDefinedInfo_cfunc.restype = nidmm.python_types.ViStatus
        return self.SetCalUserDefinedInfo_cfunc(vi, info)

    def niDMM_UnlockSession(self, vi, caller_has_lock):  # noqa: N802
        if self.UnlockSession_cfunc is None:
            self.UnlockSession_cfunc = self._library.UnlockSession
            self.UnlockSession_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViBoolean_ctype)]  # noqa: F405
            self.UnlockSession_cfunc.restype = nidmm.python_types.ViStatus
        return self.UnlockSession_cfunc(vi, caller_has_lock)

    def niDMM_close(self, vi):  # noqa: N802
        if self.close_cfunc is None:
            self.close_cfunc = self._library.close
            self.close_cfunc.argtypes = [ViSession_ctype]  # noqa: F405
            self.close_cfunc.restype = nidmm.python_types.ViStatus
        return self.close_cfunc(vi)

    def niDMM_error_message(self, vi, error_code, error_message):  # noqa: N802
        if self.error_message_cfunc is None:
            self.error_message_cfunc = self._library.error_message
            self.error_message_cfunc.argtypes = [ViSession_ctype, ViStatus_ctype, ctypes.POINTER(ViChar_ctype)]  # noqa: F405
            self.error_message_cfunc.restype = nidmm.python_types.ViStatus
        return self.error_message_cfunc(vi, error_code, error_message)

    def niDMM_error_query(self, vi, error_code, error_message):  # noqa: N802
        if self.error_query_cfunc is None:
            self.error_query_cfunc = self._library.error_query
            self.error_query_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViStatus_ctype), ctypes.POINTER(ViChar_ctype)]  # noqa: F405
            self.error_query_cfunc.restype = nidmm.python_types.ViStatus
        return self.error_query_cfunc(vi, error_code, error_message)

    def niDMM_init(self, resource_name, id_query, reset_device, vi):  # noqa: N802
        if self.init_cfunc is None:
            self.init_cfunc = self._library.init
            self.init_cfunc.argtypes = [ViString_ctype, ViBoolean_ctype, ViBoolean_ctype, ctypes.POINTER(ViSession_ctype)]  # noqa: F405
            self.init_cfunc.restype = nidmm.python_types.ViStatus
        return self.init_cfunc(resource_name, id_query, reset_device, vi)

    def niDMM_reset(self, vi):  # noqa: N802
        if self.reset_cfunc is None:
            self.reset_cfunc = self._library.reset
            self.reset_cfunc.argtypes = [ViSession_ctype]  # noqa: F405
            self.reset_cfunc.restype = nidmm.python_types.ViStatus
        return self.reset_cfunc(vi)

    def niDMM_revision_query(self, vi, instrument_driver_revision, firmware_revision):  # noqa: N802
        if self.revision_query_cfunc is None:
            self.revision_query_cfunc = self._library.revision_query
            self.revision_query_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViChar_ctype), ctypes.POINTER(ViChar_ctype)]  # noqa: F405
            self.revision_query_cfunc.restype = nidmm.python_types.ViStatus
        return self.revision_query_cfunc(vi, instrument_driver_revision, firmware_revision)

    def niDMM_self_test(self, vi, self_test_result, self_test_message):  # noqa: N802
        if self.self_test_cfunc is None:
            self.self_test_cfunc = self._library.self_test
            self.self_test_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViInt16_ctype), ctypes.POINTER(ViChar_ctype)]  # noqa: F405
            self.self_test_cfunc.restype = nidmm.python_types.ViStatus
        return self.self_test_cfunc(vi, self_test_result, self_test_message)
