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
        self._defaults['AbortGeneration'] = {}
        self._defaults['AbortGeneration']['return'] = 0
        self._defaults['AllocateNamedWaveform'] = {}
        self._defaults['AllocateNamedWaveform']['return'] = 0
        self._defaults['AllocateWaveform'] = {}
        self._defaults['AllocateWaveform']['return'] = 0
        self._defaults['AllocateWaveform']['waveformHandle'] = None
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
        self._defaults['ConfigureArbSequence'] = {}
        self._defaults['ConfigureArbSequence']['return'] = 0
        self._defaults['ConfigureArbWaveform'] = {}
        self._defaults['ConfigureArbWaveform']['return'] = 0
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
        self._defaults['ConfigureStandardWaveform'] = {}
        self._defaults['ConfigureStandardWaveform']['return'] = 0
        self._defaults['CreateAdvancedArbSequence'] = {}
        self._defaults['CreateAdvancedArbSequence']['return'] = 0
        self._defaults['CreateAdvancedArbSequence']['coercedMarkersArray'] = None
        self._defaults['CreateAdvancedArbSequence']['sequenceHandle'] = None
        self._defaults['CreateArbSequence'] = {}
        self._defaults['CreateArbSequence']['return'] = 0
        self._defaults['CreateArbSequence']['sequenceHandle'] = None
        self._defaults['CreateFreqList'] = {}
        self._defaults['CreateFreqList']['return'] = 0
        self._defaults['CreateFreqList']['frequencyListHandle'] = None
        self._defaults['CreateWaveformDispatcher'] = {}
        self._defaults['CreateWaveformDispatcher']['return'] = 0
        self._defaults['CreateWaveformDispatcher']['waveformHandle'] = None
        self._defaults['CreateWaveformF64'] = {}
        self._defaults['CreateWaveformF64']['return'] = 0
        self._defaults['CreateWaveformF64']['waveformHandle'] = None
        self._defaults['CreateWaveformFromFileF64'] = {}
        self._defaults['CreateWaveformFromFileF64']['return'] = 0
        self._defaults['CreateWaveformFromFileF64']['waveformHandle'] = None
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
        self._defaults['ExportSignal'] = {}
        self._defaults['ExportSignal']['return'] = 0
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
        self._defaults['GetError'] = {}
        self._defaults['GetError']['return'] = 0
        self._defaults['GetError']['errorCode'] = None
        self._defaults['GetError']['errorDescription'] = None
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
        self._defaults['GetFIRFilterCoefficients'] = {}
        self._defaults['GetFIRFilterCoefficients']['return'] = 0
        self._defaults['GetFIRFilterCoefficients']['numberOfCoefficientsRead'] = None
        self._defaults['GetFIRFilterCoefficients']['coefficientsArray'] = None
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
        self._defaults['InitializeWithChannels'] = {}
        self._defaults['InitializeWithChannels']['return'] = 0
        self._defaults['InitializeWithChannels']['vi'] = None
        self._defaults['InitiateGeneration'] = {}
        self._defaults['InitiateGeneration']['return'] = 0
        self._defaults['IsDone'] = {}
        self._defaults['IsDone']['return'] = 0
        self._defaults['IsDone']['Done'] = None
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
        self._defaults['ReadCurrentTemperature'] = {}
        self._defaults['ReadCurrentTemperature']['return'] = 0
        self._defaults['ReadCurrentTemperature']['Temperature'] = None
        self._defaults['ResetDevice'] = {}
        self._defaults['ResetDevice']['return'] = 0
        self._defaults['ResetWithDefaults'] = {}
        self._defaults['ResetWithDefaults']['return'] = 0
        self._defaults['SelfCal'] = {}
        self._defaults['SelfCal']['return'] = 0
        self._defaults['SendSoftwareEdgeTrigger'] = {}
        self._defaults['SendSoftwareEdgeTrigger']['return'] = 0
        self._defaults['SetAttributeViBoolean'] = {}
        self._defaults['SetAttributeViBoolean']['return'] = 0
        self._defaults['SetAttributeViInt32'] = {}
        self._defaults['SetAttributeViInt32']['return'] = 0
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
        self._defaults['WriteBinary16Waveform'] = {}
        self._defaults['WriteBinary16Waveform']['return'] = 0
        self._defaults['WriteNamedWaveformF64'] = {}
        self._defaults['WriteNamedWaveformF64']['return'] = 0
        self._defaults['WriteNamedWaveformI16'] = {}
        self._defaults['WriteNamedWaveformI16']['return'] = 0
        self._defaults['WriteScript'] = {}
        self._defaults['WriteScript']['return'] = 0
        self._defaults['WriteWaveform'] = {}
        self._defaults['WriteWaveform']['return'] = 0
        self._defaults['WriteWaveformDispatcher'] = {}
        self._defaults['WriteWaveformDispatcher']['return'] = 0
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

    def niFgen_AllocateNamedWaveform(self, vi, channel_name, waveform_name, waveform_size):  # noqa: N802
        if self._defaults['AllocateNamedWaveform']['return'] != 0:
            return self._defaults['AllocateNamedWaveform']['return']
        return self._defaults['AllocateNamedWaveform']['return']

    def niFgen_AllocateWaveform(self, vi, channel_name, waveform_size, waveform_handle):  # noqa: N802
        if self._defaults['AllocateWaveform']['return'] != 0:
            return self._defaults['AllocateWaveform']['return']
        # waveform_handle
        if self._defaults['AllocateWaveform']['waveformHandle'] is None:
            raise MockFunctionCallError("niFgen_AllocateWaveform", param='waveformHandle')
        waveform_handle.contents.value = self._defaults['AllocateWaveform']['waveformHandle']
        return self._defaults['AllocateWaveform']['return']

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

    def niFgen_ConfigureArbSequence(self, vi, channel_name, sequence_handle, gain, offset):  # noqa: N802
        if self._defaults['ConfigureArbSequence']['return'] != 0:
            return self._defaults['ConfigureArbSequence']['return']
        return self._defaults['ConfigureArbSequence']['return']

    def niFgen_ConfigureArbWaveform(self, vi, channel_name, waveform_handle, gain, offset):  # noqa: N802
        if self._defaults['ConfigureArbWaveform']['return'] != 0:
            return self._defaults['ConfigureArbWaveform']['return']
        return self._defaults['ConfigureArbWaveform']['return']

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

    def niFgen_ConfigureStandardWaveform(self, vi, channel_name, waveform, amplitude, dc_offset, frequency, start_phase):  # noqa: N802
        if self._defaults['ConfigureStandardWaveform']['return'] != 0:
            return self._defaults['ConfigureStandardWaveform']['return']
        return self._defaults['ConfigureStandardWaveform']['return']

    def niFgen_CreateAdvancedArbSequence(self, vi, sequence_length, waveform_handles_array, loop_counts_array, sample_counts_array, marker_location_array, coerced_markers_array, sequence_handle):  # noqa: N802
        if self._defaults['CreateAdvancedArbSequence']['return'] != 0:
            return self._defaults['CreateAdvancedArbSequence']['return']
        # coerced_markers_array
        if self._defaults['CreateAdvancedArbSequence']['coercedMarkersArray'] is None:
            raise MockFunctionCallError("niFgen_CreateAdvancedArbSequence", param='coercedMarkersArray')
        test_value = self._defaults['CreateAdvancedArbSequence']['coercedMarkersArray']
        try:
            coerced_markers_array_ref = coerced_markers_array.contents
        except AttributeError:
            coerced_markers_array_ref = coerced_markers_array
        assert len(coerced_markers_array_ref) >= len(test_value)
        for i in range(len(test_value)):
            coerced_markers_array_ref[i] = test_value[i]
        # sequence_handle
        if self._defaults['CreateAdvancedArbSequence']['sequenceHandle'] is None:
            raise MockFunctionCallError("niFgen_CreateAdvancedArbSequence", param='sequenceHandle')
        sequence_handle.contents.value = self._defaults['CreateAdvancedArbSequence']['sequenceHandle']
        return self._defaults['CreateAdvancedArbSequence']['return']

    def niFgen_CreateArbSequence(self, vi, sequence_length, waveform_handles_array, loop_counts_array, sequence_handle):  # noqa: N802
        if self._defaults['CreateArbSequence']['return'] != 0:
            return self._defaults['CreateArbSequence']['return']
        # sequence_handle
        if self._defaults['CreateArbSequence']['sequenceHandle'] is None:
            raise MockFunctionCallError("niFgen_CreateArbSequence", param='sequenceHandle')
        sequence_handle.contents.value = self._defaults['CreateArbSequence']['sequenceHandle']
        return self._defaults['CreateArbSequence']['return']

    def niFgen_CreateFreqList(self, vi, waveform, frequency_list_length, frequency_array, duration_array, frequency_list_handle):  # noqa: N802
        if self._defaults['CreateFreqList']['return'] != 0:
            return self._defaults['CreateFreqList']['return']
        # frequency_list_handle
        if self._defaults['CreateFreqList']['frequencyListHandle'] is None:
            raise MockFunctionCallError("niFgen_CreateFreqList", param='frequencyListHandle')
        frequency_list_handle.contents.value = self._defaults['CreateFreqList']['frequencyListHandle']
        return self._defaults['CreateFreqList']['return']

    def niFgen_CreateWaveformDispatcher(self, vi, channel_name, waveform_data_array, waveform_handle):  # noqa: N802
        if self._defaults['CreateWaveformDispatcher']['return'] != 0:
            return self._defaults['CreateWaveformDispatcher']['return']
        # waveform_handle
        if self._defaults['CreateWaveformDispatcher']['waveformHandle'] is None:
            raise MockFunctionCallError("niFgen_CreateWaveformDispatcher", param='waveformHandle')
        waveform_handle.contents.value = self._defaults['CreateWaveformDispatcher']['waveformHandle']
        return self._defaults['CreateWaveformDispatcher']['return']

    def niFgen_CreateWaveformF64(self, vi, channel_name, waveform_size, waveform_data_array, waveform_handle):  # noqa: N802
        if self._defaults['CreateWaveformF64']['return'] != 0:
            return self._defaults['CreateWaveformF64']['return']
        # waveform_handle
        if self._defaults['CreateWaveformF64']['waveformHandle'] is None:
            raise MockFunctionCallError("niFgen_CreateWaveformF64", param='waveformHandle')
        waveform_handle.contents.value = self._defaults['CreateWaveformF64']['waveformHandle']
        return self._defaults['CreateWaveformF64']['return']

    def niFgen_CreateWaveformFromFileF64(self, vi, channel_name, file_name, byte_order, waveform_handle):  # noqa: N802
        if self._defaults['CreateWaveformFromFileF64']['return'] != 0:
            return self._defaults['CreateWaveformFromFileF64']['return']
        # waveform_handle
        if self._defaults['CreateWaveformFromFileF64']['waveformHandle'] is None:
            raise MockFunctionCallError("niFgen_CreateWaveformFromFileF64", param='waveformHandle')
        waveform_handle.contents.value = self._defaults['CreateWaveformFromFileF64']['waveformHandle']
        return self._defaults['CreateWaveformFromFileF64']['return']

    def niFgen_CreateWaveformFromFileI16(self, vi, channel_name, file_name, byte_order, waveform_handle):  # noqa: N802
        if self._defaults['CreateWaveformFromFileI16']['return'] != 0:
            return self._defaults['CreateWaveformFromFileI16']['return']
        # waveform_handle
        if self._defaults['CreateWaveformFromFileI16']['waveformHandle'] is None:
            raise MockFunctionCallError("niFgen_CreateWaveformFromFileI16", param='waveformHandle')
        waveform_handle.contents.value = self._defaults['CreateWaveformFromFileI16']['waveformHandle']
        return self._defaults['CreateWaveformFromFileI16']['return']

    def niFgen_CreateWaveformI16(self, vi, channel_name, waveform_size, waveform_data_array, waveform_handle):  # noqa: N802
        if self._defaults['CreateWaveformI16']['return'] != 0:
            return self._defaults['CreateWaveformI16']['return']
        # waveform_handle
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

    def niFgen_ExportSignal(self, vi, signal, signal_identifier, output_terminal):  # noqa: N802
        if self._defaults['ExportSignal']['return'] != 0:
            return self._defaults['ExportSignal']['return']
        return self._defaults['ExportSignal']['return']

    def niFgen_GetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViBoolean']['return'] != 0:
            return self._defaults['GetAttributeViBoolean']['return']
        # attribute_value
        if self._defaults['GetAttributeViBoolean']['attributeValue'] is None:
            raise MockFunctionCallError("niFgen_GetAttributeViBoolean", param='attributeValue')
        attribute_value.contents.value = self._defaults['GetAttributeViBoolean']['attributeValue']
        return self._defaults['GetAttributeViBoolean']['return']

    def niFgen_GetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViInt32']['return'] != 0:
            return self._defaults['GetAttributeViInt32']['return']
        # attribute_value
        if self._defaults['GetAttributeViInt32']['attributeValue'] is None:
            raise MockFunctionCallError("niFgen_GetAttributeViInt32", param='attributeValue')
        attribute_value.contents.value = self._defaults['GetAttributeViInt32']['attributeValue']
        return self._defaults['GetAttributeViInt32']['return']

    def niFgen_GetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViReal64']['return'] != 0:
            return self._defaults['GetAttributeViReal64']['return']
        # attribute_value
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
        # error_code
        if self._defaults['GetError']['errorCode'] is None:
            raise MockFunctionCallError("niFgen_GetError", param='errorCode')
        error_code.contents.value = self._defaults['GetError']['errorCode']
        if self._defaults['GetError']['errorDescription'] is None:
            raise MockFunctionCallError("niFgen_GetError", param='errorDescription')
        if error_description_buffer_size.value == 0:
            return len(self._defaults['GetError']['errorDescription'])
        error_description.value = self._defaults['GetError']['errorDescription'].encode('ascii')
        return self._defaults['GetError']['return']

    def niFgen_GetExtCalLastDateAndTime(self, vi, year, month, day, hour, minute):  # noqa: N802
        if self._defaults['GetExtCalLastDateAndTime']['return'] != 0:
            return self._defaults['GetExtCalLastDateAndTime']['return']
        # year
        if self._defaults['GetExtCalLastDateAndTime']['Year'] is None:
            raise MockFunctionCallError("niFgen_GetExtCalLastDateAndTime", param='Year')
        year.contents.value = self._defaults['GetExtCalLastDateAndTime']['Year']
        # month
        if self._defaults['GetExtCalLastDateAndTime']['Month'] is None:
            raise MockFunctionCallError("niFgen_GetExtCalLastDateAndTime", param='Month')
        month.contents.value = self._defaults['GetExtCalLastDateAndTime']['Month']
        # day
        if self._defaults['GetExtCalLastDateAndTime']['Day'] is None:
            raise MockFunctionCallError("niFgen_GetExtCalLastDateAndTime", param='Day')
        day.contents.value = self._defaults['GetExtCalLastDateAndTime']['Day']
        # hour
        if self._defaults['GetExtCalLastDateAndTime']['Hour'] is None:
            raise MockFunctionCallError("niFgen_GetExtCalLastDateAndTime", param='Hour')
        hour.contents.value = self._defaults['GetExtCalLastDateAndTime']['Hour']
        # minute
        if self._defaults['GetExtCalLastDateAndTime']['Minute'] is None:
            raise MockFunctionCallError("niFgen_GetExtCalLastDateAndTime", param='Minute')
        minute.contents.value = self._defaults['GetExtCalLastDateAndTime']['Minute']
        return self._defaults['GetExtCalLastDateAndTime']['return']

    def niFgen_GetExtCalLastTemp(self, vi, temperature):  # noqa: N802
        if self._defaults['GetExtCalLastTemp']['return'] != 0:
            return self._defaults['GetExtCalLastTemp']['return']
        # temperature
        if self._defaults['GetExtCalLastTemp']['Temperature'] is None:
            raise MockFunctionCallError("niFgen_GetExtCalLastTemp", param='Temperature')
        temperature.contents.value = self._defaults['GetExtCalLastTemp']['Temperature']
        return self._defaults['GetExtCalLastTemp']['return']

    def niFgen_GetExtCalRecommendedInterval(self, vi, months):  # noqa: N802
        if self._defaults['GetExtCalRecommendedInterval']['return'] != 0:
            return self._defaults['GetExtCalRecommendedInterval']['return']
        # months
        if self._defaults['GetExtCalRecommendedInterval']['Months'] is None:
            raise MockFunctionCallError("niFgen_GetExtCalRecommendedInterval", param='Months')
        months.contents.value = self._defaults['GetExtCalRecommendedInterval']['Months']
        return self._defaults['GetExtCalRecommendedInterval']['return']

    def niFgen_GetFIRFilterCoefficients(self, vi, channel_name, array_size, coefficients_array, number_of_coefficients_read):  # noqa: N802
        if self._defaults['GetFIRFilterCoefficients']['return'] != 0:
            return self._defaults['GetFIRFilterCoefficients']['return']
        # number_of_coefficients_read
        if self._defaults['GetFIRFilterCoefficients']['numberOfCoefficientsRead'] is None:
            raise MockFunctionCallError("niFgen_GetFIRFilterCoefficients", param='numberOfCoefficientsRead')
        number_of_coefficients_read.contents.value = self._defaults['GetFIRFilterCoefficients']['numberOfCoefficientsRead']
        if self._defaults['GetFIRFilterCoefficients']['coefficientsArray'] is None:
            raise MockFunctionCallError("niFgen_GetFIRFilterCoefficients", param='coefficientsArray')
        if array_size.value == 0:
            return len(self._defaults['GetFIRFilterCoefficients']['coefficientsArray'])
        try:
            coefficients_array_ref = coefficients_array.contents
        except AttributeError:
            coefficients_array_ref = coefficients_array
        for i in range(len(self._defaults['GetFIRFilterCoefficients']['coefficientsArray'])):
            coefficients_array_ref[i] = self._defaults['GetFIRFilterCoefficients']['coefficientsArray'][i]
        return self._defaults['GetFIRFilterCoefficients']['return']

    def niFgen_GetHardwareState(self, vi, state):  # noqa: N802
        if self._defaults['GetHardwareState']['return'] != 0:
            return self._defaults['GetHardwareState']['return']
        # state
        if self._defaults['GetHardwareState']['state'] is None:
            raise MockFunctionCallError("niFgen_GetHardwareState", param='state')
        state.contents.value = self._defaults['GetHardwareState']['state']
        return self._defaults['GetHardwareState']['return']

    def niFgen_GetSelfCalLastDateAndTime(self, vi, year, month, day, hour, minute):  # noqa: N802
        if self._defaults['GetSelfCalLastDateAndTime']['return'] != 0:
            return self._defaults['GetSelfCalLastDateAndTime']['return']
        # year
        if self._defaults['GetSelfCalLastDateAndTime']['Year'] is None:
            raise MockFunctionCallError("niFgen_GetSelfCalLastDateAndTime", param='Year')
        year.contents.value = self._defaults['GetSelfCalLastDateAndTime']['Year']
        # month
        if self._defaults['GetSelfCalLastDateAndTime']['Month'] is None:
            raise MockFunctionCallError("niFgen_GetSelfCalLastDateAndTime", param='Month')
        month.contents.value = self._defaults['GetSelfCalLastDateAndTime']['Month']
        # day
        if self._defaults['GetSelfCalLastDateAndTime']['Day'] is None:
            raise MockFunctionCallError("niFgen_GetSelfCalLastDateAndTime", param='Day')
        day.contents.value = self._defaults['GetSelfCalLastDateAndTime']['Day']
        # hour
        if self._defaults['GetSelfCalLastDateAndTime']['Hour'] is None:
            raise MockFunctionCallError("niFgen_GetSelfCalLastDateAndTime", param='Hour')
        hour.contents.value = self._defaults['GetSelfCalLastDateAndTime']['Hour']
        # minute
        if self._defaults['GetSelfCalLastDateAndTime']['Minute'] is None:
            raise MockFunctionCallError("niFgen_GetSelfCalLastDateAndTime", param='Minute')
        minute.contents.value = self._defaults['GetSelfCalLastDateAndTime']['Minute']
        return self._defaults['GetSelfCalLastDateAndTime']['return']

    def niFgen_GetSelfCalLastTemp(self, vi, temperature):  # noqa: N802
        if self._defaults['GetSelfCalLastTemp']['return'] != 0:
            return self._defaults['GetSelfCalLastTemp']['return']
        # temperature
        if self._defaults['GetSelfCalLastTemp']['Temperature'] is None:
            raise MockFunctionCallError("niFgen_GetSelfCalLastTemp", param='Temperature')
        temperature.contents.value = self._defaults['GetSelfCalLastTemp']['Temperature']
        return self._defaults['GetSelfCalLastTemp']['return']

    def niFgen_GetSelfCalSupported(self, vi, self_cal_supported):  # noqa: N802
        if self._defaults['GetSelfCalSupported']['return'] != 0:
            return self._defaults['GetSelfCalSupported']['return']
        # self_cal_supported
        if self._defaults['GetSelfCalSupported']['selfCalSupported'] is None:
            raise MockFunctionCallError("niFgen_GetSelfCalSupported", param='selfCalSupported')
        self_cal_supported.contents.value = self._defaults['GetSelfCalSupported']['selfCalSupported']
        return self._defaults['GetSelfCalSupported']['return']

    def niFgen_InitializeWithChannels(self, resource_name, channel_name, reset_device, option_string, vi):  # noqa: N802
        if self._defaults['InitializeWithChannels']['return'] != 0:
            return self._defaults['InitializeWithChannels']['return']
        # vi
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
        # done
        if self._defaults['IsDone']['Done'] is None:
            raise MockFunctionCallError("niFgen_IsDone", param='Done')
        done.contents.value = self._defaults['IsDone']['Done']
        return self._defaults['IsDone']['return']

    def niFgen_QueryArbSeqCapabilities(self, vi, maximum_number_of_sequences, minimum_sequence_length, maximum_sequence_length, maximum_loop_count):  # noqa: N802
        if self._defaults['QueryArbSeqCapabilities']['return'] != 0:
            return self._defaults['QueryArbSeqCapabilities']['return']
        # maximum_number_of_sequences
        if self._defaults['QueryArbSeqCapabilities']['maximumNumberOfSequences'] is None:
            raise MockFunctionCallError("niFgen_QueryArbSeqCapabilities", param='maximumNumberOfSequences')
        maximum_number_of_sequences.contents.value = self._defaults['QueryArbSeqCapabilities']['maximumNumberOfSequences']
        # minimum_sequence_length
        if self._defaults['QueryArbSeqCapabilities']['minimumSequenceLength'] is None:
            raise MockFunctionCallError("niFgen_QueryArbSeqCapabilities", param='minimumSequenceLength')
        minimum_sequence_length.contents.value = self._defaults['QueryArbSeqCapabilities']['minimumSequenceLength']
        # maximum_sequence_length
        if self._defaults['QueryArbSeqCapabilities']['maximumSequenceLength'] is None:
            raise MockFunctionCallError("niFgen_QueryArbSeqCapabilities", param='maximumSequenceLength')
        maximum_sequence_length.contents.value = self._defaults['QueryArbSeqCapabilities']['maximumSequenceLength']
        # maximum_loop_count
        if self._defaults['QueryArbSeqCapabilities']['maximumLoopCount'] is None:
            raise MockFunctionCallError("niFgen_QueryArbSeqCapabilities", param='maximumLoopCount')
        maximum_loop_count.contents.value = self._defaults['QueryArbSeqCapabilities']['maximumLoopCount']
        return self._defaults['QueryArbSeqCapabilities']['return']

    def niFgen_QueryArbWfmCapabilities(self, vi, maximum_number_of_waveforms, waveform_quantum, minimum_waveform_size, maximum_waveform_size):  # noqa: N802
        if self._defaults['QueryArbWfmCapabilities']['return'] != 0:
            return self._defaults['QueryArbWfmCapabilities']['return']
        # maximum_number_of_waveforms
        if self._defaults['QueryArbWfmCapabilities']['maximumNumberOfWaveforms'] is None:
            raise MockFunctionCallError("niFgen_QueryArbWfmCapabilities", param='maximumNumberOfWaveforms')
        maximum_number_of_waveforms.contents.value = self._defaults['QueryArbWfmCapabilities']['maximumNumberOfWaveforms']
        # waveform_quantum
        if self._defaults['QueryArbWfmCapabilities']['waveformQuantum'] is None:
            raise MockFunctionCallError("niFgen_QueryArbWfmCapabilities", param='waveformQuantum')
        waveform_quantum.contents.value = self._defaults['QueryArbWfmCapabilities']['waveformQuantum']
        # minimum_waveform_size
        if self._defaults['QueryArbWfmCapabilities']['minimumWaveformSize'] is None:
            raise MockFunctionCallError("niFgen_QueryArbWfmCapabilities", param='minimumWaveformSize')
        minimum_waveform_size.contents.value = self._defaults['QueryArbWfmCapabilities']['minimumWaveformSize']
        # maximum_waveform_size
        if self._defaults['QueryArbWfmCapabilities']['maximumWaveformSize'] is None:
            raise MockFunctionCallError("niFgen_QueryArbWfmCapabilities", param='maximumWaveformSize')
        maximum_waveform_size.contents.value = self._defaults['QueryArbWfmCapabilities']['maximumWaveformSize']
        return self._defaults['QueryArbWfmCapabilities']['return']

    def niFgen_QueryFreqListCapabilities(self, vi, maximum_number_of_freq_lists, minimum_frequency_list_length, maximum_frequency_list_length, minimum_frequency_list_duration, maximum_frequency_list_duration, frequency_list_duration_quantum):  # noqa: N802
        if self._defaults['QueryFreqListCapabilities']['return'] != 0:
            return self._defaults['QueryFreqListCapabilities']['return']
        # maximum_number_of_freq_lists
        if self._defaults['QueryFreqListCapabilities']['maximumNumberOfFreqLists'] is None:
            raise MockFunctionCallError("niFgen_QueryFreqListCapabilities", param='maximumNumberOfFreqLists')
        maximum_number_of_freq_lists.contents.value = self._defaults['QueryFreqListCapabilities']['maximumNumberOfFreqLists']
        # minimum_frequency_list_length
        if self._defaults['QueryFreqListCapabilities']['minimumFrequencyListLength'] is None:
            raise MockFunctionCallError("niFgen_QueryFreqListCapabilities", param='minimumFrequencyListLength')
        minimum_frequency_list_length.contents.value = self._defaults['QueryFreqListCapabilities']['minimumFrequencyListLength']
        # maximum_frequency_list_length
        if self._defaults['QueryFreqListCapabilities']['maximumFrequencyListLength'] is None:
            raise MockFunctionCallError("niFgen_QueryFreqListCapabilities", param='maximumFrequencyListLength')
        maximum_frequency_list_length.contents.value = self._defaults['QueryFreqListCapabilities']['maximumFrequencyListLength']
        # minimum_frequency_list_duration
        if self._defaults['QueryFreqListCapabilities']['minimumFrequencyListDuration'] is None:
            raise MockFunctionCallError("niFgen_QueryFreqListCapabilities", param='minimumFrequencyListDuration')
        minimum_frequency_list_duration.contents.value = self._defaults['QueryFreqListCapabilities']['minimumFrequencyListDuration']
        # maximum_frequency_list_duration
        if self._defaults['QueryFreqListCapabilities']['maximumFrequencyListDuration'] is None:
            raise MockFunctionCallError("niFgen_QueryFreqListCapabilities", param='maximumFrequencyListDuration')
        maximum_frequency_list_duration.contents.value = self._defaults['QueryFreqListCapabilities']['maximumFrequencyListDuration']
        # frequency_list_duration_quantum
        if self._defaults['QueryFreqListCapabilities']['frequencyListDurationQuantum'] is None:
            raise MockFunctionCallError("niFgen_QueryFreqListCapabilities", param='frequencyListDurationQuantum')
        frequency_list_duration_quantum.contents.value = self._defaults['QueryFreqListCapabilities']['frequencyListDurationQuantum']
        return self._defaults['QueryFreqListCapabilities']['return']

    def niFgen_ReadCurrentTemperature(self, vi, temperature):  # noqa: N802
        if self._defaults['ReadCurrentTemperature']['return'] != 0:
            return self._defaults['ReadCurrentTemperature']['return']
        # temperature
        if self._defaults['ReadCurrentTemperature']['Temperature'] is None:
            raise MockFunctionCallError("niFgen_ReadCurrentTemperature", param='Temperature')
        temperature.contents.value = self._defaults['ReadCurrentTemperature']['Temperature']
        return self._defaults['ReadCurrentTemperature']['return']

    def niFgen_ResetDevice(self, vi):  # noqa: N802
        if self._defaults['ResetDevice']['return'] != 0:
            return self._defaults['ResetDevice']['return']
        return self._defaults['ResetDevice']['return']

    def niFgen_ResetWithDefaults(self, vi):  # noqa: N802
        if self._defaults['ResetWithDefaults']['return'] != 0:
            return self._defaults['ResetWithDefaults']['return']
        return self._defaults['ResetWithDefaults']['return']

    def niFgen_SelfCal(self, vi):  # noqa: N802
        if self._defaults['SelfCal']['return'] != 0:
            return self._defaults['SelfCal']['return']
        return self._defaults['SelfCal']['return']

    def niFgen_SendSoftwareEdgeTrigger(self, vi, trigger, trigger_id):  # noqa: N802
        if self._defaults['SendSoftwareEdgeTrigger']['return'] != 0:
            return self._defaults['SendSoftwareEdgeTrigger']['return']
        return self._defaults['SendSoftwareEdgeTrigger']['return']

    def niFgen_SetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViBoolean']['return'] != 0:
            return self._defaults['SetAttributeViBoolean']['return']
        return self._defaults['SetAttributeViBoolean']['return']

    def niFgen_SetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViInt32']['return'] != 0:
            return self._defaults['SetAttributeViInt32']['return']
        return self._defaults['SetAttributeViInt32']['return']

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

    def niFgen_WriteScript(self, vi, channel_name, script):  # noqa: N802
        if self._defaults['WriteScript']['return'] != 0:
            return self._defaults['WriteScript']['return']
        return self._defaults['WriteScript']['return']

    def niFgen_WriteWaveform(self, vi, channel_name, waveform_handle, size, data):  # noqa: N802
        if self._defaults['WriteWaveform']['return'] != 0:
            return self._defaults['WriteWaveform']['return']
        return self._defaults['WriteWaveform']['return']

    def niFgen_WriteWaveformDispatcher(self, vi, channel_name, waveform_name_or_handle, size, data):  # noqa: N802
        if self._defaults['WriteWaveformDispatcher']['return'] != 0:
            return self._defaults['WriteWaveformDispatcher']['return']
        return self._defaults['WriteWaveformDispatcher']['return']

    def niFgen_close(self, vi):  # noqa: N802
        if self._defaults['close']['return'] != 0:
            return self._defaults['close']['return']
        return self._defaults['close']['return']

    def niFgen_error_message(self, vi, error_code, error_message):  # noqa: N802
        if self._defaults['error_message']['return'] != 0:
            return self._defaults['error_message']['return']
        # error_message
        if self._defaults['error_message']['errorMessage'] is None:
            raise MockFunctionCallError("niFgen_error_message", param='errorMessage')
        test_value = self._defaults['error_message']['errorMessage']
        if sys.version_info.major > 2 and type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(error_message) >= len(test_value)
        for i in range(len(test_value)):
            error_message[i] = test_value[i]
        return self._defaults['error_message']['return']

    def niFgen_reset(self, vi):  # noqa: N802
        if self._defaults['reset']['return'] != 0:
            return self._defaults['reset']['return']
        return self._defaults['reset']['return']

    def niFgen_self_test(self, vi, self_test_result, self_test_message):  # noqa: N802
        if self._defaults['self_test']['return'] != 0:
            return self._defaults['self_test']['return']
        # self_test_result
        if self._defaults['self_test']['selfTestResult'] is None:
            raise MockFunctionCallError("niFgen_self_test", param='selfTestResult')
        self_test_result.contents.value = self._defaults['self_test']['selfTestResult']
        # self_test_message
        if self._defaults['self_test']['selfTestMessage'] is None:
            raise MockFunctionCallError("niFgen_self_test", param='selfTestMessage')
        test_value = self._defaults['self_test']['selfTestMessage']
        if sys.version_info.major > 2 and type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(self_test_message) >= len(test_value)
        for i in range(len(test_value)):
            self_test_message[i] = test_value[i]
        return self._defaults['self_test']['return']

    # Helper function to setup Mock object with default side effects and return values
    def set_side_effects_and_return_values(self, mock_library):
        mock_library.niFgen_AbortGeneration.side_effect = MockFunctionCallError("niFgen_AbortGeneration")
        mock_library.niFgen_AbortGeneration.return_value = 0
        mock_library.niFgen_AllocateNamedWaveform.side_effect = MockFunctionCallError("niFgen_AllocateNamedWaveform")
        mock_library.niFgen_AllocateNamedWaveform.return_value = 0
        mock_library.niFgen_AllocateWaveform.side_effect = MockFunctionCallError("niFgen_AllocateWaveform")
        mock_library.niFgen_AllocateWaveform.return_value = 0
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
        mock_library.niFgen_ConfigureArbSequence.side_effect = MockFunctionCallError("niFgen_ConfigureArbSequence")
        mock_library.niFgen_ConfigureArbSequence.return_value = 0
        mock_library.niFgen_ConfigureArbWaveform.side_effect = MockFunctionCallError("niFgen_ConfigureArbWaveform")
        mock_library.niFgen_ConfigureArbWaveform.return_value = 0
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
        mock_library.niFgen_ConfigureStandardWaveform.side_effect = MockFunctionCallError("niFgen_ConfigureStandardWaveform")
        mock_library.niFgen_ConfigureStandardWaveform.return_value = 0
        mock_library.niFgen_CreateAdvancedArbSequence.side_effect = MockFunctionCallError("niFgen_CreateAdvancedArbSequence")
        mock_library.niFgen_CreateAdvancedArbSequence.return_value = 0
        mock_library.niFgen_CreateArbSequence.side_effect = MockFunctionCallError("niFgen_CreateArbSequence")
        mock_library.niFgen_CreateArbSequence.return_value = 0
        mock_library.niFgen_CreateFreqList.side_effect = MockFunctionCallError("niFgen_CreateFreqList")
        mock_library.niFgen_CreateFreqList.return_value = 0
        mock_library.niFgen_CreateWaveformDispatcher.side_effect = MockFunctionCallError("niFgen_CreateWaveformDispatcher")
        mock_library.niFgen_CreateWaveformDispatcher.return_value = 0
        mock_library.niFgen_CreateWaveformF64.side_effect = MockFunctionCallError("niFgen_CreateWaveformF64")
        mock_library.niFgen_CreateWaveformF64.return_value = 0
        mock_library.niFgen_CreateWaveformFromFileF64.side_effect = MockFunctionCallError("niFgen_CreateWaveformFromFileF64")
        mock_library.niFgen_CreateWaveformFromFileF64.return_value = 0
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
        mock_library.niFgen_ExportSignal.side_effect = MockFunctionCallError("niFgen_ExportSignal")
        mock_library.niFgen_ExportSignal.return_value = 0
        mock_library.niFgen_GetAttributeViBoolean.side_effect = MockFunctionCallError("niFgen_GetAttributeViBoolean")
        mock_library.niFgen_GetAttributeViBoolean.return_value = 0
        mock_library.niFgen_GetAttributeViInt32.side_effect = MockFunctionCallError("niFgen_GetAttributeViInt32")
        mock_library.niFgen_GetAttributeViInt32.return_value = 0
        mock_library.niFgen_GetAttributeViReal64.side_effect = MockFunctionCallError("niFgen_GetAttributeViReal64")
        mock_library.niFgen_GetAttributeViReal64.return_value = 0
        mock_library.niFgen_GetAttributeViString.side_effect = MockFunctionCallError("niFgen_GetAttributeViString")
        mock_library.niFgen_GetAttributeViString.return_value = 0
        mock_library.niFgen_GetError.side_effect = MockFunctionCallError("niFgen_GetError")
        mock_library.niFgen_GetError.return_value = 0
        mock_library.niFgen_GetExtCalLastDateAndTime.side_effect = MockFunctionCallError("niFgen_GetExtCalLastDateAndTime")
        mock_library.niFgen_GetExtCalLastDateAndTime.return_value = 0
        mock_library.niFgen_GetExtCalLastTemp.side_effect = MockFunctionCallError("niFgen_GetExtCalLastTemp")
        mock_library.niFgen_GetExtCalLastTemp.return_value = 0
        mock_library.niFgen_GetExtCalRecommendedInterval.side_effect = MockFunctionCallError("niFgen_GetExtCalRecommendedInterval")
        mock_library.niFgen_GetExtCalRecommendedInterval.return_value = 0
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
        mock_library.niFgen_InitializeWithChannels.side_effect = MockFunctionCallError("niFgen_InitializeWithChannels")
        mock_library.niFgen_InitializeWithChannels.return_value = 0
        mock_library.niFgen_InitiateGeneration.side_effect = MockFunctionCallError("niFgen_InitiateGeneration")
        mock_library.niFgen_InitiateGeneration.return_value = 0
        mock_library.niFgen_IsDone.side_effect = MockFunctionCallError("niFgen_IsDone")
        mock_library.niFgen_IsDone.return_value = 0
        mock_library.niFgen_QueryArbSeqCapabilities.side_effect = MockFunctionCallError("niFgen_QueryArbSeqCapabilities")
        mock_library.niFgen_QueryArbSeqCapabilities.return_value = 0
        mock_library.niFgen_QueryArbWfmCapabilities.side_effect = MockFunctionCallError("niFgen_QueryArbWfmCapabilities")
        mock_library.niFgen_QueryArbWfmCapabilities.return_value = 0
        mock_library.niFgen_QueryFreqListCapabilities.side_effect = MockFunctionCallError("niFgen_QueryFreqListCapabilities")
        mock_library.niFgen_QueryFreqListCapabilities.return_value = 0
        mock_library.niFgen_ReadCurrentTemperature.side_effect = MockFunctionCallError("niFgen_ReadCurrentTemperature")
        mock_library.niFgen_ReadCurrentTemperature.return_value = 0
        mock_library.niFgen_ResetDevice.side_effect = MockFunctionCallError("niFgen_ResetDevice")
        mock_library.niFgen_ResetDevice.return_value = 0
        mock_library.niFgen_ResetWithDefaults.side_effect = MockFunctionCallError("niFgen_ResetWithDefaults")
        mock_library.niFgen_ResetWithDefaults.return_value = 0
        mock_library.niFgen_SelfCal.side_effect = MockFunctionCallError("niFgen_SelfCal")
        mock_library.niFgen_SelfCal.return_value = 0
        mock_library.niFgen_SendSoftwareEdgeTrigger.side_effect = MockFunctionCallError("niFgen_SendSoftwareEdgeTrigger")
        mock_library.niFgen_SendSoftwareEdgeTrigger.return_value = 0
        mock_library.niFgen_SetAttributeViBoolean.side_effect = MockFunctionCallError("niFgen_SetAttributeViBoolean")
        mock_library.niFgen_SetAttributeViBoolean.return_value = 0
        mock_library.niFgen_SetAttributeViInt32.side_effect = MockFunctionCallError("niFgen_SetAttributeViInt32")
        mock_library.niFgen_SetAttributeViInt32.return_value = 0
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
        mock_library.niFgen_WriteBinary16Waveform.side_effect = MockFunctionCallError("niFgen_WriteBinary16Waveform")
        mock_library.niFgen_WriteBinary16Waveform.return_value = 0
        mock_library.niFgen_WriteNamedWaveformF64.side_effect = MockFunctionCallError("niFgen_WriteNamedWaveformF64")
        mock_library.niFgen_WriteNamedWaveformF64.return_value = 0
        mock_library.niFgen_WriteNamedWaveformI16.side_effect = MockFunctionCallError("niFgen_WriteNamedWaveformI16")
        mock_library.niFgen_WriteNamedWaveformI16.return_value = 0
        mock_library.niFgen_WriteScript.side_effect = MockFunctionCallError("niFgen_WriteScript")
        mock_library.niFgen_WriteScript.return_value = 0
        mock_library.niFgen_WriteWaveform.side_effect = MockFunctionCallError("niFgen_WriteWaveform")
        mock_library.niFgen_WriteWaveform.return_value = 0
        mock_library.niFgen_WriteWaveformDispatcher.side_effect = MockFunctionCallError("niFgen_WriteWaveformDispatcher")
        mock_library.niFgen_WriteWaveformDispatcher.return_value = 0
        mock_library.niFgen_close.side_effect = MockFunctionCallError("niFgen_close")
        mock_library.niFgen_close.return_value = 0
        mock_library.niFgen_error_message.side_effect = MockFunctionCallError("niFgen_error_message")
        mock_library.niFgen_error_message.return_value = 0
        mock_library.niFgen_reset.side_effect = MockFunctionCallError("niFgen_reset")
        mock_library.niFgen_reset.return_value = 0
        mock_library.niFgen_self_test.side_effect = MockFunctionCallError("niFgen_self_test")
        mock_library.niFgen_self_test.return_value = 0
