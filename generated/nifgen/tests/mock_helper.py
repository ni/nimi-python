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
        self._defaults['AbortGeneration'] = {}
        self._defaults['AbortGeneration']['return'] = 0
        self._defaults['AdjustSampleClockRelativeDelay'] = {}
        self._defaults['AdjustSampleClockRelativeDelay']['return'] = 0
        self._defaults['AllocateNamedWaveform'] = {}
        self._defaults['AllocateNamedWaveform']['return'] = 0
        self._defaults['AllocateWaveform'] = {}
        self._defaults['AllocateWaveform']['return'] = 0
        self._defaults['AllocateWaveform']['waveformHandle'] = None
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
        self._defaults['ClearArbMemory'] = {}
        self._defaults['ClearArbMemory']['return'] = 0
        self._defaults['ClearArbSequence'] = {}
        self._defaults['ClearArbSequence']['return'] = 0
        self._defaults['ClearArbWaveform'] = {}
        self._defaults['ClearArbWaveform']['return'] = 0
        self._defaults['ClearFreqList'] = {}
        self._defaults['ClearFreqList']['return'] = 0
        self._defaults['ClearUserStandardWaveform'] = {}
        self._defaults['ClearUserStandardWaveform']['return'] = 0
        self._defaults['Commit'] = {}
        self._defaults['Commit']['return'] = 0
        self._defaults['ConfigureAmplitude'] = {}
        self._defaults['ConfigureAmplitude']['return'] = 0
        self._defaults['ConfigureArbSequence'] = {}
        self._defaults['ConfigureArbSequence']['return'] = 0
        self._defaults['ConfigureArbWaveform'] = {}
        self._defaults['ConfigureArbWaveform']['return'] = 0
        self._defaults['ConfigureChannels'] = {}
        self._defaults['ConfigureChannels']['return'] = 0
        self._defaults['ConfigureClockMode'] = {}
        self._defaults['ConfigureClockMode']['return'] = 0
        self._defaults['ConfigureCustomFIRFilterCoefficients'] = {}
        self._defaults['ConfigureCustomFIRFilterCoefficients']['return'] = 0
        self._defaults['ConfigureDigitalEdgeScriptTrigger'] = {}
        self._defaults['ConfigureDigitalEdgeScriptTrigger']['return'] = 0
        self._defaults['ConfigureDigitalEdgeStartTrigger'] = {}
        self._defaults['ConfigureDigitalEdgeStartTrigger']['return'] = 0
        self._defaults['ConfigureDigitalLevelScriptTrigger'] = {}
        self._defaults['ConfigureDigitalLevelScriptTrigger']['return'] = 0
        self._defaults['ConfigureFreqList'] = {}
        self._defaults['ConfigureFreqList']['return'] = 0
        self._defaults['ConfigureFrequency'] = {}
        self._defaults['ConfigureFrequency']['return'] = 0
        self._defaults['ConfigureGain'] = {}
        self._defaults['ConfigureGain']['return'] = 0
        self._defaults['ConfigureOperationMode'] = {}
        self._defaults['ConfigureOperationMode']['return'] = 0
        self._defaults['ConfigureOutputEnabled'] = {}
        self._defaults['ConfigureOutputEnabled']['return'] = 0
        self._defaults['ConfigureOutputImpedance'] = {}
        self._defaults['ConfigureOutputImpedance']['return'] = 0
        self._defaults['ConfigureOutputMode'] = {}
        self._defaults['ConfigureOutputMode']['return'] = 0
        self._defaults['ConfigureP2PEndpointFullnessStartTrigger'] = {}
        self._defaults['ConfigureP2PEndpointFullnessStartTrigger']['return'] = 0
        self._defaults['ConfigureRefClockFrequency'] = {}
        self._defaults['ConfigureRefClockFrequency']['return'] = 0
        self._defaults['ConfigureRefClockSource'] = {}
        self._defaults['ConfigureRefClockSource']['return'] = 0
        self._defaults['ConfigureReferenceClock'] = {}
        self._defaults['ConfigureReferenceClock']['return'] = 0
        self._defaults['ConfigureSampleClockSource'] = {}
        self._defaults['ConfigureSampleClockSource']['return'] = 0
        self._defaults['ConfigureSampleRate'] = {}
        self._defaults['ConfigureSampleRate']['return'] = 0
        self._defaults['ConfigureSoftwareEdgeScriptTrigger'] = {}
        self._defaults['ConfigureSoftwareEdgeScriptTrigger']['return'] = 0
        self._defaults['ConfigureSoftwareEdgeStartTrigger'] = {}
        self._defaults['ConfigureSoftwareEdgeStartTrigger']['return'] = 0
        self._defaults['ConfigureStandardWaveform'] = {}
        self._defaults['ConfigureStandardWaveform']['return'] = 0
        self._defaults['ConfigureSynchronization'] = {}
        self._defaults['ConfigureSynchronization']['return'] = 0
        self._defaults['ConfigureTriggerMode'] = {}
        self._defaults['ConfigureTriggerMode']['return'] = 0
        self._defaults['ConfigureTriggerSource'] = {}
        self._defaults['ConfigureTriggerSource']['return'] = 0
        self._defaults['ConfigureUpdateClockSource'] = {}
        self._defaults['ConfigureUpdateClockSource']['return'] = 0
        self._defaults['CreateAdvancedArbSequence'] = {}
        self._defaults['CreateAdvancedArbSequence']['return'] = 0
        self._defaults['CreateAdvancedArbSequence']['coercedMarkersArray'] = None
        self._defaults['CreateAdvancedArbSequence']['sequenceHandle'] = None
        self._defaults['CreateArbSequence'] = {}
        self._defaults['CreateArbSequence']['return'] = 0
        self._defaults['CreateArbSequence']['sequenceHandle'] = None
        self._defaults['CreateArbWaveform'] = {}
        self._defaults['CreateArbWaveform']['return'] = 0
        self._defaults['CreateArbWaveform']['waveformHandle'] = None
        self._defaults['CreateBinary16ArbWaveform'] = {}
        self._defaults['CreateBinary16ArbWaveform']['return'] = 0
        self._defaults['CreateBinary16ArbWaveform']['waveformHandle'] = None
        self._defaults['CreateFreqList'] = {}
        self._defaults['CreateFreqList']['return'] = 0
        self._defaults['CreateFreqList']['frequencyListHandle'] = None
        self._defaults['CreateWaveformF64'] = {}
        self._defaults['CreateWaveformF64']['return'] = 0
        self._defaults['CreateWaveformF64']['waveformHandle'] = None
        self._defaults['CreateWaveformFromFileF64'] = {}
        self._defaults['CreateWaveformFromFileF64']['return'] = 0
        self._defaults['CreateWaveformFromFileF64']['waveformHandle'] = None
        self._defaults['CreateWaveformFromFileHWS'] = {}
        self._defaults['CreateWaveformFromFileHWS']['return'] = 0
        self._defaults['CreateWaveformFromFileHWS']['waveformHandle'] = None
        self._defaults['CreateWaveformFromFileI16'] = {}
        self._defaults['CreateWaveformFromFileI16']['return'] = 0
        self._defaults['CreateWaveformFromFileI16']['waveformHandle'] = None
        self._defaults['CreateWaveformI16'] = {}
        self._defaults['CreateWaveformI16']['return'] = 0
        self._defaults['CreateWaveformI16']['waveformHandle'] = None
        self._defaults['DefineUserStandardWaveform'] = {}
        self._defaults['DefineUserStandardWaveform']['return'] = 0
        self._defaults['DeleteNamedWaveform'] = {}
        self._defaults['DeleteNamedWaveform']['return'] = 0
        self._defaults['DeleteScript'] = {}
        self._defaults['DeleteScript']['return'] = 0
        self._defaults['Disable'] = {}
        self._defaults['Disable']['return'] = 0
        self._defaults['DisableAnalogFilter'] = {}
        self._defaults['DisableAnalogFilter']['return'] = 0
        self._defaults['DisableDigitalFilter'] = {}
        self._defaults['DisableDigitalFilter']['return'] = 0
        self._defaults['DisableDigitalPatterning'] = {}
        self._defaults['DisableDigitalPatterning']['return'] = 0
        self._defaults['DisableScriptTrigger'] = {}
        self._defaults['DisableScriptTrigger']['return'] = 0
        self._defaults['DisableStartTrigger'] = {}
        self._defaults['DisableStartTrigger']['return'] = 0
        self._defaults['EnableAnalogFilter'] = {}
        self._defaults['EnableAnalogFilter']['return'] = 0
        self._defaults['EnableDigitalFilter'] = {}
        self._defaults['EnableDigitalFilter']['return'] = 0
        self._defaults['EnableDigitalPatterning'] = {}
        self._defaults['EnableDigitalPatterning']['return'] = 0
        self._defaults['ErrorHandler'] = {}
        self._defaults['ErrorHandler']['return'] = 0
        self._defaults['ErrorHandler']['errorMessage'] = None
        self._defaults['ExportSignal'] = {}
        self._defaults['ExportSignal']['return'] = 0
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
        self._defaults['GetAttributeViString'] = {}
        self._defaults['GetAttributeViString']['return'] = 0
        self._defaults['GetAttributeViString']['attributeValue'] = None
        self._defaults['GetError'] = {}
        self._defaults['GetError']['return'] = 0
        self._defaults['GetError']['errorCode'] = None
        self._defaults['GetError']['errorDescription'] = None
        self._defaults['GetFIRFilterCoefficients'] = {}
        self._defaults['GetFIRFilterCoefficients']['return'] = 0
        self._defaults['GetHardwareState'] = {}
        self._defaults['GetHardwareState']['return'] = 0
        self._defaults['GetHardwareState']['state'] = None
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
        self._defaults['GetSelfCalSupported'] = {}
        self._defaults['GetSelfCalSupported']['return'] = 0
        self._defaults['GetSelfCalSupported']['selfCalSupported'] = None
        self._defaults['InitWithOptions'] = {}
        self._defaults['InitWithOptions']['return'] = 0
        self._defaults['InitWithOptions']['vi'] = None
        self._defaults['InitializeAnalogOutputCalibration'] = {}
        self._defaults['InitializeAnalogOutputCalibration']['return'] = 0
        self._defaults['InitializeCalADCCalibration'] = {}
        self._defaults['InitializeCalADCCalibration']['return'] = 0
        self._defaults['InitializeFlatnessCalibration'] = {}
        self._defaults['InitializeFlatnessCalibration']['return'] = 0
        self._defaults['InitializeOscillatorFrequencyCalibration'] = {}
        self._defaults['InitializeOscillatorFrequencyCalibration']['return'] = 0
        self._defaults['InitializeWithChannels'] = {}
        self._defaults['InitializeWithChannels']['return'] = 0
        self._defaults['InitializeWithChannels']['vi'] = None
        self._defaults['InitiateGeneration'] = {}
        self._defaults['InitiateGeneration']['return'] = 0
        self._defaults['IsDone'] = {}
        self._defaults['IsDone']['return'] = 0
        self._defaults['IsDone']['Done'] = None
        self._defaults['ManualEnableP2PStream'] = {}
        self._defaults['ManualEnableP2PStream']['return'] = 0
        self._defaults['QueryArbSeqCapabilities'] = {}
        self._defaults['QueryArbSeqCapabilities']['return'] = 0
        self._defaults['QueryArbSeqCapabilities']['maximumNumberOfSequences'] = None
        self._defaults['QueryArbSeqCapabilities']['minimumSequenceLength'] = None
        self._defaults['QueryArbSeqCapabilities']['maximumSequenceLength'] = None
        self._defaults['QueryArbSeqCapabilities']['maximumLoopCount'] = None
        self._defaults['QueryArbWfmCapabilities'] = {}
        self._defaults['QueryArbWfmCapabilities']['return'] = 0
        self._defaults['QueryArbWfmCapabilities']['maximumNumberOfWaveforms'] = None
        self._defaults['QueryArbWfmCapabilities']['waveformQuantum'] = None
        self._defaults['QueryArbWfmCapabilities']['minimumWaveformSize'] = None
        self._defaults['QueryArbWfmCapabilities']['maximumWaveformSize'] = None
        self._defaults['QueryFreqListCapabilities'] = {}
        self._defaults['QueryFreqListCapabilities']['return'] = 0
        self._defaults['QueryFreqListCapabilities']['maximumNumberOfFreqLists'] = None
        self._defaults['QueryFreqListCapabilities']['minimumFrequencyListLength'] = None
        self._defaults['QueryFreqListCapabilities']['maximumFrequencyListLength'] = None
        self._defaults['QueryFreqListCapabilities']['minimumFrequencyListDuration'] = None
        self._defaults['QueryFreqListCapabilities']['maximumFrequencyListDuration'] = None
        self._defaults['QueryFreqListCapabilities']['frequencyListDurationQuantum'] = None
        self._defaults['ReadCalADC'] = {}
        self._defaults['ReadCalADC']['return'] = 0
        self._defaults['ReadCalADC']['calAdcValue'] = None
        self._defaults['ReadCurrentTemperature'] = {}
        self._defaults['ReadCurrentTemperature']['return'] = 0
        self._defaults['ReadCurrentTemperature']['Temperature'] = None
        self._defaults['ResetAttribute'] = {}
        self._defaults['ResetAttribute']['return'] = 0
        self._defaults['ResetDevice'] = {}
        self._defaults['ResetDevice']['return'] = 0
        self._defaults['ResetWithDefaults'] = {}
        self._defaults['ResetWithDefaults']['return'] = 0
        self._defaults['RouteSignalOut'] = {}
        self._defaults['RouteSignalOut']['return'] = 0
        self._defaults['SelfCal'] = {}
        self._defaults['SelfCal']['return'] = 0
        self._defaults['SendSoftwareEdgeTrigger'] = {}
        self._defaults['SendSoftwareEdgeTrigger']['return'] = 0
        self._defaults['SendSoftwareTrigger'] = {}
        self._defaults['SendSoftwareTrigger']['return'] = 0
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
        self._defaults['SetNamedWaveformNextWritePosition'] = {}
        self._defaults['SetNamedWaveformNextWritePosition']['return'] = 0
        self._defaults['SetWaveformNextWritePosition'] = {}
        self._defaults['SetWaveformNextWritePosition']['return'] = 0
        self._defaults['WaitUntilDone'] = {}
        self._defaults['WaitUntilDone']['return'] = 0
        self._defaults['WriteBinary16AnalogStaticValue'] = {}
        self._defaults['WriteBinary16AnalogStaticValue']['return'] = 0
        self._defaults['WriteBinary16Waveform'] = {}
        self._defaults['WriteBinary16Waveform']['return'] = 0
        self._defaults['WriteNamedWaveformF64'] = {}
        self._defaults['WriteNamedWaveformF64']['return'] = 0
        self._defaults['WriteNamedWaveformI16'] = {}
        self._defaults['WriteNamedWaveformI16']['return'] = 0
        self._defaults['WriteP2PEndpointI16'] = {}
        self._defaults['WriteP2PEndpointI16']['return'] = 0
        self._defaults['WriteScript'] = {}
        self._defaults['WriteScript']['return'] = 0
        self._defaults['WriteWaveform'] = {}
        self._defaults['WriteWaveform']['return'] = 0
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

    def niFgen_AbortGeneration(self, vi):  # noqa: N802
        if self._defaults['AbortGeneration']['return'] != 0:
            return self._defaults['AbortGeneration']['return']
        return self._defaults['AbortGeneration']['return']

    def niFgen_AdjustSampleClockRelativeDelay(self, vi, adjustment_time):  # noqa: N802
        if self._defaults['AdjustSampleClockRelativeDelay']['return'] != 0:
            return self._defaults['AdjustSampleClockRelativeDelay']['return']
        return self._defaults['AdjustSampleClockRelativeDelay']['return']

    def niFgen_AllocateNamedWaveform(self, vi, channel_name, waveform_name, waveform_size):  # noqa: N802
        if self._defaults['AllocateNamedWaveform']['return'] != 0:
            return self._defaults['AllocateNamedWaveform']['return']
        return self._defaults['AllocateNamedWaveform']['return']

    def niFgen_AllocateWaveform(self, vi, channel_name, waveform_size, waveform_handle):  # noqa: N802
        if self._defaults['AllocateWaveform']['return'] != 0:
            return self._defaults['AllocateWaveform']['return']
        if self._defaults['AllocateWaveform']['waveformHandle'] is None:
            raise MockFunctionCallError("niFgen_AllocateWaveform", param='waveformHandle')
        waveform_handle.contents.value = self._defaults['AllocateWaveform']['waveformHandle']
        return self._defaults['AllocateWaveform']['return']

    def niFgen_CheckAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['CheckAttributeViBoolean']['return'] != 0:
            return self._defaults['CheckAttributeViBoolean']['return']
        return self._defaults['CheckAttributeViBoolean']['return']

    def niFgen_CheckAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['CheckAttributeViInt32']['return'] != 0:
            return self._defaults['CheckAttributeViInt32']['return']
        return self._defaults['CheckAttributeViInt32']['return']

    def niFgen_CheckAttributeViInt64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['CheckAttributeViInt64']['return'] != 0:
            return self._defaults['CheckAttributeViInt64']['return']
        return self._defaults['CheckAttributeViInt64']['return']

    def niFgen_CheckAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['CheckAttributeViReal64']['return'] != 0:
            return self._defaults['CheckAttributeViReal64']['return']
        return self._defaults['CheckAttributeViReal64']['return']

    def niFgen_CheckAttributeViSession(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['CheckAttributeViSession']['return'] != 0:
            return self._defaults['CheckAttributeViSession']['return']
        return self._defaults['CheckAttributeViSession']['return']

    def niFgen_CheckAttributeViString(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['CheckAttributeViString']['return'] != 0:
            return self._defaults['CheckAttributeViString']['return']
        return self._defaults['CheckAttributeViString']['return']

    def niFgen_ClearArbMemory(self, vi):  # noqa: N802
        if self._defaults['ClearArbMemory']['return'] != 0:
            return self._defaults['ClearArbMemory']['return']
        return self._defaults['ClearArbMemory']['return']

    def niFgen_ClearArbSequence(self, vi, sequence_handle):  # noqa: N802
        if self._defaults['ClearArbSequence']['return'] != 0:
            return self._defaults['ClearArbSequence']['return']
        return self._defaults['ClearArbSequence']['return']

    def niFgen_ClearArbWaveform(self, vi, waveform_handle):  # noqa: N802
        if self._defaults['ClearArbWaveform']['return'] != 0:
            return self._defaults['ClearArbWaveform']['return']
        return self._defaults['ClearArbWaveform']['return']

    def niFgen_ClearFreqList(self, vi, frequency_list_handle):  # noqa: N802
        if self._defaults['ClearFreqList']['return'] != 0:
            return self._defaults['ClearFreqList']['return']
        return self._defaults['ClearFreqList']['return']

    def niFgen_ClearUserStandardWaveform(self, vi, channel_name):  # noqa: N802
        if self._defaults['ClearUserStandardWaveform']['return'] != 0:
            return self._defaults['ClearUserStandardWaveform']['return']
        return self._defaults['ClearUserStandardWaveform']['return']

    def niFgen_Commit(self, vi):  # noqa: N802
        if self._defaults['Commit']['return'] != 0:
            return self._defaults['Commit']['return']
        return self._defaults['Commit']['return']

    def niFgen_ConfigureAmplitude(self, vi, channel_name, amplitude):  # noqa: N802
        if self._defaults['ConfigureAmplitude']['return'] != 0:
            return self._defaults['ConfigureAmplitude']['return']
        return self._defaults['ConfigureAmplitude']['return']

    def niFgen_ConfigureArbSequence(self, vi, channel_name, sequence_handle, gain, offset):  # noqa: N802
        if self._defaults['ConfigureArbSequence']['return'] != 0:
            return self._defaults['ConfigureArbSequence']['return']
        return self._defaults['ConfigureArbSequence']['return']

    def niFgen_ConfigureArbWaveform(self, vi, channel_name, waveform_handle, gain, offset):  # noqa: N802
        if self._defaults['ConfigureArbWaveform']['return'] != 0:
            return self._defaults['ConfigureArbWaveform']['return']
        return self._defaults['ConfigureArbWaveform']['return']

    def niFgen_ConfigureChannels(self, vi, channels):  # noqa: N802
        if self._defaults['ConfigureChannels']['return'] != 0:
            return self._defaults['ConfigureChannels']['return']
        return self._defaults['ConfigureChannels']['return']

    def niFgen_ConfigureClockMode(self, vi, clock_mode):  # noqa: N802
        if self._defaults['ConfigureClockMode']['return'] != 0:
            return self._defaults['ConfigureClockMode']['return']
        return self._defaults['ConfigureClockMode']['return']

    def niFgen_ConfigureCustomFIRFilterCoefficients(self, vi, channel_name, number_of_coefficients, coefficients_array):  # noqa: N802
        if self._defaults['ConfigureCustomFIRFilterCoefficients']['return'] != 0:
            return self._defaults['ConfigureCustomFIRFilterCoefficients']['return']
        return self._defaults['ConfigureCustomFIRFilterCoefficients']['return']

    def niFgen_ConfigureDigitalEdgeScriptTrigger(self, vi, trigger_id, source, edge):  # noqa: N802
        if self._defaults['ConfigureDigitalEdgeScriptTrigger']['return'] != 0:
            return self._defaults['ConfigureDigitalEdgeScriptTrigger']['return']
        return self._defaults['ConfigureDigitalEdgeScriptTrigger']['return']

    def niFgen_ConfigureDigitalEdgeStartTrigger(self, vi, source, edge):  # noqa: N802
        if self._defaults['ConfigureDigitalEdgeStartTrigger']['return'] != 0:
            return self._defaults['ConfigureDigitalEdgeStartTrigger']['return']
        return self._defaults['ConfigureDigitalEdgeStartTrigger']['return']

    def niFgen_ConfigureDigitalLevelScriptTrigger(self, vi, trigger_id, source, trigger_when):  # noqa: N802
        if self._defaults['ConfigureDigitalLevelScriptTrigger']['return'] != 0:
            return self._defaults['ConfigureDigitalLevelScriptTrigger']['return']
        return self._defaults['ConfigureDigitalLevelScriptTrigger']['return']

    def niFgen_ConfigureFreqList(self, vi, channel_name, frequency_list_handle, amplitude, dc_offset, start_phase):  # noqa: N802
        if self._defaults['ConfigureFreqList']['return'] != 0:
            return self._defaults['ConfigureFreqList']['return']
        return self._defaults['ConfigureFreqList']['return']

    def niFgen_ConfigureFrequency(self, vi, channel_name, frequency):  # noqa: N802
        if self._defaults['ConfigureFrequency']['return'] != 0:
            return self._defaults['ConfigureFrequency']['return']
        return self._defaults['ConfigureFrequency']['return']

    def niFgen_ConfigureGain(self, vi, channel_name, gain):  # noqa: N802
        if self._defaults['ConfigureGain']['return'] != 0:
            return self._defaults['ConfigureGain']['return']
        return self._defaults['ConfigureGain']['return']

    def niFgen_ConfigureOperationMode(self, vi, channel_name, operation_mode):  # noqa: N802
        if self._defaults['ConfigureOperationMode']['return'] != 0:
            return self._defaults['ConfigureOperationMode']['return']
        return self._defaults['ConfigureOperationMode']['return']

    def niFgen_ConfigureOutputEnabled(self, vi, channel_name, enabled):  # noqa: N802
        if self._defaults['ConfigureOutputEnabled']['return'] != 0:
            return self._defaults['ConfigureOutputEnabled']['return']
        return self._defaults['ConfigureOutputEnabled']['return']

    def niFgen_ConfigureOutputImpedance(self, vi, channel_name, impedance):  # noqa: N802
        if self._defaults['ConfigureOutputImpedance']['return'] != 0:
            return self._defaults['ConfigureOutputImpedance']['return']
        return self._defaults['ConfigureOutputImpedance']['return']

    def niFgen_ConfigureOutputMode(self, vi, output_mode):  # noqa: N802
        if self._defaults['ConfigureOutputMode']['return'] != 0:
            return self._defaults['ConfigureOutputMode']['return']
        return self._defaults['ConfigureOutputMode']['return']

    def niFgen_ConfigureP2PEndpointFullnessStartTrigger(self, vi, p2p_endpoint_fullness_level):  # noqa: N802
        if self._defaults['ConfigureP2PEndpointFullnessStartTrigger']['return'] != 0:
            return self._defaults['ConfigureP2PEndpointFullnessStartTrigger']['return']
        return self._defaults['ConfigureP2PEndpointFullnessStartTrigger']['return']

    def niFgen_ConfigureRefClockFrequency(self, vi, reference_clock_frequency):  # noqa: N802
        if self._defaults['ConfigureRefClockFrequency']['return'] != 0:
            return self._defaults['ConfigureRefClockFrequency']['return']
        return self._defaults['ConfigureRefClockFrequency']['return']

    def niFgen_ConfigureRefClockSource(self, vi, reference_clock_source):  # noqa: N802
        if self._defaults['ConfigureRefClockSource']['return'] != 0:
            return self._defaults['ConfigureRefClockSource']['return']
        return self._defaults['ConfigureRefClockSource']['return']

    def niFgen_ConfigureReferenceClock(self, vi, reference_clock_source, reference_clock_frequency):  # noqa: N802
        if self._defaults['ConfigureReferenceClock']['return'] != 0:
            return self._defaults['ConfigureReferenceClock']['return']
        return self._defaults['ConfigureReferenceClock']['return']

    def niFgen_ConfigureSampleClockSource(self, vi, sample_clock_source):  # noqa: N802
        if self._defaults['ConfigureSampleClockSource']['return'] != 0:
            return self._defaults['ConfigureSampleClockSource']['return']
        return self._defaults['ConfigureSampleClockSource']['return']

    def niFgen_ConfigureSampleRate(self, vi, sample_rate):  # noqa: N802
        if self._defaults['ConfigureSampleRate']['return'] != 0:
            return self._defaults['ConfigureSampleRate']['return']
        return self._defaults['ConfigureSampleRate']['return']

    def niFgen_ConfigureSoftwareEdgeScriptTrigger(self, vi, trigger_id):  # noqa: N802
        if self._defaults['ConfigureSoftwareEdgeScriptTrigger']['return'] != 0:
            return self._defaults['ConfigureSoftwareEdgeScriptTrigger']['return']
        return self._defaults['ConfigureSoftwareEdgeScriptTrigger']['return']

    def niFgen_ConfigureSoftwareEdgeStartTrigger(self, vi):  # noqa: N802
        if self._defaults['ConfigureSoftwareEdgeStartTrigger']['return'] != 0:
            return self._defaults['ConfigureSoftwareEdgeStartTrigger']['return']
        return self._defaults['ConfigureSoftwareEdgeStartTrigger']['return']

    def niFgen_ConfigureStandardWaveform(self, vi, channel_name, waveform, amplitude, dc_offset, frequency, start_phase):  # noqa: N802
        if self._defaults['ConfigureStandardWaveform']['return'] != 0:
            return self._defaults['ConfigureStandardWaveform']['return']
        return self._defaults['ConfigureStandardWaveform']['return']

    def niFgen_ConfigureSynchronization(self, vi, channel_name, synchronization_source):  # noqa: N802
        if self._defaults['ConfigureSynchronization']['return'] != 0:
            return self._defaults['ConfigureSynchronization']['return']
        return self._defaults['ConfigureSynchronization']['return']

    def niFgen_ConfigureTriggerMode(self, vi, channel_name, trigger_mode):  # noqa: N802
        if self._defaults['ConfigureTriggerMode']['return'] != 0:
            return self._defaults['ConfigureTriggerMode']['return']
        return self._defaults['ConfigureTriggerMode']['return']

    def niFgen_ConfigureTriggerSource(self, vi, channel_name, trigger_source):  # noqa: N802
        if self._defaults['ConfigureTriggerSource']['return'] != 0:
            return self._defaults['ConfigureTriggerSource']['return']
        return self._defaults['ConfigureTriggerSource']['return']

    def niFgen_ConfigureUpdateClockSource(self, vi, update_clock_source):  # noqa: N802
        if self._defaults['ConfigureUpdateClockSource']['return'] != 0:
            return self._defaults['ConfigureUpdateClockSource']['return']
        return self._defaults['ConfigureUpdateClockSource']['return']

    def niFgen_CreateAdvancedArbSequence(self, vi, sequence_length, waveform_handles_array, loop_counts_array, sample_counts_array, marker_location_array, coerced_markers_array, sequence_handle):  # noqa: N802
        if self._defaults['CreateAdvancedArbSequence']['return'] != 0:
            return self._defaults['CreateAdvancedArbSequence']['return']
        if self._defaults['CreateAdvancedArbSequence']['coercedMarkersArray'] is None:
            raise MockFunctionCallError("niFgen_CreateAdvancedArbSequence", param='coercedMarkersArray')
        a = self._defaults['CreateAdvancedArbSequence']['coercedMarkersArray']
        import sys
        if sys.version_info.major > 2 and type(a) is str:
            a = a.encode('ascii')
        for i in range(min(len(coerced_markers_array), len(a))):
            coerced_markers_array[i] = a[i]
        if self._defaults['CreateAdvancedArbSequence']['sequenceHandle'] is None:
            raise MockFunctionCallError("niFgen_CreateAdvancedArbSequence", param='sequenceHandle')
        sequence_handle.contents.value = self._defaults['CreateAdvancedArbSequence']['sequenceHandle']
        return self._defaults['CreateAdvancedArbSequence']['return']

    def niFgen_CreateArbSequence(self, vi, sequence_length, waveform_handles_array, loop_counts_array, sequence_handle):  # noqa: N802
        if self._defaults['CreateArbSequence']['return'] != 0:
            return self._defaults['CreateArbSequence']['return']
        if self._defaults['CreateArbSequence']['sequenceHandle'] is None:
            raise MockFunctionCallError("niFgen_CreateArbSequence", param='sequenceHandle')
        sequence_handle.contents.value = self._defaults['CreateArbSequence']['sequenceHandle']
        return self._defaults['CreateArbSequence']['return']

    def niFgen_CreateArbWaveform(self, vi, waveform_size, waveform_data_array, waveform_handle):  # noqa: N802
        if self._defaults['CreateArbWaveform']['return'] != 0:
            return self._defaults['CreateArbWaveform']['return']
        if self._defaults['CreateArbWaveform']['waveformHandle'] is None:
            raise MockFunctionCallError("niFgen_CreateArbWaveform", param='waveformHandle')
        waveform_handle.contents.value = self._defaults['CreateArbWaveform']['waveformHandle']
        return self._defaults['CreateArbWaveform']['return']

    def niFgen_CreateBinary16ArbWaveform(self, vi, waveform_size, waveform_data_array, waveform_handle):  # noqa: N802
        if self._defaults['CreateBinary16ArbWaveform']['return'] != 0:
            return self._defaults['CreateBinary16ArbWaveform']['return']
        if self._defaults['CreateBinary16ArbWaveform']['waveformHandle'] is None:
            raise MockFunctionCallError("niFgen_CreateBinary16ArbWaveform", param='waveformHandle')
        waveform_handle.contents.value = self._defaults['CreateBinary16ArbWaveform']['waveformHandle']
        return self._defaults['CreateBinary16ArbWaveform']['return']

    def niFgen_CreateFreqList(self, vi, waveform, frequency_list_length, frequency_array, duration_array, frequency_list_handle):  # noqa: N802
        if self._defaults['CreateFreqList']['return'] != 0:
            return self._defaults['CreateFreqList']['return']
        if self._defaults['CreateFreqList']['frequencyListHandle'] is None:
            raise MockFunctionCallError("niFgen_CreateFreqList", param='frequencyListHandle')
        frequency_list_handle.contents.value = self._defaults['CreateFreqList']['frequencyListHandle']
        return self._defaults['CreateFreqList']['return']

    def niFgen_CreateWaveformF64(self, vi, channel_name, waveform_size, waveform_data_array, waveform_handle):  # noqa: N802
        if self._defaults['CreateWaveformF64']['return'] != 0:
            return self._defaults['CreateWaveformF64']['return']
        if self._defaults['CreateWaveformF64']['waveformHandle'] is None:
            raise MockFunctionCallError("niFgen_CreateWaveformF64", param='waveformHandle')
        waveform_handle.contents.value = self._defaults['CreateWaveformF64']['waveformHandle']
        return self._defaults['CreateWaveformF64']['return']

    def niFgen_CreateWaveformFromFileF64(self, vi, channel_name, file_name, byte_order, waveform_handle):  # noqa: N802
        if self._defaults['CreateWaveformFromFileF64']['return'] != 0:
            return self._defaults['CreateWaveformFromFileF64']['return']
        if self._defaults['CreateWaveformFromFileF64']['waveformHandle'] is None:
            raise MockFunctionCallError("niFgen_CreateWaveformFromFileF64", param='waveformHandle')
        waveform_handle.contents.value = self._defaults['CreateWaveformFromFileF64']['waveformHandle']
        return self._defaults['CreateWaveformFromFileF64']['return']

    def niFgen_CreateWaveformFromFileHWS(self, vi, channel_name, file_name, use_rate_from_waveform, use_gain_and_offset_from_waveform, waveform_handle):  # noqa: N802
        if self._defaults['CreateWaveformFromFileHWS']['return'] != 0:
            return self._defaults['CreateWaveformFromFileHWS']['return']
        if self._defaults['CreateWaveformFromFileHWS']['waveformHandle'] is None:
            raise MockFunctionCallError("niFgen_CreateWaveformFromFileHWS", param='waveformHandle')
        waveform_handle.contents.value = self._defaults['CreateWaveformFromFileHWS']['waveformHandle']
        return self._defaults['CreateWaveformFromFileHWS']['return']

    def niFgen_CreateWaveformFromFileI16(self, vi, channel_name, file_name, byte_order, waveform_handle):  # noqa: N802
        if self._defaults['CreateWaveformFromFileI16']['return'] != 0:
            return self._defaults['CreateWaveformFromFileI16']['return']
        if self._defaults['CreateWaveformFromFileI16']['waveformHandle'] is None:
            raise MockFunctionCallError("niFgen_CreateWaveformFromFileI16", param='waveformHandle')
        waveform_handle.contents.value = self._defaults['CreateWaveformFromFileI16']['waveformHandle']
        return self._defaults['CreateWaveformFromFileI16']['return']

    def niFgen_CreateWaveformI16(self, vi, channel_name, waveform_size, waveform_data_array, waveform_handle):  # noqa: N802
        if self._defaults['CreateWaveformI16']['return'] != 0:
            return self._defaults['CreateWaveformI16']['return']
        if self._defaults['CreateWaveformI16']['waveformHandle'] is None:
            raise MockFunctionCallError("niFgen_CreateWaveformI16", param='waveformHandle')
        waveform_handle.contents.value = self._defaults['CreateWaveformI16']['waveformHandle']
        return self._defaults['CreateWaveformI16']['return']

    def niFgen_DefineUserStandardWaveform(self, vi, channel_name, waveform_size, waveform_data_array):  # noqa: N802
        if self._defaults['DefineUserStandardWaveform']['return'] != 0:
            return self._defaults['DefineUserStandardWaveform']['return']
        return self._defaults['DefineUserStandardWaveform']['return']

    def niFgen_DeleteNamedWaveform(self, vi, channel_name, waveform_name):  # noqa: N802
        if self._defaults['DeleteNamedWaveform']['return'] != 0:
            return self._defaults['DeleteNamedWaveform']['return']
        return self._defaults['DeleteNamedWaveform']['return']

    def niFgen_DeleteScript(self, vi, channel_name, script_name):  # noqa: N802
        if self._defaults['DeleteScript']['return'] != 0:
            return self._defaults['DeleteScript']['return']
        return self._defaults['DeleteScript']['return']

    def niFgen_Disable(self, vi):  # noqa: N802
        if self._defaults['Disable']['return'] != 0:
            return self._defaults['Disable']['return']
        return self._defaults['Disable']['return']

    def niFgen_DisableAnalogFilter(self, vi, channel_name):  # noqa: N802
        if self._defaults['DisableAnalogFilter']['return'] != 0:
            return self._defaults['DisableAnalogFilter']['return']
        return self._defaults['DisableAnalogFilter']['return']

    def niFgen_DisableDigitalFilter(self, vi, channel_name):  # noqa: N802
        if self._defaults['DisableDigitalFilter']['return'] != 0:
            return self._defaults['DisableDigitalFilter']['return']
        return self._defaults['DisableDigitalFilter']['return']

    def niFgen_DisableDigitalPatterning(self, vi, channel_name):  # noqa: N802
        if self._defaults['DisableDigitalPatterning']['return'] != 0:
            return self._defaults['DisableDigitalPatterning']['return']
        return self._defaults['DisableDigitalPatterning']['return']

    def niFgen_DisableScriptTrigger(self, vi, trigger_id):  # noqa: N802
        if self._defaults['DisableScriptTrigger']['return'] != 0:
            return self._defaults['DisableScriptTrigger']['return']
        return self._defaults['DisableScriptTrigger']['return']

    def niFgen_DisableStartTrigger(self, vi):  # noqa: N802
        if self._defaults['DisableStartTrigger']['return'] != 0:
            return self._defaults['DisableStartTrigger']['return']
        return self._defaults['DisableStartTrigger']['return']

    def niFgen_EnableAnalogFilter(self, vi, channel_name, filter_correction_frequency):  # noqa: N802
        if self._defaults['EnableAnalogFilter']['return'] != 0:
            return self._defaults['EnableAnalogFilter']['return']
        return self._defaults['EnableAnalogFilter']['return']

    def niFgen_EnableDigitalFilter(self, vi, channel_name):  # noqa: N802
        if self._defaults['EnableDigitalFilter']['return'] != 0:
            return self._defaults['EnableDigitalFilter']['return']
        return self._defaults['EnableDigitalFilter']['return']

    def niFgen_EnableDigitalPatterning(self, vi, channel_name):  # noqa: N802
        if self._defaults['EnableDigitalPatterning']['return'] != 0:
            return self._defaults['EnableDigitalPatterning']['return']
        return self._defaults['EnableDigitalPatterning']['return']

    def niFgen_ErrorHandler(self, vi, error_code, error_message):  # noqa: N802
        if self._defaults['ErrorHandler']['return'] != 0:
            return self._defaults['ErrorHandler']['return']
        if self._defaults['ErrorHandler']['errorMessage'] is None:
            raise MockFunctionCallError("niFgen_ErrorHandler", param='errorMessage')
        a = self._defaults['ErrorHandler']['errorMessage']
        import sys
        if sys.version_info.major > 2 and type(a) is str:
            a = a.encode('ascii')
        for i in range(min(len(error_message), len(a))):
            error_message[i] = a[i]
        return self._defaults['ErrorHandler']['return']

    def niFgen_ExportSignal(self, vi, signal, signal_identifier, output_terminal):  # noqa: N802
        if self._defaults['ExportSignal']['return'] != 0:
            return self._defaults['ExportSignal']['return']
        return self._defaults['ExportSignal']['return']

    def niFgen_GetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViBoolean']['return'] != 0:
            return self._defaults['GetAttributeViBoolean']['return']
        if self._defaults['GetAttributeViBoolean']['attributeValue'] is None:
            raise MockFunctionCallError("niFgen_GetAttributeViBoolean", param='attributeValue')
        attribute_value.contents.value = self._defaults['GetAttributeViBoolean']['attributeValue']
        return self._defaults['GetAttributeViBoolean']['return']

    def niFgen_GetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViInt32']['return'] != 0:
            return self._defaults['GetAttributeViInt32']['return']
        if self._defaults['GetAttributeViInt32']['attributeValue'] is None:
            raise MockFunctionCallError("niFgen_GetAttributeViInt32", param='attributeValue')
        attribute_value.contents.value = self._defaults['GetAttributeViInt32']['attributeValue']
        return self._defaults['GetAttributeViInt32']['return']

    def niFgen_GetAttributeViInt64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViInt64']['return'] != 0:
            return self._defaults['GetAttributeViInt64']['return']
        if self._defaults['GetAttributeViInt64']['attributeValue'] is None:
            raise MockFunctionCallError("niFgen_GetAttributeViInt64", param='attributeValue')
        attribute_value.contents.value = self._defaults['GetAttributeViInt64']['attributeValue']
        return self._defaults['GetAttributeViInt64']['return']

    def niFgen_GetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViReal64']['return'] != 0:
            return self._defaults['GetAttributeViReal64']['return']
        if self._defaults['GetAttributeViReal64']['attributeValue'] is None:
            raise MockFunctionCallError("niFgen_GetAttributeViReal64", param='attributeValue')
        attribute_value.contents.value = self._defaults['GetAttributeViReal64']['attributeValue']
        return self._defaults['GetAttributeViReal64']['return']

    def niFgen_GetAttributeViString(self, vi, channel_name, attribute_id, array_size, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViString']['return'] != 0:
            return self._defaults['GetAttributeViString']['return']
        if self._defaults['GetAttributeViString']['attributeValue'] is None:
            raise MockFunctionCallError("niFgen_GetAttributeViString", param='attributeValue')
        if array_size.value == 0:
            return len(self._defaults['GetAttributeViString']['attributeValue'])
        attribute_value.value = self._defaults['GetAttributeViString']['attributeValue'].encode('ascii')
        return self._defaults['GetAttributeViString']['return']

    def niFgen_GetError(self, vi, error_code, error_description_buffer_size, error_description):  # noqa: N802
        if self._defaults['GetError']['return'] != 0:
            return self._defaults['GetError']['return']
        if self._defaults['GetError']['errorCode'] is None:
            raise MockFunctionCallError("niFgen_GetError", param='errorCode')
        error_code.contents.value = self._defaults['GetError']['errorCode']
        if self._defaults['GetError']['errorDescription'] is None:
            raise MockFunctionCallError("niFgen_GetError", param='errorDescription')
        if error_description_buffer_size.value == 0:
            return len(self._defaults['GetError']['errorDescription'])
        error_description.value = self._defaults['GetError']['errorDescription'].encode('ascii')
        return self._defaults['GetError']['return']

    def niFgen_GetFIRFilterCoefficients(self, vi, channel_name, array_size, coefficients_array, number_of_coefficients_read):  # noqa: N802
        if self._defaults['GetFIRFilterCoefficients']['return'] != 0:
            return self._defaults['GetFIRFilterCoefficients']['return']
        return self._defaults['GetFIRFilterCoefficients']['return']

    def niFgen_GetHardwareState(self, vi, state):  # noqa: N802
        if self._defaults['GetHardwareState']['return'] != 0:
            return self._defaults['GetHardwareState']['return']
        if self._defaults['GetHardwareState']['state'] is None:
            raise MockFunctionCallError("niFgen_GetHardwareState", param='state')
        state.contents.value = self._defaults['GetHardwareState']['state']
        return self._defaults['GetHardwareState']['return']

    def niFgen_GetSelfCalLastDateAndTime(self, vi, year, month, day, hour, minute):  # noqa: N802
        if self._defaults['GetSelfCalLastDateAndTime']['return'] != 0:
            return self._defaults['GetSelfCalLastDateAndTime']['return']
        if self._defaults['GetSelfCalLastDateAndTime']['Year'] is None:
            raise MockFunctionCallError("niFgen_GetSelfCalLastDateAndTime", param='Year')
        year.contents.value = self._defaults['GetSelfCalLastDateAndTime']['Year']
        if self._defaults['GetSelfCalLastDateAndTime']['Month'] is None:
            raise MockFunctionCallError("niFgen_GetSelfCalLastDateAndTime", param='Month')
        month.contents.value = self._defaults['GetSelfCalLastDateAndTime']['Month']
        if self._defaults['GetSelfCalLastDateAndTime']['Day'] is None:
            raise MockFunctionCallError("niFgen_GetSelfCalLastDateAndTime", param='Day')
        day.contents.value = self._defaults['GetSelfCalLastDateAndTime']['Day']
        if self._defaults['GetSelfCalLastDateAndTime']['Hour'] is None:
            raise MockFunctionCallError("niFgen_GetSelfCalLastDateAndTime", param='Hour')
        hour.contents.value = self._defaults['GetSelfCalLastDateAndTime']['Hour']
        if self._defaults['GetSelfCalLastDateAndTime']['Minute'] is None:
            raise MockFunctionCallError("niFgen_GetSelfCalLastDateAndTime", param='Minute')
        minute.contents.value = self._defaults['GetSelfCalLastDateAndTime']['Minute']
        return self._defaults['GetSelfCalLastDateAndTime']['return']

    def niFgen_GetSelfCalLastTemp(self, vi, temperature):  # noqa: N802
        if self._defaults['GetSelfCalLastTemp']['return'] != 0:
            return self._defaults['GetSelfCalLastTemp']['return']
        if self._defaults['GetSelfCalLastTemp']['Temperature'] is None:
            raise MockFunctionCallError("niFgen_GetSelfCalLastTemp", param='Temperature')
        temperature.contents.value = self._defaults['GetSelfCalLastTemp']['Temperature']
        return self._defaults['GetSelfCalLastTemp']['return']

    def niFgen_GetSelfCalSupported(self, vi, self_cal_supported):  # noqa: N802
        if self._defaults['GetSelfCalSupported']['return'] != 0:
            return self._defaults['GetSelfCalSupported']['return']
        if self._defaults['GetSelfCalSupported']['selfCalSupported'] is None:
            raise MockFunctionCallError("niFgen_GetSelfCalSupported", param='selfCalSupported')
        self_cal_supported.contents.value = self._defaults['GetSelfCalSupported']['selfCalSupported']
        return self._defaults['GetSelfCalSupported']['return']

    def niFgen_InitWithOptions(self, resource_name, id_query, reset_device, option_string, vi):  # noqa: N802
        if self._defaults['InitWithOptions']['return'] != 0:
            return self._defaults['InitWithOptions']['return']
        if self._defaults['InitWithOptions']['vi'] is None:
            raise MockFunctionCallError("niFgen_InitWithOptions", param='vi')
        vi.contents.value = self._defaults['InitWithOptions']['vi']
        return self._defaults['InitWithOptions']['return']

    def niFgen_InitializeAnalogOutputCalibration(self, vi):  # noqa: N802
        if self._defaults['InitializeAnalogOutputCalibration']['return'] != 0:
            return self._defaults['InitializeAnalogOutputCalibration']['return']
        return self._defaults['InitializeAnalogOutputCalibration']['return']

    def niFgen_InitializeCalADCCalibration(self, vi):  # noqa: N802
        if self._defaults['InitializeCalADCCalibration']['return'] != 0:
            return self._defaults['InitializeCalADCCalibration']['return']
        return self._defaults['InitializeCalADCCalibration']['return']

    def niFgen_InitializeFlatnessCalibration(self, vi):  # noqa: N802
        if self._defaults['InitializeFlatnessCalibration']['return'] != 0:
            return self._defaults['InitializeFlatnessCalibration']['return']
        return self._defaults['InitializeFlatnessCalibration']['return']

    def niFgen_InitializeOscillatorFrequencyCalibration(self, vi):  # noqa: N802
        if self._defaults['InitializeOscillatorFrequencyCalibration']['return'] != 0:
            return self._defaults['InitializeOscillatorFrequencyCalibration']['return']
        return self._defaults['InitializeOscillatorFrequencyCalibration']['return']

    def niFgen_InitializeWithChannels(self, resource_name, channel_name, reset_device, option_string, vi):  # noqa: N802
        if self._defaults['InitializeWithChannels']['return'] != 0:
            return self._defaults['InitializeWithChannels']['return']
        if self._defaults['InitializeWithChannels']['vi'] is None:
            raise MockFunctionCallError("niFgen_InitializeWithChannels", param='vi')
        vi.contents.value = self._defaults['InitializeWithChannels']['vi']
        return self._defaults['InitializeWithChannels']['return']

    def niFgen_InitiateGeneration(self, vi):  # noqa: N802
        if self._defaults['InitiateGeneration']['return'] != 0:
            return self._defaults['InitiateGeneration']['return']
        return self._defaults['InitiateGeneration']['return']

    def niFgen_IsDone(self, vi, done):  # noqa: N802
        if self._defaults['IsDone']['return'] != 0:
            return self._defaults['IsDone']['return']
        if self._defaults['IsDone']['Done'] is None:
            raise MockFunctionCallError("niFgen_IsDone", param='Done')
        done.contents.value = self._defaults['IsDone']['Done']
        return self._defaults['IsDone']['return']

    def niFgen_ManualEnableP2PStream(self, vi, endpoint_name):  # noqa: N802
        if self._defaults['ManualEnableP2PStream']['return'] != 0:
            return self._defaults['ManualEnableP2PStream']['return']
        return self._defaults['ManualEnableP2PStream']['return']

    def niFgen_QueryArbSeqCapabilities(self, vi, maximum_number_of_sequences, minimum_sequence_length, maximum_sequence_length, maximum_loop_count):  # noqa: N802
        if self._defaults['QueryArbSeqCapabilities']['return'] != 0:
            return self._defaults['QueryArbSeqCapabilities']['return']
        if self._defaults['QueryArbSeqCapabilities']['maximumNumberOfSequences'] is None:
            raise MockFunctionCallError("niFgen_QueryArbSeqCapabilities", param='maximumNumberOfSequences')
        maximum_number_of_sequences.contents.value = self._defaults['QueryArbSeqCapabilities']['maximumNumberOfSequences']
        if self._defaults['QueryArbSeqCapabilities']['minimumSequenceLength'] is None:
            raise MockFunctionCallError("niFgen_QueryArbSeqCapabilities", param='minimumSequenceLength')
        minimum_sequence_length.contents.value = self._defaults['QueryArbSeqCapabilities']['minimumSequenceLength']
        if self._defaults['QueryArbSeqCapabilities']['maximumSequenceLength'] is None:
            raise MockFunctionCallError("niFgen_QueryArbSeqCapabilities", param='maximumSequenceLength')
        maximum_sequence_length.contents.value = self._defaults['QueryArbSeqCapabilities']['maximumSequenceLength']
        if self._defaults['QueryArbSeqCapabilities']['maximumLoopCount'] is None:
            raise MockFunctionCallError("niFgen_QueryArbSeqCapabilities", param='maximumLoopCount')
        maximum_loop_count.contents.value = self._defaults['QueryArbSeqCapabilities']['maximumLoopCount']
        return self._defaults['QueryArbSeqCapabilities']['return']

    def niFgen_QueryArbWfmCapabilities(self, vi, maximum_number_of_waveforms, waveform_quantum, minimum_waveform_size, maximum_waveform_size):  # noqa: N802
        if self._defaults['QueryArbWfmCapabilities']['return'] != 0:
            return self._defaults['QueryArbWfmCapabilities']['return']
        if self._defaults['QueryArbWfmCapabilities']['maximumNumberOfWaveforms'] is None:
            raise MockFunctionCallError("niFgen_QueryArbWfmCapabilities", param='maximumNumberOfWaveforms')
        maximum_number_of_waveforms.contents.value = self._defaults['QueryArbWfmCapabilities']['maximumNumberOfWaveforms']
        if self._defaults['QueryArbWfmCapabilities']['waveformQuantum'] is None:
            raise MockFunctionCallError("niFgen_QueryArbWfmCapabilities", param='waveformQuantum')
        waveform_quantum.contents.value = self._defaults['QueryArbWfmCapabilities']['waveformQuantum']
        if self._defaults['QueryArbWfmCapabilities']['minimumWaveformSize'] is None:
            raise MockFunctionCallError("niFgen_QueryArbWfmCapabilities", param='minimumWaveformSize')
        minimum_waveform_size.contents.value = self._defaults['QueryArbWfmCapabilities']['minimumWaveformSize']
        if self._defaults['QueryArbWfmCapabilities']['maximumWaveformSize'] is None:
            raise MockFunctionCallError("niFgen_QueryArbWfmCapabilities", param='maximumWaveformSize')
        maximum_waveform_size.contents.value = self._defaults['QueryArbWfmCapabilities']['maximumWaveformSize']
        return self._defaults['QueryArbWfmCapabilities']['return']

    def niFgen_QueryFreqListCapabilities(self, vi, maximum_number_of_freq_lists, minimum_frequency_list_length, maximum_frequency_list_length, minimum_frequency_list_duration, maximum_frequency_list_duration, frequency_list_duration_quantum):  # noqa: N802
        if self._defaults['QueryFreqListCapabilities']['return'] != 0:
            return self._defaults['QueryFreqListCapabilities']['return']
        if self._defaults['QueryFreqListCapabilities']['maximumNumberOfFreqLists'] is None:
            raise MockFunctionCallError("niFgen_QueryFreqListCapabilities", param='maximumNumberOfFreqLists')
        maximum_number_of_freq_lists.contents.value = self._defaults['QueryFreqListCapabilities']['maximumNumberOfFreqLists']
        if self._defaults['QueryFreqListCapabilities']['minimumFrequencyListLength'] is None:
            raise MockFunctionCallError("niFgen_QueryFreqListCapabilities", param='minimumFrequencyListLength')
        minimum_frequency_list_length.contents.value = self._defaults['QueryFreqListCapabilities']['minimumFrequencyListLength']
        if self._defaults['QueryFreqListCapabilities']['maximumFrequencyListLength'] is None:
            raise MockFunctionCallError("niFgen_QueryFreqListCapabilities", param='maximumFrequencyListLength')
        maximum_frequency_list_length.contents.value = self._defaults['QueryFreqListCapabilities']['maximumFrequencyListLength']
        if self._defaults['QueryFreqListCapabilities']['minimumFrequencyListDuration'] is None:
            raise MockFunctionCallError("niFgen_QueryFreqListCapabilities", param='minimumFrequencyListDuration')
        minimum_frequency_list_duration.contents.value = self._defaults['QueryFreqListCapabilities']['minimumFrequencyListDuration']
        if self._defaults['QueryFreqListCapabilities']['maximumFrequencyListDuration'] is None:
            raise MockFunctionCallError("niFgen_QueryFreqListCapabilities", param='maximumFrequencyListDuration')
        maximum_frequency_list_duration.contents.value = self._defaults['QueryFreqListCapabilities']['maximumFrequencyListDuration']
        if self._defaults['QueryFreqListCapabilities']['frequencyListDurationQuantum'] is None:
            raise MockFunctionCallError("niFgen_QueryFreqListCapabilities", param='frequencyListDurationQuantum')
        frequency_list_duration_quantum.contents.value = self._defaults['QueryFreqListCapabilities']['frequencyListDurationQuantum']
        return self._defaults['QueryFreqListCapabilities']['return']

    def niFgen_ReadCalADC(self, vi, number_of_reads_to_average, return_calibrated_value, cal_adc_value):  # noqa: N802
        if self._defaults['ReadCalADC']['return'] != 0:
            return self._defaults['ReadCalADC']['return']
        if self._defaults['ReadCalADC']['calAdcValue'] is None:
            raise MockFunctionCallError("niFgen_ReadCalADC", param='calAdcValue')
        cal_adc_value.contents.value = self._defaults['ReadCalADC']['calAdcValue']
        return self._defaults['ReadCalADC']['return']

    def niFgen_ReadCurrentTemperature(self, vi, temperature):  # noqa: N802
        if self._defaults['ReadCurrentTemperature']['return'] != 0:
            return self._defaults['ReadCurrentTemperature']['return']
        if self._defaults['ReadCurrentTemperature']['Temperature'] is None:
            raise MockFunctionCallError("niFgen_ReadCurrentTemperature", param='Temperature')
        temperature.contents.value = self._defaults['ReadCurrentTemperature']['Temperature']
        return self._defaults['ReadCurrentTemperature']['return']

    def niFgen_ResetAttribute(self, vi, channel_name, attribute_id):  # noqa: N802
        if self._defaults['ResetAttribute']['return'] != 0:
            return self._defaults['ResetAttribute']['return']
        return self._defaults['ResetAttribute']['return']

    def niFgen_ResetDevice(self, vi):  # noqa: N802
        if self._defaults['ResetDevice']['return'] != 0:
            return self._defaults['ResetDevice']['return']
        return self._defaults['ResetDevice']['return']

    def niFgen_ResetWithDefaults(self, vi):  # noqa: N802
        if self._defaults['ResetWithDefaults']['return'] != 0:
            return self._defaults['ResetWithDefaults']['return']
        return self._defaults['ResetWithDefaults']['return']

    def niFgen_RouteSignalOut(self, vi, channel_name, route_signal_from, route_signal_to):  # noqa: N802
        if self._defaults['RouteSignalOut']['return'] != 0:
            return self._defaults['RouteSignalOut']['return']
        return self._defaults['RouteSignalOut']['return']

    def niFgen_SelfCal(self, vi):  # noqa: N802
        if self._defaults['SelfCal']['return'] != 0:
            return self._defaults['SelfCal']['return']
        return self._defaults['SelfCal']['return']

    def niFgen_SendSoftwareEdgeTrigger(self, vi, trigger, trigger_id):  # noqa: N802
        if self._defaults['SendSoftwareEdgeTrigger']['return'] != 0:
            return self._defaults['SendSoftwareEdgeTrigger']['return']
        return self._defaults['SendSoftwareEdgeTrigger']['return']

    def niFgen_SendSoftwareTrigger(self, vi):  # noqa: N802
        if self._defaults['SendSoftwareTrigger']['return'] != 0:
            return self._defaults['SendSoftwareTrigger']['return']
        return self._defaults['SendSoftwareTrigger']['return']

    def niFgen_SetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViBoolean']['return'] != 0:
            return self._defaults['SetAttributeViBoolean']['return']
        return self._defaults['SetAttributeViBoolean']['return']

    def niFgen_SetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViInt32']['return'] != 0:
            return self._defaults['SetAttributeViInt32']['return']
        return self._defaults['SetAttributeViInt32']['return']

    def niFgen_SetAttributeViInt64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViInt64']['return'] != 0:
            return self._defaults['SetAttributeViInt64']['return']
        return self._defaults['SetAttributeViInt64']['return']

    def niFgen_SetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViReal64']['return'] != 0:
            return self._defaults['SetAttributeViReal64']['return']
        return self._defaults['SetAttributeViReal64']['return']

    def niFgen_SetAttributeViString(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViString']['return'] != 0:
            return self._defaults['SetAttributeViString']['return']
        return self._defaults['SetAttributeViString']['return']

    def niFgen_SetNamedWaveformNextWritePosition(self, vi, channel_name, waveform_name, relative_to, offset):  # noqa: N802
        if self._defaults['SetNamedWaveformNextWritePosition']['return'] != 0:
            return self._defaults['SetNamedWaveformNextWritePosition']['return']
        return self._defaults['SetNamedWaveformNextWritePosition']['return']

    def niFgen_SetWaveformNextWritePosition(self, vi, channel_name, waveform_handle, relative_to, offset):  # noqa: N802
        if self._defaults['SetWaveformNextWritePosition']['return'] != 0:
            return self._defaults['SetWaveformNextWritePosition']['return']
        return self._defaults['SetWaveformNextWritePosition']['return']

    def niFgen_WaitUntilDone(self, vi, max_time):  # noqa: N802
        if self._defaults['WaitUntilDone']['return'] != 0:
            return self._defaults['WaitUntilDone']['return']
        return self._defaults['WaitUntilDone']['return']

    def niFgen_WriteBinary16AnalogStaticValue(self, vi, channel_name, value):  # noqa: N802
        if self._defaults['WriteBinary16AnalogStaticValue']['return'] != 0:
            return self._defaults['WriteBinary16AnalogStaticValue']['return']
        return self._defaults['WriteBinary16AnalogStaticValue']['return']

    def niFgen_WriteBinary16Waveform(self, vi, channel_name, waveform_handle, size, data):  # noqa: N802
        if self._defaults['WriteBinary16Waveform']['return'] != 0:
            return self._defaults['WriteBinary16Waveform']['return']
        return self._defaults['WriteBinary16Waveform']['return']

    def niFgen_WriteNamedWaveformF64(self, vi, channel_name, waveform_name, size, data):  # noqa: N802
        if self._defaults['WriteNamedWaveformF64']['return'] != 0:
            return self._defaults['WriteNamedWaveformF64']['return']
        return self._defaults['WriteNamedWaveformF64']['return']

    def niFgen_WriteNamedWaveformI16(self, vi, channel_name, waveform_name, size, data):  # noqa: N802
        if self._defaults['WriteNamedWaveformI16']['return'] != 0:
            return self._defaults['WriteNamedWaveformI16']['return']
        return self._defaults['WriteNamedWaveformI16']['return']

    def niFgen_WriteP2PEndpointI16(self, vi, endpoint_name, number_of_samples, endpoint_data):  # noqa: N802
        if self._defaults['WriteP2PEndpointI16']['return'] != 0:
            return self._defaults['WriteP2PEndpointI16']['return']
        return self._defaults['WriteP2PEndpointI16']['return']

    def niFgen_WriteScript(self, vi, channel_name, script):  # noqa: N802
        if self._defaults['WriteScript']['return'] != 0:
            return self._defaults['WriteScript']['return']
        return self._defaults['WriteScript']['return']

    def niFgen_WriteWaveform(self, vi, channel_name, waveform_handle, size, data):  # noqa: N802
        if self._defaults['WriteWaveform']['return'] != 0:
            return self._defaults['WriteWaveform']['return']
        return self._defaults['WriteWaveform']['return']

    def niFgen_close(self, vi):  # noqa: N802
        if self._defaults['close']['return'] != 0:
            return self._defaults['close']['return']
        return self._defaults['close']['return']

    def niFgen_error_message(self, vi, error_code, error_message):  # noqa: N802
        if self._defaults['error_message']['return'] != 0:
            return self._defaults['error_message']['return']
        if self._defaults['error_message']['errorMessage'] is None:
            raise MockFunctionCallError("niFgen_error_message", param='errorMessage')
        a = self._defaults['error_message']['errorMessage']
        import sys
        if sys.version_info.major > 2 and type(a) is str:
            a = a.encode('ascii')
        for i in range(min(len(error_message), len(a))):
            error_message[i] = a[i]
        return self._defaults['error_message']['return']

    def niFgen_reset(self, vi):  # noqa: N802
        if self._defaults['reset']['return'] != 0:
            return self._defaults['reset']['return']
        return self._defaults['reset']['return']

    def niFgen_self_test(self, vi, self_test_result, self_test_message):  # noqa: N802
        if self._defaults['self_test']['return'] != 0:
            return self._defaults['self_test']['return']
        if self._defaults['self_test']['selfTestResult'] is None:
            raise MockFunctionCallError("niFgen_self_test", param='selfTestResult')
        self_test_result.contents.value = self._defaults['self_test']['selfTestResult']
        if self._defaults['self_test']['selfTestMessage'] is None:
            raise MockFunctionCallError("niFgen_self_test", param='selfTestMessage')
        a = self._defaults['self_test']['selfTestMessage']
        import sys
        if sys.version_info.major > 2 and type(a) is str:
            a = a.encode('ascii')
        for i in range(min(len(self_test_message), len(a))):
            self_test_message[i] = a[i]
        return self._defaults['self_test']['return']

    # Helper function to setup Mock object with default side effects and return values
    def set_side_effects_and_return_values(self, mock_library):
        mock_library.niFgen_AbortGeneration.side_effect = MockFunctionCallError("niFgen_AbortGeneration")
        mock_library.niFgen_AbortGeneration.return_value = 0
        mock_library.niFgen_AdjustSampleClockRelativeDelay.side_effect = MockFunctionCallError("niFgen_AdjustSampleClockRelativeDelay")
        mock_library.niFgen_AdjustSampleClockRelativeDelay.return_value = 0
        mock_library.niFgen_AllocateNamedWaveform.side_effect = MockFunctionCallError("niFgen_AllocateNamedWaveform")
        mock_library.niFgen_AllocateNamedWaveform.return_value = 0
        mock_library.niFgen_AllocateWaveform.side_effect = MockFunctionCallError("niFgen_AllocateWaveform")
        mock_library.niFgen_AllocateWaveform.return_value = 0
        mock_library.niFgen_CheckAttributeViBoolean.side_effect = MockFunctionCallError("niFgen_CheckAttributeViBoolean")
        mock_library.niFgen_CheckAttributeViBoolean.return_value = 0
        mock_library.niFgen_CheckAttributeViInt32.side_effect = MockFunctionCallError("niFgen_CheckAttributeViInt32")
        mock_library.niFgen_CheckAttributeViInt32.return_value = 0
        mock_library.niFgen_CheckAttributeViInt64.side_effect = MockFunctionCallError("niFgen_CheckAttributeViInt64")
        mock_library.niFgen_CheckAttributeViInt64.return_value = 0
        mock_library.niFgen_CheckAttributeViReal64.side_effect = MockFunctionCallError("niFgen_CheckAttributeViReal64")
        mock_library.niFgen_CheckAttributeViReal64.return_value = 0
        mock_library.niFgen_CheckAttributeViSession.side_effect = MockFunctionCallError("niFgen_CheckAttributeViSession")
        mock_library.niFgen_CheckAttributeViSession.return_value = 0
        mock_library.niFgen_CheckAttributeViString.side_effect = MockFunctionCallError("niFgen_CheckAttributeViString")
        mock_library.niFgen_CheckAttributeViString.return_value = 0
        mock_library.niFgen_ClearArbMemory.side_effect = MockFunctionCallError("niFgen_ClearArbMemory")
        mock_library.niFgen_ClearArbMemory.return_value = 0
        mock_library.niFgen_ClearArbSequence.side_effect = MockFunctionCallError("niFgen_ClearArbSequence")
        mock_library.niFgen_ClearArbSequence.return_value = 0
        mock_library.niFgen_ClearArbWaveform.side_effect = MockFunctionCallError("niFgen_ClearArbWaveform")
        mock_library.niFgen_ClearArbWaveform.return_value = 0
        mock_library.niFgen_ClearFreqList.side_effect = MockFunctionCallError("niFgen_ClearFreqList")
        mock_library.niFgen_ClearFreqList.return_value = 0
        mock_library.niFgen_ClearUserStandardWaveform.side_effect = MockFunctionCallError("niFgen_ClearUserStandardWaveform")
        mock_library.niFgen_ClearUserStandardWaveform.return_value = 0
        mock_library.niFgen_Commit.side_effect = MockFunctionCallError("niFgen_Commit")
        mock_library.niFgen_Commit.return_value = 0
        mock_library.niFgen_ConfigureAmplitude.side_effect = MockFunctionCallError("niFgen_ConfigureAmplitude")
        mock_library.niFgen_ConfigureAmplitude.return_value = 0
        mock_library.niFgen_ConfigureArbSequence.side_effect = MockFunctionCallError("niFgen_ConfigureArbSequence")
        mock_library.niFgen_ConfigureArbSequence.return_value = 0
        mock_library.niFgen_ConfigureArbWaveform.side_effect = MockFunctionCallError("niFgen_ConfigureArbWaveform")
        mock_library.niFgen_ConfigureArbWaveform.return_value = 0
        mock_library.niFgen_ConfigureChannels.side_effect = MockFunctionCallError("niFgen_ConfigureChannels")
        mock_library.niFgen_ConfigureChannels.return_value = 0
        mock_library.niFgen_ConfigureClockMode.side_effect = MockFunctionCallError("niFgen_ConfigureClockMode")
        mock_library.niFgen_ConfigureClockMode.return_value = 0
        mock_library.niFgen_ConfigureCustomFIRFilterCoefficients.side_effect = MockFunctionCallError("niFgen_ConfigureCustomFIRFilterCoefficients")
        mock_library.niFgen_ConfigureCustomFIRFilterCoefficients.return_value = 0
        mock_library.niFgen_ConfigureDigitalEdgeScriptTrigger.side_effect = MockFunctionCallError("niFgen_ConfigureDigitalEdgeScriptTrigger")
        mock_library.niFgen_ConfigureDigitalEdgeScriptTrigger.return_value = 0
        mock_library.niFgen_ConfigureDigitalEdgeStartTrigger.side_effect = MockFunctionCallError("niFgen_ConfigureDigitalEdgeStartTrigger")
        mock_library.niFgen_ConfigureDigitalEdgeStartTrigger.return_value = 0
        mock_library.niFgen_ConfigureDigitalLevelScriptTrigger.side_effect = MockFunctionCallError("niFgen_ConfigureDigitalLevelScriptTrigger")
        mock_library.niFgen_ConfigureDigitalLevelScriptTrigger.return_value = 0
        mock_library.niFgen_ConfigureFreqList.side_effect = MockFunctionCallError("niFgen_ConfigureFreqList")
        mock_library.niFgen_ConfigureFreqList.return_value = 0
        mock_library.niFgen_ConfigureFrequency.side_effect = MockFunctionCallError("niFgen_ConfigureFrequency")
        mock_library.niFgen_ConfigureFrequency.return_value = 0
        mock_library.niFgen_ConfigureGain.side_effect = MockFunctionCallError("niFgen_ConfigureGain")
        mock_library.niFgen_ConfigureGain.return_value = 0
        mock_library.niFgen_ConfigureOperationMode.side_effect = MockFunctionCallError("niFgen_ConfigureOperationMode")
        mock_library.niFgen_ConfigureOperationMode.return_value = 0
        mock_library.niFgen_ConfigureOutputEnabled.side_effect = MockFunctionCallError("niFgen_ConfigureOutputEnabled")
        mock_library.niFgen_ConfigureOutputEnabled.return_value = 0
        mock_library.niFgen_ConfigureOutputImpedance.side_effect = MockFunctionCallError("niFgen_ConfigureOutputImpedance")
        mock_library.niFgen_ConfigureOutputImpedance.return_value = 0
        mock_library.niFgen_ConfigureOutputMode.side_effect = MockFunctionCallError("niFgen_ConfigureOutputMode")
        mock_library.niFgen_ConfigureOutputMode.return_value = 0
        mock_library.niFgen_ConfigureP2PEndpointFullnessStartTrigger.side_effect = MockFunctionCallError("niFgen_ConfigureP2PEndpointFullnessStartTrigger")
        mock_library.niFgen_ConfigureP2PEndpointFullnessStartTrigger.return_value = 0
        mock_library.niFgen_ConfigureRefClockFrequency.side_effect = MockFunctionCallError("niFgen_ConfigureRefClockFrequency")
        mock_library.niFgen_ConfigureRefClockFrequency.return_value = 0
        mock_library.niFgen_ConfigureRefClockSource.side_effect = MockFunctionCallError("niFgen_ConfigureRefClockSource")
        mock_library.niFgen_ConfigureRefClockSource.return_value = 0
        mock_library.niFgen_ConfigureReferenceClock.side_effect = MockFunctionCallError("niFgen_ConfigureReferenceClock")
        mock_library.niFgen_ConfigureReferenceClock.return_value = 0
        mock_library.niFgen_ConfigureSampleClockSource.side_effect = MockFunctionCallError("niFgen_ConfigureSampleClockSource")
        mock_library.niFgen_ConfigureSampleClockSource.return_value = 0
        mock_library.niFgen_ConfigureSampleRate.side_effect = MockFunctionCallError("niFgen_ConfigureSampleRate")
        mock_library.niFgen_ConfigureSampleRate.return_value = 0
        mock_library.niFgen_ConfigureSoftwareEdgeScriptTrigger.side_effect = MockFunctionCallError("niFgen_ConfigureSoftwareEdgeScriptTrigger")
        mock_library.niFgen_ConfigureSoftwareEdgeScriptTrigger.return_value = 0
        mock_library.niFgen_ConfigureSoftwareEdgeStartTrigger.side_effect = MockFunctionCallError("niFgen_ConfigureSoftwareEdgeStartTrigger")
        mock_library.niFgen_ConfigureSoftwareEdgeStartTrigger.return_value = 0
        mock_library.niFgen_ConfigureStandardWaveform.side_effect = MockFunctionCallError("niFgen_ConfigureStandardWaveform")
        mock_library.niFgen_ConfigureStandardWaveform.return_value = 0
        mock_library.niFgen_ConfigureSynchronization.side_effect = MockFunctionCallError("niFgen_ConfigureSynchronization")
        mock_library.niFgen_ConfigureSynchronization.return_value = 0
        mock_library.niFgen_ConfigureTriggerMode.side_effect = MockFunctionCallError("niFgen_ConfigureTriggerMode")
        mock_library.niFgen_ConfigureTriggerMode.return_value = 0
        mock_library.niFgen_ConfigureTriggerSource.side_effect = MockFunctionCallError("niFgen_ConfigureTriggerSource")
        mock_library.niFgen_ConfigureTriggerSource.return_value = 0
        mock_library.niFgen_ConfigureUpdateClockSource.side_effect = MockFunctionCallError("niFgen_ConfigureUpdateClockSource")
        mock_library.niFgen_ConfigureUpdateClockSource.return_value = 0
        mock_library.niFgen_CreateAdvancedArbSequence.side_effect = MockFunctionCallError("niFgen_CreateAdvancedArbSequence")
        mock_library.niFgen_CreateAdvancedArbSequence.return_value = 0
        mock_library.niFgen_CreateArbSequence.side_effect = MockFunctionCallError("niFgen_CreateArbSequence")
        mock_library.niFgen_CreateArbSequence.return_value = 0
        mock_library.niFgen_CreateArbWaveform.side_effect = MockFunctionCallError("niFgen_CreateArbWaveform")
        mock_library.niFgen_CreateArbWaveform.return_value = 0
        mock_library.niFgen_CreateBinary16ArbWaveform.side_effect = MockFunctionCallError("niFgen_CreateBinary16ArbWaveform")
        mock_library.niFgen_CreateBinary16ArbWaveform.return_value = 0
        mock_library.niFgen_CreateFreqList.side_effect = MockFunctionCallError("niFgen_CreateFreqList")
        mock_library.niFgen_CreateFreqList.return_value = 0
        mock_library.niFgen_CreateWaveformF64.side_effect = MockFunctionCallError("niFgen_CreateWaveformF64")
        mock_library.niFgen_CreateWaveformF64.return_value = 0
        mock_library.niFgen_CreateWaveformFromFileF64.side_effect = MockFunctionCallError("niFgen_CreateWaveformFromFileF64")
        mock_library.niFgen_CreateWaveformFromFileF64.return_value = 0
        mock_library.niFgen_CreateWaveformFromFileHWS.side_effect = MockFunctionCallError("niFgen_CreateWaveformFromFileHWS")
        mock_library.niFgen_CreateWaveformFromFileHWS.return_value = 0
        mock_library.niFgen_CreateWaveformFromFileI16.side_effect = MockFunctionCallError("niFgen_CreateWaveformFromFileI16")
        mock_library.niFgen_CreateWaveformFromFileI16.return_value = 0
        mock_library.niFgen_CreateWaveformI16.side_effect = MockFunctionCallError("niFgen_CreateWaveformI16")
        mock_library.niFgen_CreateWaveformI16.return_value = 0
        mock_library.niFgen_DefineUserStandardWaveform.side_effect = MockFunctionCallError("niFgen_DefineUserStandardWaveform")
        mock_library.niFgen_DefineUserStandardWaveform.return_value = 0
        mock_library.niFgen_DeleteNamedWaveform.side_effect = MockFunctionCallError("niFgen_DeleteNamedWaveform")
        mock_library.niFgen_DeleteNamedWaveform.return_value = 0
        mock_library.niFgen_DeleteScript.side_effect = MockFunctionCallError("niFgen_DeleteScript")
        mock_library.niFgen_DeleteScript.return_value = 0
        mock_library.niFgen_Disable.side_effect = MockFunctionCallError("niFgen_Disable")
        mock_library.niFgen_Disable.return_value = 0
        mock_library.niFgen_DisableAnalogFilter.side_effect = MockFunctionCallError("niFgen_DisableAnalogFilter")
        mock_library.niFgen_DisableAnalogFilter.return_value = 0
        mock_library.niFgen_DisableDigitalFilter.side_effect = MockFunctionCallError("niFgen_DisableDigitalFilter")
        mock_library.niFgen_DisableDigitalFilter.return_value = 0
        mock_library.niFgen_DisableDigitalPatterning.side_effect = MockFunctionCallError("niFgen_DisableDigitalPatterning")
        mock_library.niFgen_DisableDigitalPatterning.return_value = 0
        mock_library.niFgen_DisableScriptTrigger.side_effect = MockFunctionCallError("niFgen_DisableScriptTrigger")
        mock_library.niFgen_DisableScriptTrigger.return_value = 0
        mock_library.niFgen_DisableStartTrigger.side_effect = MockFunctionCallError("niFgen_DisableStartTrigger")
        mock_library.niFgen_DisableStartTrigger.return_value = 0
        mock_library.niFgen_EnableAnalogFilter.side_effect = MockFunctionCallError("niFgen_EnableAnalogFilter")
        mock_library.niFgen_EnableAnalogFilter.return_value = 0
        mock_library.niFgen_EnableDigitalFilter.side_effect = MockFunctionCallError("niFgen_EnableDigitalFilter")
        mock_library.niFgen_EnableDigitalFilter.return_value = 0
        mock_library.niFgen_EnableDigitalPatterning.side_effect = MockFunctionCallError("niFgen_EnableDigitalPatterning")
        mock_library.niFgen_EnableDigitalPatterning.return_value = 0
        mock_library.niFgen_ErrorHandler.side_effect = MockFunctionCallError("niFgen_ErrorHandler")
        mock_library.niFgen_ErrorHandler.return_value = 0
        mock_library.niFgen_ExportSignal.side_effect = MockFunctionCallError("niFgen_ExportSignal")
        mock_library.niFgen_ExportSignal.return_value = 0
        mock_library.niFgen_GetAttributeViBoolean.side_effect = MockFunctionCallError("niFgen_GetAttributeViBoolean")
        mock_library.niFgen_GetAttributeViBoolean.return_value = 0
        mock_library.niFgen_GetAttributeViInt32.side_effect = MockFunctionCallError("niFgen_GetAttributeViInt32")
        mock_library.niFgen_GetAttributeViInt32.return_value = 0
        mock_library.niFgen_GetAttributeViInt64.side_effect = MockFunctionCallError("niFgen_GetAttributeViInt64")
        mock_library.niFgen_GetAttributeViInt64.return_value = 0
        mock_library.niFgen_GetAttributeViReal64.side_effect = MockFunctionCallError("niFgen_GetAttributeViReal64")
        mock_library.niFgen_GetAttributeViReal64.return_value = 0
        mock_library.niFgen_GetAttributeViString.side_effect = MockFunctionCallError("niFgen_GetAttributeViString")
        mock_library.niFgen_GetAttributeViString.return_value = 0
        mock_library.niFgen_GetError.side_effect = MockFunctionCallError("niFgen_GetError")
        mock_library.niFgen_GetError.return_value = 0
        mock_library.niFgen_GetFIRFilterCoefficients.side_effect = MockFunctionCallError("niFgen_GetFIRFilterCoefficients")
        mock_library.niFgen_GetFIRFilterCoefficients.return_value = 0
        mock_library.niFgen_GetHardwareState.side_effect = MockFunctionCallError("niFgen_GetHardwareState")
        mock_library.niFgen_GetHardwareState.return_value = 0
        mock_library.niFgen_GetSelfCalLastDateAndTime.side_effect = MockFunctionCallError("niFgen_GetSelfCalLastDateAndTime")
        mock_library.niFgen_GetSelfCalLastDateAndTime.return_value = 0
        mock_library.niFgen_GetSelfCalLastTemp.side_effect = MockFunctionCallError("niFgen_GetSelfCalLastTemp")
        mock_library.niFgen_GetSelfCalLastTemp.return_value = 0
        mock_library.niFgen_GetSelfCalSupported.side_effect = MockFunctionCallError("niFgen_GetSelfCalSupported")
        mock_library.niFgen_GetSelfCalSupported.return_value = 0
        mock_library.niFgen_InitWithOptions.side_effect = MockFunctionCallError("niFgen_InitWithOptions")
        mock_library.niFgen_InitWithOptions.return_value = 0
        mock_library.niFgen_InitializeAnalogOutputCalibration.side_effect = MockFunctionCallError("niFgen_InitializeAnalogOutputCalibration")
        mock_library.niFgen_InitializeAnalogOutputCalibration.return_value = 0
        mock_library.niFgen_InitializeCalADCCalibration.side_effect = MockFunctionCallError("niFgen_InitializeCalADCCalibration")
        mock_library.niFgen_InitializeCalADCCalibration.return_value = 0
        mock_library.niFgen_InitializeFlatnessCalibration.side_effect = MockFunctionCallError("niFgen_InitializeFlatnessCalibration")
        mock_library.niFgen_InitializeFlatnessCalibration.return_value = 0
        mock_library.niFgen_InitializeOscillatorFrequencyCalibration.side_effect = MockFunctionCallError("niFgen_InitializeOscillatorFrequencyCalibration")
        mock_library.niFgen_InitializeOscillatorFrequencyCalibration.return_value = 0
        mock_library.niFgen_InitializeWithChannels.side_effect = MockFunctionCallError("niFgen_InitializeWithChannels")
        mock_library.niFgen_InitializeWithChannels.return_value = 0
        mock_library.niFgen_InitiateGeneration.side_effect = MockFunctionCallError("niFgen_InitiateGeneration")
        mock_library.niFgen_InitiateGeneration.return_value = 0
        mock_library.niFgen_IsDone.side_effect = MockFunctionCallError("niFgen_IsDone")
        mock_library.niFgen_IsDone.return_value = 0
        mock_library.niFgen_ManualEnableP2PStream.side_effect = MockFunctionCallError("niFgen_ManualEnableP2PStream")
        mock_library.niFgen_ManualEnableP2PStream.return_value = 0
        mock_library.niFgen_QueryArbSeqCapabilities.side_effect = MockFunctionCallError("niFgen_QueryArbSeqCapabilities")
        mock_library.niFgen_QueryArbSeqCapabilities.return_value = 0
        mock_library.niFgen_QueryArbWfmCapabilities.side_effect = MockFunctionCallError("niFgen_QueryArbWfmCapabilities")
        mock_library.niFgen_QueryArbWfmCapabilities.return_value = 0
        mock_library.niFgen_QueryFreqListCapabilities.side_effect = MockFunctionCallError("niFgen_QueryFreqListCapabilities")
        mock_library.niFgen_QueryFreqListCapabilities.return_value = 0
        mock_library.niFgen_ReadCalADC.side_effect = MockFunctionCallError("niFgen_ReadCalADC")
        mock_library.niFgen_ReadCalADC.return_value = 0
        mock_library.niFgen_ReadCurrentTemperature.side_effect = MockFunctionCallError("niFgen_ReadCurrentTemperature")
        mock_library.niFgen_ReadCurrentTemperature.return_value = 0
        mock_library.niFgen_ResetAttribute.side_effect = MockFunctionCallError("niFgen_ResetAttribute")
        mock_library.niFgen_ResetAttribute.return_value = 0
        mock_library.niFgen_ResetDevice.side_effect = MockFunctionCallError("niFgen_ResetDevice")
        mock_library.niFgen_ResetDevice.return_value = 0
        mock_library.niFgen_ResetWithDefaults.side_effect = MockFunctionCallError("niFgen_ResetWithDefaults")
        mock_library.niFgen_ResetWithDefaults.return_value = 0
        mock_library.niFgen_RouteSignalOut.side_effect = MockFunctionCallError("niFgen_RouteSignalOut")
        mock_library.niFgen_RouteSignalOut.return_value = 0
        mock_library.niFgen_SelfCal.side_effect = MockFunctionCallError("niFgen_SelfCal")
        mock_library.niFgen_SelfCal.return_value = 0
        mock_library.niFgen_SendSoftwareEdgeTrigger.side_effect = MockFunctionCallError("niFgen_SendSoftwareEdgeTrigger")
        mock_library.niFgen_SendSoftwareEdgeTrigger.return_value = 0
        mock_library.niFgen_SendSoftwareTrigger.side_effect = MockFunctionCallError("niFgen_SendSoftwareTrigger")
        mock_library.niFgen_SendSoftwareTrigger.return_value = 0
        mock_library.niFgen_SetAttributeViBoolean.side_effect = MockFunctionCallError("niFgen_SetAttributeViBoolean")
        mock_library.niFgen_SetAttributeViBoolean.return_value = 0
        mock_library.niFgen_SetAttributeViInt32.side_effect = MockFunctionCallError("niFgen_SetAttributeViInt32")
        mock_library.niFgen_SetAttributeViInt32.return_value = 0
        mock_library.niFgen_SetAttributeViInt64.side_effect = MockFunctionCallError("niFgen_SetAttributeViInt64")
        mock_library.niFgen_SetAttributeViInt64.return_value = 0
        mock_library.niFgen_SetAttributeViReal64.side_effect = MockFunctionCallError("niFgen_SetAttributeViReal64")
        mock_library.niFgen_SetAttributeViReal64.return_value = 0
        mock_library.niFgen_SetAttributeViString.side_effect = MockFunctionCallError("niFgen_SetAttributeViString")
        mock_library.niFgen_SetAttributeViString.return_value = 0
        mock_library.niFgen_SetNamedWaveformNextWritePosition.side_effect = MockFunctionCallError("niFgen_SetNamedWaveformNextWritePosition")
        mock_library.niFgen_SetNamedWaveformNextWritePosition.return_value = 0
        mock_library.niFgen_SetWaveformNextWritePosition.side_effect = MockFunctionCallError("niFgen_SetWaveformNextWritePosition")
        mock_library.niFgen_SetWaveformNextWritePosition.return_value = 0
        mock_library.niFgen_WaitUntilDone.side_effect = MockFunctionCallError("niFgen_WaitUntilDone")
        mock_library.niFgen_WaitUntilDone.return_value = 0
        mock_library.niFgen_WriteBinary16AnalogStaticValue.side_effect = MockFunctionCallError("niFgen_WriteBinary16AnalogStaticValue")
        mock_library.niFgen_WriteBinary16AnalogStaticValue.return_value = 0
        mock_library.niFgen_WriteBinary16Waveform.side_effect = MockFunctionCallError("niFgen_WriteBinary16Waveform")
        mock_library.niFgen_WriteBinary16Waveform.return_value = 0
        mock_library.niFgen_WriteNamedWaveformF64.side_effect = MockFunctionCallError("niFgen_WriteNamedWaveformF64")
        mock_library.niFgen_WriteNamedWaveformF64.return_value = 0
        mock_library.niFgen_WriteNamedWaveformI16.side_effect = MockFunctionCallError("niFgen_WriteNamedWaveformI16")
        mock_library.niFgen_WriteNamedWaveformI16.return_value = 0
        mock_library.niFgen_WriteP2PEndpointI16.side_effect = MockFunctionCallError("niFgen_WriteP2PEndpointI16")
        mock_library.niFgen_WriteP2PEndpointI16.return_value = 0
        mock_library.niFgen_WriteScript.side_effect = MockFunctionCallError("niFgen_WriteScript")
        mock_library.niFgen_WriteScript.return_value = 0
        mock_library.niFgen_WriteWaveform.side_effect = MockFunctionCallError("niFgen_WriteWaveform")
        mock_library.niFgen_WriteWaveform.return_value = 0
        mock_library.niFgen_close.side_effect = MockFunctionCallError("niFgen_close")
        mock_library.niFgen_close.return_value = 0
        mock_library.niFgen_error_message.side_effect = MockFunctionCallError("niFgen_error_message")
        mock_library.niFgen_error_message.return_value = 0
        mock_library.niFgen_reset.side_effect = MockFunctionCallError("niFgen_reset")
        mock_library.niFgen_reset.return_value = 0
        mock_library.niFgen_self_test.side_effect = MockFunctionCallError("niFgen_self_test")
        mock_library.niFgen_self_test.return_value = 0
