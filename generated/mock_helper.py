# This file was generated

import ctypes
import platform
from unittest.mock import DEFAULT

import nidmm.ctypes_types
import nidmm.python_types

class IncorrectMockFunctionCall(Exception):
    def __init__(self, function, param = None):
        self.function = function
        self.param = param
        msg = "{0} called without setting side_effect".format(self.function)
        if param is not None:
            msg += " or setting the {0} parameter return value".format(self.param)
        super(Exception, self).__init__(msg)

class side_effects_helper(object):
    def __init__(self):
        self._defaults = {}
        self._defaults['InitWithOptions'] = {}
        self._defaults['InitWithOptions']['return'] = 0
        self._defaults['InitWithOptions']['newVi'] = None
        self._defaults['close'] = {}
        self._defaults['close']['return'] = 0
        self._defaults['GetError'] = {}
        self._defaults['GetError']['return'] = 0
        self._defaults['GetError']['errorCode'] = None
        self._defaults['GetErrorMessage'] = {}
        self._defaults['GetErrorMessage']['return'] = 0
        self._defaults['ClearError'] = {}
        self._defaults['ClearError']['return'] = 0
        self._defaults['reset'] = {}
        self._defaults['reset']['return'] = 0
        self._defaults['self_test'] = {}
        self._defaults['self_test']['return'] = 0
        self._defaults['self_test']['selfTestResult'] = None
        self._defaults['SelfCal'] = {}
        self._defaults['SelfCal']['return'] = 0
        self._defaults['revision_query'] = {}
        self._defaults['revision_query']['return'] = 0
        self._defaults['InvalidateAllAttributes'] = {}
        self._defaults['InvalidateAllAttributes']['return'] = 0
        self._defaults['ResetWithDefaults'] = {}
        self._defaults['ResetWithDefaults']['return'] = 0
        self._defaults['Disable'] = {}
        self._defaults['Disable']['return'] = 0
        self._defaults['GetMeasurementPeriod'] = {}
        self._defaults['GetMeasurementPeriod']['return'] = 0
        self._defaults['GetMeasurementPeriod']['period'] = None
        self._defaults['ConfigureTrigger'] = {}
        self._defaults['ConfigureTrigger']['return'] = 0
        self._defaults['Read'] = {}
        self._defaults['Read']['return'] = 0
        self._defaults['Read']['reading'] = None
        self._defaults['Fetch'] = {}
        self._defaults['Fetch']['return'] = 0
        self._defaults['Fetch']['reading'] = None
        self._defaults['Abort'] = {}
        self._defaults['Abort']['return'] = 0
        self._defaults['Initiate'] = {}
        self._defaults['Initiate']['return'] = 0
        self._defaults['IsOverRange'] = {}
        self._defaults['IsOverRange']['return'] = 0
        self._defaults['IsOverRange']['isOverRange'] = None
        self._defaults['IsUnderRange'] = {}
        self._defaults['IsUnderRange']['return'] = 0
        self._defaults['IsUnderRange']['isUnderRange'] = None
        self._defaults['ConfigureACBandwidth'] = {}
        self._defaults['ConfigureACBandwidth']['return'] = 0
        self._defaults['ConfigureFrequencyVoltageRange'] = {}
        self._defaults['ConfigureFrequencyVoltageRange']['return'] = 0
        self._defaults['ConfigureMeasCompleteDest'] = {}
        self._defaults['ConfigureMeasCompleteDest']['return'] = 0
        self._defaults['ConfigureMultiPoint'] = {}
        self._defaults['ConfigureMultiPoint']['return'] = 0
        self._defaults['ReadMultiPoint'] = {}
        self._defaults['ReadMultiPoint']['return'] = 0
        self._defaults['ReadMultiPoint']['actualPts'] = None
        self._defaults['FetchMultiPoint'] = {}
        self._defaults['FetchMultiPoint']['return'] = 0
        self._defaults['FetchMultiPoint']['actualPts'] = None
        self._defaults['ConfigureTriggerSlope'] = {}
        self._defaults['ConfigureTriggerSlope']['return'] = 0
        self._defaults['SendSoftwareTrigger'] = {}
        self._defaults['SendSoftwareTrigger']['return'] = 0
        self._defaults['GetApertureTimeInfo'] = {}
        self._defaults['GetApertureTimeInfo']['return'] = 0
        self._defaults['GetApertureTimeInfo']['apertureTime'] = None
        self._defaults['GetApertureTimeInfo']['apertureTimeUnits'] = None
        self._defaults['GetAutoRangeValue'] = {}
        self._defaults['GetAutoRangeValue']['return'] = 0
        self._defaults['GetAutoRangeValue']['autoRangeValue'] = None
        self._defaults['ConfigureAutoZeroMode'] = {}
        self._defaults['ConfigureAutoZeroMode']['return'] = 0
        self._defaults['ConfigurePowerLineFrequency'] = {}
        self._defaults['ConfigurePowerLineFrequency']['return'] = 0
        self._defaults['ConfigureMeasurementDigits'] = {}
        self._defaults['ConfigureMeasurementDigits']['return'] = 0
        self._defaults['ConfigureMeasurementAbsolute'] = {}
        self._defaults['ConfigureMeasurementAbsolute']['return'] = 0
        self._defaults['ConfigureMeasCompleteSlope'] = {}
        self._defaults['ConfigureMeasCompleteSlope']['return'] = 0
        self._defaults['ConfigureSampleTriggerSlope'] = {}
        self._defaults['ConfigureSampleTriggerSlope']['return'] = 0
        self._defaults['ReadStatus'] = {}
        self._defaults['ReadStatus']['return'] = 0
        self._defaults['ReadStatus']['acqBacklog'] = None
        self._defaults['ReadStatus']['acqDone'] = None
        self._defaults['ConfigureADCCalibration'] = {}
        self._defaults['ConfigureADCCalibration']['return'] = 0
        self._defaults['ConfigureOffsetCompOhms'] = {}
        self._defaults['ConfigureOffsetCompOhms']['return'] = 0
        self._defaults['ConfigureCurrentSource'] = {}
        self._defaults['ConfigureCurrentSource']['return'] = 0
        self._defaults['ConfigureCableCompType'] = {}
        self._defaults['ConfigureCableCompType']['return'] = 0
        self._defaults['PerformOpenCableComp'] = {}
        self._defaults['PerformOpenCableComp']['return'] = 0
        self._defaults['PerformOpenCableComp']['conductance'] = None
        self._defaults['PerformOpenCableComp']['susceptance'] = None
        self._defaults['PerformShortCableComp'] = {}
        self._defaults['PerformShortCableComp']['return'] = 0
        self._defaults['PerformShortCableComp']['resistance'] = None
        self._defaults['PerformShortCableComp']['reactance'] = None
        self._defaults['ConfigureOpenCableCompValues'] = {}
        self._defaults['ConfigureOpenCableCompValues']['return'] = 0
        self._defaults['ConfigureShortCableCompValues'] = {}
        self._defaults['ConfigureShortCableCompValues']['return'] = 0
        self._defaults['LockSession'] = {}
        self._defaults['LockSession']['return'] = 0
        self._defaults['LockSession']['callerHasLock'] = None
        self._defaults['UnlockSession'] = {}
        self._defaults['UnlockSession']['return'] = 0
        self._defaults['UnlockSession']['callerHasLock'] = None
        self._defaults['ConfigureWaveformAcquisition'] = {}
        self._defaults['ConfigureWaveformAcquisition']['return'] = 0
        self._defaults['ConfigureWaveformCoupling'] = {}
        self._defaults['ConfigureWaveformCoupling']['return'] = 0
        self._defaults['FetchWaveform'] = {}
        self._defaults['FetchWaveform']['return'] = 0
        self._defaults['FetchWaveform']['actualPoints'] = None
        self._defaults['ReadWaveform'] = {}
        self._defaults['ReadWaveform']['return'] = 0
        self._defaults['ReadWaveform']['actualPoints'] = None
        self._defaults['GetAttributeViInt32'] = {}
        self._defaults['GetAttributeViInt32']['return'] = 0
        self._defaults['GetAttributeViInt32']['value'] = None
        self._defaults['SetAttributeViInt32'] = {}
        self._defaults['SetAttributeViInt32']['return'] = 0
        self._defaults['GetAttributeViReal64'] = {}
        self._defaults['GetAttributeViReal64']['return'] = 0
        self._defaults['GetAttributeViReal64']['value'] = None
        self._defaults['SetAttributeViReal64'] = {}
        self._defaults['SetAttributeViReal64']['return'] = 0
        self._defaults['GetAttributeViString'] = {}
        self._defaults['GetAttributeViString']['return'] = 0
        self._defaults['SetAttributeViString'] = {}
        self._defaults['SetAttributeViString']['return'] = 0
        self._defaults['GetAttributeViSession'] = {}
        self._defaults['GetAttributeViSession']['return'] = 0
        self._defaults['GetAttributeViSession']['value'] = None
        self._defaults['SetAttributeViSession'] = {}
        self._defaults['SetAttributeViSession']['return'] = 0
        self._defaults['GetAttributeViBoolean'] = {}
        self._defaults['GetAttributeViBoolean']['return'] = 0
        self._defaults['GetAttributeViBoolean']['value'] = None
        self._defaults['SetAttributeViBoolean'] = {}
        self._defaults['SetAttributeViBoolean']['return'] = 0
        self._defaults['GetNextCoercionRecord'] = {}
        self._defaults['GetNextCoercionRecord']['return'] = 0
        self._defaults['GetNextInterchangeWarning'] = {}
        self._defaults['GetNextInterchangeWarning']['return'] = 0
        self._defaults['ResetInterchangeCheck'] = {}
        self._defaults['ResetInterchangeCheck']['return'] = 0
        self._defaults['ClearInterchangeWarnings'] = {}
        self._defaults['ClearInterchangeWarnings']['return'] = 0
        self._defaults['GetChannelName'] = {}
        self._defaults['GetChannelName']['return'] = 0
        self._defaults['GetCalCount'] = {}
        self._defaults['GetCalCount']['return'] = 0
        self._defaults['GetCalCount']['count'] = None
        self._defaults['GetLastCalTemp'] = {}
        self._defaults['GetLastCalTemp']['return'] = 0
        self._defaults['GetLastCalTemp']['temperature'] = None
        self._defaults['GetDevTemp'] = {}
        self._defaults['GetDevTemp']['return'] = 0
        self._defaults['GetDevTemp']['temperature'] = None
        self._defaults['ConfigureTransducerType'] = {}
        self._defaults['ConfigureTransducerType']['return'] = 0
        self._defaults['ConfigureThermocouple'] = {}
        self._defaults['ConfigureThermocouple']['return'] = 0
        self._defaults['ConfigureFixedRefJunction'] = {}
        self._defaults['ConfigureFixedRefJunction']['return'] = 0
        self._defaults['ConfigureRTDType'] = {}
        self._defaults['ConfigureRTDType']['return'] = 0
        self._defaults['ConfigureRTDCustom'] = {}
        self._defaults['ConfigureRTDCustom']['return'] = 0
        self._defaults['ConfigureThermistorType'] = {}
        self._defaults['ConfigureThermistorType']['return'] = 0
        self._defaults['ConfigureThermistorCustom'] = {}
        self._defaults['ConfigureThermistorCustom']['return'] = 0

    def __getitem__(self, func):
        return self._defaults[func]

    def __setitem__(self, func, val):
        self._defaults[func] = val

    def niDMM_InitWithOptions_side_effect(self, resource_name, id_query, reset_device, options_string, new_vi):
        new_vi.contents.value = self._defaults['InitWithOptions']['newVi']
        return self._defaults['InitWithOptions']['return']

    def niDMM_close_side_effect(self, vi):
        return self._defaults['close']['return']

    def niDMM_GetError_side_effect(self, vi, error_code, buffer_size, description):
        error_code.contents.value = self._defaults['GetError']['errorCode']
        return self._defaults['GetError']['return']

    def niDMM_GetErrorMessage_side_effect(self, vi, error_code, buffer_size, err_message):
        return self._defaults['GetErrorMessage']['return']

    def niDMM_ClearError_side_effect(self, vi):
        return self._defaults['ClearError']['return']

    def niDMM_reset_side_effect(self, vi):
        return self._defaults['reset']['return']

    def niDMM_self_test_side_effect(self, vi, self_test_result, self_test_message):
        self_test_result.contents.value = self._defaults['self_test']['selfTestResult']
        return self._defaults['self_test']['return']

    def niDMM_SelfCal_side_effect(self, vi):
        return self._defaults['SelfCal']['return']

    def niDMM_revision_query_side_effect(self, vi, driver_rev, instr_rev):
        return self._defaults['revision_query']['return']

    def niDMM_InvalidateAllAttributes_side_effect(self, vi):
        return self._defaults['InvalidateAllAttributes']['return']

    def niDMM_ResetWithDefaults_side_effect(self, vi):
        return self._defaults['ResetWithDefaults']['return']

    def niDMM_Disable_side_effect(self, vi):
        return self._defaults['Disable']['return']

    def niDMM_GetMeasurementPeriod_side_effect(self, vi, period):
        period.contents.value = self._defaults['GetMeasurementPeriod']['period']
        return self._defaults['GetMeasurementPeriod']['return']

    def niDMM_ConfigureTrigger_side_effect(self, vi, trig_source, trigger_delay):
        return self._defaults['ConfigureTrigger']['return']

    def niDMM_Read_side_effect(self, vi, max_time, reading):
        reading.contents.value = self._defaults['Read']['reading']
        return self._defaults['Read']['return']

    def niDMM_Fetch_side_effect(self, vi, max_time, reading):
        reading.contents.value = self._defaults['Fetch']['reading']
        return self._defaults['Fetch']['return']

    def niDMM_Abort_side_effect(self, vi):
        return self._defaults['Abort']['return']

    def niDMM_Initiate_side_effect(self, vi):
        return self._defaults['Initiate']['return']

    def niDMM_IsOverRange_side_effect(self, vi, measurement_value, is_over_range):
        is_over_range.contents.value = self._defaults['IsOverRange']['isOverRange']
        return self._defaults['IsOverRange']['return']

    def niDMM_IsUnderRange_side_effect(self, vi, measurement_value, is_under_range):
        is_under_range.contents.value = self._defaults['IsUnderRange']['isUnderRange']
        return self._defaults['IsUnderRange']['return']

    def niDMM_ConfigureACBandwidth_side_effect(self, vi, min_freq, max_freq):
        return self._defaults['ConfigureACBandwidth']['return']

    def niDMM_ConfigureFrequencyVoltageRange_side_effect(self, vi, frequency_voltage_range):
        return self._defaults['ConfigureFrequencyVoltageRange']['return']

    def niDMM_ConfigureMeasCompleteDest_side_effect(self, vi, destination):
        return self._defaults['ConfigureMeasCompleteDest']['return']

    def niDMM_ConfigureMultiPoint_side_effect(self, vi, trigger_count, sample_count, sample_trigger, sample_interval):
        return self._defaults['ConfigureMultiPoint']['return']

    def niDMM_ReadMultiPoint_side_effect(self, vi, max_time, array_size, reading_array, actual_pts):
        actual_pts.contents.value = self._defaults['ReadMultiPoint']['actualPts']
        return self._defaults['ReadMultiPoint']['return']

    def niDMM_FetchMultiPoint_side_effect(self, vi, max_time, array_size, reading_array, actual_pts):
        actual_pts.contents.value = self._defaults['FetchMultiPoint']['actualPts']
        return self._defaults['FetchMultiPoint']['return']

    def niDMM_ConfigureTriggerSlope_side_effect(self, vi, polarity):
        return self._defaults['ConfigureTriggerSlope']['return']

    def niDMM_SendSoftwareTrigger_side_effect(self, vi):
        return self._defaults['SendSoftwareTrigger']['return']

    def niDMM_GetApertureTimeInfo_side_effect(self, vi, aperture_time, aperture_time_units):
        aperture_time.contents.value = self._defaults['GetApertureTimeInfo']['apertureTime']
        aperture_time_units.contents.value = self._defaults['GetApertureTimeInfo']['apertureTimeUnits']
        return self._defaults['GetApertureTimeInfo']['return']

    def niDMM_GetAutoRangeValue_side_effect(self, vi, auto_range_value):
        auto_range_value.contents.value = self._defaults['GetAutoRangeValue']['autoRangeValue']
        return self._defaults['GetAutoRangeValue']['return']

    def niDMM_ConfigureAutoZeroMode_side_effect(self, vi, auto_zero_mode):
        return self._defaults['ConfigureAutoZeroMode']['return']

    def niDMM_ConfigurePowerLineFrequency_side_effect(self, vi, frequency):
        return self._defaults['ConfigurePowerLineFrequency']['return']

    def niDMM_ConfigureMeasurementDigits_side_effect(self, vi, meas_function, range, resolution_digits):
        return self._defaults['ConfigureMeasurementDigits']['return']

    def niDMM_ConfigureMeasurementAbsolute_side_effect(self, vi, meas_function, range, resolution_absolute):
        return self._defaults['ConfigureMeasurementAbsolute']['return']

    def niDMM_ConfigureMeasCompleteSlope_side_effect(self, vi, polarity):
        return self._defaults['ConfigureMeasCompleteSlope']['return']

    def niDMM_ConfigureSampleTriggerSlope_side_effect(self, vi, polarity):
        return self._defaults['ConfigureSampleTriggerSlope']['return']

    def niDMM_ReadStatus_side_effect(self, vi, acq_backlog, acq_done):
        acq_backlog.contents.value = self._defaults['ReadStatus']['acqBacklog']
        acq_done.contents.value = self._defaults['ReadStatus']['acqDone']
        return self._defaults['ReadStatus']['return']

    def niDMM_ConfigureADCCalibration_side_effect(self, vi, adc_gain_comp):
        return self._defaults['ConfigureADCCalibration']['return']

    def niDMM_ConfigureOffsetCompOhms_side_effect(self, vi, offset_comp_ohms):
        return self._defaults['ConfigureOffsetCompOhms']['return']

    def niDMM_ConfigureCurrentSource_side_effect(self, vi, diode_current_src):
        return self._defaults['ConfigureCurrentSource']['return']

    def niDMM_ConfigureCableCompType_side_effect(self, vi, type_of_compensation):
        return self._defaults['ConfigureCableCompType']['return']

    def niDMM_PerformOpenCableComp_side_effect(self, vi, conductance, susceptance):
        conductance.contents.value = self._defaults['PerformOpenCableComp']['conductance']
        susceptance.contents.value = self._defaults['PerformOpenCableComp']['susceptance']
        return self._defaults['PerformOpenCableComp']['return']

    def niDMM_PerformShortCableComp_side_effect(self, vi, resistance, reactance):
        resistance.contents.value = self._defaults['PerformShortCableComp']['resistance']
        reactance.contents.value = self._defaults['PerformShortCableComp']['reactance']
        return self._defaults['PerformShortCableComp']['return']

    def niDMM_ConfigureOpenCableCompValues_side_effect(self, vi, conductance, susceptance):
        return self._defaults['ConfigureOpenCableCompValues']['return']

    def niDMM_ConfigureShortCableCompValues_side_effect(self, vi, resistance, reactance):
        return self._defaults['ConfigureShortCableCompValues']['return']

    def niDMM_LockSession_side_effect(self, vi, caller_has_lock):
        caller_has_lock.contents.value = self._defaults['LockSession']['callerHasLock']
        return self._defaults['LockSession']['return']

    def niDMM_UnlockSession_side_effect(self, vi, caller_has_lock):
        caller_has_lock.contents.value = self._defaults['UnlockSession']['callerHasLock']
        return self._defaults['UnlockSession']['return']

    def niDMM_ConfigureWaveformAcquisition_side_effect(self, vi, function, range, rate, waveform_points):
        return self._defaults['ConfigureWaveformAcquisition']['return']

    def niDMM_ConfigureWaveformCoupling_side_effect(self, vi, coupling):
        return self._defaults['ConfigureWaveformCoupling']['return']

    def niDMM_FetchWaveform_side_effect(self, vi, max_time, array_size, waveform_array, actual_points):
        actual_points.contents.value = self._defaults['FetchWaveform']['actualPoints']
        return self._defaults['FetchWaveform']['return']

    def niDMM_ReadWaveform_side_effect(self, vi, max_time, array_size, waveform_array, actual_points):
        actual_points.contents.value = self._defaults['ReadWaveform']['actualPoints']
        return self._defaults['ReadWaveform']['return']

    def niDMM_GetAttributeViInt32_side_effect(self, vi, channel_name, attribute_id, value):
        value.contents.value = self._defaults['GetAttributeViInt32']['value']
        return self._defaults['GetAttributeViInt32']['return']

    def niDMM_SetAttributeViInt32_side_effect(self, vi, channel_name, attribute_id, value):
        return self._defaults['SetAttributeViInt32']['return']

    def niDMM_GetAttributeViReal64_side_effect(self, vi, channel_name, attribute_id, value):
        value.contents.value = self._defaults['GetAttributeViReal64']['value']
        return self._defaults['GetAttributeViReal64']['return']

    def niDMM_SetAttributeViReal64_side_effect(self, vi, channel_name, attribute_id, value):
        return self._defaults['SetAttributeViReal64']['return']

    def niDMM_GetAttributeViString_side_effect(self, vi, channel_name, attribute_id, buf_size, value):
        return self._defaults['GetAttributeViString']['return']

    def niDMM_SetAttributeViString_side_effect(self, vi, channel_name, attribute_id, value):
        return self._defaults['SetAttributeViString']['return']

    def niDMM_GetAttributeViSession_side_effect(self, vi, channel_name, attribute_id, value):
        value.contents.value = self._defaults['GetAttributeViSession']['value']
        return self._defaults['GetAttributeViSession']['return']

    def niDMM_SetAttributeViSession_side_effect(self, vi, channel_name, attribute_id, value):
        return self._defaults['SetAttributeViSession']['return']

    def niDMM_GetAttributeViBoolean_side_effect(self, vi, channel_name, attribute_id, value):
        value.contents.value = self._defaults['GetAttributeViBoolean']['value']
        return self._defaults['GetAttributeViBoolean']['return']

    def niDMM_SetAttributeViBoolean_side_effect(self, vi, channel_name, attribute_id, value):
        return self._defaults['SetAttributeViBoolean']['return']

    def niDMM_GetNextCoercionRecord_side_effect(self, vi, buffer_size, record):
        return self._defaults['GetNextCoercionRecord']['return']

    def niDMM_GetNextInterchangeWarning_side_effect(self, vi, buffer_size, warn_string):
        return self._defaults['GetNextInterchangeWarning']['return']

    def niDMM_ResetInterchangeCheck_side_effect(self, vi):
        return self._defaults['ResetInterchangeCheck']['return']

    def niDMM_ClearInterchangeWarnings_side_effect(self, vi):
        return self._defaults['ClearInterchangeWarnings']['return']

    def niDMM_GetChannelName_side_effect(self, vi, index, buffer_size, name):
        return self._defaults['GetChannelName']['return']

    def niDMM_GetCalCount_side_effect(self, vi, cal_type, count):
        count.contents.value = self._defaults['GetCalCount']['count']
        return self._defaults['GetCalCount']['return']

    def niDMM_GetLastCalTemp_side_effect(self, vi, cal_type, temperature):
        temperature.contents.value = self._defaults['GetLastCalTemp']['temperature']
        return self._defaults['GetLastCalTemp']['return']

    def niDMM_GetDevTemp_side_effect(self, vi, reserved, temperature):
        temperature.contents.value = self._defaults['GetDevTemp']['temperature']
        return self._defaults['GetDevTemp']['return']

    def niDMM_ConfigureTransducerType_side_effect(self, vi, transducer_type):
        return self._defaults['ConfigureTransducerType']['return']

    def niDMM_ConfigureThermocouple_side_effect(self, vi, thermocouple_type, ref_junction_type):
        return self._defaults['ConfigureThermocouple']['return']

    def niDMM_ConfigureFixedRefJunction_side_effect(self, vi, fixed_ref_junction):
        return self._defaults['ConfigureFixedRefJunction']['return']

    def niDMM_ConfigureRTDType_side_effect(self, vi, rtd_type, resistance):
        return self._defaults['ConfigureRTDType']['return']

    def niDMM_ConfigureRTDCustom_side_effect(self, vi, a, b, c):
        return self._defaults['ConfigureRTDCustom']['return']

    def niDMM_ConfigureThermistorType_side_effect(self, vi, thermistor_type):
        return self._defaults['ConfigureThermistorType']['return']

    def niDMM_ConfigureThermistorCustom_side_effect(self, vi, a, b, c):
        return self._defaults['ConfigureThermistorCustom']['return']


