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
        self._defaults['GetExtCalLastDateAndTime']['year'] = None
        self._defaults['GetExtCalLastDateAndTime']['month'] = None
        self._defaults['GetExtCalLastDateAndTime']['day'] = None
        self._defaults['GetExtCalLastDateAndTime']['hour'] = None
        self._defaults['GetExtCalLastDateAndTime']['minute'] = None
        self._defaults['GetExtCalLastTemp'] = {}
        self._defaults['GetExtCalLastTemp']['return'] = 0
        self._defaults['GetExtCalLastTemp']['temperature'] = None
        self._defaults['GetExtCalRecommendedInterval'] = {}
        self._defaults['GetExtCalRecommendedInterval']['return'] = 0
        self._defaults['GetExtCalRecommendedInterval']['months'] = None
        self._defaults['GetHardwareState'] = {}
        self._defaults['GetHardwareState']['return'] = 0
        self._defaults['GetHardwareState']['state'] = None
        self._defaults['GetLastExtCalLastDateAndTime'] = {}
        self._defaults['GetLastExtCalLastDateAndTime']['return'] = 0
        self._defaults['GetLastExtCalLastDateAndTime']['month'] = None
        self._defaults['GetLastSelfCalLastDateAndTime'] = {}
        self._defaults['GetLastSelfCalLastDateAndTime']['return'] = 0
        self._defaults['GetLastSelfCalLastDateAndTime']['month'] = None
        self._defaults['GetSelfCalLastDateAndTime'] = {}
        self._defaults['GetSelfCalLastDateAndTime']['return'] = 0
        self._defaults['GetSelfCalLastDateAndTime']['year'] = None
        self._defaults['GetSelfCalLastDateAndTime']['month'] = None
        self._defaults['GetSelfCalLastDateAndTime']['day'] = None
        self._defaults['GetSelfCalLastDateAndTime']['hour'] = None
        self._defaults['GetSelfCalLastDateAndTime']['minute'] = None
        self._defaults['GetSelfCalLastTemp'] = {}
        self._defaults['GetSelfCalLastTemp']['return'] = 0
        self._defaults['GetSelfCalLastTemp']['temperature'] = None
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
        self._defaults['IsDone']['done'] = None
        self._defaults['LockSession'] = {}
        self._defaults['LockSession']['return'] = 0
        self._defaults['LockSession']['callerHasLock'] = None
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
        self._defaults['ReadCurrentTemperature']['temperature'] = None
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
        self._defaults['UnlockSession'] = {}
        self._defaults['UnlockSession']['return'] = 0
        self._defaults['UnlockSession']['callerHasLock'] = None
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
        if waveform_handle is not None:
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
        if sequence_handle is not None:
            sequence_handle.contents.value = self._defaults['CreateAdvancedArbSequence']['sequenceHandle']
        return self._defaults['CreateAdvancedArbSequence']['return']

    def niFgen_CreateArbSequence(self, vi, sequence_length, waveform_handles_array, loop_counts_array, sequence_handle):  # noqa: N802
        if self._defaults['CreateArbSequence']['return'] != 0:
            return self._defaults['CreateArbSequence']['return']
        # sequence_handle
        if self._defaults['CreateArbSequence']['sequenceHandle'] is None:
            raise MockFunctionCallError("niFgen_CreateArbSequence", param='sequenceHandle')
        if sequence_handle is not None:
            sequence_handle.contents.value = self._defaults['CreateArbSequence']['sequenceHandle']
        return self._defaults['CreateArbSequence']['return']

    def niFgen_CreateFreqList(self, vi, waveform, frequency_list_length, frequency_array, duration_array, frequency_list_handle):  # noqa: N802
        if self._defaults['CreateFreqList']['return'] != 0:
            return self._defaults['CreateFreqList']['return']
        # frequency_list_handle
        if self._defaults['CreateFreqList']['frequencyListHandle'] is None:
            raise MockFunctionCallError("niFgen_CreateFreqList", param='frequencyListHandle')
        if frequency_list_handle is not None:
            frequency_list_handle.contents.value = self._defaults['CreateFreqList']['frequencyListHandle']
        return self._defaults['CreateFreqList']['return']

    def niFgen_CreateWaveformF64(self, vi, channel_name, waveform_size, waveform_data_array, waveform_handle):  # noqa: N802
        if self._defaults['CreateWaveformF64']['return'] != 0:
            return self._defaults['CreateWaveformF64']['return']
        # waveform_handle
        if self._defaults['CreateWaveformF64']['waveformHandle'] is None:
            raise MockFunctionCallError("niFgen_CreateWaveformF64", param='waveformHandle')
        if waveform_handle is not None:
            waveform_handle.contents.value = self._defaults['CreateWaveformF64']['waveformHandle']
        return self._defaults['CreateWaveformF64']['return']

    def niFgen_CreateWaveformFromFileF64(self, vi, channel_name, file_name, byte_order, waveform_handle):  # noqa: N802
        if self._defaults['CreateWaveformFromFileF64']['return'] != 0:
            return self._defaults['CreateWaveformFromFileF64']['return']
        # waveform_handle
        if self._defaults['CreateWaveformFromFileF64']['waveformHandle'] is None:
            raise MockFunctionCallError("niFgen_CreateWaveformFromFileF64", param='waveformHandle')
        if waveform_handle is not None:
            waveform_handle.contents.value = self._defaults['CreateWaveformFromFileF64']['waveformHandle']
        return self._defaults['CreateWaveformFromFileF64']['return']

    def niFgen_CreateWaveformFromFileI16(self, vi, channel_name, file_name, byte_order, waveform_handle):  # noqa: N802
        if self._defaults['CreateWaveformFromFileI16']['return'] != 0:
            return self._defaults['CreateWaveformFromFileI16']['return']
        # waveform_handle
        if self._defaults['CreateWaveformFromFileI16']['waveformHandle'] is None:
            raise MockFunctionCallError("niFgen_CreateWaveformFromFileI16", param='waveformHandle')
        if waveform_handle is not None:
            waveform_handle.contents.value = self._defaults['CreateWaveformFromFileI16']['waveformHandle']
        return self._defaults['CreateWaveformFromFileI16']['return']

    def niFgen_CreateWaveformI16(self, vi, channel_name, waveform_size, waveform_data_array, waveform_handle):  # noqa: N802
        if self._defaults['CreateWaveformI16']['return'] != 0:
            return self._defaults['CreateWaveformI16']['return']
        # waveform_handle
        if self._defaults['CreateWaveformI16']['waveformHandle'] is None:
            raise MockFunctionCallError("niFgen_CreateWaveformI16", param='waveformHandle')
        if waveform_handle is not None:
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

    def niFgen_GetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViBoolean']['return'] != 0:
            return self._defaults['GetAttributeViBoolean']['return']
        # attribute_value
        if self._defaults['GetAttributeViBoolean']['attributeValue'] is None:
            raise MockFunctionCallError("niFgen_GetAttributeViBoolean", param='attributeValue')
        if attribute_value is not None:
            attribute_value.contents.value = self._defaults['GetAttributeViBoolean']['attributeValue']
        return self._defaults['GetAttributeViBoolean']['return']

    def niFgen_GetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViInt32']['return'] != 0:
            return self._defaults['GetAttributeViInt32']['return']
        # attribute_value
        if self._defaults['GetAttributeViInt32']['attributeValue'] is None:
            raise MockFunctionCallError("niFgen_GetAttributeViInt32", param='attributeValue')
        if attribute_value is not None:
            attribute_value.contents.value = self._defaults['GetAttributeViInt32']['attributeValue']
        return self._defaults['GetAttributeViInt32']['return']

    def niFgen_GetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViReal64']['return'] != 0:
            return self._defaults['GetAttributeViReal64']['return']
        # attribute_value
        if self._defaults['GetAttributeViReal64']['attributeValue'] is None:
            raise MockFunctionCallError("niFgen_GetAttributeViReal64", param='attributeValue')
        if attribute_value is not None:
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
        if error_code is not None:
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
        if self._defaults['GetExtCalLastDateAndTime']['year'] is None:
            raise MockFunctionCallError("niFgen_GetExtCalLastDateAndTime", param='year')
        if year is not None:
            year.contents.value = self._defaults['GetExtCalLastDateAndTime']['year']
        # month
        if self._defaults['GetExtCalLastDateAndTime']['month'] is None:
            raise MockFunctionCallError("niFgen_GetExtCalLastDateAndTime", param='month')
        if month is not None:
            month.contents.value = self._defaults['GetExtCalLastDateAndTime']['month']
        # day
        if self._defaults['GetExtCalLastDateAndTime']['day'] is None:
            raise MockFunctionCallError("niFgen_GetExtCalLastDateAndTime", param='day')
        if day is not None:
            day.contents.value = self._defaults['GetExtCalLastDateAndTime']['day']
        # hour
        if self._defaults['GetExtCalLastDateAndTime']['hour'] is None:
            raise MockFunctionCallError("niFgen_GetExtCalLastDateAndTime", param='hour')
        if hour is not None:
            hour.contents.value = self._defaults['GetExtCalLastDateAndTime']['hour']
        # minute
        if self._defaults['GetExtCalLastDateAndTime']['minute'] is None:
            raise MockFunctionCallError("niFgen_GetExtCalLastDateAndTime", param='minute')
        if minute is not None:
            minute.contents.value = self._defaults['GetExtCalLastDateAndTime']['minute']
        return self._defaults['GetExtCalLastDateAndTime']['return']

    def niFgen_GetExtCalLastTemp(self, vi, temperature):  # noqa: N802
        if self._defaults['GetExtCalLastTemp']['return'] != 0:
            return self._defaults['GetExtCalLastTemp']['return']
        # temperature
        if self._defaults['GetExtCalLastTemp']['temperature'] is None:
            raise MockFunctionCallError("niFgen_GetExtCalLastTemp", param='temperature')
        if temperature is not None:
            temperature.contents.value = self._defaults['GetExtCalLastTemp']['temperature']
        return self._defaults['GetExtCalLastTemp']['return']

    def niFgen_GetExtCalRecommendedInterval(self, vi, months):  # noqa: N802
        if self._defaults['GetExtCalRecommendedInterval']['return'] != 0:
            return self._defaults['GetExtCalRecommendedInterval']['return']
        # months
        if self._defaults['GetExtCalRecommendedInterval']['months'] is None:
            raise MockFunctionCallError("niFgen_GetExtCalRecommendedInterval", param='months')
        if months is not None:
            months.contents.value = self._defaults['GetExtCalRecommendedInterval']['months']
        return self._defaults['GetExtCalRecommendedInterval']['return']

    def niFgen_GetHardwareState(self, vi, state):  # noqa: N802
        if self._defaults['GetHardwareState']['return'] != 0:
            return self._defaults['GetHardwareState']['return']
        # state
        if self._defaults['GetHardwareState']['state'] is None:
            raise MockFunctionCallError("niFgen_GetHardwareState", param='state')
        if state is not None:
            state.contents.value = self._defaults['GetHardwareState']['state']
        return self._defaults['GetHardwareState']['return']

    def niFgen_GetLastExtCalLastDateAndTime(self, vi, month):  # noqa: N802
        if self._defaults['GetLastExtCalLastDateAndTime']['return'] != 0:
            return self._defaults['GetLastExtCalLastDateAndTime']['return']
        # month
        if self._defaults['GetLastExtCalLastDateAndTime']['month'] is None:
            raise MockFunctionCallError("niFgen_GetLastExtCalLastDateAndTime", param='month')
        if month is not None:
            month.contents.value = self._defaults['GetLastExtCalLastDateAndTime']['month']
        return self._defaults['GetLastExtCalLastDateAndTime']['return']

    def niFgen_GetLastSelfCalLastDateAndTime(self, vi, month):  # noqa: N802
        if self._defaults['GetLastSelfCalLastDateAndTime']['return'] != 0:
            return self._defaults['GetLastSelfCalLastDateAndTime']['return']
        # month
        if self._defaults['GetLastSelfCalLastDateAndTime']['month'] is None:
            raise MockFunctionCallError("niFgen_GetLastSelfCalLastDateAndTime", param='month')
        if month is not None:
            month.contents.value = self._defaults['GetLastSelfCalLastDateAndTime']['month']
        return self._defaults['GetLastSelfCalLastDateAndTime']['return']

    def niFgen_GetSelfCalLastDateAndTime(self, vi, year, month, day, hour, minute):  # noqa: N802
        if self._defaults['GetSelfCalLastDateAndTime']['return'] != 0:
            return self._defaults['GetSelfCalLastDateAndTime']['return']
        # year
        if self._defaults['GetSelfCalLastDateAndTime']['year'] is None:
            raise MockFunctionCallError("niFgen_GetSelfCalLastDateAndTime", param='year')
        if year is not None:
            year.contents.value = self._defaults['GetSelfCalLastDateAndTime']['year']
        # month
        if self._defaults['GetSelfCalLastDateAndTime']['month'] is None:
            raise MockFunctionCallError("niFgen_GetSelfCalLastDateAndTime", param='month')
        if month is not None:
            month.contents.value = self._defaults['GetSelfCalLastDateAndTime']['month']
        # day
        if self._defaults['GetSelfCalLastDateAndTime']['day'] is None:
            raise MockFunctionCallError("niFgen_GetSelfCalLastDateAndTime", param='day')
        if day is not None:
            day.contents.value = self._defaults['GetSelfCalLastDateAndTime']['day']
        # hour
        if self._defaults['GetSelfCalLastDateAndTime']['hour'] is None:
            raise MockFunctionCallError("niFgen_GetSelfCalLastDateAndTime", param='hour')
        if hour is not None:
            hour.contents.value = self._defaults['GetSelfCalLastDateAndTime']['hour']
        # minute
        if self._defaults['GetSelfCalLastDateAndTime']['minute'] is None:
            raise MockFunctionCallError("niFgen_GetSelfCalLastDateAndTime", param='minute')
        if minute is not None:
            minute.contents.value = self._defaults['GetSelfCalLastDateAndTime']['minute']
        return self._defaults['GetSelfCalLastDateAndTime']['return']

    def niFgen_GetSelfCalLastTemp(self, vi, temperature):  # noqa: N802
        if self._defaults['GetSelfCalLastTemp']['return'] != 0:
            return self._defaults['GetSelfCalLastTemp']['return']
        # temperature
        if self._defaults['GetSelfCalLastTemp']['temperature'] is None:
            raise MockFunctionCallError("niFgen_GetSelfCalLastTemp", param='temperature')
        if temperature is not None:
            temperature.contents.value = self._defaults['GetSelfCalLastTemp']['temperature']
        return self._defaults['GetSelfCalLastTemp']['return']

    def niFgen_GetSelfCalSupported(self, vi, self_cal_supported):  # noqa: N802
        if self._defaults['GetSelfCalSupported']['return'] != 0:
            return self._defaults['GetSelfCalSupported']['return']
        # self_cal_supported
        if self._defaults['GetSelfCalSupported']['selfCalSupported'] is None:
            raise MockFunctionCallError("niFgen_GetSelfCalSupported", param='selfCalSupported')
        if self_cal_supported is not None:
            self_cal_supported.contents.value = self._defaults['GetSelfCalSupported']['selfCalSupported']
        return self._defaults['GetSelfCalSupported']['return']

    def niFgen_InitializeWithChannels(self, resource_name, channel_name, reset_device, option_string, vi):  # noqa: N802
        if self._defaults['InitializeWithChannels']['return'] != 0:
            return self._defaults['InitializeWithChannels']['return']
        # vi
        if self._defaults['InitializeWithChannels']['vi'] is None:
            raise MockFunctionCallError("niFgen_InitializeWithChannels", param='vi')
        if vi is not None:
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
        if self._defaults['IsDone']['done'] is None:
            raise MockFunctionCallError("niFgen_IsDone", param='done')
        if done is not None:
            done.contents.value = self._defaults['IsDone']['done']
        return self._defaults['IsDone']['return']

    def niFgen_LockSession(self, vi, caller_has_lock):  # noqa: N802
        if self._defaults['LockSession']['return'] != 0:
            return self._defaults['LockSession']['return']
        # caller_has_lock
        if self._defaults['LockSession']['callerHasLock'] is None:
            raise MockFunctionCallError("niFgen_LockSession", param='callerHasLock')
        if caller_has_lock is not None:
            caller_has_lock.contents.value = self._defaults['LockSession']['callerHasLock']
        return self._defaults['LockSession']['return']

    def niFgen_QueryArbSeqCapabilities(self, vi, maximum_number_of_sequences, minimum_sequence_length, maximum_sequence_length, maximum_loop_count):  # noqa: N802
        if self._defaults['QueryArbSeqCapabilities']['return'] != 0:
            return self._defaults['QueryArbSeqCapabilities']['return']
        # maximum_number_of_sequences
        if self._defaults['QueryArbSeqCapabilities']['maximumNumberOfSequences'] is None:
            raise MockFunctionCallError("niFgen_QueryArbSeqCapabilities", param='maximumNumberOfSequences')
        if maximum_number_of_sequences is not None:
            maximum_number_of_sequences.contents.value = self._defaults['QueryArbSeqCapabilities']['maximumNumberOfSequences']
        # minimum_sequence_length
        if self._defaults['QueryArbSeqCapabilities']['minimumSequenceLength'] is None:
            raise MockFunctionCallError("niFgen_QueryArbSeqCapabilities", param='minimumSequenceLength')
        if minimum_sequence_length is not None:
            minimum_sequence_length.contents.value = self._defaults['QueryArbSeqCapabilities']['minimumSequenceLength']
        # maximum_sequence_length
        if self._defaults['QueryArbSeqCapabilities']['maximumSequenceLength'] is None:
            raise MockFunctionCallError("niFgen_QueryArbSeqCapabilities", param='maximumSequenceLength')
        if maximum_sequence_length is not None:
            maximum_sequence_length.contents.value = self._defaults['QueryArbSeqCapabilities']['maximumSequenceLength']
        # maximum_loop_count
        if self._defaults['QueryArbSeqCapabilities']['maximumLoopCount'] is None:
            raise MockFunctionCallError("niFgen_QueryArbSeqCapabilities", param='maximumLoopCount')
        if maximum_loop_count is not None:
            maximum_loop_count.contents.value = self._defaults['QueryArbSeqCapabilities']['maximumLoopCount']
        return self._defaults['QueryArbSeqCapabilities']['return']

    def niFgen_QueryArbWfmCapabilities(self, vi, maximum_number_of_waveforms, waveform_quantum, minimum_waveform_size, maximum_waveform_size):  # noqa: N802
        if self._defaults['QueryArbWfmCapabilities']['return'] != 0:
            return self._defaults['QueryArbWfmCapabilities']['return']
        # maximum_number_of_waveforms
        if self._defaults['QueryArbWfmCapabilities']['maximumNumberOfWaveforms'] is None:
            raise MockFunctionCallError("niFgen_QueryArbWfmCapabilities", param='maximumNumberOfWaveforms')
        if maximum_number_of_waveforms is not None:
            maximum_number_of_waveforms.contents.value = self._defaults['QueryArbWfmCapabilities']['maximumNumberOfWaveforms']
        # waveform_quantum
        if self._defaults['QueryArbWfmCapabilities']['waveformQuantum'] is None:
            raise MockFunctionCallError("niFgen_QueryArbWfmCapabilities", param='waveformQuantum')
        if waveform_quantum is not None:
            waveform_quantum.contents.value = self._defaults['QueryArbWfmCapabilities']['waveformQuantum']
        # minimum_waveform_size
        if self._defaults['QueryArbWfmCapabilities']['minimumWaveformSize'] is None:
            raise MockFunctionCallError("niFgen_QueryArbWfmCapabilities", param='minimumWaveformSize')
        if minimum_waveform_size is not None:
            minimum_waveform_size.contents.value = self._defaults['QueryArbWfmCapabilities']['minimumWaveformSize']
        # maximum_waveform_size
        if self._defaults['QueryArbWfmCapabilities']['maximumWaveformSize'] is None:
            raise MockFunctionCallError("niFgen_QueryArbWfmCapabilities", param='maximumWaveformSize')
        if maximum_waveform_size is not None:
            maximum_waveform_size.contents.value = self._defaults['QueryArbWfmCapabilities']['maximumWaveformSize']
        return self._defaults['QueryArbWfmCapabilities']['return']

    def niFgen_QueryFreqListCapabilities(self, vi, maximum_number_of_freq_lists, minimum_frequency_list_length, maximum_frequency_list_length, minimum_frequency_list_duration, maximum_frequency_list_duration, frequency_list_duration_quantum):  # noqa: N802
        if self._defaults['QueryFreqListCapabilities']['return'] != 0:
            return self._defaults['QueryFreqListCapabilities']['return']
        # maximum_number_of_freq_lists
        if self._defaults['QueryFreqListCapabilities']['maximumNumberOfFreqLists'] is None:
            raise MockFunctionCallError("niFgen_QueryFreqListCapabilities", param='maximumNumberOfFreqLists')
        if maximum_number_of_freq_lists is not None:
            maximum_number_of_freq_lists.contents.value = self._defaults['QueryFreqListCapabilities']['maximumNumberOfFreqLists']
        # minimum_frequency_list_length
        if self._defaults['QueryFreqListCapabilities']['minimumFrequencyListLength'] is None:
            raise MockFunctionCallError("niFgen_QueryFreqListCapabilities", param='minimumFrequencyListLength')
        if minimum_frequency_list_length is not None:
            minimum_frequency_list_length.contents.value = self._defaults['QueryFreqListCapabilities']['minimumFrequencyListLength']
        # maximum_frequency_list_length
        if self._defaults['QueryFreqListCapabilities']['maximumFrequencyListLength'] is None:
            raise MockFunctionCallError("niFgen_QueryFreqListCapabilities", param='maximumFrequencyListLength')
        if maximum_frequency_list_length is not None:
            maximum_frequency_list_length.contents.value = self._defaults['QueryFreqListCapabilities']['maximumFrequencyListLength']
        # minimum_frequency_list_duration
        if self._defaults['QueryFreqListCapabilities']['minimumFrequencyListDuration'] is None:
            raise MockFunctionCallError("niFgen_QueryFreqListCapabilities", param='minimumFrequencyListDuration')
        if minimum_frequency_list_duration is not None:
            minimum_frequency_list_duration.contents.value = self._defaults['QueryFreqListCapabilities']['minimumFrequencyListDuration']
        # maximum_frequency_list_duration
        if self._defaults['QueryFreqListCapabilities']['maximumFrequencyListDuration'] is None:
            raise MockFunctionCallError("niFgen_QueryFreqListCapabilities", param='maximumFrequencyListDuration')
        if maximum_frequency_list_duration is not None:
            maximum_frequency_list_duration.contents.value = self._defaults['QueryFreqListCapabilities']['maximumFrequencyListDuration']
        # frequency_list_duration_quantum
        if self._defaults['QueryFreqListCapabilities']['frequencyListDurationQuantum'] is None:
            raise MockFunctionCallError("niFgen_QueryFreqListCapabilities", param='frequencyListDurationQuantum')
        if frequency_list_duration_quantum is not None:
            frequency_list_duration_quantum.contents.value = self._defaults['QueryFreqListCapabilities']['frequencyListDurationQuantum']
        return self._defaults['QueryFreqListCapabilities']['return']

    def niFgen_ReadCurrentTemperature(self, vi, temperature):  # noqa: N802
        if self._defaults['ReadCurrentTemperature']['return'] != 0:
            return self._defaults['ReadCurrentTemperature']['return']
        # temperature
        if self._defaults['ReadCurrentTemperature']['temperature'] is None:
            raise MockFunctionCallError("niFgen_ReadCurrentTemperature", param='temperature')
        if temperature is not None:
            temperature.contents.value = self._defaults['ReadCurrentTemperature']['temperature']
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

    def niFgen_UnlockSession(self, vi, caller_has_lock):  # noqa: N802
        if self._defaults['UnlockSession']['return'] != 0:
            return self._defaults['UnlockSession']['return']
        # caller_has_lock
        if self._defaults['UnlockSession']['callerHasLock'] is None:
            raise MockFunctionCallError("niFgen_UnlockSession", param='callerHasLock')
        if caller_has_lock is not None:
            caller_has_lock.contents.value = self._defaults['UnlockSession']['callerHasLock']
        return self._defaults['UnlockSession']['return']

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
        if self_test_result is not None:
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
        mock_library.niFgen_GetHardwareState.side_effect = MockFunctionCallError("niFgen_GetHardwareState")
        mock_library.niFgen_GetHardwareState.return_value = 0
        mock_library.niFgen_GetLastExtCalLastDateAndTime.side_effect = MockFunctionCallError("niFgen_GetLastExtCalLastDateAndTime")
        mock_library.niFgen_GetLastExtCalLastDateAndTime.return_value = 0
        mock_library.niFgen_GetLastSelfCalLastDateAndTime.side_effect = MockFunctionCallError("niFgen_GetLastSelfCalLastDateAndTime")
        mock_library.niFgen_GetLastSelfCalLastDateAndTime.return_value = 0
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
        mock_library.niFgen_LockSession.side_effect = MockFunctionCallError("niFgen_LockSession")
        mock_library.niFgen_LockSession.return_value = 0
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
        mock_library.niFgen_UnlockSession.side_effect = MockFunctionCallError("niFgen_UnlockSession")
        mock_library.niFgen_UnlockSession.return_value = 0
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
        mock_library.niFgen_close.side_effect = MockFunctionCallError("niFgen_close")
        mock_library.niFgen_close.return_value = 0
        mock_library.niFgen_error_message.side_effect = MockFunctionCallError("niFgen_error_message")
        mock_library.niFgen_error_message.return_value = 0
        mock_library.niFgen_reset.side_effect = MockFunctionCallError("niFgen_reset")
        mock_library.niFgen_reset.return_value = 0
        mock_library.niFgen_self_test.side_effect = MockFunctionCallError("niFgen_self_test")
        mock_library.niFgen_self_test.return_value = 0
