# This file was generated

import ctypes

import nidmm.ctypes_types
import nidmm.python_types


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
        self._defaults['ClearInterchangeWarnings'] = {}
        self._defaults['ClearInterchangeWarnings']['return'] = 0
        self._defaults['ConfigureACBandwidth'] = {}
        self._defaults['ConfigureACBandwidth']['return'] = 0
        self._defaults['ConfigureADCCalibration'] = {}
        self._defaults['ConfigureADCCalibration']['return'] = 0
        self._defaults['ConfigureAutoZeroMode'] = {}
        self._defaults['ConfigureAutoZeroMode']['return'] = 0
        self._defaults['ConfigureCableCompType'] = {}
        self._defaults['ConfigureCableCompType']['return'] = 0
        self._defaults['ConfigureCurrentSource'] = {}
        self._defaults['ConfigureCurrentSource']['return'] = 0
        self._defaults['ConfigureFixedRefJunction'] = {}
        self._defaults['ConfigureFixedRefJunction']['return'] = 0
        self._defaults['ConfigureFrequencyVoltageRange'] = {}
        self._defaults['ConfigureFrequencyVoltageRange']['return'] = 0
        self._defaults['ConfigureMeasCompleteDest'] = {}
        self._defaults['ConfigureMeasCompleteDest']['return'] = 0
        self._defaults['ConfigureMeasCompleteSlope'] = {}
        self._defaults['ConfigureMeasCompleteSlope']['return'] = 0
        self._defaults['ConfigureMeasurementAbsolute'] = {}
        self._defaults['ConfigureMeasurementAbsolute']['return'] = 0
        self._defaults['ConfigureMeasurementDigits'] = {}
        self._defaults['ConfigureMeasurementDigits']['return'] = 0
        self._defaults['ConfigureMultiPoint'] = {}
        self._defaults['ConfigureMultiPoint']['return'] = 0
        self._defaults['ConfigureOffsetCompOhms'] = {}
        self._defaults['ConfigureOffsetCompOhms']['return'] = 0
        self._defaults['ConfigureOpenCableCompValues'] = {}
        self._defaults['ConfigureOpenCableCompValues']['return'] = 0
        self._defaults['ConfigurePowerLineFrequency'] = {}
        self._defaults['ConfigurePowerLineFrequency']['return'] = 0
        self._defaults['ConfigureRTDCustom'] = {}
        self._defaults['ConfigureRTDCustom']['return'] = 0
        self._defaults['ConfigureRTDType'] = {}
        self._defaults['ConfigureRTDType']['return'] = 0
        self._defaults['ConfigureSampleTriggerSlope'] = {}
        self._defaults['ConfigureSampleTriggerSlope']['return'] = 0
        self._defaults['ConfigureShortCableCompValues'] = {}
        self._defaults['ConfigureShortCableCompValues']['return'] = 0
        self._defaults['ConfigureThermistorCustom'] = {}
        self._defaults['ConfigureThermistorCustom']['return'] = 0
        self._defaults['ConfigureThermistorType'] = {}
        self._defaults['ConfigureThermistorType']['return'] = 0
        self._defaults['ConfigureThermocouple'] = {}
        self._defaults['ConfigureThermocouple']['return'] = 0
        self._defaults['ConfigureTransducerType'] = {}
        self._defaults['ConfigureTransducerType']['return'] = 0
        self._defaults['ConfigureTrigger'] = {}
        self._defaults['ConfigureTrigger']['return'] = 0
        self._defaults['ConfigureTriggerSlope'] = {}
        self._defaults['ConfigureTriggerSlope']['return'] = 0
        self._defaults['ConfigureWaveformAcquisition'] = {}
        self._defaults['ConfigureWaveformAcquisition']['return'] = 0
        self._defaults['ConfigureWaveformCoupling'] = {}
        self._defaults['ConfigureWaveformCoupling']['return'] = 0
        self._defaults['Disable'] = {}
        self._defaults['Disable']['return'] = 0
        self._defaults['Fetch'] = {}
        self._defaults['Fetch']['return'] = 0
        self._defaults['Fetch']['reading'] = None
        self._defaults['FetchMultiPoint'] = {}
        self._defaults['FetchMultiPoint']['return'] = 0
        self._defaults['FetchMultiPoint']['readingArray'] = None
        self._defaults['FetchMultiPoint']['actualNumberOfPoints'] = None
        self._defaults['FetchWaveform'] = {}
        self._defaults['FetchWaveform']['return'] = 0
        self._defaults['FetchWaveform']['waveformArray'] = None
        self._defaults['FetchWaveform']['actualNumberOfPoints'] = None
        self._defaults['FormatMeasAbsolute'] = {}
        self._defaults['FormatMeasAbsolute']['return'] = 0
        self._defaults['FormatMeasAbsolute']['modeString'] = None
        self._defaults['FormatMeasAbsolute']['rangeString'] = None
        self._defaults['FormatMeasAbsolute']['dataString'] = None
        self._defaults['GetApertureTimeInfo'] = {}
        self._defaults['GetApertureTimeInfo']['return'] = 0
        self._defaults['GetApertureTimeInfo']['apertureTime'] = None
        self._defaults['GetApertureTimeInfo']['apertureTimeUnits'] = None
        self._defaults['GetAttributeViBoolean'] = {}
        self._defaults['GetAttributeViBoolean']['return'] = 0
        self._defaults['GetAttributeViBoolean']['attributeValue'] = None
        self._defaults['GetAttributeViInt32'] = {}
        self._defaults['GetAttributeViInt32']['return'] = 0
        self._defaults['GetAttributeViInt32']['attributeValue'] = None
        self._defaults['GetAttributeViReal64'] = {}
        self._defaults['GetAttributeViReal64']['return'] = 0
        self._defaults['GetAttributeViReal64']['attributeValue'] = None
        self._defaults['GetAttributeViSession'] = {}
        self._defaults['GetAttributeViSession']['return'] = 0
        self._defaults['GetAttributeViSession']['attributeValue'] = None
        self._defaults['GetAttributeViString'] = {}
        self._defaults['GetAttributeViString']['return'] = 0
        self._defaults['GetAttributeViString']['attributeValue'] = None
        self._defaults['GetAutoRangeValue'] = {}
        self._defaults['GetAutoRangeValue']['return'] = 0
        self._defaults['GetAutoRangeValue']['actualRange'] = None
        self._defaults['GetCalCount'] = {}
        self._defaults['GetCalCount']['return'] = 0
        self._defaults['GetCalCount']['count'] = None
        self._defaults['GetCalDateAndTime'] = {}
        self._defaults['GetCalDateAndTime']['return'] = 0
        self._defaults['GetCalDateAndTime']['month'] = None
        self._defaults['GetCalDateAndTime']['day'] = None
        self._defaults['GetCalDateAndTime']['year'] = None
        self._defaults['GetCalDateAndTime']['hour'] = None
        self._defaults['GetCalDateAndTime']['minute'] = None
        self._defaults['GetChannelName'] = {}
        self._defaults['GetChannelName']['return'] = 0
        self._defaults['GetChannelName']['channelString'] = None
        self._defaults['GetDevTemp'] = {}
        self._defaults['GetDevTemp']['return'] = 0
        self._defaults['GetDevTemp']['temperature'] = None
        self._defaults['GetError'] = {}
        self._defaults['GetError']['return'] = 0
        self._defaults['GetError']['errorCode'] = None
        self._defaults['GetError']['description'] = None
        self._defaults['GetErrorMessage'] = {}
        self._defaults['GetErrorMessage']['return'] = 0
        self._defaults['GetErrorMessage']['errorMessage'] = None
        self._defaults['GetLastCalTemp'] = {}
        self._defaults['GetLastCalTemp']['return'] = 0
        self._defaults['GetLastCalTemp']['temperature'] = None
        self._defaults['GetMeasurementPeriod'] = {}
        self._defaults['GetMeasurementPeriod']['return'] = 0
        self._defaults['GetMeasurementPeriod']['period'] = None
        self._defaults['GetNextCoercionRecord'] = {}
        self._defaults['GetNextCoercionRecord']['return'] = 0
        self._defaults['GetNextCoercionRecord']['coercionRecord'] = None
        self._defaults['GetNextInterchangeWarning'] = {}
        self._defaults['GetNextInterchangeWarning']['return'] = 0
        self._defaults['GetNextInterchangeWarning']['interchangeWarning'] = None
        self._defaults['GetSelfCalSupported'] = {}
        self._defaults['GetSelfCalSupported']['return'] = 0
        self._defaults['GetSelfCalSupported']['selfCalSupported'] = None
        self._defaults['InitWithOptions'] = {}
        self._defaults['InitWithOptions']['return'] = 0
        self._defaults['InitWithOptions']['vi'] = None
        self._defaults['Initiate'] = {}
        self._defaults['Initiate']['return'] = 0
        self._defaults['IsOverRange'] = {}
        self._defaults['IsOverRange']['return'] = 0
        self._defaults['IsOverRange']['isOverRange'] = None
        self._defaults['IsUnderRange'] = {}
        self._defaults['IsUnderRange']['return'] = 0
        self._defaults['IsUnderRange']['isUnderRange'] = None
        self._defaults['LockSession'] = {}
        self._defaults['LockSession']['return'] = 0
        self._defaults['LockSession']['callerHasLock'] = None
        self._defaults['PerformOpenCableComp'] = {}
        self._defaults['PerformOpenCableComp']['return'] = 0
        self._defaults['PerformOpenCableComp']['conductance'] = None
        self._defaults['PerformOpenCableComp']['susceptance'] = None
        self._defaults['PerformShortCableComp'] = {}
        self._defaults['PerformShortCableComp']['return'] = 0
        self._defaults['PerformShortCableComp']['resistance'] = None
        self._defaults['PerformShortCableComp']['reactance'] = None
        self._defaults['Read'] = {}
        self._defaults['Read']['return'] = 0
        self._defaults['Read']['reading'] = None
        self._defaults['ReadMultiPoint'] = {}
        self._defaults['ReadMultiPoint']['return'] = 0
        self._defaults['ReadMultiPoint']['readingArray'] = None
        self._defaults['ReadMultiPoint']['actualNumberOfPoints'] = None
        self._defaults['ReadStatus'] = {}
        self._defaults['ReadStatus']['return'] = 0
        self._defaults['ReadStatus']['acquisitionBacklog'] = None
        self._defaults['ReadStatus']['acquisitionStatus'] = None
        self._defaults['ReadWaveform'] = {}
        self._defaults['ReadWaveform']['return'] = 0
        self._defaults['ReadWaveform']['waveformArray'] = None
        self._defaults['ReadWaveform']['actualNumberOfPoints'] = None
        self._defaults['ResetInterchangeCheck'] = {}
        self._defaults['ResetInterchangeCheck']['return'] = 0
        self._defaults['ResetWithDefaults'] = {}
        self._defaults['ResetWithDefaults']['return'] = 0
        self._defaults['SelfCal'] = {}
        self._defaults['SelfCal']['return'] = 0
        self._defaults['SendSoftwareTrigger'] = {}
        self._defaults['SendSoftwareTrigger']['return'] = 0
        self._defaults['SetAttributeViBoolean'] = {}
        self._defaults['SetAttributeViBoolean']['return'] = 0
        self._defaults['SetAttributeViInt32'] = {}
        self._defaults['SetAttributeViInt32']['return'] = 0
        self._defaults['SetAttributeViReal64'] = {}
        self._defaults['SetAttributeViReal64']['return'] = 0
        self._defaults['SetAttributeViSession'] = {}
        self._defaults['SetAttributeViSession']['return'] = 0
        self._defaults['SetAttributeViString'] = {}
        self._defaults['SetAttributeViString']['return'] = 0
        self._defaults['UnlockSession'] = {}
        self._defaults['UnlockSession']['return'] = 0
        self._defaults['UnlockSession']['callerHasLock'] = None
        self._defaults['close'] = {}
        self._defaults['close']['return'] = 0
        self._defaults['error_query'] = {}
        self._defaults['error_query']['return'] = 0
        self._defaults['error_query']['errorCode'] = None
        self._defaults['error_query']['errorMessage'] = None
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

    def niDMM_Abort(self, vi):  # noqa: N802
        if self._defaults['Abort']['return'] != 0:
            return self._defaults['Abort']['return']
        return self._defaults['Abort']['return']

    def niDMM_ClearInterchangeWarnings(self, vi):  # noqa: N802
        if self._defaults['ClearInterchangeWarnings']['return'] != 0:
            return self._defaults['ClearInterchangeWarnings']['return']
        return self._defaults['ClearInterchangeWarnings']['return']

    def niDMM_ConfigureACBandwidth(self, vi, ac_minimum_frequency_hz, ac_maximum_frequency_hz):  # noqa: N802
        if self._defaults['ConfigureACBandwidth']['return'] != 0:
            return self._defaults['ConfigureACBandwidth']['return']
        return self._defaults['ConfigureACBandwidth']['return']

    def niDMM_ConfigureADCCalibration(self, vi, adc_calibration):  # noqa: N802
        if self._defaults['ConfigureADCCalibration']['return'] != 0:
            return self._defaults['ConfigureADCCalibration']['return']
        return self._defaults['ConfigureADCCalibration']['return']

    def niDMM_ConfigureAutoZeroMode(self, vi, auto_zero_mode):  # noqa: N802
        if self._defaults['ConfigureAutoZeroMode']['return'] != 0:
            return self._defaults['ConfigureAutoZeroMode']['return']
        return self._defaults['ConfigureAutoZeroMode']['return']

    def niDMM_ConfigureCableCompType(self, vi, cable_comp_type):  # noqa: N802
        if self._defaults['ConfigureCableCompType']['return'] != 0:
            return self._defaults['ConfigureCableCompType']['return']
        return self._defaults['ConfigureCableCompType']['return']

    def niDMM_ConfigureCurrentSource(self, vi, current_source):  # noqa: N802
        if self._defaults['ConfigureCurrentSource']['return'] != 0:
            return self._defaults['ConfigureCurrentSource']['return']
        return self._defaults['ConfigureCurrentSource']['return']

    def niDMM_ConfigureFixedRefJunction(self, vi, fixed_reference_junction):  # noqa: N802
        if self._defaults['ConfigureFixedRefJunction']['return'] != 0:
            return self._defaults['ConfigureFixedRefJunction']['return']
        return self._defaults['ConfigureFixedRefJunction']['return']

    def niDMM_ConfigureFrequencyVoltageRange(self, vi, voltage_range):  # noqa: N802
        if self._defaults['ConfigureFrequencyVoltageRange']['return'] != 0:
            return self._defaults['ConfigureFrequencyVoltageRange']['return']
        return self._defaults['ConfigureFrequencyVoltageRange']['return']

    def niDMM_ConfigureMeasCompleteDest(self, vi, meas_complete_destination):  # noqa: N802
        if self._defaults['ConfigureMeasCompleteDest']['return'] != 0:
            return self._defaults['ConfigureMeasCompleteDest']['return']
        return self._defaults['ConfigureMeasCompleteDest']['return']

    def niDMM_ConfigureMeasCompleteSlope(self, vi, meas_complete_slope):  # noqa: N802
        if self._defaults['ConfigureMeasCompleteSlope']['return'] != 0:
            return self._defaults['ConfigureMeasCompleteSlope']['return']
        return self._defaults['ConfigureMeasCompleteSlope']['return']

    def niDMM_ConfigureMeasurementAbsolute(self, vi, measurement_function, range, resolution_absolute):  # noqa: N802
        if self._defaults['ConfigureMeasurementAbsolute']['return'] != 0:
            return self._defaults['ConfigureMeasurementAbsolute']['return']
        return self._defaults['ConfigureMeasurementAbsolute']['return']

    def niDMM_ConfigureMeasurementDigits(self, vi, measurement_function, range, resolution_digits):  # noqa: N802
        if self._defaults['ConfigureMeasurementDigits']['return'] != 0:
            return self._defaults['ConfigureMeasurementDigits']['return']
        return self._defaults['ConfigureMeasurementDigits']['return']

    def niDMM_ConfigureMultiPoint(self, vi, trigger_count, sample_count, sample_trigger, sample_interval):  # noqa: N802
        if self._defaults['ConfigureMultiPoint']['return'] != 0:
            return self._defaults['ConfigureMultiPoint']['return']
        return self._defaults['ConfigureMultiPoint']['return']

    def niDMM_ConfigureOffsetCompOhms(self, vi, offset_comp_ohms):  # noqa: N802
        if self._defaults['ConfigureOffsetCompOhms']['return'] != 0:
            return self._defaults['ConfigureOffsetCompOhms']['return']
        return self._defaults['ConfigureOffsetCompOhms']['return']

    def niDMM_ConfigureOpenCableCompValues(self, vi, conductance, susceptance):  # noqa: N802
        if self._defaults['ConfigureOpenCableCompValues']['return'] != 0:
            return self._defaults['ConfigureOpenCableCompValues']['return']
        return self._defaults['ConfigureOpenCableCompValues']['return']

    def niDMM_ConfigurePowerLineFrequency(self, vi, power_line_frequency_hz):  # noqa: N802
        if self._defaults['ConfigurePowerLineFrequency']['return'] != 0:
            return self._defaults['ConfigurePowerLineFrequency']['return']
        return self._defaults['ConfigurePowerLineFrequency']['return']

    def niDMM_ConfigureRTDCustom(self, vi, rtd_a, rtd_b, rtd_c):  # noqa: N802
        if self._defaults['ConfigureRTDCustom']['return'] != 0:
            return self._defaults['ConfigureRTDCustom']['return']
        return self._defaults['ConfigureRTDCustom']['return']

    def niDMM_ConfigureRTDType(self, vi, rtd_type, rtd_resistance):  # noqa: N802
        if self._defaults['ConfigureRTDType']['return'] != 0:
            return self._defaults['ConfigureRTDType']['return']
        return self._defaults['ConfigureRTDType']['return']

    def niDMM_ConfigureSampleTriggerSlope(self, vi, sample_trigger_slope):  # noqa: N802
        if self._defaults['ConfigureSampleTriggerSlope']['return'] != 0:
            return self._defaults['ConfigureSampleTriggerSlope']['return']
        return self._defaults['ConfigureSampleTriggerSlope']['return']

    def niDMM_ConfigureShortCableCompValues(self, vi, resistance, reactance):  # noqa: N802
        if self._defaults['ConfigureShortCableCompValues']['return'] != 0:
            return self._defaults['ConfigureShortCableCompValues']['return']
        return self._defaults['ConfigureShortCableCompValues']['return']

    def niDMM_ConfigureThermistorCustom(self, vi, thermistor_a, thermistor_b, thermistor_c):  # noqa: N802
        if self._defaults['ConfigureThermistorCustom']['return'] != 0:
            return self._defaults['ConfigureThermistorCustom']['return']
        return self._defaults['ConfigureThermistorCustom']['return']

    def niDMM_ConfigureThermistorType(self, vi, thermistor_type):  # noqa: N802
        if self._defaults['ConfigureThermistorType']['return'] != 0:
            return self._defaults['ConfigureThermistorType']['return']
        return self._defaults['ConfigureThermistorType']['return']

    def niDMM_ConfigureThermocouple(self, vi, thermocouple_type, reference_junction_type):  # noqa: N802
        if self._defaults['ConfigureThermocouple']['return'] != 0:
            return self._defaults['ConfigureThermocouple']['return']
        return self._defaults['ConfigureThermocouple']['return']

    def niDMM_ConfigureTransducerType(self, vi, transducer_type):  # noqa: N802
        if self._defaults['ConfigureTransducerType']['return'] != 0:
            return self._defaults['ConfigureTransducerType']['return']
        return self._defaults['ConfigureTransducerType']['return']

    def niDMM_ConfigureTrigger(self, vi, trigger_source, trigger_delay):  # noqa: N802
        if self._defaults['ConfigureTrigger']['return'] != 0:
            return self._defaults['ConfigureTrigger']['return']
        return self._defaults['ConfigureTrigger']['return']

    def niDMM_ConfigureTriggerSlope(self, vi, trigger_slope):  # noqa: N802
        if self._defaults['ConfigureTriggerSlope']['return'] != 0:
            return self._defaults['ConfigureTriggerSlope']['return']
        return self._defaults['ConfigureTriggerSlope']['return']

    def niDMM_ConfigureWaveformAcquisition(self, vi, measurement_function, range, rate, waveform_points):  # noqa: N802
        if self._defaults['ConfigureWaveformAcquisition']['return'] != 0:
            return self._defaults['ConfigureWaveformAcquisition']['return']
        return self._defaults['ConfigureWaveformAcquisition']['return']

    def niDMM_ConfigureWaveformCoupling(self, vi, waveform_coupling):  # noqa: N802
        if self._defaults['ConfigureWaveformCoupling']['return'] != 0:
            return self._defaults['ConfigureWaveformCoupling']['return']
        return self._defaults['ConfigureWaveformCoupling']['return']

    def niDMM_Disable(self, vi):  # noqa: N802
        if self._defaults['Disable']['return'] != 0:
            return self._defaults['Disable']['return']
        return self._defaults['Disable']['return']

    def niDMM_Fetch(self, vi, maximum_time, reading):  # noqa: N802
        if self._defaults['Fetch']['return'] != 0:
            return self._defaults['Fetch']['return']
        if self._defaults['Fetch']['reading'] is None:
            raise MockFunctionCallError("niDMM_Fetch", param='reading')
        reading.contents.value = self._defaults['Fetch']['reading']
        return self._defaults['Fetch']['return']

    def niDMM_FetchMultiPoint(self, vi, maximum_time, array_size, reading_array, actual_number_of_points):  # noqa: N802
        if self._defaults['FetchMultiPoint']['return'] != 0:
            return self._defaults['FetchMultiPoint']['return']
        if self._defaults['FetchMultiPoint']['readingArray'] is None:
            raise MockFunctionCallError("niDMM_FetchMultiPoint", param='readingArray')
        reading_array.contents.value = self._defaults['FetchMultiPoint']['readingArray']
        if self._defaults['FetchMultiPoint']['actualNumberOfPoints'] is None:
            raise MockFunctionCallError("niDMM_FetchMultiPoint", param='actualNumberOfPoints')
        actual_number_of_points.contents.value = self._defaults['FetchMultiPoint']['actualNumberOfPoints']
        return self._defaults['FetchMultiPoint']['return']

    def niDMM_FetchWaveform(self, vi, maximum_time, array_size, waveform_array, actual_number_of_points):  # noqa: N802
        if self._defaults['FetchWaveform']['return'] != 0:
            return self._defaults['FetchWaveform']['return']
        if self._defaults['FetchWaveform']['waveformArray'] is None:
            raise MockFunctionCallError("niDMM_FetchWaveform", param='waveformArray')
        waveform_array.contents.value = self._defaults['FetchWaveform']['waveformArray']
        if self._defaults['FetchWaveform']['actualNumberOfPoints'] is None:
            raise MockFunctionCallError("niDMM_FetchWaveform", param='actualNumberOfPoints')
        actual_number_of_points.contents.value = self._defaults['FetchWaveform']['actualNumberOfPoints']
        return self._defaults['FetchWaveform']['return']

    def niDMM_FormatMeasAbsolute(self, measurement_function, range, resolution, measurement, mode_string, range_string, data_string):  # noqa: N802
        if self._defaults['FormatMeasAbsolute']['return'] != 0:
            return self._defaults['FormatMeasAbsolute']['return']
        if self._defaults['FormatMeasAbsolute']['modeString'] is None:
            raise MockFunctionCallError("niDMM_FormatMeasAbsolute", param='modeString')
        mode_string.contents.value = self._defaults['FormatMeasAbsolute']['modeString']
        if self._defaults['FormatMeasAbsolute']['rangeString'] is None:
            raise MockFunctionCallError("niDMM_FormatMeasAbsolute", param='rangeString')
        range_string.contents.value = self._defaults['FormatMeasAbsolute']['rangeString']
        if self._defaults['FormatMeasAbsolute']['dataString'] is None:
            raise MockFunctionCallError("niDMM_FormatMeasAbsolute", param='dataString')
        data_string.contents.value = self._defaults['FormatMeasAbsolute']['dataString']
        return self._defaults['FormatMeasAbsolute']['return']

    def niDMM_GetApertureTimeInfo(self, vi, aperture_time, aperture_time_units):  # noqa: N802
        if self._defaults['GetApertureTimeInfo']['return'] != 0:
            return self._defaults['GetApertureTimeInfo']['return']
        if self._defaults['GetApertureTimeInfo']['apertureTime'] is None:
            raise MockFunctionCallError("niDMM_GetApertureTimeInfo", param='apertureTime')
        aperture_time.contents.value = self._defaults['GetApertureTimeInfo']['apertureTime']
        if self._defaults['GetApertureTimeInfo']['apertureTimeUnits'] is None:
            raise MockFunctionCallError("niDMM_GetApertureTimeInfo", param='apertureTimeUnits')
        aperture_time_units.contents.value = self._defaults['GetApertureTimeInfo']['apertureTimeUnits']
        return self._defaults['GetApertureTimeInfo']['return']

    def niDMM_GetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViBoolean']['return'] != 0:
            return self._defaults['GetAttributeViBoolean']['return']
        if self._defaults['GetAttributeViBoolean']['attributeValue'] is None:
            raise MockFunctionCallError("niDMM_GetAttributeViBoolean", param='attributeValue')
        attribute_value.contents.value = self._defaults['GetAttributeViBoolean']['attributeValue']
        return self._defaults['GetAttributeViBoolean']['return']

    def niDMM_GetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViInt32']['return'] != 0:
            return self._defaults['GetAttributeViInt32']['return']
        if self._defaults['GetAttributeViInt32']['attributeValue'] is None:
            raise MockFunctionCallError("niDMM_GetAttributeViInt32", param='attributeValue')
        attribute_value.contents.value = self._defaults['GetAttributeViInt32']['attributeValue']
        return self._defaults['GetAttributeViInt32']['return']

    def niDMM_GetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViReal64']['return'] != 0:
            return self._defaults['GetAttributeViReal64']['return']
        if self._defaults['GetAttributeViReal64']['attributeValue'] is None:
            raise MockFunctionCallError("niDMM_GetAttributeViReal64", param='attributeValue')
        attribute_value.contents.value = self._defaults['GetAttributeViReal64']['attributeValue']
        return self._defaults['GetAttributeViReal64']['return']

    def niDMM_GetAttributeViSession(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViSession']['return'] != 0:
            return self._defaults['GetAttributeViSession']['return']
        if self._defaults['GetAttributeViSession']['attributeValue'] is None:
            raise MockFunctionCallError("niDMM_GetAttributeViSession", param='attributeValue')
        attribute_value.contents.value = self._defaults['GetAttributeViSession']['attributeValue']
        return self._defaults['GetAttributeViSession']['return']

    def niDMM_GetAttributeViString(self, vi, channel_name, attribute_id, buffer_size, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViString']['return'] != 0:
            return self._defaults['GetAttributeViString']['return']
        if self._defaults['GetAttributeViString']['attributeValue'] is None:
            raise MockFunctionCallError("niDMM_GetAttributeViString", param='attributeValue')
        if buffer_size == 0:
            return len(self._defaults['GetAttributeViString']['attributeValue'])
        t = nidmm.ctypes_types.ViString_ctype(self._defaults['GetAttributeViString']['attributeValue'].encode('ascii'))
        attribute_value.value = ctypes.cast(t, nidmm.ctypes_types.ViString_ctype).value
        return self._defaults['GetAttributeViString']['return']

    def niDMM_GetAutoRangeValue(self, vi, actual_range):  # noqa: N802
        if self._defaults['GetAutoRangeValue']['return'] != 0:
            return self._defaults['GetAutoRangeValue']['return']
        if self._defaults['GetAutoRangeValue']['actualRange'] is None:
            raise MockFunctionCallError("niDMM_GetAutoRangeValue", param='actualRange')
        actual_range.contents.value = self._defaults['GetAutoRangeValue']['actualRange']
        return self._defaults['GetAutoRangeValue']['return']

    def niDMM_GetCalCount(self, vi, cal_type, count):  # noqa: N802
        if self._defaults['GetCalCount']['return'] != 0:
            return self._defaults['GetCalCount']['return']
        if self._defaults['GetCalCount']['count'] is None:
            raise MockFunctionCallError("niDMM_GetCalCount", param='count')
        count.contents.value = self._defaults['GetCalCount']['count']
        return self._defaults['GetCalCount']['return']

    def niDMM_GetCalDateAndTime(self, vi, cal_type, month, day, year, hour, minute):  # noqa: N802
        if self._defaults['GetCalDateAndTime']['return'] != 0:
            return self._defaults['GetCalDateAndTime']['return']
        if self._defaults['GetCalDateAndTime']['month'] is None:
            raise MockFunctionCallError("niDMM_GetCalDateAndTime", param='month')
        month.contents.value = self._defaults['GetCalDateAndTime']['month']
        if self._defaults['GetCalDateAndTime']['day'] is None:
            raise MockFunctionCallError("niDMM_GetCalDateAndTime", param='day')
        day.contents.value = self._defaults['GetCalDateAndTime']['day']
        if self._defaults['GetCalDateAndTime']['year'] is None:
            raise MockFunctionCallError("niDMM_GetCalDateAndTime", param='year')
        year.contents.value = self._defaults['GetCalDateAndTime']['year']
        if self._defaults['GetCalDateAndTime']['hour'] is None:
            raise MockFunctionCallError("niDMM_GetCalDateAndTime", param='hour')
        hour.contents.value = self._defaults['GetCalDateAndTime']['hour']
        if self._defaults['GetCalDateAndTime']['minute'] is None:
            raise MockFunctionCallError("niDMM_GetCalDateAndTime", param='minute')
        minute.contents.value = self._defaults['GetCalDateAndTime']['minute']
        return self._defaults['GetCalDateAndTime']['return']

    def niDMM_GetChannelName(self, vi, index, buffer_size, channel_string):  # noqa: N802
        if self._defaults['GetChannelName']['return'] != 0:
            return self._defaults['GetChannelName']['return']
        if self._defaults['GetChannelName']['channelString'] is None:
            raise MockFunctionCallError("niDMM_GetChannelName", param='channelString')
        channel_string.contents.value = self._defaults['GetChannelName']['channelString']
        return self._defaults['GetChannelName']['return']

    def niDMM_GetDevTemp(self, vi, options, temperature):  # noqa: N802
        if self._defaults['GetDevTemp']['return'] != 0:
            return self._defaults['GetDevTemp']['return']
        if self._defaults['GetDevTemp']['temperature'] is None:
            raise MockFunctionCallError("niDMM_GetDevTemp", param='temperature')
        temperature.contents.value = self._defaults['GetDevTemp']['temperature']
        return self._defaults['GetDevTemp']['return']

    def niDMM_GetError(self, vi, error_code, buffer_size, description):  # noqa: N802
        if self._defaults['GetError']['return'] != 0:
            return self._defaults['GetError']['return']
        if self._defaults['GetError']['errorCode'] is None:
            raise MockFunctionCallError("niDMM_GetError", param='errorCode')
        error_code.contents.value = self._defaults['GetError']['errorCode']
        if self._defaults['GetError']['description'] is None:
            raise MockFunctionCallError("niDMM_GetError", param='description')
        if buffer_size == 0:
            return len(self._defaults['GetError']['description'])
        t = nidmm.ctypes_types.ViString_ctype(self._defaults['GetError']['description'].encode('ascii'))
        description.value = ctypes.cast(t, nidmm.ctypes_types.ViString_ctype).value
        return self._defaults['GetError']['return']

    def niDMM_GetErrorMessage(self, vi, error_code, buffer_size, error_message):  # noqa: N802
        if self._defaults['GetErrorMessage']['return'] != 0:
            return self._defaults['GetErrorMessage']['return']
        if self._defaults['GetErrorMessage']['errorMessage'] is None:
            raise MockFunctionCallError("niDMM_GetErrorMessage", param='errorMessage')
        if buffer_size == 0:
            return len(self._defaults['GetErrorMessage']['errorMessage'])
        t = nidmm.ctypes_types.ViString_ctype(self._defaults['GetErrorMessage']['errorMessage'].encode('ascii'))
        error_message.value = ctypes.cast(t, nidmm.ctypes_types.ViString_ctype).value
        return self._defaults['GetErrorMessage']['return']

    def niDMM_GetLastCalTemp(self, vi, cal_type, temperature):  # noqa: N802
        if self._defaults['GetLastCalTemp']['return'] != 0:
            return self._defaults['GetLastCalTemp']['return']
        if self._defaults['GetLastCalTemp']['temperature'] is None:
            raise MockFunctionCallError("niDMM_GetLastCalTemp", param='temperature')
        temperature.contents.value = self._defaults['GetLastCalTemp']['temperature']
        return self._defaults['GetLastCalTemp']['return']

    def niDMM_GetMeasurementPeriod(self, vi, period):  # noqa: N802
        if self._defaults['GetMeasurementPeriod']['return'] != 0:
            return self._defaults['GetMeasurementPeriod']['return']
        if self._defaults['GetMeasurementPeriod']['period'] is None:
            raise MockFunctionCallError("niDMM_GetMeasurementPeriod", param='period')
        period.contents.value = self._defaults['GetMeasurementPeriod']['period']
        return self._defaults['GetMeasurementPeriod']['return']

    def niDMM_GetNextCoercionRecord(self, vi, buffer_size, coercion_record):  # noqa: N802
        if self._defaults['GetNextCoercionRecord']['return'] != 0:
            return self._defaults['GetNextCoercionRecord']['return']
        if self._defaults['GetNextCoercionRecord']['coercionRecord'] is None:
            raise MockFunctionCallError("niDMM_GetNextCoercionRecord", param='coercionRecord')
        coercion_record.contents.value = self._defaults['GetNextCoercionRecord']['coercionRecord']
        return self._defaults['GetNextCoercionRecord']['return']

    def niDMM_GetNextInterchangeWarning(self, vi, buffer_size, interchange_warning):  # noqa: N802
        if self._defaults['GetNextInterchangeWarning']['return'] != 0:
            return self._defaults['GetNextInterchangeWarning']['return']
        if self._defaults['GetNextInterchangeWarning']['interchangeWarning'] is None:
            raise MockFunctionCallError("niDMM_GetNextInterchangeWarning", param='interchangeWarning')
        if buffer_size == 0:
            return len(self._defaults['GetNextInterchangeWarning']['interchangeWarning'])
        t = nidmm.ctypes_types.ViChar_ctype(self._defaults['GetNextInterchangeWarning']['interchangeWarning'].encode('ascii'))
        interchange_warning.value = ctypes.cast(t, nidmm.ctypes_types.ViChar_ctype).value
        return self._defaults['GetNextInterchangeWarning']['return']

    def niDMM_GetSelfCalSupported(self, vi, self_cal_supported):  # noqa: N802
        if self._defaults['GetSelfCalSupported']['return'] != 0:
            return self._defaults['GetSelfCalSupported']['return']
        if self._defaults['GetSelfCalSupported']['selfCalSupported'] is None:
            raise MockFunctionCallError("niDMM_GetSelfCalSupported", param='selfCalSupported')
        self_cal_supported.contents.value = self._defaults['GetSelfCalSupported']['selfCalSupported']
        return self._defaults['GetSelfCalSupported']['return']

    def niDMM_InitWithOptions(self, resource_name, id_query, reset_device, option_string, vi):  # noqa: N802
        if self._defaults['InitWithOptions']['return'] != 0:
            return self._defaults['InitWithOptions']['return']
        if self._defaults['InitWithOptions']['vi'] is None:
            raise MockFunctionCallError("niDMM_InitWithOptions", param='vi')
        vi.contents.value = self._defaults['InitWithOptions']['vi']
        return self._defaults['InitWithOptions']['return']

    def niDMM_Initiate(self, vi):  # noqa: N802
        if self._defaults['Initiate']['return'] != 0:
            return self._defaults['Initiate']['return']
        return self._defaults['Initiate']['return']

    def niDMM_IsOverRange(self, vi, measurement_value, is_over_range):  # noqa: N802
        if self._defaults['IsOverRange']['return'] != 0:
            return self._defaults['IsOverRange']['return']
        if self._defaults['IsOverRange']['isOverRange'] is None:
            raise MockFunctionCallError("niDMM_IsOverRange", param='isOverRange')
        is_over_range.contents.value = self._defaults['IsOverRange']['isOverRange']
        return self._defaults['IsOverRange']['return']

    def niDMM_IsUnderRange(self, vi, measurement_value, is_under_range):  # noqa: N802
        if self._defaults['IsUnderRange']['return'] != 0:
            return self._defaults['IsUnderRange']['return']
        if self._defaults['IsUnderRange']['isUnderRange'] is None:
            raise MockFunctionCallError("niDMM_IsUnderRange", param='isUnderRange')
        is_under_range.contents.value = self._defaults['IsUnderRange']['isUnderRange']
        return self._defaults['IsUnderRange']['return']

    def niDMM_LockSession(self, vi, caller_has_lock):  # noqa: N802
        if self._defaults['LockSession']['return'] != 0:
            return self._defaults['LockSession']['return']
        if self._defaults['LockSession']['callerHasLock'] is None:
            raise MockFunctionCallError("niDMM_LockSession", param='callerHasLock')
        caller_has_lock.contents.value = self._defaults['LockSession']['callerHasLock']
        return self._defaults['LockSession']['return']

    def niDMM_PerformOpenCableComp(self, vi, conductance, susceptance):  # noqa: N802
        if self._defaults['PerformOpenCableComp']['return'] != 0:
            return self._defaults['PerformOpenCableComp']['return']
        if self._defaults['PerformOpenCableComp']['conductance'] is None:
            raise MockFunctionCallError("niDMM_PerformOpenCableComp", param='conductance')
        conductance.contents.value = self._defaults['PerformOpenCableComp']['conductance']
        if self._defaults['PerformOpenCableComp']['susceptance'] is None:
            raise MockFunctionCallError("niDMM_PerformOpenCableComp", param='susceptance')
        susceptance.contents.value = self._defaults['PerformOpenCableComp']['susceptance']
        return self._defaults['PerformOpenCableComp']['return']

    def niDMM_PerformShortCableComp(self, vi, resistance, reactance):  # noqa: N802
        if self._defaults['PerformShortCableComp']['return'] != 0:
            return self._defaults['PerformShortCableComp']['return']
        if self._defaults['PerformShortCableComp']['resistance'] is None:
            raise MockFunctionCallError("niDMM_PerformShortCableComp", param='resistance')
        resistance.contents.value = self._defaults['PerformShortCableComp']['resistance']
        if self._defaults['PerformShortCableComp']['reactance'] is None:
            raise MockFunctionCallError("niDMM_PerformShortCableComp", param='reactance')
        reactance.contents.value = self._defaults['PerformShortCableComp']['reactance']
        return self._defaults['PerformShortCableComp']['return']

    def niDMM_Read(self, vi, maximum_time, reading):  # noqa: N802
        if self._defaults['Read']['return'] != 0:
            return self._defaults['Read']['return']
        if self._defaults['Read']['reading'] is None:
            raise MockFunctionCallError("niDMM_Read", param='reading')
        reading.contents.value = self._defaults['Read']['reading']
        return self._defaults['Read']['return']

    def niDMM_ReadMultiPoint(self, vi, maximum_time, array_size, reading_array, actual_number_of_points):  # noqa: N802
        if self._defaults['ReadMultiPoint']['return'] != 0:
            return self._defaults['ReadMultiPoint']['return']
        if self._defaults['ReadMultiPoint']['readingArray'] is None:
            raise MockFunctionCallError("niDMM_ReadMultiPoint", param='readingArray')
        reading_array.contents.value = self._defaults['ReadMultiPoint']['readingArray']
        if self._defaults['ReadMultiPoint']['actualNumberOfPoints'] is None:
            raise MockFunctionCallError("niDMM_ReadMultiPoint", param='actualNumberOfPoints')
        actual_number_of_points.contents.value = self._defaults['ReadMultiPoint']['actualNumberOfPoints']
        return self._defaults['ReadMultiPoint']['return']

    def niDMM_ReadStatus(self, vi, acquisition_backlog, acquisition_status):  # noqa: N802
        if self._defaults['ReadStatus']['return'] != 0:
            return self._defaults['ReadStatus']['return']
        if self._defaults['ReadStatus']['acquisitionBacklog'] is None:
            raise MockFunctionCallError("niDMM_ReadStatus", param='acquisitionBacklog')
        acquisition_backlog.contents.value = self._defaults['ReadStatus']['acquisitionBacklog']
        if self._defaults['ReadStatus']['acquisitionStatus'] is None:
            raise MockFunctionCallError("niDMM_ReadStatus", param='acquisitionStatus')
        acquisition_status.contents.value = self._defaults['ReadStatus']['acquisitionStatus']
        return self._defaults['ReadStatus']['return']

    def niDMM_ReadWaveform(self, vi, maximum_time, array_size, waveform_array, actual_number_of_points):  # noqa: N802
        if self._defaults['ReadWaveform']['return'] != 0:
            return self._defaults['ReadWaveform']['return']
        if self._defaults['ReadWaveform']['waveformArray'] is None:
            raise MockFunctionCallError("niDMM_ReadWaveform", param='waveformArray')
        waveform_array.contents.value = self._defaults['ReadWaveform']['waveformArray']
        if self._defaults['ReadWaveform']['actualNumberOfPoints'] is None:
            raise MockFunctionCallError("niDMM_ReadWaveform", param='actualNumberOfPoints')
        actual_number_of_points.contents.value = self._defaults['ReadWaveform']['actualNumberOfPoints']
        return self._defaults['ReadWaveform']['return']

    def niDMM_ResetInterchangeCheck(self, vi):  # noqa: N802
        if self._defaults['ResetInterchangeCheck']['return'] != 0:
            return self._defaults['ResetInterchangeCheck']['return']
        return self._defaults['ResetInterchangeCheck']['return']

    def niDMM_ResetWithDefaults(self, vi):  # noqa: N802
        if self._defaults['ResetWithDefaults']['return'] != 0:
            return self._defaults['ResetWithDefaults']['return']
        return self._defaults['ResetWithDefaults']['return']

    def niDMM_SelfCal(self, vi):  # noqa: N802
        if self._defaults['SelfCal']['return'] != 0:
            return self._defaults['SelfCal']['return']
        return self._defaults['SelfCal']['return']

    def niDMM_SendSoftwareTrigger(self, vi):  # noqa: N802
        if self._defaults['SendSoftwareTrigger']['return'] != 0:
            return self._defaults['SendSoftwareTrigger']['return']
        return self._defaults['SendSoftwareTrigger']['return']

    def niDMM_SetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViBoolean']['return'] != 0:
            return self._defaults['SetAttributeViBoolean']['return']
        return self._defaults['SetAttributeViBoolean']['return']

    def niDMM_SetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViInt32']['return'] != 0:
            return self._defaults['SetAttributeViInt32']['return']
        return self._defaults['SetAttributeViInt32']['return']

    def niDMM_SetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViReal64']['return'] != 0:
            return self._defaults['SetAttributeViReal64']['return']
        return self._defaults['SetAttributeViReal64']['return']

    def niDMM_SetAttributeViSession(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViSession']['return'] != 0:
            return self._defaults['SetAttributeViSession']['return']
        return self._defaults['SetAttributeViSession']['return']

    def niDMM_SetAttributeViString(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViString']['return'] != 0:
            return self._defaults['SetAttributeViString']['return']
        return self._defaults['SetAttributeViString']['return']

    def niDMM_UnlockSession(self, vi, caller_has_lock):  # noqa: N802
        if self._defaults['UnlockSession']['return'] != 0:
            return self._defaults['UnlockSession']['return']
        if self._defaults['UnlockSession']['callerHasLock'] is None:
            raise MockFunctionCallError("niDMM_UnlockSession", param='callerHasLock')
        caller_has_lock.contents.value = self._defaults['UnlockSession']['callerHasLock']
        return self._defaults['UnlockSession']['return']

    def niDMM_close(self, vi):  # noqa: N802
        if self._defaults['close']['return'] != 0:
            return self._defaults['close']['return']
        return self._defaults['close']['return']

    def niDMM_error_query(self, vi, error_code, error_message):  # noqa: N802
        if self._defaults['error_query']['return'] != 0:
            return self._defaults['error_query']['return']
        if self._defaults['error_query']['errorCode'] is None:
            raise MockFunctionCallError("niDMM_error_query", param='errorCode')
        error_code.contents.value = self._defaults['error_query']['errorCode']
        if self._defaults['error_query']['errorMessage'] is None:
            raise MockFunctionCallError("niDMM_error_query", param='errorMessage')
        error_message.contents.value = self._defaults['error_query']['errorMessage']
        return self._defaults['error_query']['return']

    def niDMM_reset(self, vi):  # noqa: N802
        if self._defaults['reset']['return'] != 0:
            return self._defaults['reset']['return']
        return self._defaults['reset']['return']

    def niDMM_revision_query(self, vi, instrument_driver_revision, firmware_revision):  # noqa: N802
        if self._defaults['revision_query']['return'] != 0:
            return self._defaults['revision_query']['return']
        if self._defaults['revision_query']['instrumentDriverRevision'] is None:
            raise MockFunctionCallError("niDMM_revision_query", param='instrumentDriverRevision')
        instrument_driver_revision.contents.value = self._defaults['revision_query']['instrumentDriverRevision']
        if self._defaults['revision_query']['firmwareRevision'] is None:
            raise MockFunctionCallError("niDMM_revision_query", param='firmwareRevision')
        firmware_revision.contents.value = self._defaults['revision_query']['firmwareRevision']
        return self._defaults['revision_query']['return']

    def niDMM_self_test(self, vi, self_test_result, self_test_message):  # noqa: N802
        if self._defaults['self_test']['return'] != 0:
            return self._defaults['self_test']['return']
        if self._defaults['self_test']['selfTestResult'] is None:
            raise MockFunctionCallError("niDMM_self_test", param='selfTestResult')
        self_test_result.contents.value = self._defaults['self_test']['selfTestResult']
        if self._defaults['self_test']['selfTestMessage'] is None:
            raise MockFunctionCallError("niDMM_self_test", param='selfTestMessage')
        self_test_message.contents.value = self._defaults['self_test']['selfTestMessage']
        return self._defaults['self_test']['return']

    # Helper function to setup Mock object with default side effects and return values
    def set_side_effects_and_return_values(self, mock_library):
        mock_library.niDMM_Abort.side_effect = MockFunctionCallError("niDMM_Abort")
        mock_library.niDMM_Abort.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_ClearInterchangeWarnings.side_effect = MockFunctionCallError("niDMM_ClearInterchangeWarnings")
        mock_library.niDMM_ClearInterchangeWarnings.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_ConfigureACBandwidth.side_effect = MockFunctionCallError("niDMM_ConfigureACBandwidth")
        mock_library.niDMM_ConfigureACBandwidth.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_ConfigureADCCalibration.side_effect = MockFunctionCallError("niDMM_ConfigureADCCalibration")
        mock_library.niDMM_ConfigureADCCalibration.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_ConfigureAutoZeroMode.side_effect = MockFunctionCallError("niDMM_ConfigureAutoZeroMode")
        mock_library.niDMM_ConfigureAutoZeroMode.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_ConfigureCableCompType.side_effect = MockFunctionCallError("niDMM_ConfigureCableCompType")
        mock_library.niDMM_ConfigureCableCompType.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_ConfigureCurrentSource.side_effect = MockFunctionCallError("niDMM_ConfigureCurrentSource")
        mock_library.niDMM_ConfigureCurrentSource.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_ConfigureFixedRefJunction.side_effect = MockFunctionCallError("niDMM_ConfigureFixedRefJunction")
        mock_library.niDMM_ConfigureFixedRefJunction.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_ConfigureFrequencyVoltageRange.side_effect = MockFunctionCallError("niDMM_ConfigureFrequencyVoltageRange")
        mock_library.niDMM_ConfigureFrequencyVoltageRange.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_ConfigureMeasCompleteDest.side_effect = MockFunctionCallError("niDMM_ConfigureMeasCompleteDest")
        mock_library.niDMM_ConfigureMeasCompleteDest.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_ConfigureMeasCompleteSlope.side_effect = MockFunctionCallError("niDMM_ConfigureMeasCompleteSlope")
        mock_library.niDMM_ConfigureMeasCompleteSlope.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_ConfigureMeasurementAbsolute.side_effect = MockFunctionCallError("niDMM_ConfigureMeasurementAbsolute")
        mock_library.niDMM_ConfigureMeasurementAbsolute.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_ConfigureMeasurementDigits.side_effect = MockFunctionCallError("niDMM_ConfigureMeasurementDigits")
        mock_library.niDMM_ConfigureMeasurementDigits.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_ConfigureMultiPoint.side_effect = MockFunctionCallError("niDMM_ConfigureMultiPoint")
        mock_library.niDMM_ConfigureMultiPoint.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_ConfigureOffsetCompOhms.side_effect = MockFunctionCallError("niDMM_ConfigureOffsetCompOhms")
        mock_library.niDMM_ConfigureOffsetCompOhms.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_ConfigureOpenCableCompValues.side_effect = MockFunctionCallError("niDMM_ConfigureOpenCableCompValues")
        mock_library.niDMM_ConfigureOpenCableCompValues.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_ConfigurePowerLineFrequency.side_effect = MockFunctionCallError("niDMM_ConfigurePowerLineFrequency")
        mock_library.niDMM_ConfigurePowerLineFrequency.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_ConfigureRTDCustom.side_effect = MockFunctionCallError("niDMM_ConfigureRTDCustom")
        mock_library.niDMM_ConfigureRTDCustom.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_ConfigureRTDType.side_effect = MockFunctionCallError("niDMM_ConfigureRTDType")
        mock_library.niDMM_ConfigureRTDType.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_ConfigureSampleTriggerSlope.side_effect = MockFunctionCallError("niDMM_ConfigureSampleTriggerSlope")
        mock_library.niDMM_ConfigureSampleTriggerSlope.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_ConfigureShortCableCompValues.side_effect = MockFunctionCallError("niDMM_ConfigureShortCableCompValues")
        mock_library.niDMM_ConfigureShortCableCompValues.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_ConfigureThermistorCustom.side_effect = MockFunctionCallError("niDMM_ConfigureThermistorCustom")
        mock_library.niDMM_ConfigureThermistorCustom.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_ConfigureThermistorType.side_effect = MockFunctionCallError("niDMM_ConfigureThermistorType")
        mock_library.niDMM_ConfigureThermistorType.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_ConfigureThermocouple.side_effect = MockFunctionCallError("niDMM_ConfigureThermocouple")
        mock_library.niDMM_ConfigureThermocouple.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_ConfigureTransducerType.side_effect = MockFunctionCallError("niDMM_ConfigureTransducerType")
        mock_library.niDMM_ConfigureTransducerType.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_ConfigureTrigger.side_effect = MockFunctionCallError("niDMM_ConfigureTrigger")
        mock_library.niDMM_ConfigureTrigger.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_ConfigureTriggerSlope.side_effect = MockFunctionCallError("niDMM_ConfigureTriggerSlope")
        mock_library.niDMM_ConfigureTriggerSlope.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_ConfigureWaveformAcquisition.side_effect = MockFunctionCallError("niDMM_ConfigureWaveformAcquisition")
        mock_library.niDMM_ConfigureWaveformAcquisition.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_ConfigureWaveformCoupling.side_effect = MockFunctionCallError("niDMM_ConfigureWaveformCoupling")
        mock_library.niDMM_ConfigureWaveformCoupling.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_Disable.side_effect = MockFunctionCallError("niDMM_Disable")
        mock_library.niDMM_Disable.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_Fetch.side_effect = MockFunctionCallError("niDMM_Fetch")
        mock_library.niDMM_Fetch.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_FetchMultiPoint.side_effect = MockFunctionCallError("niDMM_FetchMultiPoint")
        mock_library.niDMM_FetchMultiPoint.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_FetchWaveform.side_effect = MockFunctionCallError("niDMM_FetchWaveform")
        mock_library.niDMM_FetchWaveform.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_FormatMeasAbsolute.side_effect = MockFunctionCallError("niDMM_FormatMeasAbsolute")
        mock_library.niDMM_FormatMeasAbsolute.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_GetApertureTimeInfo.side_effect = MockFunctionCallError("niDMM_GetApertureTimeInfo")
        mock_library.niDMM_GetApertureTimeInfo.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_GetAttributeViBoolean.side_effect = MockFunctionCallError("niDMM_GetAttributeViBoolean")
        mock_library.niDMM_GetAttributeViBoolean.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_GetAttributeViInt32.side_effect = MockFunctionCallError("niDMM_GetAttributeViInt32")
        mock_library.niDMM_GetAttributeViInt32.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_GetAttributeViReal64.side_effect = MockFunctionCallError("niDMM_GetAttributeViReal64")
        mock_library.niDMM_GetAttributeViReal64.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_GetAttributeViSession.side_effect = MockFunctionCallError("niDMM_GetAttributeViSession")
        mock_library.niDMM_GetAttributeViSession.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_GetAttributeViString.side_effect = MockFunctionCallError("niDMM_GetAttributeViString")
        mock_library.niDMM_GetAttributeViString.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_GetAutoRangeValue.side_effect = MockFunctionCallError("niDMM_GetAutoRangeValue")
        mock_library.niDMM_GetAutoRangeValue.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_GetCalCount.side_effect = MockFunctionCallError("niDMM_GetCalCount")
        mock_library.niDMM_GetCalCount.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_GetCalDateAndTime.side_effect = MockFunctionCallError("niDMM_GetCalDateAndTime")
        mock_library.niDMM_GetCalDateAndTime.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_GetChannelName.side_effect = MockFunctionCallError("niDMM_GetChannelName")
        mock_library.niDMM_GetChannelName.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_GetDevTemp.side_effect = MockFunctionCallError("niDMM_GetDevTemp")
        mock_library.niDMM_GetDevTemp.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_GetError.side_effect = MockFunctionCallError("niDMM_GetError")
        mock_library.niDMM_GetError.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_GetErrorMessage.side_effect = MockFunctionCallError("niDMM_GetErrorMessage")
        mock_library.niDMM_GetErrorMessage.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_GetLastCalTemp.side_effect = MockFunctionCallError("niDMM_GetLastCalTemp")
        mock_library.niDMM_GetLastCalTemp.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_GetMeasurementPeriod.side_effect = MockFunctionCallError("niDMM_GetMeasurementPeriod")
        mock_library.niDMM_GetMeasurementPeriod.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_GetNextCoercionRecord.side_effect = MockFunctionCallError("niDMM_GetNextCoercionRecord")
        mock_library.niDMM_GetNextCoercionRecord.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_GetNextInterchangeWarning.side_effect = MockFunctionCallError("niDMM_GetNextInterchangeWarning")
        mock_library.niDMM_GetNextInterchangeWarning.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_GetSelfCalSupported.side_effect = MockFunctionCallError("niDMM_GetSelfCalSupported")
        mock_library.niDMM_GetSelfCalSupported.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_InitWithOptions.side_effect = MockFunctionCallError("niDMM_InitWithOptions")
        mock_library.niDMM_InitWithOptions.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_Initiate.side_effect = MockFunctionCallError("niDMM_Initiate")
        mock_library.niDMM_Initiate.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_IsOverRange.side_effect = MockFunctionCallError("niDMM_IsOverRange")
        mock_library.niDMM_IsOverRange.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_IsUnderRange.side_effect = MockFunctionCallError("niDMM_IsUnderRange")
        mock_library.niDMM_IsUnderRange.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_LockSession.side_effect = MockFunctionCallError("niDMM_LockSession")
        mock_library.niDMM_LockSession.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_PerformOpenCableComp.side_effect = MockFunctionCallError("niDMM_PerformOpenCableComp")
        mock_library.niDMM_PerformOpenCableComp.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_PerformShortCableComp.side_effect = MockFunctionCallError("niDMM_PerformShortCableComp")
        mock_library.niDMM_PerformShortCableComp.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_Read.side_effect = MockFunctionCallError("niDMM_Read")
        mock_library.niDMM_Read.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_ReadMultiPoint.side_effect = MockFunctionCallError("niDMM_ReadMultiPoint")
        mock_library.niDMM_ReadMultiPoint.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_ReadStatus.side_effect = MockFunctionCallError("niDMM_ReadStatus")
        mock_library.niDMM_ReadStatus.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_ReadWaveform.side_effect = MockFunctionCallError("niDMM_ReadWaveform")
        mock_library.niDMM_ReadWaveform.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_ResetInterchangeCheck.side_effect = MockFunctionCallError("niDMM_ResetInterchangeCheck")
        mock_library.niDMM_ResetInterchangeCheck.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_ResetWithDefaults.side_effect = MockFunctionCallError("niDMM_ResetWithDefaults")
        mock_library.niDMM_ResetWithDefaults.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_SelfCal.side_effect = MockFunctionCallError("niDMM_SelfCal")
        mock_library.niDMM_SelfCal.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_SendSoftwareTrigger.side_effect = MockFunctionCallError("niDMM_SendSoftwareTrigger")
        mock_library.niDMM_SendSoftwareTrigger.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_SetAttributeViBoolean.side_effect = MockFunctionCallError("niDMM_SetAttributeViBoolean")
        mock_library.niDMM_SetAttributeViBoolean.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_SetAttributeViInt32.side_effect = MockFunctionCallError("niDMM_SetAttributeViInt32")
        mock_library.niDMM_SetAttributeViInt32.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_SetAttributeViReal64.side_effect = MockFunctionCallError("niDMM_SetAttributeViReal64")
        mock_library.niDMM_SetAttributeViReal64.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_SetAttributeViSession.side_effect = MockFunctionCallError("niDMM_SetAttributeViSession")
        mock_library.niDMM_SetAttributeViSession.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_SetAttributeViString.side_effect = MockFunctionCallError("niDMM_SetAttributeViString")
        mock_library.niDMM_SetAttributeViString.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_UnlockSession.side_effect = MockFunctionCallError("niDMM_UnlockSession")
        mock_library.niDMM_UnlockSession.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_close.side_effect = MockFunctionCallError("niDMM_close")
        mock_library.niDMM_close.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_error_query.side_effect = MockFunctionCallError("niDMM_error_query")
        mock_library.niDMM_error_query.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_reset.side_effect = MockFunctionCallError("niDMM_reset")
        mock_library.niDMM_reset.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_revision_query.side_effect = MockFunctionCallError("niDMM_revision_query")
        mock_library.niDMM_revision_query.return_value = nidmm.python_types.ViStatus(0)
        mock_library.niDMM_self_test.side_effect = MockFunctionCallError("niDMM_self_test")
        mock_library.niDMM_self_test.return_value = nidmm.python_types.ViStatus(0)
