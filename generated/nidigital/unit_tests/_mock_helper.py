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
        self._defaults['ClearError'] = {}
        self._defaults['ClearError']['return'] = 0
        self._defaults['ClockGenerator_Abort'] = {}
        self._defaults['ClockGenerator_Abort']['return'] = 0
        self._defaults['ClockGenerator_GenerateClock'] = {}
        self._defaults['ClockGenerator_GenerateClock']['return'] = 0
        self._defaults['ClockGenerator_Initiate'] = {}
        self._defaults['ClockGenerator_Initiate']['return'] = 0
        self._defaults['Commit'] = {}
        self._defaults['Commit']['return'] = 0
        self._defaults['ConfigureActiveLoadLevels'] = {}
        self._defaults['ConfigureActiveLoadLevels']['return'] = 0
        self._defaults['ConfigureCycleNumberHistoryRAMTrigger'] = {}
        self._defaults['ConfigureCycleNumberHistoryRAMTrigger']['return'] = 0
        self._defaults['ConfigureDigitalEdgeConditionalJumpTrigger'] = {}
        self._defaults['ConfigureDigitalEdgeConditionalJumpTrigger']['return'] = 0
        self._defaults['ConfigureDigitalEdgeStartTrigger'] = {}
        self._defaults['ConfigureDigitalEdgeStartTrigger']['return'] = 0
        self._defaults['ConfigureFirstFailureHistoryRAMTrigger'] = {}
        self._defaults['ConfigureFirstFailureHistoryRAMTrigger']['return'] = 0
        self._defaults['ConfigureHistoryRAMCyclesToAcquire'] = {}
        self._defaults['ConfigureHistoryRAMCyclesToAcquire']['return'] = 0
        self._defaults['ConfigurePatternBurstSites'] = {}
        self._defaults['ConfigurePatternBurstSites']['return'] = 0
        self._defaults['ConfigurePatternLabelHistoryRAMTrigger'] = {}
        self._defaults['ConfigurePatternLabelHistoryRAMTrigger']['return'] = 0
        self._defaults['ConfigureSoftwareEdgeConditionalJumpTrigger'] = {}
        self._defaults['ConfigureSoftwareEdgeConditionalJumpTrigger']['return'] = 0
        self._defaults['ConfigureSoftwareEdgeStartTrigger'] = {}
        self._defaults['ConfigureSoftwareEdgeStartTrigger']['return'] = 0
        self._defaults['ConfigureStartLabel'] = {}
        self._defaults['ConfigureStartLabel']['return'] = 0
        self._defaults['ConfigureTerminationMode'] = {}
        self._defaults['ConfigureTerminationMode']['return'] = 0
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
        self._defaults['CreateChannelMap'] = {}
        self._defaults['CreateChannelMap']['return'] = 0
        self._defaults['CreatePinGroup'] = {}
        self._defaults['CreatePinGroup']['return'] = 0
        self._defaults['CreatePinMap'] = {}
        self._defaults['CreatePinMap']['return'] = 0
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
        self._defaults['DisableConditionalJumpTrigger'] = {}
        self._defaults['DisableConditionalJumpTrigger']['return'] = 0
        self._defaults['DisableSites'] = {}
        self._defaults['DisableSites']['return'] = 0
        self._defaults['DisableStartTrigger'] = {}
        self._defaults['DisableStartTrigger']['return'] = 0
        self._defaults['EnableSites'] = {}
        self._defaults['EnableSites']['return'] = 0
        self._defaults['EndChannelMap'] = {}
        self._defaults['EndChannelMap']['return'] = 0
        self._defaults['ExportSignal'] = {}
        self._defaults['ExportSignal']['return'] = 0
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
        self._defaults['FrequencyCounter_ConfigureMeasurementTime'] = {}
        self._defaults['FrequencyCounter_ConfigureMeasurementTime']['return'] = 0
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
        self._defaults['GetAttributeViSession'] = {}
        self._defaults['GetAttributeViSession']['return'] = 0
        self._defaults['GetAttributeViSession']['value'] = None
        self._defaults['GetAttributeViString'] = {}
        self._defaults['GetAttributeViString']['return'] = 0
        self._defaults['GetAttributeViString']['value'] = None
        self._defaults['GetChannelName'] = {}
        self._defaults['GetChannelName']['return'] = 0
        self._defaults['GetChannelName']['name'] = None
        self._defaults['GetChannelNameFromString'] = {}
        self._defaults['GetChannelNameFromString']['return'] = 0
        self._defaults['GetChannelNameFromString']['name'] = None
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
        self._defaults['GetPatternPinIndexes'] = {}
        self._defaults['GetPatternPinIndexes']['return'] = 0
        self._defaults['GetPatternPinIndexes']['actualNumPins'] = None
        self._defaults['GetPatternPinIndexes']['pinIndexes'] = None
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
        self._defaults['MapPinToChannel'] = {}
        self._defaults['MapPinToChannel']['return'] = 0
        self._defaults['PPMU_ConfigureApertureTime'] = {}
        self._defaults['PPMU_ConfigureApertureTime']['return'] = 0
        self._defaults['PPMU_ConfigureCurrentLevel'] = {}
        self._defaults['PPMU_ConfigureCurrentLevel']['return'] = 0
        self._defaults['PPMU_ConfigureCurrentLevelRange'] = {}
        self._defaults['PPMU_ConfigureCurrentLevelRange']['return'] = 0
        self._defaults['PPMU_ConfigureCurrentLimit'] = {}
        self._defaults['PPMU_ConfigureCurrentLimit']['return'] = 0
        self._defaults['PPMU_ConfigureCurrentLimitRange'] = {}
        self._defaults['PPMU_ConfigureCurrentLimitRange']['return'] = 0
        self._defaults['PPMU_ConfigureOutputFunction'] = {}
        self._defaults['PPMU_ConfigureOutputFunction']['return'] = 0
        self._defaults['PPMU_ConfigureVoltageLevel'] = {}
        self._defaults['PPMU_ConfigureVoltageLevel']['return'] = 0
        self._defaults['PPMU_ConfigureVoltageLimits'] = {}
        self._defaults['PPMU_ConfigureVoltageLimits']['return'] = 0
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
        self._defaults['ResetAttribute'] = {}
        self._defaults['ResetAttribute']['return'] = 0
        self._defaults['ResetDevice'] = {}
        self._defaults['ResetDevice']['return'] = 0
        self._defaults['SelectFunction'] = {}
        self._defaults['SelectFunction']['return'] = 0
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
        self._defaults['SetAttributeViSession'] = {}
        self._defaults['SetAttributeViSession']['return'] = 0
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

    def niDigital_ClearError(self, vi):  # noqa: N802
        if self._defaults['ClearError']['return'] != 0:
            return self._defaults['ClearError']['return']
        return self._defaults['ClearError']['return']

    def niDigital_ClockGenerator_Abort(self, vi, channel_list):  # noqa: N802
        if self._defaults['ClockGenerator_Abort']['return'] != 0:
            return self._defaults['ClockGenerator_Abort']['return']
        return self._defaults['ClockGenerator_Abort']['return']

    def niDigital_ClockGenerator_GenerateClock(self, vi, channel_list, frequency, select_digital_function):  # noqa: N802
        if self._defaults['ClockGenerator_GenerateClock']['return'] != 0:
            return self._defaults['ClockGenerator_GenerateClock']['return']
        return self._defaults['ClockGenerator_GenerateClock']['return']

    def niDigital_ClockGenerator_Initiate(self, vi, channel_list):  # noqa: N802
        if self._defaults['ClockGenerator_Initiate']['return'] != 0:
            return self._defaults['ClockGenerator_Initiate']['return']
        return self._defaults['ClockGenerator_Initiate']['return']

    def niDigital_Commit(self, vi):  # noqa: N802
        if self._defaults['Commit']['return'] != 0:
            return self._defaults['Commit']['return']
        return self._defaults['Commit']['return']

    def niDigital_ConfigureActiveLoadLevels(self, vi, channel_list, iol, ioh, vcom):  # noqa: N802
        if self._defaults['ConfigureActiveLoadLevels']['return'] != 0:
            return self._defaults['ConfigureActiveLoadLevels']['return']
        return self._defaults['ConfigureActiveLoadLevels']['return']

    def niDigital_ConfigureCycleNumberHistoryRAMTrigger(self, vi, cycle_number, pretrigger_samples):  # noqa: N802
        if self._defaults['ConfigureCycleNumberHistoryRAMTrigger']['return'] != 0:
            return self._defaults['ConfigureCycleNumberHistoryRAMTrigger']['return']
        return self._defaults['ConfigureCycleNumberHistoryRAMTrigger']['return']

    def niDigital_ConfigureDigitalEdgeConditionalJumpTrigger(self, vi, trigger_identifier, source, edge):  # noqa: N802
        if self._defaults['ConfigureDigitalEdgeConditionalJumpTrigger']['return'] != 0:
            return self._defaults['ConfigureDigitalEdgeConditionalJumpTrigger']['return']
        return self._defaults['ConfigureDigitalEdgeConditionalJumpTrigger']['return']

    def niDigital_ConfigureDigitalEdgeStartTrigger(self, vi, source, edge):  # noqa: N802
        if self._defaults['ConfigureDigitalEdgeStartTrigger']['return'] != 0:
            return self._defaults['ConfigureDigitalEdgeStartTrigger']['return']
        return self._defaults['ConfigureDigitalEdgeStartTrigger']['return']

    def niDigital_ConfigureFirstFailureHistoryRAMTrigger(self, vi, pretrigger_samples):  # noqa: N802
        if self._defaults['ConfigureFirstFailureHistoryRAMTrigger']['return'] != 0:
            return self._defaults['ConfigureFirstFailureHistoryRAMTrigger']['return']
        return self._defaults['ConfigureFirstFailureHistoryRAMTrigger']['return']

    def niDigital_ConfigureHistoryRAMCyclesToAcquire(self, vi, cycles_to_acquire):  # noqa: N802
        if self._defaults['ConfigureHistoryRAMCyclesToAcquire']['return'] != 0:
            return self._defaults['ConfigureHistoryRAMCyclesToAcquire']['return']
        return self._defaults['ConfigureHistoryRAMCyclesToAcquire']['return']

    def niDigital_ConfigurePatternBurstSites(self, vi, site_list):  # noqa: N802
        if self._defaults['ConfigurePatternBurstSites']['return'] != 0:
            return self._defaults['ConfigurePatternBurstSites']['return']
        return self._defaults['ConfigurePatternBurstSites']['return']

    def niDigital_ConfigurePatternLabelHistoryRAMTrigger(self, vi, label, vector_offset, cycle_offset, pretrigger_samples):  # noqa: N802
        if self._defaults['ConfigurePatternLabelHistoryRAMTrigger']['return'] != 0:
            return self._defaults['ConfigurePatternLabelHistoryRAMTrigger']['return']
        return self._defaults['ConfigurePatternLabelHistoryRAMTrigger']['return']

    def niDigital_ConfigureSoftwareEdgeConditionalJumpTrigger(self, vi, trigger_identifier):  # noqa: N802
        if self._defaults['ConfigureSoftwareEdgeConditionalJumpTrigger']['return'] != 0:
            return self._defaults['ConfigureSoftwareEdgeConditionalJumpTrigger']['return']
        return self._defaults['ConfigureSoftwareEdgeConditionalJumpTrigger']['return']

    def niDigital_ConfigureSoftwareEdgeStartTrigger(self, vi):  # noqa: N802
        if self._defaults['ConfigureSoftwareEdgeStartTrigger']['return'] != 0:
            return self._defaults['ConfigureSoftwareEdgeStartTrigger']['return']
        return self._defaults['ConfigureSoftwareEdgeStartTrigger']['return']

    def niDigital_ConfigureStartLabel(self, vi, label):  # noqa: N802
        if self._defaults['ConfigureStartLabel']['return'] != 0:
            return self._defaults['ConfigureStartLabel']['return']
        return self._defaults['ConfigureStartLabel']['return']

    def niDigital_ConfigureTerminationMode(self, vi, channel_list, mode):  # noqa: N802
        if self._defaults['ConfigureTerminationMode']['return'] != 0:
            return self._defaults['ConfigureTerminationMode']['return']
        return self._defaults['ConfigureTerminationMode']['return']

    def niDigital_ConfigureTimeSetCompareEdgesStrobe(self, vi, pin_list, time_set, strobe_edge):  # noqa: N802
        if self._defaults['ConfigureTimeSetCompareEdgesStrobe']['return'] != 0:
            return self._defaults['ConfigureTimeSetCompareEdgesStrobe']['return']
        return self._defaults['ConfigureTimeSetCompareEdgesStrobe']['return']

    def niDigital_ConfigureTimeSetCompareEdgesStrobe2x(self, vi, pin_list, time_set, strobe_edge, strobe2_edge):  # noqa: N802
        if self._defaults['ConfigureTimeSetCompareEdgesStrobe2x']['return'] != 0:
            return self._defaults['ConfigureTimeSetCompareEdgesStrobe2x']['return']
        return self._defaults['ConfigureTimeSetCompareEdgesStrobe2x']['return']

    def niDigital_ConfigureTimeSetDriveEdges(self, vi, pin_list, time_set, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge):  # noqa: N802
        if self._defaults['ConfigureTimeSetDriveEdges']['return'] != 0:
            return self._defaults['ConfigureTimeSetDriveEdges']['return']
        return self._defaults['ConfigureTimeSetDriveEdges']['return']

    def niDigital_ConfigureTimeSetDriveEdges2x(self, vi, pin_list, time_set, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge, drive_data2_edge, drive_return2_edge):  # noqa: N802
        if self._defaults['ConfigureTimeSetDriveEdges2x']['return'] != 0:
            return self._defaults['ConfigureTimeSetDriveEdges2x']['return']
        return self._defaults['ConfigureTimeSetDriveEdges2x']['return']

    def niDigital_ConfigureTimeSetDriveFormat(self, vi, pin_list, time_set, drive_format):  # noqa: N802
        if self._defaults['ConfigureTimeSetDriveFormat']['return'] != 0:
            return self._defaults['ConfigureTimeSetDriveFormat']['return']
        return self._defaults['ConfigureTimeSetDriveFormat']['return']

    def niDigital_ConfigureTimeSetEdge(self, vi, pin_list, time_set, edge, time):  # noqa: N802
        if self._defaults['ConfigureTimeSetEdge']['return'] != 0:
            return self._defaults['ConfigureTimeSetEdge']['return']
        return self._defaults['ConfigureTimeSetEdge']['return']

    def niDigital_ConfigureTimeSetEdgeMultiplier(self, vi, pin_list, time_set, edge_multiplier):  # noqa: N802
        if self._defaults['ConfigureTimeSetEdgeMultiplier']['return'] != 0:
            return self._defaults['ConfigureTimeSetEdgeMultiplier']['return']
        return self._defaults['ConfigureTimeSetEdgeMultiplier']['return']

    def niDigital_ConfigureTimeSetPeriod(self, vi, time_set, period):  # noqa: N802
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

    def niDigital_CreateChannelMap(self, vi, num_sites):  # noqa: N802
        if self._defaults['CreateChannelMap']['return'] != 0:
            return self._defaults['CreateChannelMap']['return']
        return self._defaults['CreateChannelMap']['return']

    def niDigital_CreatePinGroup(self, vi, pin_group_name, pin_list):  # noqa: N802
        if self._defaults['CreatePinGroup']['return'] != 0:
            return self._defaults['CreatePinGroup']['return']
        return self._defaults['CreatePinGroup']['return']

    def niDigital_CreatePinMap(self, vi, dut_pin_list, system_pin_list):  # noqa: N802
        if self._defaults['CreatePinMap']['return'] != 0:
            return self._defaults['CreatePinMap']['return']
        return self._defaults['CreatePinMap']['return']

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

    def niDigital_DisableConditionalJumpTrigger(self, vi, trigger_identifier):  # noqa: N802
        if self._defaults['DisableConditionalJumpTrigger']['return'] != 0:
            return self._defaults['DisableConditionalJumpTrigger']['return']
        return self._defaults['DisableConditionalJumpTrigger']['return']

    def niDigital_DisableSites(self, vi, site_list):  # noqa: N802
        if self._defaults['DisableSites']['return'] != 0:
            return self._defaults['DisableSites']['return']
        return self._defaults['DisableSites']['return']

    def niDigital_DisableStartTrigger(self, vi):  # noqa: N802
        if self._defaults['DisableStartTrigger']['return'] != 0:
            return self._defaults['DisableStartTrigger']['return']
        return self._defaults['DisableStartTrigger']['return']

    def niDigital_EnableSites(self, vi, site_list):  # noqa: N802
        if self._defaults['EnableSites']['return'] != 0:
            return self._defaults['EnableSites']['return']
        return self._defaults['EnableSites']['return']

    def niDigital_EndChannelMap(self, vi):  # noqa: N802
        if self._defaults['EndChannelMap']['return'] != 0:
            return self._defaults['EndChannelMap']['return']
        return self._defaults['EndChannelMap']['return']

    def niDigital_ExportSignal(self, vi, signal, signal_identifier, output_terminal):  # noqa: N802
        if self._defaults['ExportSignal']['return'] != 0:
            return self._defaults['ExportSignal']['return']
        return self._defaults['ExportSignal']['return']

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

    def niDigital_FrequencyCounter_ConfigureMeasurementTime(self, vi, channel_list, measurement_time):  # noqa: N802
        if self._defaults['FrequencyCounter_ConfigureMeasurementTime']['return'] != 0:
            return self._defaults['FrequencyCounter_ConfigureMeasurementTime']['return']
        return self._defaults['FrequencyCounter_ConfigureMeasurementTime']['return']

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

    def niDigital_GetAttributeViSession(self, vi, channel_name, attribute, value):  # noqa: N802
        if self._defaults['GetAttributeViSession']['return'] != 0:
            return self._defaults['GetAttributeViSession']['return']
        # value
        if self._defaults['GetAttributeViSession']['value'] is None:
            raise MockFunctionCallError("niDigital_GetAttributeViSession", param='value')
        if value is not None:
            value.contents.value = self._defaults['GetAttributeViSession']['value']
        return self._defaults['GetAttributeViSession']['return']

    def niDigital_GetAttributeViString(self, vi, channel_name, attribute, buffer_size, value):  # noqa: N802
        if self._defaults['GetAttributeViString']['return'] != 0:
            return self._defaults['GetAttributeViString']['return']
        if self._defaults['GetAttributeViString']['value'] is None:
            raise MockFunctionCallError("niDigital_GetAttributeViString", param='value')
        if buffer_size.value == 0:
            return len(self._defaults['GetAttributeViString']['value'])
        value.value = self._defaults['GetAttributeViString']['value'].encode('ascii')
        return self._defaults['GetAttributeViString']['return']

    def niDigital_GetChannelName(self, vi, index, name_buffer_size, name):  # noqa: N802
        if self._defaults['GetChannelName']['return'] != 0:
            return self._defaults['GetChannelName']['return']
        if self._defaults['GetChannelName']['name'] is None:
            raise MockFunctionCallError("niDigital_GetChannelName", param='name')
        if name_buffer_size.value == 0:
            return len(self._defaults['GetChannelName']['name'])
        name.value = self._defaults['GetChannelName']['name'].encode('ascii')
        return self._defaults['GetChannelName']['return']

    def niDigital_GetChannelNameFromString(self, vi, index, name_buffer_size, name):  # noqa: N802
        if self._defaults['GetChannelNameFromString']['return'] != 0:
            return self._defaults['GetChannelNameFromString']['return']
        if self._defaults['GetChannelNameFromString']['name'] is None:
            raise MockFunctionCallError("niDigital_GetChannelNameFromString", param='name')
        if name_buffer_size.value == 0:
            return len(self._defaults['GetChannelNameFromString']['name'])
        name.value = self._defaults['GetChannelNameFromString']['name'].encode('ascii')
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

    def niDigital_GetPatternPinIndexes(self, vi, start_label, pin_indexes_buffer_size, pin_indexes, actual_num_pins):  # noqa: N802
        if self._defaults['GetPatternPinIndexes']['return'] != 0:
            return self._defaults['GetPatternPinIndexes']['return']
        # actual_num_pins
        if self._defaults['GetPatternPinIndexes']['actualNumPins'] is None:
            raise MockFunctionCallError("niDigital_GetPatternPinIndexes", param='actualNumPins')
        if actual_num_pins is not None:
            actual_num_pins.contents.value = self._defaults['GetPatternPinIndexes']['actualNumPins']
        if self._defaults['GetPatternPinIndexes']['pinIndexes'] is None:
            raise MockFunctionCallError("niDigital_GetPatternPinIndexes", param='pinIndexes')
        if pin_indexes_buffer_size.value == 0:
            return len(self._defaults['GetPatternPinIndexes']['pinIndexes'])
        try:
            pin_indexes_ref = pin_indexes.contents
        except AttributeError:
            pin_indexes_ref = pin_indexes
        for i in range(len(self._defaults['GetPatternPinIndexes']['pinIndexes'])):
            pin_indexes_ref[i] = self._defaults['GetPatternPinIndexes']['pinIndexes'][i]
        return self._defaults['GetPatternPinIndexes']['return']

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

    def niDigital_GetTimeSetDriveFormat(self, vi, pin, time_set, format):  # noqa: N802
        if self._defaults['GetTimeSetDriveFormat']['return'] != 0:
            return self._defaults['GetTimeSetDriveFormat']['return']
        # format
        if self._defaults['GetTimeSetDriveFormat']['format'] is None:
            raise MockFunctionCallError("niDigital_GetTimeSetDriveFormat", param='format')
        if format is not None:
            format.contents.value = self._defaults['GetTimeSetDriveFormat']['format']
        return self._defaults['GetTimeSetDriveFormat']['return']

    def niDigital_GetTimeSetEdge(self, vi, pin, time_set, edge, time):  # noqa: N802
        if self._defaults['GetTimeSetEdge']['return'] != 0:
            return self._defaults['GetTimeSetEdge']['return']
        # time
        if self._defaults['GetTimeSetEdge']['time'] is None:
            raise MockFunctionCallError("niDigital_GetTimeSetEdge", param='time')
        if time is not None:
            time.contents.value = self._defaults['GetTimeSetEdge']['time']
        return self._defaults['GetTimeSetEdge']['return']

    def niDigital_GetTimeSetEdgeMultiplier(self, vi, pin, time_set, edge_multiplier):  # noqa: N802
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

    def niDigital_GetTimeSetPeriod(self, vi, time_set, period):  # noqa: N802
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

    def niDigital_LoadLevels(self, vi, levels_file_path):  # noqa: N802
        if self._defaults['LoadLevels']['return'] != 0:
            return self._defaults['LoadLevels']['return']
        return self._defaults['LoadLevels']['return']

    def niDigital_LoadPattern(self, vi, file_path):  # noqa: N802
        if self._defaults['LoadPattern']['return'] != 0:
            return self._defaults['LoadPattern']['return']
        return self._defaults['LoadPattern']['return']

    def niDigital_LoadPinMap(self, vi, pin_map_file_path):  # noqa: N802
        if self._defaults['LoadPinMap']['return'] != 0:
            return self._defaults['LoadPinMap']['return']
        return self._defaults['LoadPinMap']['return']

    def niDigital_LoadSpecifications(self, vi, specifications_file_path):  # noqa: N802
        if self._defaults['LoadSpecifications']['return'] != 0:
            return self._defaults['LoadSpecifications']['return']
        return self._defaults['LoadSpecifications']['return']

    def niDigital_LoadTiming(self, vi, timing_file_path):  # noqa: N802
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

    def niDigital_MapPinToChannel(self, vi, pin, site, channel):  # noqa: N802
        if self._defaults['MapPinToChannel']['return'] != 0:
            return self._defaults['MapPinToChannel']['return']
        return self._defaults['MapPinToChannel']['return']

    def niDigital_PPMU_ConfigureApertureTime(self, vi, channel_name, aperture_time, units):  # noqa: N802
        if self._defaults['PPMU_ConfigureApertureTime']['return'] != 0:
            return self._defaults['PPMU_ConfigureApertureTime']['return']
        return self._defaults['PPMU_ConfigureApertureTime']['return']

    def niDigital_PPMU_ConfigureCurrentLevel(self, vi, channel_list, current_level):  # noqa: N802
        if self._defaults['PPMU_ConfigureCurrentLevel']['return'] != 0:
            return self._defaults['PPMU_ConfigureCurrentLevel']['return']
        return self._defaults['PPMU_ConfigureCurrentLevel']['return']

    def niDigital_PPMU_ConfigureCurrentLevelRange(self, vi, channel_list, range):  # noqa: N802
        if self._defaults['PPMU_ConfigureCurrentLevelRange']['return'] != 0:
            return self._defaults['PPMU_ConfigureCurrentLevelRange']['return']
        return self._defaults['PPMU_ConfigureCurrentLevelRange']['return']

    def niDigital_PPMU_ConfigureCurrentLimit(self, vi, channel_list, behavior, limit):  # noqa: N802
        if self._defaults['PPMU_ConfigureCurrentLimit']['return'] != 0:
            return self._defaults['PPMU_ConfigureCurrentLimit']['return']
        return self._defaults['PPMU_ConfigureCurrentLimit']['return']

    def niDigital_PPMU_ConfigureCurrentLimitRange(self, vi, channel_list, range):  # noqa: N802
        if self._defaults['PPMU_ConfigureCurrentLimitRange']['return'] != 0:
            return self._defaults['PPMU_ConfigureCurrentLimitRange']['return']
        return self._defaults['PPMU_ConfigureCurrentLimitRange']['return']

    def niDigital_PPMU_ConfigureOutputFunction(self, vi, channel_list, output_function):  # noqa: N802
        if self._defaults['PPMU_ConfigureOutputFunction']['return'] != 0:
            return self._defaults['PPMU_ConfigureOutputFunction']['return']
        return self._defaults['PPMU_ConfigureOutputFunction']['return']

    def niDigital_PPMU_ConfigureVoltageLevel(self, vi, channel_list, voltage_level):  # noqa: N802
        if self._defaults['PPMU_ConfigureVoltageLevel']['return'] != 0:
            return self._defaults['PPMU_ConfigureVoltageLevel']['return']
        return self._defaults['PPMU_ConfigureVoltageLevel']['return']

    def niDigital_PPMU_ConfigureVoltageLimits(self, vi, channel_list, lower_voltage_limit, upper_voltage_limit):  # noqa: N802
        if self._defaults['PPMU_ConfigureVoltageLimits']['return'] != 0:
            return self._defaults['PPMU_ConfigureVoltageLimits']['return']
        return self._defaults['PPMU_ConfigureVoltageLimits']['return']

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

    def niDigital_ResetAttribute(self, vi, channel_name, attribute_id):  # noqa: N802
        if self._defaults['ResetAttribute']['return'] != 0:
            return self._defaults['ResetAttribute']['return']
        return self._defaults['ResetAttribute']['return']

    def niDigital_ResetDevice(self, vi):  # noqa: N802
        if self._defaults['ResetDevice']['return'] != 0:
            return self._defaults['ResetDevice']['return']
        return self._defaults['ResetDevice']['return']

    def niDigital_SelectFunction(self, vi, channel_list, function):  # noqa: N802
        if self._defaults['SelectFunction']['return'] != 0:
            return self._defaults['SelectFunction']['return']
        return self._defaults['SelectFunction']['return']

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

    def niDigital_SetAttributeViSession(self, vi, channel_name, attribute, value):  # noqa: N802
        if self._defaults['SetAttributeViSession']['return'] != 0:
            return self._defaults['SetAttributeViSession']['return']
        return self._defaults['SetAttributeViSession']['return']

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

    def niDigital_UnloadSpecifications(self, vi, specifications_file_path):  # noqa: N802
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
        if sys.version_info.major > 2 and type(test_value) is str:
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
        if sys.version_info.major > 2 and type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(test_message) >= len(test_value)
        for i in range(len(test_value)):
            test_message[i] = test_value[i]
        return self._defaults['self_test']['return']

    # Helper function to setup Mock object with default side effects and return values
    def set_side_effects_and_return_values(self, mock_library):
        mock_library.niDigital_Abort.side_effect = MockFunctionCallError("niDigital_Abort")
        mock_library.niDigital_Abort.return_value = 0
        mock_library.niDigital_AbortKeepAlive.side_effect = MockFunctionCallError("niDigital_AbortKeepAlive")
        mock_library.niDigital_AbortKeepAlive.return_value = 0
        mock_library.niDigital_ApplyLevelsAndTiming.side_effect = MockFunctionCallError("niDigital_ApplyLevelsAndTiming")
        mock_library.niDigital_ApplyLevelsAndTiming.return_value = 0
        mock_library.niDigital_ApplyTDROffsets.side_effect = MockFunctionCallError("niDigital_ApplyTDROffsets")
        mock_library.niDigital_ApplyTDROffsets.return_value = 0
        mock_library.niDigital_BurstPattern.side_effect = MockFunctionCallError("niDigital_BurstPattern")
        mock_library.niDigital_BurstPattern.return_value = 0
        mock_library.niDigital_ClearError.side_effect = MockFunctionCallError("niDigital_ClearError")
        mock_library.niDigital_ClearError.return_value = 0
        mock_library.niDigital_ClockGenerator_Abort.side_effect = MockFunctionCallError("niDigital_ClockGenerator_Abort")
        mock_library.niDigital_ClockGenerator_Abort.return_value = 0
        mock_library.niDigital_ClockGenerator_GenerateClock.side_effect = MockFunctionCallError("niDigital_ClockGenerator_GenerateClock")
        mock_library.niDigital_ClockGenerator_GenerateClock.return_value = 0
        mock_library.niDigital_ClockGenerator_Initiate.side_effect = MockFunctionCallError("niDigital_ClockGenerator_Initiate")
        mock_library.niDigital_ClockGenerator_Initiate.return_value = 0
        mock_library.niDigital_Commit.side_effect = MockFunctionCallError("niDigital_Commit")
        mock_library.niDigital_Commit.return_value = 0
        mock_library.niDigital_ConfigureActiveLoadLevels.side_effect = MockFunctionCallError("niDigital_ConfigureActiveLoadLevels")
        mock_library.niDigital_ConfigureActiveLoadLevels.return_value = 0
        mock_library.niDigital_ConfigureCycleNumberHistoryRAMTrigger.side_effect = MockFunctionCallError("niDigital_ConfigureCycleNumberHistoryRAMTrigger")
        mock_library.niDigital_ConfigureCycleNumberHistoryRAMTrigger.return_value = 0
        mock_library.niDigital_ConfigureDigitalEdgeConditionalJumpTrigger.side_effect = MockFunctionCallError("niDigital_ConfigureDigitalEdgeConditionalJumpTrigger")
        mock_library.niDigital_ConfigureDigitalEdgeConditionalJumpTrigger.return_value = 0
        mock_library.niDigital_ConfigureDigitalEdgeStartTrigger.side_effect = MockFunctionCallError("niDigital_ConfigureDigitalEdgeStartTrigger")
        mock_library.niDigital_ConfigureDigitalEdgeStartTrigger.return_value = 0
        mock_library.niDigital_ConfigureFirstFailureHistoryRAMTrigger.side_effect = MockFunctionCallError("niDigital_ConfigureFirstFailureHistoryRAMTrigger")
        mock_library.niDigital_ConfigureFirstFailureHistoryRAMTrigger.return_value = 0
        mock_library.niDigital_ConfigureHistoryRAMCyclesToAcquire.side_effect = MockFunctionCallError("niDigital_ConfigureHistoryRAMCyclesToAcquire")
        mock_library.niDigital_ConfigureHistoryRAMCyclesToAcquire.return_value = 0
        mock_library.niDigital_ConfigurePatternBurstSites.side_effect = MockFunctionCallError("niDigital_ConfigurePatternBurstSites")
        mock_library.niDigital_ConfigurePatternBurstSites.return_value = 0
        mock_library.niDigital_ConfigurePatternLabelHistoryRAMTrigger.side_effect = MockFunctionCallError("niDigital_ConfigurePatternLabelHistoryRAMTrigger")
        mock_library.niDigital_ConfigurePatternLabelHistoryRAMTrigger.return_value = 0
        mock_library.niDigital_ConfigureSoftwareEdgeConditionalJumpTrigger.side_effect = MockFunctionCallError("niDigital_ConfigureSoftwareEdgeConditionalJumpTrigger")
        mock_library.niDigital_ConfigureSoftwareEdgeConditionalJumpTrigger.return_value = 0
        mock_library.niDigital_ConfigureSoftwareEdgeStartTrigger.side_effect = MockFunctionCallError("niDigital_ConfigureSoftwareEdgeStartTrigger")
        mock_library.niDigital_ConfigureSoftwareEdgeStartTrigger.return_value = 0
        mock_library.niDigital_ConfigureStartLabel.side_effect = MockFunctionCallError("niDigital_ConfigureStartLabel")
        mock_library.niDigital_ConfigureStartLabel.return_value = 0
        mock_library.niDigital_ConfigureTerminationMode.side_effect = MockFunctionCallError("niDigital_ConfigureTerminationMode")
        mock_library.niDigital_ConfigureTerminationMode.return_value = 0
        mock_library.niDigital_ConfigureTimeSetCompareEdgesStrobe.side_effect = MockFunctionCallError("niDigital_ConfigureTimeSetCompareEdgesStrobe")
        mock_library.niDigital_ConfigureTimeSetCompareEdgesStrobe.return_value = 0
        mock_library.niDigital_ConfigureTimeSetCompareEdgesStrobe2x.side_effect = MockFunctionCallError("niDigital_ConfigureTimeSetCompareEdgesStrobe2x")
        mock_library.niDigital_ConfigureTimeSetCompareEdgesStrobe2x.return_value = 0
        mock_library.niDigital_ConfigureTimeSetDriveEdges.side_effect = MockFunctionCallError("niDigital_ConfigureTimeSetDriveEdges")
        mock_library.niDigital_ConfigureTimeSetDriveEdges.return_value = 0
        mock_library.niDigital_ConfigureTimeSetDriveEdges2x.side_effect = MockFunctionCallError("niDigital_ConfigureTimeSetDriveEdges2x")
        mock_library.niDigital_ConfigureTimeSetDriveEdges2x.return_value = 0
        mock_library.niDigital_ConfigureTimeSetDriveFormat.side_effect = MockFunctionCallError("niDigital_ConfigureTimeSetDriveFormat")
        mock_library.niDigital_ConfigureTimeSetDriveFormat.return_value = 0
        mock_library.niDigital_ConfigureTimeSetEdge.side_effect = MockFunctionCallError("niDigital_ConfigureTimeSetEdge")
        mock_library.niDigital_ConfigureTimeSetEdge.return_value = 0
        mock_library.niDigital_ConfigureTimeSetEdgeMultiplier.side_effect = MockFunctionCallError("niDigital_ConfigureTimeSetEdgeMultiplier")
        mock_library.niDigital_ConfigureTimeSetEdgeMultiplier.return_value = 0
        mock_library.niDigital_ConfigureTimeSetPeriod.side_effect = MockFunctionCallError("niDigital_ConfigureTimeSetPeriod")
        mock_library.niDigital_ConfigureTimeSetPeriod.return_value = 0
        mock_library.niDigital_ConfigureVoltageLevels.side_effect = MockFunctionCallError("niDigital_ConfigureVoltageLevels")
        mock_library.niDigital_ConfigureVoltageLevels.return_value = 0
        mock_library.niDigital_CreateCaptureWaveformFromFileDigicapture.side_effect = MockFunctionCallError("niDigital_CreateCaptureWaveformFromFileDigicapture")
        mock_library.niDigital_CreateCaptureWaveformFromFileDigicapture.return_value = 0
        mock_library.niDigital_CreateCaptureWaveformParallel.side_effect = MockFunctionCallError("niDigital_CreateCaptureWaveformParallel")
        mock_library.niDigital_CreateCaptureWaveformParallel.return_value = 0
        mock_library.niDigital_CreateCaptureWaveformSerial.side_effect = MockFunctionCallError("niDigital_CreateCaptureWaveformSerial")
        mock_library.niDigital_CreateCaptureWaveformSerial.return_value = 0
        mock_library.niDigital_CreateChannelMap.side_effect = MockFunctionCallError("niDigital_CreateChannelMap")
        mock_library.niDigital_CreateChannelMap.return_value = 0
        mock_library.niDigital_CreatePinGroup.side_effect = MockFunctionCallError("niDigital_CreatePinGroup")
        mock_library.niDigital_CreatePinGroup.return_value = 0
        mock_library.niDigital_CreatePinMap.side_effect = MockFunctionCallError("niDigital_CreatePinMap")
        mock_library.niDigital_CreatePinMap.return_value = 0
        mock_library.niDigital_CreateSourceWaveformFromFileTDMS.side_effect = MockFunctionCallError("niDigital_CreateSourceWaveformFromFileTDMS")
        mock_library.niDigital_CreateSourceWaveformFromFileTDMS.return_value = 0
        mock_library.niDigital_CreateSourceWaveformParallel.side_effect = MockFunctionCallError("niDigital_CreateSourceWaveformParallel")
        mock_library.niDigital_CreateSourceWaveformParallel.return_value = 0
        mock_library.niDigital_CreateSourceWaveformSerial.side_effect = MockFunctionCallError("niDigital_CreateSourceWaveformSerial")
        mock_library.niDigital_CreateSourceWaveformSerial.return_value = 0
        mock_library.niDigital_CreateTimeSet.side_effect = MockFunctionCallError("niDigital_CreateTimeSet")
        mock_library.niDigital_CreateTimeSet.return_value = 0
        mock_library.niDigital_DeleteAllTimeSets.side_effect = MockFunctionCallError("niDigital_DeleteAllTimeSets")
        mock_library.niDigital_DeleteAllTimeSets.return_value = 0
        mock_library.niDigital_DisableConditionalJumpTrigger.side_effect = MockFunctionCallError("niDigital_DisableConditionalJumpTrigger")
        mock_library.niDigital_DisableConditionalJumpTrigger.return_value = 0
        mock_library.niDigital_DisableSites.side_effect = MockFunctionCallError("niDigital_DisableSites")
        mock_library.niDigital_DisableSites.return_value = 0
        mock_library.niDigital_DisableStartTrigger.side_effect = MockFunctionCallError("niDigital_DisableStartTrigger")
        mock_library.niDigital_DisableStartTrigger.return_value = 0
        mock_library.niDigital_EnableSites.side_effect = MockFunctionCallError("niDigital_EnableSites")
        mock_library.niDigital_EnableSites.return_value = 0
        mock_library.niDigital_EndChannelMap.side_effect = MockFunctionCallError("niDigital_EndChannelMap")
        mock_library.niDigital_EndChannelMap.return_value = 0
        mock_library.niDigital_ExportSignal.side_effect = MockFunctionCallError("niDigital_ExportSignal")
        mock_library.niDigital_ExportSignal.return_value = 0
        mock_library.niDigital_FetchHistoryRAMCycleInformation.side_effect = MockFunctionCallError("niDigital_FetchHistoryRAMCycleInformation")
        mock_library.niDigital_FetchHistoryRAMCycleInformation.return_value = 0
        mock_library.niDigital_FetchHistoryRAMCyclePinData.side_effect = MockFunctionCallError("niDigital_FetchHistoryRAMCyclePinData")
        mock_library.niDigital_FetchHistoryRAMCyclePinData.return_value = 0
        mock_library.niDigital_FetchHistoryRAMScanCycleNumber.side_effect = MockFunctionCallError("niDigital_FetchHistoryRAMScanCycleNumber")
        mock_library.niDigital_FetchHistoryRAMScanCycleNumber.return_value = 0
        mock_library.niDigital_FrequencyCounter_ConfigureMeasurementTime.side_effect = MockFunctionCallError("niDigital_FrequencyCounter_ConfigureMeasurementTime")
        mock_library.niDigital_FrequencyCounter_ConfigureMeasurementTime.return_value = 0
        mock_library.niDigital_FrequencyCounter_MeasureFrequency.side_effect = MockFunctionCallError("niDigital_FrequencyCounter_MeasureFrequency")
        mock_library.niDigital_FrequencyCounter_MeasureFrequency.return_value = 0
        mock_library.niDigital_GetAttributeViBoolean.side_effect = MockFunctionCallError("niDigital_GetAttributeViBoolean")
        mock_library.niDigital_GetAttributeViBoolean.return_value = 0
        mock_library.niDigital_GetAttributeViInt32.side_effect = MockFunctionCallError("niDigital_GetAttributeViInt32")
        mock_library.niDigital_GetAttributeViInt32.return_value = 0
        mock_library.niDigital_GetAttributeViInt64.side_effect = MockFunctionCallError("niDigital_GetAttributeViInt64")
        mock_library.niDigital_GetAttributeViInt64.return_value = 0
        mock_library.niDigital_GetAttributeViReal64.side_effect = MockFunctionCallError("niDigital_GetAttributeViReal64")
        mock_library.niDigital_GetAttributeViReal64.return_value = 0
        mock_library.niDigital_GetAttributeViSession.side_effect = MockFunctionCallError("niDigital_GetAttributeViSession")
        mock_library.niDigital_GetAttributeViSession.return_value = 0
        mock_library.niDigital_GetAttributeViString.side_effect = MockFunctionCallError("niDigital_GetAttributeViString")
        mock_library.niDigital_GetAttributeViString.return_value = 0
        mock_library.niDigital_GetChannelName.side_effect = MockFunctionCallError("niDigital_GetChannelName")
        mock_library.niDigital_GetChannelName.return_value = 0
        mock_library.niDigital_GetChannelNameFromString.side_effect = MockFunctionCallError("niDigital_GetChannelNameFromString")
        mock_library.niDigital_GetChannelNameFromString.return_value = 0
        mock_library.niDigital_GetError.side_effect = MockFunctionCallError("niDigital_GetError")
        mock_library.niDigital_GetError.return_value = 0
        mock_library.niDigital_GetFailCount.side_effect = MockFunctionCallError("niDigital_GetFailCount")
        mock_library.niDigital_GetFailCount.return_value = 0
        mock_library.niDigital_GetHistoryRAMSampleCount.side_effect = MockFunctionCallError("niDigital_GetHistoryRAMSampleCount")
        mock_library.niDigital_GetHistoryRAMSampleCount.return_value = 0
        mock_library.niDigital_GetPatternName.side_effect = MockFunctionCallError("niDigital_GetPatternName")
        mock_library.niDigital_GetPatternName.return_value = 0
        mock_library.niDigital_GetPatternPinIndexes.side_effect = MockFunctionCallError("niDigital_GetPatternPinIndexes")
        mock_library.niDigital_GetPatternPinIndexes.return_value = 0
        mock_library.niDigital_GetPatternPinList.side_effect = MockFunctionCallError("niDigital_GetPatternPinList")
        mock_library.niDigital_GetPatternPinList.return_value = 0
        mock_library.niDigital_GetPinName.side_effect = MockFunctionCallError("niDigital_GetPinName")
        mock_library.niDigital_GetPinName.return_value = 0
        mock_library.niDigital_GetPinResultsPinInformation.side_effect = MockFunctionCallError("niDigital_GetPinResultsPinInformation")
        mock_library.niDigital_GetPinResultsPinInformation.return_value = 0
        mock_library.niDigital_GetSitePassFail.side_effect = MockFunctionCallError("niDigital_GetSitePassFail")
        mock_library.niDigital_GetSitePassFail.return_value = 0
        mock_library.niDigital_GetSiteResultsSiteNumbers.side_effect = MockFunctionCallError("niDigital_GetSiteResultsSiteNumbers")
        mock_library.niDigital_GetSiteResultsSiteNumbers.return_value = 0
        mock_library.niDigital_GetTimeSetDriveFormat.side_effect = MockFunctionCallError("niDigital_GetTimeSetDriveFormat")
        mock_library.niDigital_GetTimeSetDriveFormat.return_value = 0
        mock_library.niDigital_GetTimeSetEdge.side_effect = MockFunctionCallError("niDigital_GetTimeSetEdge")
        mock_library.niDigital_GetTimeSetEdge.return_value = 0
        mock_library.niDigital_GetTimeSetEdgeMultiplier.side_effect = MockFunctionCallError("niDigital_GetTimeSetEdgeMultiplier")
        mock_library.niDigital_GetTimeSetEdgeMultiplier.return_value = 0
        mock_library.niDigital_GetTimeSetName.side_effect = MockFunctionCallError("niDigital_GetTimeSetName")
        mock_library.niDigital_GetTimeSetName.return_value = 0
        mock_library.niDigital_GetTimeSetPeriod.side_effect = MockFunctionCallError("niDigital_GetTimeSetPeriod")
        mock_library.niDigital_GetTimeSetPeriod.return_value = 0
        mock_library.niDigital_InitWithOptions.side_effect = MockFunctionCallError("niDigital_InitWithOptions")
        mock_library.niDigital_InitWithOptions.return_value = 0
        mock_library.niDigital_Initiate.side_effect = MockFunctionCallError("niDigital_Initiate")
        mock_library.niDigital_Initiate.return_value = 0
        mock_library.niDigital_IsDone.side_effect = MockFunctionCallError("niDigital_IsDone")
        mock_library.niDigital_IsDone.return_value = 0
        mock_library.niDigital_IsSiteEnabled.side_effect = MockFunctionCallError("niDigital_IsSiteEnabled")
        mock_library.niDigital_IsSiteEnabled.return_value = 0
        mock_library.niDigital_LoadLevels.side_effect = MockFunctionCallError("niDigital_LoadLevels")
        mock_library.niDigital_LoadLevels.return_value = 0
        mock_library.niDigital_LoadPattern.side_effect = MockFunctionCallError("niDigital_LoadPattern")
        mock_library.niDigital_LoadPattern.return_value = 0
        mock_library.niDigital_LoadPinMap.side_effect = MockFunctionCallError("niDigital_LoadPinMap")
        mock_library.niDigital_LoadPinMap.return_value = 0
        mock_library.niDigital_LoadSpecifications.side_effect = MockFunctionCallError("niDigital_LoadSpecifications")
        mock_library.niDigital_LoadSpecifications.return_value = 0
        mock_library.niDigital_LoadTiming.side_effect = MockFunctionCallError("niDigital_LoadTiming")
        mock_library.niDigital_LoadTiming.return_value = 0
        mock_library.niDigital_LockSession.side_effect = MockFunctionCallError("niDigital_LockSession")
        mock_library.niDigital_LockSession.return_value = 0
        mock_library.niDigital_MapPinToChannel.side_effect = MockFunctionCallError("niDigital_MapPinToChannel")
        mock_library.niDigital_MapPinToChannel.return_value = 0
        mock_library.niDigital_PPMU_ConfigureApertureTime.side_effect = MockFunctionCallError("niDigital_PPMU_ConfigureApertureTime")
        mock_library.niDigital_PPMU_ConfigureApertureTime.return_value = 0
        mock_library.niDigital_PPMU_ConfigureCurrentLevel.side_effect = MockFunctionCallError("niDigital_PPMU_ConfigureCurrentLevel")
        mock_library.niDigital_PPMU_ConfigureCurrentLevel.return_value = 0
        mock_library.niDigital_PPMU_ConfigureCurrentLevelRange.side_effect = MockFunctionCallError("niDigital_PPMU_ConfigureCurrentLevelRange")
        mock_library.niDigital_PPMU_ConfigureCurrentLevelRange.return_value = 0
        mock_library.niDigital_PPMU_ConfigureCurrentLimit.side_effect = MockFunctionCallError("niDigital_PPMU_ConfigureCurrentLimit")
        mock_library.niDigital_PPMU_ConfigureCurrentLimit.return_value = 0
        mock_library.niDigital_PPMU_ConfigureCurrentLimitRange.side_effect = MockFunctionCallError("niDigital_PPMU_ConfigureCurrentLimitRange")
        mock_library.niDigital_PPMU_ConfigureCurrentLimitRange.return_value = 0
        mock_library.niDigital_PPMU_ConfigureOutputFunction.side_effect = MockFunctionCallError("niDigital_PPMU_ConfigureOutputFunction")
        mock_library.niDigital_PPMU_ConfigureOutputFunction.return_value = 0
        mock_library.niDigital_PPMU_ConfigureVoltageLevel.side_effect = MockFunctionCallError("niDigital_PPMU_ConfigureVoltageLevel")
        mock_library.niDigital_PPMU_ConfigureVoltageLevel.return_value = 0
        mock_library.niDigital_PPMU_ConfigureVoltageLimits.side_effect = MockFunctionCallError("niDigital_PPMU_ConfigureVoltageLimits")
        mock_library.niDigital_PPMU_ConfigureVoltageLimits.return_value = 0
        mock_library.niDigital_PPMU_Measure.side_effect = MockFunctionCallError("niDigital_PPMU_Measure")
        mock_library.niDigital_PPMU_Measure.return_value = 0
        mock_library.niDigital_PPMU_Source.side_effect = MockFunctionCallError("niDigital_PPMU_Source")
        mock_library.niDigital_PPMU_Source.return_value = 0
        mock_library.niDigital_ReadSequencerFlag.side_effect = MockFunctionCallError("niDigital_ReadSequencerFlag")
        mock_library.niDigital_ReadSequencerFlag.return_value = 0
        mock_library.niDigital_ReadSequencerRegister.side_effect = MockFunctionCallError("niDigital_ReadSequencerRegister")
        mock_library.niDigital_ReadSequencerRegister.return_value = 0
        mock_library.niDigital_ReadStatic.side_effect = MockFunctionCallError("niDigital_ReadStatic")
        mock_library.niDigital_ReadStatic.return_value = 0
        mock_library.niDigital_ResetAttribute.side_effect = MockFunctionCallError("niDigital_ResetAttribute")
        mock_library.niDigital_ResetAttribute.return_value = 0
        mock_library.niDigital_ResetDevice.side_effect = MockFunctionCallError("niDigital_ResetDevice")
        mock_library.niDigital_ResetDevice.return_value = 0
        mock_library.niDigital_SelectFunction.side_effect = MockFunctionCallError("niDigital_SelectFunction")
        mock_library.niDigital_SelectFunction.return_value = 0
        mock_library.niDigital_SelfCalibrate.side_effect = MockFunctionCallError("niDigital_SelfCalibrate")
        mock_library.niDigital_SelfCalibrate.return_value = 0
        mock_library.niDigital_SendSoftwareEdgeTrigger.side_effect = MockFunctionCallError("niDigital_SendSoftwareEdgeTrigger")
        mock_library.niDigital_SendSoftwareEdgeTrigger.return_value = 0
        mock_library.niDigital_SetAttributeViBoolean.side_effect = MockFunctionCallError("niDigital_SetAttributeViBoolean")
        mock_library.niDigital_SetAttributeViBoolean.return_value = 0
        mock_library.niDigital_SetAttributeViInt32.side_effect = MockFunctionCallError("niDigital_SetAttributeViInt32")
        mock_library.niDigital_SetAttributeViInt32.return_value = 0
        mock_library.niDigital_SetAttributeViInt64.side_effect = MockFunctionCallError("niDigital_SetAttributeViInt64")
        mock_library.niDigital_SetAttributeViInt64.return_value = 0
        mock_library.niDigital_SetAttributeViReal64.side_effect = MockFunctionCallError("niDigital_SetAttributeViReal64")
        mock_library.niDigital_SetAttributeViReal64.return_value = 0
        mock_library.niDigital_SetAttributeViSession.side_effect = MockFunctionCallError("niDigital_SetAttributeViSession")
        mock_library.niDigital_SetAttributeViSession.return_value = 0
        mock_library.niDigital_SetAttributeViString.side_effect = MockFunctionCallError("niDigital_SetAttributeViString")
        mock_library.niDigital_SetAttributeViString.return_value = 0
        mock_library.niDigital_TDR.side_effect = MockFunctionCallError("niDigital_TDR")
        mock_library.niDigital_TDR.return_value = 0
        mock_library.niDigital_UnloadAllPatterns.side_effect = MockFunctionCallError("niDigital_UnloadAllPatterns")
        mock_library.niDigital_UnloadAllPatterns.return_value = 0
        mock_library.niDigital_UnloadSpecifications.side_effect = MockFunctionCallError("niDigital_UnloadSpecifications")
        mock_library.niDigital_UnloadSpecifications.return_value = 0
        mock_library.niDigital_UnlockSession.side_effect = MockFunctionCallError("niDigital_UnlockSession")
        mock_library.niDigital_UnlockSession.return_value = 0
        mock_library.niDigital_WaitUntilDone.side_effect = MockFunctionCallError("niDigital_WaitUntilDone")
        mock_library.niDigital_WaitUntilDone.return_value = 0
        mock_library.niDigital_WriteSequencerFlag.side_effect = MockFunctionCallError("niDigital_WriteSequencerFlag")
        mock_library.niDigital_WriteSequencerFlag.return_value = 0
        mock_library.niDigital_WriteSequencerRegister.side_effect = MockFunctionCallError("niDigital_WriteSequencerRegister")
        mock_library.niDigital_WriteSequencerRegister.return_value = 0
        mock_library.niDigital_WriteSourceWaveformBroadcastU32.side_effect = MockFunctionCallError("niDigital_WriteSourceWaveformBroadcastU32")
        mock_library.niDigital_WriteSourceWaveformBroadcastU32.return_value = 0
        mock_library.niDigital_WriteSourceWaveformDataFromFileTDMS.side_effect = MockFunctionCallError("niDigital_WriteSourceWaveformDataFromFileTDMS")
        mock_library.niDigital_WriteSourceWaveformDataFromFileTDMS.return_value = 0
        mock_library.niDigital_WriteStatic.side_effect = MockFunctionCallError("niDigital_WriteStatic")
        mock_library.niDigital_WriteStatic.return_value = 0
        mock_library.niDigital_close.side_effect = MockFunctionCallError("niDigital_close")
        mock_library.niDigital_close.return_value = 0
        mock_library.niDigital_error_message.side_effect = MockFunctionCallError("niDigital_error_message")
        mock_library.niDigital_error_message.return_value = 0
        mock_library.niDigital_reset.side_effect = MockFunctionCallError("niDigital_reset")
        mock_library.niDigital_reset.return_value = 0
        mock_library.niDigital_self_test.side_effect = MockFunctionCallError("niDigital_self_test")
        mock_library.niDigital_self_test.return_value = 0
