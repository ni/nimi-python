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
        self._defaults['ChangeExternalCalibrationPassword'] = {}
        self._defaults['ChangeExternalCalibrationPassword']['return'] = 0
        self._defaults['CheckAcquisitionStatus'] = {}
        self._defaults['CheckAcquisitionStatus']['return'] = 0
        self._defaults['CheckAcquisitionStatus']['isDone'] = None
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
        self._defaults['ConfigureDigitalEdgeAdvanceTrigger'] = {}
        self._defaults['ConfigureDigitalEdgeAdvanceTrigger']['return'] = 0
        self._defaults['ConfigureDigitalEdgeRefTrigger'] = {}
        self._defaults['ConfigureDigitalEdgeRefTrigger']['return'] = 0
        self._defaults['ConfigureDigitalEdgeStartTrigger'] = {}
        self._defaults['ConfigureDigitalEdgeStartTrigger']['return'] = 0
        self._defaults['ConfigureIQPowerEdgeRefTrigger'] = {}
        self._defaults['ConfigureIQPowerEdgeRefTrigger']['return'] = 0
        self._defaults['ConfigureRefClock'] = {}
        self._defaults['ConfigureRefClock']['return'] = 0
        self._defaults['ConfigureSoftwareEdgeAdvanceTrigger'] = {}
        self._defaults['ConfigureSoftwareEdgeAdvanceTrigger']['return'] = 0
        self._defaults['ConfigureSoftwareEdgeRefTrigger'] = {}
        self._defaults['ConfigureSoftwareEdgeRefTrigger']['return'] = 0
        self._defaults['ConfigureSoftwareEdgeStartTrigger'] = {}
        self._defaults['ConfigureSoftwareEdgeStartTrigger']['return'] = 0
        self._defaults['ConfigureSpectrumFrequencyCenterSpan'] = {}
        self._defaults['ConfigureSpectrumFrequencyCenterSpan']['return'] = 0
        self._defaults['ConfigureSpectrumFrequencyStartStop'] = {}
        self._defaults['ConfigureSpectrumFrequencyStartStop']['return'] = 0
        self._defaults['CreateDeembeddingSparameterTableArray'] = {}
        self._defaults['CreateDeembeddingSparameterTableArray']['return'] = 0
        self._defaults['CreateDeembeddingSparameterTableS2PFile'] = {}
        self._defaults['CreateDeembeddingSparameterTableS2PFile']['return'] = 0
        self._defaults['DeleteAllDeembeddingTables'] = {}
        self._defaults['DeleteAllDeembeddingTables']['return'] = 0
        self._defaults['DeleteDeembeddingTable'] = {}
        self._defaults['DeleteDeembeddingTable']['return'] = 0
        self._defaults['DisableAdvanceTrigger'] = {}
        self._defaults['DisableAdvanceTrigger']['return'] = 0
        self._defaults['DisableRefTrigger'] = {}
        self._defaults['DisableRefTrigger']['return'] = 0
        self._defaults['DisableStartTrigger'] = {}
        self._defaults['DisableStartTrigger']['return'] = 0
        self._defaults['EnableSessionAccess'] = {}
        self._defaults['EnableSessionAccess']['return'] = 0
        self._defaults['ErrorMessage'] = {}
        self._defaults['ErrorMessage']['return'] = 0
        self._defaults['ErrorMessage']['errorMessage'] = None
        self._defaults['FetchIQMultiRecordComplexF32'] = {}
        self._defaults['FetchIQMultiRecordComplexF32']['return'] = 0
        self._defaults['FetchIQMultiRecordComplexF32']['wfmInfo'] = None
        self._defaults['FetchIQMultiRecordComplexF64'] = {}
        self._defaults['FetchIQMultiRecordComplexF64']['return'] = 0
        self._defaults['FetchIQMultiRecordComplexF64']['wfmInfo'] = None
        self._defaults['FetchIQMultiRecordComplexI16'] = {}
        self._defaults['FetchIQMultiRecordComplexI16']['return'] = 0
        self._defaults['FetchIQMultiRecordComplexI16']['wfmInfo'] = None
        self._defaults['FetchIQSingleRecordComplexF32'] = {}
        self._defaults['FetchIQSingleRecordComplexF32']['return'] = 0
        self._defaults['FetchIQSingleRecordComplexF32']['wfmInfo'] = None
        self._defaults['FetchIQSingleRecordComplexF64'] = {}
        self._defaults['FetchIQSingleRecordComplexF64']['return'] = 0
        self._defaults['FetchIQSingleRecordComplexF64']['wfmInfo'] = None
        self._defaults['FetchIQSingleRecordComplexI16'] = {}
        self._defaults['FetchIQSingleRecordComplexI16']['return'] = 0
        self._defaults['FetchIQSingleRecordComplexI16']['wfmInfo'] = None
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
        self._defaults['GetDeembeddingSparameters'] = {}
        self._defaults['GetDeembeddingSparameters']['return'] = 0
        self._defaults['GetDeembeddingSparameters']['sparameters'] = None
        self._defaults['GetDeembeddingSparameters']['numberOfSparameters'] = None
        self._defaults['GetDeembeddingSparameters']['numberOfPorts'] = None
        self._defaults['GetDeembeddingTableNumberOfPorts'] = {}
        self._defaults['GetDeembeddingTableNumberOfPorts']['return'] = 0
        self._defaults['GetDeembeddingTableNumberOfPorts']['numberOfPorts'] = None
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
        self._defaults['GetExtCalRecommendedInterval'] = {}
        self._defaults['GetExtCalRecommendedInterval']['return'] = 0
        self._defaults['GetExtCalRecommendedInterval']['months'] = None
        self._defaults['GetFetchBacklog'] = {}
        self._defaults['GetFetchBacklog']['return'] = 0
        self._defaults['GetFetchBacklog']['backlog'] = None
        self._defaults['GetFrequencyResponse'] = {}
        self._defaults['GetFrequencyResponse']['return'] = 0
        self._defaults['GetFrequencyResponse']['numberOfFrequencies'] = None
        self._defaults['GetFrequencyResponse']['frequencies'] = None
        self._defaults['GetFrequencyResponse']['magnitudeResponse'] = None
        self._defaults['GetFrequencyResponse']['phaseResponse'] = None
        self._defaults['GetScalingCoefficients'] = {}
        self._defaults['GetScalingCoefficients']['return'] = 0
        self._defaults['GetScalingCoefficients']['numberOfCoefficientSets'] = None
        self._defaults['GetScalingCoefficients']['coefficientInfo'] = None
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
        self._defaults['GetTerminalName'] = {}
        self._defaults['GetTerminalName']['return'] = 0
        self._defaults['GetTerminalName']['terminalName'] = None
        self._defaults['InitWithOptions'] = {}
        self._defaults['InitWithOptions']['return'] = 0
        self._defaults['InitWithOptions']['newVi'] = None
        self._defaults['Initiate'] = {}
        self._defaults['Initiate']['return'] = 0
        self._defaults['IsSelfCalValid'] = {}
        self._defaults['IsSelfCalValid']['return'] = 0
        self._defaults['IsSelfCalValid']['selfCalValid'] = None
        self._defaults['IsSelfCalValid']['validSteps'] = None
        self._defaults['LoadConfigurationsFromFile'] = {}
        self._defaults['LoadConfigurationsFromFile']['return'] = 0
        self._defaults['LockSession'] = {}
        self._defaults['LockSession']['return'] = 0
        self._defaults['LockSession']['callerHasLock'] = None
        self._defaults['PerformThermalCorrection'] = {}
        self._defaults['PerformThermalCorrection']['return'] = 0
        self._defaults['ReadIQSingleRecordComplexF64'] = {}
        self._defaults['ReadIQSingleRecordComplexF64']['return'] = 0
        self._defaults['ReadIQSingleRecordComplexF64']['wfmInfo'] = None
        self._defaults['ReadPowerSpectrumF32'] = {}
        self._defaults['ReadPowerSpectrumF32']['return'] = 0
        self._defaults['ReadPowerSpectrumF32']['spectrumInfo'] = None
        self._defaults['ReadPowerSpectrumF64'] = {}
        self._defaults['ReadPowerSpectrumF64']['return'] = 0
        self._defaults['ReadPowerSpectrumF64']['spectrumInfo'] = None
        self._defaults['ResetDevice'] = {}
        self._defaults['ResetDevice']['return'] = 0
        self._defaults['ResetWithOptions'] = {}
        self._defaults['ResetWithOptions']['return'] = 0
        self._defaults['SaveConfigurationsToFile'] = {}
        self._defaults['SaveConfigurationsToFile']['return'] = 0
        self._defaults['SelfCalibrateRange'] = {}
        self._defaults['SelfCalibrateRange']['return'] = 0
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
        self._defaults['UnlockSession'] = {}
        self._defaults['UnlockSession']['return'] = 0
        self._defaults['UnlockSession']['callerHasLock'] = None
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

    def niRFSA_Abort(self, vi):  # noqa: N802
        if self._defaults['Abort']['return'] != 0:
            return self._defaults['Abort']['return']
        return self._defaults['Abort']['return']

    def niRFSA_ChangeExternalCalibrationPassword(self, vi, old_password, new_password):  # noqa: N802
        if self._defaults['ChangeExternalCalibrationPassword']['return'] != 0:
            return self._defaults['ChangeExternalCalibrationPassword']['return']
        return self._defaults['ChangeExternalCalibrationPassword']['return']

    def niRFSA_CheckAcquisitionStatus(self, vi, is_done):  # noqa: N802
        if self._defaults['CheckAcquisitionStatus']['return'] != 0:
            return self._defaults['CheckAcquisitionStatus']['return']
        # is_done
        if self._defaults['CheckAcquisitionStatus']['isDone'] is None:
            raise MockFunctionCallError("niRFSA_CheckAcquisitionStatus", param='isDone')
        if is_done is not None:
            is_done.contents.value = self._defaults['CheckAcquisitionStatus']['isDone']
        return self._defaults['CheckAcquisitionStatus']['return']

    def niRFSA_ClearSelfCalibrateRange(self, vi):  # noqa: N802
        if self._defaults['ClearSelfCalibrateRange']['return'] != 0:
            return self._defaults['ClearSelfCalibrateRange']['return']
        return self._defaults['ClearSelfCalibrateRange']['return']

    def niRFSA_Commit(self, vi):  # noqa: N802
        if self._defaults['Commit']['return'] != 0:
            return self._defaults['Commit']['return']
        return self._defaults['Commit']['return']

    def niRFSA_ConfigureDeembeddingTableInterpolationLinear(self, vi, port, table_name, format):  # noqa: N802
        if self._defaults['ConfigureDeembeddingTableInterpolationLinear']['return'] != 0:
            return self._defaults['ConfigureDeembeddingTableInterpolationLinear']['return']
        return self._defaults['ConfigureDeembeddingTableInterpolationLinear']['return']

    def niRFSA_ConfigureDeembeddingTableInterpolationNearest(self, vi, port, table_name):  # noqa: N802
        if self._defaults['ConfigureDeembeddingTableInterpolationNearest']['return'] != 0:
            return self._defaults['ConfigureDeembeddingTableInterpolationNearest']['return']
        return self._defaults['ConfigureDeembeddingTableInterpolationNearest']['return']

    def niRFSA_ConfigureDeembeddingTableInterpolationSpline(self, vi, port, table_name):  # noqa: N802
        if self._defaults['ConfigureDeembeddingTableInterpolationSpline']['return'] != 0:
            return self._defaults['ConfigureDeembeddingTableInterpolationSpline']['return']
        return self._defaults['ConfigureDeembeddingTableInterpolationSpline']['return']

    def niRFSA_ConfigureDigitalEdgeAdvanceTrigger(self, vi, source, edge):  # noqa: N802
        if self._defaults['ConfigureDigitalEdgeAdvanceTrigger']['return'] != 0:
            return self._defaults['ConfigureDigitalEdgeAdvanceTrigger']['return']
        return self._defaults['ConfigureDigitalEdgeAdvanceTrigger']['return']

    def niRFSA_ConfigureDigitalEdgeRefTrigger(self, vi, source, edge, pretrigger_samples):  # noqa: N802
        if self._defaults['ConfigureDigitalEdgeRefTrigger']['return'] != 0:
            return self._defaults['ConfigureDigitalEdgeRefTrigger']['return']
        return self._defaults['ConfigureDigitalEdgeRefTrigger']['return']

    def niRFSA_ConfigureDigitalEdgeStartTrigger(self, vi, source, edge):  # noqa: N802
        if self._defaults['ConfigureDigitalEdgeStartTrigger']['return'] != 0:
            return self._defaults['ConfigureDigitalEdgeStartTrigger']['return']
        return self._defaults['ConfigureDigitalEdgeStartTrigger']['return']

    def niRFSA_ConfigureIQPowerEdgeRefTrigger(self, vi, source, level, slope, pretrigger_samples):  # noqa: N802
        if self._defaults['ConfigureIQPowerEdgeRefTrigger']['return'] != 0:
            return self._defaults['ConfigureIQPowerEdgeRefTrigger']['return']
        return self._defaults['ConfigureIQPowerEdgeRefTrigger']['return']

    def niRFSA_ConfigureRefClock(self, vi, clock_source, ref_clock_rate):  # noqa: N802
        if self._defaults['ConfigureRefClock']['return'] != 0:
            return self._defaults['ConfigureRefClock']['return']
        return self._defaults['ConfigureRefClock']['return']

    def niRFSA_ConfigureSoftwareEdgeAdvanceTrigger(self, vi):  # noqa: N802
        if self._defaults['ConfigureSoftwareEdgeAdvanceTrigger']['return'] != 0:
            return self._defaults['ConfigureSoftwareEdgeAdvanceTrigger']['return']
        return self._defaults['ConfigureSoftwareEdgeAdvanceTrigger']['return']

    def niRFSA_ConfigureSoftwareEdgeRefTrigger(self, vi, pretrigger_samples):  # noqa: N802
        if self._defaults['ConfigureSoftwareEdgeRefTrigger']['return'] != 0:
            return self._defaults['ConfigureSoftwareEdgeRefTrigger']['return']
        return self._defaults['ConfigureSoftwareEdgeRefTrigger']['return']

    def niRFSA_ConfigureSoftwareEdgeStartTrigger(self, vi):  # noqa: N802
        if self._defaults['ConfigureSoftwareEdgeStartTrigger']['return'] != 0:
            return self._defaults['ConfigureSoftwareEdgeStartTrigger']['return']
        return self._defaults['ConfigureSoftwareEdgeStartTrigger']['return']

    def niRFSA_ConfigureSpectrumFrequencyCenterSpan(self, vi, channel_list, center_frequency, span):  # noqa: N802
        if self._defaults['ConfigureSpectrumFrequencyCenterSpan']['return'] != 0:
            return self._defaults['ConfigureSpectrumFrequencyCenterSpan']['return']
        return self._defaults['ConfigureSpectrumFrequencyCenterSpan']['return']

    def niRFSA_ConfigureSpectrumFrequencyStartStop(self, vi, channel_list, start_frequency, stop_frequency):  # noqa: N802
        if self._defaults['ConfigureSpectrumFrequencyStartStop']['return'] != 0:
            return self._defaults['ConfigureSpectrumFrequencyStartStop']['return']
        return self._defaults['ConfigureSpectrumFrequencyStartStop']['return']

    def niRFSA_CreateDeembeddingSparameterTableArray(self, vi, port, table_name, frequencies, frequencies_size, sparameter_table, sparameter_table_size, number_of_ports, sparameter_orientation):  # noqa: N802
        if self._defaults['CreateDeembeddingSparameterTableArray']['return'] != 0:
            return self._defaults['CreateDeembeddingSparameterTableArray']['return']
        return self._defaults['CreateDeembeddingSparameterTableArray']['return']

    def niRFSA_CreateDeembeddingSparameterTableS2PFile(self, vi, port, table_name, s2p_file_path, sparameter_orientation):  # noqa: N802
        if self._defaults['CreateDeembeddingSparameterTableS2PFile']['return'] != 0:
            return self._defaults['CreateDeembeddingSparameterTableS2PFile']['return']
        return self._defaults['CreateDeembeddingSparameterTableS2PFile']['return']

    def niRFSA_DeleteAllDeembeddingTables(self, vi):  # noqa: N802
        if self._defaults['DeleteAllDeembeddingTables']['return'] != 0:
            return self._defaults['DeleteAllDeembeddingTables']['return']
        return self._defaults['DeleteAllDeembeddingTables']['return']

    def niRFSA_DeleteDeembeddingTable(self, vi, port, table_name):  # noqa: N802
        if self._defaults['DeleteDeembeddingTable']['return'] != 0:
            return self._defaults['DeleteDeembeddingTable']['return']
        return self._defaults['DeleteDeembeddingTable']['return']

    def niRFSA_DisableAdvanceTrigger(self, vi):  # noqa: N802
        if self._defaults['DisableAdvanceTrigger']['return'] != 0:
            return self._defaults['DisableAdvanceTrigger']['return']
        return self._defaults['DisableAdvanceTrigger']['return']

    def niRFSA_DisableRefTrigger(self, vi):  # noqa: N802
        if self._defaults['DisableRefTrigger']['return'] != 0:
            return self._defaults['DisableRefTrigger']['return']
        return self._defaults['DisableRefTrigger']['return']

    def niRFSA_DisableStartTrigger(self, vi):  # noqa: N802
        if self._defaults['DisableStartTrigger']['return'] != 0:
            return self._defaults['DisableStartTrigger']['return']
        return self._defaults['DisableStartTrigger']['return']

    def niRFSA_EnableSessionAccess(self, vi, enable):  # noqa: N802
        if self._defaults['EnableSessionAccess']['return'] != 0:
            return self._defaults['EnableSessionAccess']['return']
        return self._defaults['EnableSessionAccess']['return']

    def niRFSA_ErrorMessage(self, vi, error_code, error_message):  # noqa: N802
        if self._defaults['ErrorMessage']['return'] != 0:
            return self._defaults['ErrorMessage']['return']
        # error_message
        if self._defaults['ErrorMessage']['errorMessage'] is None:
            raise MockFunctionCallError("niRFSA_ErrorMessage", param='errorMessage')
        test_value = self._defaults['ErrorMessage']['errorMessage']
        if type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(error_message) >= len(test_value)
        for i in range(len(test_value)):
            error_message[i] = test_value[i]
        return self._defaults['ErrorMessage']['return']

    def niRFSA_FetchIQMultiRecordComplexF32(self, vi, channel_list, starting_record, number_of_records, number_of_samples, timeout, iq_data_arrays, wfm_info):  # noqa: N802
        if self._defaults['FetchIQMultiRecordComplexF32']['return'] != 0:
            return self._defaults['FetchIQMultiRecordComplexF32']['return']
        # wfm_info
        if self._defaults['FetchIQMultiRecordComplexF32']['wfmInfo'] is None:
            raise MockFunctionCallError("niRFSA_FetchIQMultiRecordComplexF32", param='wfmInfo')
        for field in self._defaults['FetchIQMultiRecordComplexF32']['wfm_info']._fields_:
            field_name = field[0]
            setattr(wfm_info.contents, field_name, getattr(self._defaults['FetchIQMultiRecordComplexF32']['wfm_info'], field_name))
        return self._defaults['FetchIQMultiRecordComplexF32']['return']

    def niRFSA_FetchIQMultiRecordComplexF64(self, vi, channel_list, starting_record, number_of_records, number_of_samples, timeout, iq_data_arrays, wfm_info):  # noqa: N802
        if self._defaults['FetchIQMultiRecordComplexF64']['return'] != 0:
            return self._defaults['FetchIQMultiRecordComplexF64']['return']
        # wfm_info
        if self._defaults['FetchIQMultiRecordComplexF64']['wfmInfo'] is None:
            raise MockFunctionCallError("niRFSA_FetchIQMultiRecordComplexF64", param='wfmInfo')
        for field in self._defaults['FetchIQMultiRecordComplexF64']['wfm_info']._fields_:
            field_name = field[0]
            setattr(wfm_info.contents, field_name, getattr(self._defaults['FetchIQMultiRecordComplexF64']['wfm_info'], field_name))
        return self._defaults['FetchIQMultiRecordComplexF64']['return']

    def niRFSA_FetchIQMultiRecordComplexI16(self, vi, channel_list, starting_record, number_of_records, number_of_samples, timeout, iq_data_arrays, wfm_info):  # noqa: N802
        if self._defaults['FetchIQMultiRecordComplexI16']['return'] != 0:
            return self._defaults['FetchIQMultiRecordComplexI16']['return']
        # wfm_info
        if self._defaults['FetchIQMultiRecordComplexI16']['wfmInfo'] is None:
            raise MockFunctionCallError("niRFSA_FetchIQMultiRecordComplexI16", param='wfmInfo')
        for field in self._defaults['FetchIQMultiRecordComplexI16']['wfm_info']._fields_:
            field_name = field[0]
            setattr(wfm_info.contents, field_name, getattr(self._defaults['FetchIQMultiRecordComplexI16']['wfm_info'], field_name))
        return self._defaults['FetchIQMultiRecordComplexI16']['return']

    def niRFSA_FetchIQSingleRecordComplexF32(self, vi, channel_list, record_number, number_of_samples, timeout, iq_data_array, wfm_info):  # noqa: N802
        if self._defaults['FetchIQSingleRecordComplexF32']['return'] != 0:
            return self._defaults['FetchIQSingleRecordComplexF32']['return']
        # wfm_info
        if self._defaults['FetchIQSingleRecordComplexF32']['wfmInfo'] is None:
            raise MockFunctionCallError("niRFSA_FetchIQSingleRecordComplexF32", param='wfmInfo')
        for field in self._defaults['FetchIQSingleRecordComplexF32']['wfm_info']._fields_:
            field_name = field[0]
            setattr(wfm_info.contents, field_name, getattr(self._defaults['FetchIQSingleRecordComplexF32']['wfm_info'], field_name))
        return self._defaults['FetchIQSingleRecordComplexF32']['return']

    def niRFSA_FetchIQSingleRecordComplexF64(self, vi, channel_list, record_number, number_of_samples, timeout, iq_data_array, wfm_info):  # noqa: N802
        if self._defaults['FetchIQSingleRecordComplexF64']['return'] != 0:
            return self._defaults['FetchIQSingleRecordComplexF64']['return']
        # wfm_info
        if self._defaults['FetchIQSingleRecordComplexF64']['wfmInfo'] is None:
            raise MockFunctionCallError("niRFSA_FetchIQSingleRecordComplexF64", param='wfmInfo')
        for field in self._defaults['FetchIQSingleRecordComplexF64']['wfm_info']._fields_:
            field_name = field[0]
            setattr(wfm_info.contents, field_name, getattr(self._defaults['FetchIQSingleRecordComplexF64']['wfm_info'], field_name))
        return self._defaults['FetchIQSingleRecordComplexF64']['return']

    def niRFSA_FetchIQSingleRecordComplexI16(self, vi, channel_list, record_number, number_of_samples, timeout, iq_data_array, wfm_info):  # noqa: N802
        if self._defaults['FetchIQSingleRecordComplexI16']['return'] != 0:
            return self._defaults['FetchIQSingleRecordComplexI16']['return']
        # wfm_info
        if self._defaults['FetchIQSingleRecordComplexI16']['wfmInfo'] is None:
            raise MockFunctionCallError("niRFSA_FetchIQSingleRecordComplexI16", param='wfmInfo')
        for field in self._defaults['FetchIQSingleRecordComplexI16']['wfm_info']._fields_:
            field_name = field[0]
            setattr(wfm_info.contents, field_name, getattr(self._defaults['FetchIQSingleRecordComplexI16']['wfm_info'], field_name))
        return self._defaults['FetchIQSingleRecordComplexI16']['return']

    def niRFSA_GetAttributeViBoolean(self, vi, channel_name, attribute_id, value):  # noqa: N802
        if self._defaults['GetAttributeViBoolean']['return'] != 0:
            return self._defaults['GetAttributeViBoolean']['return']
        # value
        if self._defaults['GetAttributeViBoolean']['value'] is None:
            raise MockFunctionCallError("niRFSA_GetAttributeViBoolean", param='value')
        if value is not None:
            value.contents.value = self._defaults['GetAttributeViBoolean']['value']
        return self._defaults['GetAttributeViBoolean']['return']

    def niRFSA_GetAttributeViInt32(self, vi, channel_name, attribute_id, value):  # noqa: N802
        if self._defaults['GetAttributeViInt32']['return'] != 0:
            return self._defaults['GetAttributeViInt32']['return']
        # value
        if self._defaults['GetAttributeViInt32']['value'] is None:
            raise MockFunctionCallError("niRFSA_GetAttributeViInt32", param='value')
        if value is not None:
            value.contents.value = self._defaults['GetAttributeViInt32']['value']
        return self._defaults['GetAttributeViInt32']['return']

    def niRFSA_GetAttributeViInt64(self, vi, channel_name, attribute_id, value):  # noqa: N802
        if self._defaults['GetAttributeViInt64']['return'] != 0:
            return self._defaults['GetAttributeViInt64']['return']
        # value
        if self._defaults['GetAttributeViInt64']['value'] is None:
            raise MockFunctionCallError("niRFSA_GetAttributeViInt64", param='value')
        if value is not None:
            value.contents.value = self._defaults['GetAttributeViInt64']['value']
        return self._defaults['GetAttributeViInt64']['return']

    def niRFSA_GetAttributeViReal64(self, vi, channel_name, attribute_id, value):  # noqa: N802
        if self._defaults['GetAttributeViReal64']['return'] != 0:
            return self._defaults['GetAttributeViReal64']['return']
        # value
        if self._defaults['GetAttributeViReal64']['value'] is None:
            raise MockFunctionCallError("niRFSA_GetAttributeViReal64", param='value')
        if value is not None:
            value.contents.value = self._defaults['GetAttributeViReal64']['value']
        return self._defaults['GetAttributeViReal64']['return']

    def niRFSA_GetAttributeViSession(self, vi, channel_name, attribute_id, value):  # noqa: N802
        if self._defaults['GetAttributeViSession']['return'] != 0:
            return self._defaults['GetAttributeViSession']['return']
        # value
        if self._defaults['GetAttributeViSession']['value'] is None:
            raise MockFunctionCallError("niRFSA_GetAttributeViSession", param='value')
        if value is not None:
            value.contents.value = self._defaults['GetAttributeViSession']['value']
        return self._defaults['GetAttributeViSession']['return']

    def niRFSA_GetAttributeViString(self, vi, channel_name, attribute_id, buf_size, value):  # noqa: N802
        if self._defaults['GetAttributeViString']['return'] != 0:
            return self._defaults['GetAttributeViString']['return']
        # value
        if self._defaults['GetAttributeViString']['value'] is None:
            raise MockFunctionCallError("niRFSA_GetAttributeViString", param='value')
        if buf_size.value == 0:
            return len(self._defaults['GetAttributeViString']['value'])
        value.value = self._defaults['GetAttributeViString']['value'].encode('ascii')
        return self._defaults['GetAttributeViString']['return']

    def niRFSA_GetDeembeddingSparameters(self, vi, sparameters, sparameters_array_size, number_of_sparameters, number_of_ports):  # noqa: N802
        if self._defaults['GetDeembeddingSparameters']['return'] != 0:
            return self._defaults['GetDeembeddingSparameters']['return']
        # sparameters
        if self._defaults['GetDeembeddingSparameters']['sparameters'] is None:
            raise MockFunctionCallError("niRFSA_GetDeembeddingSparameters", param='sparameters')
        test_value = self._defaults['GetDeembeddingSparameters']['sparameters']
        try:
            sparameters_ref = sparameters.contents
        except AttributeError:
            sparameters_ref = sparameters
        assert len(sparameters_ref) >= len(test_value)
        for i in range(len(test_value)):
            sparameters_ref[i] = test_value[i]
        # number_of_sparameters
        if self._defaults['GetDeembeddingSparameters']['numberOfSparameters'] is None:
            raise MockFunctionCallError("niRFSA_GetDeembeddingSparameters", param='numberOfSparameters')
        if number_of_sparameters is not None:
            number_of_sparameters.contents.value = self._defaults['GetDeembeddingSparameters']['numberOfSparameters']
        # number_of_ports
        if self._defaults['GetDeembeddingSparameters']['numberOfPorts'] is None:
            raise MockFunctionCallError("niRFSA_GetDeembeddingSparameters", param='numberOfPorts')
        if number_of_ports is not None:
            number_of_ports.contents.value = self._defaults['GetDeembeddingSparameters']['numberOfPorts']
        return self._defaults['GetDeembeddingSparameters']['return']

    def niRFSA_GetDeembeddingTableNumberOfPorts(self, vi, number_of_ports):  # noqa: N802
        if self._defaults['GetDeembeddingTableNumberOfPorts']['return'] != 0:
            return self._defaults['GetDeembeddingTableNumberOfPorts']['return']
        # number_of_ports
        if self._defaults['GetDeembeddingTableNumberOfPorts']['numberOfPorts'] is None:
            raise MockFunctionCallError("niRFSA_GetDeembeddingTableNumberOfPorts", param='numberOfPorts')
        if number_of_ports is not None:
            number_of_ports.contents.value = self._defaults['GetDeembeddingTableNumberOfPorts']['numberOfPorts']
        return self._defaults['GetDeembeddingTableNumberOfPorts']['return']

    def niRFSA_GetError(self, vi, error_code, error_description_buffer_size, error_description):  # noqa: N802
        if self._defaults['GetError']['return'] != 0:
            return self._defaults['GetError']['return']
        # error_code
        if self._defaults['GetError']['errorCode'] is None:
            raise MockFunctionCallError("niRFSA_GetError", param='errorCode')
        if error_code is not None:
            error_code.contents.value = self._defaults['GetError']['errorCode']
        # error_description
        if self._defaults['GetError']['errorDescription'] is None:
            raise MockFunctionCallError("niRFSA_GetError", param='errorDescription')
        if error_description_buffer_size.value == 0:
            return len(self._defaults['GetError']['errorDescription'])
        error_description.value = self._defaults['GetError']['errorDescription'].encode('ascii')
        return self._defaults['GetError']['return']

    def niRFSA_GetExtCalLastDateAndTime(self, vi, year, month, day, hour, minute):  # noqa: N802
        if self._defaults['GetExtCalLastDateAndTime']['return'] != 0:
            return self._defaults['GetExtCalLastDateAndTime']['return']
        # year
        if self._defaults['GetExtCalLastDateAndTime']['year'] is None:
            raise MockFunctionCallError("niRFSA_GetExtCalLastDateAndTime", param='year')
        if year is not None:
            year.contents.value = self._defaults['GetExtCalLastDateAndTime']['year']
        # month
        if self._defaults['GetExtCalLastDateAndTime']['month'] is None:
            raise MockFunctionCallError("niRFSA_GetExtCalLastDateAndTime", param='month')
        if month is not None:
            month.contents.value = self._defaults['GetExtCalLastDateAndTime']['month']
        # day
        if self._defaults['GetExtCalLastDateAndTime']['day'] is None:
            raise MockFunctionCallError("niRFSA_GetExtCalLastDateAndTime", param='day')
        if day is not None:
            day.contents.value = self._defaults['GetExtCalLastDateAndTime']['day']
        # hour
        if self._defaults['GetExtCalLastDateAndTime']['hour'] is None:
            raise MockFunctionCallError("niRFSA_GetExtCalLastDateAndTime", param='hour')
        if hour is not None:
            hour.contents.value = self._defaults['GetExtCalLastDateAndTime']['hour']
        # minute
        if self._defaults['GetExtCalLastDateAndTime']['minute'] is None:
            raise MockFunctionCallError("niRFSA_GetExtCalLastDateAndTime", param='minute')
        if minute is not None:
            minute.contents.value = self._defaults['GetExtCalLastDateAndTime']['minute']
        return self._defaults['GetExtCalLastDateAndTime']['return']

    def niRFSA_GetExtCalRecommendedInterval(self, vi, months):  # noqa: N802
        if self._defaults['GetExtCalRecommendedInterval']['return'] != 0:
            return self._defaults['GetExtCalRecommendedInterval']['return']
        # months
        if self._defaults['GetExtCalRecommendedInterval']['months'] is None:
            raise MockFunctionCallError("niRFSA_GetExtCalRecommendedInterval", param='months')
        if months is not None:
            months.contents.value = self._defaults['GetExtCalRecommendedInterval']['months']
        return self._defaults['GetExtCalRecommendedInterval']['return']

    def niRFSA_GetFetchBacklog(self, vi, channel_list, record_number, backlog):  # noqa: N802
        if self._defaults['GetFetchBacklog']['return'] != 0:
            return self._defaults['GetFetchBacklog']['return']
        # backlog
        if self._defaults['GetFetchBacklog']['backlog'] is None:
            raise MockFunctionCallError("niRFSA_GetFetchBacklog", param='backlog')
        if backlog is not None:
            backlog.contents.value = self._defaults['GetFetchBacklog']['backlog']
        return self._defaults['GetFetchBacklog']['return']

    def niRFSA_GetFrequencyResponse(self, vi, channel_list, buffer_size, frequencies, magnitude_response, phase_response, number_of_frequencies):  # noqa: N802
        if self._defaults['GetFrequencyResponse']['return'] != 0:
            return self._defaults['GetFrequencyResponse']['return']
        # number_of_frequencies
        if self._defaults['GetFrequencyResponse']['numberOfFrequencies'] is None:
            raise MockFunctionCallError("niRFSA_GetFrequencyResponse", param='numberOfFrequencies')
        if number_of_frequencies is not None:
            number_of_frequencies.contents.value = self._defaults['GetFrequencyResponse']['numberOfFrequencies']
        # frequencies
        if self._defaults['GetFrequencyResponse']['frequencies'] is None:
            raise MockFunctionCallError("niRFSA_GetFrequencyResponse", param='frequencies')
        if buffer_size.value == 0:
            return len(self._defaults['GetFrequencyResponse']['frequencies'])
        try:
            frequencies_ref = frequencies.contents
        except AttributeError:
            frequencies_ref = frequencies
        for i in range(len(self._defaults['GetFrequencyResponse']['frequencies'])):
            frequencies_ref[i] = self._defaults['GetFrequencyResponse']['frequencies'][i]
        # magnitude_response
        if self._defaults['GetFrequencyResponse']['magnitudeResponse'] is None:
            raise MockFunctionCallError("niRFSA_GetFrequencyResponse", param='magnitudeResponse')
        if buffer_size.value == 0:
            return len(self._defaults['GetFrequencyResponse']['magnitudeResponse'])
        try:
            magnitude_response_ref = magnitude_response.contents
        except AttributeError:
            magnitude_response_ref = magnitude_response
        for i in range(len(self._defaults['GetFrequencyResponse']['magnitudeResponse'])):
            magnitude_response_ref[i] = self._defaults['GetFrequencyResponse']['magnitudeResponse'][i]
        # phase_response
        if self._defaults['GetFrequencyResponse']['phaseResponse'] is None:
            raise MockFunctionCallError("niRFSA_GetFrequencyResponse", param='phaseResponse')
        if buffer_size.value == 0:
            return len(self._defaults['GetFrequencyResponse']['phaseResponse'])
        try:
            phase_response_ref = phase_response.contents
        except AttributeError:
            phase_response_ref = phase_response
        for i in range(len(self._defaults['GetFrequencyResponse']['phaseResponse'])):
            phase_response_ref[i] = self._defaults['GetFrequencyResponse']['phaseResponse'][i]
        return self._defaults['GetFrequencyResponse']['return']

    def niRFSA_GetScalingCoefficients(self, vi, channel_list, array_size, coefficient_info, number_of_coefficient_sets):  # noqa: N802
        if self._defaults['GetScalingCoefficients']['return'] != 0:
            return self._defaults['GetScalingCoefficients']['return']
        # number_of_coefficient_sets
        if self._defaults['GetScalingCoefficients']['numberOfCoefficientSets'] is None:
            raise MockFunctionCallError("niRFSA_GetScalingCoefficients", param='numberOfCoefficientSets')
        if number_of_coefficient_sets is not None:
            number_of_coefficient_sets.contents.value = self._defaults['GetScalingCoefficients']['numberOfCoefficientSets']
        # coefficient_info
        if self._defaults['GetScalingCoefficients']['coefficientInfo'] is None:
            raise MockFunctionCallError("niRFSA_GetScalingCoefficients", param='coefficientInfo')
        if array_size.value == 0:
            return len(self._defaults['GetScalingCoefficients']['coefficientInfo'])
        try:
            coefficient_info_ref = coefficient_info.contents
        except AttributeError:
            coefficient_info_ref = coefficient_info
        for i in range(len(self._defaults['GetScalingCoefficients']['coefficientInfo'])):
            coefficient_info_ref[i] = self._defaults['GetScalingCoefficients']['coefficientInfo'][i]
        return self._defaults['GetScalingCoefficients']['return']

    def niRFSA_GetSelfCalLastDateAndTime(self, vi, self_calibration_step, year, month, day, hour, minute):  # noqa: N802
        if self._defaults['GetSelfCalLastDateAndTime']['return'] != 0:
            return self._defaults['GetSelfCalLastDateAndTime']['return']
        # year
        if self._defaults['GetSelfCalLastDateAndTime']['year'] is None:
            raise MockFunctionCallError("niRFSA_GetSelfCalLastDateAndTime", param='year')
        if year is not None:
            year.contents.value = self._defaults['GetSelfCalLastDateAndTime']['year']
        # month
        if self._defaults['GetSelfCalLastDateAndTime']['month'] is None:
            raise MockFunctionCallError("niRFSA_GetSelfCalLastDateAndTime", param='month')
        if month is not None:
            month.contents.value = self._defaults['GetSelfCalLastDateAndTime']['month']
        # day
        if self._defaults['GetSelfCalLastDateAndTime']['day'] is None:
            raise MockFunctionCallError("niRFSA_GetSelfCalLastDateAndTime", param='day')
        if day is not None:
            day.contents.value = self._defaults['GetSelfCalLastDateAndTime']['day']
        # hour
        if self._defaults['GetSelfCalLastDateAndTime']['hour'] is None:
            raise MockFunctionCallError("niRFSA_GetSelfCalLastDateAndTime", param='hour')
        if hour is not None:
            hour.contents.value = self._defaults['GetSelfCalLastDateAndTime']['hour']
        # minute
        if self._defaults['GetSelfCalLastDateAndTime']['minute'] is None:
            raise MockFunctionCallError("niRFSA_GetSelfCalLastDateAndTime", param='minute')
        if minute is not None:
            minute.contents.value = self._defaults['GetSelfCalLastDateAndTime']['minute']
        return self._defaults['GetSelfCalLastDateAndTime']['return']

    def niRFSA_GetSelfCalLastTemp(self, vi, self_calibration_step, temperature):  # noqa: N802
        if self._defaults['GetSelfCalLastTemp']['return'] != 0:
            return self._defaults['GetSelfCalLastTemp']['return']
        # temperature
        if self._defaults['GetSelfCalLastTemp']['temperature'] is None:
            raise MockFunctionCallError("niRFSA_GetSelfCalLastTemp", param='temperature')
        if temperature is not None:
            temperature.contents.value = self._defaults['GetSelfCalLastTemp']['temperature']
        return self._defaults['GetSelfCalLastTemp']['return']

    def niRFSA_GetTerminalName(self, vi, signal, signal_identifier, buffer_size, terminal_name):  # noqa: N802
        if self._defaults['GetTerminalName']['return'] != 0:
            return self._defaults['GetTerminalName']['return']
        # terminal_name
        if self._defaults['GetTerminalName']['terminalName'] is None:
            raise MockFunctionCallError("niRFSA_GetTerminalName", param='terminalName')
        if buffer_size.value == 0:
            return len(self._defaults['GetTerminalName']['terminalName'])
        terminal_name.value = self._defaults['GetTerminalName']['terminalName'].encode('ascii')
        return self._defaults['GetTerminalName']['return']

    def niRFSA_InitWithOptions(self, resource_name, id_query, reset_device, option_string, new_vi):  # noqa: N802
        if self._defaults['InitWithOptions']['return'] != 0:
            return self._defaults['InitWithOptions']['return']
        # new_vi
        if self._defaults['InitWithOptions']['newVi'] is None:
            raise MockFunctionCallError("niRFSA_InitWithOptions", param='newVi')
        if new_vi is not None:
            new_vi.contents.value = self._defaults['InitWithOptions']['newVi']
        return self._defaults['InitWithOptions']['return']

    def niRFSA_Initiate(self, vi):  # noqa: N802
        if self._defaults['Initiate']['return'] != 0:
            return self._defaults['Initiate']['return']
        return self._defaults['Initiate']['return']

    def niRFSA_IsSelfCalValid(self, vi, self_cal_valid, valid_steps):  # noqa: N802
        if self._defaults['IsSelfCalValid']['return'] != 0:
            return self._defaults['IsSelfCalValid']['return']
        # self_cal_valid
        if self._defaults['IsSelfCalValid']['selfCalValid'] is None:
            raise MockFunctionCallError("niRFSA_IsSelfCalValid", param='selfCalValid')
        if self_cal_valid is not None:
            self_cal_valid.contents.value = self._defaults['IsSelfCalValid']['selfCalValid']
        # valid_steps
        if self._defaults['IsSelfCalValid']['validSteps'] is None:
            raise MockFunctionCallError("niRFSA_IsSelfCalValid", param='validSteps')
        if valid_steps is not None:
            valid_steps.contents.value = self._defaults['IsSelfCalValid']['validSteps']
        return self._defaults['IsSelfCalValid']['return']

    def niRFSA_LoadConfigurationsFromFile(self, vi, channel_name, file_path):  # noqa: N802
        if self._defaults['LoadConfigurationsFromFile']['return'] != 0:
            return self._defaults['LoadConfigurationsFromFile']['return']
        return self._defaults['LoadConfigurationsFromFile']['return']

    def niRFSA_LockSession(self, vi, caller_has_lock):  # noqa: N802
        if self._defaults['LockSession']['return'] != 0:
            return self._defaults['LockSession']['return']
        # caller_has_lock
        if self._defaults['LockSession']['callerHasLock'] is None:
            raise MockFunctionCallError("niRFSA_LockSession", param='callerHasLock')
        if caller_has_lock is not None:
            caller_has_lock.contents.value = self._defaults['LockSession']['callerHasLock']
        return self._defaults['LockSession']['return']

    def niRFSA_PerformThermalCorrection(self, vi):  # noqa: N802
        if self._defaults['PerformThermalCorrection']['return'] != 0:
            return self._defaults['PerformThermalCorrection']['return']
        return self._defaults['PerformThermalCorrection']['return']

    def niRFSA_ReadIQSingleRecordComplexF64(self, vi, channel_list, timeout, iq_data_array, data_array_size, wfm_info):  # noqa: N802
        if self._defaults['ReadIQSingleRecordComplexF64']['return'] != 0:
            return self._defaults['ReadIQSingleRecordComplexF64']['return']
        # wfm_info
        if self._defaults['ReadIQSingleRecordComplexF64']['wfmInfo'] is None:
            raise MockFunctionCallError("niRFSA_ReadIQSingleRecordComplexF64", param='wfmInfo')
        for field in self._defaults['ReadIQSingleRecordComplexF64']['wfm_info']._fields_:
            field_name = field[0]
            setattr(wfm_info.contents, field_name, getattr(self._defaults['ReadIQSingleRecordComplexF64']['wfm_info'], field_name))
        return self._defaults['ReadIQSingleRecordComplexF64']['return']

    def niRFSA_ReadPowerSpectrumF32(self, vi, channel_list, timeout, power_spectrum_data_array, data_array_size, spectrum_info):  # noqa: N802
        if self._defaults['ReadPowerSpectrumF32']['return'] != 0:
            return self._defaults['ReadPowerSpectrumF32']['return']
        # spectrum_info
        if self._defaults['ReadPowerSpectrumF32']['spectrumInfo'] is None:
            raise MockFunctionCallError("niRFSA_ReadPowerSpectrumF32", param='spectrumInfo')
        for field in self._defaults['ReadPowerSpectrumF32']['spectrum_info']._fields_:
            field_name = field[0]
            setattr(spectrum_info.contents, field_name, getattr(self._defaults['ReadPowerSpectrumF32']['spectrum_info'], field_name))
        return self._defaults['ReadPowerSpectrumF32']['return']

    def niRFSA_ReadPowerSpectrumF64(self, vi, channel_list, timeout, power_spectrum_data_array, data_array_size, spectrum_info):  # noqa: N802
        if self._defaults['ReadPowerSpectrumF64']['return'] != 0:
            return self._defaults['ReadPowerSpectrumF64']['return']
        # spectrum_info
        if self._defaults['ReadPowerSpectrumF64']['spectrumInfo'] is None:
            raise MockFunctionCallError("niRFSA_ReadPowerSpectrumF64", param='spectrumInfo')
        for field in self._defaults['ReadPowerSpectrumF64']['spectrum_info']._fields_:
            field_name = field[0]
            setattr(spectrum_info.contents, field_name, getattr(self._defaults['ReadPowerSpectrumF64']['spectrum_info'], field_name))
        return self._defaults['ReadPowerSpectrumF64']['return']

    def niRFSA_ResetDevice(self, vi):  # noqa: N802
        if self._defaults['ResetDevice']['return'] != 0:
            return self._defaults['ResetDevice']['return']
        return self._defaults['ResetDevice']['return']

    def niRFSA_ResetWithOptions(self, vi, steps_to_omit):  # noqa: N802
        if self._defaults['ResetWithOptions']['return'] != 0:
            return self._defaults['ResetWithOptions']['return']
        return self._defaults['ResetWithOptions']['return']

    def niRFSA_SaveConfigurationsToFile(self, vi, channel_name, file_path):  # noqa: N802
        if self._defaults['SaveConfigurationsToFile']['return'] != 0:
            return self._defaults['SaveConfigurationsToFile']['return']
        return self._defaults['SaveConfigurationsToFile']['return']

    def niRFSA_SelfCalibrateRange(self, vi, steps_to_omit, minimum_frequency, maximum_frequency, minimum_reference_level, maximum_reference_level):  # noqa: N802
        if self._defaults['SelfCalibrateRange']['return'] != 0:
            return self._defaults['SelfCalibrateRange']['return']
        return self._defaults['SelfCalibrateRange']['return']

    def niRFSA_SendSoftwareEdgeTrigger(self, vi, trigger, trigger_identifier):  # noqa: N802
        if self._defaults['SendSoftwareEdgeTrigger']['return'] != 0:
            return self._defaults['SendSoftwareEdgeTrigger']['return']
        return self._defaults['SendSoftwareEdgeTrigger']['return']

    def niRFSA_SetAttributeViBoolean(self, vi, channel_name, attribute_id, value):  # noqa: N802
        if self._defaults['SetAttributeViBoolean']['return'] != 0:
            return self._defaults['SetAttributeViBoolean']['return']
        return self._defaults['SetAttributeViBoolean']['return']

    def niRFSA_SetAttributeViInt32(self, vi, channel_name, attribute_id, value):  # noqa: N802
        if self._defaults['SetAttributeViInt32']['return'] != 0:
            return self._defaults['SetAttributeViInt32']['return']
        return self._defaults['SetAttributeViInt32']['return']

    def niRFSA_SetAttributeViInt64(self, vi, channel_name, attribute_id, value):  # noqa: N802
        if self._defaults['SetAttributeViInt64']['return'] != 0:
            return self._defaults['SetAttributeViInt64']['return']
        return self._defaults['SetAttributeViInt64']['return']

    def niRFSA_SetAttributeViReal64(self, vi, channel_name, attribute_id, value):  # noqa: N802
        if self._defaults['SetAttributeViReal64']['return'] != 0:
            return self._defaults['SetAttributeViReal64']['return']
        return self._defaults['SetAttributeViReal64']['return']

    def niRFSA_SetAttributeViSession(self, vi, channel_name, attribute_id, value):  # noqa: N802
        if self._defaults['SetAttributeViSession']['return'] != 0:
            return self._defaults['SetAttributeViSession']['return']
        return self._defaults['SetAttributeViSession']['return']

    def niRFSA_SetAttributeViString(self, vi, channel_name, attribute_id, value):  # noqa: N802
        if self._defaults['SetAttributeViString']['return'] != 0:
            return self._defaults['SetAttributeViString']['return']
        return self._defaults['SetAttributeViString']['return']

    def niRFSA_UnlockSession(self, vi, caller_has_lock):  # noqa: N802
        if self._defaults['UnlockSession']['return'] != 0:
            return self._defaults['UnlockSession']['return']
        # caller_has_lock
        if self._defaults['UnlockSession']['callerHasLock'] is None:
            raise MockFunctionCallError("niRFSA_UnlockSession", param='callerHasLock')
        if caller_has_lock is not None:
            caller_has_lock.contents.value = self._defaults['UnlockSession']['callerHasLock']
        return self._defaults['UnlockSession']['return']

    def niRFSA_close(self, vi):  # noqa: N802
        if self._defaults['close']['return'] != 0:
            return self._defaults['close']['return']
        return self._defaults['close']['return']

    def niRFSA_reset(self, vi):  # noqa: N802
        if self._defaults['reset']['return'] != 0:
            return self._defaults['reset']['return']
        return self._defaults['reset']['return']

    def niRFSA_self_test(self, vi, self_test_result, self_test_message):  # noqa: N802
        if self._defaults['self_test']['return'] != 0:
            return self._defaults['self_test']['return']
        # self_test_result
        if self._defaults['self_test']['selfTestResult'] is None:
            raise MockFunctionCallError("niRFSA_self_test", param='selfTestResult')
        if self_test_result is not None:
            self_test_result.contents.value = self._defaults['self_test']['selfTestResult']
        # self_test_message
        if self._defaults['self_test']['selfTestMessage'] is None:
            raise MockFunctionCallError("niRFSA_self_test", param='selfTestMessage')
        test_value = self._defaults['self_test']['selfTestMessage']
        if type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(self_test_message) >= len(test_value)
        for i in range(len(test_value)):
            self_test_message[i] = test_value[i]
        return self._defaults['self_test']['return']

    # Helper function to setup Mock object with default side effects and return values
    def set_side_effects_and_return_values(self, mock_library):
        mock_library.niRFSA_Abort.side_effect = MockFunctionCallError("niRFSA_Abort")
        mock_library.niRFSA_Abort.return_value = 0
        mock_library.niRFSA_ChangeExternalCalibrationPassword.side_effect = MockFunctionCallError("niRFSA_ChangeExternalCalibrationPassword")
        mock_library.niRFSA_ChangeExternalCalibrationPassword.return_value = 0
        mock_library.niRFSA_CheckAcquisitionStatus.side_effect = MockFunctionCallError("niRFSA_CheckAcquisitionStatus")
        mock_library.niRFSA_CheckAcquisitionStatus.return_value = 0
        mock_library.niRFSA_ClearSelfCalibrateRange.side_effect = MockFunctionCallError("niRFSA_ClearSelfCalibrateRange")
        mock_library.niRFSA_ClearSelfCalibrateRange.return_value = 0
        mock_library.niRFSA_Commit.side_effect = MockFunctionCallError("niRFSA_Commit")
        mock_library.niRFSA_Commit.return_value = 0
        mock_library.niRFSA_ConfigureDeembeddingTableInterpolationLinear.side_effect = MockFunctionCallError("niRFSA_ConfigureDeembeddingTableInterpolationLinear")
        mock_library.niRFSA_ConfigureDeembeddingTableInterpolationLinear.return_value = 0
        mock_library.niRFSA_ConfigureDeembeddingTableInterpolationNearest.side_effect = MockFunctionCallError("niRFSA_ConfigureDeembeddingTableInterpolationNearest")
        mock_library.niRFSA_ConfigureDeembeddingTableInterpolationNearest.return_value = 0
        mock_library.niRFSA_ConfigureDeembeddingTableInterpolationSpline.side_effect = MockFunctionCallError("niRFSA_ConfigureDeembeddingTableInterpolationSpline")
        mock_library.niRFSA_ConfigureDeembeddingTableInterpolationSpline.return_value = 0
        mock_library.niRFSA_ConfigureDigitalEdgeAdvanceTrigger.side_effect = MockFunctionCallError("niRFSA_ConfigureDigitalEdgeAdvanceTrigger")
        mock_library.niRFSA_ConfigureDigitalEdgeAdvanceTrigger.return_value = 0
        mock_library.niRFSA_ConfigureDigitalEdgeRefTrigger.side_effect = MockFunctionCallError("niRFSA_ConfigureDigitalEdgeRefTrigger")
        mock_library.niRFSA_ConfigureDigitalEdgeRefTrigger.return_value = 0
        mock_library.niRFSA_ConfigureDigitalEdgeStartTrigger.side_effect = MockFunctionCallError("niRFSA_ConfigureDigitalEdgeStartTrigger")
        mock_library.niRFSA_ConfigureDigitalEdgeStartTrigger.return_value = 0
        mock_library.niRFSA_ConfigureIQPowerEdgeRefTrigger.side_effect = MockFunctionCallError("niRFSA_ConfigureIQPowerEdgeRefTrigger")
        mock_library.niRFSA_ConfigureIQPowerEdgeRefTrigger.return_value = 0
        mock_library.niRFSA_ConfigureRefClock.side_effect = MockFunctionCallError("niRFSA_ConfigureRefClock")
        mock_library.niRFSA_ConfigureRefClock.return_value = 0
        mock_library.niRFSA_ConfigureSoftwareEdgeAdvanceTrigger.side_effect = MockFunctionCallError("niRFSA_ConfigureSoftwareEdgeAdvanceTrigger")
        mock_library.niRFSA_ConfigureSoftwareEdgeAdvanceTrigger.return_value = 0
        mock_library.niRFSA_ConfigureSoftwareEdgeRefTrigger.side_effect = MockFunctionCallError("niRFSA_ConfigureSoftwareEdgeRefTrigger")
        mock_library.niRFSA_ConfigureSoftwareEdgeRefTrigger.return_value = 0
        mock_library.niRFSA_ConfigureSoftwareEdgeStartTrigger.side_effect = MockFunctionCallError("niRFSA_ConfigureSoftwareEdgeStartTrigger")
        mock_library.niRFSA_ConfigureSoftwareEdgeStartTrigger.return_value = 0
        mock_library.niRFSA_ConfigureSpectrumFrequencyCenterSpan.side_effect = MockFunctionCallError("niRFSA_ConfigureSpectrumFrequencyCenterSpan")
        mock_library.niRFSA_ConfigureSpectrumFrequencyCenterSpan.return_value = 0
        mock_library.niRFSA_ConfigureSpectrumFrequencyStartStop.side_effect = MockFunctionCallError("niRFSA_ConfigureSpectrumFrequencyStartStop")
        mock_library.niRFSA_ConfigureSpectrumFrequencyStartStop.return_value = 0
        mock_library.niRFSA_CreateDeembeddingSparameterTableArray.side_effect = MockFunctionCallError("niRFSA_CreateDeembeddingSparameterTableArray")
        mock_library.niRFSA_CreateDeembeddingSparameterTableArray.return_value = 0
        mock_library.niRFSA_CreateDeembeddingSparameterTableS2PFile.side_effect = MockFunctionCallError("niRFSA_CreateDeembeddingSparameterTableS2PFile")
        mock_library.niRFSA_CreateDeembeddingSparameterTableS2PFile.return_value = 0
        mock_library.niRFSA_DeleteAllDeembeddingTables.side_effect = MockFunctionCallError("niRFSA_DeleteAllDeembeddingTables")
        mock_library.niRFSA_DeleteAllDeembeddingTables.return_value = 0
        mock_library.niRFSA_DeleteDeembeddingTable.side_effect = MockFunctionCallError("niRFSA_DeleteDeembeddingTable")
        mock_library.niRFSA_DeleteDeembeddingTable.return_value = 0
        mock_library.niRFSA_DisableAdvanceTrigger.side_effect = MockFunctionCallError("niRFSA_DisableAdvanceTrigger")
        mock_library.niRFSA_DisableAdvanceTrigger.return_value = 0
        mock_library.niRFSA_DisableRefTrigger.side_effect = MockFunctionCallError("niRFSA_DisableRefTrigger")
        mock_library.niRFSA_DisableRefTrigger.return_value = 0
        mock_library.niRFSA_DisableStartTrigger.side_effect = MockFunctionCallError("niRFSA_DisableStartTrigger")
        mock_library.niRFSA_DisableStartTrigger.return_value = 0
        mock_library.niRFSA_EnableSessionAccess.side_effect = MockFunctionCallError("niRFSA_EnableSessionAccess")
        mock_library.niRFSA_EnableSessionAccess.return_value = 0
        mock_library.niRFSA_ErrorMessage.side_effect = MockFunctionCallError("niRFSA_ErrorMessage")
        mock_library.niRFSA_ErrorMessage.return_value = 0
        mock_library.niRFSA_FetchIQMultiRecordComplexF32.side_effect = MockFunctionCallError("niRFSA_FetchIQMultiRecordComplexF32")
        mock_library.niRFSA_FetchIQMultiRecordComplexF32.return_value = 0
        mock_library.niRFSA_FetchIQMultiRecordComplexF64.side_effect = MockFunctionCallError("niRFSA_FetchIQMultiRecordComplexF64")
        mock_library.niRFSA_FetchIQMultiRecordComplexF64.return_value = 0
        mock_library.niRFSA_FetchIQMultiRecordComplexI16.side_effect = MockFunctionCallError("niRFSA_FetchIQMultiRecordComplexI16")
        mock_library.niRFSA_FetchIQMultiRecordComplexI16.return_value = 0
        mock_library.niRFSA_FetchIQSingleRecordComplexF32.side_effect = MockFunctionCallError("niRFSA_FetchIQSingleRecordComplexF32")
        mock_library.niRFSA_FetchIQSingleRecordComplexF32.return_value = 0
        mock_library.niRFSA_FetchIQSingleRecordComplexF64.side_effect = MockFunctionCallError("niRFSA_FetchIQSingleRecordComplexF64")
        mock_library.niRFSA_FetchIQSingleRecordComplexF64.return_value = 0
        mock_library.niRFSA_FetchIQSingleRecordComplexI16.side_effect = MockFunctionCallError("niRFSA_FetchIQSingleRecordComplexI16")
        mock_library.niRFSA_FetchIQSingleRecordComplexI16.return_value = 0
        mock_library.niRFSA_GetAttributeViBoolean.side_effect = MockFunctionCallError("niRFSA_GetAttributeViBoolean")
        mock_library.niRFSA_GetAttributeViBoolean.return_value = 0
        mock_library.niRFSA_GetAttributeViInt32.side_effect = MockFunctionCallError("niRFSA_GetAttributeViInt32")
        mock_library.niRFSA_GetAttributeViInt32.return_value = 0
        mock_library.niRFSA_GetAttributeViInt64.side_effect = MockFunctionCallError("niRFSA_GetAttributeViInt64")
        mock_library.niRFSA_GetAttributeViInt64.return_value = 0
        mock_library.niRFSA_GetAttributeViReal64.side_effect = MockFunctionCallError("niRFSA_GetAttributeViReal64")
        mock_library.niRFSA_GetAttributeViReal64.return_value = 0
        mock_library.niRFSA_GetAttributeViSession.side_effect = MockFunctionCallError("niRFSA_GetAttributeViSession")
        mock_library.niRFSA_GetAttributeViSession.return_value = 0
        mock_library.niRFSA_GetAttributeViString.side_effect = MockFunctionCallError("niRFSA_GetAttributeViString")
        mock_library.niRFSA_GetAttributeViString.return_value = 0
        mock_library.niRFSA_GetDeembeddingSparameters.side_effect = MockFunctionCallError("niRFSA_GetDeembeddingSparameters")
        mock_library.niRFSA_GetDeembeddingSparameters.return_value = 0
        mock_library.niRFSA_GetDeembeddingTableNumberOfPorts.side_effect = MockFunctionCallError("niRFSA_GetDeembeddingTableNumberOfPorts")
        mock_library.niRFSA_GetDeembeddingTableNumberOfPorts.return_value = 0
        mock_library.niRFSA_GetError.side_effect = MockFunctionCallError("niRFSA_GetError")
        mock_library.niRFSA_GetError.return_value = 0
        mock_library.niRFSA_GetExtCalLastDateAndTime.side_effect = MockFunctionCallError("niRFSA_GetExtCalLastDateAndTime")
        mock_library.niRFSA_GetExtCalLastDateAndTime.return_value = 0
        mock_library.niRFSA_GetExtCalRecommendedInterval.side_effect = MockFunctionCallError("niRFSA_GetExtCalRecommendedInterval")
        mock_library.niRFSA_GetExtCalRecommendedInterval.return_value = 0
        mock_library.niRFSA_GetFetchBacklog.side_effect = MockFunctionCallError("niRFSA_GetFetchBacklog")
        mock_library.niRFSA_GetFetchBacklog.return_value = 0
        mock_library.niRFSA_GetFrequencyResponse.side_effect = MockFunctionCallError("niRFSA_GetFrequencyResponse")
        mock_library.niRFSA_GetFrequencyResponse.return_value = 0
        mock_library.niRFSA_GetScalingCoefficients.side_effect = MockFunctionCallError("niRFSA_GetScalingCoefficients")
        mock_library.niRFSA_GetScalingCoefficients.return_value = 0
        mock_library.niRFSA_GetSelfCalLastDateAndTime.side_effect = MockFunctionCallError("niRFSA_GetSelfCalLastDateAndTime")
        mock_library.niRFSA_GetSelfCalLastDateAndTime.return_value = 0
        mock_library.niRFSA_GetSelfCalLastTemp.side_effect = MockFunctionCallError("niRFSA_GetSelfCalLastTemp")
        mock_library.niRFSA_GetSelfCalLastTemp.return_value = 0
        mock_library.niRFSA_GetTerminalName.side_effect = MockFunctionCallError("niRFSA_GetTerminalName")
        mock_library.niRFSA_GetTerminalName.return_value = 0
        mock_library.niRFSA_InitWithOptions.side_effect = MockFunctionCallError("niRFSA_InitWithOptions")
        mock_library.niRFSA_InitWithOptions.return_value = 0
        mock_library.niRFSA_Initiate.side_effect = MockFunctionCallError("niRFSA_Initiate")
        mock_library.niRFSA_Initiate.return_value = 0
        mock_library.niRFSA_IsSelfCalValid.side_effect = MockFunctionCallError("niRFSA_IsSelfCalValid")
        mock_library.niRFSA_IsSelfCalValid.return_value = 0
        mock_library.niRFSA_LoadConfigurationsFromFile.side_effect = MockFunctionCallError("niRFSA_LoadConfigurationsFromFile")
        mock_library.niRFSA_LoadConfigurationsFromFile.return_value = 0
        mock_library.niRFSA_LockSession.side_effect = MockFunctionCallError("niRFSA_LockSession")
        mock_library.niRFSA_LockSession.return_value = 0
        mock_library.niRFSA_PerformThermalCorrection.side_effect = MockFunctionCallError("niRFSA_PerformThermalCorrection")
        mock_library.niRFSA_PerformThermalCorrection.return_value = 0
        mock_library.niRFSA_ReadIQSingleRecordComplexF64.side_effect = MockFunctionCallError("niRFSA_ReadIQSingleRecordComplexF64")
        mock_library.niRFSA_ReadIQSingleRecordComplexF64.return_value = 0
        mock_library.niRFSA_ReadPowerSpectrumF32.side_effect = MockFunctionCallError("niRFSA_ReadPowerSpectrumF32")
        mock_library.niRFSA_ReadPowerSpectrumF32.return_value = 0
        mock_library.niRFSA_ReadPowerSpectrumF64.side_effect = MockFunctionCallError("niRFSA_ReadPowerSpectrumF64")
        mock_library.niRFSA_ReadPowerSpectrumF64.return_value = 0
        mock_library.niRFSA_ResetDevice.side_effect = MockFunctionCallError("niRFSA_ResetDevice")
        mock_library.niRFSA_ResetDevice.return_value = 0
        mock_library.niRFSA_ResetWithOptions.side_effect = MockFunctionCallError("niRFSA_ResetWithOptions")
        mock_library.niRFSA_ResetWithOptions.return_value = 0
        mock_library.niRFSA_SaveConfigurationsToFile.side_effect = MockFunctionCallError("niRFSA_SaveConfigurationsToFile")
        mock_library.niRFSA_SaveConfigurationsToFile.return_value = 0
        mock_library.niRFSA_SelfCalibrateRange.side_effect = MockFunctionCallError("niRFSA_SelfCalibrateRange")
        mock_library.niRFSA_SelfCalibrateRange.return_value = 0
        mock_library.niRFSA_SendSoftwareEdgeTrigger.side_effect = MockFunctionCallError("niRFSA_SendSoftwareEdgeTrigger")
        mock_library.niRFSA_SendSoftwareEdgeTrigger.return_value = 0
        mock_library.niRFSA_SetAttributeViBoolean.side_effect = MockFunctionCallError("niRFSA_SetAttributeViBoolean")
        mock_library.niRFSA_SetAttributeViBoolean.return_value = 0
        mock_library.niRFSA_SetAttributeViInt32.side_effect = MockFunctionCallError("niRFSA_SetAttributeViInt32")
        mock_library.niRFSA_SetAttributeViInt32.return_value = 0
        mock_library.niRFSA_SetAttributeViInt64.side_effect = MockFunctionCallError("niRFSA_SetAttributeViInt64")
        mock_library.niRFSA_SetAttributeViInt64.return_value = 0
        mock_library.niRFSA_SetAttributeViReal64.side_effect = MockFunctionCallError("niRFSA_SetAttributeViReal64")
        mock_library.niRFSA_SetAttributeViReal64.return_value = 0
        mock_library.niRFSA_SetAttributeViSession.side_effect = MockFunctionCallError("niRFSA_SetAttributeViSession")
        mock_library.niRFSA_SetAttributeViSession.return_value = 0
        mock_library.niRFSA_SetAttributeViString.side_effect = MockFunctionCallError("niRFSA_SetAttributeViString")
        mock_library.niRFSA_SetAttributeViString.return_value = 0
        mock_library.niRFSA_UnlockSession.side_effect = MockFunctionCallError("niRFSA_UnlockSession")
        mock_library.niRFSA_UnlockSession.return_value = 0
        mock_library.niRFSA_close.side_effect = MockFunctionCallError("niRFSA_close")
        mock_library.niRFSA_close.return_value = 0
        mock_library.niRFSA_reset.side_effect = MockFunctionCallError("niRFSA_reset")
        mock_library.niRFSA_reset.return_value = 0
        mock_library.niRFSA_self_test.side_effect = MockFunctionCallError("niRFSA_self_test")
        mock_library.niRFSA_self_test.return_value = 0
