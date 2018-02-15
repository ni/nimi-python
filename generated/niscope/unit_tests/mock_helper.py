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
        self._defaults['ActualNumWfms'] = {}
        self._defaults['ActualNumWfms']['return'] = 0
        self._defaults['ActualNumWfms']['numWfms'] = None
        self._defaults['AutoSetup'] = {}
        self._defaults['AutoSetup']['return'] = 0
        self._defaults['CalSelfCalibrate'] = {}
        self._defaults['CalSelfCalibrate']['return'] = 0
        self._defaults['ClearWaveformMeasurementStats'] = {}
        self._defaults['ClearWaveformMeasurementStats']['return'] = 0
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
        self._defaults['ExportSignal'] = {}
        self._defaults['ExportSignal']['return'] = 0
        self._defaults['FancyFetch'] = {}
        self._defaults['FancyFetch']['return'] = 0
        self._defaults['FancyFetch']['wfmInfo'] = None
        self._defaults['Fetch'] = {}
        self._defaults['Fetch']['return'] = 0
        self._defaults['Fetch']['Wfm'] = None
        self._defaults['Fetch']['wfmInfo'] = None
        self._defaults['FetchBinary16'] = {}
        self._defaults['FetchBinary16']['return'] = 0
        self._defaults['FetchBinary16']['Wfm'] = None
        self._defaults['FetchBinary16']['wfmInfo'] = None
        self._defaults['FetchBinary32'] = {}
        self._defaults['FetchBinary32']['return'] = 0
        self._defaults['FetchBinary32']['Wfm'] = None
        self._defaults['FetchBinary32']['wfmInfo'] = None
        self._defaults['FetchBinary8'] = {}
        self._defaults['FetchBinary8']['return'] = 0
        self._defaults['FetchBinary8']['Wfm'] = None
        self._defaults['FetchBinary8']['wfmInfo'] = None
        self._defaults['FetchDispatcher'] = {}
        self._defaults['FetchDispatcher']['return'] = 0
        self._defaults['FetchDispatcher']['wfmInfo'] = None
        self._defaults['FetchMeasurement'] = {}
        self._defaults['FetchMeasurement']['return'] = 0
        self._defaults['FetchMeasurement']['Result'] = None
        self._defaults['FetchMeasurementStats'] = {}
        self._defaults['FetchMeasurementStats']['return'] = 0
        self._defaults['FetchMeasurementStats']['Result'] = None
        self._defaults['FetchMeasurementStats']['Mean'] = None
        self._defaults['FetchMeasurementStats']['Stdev'] = None
        self._defaults['FetchMeasurementStats']['Min'] = None
        self._defaults['FetchMeasurementStats']['Max'] = None
        self._defaults['FetchMeasurementStats']['numInStats'] = None
        self._defaults['GetAttributeViBoolean'] = {}
        self._defaults['GetAttributeViBoolean']['return'] = 0
        self._defaults['GetAttributeViBoolean']['Value'] = None
        self._defaults['GetAttributeViInt32'] = {}
        self._defaults['GetAttributeViInt32']['return'] = 0
        self._defaults['GetAttributeViInt32']['Value'] = None
        self._defaults['GetAttributeViReal64'] = {}
        self._defaults['GetAttributeViReal64']['return'] = 0
        self._defaults['GetAttributeViReal64']['Value'] = None
        self._defaults['GetAttributeViString'] = {}
        self._defaults['GetAttributeViString']['return'] = 0
        self._defaults['GetAttributeViString']['Value'] = None
        self._defaults['GetEqualizationFilterCoefficients'] = {}
        self._defaults['GetEqualizationFilterCoefficients']['return'] = 0
        self._defaults['GetEqualizationFilterCoefficients']['Coefficients'] = None
        self._defaults['GetError'] = {}
        self._defaults['GetError']['return'] = 0
        self._defaults['GetError']['errorCode'] = None
        self._defaults['GetError']['Description'] = None
        self._defaults['InitWithOptions'] = {}
        self._defaults['InitWithOptions']['return'] = 0
        self._defaults['InitWithOptions']['vi'] = None
        self._defaults['InitiateAcquisition'] = {}
        self._defaults['InitiateAcquisition']['return'] = 0
        self._defaults['ProbeCompensationSignalStart'] = {}
        self._defaults['ProbeCompensationSignalStart']['return'] = 0
        self._defaults['ProbeCompensationSignalStop'] = {}
        self._defaults['ProbeCompensationSignalStop']['return'] = 0
        self._defaults['Read'] = {}
        self._defaults['Read']['return'] = 0
        self._defaults['Read']['Wfm'] = None
        self._defaults['Read']['wfmInfo'] = None
        self._defaults['ReadMeasurement'] = {}
        self._defaults['ReadMeasurement']['return'] = 0
        self._defaults['ReadMeasurement']['Result'] = None
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
        self._defaults['SetAttributeViReal64'] = {}
        self._defaults['SetAttributeViReal64']['return'] = 0
        self._defaults['SetAttributeViString'] = {}
        self._defaults['SetAttributeViString']['return'] = 0
        self._defaults['close'] = {}
        self._defaults['close']['return'] = 0
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
        acquisition_status.contents.value = self._defaults['AcquisitionStatus']['acquisitionStatus']
        return self._defaults['AcquisitionStatus']['return']

    def niScope_ActualNumWfms(self, vi, channel_list, num_wfms):  # noqa: N802
        if self._defaults['ActualNumWfms']['return'] != 0:
            return self._defaults['ActualNumWfms']['return']
        # num_wfms
        if self._defaults['ActualNumWfms']['numWfms'] is None:
            raise MockFunctionCallError("niScope_ActualNumWfms", param='numWfms')
        num_wfms.contents.value = self._defaults['ActualNumWfms']['numWfms']
        return self._defaults['ActualNumWfms']['return']

    def niScope_AutoSetup(self, vi):  # noqa: N802
        if self._defaults['AutoSetup']['return'] != 0:
            return self._defaults['AutoSetup']['return']
        return self._defaults['AutoSetup']['return']

    def niScope_CalSelfCalibrate(self, vi, channel_list, option):  # noqa: N802
        if self._defaults['CalSelfCalibrate']['return'] != 0:
            return self._defaults['CalSelfCalibrate']['return']
        return self._defaults['CalSelfCalibrate']['return']

    def niScope_ClearWaveformMeasurementStats(self, vi, channel_list, clearable_measurement_function):  # noqa: N802
        if self._defaults['ClearWaveformMeasurementStats']['return'] != 0:
            return self._defaults['ClearWaveformMeasurementStats']['return']
        return self._defaults['ClearWaveformMeasurementStats']['return']

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

    def niScope_ExportSignal(self, vi, signal, signal_identifier, output_terminal):  # noqa: N802
        if self._defaults['ExportSignal']['return'] != 0:
            return self._defaults['ExportSignal']['return']
        return self._defaults['ExportSignal']['return']

    def niScope_FancyFetch(self, vi, channel_list, timeout, num_samples, fetch_relative_to, fetch_offet, fetch_record_number, fetch_num_records, wfm, wfm_info):  # noqa: N802
        if self._defaults['FancyFetch']['return'] != 0:
            return self._defaults['FancyFetch']['return']
        # wfm_info
        if self._defaults['FancyFetch']['wfmInfo'] is None:
            raise MockFunctionCallError("niScope_FancyFetch", param='wfmInfo')
        test_value = self._defaults['FancyFetch']['wfmInfo']
        try:
            wfm_info_ref = wfm_info.contents
        except AttributeError:
            wfm_info_ref = wfm_info
        assert len(wfm_info_ref) >= len(test_value)
        for i in range(len(test_value)):
            wfm_info_ref[i] = test_value[i]
        return self._defaults['FancyFetch']['return']

    def niScope_Fetch(self, vi, channel_list, timeout, num_samples, wfm, wfm_info):  # noqa: N802
        if self._defaults['Fetch']['return'] != 0:
            return self._defaults['Fetch']['return']
        # wfm
        if self._defaults['Fetch']['Wfm'] is None:
            raise MockFunctionCallError("niScope_Fetch", param='Wfm')
        test_value = self._defaults['Fetch']['Wfm']
        try:
            wfm_ref = wfm.contents
        except AttributeError:
            wfm_ref = wfm
        assert len(wfm_ref) >= len(test_value)
        for i in range(len(test_value)):
            wfm_ref[i] = test_value[i]
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

    def niScope_FetchBinary16(self, vi, channel_list, timeout, num_samples, wfm, wfm_info):  # noqa: N802
        if self._defaults['FetchBinary16']['return'] != 0:
            return self._defaults['FetchBinary16']['return']
        # wfm
        if self._defaults['FetchBinary16']['Wfm'] is None:
            raise MockFunctionCallError("niScope_FetchBinary16", param='Wfm')
        test_value = self._defaults['FetchBinary16']['Wfm']
        try:
            wfm_ref = wfm.contents
        except AttributeError:
            wfm_ref = wfm
        assert len(wfm_ref) >= len(test_value)
        for i in range(len(test_value)):
            wfm_ref[i] = test_value[i]
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

    def niScope_FetchBinary32(self, vi, channel_list, timeout, num_samples, wfm, wfm_info):  # noqa: N802
        if self._defaults['FetchBinary32']['return'] != 0:
            return self._defaults['FetchBinary32']['return']
        # wfm
        if self._defaults['FetchBinary32']['Wfm'] is None:
            raise MockFunctionCallError("niScope_FetchBinary32", param='Wfm')
        test_value = self._defaults['FetchBinary32']['Wfm']
        try:
            wfm_ref = wfm.contents
        except AttributeError:
            wfm_ref = wfm
        assert len(wfm_ref) >= len(test_value)
        for i in range(len(test_value)):
            wfm_ref[i] = test_value[i]
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

    def niScope_FetchBinary8(self, vi, channel_list, timeout, num_samples, wfm, wfm_info):  # noqa: N802
        if self._defaults['FetchBinary8']['return'] != 0:
            return self._defaults['FetchBinary8']['return']
        # wfm
        if self._defaults['FetchBinary8']['Wfm'] is None:
            raise MockFunctionCallError("niScope_FetchBinary8", param='Wfm')
        test_value = self._defaults['FetchBinary8']['Wfm']
        try:
            wfm_ref = wfm.contents
        except AttributeError:
            wfm_ref = wfm
        assert len(wfm_ref) >= len(test_value)
        for i in range(len(test_value)):
            wfm_ref[i] = test_value[i]
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

    def niScope_FetchDispatcher(self, vi, channel_list, timeout, num_samples, wfm, wfm_info):  # noqa: N802
        if self._defaults['FetchDispatcher']['return'] != 0:
            return self._defaults['FetchDispatcher']['return']
        # wfm_info
        if self._defaults['FetchDispatcher']['wfmInfo'] is None:
            raise MockFunctionCallError("niScope_FetchDispatcher", param='wfmInfo')
        test_value = self._defaults['FetchDispatcher']['wfmInfo']
        try:
            wfm_info_ref = wfm_info.contents
        except AttributeError:
            wfm_info_ref = wfm_info
        assert len(wfm_info_ref) >= len(test_value)
        for i in range(len(test_value)):
            wfm_info_ref[i] = test_value[i]
        return self._defaults['FetchDispatcher']['return']

    def niScope_FetchMeasurement(self, vi, channel_list, timeout, scalar_meas_function, result):  # noqa: N802
        if self._defaults['FetchMeasurement']['return'] != 0:
            return self._defaults['FetchMeasurement']['return']
        # result
        if self._defaults['FetchMeasurement']['Result'] is None:
            raise MockFunctionCallError("niScope_FetchMeasurement", param='Result')
        test_value = self._defaults['FetchMeasurement']['Result']
        try:
            result_ref = result.contents
        except AttributeError:
            result_ref = result
        assert len(result_ref) >= len(test_value)
        for i in range(len(test_value)):
            result_ref[i] = test_value[i]
        return self._defaults['FetchMeasurement']['return']

    def niScope_FetchMeasurementStats(self, vi, channel_list, timeout, scalar_meas_function, result, mean, stdev, min, max, num_in_stats):  # noqa: N802
        if self._defaults['FetchMeasurementStats']['return'] != 0:
            return self._defaults['FetchMeasurementStats']['return']
        # result
        if self._defaults['FetchMeasurementStats']['Result'] is None:
            raise MockFunctionCallError("niScope_FetchMeasurementStats", param='Result')
        test_value = self._defaults['FetchMeasurementStats']['Result']
        try:
            result_ref = result.contents
        except AttributeError:
            result_ref = result
        assert len(result_ref) >= len(test_value)
        for i in range(len(test_value)):
            result_ref[i] = test_value[i]
        # mean
        if self._defaults['FetchMeasurementStats']['Mean'] is None:
            raise MockFunctionCallError("niScope_FetchMeasurementStats", param='Mean')
        test_value = self._defaults['FetchMeasurementStats']['Mean']
        try:
            mean_ref = mean.contents
        except AttributeError:
            mean_ref = mean
        assert len(mean_ref) >= len(test_value)
        for i in range(len(test_value)):
            mean_ref[i] = test_value[i]
        # stdev
        if self._defaults['FetchMeasurementStats']['Stdev'] is None:
            raise MockFunctionCallError("niScope_FetchMeasurementStats", param='Stdev')
        test_value = self._defaults['FetchMeasurementStats']['Stdev']
        try:
            stdev_ref = stdev.contents
        except AttributeError:
            stdev_ref = stdev
        assert len(stdev_ref) >= len(test_value)
        for i in range(len(test_value)):
            stdev_ref[i] = test_value[i]
        # min
        if self._defaults['FetchMeasurementStats']['Min'] is None:
            raise MockFunctionCallError("niScope_FetchMeasurementStats", param='Min')
        test_value = self._defaults['FetchMeasurementStats']['Min']
        try:
            min_ref = min.contents
        except AttributeError:
            min_ref = min
        assert len(min_ref) >= len(test_value)
        for i in range(len(test_value)):
            min_ref[i] = test_value[i]
        # max
        if self._defaults['FetchMeasurementStats']['Max'] is None:
            raise MockFunctionCallError("niScope_FetchMeasurementStats", param='Max')
        test_value = self._defaults['FetchMeasurementStats']['Max']
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
        if self._defaults['GetAttributeViBoolean']['Value'] is None:
            raise MockFunctionCallError("niScope_GetAttributeViBoolean", param='Value')
        value.contents.value = self._defaults['GetAttributeViBoolean']['Value']
        return self._defaults['GetAttributeViBoolean']['return']

    def niScope_GetAttributeViInt32(self, vi, channel_list, attribute_id, value):  # noqa: N802
        if self._defaults['GetAttributeViInt32']['return'] != 0:
            return self._defaults['GetAttributeViInt32']['return']
        # value
        if self._defaults['GetAttributeViInt32']['Value'] is None:
            raise MockFunctionCallError("niScope_GetAttributeViInt32", param='Value')
        value.contents.value = self._defaults['GetAttributeViInt32']['Value']
        return self._defaults['GetAttributeViInt32']['return']

    def niScope_GetAttributeViReal64(self, vi, channel_list, attribute_id, value):  # noqa: N802
        if self._defaults['GetAttributeViReal64']['return'] != 0:
            return self._defaults['GetAttributeViReal64']['return']
        # value
        if self._defaults['GetAttributeViReal64']['Value'] is None:
            raise MockFunctionCallError("niScope_GetAttributeViReal64", param='Value')
        value.contents.value = self._defaults['GetAttributeViReal64']['Value']
        return self._defaults['GetAttributeViReal64']['return']

    def niScope_GetAttributeViString(self, vi, channel_list, attribute_id, buf_size, value):  # noqa: N802
        if self._defaults['GetAttributeViString']['return'] != 0:
            return self._defaults['GetAttributeViString']['return']
        if self._defaults['GetAttributeViString']['Value'] is None:
            raise MockFunctionCallError("niScope_GetAttributeViString", param='Value')
        if buf_size.value == 0:
            return len(self._defaults['GetAttributeViString']['Value'])
        value.value = self._defaults['GetAttributeViString']['Value'].encode('ascii')
        return self._defaults['GetAttributeViString']['return']

    def niScope_GetEqualizationFilterCoefficients(self, vi, channel, number_of_coefficients, coefficients):  # noqa: N802
        if self._defaults['GetEqualizationFilterCoefficients']['return'] != 0:
            return self._defaults['GetEqualizationFilterCoefficients']['return']
        # coefficients
        if self._defaults['GetEqualizationFilterCoefficients']['Coefficients'] is None:
            raise MockFunctionCallError("niScope_GetEqualizationFilterCoefficients", param='Coefficients')
        test_value = self._defaults['GetEqualizationFilterCoefficients']['Coefficients']
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
        error_code.contents.value = self._defaults['GetError']['errorCode']
        if self._defaults['GetError']['Description'] is None:
            raise MockFunctionCallError("niScope_GetError", param='Description')
        if buffer_size.value == 0:
            return len(self._defaults['GetError']['Description'])
        description.value = self._defaults['GetError']['Description'].encode('ascii')
        return self._defaults['GetError']['return']

    def niScope_InitWithOptions(self, resource_name, id_query, reset_device, option_string, vi):  # noqa: N802
        if self._defaults['InitWithOptions']['return'] != 0:
            return self._defaults['InitWithOptions']['return']
        # vi
        if self._defaults['InitWithOptions']['vi'] is None:
            raise MockFunctionCallError("niScope_InitWithOptions", param='vi')
        vi.contents.value = self._defaults['InitWithOptions']['vi']
        return self._defaults['InitWithOptions']['return']

    def niScope_InitiateAcquisition(self, vi):  # noqa: N802
        if self._defaults['InitiateAcquisition']['return'] != 0:
            return self._defaults['InitiateAcquisition']['return']
        return self._defaults['InitiateAcquisition']['return']

    def niScope_ProbeCompensationSignalStart(self, vi):  # noqa: N802
        if self._defaults['ProbeCompensationSignalStart']['return'] != 0:
            return self._defaults['ProbeCompensationSignalStart']['return']
        return self._defaults['ProbeCompensationSignalStart']['return']

    def niScope_ProbeCompensationSignalStop(self, vi):  # noqa: N802
        if self._defaults['ProbeCompensationSignalStop']['return'] != 0:
            return self._defaults['ProbeCompensationSignalStop']['return']
        return self._defaults['ProbeCompensationSignalStop']['return']

    def niScope_Read(self, vi, channel_list, timeout, num_samples, wfm, wfm_info):  # noqa: N802
        if self._defaults['Read']['return'] != 0:
            return self._defaults['Read']['return']
        # wfm
        if self._defaults['Read']['Wfm'] is None:
            raise MockFunctionCallError("niScope_Read", param='Wfm')
        test_value = self._defaults['Read']['Wfm']
        try:
            wfm_ref = wfm.contents
        except AttributeError:
            wfm_ref = wfm
        assert len(wfm_ref) >= len(test_value)
        for i in range(len(test_value)):
            wfm_ref[i] = test_value[i]
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

    def niScope_ReadMeasurement(self, vi, channel_list, timeout, scalar_meas_function, result):  # noqa: N802
        if self._defaults['ReadMeasurement']['return'] != 0:
            return self._defaults['ReadMeasurement']['return']
        # result
        if self._defaults['ReadMeasurement']['Result'] is None:
            raise MockFunctionCallError("niScope_ReadMeasurement", param='Result')
        test_value = self._defaults['ReadMeasurement']['Result']
        try:
            result_ref = result.contents
        except AttributeError:
            result_ref = result
        assert len(result_ref) >= len(test_value)
        for i in range(len(test_value)):
            result_ref[i] = test_value[i]
        return self._defaults['ReadMeasurement']['return']

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

    def niScope_SetAttributeViReal64(self, vi, channel_list, attribute_id, value):  # noqa: N802
        if self._defaults['SetAttributeViReal64']['return'] != 0:
            return self._defaults['SetAttributeViReal64']['return']
        return self._defaults['SetAttributeViReal64']['return']

    def niScope_SetAttributeViString(self, vi, channel_list, attribute_id, value):  # noqa: N802
        if self._defaults['SetAttributeViString']['return'] != 0:
            return self._defaults['SetAttributeViString']['return']
        return self._defaults['SetAttributeViString']['return']

    def niScope_close(self, vi):  # noqa: N802
        if self._defaults['close']['return'] != 0:
            return self._defaults['close']['return']
        return self._defaults['close']['return']

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
        self_test_result.contents.value = self._defaults['self_test']['selfTestResult']
        # self_test_message
        if self._defaults['self_test']['selfTestMessage'] is None:
            raise MockFunctionCallError("niScope_self_test", param='selfTestMessage')
        test_value = self._defaults['self_test']['selfTestMessage']
        if sys.version_info.major > 2 and type(test_value) is str:
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
        mock_library.niScope_ActualNumWfms.side_effect = MockFunctionCallError("niScope_ActualNumWfms")
        mock_library.niScope_ActualNumWfms.return_value = 0
        mock_library.niScope_AutoSetup.side_effect = MockFunctionCallError("niScope_AutoSetup")
        mock_library.niScope_AutoSetup.return_value = 0
        mock_library.niScope_CalSelfCalibrate.side_effect = MockFunctionCallError("niScope_CalSelfCalibrate")
        mock_library.niScope_CalSelfCalibrate.return_value = 0
        mock_library.niScope_ClearWaveformMeasurementStats.side_effect = MockFunctionCallError("niScope_ClearWaveformMeasurementStats")
        mock_library.niScope_ClearWaveformMeasurementStats.return_value = 0
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
        mock_library.niScope_ExportSignal.side_effect = MockFunctionCallError("niScope_ExportSignal")
        mock_library.niScope_ExportSignal.return_value = 0
        mock_library.niScope_FancyFetch.side_effect = MockFunctionCallError("niScope_FancyFetch")
        mock_library.niScope_FancyFetch.return_value = 0
        mock_library.niScope_Fetch.side_effect = MockFunctionCallError("niScope_Fetch")
        mock_library.niScope_Fetch.return_value = 0
        mock_library.niScope_FetchBinary16.side_effect = MockFunctionCallError("niScope_FetchBinary16")
        mock_library.niScope_FetchBinary16.return_value = 0
        mock_library.niScope_FetchBinary32.side_effect = MockFunctionCallError("niScope_FetchBinary32")
        mock_library.niScope_FetchBinary32.return_value = 0
        mock_library.niScope_FetchBinary8.side_effect = MockFunctionCallError("niScope_FetchBinary8")
        mock_library.niScope_FetchBinary8.return_value = 0
        mock_library.niScope_FetchDispatcher.side_effect = MockFunctionCallError("niScope_FetchDispatcher")
        mock_library.niScope_FetchDispatcher.return_value = 0
        mock_library.niScope_FetchMeasurement.side_effect = MockFunctionCallError("niScope_FetchMeasurement")
        mock_library.niScope_FetchMeasurement.return_value = 0
        mock_library.niScope_FetchMeasurementStats.side_effect = MockFunctionCallError("niScope_FetchMeasurementStats")
        mock_library.niScope_FetchMeasurementStats.return_value = 0
        mock_library.niScope_GetAttributeViBoolean.side_effect = MockFunctionCallError("niScope_GetAttributeViBoolean")
        mock_library.niScope_GetAttributeViBoolean.return_value = 0
        mock_library.niScope_GetAttributeViInt32.side_effect = MockFunctionCallError("niScope_GetAttributeViInt32")
        mock_library.niScope_GetAttributeViInt32.return_value = 0
        mock_library.niScope_GetAttributeViReal64.side_effect = MockFunctionCallError("niScope_GetAttributeViReal64")
        mock_library.niScope_GetAttributeViReal64.return_value = 0
        mock_library.niScope_GetAttributeViString.side_effect = MockFunctionCallError("niScope_GetAttributeViString")
        mock_library.niScope_GetAttributeViString.return_value = 0
        mock_library.niScope_GetEqualizationFilterCoefficients.side_effect = MockFunctionCallError("niScope_GetEqualizationFilterCoefficients")
        mock_library.niScope_GetEqualizationFilterCoefficients.return_value = 0
        mock_library.niScope_GetError.side_effect = MockFunctionCallError("niScope_GetError")
        mock_library.niScope_GetError.return_value = 0
        mock_library.niScope_InitWithOptions.side_effect = MockFunctionCallError("niScope_InitWithOptions")
        mock_library.niScope_InitWithOptions.return_value = 0
        mock_library.niScope_InitiateAcquisition.side_effect = MockFunctionCallError("niScope_InitiateAcquisition")
        mock_library.niScope_InitiateAcquisition.return_value = 0
        mock_library.niScope_ProbeCompensationSignalStart.side_effect = MockFunctionCallError("niScope_ProbeCompensationSignalStart")
        mock_library.niScope_ProbeCompensationSignalStart.return_value = 0
        mock_library.niScope_ProbeCompensationSignalStop.side_effect = MockFunctionCallError("niScope_ProbeCompensationSignalStop")
        mock_library.niScope_ProbeCompensationSignalStop.return_value = 0
        mock_library.niScope_Read.side_effect = MockFunctionCallError("niScope_Read")
        mock_library.niScope_Read.return_value = 0
        mock_library.niScope_ReadMeasurement.side_effect = MockFunctionCallError("niScope_ReadMeasurement")
        mock_library.niScope_ReadMeasurement.return_value = 0
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
        mock_library.niScope_SetAttributeViReal64.side_effect = MockFunctionCallError("niScope_SetAttributeViReal64")
        mock_library.niScope_SetAttributeViReal64.return_value = 0
        mock_library.niScope_SetAttributeViString.side_effect = MockFunctionCallError("niScope_SetAttributeViString")
        mock_library.niScope_SetAttributeViString.return_value = 0
        mock_library.niScope_close.side_effect = MockFunctionCallError("niScope_close")
        mock_library.niScope_close.return_value = 0
        mock_library.niScope_reset.side_effect = MockFunctionCallError("niScope_reset")
        mock_library.niScope_reset.return_value = 0
        mock_library.niScope_self_test.side_effect = MockFunctionCallError("niScope_self_test")
        mock_library.niScope_self_test.return_value = 0
