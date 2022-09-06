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
        self._defaults['AbortKeepAlive'] = {}
        self._defaults['AbortKeepAlive']['return'] = 0
        self._defaults['ApplyLevelsAndTiming'] = {}
        self._defaults['ApplyLevelsAndTiming']['return'] = 0
        self._defaults['ApplyTDROffsets'] = {}
        self._defaults['ApplyTDROffsets']['return'] = 0
        self._defaults['BurstPattern'] = {}
        self._defaults['BurstPattern']['return'] = 0
        self._defaults['ClockGenerator_Abort'] = {}
        self._defaults['ClockGenerator_Abort']['return'] = 0
        self._defaults['ClockGenerator_GenerateClock'] = {}
        self._defaults['ClockGenerator_GenerateClock']['return'] = 0
        self._defaults['Commit'] = {}
        self._defaults['Commit']['return'] = 0
        self._defaults['ConfigureActiveLoadLevels'] = {}
        self._defaults['ConfigureActiveLoadLevels']['return'] = 0
        self._defaults['ConfigurePatternBurstSites'] = {}
        self._defaults['ConfigurePatternBurstSites']['return'] = 0
        self._defaults['ConfigureTimeSetCompareEdgesStrobe'] = {}
        self._defaults['ConfigureTimeSetCompareEdgesStrobe']['return'] = 0
        self._defaults['ConfigureTimeSetCompareEdgesStrobe2x'] = {}
        self._defaults['ConfigureTimeSetCompareEdgesStrobe2x']['return'] = 0
        self._defaults['ConfigureTimeSetDriveEdges'] = {}
        self._defaults['ConfigureTimeSetDriveEdges']['return'] = 0
        self._defaults['ConfigureTimeSetDriveEdges2x'] = {}
        self._defaults['ConfigureTimeSetDriveEdges2x']['return'] = 0
        self._defaults['ConfigureTimeSetDriveFormat'] = {}
        self._defaults['ConfigureTimeSetDriveFormat']['return'] = 0
        self._defaults['ConfigureTimeSetEdge'] = {}
        self._defaults['ConfigureTimeSetEdge']['return'] = 0
        self._defaults['ConfigureTimeSetEdgeMultiplier'] = {}
        self._defaults['ConfigureTimeSetEdgeMultiplier']['return'] = 0
        self._defaults['ConfigureTimeSetPeriod'] = {}
        self._defaults['ConfigureTimeSetPeriod']['return'] = 0
        self._defaults['ConfigureVoltageLevels'] = {}
        self._defaults['ConfigureVoltageLevels']['return'] = 0
        self._defaults['CreateCaptureWaveformFromFileDigicapture'] = {}
        self._defaults['CreateCaptureWaveformFromFileDigicapture']['return'] = 0
        self._defaults['CreateCaptureWaveformParallel'] = {}
        self._defaults['CreateCaptureWaveformParallel']['return'] = 0
        self._defaults['CreateCaptureWaveformSerial'] = {}
        self._defaults['CreateCaptureWaveformSerial']['return'] = 0
        self._defaults['CreateSourceWaveformFromFileTDMS'] = {}
        self._defaults['CreateSourceWaveformFromFileTDMS']['return'] = 0
        self._defaults['CreateSourceWaveformParallel'] = {}
        self._defaults['CreateSourceWaveformParallel']['return'] = 0
        self._defaults['CreateSourceWaveformSerial'] = {}
        self._defaults['CreateSourceWaveformSerial']['return'] = 0
        self._defaults['CreateTimeSet'] = {}
        self._defaults['CreateTimeSet']['return'] = 0
        self._defaults['DeleteAllTimeSets'] = {}
        self._defaults['DeleteAllTimeSets']['return'] = 0
        self._defaults['DisableSites'] = {}
        self._defaults['DisableSites']['return'] = 0
        self._defaults['EnableSites'] = {}
        self._defaults['EnableSites']['return'] = 0
        self._defaults['FetchHistoryRAMCycleInformation'] = {}
        self._defaults['FetchHistoryRAMCycleInformation']['return'] = 0
        self._defaults['FetchHistoryRAMCycleInformation']['patternIndex'] = None
        self._defaults['FetchHistoryRAMCycleInformation']['timeSetIndex'] = None
        self._defaults['FetchHistoryRAMCycleInformation']['vectorNumber'] = None
        self._defaults['FetchHistoryRAMCycleInformation']['cycleNumber'] = None
        self._defaults['FetchHistoryRAMCycleInformation']['numDutCycles'] = None
        self._defaults['FetchHistoryRAMCyclePinData'] = {}
        self._defaults['FetchHistoryRAMCyclePinData']['return'] = 0
        self._defaults['FetchHistoryRAMCyclePinData']['actualNumPinData'] = None
        self._defaults['FetchHistoryRAMCyclePinData']['expectedPinStates'] = None
        self._defaults['FetchHistoryRAMCyclePinData']['actualPinStates'] = None
        self._defaults['FetchHistoryRAMCyclePinData']['perPinPassFail'] = None
        self._defaults['FetchHistoryRAMScanCycleNumber'] = {}
        self._defaults['FetchHistoryRAMScanCycleNumber']['return'] = 0
        self._defaults['FetchHistoryRAMScanCycleNumber']['scanCycleNumber'] = None
        self._defaults['FrequencyCounter_MeasureFrequency'] = {}
        self._defaults['FrequencyCounter_MeasureFrequency']['return'] = 0
        self._defaults['FrequencyCounter_MeasureFrequency']['actualNumFrequencies'] = None
        self._defaults['FrequencyCounter_MeasureFrequency']['frequencies'] = None
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
        self._defaults['GetChannelNameFromString']['names'] = None
        self._defaults['GetError'] = {}
        self._defaults['GetError']['return'] = 0
        self._defaults['GetError']['errorCode'] = None
        self._defaults['GetError']['errorDescription'] = None
        self._defaults['GetFailCount'] = {}
        self._defaults['GetFailCount']['return'] = 0
        self._defaults['GetFailCount']['actualNumRead'] = None
        self._defaults['GetFailCount']['failureCount'] = None
        self._defaults['GetHistoryRAMSampleCount'] = {}
        self._defaults['GetHistoryRAMSampleCount']['return'] = 0
        self._defaults['GetHistoryRAMSampleCount']['sampleCount'] = None
        self._defaults['GetPatternName'] = {}
        self._defaults['GetPatternName']['return'] = 0
        self._defaults['GetPatternName']['name'] = None
        self._defaults['GetPatternPinList'] = {}
        self._defaults['GetPatternPinList']['return'] = 0
        self._defaults['GetPatternPinList']['pinList'] = None
        self._defaults['GetPinName'] = {}
        self._defaults['GetPinName']['return'] = 0
        self._defaults['GetPinName']['name'] = None
        self._defaults['GetPinResultsPinInformation'] = {}
        self._defaults['GetPinResultsPinInformation']['return'] = 0
        self._defaults['GetPinResultsPinInformation']['actualNumValues'] = None
        self._defaults['GetPinResultsPinInformation']['pinIndexes'] = None
        self._defaults['GetPinResultsPinInformation']['siteNumbers'] = None
        self._defaults['GetPinResultsPinInformation']['channelIndexes'] = None
        self._defaults['GetSitePassFail'] = {}
        self._defaults['GetSitePassFail']['return'] = 0
        self._defaults['GetSitePassFail']['actualNumSites'] = None
        self._defaults['GetSitePassFail']['passFail'] = None
        self._defaults['GetSiteResultsSiteNumbers'] = {}
        self._defaults['GetSiteResultsSiteNumbers']['return'] = 0
        self._defaults['GetSiteResultsSiteNumbers']['actualNumSiteNumbers'] = None
        self._defaults['GetSiteResultsSiteNumbers']['siteNumbers'] = None
        self._defaults['GetTimeSetDriveFormat'] = {}
        self._defaults['GetTimeSetDriveFormat']['return'] = 0
        self._defaults['GetTimeSetDriveFormat']['format'] = None
        self._defaults['GetTimeSetEdge'] = {}
        self._defaults['GetTimeSetEdge']['return'] = 0
        self._defaults['GetTimeSetEdge']['time'] = None
        self._defaults['GetTimeSetEdgeMultiplier'] = {}
        self._defaults['GetTimeSetEdgeMultiplier']['return'] = 0
        self._defaults['GetTimeSetEdgeMultiplier']['edgeMultiplier'] = None
        self._defaults['GetTimeSetName'] = {}
        self._defaults['GetTimeSetName']['return'] = 0
        self._defaults['GetTimeSetName']['name'] = None
        self._defaults['GetTimeSetPeriod'] = {}
        self._defaults['GetTimeSetPeriod']['return'] = 0
        self._defaults['GetTimeSetPeriod']['period'] = None
        self._defaults['InitWithOptions'] = {}
        self._defaults['InitWithOptions']['return'] = 0
        self._defaults['InitWithOptions']['newVi'] = None
        self._defaults['Initiate'] = {}
        self._defaults['Initiate']['return'] = 0
        self._defaults['IsDone'] = {}
        self._defaults['IsDone']['return'] = 0
        self._defaults['IsDone']['done'] = None
        self._defaults['IsSiteEnabled'] = {}
        self._defaults['IsSiteEnabled']['return'] = 0
        self._defaults['IsSiteEnabled']['enable'] = None
        self._defaults['LoadLevels'] = {}
        self._defaults['LoadLevels']['return'] = 0
        self._defaults['LoadPattern'] = {}
        self._defaults['LoadPattern']['return'] = 0
        self._defaults['LoadPinMap'] = {}
        self._defaults['LoadPinMap']['return'] = 0
        self._defaults['LoadSpecifications'] = {}
        self._defaults['LoadSpecifications']['return'] = 0
        self._defaults['LoadTiming'] = {}
        self._defaults['LoadTiming']['return'] = 0
        self._defaults['LockSession'] = {}
        self._defaults['LockSession']['return'] = 0
        self._defaults['LockSession']['callerHasLock'] = None
        self._defaults['PPMU_Measure'] = {}
        self._defaults['PPMU_Measure']['return'] = 0
        self._defaults['PPMU_Measure']['actualNumRead'] = None
        self._defaults['PPMU_Measure']['measurements'] = None
        self._defaults['PPMU_Source'] = {}
        self._defaults['PPMU_Source']['return'] = 0
        self._defaults['ReadSequencerFlag'] = {}
        self._defaults['ReadSequencerFlag']['return'] = 0
        self._defaults['ReadSequencerFlag']['value'] = None
        self._defaults['ReadSequencerRegister'] = {}
        self._defaults['ReadSequencerRegister']['return'] = 0
        self._defaults['ReadSequencerRegister']['value'] = None
        self._defaults['ReadStatic'] = {}
        self._defaults['ReadStatic']['return'] = 0
        self._defaults['ReadStatic']['actualNumRead'] = None
        self._defaults['ReadStatic']['data'] = None
        self._defaults['ResetDevice'] = {}
        self._defaults['ResetDevice']['return'] = 0
        self._defaults['SelfCalibrate'] = {}
        self._defaults['SelfCalibrate']['return'] = 0
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
        self._defaults['SetAttributeViString'] = {}
        self._defaults['SetAttributeViString']['return'] = 0
        self._defaults['TDR'] = {}
        self._defaults['TDR']['return'] = 0
        self._defaults['TDR']['actualNumOffsets'] = None
        self._defaults['TDR']['offsets'] = None
        self._defaults['UnloadAllPatterns'] = {}
        self._defaults['UnloadAllPatterns']['return'] = 0
        self._defaults['UnloadSpecifications'] = {}
        self._defaults['UnloadSpecifications']['return'] = 0
        self._defaults['UnlockSession'] = {}
        self._defaults['UnlockSession']['return'] = 0
        self._defaults['UnlockSession']['callerHasLock'] = None
        self._defaults['WaitUntilDone'] = {}
        self._defaults['WaitUntilDone']['return'] = 0
        self._defaults['WriteSequencerFlag'] = {}
        self._defaults['WriteSequencerFlag']['return'] = 0
        self._defaults['WriteSequencerRegister'] = {}
        self._defaults['WriteSequencerRegister']['return'] = 0
        self._defaults['WriteSourceWaveformBroadcastU32'] = {}
        self._defaults['WriteSourceWaveformBroadcastU32']['return'] = 0
        self._defaults['WriteSourceWaveformDataFromFileTDMS'] = {}
        self._defaults['WriteSourceWaveformDataFromFileTDMS']['return'] = 0
        self._defaults['WriteSourceWaveformSiteUniqueU32'] = {}
        self._defaults['WriteSourceWaveformSiteUniqueU32']['return'] = 0
        self._defaults['WriteStatic'] = {}
        self._defaults['WriteStatic']['return'] = 0
        self._defaults['close'] = {}
        self._defaults['close']['return'] = 0
        self._defaults['error_message'] = {}
        self._defaults['error_message']['return'] = 0
        self._defaults['error_message']['errorMessage'] = None
        self._defaults['reset'] = {}
        self._defaults['reset']['return'] = 0
        self._defaults['self_test'] = {}
        self._defaults['self_test']['return'] = 0
        self._defaults['self_test']['testResult'] = None
        self._defaults['self_test']['testMessage'] = None

    def __getitem__(self, func):
        return self._defaults[func]

    def __setitem__(self, func, val):
        self._defaults[func] = val

    def niDigital_Abort(self, vi):  # noqa: N802
        if self._defaults['Abort']['return'] != 0:
            return self._defaults['Abort']['return']
        return self._defaults['Abort']['return']

    def niDigital_AbortKeepAlive(self, vi):  # noqa: N802
        if self._defaults['AbortKeepAlive']['return'] != 0:
            return self._defaults['AbortKeepAlive']['return']
        return self._defaults['AbortKeepAlive']['return']

    def niDigital_ApplyLevelsAndTiming(self, vi, site_list, levels_sheet, timing_sheet, initial_state_high_pins, initial_state_low_pins, initial_state_tristate_pins):  # noqa: N802
        if self._defaults['ApplyLevelsAndTiming']['return'] != 0:
            return self._defaults['ApplyLevelsAndTiming']['return']
        return self._defaults['ApplyLevelsAndTiming']['return']

    def niDigital_ApplyTDROffsets(self, vi, channel_list, num_offsets, offsets):  # noqa: N802
        if self._defaults['ApplyTDROffsets']['return'] != 0:
            return self._defaults['ApplyTDROffsets']['return']
        return self._defaults['ApplyTDROffsets']['return']

    def niDigital_BurstPattern(self, vi, site_list, start_label, select_digital_function, wait_until_done, timeout):  # noqa: N802
        if self._defaults['BurstPattern']['return'] != 0:
            return self._defaults['BurstPattern']['return']
        return self._defaults['BurstPattern']['return']

    def niDigital_ClockGenerator_Abort(self, vi, channel_list):  # noqa: N802
        if self._defaults['ClockGenerator_Abort']['return'] != 0:
            return self._defaults['ClockGenerator_Abort']['return']
        return self._defaults['ClockGenerator_Abort']['return']

    def niDigital_ClockGenerator_GenerateClock(self, vi, channel_list, frequency, select_digital_function):  # noqa: N802
        if self._defaults['ClockGenerator_GenerateClock']['return'] != 0:
            return self._defaults['ClockGenerator_GenerateClock']['return']
        return self._defaults['ClockGenerator_GenerateClock']['return']

    def niDigital_Commit(self, vi):  # noqa: N802
        if self._defaults['Commit']['return'] != 0:
            return self._defaults['Commit']['return']
        return self._defaults['Commit']['return']

    def niDigital_ConfigureActiveLoadLevels(self, vi, channel_list, iol, ioh, vcom):  # noqa: N802
        if self._defaults['ConfigureActiveLoadLevels']['return'] != 0:
            return self._defaults['ConfigureActiveLoadLevels']['return']
        return self._defaults['ConfigureActiveLoadLevels']['return']

    def niDigital_ConfigurePatternBurstSites(self, vi, site_list):  # noqa: N802
        if self._defaults['ConfigurePatternBurstSites']['return'] != 0:
            return self._defaults['ConfigurePatternBurstSites']['return']
        return self._defaults['ConfigurePatternBurstSites']['return']

    def niDigital_ConfigureTimeSetCompareEdgesStrobe(self, vi, pin_list, time_set_name, strobe_edge):  # noqa: N802
        if self._defaults['ConfigureTimeSetCompareEdgesStrobe']['return'] != 0:
            return self._defaults['ConfigureTimeSetCompareEdgesStrobe']['return']
        return self._defaults['ConfigureTimeSetCompareEdgesStrobe']['return']

    def niDigital_ConfigureTimeSetCompareEdgesStrobe2x(self, vi, pin_list, time_set_name, strobe_edge, strobe2_edge):  # noqa: N802
        if self._defaults['ConfigureTimeSetCompareEdgesStrobe2x']['return'] != 0:
            return self._defaults['ConfigureTimeSetCompareEdgesStrobe2x']['return']
        return self._defaults['ConfigureTimeSetCompareEdgesStrobe2x']['return']

    def niDigital_ConfigureTimeSetDriveEdges(self, vi, pin_list, time_set_name, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge):  # noqa: N802
        if self._defaults['ConfigureTimeSetDriveEdges']['return'] != 0:
            return self._defaults['ConfigureTimeSetDriveEdges']['return']
        return self._defaults['ConfigureTimeSetDriveEdges']['return']

    def niDigital_ConfigureTimeSetDriveEdges2x(self, vi, pin_list, time_set_name, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge, drive_data2_edge, drive_return2_edge):  # noqa: N802
        if self._defaults['ConfigureTimeSetDriveEdges2x']['return'] != 0:
            return self._defaults['ConfigureTimeSetDriveEdges2x']['return']
        return self._defaults['ConfigureTimeSetDriveEdges2x']['return']

    def niDigital_ConfigureTimeSetDriveFormat(self, vi, pin_list, time_set_name, drive_format):  # noqa: N802
        if self._defaults['ConfigureTimeSetDriveFormat']['return'] != 0:
            return self._defaults['ConfigureTimeSetDriveFormat']['return']
        return self._defaults['ConfigureTimeSetDriveFormat']['return']

    def niDigital_ConfigureTimeSetEdge(self, vi, pin_list, time_set_name, edge, time):  # noqa: N802
        if self._defaults['ConfigureTimeSetEdge']['return'] != 0:
            return self._defaults['ConfigureTimeSetEdge']['return']
        return self._defaults['ConfigureTimeSetEdge']['return']

    def niDigital_ConfigureTimeSetEdgeMultiplier(self, vi, pin_list, time_set_name, edge_multiplier):  # noqa: N802
        if self._defaults['ConfigureTimeSetEdgeMultiplier']['return'] != 0:
            return self._defaults['ConfigureTimeSetEdgeMultiplier']['return']
        return self._defaults['ConfigureTimeSetEdgeMultiplier']['return']

    def niDigital_ConfigureTimeSetPeriod(self, vi, time_set_name, period):  # noqa: N802
        if self._defaults['ConfigureTimeSetPeriod']['return'] != 0:
            return self._defaults['ConfigureTimeSetPeriod']['return']
        return self._defaults['ConfigureTimeSetPeriod']['return']

    def niDigital_ConfigureVoltageLevels(self, vi, channel_list, vil, vih, vol, voh, vterm):  # noqa: N802
        if self._defaults['ConfigureVoltageLevels']['return'] != 0:
            return self._defaults['ConfigureVoltageLevels']['return']
        return self._defaults['ConfigureVoltageLevels']['return']

    def niDigital_CreateCaptureWaveformFromFileDigicapture(self, vi, waveform_name, waveform_file_path):  # noqa: N802
        if self._defaults['CreateCaptureWaveformFromFileDigicapture']['return'] != 0:
            return self._defaults['CreateCaptureWaveformFromFileDigicapture']['return']
        return self._defaults['CreateCaptureWaveformFromFileDigicapture']['return']

    def niDigital_CreateCaptureWaveformParallel(self, vi, pin_list, waveform_name):  # noqa: N802
        if self._defaults['CreateCaptureWaveformParallel']['return'] != 0:
            return self._defaults['CreateCaptureWaveformParallel']['return']
        return self._defaults['CreateCaptureWaveformParallel']['return']

    def niDigital_CreateCaptureWaveformSerial(self, vi, pin_list, waveform_name, sample_width, bit_order):  # noqa: N802
        if self._defaults['CreateCaptureWaveformSerial']['return'] != 0:
            return self._defaults['CreateCaptureWaveformSerial']['return']
        return self._defaults['CreateCaptureWaveformSerial']['return']

    def niDigital_CreateSourceWaveformFromFileTDMS(self, vi, waveform_name, waveform_file_path, write_waveform_data):  # noqa: N802
        if self._defaults['CreateSourceWaveformFromFileTDMS']['return'] != 0:
            return self._defaults['CreateSourceWaveformFromFileTDMS']['return']
        return self._defaults['CreateSourceWaveformFromFileTDMS']['return']

    def niDigital_CreateSourceWaveformParallel(self, vi, pin_list, waveform_name, data_mapping):  # noqa: N802
        if self._defaults['CreateSourceWaveformParallel']['return'] != 0:
            return self._defaults['CreateSourceWaveformParallel']['return']
        return self._defaults['CreateSourceWaveformParallel']['return']

    def niDigital_CreateSourceWaveformSerial(self, vi, pin_list, waveform_name, data_mapping, sample_width, bit_order):  # noqa: N802
        if self._defaults['CreateSourceWaveformSerial']['return'] != 0:
            return self._defaults['CreateSourceWaveformSerial']['return']
        return self._defaults['CreateSourceWaveformSerial']['return']

    def niDigital_CreateTimeSet(self, vi, name):  # noqa: N802
        if self._defaults['CreateTimeSet']['return'] != 0:
            return self._defaults['CreateTimeSet']['return']
        return self._defaults['CreateTimeSet']['return']

    def niDigital_DeleteAllTimeSets(self, vi):  # noqa: N802
        if self._defaults['DeleteAllTimeSets']['return'] != 0:
            return self._defaults['DeleteAllTimeSets']['return']
        return self._defaults['DeleteAllTimeSets']['return']

    def niDigital_DisableSites(self, vi, site_list):  # noqa: N802
        if self._defaults['DisableSites']['return'] != 0:
            return self._defaults['DisableSites']['return']
        return self._defaults['DisableSites']['return']

    def niDigital_EnableSites(self, vi, site_list):  # noqa: N802
        if self._defaults['EnableSites']['return'] != 0:
            return self._defaults['EnableSites']['return']
        return self._defaults['EnableSites']['return']

    def niDigital_FetchHistoryRAMCycleInformation(self, vi, site, sample_index, pattern_index, time_set_index, vector_number, cycle_number, num_dut_cycles):  # noqa: N802
        if self._defaults['FetchHistoryRAMCycleInformation']['return'] != 0:
            return self._defaults['FetchHistoryRAMCycleInformation']['return']
        # pattern_index
        if self._defaults['FetchHistoryRAMCycleInformation']['patternIndex'] is None:
            raise MockFunctionCallError("niDigital_FetchHistoryRAMCycleInformation", param='patternIndex')
        if pattern_index is not None:
            pattern_index.contents.value = self._defaults['FetchHistoryRAMCycleInformation']['patternIndex']
        # time_set_index
        if self._defaults['FetchHistoryRAMCycleInformation']['timeSetIndex'] is None:
            raise MockFunctionCallError("niDigital_FetchHistoryRAMCycleInformation", param='timeSetIndex')
        if time_set_index is not None:
            time_set_index.contents.value = self._defaults['FetchHistoryRAMCycleInformation']['timeSetIndex']
        # vector_number
        if self._defaults['FetchHistoryRAMCycleInformation']['vectorNumber'] is None:
            raise MockFunctionCallError("niDigital_FetchHistoryRAMCycleInformation", param='vectorNumber')
        if vector_number is not None:
            vector_number.contents.value = self._defaults['FetchHistoryRAMCycleInformation']['vectorNumber']
        # cycle_number
        if self._defaults['FetchHistoryRAMCycleInformation']['cycleNumber'] is None:
            raise MockFunctionCallError("niDigital_FetchHistoryRAMCycleInformation", param='cycleNumber')
        if cycle_number is not None:
            cycle_number.contents.value = self._defaults['FetchHistoryRAMCycleInformation']['cycleNumber']
        # num_dut_cycles
        if self._defaults['FetchHistoryRAMCycleInformation']['numDutCycles'] is None:
            raise MockFunctionCallError("niDigital_FetchHistoryRAMCycleInformation", param='numDutCycles')
        if num_dut_cycles is not None:
            num_dut_cycles.contents.value = self._defaults['FetchHistoryRAMCycleInformation']['numDutCycles']
        return self._defaults['FetchHistoryRAMCycleInformation']['return']

    def niDigital_FetchHistoryRAMCyclePinData(self, vi, site, pin_list, sample_index, dut_cycle_index, pin_data_buffer_size, expected_pin_states, actual_pin_states, per_pin_pass_fail, actual_num_pin_data):  # noqa: N802
        if self._defaults['FetchHistoryRAMCyclePinData']['return'] != 0:
            return self._defaults['FetchHistoryRAMCyclePinData']['return']
        # actual_num_pin_data
        if self._defaults['FetchHistoryRAMCyclePinData']['actualNumPinData'] is None:
            raise MockFunctionCallError("niDigital_FetchHistoryRAMCyclePinData", param='actualNumPinData')
        if actual_num_pin_data is not None:
            actual_num_pin_data.contents.value = self._defaults['FetchHistoryRAMCyclePinData']['actualNumPinData']
        if self._defaults['FetchHistoryRAMCyclePinData']['expectedPinStates'] is None:
            raise MockFunctionCallError("niDigital_FetchHistoryRAMCyclePinData", param='expectedPinStates')
        if pin_data_buffer_size.value == 0:
            return len(self._defaults['FetchHistoryRAMCyclePinData']['expectedPinStates'])
        try:
            expected_pin_states_ref = expected_pin_states.contents
        except AttributeError:
            expected_pin_states_ref = expected_pin_states
        for i in range(len(self._defaults['FetchHistoryRAMCyclePinData']['expectedPinStates'])):
            expected_pin_states_ref[i] = self._defaults['FetchHistoryRAMCyclePinData']['expectedPinStates'][i]
        if self._defaults['FetchHistoryRAMCyclePinData']['actualPinStates'] is None:
            raise MockFunctionCallError("niDigital_FetchHistoryRAMCyclePinData", param='actualPinStates')
        if pin_data_buffer_size.value == 0:
            return len(self._defaults['FetchHistoryRAMCyclePinData']['actualPinStates'])
        try:
            actual_pin_states_ref = actual_pin_states.contents
        except AttributeError:
            actual_pin_states_ref = actual_pin_states
        for i in range(len(self._defaults['FetchHistoryRAMCyclePinData']['actualPinStates'])):
            actual_pin_states_ref[i] = self._defaults['FetchHistoryRAMCyclePinData']['actualPinStates'][i]
        if self._defaults['FetchHistoryRAMCyclePinData']['perPinPassFail'] is None:
            raise MockFunctionCallError("niDigital_FetchHistoryRAMCyclePinData", param='perPinPassFail')
        if pin_data_buffer_size.value == 0:
            return len(self._defaults['FetchHistoryRAMCyclePinData']['perPinPassFail'])
        try:
            per_pin_pass_fail_ref = per_pin_pass_fail.contents
        except AttributeError:
            per_pin_pass_fail_ref = per_pin_pass_fail
        for i in range(len(self._defaults['FetchHistoryRAMCyclePinData']['perPinPassFail'])):
            per_pin_pass_fail_ref[i] = self._defaults['FetchHistoryRAMCyclePinData']['perPinPassFail'][i]
        return self._defaults['FetchHistoryRAMCyclePinData']['return']

    def niDigital_FetchHistoryRAMScanCycleNumber(self, vi, site, sample_index, scan_cycle_number):  # noqa: N802
        if self._defaults['FetchHistoryRAMScanCycleNumber']['return'] != 0:
            return self._defaults['FetchHistoryRAMScanCycleNumber']['return']
        # scan_cycle_number
        if self._defaults['FetchHistoryRAMScanCycleNumber']['scanCycleNumber'] is None:
            raise MockFunctionCallError("niDigital_FetchHistoryRAMScanCycleNumber", param='scanCycleNumber')
        if scan_cycle_number is not None:
            scan_cycle_number.contents.value = self._defaults['FetchHistoryRAMScanCycleNumber']['scanCycleNumber']
        return self._defaults['FetchHistoryRAMScanCycleNumber']['return']

    def niDigital_FrequencyCounter_MeasureFrequency(self, vi, channel_list, frequencies_buffer_size, frequencies, actual_num_frequencies):  # noqa: N802
        if self._defaults['FrequencyCounter_MeasureFrequency']['return'] != 0:
            return self._defaults['FrequencyCounter_MeasureFrequency']['return']
        # actual_num_frequencies
        if self._defaults['FrequencyCounter_MeasureFrequency']['actualNumFrequencies'] is None:
            raise MockFunctionCallError("niDigital_FrequencyCounter_MeasureFrequency", param='actualNumFrequencies')
        if actual_num_frequencies is not None:
            actual_num_frequencies.contents.value = self._defaults['FrequencyCounter_MeasureFrequency']['actualNumFrequencies']
        if self._defaults['FrequencyCounter_MeasureFrequency']['frequencies'] is None:
            raise MockFunctionCallError("niDigital_FrequencyCounter_MeasureFrequency", param='frequencies')
        if frequencies_buffer_size.value == 0:
            return len(self._defaults['FrequencyCounter_MeasureFrequency']['frequencies'])
        try:
            frequencies_ref = frequencies.contents
        except AttributeError:
            frequencies_ref = frequencies
        for i in range(len(self._defaults['FrequencyCounter_MeasureFrequency']['frequencies'])):
            frequencies_ref[i] = self._defaults['FrequencyCounter_MeasureFrequency']['frequencies'][i]
        return self._defaults['FrequencyCounter_MeasureFrequency']['return']

    def niDigital_GetAttributeViBoolean(self, vi, channel_name, attribute, value):  # noqa: N802
        if self._defaults['GetAttributeViBoolean']['return'] != 0:
            return self._defaults['GetAttributeViBoolean']['return']
        # value
        if self._defaults['GetAttributeViBoolean']['value'] is None:
            raise MockFunctionCallError("niDigital_GetAttributeViBoolean", param='value')
        if value is not None:
            value.contents.value = self._defaults['GetAttributeViBoolean']['value']
        return self._defaults['GetAttributeViBoolean']['return']

    def niDigital_GetAttributeViInt32(self, vi, channel_name, attribute, value):  # noqa: N802
        if self._defaults['GetAttributeViInt32']['return'] != 0:
            return self._defaults['GetAttributeViInt32']['return']
        # value
        if self._defaults['GetAttributeViInt32']['value'] is None:
            raise MockFunctionCallError("niDigital_GetAttributeViInt32", param='value')
        if value is not None:
            value.contents.value = self._defaults['GetAttributeViInt32']['value']
        return self._defaults['GetAttributeViInt32']['return']

    def niDigital_GetAttributeViInt64(self, vi, channel_name, attribute, value):  # noqa: N802
        if self._defaults['GetAttributeViInt64']['return'] != 0:
            return self._defaults['GetAttributeViInt64']['return']
        # value
        if self._defaults['GetAttributeViInt64']['value'] is None:
            raise MockFunctionCallError("niDigital_GetAttributeViInt64", param='value')
        if value is not None:
            value.contents.value = self._defaults['GetAttributeViInt64']['value']
        return self._defaults['GetAttributeViInt64']['return']

    def niDigital_GetAttributeViReal64(self, vi, channel_name, attribute, value):  # noqa: N802
        if self._defaults['GetAttributeViReal64']['return'] != 0:
            return self._defaults['GetAttributeViReal64']['return']
        # value
        if self._defaults['GetAttributeViReal64']['value'] is None:
            raise MockFunctionCallError("niDigital_GetAttributeViReal64", param='value')
        if value is not None:
            value.contents.value = self._defaults['GetAttributeViReal64']['value']
        return self._defaults['GetAttributeViReal64']['return']

    def niDigital_GetAttributeViString(self, vi, channel_name, attribute, buffer_size, value):  # noqa: N802
        if self._defaults['GetAttributeViString']['return'] != 0:
            return self._defaults['GetAttributeViString']['return']
        if self._defaults['GetAttributeViString']['value'] is None:
            raise MockFunctionCallError("niDigital_GetAttributeViString", param='value')
        if buffer_size.value == 0:
            return len(self._defaults['GetAttributeViString']['value'])
        value.value = self._defaults['GetAttributeViString']['value'].encode('ascii')
        return self._defaults['GetAttributeViString']['return']

    def niDigital_GetChannelNameFromString(self, vi, indices, name_buffer_size, names):  # noqa: N802
        if self._defaults['GetChannelNameFromString']['return'] != 0:
            return self._defaults['GetChannelNameFromString']['return']
        if self._defaults['GetChannelNameFromString']['names'] is None:
            raise MockFunctionCallError("niDigital_GetChannelNameFromString", param='names')
        if name_buffer_size.value == 0:
            return len(self._defaults['GetChannelNameFromString']['names'])
        names.value = self._defaults['GetChannelNameFromString']['names'].encode('ascii')
        return self._defaults['GetChannelNameFromString']['return']

    def niDigital_GetError(self, vi, error_code, error_description_buffer_size, error_description):  # noqa: N802
        if self._defaults['GetError']['return'] != 0:
            return self._defaults['GetError']['return']
        # error_code
        if self._defaults['GetError']['errorCode'] is None:
            raise MockFunctionCallError("niDigital_GetError", param='errorCode')
        if error_code is not None:
            error_code.contents.value = self._defaults['GetError']['errorCode']
        if self._defaults['GetError']['errorDescription'] is None:
            raise MockFunctionCallError("niDigital_GetError", param='errorDescription')
        if error_description_buffer_size.value == 0:
            return len(self._defaults['GetError']['errorDescription'])
        error_description.value = self._defaults['GetError']['errorDescription'].encode('ascii')
        return self._defaults['GetError']['return']

    def niDigital_GetFailCount(self, vi, channel_list, buffer_size, failure_count, actual_num_read):  # noqa: N802
        if self._defaults['GetFailCount']['return'] != 0:
            return self._defaults['GetFailCount']['return']
        # actual_num_read
        if self._defaults['GetFailCount']['actualNumRead'] is None:
            raise MockFunctionCallError("niDigital_GetFailCount", param='actualNumRead')
        if actual_num_read is not None:
            actual_num_read.contents.value = self._defaults['GetFailCount']['actualNumRead']
        if self._defaults['GetFailCount']['failureCount'] is None:
            raise MockFunctionCallError("niDigital_GetFailCount", param='failureCount')
        if buffer_size.value == 0:
            return len(self._defaults['GetFailCount']['failureCount'])
        try:
            failure_count_ref = failure_count.contents
        except AttributeError:
            failure_count_ref = failure_count
        for i in range(len(self._defaults['GetFailCount']['failureCount'])):
            failure_count_ref[i] = self._defaults['GetFailCount']['failureCount'][i]
        return self._defaults['GetFailCount']['return']

    def niDigital_GetHistoryRAMSampleCount(self, vi, site, sample_count):  # noqa: N802
        if self._defaults['GetHistoryRAMSampleCount']['return'] != 0:
            return self._defaults['GetHistoryRAMSampleCount']['return']
        # sample_count
        if self._defaults['GetHistoryRAMSampleCount']['sampleCount'] is None:
            raise MockFunctionCallError("niDigital_GetHistoryRAMSampleCount", param='sampleCount')
        if sample_count is not None:
            sample_count.contents.value = self._defaults['GetHistoryRAMSampleCount']['sampleCount']
        return self._defaults['GetHistoryRAMSampleCount']['return']

    def niDigital_GetPatternName(self, vi, pattern_index, name_buffer_size, name):  # noqa: N802
        if self._defaults['GetPatternName']['return'] != 0:
            return self._defaults['GetPatternName']['return']
        if self._defaults['GetPatternName']['name'] is None:
            raise MockFunctionCallError("niDigital_GetPatternName", param='name')
        if name_buffer_size.value == 0:
            return len(self._defaults['GetPatternName']['name'])
        name.value = self._defaults['GetPatternName']['name'].encode('ascii')
        return self._defaults['GetPatternName']['return']

    def niDigital_GetPatternPinList(self, vi, start_label, pin_list_buffer_size, pin_list):  # noqa: N802
        if self._defaults['GetPatternPinList']['return'] != 0:
            return self._defaults['GetPatternPinList']['return']
        if self._defaults['GetPatternPinList']['pinList'] is None:
            raise MockFunctionCallError("niDigital_GetPatternPinList", param='pinList')
        if pin_list_buffer_size.value == 0:
            return len(self._defaults['GetPatternPinList']['pinList'])
        pin_list.value = self._defaults['GetPatternPinList']['pinList'].encode('ascii')
        return self._defaults['GetPatternPinList']['return']

    def niDigital_GetPinName(self, vi, pin_index, name_buffer_size, name):  # noqa: N802
        if self._defaults['GetPinName']['return'] != 0:
            return self._defaults['GetPinName']['return']
        if self._defaults['GetPinName']['name'] is None:
            raise MockFunctionCallError("niDigital_GetPinName", param='name')
        if name_buffer_size.value == 0:
            return len(self._defaults['GetPinName']['name'])
        name.value = self._defaults['GetPinName']['name'].encode('ascii')
        return self._defaults['GetPinName']['return']

    def niDigital_GetPinResultsPinInformation(self, vi, channel_list, buffer_size, pin_indexes, site_numbers, channel_indexes, actual_num_values):  # noqa: N802
        if self._defaults['GetPinResultsPinInformation']['return'] != 0:
            return self._defaults['GetPinResultsPinInformation']['return']
        # actual_num_values
        if self._defaults['GetPinResultsPinInformation']['actualNumValues'] is None:
            raise MockFunctionCallError("niDigital_GetPinResultsPinInformation", param='actualNumValues')
        if actual_num_values is not None:
            actual_num_values.contents.value = self._defaults['GetPinResultsPinInformation']['actualNumValues']
        if self._defaults['GetPinResultsPinInformation']['pinIndexes'] is None:
            raise MockFunctionCallError("niDigital_GetPinResultsPinInformation", param='pinIndexes')
        if buffer_size.value == 0:
            return len(self._defaults['GetPinResultsPinInformation']['pinIndexes'])
        try:
            pin_indexes_ref = pin_indexes.contents
        except AttributeError:
            pin_indexes_ref = pin_indexes
        for i in range(len(self._defaults['GetPinResultsPinInformation']['pinIndexes'])):
            pin_indexes_ref[i] = self._defaults['GetPinResultsPinInformation']['pinIndexes'][i]
        if self._defaults['GetPinResultsPinInformation']['siteNumbers'] is None:
            raise MockFunctionCallError("niDigital_GetPinResultsPinInformation", param='siteNumbers')
        if buffer_size.value == 0:
            return len(self._defaults['GetPinResultsPinInformation']['siteNumbers'])
        try:
            site_numbers_ref = site_numbers.contents
        except AttributeError:
            site_numbers_ref = site_numbers
        for i in range(len(self._defaults['GetPinResultsPinInformation']['siteNumbers'])):
            site_numbers_ref[i] = self._defaults['GetPinResultsPinInformation']['siteNumbers'][i]
        if self._defaults['GetPinResultsPinInformation']['channelIndexes'] is None:
            raise MockFunctionCallError("niDigital_GetPinResultsPinInformation", param='channelIndexes')
        if buffer_size.value == 0:
            return len(self._defaults['GetPinResultsPinInformation']['channelIndexes'])
        try:
            channel_indexes_ref = channel_indexes.contents
        except AttributeError:
            channel_indexes_ref = channel_indexes
        for i in range(len(self._defaults['GetPinResultsPinInformation']['channelIndexes'])):
            channel_indexes_ref[i] = self._defaults['GetPinResultsPinInformation']['channelIndexes'][i]
        return self._defaults['GetPinResultsPinInformation']['return']

    def niDigital_GetSitePassFail(self, vi, site_list, pass_fail_buffer_size, pass_fail, actual_num_sites):  # noqa: N802
        if self._defaults['GetSitePassFail']['return'] != 0:
            return self._defaults['GetSitePassFail']['return']
        # actual_num_sites
        if self._defaults['GetSitePassFail']['actualNumSites'] is None:
            raise MockFunctionCallError("niDigital_GetSitePassFail", param='actualNumSites')
        if actual_num_sites is not None:
            actual_num_sites.contents.value = self._defaults['GetSitePassFail']['actualNumSites']
        if self._defaults['GetSitePassFail']['passFail'] is None:
            raise MockFunctionCallError("niDigital_GetSitePassFail", param='passFail')
        if pass_fail_buffer_size.value == 0:
            return len(self._defaults['GetSitePassFail']['passFail'])
        try:
            pass_fail_ref = pass_fail.contents
        except AttributeError:
            pass_fail_ref = pass_fail
        for i in range(len(self._defaults['GetSitePassFail']['passFail'])):
            pass_fail_ref[i] = self._defaults['GetSitePassFail']['passFail'][i]
        return self._defaults['GetSitePassFail']['return']

    def niDigital_GetSiteResultsSiteNumbers(self, vi, site_list, site_result_type, site_numbers_buffer_size, site_numbers, actual_num_site_numbers):  # noqa: N802
        if self._defaults['GetSiteResultsSiteNumbers']['return'] != 0:
            return self._defaults['GetSiteResultsSiteNumbers']['return']
        # actual_num_site_numbers
        if self._defaults['GetSiteResultsSiteNumbers']['actualNumSiteNumbers'] is None:
            raise MockFunctionCallError("niDigital_GetSiteResultsSiteNumbers", param='actualNumSiteNumbers')
        if actual_num_site_numbers is not None:
            actual_num_site_numbers.contents.value = self._defaults['GetSiteResultsSiteNumbers']['actualNumSiteNumbers']
        if self._defaults['GetSiteResultsSiteNumbers']['siteNumbers'] is None:
            raise MockFunctionCallError("niDigital_GetSiteResultsSiteNumbers", param='siteNumbers')
        if site_numbers_buffer_size.value == 0:
            return len(self._defaults['GetSiteResultsSiteNumbers']['siteNumbers'])
        try:
            site_numbers_ref = site_numbers.contents
        except AttributeError:
            site_numbers_ref = site_numbers
        for i in range(len(self._defaults['GetSiteResultsSiteNumbers']['siteNumbers'])):
            site_numbers_ref[i] = self._defaults['GetSiteResultsSiteNumbers']['siteNumbers'][i]
        return self._defaults['GetSiteResultsSiteNumbers']['return']

    def niDigital_GetTimeSetDriveFormat(self, vi, pin, time_set_name, format):  # noqa: N802
        if self._defaults['GetTimeSetDriveFormat']['return'] != 0:
            return self._defaults['GetTimeSetDriveFormat']['return']
        # format
        if self._defaults['GetTimeSetDriveFormat']['format'] is None:
            raise MockFunctionCallError("niDigital_GetTimeSetDriveFormat", param='format')
        if format is not None:
            format.contents.value = self._defaults['GetTimeSetDriveFormat']['format']
        return self._defaults['GetTimeSetDriveFormat']['return']

    def niDigital_GetTimeSetEdge(self, vi, pin, time_set_name, edge, time):  # noqa: N802
        if self._defaults['GetTimeSetEdge']['return'] != 0:
            return self._defaults['GetTimeSetEdge']['return']
        # time
        if self._defaults['GetTimeSetEdge']['time'] is None:
            raise MockFunctionCallError("niDigital_GetTimeSetEdge", param='time')
        if time is not None:
            time.contents.value = self._defaults['GetTimeSetEdge']['time']
        return self._defaults['GetTimeSetEdge']['return']

    def niDigital_GetTimeSetEdgeMultiplier(self, vi, pin, time_set_name, edge_multiplier):  # noqa: N802
        if self._defaults['GetTimeSetEdgeMultiplier']['return'] != 0:
            return self._defaults['GetTimeSetEdgeMultiplier']['return']
        # edge_multiplier
        if self._defaults['GetTimeSetEdgeMultiplier']['edgeMultiplier'] is None:
            raise MockFunctionCallError("niDigital_GetTimeSetEdgeMultiplier", param='edgeMultiplier')
        if edge_multiplier is not None:
            edge_multiplier.contents.value = self._defaults['GetTimeSetEdgeMultiplier']['edgeMultiplier']
        return self._defaults['GetTimeSetEdgeMultiplier']['return']

    def niDigital_GetTimeSetName(self, vi, time_set_index, name_buffer_size, name):  # noqa: N802
        if self._defaults['GetTimeSetName']['return'] != 0:
            return self._defaults['GetTimeSetName']['return']
        if self._defaults['GetTimeSetName']['name'] is None:
            raise MockFunctionCallError("niDigital_GetTimeSetName", param='name')
        if name_buffer_size.value == 0:
            return len(self._defaults['GetTimeSetName']['name'])
        name.value = self._defaults['GetTimeSetName']['name'].encode('ascii')
        return self._defaults['GetTimeSetName']['return']

    def niDigital_GetTimeSetPeriod(self, vi, time_set_name, period):  # noqa: N802
        if self._defaults['GetTimeSetPeriod']['return'] != 0:
            return self._defaults['GetTimeSetPeriod']['return']
        # period
        if self._defaults['GetTimeSetPeriod']['period'] is None:
            raise MockFunctionCallError("niDigital_GetTimeSetPeriod", param='period')
        if period is not None:
            period.contents.value = self._defaults['GetTimeSetPeriod']['period']
        return self._defaults['GetTimeSetPeriod']['return']

    def niDigital_InitWithOptions(self, resource_name, id_query, reset_device, option_string, new_vi):  # noqa: N802
        if self._defaults['InitWithOptions']['return'] != 0:
            return self._defaults['InitWithOptions']['return']
        # new_vi
        if self._defaults['InitWithOptions']['newVi'] is None:
            raise MockFunctionCallError("niDigital_InitWithOptions", param='newVi')
        if new_vi is not None:
            new_vi.contents.value = self._defaults['InitWithOptions']['newVi']
        return self._defaults['InitWithOptions']['return']

    def niDigital_Initiate(self, vi):  # noqa: N802
        if self._defaults['Initiate']['return'] != 0:
            return self._defaults['Initiate']['return']
        return self._defaults['Initiate']['return']

    def niDigital_IsDone(self, vi, done):  # noqa: N802
        if self._defaults['IsDone']['return'] != 0:
            return self._defaults['IsDone']['return']
        # done
        if self._defaults['IsDone']['done'] is None:
            raise MockFunctionCallError("niDigital_IsDone", param='done')
        if done is not None:
            done.contents.value = self._defaults['IsDone']['done']
        return self._defaults['IsDone']['return']

    def niDigital_IsSiteEnabled(self, vi, site, enable):  # noqa: N802
        if self._defaults['IsSiteEnabled']['return'] != 0:
            return self._defaults['IsSiteEnabled']['return']
        # enable
        if self._defaults['IsSiteEnabled']['enable'] is None:
            raise MockFunctionCallError("niDigital_IsSiteEnabled", param='enable')
        if enable is not None:
            enable.contents.value = self._defaults['IsSiteEnabled']['enable']
        return self._defaults['IsSiteEnabled']['return']

    def niDigital_LoadLevels(self, vi, file_path):  # noqa: N802
        if self._defaults['LoadLevels']['return'] != 0:
            return self._defaults['LoadLevels']['return']
        return self._defaults['LoadLevels']['return']

    def niDigital_LoadPattern(self, vi, file_path):  # noqa: N802
        if self._defaults['LoadPattern']['return'] != 0:
            return self._defaults['LoadPattern']['return']
        return self._defaults['LoadPattern']['return']

    def niDigital_LoadPinMap(self, vi, file_path):  # noqa: N802
        if self._defaults['LoadPinMap']['return'] != 0:
            return self._defaults['LoadPinMap']['return']
        return self._defaults['LoadPinMap']['return']

    def niDigital_LoadSpecifications(self, vi, file_path):  # noqa: N802
        if self._defaults['LoadSpecifications']['return'] != 0:
            return self._defaults['LoadSpecifications']['return']
        return self._defaults['LoadSpecifications']['return']

    def niDigital_LoadTiming(self, vi, file_path):  # noqa: N802
        if self._defaults['LoadTiming']['return'] != 0:
            return self._defaults['LoadTiming']['return']
        return self._defaults['LoadTiming']['return']

    def niDigital_LockSession(self, vi, caller_has_lock):  # noqa: N802
        if self._defaults['LockSession']['return'] != 0:
            return self._defaults['LockSession']['return']
        # caller_has_lock
        if self._defaults['LockSession']['callerHasLock'] is None:
            raise MockFunctionCallError("niDigital_LockSession", param='callerHasLock')
        if caller_has_lock is not None:
            caller_has_lock.contents.value = self._defaults['LockSession']['callerHasLock']
        return self._defaults['LockSession']['return']

    def niDigital_PPMU_Measure(self, vi, channel_list, measurement_type, buffer_size, measurements, actual_num_read):  # noqa: N802
        if self._defaults['PPMU_Measure']['return'] != 0:
            return self._defaults['PPMU_Measure']['return']
        # actual_num_read
        if self._defaults['PPMU_Measure']['actualNumRead'] is None:
            raise MockFunctionCallError("niDigital_PPMU_Measure", param='actualNumRead')
        if actual_num_read is not None:
            actual_num_read.contents.value = self._defaults['PPMU_Measure']['actualNumRead']
        if self._defaults['PPMU_Measure']['measurements'] is None:
            raise MockFunctionCallError("niDigital_PPMU_Measure", param='measurements')
        if buffer_size.value == 0:
            return len(self._defaults['PPMU_Measure']['measurements'])
        try:
            measurements_ref = measurements.contents
        except AttributeError:
            measurements_ref = measurements
        for i in range(len(self._defaults['PPMU_Measure']['measurements'])):
            measurements_ref[i] = self._defaults['PPMU_Measure']['measurements'][i]
        return self._defaults['PPMU_Measure']['return']

    def niDigital_PPMU_Source(self, vi, channel_list):  # noqa: N802
        if self._defaults['PPMU_Source']['return'] != 0:
            return self._defaults['PPMU_Source']['return']
        return self._defaults['PPMU_Source']['return']

    def niDigital_ReadSequencerFlag(self, vi, flag, value):  # noqa: N802
        if self._defaults['ReadSequencerFlag']['return'] != 0:
            return self._defaults['ReadSequencerFlag']['return']
        # value
        if self._defaults['ReadSequencerFlag']['value'] is None:
            raise MockFunctionCallError("niDigital_ReadSequencerFlag", param='value')
        if value is not None:
            value.contents.value = self._defaults['ReadSequencerFlag']['value']
        return self._defaults['ReadSequencerFlag']['return']

    def niDigital_ReadSequencerRegister(self, vi, reg, value):  # noqa: N802
        if self._defaults['ReadSequencerRegister']['return'] != 0:
            return self._defaults['ReadSequencerRegister']['return']
        # value
        if self._defaults['ReadSequencerRegister']['value'] is None:
            raise MockFunctionCallError("niDigital_ReadSequencerRegister", param='value')
        if value is not None:
            value.contents.value = self._defaults['ReadSequencerRegister']['value']
        return self._defaults['ReadSequencerRegister']['return']

    def niDigital_ReadStatic(self, vi, channel_list, buffer_size, data, actual_num_read):  # noqa: N802
        if self._defaults['ReadStatic']['return'] != 0:
            return self._defaults['ReadStatic']['return']
        # actual_num_read
        if self._defaults['ReadStatic']['actualNumRead'] is None:
            raise MockFunctionCallError("niDigital_ReadStatic", param='actualNumRead')
        if actual_num_read is not None:
            actual_num_read.contents.value = self._defaults['ReadStatic']['actualNumRead']
        if self._defaults['ReadStatic']['data'] is None:
            raise MockFunctionCallError("niDigital_ReadStatic", param='data')
        if buffer_size.value == 0:
            return len(self._defaults['ReadStatic']['data'])
        try:
            data_ref = data.contents
        except AttributeError:
            data_ref = data
        for i in range(len(self._defaults['ReadStatic']['data'])):
            data_ref[i] = self._defaults['ReadStatic']['data'][i]
        return self._defaults['ReadStatic']['return']

    def niDigital_ResetDevice(self, vi):  # noqa: N802
        if self._defaults['ResetDevice']['return'] != 0:
            return self._defaults['ResetDevice']['return']
        return self._defaults['ResetDevice']['return']

    def niDigital_SelfCalibrate(self, vi):  # noqa: N802
        if self._defaults['SelfCalibrate']['return'] != 0:
            return self._defaults['SelfCalibrate']['return']
        return self._defaults['SelfCalibrate']['return']

    def niDigital_SendSoftwareEdgeTrigger(self, vi, trigger, trigger_identifier):  # noqa: N802
        if self._defaults['SendSoftwareEdgeTrigger']['return'] != 0:
            return self._defaults['SendSoftwareEdgeTrigger']['return']
        return self._defaults['SendSoftwareEdgeTrigger']['return']

    def niDigital_SetAttributeViBoolean(self, vi, channel_name, attribute, value):  # noqa: N802
        if self._defaults['SetAttributeViBoolean']['return'] != 0:
            return self._defaults['SetAttributeViBoolean']['return']
        return self._defaults['SetAttributeViBoolean']['return']

    def niDigital_SetAttributeViInt32(self, vi, channel_name, attribute, value):  # noqa: N802
        if self._defaults['SetAttributeViInt32']['return'] != 0:
            return self._defaults['SetAttributeViInt32']['return']
        return self._defaults['SetAttributeViInt32']['return']

    def niDigital_SetAttributeViInt64(self, vi, channel_name, attribute, value):  # noqa: N802
        if self._defaults['SetAttributeViInt64']['return'] != 0:
            return self._defaults['SetAttributeViInt64']['return']
        return self._defaults['SetAttributeViInt64']['return']

    def niDigital_SetAttributeViReal64(self, vi, channel_name, attribute, value):  # noqa: N802
        if self._defaults['SetAttributeViReal64']['return'] != 0:
            return self._defaults['SetAttributeViReal64']['return']
        return self._defaults['SetAttributeViReal64']['return']

    def niDigital_SetAttributeViString(self, vi, channel_name, attribute, value):  # noqa: N802
        if self._defaults['SetAttributeViString']['return'] != 0:
            return self._defaults['SetAttributeViString']['return']
        return self._defaults['SetAttributeViString']['return']

    def niDigital_TDR(self, vi, channel_list, apply_offsets, offsets_buffer_size, offsets, actual_num_offsets):  # noqa: N802
        if self._defaults['TDR']['return'] != 0:
            return self._defaults['TDR']['return']
        # actual_num_offsets
        if self._defaults['TDR']['actualNumOffsets'] is None:
            raise MockFunctionCallError("niDigital_TDR", param='actualNumOffsets')
        if actual_num_offsets is not None:
            actual_num_offsets.contents.value = self._defaults['TDR']['actualNumOffsets']
        if self._defaults['TDR']['offsets'] is None:
            raise MockFunctionCallError("niDigital_TDR", param='offsets')
        if offsets_buffer_size.value == 0:
            return len(self._defaults['TDR']['offsets'])
        try:
            offsets_ref = offsets.contents
        except AttributeError:
            offsets_ref = offsets
        for i in range(len(self._defaults['TDR']['offsets'])):
            offsets_ref[i] = self._defaults['TDR']['offsets'][i]
        return self._defaults['TDR']['return']

    def niDigital_UnloadAllPatterns(self, vi, unload_keep_alive_pattern):  # noqa: N802
        if self._defaults['UnloadAllPatterns']['return'] != 0:
            return self._defaults['UnloadAllPatterns']['return']
        return self._defaults['UnloadAllPatterns']['return']

    def niDigital_UnloadSpecifications(self, vi, file_path):  # noqa: N802
        if self._defaults['UnloadSpecifications']['return'] != 0:
            return self._defaults['UnloadSpecifications']['return']
        return self._defaults['UnloadSpecifications']['return']

    def niDigital_UnlockSession(self, vi, caller_has_lock):  # noqa: N802
        if self._defaults['UnlockSession']['return'] != 0:
            return self._defaults['UnlockSession']['return']
        # caller_has_lock
        if self._defaults['UnlockSession']['callerHasLock'] is None:
            raise MockFunctionCallError("niDigital_UnlockSession", param='callerHasLock')
        if caller_has_lock is not None:
            caller_has_lock.contents.value = self._defaults['UnlockSession']['callerHasLock']
        return self._defaults['UnlockSession']['return']

    def niDigital_WaitUntilDone(self, vi, timeout):  # noqa: N802
        if self._defaults['WaitUntilDone']['return'] != 0:
            return self._defaults['WaitUntilDone']['return']
        return self._defaults['WaitUntilDone']['return']

    def niDigital_WriteSequencerFlag(self, vi, flag, value):  # noqa: N802
        if self._defaults['WriteSequencerFlag']['return'] != 0:
            return self._defaults['WriteSequencerFlag']['return']
        return self._defaults['WriteSequencerFlag']['return']

    def niDigital_WriteSequencerRegister(self, vi, reg, value):  # noqa: N802
        if self._defaults['WriteSequencerRegister']['return'] != 0:
            return self._defaults['WriteSequencerRegister']['return']
        return self._defaults['WriteSequencerRegister']['return']

    def niDigital_WriteSourceWaveformBroadcastU32(self, vi, waveform_name, waveform_size, waveform_data):  # noqa: N802
        if self._defaults['WriteSourceWaveformBroadcastU32']['return'] != 0:
            return self._defaults['WriteSourceWaveformBroadcastU32']['return']
        return self._defaults['WriteSourceWaveformBroadcastU32']['return']

    def niDigital_WriteSourceWaveformDataFromFileTDMS(self, vi, waveform_name, waveform_file_path):  # noqa: N802
        if self._defaults['WriteSourceWaveformDataFromFileTDMS']['return'] != 0:
            return self._defaults['WriteSourceWaveformDataFromFileTDMS']['return']
        return self._defaults['WriteSourceWaveformDataFromFileTDMS']['return']

    def niDigital_WriteSourceWaveformSiteUniqueU32(self, vi, site_list, waveform_name, num_waveforms, samples_per_waveform, waveform_data):  # noqa: N802
        if self._defaults['WriteSourceWaveformSiteUniqueU32']['return'] != 0:
            return self._defaults['WriteSourceWaveformSiteUniqueU32']['return']
        return self._defaults['WriteSourceWaveformSiteUniqueU32']['return']

    def niDigital_WriteStatic(self, vi, channel_list, state):  # noqa: N802
        if self._defaults['WriteStatic']['return'] != 0:
            return self._defaults['WriteStatic']['return']
        return self._defaults['WriteStatic']['return']

    def niDigital_close(self, vi):  # noqa: N802
        if self._defaults['close']['return'] != 0:
            return self._defaults['close']['return']
        return self._defaults['close']['return']

    def niDigital_error_message(self, vi, error_code, error_message):  # noqa: N802
        if self._defaults['error_message']['return'] != 0:
            return self._defaults['error_message']['return']
        # error_message
        if self._defaults['error_message']['errorMessage'] is None:
            raise MockFunctionCallError("niDigital_error_message", param='errorMessage')
        test_value = self._defaults['error_message']['errorMessage']
        if type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(error_message) >= len(test_value)
        for i in range(len(test_value)):
            error_message[i] = test_value[i]
        return self._defaults['error_message']['return']

    def niDigital_reset(self, vi):  # noqa: N802
        if self._defaults['reset']['return'] != 0:
            return self._defaults['reset']['return']
        return self._defaults['reset']['return']

    def niDigital_self_test(self, vi, test_result, test_message):  # noqa: N802
        if self._defaults['self_test']['return'] != 0:
            return self._defaults['self_test']['return']
        # test_result
        if self._defaults['self_test']['testResult'] is None:
            raise MockFunctionCallError("niDigital_self_test", param='testResult')
        if test_result is not None:
            test_result.contents.value = self._defaults['self_test']['testResult']
        # test_message
        if self._defaults['self_test']['testMessage'] is None:
            raise MockFunctionCallError("niDigital_self_test", param='testMessage')
        test_value = self._defaults['self_test']['testMessage']
        if type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(test_message) >= len(test_value)
        for i in range(len(test_value)):
            test_message[i] = test_value[i]
        return self._defaults['self_test']['return']

    # Helper function to setup Mock object with default side effects and return values
    def set_side_effects_and_return_values(self, mock_library):
        mock_library.niDigital_Abort_cfunc.side_effect = MockFunctionCallError("niDigital_Abort_cfunc")
        mock_library.niDigital_Abort_cfunc.return_value = 0
        mock_library.niDigital_AbortKeepAlive_cfunc.side_effect = MockFunctionCallError("niDigital_AbortKeepAlive_cfunc")
        mock_library.niDigital_AbortKeepAlive_cfunc.return_value = 0
        mock_library.niDigital_ApplyLevelsAndTiming_cfunc.side_effect = MockFunctionCallError("niDigital_ApplyLevelsAndTiming_cfunc")
        mock_library.niDigital_ApplyLevelsAndTiming_cfunc.return_value = 0
        mock_library.niDigital_ApplyTDROffsets_cfunc.side_effect = MockFunctionCallError("niDigital_ApplyTDROffsets_cfunc")
        mock_library.niDigital_ApplyTDROffsets_cfunc.return_value = 0
        mock_library.niDigital_BurstPattern_cfunc.side_effect = MockFunctionCallError("niDigital_BurstPattern_cfunc")
        mock_library.niDigital_BurstPattern_cfunc.return_value = 0
        mock_library.niDigital_ClockGenerator_Abort_cfunc.side_effect = MockFunctionCallError("niDigital_ClockGenerator_Abort_cfunc")
        mock_library.niDigital_ClockGenerator_Abort_cfunc.return_value = 0
        mock_library.niDigital_ClockGenerator_GenerateClock_cfunc.side_effect = MockFunctionCallError("niDigital_ClockGenerator_GenerateClock_cfunc")
        mock_library.niDigital_ClockGenerator_GenerateClock_cfunc.return_value = 0
        mock_library.niDigital_Commit_cfunc.side_effect = MockFunctionCallError("niDigital_Commit_cfunc")
        mock_library.niDigital_Commit_cfunc.return_value = 0
        mock_library.niDigital_ConfigureActiveLoadLevels_cfunc.side_effect = MockFunctionCallError("niDigital_ConfigureActiveLoadLevels_cfunc")
        mock_library.niDigital_ConfigureActiveLoadLevels_cfunc.return_value = 0
        mock_library.niDigital_ConfigurePatternBurstSites_cfunc.side_effect = MockFunctionCallError("niDigital_ConfigurePatternBurstSites_cfunc")
        mock_library.niDigital_ConfigurePatternBurstSites_cfunc.return_value = 0
        mock_library.niDigital_ConfigureTimeSetCompareEdgesStrobe_cfunc.side_effect = MockFunctionCallError("niDigital_ConfigureTimeSetCompareEdgesStrobe_cfunc")
        mock_library.niDigital_ConfigureTimeSetCompareEdgesStrobe_cfunc.return_value = 0
        mock_library.niDigital_ConfigureTimeSetCompareEdgesStrobe2x_cfunc.side_effect = MockFunctionCallError("niDigital_ConfigureTimeSetCompareEdgesStrobe2x_cfunc")
        mock_library.niDigital_ConfigureTimeSetCompareEdgesStrobe2x_cfunc.return_value = 0
        mock_library.niDigital_ConfigureTimeSetDriveEdges_cfunc.side_effect = MockFunctionCallError("niDigital_ConfigureTimeSetDriveEdges_cfunc")
        mock_library.niDigital_ConfigureTimeSetDriveEdges_cfunc.return_value = 0
        mock_library.niDigital_ConfigureTimeSetDriveEdges2x_cfunc.side_effect = MockFunctionCallError("niDigital_ConfigureTimeSetDriveEdges2x_cfunc")
        mock_library.niDigital_ConfigureTimeSetDriveEdges2x_cfunc.return_value = 0
        mock_library.niDigital_ConfigureTimeSetDriveFormat_cfunc.side_effect = MockFunctionCallError("niDigital_ConfigureTimeSetDriveFormat_cfunc")
        mock_library.niDigital_ConfigureTimeSetDriveFormat_cfunc.return_value = 0
        mock_library.niDigital_ConfigureTimeSetEdge_cfunc.side_effect = MockFunctionCallError("niDigital_ConfigureTimeSetEdge_cfunc")
        mock_library.niDigital_ConfigureTimeSetEdge_cfunc.return_value = 0
        mock_library.niDigital_ConfigureTimeSetEdgeMultiplier_cfunc.side_effect = MockFunctionCallError("niDigital_ConfigureTimeSetEdgeMultiplier_cfunc")
        mock_library.niDigital_ConfigureTimeSetEdgeMultiplier_cfunc.return_value = 0
        mock_library.niDigital_ConfigureTimeSetPeriod_cfunc.side_effect = MockFunctionCallError("niDigital_ConfigureTimeSetPeriod_cfunc")
        mock_library.niDigital_ConfigureTimeSetPeriod_cfunc.return_value = 0
        mock_library.niDigital_ConfigureVoltageLevels_cfunc.side_effect = MockFunctionCallError("niDigital_ConfigureVoltageLevels_cfunc")
        mock_library.niDigital_ConfigureVoltageLevels_cfunc.return_value = 0
        mock_library.niDigital_CreateCaptureWaveformFromFileDigicapture_cfunc.side_effect = MockFunctionCallError("niDigital_CreateCaptureWaveformFromFileDigicapture_cfunc")
        mock_library.niDigital_CreateCaptureWaveformFromFileDigicapture_cfunc.return_value = 0
        mock_library.niDigital_CreateCaptureWaveformParallel_cfunc.side_effect = MockFunctionCallError("niDigital_CreateCaptureWaveformParallel_cfunc")
        mock_library.niDigital_CreateCaptureWaveformParallel_cfunc.return_value = 0
        mock_library.niDigital_CreateCaptureWaveformSerial_cfunc.side_effect = MockFunctionCallError("niDigital_CreateCaptureWaveformSerial_cfunc")
        mock_library.niDigital_CreateCaptureWaveformSerial_cfunc.return_value = 0
        mock_library.niDigital_CreateSourceWaveformFromFileTDMS_cfunc.side_effect = MockFunctionCallError("niDigital_CreateSourceWaveformFromFileTDMS_cfunc")
        mock_library.niDigital_CreateSourceWaveformFromFileTDMS_cfunc.return_value = 0
        mock_library.niDigital_CreateSourceWaveformParallel_cfunc.side_effect = MockFunctionCallError("niDigital_CreateSourceWaveformParallel_cfunc")
        mock_library.niDigital_CreateSourceWaveformParallel_cfunc.return_value = 0
        mock_library.niDigital_CreateSourceWaveformSerial_cfunc.side_effect = MockFunctionCallError("niDigital_CreateSourceWaveformSerial_cfunc")
        mock_library.niDigital_CreateSourceWaveformSerial_cfunc.return_value = 0
        mock_library.niDigital_CreateTimeSet_cfunc.side_effect = MockFunctionCallError("niDigital_CreateTimeSet_cfunc")
        mock_library.niDigital_CreateTimeSet_cfunc.return_value = 0
        mock_library.niDigital_DeleteAllTimeSets_cfunc.side_effect = MockFunctionCallError("niDigital_DeleteAllTimeSets_cfunc")
        mock_library.niDigital_DeleteAllTimeSets_cfunc.return_value = 0
        mock_library.niDigital_DisableSites_cfunc.side_effect = MockFunctionCallError("niDigital_DisableSites_cfunc")
        mock_library.niDigital_DisableSites_cfunc.return_value = 0
        mock_library.niDigital_EnableSites_cfunc.side_effect = MockFunctionCallError("niDigital_EnableSites_cfunc")
        mock_library.niDigital_EnableSites_cfunc.return_value = 0
        mock_library.niDigital_FetchHistoryRAMCycleInformation_cfunc.side_effect = MockFunctionCallError("niDigital_FetchHistoryRAMCycleInformation_cfunc")
        mock_library.niDigital_FetchHistoryRAMCycleInformation_cfunc.return_value = 0
        mock_library.niDigital_FetchHistoryRAMCyclePinData_cfunc.side_effect = MockFunctionCallError("niDigital_FetchHistoryRAMCyclePinData_cfunc")
        mock_library.niDigital_FetchHistoryRAMCyclePinData_cfunc.return_value = 0
        mock_library.niDigital_FetchHistoryRAMScanCycleNumber_cfunc.side_effect = MockFunctionCallError("niDigital_FetchHistoryRAMScanCycleNumber_cfunc")
        mock_library.niDigital_FetchHistoryRAMScanCycleNumber_cfunc.return_value = 0
        mock_library.niDigital_FrequencyCounter_MeasureFrequency_cfunc.side_effect = MockFunctionCallError("niDigital_FrequencyCounter_MeasureFrequency_cfunc")
        mock_library.niDigital_FrequencyCounter_MeasureFrequency_cfunc.return_value = 0
        mock_library.niDigital_GetAttributeViBoolean_cfunc.side_effect = MockFunctionCallError("niDigital_GetAttributeViBoolean_cfunc")
        mock_library.niDigital_GetAttributeViBoolean_cfunc.return_value = 0
        mock_library.niDigital_GetAttributeViInt32_cfunc.side_effect = MockFunctionCallError("niDigital_GetAttributeViInt32_cfunc")
        mock_library.niDigital_GetAttributeViInt32_cfunc.return_value = 0
        mock_library.niDigital_GetAttributeViInt64_cfunc.side_effect = MockFunctionCallError("niDigital_GetAttributeViInt64_cfunc")
        mock_library.niDigital_GetAttributeViInt64_cfunc.return_value = 0
        mock_library.niDigital_GetAttributeViReal64_cfunc.side_effect = MockFunctionCallError("niDigital_GetAttributeViReal64_cfunc")
        mock_library.niDigital_GetAttributeViReal64_cfunc.return_value = 0
        mock_library.niDigital_GetAttributeViString_cfunc.side_effect = MockFunctionCallError("niDigital_GetAttributeViString_cfunc")
        mock_library.niDigital_GetAttributeViString_cfunc.return_value = 0
        mock_library.niDigital_GetChannelNameFromString_cfunc.side_effect = MockFunctionCallError("niDigital_GetChannelNameFromString_cfunc")
        mock_library.niDigital_GetChannelNameFromString_cfunc.return_value = 0
        mock_library.niDigital_GetError_cfunc.side_effect = MockFunctionCallError("niDigital_GetError_cfunc")
        mock_library.niDigital_GetError_cfunc.return_value = 0
        mock_library.niDigital_GetFailCount_cfunc.side_effect = MockFunctionCallError("niDigital_GetFailCount_cfunc")
        mock_library.niDigital_GetFailCount_cfunc.return_value = 0
        mock_library.niDigital_GetHistoryRAMSampleCount_cfunc.side_effect = MockFunctionCallError("niDigital_GetHistoryRAMSampleCount_cfunc")
        mock_library.niDigital_GetHistoryRAMSampleCount_cfunc.return_value = 0
        mock_library.niDigital_GetPatternName_cfunc.side_effect = MockFunctionCallError("niDigital_GetPatternName_cfunc")
        mock_library.niDigital_GetPatternName_cfunc.return_value = 0
        mock_library.niDigital_GetPatternPinList_cfunc.side_effect = MockFunctionCallError("niDigital_GetPatternPinList_cfunc")
        mock_library.niDigital_GetPatternPinList_cfunc.return_value = 0
        mock_library.niDigital_GetPinName_cfunc.side_effect = MockFunctionCallError("niDigital_GetPinName_cfunc")
        mock_library.niDigital_GetPinName_cfunc.return_value = 0
        mock_library.niDigital_GetPinResultsPinInformation_cfunc.side_effect = MockFunctionCallError("niDigital_GetPinResultsPinInformation_cfunc")
        mock_library.niDigital_GetPinResultsPinInformation_cfunc.return_value = 0
        mock_library.niDigital_GetSitePassFail_cfunc.side_effect = MockFunctionCallError("niDigital_GetSitePassFail_cfunc")
        mock_library.niDigital_GetSitePassFail_cfunc.return_value = 0
        mock_library.niDigital_GetSiteResultsSiteNumbers_cfunc.side_effect = MockFunctionCallError("niDigital_GetSiteResultsSiteNumbers_cfunc")
        mock_library.niDigital_GetSiteResultsSiteNumbers_cfunc.return_value = 0
        mock_library.niDigital_GetTimeSetDriveFormat_cfunc.side_effect = MockFunctionCallError("niDigital_GetTimeSetDriveFormat_cfunc")
        mock_library.niDigital_GetTimeSetDriveFormat_cfunc.return_value = 0
        mock_library.niDigital_GetTimeSetEdge_cfunc.side_effect = MockFunctionCallError("niDigital_GetTimeSetEdge_cfunc")
        mock_library.niDigital_GetTimeSetEdge_cfunc.return_value = 0
        mock_library.niDigital_GetTimeSetEdgeMultiplier_cfunc.side_effect = MockFunctionCallError("niDigital_GetTimeSetEdgeMultiplier_cfunc")
        mock_library.niDigital_GetTimeSetEdgeMultiplier_cfunc.return_value = 0
        mock_library.niDigital_GetTimeSetName_cfunc.side_effect = MockFunctionCallError("niDigital_GetTimeSetName_cfunc")
        mock_library.niDigital_GetTimeSetName_cfunc.return_value = 0
        mock_library.niDigital_GetTimeSetPeriod_cfunc.side_effect = MockFunctionCallError("niDigital_GetTimeSetPeriod_cfunc")
        mock_library.niDigital_GetTimeSetPeriod_cfunc.return_value = 0
        mock_library.niDigital_InitWithOptions_cfunc.side_effect = MockFunctionCallError("niDigital_InitWithOptions_cfunc")
        mock_library.niDigital_InitWithOptions_cfunc.return_value = 0
        mock_library.niDigital_Initiate_cfunc.side_effect = MockFunctionCallError("niDigital_Initiate_cfunc")
        mock_library.niDigital_Initiate_cfunc.return_value = 0
        mock_library.niDigital_IsDone_cfunc.side_effect = MockFunctionCallError("niDigital_IsDone_cfunc")
        mock_library.niDigital_IsDone_cfunc.return_value = 0
        mock_library.niDigital_IsSiteEnabled_cfunc.side_effect = MockFunctionCallError("niDigital_IsSiteEnabled_cfunc")
        mock_library.niDigital_IsSiteEnabled_cfunc.return_value = 0
        mock_library.niDigital_LoadLevels_cfunc.side_effect = MockFunctionCallError("niDigital_LoadLevels_cfunc")
        mock_library.niDigital_LoadLevels_cfunc.return_value = 0
        mock_library.niDigital_LoadPattern_cfunc.side_effect = MockFunctionCallError("niDigital_LoadPattern_cfunc")
        mock_library.niDigital_LoadPattern_cfunc.return_value = 0
        mock_library.niDigital_LoadPinMap_cfunc.side_effect = MockFunctionCallError("niDigital_LoadPinMap_cfunc")
        mock_library.niDigital_LoadPinMap_cfunc.return_value = 0
        mock_library.niDigital_LoadSpecifications_cfunc.side_effect = MockFunctionCallError("niDigital_LoadSpecifications_cfunc")
        mock_library.niDigital_LoadSpecifications_cfunc.return_value = 0
        mock_library.niDigital_LoadTiming_cfunc.side_effect = MockFunctionCallError("niDigital_LoadTiming_cfunc")
        mock_library.niDigital_LoadTiming_cfunc.return_value = 0
        mock_library.niDigital_LockSession_cfunc.side_effect = MockFunctionCallError("niDigital_LockSession_cfunc")
        mock_library.niDigital_LockSession_cfunc.return_value = 0
        mock_library.niDigital_PPMU_Measure_cfunc.side_effect = MockFunctionCallError("niDigital_PPMU_Measure_cfunc")
        mock_library.niDigital_PPMU_Measure_cfunc.return_value = 0
        mock_library.niDigital_PPMU_Source_cfunc.side_effect = MockFunctionCallError("niDigital_PPMU_Source_cfunc")
        mock_library.niDigital_PPMU_Source_cfunc.return_value = 0
        mock_library.niDigital_ReadSequencerFlag_cfunc.side_effect = MockFunctionCallError("niDigital_ReadSequencerFlag_cfunc")
        mock_library.niDigital_ReadSequencerFlag_cfunc.return_value = 0
        mock_library.niDigital_ReadSequencerRegister_cfunc.side_effect = MockFunctionCallError("niDigital_ReadSequencerRegister_cfunc")
        mock_library.niDigital_ReadSequencerRegister_cfunc.return_value = 0
        mock_library.niDigital_ReadStatic_cfunc.side_effect = MockFunctionCallError("niDigital_ReadStatic_cfunc")
        mock_library.niDigital_ReadStatic_cfunc.return_value = 0
        mock_library.niDigital_ResetDevice_cfunc.side_effect = MockFunctionCallError("niDigital_ResetDevice_cfunc")
        mock_library.niDigital_ResetDevice_cfunc.return_value = 0
        mock_library.niDigital_SelfCalibrate_cfunc.side_effect = MockFunctionCallError("niDigital_SelfCalibrate_cfunc")
        mock_library.niDigital_SelfCalibrate_cfunc.return_value = 0
        mock_library.niDigital_SendSoftwareEdgeTrigger_cfunc.side_effect = MockFunctionCallError("niDigital_SendSoftwareEdgeTrigger_cfunc")
        mock_library.niDigital_SendSoftwareEdgeTrigger_cfunc.return_value = 0
        mock_library.niDigital_SetAttributeViBoolean_cfunc.side_effect = MockFunctionCallError("niDigital_SetAttributeViBoolean_cfunc")
        mock_library.niDigital_SetAttributeViBoolean_cfunc.return_value = 0
        mock_library.niDigital_SetAttributeViInt32_cfunc.side_effect = MockFunctionCallError("niDigital_SetAttributeViInt32_cfunc")
        mock_library.niDigital_SetAttributeViInt32_cfunc.return_value = 0
        mock_library.niDigital_SetAttributeViInt64_cfunc.side_effect = MockFunctionCallError("niDigital_SetAttributeViInt64_cfunc")
        mock_library.niDigital_SetAttributeViInt64_cfunc.return_value = 0
        mock_library.niDigital_SetAttributeViReal64_cfunc.side_effect = MockFunctionCallError("niDigital_SetAttributeViReal64_cfunc")
        mock_library.niDigital_SetAttributeViReal64_cfunc.return_value = 0
        mock_library.niDigital_SetAttributeViString_cfunc.side_effect = MockFunctionCallError("niDigital_SetAttributeViString_cfunc")
        mock_library.niDigital_SetAttributeViString_cfunc.return_value = 0
        mock_library.niDigital_TDR_cfunc.side_effect = MockFunctionCallError("niDigital_TDR_cfunc")
        mock_library.niDigital_TDR_cfunc.return_value = 0
        mock_library.niDigital_UnloadAllPatterns_cfunc.side_effect = MockFunctionCallError("niDigital_UnloadAllPatterns_cfunc")
        mock_library.niDigital_UnloadAllPatterns_cfunc.return_value = 0
        mock_library.niDigital_UnloadSpecifications_cfunc.side_effect = MockFunctionCallError("niDigital_UnloadSpecifications_cfunc")
        mock_library.niDigital_UnloadSpecifications_cfunc.return_value = 0
        mock_library.niDigital_UnlockSession_cfunc.side_effect = MockFunctionCallError("niDigital_UnlockSession_cfunc")
        mock_library.niDigital_UnlockSession_cfunc.return_value = 0
        mock_library.niDigital_WaitUntilDone_cfunc.side_effect = MockFunctionCallError("niDigital_WaitUntilDone_cfunc")
        mock_library.niDigital_WaitUntilDone_cfunc.return_value = 0
        mock_library.niDigital_WriteSequencerFlag_cfunc.side_effect = MockFunctionCallError("niDigital_WriteSequencerFlag_cfunc")
        mock_library.niDigital_WriteSequencerFlag_cfunc.return_value = 0
        mock_library.niDigital_WriteSequencerRegister_cfunc.side_effect = MockFunctionCallError("niDigital_WriteSequencerRegister_cfunc")
        mock_library.niDigital_WriteSequencerRegister_cfunc.return_value = 0
        mock_library.niDigital_WriteSourceWaveformBroadcastU32_cfunc.side_effect = MockFunctionCallError("niDigital_WriteSourceWaveformBroadcastU32_cfunc")
        mock_library.niDigital_WriteSourceWaveformBroadcastU32_cfunc.return_value = 0
        mock_library.niDigital_WriteSourceWaveformDataFromFileTDMS_cfunc.side_effect = MockFunctionCallError("niDigital_WriteSourceWaveformDataFromFileTDMS_cfunc")
        mock_library.niDigital_WriteSourceWaveformDataFromFileTDMS_cfunc.return_value = 0
        mock_library.niDigital_WriteSourceWaveformSiteUniqueU32_cfunc.side_effect = MockFunctionCallError("niDigital_WriteSourceWaveformSiteUniqueU32_cfunc")
        mock_library.niDigital_WriteSourceWaveformSiteUniqueU32_cfunc.return_value = 0
        mock_library.niDigital_WriteStatic_cfunc.side_effect = MockFunctionCallError("niDigital_WriteStatic_cfunc")
        mock_library.niDigital_WriteStatic_cfunc.return_value = 0
        mock_library.niDigital_close_cfunc.side_effect = MockFunctionCallError("niDigital_close_cfunc")
        mock_library.niDigital_close_cfunc.return_value = 0
        mock_library.niDigital_error_message_cfunc.side_effect = MockFunctionCallError("niDigital_error_message_cfunc")
        mock_library.niDigital_error_message_cfunc.return_value = 0
        mock_library.niDigital_reset_cfunc.side_effect = MockFunctionCallError("niDigital_reset_cfunc")
        mock_library.niDigital_reset_cfunc.return_value = 0
        mock_library.niDigital_self_test_cfunc.side_effect = MockFunctionCallError("niDigital_self_test_cfunc")
        mock_library.niDigital_self_test_cfunc.return_value = 0