# Helper function to setup Mock object with default side affects and return values
def set_side_effects_and_return_values(mock_library):
    mock_library.niDMM_InitWithOptions.side_effect = IncorrectMockFunctionCall("niDMM_InitWithOptions")
    mock_library.niDMM_InitWithOptions.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_close.side_effect = IncorrectMockFunctionCall("niDMM_close")
    mock_library.niDMM_close.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_GetError.side_effect = IncorrectMockFunctionCall("niDMM_GetError")
    mock_library.niDMM_GetError.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_GetErrorMessage.side_effect = IncorrectMockFunctionCall("niDMM_GetErrorMessage")
    mock_library.niDMM_GetErrorMessage.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_ClearError.side_effect = IncorrectMockFunctionCall("niDMM_ClearError")
    mock_library.niDMM_ClearError.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_reset.side_effect = IncorrectMockFunctionCall("niDMM_reset")
    mock_library.niDMM_reset.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_self_test.side_effect = IncorrectMockFunctionCall("niDMM_self_test")
    mock_library.niDMM_self_test.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_SelfCal.side_effect = IncorrectMockFunctionCall("niDMM_SelfCal")
    mock_library.niDMM_SelfCal.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_revision_query.side_effect = IncorrectMockFunctionCall("niDMM_revision_query")
    mock_library.niDMM_revision_query.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_InvalidateAllAttributes.side_effect = IncorrectMockFunctionCall("niDMM_InvalidateAllAttributes")
    mock_library.niDMM_InvalidateAllAttributes.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_ResetWithDefaults.side_effect = IncorrectMockFunctionCall("niDMM_ResetWithDefaults")
    mock_library.niDMM_ResetWithDefaults.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_Disable.side_effect = IncorrectMockFunctionCall("niDMM_Disable")
    mock_library.niDMM_Disable.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_GetMeasurementPeriod.side_effect = IncorrectMockFunctionCall("niDMM_GetMeasurementPeriod")
    mock_library.niDMM_GetMeasurementPeriod.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_ConfigureTrigger.side_effect = IncorrectMockFunctionCall("niDMM_ConfigureTrigger")
    mock_library.niDMM_ConfigureTrigger.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_Read.side_effect = IncorrectMockFunctionCall("niDMM_Read")
    mock_library.niDMM_Read.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_Fetch.side_effect = IncorrectMockFunctionCall("niDMM_Fetch")
    mock_library.niDMM_Fetch.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_Abort.side_effect = IncorrectMockFunctionCall("niDMM_Abort")
    mock_library.niDMM_Abort.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_Initiate.side_effect = IncorrectMockFunctionCall("niDMM_Initiate")
    mock_library.niDMM_Initiate.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_IsOverRange.side_effect = IncorrectMockFunctionCall("niDMM_IsOverRange")
    mock_library.niDMM_IsOverRange.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_IsUnderRange.side_effect = IncorrectMockFunctionCall("niDMM_IsUnderRange")
    mock_library.niDMM_IsUnderRange.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_ConfigureACBandwidth.side_effect = IncorrectMockFunctionCall("niDMM_ConfigureACBandwidth")
    mock_library.niDMM_ConfigureACBandwidth.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_ConfigureFrequencyVoltageRange.side_effect = IncorrectMockFunctionCall("niDMM_ConfigureFrequencyVoltageRange")
    mock_library.niDMM_ConfigureFrequencyVoltageRange.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_ConfigureMeasCompleteDest.side_effect = IncorrectMockFunctionCall("niDMM_ConfigureMeasCompleteDest")
    mock_library.niDMM_ConfigureMeasCompleteDest.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_ConfigureMultiPoint.side_effect = IncorrectMockFunctionCall("niDMM_ConfigureMultiPoint")
    mock_library.niDMM_ConfigureMultiPoint.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_ReadMultiPoint.side_effect = IncorrectMockFunctionCall("niDMM_ReadMultiPoint")
    mock_library.niDMM_ReadMultiPoint.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_FetchMultiPoint.side_effect = IncorrectMockFunctionCall("niDMM_FetchMultiPoint")
    mock_library.niDMM_FetchMultiPoint.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_ConfigureTriggerSlope.side_effect = IncorrectMockFunctionCall("niDMM_ConfigureTriggerSlope")
    mock_library.niDMM_ConfigureTriggerSlope.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_SendSoftwareTrigger.side_effect = IncorrectMockFunctionCall("niDMM_SendSoftwareTrigger")
    mock_library.niDMM_SendSoftwareTrigger.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_GetApertureTimeInfo.side_effect = IncorrectMockFunctionCall("niDMM_GetApertureTimeInfo")
    mock_library.niDMM_GetApertureTimeInfo.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_GetAutoRangeValue.side_effect = IncorrectMockFunctionCall("niDMM_GetAutoRangeValue")
    mock_library.niDMM_GetAutoRangeValue.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_ConfigureAutoZeroMode.side_effect = IncorrectMockFunctionCall("niDMM_ConfigureAutoZeroMode")
    mock_library.niDMM_ConfigureAutoZeroMode.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_ConfigurePowerLineFrequency.side_effect = IncorrectMockFunctionCall("niDMM_ConfigurePowerLineFrequency")
    mock_library.niDMM_ConfigurePowerLineFrequency.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_ConfigureMeasurementDigits.side_effect = IncorrectMockFunctionCall("niDMM_ConfigureMeasurementDigits")
    mock_library.niDMM_ConfigureMeasurementDigits.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_ConfigureMeasurementAbsolute.side_effect = IncorrectMockFunctionCall("niDMM_ConfigureMeasurementAbsolute")
    mock_library.niDMM_ConfigureMeasurementAbsolute.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_ConfigureMeasCompleteSlope.side_effect = IncorrectMockFunctionCall("niDMM_ConfigureMeasCompleteSlope")
    mock_library.niDMM_ConfigureMeasCompleteSlope.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_ConfigureSampleTriggerSlope.side_effect = IncorrectMockFunctionCall("niDMM_ConfigureSampleTriggerSlope")
    mock_library.niDMM_ConfigureSampleTriggerSlope.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_ReadStatus.side_effect = IncorrectMockFunctionCall("niDMM_ReadStatus")
    mock_library.niDMM_ReadStatus.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_ConfigureADCCalibration.side_effect = IncorrectMockFunctionCall("niDMM_ConfigureADCCalibration")
    mock_library.niDMM_ConfigureADCCalibration.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_ConfigureOffsetCompOhms.side_effect = IncorrectMockFunctionCall("niDMM_ConfigureOffsetCompOhms")
    mock_library.niDMM_ConfigureOffsetCompOhms.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_ConfigureCurrentSource.side_effect = IncorrectMockFunctionCall("niDMM_ConfigureCurrentSource")
    mock_library.niDMM_ConfigureCurrentSource.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_ConfigureCableCompType.side_effect = IncorrectMockFunctionCall("niDMM_ConfigureCableCompType")
    mock_library.niDMM_ConfigureCableCompType.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_PerformOpenCableComp.side_effect = IncorrectMockFunctionCall("niDMM_PerformOpenCableComp")
    mock_library.niDMM_PerformOpenCableComp.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_PerformShortCableComp.side_effect = IncorrectMockFunctionCall("niDMM_PerformShortCableComp")
    mock_library.niDMM_PerformShortCableComp.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_ConfigureOpenCableCompValues.side_effect = IncorrectMockFunctionCall("niDMM_ConfigureOpenCableCompValues")
    mock_library.niDMM_ConfigureOpenCableCompValues.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_ConfigureShortCableCompValues.side_effect = IncorrectMockFunctionCall("niDMM_ConfigureShortCableCompValues")
    mock_library.niDMM_ConfigureShortCableCompValues.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_LockSession.side_effect = IncorrectMockFunctionCall("niDMM_LockSession")
    mock_library.niDMM_LockSession.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_UnlockSession.side_effect = IncorrectMockFunctionCall("niDMM_UnlockSession")
    mock_library.niDMM_UnlockSession.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_ConfigureWaveformAcquisition.side_effect = IncorrectMockFunctionCall("niDMM_ConfigureWaveformAcquisition")
    mock_library.niDMM_ConfigureWaveformAcquisition.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_ConfigureWaveformCoupling.side_effect = IncorrectMockFunctionCall("niDMM_ConfigureWaveformCoupling")
    mock_library.niDMM_ConfigureWaveformCoupling.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_FetchWaveform.side_effect = IncorrectMockFunctionCall("niDMM_FetchWaveform")
    mock_library.niDMM_FetchWaveform.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_ReadWaveform.side_effect = IncorrectMockFunctionCall("niDMM_ReadWaveform")
    mock_library.niDMM_ReadWaveform.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_GetAttributeViInt32.side_effect = IncorrectMockFunctionCall("niDMM_GetAttributeViInt32")
    mock_library.niDMM_GetAttributeViInt32.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_SetAttributeViInt32.side_effect = IncorrectMockFunctionCall("niDMM_SetAttributeViInt32")
    mock_library.niDMM_SetAttributeViInt32.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_GetAttributeViReal64.side_effect = IncorrectMockFunctionCall("niDMM_GetAttributeViReal64")
    mock_library.niDMM_GetAttributeViReal64.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_SetAttributeViReal64.side_effect = IncorrectMockFunctionCall("niDMM_SetAttributeViReal64")
    mock_library.niDMM_SetAttributeViReal64.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_GetAttributeViString.side_effect = IncorrectMockFunctionCall("niDMM_GetAttributeViString")
    mock_library.niDMM_GetAttributeViString.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_SetAttributeViString.side_effect = IncorrectMockFunctionCall("niDMM_SetAttributeViString")
    mock_library.niDMM_SetAttributeViString.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_GetAttributeViSession.side_effect = IncorrectMockFunctionCall("niDMM_GetAttributeViSession")
    mock_library.niDMM_GetAttributeViSession.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_SetAttributeViSession.side_effect = IncorrectMockFunctionCall("niDMM_SetAttributeViSession")
    mock_library.niDMM_SetAttributeViSession.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_GetAttributeViBoolean.side_effect = IncorrectMockFunctionCall("niDMM_GetAttributeViBoolean")
    mock_library.niDMM_GetAttributeViBoolean.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_SetAttributeViBoolean.side_effect = IncorrectMockFunctionCall("niDMM_SetAttributeViBoolean")
    mock_library.niDMM_SetAttributeViBoolean.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_GetNextCoercionRecord.side_effect = IncorrectMockFunctionCall("niDMM_GetNextCoercionRecord")
    mock_library.niDMM_GetNextCoercionRecord.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_GetNextInterchangeWarning.side_effect = IncorrectMockFunctionCall("niDMM_GetNextInterchangeWarning")
    mock_library.niDMM_GetNextInterchangeWarning.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_ResetInterchangeCheck.side_effect = IncorrectMockFunctionCall("niDMM_ResetInterchangeCheck")
    mock_library.niDMM_ResetInterchangeCheck.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_ClearInterchangeWarnings.side_effect = IncorrectMockFunctionCall("niDMM_ClearInterchangeWarnings")
    mock_library.niDMM_ClearInterchangeWarnings.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_GetChannelName.side_effect = IncorrectMockFunctionCall("niDMM_GetChannelName")
    mock_library.niDMM_GetChannelName.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_GetCalCount.side_effect = IncorrectMockFunctionCall("niDMM_GetCalCount")
    mock_library.niDMM_GetCalCount.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_GetLastCalTemp.side_effect = IncorrectMockFunctionCall("niDMM_GetLastCalTemp")
    mock_library.niDMM_GetLastCalTemp.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_GetDevTemp.side_effect = IncorrectMockFunctionCall("niDMM_GetDevTemp")
    mock_library.niDMM_GetDevTemp.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_ConfigureTransducerType.side_effect = IncorrectMockFunctionCall("niDMM_ConfigureTransducerType")
    mock_library.niDMM_ConfigureTransducerType.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_ConfigureThermocouple.side_effect = IncorrectMockFunctionCall("niDMM_ConfigureThermocouple")
    mock_library.niDMM_ConfigureThermocouple.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_ConfigureFixedRefJunction.side_effect = IncorrectMockFunctionCall("niDMM_ConfigureFixedRefJunction")
    mock_library.niDMM_ConfigureFixedRefJunction.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_ConfigureRTDType.side_effect = IncorrectMockFunctionCall("niDMM_ConfigureRTDType")
    mock_library.niDMM_ConfigureRTDType.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_ConfigureRTDCustom.side_effect = IncorrectMockFunctionCall("niDMM_ConfigureRTDCustom")
    mock_library.niDMM_ConfigureRTDCustom.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_ConfigureThermistorType.side_effect = IncorrectMockFunctionCall("niDMM_ConfigureThermistorType")
    mock_library.niDMM_ConfigureThermistorType.return_value = nidmm.python_types.ViStatus(0)
    mock_library.niDMM_ConfigureThermistorCustom.side_effect = IncorrectMockFunctionCall("niDMM_ConfigureThermistorCustom")
    mock_library.niDMM_ConfigureThermistorCustom.return_value = nidmm.python_types.ViStatus(0)




