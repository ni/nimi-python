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
        self._defaults['AllocateArbWaveform'] = {}
        self._defaults['AllocateArbWaveform']['return'] = 0
        self._defaults['ChangeExternalCalibrationPassword'] = {}
        self._defaults['ChangeExternalCalibrationPassword']['return'] = 0
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
        self._defaults['CheckGenerationStatus'] = {}
        self._defaults['CheckGenerationStatus']['return'] = 0
        self._defaults['CheckGenerationStatus']['isDone'] = None
        self._defaults['CheckIfConfigurationListExists'] = {}
        self._defaults['CheckIfConfigurationListExists']['return'] = 0
        self._defaults['CheckIfConfigurationListExists']['listExists'] = None
        self._defaults['CheckIfScriptExists'] = {}
        self._defaults['CheckIfScriptExists']['return'] = 0
        self._defaults['CheckIfScriptExists']['scriptExists'] = None
        self._defaults['CheckIfWaveformExists'] = {}
        self._defaults['CheckIfWaveformExists']['return'] = 0
        self._defaults['CheckIfWaveformExists']['waveformExists'] = None
        self._defaults['ClearAllArbWaveforms'] = {}
        self._defaults['ClearAllArbWaveforms']['return'] = 0
        self._defaults['ClearArbWaveform'] = {}
        self._defaults['ClearArbWaveform']['return'] = 0
        self._defaults['ClearError'] = {}
        self._defaults['ClearError']['return'] = 0
        self._defaults['ClearSelfCalibrateRange'] = {}
        self._defaults['ClearSelfCalibrateRange']['return'] = 0
        self._defaults['Commit'] = {}
        self._defaults['Commit']['return'] = 0
        self._defaults['ConfigureDeembeddingTableInterpolationLinear'] = {}
        self._defaults['ConfigureDeembeddingTableInterpolationLinear']['return'] = 0
        self._defaults['ConfigureDeembeddingTableInterpolationNearest'] = {}
        self._defaults['ConfigureDeembeddingTableInterpolationNearest']['return'] = 0
        self._defaults['ConfigureDeembeddingTableInterpolationSpline'] = {}
        self._defaults['ConfigureDeembeddingTableInterpolationSpline']['return'] = 0
        self._defaults['ConfigureDigitalEdgeConfigurationListStepTrigger'] = {}
        self._defaults['ConfigureDigitalEdgeConfigurationListStepTrigger']['return'] = 0
        self._defaults['ConfigureDigitalEdgeScriptTrigger'] = {}
        self._defaults['ConfigureDigitalEdgeScriptTrigger']['return'] = 0
        self._defaults['ConfigureDigitalEdgeStartTrigger'] = {}
        self._defaults['ConfigureDigitalEdgeStartTrigger']['return'] = 0
        self._defaults['ConfigureDigitalLevelScriptTrigger'] = {}
        self._defaults['ConfigureDigitalLevelScriptTrigger']['return'] = 0
        self._defaults['ConfigureDigitalModulationUserDefinedWaveform'] = {}
        self._defaults['ConfigureDigitalModulationUserDefinedWaveform']['return'] = 0
        self._defaults['ConfigureGenerationMode'] = {}
        self._defaults['ConfigureGenerationMode']['return'] = 0
        self._defaults['ConfigureOutputEnabled'] = {}
        self._defaults['ConfigureOutputEnabled']['return'] = 0
        self._defaults['ConfigureP2PEndpointFullnessStartTrigger'] = {}
        self._defaults['ConfigureP2PEndpointFullnessStartTrigger']['return'] = 0
        self._defaults['ConfigurePowerLevelType'] = {}
        self._defaults['ConfigurePowerLevelType']['return'] = 0
        self._defaults['ConfigurePxiChassisClk10'] = {}
        self._defaults['ConfigurePxiChassisClk10']['return'] = 0
        self._defaults['ConfigureRF'] = {}
        self._defaults['ConfigureRF']['return'] = 0
        self._defaults['ConfigureRefClock'] = {}
        self._defaults['ConfigureRefClock']['return'] = 0
        self._defaults['ConfigureSignalBandwidth'] = {}
        self._defaults['ConfigureSignalBandwidth']['return'] = 0
        self._defaults['ConfigureSoftwareScriptTrigger'] = {}
        self._defaults['ConfigureSoftwareScriptTrigger']['return'] = 0
        self._defaults['ConfigureSoftwareStartTrigger'] = {}
        self._defaults['ConfigureSoftwareStartTrigger']['return'] = 0
        self._defaults['CreateConfigurationList'] = {}
        self._defaults['CreateConfigurationList']['return'] = 0
        self._defaults['CreateConfigurationListStep'] = {}
        self._defaults['CreateConfigurationListStep']['return'] = 0
        self._defaults['CreateDeembeddingSparameterTableS2PFile'] = {}
        self._defaults['CreateDeembeddingSparameterTableS2PFile']['return'] = 0
        self._defaults['DeleteAllDeembeddingTables'] = {}
        self._defaults['DeleteAllDeembeddingTables']['return'] = 0
        self._defaults['DeleteConfigurationList'] = {}
        self._defaults['DeleteConfigurationList']['return'] = 0
        self._defaults['DeleteDeembeddingTable'] = {}
        self._defaults['DeleteDeembeddingTable']['return'] = 0
        self._defaults['Disable'] = {}
        self._defaults['Disable']['return'] = 0
        self._defaults['DisableConfigurationListStepTrigger'] = {}
        self._defaults['DisableConfigurationListStepTrigger']['return'] = 0
        self._defaults['DisableScriptTrigger'] = {}
        self._defaults['DisableScriptTrigger']['return'] = 0
        self._defaults['DisableStartTrigger'] = {}
        self._defaults['DisableStartTrigger']['return'] = 0
        self._defaults['ErrorMessage'] = {}
        self._defaults['ErrorMessage']['return'] = 0
        self._defaults['ErrorQuery'] = {}
        self._defaults['ErrorQuery']['return'] = 0
        self._defaults['ErrorQuery']['errorCode'] = None
        self._defaults['ExportSignal'] = {}
        self._defaults['ExportSignal']['return'] = 0
        self._defaults['GetAllNamedWaveformNames'] = {}
        self._defaults['GetAllNamedWaveformNames']['return'] = 0
        self._defaults['GetAllNamedWaveformNames']['actualBufferSize'] = None
        self._defaults['GetAllScriptNames'] = {}
        self._defaults['GetAllScriptNames']['return'] = 0
        self._defaults['GetAllScriptNames']['actualBufferSize'] = None
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
        self._defaults['GetChannelName'] = {}
        self._defaults['GetChannelName']['return'] = 0
        self._defaults['GetDeembeddingSparameters'] = {}
        self._defaults['GetDeembeddingSparameters']['return'] = 0
        self._defaults['GetDeembeddingSparameters']['sparameters'] = None
        self._defaults['GetDeembeddingSparameters']['numberOfSparameters'] = None
        self._defaults['GetDeembeddingSparameters']['numberOfPorts'] = None
        self._defaults['GetError'] = {}
        self._defaults['GetError']['return'] = 0
        self._defaults['GetError']['errorCode'] = None
        self._defaults['GetError']['errorDescription'] = None
        self._defaults['GetExternalCalibrationLastDateAndTime'] = {}
        self._defaults['GetExternalCalibrationLastDateAndTime']['return'] = 0
        self._defaults['GetExternalCalibrationLastDateAndTime']['year'] = None
        self._defaults['GetExternalCalibrationLastDateAndTime']['month'] = None
        self._defaults['GetExternalCalibrationLastDateAndTime']['day'] = None
        self._defaults['GetExternalCalibrationLastDateAndTime']['hour'] = None
        self._defaults['GetExternalCalibrationLastDateAndTime']['minute'] = None
        self._defaults['GetExternalCalibrationLastDateAndTime']['second'] = None
        self._defaults['GetMaxSettablePower'] = {}
        self._defaults['GetMaxSettablePower']['return'] = 0
        self._defaults['GetMaxSettablePower']['value'] = None
        self._defaults['GetSelfCalibrationDateAndTime'] = {}
        self._defaults['GetSelfCalibrationDateAndTime']['return'] = 0
        self._defaults['GetSelfCalibrationDateAndTime']['year'] = None
        self._defaults['GetSelfCalibrationDateAndTime']['month'] = None
        self._defaults['GetSelfCalibrationDateAndTime']['day'] = None
        self._defaults['GetSelfCalibrationDateAndTime']['hour'] = None
        self._defaults['GetSelfCalibrationDateAndTime']['minute'] = None
        self._defaults['GetSelfCalibrationDateAndTime']['second'] = None
        self._defaults['GetSelfCalibrationTemperature'] = {}
        self._defaults['GetSelfCalibrationTemperature']['return'] = 0
        self._defaults['GetSelfCalibrationTemperature']['temperature'] = None
        self._defaults['GetStreamEndpointHandle'] = {}
        self._defaults['GetStreamEndpointHandle']['return'] = 0
        self._defaults['GetStreamEndpointHandle']['readerHandle'] = None
        self._defaults['GetTerminalName'] = {}
        self._defaults['GetTerminalName']['return'] = 0
        self._defaults['GetWaveformBurstStartLocations'] = {}
        self._defaults['GetWaveformBurstStartLocations']['return'] = 0
        self._defaults['GetWaveformBurstStartLocations']['locations'] = None
        self._defaults['GetWaveformBurstStartLocations']['requiredSize'] = None
        self._defaults['GetWaveformBurstStopLocations'] = {}
        self._defaults['GetWaveformBurstStopLocations']['return'] = 0
        self._defaults['GetWaveformBurstStopLocations']['locations'] = None
        self._defaults['GetWaveformBurstStopLocations']['requiredSize'] = None
        self._defaults['GetWaveformMarkerEventLocations'] = {}
        self._defaults['GetWaveformMarkerEventLocations']['return'] = 0
        self._defaults['GetWaveformMarkerEventLocations']['locations'] = None
        self._defaults['GetWaveformMarkerEventLocations']['requiredSize'] = None
        self._defaults['InitWithOptions'] = {}
        self._defaults['InitWithOptions']['return'] = 0
        self._defaults['InitWithOptions']['newVi'] = None
        self._defaults['Initiate'] = {}
        self._defaults['Initiate']['return'] = 0
        self._defaults['LoadConfigurationsFromFile'] = {}
        self._defaults['LoadConfigurationsFromFile']['return'] = 0
        self._defaults['LockSession'] = {}
        self._defaults['LockSession']['return'] = 0
        self._defaults['LockSession']['callerHasLock'] = None
        self._defaults['PerformPowerSearch'] = {}
        self._defaults['PerformPowerSearch']['return'] = 0
        self._defaults['PerformThermalCorrection'] = {}
        self._defaults['PerformThermalCorrection']['return'] = 0
        self._defaults['QueryArbWaveformCapabilities'] = {}
        self._defaults['QueryArbWaveformCapabilities']['return'] = 0
        self._defaults['QueryArbWaveformCapabilities']['maxNumberWaveforms'] = None
        self._defaults['QueryArbWaveformCapabilities']['waveformQuantum'] = None
        self._defaults['QueryArbWaveformCapabilities']['minWaveformSize'] = None
        self._defaults['QueryArbWaveformCapabilities']['maxWaveformSize'] = None
        self._defaults['ReadAndDownloadWaveformFromFileTDMS'] = {}
        self._defaults['ReadAndDownloadWaveformFromFileTDMS']['return'] = 0
        self._defaults['Reset'] = {}
        self._defaults['Reset']['return'] = 0
        self._defaults['ResetAttribute'] = {}
        self._defaults['ResetAttribute']['return'] = 0
        self._defaults['ResetDevice'] = {}
        self._defaults['ResetDevice']['return'] = 0
        self._defaults['ResetWithDefaults'] = {}
        self._defaults['ResetWithDefaults']['return'] = 0
        self._defaults['ResetWithOptions'] = {}
        self._defaults['ResetWithOptions']['return'] = 0
        self._defaults['RevisionQuery'] = {}
        self._defaults['RevisionQuery']['return'] = 0
        self._defaults['SaveConfigurationsToFile'] = {}
        self._defaults['SaveConfigurationsToFile']['return'] = 0
        self._defaults['SelectArbWaveform'] = {}
        self._defaults['SelectArbWaveform']['return'] = 0
        self._defaults['SelfCal'] = {}
        self._defaults['SelfCal']['return'] = 0
        self._defaults['SelfCalibrateRange'] = {}
        self._defaults['SelfCalibrateRange']['return'] = 0
        self._defaults['SelfTest'] = {}
        self._defaults['SelfTest']['return'] = 0
        self._defaults['SelfTest']['selfTestResult'] = None
        self._defaults['SendSoftwareEdgeTrigger'] = {}
        self._defaults['SendSoftwareEdgeTrigger']['return'] = 0
        self._defaults['SetArbWaveformNextWritePosition'] = {}
        self._defaults['SetArbWaveformNextWritePosition']['return'] = 0
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
        self._defaults['SetWaveformBurstStartLocations'] = {}
        self._defaults['SetWaveformBurstStartLocations']['return'] = 0
        self._defaults['SetWaveformBurstStartLocations']['locations'] = None
        self._defaults['SetWaveformBurstStopLocations'] = {}
        self._defaults['SetWaveformBurstStopLocations']['return'] = 0
        self._defaults['SetWaveformBurstStopLocations']['locations'] = None
        self._defaults['SetWaveformMarkerEventLocations'] = {}
        self._defaults['SetWaveformMarkerEventLocations']['return'] = 0
        self._defaults['SetWaveformMarkerEventLocations']['locations'] = None
        self._defaults['UnlockSession'] = {}
        self._defaults['UnlockSession']['return'] = 0
        self._defaults['UnlockSession']['callerHasLock'] = None
        self._defaults['WaitUntilSettled'] = {}
        self._defaults['WaitUntilSettled']['return'] = 0
        self._defaults['WriteArbWaveform'] = {}
        self._defaults['WriteArbWaveform']['return'] = 0
        self._defaults['WriteArbWaveformF32'] = {}
        self._defaults['WriteArbWaveformF32']['return'] = 0
        self._defaults['WriteP2PEndpointI16'] = {}
        self._defaults['WriteP2PEndpointI16']['return'] = 0
        self._defaults['WriteScript'] = {}
        self._defaults['WriteScript']['return'] = 0
        self._defaults['close'] = {}
        self._defaults['close']['return'] = 0

    def __getitem__(self, func):
        return self._defaults[func]

    def __setitem__(self, func, val):
        self._defaults[func] = val

    def niRFSG_Abort(self, vi):  # noqa: N802
        if self._defaults['Abort']['return'] != 0:
            return self._defaults['Abort']['return']
        return self._defaults['Abort']['return']

    def niRFSG_AllocateArbWaveform(self, vi, waveform_name, size_in_samples):  # noqa: N802
        if self._defaults['AllocateArbWaveform']['return'] != 0:
            return self._defaults['AllocateArbWaveform']['return']
        return self._defaults['AllocateArbWaveform']['return']

    def niRFSG_ChangeExternalCalibrationPassword(self, vi, old_password, new_password):  # noqa: N802
        if self._defaults['ChangeExternalCalibrationPassword']['return'] != 0:
            return self._defaults['ChangeExternalCalibrationPassword']['return']
        return self._defaults['ChangeExternalCalibrationPassword']['return']

    def niRFSG_CheckAttributeViBoolean(self, vi, channel_name, attribute, value):  # noqa: N802
        if self._defaults['CheckAttributeViBoolean']['return'] != 0:
            return self._defaults['CheckAttributeViBoolean']['return']
        return self._defaults['CheckAttributeViBoolean']['return']

    def niRFSG_CheckAttributeViInt32(self, vi, channel_name, attribute, value):  # noqa: N802
        if self._defaults['CheckAttributeViInt32']['return'] != 0:
            return self._defaults['CheckAttributeViInt32']['return']
        return self._defaults['CheckAttributeViInt32']['return']

    def niRFSG_CheckAttributeViInt64(self, vi, channel_name, attribute, value):  # noqa: N802
        if self._defaults['CheckAttributeViInt64']['return'] != 0:
            return self._defaults['CheckAttributeViInt64']['return']
        return self._defaults['CheckAttributeViInt64']['return']

    def niRFSG_CheckAttributeViReal64(self, vi, channel_name, attribute, value):  # noqa: N802
        if self._defaults['CheckAttributeViReal64']['return'] != 0:
            return self._defaults['CheckAttributeViReal64']['return']
        return self._defaults['CheckAttributeViReal64']['return']

    def niRFSG_CheckAttributeViSession(self, vi, channel_name, attribute, value):  # noqa: N802
        if self._defaults['CheckAttributeViSession']['return'] != 0:
            return self._defaults['CheckAttributeViSession']['return']
        return self._defaults['CheckAttributeViSession']['return']

    def niRFSG_CheckAttributeViString(self, vi, channel_name, attribute, value):  # noqa: N802
        if self._defaults['CheckAttributeViString']['return'] != 0:
            return self._defaults['CheckAttributeViString']['return']
        return self._defaults['CheckAttributeViString']['return']

    def niRFSG_CheckGenerationStatus(self, vi, is_done):  # noqa: N802
        if self._defaults['CheckGenerationStatus']['return'] != 0:
            return self._defaults['CheckGenerationStatus']['return']
        # is_done
        if self._defaults['CheckGenerationStatus']['isDone'] is None:
            raise MockFunctionCallError("niRFSG_CheckGenerationStatus", param='isDone')
        if is_done is not None:
            is_done.contents.value = self._defaults['CheckGenerationStatus']['isDone']
        return self._defaults['CheckGenerationStatus']['return']

    def niRFSG_CheckIfConfigurationListExists(self, vi, list_name, list_exists):  # noqa: N802
        if self._defaults['CheckIfConfigurationListExists']['return'] != 0:
            return self._defaults['CheckIfConfigurationListExists']['return']
        # list_exists
        if self._defaults['CheckIfConfigurationListExists']['listExists'] is None:
            raise MockFunctionCallError("niRFSG_CheckIfConfigurationListExists", param='listExists')
        if list_exists is not None:
            list_exists.contents.value = self._defaults['CheckIfConfigurationListExists']['listExists']
        return self._defaults['CheckIfConfigurationListExists']['return']

    def niRFSG_CheckIfScriptExists(self, vi, script_name, script_exists):  # noqa: N802
        if self._defaults['CheckIfScriptExists']['return'] != 0:
            return self._defaults['CheckIfScriptExists']['return']
        # script_exists
        if self._defaults['CheckIfScriptExists']['scriptExists'] is None:
            raise MockFunctionCallError("niRFSG_CheckIfScriptExists", param='scriptExists')
        if script_exists is not None:
            script_exists.contents.value = self._defaults['CheckIfScriptExists']['scriptExists']
        return self._defaults['CheckIfScriptExists']['return']

    def niRFSG_CheckIfWaveformExists(self, vi, waveform_name, waveform_exists):  # noqa: N802
        if self._defaults['CheckIfWaveformExists']['return'] != 0:
            return self._defaults['CheckIfWaveformExists']['return']
        # waveform_exists
        if self._defaults['CheckIfWaveformExists']['waveformExists'] is None:
            raise MockFunctionCallError("niRFSG_CheckIfWaveformExists", param='waveformExists')
        if waveform_exists is not None:
            waveform_exists.contents.value = self._defaults['CheckIfWaveformExists']['waveformExists']
        return self._defaults['CheckIfWaveformExists']['return']

    def niRFSG_ClearAllArbWaveforms(self, vi):  # noqa: N802
        if self._defaults['ClearAllArbWaveforms']['return'] != 0:
            return self._defaults['ClearAllArbWaveforms']['return']
        return self._defaults['ClearAllArbWaveforms']['return']

    def niRFSG_ClearArbWaveform(self, vi, name):  # noqa: N802
        if self._defaults['ClearArbWaveform']['return'] != 0:
            return self._defaults['ClearArbWaveform']['return']
        return self._defaults['ClearArbWaveform']['return']

    def niRFSG_ClearError(self, vi):  # noqa: N802
        if self._defaults['ClearError']['return'] != 0:
            return self._defaults['ClearError']['return']
        return self._defaults['ClearError']['return']

    def niRFSG_ClearSelfCalibrateRange(self, vi):  # noqa: N802
        if self._defaults['ClearSelfCalibrateRange']['return'] != 0:
            return self._defaults['ClearSelfCalibrateRange']['return']
        return self._defaults['ClearSelfCalibrateRange']['return']

    def niRFSG_Commit(self, vi):  # noqa: N802
        if self._defaults['Commit']['return'] != 0:
            return self._defaults['Commit']['return']
        return self._defaults['Commit']['return']

    def niRFSG_ConfigureDeembeddingTableInterpolationLinear(self, vi, port, table_name, format):  # noqa: N802
        if self._defaults['ConfigureDeembeddingTableInterpolationLinear']['return'] != 0:
            return self._defaults['ConfigureDeembeddingTableInterpolationLinear']['return']
        return self._defaults['ConfigureDeembeddingTableInterpolationLinear']['return']

    def niRFSG_ConfigureDeembeddingTableInterpolationNearest(self, vi, port, table_name):  # noqa: N802
        if self._defaults['ConfigureDeembeddingTableInterpolationNearest']['return'] != 0:
            return self._defaults['ConfigureDeembeddingTableInterpolationNearest']['return']
        return self._defaults['ConfigureDeembeddingTableInterpolationNearest']['return']

    def niRFSG_ConfigureDeembeddingTableInterpolationSpline(self, vi, port, table_name):  # noqa: N802
        if self._defaults['ConfigureDeembeddingTableInterpolationSpline']['return'] != 0:
            return self._defaults['ConfigureDeembeddingTableInterpolationSpline']['return']
        return self._defaults['ConfigureDeembeddingTableInterpolationSpline']['return']

    def niRFSG_ConfigureDigitalEdgeConfigurationListStepTrigger(self, vi, source, edge):  # noqa: N802
        if self._defaults['ConfigureDigitalEdgeConfigurationListStepTrigger']['return'] != 0:
            return self._defaults['ConfigureDigitalEdgeConfigurationListStepTrigger']['return']
        return self._defaults['ConfigureDigitalEdgeConfigurationListStepTrigger']['return']

    def niRFSG_ConfigureDigitalEdgeScriptTrigger(self, vi, trigger_id, source, edge):  # noqa: N802
        if self._defaults['ConfigureDigitalEdgeScriptTrigger']['return'] != 0:
            return self._defaults['ConfigureDigitalEdgeScriptTrigger']['return']
        return self._defaults['ConfigureDigitalEdgeScriptTrigger']['return']

    def niRFSG_ConfigureDigitalEdgeStartTrigger(self, vi, source, edge):  # noqa: N802
        if self._defaults['ConfigureDigitalEdgeStartTrigger']['return'] != 0:
            return self._defaults['ConfigureDigitalEdgeStartTrigger']['return']
        return self._defaults['ConfigureDigitalEdgeStartTrigger']['return']

    def niRFSG_ConfigureDigitalLevelScriptTrigger(self, vi, trigger_id, source, level):  # noqa: N802
        if self._defaults['ConfigureDigitalLevelScriptTrigger']['return'] != 0:
            return self._defaults['ConfigureDigitalLevelScriptTrigger']['return']
        return self._defaults['ConfigureDigitalLevelScriptTrigger']['return']

    def niRFSG_ConfigureDigitalModulationUserDefinedWaveform(self, vi, number_of_samples, user_defined_waveform):  # noqa: N802
        if self._defaults['ConfigureDigitalModulationUserDefinedWaveform']['return'] != 0:
            return self._defaults['ConfigureDigitalModulationUserDefinedWaveform']['return']
        return self._defaults['ConfigureDigitalModulationUserDefinedWaveform']['return']

    def niRFSG_ConfigureGenerationMode(self, vi, generation_mode):  # noqa: N802
        if self._defaults['ConfigureGenerationMode']['return'] != 0:
            return self._defaults['ConfigureGenerationMode']['return']
        return self._defaults['ConfigureGenerationMode']['return']

    def niRFSG_ConfigureOutputEnabled(self, vi, output_enabled):  # noqa: N802
        if self._defaults['ConfigureOutputEnabled']['return'] != 0:
            return self._defaults['ConfigureOutputEnabled']['return']
        return self._defaults['ConfigureOutputEnabled']['return']

    def niRFSG_ConfigureP2PEndpointFullnessStartTrigger(self, vi, p2p_endpoint_fullness_level):  # noqa: N802
        if self._defaults['ConfigureP2PEndpointFullnessStartTrigger']['return'] != 0:
            return self._defaults['ConfigureP2PEndpointFullnessStartTrigger']['return']
        return self._defaults['ConfigureP2PEndpointFullnessStartTrigger']['return']

    def niRFSG_ConfigurePowerLevelType(self, vi, power_level_type):  # noqa: N802
        if self._defaults['ConfigurePowerLevelType']['return'] != 0:
            return self._defaults['ConfigurePowerLevelType']['return']
        return self._defaults['ConfigurePowerLevelType']['return']

    def niRFSG_ConfigurePxiChassisClk10(self, vi, pxi_clk10_source):  # noqa: N802
        if self._defaults['ConfigurePxiChassisClk10']['return'] != 0:
            return self._defaults['ConfigurePxiChassisClk10']['return']
        return self._defaults['ConfigurePxiChassisClk10']['return']

    def niRFSG_ConfigureRF(self, vi, frequency, power_level):  # noqa: N802
        if self._defaults['ConfigureRF']['return'] != 0:
            return self._defaults['ConfigureRF']['return']
        return self._defaults['ConfigureRF']['return']

    def niRFSG_ConfigureRefClock(self, vi, ref_clock_source, ref_clock_rate):  # noqa: N802
        if self._defaults['ConfigureRefClock']['return'] != 0:
            return self._defaults['ConfigureRefClock']['return']
        return self._defaults['ConfigureRefClock']['return']

    def niRFSG_ConfigureSignalBandwidth(self, vi, signal_bandwidth):  # noqa: N802
        if self._defaults['ConfigureSignalBandwidth']['return'] != 0:
            return self._defaults['ConfigureSignalBandwidth']['return']
        return self._defaults['ConfigureSignalBandwidth']['return']

    def niRFSG_ConfigureSoftwareScriptTrigger(self, vi, trigger_id):  # noqa: N802
        if self._defaults['ConfigureSoftwareScriptTrigger']['return'] != 0:
            return self._defaults['ConfigureSoftwareScriptTrigger']['return']
        return self._defaults['ConfigureSoftwareScriptTrigger']['return']

    def niRFSG_ConfigureSoftwareStartTrigger(self, vi):  # noqa: N802
        if self._defaults['ConfigureSoftwareStartTrigger']['return'] != 0:
            return self._defaults['ConfigureSoftwareStartTrigger']['return']
        return self._defaults['ConfigureSoftwareStartTrigger']['return']

    def niRFSG_CreateConfigurationList(self, vi, list_name, number_of_attributes, configuration_list_attributes, set_as_active_list):  # noqa: N802
        if self._defaults['CreateConfigurationList']['return'] != 0:
            return self._defaults['CreateConfigurationList']['return']
        return self._defaults['CreateConfigurationList']['return']

    def niRFSG_CreateConfigurationListStep(self, vi, set_as_active_step):  # noqa: N802
        if self._defaults['CreateConfigurationListStep']['return'] != 0:
            return self._defaults['CreateConfigurationListStep']['return']
        return self._defaults['CreateConfigurationListStep']['return']

    def niRFSG_CreateDeembeddingSparameterTableS2PFile(self, vi, port, table_name, s2p_file_path, sparameter_orientation):  # noqa: N802
        if self._defaults['CreateDeembeddingSparameterTableS2PFile']['return'] != 0:
            return self._defaults['CreateDeembeddingSparameterTableS2PFile']['return']
        return self._defaults['CreateDeembeddingSparameterTableS2PFile']['return']

    def niRFSG_DeleteAllDeembeddingTables(self, vi):  # noqa: N802
        if self._defaults['DeleteAllDeembeddingTables']['return'] != 0:
            return self._defaults['DeleteAllDeembeddingTables']['return']
        return self._defaults['DeleteAllDeembeddingTables']['return']

    def niRFSG_DeleteConfigurationList(self, vi, list_name):  # noqa: N802
        if self._defaults['DeleteConfigurationList']['return'] != 0:
            return self._defaults['DeleteConfigurationList']['return']
        return self._defaults['DeleteConfigurationList']['return']

    def niRFSG_DeleteDeembeddingTable(self, vi, port, table_name):  # noqa: N802
        if self._defaults['DeleteDeembeddingTable']['return'] != 0:
            return self._defaults['DeleteDeembeddingTable']['return']
        return self._defaults['DeleteDeembeddingTable']['return']

    def niRFSG_Disable(self, vi):  # noqa: N802
        if self._defaults['Disable']['return'] != 0:
            return self._defaults['Disable']['return']
        return self._defaults['Disable']['return']

    def niRFSG_DisableConfigurationListStepTrigger(self, vi):  # noqa: N802
        if self._defaults['DisableConfigurationListStepTrigger']['return'] != 0:
            return self._defaults['DisableConfigurationListStepTrigger']['return']
        return self._defaults['DisableConfigurationListStepTrigger']['return']

    def niRFSG_DisableScriptTrigger(self, vi, trigger_id):  # noqa: N802
        if self._defaults['DisableScriptTrigger']['return'] != 0:
            return self._defaults['DisableScriptTrigger']['return']
        return self._defaults['DisableScriptTrigger']['return']

    def niRFSG_DisableStartTrigger(self, vi):  # noqa: N802
        if self._defaults['DisableStartTrigger']['return'] != 0:
            return self._defaults['DisableStartTrigger']['return']
        return self._defaults['DisableStartTrigger']['return']

    def niRFSG_ErrorMessage(self, vi, error_code, error_message):  # noqa: N802
        if self._defaults['ErrorMessage']['return'] != 0:
            return self._defaults['ErrorMessage']['return']
        return self._defaults['ErrorMessage']['return']

    def niRFSG_ErrorQuery(self, vi, error_code, error_message):  # noqa: N802
        if self._defaults['ErrorQuery']['return'] != 0:
            return self._defaults['ErrorQuery']['return']
        # error_code
        if self._defaults['ErrorQuery']['errorCode'] is None:
            raise MockFunctionCallError("niRFSG_ErrorQuery", param='errorCode')
        if error_code is not None:
            error_code.contents.value = self._defaults['ErrorQuery']['errorCode']
        return self._defaults['ErrorQuery']['return']

    def niRFSG_ExportSignal(self, vi, signal, signal_identifier, output_terminal):  # noqa: N802
        if self._defaults['ExportSignal']['return'] != 0:
            return self._defaults['ExportSignal']['return']
        return self._defaults['ExportSignal']['return']

    def niRFSG_GetAllNamedWaveformNames(self, vi, waveform_names, buffer_size, actual_buffer_size):  # noqa: N802
        if self._defaults['GetAllNamedWaveformNames']['return'] != 0:
            return self._defaults['GetAllNamedWaveformNames']['return']
        # actual_buffer_size
        if self._defaults['GetAllNamedWaveformNames']['actualBufferSize'] is None:
            raise MockFunctionCallError("niRFSG_GetAllNamedWaveformNames", param='actualBufferSize')
        if actual_buffer_size is not None:
            actual_buffer_size.contents.value = self._defaults['GetAllNamedWaveformNames']['actualBufferSize']
        return self._defaults['GetAllNamedWaveformNames']['return']

    def niRFSG_GetAllScriptNames(self, vi, script_names, buffer_size, actual_buffer_size):  # noqa: N802
        if self._defaults['GetAllScriptNames']['return'] != 0:
            return self._defaults['GetAllScriptNames']['return']
        # actual_buffer_size
        if self._defaults['GetAllScriptNames']['actualBufferSize'] is None:
            raise MockFunctionCallError("niRFSG_GetAllScriptNames", param='actualBufferSize')
        if actual_buffer_size is not None:
            actual_buffer_size.contents.value = self._defaults['GetAllScriptNames']['actualBufferSize']
        return self._defaults['GetAllScriptNames']['return']

    def niRFSG_GetAttributeViBoolean(self, vi, channel_name, attribute, value):  # noqa: N802
        if self._defaults['GetAttributeViBoolean']['return'] != 0:
            return self._defaults['GetAttributeViBoolean']['return']
        # value
        if self._defaults['GetAttributeViBoolean']['value'] is None:
            raise MockFunctionCallError("niRFSG_GetAttributeViBoolean", param='value')
        if value is not None:
            value.contents.value = self._defaults['GetAttributeViBoolean']['value']
        return self._defaults['GetAttributeViBoolean']['return']

    def niRFSG_GetAttributeViInt32(self, vi, channel_name, attribute, value):  # noqa: N802
        if self._defaults['GetAttributeViInt32']['return'] != 0:
            return self._defaults['GetAttributeViInt32']['return']
        # value
        if self._defaults['GetAttributeViInt32']['value'] is None:
            raise MockFunctionCallError("niRFSG_GetAttributeViInt32", param='value')
        if value is not None:
            value.contents.value = self._defaults['GetAttributeViInt32']['value']
        return self._defaults['GetAttributeViInt32']['return']

    def niRFSG_GetAttributeViInt64(self, vi, channel_name, attribute, value):  # noqa: N802
        if self._defaults['GetAttributeViInt64']['return'] != 0:
            return self._defaults['GetAttributeViInt64']['return']
        # value
        if self._defaults['GetAttributeViInt64']['value'] is None:
            raise MockFunctionCallError("niRFSG_GetAttributeViInt64", param='value')
        if value is not None:
            value.contents.value = self._defaults['GetAttributeViInt64']['value']
        return self._defaults['GetAttributeViInt64']['return']

    def niRFSG_GetAttributeViReal64(self, vi, channel_name, attribute, value):  # noqa: N802
        if self._defaults['GetAttributeViReal64']['return'] != 0:
            return self._defaults['GetAttributeViReal64']['return']
        # value
        if self._defaults['GetAttributeViReal64']['value'] is None:
            raise MockFunctionCallError("niRFSG_GetAttributeViReal64", param='value')
        if value is not None:
            value.contents.value = self._defaults['GetAttributeViReal64']['value']
        return self._defaults['GetAttributeViReal64']['return']

    def niRFSG_GetAttributeViSession(self, vi, channel_name, attribute, value):  # noqa: N802
        if self._defaults['GetAttributeViSession']['return'] != 0:
            return self._defaults['GetAttributeViSession']['return']
        # value
        if self._defaults['GetAttributeViSession']['value'] is None:
            raise MockFunctionCallError("niRFSG_GetAttributeViSession", param='value')
        if value is not None:
            value.contents.value = self._defaults['GetAttributeViSession']['value']
        return self._defaults['GetAttributeViSession']['return']

    def niRFSG_GetAttributeViString(self, vi, channel_name, attribute, buf_size, value):  # noqa: N802
        if self._defaults['GetAttributeViString']['return'] != 0:
            return self._defaults['GetAttributeViString']['return']
        return self._defaults['GetAttributeViString']['return']

    def niRFSG_GetChannelName(self, vi, index, buffer_size, name):  # noqa: N802
        if self._defaults['GetChannelName']['return'] != 0:
            return self._defaults['GetChannelName']['return']
        return self._defaults['GetChannelName']['return']

    def niRFSG_GetDeembeddingSparameters(self, vi, sparameters, sparameters_array_size, number_of_sparameters, number_of_ports):  # noqa: N802
        if self._defaults['GetDeembeddingSparameters']['return'] != 0:
            return self._defaults['GetDeembeddingSparameters']['return']
        # sparameters
        if self._defaults['GetDeembeddingSparameters']['sparameters'] is None:
            raise MockFunctionCallError("niRFSG_GetDeembeddingSparameters", param='sparameters')
        if sparameters is not None:
            sparameters.contents.value = self._defaults['GetDeembeddingSparameters']['sparameters']
        # number_of_sparameters
        if self._defaults['GetDeembeddingSparameters']['numberOfSparameters'] is None:
            raise MockFunctionCallError("niRFSG_GetDeembeddingSparameters", param='numberOfSparameters')
        if number_of_sparameters is not None:
            number_of_sparameters.contents.value = self._defaults['GetDeembeddingSparameters']['numberOfSparameters']
        # number_of_ports
        if self._defaults['GetDeembeddingSparameters']['numberOfPorts'] is None:
            raise MockFunctionCallError("niRFSG_GetDeembeddingSparameters", param='numberOfPorts')
        if number_of_ports is not None:
            number_of_ports.contents.value = self._defaults['GetDeembeddingSparameters']['numberOfPorts']
        return self._defaults['GetDeembeddingSparameters']['return']

    def niRFSG_GetError(self, vi, error_code, error_description_buffer_size, error_description):  # noqa: N802
        if self._defaults['GetError']['return'] != 0:
            return self._defaults['GetError']['return']
        # error_code
        if self._defaults['GetError']['errorCode'] is None:
            raise MockFunctionCallError("niRFSG_GetError", param='errorCode')
        if error_code is not None:
            error_code.contents.value = self._defaults['GetError']['errorCode']
        # error_description
        if self._defaults['GetError']['errorDescription'] is None:
            raise MockFunctionCallError("niRFSG_GetError", param='errorDescription')
        if error_description_buffer_size.value == 0:
            return len(self._defaults['GetError']['errorDescription'])
        error_description.value = self._defaults['GetError']['errorDescription'].encode('ascii')
        return self._defaults['GetError']['return']

    def niRFSG_GetExternalCalibrationLastDateAndTime(self, vi, year, month, day, hour, minute, second):  # noqa: N802
        if self._defaults['GetExternalCalibrationLastDateAndTime']['return'] != 0:
            return self._defaults['GetExternalCalibrationLastDateAndTime']['return']
        # year
        if self._defaults['GetExternalCalibrationLastDateAndTime']['year'] is None:
            raise MockFunctionCallError("niRFSG_GetExternalCalibrationLastDateAndTime", param='year')
        if year is not None:
            year.contents.value = self._defaults['GetExternalCalibrationLastDateAndTime']['year']
        # month
        if self._defaults['GetExternalCalibrationLastDateAndTime']['month'] is None:
            raise MockFunctionCallError("niRFSG_GetExternalCalibrationLastDateAndTime", param='month')
        if month is not None:
            month.contents.value = self._defaults['GetExternalCalibrationLastDateAndTime']['month']
        # day
        if self._defaults['GetExternalCalibrationLastDateAndTime']['day'] is None:
            raise MockFunctionCallError("niRFSG_GetExternalCalibrationLastDateAndTime", param='day')
        if day is not None:
            day.contents.value = self._defaults['GetExternalCalibrationLastDateAndTime']['day']
        # hour
        if self._defaults['GetExternalCalibrationLastDateAndTime']['hour'] is None:
            raise MockFunctionCallError("niRFSG_GetExternalCalibrationLastDateAndTime", param='hour')
        if hour is not None:
            hour.contents.value = self._defaults['GetExternalCalibrationLastDateAndTime']['hour']
        # minute
        if self._defaults['GetExternalCalibrationLastDateAndTime']['minute'] is None:
            raise MockFunctionCallError("niRFSG_GetExternalCalibrationLastDateAndTime", param='minute')
        if minute is not None:
            minute.contents.value = self._defaults['GetExternalCalibrationLastDateAndTime']['minute']
        # second
        if self._defaults['GetExternalCalibrationLastDateAndTime']['second'] is None:
            raise MockFunctionCallError("niRFSG_GetExternalCalibrationLastDateAndTime", param='second')
        if second is not None:
            second.contents.value = self._defaults['GetExternalCalibrationLastDateAndTime']['second']
        return self._defaults['GetExternalCalibrationLastDateAndTime']['return']

    def niRFSG_GetMaxSettablePower(self, vi, value):  # noqa: N802
        if self._defaults['GetMaxSettablePower']['return'] != 0:
            return self._defaults['GetMaxSettablePower']['return']
        # value
        if self._defaults['GetMaxSettablePower']['value'] is None:
            raise MockFunctionCallError("niRFSG_GetMaxSettablePower", param='value')
        if value is not None:
            value.contents.value = self._defaults['GetMaxSettablePower']['value']
        return self._defaults['GetMaxSettablePower']['return']

    def niRFSG_GetSelfCalibrationDateAndTime(self, vi, module, year, month, day, hour, minute, second):  # noqa: N802
        if self._defaults['GetSelfCalibrationDateAndTime']['return'] != 0:
            return self._defaults['GetSelfCalibrationDateAndTime']['return']
        # year
        if self._defaults['GetSelfCalibrationDateAndTime']['year'] is None:
            raise MockFunctionCallError("niRFSG_GetSelfCalibrationDateAndTime", param='year')
        if year is not None:
            year.contents.value = self._defaults['GetSelfCalibrationDateAndTime']['year']
        # month
        if self._defaults['GetSelfCalibrationDateAndTime']['month'] is None:
            raise MockFunctionCallError("niRFSG_GetSelfCalibrationDateAndTime", param='month')
        if month is not None:
            month.contents.value = self._defaults['GetSelfCalibrationDateAndTime']['month']
        # day
        if self._defaults['GetSelfCalibrationDateAndTime']['day'] is None:
            raise MockFunctionCallError("niRFSG_GetSelfCalibrationDateAndTime", param='day')
        if day is not None:
            day.contents.value = self._defaults['GetSelfCalibrationDateAndTime']['day']
        # hour
        if self._defaults['GetSelfCalibrationDateAndTime']['hour'] is None:
            raise MockFunctionCallError("niRFSG_GetSelfCalibrationDateAndTime", param='hour')
        if hour is not None:
            hour.contents.value = self._defaults['GetSelfCalibrationDateAndTime']['hour']
        # minute
        if self._defaults['GetSelfCalibrationDateAndTime']['minute'] is None:
            raise MockFunctionCallError("niRFSG_GetSelfCalibrationDateAndTime", param='minute')
        if minute is not None:
            minute.contents.value = self._defaults['GetSelfCalibrationDateAndTime']['minute']
        # second
        if self._defaults['GetSelfCalibrationDateAndTime']['second'] is None:
            raise MockFunctionCallError("niRFSG_GetSelfCalibrationDateAndTime", param='second')
        if second is not None:
            second.contents.value = self._defaults['GetSelfCalibrationDateAndTime']['second']
        return self._defaults['GetSelfCalibrationDateAndTime']['return']

    def niRFSG_GetSelfCalibrationTemperature(self, vi, module, temperature):  # noqa: N802
        if self._defaults['GetSelfCalibrationTemperature']['return'] != 0:
            return self._defaults['GetSelfCalibrationTemperature']['return']
        # temperature
        if self._defaults['GetSelfCalibrationTemperature']['temperature'] is None:
            raise MockFunctionCallError("niRFSG_GetSelfCalibrationTemperature", param='temperature')
        if temperature is not None:
            temperature.contents.value = self._defaults['GetSelfCalibrationTemperature']['temperature']
        return self._defaults['GetSelfCalibrationTemperature']['return']

    def niRFSG_GetStreamEndpointHandle(self, vi, stream_endpoint, reader_handle):  # noqa: N802
        if self._defaults['GetStreamEndpointHandle']['return'] != 0:
            return self._defaults['GetStreamEndpointHandle']['return']
        # reader_handle
        if self._defaults['GetStreamEndpointHandle']['readerHandle'] is None:
            raise MockFunctionCallError("niRFSG_GetStreamEndpointHandle", param='readerHandle')
        if reader_handle is not None:
            reader_handle.contents.value = self._defaults['GetStreamEndpointHandle']['readerHandle']
        return self._defaults['GetStreamEndpointHandle']['return']

    def niRFSG_GetTerminalName(self, vi, signal, signal_identifier, buffer_size, terminal_name):  # noqa: N802
        if self._defaults['GetTerminalName']['return'] != 0:
            return self._defaults['GetTerminalName']['return']
        return self._defaults['GetTerminalName']['return']

    def niRFSG_GetWaveformBurstStartLocations(self, vi, channel_name, number_of_locations, locations, required_size):  # noqa: N802
        if self._defaults['GetWaveformBurstStartLocations']['return'] != 0:
            return self._defaults['GetWaveformBurstStartLocations']['return']
        # locations
        if self._defaults['GetWaveformBurstStartLocations']['locations'] is None:
            raise MockFunctionCallError("niRFSG_GetWaveformBurstStartLocations", param='locations')
        if locations is not None:
            locations.contents.value = self._defaults['GetWaveformBurstStartLocations']['locations']
        # required_size
        if self._defaults['GetWaveformBurstStartLocations']['requiredSize'] is None:
            raise MockFunctionCallError("niRFSG_GetWaveformBurstStartLocations", param='requiredSize')
        if required_size is not None:
            required_size.contents.value = self._defaults['GetWaveformBurstStartLocations']['requiredSize']
        return self._defaults['GetWaveformBurstStartLocations']['return']

    def niRFSG_GetWaveformBurstStopLocations(self, vi, channel_name, number_of_locations, locations, required_size):  # noqa: N802
        if self._defaults['GetWaveformBurstStopLocations']['return'] != 0:
            return self._defaults['GetWaveformBurstStopLocations']['return']
        # locations
        if self._defaults['GetWaveformBurstStopLocations']['locations'] is None:
            raise MockFunctionCallError("niRFSG_GetWaveformBurstStopLocations", param='locations')
        if locations is not None:
            locations.contents.value = self._defaults['GetWaveformBurstStopLocations']['locations']
        # required_size
        if self._defaults['GetWaveformBurstStopLocations']['requiredSize'] is None:
            raise MockFunctionCallError("niRFSG_GetWaveformBurstStopLocations", param='requiredSize')
        if required_size is not None:
            required_size.contents.value = self._defaults['GetWaveformBurstStopLocations']['requiredSize']
        return self._defaults['GetWaveformBurstStopLocations']['return']

    def niRFSG_GetWaveformMarkerEventLocations(self, vi, channel_name, number_of_locations, locations, required_size):  # noqa: N802
        if self._defaults['GetWaveformMarkerEventLocations']['return'] != 0:
            return self._defaults['GetWaveformMarkerEventLocations']['return']
        # locations
        if self._defaults['GetWaveformMarkerEventLocations']['locations'] is None:
            raise MockFunctionCallError("niRFSG_GetWaveformMarkerEventLocations", param='locations')
        if locations is not None:
            locations.contents.value = self._defaults['GetWaveformMarkerEventLocations']['locations']
        # required_size
        if self._defaults['GetWaveformMarkerEventLocations']['requiredSize'] is None:
            raise MockFunctionCallError("niRFSG_GetWaveformMarkerEventLocations", param='requiredSize')
        if required_size is not None:
            required_size.contents.value = self._defaults['GetWaveformMarkerEventLocations']['requiredSize']
        return self._defaults['GetWaveformMarkerEventLocations']['return']

    def niRFSG_InitWithOptions(self, resource_name, id_query, reset_device, option_string, new_vi):  # noqa: N802
        if self._defaults['InitWithOptions']['return'] != 0:
            return self._defaults['InitWithOptions']['return']
        # new_vi
        if self._defaults['InitWithOptions']['newVi'] is None:
            raise MockFunctionCallError("niRFSG_InitWithOptions", param='newVi')
        if new_vi is not None:
            new_vi.contents.value = self._defaults['InitWithOptions']['newVi']
        return self._defaults['InitWithOptions']['return']

    def niRFSG_Initiate(self, vi):  # noqa: N802
        if self._defaults['Initiate']['return'] != 0:
            return self._defaults['Initiate']['return']
        return self._defaults['Initiate']['return']

    def niRFSG_LoadConfigurationsFromFile(self, vi, channel_name, file_path):  # noqa: N802
        if self._defaults['LoadConfigurationsFromFile']['return'] != 0:
            return self._defaults['LoadConfigurationsFromFile']['return']
        return self._defaults['LoadConfigurationsFromFile']['return']

    def niRFSG_LockSession(self, vi, caller_has_lock):  # noqa: N802
        if self._defaults['LockSession']['return'] != 0:
            return self._defaults['LockSession']['return']
        # caller_has_lock
        if self._defaults['LockSession']['callerHasLock'] is None:
            raise MockFunctionCallError("niRFSG_LockSession", param='callerHasLock')
        if caller_has_lock is not None:
            caller_has_lock.contents.value = self._defaults['LockSession']['callerHasLock']
        return self._defaults['LockSession']['return']

    def niRFSG_PerformPowerSearch(self, vi):  # noqa: N802
        if self._defaults['PerformPowerSearch']['return'] != 0:
            return self._defaults['PerformPowerSearch']['return']
        return self._defaults['PerformPowerSearch']['return']

    def niRFSG_PerformThermalCorrection(self, vi):  # noqa: N802
        if self._defaults['PerformThermalCorrection']['return'] != 0:
            return self._defaults['PerformThermalCorrection']['return']
        return self._defaults['PerformThermalCorrection']['return']

    def niRFSG_QueryArbWaveformCapabilities(self, vi, max_number_waveforms, waveform_quantum, min_waveform_size, max_waveform_size):  # noqa: N802
        if self._defaults['QueryArbWaveformCapabilities']['return'] != 0:
            return self._defaults['QueryArbWaveformCapabilities']['return']
        # max_number_waveforms
        if self._defaults['QueryArbWaveformCapabilities']['maxNumberWaveforms'] is None:
            raise MockFunctionCallError("niRFSG_QueryArbWaveformCapabilities", param='maxNumberWaveforms')
        if max_number_waveforms is not None:
            max_number_waveforms.contents.value = self._defaults['QueryArbWaveformCapabilities']['maxNumberWaveforms']
        # waveform_quantum
        if self._defaults['QueryArbWaveformCapabilities']['waveformQuantum'] is None:
            raise MockFunctionCallError("niRFSG_QueryArbWaveformCapabilities", param='waveformQuantum')
        if waveform_quantum is not None:
            waveform_quantum.contents.value = self._defaults['QueryArbWaveformCapabilities']['waveformQuantum']
        # min_waveform_size
        if self._defaults['QueryArbWaveformCapabilities']['minWaveformSize'] is None:
            raise MockFunctionCallError("niRFSG_QueryArbWaveformCapabilities", param='minWaveformSize')
        if min_waveform_size is not None:
            min_waveform_size.contents.value = self._defaults['QueryArbWaveformCapabilities']['minWaveformSize']
        # max_waveform_size
        if self._defaults['QueryArbWaveformCapabilities']['maxWaveformSize'] is None:
            raise MockFunctionCallError("niRFSG_QueryArbWaveformCapabilities", param='maxWaveformSize')
        if max_waveform_size is not None:
            max_waveform_size.contents.value = self._defaults['QueryArbWaveformCapabilities']['maxWaveformSize']
        return self._defaults['QueryArbWaveformCapabilities']['return']

    def niRFSG_ReadAndDownloadWaveformFromFileTDMS(self, vi, waveform_name, file_path, waveform_index):  # noqa: N802
        if self._defaults['ReadAndDownloadWaveformFromFileTDMS']['return'] != 0:
            return self._defaults['ReadAndDownloadWaveformFromFileTDMS']['return']
        return self._defaults['ReadAndDownloadWaveformFromFileTDMS']['return']

    def niRFSG_Reset(self, vi):  # noqa: N802
        if self._defaults['Reset']['return'] != 0:
            return self._defaults['Reset']['return']
        return self._defaults['Reset']['return']

    def niRFSG_ResetAttribute(self, vi, channel_name, attribute_id):  # noqa: N802
        if self._defaults['ResetAttribute']['return'] != 0:
            return self._defaults['ResetAttribute']['return']
        return self._defaults['ResetAttribute']['return']

    def niRFSG_ResetDevice(self, vi):  # noqa: N802
        if self._defaults['ResetDevice']['return'] != 0:
            return self._defaults['ResetDevice']['return']
        return self._defaults['ResetDevice']['return']

    def niRFSG_ResetWithDefaults(self, vi):  # noqa: N802
        if self._defaults['ResetWithDefaults']['return'] != 0:
            return self._defaults['ResetWithDefaults']['return']
        return self._defaults['ResetWithDefaults']['return']

    def niRFSG_ResetWithOptions(self, vi, steps_to_omit):  # noqa: N802
        if self._defaults['ResetWithOptions']['return'] != 0:
            return self._defaults['ResetWithOptions']['return']
        return self._defaults['ResetWithOptions']['return']

    def niRFSG_RevisionQuery(self, vi, instrument_driver_revision, firmware_revision):  # noqa: N802
        if self._defaults['RevisionQuery']['return'] != 0:
            return self._defaults['RevisionQuery']['return']
        return self._defaults['RevisionQuery']['return']

    def niRFSG_SaveConfigurationsToFile(self, vi, channel_name, file_path):  # noqa: N802
        if self._defaults['SaveConfigurationsToFile']['return'] != 0:
            return self._defaults['SaveConfigurationsToFile']['return']
        return self._defaults['SaveConfigurationsToFile']['return']

    def niRFSG_SelectArbWaveform(self, vi, name):  # noqa: N802
        if self._defaults['SelectArbWaveform']['return'] != 0:
            return self._defaults['SelectArbWaveform']['return']
        return self._defaults['SelectArbWaveform']['return']

    def niRFSG_SelfCal(self, vi):  # noqa: N802
        if self._defaults['SelfCal']['return'] != 0:
            return self._defaults['SelfCal']['return']
        return self._defaults['SelfCal']['return']

    def niRFSG_SelfCalibrateRange(self, vi, steps_to_omit, min_frequency, max_frequency, min_power_level, max_power_level):  # noqa: N802
        if self._defaults['SelfCalibrateRange']['return'] != 0:
            return self._defaults['SelfCalibrateRange']['return']
        return self._defaults['SelfCalibrateRange']['return']

    def niRFSG_SelfTest(self, vi, self_test_result, self_test_message):  # noqa: N802
        if self._defaults['SelfTest']['return'] != 0:
            return self._defaults['SelfTest']['return']
        # self_test_result
        if self._defaults['SelfTest']['selfTestResult'] is None:
            raise MockFunctionCallError("niRFSG_SelfTest", param='selfTestResult')
        if self_test_result is not None:
            self_test_result.contents.value = self._defaults['SelfTest']['selfTestResult']
        return self._defaults['SelfTest']['return']

    def niRFSG_SendSoftwareEdgeTrigger(self, vi, trigger, trigger_identifier):  # noqa: N802
        if self._defaults['SendSoftwareEdgeTrigger']['return'] != 0:
            return self._defaults['SendSoftwareEdgeTrigger']['return']
        return self._defaults['SendSoftwareEdgeTrigger']['return']

    def niRFSG_SetArbWaveformNextWritePosition(self, vi, waveform_name, relative_to, offset):  # noqa: N802
        if self._defaults['SetArbWaveformNextWritePosition']['return'] != 0:
            return self._defaults['SetArbWaveformNextWritePosition']['return']
        return self._defaults['SetArbWaveformNextWritePosition']['return']

    def niRFSG_SetAttributeViBoolean(self, vi, channel_name, attribute, value):  # noqa: N802
        if self._defaults['SetAttributeViBoolean']['return'] != 0:
            return self._defaults['SetAttributeViBoolean']['return']
        return self._defaults['SetAttributeViBoolean']['return']

    def niRFSG_SetAttributeViInt32(self, vi, channel_name, attribute, value):  # noqa: N802
        if self._defaults['SetAttributeViInt32']['return'] != 0:
            return self._defaults['SetAttributeViInt32']['return']
        return self._defaults['SetAttributeViInt32']['return']

    def niRFSG_SetAttributeViInt64(self, vi, channel_name, attribute, value):  # noqa: N802
        if self._defaults['SetAttributeViInt64']['return'] != 0:
            return self._defaults['SetAttributeViInt64']['return']
        return self._defaults['SetAttributeViInt64']['return']

    def niRFSG_SetAttributeViReal64(self, vi, channel_name, attribute, value):  # noqa: N802
        if self._defaults['SetAttributeViReal64']['return'] != 0:
            return self._defaults['SetAttributeViReal64']['return']
        return self._defaults['SetAttributeViReal64']['return']

    def niRFSG_SetAttributeViSession(self, vi, channel_name, attribute, value):  # noqa: N802
        if self._defaults['SetAttributeViSession']['return'] != 0:
            return self._defaults['SetAttributeViSession']['return']
        return self._defaults['SetAttributeViSession']['return']

    def niRFSG_SetAttributeViString(self, vi, channel_name, attribute, value):  # noqa: N802
        if self._defaults['SetAttributeViString']['return'] != 0:
            return self._defaults['SetAttributeViString']['return']
        return self._defaults['SetAttributeViString']['return']

    def niRFSG_SetWaveformBurstStartLocations(self, vi, channel_name, number_of_locations, locations):  # noqa: N802
        if self._defaults['SetWaveformBurstStartLocations']['return'] != 0:
            return self._defaults['SetWaveformBurstStartLocations']['return']
        # locations
        if self._defaults['SetWaveformBurstStartLocations']['locations'] is None:
            raise MockFunctionCallError("niRFSG_SetWaveformBurstStartLocations", param='locations')
        if locations is not None:
            locations.contents.value = self._defaults['SetWaveformBurstStartLocations']['locations']
        return self._defaults['SetWaveformBurstStartLocations']['return']

    def niRFSG_SetWaveformBurstStopLocations(self, vi, channel_name, number_of_locations, locations):  # noqa: N802
        if self._defaults['SetWaveformBurstStopLocations']['return'] != 0:
            return self._defaults['SetWaveformBurstStopLocations']['return']
        # locations
        if self._defaults['SetWaveformBurstStopLocations']['locations'] is None:
            raise MockFunctionCallError("niRFSG_SetWaveformBurstStopLocations", param='locations')
        if locations is not None:
            locations.contents.value = self._defaults['SetWaveformBurstStopLocations']['locations']
        return self._defaults['SetWaveformBurstStopLocations']['return']

    def niRFSG_SetWaveformMarkerEventLocations(self, vi, channel_name, number_of_locations, locations):  # noqa: N802
        if self._defaults['SetWaveformMarkerEventLocations']['return'] != 0:
            return self._defaults['SetWaveformMarkerEventLocations']['return']
        # locations
        if self._defaults['SetWaveformMarkerEventLocations']['locations'] is None:
            raise MockFunctionCallError("niRFSG_SetWaveformMarkerEventLocations", param='locations')
        if locations is not None:
            locations.contents.value = self._defaults['SetWaveformMarkerEventLocations']['locations']
        return self._defaults['SetWaveformMarkerEventLocations']['return']

    def niRFSG_UnlockSession(self, vi, caller_has_lock):  # noqa: N802
        if self._defaults['UnlockSession']['return'] != 0:
            return self._defaults['UnlockSession']['return']
        # caller_has_lock
        if self._defaults['UnlockSession']['callerHasLock'] is None:
            raise MockFunctionCallError("niRFSG_UnlockSession", param='callerHasLock')
        if caller_has_lock is not None:
            caller_has_lock.contents.value = self._defaults['UnlockSession']['callerHasLock']
        return self._defaults['UnlockSession']['return']

    def niRFSG_WaitUntilSettled(self, vi, max_time_milliseconds):  # noqa: N802
        if self._defaults['WaitUntilSettled']['return'] != 0:
            return self._defaults['WaitUntilSettled']['return']
        return self._defaults['WaitUntilSettled']['return']

    def niRFSG_WriteArbWaveform(self, vi, waveform_name, number_of_samples, i_data, q_data, more_data_pending):  # noqa: N802
        if self._defaults['WriteArbWaveform']['return'] != 0:
            return self._defaults['WriteArbWaveform']['return']
        return self._defaults['WriteArbWaveform']['return']

    def niRFSG_WriteArbWaveformF32(self, vi, waveform_name, number_of_samples, i_data, q_data, more_data_pending):  # noqa: N802
        if self._defaults['WriteArbWaveformF32']['return'] != 0:
            return self._defaults['WriteArbWaveformF32']['return']
        return self._defaults['WriteArbWaveformF32']['return']

    def niRFSG_WriteP2PEndpointI16(self, vi, stream_endpoint, number_of_samples, endpoint_data):  # noqa: N802
        if self._defaults['WriteP2PEndpointI16']['return'] != 0:
            return self._defaults['WriteP2PEndpointI16']['return']
        return self._defaults['WriteP2PEndpointI16']['return']

    def niRFSG_WriteScript(self, vi, script):  # noqa: N802
        if self._defaults['WriteScript']['return'] != 0:
            return self._defaults['WriteScript']['return']
        return self._defaults['WriteScript']['return']

    def niRFSG_close(self, vi):  # noqa: N802
        if self._defaults['close']['return'] != 0:
            return self._defaults['close']['return']
        return self._defaults['close']['return']

    # Helper function to setup Mock object with default side effects and return values
    def set_side_effects_and_return_values(self, mock_library):
        mock_library.niRFSG_Abort.side_effect = MockFunctionCallError("niRFSG_Abort")
        mock_library.niRFSG_Abort.return_value = 0
        mock_library.niRFSG_AllocateArbWaveform.side_effect = MockFunctionCallError("niRFSG_AllocateArbWaveform")
        mock_library.niRFSG_AllocateArbWaveform.return_value = 0
        mock_library.niRFSG_ChangeExternalCalibrationPassword.side_effect = MockFunctionCallError("niRFSG_ChangeExternalCalibrationPassword")
        mock_library.niRFSG_ChangeExternalCalibrationPassword.return_value = 0
        mock_library.niRFSG_CheckAttributeViBoolean.side_effect = MockFunctionCallError("niRFSG_CheckAttributeViBoolean")
        mock_library.niRFSG_CheckAttributeViBoolean.return_value = 0
        mock_library.niRFSG_CheckAttributeViInt32.side_effect = MockFunctionCallError("niRFSG_CheckAttributeViInt32")
        mock_library.niRFSG_CheckAttributeViInt32.return_value = 0
        mock_library.niRFSG_CheckAttributeViInt64.side_effect = MockFunctionCallError("niRFSG_CheckAttributeViInt64")
        mock_library.niRFSG_CheckAttributeViInt64.return_value = 0
        mock_library.niRFSG_CheckAttributeViReal64.side_effect = MockFunctionCallError("niRFSG_CheckAttributeViReal64")
        mock_library.niRFSG_CheckAttributeViReal64.return_value = 0
        mock_library.niRFSG_CheckAttributeViSession.side_effect = MockFunctionCallError("niRFSG_CheckAttributeViSession")
        mock_library.niRFSG_CheckAttributeViSession.return_value = 0
        mock_library.niRFSG_CheckAttributeViString.side_effect = MockFunctionCallError("niRFSG_CheckAttributeViString")
        mock_library.niRFSG_CheckAttributeViString.return_value = 0
        mock_library.niRFSG_CheckGenerationStatus.side_effect = MockFunctionCallError("niRFSG_CheckGenerationStatus")
        mock_library.niRFSG_CheckGenerationStatus.return_value = 0
        mock_library.niRFSG_CheckIfConfigurationListExists.side_effect = MockFunctionCallError("niRFSG_CheckIfConfigurationListExists")
        mock_library.niRFSG_CheckIfConfigurationListExists.return_value = 0
        mock_library.niRFSG_CheckIfScriptExists.side_effect = MockFunctionCallError("niRFSG_CheckIfScriptExists")
        mock_library.niRFSG_CheckIfScriptExists.return_value = 0
        mock_library.niRFSG_CheckIfWaveformExists.side_effect = MockFunctionCallError("niRFSG_CheckIfWaveformExists")
        mock_library.niRFSG_CheckIfWaveformExists.return_value = 0
        mock_library.niRFSG_ClearAllArbWaveforms.side_effect = MockFunctionCallError("niRFSG_ClearAllArbWaveforms")
        mock_library.niRFSG_ClearAllArbWaveforms.return_value = 0
        mock_library.niRFSG_ClearArbWaveform.side_effect = MockFunctionCallError("niRFSG_ClearArbWaveform")
        mock_library.niRFSG_ClearArbWaveform.return_value = 0
        mock_library.niRFSG_ClearError.side_effect = MockFunctionCallError("niRFSG_ClearError")
        mock_library.niRFSG_ClearError.return_value = 0
        mock_library.niRFSG_ClearSelfCalibrateRange.side_effect = MockFunctionCallError("niRFSG_ClearSelfCalibrateRange")
        mock_library.niRFSG_ClearSelfCalibrateRange.return_value = 0
        mock_library.niRFSG_Commit.side_effect = MockFunctionCallError("niRFSG_Commit")
        mock_library.niRFSG_Commit.return_value = 0
        mock_library.niRFSG_ConfigureDeembeddingTableInterpolationLinear.side_effect = MockFunctionCallError("niRFSG_ConfigureDeembeddingTableInterpolationLinear")
        mock_library.niRFSG_ConfigureDeembeddingTableInterpolationLinear.return_value = 0
        mock_library.niRFSG_ConfigureDeembeddingTableInterpolationNearest.side_effect = MockFunctionCallError("niRFSG_ConfigureDeembeddingTableInterpolationNearest")
        mock_library.niRFSG_ConfigureDeembeddingTableInterpolationNearest.return_value = 0
        mock_library.niRFSG_ConfigureDeembeddingTableInterpolationSpline.side_effect = MockFunctionCallError("niRFSG_ConfigureDeembeddingTableInterpolationSpline")
        mock_library.niRFSG_ConfigureDeembeddingTableInterpolationSpline.return_value = 0
        mock_library.niRFSG_ConfigureDigitalEdgeConfigurationListStepTrigger.side_effect = MockFunctionCallError("niRFSG_ConfigureDigitalEdgeConfigurationListStepTrigger")
        mock_library.niRFSG_ConfigureDigitalEdgeConfigurationListStepTrigger.return_value = 0
        mock_library.niRFSG_ConfigureDigitalEdgeScriptTrigger.side_effect = MockFunctionCallError("niRFSG_ConfigureDigitalEdgeScriptTrigger")
        mock_library.niRFSG_ConfigureDigitalEdgeScriptTrigger.return_value = 0
        mock_library.niRFSG_ConfigureDigitalEdgeStartTrigger.side_effect = MockFunctionCallError("niRFSG_ConfigureDigitalEdgeStartTrigger")
        mock_library.niRFSG_ConfigureDigitalEdgeStartTrigger.return_value = 0
        mock_library.niRFSG_ConfigureDigitalLevelScriptTrigger.side_effect = MockFunctionCallError("niRFSG_ConfigureDigitalLevelScriptTrigger")
        mock_library.niRFSG_ConfigureDigitalLevelScriptTrigger.return_value = 0
        mock_library.niRFSG_ConfigureDigitalModulationUserDefinedWaveform.side_effect = MockFunctionCallError("niRFSG_ConfigureDigitalModulationUserDefinedWaveform")
        mock_library.niRFSG_ConfigureDigitalModulationUserDefinedWaveform.return_value = 0
        mock_library.niRFSG_ConfigureGenerationMode.side_effect = MockFunctionCallError("niRFSG_ConfigureGenerationMode")
        mock_library.niRFSG_ConfigureGenerationMode.return_value = 0
        mock_library.niRFSG_ConfigureOutputEnabled.side_effect = MockFunctionCallError("niRFSG_ConfigureOutputEnabled")
        mock_library.niRFSG_ConfigureOutputEnabled.return_value = 0
        mock_library.niRFSG_ConfigureP2PEndpointFullnessStartTrigger.side_effect = MockFunctionCallError("niRFSG_ConfigureP2PEndpointFullnessStartTrigger")
        mock_library.niRFSG_ConfigureP2PEndpointFullnessStartTrigger.return_value = 0
        mock_library.niRFSG_ConfigurePowerLevelType.side_effect = MockFunctionCallError("niRFSG_ConfigurePowerLevelType")
        mock_library.niRFSG_ConfigurePowerLevelType.return_value = 0
        mock_library.niRFSG_ConfigurePxiChassisClk10.side_effect = MockFunctionCallError("niRFSG_ConfigurePxiChassisClk10")
        mock_library.niRFSG_ConfigurePxiChassisClk10.return_value = 0
        mock_library.niRFSG_ConfigureRF.side_effect = MockFunctionCallError("niRFSG_ConfigureRF")
        mock_library.niRFSG_ConfigureRF.return_value = 0
        mock_library.niRFSG_ConfigureRefClock.side_effect = MockFunctionCallError("niRFSG_ConfigureRefClock")
        mock_library.niRFSG_ConfigureRefClock.return_value = 0
        mock_library.niRFSG_ConfigureSignalBandwidth.side_effect = MockFunctionCallError("niRFSG_ConfigureSignalBandwidth")
        mock_library.niRFSG_ConfigureSignalBandwidth.return_value = 0
        mock_library.niRFSG_ConfigureSoftwareScriptTrigger.side_effect = MockFunctionCallError("niRFSG_ConfigureSoftwareScriptTrigger")
        mock_library.niRFSG_ConfigureSoftwareScriptTrigger.return_value = 0
        mock_library.niRFSG_ConfigureSoftwareStartTrigger.side_effect = MockFunctionCallError("niRFSG_ConfigureSoftwareStartTrigger")
        mock_library.niRFSG_ConfigureSoftwareStartTrigger.return_value = 0
        mock_library.niRFSG_CreateConfigurationList.side_effect = MockFunctionCallError("niRFSG_CreateConfigurationList")
        mock_library.niRFSG_CreateConfigurationList.return_value = 0
        mock_library.niRFSG_CreateConfigurationListStep.side_effect = MockFunctionCallError("niRFSG_CreateConfigurationListStep")
        mock_library.niRFSG_CreateConfigurationListStep.return_value = 0
        mock_library.niRFSG_CreateDeembeddingSparameterTableS2PFile.side_effect = MockFunctionCallError("niRFSG_CreateDeembeddingSparameterTableS2PFile")
        mock_library.niRFSG_CreateDeembeddingSparameterTableS2PFile.return_value = 0
        mock_library.niRFSG_DeleteAllDeembeddingTables.side_effect = MockFunctionCallError("niRFSG_DeleteAllDeembeddingTables")
        mock_library.niRFSG_DeleteAllDeembeddingTables.return_value = 0
        mock_library.niRFSG_DeleteConfigurationList.side_effect = MockFunctionCallError("niRFSG_DeleteConfigurationList")
        mock_library.niRFSG_DeleteConfigurationList.return_value = 0
        mock_library.niRFSG_DeleteDeembeddingTable.side_effect = MockFunctionCallError("niRFSG_DeleteDeembeddingTable")
        mock_library.niRFSG_DeleteDeembeddingTable.return_value = 0
        mock_library.niRFSG_Disable.side_effect = MockFunctionCallError("niRFSG_Disable")
        mock_library.niRFSG_Disable.return_value = 0
        mock_library.niRFSG_DisableConfigurationListStepTrigger.side_effect = MockFunctionCallError("niRFSG_DisableConfigurationListStepTrigger")
        mock_library.niRFSG_DisableConfigurationListStepTrigger.return_value = 0
        mock_library.niRFSG_DisableScriptTrigger.side_effect = MockFunctionCallError("niRFSG_DisableScriptTrigger")
        mock_library.niRFSG_DisableScriptTrigger.return_value = 0
        mock_library.niRFSG_DisableStartTrigger.side_effect = MockFunctionCallError("niRFSG_DisableStartTrigger")
        mock_library.niRFSG_DisableStartTrigger.return_value = 0
        mock_library.niRFSG_ErrorMessage.side_effect = MockFunctionCallError("niRFSG_ErrorMessage")
        mock_library.niRFSG_ErrorMessage.return_value = 0
        mock_library.niRFSG_ErrorQuery.side_effect = MockFunctionCallError("niRFSG_ErrorQuery")
        mock_library.niRFSG_ErrorQuery.return_value = 0
        mock_library.niRFSG_ExportSignal.side_effect = MockFunctionCallError("niRFSG_ExportSignal")
        mock_library.niRFSG_ExportSignal.return_value = 0
        mock_library.niRFSG_GetAllNamedWaveformNames.side_effect = MockFunctionCallError("niRFSG_GetAllNamedWaveformNames")
        mock_library.niRFSG_GetAllNamedWaveformNames.return_value = 0
        mock_library.niRFSG_GetAllScriptNames.side_effect = MockFunctionCallError("niRFSG_GetAllScriptNames")
        mock_library.niRFSG_GetAllScriptNames.return_value = 0
        mock_library.niRFSG_GetAttributeViBoolean.side_effect = MockFunctionCallError("niRFSG_GetAttributeViBoolean")
        mock_library.niRFSG_GetAttributeViBoolean.return_value = 0
        mock_library.niRFSG_GetAttributeViInt32.side_effect = MockFunctionCallError("niRFSG_GetAttributeViInt32")
        mock_library.niRFSG_GetAttributeViInt32.return_value = 0
        mock_library.niRFSG_GetAttributeViInt64.side_effect = MockFunctionCallError("niRFSG_GetAttributeViInt64")
        mock_library.niRFSG_GetAttributeViInt64.return_value = 0
        mock_library.niRFSG_GetAttributeViReal64.side_effect = MockFunctionCallError("niRFSG_GetAttributeViReal64")
        mock_library.niRFSG_GetAttributeViReal64.return_value = 0
        mock_library.niRFSG_GetAttributeViSession.side_effect = MockFunctionCallError("niRFSG_GetAttributeViSession")
        mock_library.niRFSG_GetAttributeViSession.return_value = 0
        mock_library.niRFSG_GetAttributeViString.side_effect = MockFunctionCallError("niRFSG_GetAttributeViString")
        mock_library.niRFSG_GetAttributeViString.return_value = 0
        mock_library.niRFSG_GetChannelName.side_effect = MockFunctionCallError("niRFSG_GetChannelName")
        mock_library.niRFSG_GetChannelName.return_value = 0
        mock_library.niRFSG_GetDeembeddingSparameters.side_effect = MockFunctionCallError("niRFSG_GetDeembeddingSparameters")
        mock_library.niRFSG_GetDeembeddingSparameters.return_value = 0
        mock_library.niRFSG_GetError.side_effect = MockFunctionCallError("niRFSG_GetError")
        mock_library.niRFSG_GetError.return_value = 0
        mock_library.niRFSG_GetExternalCalibrationLastDateAndTime.side_effect = MockFunctionCallError("niRFSG_GetExternalCalibrationLastDateAndTime")
        mock_library.niRFSG_GetExternalCalibrationLastDateAndTime.return_value = 0
        mock_library.niRFSG_GetMaxSettablePower.side_effect = MockFunctionCallError("niRFSG_GetMaxSettablePower")
        mock_library.niRFSG_GetMaxSettablePower.return_value = 0
        mock_library.niRFSG_GetSelfCalibrationDateAndTime.side_effect = MockFunctionCallError("niRFSG_GetSelfCalibrationDateAndTime")
        mock_library.niRFSG_GetSelfCalibrationDateAndTime.return_value = 0
        mock_library.niRFSG_GetSelfCalibrationTemperature.side_effect = MockFunctionCallError("niRFSG_GetSelfCalibrationTemperature")
        mock_library.niRFSG_GetSelfCalibrationTemperature.return_value = 0
        mock_library.niRFSG_GetStreamEndpointHandle.side_effect = MockFunctionCallError("niRFSG_GetStreamEndpointHandle")
        mock_library.niRFSG_GetStreamEndpointHandle.return_value = 0
        mock_library.niRFSG_GetTerminalName.side_effect = MockFunctionCallError("niRFSG_GetTerminalName")
        mock_library.niRFSG_GetTerminalName.return_value = 0
        mock_library.niRFSG_GetWaveformBurstStartLocations.side_effect = MockFunctionCallError("niRFSG_GetWaveformBurstStartLocations")
        mock_library.niRFSG_GetWaveformBurstStartLocations.return_value = 0
        mock_library.niRFSG_GetWaveformBurstStopLocations.side_effect = MockFunctionCallError("niRFSG_GetWaveformBurstStopLocations")
        mock_library.niRFSG_GetWaveformBurstStopLocations.return_value = 0
        mock_library.niRFSG_GetWaveformMarkerEventLocations.side_effect = MockFunctionCallError("niRFSG_GetWaveformMarkerEventLocations")
        mock_library.niRFSG_GetWaveformMarkerEventLocations.return_value = 0
        mock_library.niRFSG_InitWithOptions.side_effect = MockFunctionCallError("niRFSG_InitWithOptions")
        mock_library.niRFSG_InitWithOptions.return_value = 0
        mock_library.niRFSG_Initiate.side_effect = MockFunctionCallError("niRFSG_Initiate")
        mock_library.niRFSG_Initiate.return_value = 0
        mock_library.niRFSG_LoadConfigurationsFromFile.side_effect = MockFunctionCallError("niRFSG_LoadConfigurationsFromFile")
        mock_library.niRFSG_LoadConfigurationsFromFile.return_value = 0
        mock_library.niRFSG_LockSession.side_effect = MockFunctionCallError("niRFSG_LockSession")
        mock_library.niRFSG_LockSession.return_value = 0
        mock_library.niRFSG_PerformPowerSearch.side_effect = MockFunctionCallError("niRFSG_PerformPowerSearch")
        mock_library.niRFSG_PerformPowerSearch.return_value = 0
        mock_library.niRFSG_PerformThermalCorrection.side_effect = MockFunctionCallError("niRFSG_PerformThermalCorrection")
        mock_library.niRFSG_PerformThermalCorrection.return_value = 0
        mock_library.niRFSG_QueryArbWaveformCapabilities.side_effect = MockFunctionCallError("niRFSG_QueryArbWaveformCapabilities")
        mock_library.niRFSG_QueryArbWaveformCapabilities.return_value = 0
        mock_library.niRFSG_ReadAndDownloadWaveformFromFileTDMS.side_effect = MockFunctionCallError("niRFSG_ReadAndDownloadWaveformFromFileTDMS")
        mock_library.niRFSG_ReadAndDownloadWaveformFromFileTDMS.return_value = 0
        mock_library.niRFSG_Reset.side_effect = MockFunctionCallError("niRFSG_Reset")
        mock_library.niRFSG_Reset.return_value = 0
        mock_library.niRFSG_ResetAttribute.side_effect = MockFunctionCallError("niRFSG_ResetAttribute")
        mock_library.niRFSG_ResetAttribute.return_value = 0
        mock_library.niRFSG_ResetDevice.side_effect = MockFunctionCallError("niRFSG_ResetDevice")
        mock_library.niRFSG_ResetDevice.return_value = 0
        mock_library.niRFSG_ResetWithDefaults.side_effect = MockFunctionCallError("niRFSG_ResetWithDefaults")
        mock_library.niRFSG_ResetWithDefaults.return_value = 0
        mock_library.niRFSG_ResetWithOptions.side_effect = MockFunctionCallError("niRFSG_ResetWithOptions")
        mock_library.niRFSG_ResetWithOptions.return_value = 0
        mock_library.niRFSG_RevisionQuery.side_effect = MockFunctionCallError("niRFSG_RevisionQuery")
        mock_library.niRFSG_RevisionQuery.return_value = 0
        mock_library.niRFSG_SaveConfigurationsToFile.side_effect = MockFunctionCallError("niRFSG_SaveConfigurationsToFile")
        mock_library.niRFSG_SaveConfigurationsToFile.return_value = 0
        mock_library.niRFSG_SelectArbWaveform.side_effect = MockFunctionCallError("niRFSG_SelectArbWaveform")
        mock_library.niRFSG_SelectArbWaveform.return_value = 0
        mock_library.niRFSG_SelfCal.side_effect = MockFunctionCallError("niRFSG_SelfCal")
        mock_library.niRFSG_SelfCal.return_value = 0
        mock_library.niRFSG_SelfCalibrateRange.side_effect = MockFunctionCallError("niRFSG_SelfCalibrateRange")
        mock_library.niRFSG_SelfCalibrateRange.return_value = 0
        mock_library.niRFSG_SelfTest.side_effect = MockFunctionCallError("niRFSG_SelfTest")
        mock_library.niRFSG_SelfTest.return_value = 0
        mock_library.niRFSG_SendSoftwareEdgeTrigger.side_effect = MockFunctionCallError("niRFSG_SendSoftwareEdgeTrigger")
        mock_library.niRFSG_SendSoftwareEdgeTrigger.return_value = 0
        mock_library.niRFSG_SetArbWaveformNextWritePosition.side_effect = MockFunctionCallError("niRFSG_SetArbWaveformNextWritePosition")
        mock_library.niRFSG_SetArbWaveformNextWritePosition.return_value = 0
        mock_library.niRFSG_SetAttributeViBoolean.side_effect = MockFunctionCallError("niRFSG_SetAttributeViBoolean")
        mock_library.niRFSG_SetAttributeViBoolean.return_value = 0
        mock_library.niRFSG_SetAttributeViInt32.side_effect = MockFunctionCallError("niRFSG_SetAttributeViInt32")
        mock_library.niRFSG_SetAttributeViInt32.return_value = 0
        mock_library.niRFSG_SetAttributeViInt64.side_effect = MockFunctionCallError("niRFSG_SetAttributeViInt64")
        mock_library.niRFSG_SetAttributeViInt64.return_value = 0
        mock_library.niRFSG_SetAttributeViReal64.side_effect = MockFunctionCallError("niRFSG_SetAttributeViReal64")
        mock_library.niRFSG_SetAttributeViReal64.return_value = 0
        mock_library.niRFSG_SetAttributeViSession.side_effect = MockFunctionCallError("niRFSG_SetAttributeViSession")
        mock_library.niRFSG_SetAttributeViSession.return_value = 0
        mock_library.niRFSG_SetAttributeViString.side_effect = MockFunctionCallError("niRFSG_SetAttributeViString")
        mock_library.niRFSG_SetAttributeViString.return_value = 0
        mock_library.niRFSG_SetWaveformBurstStartLocations.side_effect = MockFunctionCallError("niRFSG_SetWaveformBurstStartLocations")
        mock_library.niRFSG_SetWaveformBurstStartLocations.return_value = 0
        mock_library.niRFSG_SetWaveformBurstStopLocations.side_effect = MockFunctionCallError("niRFSG_SetWaveformBurstStopLocations")
        mock_library.niRFSG_SetWaveformBurstStopLocations.return_value = 0
        mock_library.niRFSG_SetWaveformMarkerEventLocations.side_effect = MockFunctionCallError("niRFSG_SetWaveformMarkerEventLocations")
        mock_library.niRFSG_SetWaveformMarkerEventLocations.return_value = 0
        mock_library.niRFSG_UnlockSession.side_effect = MockFunctionCallError("niRFSG_UnlockSession")
        mock_library.niRFSG_UnlockSession.return_value = 0
        mock_library.niRFSG_WaitUntilSettled.side_effect = MockFunctionCallError("niRFSG_WaitUntilSettled")
        mock_library.niRFSG_WaitUntilSettled.return_value = 0
        mock_library.niRFSG_WriteArbWaveform.side_effect = MockFunctionCallError("niRFSG_WriteArbWaveform")
        mock_library.niRFSG_WriteArbWaveform.return_value = 0
        mock_library.niRFSG_WriteArbWaveformF32.side_effect = MockFunctionCallError("niRFSG_WriteArbWaveformF32")
        mock_library.niRFSG_WriteArbWaveformF32.return_value = 0
        mock_library.niRFSG_WriteP2PEndpointI16.side_effect = MockFunctionCallError("niRFSG_WriteP2PEndpointI16")
        mock_library.niRFSG_WriteP2PEndpointI16.return_value = 0
        mock_library.niRFSG_WriteScript.side_effect = MockFunctionCallError("niRFSG_WriteScript")
        mock_library.niRFSG_WriteScript.return_value = 0
        mock_library.niRFSG_close.side_effect = MockFunctionCallError("niRFSG_close")
        mock_library.niRFSG_close.return_value = 0
