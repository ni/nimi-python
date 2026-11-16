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
        self._defaults['AcquisitionStatus'] = {}
        self._defaults['AcquisitionStatus']['return'] = 0
        self._defaults['AcquisitionStatus']['acquisitionStatus'] = None
        self._defaults['ActualMeasWfmSize'] = {}
        self._defaults['ActualMeasWfmSize']['return'] = 0
        self._defaults['ActualMeasWfmSize']['measWaveformSize'] = None
        self._defaults['ActualNumWfms'] = {}
        self._defaults['ActualNumWfms']['return'] = 0
        self._defaults['ActualNumWfms']['numWfms'] = None
        self._defaults['AddWaveformProcessing'] = {}
        self._defaults['AddWaveformProcessing']['return'] = 0
        self._defaults['AutoSetup'] = {}
        self._defaults['AutoSetup']['return'] = 0
        self._defaults['CalFetchDate'] = {}
        self._defaults['CalFetchDate']['return'] = 0
        self._defaults['CalFetchDate']['year'] = None
        self._defaults['CalFetchDate']['month'] = None
        self._defaults['CalFetchDate']['day'] = None
        self._defaults['CalFetchTemperature'] = {}
        self._defaults['CalFetchTemperature']['return'] = 0
        self._defaults['CalFetchTemperature']['temperature'] = None
        self._defaults['CalSelfCalibrate'] = {}
        self._defaults['CalSelfCalibrate']['return'] = 0
        self._defaults['ClearWaveformMeasurementStats'] = {}
        self._defaults['ClearWaveformMeasurementStats']['return'] = 0
        self._defaults['ClearWaveformProcessing'] = {}
        self._defaults['ClearWaveformProcessing']['return'] = 0
        self._defaults['Commit'] = {}
        self._defaults['Commit']['return'] = 0
        self._defaults['ConfigureChanCharacteristics'] = {}
        self._defaults['ConfigureChanCharacteristics']['return'] = 0
        self._defaults['ConfigureEqualizationFilterCoefficients'] = {}
        self._defaults['ConfigureEqualizationFilterCoefficients']['return'] = 0
        self._defaults['ConfigureHorizontalTiming'] = {}
        self._defaults['ConfigureHorizontalTiming']['return'] = 0
        self._defaults['ConfigureRefLevels'] = {}
        self._defaults['ConfigureRefLevels']['return'] = 0
        self._defaults['ConfigureTriggerDigital'] = {}
        self._defaults['ConfigureTriggerDigital']['return'] = 0
        self._defaults['ConfigureTriggerEdge'] = {}
        self._defaults['ConfigureTriggerEdge']['return'] = 0
        self._defaults['ConfigureTriggerHysteresis'] = {}
        self._defaults['ConfigureTriggerHysteresis']['return'] = 0
        self._defaults['ConfigureTriggerImmediate'] = {}
        self._defaults['ConfigureTriggerImmediate']['return'] = 0
        self._defaults['ConfigureTriggerSoftware'] = {}
        self._defaults['ConfigureTriggerSoftware']['return'] = 0
        self._defaults['ConfigureTriggerVideo'] = {}
        self._defaults['ConfigureTriggerVideo']['return'] = 0
        self._defaults['ConfigureTriggerWindow'] = {}
        self._defaults['ConfigureTriggerWindow']['return'] = 0
        self._defaults['ConfigureVertical'] = {}
        self._defaults['ConfigureVertical']['return'] = 0
        self._defaults['Disable'] = {}
        self._defaults['Disable']['return'] = 0
        self._defaults['ExportAttributeConfigurationBuffer'] = {}
        self._defaults['ExportAttributeConfigurationBuffer']['return'] = 0
        self._defaults['ExportAttributeConfigurationBuffer']['configuration'] = None
        self._defaults['ExportAttributeConfigurationFile'] = {}
        self._defaults['ExportAttributeConfigurationFile']['return'] = 0
        self._defaults['Fetch'] = {}
        self._defaults['Fetch']['return'] = 0
        self._defaults['Fetch']['waveform'] = None
        self._defaults['Fetch']['wfmInfo'] = None
        self._defaults['FetchArrayMeasurement'] = {}
        self._defaults['FetchArrayMeasurement']['return'] = 0
        self._defaults['FetchArrayMeasurement']['measWfm'] = None
        self._defaults['FetchArrayMeasurement']['wfmInfo'] = None
        self._defaults['FetchBinary16'] = {}
        self._defaults['FetchBinary16']['return'] = 0
        self._defaults['FetchBinary16']['waveform'] = None
        self._defaults['FetchBinary16']['wfmInfo'] = None
        self._defaults['FetchBinary32'] = {}
        self._defaults['FetchBinary32']['return'] = 0
        self._defaults['FetchBinary32']['waveform'] = None
        self._defaults['FetchBinary32']['wfmInfo'] = None
        self._defaults['FetchBinary8'] = {}
        self._defaults['FetchBinary8']['return'] = 0
        self._defaults['FetchBinary8']['waveform'] = None
        self._defaults['FetchBinary8']['wfmInfo'] = None
        self._defaults['FetchMeasurementStats'] = {}
        self._defaults['FetchMeasurementStats']['return'] = 0
        self._defaults['FetchMeasurementStats']['result'] = None
        self._defaults['FetchMeasurementStats']['mean'] = None
        self._defaults['FetchMeasurementStats']['stdev'] = None
        self._defaults['FetchMeasurementStats']['min'] = None
        self._defaults['FetchMeasurementStats']['max'] = None
        self._defaults['FetchMeasurementStats']['numInStats'] = None
        self._defaults['GetAttributeViBoolean'] = {}
        self._defaults['GetAttributeViBoolean']['return'] = 0
        self._defaults['GetAttributeViBoolean']['value'] = None
        self._defaults['GetAttributeViInt32'] = {}
        self._defaults['GetAttributeViInt32']['return'] = 0
        self._defaults['GetAttributeViInt32']['value'] = None
        self._defaults['GetAttributeViInt64'] = {}
        self._defaults['GetAttributeViInt64']['return'] = 0
        self._defaults['GetAttributeViInt64']['value'] = None
        self._defaults['GetAttributeViReal64'] = {}
        self._defaults['GetAttributeViReal64']['return'] = 0
        self._defaults['GetAttributeViReal64']['value'] = None
        self._defaults['GetAttributeViString'] = {}
        self._defaults['GetAttributeViString']['return'] = 0
        self._defaults['GetAttributeViString']['value'] = None
        self._defaults['GetChannelNameFromString'] = {}
        self._defaults['GetChannelNameFromString']['return'] = 0
        self._defaults['GetChannelNameFromString']['name'] = None
        self._defaults['GetEqualizationFilterCoefficients'] = {}
        self._defaults['GetEqualizationFilterCoefficients']['return'] = 0
        self._defaults['GetEqualizationFilterCoefficients']['coefficients'] = None
        self._defaults['GetError'] = {}
        self._defaults['GetError']['return'] = 0
        self._defaults['GetError']['errorCode'] = None
        self._defaults['GetError']['description'] = None
        self._defaults['ImportAttributeConfigurationBuffer'] = {}
        self._defaults['ImportAttributeConfigurationBuffer']['return'] = 0
        self._defaults['ImportAttributeConfigurationFile'] = {}
        self._defaults['ImportAttributeConfigurationFile']['return'] = 0
        self._defaults['InitWithOptions'] = {}
        self._defaults['InitWithOptions']['return'] = 0
        self._defaults['InitWithOptions']['vi'] = None
        self._defaults['InitiateAcquisition'] = {}
        self._defaults['InitiateAcquisition']['return'] = 0
        self._defaults['LockSession'] = {}
        self._defaults['LockSession']['return'] = 0
        self._defaults['LockSession']['callerHasLock'] = None
        self._defaults['ProbeCompensationSignalStart'] = {}
        self._defaults['ProbeCompensationSignalStart']['return'] = 0
        self._defaults['ProbeCompensationSignalStop'] = {}
        self._defaults['ProbeCompensationSignalStop']['return'] = 0
        self._defaults['Read'] = {}
        self._defaults['Read']['return'] = 0
        self._defaults['Read']['waveform'] = None
        self._defaults['Read']['wfmInfo'] = None
        self._defaults['ResetDevice'] = {}
        self._defaults['ResetDevice']['return'] = 0
        self._defaults['ResetWithDefaults'] = {}
        self._defaults['ResetWithDefaults']['return'] = 0
        self._defaults['SendSoftwareTriggerEdge'] = {}
        self._defaults['SendSoftwareTriggerEdge']['return'] = 0
        self._defaults['SetAttributeViBoolean'] = {}
        self._defaults['SetAttributeViBoolean']['return'] = 0
        self._defaults['SetAttributeViInt32'] = {}
        self._defaults['SetAttributeViInt32']['return'] = 0
        self._defaults['SetAttributeViInt64'] = {}
        self._defaults['SetAttributeViInt64']['return'] = 0
        self._defaults['SetAttributeViReal64'] = {}
        self._defaults['SetAttributeViReal64']['return'] = 0
        self._defaults['SetAttributeViString'] = {}
        self._defaults['SetAttributeViString']['return'] = 0
        self._defaults['SetRuntimeEnvironment'] = {}
        self._defaults['SetRuntimeEnvironment']['return'] = 0
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

    def niScope_Abort(self, vi):  # noqa: N802
        if self._defaults['Abort']['return'] != 0:
            return self._defaults['Abort']['return']
        return self._defaults['Abort']['return']

    def niScope_AcquisitionStatus(self, vi, acquisition_status):  # noqa: N802
        if self._defaults['AcquisitionStatus']['return'] != 0:
            return self._defaults['AcquisitionStatus']['return']
        # acquisition_status
        if self._defaults['AcquisitionStatus']['acquisitionStatus'] is None:
            raise MockFunctionCallError("niScope_AcquisitionStatus", param='acquisitionStatus')
        if acquisition_status is not None:
            acquisition_status.contents.value = self._defaults['AcquisitionStatus']['acquisitionStatus']
        return self._defaults['AcquisitionStatus']['return']

    def niScope_ActualMeasWfmSize(self, vi, array_meas_function, meas_waveform_size):  # noqa: N802
        if self._defaults['ActualMeasWfmSize']['return'] != 0:
            return self._defaults['ActualMeasWfmSize']['return']
        # meas_waveform_size
        if self._defaults['ActualMeasWfmSize']['measWaveformSize'] is None:
            raise MockFunctionCallError("niScope_ActualMeasWfmSize", param='measWaveformSize')
        if meas_waveform_size is not None:
            meas_waveform_size.contents.value = self._defaults['ActualMeasWfmSize']['measWaveformSize']
        return self._defaults['ActualMeasWfmSize']['return']

    def niScope_ActualNumWfms(self, vi, channel_list, num_wfms):  # noqa: N802
        if self._defaults['ActualNumWfms']['return'] != 0:
            return self._defaults['ActualNumWfms']['return']
        # num_wfms
        if self._defaults['ActualNumWfms']['numWfms'] is None:
            raise MockFunctionCallError("niScope_ActualNumWfms", param='numWfms')
        if num_wfms is not None:
            num_wfms.contents.value = self._defaults['ActualNumWfms']['numWfms']
        return self._defaults['ActualNumWfms']['return']

    def niScope_AddWaveformProcessing(self, vi, channel_list, meas_function):  # noqa: N802
        if self._defaults['AddWaveformProcessing']['return'] != 0:
            return self._defaults['AddWaveformProcessing']['return']
        return self._defaults['AddWaveformProcessing']['return']

    def niScope_AutoSetup(self, vi):  # noqa: N802
        if self._defaults['AutoSetup']['return'] != 0:
            return self._defaults['AutoSetup']['return']
        return self._defaults['AutoSetup']['return']

    def niScope_CalFetchDate(self, vi, which_one, year, month, day):  # noqa: N802
        if self._defaults['CalFetchDate']['return'] != 0:
            return self._defaults['CalFetchDate']['return']
        # year
        if self._defaults['CalFetchDate']['year'] is None:
            raise MockFunctionCallError("niScope_CalFetchDate", param='year')
        if year is not None:
            year.contents.value = self._defaults['CalFetchDate']['year']
        # month
        if self._defaults['CalFetchDate']['month'] is None:
            raise MockFunctionCallError("niScope_CalFetchDate", param='month')
        if month is not None:
            month.contents.value = self._defaults['CalFetchDate']['month']
        # day
        if self._defaults['CalFetchDate']['day'] is None:
            raise MockFunctionCallError("niScope_CalFetchDate", param='day')
        if day is not None:
            day.contents.value = self._defaults['CalFetchDate']['day']
        return self._defaults['CalFetchDate']['return']

    def niScope_CalFetchTemperature(self, vi, which_one, temperature):  # noqa: N802
        if self._defaults['CalFetchTemperature']['return'] != 0:
            return self._defaults['CalFetchTemperature']['return']
        # temperature
        if self._defaults['CalFetchTemperature']['temperature'] is None:
            raise MockFunctionCallError("niScope_CalFetchTemperature", param='temperature')
        if temperature is not None:
            temperature.contents.value = self._defaults['CalFetchTemperature']['temperature']
        return self._defaults['CalFetchTemperature']['return']

    def niScope_CalSelfCalibrate(self, vi, channel_list, option):  # noqa: N802
        if self._defaults['CalSelfCalibrate']['return'] != 0:
            return self._defaults['CalSelfCalibrate']['return']
        return self._defaults['CalSelfCalibrate']['return']

    def niScope_ClearWaveformMeasurementStats(self, vi, channel_list, clearable_measurement_function):  # noqa: N802
        if self._defaults['ClearWaveformMeasurementStats']['return'] != 0:
            return self._defaults['ClearWaveformMeasurementStats']['return']
        return self._defaults['ClearWaveformMeasurementStats']['return']

    def niScope_ClearWaveformProcessing(self, vi, channel_list):  # noqa: N802
        if self._defaults['ClearWaveformProcessing']['return'] != 0:
            return self._defaults['ClearWaveformProcessing']['return']
        return self._defaults['ClearWaveformProcessing']['return']

    def niScope_Commit(self, vi):  # noqa: N802
        if self._defaults['Commit']['return'] != 0:
            return self._defaults['Commit']['return']
        return self._defaults['Commit']['return']

    def niScope_ConfigureChanCharacteristics(self, vi, channel_list, input_impedance, max_input_frequency):  # noqa: N802
        if self._defaults['ConfigureChanCharacteristics']['return'] != 0:
            return self._defaults['ConfigureChanCharacteristics']['return']
        return self._defaults['ConfigureChanCharacteristics']['return']

    def niScope_ConfigureEqualizationFilterCoefficients(self, vi, channel_list, number_of_coefficients, coefficients):  # noqa: N802
        if self._defaults['ConfigureEqualizationFilterCoefficients']['return'] != 0:
            return self._defaults['ConfigureEqualizationFilterCoefficients']['return']
        return self._defaults['ConfigureEqualizationFilterCoefficients']['return']

    def niScope_ConfigureHorizontalTiming(self, vi, min_sample_rate, min_num_pts, ref_position, num_records, enforce_realtime):  # noqa: N802
        if self._defaults['ConfigureHorizontalTiming']['return'] != 0:
            return self._defaults['ConfigureHorizontalTiming']['return']
        return self._defaults['ConfigureHorizontalTiming']['return']

    def niScope_ConfigureRefLevels(self, vi, low, mid, high):  # noqa: N802
        if self._defaults['ConfigureRefLevels']['return'] != 0:
            return self._defaults['ConfigureRefLevels']['return']
        return self._defaults['ConfigureRefLevels']['return']

    def niScope_ConfigureTriggerDigital(self, vi, trigger_source, slope, holdoff, delay):  # noqa: N802
        if self._defaults['ConfigureTriggerDigital']['return'] != 0:
            return self._defaults['ConfigureTriggerDigital']['return']
        return self._defaults['ConfigureTriggerDigital']['return']

    def niScope_ConfigureTriggerEdge(self, vi, trigger_source, level, slope, trigger_coupling, holdoff, delay):  # noqa: N802
        if self._defaults['ConfigureTriggerEdge']['return'] != 0:
            return self._defaults['ConfigureTriggerEdge']['return']
        return self._defaults['ConfigureTriggerEdge']['return']

    def niScope_ConfigureTriggerHysteresis(self, vi, trigger_source, level, hysteresis, slope, trigger_coupling, holdoff, delay):  # noqa: N802
        if self._defaults['ConfigureTriggerHysteresis']['return'] != 0:
            return self._defaults['ConfigureTriggerHysteresis']['return']
        return self._defaults['ConfigureTriggerHysteresis']['return']

    def niScope_ConfigureTriggerImmediate(self, vi):  # noqa: N802
        if self._defaults['ConfigureTriggerImmediate']['return'] != 0:
            return self._defaults['ConfigureTriggerImmediate']['return']
        return self._defaults['ConfigureTriggerImmediate']['return']

    def niScope_ConfigureTriggerSoftware(self, vi, holdoff, delay):  # noqa: N802
        if self._defaults['ConfigureTriggerSoftware']['return'] != 0:
            return self._defaults['ConfigureTriggerSoftware']['return']
        return self._defaults['ConfigureTriggerSoftware']['return']

    def niScope_ConfigureTriggerVideo(self, vi, trigger_source, enable_dc_restore, signal_format, event, line_number, polarity, trigger_coupling, holdoff, delay):  # noqa: N802
        if self._defaults['ConfigureTriggerVideo']['return'] != 0:
            return self._defaults['ConfigureTriggerVideo']['return']
        return self._defaults['ConfigureTriggerVideo']['return']

    def niScope_ConfigureTriggerWindow(self, vi, trigger_source, low_level, high_level, window_mode, trigger_coupling, holdoff, delay):  # noqa: N802
        if self._defaults['ConfigureTriggerWindow']['return'] != 0:
            return self._defaults['ConfigureTriggerWindow']['return']
        return self._defaults['ConfigureTriggerWindow']['return']

    def niScope_ConfigureVertical(self, vi, channel_list, range, offset, coupling, probe_attenuation, enabled):  # noqa: N802
        if self._defaults['ConfigureVertical']['return'] != 0:
            return self._defaults['ConfigureVertical']['return']
        return self._defaults['ConfigureVertical']['return']

    def niScope_Disable(self, vi):  # noqa: N802
        if self._defaults['Disable']['return'] != 0:
            return self._defaults['Disable']['return']
        return self._defaults['Disable']['return']

    def niScope_ExportAttributeConfigurationBuffer(self, vi, size_in_bytes, configuration):  # noqa: N802
        if self._defaults['ExportAttributeConfigurationBuffer']['return'] != 0:
            return self._defaults['ExportAttributeConfigurationBuffer']['return']
        # configuration
        if self._defaults['ExportAttributeConfigurationBuffer']['configuration'] is None:
            raise MockFunctionCallError("niScope_ExportAttributeConfigurationBuffer", param='configuration')
        if size_in_bytes.value == 0:
            return len(self._defaults['ExportAttributeConfigurationBuffer']['configuration'])
        try:
            configuration_ref = configuration.contents
        except AttributeError:
            configuration_ref = configuration
        for i in range(len(self._defaults['ExportAttributeConfigurationBuffer']['configuration'])):
            configuration_ref[i] = self._defaults['ExportAttributeConfigurationBuffer']['configuration'][i]
        return self._defaults['ExportAttributeConfigurationBuffer']['return']

    def niScope_ExportAttributeConfigurationFile(self, vi, file_path):  # noqa: N802
        if self._defaults['ExportAttributeConfigurationFile']['return'] != 0:
            return self._defaults['ExportAttributeConfigurationFile']['return']
        return self._defaults['ExportAttributeConfigurationFile']['return']

    def niScope_Fetch(self, vi, channel_list, timeout, num_samples, waveform, wfm_info):  # noqa: N802
        if self._defaults['Fetch']['return'] != 0:
            return self._defaults['Fetch']['return']
        # waveform
        if self._defaults['Fetch']['waveform'] is None:
            raise MockFunctionCallError("niScope_Fetch", param='waveform')
        test_value = self._defaults['Fetch']['waveform']
        try:
            waveform_ref = waveform.contents
        except AttributeError:
            waveform_ref = waveform
        assert len(waveform_ref) >= len(test_value)
        for i in range(len(test_value)):
            waveform_ref[i] = test_value[i]
        # wfm_info
        if self._defaults['Fetch']['wfmInfo'] is None:
            raise MockFunctionCallError("niScope_Fetch", param='wfmInfo')
        test_value = self._defaults['Fetch']['wfmInfo']
        try:
            wfm_info_ref = wfm_info.contents
        except AttributeError:
            wfm_info_ref = wfm_info
        assert len(wfm_info_ref) >= len(test_value)
        for i in range(len(test_value)):
            wfm_info_ref[i] = test_value[i]
        return self._defaults['Fetch']['return']

    def niScope_FetchArrayMeasurement(self, vi, channel_list, timeout, array_meas_function, measurement_waveform_size, meas_wfm, wfm_info):  # noqa: N802
        if self._defaults['FetchArrayMeasurement']['return'] != 0:
            return self._defaults['FetchArrayMeasurement']['return']
        # meas_wfm
        if self._defaults['FetchArrayMeasurement']['measWfm'] is None:
            raise MockFunctionCallError("niScope_FetchArrayMeasurement", param='measWfm')
        test_value = self._defaults['FetchArrayMeasurement']['measWfm']
        try:
            meas_wfm_ref = meas_wfm.contents
        except AttributeError:
            meas_wfm_ref = meas_wfm
        assert len(meas_wfm_ref) >= len(test_value)
        for i in range(len(test_value)):
            meas_wfm_ref[i] = test_value[i]
        # wfm_info
        if self._defaults['FetchArrayMeasurement']['wfmInfo'] is None:
            raise MockFunctionCallError("niScope_FetchArrayMeasurement", param='wfmInfo')
        test_value = self._defaults['FetchArrayMeasurement']['wfmInfo']
        try:
            wfm_info_ref = wfm_info.contents
        except AttributeError:
            wfm_info_ref = wfm_info
        assert len(wfm_info_ref) >= len(test_value)
        for i in range(len(test_value)):
            wfm_info_ref[i] = test_value[i]
        return self._defaults['FetchArrayMeasurement']['return']

    def niScope_FetchBinary16(self, vi, channel_list, timeout, num_samples, waveform, wfm_info):  # noqa: N802
        if self._defaults['FetchBinary16']['return'] != 0:
            return self._defaults['FetchBinary16']['return']
        # waveform
        if self._defaults['FetchBinary16']['waveform'] is None:
            raise MockFunctionCallError("niScope_FetchBinary16", param='waveform')
        test_value = self._defaults['FetchBinary16']['waveform']
        try:
            waveform_ref = waveform.contents
        except AttributeError:
            waveform_ref = waveform
        assert len(waveform_ref) >= len(test_value)
        for i in range(len(test_value)):
            waveform_ref[i] = test_value[i]
        # wfm_info
        if self._defaults['FetchBinary16']['wfmInfo'] is None:
            raise MockFunctionCallError("niScope_FetchBinary16", param='wfmInfo')
        test_value = self._defaults['FetchBinary16']['wfmInfo']
        try:
            wfm_info_ref = wfm_info.contents
        except AttributeError:
            wfm_info_ref = wfm_info
        assert len(wfm_info_ref) >= len(test_value)
        for i in range(len(test_value)):
            wfm_info_ref[i] = test_value[i]
        return self._defaults['FetchBinary16']['return']

    def niScope_FetchBinary32(self, vi, channel_list, timeout, num_samples, waveform, wfm_info):  # noqa: N802
        if self._defaults['FetchBinary32']['return'] != 0:
            return self._defaults['FetchBinary32']['return']
        # waveform
        if self._defaults['FetchBinary32']['waveform'] is None:
            raise MockFunctionCallError("niScope_FetchBinary32", param='waveform')
        test_value = self._defaults['FetchBinary32']['waveform']
        try:
            waveform_ref = waveform.contents
        except AttributeError:
            waveform_ref = waveform
        assert len(waveform_ref) >= len(test_value)
        for i in range(len(test_value)):
            waveform_ref[i] = test_value[i]
        # wfm_info
        if self._defaults['FetchBinary32']['wfmInfo'] is None:
            raise MockFunctionCallError("niScope_FetchBinary32", param='wfmInfo')
        test_value = self._defaults['FetchBinary32']['wfmInfo']
        try:
            wfm_info_ref = wfm_info.contents
        except AttributeError:
            wfm_info_ref = wfm_info
        assert len(wfm_info_ref) >= len(test_value)
        for i in range(len(test_value)):
            wfm_info_ref[i] = test_value[i]
        return self._defaults['FetchBinary32']['return']

    def niScope_FetchBinary8(self, vi, channel_list, timeout, num_samples, waveform, wfm_info):  # noqa: N802
        if self._defaults['FetchBinary8']['return'] != 0:
            return self._defaults['FetchBinary8']['return']
        # waveform
        if self._defaults['FetchBinary8']['waveform'] is None:
            raise MockFunctionCallError("niScope_FetchBinary8", param='waveform')
        test_value = self._defaults['FetchBinary8']['waveform']
        try:
            waveform_ref = waveform.contents
        except AttributeError:
            waveform_ref = waveform
        assert len(waveform_ref) >= len(test_value)
        for i in range(len(test_value)):
            waveform_ref[i] = test_value[i]
        # wfm_info
        if self._defaults['FetchBinary8']['wfmInfo'] is None:
            raise MockFunctionCallError("niScope_FetchBinary8", param='wfmInfo')
        test_value = self._defaults['FetchBinary8']['wfmInfo']
        try:
            wfm_info_ref = wfm_info.contents
        except AttributeError:
            wfm_info_ref = wfm_info
        assert len(wfm_info_ref) >= len(test_value)
        for i in range(len(test_value)):
            wfm_info_ref[i] = test_value[i]
        return self._defaults['FetchBinary8']['return']

    def niScope_FetchMeasurementStats(self, vi, channel_list, timeout, scalar_meas_function, result, mean, stdev, min, max, num_in_stats):  # noqa: N802
        if self._defaults['FetchMeasurementStats']['return'] != 0:
            return self._defaults['FetchMeasurementStats']['return']
        # result
        if self._defaults['FetchMeasurementStats']['result'] is None:
            raise MockFunctionCallError("niScope_FetchMeasurementStats", param='result')
        test_value = self._defaults['FetchMeasurementStats']['result']
        try:
            result_ref = result.contents
        except AttributeError:
            result_ref = result
        assert len(result_ref) >= len(test_value)
        for i in range(len(test_value)):
            result_ref[i] = test_value[i]
        # mean
        if self._defaults['FetchMeasurementStats']['mean'] is None:
            raise MockFunctionCallError("niScope_FetchMeasurementStats", param='mean')
        test_value = self._defaults['FetchMeasurementStats']['mean']
        try:
            mean_ref = mean.contents
        except AttributeError:
            mean_ref = mean
        assert len(mean_ref) >= len(test_value)
        for i in range(len(test_value)):
            mean_ref[i] = test_value[i]
        # stdev
        if self._defaults['FetchMeasurementStats']['stdev'] is None:
            raise MockFunctionCallError("niScope_FetchMeasurementStats", param='stdev')
        test_value = self._defaults['FetchMeasurementStats']['stdev']
        try:
            stdev_ref = stdev.contents
        except AttributeError:
            stdev_ref = stdev
        assert len(stdev_ref) >= len(test_value)
        for i in range(len(test_value)):
            stdev_ref[i] = test_value[i]
        # min
        if self._defaults['FetchMeasurementStats']['min'] is None:
            raise MockFunctionCallError("niScope_FetchMeasurementStats", param='min')
        test_value = self._defaults['FetchMeasurementStats']['min']
        try:
            min_ref = min.contents
        except AttributeError:
            min_ref = min
        assert len(min_ref) >= len(test_value)
        for i in range(len(test_value)):
            min_ref[i] = test_value[i]
        # max
        if self._defaults['FetchMeasurementStats']['max'] is None:
            raise MockFunctionCallError("niScope_FetchMeasurementStats", param='max')
        test_value = self._defaults['FetchMeasurementStats']['max']
        try:
            max_ref = max.contents
        except AttributeError:
            max_ref = max
        assert len(max_ref) >= len(test_value)
        for i in range(len(test_value)):
            max_ref[i] = test_value[i]
        # num_in_stats
        if self._defaults['FetchMeasurementStats']['numInStats'] is None:
            raise MockFunctionCallError("niScope_FetchMeasurementStats", param='numInStats')
        test_value = self._defaults['FetchMeasurementStats']['numInStats']
        try:
            num_in_stats_ref = num_in_stats.contents
        except AttributeError:
            num_in_stats_ref = num_in_stats
        assert len(num_in_stats_ref) >= len(test_value)
        for i in range(len(test_value)):
            num_in_stats_ref[i] = test_value[i]
        return self._defaults['FetchMeasurementStats']['return']

    def niScope_GetAttributeViBoolean(self, vi, channel_list, attribute_id, value):  # noqa: N802
        if self._defaults['GetAttributeViBoolean']['return'] != 0:
            return self._defaults['GetAttributeViBoolean']['return']
        # value
        if self._defaults['GetAttributeViBoolean']['value'] is None:
            raise MockFunctionCallError("niScope_GetAttributeViBoolean", param='value')
        if value is not None:
            value.contents.value = self._defaults['GetAttributeViBoolean']['value']
        return self._defaults['GetAttributeViBoolean']['return']

    def niScope_GetAttributeViInt32(self, vi, channel_list, attribute_id, value):  # noqa: N802
        if self._defaults['GetAttributeViInt32']['return'] != 0:
            return self._defaults['GetAttributeViInt32']['return']
        # value
        if self._defaults['GetAttributeViInt32']['value'] is None:
            raise MockFunctionCallError("niScope_GetAttributeViInt32", param='value')
        if value is not None:
            value.contents.value = self._defaults['GetAttributeViInt32']['value']
        return self._defaults['GetAttributeViInt32']['return']

    def niScope_GetAttributeViInt64(self, vi, channel_list, attribute_id, value):  # noqa: N802
        if self._defaults['GetAttributeViInt64']['return'] != 0:
            return self._defaults['GetAttributeViInt64']['return']
        # value
        if self._defaults['GetAttributeViInt64']['value'] is None:
            raise MockFunctionCallError("niScope_GetAttributeViInt64", param='value')
        if value is not None:
            value.contents.value = self._defaults['GetAttributeViInt64']['value']
        return self._defaults['GetAttributeViInt64']['return']

    def niScope_GetAttributeViReal64(self, vi, channel_list, attribute_id, value):  # noqa: N802
        if self._defaults['GetAttributeViReal64']['return'] != 0:
            return self._defaults['GetAttributeViReal64']['return']
        # value
        if self._defaults['GetAttributeViReal64']['value'] is None:
            raise MockFunctionCallError("niScope_GetAttributeViReal64", param='value')
        if value is not None:
            value.contents.value = self._defaults['GetAttributeViReal64']['value']
        return self._defaults['GetAttributeViReal64']['return']

    def niScope_GetAttributeViString(self, vi, channel_list, attribute_id, buf_size, value):  # noqa: N802
        if self._defaults['GetAttributeViString']['return'] != 0:
            return self._defaults['GetAttributeViString']['return']
        # value
        if self._defaults['GetAttributeViString']['value'] is None:
            raise MockFunctionCallError("niScope_GetAttributeViString", param='value')
        if buf_size.value == 0:
            return len(self._defaults['GetAttributeViString']['value'])
        value.value = self._defaults['GetAttributeViString']['value'].encode('ascii')
        return self._defaults['GetAttributeViString']['return']

    def niScope_GetChannelNameFromString(self, vi, indices, buffer_size, names):  # noqa: N802
        if self._defaults['GetChannelNameFromString']['return'] != 0:
            return self._defaults['GetChannelNameFromString']['return']
        # names
        if self._defaults['GetChannelNameFromString']['name'] is None:
            raise MockFunctionCallError("niScope_GetChannelNameFromString", param='name')
        if buffer_size.value == 0:
            return len(self._defaults['GetChannelNameFromString']['name'])
        names.value = self._defaults['GetChannelNameFromString']['name'].encode('ascii')
        return self._defaults['GetChannelNameFromString']['return']

    def niScope_GetEqualizationFilterCoefficients(self, vi, channel, number_of_coefficients, coefficients):  # noqa: N802
        if self._defaults['GetEqualizationFilterCoefficients']['return'] != 0:
            return self._defaults['GetEqualizationFilterCoefficients']['return']
        # coefficients
        if self._defaults['GetEqualizationFilterCoefficients']['coefficients'] is None:
            raise MockFunctionCallError("niScope_GetEqualizationFilterCoefficients", param='coefficients')
        test_value = self._defaults['GetEqualizationFilterCoefficients']['coefficients']
        try:
            coefficients_ref = coefficients.contents
        except AttributeError:
            coefficients_ref = coefficients
        assert len(coefficients_ref) >= len(test_value)
        for i in range(len(test_value)):
            coefficients_ref[i] = test_value[i]
        return self._defaults['GetEqualizationFilterCoefficients']['return']

    def niScope_GetError(self, vi, error_code, buffer_size, description):  # noqa: N802
        if self._defaults['GetError']['return'] != 0:
            return self._defaults['GetError']['return']
        # error_code
        if self._defaults['GetError']['errorCode'] is None:
            raise MockFunctionCallError("niScope_GetError", param='errorCode')
        if error_code is not None:
            error_code.contents.value = self._defaults['GetError']['errorCode']
        # description
        if self._defaults['GetError']['description'] is None:
            raise MockFunctionCallError("niScope_GetError", param='description')
        if buffer_size.value == 0:
            return len(self._defaults['GetError']['description'])
        description.value = self._defaults['GetError']['description'].encode('ascii')
        return self._defaults['GetError']['return']

    def niScope_ImportAttributeConfigurationBuffer(self, vi, size_in_bytes, configuration):  # noqa: N802
        if self._defaults['ImportAttributeConfigurationBuffer']['return'] != 0:
            return self._defaults['ImportAttributeConfigurationBuffer']['return']
        return self._defaults['ImportAttributeConfigurationBuffer']['return']

    def niScope_ImportAttributeConfigurationFile(self, vi, file_path):  # noqa: N802
        if self._defaults['ImportAttributeConfigurationFile']['return'] != 0:
            return self._defaults['ImportAttributeConfigurationFile']['return']
        return self._defaults['ImportAttributeConfigurationFile']['return']

    def niScope_InitWithOptions(self, resource_name, id_query, reset_device, option_string, vi):  # noqa: N802
        if self._defaults['InitWithOptions']['return'] != 0:
            return self._defaults['InitWithOptions']['return']
        # vi
        if self._defaults['InitWithOptions']['vi'] is None:
            raise MockFunctionCallError("niScope_InitWithOptions", param='vi')
        if vi is not None:
            vi.contents.value = self._defaults['InitWithOptions']['vi']
        return self._defaults['InitWithOptions']['return']

    def niScope_InitiateAcquisition(self, vi):  # noqa: N802
        if self._defaults['InitiateAcquisition']['return'] != 0:
            return self._defaults['InitiateAcquisition']['return']
        return self._defaults['InitiateAcquisition']['return']

    def niScope_LockSession(self, vi, caller_has_lock):  # noqa: N802
        if self._defaults['LockSession']['return'] != 0:
            return self._defaults['LockSession']['return']
        # caller_has_lock
        if self._defaults['LockSession']['callerHasLock'] is None:
            raise MockFunctionCallError("niScope_LockSession", param='callerHasLock')
        if caller_has_lock is not None:
            caller_has_lock.contents.value = self._defaults['LockSession']['callerHasLock']
        return self._defaults['LockSession']['return']

    def niScope_ProbeCompensationSignalStart(self, vi):  # noqa: N802
        if self._defaults['ProbeCompensationSignalStart']['return'] != 0:
            return self._defaults['ProbeCompensationSignalStart']['return']
        return self._defaults['ProbeCompensationSignalStart']['return']

    def niScope_ProbeCompensationSignalStop(self, vi):  # noqa: N802
        if self._defaults['ProbeCompensationSignalStop']['return'] != 0:
            return self._defaults['ProbeCompensationSignalStop']['return']
        return self._defaults['ProbeCompensationSignalStop']['return']

    def niScope_Read(self, vi, channel_list, timeout, num_samples, waveform, wfm_info):  # noqa: N802
        if self._defaults['Read']['return'] != 0:
            return self._defaults['Read']['return']
        # waveform
        if self._defaults['Read']['waveform'] is None:
            raise MockFunctionCallError("niScope_Read", param='waveform')
        test_value = self._defaults['Read']['waveform']
        try:
            waveform_ref = waveform.contents
        except AttributeError:
            waveform_ref = waveform
        assert len(waveform_ref) >= len(test_value)
        for i in range(len(test_value)):
            waveform_ref[i] = test_value[i]
        # wfm_info
        if self._defaults['Read']['wfmInfo'] is None:
            raise MockFunctionCallError("niScope_Read", param='wfmInfo')
        test_value = self._defaults['Read']['wfmInfo']
        try:
            wfm_info_ref = wfm_info.contents
        except AttributeError:
            wfm_info_ref = wfm_info
        assert len(wfm_info_ref) >= len(test_value)
        for i in range(len(test_value)):
            wfm_info_ref[i] = test_value[i]
        return self._defaults['Read']['return']

    def niScope_ResetDevice(self, vi):  # noqa: N802
        if self._defaults['ResetDevice']['return'] != 0:
            return self._defaults['ResetDevice']['return']
        return self._defaults['ResetDevice']['return']

    def niScope_ResetWithDefaults(self, vi):  # noqa: N802
        if self._defaults['ResetWithDefaults']['return'] != 0:
            return self._defaults['ResetWithDefaults']['return']
        return self._defaults['ResetWithDefaults']['return']

    def niScope_SendSoftwareTriggerEdge(self, vi, which_trigger):  # noqa: N802
        if self._defaults['SendSoftwareTriggerEdge']['return'] != 0:
            return self._defaults['SendSoftwareTriggerEdge']['return']
        return self._defaults['SendSoftwareTriggerEdge']['return']

    def niScope_SetAttributeViBoolean(self, vi, channel_list, attribute_id, value):  # noqa: N802
        if self._defaults['SetAttributeViBoolean']['return'] != 0:
            return self._defaults['SetAttributeViBoolean']['return']
        return self._defaults['SetAttributeViBoolean']['return']

    def niScope_SetAttributeViInt32(self, vi, channel_list, attribute_id, value):  # noqa: N802
        if self._defaults['SetAttributeViInt32']['return'] != 0:
            return self._defaults['SetAttributeViInt32']['return']
        return self._defaults['SetAttributeViInt32']['return']

    def niScope_SetAttributeViInt64(self, vi, channel_list, attribute_id, value):  # noqa: N802
        if self._defaults['SetAttributeViInt64']['return'] != 0:
            return self._defaults['SetAttributeViInt64']['return']
        return self._defaults['SetAttributeViInt64']['return']

    def niScope_SetAttributeViReal64(self, vi, channel_list, attribute_id, value):  # noqa: N802
        if self._defaults['SetAttributeViReal64']['return'] != 0:
            return self._defaults['SetAttributeViReal64']['return']
        return self._defaults['SetAttributeViReal64']['return']

    def niScope_SetAttributeViString(self, vi, channel_list, attribute_id, value):  # noqa: N802
        if self._defaults['SetAttributeViString']['return'] != 0:
            return self._defaults['SetAttributeViString']['return']
        return self._defaults['SetAttributeViString']['return']

    def niScope_SetRuntimeEnvironment(self, environment, environment_version, reserved1, reserved2):  # noqa: N802
        if self._defaults['SetRuntimeEnvironment']['return'] != 0:
            return self._defaults['SetRuntimeEnvironment']['return']
        return self._defaults['SetRuntimeEnvironment']['return']

    def niScope_UnlockSession(self, vi, caller_has_lock):  # noqa: N802
        if self._defaults['UnlockSession']['return'] != 0:
            return self._defaults['UnlockSession']['return']
        # caller_has_lock
        if self._defaults['UnlockSession']['callerHasLock'] is None:
            raise MockFunctionCallError("niScope_UnlockSession", param='callerHasLock')
        if caller_has_lock is not None:
            caller_has_lock.contents.value = self._defaults['UnlockSession']['callerHasLock']
        return self._defaults['UnlockSession']['return']

    def niScope_close(self, vi):  # noqa: N802
        if self._defaults['close']['return'] != 0:
            return self._defaults['close']['return']
        return self._defaults['close']['return']

    def niScope_error_message(self, vi, error_code, error_message):  # noqa: N802
        if self._defaults['error_message']['return'] != 0:
            return self._defaults['error_message']['return']
        # error_message
        if self._defaults['error_message']['errorMessage'] is None:
            raise MockFunctionCallError("niScope_error_message", param='errorMessage')
        test_value = self._defaults['error_message']['errorMessage']
        if type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(error_message) >= len(test_value)
        for i in range(len(test_value)):
            error_message[i] = test_value[i]
        return self._defaults['error_message']['return']

    def niScope_reset(self, vi):  # noqa: N802
        if self._defaults['reset']['return'] != 0:
            return self._defaults['reset']['return']
        return self._defaults['reset']['return']

    def niScope_self_test(self, vi, self_test_result, self_test_message):  # noqa: N802
        if self._defaults['self_test']['return'] != 0:
            return self._defaults['self_test']['return']
        # self_test_result
        if self._defaults['self_test']['selfTestResult'] is None:
            raise MockFunctionCallError("niScope_self_test", param='selfTestResult')
        if self_test_result is not None:
            self_test_result.contents.value = self._defaults['self_test']['selfTestResult']
        # self_test_message
        if self._defaults['self_test']['selfTestMessage'] is None:
            raise MockFunctionCallError("niScope_self_test", param='selfTestMessage')
        test_value = self._defaults['self_test']['selfTestMessage']
        if type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(self_test_message) >= len(test_value)
        for i in range(len(test_value)):
            self_test_message[i] = test_value[i]
        return self._defaults['self_test']['return']

    # Helper function to setup Mock object with default side effects and return values
    def set_side_effects_and_return_values(self, mock_library):
        mock_library.niScope_Abort.side_effect = MockFunctionCallError("niScope_Abort")
        mock_library.niScope_Abort.return_value = 0
        mock_library.niScope_AcquisitionStatus.side_effect = MockFunctionCallError("niScope_AcquisitionStatus")
        mock_library.niScope_AcquisitionStatus.return_value = 0
        mock_library.niScope_ActualMeasWfmSize.side_effect = MockFunctionCallError("niScope_ActualMeasWfmSize")
        mock_library.niScope_ActualMeasWfmSize.return_value = 0
        mock_library.niScope_ActualNumWfms.side_effect = MockFunctionCallError("niScope_ActualNumWfms")
        mock_library.niScope_ActualNumWfms.return_value = 0
        mock_library.niScope_AddWaveformProcessing.side_effect = MockFunctionCallError("niScope_AddWaveformProcessing")
        mock_library.niScope_AddWaveformProcessing.return_value = 0
        mock_library.niScope_AutoSetup.side_effect = MockFunctionCallError("niScope_AutoSetup")
        mock_library.niScope_AutoSetup.return_value = 0
        mock_library.niScope_CalFetchDate.side_effect = MockFunctionCallError("niScope_CalFetchDate")
        mock_library.niScope_CalFetchDate.return_value = 0
        mock_library.niScope_CalFetchTemperature.side_effect = MockFunctionCallError("niScope_CalFetchTemperature")
        mock_library.niScope_CalFetchTemperature.return_value = 0
        mock_library.niScope_CalSelfCalibrate.side_effect = MockFunctionCallError("niScope_CalSelfCalibrate")
        mock_library.niScope_CalSelfCalibrate.return_value = 0
        mock_library.niScope_ClearWaveformMeasurementStats.side_effect = MockFunctionCallError("niScope_ClearWaveformMeasurementStats")
        mock_library.niScope_ClearWaveformMeasurementStats.return_value = 0
        mock_library.niScope_ClearWaveformProcessing.side_effect = MockFunctionCallError("niScope_ClearWaveformProcessing")
        mock_library.niScope_ClearWaveformProcessing.return_value = 0
        mock_library.niScope_Commit.side_effect = MockFunctionCallError("niScope_Commit")
        mock_library.niScope_Commit.return_value = 0
        mock_library.niScope_ConfigureChanCharacteristics.side_effect = MockFunctionCallError("niScope_ConfigureChanCharacteristics")
        mock_library.niScope_ConfigureChanCharacteristics.return_value = 0
        mock_library.niScope_ConfigureEqualizationFilterCoefficients.side_effect = MockFunctionCallError("niScope_ConfigureEqualizationFilterCoefficients")
        mock_library.niScope_ConfigureEqualizationFilterCoefficients.return_value = 0
        mock_library.niScope_ConfigureHorizontalTiming.side_effect = MockFunctionCallError("niScope_ConfigureHorizontalTiming")
        mock_library.niScope_ConfigureHorizontalTiming.return_value = 0
        mock_library.niScope_ConfigureRefLevels.side_effect = MockFunctionCallError("niScope_ConfigureRefLevels")
        mock_library.niScope_ConfigureRefLevels.return_value = 0
        mock_library.niScope_ConfigureTriggerDigital.side_effect = MockFunctionCallError("niScope_ConfigureTriggerDigital")
        mock_library.niScope_ConfigureTriggerDigital.return_value = 0
        mock_library.niScope_ConfigureTriggerEdge.side_effect = MockFunctionCallError("niScope_ConfigureTriggerEdge")
        mock_library.niScope_ConfigureTriggerEdge.return_value = 0
        mock_library.niScope_ConfigureTriggerHysteresis.side_effect = MockFunctionCallError("niScope_ConfigureTriggerHysteresis")
        mock_library.niScope_ConfigureTriggerHysteresis.return_value = 0
        mock_library.niScope_ConfigureTriggerImmediate.side_effect = MockFunctionCallError("niScope_ConfigureTriggerImmediate")
        mock_library.niScope_ConfigureTriggerImmediate.return_value = 0
        mock_library.niScope_ConfigureTriggerSoftware.side_effect = MockFunctionCallError("niScope_ConfigureTriggerSoftware")
        mock_library.niScope_ConfigureTriggerSoftware.return_value = 0
        mock_library.niScope_ConfigureTriggerVideo.side_effect = MockFunctionCallError("niScope_ConfigureTriggerVideo")
        mock_library.niScope_ConfigureTriggerVideo.return_value = 0
        mock_library.niScope_ConfigureTriggerWindow.side_effect = MockFunctionCallError("niScope_ConfigureTriggerWindow")
        mock_library.niScope_ConfigureTriggerWindow.return_value = 0
        mock_library.niScope_ConfigureVertical.side_effect = MockFunctionCallError("niScope_ConfigureVertical")
        mock_library.niScope_ConfigureVertical.return_value = 0
        mock_library.niScope_Disable.side_effect = MockFunctionCallError("niScope_Disable")
        mock_library.niScope_Disable.return_value = 0
        mock_library.niScope_ExportAttributeConfigurationBuffer.side_effect = MockFunctionCallError("niScope_ExportAttributeConfigurationBuffer")
        mock_library.niScope_ExportAttributeConfigurationBuffer.return_value = 0
        mock_library.niScope_ExportAttributeConfigurationFile.side_effect = MockFunctionCallError("niScope_ExportAttributeConfigurationFile")
        mock_library.niScope_ExportAttributeConfigurationFile.return_value = 0
        mock_library.niScope_Fetch.side_effect = MockFunctionCallError("niScope_Fetch")
        mock_library.niScope_Fetch.return_value = 0
        mock_library.niScope_FetchArrayMeasurement.side_effect = MockFunctionCallError("niScope_FetchArrayMeasurement")
        mock_library.niScope_FetchArrayMeasurement.return_value = 0
        mock_library.niScope_FetchBinary16.side_effect = MockFunctionCallError("niScope_FetchBinary16")
        mock_library.niScope_FetchBinary16.return_value = 0
        mock_library.niScope_FetchBinary32.side_effect = MockFunctionCallError("niScope_FetchBinary32")
        mock_library.niScope_FetchBinary32.return_value = 0
        mock_library.niScope_FetchBinary8.side_effect = MockFunctionCallError("niScope_FetchBinary8")
        mock_library.niScope_FetchBinary8.return_value = 0
        mock_library.niScope_FetchMeasurementStats.side_effect = MockFunctionCallError("niScope_FetchMeasurementStats")
        mock_library.niScope_FetchMeasurementStats.return_value = 0
        mock_library.niScope_GetAttributeViBoolean.side_effect = MockFunctionCallError("niScope_GetAttributeViBoolean")
        mock_library.niScope_GetAttributeViBoolean.return_value = 0
        mock_library.niScope_GetAttributeViInt32.side_effect = MockFunctionCallError("niScope_GetAttributeViInt32")
        mock_library.niScope_GetAttributeViInt32.return_value = 0
        mock_library.niScope_GetAttributeViInt64.side_effect = MockFunctionCallError("niScope_GetAttributeViInt64")
        mock_library.niScope_GetAttributeViInt64.return_value = 0
        mock_library.niScope_GetAttributeViReal64.side_effect = MockFunctionCallError("niScope_GetAttributeViReal64")
        mock_library.niScope_GetAttributeViReal64.return_value = 0
        mock_library.niScope_GetAttributeViString.side_effect = MockFunctionCallError("niScope_GetAttributeViString")
        mock_library.niScope_GetAttributeViString.return_value = 0
        mock_library.niScope_GetChannelNameFromString.side_effect = MockFunctionCallError("niScope_GetChannelNameFromString")
        mock_library.niScope_GetChannelNameFromString.return_value = 0
        mock_library.niScope_GetEqualizationFilterCoefficients.side_effect = MockFunctionCallError("niScope_GetEqualizationFilterCoefficients")
        mock_library.niScope_GetEqualizationFilterCoefficients.return_value = 0
        mock_library.niScope_GetError.side_effect = MockFunctionCallError("niScope_GetError")
        mock_library.niScope_GetError.return_value = 0
        mock_library.niScope_ImportAttributeConfigurationBuffer.side_effect = MockFunctionCallError("niScope_ImportAttributeConfigurationBuffer")
        mock_library.niScope_ImportAttributeConfigurationBuffer.return_value = 0
        mock_library.niScope_ImportAttributeConfigurationFile.side_effect = MockFunctionCallError("niScope_ImportAttributeConfigurationFile")
        mock_library.niScope_ImportAttributeConfigurationFile.return_value = 0
        mock_library.niScope_InitWithOptions.side_effect = MockFunctionCallError("niScope_InitWithOptions")
        mock_library.niScope_InitWithOptions.return_value = 0
        mock_library.niScope_InitiateAcquisition.side_effect = MockFunctionCallError("niScope_InitiateAcquisition")
        mock_library.niScope_InitiateAcquisition.return_value = 0
        mock_library.niScope_LockSession.side_effect = MockFunctionCallError("niScope_LockSession")
        mock_library.niScope_LockSession.return_value = 0
        mock_library.niScope_ProbeCompensationSignalStart.side_effect = MockFunctionCallError("niScope_ProbeCompensationSignalStart")
        mock_library.niScope_ProbeCompensationSignalStart.return_value = 0
        mock_library.niScope_ProbeCompensationSignalStop.side_effect = MockFunctionCallError("niScope_ProbeCompensationSignalStop")
        mock_library.niScope_ProbeCompensationSignalStop.return_value = 0
        mock_library.niScope_Read.side_effect = MockFunctionCallError("niScope_Read")
        mock_library.niScope_Read.return_value = 0
        mock_library.niScope_ResetDevice.side_effect = MockFunctionCallError("niScope_ResetDevice")
        mock_library.niScope_ResetDevice.return_value = 0
        mock_library.niScope_ResetWithDefaults.side_effect = MockFunctionCallError("niScope_ResetWithDefaults")
        mock_library.niScope_ResetWithDefaults.return_value = 0
        mock_library.niScope_SendSoftwareTriggerEdge.side_effect = MockFunctionCallError("niScope_SendSoftwareTriggerEdge")
        mock_library.niScope_SendSoftwareTriggerEdge.return_value = 0
        mock_library.niScope_SetAttributeViBoolean.side_effect = MockFunctionCallError("niScope_SetAttributeViBoolean")
        mock_library.niScope_SetAttributeViBoolean.return_value = 0
        mock_library.niScope_SetAttributeViInt32.side_effect = MockFunctionCallError("niScope_SetAttributeViInt32")
        mock_library.niScope_SetAttributeViInt32.return_value = 0
        mock_library.niScope_SetAttributeViInt64.side_effect = MockFunctionCallError("niScope_SetAttributeViInt64")
        mock_library.niScope_SetAttributeViInt64.return_value = 0
        mock_library.niScope_SetAttributeViReal64.side_effect = MockFunctionCallError("niScope_SetAttributeViReal64")
        mock_library.niScope_SetAttributeViReal64.return_value = 0
        mock_library.niScope_SetAttributeViString.side_effect = MockFunctionCallError("niScope_SetAttributeViString")
        mock_library.niScope_SetAttributeViString.return_value = 0
        mock_library.niScope_SetRuntimeEnvironment.side_effect = MockFunctionCallError("niScope_SetRuntimeEnvironment")
        mock_library.niScope_SetRuntimeEnvironment.return_value = 0
        mock_library.niScope_UnlockSession.side_effect = MockFunctionCallError("niScope_UnlockSession")
        mock_library.niScope_UnlockSession.return_value = 0
        mock_library.niScope_close.side_effect = MockFunctionCallError("niScope_close")
        mock_library.niScope_close.return_value = 0
        mock_library.niScope_error_message.side_effect = MockFunctionCallError("niScope_error_message")
        mock_library.niScope_error_message.return_value = 0
        mock_library.niScope_reset.side_effect = MockFunctionCallError("niScope_reset")
        mock_library.niScope_reset.return_value = 0
        mock_library.niScope_self_test.side_effect = MockFunctionCallError("niScope_self_test")
        mock_library.niScope_self_test.return_value = 0
