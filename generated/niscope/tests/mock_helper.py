# This file was generated


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
        self._defaults['ActualRecordLength'] = {}
        self._defaults['ActualRecordLength']['return'] = 0
        self._defaults['ActualRecordLength']['recordLength'] = None
        self._defaults['AddWaveformProcessing'] = {}
        self._defaults['AddWaveformProcessing']['return'] = 0
        self._defaults['AdjustSampleClockRelativeDelay'] = {}
        self._defaults['AdjustSampleClockRelativeDelay']['return'] = 0
        self._defaults['AutoSetup'] = {}
        self._defaults['AutoSetup']['return'] = 0
        self._defaults['CalSelfCalibrate'] = {}
        self._defaults['CalSelfCalibrate']['return'] = 0
        self._defaults['CheckAttributeViBoolean'] = {}
        self._defaults['CheckAttributeViBoolean']['return'] = 0
        self._defaults['CheckAttributeViInt32'] = {}
        self._defaults['CheckAttributeViInt32']['return'] = 0
        self._defaults['CheckAttributeViInt64'] = {}
        self._defaults['CheckAttributeViInt64']['return'] = 0
        self._defaults['CheckAttributeViReal64'] = {}
        self._defaults['CheckAttributeViReal64']['return'] = 0
        self._defaults['CheckAttributeViSession'] = {}
        self._defaults['CheckAttributeViSession']['return'] = 0
        self._defaults['CheckAttributeViString'] = {}
        self._defaults['CheckAttributeViString']['return'] = 0
        self._defaults['ClearWaveformMeasurementStats'] = {}
        self._defaults['ClearWaveformMeasurementStats']['return'] = 0
        self._defaults['ClearWaveformProcessing'] = {}
        self._defaults['ClearWaveformProcessing']['return'] = 0
        self._defaults['Commit'] = {}
        self._defaults['Commit']['return'] = 0
        self._defaults['ConfigureAcquisition'] = {}
        self._defaults['ConfigureAcquisition']['return'] = 0
        self._defaults['ConfigureAcquisitionRecord'] = {}
        self._defaults['ConfigureAcquisitionRecord']['return'] = 0
        self._defaults['ConfigureChanCharacteristics'] = {}
        self._defaults['ConfigureChanCharacteristics']['return'] = 0
        self._defaults['ConfigureChannel'] = {}
        self._defaults['ConfigureChannel']['return'] = 0
        self._defaults['ConfigureClock'] = {}
        self._defaults['ConfigureClock']['return'] = 0
        self._defaults['ConfigureEdgeTriggerSource'] = {}
        self._defaults['ConfigureEdgeTriggerSource']['return'] = 0
        self._defaults['ConfigureEqualizationFilterCoefficients'] = {}
        self._defaults['ConfigureEqualizationFilterCoefficients']['return'] = 0
        self._defaults['ConfigureHorizontalTiming'] = {}
        self._defaults['ConfigureHorizontalTiming']['return'] = 0
        self._defaults['ConfigureRefLevels'] = {}
        self._defaults['ConfigureRefLevels']['return'] = 0
        self._defaults['ConfigureTVTriggerLineNumber'] = {}
        self._defaults['ConfigureTVTriggerLineNumber']['return'] = 0
        self._defaults['ConfigureTVTriggerSource'] = {}
        self._defaults['ConfigureTVTriggerSource']['return'] = 0
        self._defaults['ConfigureTrigger'] = {}
        self._defaults['ConfigureTrigger']['return'] = 0
        self._defaults['ConfigureTriggerCoupling'] = {}
        self._defaults['ConfigureTriggerCoupling']['return'] = 0
        self._defaults['ConfigureTriggerDigital'] = {}
        self._defaults['ConfigureTriggerDigital']['return'] = 0
        self._defaults['ConfigureTriggerEdge'] = {}
        self._defaults['ConfigureTriggerEdge']['return'] = 0
        self._defaults['ConfigureTriggerHysteresis'] = {}
        self._defaults['ConfigureTriggerHysteresis']['return'] = 0
        self._defaults['ConfigureTriggerImmediate'] = {}
        self._defaults['ConfigureTriggerImmediate']['return'] = 0
        self._defaults['ConfigureTriggerOutput'] = {}
        self._defaults['ConfigureTriggerOutput']['return'] = 0
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
        self._defaults['FetchWaveform'] = {}
        self._defaults['FetchWaveform']['return'] = 0
        self._defaults['FetchWaveform']['Waveform'] = None
        self._defaults['FetchWaveform']['actualPoints'] = None
        self._defaults['FetchWaveform']['initialX'] = None
        self._defaults['FetchWaveform']['xIncrement'] = None
        self._defaults['FetchWaveformMeasurement'] = {}
        self._defaults['FetchWaveformMeasurement']['return'] = 0
        self._defaults['FetchWaveformMeasurement']['Measurement'] = None
        self._defaults['GetAttributeViBoolean'] = {}
        self._defaults['GetAttributeViBoolean']['return'] = 0
        self._defaults['GetAttributeViBoolean']['Value'] = None
        self._defaults['GetAttributeViInt32'] = {}
        self._defaults['GetAttributeViInt32']['return'] = 0
        self._defaults['GetAttributeViInt32']['Value'] = None
        self._defaults['GetAttributeViInt64'] = {}
        self._defaults['GetAttributeViInt64']['return'] = 0
        self._defaults['GetAttributeViInt64']['Value'] = None
        self._defaults['GetAttributeViReal64'] = {}
        self._defaults['GetAttributeViReal64']['return'] = 0
        self._defaults['GetAttributeViReal64']['Value'] = None
        self._defaults['GetAttributeViString'] = {}
        self._defaults['GetAttributeViString']['return'] = 0
        self._defaults['GetAttributeViString']['Value'] = None
        self._defaults['GetChannelName'] = {}
        self._defaults['GetChannelName']['return'] = 0
        self._defaults['GetChannelName']['channelString'] = None
        self._defaults['GetEqualizationFilterCoefficients'] = {}
        self._defaults['GetEqualizationFilterCoefficients']['return'] = 0
        self._defaults['GetEqualizationFilterCoefficients']['Coefficients'] = None
        self._defaults['GetError'] = {}
        self._defaults['GetError']['return'] = 0
        self._defaults['GetError']['errorCode'] = None
        self._defaults['GetError']['Description'] = None
        self._defaults['GetErrorMessage'] = {}
        self._defaults['GetErrorMessage']['return'] = 0
        self._defaults['GetErrorMessage']['errorMessage'] = None
        self._defaults['GetFrequencyResponse'] = {}
        self._defaults['GetFrequencyResponse']['return'] = 0
        self._defaults['GetFrequencyResponse']['numberOfFrequencies'] = None
        self._defaults['GetStreamEndpointHandle'] = {}
        self._defaults['GetStreamEndpointHandle']['return'] = 0
        self._defaults['GetStreamEndpointHandle']['writerHandle'] = None
        self._defaults['InitWithOptions'] = {}
        self._defaults['InitWithOptions']['return'] = 0
        self._defaults['InitWithOptions']['vi'] = None
        self._defaults['InitiateAcquisition'] = {}
        self._defaults['InitiateAcquisition']['return'] = 0
        self._defaults['IsDeviceReady'] = {}
        self._defaults['IsDeviceReady']['return'] = 0
        self._defaults['IsDeviceReady']['deviceReady'] = None
        self._defaults['IsInvalidWfmElement'] = {}
        self._defaults['IsInvalidWfmElement']['return'] = 0
        self._defaults['IsInvalidWfmElement']['isInvalid'] = None
        self._defaults['ProbeCompensationSignalStart'] = {}
        self._defaults['ProbeCompensationSignalStart']['return'] = 0
        self._defaults['ProbeCompensationSignalStop'] = {}
        self._defaults['ProbeCompensationSignalStop']['return'] = 0
        self._defaults['ReadMeasurement'] = {}
        self._defaults['ReadMeasurement']['return'] = 0
        self._defaults['ReadMeasurement']['Result'] = None
        self._defaults['ReadWaveform'] = {}
        self._defaults['ReadWaveform']['return'] = 0
        self._defaults['ReadWaveform']['Waveform'] = None
        self._defaults['ReadWaveform']['actualPoints'] = None
        self._defaults['ReadWaveform']['initialX'] = None
        self._defaults['ReadWaveform']['xIncrement'] = None
        self._defaults['ReadWaveformMeasurement'] = {}
        self._defaults['ReadWaveformMeasurement']['return'] = 0
        self._defaults['ReadWaveformMeasurement']['Measurement'] = None
        self._defaults['ResetDevice'] = {}
        self._defaults['ResetDevice']['return'] = 0
        self._defaults['ResetWithDefaults'] = {}
        self._defaults['ResetWithDefaults']['return'] = 0
        self._defaults['SampleMode'] = {}
        self._defaults['SampleMode']['return'] = 0
        self._defaults['SampleMode']['sampleMode'] = None
        self._defaults['SampleRate'] = {}
        self._defaults['SampleRate']['return'] = 0
        self._defaults['SampleRate']['sampleRate'] = None
        self._defaults['SendSWTrigger'] = {}
        self._defaults['SendSWTrigger']['return'] = 0
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
        self._defaults['close'] = {}
        self._defaults['close']['return'] = 0
        self._defaults['errorHandler'] = {}
        self._defaults['errorHandler']['return'] = 0
        self._defaults['errorHandler']['errorSource'] = None
        self._defaults['errorHandler']['errorDescription'] = None
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
        if self._defaults['AcquisitionStatus']['acquisitionStatus'] is None:
            raise MockFunctionCallError("niScope_AcquisitionStatus", param='acquisitionStatus')
        acquisition_status.contents.value = self._defaults['AcquisitionStatus']['acquisitionStatus']
        return self._defaults['AcquisitionStatus']['return']

    def niScope_ActualMeasWfmSize(self, vi, array_meas_function, meas_waveform_size):  # noqa: N802
        if self._defaults['ActualMeasWfmSize']['return'] != 0:
            return self._defaults['ActualMeasWfmSize']['return']
        if self._defaults['ActualMeasWfmSize']['measWaveformSize'] is None:
            raise MockFunctionCallError("niScope_ActualMeasWfmSize", param='measWaveformSize')
        meas_waveform_size.contents.value = self._defaults['ActualMeasWfmSize']['measWaveformSize']
        return self._defaults['ActualMeasWfmSize']['return']

    def niScope_ActualNumWfms(self, vi, channel_list, num_wfms):  # noqa: N802
        if self._defaults['ActualNumWfms']['return'] != 0:
            return self._defaults['ActualNumWfms']['return']
        if self._defaults['ActualNumWfms']['numWfms'] is None:
            raise MockFunctionCallError("niScope_ActualNumWfms", param='numWfms')
        num_wfms.contents.value = self._defaults['ActualNumWfms']['numWfms']
        return self._defaults['ActualNumWfms']['return']

    def niScope_ActualRecordLength(self, vi, record_length):  # noqa: N802
        if self._defaults['ActualRecordLength']['return'] != 0:
            return self._defaults['ActualRecordLength']['return']
        if self._defaults['ActualRecordLength']['recordLength'] is None:
            raise MockFunctionCallError("niScope_ActualRecordLength", param='recordLength')
        record_length.contents.value = self._defaults['ActualRecordLength']['recordLength']
        return self._defaults['ActualRecordLength']['return']

    def niScope_AddWaveformProcessing(self, vi, channel_list, meas_function):  # noqa: N802
        if self._defaults['AddWaveformProcessing']['return'] != 0:
            return self._defaults['AddWaveformProcessing']['return']
        return self._defaults['AddWaveformProcessing']['return']

    def niScope_AdjustSampleClockRelativeDelay(self, vi, delay):  # noqa: N802
        if self._defaults['AdjustSampleClockRelativeDelay']['return'] != 0:
            return self._defaults['AdjustSampleClockRelativeDelay']['return']
        return self._defaults['AdjustSampleClockRelativeDelay']['return']

    def niScope_AutoSetup(self, vi):  # noqa: N802
        if self._defaults['AutoSetup']['return'] != 0:
            return self._defaults['AutoSetup']['return']
        return self._defaults['AutoSetup']['return']

    def niScope_CalSelfCalibrate(self, vi, channel_list, option):  # noqa: N802
        if self._defaults['CalSelfCalibrate']['return'] != 0:
            return self._defaults['CalSelfCalibrate']['return']
        return self._defaults['CalSelfCalibrate']['return']

    def niScope_CheckAttributeViBoolean(self, vi, channel_list, attribute_id, value):  # noqa: N802
        if self._defaults['CheckAttributeViBoolean']['return'] != 0:
            return self._defaults['CheckAttributeViBoolean']['return']
        return self._defaults['CheckAttributeViBoolean']['return']

    def niScope_CheckAttributeViInt32(self, vi, channel_list, attribute_id, value):  # noqa: N802
        if self._defaults['CheckAttributeViInt32']['return'] != 0:
            return self._defaults['CheckAttributeViInt32']['return']
        return self._defaults['CheckAttributeViInt32']['return']

    def niScope_CheckAttributeViInt64(self, vi, channel_list, attribute_id, value):  # noqa: N802
        if self._defaults['CheckAttributeViInt64']['return'] != 0:
            return self._defaults['CheckAttributeViInt64']['return']
        return self._defaults['CheckAttributeViInt64']['return']

    def niScope_CheckAttributeViReal64(self, vi, channel_list, attribute_id, value):  # noqa: N802
        if self._defaults['CheckAttributeViReal64']['return'] != 0:
            return self._defaults['CheckAttributeViReal64']['return']
        return self._defaults['CheckAttributeViReal64']['return']

    def niScope_CheckAttributeViSession(self, vi, channel_list, attribute_id, value):  # noqa: N802
        if self._defaults['CheckAttributeViSession']['return'] != 0:
            return self._defaults['CheckAttributeViSession']['return']
        return self._defaults['CheckAttributeViSession']['return']

    def niScope_CheckAttributeViString(self, vi, channel_list, attribute_id, value):  # noqa: N802
        if self._defaults['CheckAttributeViString']['return'] != 0:
            return self._defaults['CheckAttributeViString']['return']
        return self._defaults['CheckAttributeViString']['return']

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

    def niScope_ConfigureAcquisition(self, vi, acquisition_type):  # noqa: N802
        if self._defaults['ConfigureAcquisition']['return'] != 0:
            return self._defaults['ConfigureAcquisition']['return']
        return self._defaults['ConfigureAcquisition']['return']

    def niScope_ConfigureAcquisitionRecord(self, vi, time_per_record, min_num_points, acquisition_start_time):  # noqa: N802
        if self._defaults['ConfigureAcquisitionRecord']['return'] != 0:
            return self._defaults['ConfigureAcquisitionRecord']['return']
        return self._defaults['ConfigureAcquisitionRecord']['return']

    def niScope_ConfigureChanCharacteristics(self, vi, channel_list, input_impedance, max_input_frequency):  # noqa: N802
        if self._defaults['ConfigureChanCharacteristics']['return'] != 0:
            return self._defaults['ConfigureChanCharacteristics']['return']
        return self._defaults['ConfigureChanCharacteristics']['return']

    def niScope_ConfigureChannel(self, vi, channel, range, offset, coupling, probe_attenuation, enabled):  # noqa: N802
        if self._defaults['ConfigureChannel']['return'] != 0:
            return self._defaults['ConfigureChannel']['return']
        return self._defaults['ConfigureChannel']['return']

    def niScope_ConfigureClock(self, vi, input_clock_source, output_clock_source, clock_sync_pulse_source, master_enabled):  # noqa: N802
        if self._defaults['ConfigureClock']['return'] != 0:
            return self._defaults['ConfigureClock']['return']
        return self._defaults['ConfigureClock']['return']

    def niScope_ConfigureEdgeTriggerSource(self, vi, source, level, slope):  # noqa: N802
        if self._defaults['ConfigureEdgeTriggerSource']['return'] != 0:
            return self._defaults['ConfigureEdgeTriggerSource']['return']
        return self._defaults['ConfigureEdgeTriggerSource']['return']

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

    def niScope_ConfigureTVTriggerLineNumber(self, vi, line_number):  # noqa: N802
        if self._defaults['ConfigureTVTriggerLineNumber']['return'] != 0:
            return self._defaults['ConfigureTVTriggerLineNumber']['return']
        return self._defaults['ConfigureTVTriggerLineNumber']['return']

    def niScope_ConfigureTVTriggerSource(self, vi, source, signal_format, event, polarity):  # noqa: N802
        if self._defaults['ConfigureTVTriggerSource']['return'] != 0:
            return self._defaults['ConfigureTVTriggerSource']['return']
        return self._defaults['ConfigureTVTriggerSource']['return']

    def niScope_ConfigureTrigger(self, vi, trigger_type, holdoff):  # noqa: N802
        if self._defaults['ConfigureTrigger']['return'] != 0:
            return self._defaults['ConfigureTrigger']['return']
        return self._defaults['ConfigureTrigger']['return']

    def niScope_ConfigureTriggerCoupling(self, vi, coupling):  # noqa: N802
        if self._defaults['ConfigureTriggerCoupling']['return'] != 0:
            return self._defaults['ConfigureTriggerCoupling']['return']
        return self._defaults['ConfigureTriggerCoupling']['return']

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

    def niScope_ConfigureTriggerOutput(self, vi, trigger_event, trigger_output):  # noqa: N802
        if self._defaults['ConfigureTriggerOutput']['return'] != 0:
            return self._defaults['ConfigureTriggerOutput']['return']
        return self._defaults['ConfigureTriggerOutput']['return']

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

    def niScope_FetchMeasurement(self, vi, channel_list, timeout, scalar_meas_function, result):  # noqa: N802
        if self._defaults['FetchMeasurement']['return'] != 0:
            return self._defaults['FetchMeasurement']['return']
        if self._defaults['FetchMeasurement']['Result'] is None:
            raise MockFunctionCallError("niScope_FetchMeasurement", param='Result')
        a = self._defaults['FetchMeasurement']['Result']
        import sys
        if sys.version_info.major > 2 and type(a) is str:
            a = a.encode('ascii')
        for i in range(min(len(result), len(a))):
            result[i] = a[i]
        return self._defaults['FetchMeasurement']['return']

    def niScope_FetchMeasurementStats(self, vi, channel_list, timeout, scalar_meas_function, result, mean, stdev, min, max, num_in_stats):  # noqa: N802
        if self._defaults['FetchMeasurementStats']['return'] != 0:
            return self._defaults['FetchMeasurementStats']['return']
        if self._defaults['FetchMeasurementStats']['Result'] is None:
            raise MockFunctionCallError("niScope_FetchMeasurementStats", param='Result')
        a = self._defaults['FetchMeasurementStats']['Result']
        import sys
        if sys.version_info.major > 2 and type(a) is str:
            a = a.encode('ascii')
        for i in range(min(len(result), len(a))):
            result[i] = a[i]
        if self._defaults['FetchMeasurementStats']['Mean'] is None:
            raise MockFunctionCallError("niScope_FetchMeasurementStats", param='Mean')
        a = self._defaults['FetchMeasurementStats']['Mean']
        import sys
        if sys.version_info.major > 2 and type(a) is str:
            a = a.encode('ascii')
        for i in range(min(len(mean), len(a))):
            mean[i] = a[i]
        if self._defaults['FetchMeasurementStats']['Stdev'] is None:
            raise MockFunctionCallError("niScope_FetchMeasurementStats", param='Stdev')
        a = self._defaults['FetchMeasurementStats']['Stdev']
        import sys
        if sys.version_info.major > 2 and type(a) is str:
            a = a.encode('ascii')
        for i in range(min(len(stdev), len(a))):
            stdev[i] = a[i]
        if self._defaults['FetchMeasurementStats']['Min'] is None:
            raise MockFunctionCallError("niScope_FetchMeasurementStats", param='Min')
        a = self._defaults['FetchMeasurementStats']['Min']
        import sys
        if sys.version_info.major > 2 and type(a) is str:
            a = a.encode('ascii')
        for i in range(min(len(min), len(a))):
            min[i] = a[i]
        if self._defaults['FetchMeasurementStats']['Max'] is None:
            raise MockFunctionCallError("niScope_FetchMeasurementStats", param='Max')
        a = self._defaults['FetchMeasurementStats']['Max']
        import sys
        if sys.version_info.major > 2 and type(a) is str:
            a = a.encode('ascii')
        for i in range(min(len(max), len(a))):
            max[i] = a[i]
        if self._defaults['FetchMeasurementStats']['numInStats'] is None:
            raise MockFunctionCallError("niScope_FetchMeasurementStats", param='numInStats')
        a = self._defaults['FetchMeasurementStats']['numInStats']
        import sys
        if sys.version_info.major > 2 and type(a) is str:
            a = a.encode('ascii')
        for i in range(min(len(num_in_stats), len(a))):
            num_in_stats[i] = a[i]
        return self._defaults['FetchMeasurementStats']['return']

    def niScope_FetchWaveform(self, vi, channel, waveform_size, waveform, actual_points, initial_x, x_increment):  # noqa: N802
        if self._defaults['FetchWaveform']['return'] != 0:
            return self._defaults['FetchWaveform']['return']
        if self._defaults['FetchWaveform']['Waveform'] is None:
            raise MockFunctionCallError("niScope_FetchWaveform", param='Waveform')
        a = self._defaults['FetchWaveform']['Waveform']
        import sys
        if sys.version_info.major > 2 and type(a) is str:
            a = a.encode('ascii')
        for i in range(min(len(waveform), len(a))):
            waveform[i] = a[i]
        if self._defaults['FetchWaveform']['actualPoints'] is None:
            raise MockFunctionCallError("niScope_FetchWaveform", param='actualPoints')
        actual_points.contents.value = self._defaults['FetchWaveform']['actualPoints']
        if self._defaults['FetchWaveform']['initialX'] is None:
            raise MockFunctionCallError("niScope_FetchWaveform", param='initialX')
        initial_x.contents.value = self._defaults['FetchWaveform']['initialX']
        if self._defaults['FetchWaveform']['xIncrement'] is None:
            raise MockFunctionCallError("niScope_FetchWaveform", param='xIncrement')
        x_increment.contents.value = self._defaults['FetchWaveform']['xIncrement']
        return self._defaults['FetchWaveform']['return']

    def niScope_FetchWaveformMeasurement(self, vi, channel, meas_function, measurement):  # noqa: N802
        if self._defaults['FetchWaveformMeasurement']['return'] != 0:
            return self._defaults['FetchWaveformMeasurement']['return']
        if self._defaults['FetchWaveformMeasurement']['Measurement'] is None:
            raise MockFunctionCallError("niScope_FetchWaveformMeasurement", param='Measurement')
        measurement.contents.value = self._defaults['FetchWaveformMeasurement']['Measurement']
        return self._defaults['FetchWaveformMeasurement']['return']

    def niScope_GetAttributeViBoolean(self, vi, channel_list, attribute_id, value):  # noqa: N802
        if self._defaults['GetAttributeViBoolean']['return'] != 0:
            return self._defaults['GetAttributeViBoolean']['return']
        if self._defaults['GetAttributeViBoolean']['Value'] is None:
            raise MockFunctionCallError("niScope_GetAttributeViBoolean", param='Value')
        value.contents.value = self._defaults['GetAttributeViBoolean']['Value']
        return self._defaults['GetAttributeViBoolean']['return']

    def niScope_GetAttributeViInt32(self, vi, channel_list, attribute_id, value):  # noqa: N802
        if self._defaults['GetAttributeViInt32']['return'] != 0:
            return self._defaults['GetAttributeViInt32']['return']
        if self._defaults['GetAttributeViInt32']['Value'] is None:
            raise MockFunctionCallError("niScope_GetAttributeViInt32", param='Value')
        value.contents.value = self._defaults['GetAttributeViInt32']['Value']
        return self._defaults['GetAttributeViInt32']['return']

    def niScope_GetAttributeViInt64(self, vi, channel_list, attribute_id, value):  # noqa: N802
        if self._defaults['GetAttributeViInt64']['return'] != 0:
            return self._defaults['GetAttributeViInt64']['return']
        if self._defaults['GetAttributeViInt64']['Value'] is None:
            raise MockFunctionCallError("niScope_GetAttributeViInt64", param='Value')
        value.contents.value = self._defaults['GetAttributeViInt64']['Value']
        return self._defaults['GetAttributeViInt64']['return']

    def niScope_GetAttributeViReal64(self, vi, channel_list, attribute_id, value):  # noqa: N802
        if self._defaults['GetAttributeViReal64']['return'] != 0:
            return self._defaults['GetAttributeViReal64']['return']
        if self._defaults['GetAttributeViReal64']['Value'] is None:
            raise MockFunctionCallError("niScope_GetAttributeViReal64", param='Value')
        value.contents.value = self._defaults['GetAttributeViReal64']['Value']
        return self._defaults['GetAttributeViReal64']['return']

    def niScope_GetAttributeViString(self, vi, channel_list, attribute_id, buf_size, value):  # noqa: N802
        if self._defaults['GetAttributeViString']['return'] != 0:
            return self._defaults['GetAttributeViString']['return']
        if self._defaults['GetAttributeViString']['Value'] is None:
            raise MockFunctionCallError("niScope_GetAttributeViString", param='Value')
        if buf_size == 0:
            return len(self._defaults['GetAttributeViString']['Value'])
        value.value = self._defaults['GetAttributeViString']['Value'].encode('ascii')
        return self._defaults['GetAttributeViString']['return']

    def niScope_GetChannelName(self, vi, index, buffer_size, channel_string):  # noqa: N802
        if self._defaults['GetChannelName']['return'] != 0:
            return self._defaults['GetChannelName']['return']
        if self._defaults['GetChannelName']['channelString'] is None:
            raise MockFunctionCallError("niScope_GetChannelName", param='channelString')
        a = self._defaults['GetChannelName']['channelString']
        import sys
        if sys.version_info.major > 2 and type(a) is str:
            a = a.encode('ascii')
        for i in range(min(len(channel_string), len(a))):
            channel_string[i] = a[i]
        return self._defaults['GetChannelName']['return']

    def niScope_GetEqualizationFilterCoefficients(self, vi, channel, number_of_coefficients, coefficients):  # noqa: N802
        if self._defaults['GetEqualizationFilterCoefficients']['return'] != 0:
            return self._defaults['GetEqualizationFilterCoefficients']['return']
        if self._defaults['GetEqualizationFilterCoefficients']['Coefficients'] is None:
            raise MockFunctionCallError("niScope_GetEqualizationFilterCoefficients", param='Coefficients')
        a = self._defaults['GetEqualizationFilterCoefficients']['Coefficients']
        import sys
        if sys.version_info.major > 2 and type(a) is str:
            a = a.encode('ascii')
        for i in range(min(len(coefficients), len(a))):
            coefficients[i] = a[i]
        return self._defaults['GetEqualizationFilterCoefficients']['return']

    def niScope_GetError(self, vi, error_code, buffer_size, description):  # noqa: N802
        if self._defaults['GetError']['return'] != 0:
            return self._defaults['GetError']['return']
        if self._defaults['GetError']['errorCode'] is None:
            raise MockFunctionCallError("niScope_GetError", param='errorCode')
        error_code.contents.value = self._defaults['GetError']['errorCode']
        if self._defaults['GetError']['Description'] is None:
            raise MockFunctionCallError("niScope_GetError", param='Description')
        if buffer_size == 0:
            return len(self._defaults['GetError']['Description'])
        description.value = self._defaults['GetError']['Description'].encode('ascii')
        return self._defaults['GetError']['return']

    def niScope_GetErrorMessage(self, vi, error_code, buffer__size, error_message):  # noqa: N802
        if self._defaults['GetErrorMessage']['return'] != 0:
            return self._defaults['GetErrorMessage']['return']
        if self._defaults['GetErrorMessage']['errorMessage'] is None:
            raise MockFunctionCallError("niScope_GetErrorMessage", param='errorMessage')
        a = self._defaults['GetErrorMessage']['errorMessage']
        import sys
        if sys.version_info.major > 2 and type(a) is str:
            a = a.encode('ascii')
        for i in range(min(len(error_message), len(a))):
            error_message[i] = a[i]
        return self._defaults['GetErrorMessage']['return']

    def niScope_GetFrequencyResponse(self, vi, channel, buffer_size, frequencies, amplitudes, phases, number_of_frequencies):  # noqa: N802
        if self._defaults['GetFrequencyResponse']['return'] != 0:
            return self._defaults['GetFrequencyResponse']['return']
        if self._defaults['GetFrequencyResponse']['numberOfFrequencies'] is None:
            raise MockFunctionCallError("niScope_GetFrequencyResponse", param='numberOfFrequencies')
        number_of_frequencies.contents.value = self._defaults['GetFrequencyResponse']['numberOfFrequencies']
        return self._defaults['GetFrequencyResponse']['return']

    def niScope_GetStreamEndpointHandle(self, vi, stream_name, writer_handle):  # noqa: N802
        if self._defaults['GetStreamEndpointHandle']['return'] != 0:
            return self._defaults['GetStreamEndpointHandle']['return']
        if self._defaults['GetStreamEndpointHandle']['writerHandle'] is None:
            raise MockFunctionCallError("niScope_GetStreamEndpointHandle", param='writerHandle')
        writer_handle.contents.value = self._defaults['GetStreamEndpointHandle']['writerHandle']
        return self._defaults['GetStreamEndpointHandle']['return']

    def niScope_InitWithOptions(self, resource_name, id_query, reset_device, option_string, vi):  # noqa: N802
        if self._defaults['InitWithOptions']['return'] != 0:
            return self._defaults['InitWithOptions']['return']
        if self._defaults['InitWithOptions']['vi'] is None:
            raise MockFunctionCallError("niScope_InitWithOptions", param='vi')
        vi.contents.value = self._defaults['InitWithOptions']['vi']
        return self._defaults['InitWithOptions']['return']

    def niScope_InitiateAcquisition(self, vi):  # noqa: N802
        if self._defaults['InitiateAcquisition']['return'] != 0:
            return self._defaults['InitiateAcquisition']['return']
        return self._defaults['InitiateAcquisition']['return']

    def niScope_IsDeviceReady(self, resource_name, channel_list, device_ready):  # noqa: N802
        if self._defaults['IsDeviceReady']['return'] != 0:
            return self._defaults['IsDeviceReady']['return']
        if self._defaults['IsDeviceReady']['deviceReady'] is None:
            raise MockFunctionCallError("niScope_IsDeviceReady", param='deviceReady')
        device_ready.contents.value = self._defaults['IsDeviceReady']['deviceReady']
        return self._defaults['IsDeviceReady']['return']

    def niScope_IsInvalidWfmElement(self, vi, element_value, is_invalid):  # noqa: N802
        if self._defaults['IsInvalidWfmElement']['return'] != 0:
            return self._defaults['IsInvalidWfmElement']['return']
        if self._defaults['IsInvalidWfmElement']['isInvalid'] is None:
            raise MockFunctionCallError("niScope_IsInvalidWfmElement", param='isInvalid')
        is_invalid.contents.value = self._defaults['IsInvalidWfmElement']['isInvalid']
        return self._defaults['IsInvalidWfmElement']['return']

    def niScope_ProbeCompensationSignalStart(self, vi):  # noqa: N802
        if self._defaults['ProbeCompensationSignalStart']['return'] != 0:
            return self._defaults['ProbeCompensationSignalStart']['return']
        return self._defaults['ProbeCompensationSignalStart']['return']

    def niScope_ProbeCompensationSignalStop(self, vi):  # noqa: N802
        if self._defaults['ProbeCompensationSignalStop']['return'] != 0:
            return self._defaults['ProbeCompensationSignalStop']['return']
        return self._defaults['ProbeCompensationSignalStop']['return']

    def niScope_ReadMeasurement(self, vi, channel_list, timeout, scalar_meas_function, result):  # noqa: N802
        if self._defaults['ReadMeasurement']['return'] != 0:
            return self._defaults['ReadMeasurement']['return']
        if self._defaults['ReadMeasurement']['Result'] is None:
            raise MockFunctionCallError("niScope_ReadMeasurement", param='Result')
        a = self._defaults['ReadMeasurement']['Result']
        import sys
        if sys.version_info.major > 2 and type(a) is str:
            a = a.encode('ascii')
        for i in range(min(len(result), len(a))):
            result[i] = a[i]
        return self._defaults['ReadMeasurement']['return']

    def niScope_ReadWaveform(self, vi, channel, waveform_size, max_time, waveform, actual_points, initial_x, x_increment):  # noqa: N802
        if self._defaults['ReadWaveform']['return'] != 0:
            return self._defaults['ReadWaveform']['return']
        if self._defaults['ReadWaveform']['Waveform'] is None:
            raise MockFunctionCallError("niScope_ReadWaveform", param='Waveform')
        a = self._defaults['ReadWaveform']['Waveform']
        import sys
        if sys.version_info.major > 2 and type(a) is str:
            a = a.encode('ascii')
        for i in range(min(len(waveform), len(a))):
            waveform[i] = a[i]
        if self._defaults['ReadWaveform']['actualPoints'] is None:
            raise MockFunctionCallError("niScope_ReadWaveform", param='actualPoints')
        actual_points.contents.value = self._defaults['ReadWaveform']['actualPoints']
        if self._defaults['ReadWaveform']['initialX'] is None:
            raise MockFunctionCallError("niScope_ReadWaveform", param='initialX')
        initial_x.contents.value = self._defaults['ReadWaveform']['initialX']
        if self._defaults['ReadWaveform']['xIncrement'] is None:
            raise MockFunctionCallError("niScope_ReadWaveform", param='xIncrement')
        x_increment.contents.value = self._defaults['ReadWaveform']['xIncrement']
        return self._defaults['ReadWaveform']['return']

    def niScope_ReadWaveformMeasurement(self, vi, channel, meas_function, max_time, measurement):  # noqa: N802
        if self._defaults['ReadWaveformMeasurement']['return'] != 0:
            return self._defaults['ReadWaveformMeasurement']['return']
        if self._defaults['ReadWaveformMeasurement']['Measurement'] is None:
            raise MockFunctionCallError("niScope_ReadWaveformMeasurement", param='Measurement')
        measurement.contents.value = self._defaults['ReadWaveformMeasurement']['Measurement']
        return self._defaults['ReadWaveformMeasurement']['return']

    def niScope_ResetDevice(self, vi):  # noqa: N802
        if self._defaults['ResetDevice']['return'] != 0:
            return self._defaults['ResetDevice']['return']
        return self._defaults['ResetDevice']['return']

    def niScope_ResetWithDefaults(self, vi):  # noqa: N802
        if self._defaults['ResetWithDefaults']['return'] != 0:
            return self._defaults['ResetWithDefaults']['return']
        return self._defaults['ResetWithDefaults']['return']

    def niScope_SampleMode(self, vi, sample_mode):  # noqa: N802
        if self._defaults['SampleMode']['return'] != 0:
            return self._defaults['SampleMode']['return']
        if self._defaults['SampleMode']['sampleMode'] is None:
            raise MockFunctionCallError("niScope_SampleMode", param='sampleMode')
        sample_mode.contents.value = self._defaults['SampleMode']['sampleMode']
        return self._defaults['SampleMode']['return']

    def niScope_SampleRate(self, vi, sample_rate):  # noqa: N802
        if self._defaults['SampleRate']['return'] != 0:
            return self._defaults['SampleRate']['return']
        if self._defaults['SampleRate']['sampleRate'] is None:
            raise MockFunctionCallError("niScope_SampleRate", param='sampleRate')
        sample_rate.contents.value = self._defaults['SampleRate']['sampleRate']
        return self._defaults['SampleRate']['return']

    def niScope_SendSWTrigger(self, vi):  # noqa: N802
        if self._defaults['SendSWTrigger']['return'] != 0:
            return self._defaults['SendSWTrigger']['return']
        return self._defaults['SendSWTrigger']['return']

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

    def niScope_close(self, vi):  # noqa: N802
        if self._defaults['close']['return'] != 0:
            return self._defaults['close']['return']
        return self._defaults['close']['return']

    def niScope_errorHandler(self, vi, error_code, error_source, error_description):  # noqa: N802
        if self._defaults['errorHandler']['return'] != 0:
            return self._defaults['errorHandler']['return']
        if self._defaults['errorHandler']['errorSource'] is None:
            raise MockFunctionCallError("niScope_errorHandler", param='errorSource')
        a = self._defaults['errorHandler']['errorSource']
        import sys
        if sys.version_info.major > 2 and type(a) is str:
            a = a.encode('ascii')
        for i in range(min(len(error_source), len(a))):
            error_source[i] = a[i]
        if self._defaults['errorHandler']['errorDescription'] is None:
            raise MockFunctionCallError("niScope_errorHandler", param='errorDescription')
        a = self._defaults['errorHandler']['errorDescription']
        import sys
        if sys.version_info.major > 2 and type(a) is str:
            a = a.encode('ascii')
        for i in range(min(len(error_description), len(a))):
            error_description[i] = a[i]
        return self._defaults['errorHandler']['return']

    def niScope_reset(self, vi):  # noqa: N802
        if self._defaults['reset']['return'] != 0:
            return self._defaults['reset']['return']
        return self._defaults['reset']['return']

    def niScope_self_test(self, vi, self_test_result, self_test_message):  # noqa: N802
        if self._defaults['self_test']['return'] != 0:
            return self._defaults['self_test']['return']
        if self._defaults['self_test']['selfTestResult'] is None:
            raise MockFunctionCallError("niScope_self_test", param='selfTestResult')
        self_test_result.contents.value = self._defaults['self_test']['selfTestResult']
        if self._defaults['self_test']['selfTestMessage'] is None:
            raise MockFunctionCallError("niScope_self_test", param='selfTestMessage')
        a = self._defaults['self_test']['selfTestMessage']
        import sys
        if sys.version_info.major > 2 and type(a) is str:
            a = a.encode('ascii')
        for i in range(min(len(self_test_message), len(a))):
            self_test_message[i] = a[i]
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
        mock_library.niScope_ActualRecordLength.side_effect = MockFunctionCallError("niScope_ActualRecordLength")
        mock_library.niScope_ActualRecordLength.return_value = 0
        mock_library.niScope_AddWaveformProcessing.side_effect = MockFunctionCallError("niScope_AddWaveformProcessing")
        mock_library.niScope_AddWaveformProcessing.return_value = 0
        mock_library.niScope_AdjustSampleClockRelativeDelay.side_effect = MockFunctionCallError("niScope_AdjustSampleClockRelativeDelay")
        mock_library.niScope_AdjustSampleClockRelativeDelay.return_value = 0
        mock_library.niScope_AutoSetup.side_effect = MockFunctionCallError("niScope_AutoSetup")
        mock_library.niScope_AutoSetup.return_value = 0
        mock_library.niScope_CalSelfCalibrate.side_effect = MockFunctionCallError("niScope_CalSelfCalibrate")
        mock_library.niScope_CalSelfCalibrate.return_value = 0
        mock_library.niScope_CheckAttributeViBoolean.side_effect = MockFunctionCallError("niScope_CheckAttributeViBoolean")
        mock_library.niScope_CheckAttributeViBoolean.return_value = 0
        mock_library.niScope_CheckAttributeViInt32.side_effect = MockFunctionCallError("niScope_CheckAttributeViInt32")
        mock_library.niScope_CheckAttributeViInt32.return_value = 0
        mock_library.niScope_CheckAttributeViInt64.side_effect = MockFunctionCallError("niScope_CheckAttributeViInt64")
        mock_library.niScope_CheckAttributeViInt64.return_value = 0
        mock_library.niScope_CheckAttributeViReal64.side_effect = MockFunctionCallError("niScope_CheckAttributeViReal64")
        mock_library.niScope_CheckAttributeViReal64.return_value = 0
        mock_library.niScope_CheckAttributeViSession.side_effect = MockFunctionCallError("niScope_CheckAttributeViSession")
        mock_library.niScope_CheckAttributeViSession.return_value = 0
        mock_library.niScope_CheckAttributeViString.side_effect = MockFunctionCallError("niScope_CheckAttributeViString")
        mock_library.niScope_CheckAttributeViString.return_value = 0
        mock_library.niScope_ClearWaveformMeasurementStats.side_effect = MockFunctionCallError("niScope_ClearWaveformMeasurementStats")
        mock_library.niScope_ClearWaveformMeasurementStats.return_value = 0
        mock_library.niScope_ClearWaveformProcessing.side_effect = MockFunctionCallError("niScope_ClearWaveformProcessing")
        mock_library.niScope_ClearWaveformProcessing.return_value = 0
        mock_library.niScope_Commit.side_effect = MockFunctionCallError("niScope_Commit")
        mock_library.niScope_Commit.return_value = 0
        mock_library.niScope_ConfigureAcquisition.side_effect = MockFunctionCallError("niScope_ConfigureAcquisition")
        mock_library.niScope_ConfigureAcquisition.return_value = 0
        mock_library.niScope_ConfigureAcquisitionRecord.side_effect = MockFunctionCallError("niScope_ConfigureAcquisitionRecord")
        mock_library.niScope_ConfigureAcquisitionRecord.return_value = 0
        mock_library.niScope_ConfigureChanCharacteristics.side_effect = MockFunctionCallError("niScope_ConfigureChanCharacteristics")
        mock_library.niScope_ConfigureChanCharacteristics.return_value = 0
        mock_library.niScope_ConfigureChannel.side_effect = MockFunctionCallError("niScope_ConfigureChannel")
        mock_library.niScope_ConfigureChannel.return_value = 0
        mock_library.niScope_ConfigureClock.side_effect = MockFunctionCallError("niScope_ConfigureClock")
        mock_library.niScope_ConfigureClock.return_value = 0
        mock_library.niScope_ConfigureEdgeTriggerSource.side_effect = MockFunctionCallError("niScope_ConfigureEdgeTriggerSource")
        mock_library.niScope_ConfigureEdgeTriggerSource.return_value = 0
        mock_library.niScope_ConfigureEqualizationFilterCoefficients.side_effect = MockFunctionCallError("niScope_ConfigureEqualizationFilterCoefficients")
        mock_library.niScope_ConfigureEqualizationFilterCoefficients.return_value = 0
        mock_library.niScope_ConfigureHorizontalTiming.side_effect = MockFunctionCallError("niScope_ConfigureHorizontalTiming")
        mock_library.niScope_ConfigureHorizontalTiming.return_value = 0
        mock_library.niScope_ConfigureRefLevels.side_effect = MockFunctionCallError("niScope_ConfigureRefLevels")
        mock_library.niScope_ConfigureRefLevels.return_value = 0
        mock_library.niScope_ConfigureTVTriggerLineNumber.side_effect = MockFunctionCallError("niScope_ConfigureTVTriggerLineNumber")
        mock_library.niScope_ConfigureTVTriggerLineNumber.return_value = 0
        mock_library.niScope_ConfigureTVTriggerSource.side_effect = MockFunctionCallError("niScope_ConfigureTVTriggerSource")
        mock_library.niScope_ConfigureTVTriggerSource.return_value = 0
        mock_library.niScope_ConfigureTrigger.side_effect = MockFunctionCallError("niScope_ConfigureTrigger")
        mock_library.niScope_ConfigureTrigger.return_value = 0
        mock_library.niScope_ConfigureTriggerCoupling.side_effect = MockFunctionCallError("niScope_ConfigureTriggerCoupling")
        mock_library.niScope_ConfigureTriggerCoupling.return_value = 0
        mock_library.niScope_ConfigureTriggerDigital.side_effect = MockFunctionCallError("niScope_ConfigureTriggerDigital")
        mock_library.niScope_ConfigureTriggerDigital.return_value = 0
        mock_library.niScope_ConfigureTriggerEdge.side_effect = MockFunctionCallError("niScope_ConfigureTriggerEdge")
        mock_library.niScope_ConfigureTriggerEdge.return_value = 0
        mock_library.niScope_ConfigureTriggerHysteresis.side_effect = MockFunctionCallError("niScope_ConfigureTriggerHysteresis")
        mock_library.niScope_ConfigureTriggerHysteresis.return_value = 0
        mock_library.niScope_ConfigureTriggerImmediate.side_effect = MockFunctionCallError("niScope_ConfigureTriggerImmediate")
        mock_library.niScope_ConfigureTriggerImmediate.return_value = 0
        mock_library.niScope_ConfigureTriggerOutput.side_effect = MockFunctionCallError("niScope_ConfigureTriggerOutput")
        mock_library.niScope_ConfigureTriggerOutput.return_value = 0
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
        mock_library.niScope_FetchMeasurement.side_effect = MockFunctionCallError("niScope_FetchMeasurement")
        mock_library.niScope_FetchMeasurement.return_value = 0
        mock_library.niScope_FetchMeasurementStats.side_effect = MockFunctionCallError("niScope_FetchMeasurementStats")
        mock_library.niScope_FetchMeasurementStats.return_value = 0
        mock_library.niScope_FetchWaveform.side_effect = MockFunctionCallError("niScope_FetchWaveform")
        mock_library.niScope_FetchWaveform.return_value = 0
        mock_library.niScope_FetchWaveformMeasurement.side_effect = MockFunctionCallError("niScope_FetchWaveformMeasurement")
        mock_library.niScope_FetchWaveformMeasurement.return_value = 0
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
        mock_library.niScope_GetChannelName.side_effect = MockFunctionCallError("niScope_GetChannelName")
        mock_library.niScope_GetChannelName.return_value = 0
        mock_library.niScope_GetEqualizationFilterCoefficients.side_effect = MockFunctionCallError("niScope_GetEqualizationFilterCoefficients")
        mock_library.niScope_GetEqualizationFilterCoefficients.return_value = 0
        mock_library.niScope_GetError.side_effect = MockFunctionCallError("niScope_GetError")
        mock_library.niScope_GetError.return_value = 0
        mock_library.niScope_GetErrorMessage.side_effect = MockFunctionCallError("niScope_GetErrorMessage")
        mock_library.niScope_GetErrorMessage.return_value = 0
        mock_library.niScope_GetFrequencyResponse.side_effect = MockFunctionCallError("niScope_GetFrequencyResponse")
        mock_library.niScope_GetFrequencyResponse.return_value = 0
        mock_library.niScope_GetStreamEndpointHandle.side_effect = MockFunctionCallError("niScope_GetStreamEndpointHandle")
        mock_library.niScope_GetStreamEndpointHandle.return_value = 0
        mock_library.niScope_InitWithOptions.side_effect = MockFunctionCallError("niScope_InitWithOptions")
        mock_library.niScope_InitWithOptions.return_value = 0
        mock_library.niScope_InitiateAcquisition.side_effect = MockFunctionCallError("niScope_InitiateAcquisition")
        mock_library.niScope_InitiateAcquisition.return_value = 0
        mock_library.niScope_IsDeviceReady.side_effect = MockFunctionCallError("niScope_IsDeviceReady")
        mock_library.niScope_IsDeviceReady.return_value = 0
        mock_library.niScope_IsInvalidWfmElement.side_effect = MockFunctionCallError("niScope_IsInvalidWfmElement")
        mock_library.niScope_IsInvalidWfmElement.return_value = 0
        mock_library.niScope_ProbeCompensationSignalStart.side_effect = MockFunctionCallError("niScope_ProbeCompensationSignalStart")
        mock_library.niScope_ProbeCompensationSignalStart.return_value = 0
        mock_library.niScope_ProbeCompensationSignalStop.side_effect = MockFunctionCallError("niScope_ProbeCompensationSignalStop")
        mock_library.niScope_ProbeCompensationSignalStop.return_value = 0
        mock_library.niScope_ReadMeasurement.side_effect = MockFunctionCallError("niScope_ReadMeasurement")
        mock_library.niScope_ReadMeasurement.return_value = 0
        mock_library.niScope_ReadWaveform.side_effect = MockFunctionCallError("niScope_ReadWaveform")
        mock_library.niScope_ReadWaveform.return_value = 0
        mock_library.niScope_ReadWaveformMeasurement.side_effect = MockFunctionCallError("niScope_ReadWaveformMeasurement")
        mock_library.niScope_ReadWaveformMeasurement.return_value = 0
        mock_library.niScope_ResetDevice.side_effect = MockFunctionCallError("niScope_ResetDevice")
        mock_library.niScope_ResetDevice.return_value = 0
        mock_library.niScope_ResetWithDefaults.side_effect = MockFunctionCallError("niScope_ResetWithDefaults")
        mock_library.niScope_ResetWithDefaults.return_value = 0
        mock_library.niScope_SampleMode.side_effect = MockFunctionCallError("niScope_SampleMode")
        mock_library.niScope_SampleMode.return_value = 0
        mock_library.niScope_SampleRate.side_effect = MockFunctionCallError("niScope_SampleRate")
        mock_library.niScope_SampleRate.return_value = 0
        mock_library.niScope_SendSWTrigger.side_effect = MockFunctionCallError("niScope_SendSWTrigger")
        mock_library.niScope_SendSWTrigger.return_value = 0
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
        mock_library.niScope_close.side_effect = MockFunctionCallError("niScope_close")
        mock_library.niScope_close.return_value = 0
        mock_library.niScope_errorHandler.side_effect = MockFunctionCallError("niScope_errorHandler")
        mock_library.niScope_errorHandler.return_value = 0
        mock_library.niScope_reset.side_effect = MockFunctionCallError("niScope_reset")
        mock_library.niScope_reset.return_value = 0
        mock_library.niScope_self_test.side_effect = MockFunctionCallError("niScope_self_test")
        mock_library.niScope_self_test.return_value = 0
