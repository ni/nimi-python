# This file was generated

import ctypes

import nidcpower.ctypes_types
import nidcpower.python_types


class MockFunctionCallError(Exception):
    def __init__(self, function, param=None):
        self.function = function
        self.param = param
        msg = "{0} called without setting side_effect".format(self.function)
        if param is not None:
            msg += " or setting the {0} parameter return value".format(self.param)
        super(Exception, self).__init__(msg)


class SideEffectsHelper(object):
    def __init__(self):
        self._defaults = {}
        self._defaults['Abort'] = {}
        self._defaults['Abort']['return'] = 0
        self._defaults['CalAdjustCurrentLimit'] = {}
        self._defaults['CalAdjustCurrentLimit']['return'] = 0
        self._defaults['CalAdjustCurrentMeasurement'] = {}
        self._defaults['CalAdjustCurrentMeasurement']['return'] = 0
        self._defaults['CalAdjustInternalReference'] = {}
        self._defaults['CalAdjustInternalReference']['return'] = 0
        self._defaults['CalAdjustOutputResistance'] = {}
        self._defaults['CalAdjustOutputResistance']['return'] = 0
        self._defaults['CalAdjustResidualCurrentOffset'] = {}
        self._defaults['CalAdjustResidualCurrentOffset']['return'] = 0
        self._defaults['CalAdjustResidualVoltageOffset'] = {}
        self._defaults['CalAdjustResidualVoltageOffset']['return'] = 0
        self._defaults['CalAdjustVoltageLevel'] = {}
        self._defaults['CalAdjustVoltageLevel']['return'] = 0
        self._defaults['CalAdjustVoltageMeasurement'] = {}
        self._defaults['CalAdjustVoltageMeasurement']['return'] = 0
        self._defaults['CalSelfCalibrate'] = {}
        self._defaults['CalSelfCalibrate']['return'] = 0
        self._defaults['ChangeExtCalPassword'] = {}
        self._defaults['ChangeExtCalPassword']['return'] = 0
        self._defaults['ClearError'] = {}
        self._defaults['ClearError']['return'] = 0
        self._defaults['ClearInterchangeWarnings'] = {}
        self._defaults['ClearInterchangeWarnings']['return'] = 0
        self._defaults['CloseExtCal'] = {}
        self._defaults['CloseExtCal']['return'] = 0
        self._defaults['Commit'] = {}
        self._defaults['Commit']['return'] = 0
        self._defaults['ConfigureApertureTime'] = {}
        self._defaults['ConfigureApertureTime']['return'] = 0
        self._defaults['ConfigureAutoZero'] = {}
        self._defaults['ConfigureAutoZero']['return'] = 0
        self._defaults['ConfigureCurrentLevel'] = {}
        self._defaults['ConfigureCurrentLevel']['return'] = 0
        self._defaults['ConfigureCurrentLevelRange'] = {}
        self._defaults['ConfigureCurrentLevelRange']['return'] = 0
        self._defaults['ConfigureCurrentLimit'] = {}
        self._defaults['ConfigureCurrentLimit']['return'] = 0
        self._defaults['ConfigureCurrentLimitRange'] = {}
        self._defaults['ConfigureCurrentLimitRange']['return'] = 0
        self._defaults['ConfigureDigitalEdgeMeasureTrigger'] = {}
        self._defaults['ConfigureDigitalEdgeMeasureTrigger']['return'] = 0
        self._defaults['ConfigureDigitalEdgePulseTrigger'] = {}
        self._defaults['ConfigureDigitalEdgePulseTrigger']['return'] = 0
        self._defaults['ConfigureDigitalEdgeSequenceAdvanceTrigger'] = {}
        self._defaults['ConfigureDigitalEdgeSequenceAdvanceTrigger']['return'] = 0
        self._defaults['ConfigureDigitalEdgeSourceTrigger'] = {}
        self._defaults['ConfigureDigitalEdgeSourceTrigger']['return'] = 0
        self._defaults['ConfigureDigitalEdgeStartTrigger'] = {}
        self._defaults['ConfigureDigitalEdgeStartTrigger']['return'] = 0
        self._defaults['ConfigureOutputEnabled'] = {}
        self._defaults['ConfigureOutputEnabled']['return'] = 0
        self._defaults['ConfigureOutputFunction'] = {}
        self._defaults['ConfigureOutputFunction']['return'] = 0
        self._defaults['ConfigureOutputRange'] = {}
        self._defaults['ConfigureOutputRange']['return'] = 0
        self._defaults['ConfigureOutputResistance'] = {}
        self._defaults['ConfigureOutputResistance']['return'] = 0
        self._defaults['ConfigurePowerLineFrequency'] = {}
        self._defaults['ConfigurePowerLineFrequency']['return'] = 0
        self._defaults['ConfigurePulseBiasCurrentLevel'] = {}
        self._defaults['ConfigurePulseBiasCurrentLevel']['return'] = 0
        self._defaults['ConfigurePulseBiasCurrentLimit'] = {}
        self._defaults['ConfigurePulseBiasCurrentLimit']['return'] = 0
        self._defaults['ConfigurePulseBiasVoltageLevel'] = {}
        self._defaults['ConfigurePulseBiasVoltageLevel']['return'] = 0
        self._defaults['ConfigurePulseBiasVoltageLimit'] = {}
        self._defaults['ConfigurePulseBiasVoltageLimit']['return'] = 0
        self._defaults['ConfigurePulseCurrentLevel'] = {}
        self._defaults['ConfigurePulseCurrentLevel']['return'] = 0
        self._defaults['ConfigurePulseCurrentLevelRange'] = {}
        self._defaults['ConfigurePulseCurrentLevelRange']['return'] = 0
        self._defaults['ConfigurePulseCurrentLimit'] = {}
        self._defaults['ConfigurePulseCurrentLimit']['return'] = 0
        self._defaults['ConfigurePulseCurrentLimitRange'] = {}
        self._defaults['ConfigurePulseCurrentLimitRange']['return'] = 0
        self._defaults['ConfigurePulseVoltageLevel'] = {}
        self._defaults['ConfigurePulseVoltageLevel']['return'] = 0
        self._defaults['ConfigurePulseVoltageLevelRange'] = {}
        self._defaults['ConfigurePulseVoltageLevelRange']['return'] = 0
        self._defaults['ConfigurePulseVoltageLimit'] = {}
        self._defaults['ConfigurePulseVoltageLimit']['return'] = 0
        self._defaults['ConfigurePulseVoltageLimitRange'] = {}
        self._defaults['ConfigurePulseVoltageLimitRange']['return'] = 0
        self._defaults['ConfigureSense'] = {}
        self._defaults['ConfigureSense']['return'] = 0
        self._defaults['ConfigureSoftwareEdgeMeasureTrigger'] = {}
        self._defaults['ConfigureSoftwareEdgeMeasureTrigger']['return'] = 0
        self._defaults['ConfigureSoftwareEdgePulseTrigger'] = {}
        self._defaults['ConfigureSoftwareEdgePulseTrigger']['return'] = 0
        self._defaults['ConfigureSoftwareEdgeSequenceAdvanceTrigger'] = {}
        self._defaults['ConfigureSoftwareEdgeSequenceAdvanceTrigger']['return'] = 0
        self._defaults['ConfigureSoftwareEdgeSourceTrigger'] = {}
        self._defaults['ConfigureSoftwareEdgeSourceTrigger']['return'] = 0
        self._defaults['ConfigureSoftwareEdgeStartTrigger'] = {}
        self._defaults['ConfigureSoftwareEdgeStartTrigger']['return'] = 0
        self._defaults['ConfigureSourceMode'] = {}
        self._defaults['ConfigureSourceMode']['return'] = 0
        self._defaults['ConfigureVoltageLevel'] = {}
        self._defaults['ConfigureVoltageLevel']['return'] = 0
        self._defaults['ConfigureVoltageLevelRange'] = {}
        self._defaults['ConfigureVoltageLevelRange']['return'] = 0
        self._defaults['ConfigureVoltageLimit'] = {}
        self._defaults['ConfigureVoltageLimit']['return'] = 0
        self._defaults['ConfigureVoltageLimitRange'] = {}
        self._defaults['ConfigureVoltageLimitRange']['return'] = 0
        self._defaults['ConnectInternalReference'] = {}
        self._defaults['ConnectInternalReference']['return'] = 0
        self._defaults['CreateAdvancedSequence'] = {}
        self._defaults['CreateAdvancedSequence']['return'] = 0
        self._defaults['CreateAdvancedSequenceStep'] = {}
        self._defaults['CreateAdvancedSequenceStep']['return'] = 0
        self._defaults['DeleteAdvancedSequence'] = {}
        self._defaults['DeleteAdvancedSequence']['return'] = 0
        self._defaults['Disable'] = {}
        self._defaults['Disable']['return'] = 0
        self._defaults['DisablePulseTrigger'] = {}
        self._defaults['DisablePulseTrigger']['return'] = 0
        self._defaults['DisableSequenceAdvanceTrigger'] = {}
        self._defaults['DisableSequenceAdvanceTrigger']['return'] = 0
        self._defaults['DisableSourceTrigger'] = {}
        self._defaults['DisableSourceTrigger']['return'] = 0
        self._defaults['DisableStartTrigger'] = {}
        self._defaults['DisableStartTrigger']['return'] = 0
        self._defaults['ExportSignal'] = {}
        self._defaults['ExportSignal']['return'] = 0
        self._defaults['FetchMultiple'] = {}
        self._defaults['FetchMultiple']['return'] = 0
        self._defaults['FetchMultiple']['voltageMeasurements'] = None
        self._defaults['FetchMultiple']['currentMeasurements'] = None
        self._defaults['FetchMultiple']['inCompliance'] = None
        self._defaults['FetchMultiple']['actualCount'] = None
        self._defaults['GetAttributeViBoolean'] = {}
        self._defaults['GetAttributeViBoolean']['return'] = 0
        self._defaults['GetAttributeViBoolean']['attributeValue'] = None
        self._defaults['GetAttributeViInt32'] = {}
        self._defaults['GetAttributeViInt32']['return'] = 0
        self._defaults['GetAttributeViInt32']['attributeValue'] = None
        self._defaults['GetAttributeViInt64'] = {}
        self._defaults['GetAttributeViInt64']['return'] = 0
        self._defaults['GetAttributeViInt64']['attributeValue'] = None
        self._defaults['GetAttributeViReal64'] = {}
        self._defaults['GetAttributeViReal64']['return'] = 0
        self._defaults['GetAttributeViReal64']['attributeValue'] = None
        self._defaults['GetAttributeViSession'] = {}
        self._defaults['GetAttributeViSession']['return'] = 0
        self._defaults['GetAttributeViSession']['attributeValue'] = None
        self._defaults['GetAttributeViString'] = {}
        self._defaults['GetAttributeViString']['return'] = 0
        self._defaults['GetAttributeViString']['attributeValue'] = None
        self._defaults['GetCalUserDefinedInfo'] = {}
        self._defaults['GetCalUserDefinedInfo']['return'] = 0
        self._defaults['GetCalUserDefinedInfo']['Info'] = None
        self._defaults['GetCalUserDefinedInfoMaxSize'] = {}
        self._defaults['GetCalUserDefinedInfoMaxSize']['return'] = 0
        self._defaults['GetCalUserDefinedInfoMaxSize']['infoSize'] = None
        self._defaults['GetChannelName'] = {}
        self._defaults['GetChannelName']['return'] = 0
        self._defaults['GetChannelName']['channelName'] = None
        self._defaults['GetError'] = {}
        self._defaults['GetError']['return'] = 0
        self._defaults['GetError']['Code'] = None
        self._defaults['GetError']['Description'] = None
        self._defaults['GetExtCalLastDateAndTime'] = {}
        self._defaults['GetExtCalLastDateAndTime']['return'] = 0
        self._defaults['GetExtCalLastDateAndTime']['Year'] = None
        self._defaults['GetExtCalLastDateAndTime']['Month'] = None
        self._defaults['GetExtCalLastDateAndTime']['Day'] = None
        self._defaults['GetExtCalLastDateAndTime']['Hour'] = None
        self._defaults['GetExtCalLastDateAndTime']['Minute'] = None
        self._defaults['GetExtCalLastTemp'] = {}
        self._defaults['GetExtCalLastTemp']['return'] = 0
        self._defaults['GetExtCalLastTemp']['Temperature'] = None
        self._defaults['GetExtCalRecommendedInterval'] = {}
        self._defaults['GetExtCalRecommendedInterval']['return'] = 0
        self._defaults['GetExtCalRecommendedInterval']['Months'] = None
        self._defaults['GetNextCoercionRecord'] = {}
        self._defaults['GetNextCoercionRecord']['return'] = 0
        self._defaults['GetNextCoercionRecord']['coercionRecord'] = None
        self._defaults['GetNextInterchangeWarning'] = {}
        self._defaults['GetNextInterchangeWarning']['return'] = 0
        self._defaults['GetNextInterchangeWarning']['interchangeWarning'] = None
        self._defaults['GetSelfCalLastDateAndTime'] = {}
        self._defaults['GetSelfCalLastDateAndTime']['return'] = 0
        self._defaults['GetSelfCalLastDateAndTime']['Year'] = None
        self._defaults['GetSelfCalLastDateAndTime']['Month'] = None
        self._defaults['GetSelfCalLastDateAndTime']['Day'] = None
        self._defaults['GetSelfCalLastDateAndTime']['Hour'] = None
        self._defaults['GetSelfCalLastDateAndTime']['Minute'] = None
        self._defaults['GetSelfCalLastTemp'] = {}
        self._defaults['GetSelfCalLastTemp']['return'] = 0
        self._defaults['GetSelfCalLastTemp']['Temperature'] = None
        self._defaults['InitExtCal'] = {}
        self._defaults['InitExtCal']['return'] = 0
        self._defaults['InitExtCal']['vi'] = None
        self._defaults['InitWithOptions'] = {}
        self._defaults['InitWithOptions']['return'] = 0
        self._defaults['InitWithOptions']['vi'] = None
        self._defaults['InitializeWithChannels'] = {}
        self._defaults['InitializeWithChannels']['return'] = 0
        self._defaults['InitializeWithChannels']['vi'] = None
        self._defaults['Initiate'] = {}
        self._defaults['Initiate']['return'] = 0
        self._defaults['LockSession'] = {}
        self._defaults['LockSession']['return'] = 0
        self._defaults['LockSession']['callerHasLock'] = None
        self._defaults['Measure'] = {}
        self._defaults['Measure']['return'] = 0
        self._defaults['Measure']['Measurement'] = None
        self._defaults['MeasureMultiple'] = {}
        self._defaults['MeasureMultiple']['return'] = 0
        self._defaults['MeasureMultiple']['voltageMeasurements'] = None
        self._defaults['MeasureMultiple']['currentMeasurements'] = None
        self._defaults['QueryInCompliance'] = {}
        self._defaults['QueryInCompliance']['return'] = 0
        self._defaults['QueryInCompliance']['inCompliance'] = None
        self._defaults['QueryMaxCurrentLimit'] = {}
        self._defaults['QueryMaxCurrentLimit']['return'] = 0
        self._defaults['QueryMaxCurrentLimit']['maxCurrentLimit'] = None
        self._defaults['QueryMaxVoltageLevel'] = {}
        self._defaults['QueryMaxVoltageLevel']['return'] = 0
        self._defaults['QueryMaxVoltageLevel']['maxVoltageLevel'] = None
        self._defaults['QueryMinCurrentLimit'] = {}
        self._defaults['QueryMinCurrentLimit']['return'] = 0
        self._defaults['QueryMinCurrentLimit']['minCurrentLimit'] = None
        self._defaults['QueryOutputState'] = {}
        self._defaults['QueryOutputState']['return'] = 0
        self._defaults['QueryOutputState']['inState'] = None
        self._defaults['ReadCurrentTemperature'] = {}
        self._defaults['ReadCurrentTemperature']['return'] = 0
        self._defaults['ReadCurrentTemperature']['Temperature'] = None
        self._defaults['ResetDevice'] = {}
        self._defaults['ResetDevice']['return'] = 0
        self._defaults['ResetInterchangeCheck'] = {}
        self._defaults['ResetInterchangeCheck']['return'] = 0
        self._defaults['ResetWithDefaults'] = {}
        self._defaults['ResetWithDefaults']['return'] = 0
        self._defaults['SendSoftwareEdgeTrigger'] = {}
        self._defaults['SendSoftwareEdgeTrigger']['return'] = 0
        self._defaults['SetAttributeViBoolean'] = {}
        self._defaults['SetAttributeViBoolean']['return'] = 0
        self._defaults['SetAttributeViInt32'] = {}
        self._defaults['SetAttributeViInt32']['return'] = 0
        self._defaults['SetAttributeViInt64'] = {}
        self._defaults['SetAttributeViInt64']['return'] = 0
        self._defaults['SetAttributeViReal64'] = {}
        self._defaults['SetAttributeViReal64']['return'] = 0
        self._defaults['SetAttributeViSession'] = {}
        self._defaults['SetAttributeViSession']['return'] = 0
        self._defaults['SetAttributeViString'] = {}
        self._defaults['SetAttributeViString']['return'] = 0
        self._defaults['SetCalUserDefinedInfo'] = {}
        self._defaults['SetCalUserDefinedInfo']['return'] = 0
        self._defaults['SetSequence'] = {}
        self._defaults['SetSequence']['return'] = 0
        self._defaults['UnlockSession'] = {}
        self._defaults['UnlockSession']['return'] = 0
        self._defaults['UnlockSession']['callerHasLock'] = None
        self._defaults['WaitForEvent'] = {}
        self._defaults['WaitForEvent']['return'] = 0
        self._defaults['close'] = {}
        self._defaults['close']['return'] = 0
        self._defaults['error_message'] = {}
        self._defaults['error_message']['return'] = 0
        self._defaults['error_message']['errorMessage'] = None
        self._defaults['init'] = {}
        self._defaults['init']['return'] = 0
        self._defaults['init']['vi'] = None
        self._defaults['reset'] = {}
        self._defaults['reset']['return'] = 0
        self._defaults['revision_query'] = {}
        self._defaults['revision_query']['return'] = 0
        self._defaults['revision_query']['instrumentDriverRevision'] = None
        self._defaults['revision_query']['firmwareRevision'] = None
        self._defaults['self_test'] = {}
        self._defaults['self_test']['return'] = 0
        self._defaults['self_test']['selfTestResult'] = None
        self._defaults['self_test']['selfTestMessage'] = None

    def __getitem__(self, func):
        return self._defaults[func]

    def __setitem__(self, func, val):
        self._defaults[func] = val

    def niDCPower_Abort(self, vi):  # noqa: N802
        if self._defaults['Abort']['return'] != 0:
            return self._defaults['Abort']['return']
        return self._defaults['Abort']['return']

    def niDCPower_CalAdjustCurrentLimit(self, vi, channel_name, range, number_of_measurements, requested_outputs, measured_outputs):  # noqa: N802
        if self._defaults['CalAdjustCurrentLimit']['return'] != 0:
            return self._defaults['CalAdjustCurrentLimit']['return']
        return self._defaults['CalAdjustCurrentLimit']['return']

    def niDCPower_CalAdjustCurrentMeasurement(self, vi, channel_name, range, number_of_measurements, reported_outputs, measured_outputs):  # noqa: N802
        if self._defaults['CalAdjustCurrentMeasurement']['return'] != 0:
            return self._defaults['CalAdjustCurrentMeasurement']['return']
        return self._defaults['CalAdjustCurrentMeasurement']['return']

    def niDCPower_CalAdjustInternalReference(self, vi, internal_reference, adjusted_internal_reference):  # noqa: N802
        if self._defaults['CalAdjustInternalReference']['return'] != 0:
            return self._defaults['CalAdjustInternalReference']['return']
        return self._defaults['CalAdjustInternalReference']['return']

    def niDCPower_CalAdjustOutputResistance(self, vi, channel_name, number_of_measurements, requested_outputs, measured_outputs):  # noqa: N802
        if self._defaults['CalAdjustOutputResistance']['return'] != 0:
            return self._defaults['CalAdjustOutputResistance']['return']
        return self._defaults['CalAdjustOutputResistance']['return']

    def niDCPower_CalAdjustResidualCurrentOffset(self, vi, channel_name):  # noqa: N802
        if self._defaults['CalAdjustResidualCurrentOffset']['return'] != 0:
            return self._defaults['CalAdjustResidualCurrentOffset']['return']
        return self._defaults['CalAdjustResidualCurrentOffset']['return']

    def niDCPower_CalAdjustResidualVoltageOffset(self, vi, channel_name):  # noqa: N802
        if self._defaults['CalAdjustResidualVoltageOffset']['return'] != 0:
            return self._defaults['CalAdjustResidualVoltageOffset']['return']
        return self._defaults['CalAdjustResidualVoltageOffset']['return']

    def niDCPower_CalAdjustVoltageLevel(self, vi, channel_name, range, number_of_measurements, requested_outputs, measured_outputs):  # noqa: N802
        if self._defaults['CalAdjustVoltageLevel']['return'] != 0:
            return self._defaults['CalAdjustVoltageLevel']['return']
        return self._defaults['CalAdjustVoltageLevel']['return']

    def niDCPower_CalAdjustVoltageMeasurement(self, vi, channel_name, range, number_of_measurements, reported_outputs, measured_outputs):  # noqa: N802
        if self._defaults['CalAdjustVoltageMeasurement']['return'] != 0:
            return self._defaults['CalAdjustVoltageMeasurement']['return']
        return self._defaults['CalAdjustVoltageMeasurement']['return']

    def niDCPower_CalSelfCalibrate(self, vi, channel_name):  # noqa: N802
        if self._defaults['CalSelfCalibrate']['return'] != 0:
            return self._defaults['CalSelfCalibrate']['return']
        return self._defaults['CalSelfCalibrate']['return']

    def niDCPower_ChangeExtCalPassword(self, vi, old_password, new_password):  # noqa: N802
        if self._defaults['ChangeExtCalPassword']['return'] != 0:
            return self._defaults['ChangeExtCalPassword']['return']
        return self._defaults['ChangeExtCalPassword']['return']

    def niDCPower_ClearError(self, vi):  # noqa: N802
        if self._defaults['ClearError']['return'] != 0:
            return self._defaults['ClearError']['return']
        return self._defaults['ClearError']['return']

    def niDCPower_ClearInterchangeWarnings(self, vi):  # noqa: N802
        if self._defaults['ClearInterchangeWarnings']['return'] != 0:
            return self._defaults['ClearInterchangeWarnings']['return']
        return self._defaults['ClearInterchangeWarnings']['return']

    def niDCPower_CloseExtCal(self, vi, action):  # noqa: N802
        if self._defaults['CloseExtCal']['return'] != 0:
            return self._defaults['CloseExtCal']['return']
        return self._defaults['CloseExtCal']['return']

    def niDCPower_Commit(self, vi):  # noqa: N802
        if self._defaults['Commit']['return'] != 0:
            return self._defaults['Commit']['return']
        return self._defaults['Commit']['return']

    def niDCPower_ConfigureApertureTime(self, vi, channel_name, aperture_time, units):  # noqa: N802
        if self._defaults['ConfigureApertureTime']['return'] != 0:
            return self._defaults['ConfigureApertureTime']['return']
        return self._defaults['ConfigureApertureTime']['return']

    def niDCPower_ConfigureAutoZero(self, vi, channel_name, auto_zero):  # noqa: N802
        if self._defaults['ConfigureAutoZero']['return'] != 0:
            return self._defaults['ConfigureAutoZero']['return']
        return self._defaults['ConfigureAutoZero']['return']

    def niDCPower_ConfigureCurrentLevel(self, vi, channel_name, level):  # noqa: N802
        if self._defaults['ConfigureCurrentLevel']['return'] != 0:
            return self._defaults['ConfigureCurrentLevel']['return']
        return self._defaults['ConfigureCurrentLevel']['return']

    def niDCPower_ConfigureCurrentLevelRange(self, vi, channel_name, range):  # noqa: N802
        if self._defaults['ConfigureCurrentLevelRange']['return'] != 0:
            return self._defaults['ConfigureCurrentLevelRange']['return']
        return self._defaults['ConfigureCurrentLevelRange']['return']

    def niDCPower_ConfigureCurrentLimit(self, vi, channel_name, behavior, limit):  # noqa: N802
        if self._defaults['ConfigureCurrentLimit']['return'] != 0:
            return self._defaults['ConfigureCurrentLimit']['return']
        return self._defaults['ConfigureCurrentLimit']['return']

    def niDCPower_ConfigureCurrentLimitRange(self, vi, channel_name, range):  # noqa: N802
        if self._defaults['ConfigureCurrentLimitRange']['return'] != 0:
            return self._defaults['ConfigureCurrentLimitRange']['return']
        return self._defaults['ConfigureCurrentLimitRange']['return']

    def niDCPower_ConfigureDigitalEdgeMeasureTrigger(self, vi, input_terminal, edge):  # noqa: N802
        if self._defaults['ConfigureDigitalEdgeMeasureTrigger']['return'] != 0:
            return self._defaults['ConfigureDigitalEdgeMeasureTrigger']['return']
        return self._defaults['ConfigureDigitalEdgeMeasureTrigger']['return']

    def niDCPower_ConfigureDigitalEdgePulseTrigger(self, vi, input_terminal, edge):  # noqa: N802
        if self._defaults['ConfigureDigitalEdgePulseTrigger']['return'] != 0:
            return self._defaults['ConfigureDigitalEdgePulseTrigger']['return']
        return self._defaults['ConfigureDigitalEdgePulseTrigger']['return']

    def niDCPower_ConfigureDigitalEdgeSequenceAdvanceTrigger(self, vi, input_terminal, edge):  # noqa: N802
        if self._defaults['ConfigureDigitalEdgeSequenceAdvanceTrigger']['return'] != 0:
            return self._defaults['ConfigureDigitalEdgeSequenceAdvanceTrigger']['return']
        return self._defaults['ConfigureDigitalEdgeSequenceAdvanceTrigger']['return']

    def niDCPower_ConfigureDigitalEdgeSourceTrigger(self, vi, input_terminal, edge):  # noqa: N802
        if self._defaults['ConfigureDigitalEdgeSourceTrigger']['return'] != 0:
            return self._defaults['ConfigureDigitalEdgeSourceTrigger']['return']
        return self._defaults['ConfigureDigitalEdgeSourceTrigger']['return']

    def niDCPower_ConfigureDigitalEdgeStartTrigger(self, vi, input_terminal, edge):  # noqa: N802
        if self._defaults['ConfigureDigitalEdgeStartTrigger']['return'] != 0:
            return self._defaults['ConfigureDigitalEdgeStartTrigger']['return']
        return self._defaults['ConfigureDigitalEdgeStartTrigger']['return']

    def niDCPower_ConfigureOutputEnabled(self, vi, channel_name, enabled):  # noqa: N802
        if self._defaults['ConfigureOutputEnabled']['return'] != 0:
            return self._defaults['ConfigureOutputEnabled']['return']
        return self._defaults['ConfigureOutputEnabled']['return']

    def niDCPower_ConfigureOutputFunction(self, vi, channel_name, function):  # noqa: N802
        if self._defaults['ConfigureOutputFunction']['return'] != 0:
            return self._defaults['ConfigureOutputFunction']['return']
        return self._defaults['ConfigureOutputFunction']['return']

    def niDCPower_ConfigureOutputRange(self, vi, channel_name, range_type, range):  # noqa: N802
        if self._defaults['ConfigureOutputRange']['return'] != 0:
            return self._defaults['ConfigureOutputRange']['return']
        return self._defaults['ConfigureOutputRange']['return']

    def niDCPower_ConfigureOutputResistance(self, vi, channel_name, resistance):  # noqa: N802
        if self._defaults['ConfigureOutputResistance']['return'] != 0:
            return self._defaults['ConfigureOutputResistance']['return']
        return self._defaults['ConfigureOutputResistance']['return']

    def niDCPower_ConfigurePowerLineFrequency(self, vi, powerline_frequency):  # noqa: N802
        if self._defaults['ConfigurePowerLineFrequency']['return'] != 0:
            return self._defaults['ConfigurePowerLineFrequency']['return']
        return self._defaults['ConfigurePowerLineFrequency']['return']

    def niDCPower_ConfigurePulseBiasCurrentLevel(self, vi, channel_name, level):  # noqa: N802
        if self._defaults['ConfigurePulseBiasCurrentLevel']['return'] != 0:
            return self._defaults['ConfigurePulseBiasCurrentLevel']['return']
        return self._defaults['ConfigurePulseBiasCurrentLevel']['return']

    def niDCPower_ConfigurePulseBiasCurrentLimit(self, vi, channel_name, limit):  # noqa: N802
        if self._defaults['ConfigurePulseBiasCurrentLimit']['return'] != 0:
            return self._defaults['ConfigurePulseBiasCurrentLimit']['return']
        return self._defaults['ConfigurePulseBiasCurrentLimit']['return']

    def niDCPower_ConfigurePulseBiasVoltageLevel(self, vi, channel_name, level):  # noqa: N802
        if self._defaults['ConfigurePulseBiasVoltageLevel']['return'] != 0:
            return self._defaults['ConfigurePulseBiasVoltageLevel']['return']
        return self._defaults['ConfigurePulseBiasVoltageLevel']['return']

    def niDCPower_ConfigurePulseBiasVoltageLimit(self, vi, channel_name, limit):  # noqa: N802
        if self._defaults['ConfigurePulseBiasVoltageLimit']['return'] != 0:
            return self._defaults['ConfigurePulseBiasVoltageLimit']['return']
        return self._defaults['ConfigurePulseBiasVoltageLimit']['return']

    def niDCPower_ConfigurePulseCurrentLevel(self, vi, channel_name, level):  # noqa: N802
        if self._defaults['ConfigurePulseCurrentLevel']['return'] != 0:
            return self._defaults['ConfigurePulseCurrentLevel']['return']
        return self._defaults['ConfigurePulseCurrentLevel']['return']

    def niDCPower_ConfigurePulseCurrentLevelRange(self, vi, channel_name, range):  # noqa: N802
        if self._defaults['ConfigurePulseCurrentLevelRange']['return'] != 0:
            return self._defaults['ConfigurePulseCurrentLevelRange']['return']
        return self._defaults['ConfigurePulseCurrentLevelRange']['return']

    def niDCPower_ConfigurePulseCurrentLimit(self, vi, channel_name, limit):  # noqa: N802
        if self._defaults['ConfigurePulseCurrentLimit']['return'] != 0:
            return self._defaults['ConfigurePulseCurrentLimit']['return']
        return self._defaults['ConfigurePulseCurrentLimit']['return']

    def niDCPower_ConfigurePulseCurrentLimitRange(self, vi, channel_name, range):  # noqa: N802
        if self._defaults['ConfigurePulseCurrentLimitRange']['return'] != 0:
            return self._defaults['ConfigurePulseCurrentLimitRange']['return']
        return self._defaults['ConfigurePulseCurrentLimitRange']['return']

    def niDCPower_ConfigurePulseVoltageLevel(self, vi, channel_name, level):  # noqa: N802
        if self._defaults['ConfigurePulseVoltageLevel']['return'] != 0:
            return self._defaults['ConfigurePulseVoltageLevel']['return']
        return self._defaults['ConfigurePulseVoltageLevel']['return']

    def niDCPower_ConfigurePulseVoltageLevelRange(self, vi, channel_name, range):  # noqa: N802
        if self._defaults['ConfigurePulseVoltageLevelRange']['return'] != 0:
            return self._defaults['ConfigurePulseVoltageLevelRange']['return']
        return self._defaults['ConfigurePulseVoltageLevelRange']['return']

    def niDCPower_ConfigurePulseVoltageLimit(self, vi, channel_name, limit):  # noqa: N802
        if self._defaults['ConfigurePulseVoltageLimit']['return'] != 0:
            return self._defaults['ConfigurePulseVoltageLimit']['return']
        return self._defaults['ConfigurePulseVoltageLimit']['return']

    def niDCPower_ConfigurePulseVoltageLimitRange(self, vi, channel_name, range):  # noqa: N802
        if self._defaults['ConfigurePulseVoltageLimitRange']['return'] != 0:
            return self._defaults['ConfigurePulseVoltageLimitRange']['return']
        return self._defaults['ConfigurePulseVoltageLimitRange']['return']

    def niDCPower_ConfigureSense(self, vi, channel_name, sense):  # noqa: N802
        if self._defaults['ConfigureSense']['return'] != 0:
            return self._defaults['ConfigureSense']['return']
        return self._defaults['ConfigureSense']['return']

    def niDCPower_ConfigureSoftwareEdgeMeasureTrigger(self, vi):  # noqa: N802
        if self._defaults['ConfigureSoftwareEdgeMeasureTrigger']['return'] != 0:
            return self._defaults['ConfigureSoftwareEdgeMeasureTrigger']['return']
        return self._defaults['ConfigureSoftwareEdgeMeasureTrigger']['return']

    def niDCPower_ConfigureSoftwareEdgePulseTrigger(self, vi):  # noqa: N802
        if self._defaults['ConfigureSoftwareEdgePulseTrigger']['return'] != 0:
            return self._defaults['ConfigureSoftwareEdgePulseTrigger']['return']
        return self._defaults['ConfigureSoftwareEdgePulseTrigger']['return']

    def niDCPower_ConfigureSoftwareEdgeSequenceAdvanceTrigger(self, vi):  # noqa: N802
        if self._defaults['ConfigureSoftwareEdgeSequenceAdvanceTrigger']['return'] != 0:
            return self._defaults['ConfigureSoftwareEdgeSequenceAdvanceTrigger']['return']
        return self._defaults['ConfigureSoftwareEdgeSequenceAdvanceTrigger']['return']

    def niDCPower_ConfigureSoftwareEdgeSourceTrigger(self, vi):  # noqa: N802
        if self._defaults['ConfigureSoftwareEdgeSourceTrigger']['return'] != 0:
            return self._defaults['ConfigureSoftwareEdgeSourceTrigger']['return']
        return self._defaults['ConfigureSoftwareEdgeSourceTrigger']['return']

    def niDCPower_ConfigureSoftwareEdgeStartTrigger(self, vi):  # noqa: N802
        if self._defaults['ConfigureSoftwareEdgeStartTrigger']['return'] != 0:
            return self._defaults['ConfigureSoftwareEdgeStartTrigger']['return']
        return self._defaults['ConfigureSoftwareEdgeStartTrigger']['return']

    def niDCPower_ConfigureSourceMode(self, vi, source_mode):  # noqa: N802
        if self._defaults['ConfigureSourceMode']['return'] != 0:
            return self._defaults['ConfigureSourceMode']['return']
        return self._defaults['ConfigureSourceMode']['return']

    def niDCPower_ConfigureVoltageLevel(self, vi, channel_name, level):  # noqa: N802
        if self._defaults['ConfigureVoltageLevel']['return'] != 0:
            return self._defaults['ConfigureVoltageLevel']['return']
        return self._defaults['ConfigureVoltageLevel']['return']

    def niDCPower_ConfigureVoltageLevelRange(self, vi, channel_name, range):  # noqa: N802
        if self._defaults['ConfigureVoltageLevelRange']['return'] != 0:
            return self._defaults['ConfigureVoltageLevelRange']['return']
        return self._defaults['ConfigureVoltageLevelRange']['return']

    def niDCPower_ConfigureVoltageLimit(self, vi, channel_name, limit):  # noqa: N802
        if self._defaults['ConfigureVoltageLimit']['return'] != 0:
            return self._defaults['ConfigureVoltageLimit']['return']
        return self._defaults['ConfigureVoltageLimit']['return']

    def niDCPower_ConfigureVoltageLimitRange(self, vi, channel_name, range):  # noqa: N802
        if self._defaults['ConfigureVoltageLimitRange']['return'] != 0:
            return self._defaults['ConfigureVoltageLimitRange']['return']
        return self._defaults['ConfigureVoltageLimitRange']['return']

    def niDCPower_ConnectInternalReference(self, vi, internal_reference):  # noqa: N802
        if self._defaults['ConnectInternalReference']['return'] != 0:
            return self._defaults['ConnectInternalReference']['return']
        return self._defaults['ConnectInternalReference']['return']

    def niDCPower_CreateAdvancedSequence(self, vi, sequence_name, attribute_id_count, attribute_ids, set_as_active_sequence):  # noqa: N802
        if self._defaults['CreateAdvancedSequence']['return'] != 0:
            return self._defaults['CreateAdvancedSequence']['return']
        return self._defaults['CreateAdvancedSequence']['return']

    def niDCPower_CreateAdvancedSequenceStep(self, vi, set_as_active_step):  # noqa: N802
        if self._defaults['CreateAdvancedSequenceStep']['return'] != 0:
            return self._defaults['CreateAdvancedSequenceStep']['return']
        return self._defaults['CreateAdvancedSequenceStep']['return']

    def niDCPower_DeleteAdvancedSequence(self, vi, sequence_name):  # noqa: N802
        if self._defaults['DeleteAdvancedSequence']['return'] != 0:
            return self._defaults['DeleteAdvancedSequence']['return']
        return self._defaults['DeleteAdvancedSequence']['return']

    def niDCPower_Disable(self, vi):  # noqa: N802
        if self._defaults['Disable']['return'] != 0:
            return self._defaults['Disable']['return']
        return self._defaults['Disable']['return']

    def niDCPower_DisablePulseTrigger(self, vi):  # noqa: N802
        if self._defaults['DisablePulseTrigger']['return'] != 0:
            return self._defaults['DisablePulseTrigger']['return']
        return self._defaults['DisablePulseTrigger']['return']

    def niDCPower_DisableSequenceAdvanceTrigger(self, vi):  # noqa: N802
        if self._defaults['DisableSequenceAdvanceTrigger']['return'] != 0:
            return self._defaults['DisableSequenceAdvanceTrigger']['return']
        return self._defaults['DisableSequenceAdvanceTrigger']['return']

    def niDCPower_DisableSourceTrigger(self, vi):  # noqa: N802
        if self._defaults['DisableSourceTrigger']['return'] != 0:
            return self._defaults['DisableSourceTrigger']['return']
        return self._defaults['DisableSourceTrigger']['return']

    def niDCPower_DisableStartTrigger(self, vi):  # noqa: N802
        if self._defaults['DisableStartTrigger']['return'] != 0:
            return self._defaults['DisableStartTrigger']['return']
        return self._defaults['DisableStartTrigger']['return']

    def niDCPower_ExportSignal(self, vi, signal, signal_identifier, output_terminal):  # noqa: N802
        if self._defaults['ExportSignal']['return'] != 0:
            return self._defaults['ExportSignal']['return']
        return self._defaults['ExportSignal']['return']

    def niDCPower_FetchMultiple(self, vi, channel_name, timeout, count, voltage_measurements, current_measurements, in_compliance, actual_count):  # noqa: N802
        if self._defaults['FetchMultiple']['return'] != 0:
            return self._defaults['FetchMultiple']['return']
        if self._defaults['FetchMultiple']['voltageMeasurements'] is None:
            raise MockFunctionCallError("niDCPower_FetchMultiple", param='voltageMeasurements')
        voltage_measurements.contents.value = self._defaults['FetchMultiple']['voltageMeasurements']
        if self._defaults['FetchMultiple']['currentMeasurements'] is None:
            raise MockFunctionCallError("niDCPower_FetchMultiple", param='currentMeasurements')
        current_measurements.contents.value = self._defaults['FetchMultiple']['currentMeasurements']
        if self._defaults['FetchMultiple']['inCompliance'] is None:
            raise MockFunctionCallError("niDCPower_FetchMultiple", param='inCompliance')
        in_compliance.contents.value = self._defaults['FetchMultiple']['inCompliance']
        if self._defaults['FetchMultiple']['actualCount'] is None:
            raise MockFunctionCallError("niDCPower_FetchMultiple", param='actualCount')
        actual_count.contents.value = self._defaults['FetchMultiple']['actualCount']
        return self._defaults['FetchMultiple']['return']

    def niDCPower_GetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViBoolean']['return'] != 0:
            return self._defaults['GetAttributeViBoolean']['return']
        if self._defaults['GetAttributeViBoolean']['attributeValue'] is None:
            raise MockFunctionCallError("niDCPower_GetAttributeViBoolean", param='attributeValue')
        attribute_value.contents.value = self._defaults['GetAttributeViBoolean']['attributeValue']
        return self._defaults['GetAttributeViBoolean']['return']

    def niDCPower_GetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViInt32']['return'] != 0:
            return self._defaults['GetAttributeViInt32']['return']
        if self._defaults['GetAttributeViInt32']['attributeValue'] is None:
            raise MockFunctionCallError("niDCPower_GetAttributeViInt32", param='attributeValue')
        attribute_value.contents.value = self._defaults['GetAttributeViInt32']['attributeValue']
        return self._defaults['GetAttributeViInt32']['return']

    def niDCPower_GetAttributeViInt64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViInt64']['return'] != 0:
            return self._defaults['GetAttributeViInt64']['return']
        if self._defaults['GetAttributeViInt64']['attributeValue'] is None:
            raise MockFunctionCallError("niDCPower_GetAttributeViInt64", param='attributeValue')
        attribute_value.contents.value = self._defaults['GetAttributeViInt64']['attributeValue']
        return self._defaults['GetAttributeViInt64']['return']

    def niDCPower_GetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViReal64']['return'] != 0:
            return self._defaults['GetAttributeViReal64']['return']
        if self._defaults['GetAttributeViReal64']['attributeValue'] is None:
            raise MockFunctionCallError("niDCPower_GetAttributeViReal64", param='attributeValue')
        attribute_value.contents.value = self._defaults['GetAttributeViReal64']['attributeValue']
        return self._defaults['GetAttributeViReal64']['return']

    def niDCPower_GetAttributeViSession(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViSession']['return'] != 0:
            return self._defaults['GetAttributeViSession']['return']
        if self._defaults['GetAttributeViSession']['attributeValue'] is None:
            raise MockFunctionCallError("niDCPower_GetAttributeViSession", param='attributeValue')
        attribute_value.contents.value = self._defaults['GetAttributeViSession']['attributeValue']
        return self._defaults['GetAttributeViSession']['return']

    def niDCPower_GetAttributeViString(self, vi, channel_name, attribute_id, buffer_size, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViString']['return'] != 0:
            return self._defaults['GetAttributeViString']['return']
        if self._defaults['GetAttributeViString']['attributeValue'] is None:
            raise MockFunctionCallError("niDCPower_GetAttributeViString", param='attributeValue')
        attribute_value.contents.value = self._defaults['GetAttributeViString']['attributeValue']
        return self._defaults['GetAttributeViString']['return']

    def niDCPower_GetCalUserDefinedInfo(self, vi, info):  # noqa: N802
        if self._defaults['GetCalUserDefinedInfo']['return'] != 0:
            return self._defaults['GetCalUserDefinedInfo']['return']
        if self._defaults['GetCalUserDefinedInfo']['Info'] is None:
            raise MockFunctionCallError("niDCPower_GetCalUserDefinedInfo", param='Info')
        info.contents.value = self._defaults['GetCalUserDefinedInfo']['Info']
        return self._defaults['GetCalUserDefinedInfo']['return']

    def niDCPower_GetCalUserDefinedInfoMaxSize(self, vi, info_size):  # noqa: N802
        if self._defaults['GetCalUserDefinedInfoMaxSize']['return'] != 0:
            return self._defaults['GetCalUserDefinedInfoMaxSize']['return']
        if self._defaults['GetCalUserDefinedInfoMaxSize']['infoSize'] is None:
            raise MockFunctionCallError("niDCPower_GetCalUserDefinedInfoMaxSize", param='infoSize')
        info_size.contents.value = self._defaults['GetCalUserDefinedInfoMaxSize']['infoSize']
        return self._defaults['GetCalUserDefinedInfoMaxSize']['return']

    def niDCPower_GetChannelName(self, vi, index, buffer_size, channel_name):  # noqa: N802
        if self._defaults['GetChannelName']['return'] != 0:
            return self._defaults['GetChannelName']['return']
        if self._defaults['GetChannelName']['channelName'] is None:
            raise MockFunctionCallError("niDCPower_GetChannelName", param='channelName')
        channel_name.contents.value = self._defaults['GetChannelName']['channelName']
        return self._defaults['GetChannelName']['return']

    def niDCPower_GetError(self, vi, code, buffer_size, description):  # noqa: N802
        if self._defaults['GetError']['return'] != 0:
            return self._defaults['GetError']['return']
        if self._defaults['GetError']['Code'] is None:
            raise MockFunctionCallError("niDCPower_GetError", param='Code')
        code.contents.value = self._defaults['GetError']['Code']
        if self._defaults['GetError']['Description'] is None:
            raise MockFunctionCallError("niDCPower_GetError", param='Description')
        description.contents.value = self._defaults['GetError']['Description']
        return self._defaults['GetError']['return']

    def niDCPower_GetExtCalLastDateAndTime(self, vi, year, month, day, hour, minute):  # noqa: N802
        if self._defaults['GetExtCalLastDateAndTime']['return'] != 0:
            return self._defaults['GetExtCalLastDateAndTime']['return']
        if self._defaults['GetExtCalLastDateAndTime']['Year'] is None:
            raise MockFunctionCallError("niDCPower_GetExtCalLastDateAndTime", param='Year')
        year.contents.value = self._defaults['GetExtCalLastDateAndTime']['Year']
        if self._defaults['GetExtCalLastDateAndTime']['Month'] is None:
            raise MockFunctionCallError("niDCPower_GetExtCalLastDateAndTime", param='Month')
        month.contents.value = self._defaults['GetExtCalLastDateAndTime']['Month']
        if self._defaults['GetExtCalLastDateAndTime']['Day'] is None:
            raise MockFunctionCallError("niDCPower_GetExtCalLastDateAndTime", param='Day')
        day.contents.value = self._defaults['GetExtCalLastDateAndTime']['Day']
        if self._defaults['GetExtCalLastDateAndTime']['Hour'] is None:
            raise MockFunctionCallError("niDCPower_GetExtCalLastDateAndTime", param='Hour')
        hour.contents.value = self._defaults['GetExtCalLastDateAndTime']['Hour']
        if self._defaults['GetExtCalLastDateAndTime']['Minute'] is None:
            raise MockFunctionCallError("niDCPower_GetExtCalLastDateAndTime", param='Minute')
        minute.contents.value = self._defaults['GetExtCalLastDateAndTime']['Minute']
        return self._defaults['GetExtCalLastDateAndTime']['return']

    def niDCPower_GetExtCalLastTemp(self, vi, temperature):  # noqa: N802
        if self._defaults['GetExtCalLastTemp']['return'] != 0:
            return self._defaults['GetExtCalLastTemp']['return']
        if self._defaults['GetExtCalLastTemp']['Temperature'] is None:
            raise MockFunctionCallError("niDCPower_GetExtCalLastTemp", param='Temperature')
        temperature.contents.value = self._defaults['GetExtCalLastTemp']['Temperature']
        return self._defaults['GetExtCalLastTemp']['return']

    def niDCPower_GetExtCalRecommendedInterval(self, vi, months):  # noqa: N802
        if self._defaults['GetExtCalRecommendedInterval']['return'] != 0:
            return self._defaults['GetExtCalRecommendedInterval']['return']
        if self._defaults['GetExtCalRecommendedInterval']['Months'] is None:
            raise MockFunctionCallError("niDCPower_GetExtCalRecommendedInterval", param='Months')
        months.contents.value = self._defaults['GetExtCalRecommendedInterval']['Months']
        return self._defaults['GetExtCalRecommendedInterval']['return']

    def niDCPower_GetNextCoercionRecord(self, vi, buffer_size, coercion_record):  # noqa: N802
        if self._defaults['GetNextCoercionRecord']['return'] != 0:
            return self._defaults['GetNextCoercionRecord']['return']
        if self._defaults['GetNextCoercionRecord']['coercionRecord'] is None:
            raise MockFunctionCallError("niDCPower_GetNextCoercionRecord", param='coercionRecord')
        coercion_record.contents.value = self._defaults['GetNextCoercionRecord']['coercionRecord']
        return self._defaults['GetNextCoercionRecord']['return']

    def niDCPower_GetNextInterchangeWarning(self, vi, buffer_size, interchange_warning):  # noqa: N802
        if self._defaults['GetNextInterchangeWarning']['return'] != 0:
            return self._defaults['GetNextInterchangeWarning']['return']
        if self._defaults['GetNextInterchangeWarning']['interchangeWarning'] is None:
            raise MockFunctionCallError("niDCPower_GetNextInterchangeWarning", param='interchangeWarning')
        interchange_warning.contents.value = self._defaults['GetNextInterchangeWarning']['interchangeWarning']
        return self._defaults['GetNextInterchangeWarning']['return']

    def niDCPower_GetSelfCalLastDateAndTime(self, vi, year, month, day, hour, minute):  # noqa: N802
        if self._defaults['GetSelfCalLastDateAndTime']['return'] != 0:
            return self._defaults['GetSelfCalLastDateAndTime']['return']
        if self._defaults['GetSelfCalLastDateAndTime']['Year'] is None:
            raise MockFunctionCallError("niDCPower_GetSelfCalLastDateAndTime", param='Year')
        year.contents.value = self._defaults['GetSelfCalLastDateAndTime']['Year']
        if self._defaults['GetSelfCalLastDateAndTime']['Month'] is None:
            raise MockFunctionCallError("niDCPower_GetSelfCalLastDateAndTime", param='Month')
        month.contents.value = self._defaults['GetSelfCalLastDateAndTime']['Month']
        if self._defaults['GetSelfCalLastDateAndTime']['Day'] is None:
            raise MockFunctionCallError("niDCPower_GetSelfCalLastDateAndTime", param='Day')
        day.contents.value = self._defaults['GetSelfCalLastDateAndTime']['Day']
        if self._defaults['GetSelfCalLastDateAndTime']['Hour'] is None:
            raise MockFunctionCallError("niDCPower_GetSelfCalLastDateAndTime", param='Hour')
        hour.contents.value = self._defaults['GetSelfCalLastDateAndTime']['Hour']
        if self._defaults['GetSelfCalLastDateAndTime']['Minute'] is None:
            raise MockFunctionCallError("niDCPower_GetSelfCalLastDateAndTime", param='Minute')
        minute.contents.value = self._defaults['GetSelfCalLastDateAndTime']['Minute']
        return self._defaults['GetSelfCalLastDateAndTime']['return']

    def niDCPower_GetSelfCalLastTemp(self, vi, temperature):  # noqa: N802
        if self._defaults['GetSelfCalLastTemp']['return'] != 0:
            return self._defaults['GetSelfCalLastTemp']['return']
        if self._defaults['GetSelfCalLastTemp']['Temperature'] is None:
            raise MockFunctionCallError("niDCPower_GetSelfCalLastTemp", param='Temperature')
        temperature.contents.value = self._defaults['GetSelfCalLastTemp']['Temperature']
        return self._defaults['GetSelfCalLastTemp']['return']

    def niDCPower_InitExtCal(self, resource_name, password, vi):  # noqa: N802
        if self._defaults['InitExtCal']['return'] != 0:
            return self._defaults['InitExtCal']['return']
        if self._defaults['InitExtCal']['vi'] is None:
            raise MockFunctionCallError("niDCPower_InitExtCal", param='vi')
        vi.contents.value = self._defaults['InitExtCal']['vi']
        return self._defaults['InitExtCal']['return']

    def niDCPower_InitWithOptions(self, resource_name, id_query, reset_device, option_string, vi):  # noqa: N802
        if self._defaults['InitWithOptions']['return'] != 0:
            return self._defaults['InitWithOptions']['return']
        if self._defaults['InitWithOptions']['vi'] is None:
            raise MockFunctionCallError("niDCPower_InitWithOptions", param='vi')
        vi.contents.value = self._defaults['InitWithOptions']['vi']
        return self._defaults['InitWithOptions']['return']

    def niDCPower_InitializeWithChannels(self, resource_name, channels, reset, option_string, vi):  # noqa: N802
        if self._defaults['InitializeWithChannels']['return'] != 0:
            return self._defaults['InitializeWithChannels']['return']
        if self._defaults['InitializeWithChannels']['vi'] is None:
            raise MockFunctionCallError("niDCPower_InitializeWithChannels", param='vi')
        vi.contents.value = self._defaults['InitializeWithChannels']['vi']
        return self._defaults['InitializeWithChannels']['return']

    def niDCPower_Initiate(self, vi):  # noqa: N802
        if self._defaults['Initiate']['return'] != 0:
            return self._defaults['Initiate']['return']
        return self._defaults['Initiate']['return']

    def niDCPower_LockSession(self, vi, caller_has_lock):  # noqa: N802
        if self._defaults['LockSession']['return'] != 0:
            return self._defaults['LockSession']['return']
        if self._defaults['LockSession']['callerHasLock'] is None:
            raise MockFunctionCallError("niDCPower_LockSession", param='callerHasLock')
        caller_has_lock.contents.value = self._defaults['LockSession']['callerHasLock']
        return self._defaults['LockSession']['return']

    def niDCPower_Measure(self, vi, channel_name, measurement_type, measurement):  # noqa: N802
        if self._defaults['Measure']['return'] != 0:
            return self._defaults['Measure']['return']
        if self._defaults['Measure']['Measurement'] is None:
            raise MockFunctionCallError("niDCPower_Measure", param='Measurement')
        measurement.contents.value = self._defaults['Measure']['Measurement']
        return self._defaults['Measure']['return']

    def niDCPower_MeasureMultiple(self, vi, channel_name, voltage_measurements, current_measurements):  # noqa: N802
        if self._defaults['MeasureMultiple']['return'] != 0:
            return self._defaults['MeasureMultiple']['return']
        if self._defaults['MeasureMultiple']['voltageMeasurements'] is None:
            raise MockFunctionCallError("niDCPower_MeasureMultiple", param='voltageMeasurements')
        voltage_measurements.contents.value = self._defaults['MeasureMultiple']['voltageMeasurements']
        if self._defaults['MeasureMultiple']['currentMeasurements'] is None:
            raise MockFunctionCallError("niDCPower_MeasureMultiple", param='currentMeasurements')
        current_measurements.contents.value = self._defaults['MeasureMultiple']['currentMeasurements']
        return self._defaults['MeasureMultiple']['return']

    def niDCPower_QueryInCompliance(self, vi, channel_name, in_compliance):  # noqa: N802
        if self._defaults['QueryInCompliance']['return'] != 0:
            return self._defaults['QueryInCompliance']['return']
        if self._defaults['QueryInCompliance']['inCompliance'] is None:
            raise MockFunctionCallError("niDCPower_QueryInCompliance", param='inCompliance')
        in_compliance.contents.value = self._defaults['QueryInCompliance']['inCompliance']
        return self._defaults['QueryInCompliance']['return']

    def niDCPower_QueryMaxCurrentLimit(self, vi, channel_name, voltage_level, max_current_limit):  # noqa: N802
        if self._defaults['QueryMaxCurrentLimit']['return'] != 0:
            return self._defaults['QueryMaxCurrentLimit']['return']
        if self._defaults['QueryMaxCurrentLimit']['maxCurrentLimit'] is None:
            raise MockFunctionCallError("niDCPower_QueryMaxCurrentLimit", param='maxCurrentLimit')
        max_current_limit.contents.value = self._defaults['QueryMaxCurrentLimit']['maxCurrentLimit']
        return self._defaults['QueryMaxCurrentLimit']['return']

    def niDCPower_QueryMaxVoltageLevel(self, vi, channel_name, current_limit, max_voltage_level):  # noqa: N802
        if self._defaults['QueryMaxVoltageLevel']['return'] != 0:
            return self._defaults['QueryMaxVoltageLevel']['return']
        if self._defaults['QueryMaxVoltageLevel']['maxVoltageLevel'] is None:
            raise MockFunctionCallError("niDCPower_QueryMaxVoltageLevel", param='maxVoltageLevel')
        max_voltage_level.contents.value = self._defaults['QueryMaxVoltageLevel']['maxVoltageLevel']
        return self._defaults['QueryMaxVoltageLevel']['return']

    def niDCPower_QueryMinCurrentLimit(self, vi, channel_name, voltage_level, min_current_limit):  # noqa: N802
        if self._defaults['QueryMinCurrentLimit']['return'] != 0:
            return self._defaults['QueryMinCurrentLimit']['return']
        if self._defaults['QueryMinCurrentLimit']['minCurrentLimit'] is None:
            raise MockFunctionCallError("niDCPower_QueryMinCurrentLimit", param='minCurrentLimit')
        min_current_limit.contents.value = self._defaults['QueryMinCurrentLimit']['minCurrentLimit']
        return self._defaults['QueryMinCurrentLimit']['return']

    def niDCPower_QueryOutputState(self, vi, channel_name, output_state, in_state):  # noqa: N802
        if self._defaults['QueryOutputState']['return'] != 0:
            return self._defaults['QueryOutputState']['return']
        if self._defaults['QueryOutputState']['inState'] is None:
            raise MockFunctionCallError("niDCPower_QueryOutputState", param='inState')
        in_state.contents.value = self._defaults['QueryOutputState']['inState']
        return self._defaults['QueryOutputState']['return']

    def niDCPower_ReadCurrentTemperature(self, vi, temperature):  # noqa: N802
        if self._defaults['ReadCurrentTemperature']['return'] != 0:
            return self._defaults['ReadCurrentTemperature']['return']
        if self._defaults['ReadCurrentTemperature']['Temperature'] is None:
            raise MockFunctionCallError("niDCPower_ReadCurrentTemperature", param='Temperature')
        temperature.contents.value = self._defaults['ReadCurrentTemperature']['Temperature']
        return self._defaults['ReadCurrentTemperature']['return']

    def niDCPower_ResetDevice(self, vi):  # noqa: N802
        if self._defaults['ResetDevice']['return'] != 0:
            return self._defaults['ResetDevice']['return']
        return self._defaults['ResetDevice']['return']

    def niDCPower_ResetInterchangeCheck(self, vi):  # noqa: N802
        if self._defaults['ResetInterchangeCheck']['return'] != 0:
            return self._defaults['ResetInterchangeCheck']['return']
        return self._defaults['ResetInterchangeCheck']['return']

    def niDCPower_ResetWithDefaults(self, vi):  # noqa: N802
        if self._defaults['ResetWithDefaults']['return'] != 0:
            return self._defaults['ResetWithDefaults']['return']
        return self._defaults['ResetWithDefaults']['return']

    def niDCPower_SendSoftwareEdgeTrigger(self, vi, trigger):  # noqa: N802
        if self._defaults['SendSoftwareEdgeTrigger']['return'] != 0:
            return self._defaults['SendSoftwareEdgeTrigger']['return']
        return self._defaults['SendSoftwareEdgeTrigger']['return']

    def niDCPower_SetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViBoolean']['return'] != 0:
            return self._defaults['SetAttributeViBoolean']['return']
        return self._defaults['SetAttributeViBoolean']['return']

    def niDCPower_SetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViInt32']['return'] != 0:
            return self._defaults['SetAttributeViInt32']['return']
        return self._defaults['SetAttributeViInt32']['return']

    def niDCPower_SetAttributeViInt64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViInt64']['return'] != 0:
            return self._defaults['SetAttributeViInt64']['return']
        return self._defaults['SetAttributeViInt64']['return']

    def niDCPower_SetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViReal64']['return'] != 0:
            return self._defaults['SetAttributeViReal64']['return']
        return self._defaults['SetAttributeViReal64']['return']

    def niDCPower_SetAttributeViSession(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViSession']['return'] != 0:
            return self._defaults['SetAttributeViSession']['return']
        return self._defaults['SetAttributeViSession']['return']

    def niDCPower_SetAttributeViString(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViString']['return'] != 0:
            return self._defaults['SetAttributeViString']['return']
        return self._defaults['SetAttributeViString']['return']

    def niDCPower_SetCalUserDefinedInfo(self, vi, info):  # noqa: N802
        if self._defaults['SetCalUserDefinedInfo']['return'] != 0:
            return self._defaults['SetCalUserDefinedInfo']['return']
        return self._defaults['SetCalUserDefinedInfo']['return']

    def niDCPower_SetSequence(self, vi, channel_name, values, source_delays, size):  # noqa: N802
        if self._defaults['SetSequence']['return'] != 0:
            return self._defaults['SetSequence']['return']
        return self._defaults['SetSequence']['return']

    def niDCPower_UnlockSession(self, vi, caller_has_lock):  # noqa: N802
        if self._defaults['UnlockSession']['return'] != 0:
            return self._defaults['UnlockSession']['return']
        if self._defaults['UnlockSession']['callerHasLock'] is None:
            raise MockFunctionCallError("niDCPower_UnlockSession", param='callerHasLock')
        caller_has_lock.contents.value = self._defaults['UnlockSession']['callerHasLock']
        return self._defaults['UnlockSession']['return']

    def niDCPower_WaitForEvent(self, vi, event_id, timeout):  # noqa: N802
        if self._defaults['WaitForEvent']['return'] != 0:
            return self._defaults['WaitForEvent']['return']
        return self._defaults['WaitForEvent']['return']

    def niDCPower_close(self, vi):  # noqa: N802
        if self._defaults['close']['return'] != 0:
            return self._defaults['close']['return']
        return self._defaults['close']['return']

    def niDCPower_error_message(self, vi, error_code, error_message):  # noqa: N802
        if self._defaults['error_message']['return'] != 0:
            return self._defaults['error_message']['return']
        if self._defaults['error_message']['errorMessage'] is None:
            raise MockFunctionCallError("niDCPower_error_message", param='errorMessage')
        error_message.contents.value = self._defaults['error_message']['errorMessage']
        return self._defaults['error_message']['return']

    def niDCPower_init(self, resource_name, id_query, reset_device, vi):  # noqa: N802
        if self._defaults['init']['return'] != 0:
            return self._defaults['init']['return']
        if self._defaults['init']['vi'] is None:
            raise MockFunctionCallError("niDCPower_init", param='vi')
        vi.contents.value = self._defaults['init']['vi']
        return self._defaults['init']['return']

    def niDCPower_reset(self, vi):  # noqa: N802
        if self._defaults['reset']['return'] != 0:
            return self._defaults['reset']['return']
        return self._defaults['reset']['return']

    def niDCPower_revision_query(self, vi, instrument_driver_revision, firmware_revision):  # noqa: N802
        if self._defaults['revision_query']['return'] != 0:
            return self._defaults['revision_query']['return']
        if self._defaults['revision_query']['instrumentDriverRevision'] is None:
            raise MockFunctionCallError("niDCPower_revision_query", param='instrumentDriverRevision')
        instrument_driver_revision.contents.value = self._defaults['revision_query']['instrumentDriverRevision']
        if self._defaults['revision_query']['firmwareRevision'] is None:
            raise MockFunctionCallError("niDCPower_revision_query", param='firmwareRevision')
        firmware_revision.contents.value = self._defaults['revision_query']['firmwareRevision']
        return self._defaults['revision_query']['return']

    def niDCPower_self_test(self, vi, self_test_result, self_test_message):  # noqa: N802
        if self._defaults['self_test']['return'] != 0:
            return self._defaults['self_test']['return']
        if self._defaults['self_test']['selfTestResult'] is None:
            raise MockFunctionCallError("niDCPower_self_test", param='selfTestResult')
        self_test_result.contents.value = self._defaults['self_test']['selfTestResult']
        if self._defaults['self_test']['selfTestMessage'] is None:
            raise MockFunctionCallError("niDCPower_self_test", param='selfTestMessage')
        self_test_message.contents.value = self._defaults['self_test']['selfTestMessage']
        return self._defaults['self_test']['return']

    # Helper function to setup Mock object with default side effects and return values
    def set_side_effects_and_return_values(self, mock_library):
        mock_library.niDCPower_Abort.side_effect = MockFunctionCallError("niDCPower_Abort")
        mock_library.niDCPower_Abort.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_CalAdjustCurrentLimit.side_effect = MockFunctionCallError("niDCPower_CalAdjustCurrentLimit")
        mock_library.niDCPower_CalAdjustCurrentLimit.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_CalAdjustCurrentMeasurement.side_effect = MockFunctionCallError("niDCPower_CalAdjustCurrentMeasurement")
        mock_library.niDCPower_CalAdjustCurrentMeasurement.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_CalAdjustInternalReference.side_effect = MockFunctionCallError("niDCPower_CalAdjustInternalReference")
        mock_library.niDCPower_CalAdjustInternalReference.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_CalAdjustOutputResistance.side_effect = MockFunctionCallError("niDCPower_CalAdjustOutputResistance")
        mock_library.niDCPower_CalAdjustOutputResistance.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_CalAdjustResidualCurrentOffset.side_effect = MockFunctionCallError("niDCPower_CalAdjustResidualCurrentOffset")
        mock_library.niDCPower_CalAdjustResidualCurrentOffset.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_CalAdjustResidualVoltageOffset.side_effect = MockFunctionCallError("niDCPower_CalAdjustResidualVoltageOffset")
        mock_library.niDCPower_CalAdjustResidualVoltageOffset.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_CalAdjustVoltageLevel.side_effect = MockFunctionCallError("niDCPower_CalAdjustVoltageLevel")
        mock_library.niDCPower_CalAdjustVoltageLevel.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_CalAdjustVoltageMeasurement.side_effect = MockFunctionCallError("niDCPower_CalAdjustVoltageMeasurement")
        mock_library.niDCPower_CalAdjustVoltageMeasurement.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_CalSelfCalibrate.side_effect = MockFunctionCallError("niDCPower_CalSelfCalibrate")
        mock_library.niDCPower_CalSelfCalibrate.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_ChangeExtCalPassword.side_effect = MockFunctionCallError("niDCPower_ChangeExtCalPassword")
        mock_library.niDCPower_ChangeExtCalPassword.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_ClearError.side_effect = MockFunctionCallError("niDCPower_ClearError")
        mock_library.niDCPower_ClearError.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_ClearInterchangeWarnings.side_effect = MockFunctionCallError("niDCPower_ClearInterchangeWarnings")
        mock_library.niDCPower_ClearInterchangeWarnings.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_CloseExtCal.side_effect = MockFunctionCallError("niDCPower_CloseExtCal")
        mock_library.niDCPower_CloseExtCal.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_Commit.side_effect = MockFunctionCallError("niDCPower_Commit")
        mock_library.niDCPower_Commit.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_ConfigureApertureTime.side_effect = MockFunctionCallError("niDCPower_ConfigureApertureTime")
        mock_library.niDCPower_ConfigureApertureTime.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_ConfigureAutoZero.side_effect = MockFunctionCallError("niDCPower_ConfigureAutoZero")
        mock_library.niDCPower_ConfigureAutoZero.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_ConfigureCurrentLevel.side_effect = MockFunctionCallError("niDCPower_ConfigureCurrentLevel")
        mock_library.niDCPower_ConfigureCurrentLevel.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_ConfigureCurrentLevelRange.side_effect = MockFunctionCallError("niDCPower_ConfigureCurrentLevelRange")
        mock_library.niDCPower_ConfigureCurrentLevelRange.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_ConfigureCurrentLimit.side_effect = MockFunctionCallError("niDCPower_ConfigureCurrentLimit")
        mock_library.niDCPower_ConfigureCurrentLimit.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_ConfigureCurrentLimitRange.side_effect = MockFunctionCallError("niDCPower_ConfigureCurrentLimitRange")
        mock_library.niDCPower_ConfigureCurrentLimitRange.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_ConfigureDigitalEdgeMeasureTrigger.side_effect = MockFunctionCallError("niDCPower_ConfigureDigitalEdgeMeasureTrigger")
        mock_library.niDCPower_ConfigureDigitalEdgeMeasureTrigger.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_ConfigureDigitalEdgePulseTrigger.side_effect = MockFunctionCallError("niDCPower_ConfigureDigitalEdgePulseTrigger")
        mock_library.niDCPower_ConfigureDigitalEdgePulseTrigger.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_ConfigureDigitalEdgeSequenceAdvanceTrigger.side_effect = MockFunctionCallError("niDCPower_ConfigureDigitalEdgeSequenceAdvanceTrigger")
        mock_library.niDCPower_ConfigureDigitalEdgeSequenceAdvanceTrigger.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_ConfigureDigitalEdgeSourceTrigger.side_effect = MockFunctionCallError("niDCPower_ConfigureDigitalEdgeSourceTrigger")
        mock_library.niDCPower_ConfigureDigitalEdgeSourceTrigger.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_ConfigureDigitalEdgeStartTrigger.side_effect = MockFunctionCallError("niDCPower_ConfigureDigitalEdgeStartTrigger")
        mock_library.niDCPower_ConfigureDigitalEdgeStartTrigger.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_ConfigureOutputEnabled.side_effect = MockFunctionCallError("niDCPower_ConfigureOutputEnabled")
        mock_library.niDCPower_ConfigureOutputEnabled.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_ConfigureOutputFunction.side_effect = MockFunctionCallError("niDCPower_ConfigureOutputFunction")
        mock_library.niDCPower_ConfigureOutputFunction.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_ConfigureOutputRange.side_effect = MockFunctionCallError("niDCPower_ConfigureOutputRange")
        mock_library.niDCPower_ConfigureOutputRange.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_ConfigureOutputResistance.side_effect = MockFunctionCallError("niDCPower_ConfigureOutputResistance")
        mock_library.niDCPower_ConfigureOutputResistance.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_ConfigurePowerLineFrequency.side_effect = MockFunctionCallError("niDCPower_ConfigurePowerLineFrequency")
        mock_library.niDCPower_ConfigurePowerLineFrequency.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_ConfigurePulseBiasCurrentLevel.side_effect = MockFunctionCallError("niDCPower_ConfigurePulseBiasCurrentLevel")
        mock_library.niDCPower_ConfigurePulseBiasCurrentLevel.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_ConfigurePulseBiasCurrentLimit.side_effect = MockFunctionCallError("niDCPower_ConfigurePulseBiasCurrentLimit")
        mock_library.niDCPower_ConfigurePulseBiasCurrentLimit.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_ConfigurePulseBiasVoltageLevel.side_effect = MockFunctionCallError("niDCPower_ConfigurePulseBiasVoltageLevel")
        mock_library.niDCPower_ConfigurePulseBiasVoltageLevel.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_ConfigurePulseBiasVoltageLimit.side_effect = MockFunctionCallError("niDCPower_ConfigurePulseBiasVoltageLimit")
        mock_library.niDCPower_ConfigurePulseBiasVoltageLimit.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_ConfigurePulseCurrentLevel.side_effect = MockFunctionCallError("niDCPower_ConfigurePulseCurrentLevel")
        mock_library.niDCPower_ConfigurePulseCurrentLevel.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_ConfigurePulseCurrentLevelRange.side_effect = MockFunctionCallError("niDCPower_ConfigurePulseCurrentLevelRange")
        mock_library.niDCPower_ConfigurePulseCurrentLevelRange.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_ConfigurePulseCurrentLimit.side_effect = MockFunctionCallError("niDCPower_ConfigurePulseCurrentLimit")
        mock_library.niDCPower_ConfigurePulseCurrentLimit.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_ConfigurePulseCurrentLimitRange.side_effect = MockFunctionCallError("niDCPower_ConfigurePulseCurrentLimitRange")
        mock_library.niDCPower_ConfigurePulseCurrentLimitRange.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_ConfigurePulseVoltageLevel.side_effect = MockFunctionCallError("niDCPower_ConfigurePulseVoltageLevel")
        mock_library.niDCPower_ConfigurePulseVoltageLevel.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_ConfigurePulseVoltageLevelRange.side_effect = MockFunctionCallError("niDCPower_ConfigurePulseVoltageLevelRange")
        mock_library.niDCPower_ConfigurePulseVoltageLevelRange.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_ConfigurePulseVoltageLimit.side_effect = MockFunctionCallError("niDCPower_ConfigurePulseVoltageLimit")
        mock_library.niDCPower_ConfigurePulseVoltageLimit.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_ConfigurePulseVoltageLimitRange.side_effect = MockFunctionCallError("niDCPower_ConfigurePulseVoltageLimitRange")
        mock_library.niDCPower_ConfigurePulseVoltageLimitRange.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_ConfigureSense.side_effect = MockFunctionCallError("niDCPower_ConfigureSense")
        mock_library.niDCPower_ConfigureSense.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_ConfigureSoftwareEdgeMeasureTrigger.side_effect = MockFunctionCallError("niDCPower_ConfigureSoftwareEdgeMeasureTrigger")
        mock_library.niDCPower_ConfigureSoftwareEdgeMeasureTrigger.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_ConfigureSoftwareEdgePulseTrigger.side_effect = MockFunctionCallError("niDCPower_ConfigureSoftwareEdgePulseTrigger")
        mock_library.niDCPower_ConfigureSoftwareEdgePulseTrigger.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_ConfigureSoftwareEdgeSequenceAdvanceTrigger.side_effect = MockFunctionCallError("niDCPower_ConfigureSoftwareEdgeSequenceAdvanceTrigger")
        mock_library.niDCPower_ConfigureSoftwareEdgeSequenceAdvanceTrigger.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_ConfigureSoftwareEdgeSourceTrigger.side_effect = MockFunctionCallError("niDCPower_ConfigureSoftwareEdgeSourceTrigger")
        mock_library.niDCPower_ConfigureSoftwareEdgeSourceTrigger.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_ConfigureSoftwareEdgeStartTrigger.side_effect = MockFunctionCallError("niDCPower_ConfigureSoftwareEdgeStartTrigger")
        mock_library.niDCPower_ConfigureSoftwareEdgeStartTrigger.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_ConfigureSourceMode.side_effect = MockFunctionCallError("niDCPower_ConfigureSourceMode")
        mock_library.niDCPower_ConfigureSourceMode.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_ConfigureVoltageLevel.side_effect = MockFunctionCallError("niDCPower_ConfigureVoltageLevel")
        mock_library.niDCPower_ConfigureVoltageLevel.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_ConfigureVoltageLevelRange.side_effect = MockFunctionCallError("niDCPower_ConfigureVoltageLevelRange")
        mock_library.niDCPower_ConfigureVoltageLevelRange.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_ConfigureVoltageLimit.side_effect = MockFunctionCallError("niDCPower_ConfigureVoltageLimit")
        mock_library.niDCPower_ConfigureVoltageLimit.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_ConfigureVoltageLimitRange.side_effect = MockFunctionCallError("niDCPower_ConfigureVoltageLimitRange")
        mock_library.niDCPower_ConfigureVoltageLimitRange.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_ConnectInternalReference.side_effect = MockFunctionCallError("niDCPower_ConnectInternalReference")
        mock_library.niDCPower_ConnectInternalReference.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_CreateAdvancedSequence.side_effect = MockFunctionCallError("niDCPower_CreateAdvancedSequence")
        mock_library.niDCPower_CreateAdvancedSequence.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_CreateAdvancedSequenceStep.side_effect = MockFunctionCallError("niDCPower_CreateAdvancedSequenceStep")
        mock_library.niDCPower_CreateAdvancedSequenceStep.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_DeleteAdvancedSequence.side_effect = MockFunctionCallError("niDCPower_DeleteAdvancedSequence")
        mock_library.niDCPower_DeleteAdvancedSequence.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_Disable.side_effect = MockFunctionCallError("niDCPower_Disable")
        mock_library.niDCPower_Disable.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_DisablePulseTrigger.side_effect = MockFunctionCallError("niDCPower_DisablePulseTrigger")
        mock_library.niDCPower_DisablePulseTrigger.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_DisableSequenceAdvanceTrigger.side_effect = MockFunctionCallError("niDCPower_DisableSequenceAdvanceTrigger")
        mock_library.niDCPower_DisableSequenceAdvanceTrigger.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_DisableSourceTrigger.side_effect = MockFunctionCallError("niDCPower_DisableSourceTrigger")
        mock_library.niDCPower_DisableSourceTrigger.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_DisableStartTrigger.side_effect = MockFunctionCallError("niDCPower_DisableStartTrigger")
        mock_library.niDCPower_DisableStartTrigger.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_ExportSignal.side_effect = MockFunctionCallError("niDCPower_ExportSignal")
        mock_library.niDCPower_ExportSignal.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_FetchMultiple.side_effect = MockFunctionCallError("niDCPower_FetchMultiple")
        mock_library.niDCPower_FetchMultiple.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_GetAttributeViBoolean.side_effect = MockFunctionCallError("niDCPower_GetAttributeViBoolean")
        mock_library.niDCPower_GetAttributeViBoolean.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_GetAttributeViInt32.side_effect = MockFunctionCallError("niDCPower_GetAttributeViInt32")
        mock_library.niDCPower_GetAttributeViInt32.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_GetAttributeViInt64.side_effect = MockFunctionCallError("niDCPower_GetAttributeViInt64")
        mock_library.niDCPower_GetAttributeViInt64.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_GetAttributeViReal64.side_effect = MockFunctionCallError("niDCPower_GetAttributeViReal64")
        mock_library.niDCPower_GetAttributeViReal64.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_GetAttributeViSession.side_effect = MockFunctionCallError("niDCPower_GetAttributeViSession")
        mock_library.niDCPower_GetAttributeViSession.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_GetAttributeViString.side_effect = MockFunctionCallError("niDCPower_GetAttributeViString")
        mock_library.niDCPower_GetAttributeViString.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_GetCalUserDefinedInfo.side_effect = MockFunctionCallError("niDCPower_GetCalUserDefinedInfo")
        mock_library.niDCPower_GetCalUserDefinedInfo.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_GetCalUserDefinedInfoMaxSize.side_effect = MockFunctionCallError("niDCPower_GetCalUserDefinedInfoMaxSize")
        mock_library.niDCPower_GetCalUserDefinedInfoMaxSize.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_GetChannelName.side_effect = MockFunctionCallError("niDCPower_GetChannelName")
        mock_library.niDCPower_GetChannelName.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_GetError.side_effect = MockFunctionCallError("niDCPower_GetError")
        mock_library.niDCPower_GetError.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_GetExtCalLastDateAndTime.side_effect = MockFunctionCallError("niDCPower_GetExtCalLastDateAndTime")
        mock_library.niDCPower_GetExtCalLastDateAndTime.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_GetExtCalLastTemp.side_effect = MockFunctionCallError("niDCPower_GetExtCalLastTemp")
        mock_library.niDCPower_GetExtCalLastTemp.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_GetExtCalRecommendedInterval.side_effect = MockFunctionCallError("niDCPower_GetExtCalRecommendedInterval")
        mock_library.niDCPower_GetExtCalRecommendedInterval.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_GetNextCoercionRecord.side_effect = MockFunctionCallError("niDCPower_GetNextCoercionRecord")
        mock_library.niDCPower_GetNextCoercionRecord.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_GetNextInterchangeWarning.side_effect = MockFunctionCallError("niDCPower_GetNextInterchangeWarning")
        mock_library.niDCPower_GetNextInterchangeWarning.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_GetSelfCalLastDateAndTime.side_effect = MockFunctionCallError("niDCPower_GetSelfCalLastDateAndTime")
        mock_library.niDCPower_GetSelfCalLastDateAndTime.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_GetSelfCalLastTemp.side_effect = MockFunctionCallError("niDCPower_GetSelfCalLastTemp")
        mock_library.niDCPower_GetSelfCalLastTemp.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_InitExtCal.side_effect = MockFunctionCallError("niDCPower_InitExtCal")
        mock_library.niDCPower_InitExtCal.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_InitWithOptions.side_effect = MockFunctionCallError("niDCPower_InitWithOptions")
        mock_library.niDCPower_InitWithOptions.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_InitializeWithChannels.side_effect = MockFunctionCallError("niDCPower_InitializeWithChannels")
        mock_library.niDCPower_InitializeWithChannels.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_Initiate.side_effect = MockFunctionCallError("niDCPower_Initiate")
        mock_library.niDCPower_Initiate.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_LockSession.side_effect = MockFunctionCallError("niDCPower_LockSession")
        mock_library.niDCPower_LockSession.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_Measure.side_effect = MockFunctionCallError("niDCPower_Measure")
        mock_library.niDCPower_Measure.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_MeasureMultiple.side_effect = MockFunctionCallError("niDCPower_MeasureMultiple")
        mock_library.niDCPower_MeasureMultiple.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_QueryInCompliance.side_effect = MockFunctionCallError("niDCPower_QueryInCompliance")
        mock_library.niDCPower_QueryInCompliance.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_QueryMaxCurrentLimit.side_effect = MockFunctionCallError("niDCPower_QueryMaxCurrentLimit")
        mock_library.niDCPower_QueryMaxCurrentLimit.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_QueryMaxVoltageLevel.side_effect = MockFunctionCallError("niDCPower_QueryMaxVoltageLevel")
        mock_library.niDCPower_QueryMaxVoltageLevel.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_QueryMinCurrentLimit.side_effect = MockFunctionCallError("niDCPower_QueryMinCurrentLimit")
        mock_library.niDCPower_QueryMinCurrentLimit.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_QueryOutputState.side_effect = MockFunctionCallError("niDCPower_QueryOutputState")
        mock_library.niDCPower_QueryOutputState.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_ReadCurrentTemperature.side_effect = MockFunctionCallError("niDCPower_ReadCurrentTemperature")
        mock_library.niDCPower_ReadCurrentTemperature.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_ResetDevice.side_effect = MockFunctionCallError("niDCPower_ResetDevice")
        mock_library.niDCPower_ResetDevice.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_ResetInterchangeCheck.side_effect = MockFunctionCallError("niDCPower_ResetInterchangeCheck")
        mock_library.niDCPower_ResetInterchangeCheck.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_ResetWithDefaults.side_effect = MockFunctionCallError("niDCPower_ResetWithDefaults")
        mock_library.niDCPower_ResetWithDefaults.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_SendSoftwareEdgeTrigger.side_effect = MockFunctionCallError("niDCPower_SendSoftwareEdgeTrigger")
        mock_library.niDCPower_SendSoftwareEdgeTrigger.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_SetAttributeViBoolean.side_effect = MockFunctionCallError("niDCPower_SetAttributeViBoolean")
        mock_library.niDCPower_SetAttributeViBoolean.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_SetAttributeViInt32.side_effect = MockFunctionCallError("niDCPower_SetAttributeViInt32")
        mock_library.niDCPower_SetAttributeViInt32.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_SetAttributeViInt64.side_effect = MockFunctionCallError("niDCPower_SetAttributeViInt64")
        mock_library.niDCPower_SetAttributeViInt64.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_SetAttributeViReal64.side_effect = MockFunctionCallError("niDCPower_SetAttributeViReal64")
        mock_library.niDCPower_SetAttributeViReal64.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_SetAttributeViSession.side_effect = MockFunctionCallError("niDCPower_SetAttributeViSession")
        mock_library.niDCPower_SetAttributeViSession.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_SetAttributeViString.side_effect = MockFunctionCallError("niDCPower_SetAttributeViString")
        mock_library.niDCPower_SetAttributeViString.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_SetCalUserDefinedInfo.side_effect = MockFunctionCallError("niDCPower_SetCalUserDefinedInfo")
        mock_library.niDCPower_SetCalUserDefinedInfo.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_SetSequence.side_effect = MockFunctionCallError("niDCPower_SetSequence")
        mock_library.niDCPower_SetSequence.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_UnlockSession.side_effect = MockFunctionCallError("niDCPower_UnlockSession")
        mock_library.niDCPower_UnlockSession.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_WaitForEvent.side_effect = MockFunctionCallError("niDCPower_WaitForEvent")
        mock_library.niDCPower_WaitForEvent.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_close.side_effect = MockFunctionCallError("niDCPower_close")
        mock_library.niDCPower_close.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_error_message.side_effect = MockFunctionCallError("niDCPower_error_message")
        mock_library.niDCPower_error_message.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_init.side_effect = MockFunctionCallError("niDCPower_init")
        mock_library.niDCPower_init.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_reset.side_effect = MockFunctionCallError("niDCPower_reset")
        mock_library.niDCPower_reset.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_revision_query.side_effect = MockFunctionCallError("niDCPower_revision_query")
        mock_library.niDCPower_revision_query.return_value = nidcpower.python_types.ViStatus(0)
        mock_library.niDCPower_self_test.side_effect = MockFunctionCallError("niDCPower_self_test")
        mock_library.niDCPower_self_test.return_value = nidcpower.python_types.ViStatus(0)
