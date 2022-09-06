# -*- coding: utf-8 -*-
# This file was generated
import sys  # noqa: F401   - Not all mock_helpers will need this


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
        self._defaults['ConfigureMeasurementAbsolute'] = {}
        self._defaults['ConfigureMeasurementAbsolute']['return'] = 0
        self._defaults['ConfigureMeasurementDigits'] = {}
        self._defaults['ConfigureMeasurementDigits']['return'] = 0
        self._defaults['ConfigureMultiPoint'] = {}
        self._defaults['ConfigureMultiPoint']['return'] = 0
        self._defaults['ConfigureRTDCustom'] = {}
        self._defaults['ConfigureRTDCustom']['return'] = 0
        self._defaults['ConfigureRTDType'] = {}
        self._defaults['ConfigureRTDType']['return'] = 0
        self._defaults['ConfigureThermistorCustom'] = {}
        self._defaults['ConfigureThermistorCustom']['return'] = 0
        self._defaults['ConfigureThermocouple'] = {}
        self._defaults['ConfigureThermocouple']['return'] = 0
        self._defaults['ConfigureTrigger'] = {}
        self._defaults['ConfigureTrigger']['return'] = 0
        self._defaults['ConfigureWaveformAcquisition'] = {}
        self._defaults['ConfigureWaveformAcquisition']['return'] = 0
        self._defaults['Disable'] = {}
        self._defaults['Disable']['return'] = 0
        self._defaults['ExportAttributeConfigurationBuffer'] = {}
        self._defaults['ExportAttributeConfigurationBuffer']['return'] = 0
        self._defaults['ExportAttributeConfigurationBuffer']['configuration'] = None
        self._defaults['ExportAttributeConfigurationFile'] = {}
        self._defaults['ExportAttributeConfigurationFile']['return'] = 0
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
        self._defaults['GetAttributeViBoolean'] = {}
        self._defaults['GetAttributeViBoolean']['return'] = 0
        self._defaults['GetAttributeViBoolean']['attributeValue'] = None
        self._defaults['GetAttributeViInt32'] = {}
        self._defaults['GetAttributeViInt32']['return'] = 0
        self._defaults['GetAttributeViInt32']['attributeValue'] = None
        self._defaults['GetAttributeViReal64'] = {}
        self._defaults['GetAttributeViReal64']['return'] = 0
        self._defaults['GetAttributeViReal64']['attributeValue'] = None
        self._defaults['GetAttributeViString'] = {}
        self._defaults['GetAttributeViString']['return'] = 0
        self._defaults['GetAttributeViString']['attributeValue'] = None
        self._defaults['GetCalDateAndTime'] = {}
        self._defaults['GetCalDateAndTime']['return'] = 0
        self._defaults['GetCalDateAndTime']['month'] = None
        self._defaults['GetCalDateAndTime']['day'] = None
        self._defaults['GetCalDateAndTime']['year'] = None
        self._defaults['GetCalDateAndTime']['hour'] = None
        self._defaults['GetCalDateAndTime']['minute'] = None
        self._defaults['GetDevTemp'] = {}
        self._defaults['GetDevTemp']['return'] = 0
        self._defaults['GetDevTemp']['temperature'] = None
        self._defaults['GetError'] = {}
        self._defaults['GetError']['return'] = 0
        self._defaults['GetError']['errorCode'] = None
        self._defaults['GetError']['description'] = None
        self._defaults['GetExtCalRecommendedInterval'] = {}
        self._defaults['GetExtCalRecommendedInterval']['return'] = 0
        self._defaults['GetExtCalRecommendedInterval']['months'] = None
        self._defaults['GetLastCalTemp'] = {}
        self._defaults['GetLastCalTemp']['return'] = 0
        self._defaults['GetLastCalTemp']['temperature'] = None
        self._defaults['GetSelfCalSupported'] = {}
        self._defaults['GetSelfCalSupported']['return'] = 0
        self._defaults['GetSelfCalSupported']['selfCalSupported'] = None
        self._defaults['ImportAttributeConfigurationBuffer'] = {}
        self._defaults['ImportAttributeConfigurationBuffer']['return'] = 0
        self._defaults['ImportAttributeConfigurationFile'] = {}
        self._defaults['ImportAttributeConfigurationFile']['return'] = 0
        self._defaults['InitWithOptions'] = {}
        self._defaults['InitWithOptions']['return'] = 0
        self._defaults['InitWithOptions']['vi'] = None
        self._defaults['Initiate'] = {}
        self._defaults['Initiate']['return'] = 0
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
        self._defaults['SetAttributeViString'] = {}
        self._defaults['SetAttributeViString']['return'] = 0
        self._defaults['UnlockSession'] = {}
        self._defaults['UnlockSession']['return'] = 0
        self._defaults['UnlockSession']['callerHasLock'] = None
        self._defaults['close'] = {}
        self._defaults['close']['return'] = 0
        self._defaults['error_message'] = {}
        self._defaults['error_message']['return'] = 0
        self._defaults['error_message']['errorMessage'] = None
        self._defaults['reset'] = {}
        self._defaults['reset']['return'] = 0
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

    def niDMM_ConfigureRTDCustom(self, vi, rtd_a, rtd_b, rtd_c):  # noqa: N802
        if self._defaults['ConfigureRTDCustom']['return'] != 0:
            return self._defaults['ConfigureRTDCustom']['return']
        return self._defaults['ConfigureRTDCustom']['return']

    def niDMM_ConfigureRTDType(self, vi, rtd_type, rtd_resistance):  # noqa: N802
        if self._defaults['ConfigureRTDType']['return'] != 0:
            return self._defaults['ConfigureRTDType']['return']
        return self._defaults['ConfigureRTDType']['return']

    def niDMM_ConfigureThermistorCustom(self, vi, thermistor_a, thermistor_b, thermistor_c):  # noqa: N802
        if self._defaults['ConfigureThermistorCustom']['return'] != 0:
            return self._defaults['ConfigureThermistorCustom']['return']
        return self._defaults['ConfigureThermistorCustom']['return']

    def niDMM_ConfigureThermocouple(self, vi, thermocouple_type, reference_junction_type):  # noqa: N802
        if self._defaults['ConfigureThermocouple']['return'] != 0:
            return self._defaults['ConfigureThermocouple']['return']
        return self._defaults['ConfigureThermocouple']['return']

    def niDMM_ConfigureTrigger(self, vi, trigger_source, trigger_delay):  # noqa: N802
        if self._defaults['ConfigureTrigger']['return'] != 0:
            return self._defaults['ConfigureTrigger']['return']
        return self._defaults['ConfigureTrigger']['return']

    def niDMM_ConfigureWaveformAcquisition(self, vi, measurement_function, range, rate, waveform_points):  # noqa: N802
        if self._defaults['ConfigureWaveformAcquisition']['return'] != 0:
            return self._defaults['ConfigureWaveformAcquisition']['return']
        return self._defaults['ConfigureWaveformAcquisition']['return']

    def niDMM_Disable(self, vi):  # noqa: N802
        if self._defaults['Disable']['return'] != 0:
            return self._defaults['Disable']['return']
        return self._defaults['Disable']['return']

    def niDMM_ExportAttributeConfigurationBuffer(self, vi, size, configuration):  # noqa: N802
        if self._defaults['ExportAttributeConfigurationBuffer']['return'] != 0:
            return self._defaults['ExportAttributeConfigurationBuffer']['return']
        if self._defaults['ExportAttributeConfigurationBuffer']['configuration'] is None:
            raise MockFunctionCallError("niDMM_ExportAttributeConfigurationBuffer", param='configuration')
        if size.value == 0:
            return len(self._defaults['ExportAttributeConfigurationBuffer']['configuration'])
        try:
            configuration_ref = configuration.contents
        except AttributeError:
            configuration_ref = configuration
        for i in range(len(self._defaults['ExportAttributeConfigurationBuffer']['configuration'])):
            configuration_ref[i] = self._defaults['ExportAttributeConfigurationBuffer']['configuration'][i]
        return self._defaults['ExportAttributeConfigurationBuffer']['return']

    def niDMM_ExportAttributeConfigurationFile(self, vi, file_path):  # noqa: N802
        if self._defaults['ExportAttributeConfigurationFile']['return'] != 0:
            return self._defaults['ExportAttributeConfigurationFile']['return']
        return self._defaults['ExportAttributeConfigurationFile']['return']

    def niDMM_Fetch(self, vi, maximum_time, reading):  # noqa: N802
        if self._defaults['Fetch']['return'] != 0:
            return self._defaults['Fetch']['return']
        # reading
        if self._defaults['Fetch']['reading'] is None:
            raise MockFunctionCallError("niDMM_Fetch", param='reading')
        if reading is not None:
            reading.contents.value = self._defaults['Fetch']['reading']
        return self._defaults['Fetch']['return']

    def niDMM_FetchMultiPoint(self, vi, maximum_time, array_size, reading_array, actual_number_of_points):  # noqa: N802
        if self._defaults['FetchMultiPoint']['return'] != 0:
            return self._defaults['FetchMultiPoint']['return']
        # reading_array
        if self._defaults['FetchMultiPoint']['readingArray'] is None:
            raise MockFunctionCallError("niDMM_FetchMultiPoint", param='readingArray')
        test_value = self._defaults['FetchMultiPoint']['readingArray']
        try:
            reading_array_ref = reading_array.contents
        except AttributeError:
            reading_array_ref = reading_array
        assert len(reading_array_ref) >= len(test_value)
        for i in range(len(test_value)):
            reading_array_ref[i] = test_value[i]
        # actual_number_of_points
        if self._defaults['FetchMultiPoint']['actualNumberOfPoints'] is None:
            raise MockFunctionCallError("niDMM_FetchMultiPoint", param='actualNumberOfPoints')
        if actual_number_of_points is not None:
            actual_number_of_points.contents.value = self._defaults['FetchMultiPoint']['actualNumberOfPoints']
        return self._defaults['FetchMultiPoint']['return']

    def niDMM_FetchWaveform(self, vi, maximum_time, array_size, waveform_array, actual_number_of_points):  # noqa: N802
        if self._defaults['FetchWaveform']['return'] != 0:
            return self._defaults['FetchWaveform']['return']
        # waveform_array
        if self._defaults['FetchWaveform']['waveformArray'] is None:
            raise MockFunctionCallError("niDMM_FetchWaveform", param='waveformArray')
        test_value = self._defaults['FetchWaveform']['waveformArray']
        try:
            waveform_array_ref = waveform_array.contents
        except AttributeError:
            waveform_array_ref = waveform_array
        assert len(waveform_array_ref) >= len(test_value)
        for i in range(len(test_value)):
            waveform_array_ref[i] = test_value[i]
        # actual_number_of_points
        if self._defaults['FetchWaveform']['actualNumberOfPoints'] is None:
            raise MockFunctionCallError("niDMM_FetchWaveform", param='actualNumberOfPoints')
        if actual_number_of_points is not None:
            actual_number_of_points.contents.value = self._defaults['FetchWaveform']['actualNumberOfPoints']
        return self._defaults['FetchWaveform']['return']

    def niDMM_GetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViBoolean']['return'] != 0:
            return self._defaults['GetAttributeViBoolean']['return']
        # attribute_value
        if self._defaults['GetAttributeViBoolean']['attributeValue'] is None:
            raise MockFunctionCallError("niDMM_GetAttributeViBoolean", param='attributeValue')
        if attribute_value is not None:
            attribute_value.contents.value = self._defaults['GetAttributeViBoolean']['attributeValue']
        return self._defaults['GetAttributeViBoolean']['return']

    def niDMM_GetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViInt32']['return'] != 0:
            return self._defaults['GetAttributeViInt32']['return']
        # attribute_value
        if self._defaults['GetAttributeViInt32']['attributeValue'] is None:
            raise MockFunctionCallError("niDMM_GetAttributeViInt32", param='attributeValue')
        if attribute_value is not None:
            attribute_value.contents.value = self._defaults['GetAttributeViInt32']['attributeValue']
        return self._defaults['GetAttributeViInt32']['return']

    def niDMM_GetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViReal64']['return'] != 0:
            return self._defaults['GetAttributeViReal64']['return']
        # attribute_value
        if self._defaults['GetAttributeViReal64']['attributeValue'] is None:
            raise MockFunctionCallError("niDMM_GetAttributeViReal64", param='attributeValue')
        if attribute_value is not None:
            attribute_value.contents.value = self._defaults['GetAttributeViReal64']['attributeValue']
        return self._defaults['GetAttributeViReal64']['return']

    def niDMM_GetAttributeViString(self, vi, channel_name, attribute_id, buffer_size, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViString']['return'] != 0:
            return self._defaults['GetAttributeViString']['return']
        if self._defaults['GetAttributeViString']['attributeValue'] is None:
            raise MockFunctionCallError("niDMM_GetAttributeViString", param='attributeValue')
        if buffer_size.value == 0:
            return len(self._defaults['GetAttributeViString']['attributeValue'])
        attribute_value.value = self._defaults['GetAttributeViString']['attributeValue'].encode('ascii')
        return self._defaults['GetAttributeViString']['return']

    def niDMM_GetCalDateAndTime(self, vi, cal_type, month, day, year, hour, minute):  # noqa: N802
        if self._defaults['GetCalDateAndTime']['return'] != 0:
            return self._defaults['GetCalDateAndTime']['return']
        # month
        if self._defaults['GetCalDateAndTime']['month'] is None:
            raise MockFunctionCallError("niDMM_GetCalDateAndTime", param='month')
        if month is not None:
            month.contents.value = self._defaults['GetCalDateAndTime']['month']
        # day
        if self._defaults['GetCalDateAndTime']['day'] is None:
            raise MockFunctionCallError("niDMM_GetCalDateAndTime", param='day')
        if day is not None:
            day.contents.value = self._defaults['GetCalDateAndTime']['day']
        # year
        if self._defaults['GetCalDateAndTime']['year'] is None:
            raise MockFunctionCallError("niDMM_GetCalDateAndTime", param='year')
        if year is not None:
            year.contents.value = self._defaults['GetCalDateAndTime']['year']
        # hour
        if self._defaults['GetCalDateAndTime']['hour'] is None:
            raise MockFunctionCallError("niDMM_GetCalDateAndTime", param='hour')
        if hour is not None:
            hour.contents.value = self._defaults['GetCalDateAndTime']['hour']
        # minute
        if self._defaults['GetCalDateAndTime']['minute'] is None:
            raise MockFunctionCallError("niDMM_GetCalDateAndTime", param='minute')
        if minute is not None:
            minute.contents.value = self._defaults['GetCalDateAndTime']['minute']
        return self._defaults['GetCalDateAndTime']['return']

    def niDMM_GetDevTemp(self, vi, options, temperature):  # noqa: N802
        if self._defaults['GetDevTemp']['return'] != 0:
            return self._defaults['GetDevTemp']['return']
        # temperature
        if self._defaults['GetDevTemp']['temperature'] is None:
            raise MockFunctionCallError("niDMM_GetDevTemp", param='temperature')
        if temperature is not None:
            temperature.contents.value = self._defaults['GetDevTemp']['temperature']
        return self._defaults['GetDevTemp']['return']

    def niDMM_GetError(self, vi, error_code, buffer_size, description):  # noqa: N802
        if self._defaults['GetError']['return'] != 0:
            return self._defaults['GetError']['return']
        # error_code
        if self._defaults['GetError']['errorCode'] is None:
            raise MockFunctionCallError("niDMM_GetError", param='errorCode')
        if error_code is not None:
            error_code.contents.value = self._defaults['GetError']['errorCode']
        if self._defaults['GetError']['description'] is None:
            raise MockFunctionCallError("niDMM_GetError", param='description')
        if buffer_size.value == 0:
            return len(self._defaults['GetError']['description'])
        description.value = self._defaults['GetError']['description'].encode('ascii')
        return self._defaults['GetError']['return']

    def niDMM_GetExtCalRecommendedInterval(self, vi, months):  # noqa: N802
        if self._defaults['GetExtCalRecommendedInterval']['return'] != 0:
            return self._defaults['GetExtCalRecommendedInterval']['return']
        # months
        if self._defaults['GetExtCalRecommendedInterval']['months'] is None:
            raise MockFunctionCallError("niDMM_GetExtCalRecommendedInterval", param='months')
        if months is not None:
            months.contents.value = self._defaults['GetExtCalRecommendedInterval']['months']
        return self._defaults['GetExtCalRecommendedInterval']['return']

    def niDMM_GetLastCalTemp(self, vi, cal_type, temperature):  # noqa: N802
        if self._defaults['GetLastCalTemp']['return'] != 0:
            return self._defaults['GetLastCalTemp']['return']
        # temperature
        if self._defaults['GetLastCalTemp']['temperature'] is None:
            raise MockFunctionCallError("niDMM_GetLastCalTemp", param='temperature')
        if temperature is not None:
            temperature.contents.value = self._defaults['GetLastCalTemp']['temperature']
        return self._defaults['GetLastCalTemp']['return']

    def niDMM_GetSelfCalSupported(self, vi, self_cal_supported):  # noqa: N802
        if self._defaults['GetSelfCalSupported']['return'] != 0:
            return self._defaults['GetSelfCalSupported']['return']
        # self_cal_supported
        if self._defaults['GetSelfCalSupported']['selfCalSupported'] is None:
            raise MockFunctionCallError("niDMM_GetSelfCalSupported", param='selfCalSupported')
        if self_cal_supported is not None:
            self_cal_supported.contents.value = self._defaults['GetSelfCalSupported']['selfCalSupported']
        return self._defaults['GetSelfCalSupported']['return']

    def niDMM_ImportAttributeConfigurationBuffer(self, vi, size, configuration):  # noqa: N802
        if self._defaults['ImportAttributeConfigurationBuffer']['return'] != 0:
            return self._defaults['ImportAttributeConfigurationBuffer']['return']
        return self._defaults['ImportAttributeConfigurationBuffer']['return']

    def niDMM_ImportAttributeConfigurationFile(self, vi, file_path):  # noqa: N802
        if self._defaults['ImportAttributeConfigurationFile']['return'] != 0:
            return self._defaults['ImportAttributeConfigurationFile']['return']
        return self._defaults['ImportAttributeConfigurationFile']['return']

    def niDMM_InitWithOptions(self, resource_name, id_query, reset_device, option_string, vi):  # noqa: N802
        if self._defaults['InitWithOptions']['return'] != 0:
            return self._defaults['InitWithOptions']['return']
        # vi
        if self._defaults['InitWithOptions']['vi'] is None:
            raise MockFunctionCallError("niDMM_InitWithOptions", param='vi')
        if vi is not None:
            vi.contents.value = self._defaults['InitWithOptions']['vi']
        return self._defaults['InitWithOptions']['return']

    def niDMM_Initiate(self, vi):  # noqa: N802
        if self._defaults['Initiate']['return'] != 0:
            return self._defaults['Initiate']['return']
        return self._defaults['Initiate']['return']

    def niDMM_LockSession(self, vi, caller_has_lock):  # noqa: N802
        if self._defaults['LockSession']['return'] != 0:
            return self._defaults['LockSession']['return']
        # caller_has_lock
        if self._defaults['LockSession']['callerHasLock'] is None:
            raise MockFunctionCallError("niDMM_LockSession", param='callerHasLock')
        if caller_has_lock is not None:
            caller_has_lock.contents.value = self._defaults['LockSession']['callerHasLock']
        return self._defaults['LockSession']['return']

    def niDMM_PerformOpenCableComp(self, vi, conductance, susceptance):  # noqa: N802
        if self._defaults['PerformOpenCableComp']['return'] != 0:
            return self._defaults['PerformOpenCableComp']['return']
        # conductance
        if self._defaults['PerformOpenCableComp']['conductance'] is None:
            raise MockFunctionCallError("niDMM_PerformOpenCableComp", param='conductance')
        if conductance is not None:
            conductance.contents.value = self._defaults['PerformOpenCableComp']['conductance']
        # susceptance
        if self._defaults['PerformOpenCableComp']['susceptance'] is None:
            raise MockFunctionCallError("niDMM_PerformOpenCableComp", param='susceptance')
        if susceptance is not None:
            susceptance.contents.value = self._defaults['PerformOpenCableComp']['susceptance']
        return self._defaults['PerformOpenCableComp']['return']

    def niDMM_PerformShortCableComp(self, vi, resistance, reactance):  # noqa: N802
        if self._defaults['PerformShortCableComp']['return'] != 0:
            return self._defaults['PerformShortCableComp']['return']
        # resistance
        if self._defaults['PerformShortCableComp']['resistance'] is None:
            raise MockFunctionCallError("niDMM_PerformShortCableComp", param='resistance')
        if resistance is not None:
            resistance.contents.value = self._defaults['PerformShortCableComp']['resistance']
        # reactance
        if self._defaults['PerformShortCableComp']['reactance'] is None:
            raise MockFunctionCallError("niDMM_PerformShortCableComp", param='reactance')
        if reactance is not None:
            reactance.contents.value = self._defaults['PerformShortCableComp']['reactance']
        return self._defaults['PerformShortCableComp']['return']

    def niDMM_Read(self, vi, maximum_time, reading):  # noqa: N802
        if self._defaults['Read']['return'] != 0:
            return self._defaults['Read']['return']
        # reading
        if self._defaults['Read']['reading'] is None:
            raise MockFunctionCallError("niDMM_Read", param='reading')
        if reading is not None:
            reading.contents.value = self._defaults['Read']['reading']
        return self._defaults['Read']['return']

    def niDMM_ReadMultiPoint(self, vi, maximum_time, array_size, reading_array, actual_number_of_points):  # noqa: N802
        if self._defaults['ReadMultiPoint']['return'] != 0:
            return self._defaults['ReadMultiPoint']['return']
        # reading_array
        if self._defaults['ReadMultiPoint']['readingArray'] is None:
            raise MockFunctionCallError("niDMM_ReadMultiPoint", param='readingArray')
        test_value = self._defaults['ReadMultiPoint']['readingArray']
        try:
            reading_array_ref = reading_array.contents
        except AttributeError:
            reading_array_ref = reading_array
        assert len(reading_array_ref) >= len(test_value)
        for i in range(len(test_value)):
            reading_array_ref[i] = test_value[i]
        # actual_number_of_points
        if self._defaults['ReadMultiPoint']['actualNumberOfPoints'] is None:
            raise MockFunctionCallError("niDMM_ReadMultiPoint", param='actualNumberOfPoints')
        if actual_number_of_points is not None:
            actual_number_of_points.contents.value = self._defaults['ReadMultiPoint']['actualNumberOfPoints']
        return self._defaults['ReadMultiPoint']['return']

    def niDMM_ReadStatus(self, vi, acquisition_backlog, acquisition_status):  # noqa: N802
        if self._defaults['ReadStatus']['return'] != 0:
            return self._defaults['ReadStatus']['return']
        # acquisition_backlog
        if self._defaults['ReadStatus']['acquisitionBacklog'] is None:
            raise MockFunctionCallError("niDMM_ReadStatus", param='acquisitionBacklog')
        if acquisition_backlog is not None:
            acquisition_backlog.contents.value = self._defaults['ReadStatus']['acquisitionBacklog']
        # acquisition_status
        if self._defaults['ReadStatus']['acquisitionStatus'] is None:
            raise MockFunctionCallError("niDMM_ReadStatus", param='acquisitionStatus')
        if acquisition_status is not None:
            acquisition_status.contents.value = self._defaults['ReadStatus']['acquisitionStatus']
        return self._defaults['ReadStatus']['return']

    def niDMM_ReadWaveform(self, vi, maximum_time, array_size, waveform_array, actual_number_of_points):  # noqa: N802
        if self._defaults['ReadWaveform']['return'] != 0:
            return self._defaults['ReadWaveform']['return']
        # waveform_array
        if self._defaults['ReadWaveform']['waveformArray'] is None:
            raise MockFunctionCallError("niDMM_ReadWaveform", param='waveformArray')
        test_value = self._defaults['ReadWaveform']['waveformArray']
        try:
            waveform_array_ref = waveform_array.contents
        except AttributeError:
            waveform_array_ref = waveform_array
        assert len(waveform_array_ref) >= len(test_value)
        for i in range(len(test_value)):
            waveform_array_ref[i] = test_value[i]
        # actual_number_of_points
        if self._defaults['ReadWaveform']['actualNumberOfPoints'] is None:
            raise MockFunctionCallError("niDMM_ReadWaveform", param='actualNumberOfPoints')
        if actual_number_of_points is not None:
            actual_number_of_points.contents.value = self._defaults['ReadWaveform']['actualNumberOfPoints']
        return self._defaults['ReadWaveform']['return']

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

    def niDMM_SetAttributeViString(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViString']['return'] != 0:
            return self._defaults['SetAttributeViString']['return']
        return self._defaults['SetAttributeViString']['return']

    def niDMM_UnlockSession(self, vi, caller_has_lock):  # noqa: N802
        if self._defaults['UnlockSession']['return'] != 0:
            return self._defaults['UnlockSession']['return']
        # caller_has_lock
        if self._defaults['UnlockSession']['callerHasLock'] is None:
            raise MockFunctionCallError("niDMM_UnlockSession", param='callerHasLock')
        if caller_has_lock is not None:
            caller_has_lock.contents.value = self._defaults['UnlockSession']['callerHasLock']
        return self._defaults['UnlockSession']['return']

    def niDMM_close(self, vi):  # noqa: N802
        if self._defaults['close']['return'] != 0:
            return self._defaults['close']['return']
        return self._defaults['close']['return']

    def niDMM_error_message(self, vi, error_code, error_message):  # noqa: N802
        if self._defaults['error_message']['return'] != 0:
            return self._defaults['error_message']['return']
        # error_message
        if self._defaults['error_message']['errorMessage'] is None:
            raise MockFunctionCallError("niDMM_error_message", param='errorMessage')
        test_value = self._defaults['error_message']['errorMessage']
        if type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(error_message) >= len(test_value)
        for i in range(len(test_value)):
            error_message[i] = test_value[i]
        return self._defaults['error_message']['return']

    def niDMM_reset(self, vi):  # noqa: N802
        if self._defaults['reset']['return'] != 0:
            return self._defaults['reset']['return']
        return self._defaults['reset']['return']

    def niDMM_self_test(self, vi, self_test_result, self_test_message):  # noqa: N802
        if self._defaults['self_test']['return'] != 0:
            return self._defaults['self_test']['return']
        # self_test_result
        if self._defaults['self_test']['selfTestResult'] is None:
            raise MockFunctionCallError("niDMM_self_test", param='selfTestResult')
        if self_test_result is not None:
            self_test_result.contents.value = self._defaults['self_test']['selfTestResult']
        # self_test_message
        if self._defaults['self_test']['selfTestMessage'] is None:
            raise MockFunctionCallError("niDMM_self_test", param='selfTestMessage')
        test_value = self._defaults['self_test']['selfTestMessage']
        if type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(self_test_message) >= len(test_value)
        for i in range(len(test_value)):
            self_test_message[i] = test_value[i]
        return self._defaults['self_test']['return']

    # Helper function to setup Mock object with default side effects and return values
    def set_side_effects_and_return_values(self, mock_library):
        mock_library.niDMM_Abort_cfunc.side_effect = MockFunctionCallError("niDMM_Abort_cfunc")
        mock_library.niDMM_Abort_cfunc.return_value = 0
        mock_library.niDMM_ConfigureMeasurementAbsolute_cfunc.side_effect = MockFunctionCallError("niDMM_ConfigureMeasurementAbsolute_cfunc")
        mock_library.niDMM_ConfigureMeasurementAbsolute_cfunc.return_value = 0
        mock_library.niDMM_ConfigureMeasurementDigits_cfunc.side_effect = MockFunctionCallError("niDMM_ConfigureMeasurementDigits_cfunc")
        mock_library.niDMM_ConfigureMeasurementDigits_cfunc.return_value = 0
        mock_library.niDMM_ConfigureMultiPoint_cfunc.side_effect = MockFunctionCallError("niDMM_ConfigureMultiPoint_cfunc")
        mock_library.niDMM_ConfigureMultiPoint_cfunc.return_value = 0
        mock_library.niDMM_ConfigureRTDCustom_cfunc.side_effect = MockFunctionCallError("niDMM_ConfigureRTDCustom_cfunc")
        mock_library.niDMM_ConfigureRTDCustom_cfunc.return_value = 0
        mock_library.niDMM_ConfigureRTDType_cfunc.side_effect = MockFunctionCallError("niDMM_ConfigureRTDType_cfunc")
        mock_library.niDMM_ConfigureRTDType_cfunc.return_value = 0
        mock_library.niDMM_ConfigureThermistorCustom_cfunc.side_effect = MockFunctionCallError("niDMM_ConfigureThermistorCustom_cfunc")
        mock_library.niDMM_ConfigureThermistorCustom_cfunc.return_value = 0
        mock_library.niDMM_ConfigureThermocouple_cfunc.side_effect = MockFunctionCallError("niDMM_ConfigureThermocouple_cfunc")
        mock_library.niDMM_ConfigureThermocouple_cfunc.return_value = 0
        mock_library.niDMM_ConfigureTrigger_cfunc.side_effect = MockFunctionCallError("niDMM_ConfigureTrigger_cfunc")
        mock_library.niDMM_ConfigureTrigger_cfunc.return_value = 0
        mock_library.niDMM_ConfigureWaveformAcquisition_cfunc.side_effect = MockFunctionCallError("niDMM_ConfigureWaveformAcquisition_cfunc")
        mock_library.niDMM_ConfigureWaveformAcquisition_cfunc.return_value = 0
        mock_library.niDMM_Disable_cfunc.side_effect = MockFunctionCallError("niDMM_Disable_cfunc")
        mock_library.niDMM_Disable_cfunc.return_value = 0
        mock_library.niDMM_ExportAttributeConfigurationBuffer_cfunc.side_effect = MockFunctionCallError("niDMM_ExportAttributeConfigurationBuffer_cfunc")
        mock_library.niDMM_ExportAttributeConfigurationBuffer_cfunc.return_value = 0
        mock_library.niDMM_ExportAttributeConfigurationFile_cfunc.side_effect = MockFunctionCallError("niDMM_ExportAttributeConfigurationFile_cfunc")
        mock_library.niDMM_ExportAttributeConfigurationFile_cfunc.return_value = 0
        mock_library.niDMM_Fetch_cfunc.side_effect = MockFunctionCallError("niDMM_Fetch_cfunc")
        mock_library.niDMM_Fetch_cfunc.return_value = 0
        mock_library.niDMM_FetchMultiPoint_cfunc.side_effect = MockFunctionCallError("niDMM_FetchMultiPoint_cfunc")
        mock_library.niDMM_FetchMultiPoint_cfunc.return_value = 0
        mock_library.niDMM_FetchWaveform_cfunc.side_effect = MockFunctionCallError("niDMM_FetchWaveform_cfunc")
        mock_library.niDMM_FetchWaveform_cfunc.return_value = 0
        mock_library.niDMM_GetAttributeViBoolean_cfunc.side_effect = MockFunctionCallError("niDMM_GetAttributeViBoolean_cfunc")
        mock_library.niDMM_GetAttributeViBoolean_cfunc.return_value = 0
        mock_library.niDMM_GetAttributeViInt32_cfunc.side_effect = MockFunctionCallError("niDMM_GetAttributeViInt32_cfunc")
        mock_library.niDMM_GetAttributeViInt32_cfunc.return_value = 0
        mock_library.niDMM_GetAttributeViReal64_cfunc.side_effect = MockFunctionCallError("niDMM_GetAttributeViReal64_cfunc")
        mock_library.niDMM_GetAttributeViReal64_cfunc.return_value = 0
        mock_library.niDMM_GetAttributeViString_cfunc.side_effect = MockFunctionCallError("niDMM_GetAttributeViString_cfunc")
        mock_library.niDMM_GetAttributeViString_cfunc.return_value = 0
        mock_library.niDMM_GetCalDateAndTime_cfunc.side_effect = MockFunctionCallError("niDMM_GetCalDateAndTime_cfunc")
        mock_library.niDMM_GetCalDateAndTime_cfunc.return_value = 0
        mock_library.niDMM_GetDevTemp_cfunc.side_effect = MockFunctionCallError("niDMM_GetDevTemp_cfunc")
        mock_library.niDMM_GetDevTemp_cfunc.return_value = 0
        mock_library.niDMM_GetError_cfunc.side_effect = MockFunctionCallError("niDMM_GetError_cfunc")
        mock_library.niDMM_GetError_cfunc.return_value = 0
        mock_library.niDMM_GetExtCalRecommendedInterval_cfunc.side_effect = MockFunctionCallError("niDMM_GetExtCalRecommendedInterval_cfunc")
        mock_library.niDMM_GetExtCalRecommendedInterval_cfunc.return_value = 0
        mock_library.niDMM_GetLastCalTemp_cfunc.side_effect = MockFunctionCallError("niDMM_GetLastCalTemp_cfunc")
        mock_library.niDMM_GetLastCalTemp_cfunc.return_value = 0
        mock_library.niDMM_GetSelfCalSupported_cfunc.side_effect = MockFunctionCallError("niDMM_GetSelfCalSupported_cfunc")
        mock_library.niDMM_GetSelfCalSupported_cfunc.return_value = 0
        mock_library.niDMM_ImportAttributeConfigurationBuffer_cfunc.side_effect = MockFunctionCallError("niDMM_ImportAttributeConfigurationBuffer_cfunc")
        mock_library.niDMM_ImportAttributeConfigurationBuffer_cfunc.return_value = 0
        mock_library.niDMM_ImportAttributeConfigurationFile_cfunc.side_effect = MockFunctionCallError("niDMM_ImportAttributeConfigurationFile_cfunc")
        mock_library.niDMM_ImportAttributeConfigurationFile_cfunc.return_value = 0
        mock_library.niDMM_InitWithOptions_cfunc.side_effect = MockFunctionCallError("niDMM_InitWithOptions_cfunc")
        mock_library.niDMM_InitWithOptions_cfunc.return_value = 0
        mock_library.niDMM_Initiate_cfunc.side_effect = MockFunctionCallError("niDMM_Initiate_cfunc")
        mock_library.niDMM_Initiate_cfunc.return_value = 0
        mock_library.niDMM_LockSession_cfunc.side_effect = MockFunctionCallError("niDMM_LockSession_cfunc")
        mock_library.niDMM_LockSession_cfunc.return_value = 0
        mock_library.niDMM_PerformOpenCableComp_cfunc.side_effect = MockFunctionCallError("niDMM_PerformOpenCableComp_cfunc")
        mock_library.niDMM_PerformOpenCableComp_cfunc.return_value = 0
        mock_library.niDMM_PerformShortCableComp_cfunc.side_effect = MockFunctionCallError("niDMM_PerformShortCableComp_cfunc")
        mock_library.niDMM_PerformShortCableComp_cfunc.return_value = 0
        mock_library.niDMM_Read_cfunc.side_effect = MockFunctionCallError("niDMM_Read_cfunc")
        mock_library.niDMM_Read_cfunc.return_value = 0
        mock_library.niDMM_ReadMultiPoint_cfunc.side_effect = MockFunctionCallError("niDMM_ReadMultiPoint_cfunc")
        mock_library.niDMM_ReadMultiPoint_cfunc.return_value = 0
        mock_library.niDMM_ReadStatus_cfunc.side_effect = MockFunctionCallError("niDMM_ReadStatus_cfunc")
        mock_library.niDMM_ReadStatus_cfunc.return_value = 0
        mock_library.niDMM_ReadWaveform_cfunc.side_effect = MockFunctionCallError("niDMM_ReadWaveform_cfunc")
        mock_library.niDMM_ReadWaveform_cfunc.return_value = 0
        mock_library.niDMM_ResetWithDefaults_cfunc.side_effect = MockFunctionCallError("niDMM_ResetWithDefaults_cfunc")
        mock_library.niDMM_ResetWithDefaults_cfunc.return_value = 0
        mock_library.niDMM_SelfCal_cfunc.side_effect = MockFunctionCallError("niDMM_SelfCal_cfunc")
        mock_library.niDMM_SelfCal_cfunc.return_value = 0
        mock_library.niDMM_SendSoftwareTrigger_cfunc.side_effect = MockFunctionCallError("niDMM_SendSoftwareTrigger_cfunc")
        mock_library.niDMM_SendSoftwareTrigger_cfunc.return_value = 0
        mock_library.niDMM_SetAttributeViBoolean_cfunc.side_effect = MockFunctionCallError("niDMM_SetAttributeViBoolean_cfunc")
        mock_library.niDMM_SetAttributeViBoolean_cfunc.return_value = 0
        mock_library.niDMM_SetAttributeViInt32_cfunc.side_effect = MockFunctionCallError("niDMM_SetAttributeViInt32_cfunc")
        mock_library.niDMM_SetAttributeViInt32_cfunc.return_value = 0
        mock_library.niDMM_SetAttributeViReal64_cfunc.side_effect = MockFunctionCallError("niDMM_SetAttributeViReal64_cfunc")
        mock_library.niDMM_SetAttributeViReal64_cfunc.return_value = 0
        mock_library.niDMM_SetAttributeViString_cfunc.side_effect = MockFunctionCallError("niDMM_SetAttributeViString_cfunc")
        mock_library.niDMM_SetAttributeViString_cfunc.return_value = 0
        mock_library.niDMM_UnlockSession_cfunc.side_effect = MockFunctionCallError("niDMM_UnlockSession_cfunc")
        mock_library.niDMM_UnlockSession_cfunc.return_value = 0
        mock_library.niDMM_close_cfunc.side_effect = MockFunctionCallError("niDMM_close_cfunc")
        mock_library.niDMM_close_cfunc.return_value = 0
        mock_library.niDMM_error_message_cfunc.side_effect = MockFunctionCallError("niDMM_error_message_cfunc")
        mock_library.niDMM_error_message_cfunc.return_value = 0
        mock_library.niDMM_reset_cfunc.side_effect = MockFunctionCallError("niDMM_reset_cfunc")
        mock_library.niDMM_reset_cfunc.return_value = 0
        mock_library.niDMM_self_test_cfunc.side_effect = MockFunctionCallError("niDMM_self_test_cfunc")
        mock_library.niDMM_self_test_cfunc.return_value = 0
