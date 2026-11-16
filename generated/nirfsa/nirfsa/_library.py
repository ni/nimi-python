# -*- coding: utf-8 -*-
# This file was generated

import ctypes
import nirfsa.errors as errors
import threading

from nirfsa._complextype import *  # noqa: F403
from nirfsa._visatype import *  # noqa: F403,H303

import nirfsa.coefficient_info_type as coefficient_info_type  # noqa: F401

import nirfsa.waveform_info as waveform_info  # noqa: F401

import nirfsa.spectrum_info_type as spectrum_info_type  # noqa: F401


class Library(object):
    '''Library

    Wrapper around driver library.
    Class will setup the correct ctypes information for every function on first call.
    '''

    def __init__(self, ctypes_library):
        self._func_lock = threading.Lock()
        self._library = ctypes_library
        # We cache the cfunc object from the ctypes.CDLL object
        self.niRFSA_Abort_cfunc = None
        self.niRFSA_ChangeExternalCalibrationPassword_cfunc = None
        self.niRFSA_CheckAcquisitionStatus_cfunc = None
        self.niRFSA_ClearSelfCalibrateRange_cfunc = None
        self.niRFSA_Commit_cfunc = None
        self.niRFSA_ConfigureDeembeddingTableInterpolationLinear_cfunc = None
        self.niRFSA_ConfigureDeembeddingTableInterpolationNearest_cfunc = None
        self.niRFSA_ConfigureDeembeddingTableInterpolationSpline_cfunc = None
        self.niRFSA_ConfigureDigitalEdgeAdvanceTrigger_cfunc = None
        self.niRFSA_ConfigureDigitalEdgeRefTrigger_cfunc = None
        self.niRFSA_ConfigureDigitalEdgeStartTrigger_cfunc = None
        self.niRFSA_ConfigureIQPowerEdgeRefTrigger_cfunc = None
        self.niRFSA_ConfigureRefClock_cfunc = None
        self.niRFSA_ConfigureSoftwareEdgeAdvanceTrigger_cfunc = None
        self.niRFSA_ConfigureSoftwareEdgeRefTrigger_cfunc = None
        self.niRFSA_ConfigureSoftwareEdgeStartTrigger_cfunc = None
        self.niRFSA_ConfigureSpectrumFrequencyCenterSpan_cfunc = None
        self.niRFSA_ConfigureSpectrumFrequencyStartStop_cfunc = None
        self.niRFSA_CreateDeembeddingSparameterTableArray_cfunc = None
        self.niRFSA_CreateDeembeddingSparameterTableS2PFile_cfunc = None
        self.niRFSA_DeleteAllDeembeddingTables_cfunc = None
        self.niRFSA_DeleteDeembeddingTable_cfunc = None
        self.niRFSA_DisableAdvanceTrigger_cfunc = None
        self.niRFSA_DisableRefTrigger_cfunc = None
        self.niRFSA_DisableStartTrigger_cfunc = None
        self.niRFSA_EnableSessionAccess_cfunc = None
        self.niRFSA_ErrorMessage_cfunc = None
        self.niRFSA_FetchIQMultiRecordComplexF32_cfunc = None
        self.niRFSA_FetchIQMultiRecordComplexF64_cfunc = None
        self.niRFSA_FetchIQMultiRecordComplexI16_cfunc = None
        self.niRFSA_FetchIQSingleRecordComplexF32_cfunc = None
        self.niRFSA_FetchIQSingleRecordComplexF64_cfunc = None
        self.niRFSA_FetchIQSingleRecordComplexI16_cfunc = None
        self.niRFSA_GetAttributeViBoolean_cfunc = None
        self.niRFSA_GetAttributeViInt32_cfunc = None
        self.niRFSA_GetAttributeViInt64_cfunc = None
        self.niRFSA_GetAttributeViReal64_cfunc = None
        self.niRFSA_GetAttributeViSession_cfunc = None
        self.niRFSA_GetAttributeViString_cfunc = None
        self.niRFSA_GetDeembeddingSparameters_cfunc = None
        self.niRFSA_GetDeembeddingTableNumberOfPorts_cfunc = None
        self.niRFSA_GetError_cfunc = None
        self.niRFSA_GetExtCalLastDateAndTime_cfunc = None
        self.niRFSA_GetExtCalRecommendedInterval_cfunc = None
        self.niRFSA_GetFetchBacklog_cfunc = None
        self.niRFSA_GetFrequencyResponse_cfunc = None
        self.niRFSA_GetScalingCoefficients_cfunc = None
        self.niRFSA_GetSelfCalLastDateAndTime_cfunc = None
        self.niRFSA_GetSelfCalLastTemp_cfunc = None
        self.niRFSA_GetTerminalName_cfunc = None
        self.niRFSA_InitWithOptions_cfunc = None
        self.niRFSA_Initiate_cfunc = None
        self.niRFSA_IsSelfCalValid_cfunc = None
        self.niRFSA_LoadConfigurationsFromFile_cfunc = None
        self.niRFSA_LockSession_cfunc = None
        self.niRFSA_PerformThermalCorrection_cfunc = None
        self.niRFSA_ReadIQSingleRecordComplexF64_cfunc = None
        self.niRFSA_ReadPowerSpectrumF32_cfunc = None
        self.niRFSA_ReadPowerSpectrumF64_cfunc = None
        self.niRFSA_ResetDevice_cfunc = None
        self.niRFSA_ResetWithOptions_cfunc = None
        self.niRFSA_SaveConfigurationsToFile_cfunc = None
        self.niRFSA_SelfCalibrateRange_cfunc = None
        self.niRFSA_SendSoftwareEdgeTrigger_cfunc = None
        self.niRFSA_SetAttributeViBoolean_cfunc = None
        self.niRFSA_SetAttributeViInt32_cfunc = None
        self.niRFSA_SetAttributeViInt64_cfunc = None
        self.niRFSA_SetAttributeViReal64_cfunc = None
        self.niRFSA_SetAttributeViSession_cfunc = None
        self.niRFSA_SetAttributeViString_cfunc = None
        self.niRFSA_UnlockSession_cfunc = None
        self.niRFSA_close_cfunc = None
        self.niRFSA_reset_cfunc = None
        self.niRFSA_self_test_cfunc = None

    def _get_library_function(self, name):
        try:
            function = getattr(self._library, name)
        except AttributeError as e:
            raise errors.DriverTooOldError() from e
        return function

    def niRFSA_Abort(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_Abort_cfunc is None:
                self.niRFSA_Abort_cfunc = self._get_library_function('niRFSA_Abort')
                self.niRFSA_Abort_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSA_Abort_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_Abort_cfunc(vi)

    def niRFSA_ChangeExternalCalibrationPassword(self, vi, old_password, new_password):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ChangeExternalCalibrationPassword_cfunc is None:
                self.niRFSA_ChangeExternalCalibrationPassword_cfunc = self._get_library_function('niRFSA_ChangeExternalCalibrationPassword')
                self.niRFSA_ChangeExternalCalibrationPassword_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSA_ChangeExternalCalibrationPassword_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ChangeExternalCalibrationPassword_cfunc(vi, old_password, new_password)

    def niRFSA_CheckAcquisitionStatus(self, vi, is_done):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_CheckAcquisitionStatus_cfunc is None:
                self.niRFSA_CheckAcquisitionStatus_cfunc = self._get_library_function('niRFSA_CheckAcquisitionStatus')
                self.niRFSA_CheckAcquisitionStatus_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niRFSA_CheckAcquisitionStatus_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_CheckAcquisitionStatus_cfunc(vi, is_done)

    def niRFSA_ClearSelfCalibrateRange(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ClearSelfCalibrateRange_cfunc is None:
                self.niRFSA_ClearSelfCalibrateRange_cfunc = self._get_library_function('niRFSA_ClearSelfCalibrateRange')
                self.niRFSA_ClearSelfCalibrateRange_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSA_ClearSelfCalibrateRange_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ClearSelfCalibrateRange_cfunc(vi)

    def niRFSA_Commit(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_Commit_cfunc is None:
                self.niRFSA_Commit_cfunc = self._get_library_function('niRFSA_Commit')
                self.niRFSA_Commit_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSA_Commit_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_Commit_cfunc(vi)

    def niRFSA_ConfigureDeembeddingTableInterpolationLinear(self, vi, port, table_name, format):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ConfigureDeembeddingTableInterpolationLinear_cfunc is None:
                self.niRFSA_ConfigureDeembeddingTableInterpolationLinear_cfunc = self._get_library_function('niRFSA_ConfigureDeembeddingTableInterpolationLinear')
                self.niRFSA_ConfigureDeembeddingTableInterpolationLinear_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niRFSA_ConfigureDeembeddingTableInterpolationLinear_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ConfigureDeembeddingTableInterpolationLinear_cfunc(vi, port, table_name, format)

    def niRFSA_ConfigureDeembeddingTableInterpolationNearest(self, vi, port, table_name):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ConfigureDeembeddingTableInterpolationNearest_cfunc is None:
                self.niRFSA_ConfigureDeembeddingTableInterpolationNearest_cfunc = self._get_library_function('niRFSA_ConfigureDeembeddingTableInterpolationNearest')
                self.niRFSA_ConfigureDeembeddingTableInterpolationNearest_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSA_ConfigureDeembeddingTableInterpolationNearest_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ConfigureDeembeddingTableInterpolationNearest_cfunc(vi, port, table_name)

    def niRFSA_ConfigureDeembeddingTableInterpolationSpline(self, vi, port, table_name):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ConfigureDeembeddingTableInterpolationSpline_cfunc is None:
                self.niRFSA_ConfigureDeembeddingTableInterpolationSpline_cfunc = self._get_library_function('niRFSA_ConfigureDeembeddingTableInterpolationSpline')
                self.niRFSA_ConfigureDeembeddingTableInterpolationSpline_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSA_ConfigureDeembeddingTableInterpolationSpline_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ConfigureDeembeddingTableInterpolationSpline_cfunc(vi, port, table_name)

    def niRFSA_ConfigureDigitalEdgeAdvanceTrigger(self, vi, source, edge):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ConfigureDigitalEdgeAdvanceTrigger_cfunc is None:
                self.niRFSA_ConfigureDigitalEdgeAdvanceTrigger_cfunc = self._get_library_function('niRFSA_ConfigureDigitalEdgeAdvanceTrigger')
                self.niRFSA_ConfigureDigitalEdgeAdvanceTrigger_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niRFSA_ConfigureDigitalEdgeAdvanceTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ConfigureDigitalEdgeAdvanceTrigger_cfunc(vi, source, edge)

    def niRFSA_ConfigureDigitalEdgeRefTrigger(self, vi, source, edge, pretrigger_samples):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ConfigureDigitalEdgeRefTrigger_cfunc is None:
                self.niRFSA_ConfigureDigitalEdgeRefTrigger_cfunc = self._get_library_function('niRFSA_ConfigureDigitalEdgeRefTrigger')
                self.niRFSA_ConfigureDigitalEdgeRefTrigger_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViInt64]  # noqa: F405
                self.niRFSA_ConfigureDigitalEdgeRefTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ConfigureDigitalEdgeRefTrigger_cfunc(vi, source, edge, pretrigger_samples)

    def niRFSA_ConfigureDigitalEdgeStartTrigger(self, vi, source, edge):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ConfigureDigitalEdgeStartTrigger_cfunc is None:
                self.niRFSA_ConfigureDigitalEdgeStartTrigger_cfunc = self._get_library_function('niRFSA_ConfigureDigitalEdgeStartTrigger')
                self.niRFSA_ConfigureDigitalEdgeStartTrigger_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niRFSA_ConfigureDigitalEdgeStartTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ConfigureDigitalEdgeStartTrigger_cfunc(vi, source, edge)

    def niRFSA_ConfigureIQPowerEdgeRefTrigger(self, vi, source, level, slope, pretrigger_samples):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ConfigureIQPowerEdgeRefTrigger_cfunc is None:
                self.niRFSA_ConfigureIQPowerEdgeRefTrigger_cfunc = self._get_library_function('niRFSA_ConfigureIQPowerEdgeRefTrigger')
                self.niRFSA_ConfigureIQPowerEdgeRefTrigger_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViInt32, ViInt64]  # noqa: F405
                self.niRFSA_ConfigureIQPowerEdgeRefTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ConfigureIQPowerEdgeRefTrigger_cfunc(vi, source, level, slope, pretrigger_samples)

    def niRFSA_ConfigureRefClock(self, vi, clock_source, ref_clock_rate):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ConfigureRefClock_cfunc is None:
                self.niRFSA_ConfigureRefClock_cfunc = self._get_library_function('niRFSA_ConfigureRefClock')
                self.niRFSA_ConfigureRefClock_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64]  # noqa: F405
                self.niRFSA_ConfigureRefClock_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ConfigureRefClock_cfunc(vi, clock_source, ref_clock_rate)

    def niRFSA_ConfigureSoftwareEdgeAdvanceTrigger(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ConfigureSoftwareEdgeAdvanceTrigger_cfunc is None:
                self.niRFSA_ConfigureSoftwareEdgeAdvanceTrigger_cfunc = self._get_library_function('niRFSA_ConfigureSoftwareEdgeAdvanceTrigger')
                self.niRFSA_ConfigureSoftwareEdgeAdvanceTrigger_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSA_ConfigureSoftwareEdgeAdvanceTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ConfigureSoftwareEdgeAdvanceTrigger_cfunc(vi)

    def niRFSA_ConfigureSoftwareEdgeRefTrigger(self, vi, pretrigger_samples):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ConfigureSoftwareEdgeRefTrigger_cfunc is None:
                self.niRFSA_ConfigureSoftwareEdgeRefTrigger_cfunc = self._get_library_function('niRFSA_ConfigureSoftwareEdgeRefTrigger')
                self.niRFSA_ConfigureSoftwareEdgeRefTrigger_cfunc.argtypes = [ViSession, ViInt64]  # noqa: F405
                self.niRFSA_ConfigureSoftwareEdgeRefTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ConfigureSoftwareEdgeRefTrigger_cfunc(vi, pretrigger_samples)

    def niRFSA_ConfigureSoftwareEdgeStartTrigger(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ConfigureSoftwareEdgeStartTrigger_cfunc is None:
                self.niRFSA_ConfigureSoftwareEdgeStartTrigger_cfunc = self._get_library_function('niRFSA_ConfigureSoftwareEdgeStartTrigger')
                self.niRFSA_ConfigureSoftwareEdgeStartTrigger_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSA_ConfigureSoftwareEdgeStartTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ConfigureSoftwareEdgeStartTrigger_cfunc(vi)

    def niRFSA_ConfigureSpectrumFrequencyCenterSpan(self, vi, channel_list, center_frequency, span):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ConfigureSpectrumFrequencyCenterSpan_cfunc is None:
                self.niRFSA_ConfigureSpectrumFrequencyCenterSpan_cfunc = self._get_library_function('niRFSA_ConfigureSpectrumFrequencyCenterSpan')
                self.niRFSA_ConfigureSpectrumFrequencyCenterSpan_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViReal64]  # noqa: F405
                self.niRFSA_ConfigureSpectrumFrequencyCenterSpan_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ConfigureSpectrumFrequencyCenterSpan_cfunc(vi, channel_list, center_frequency, span)

    def niRFSA_ConfigureSpectrumFrequencyStartStop(self, vi, channel_list, start_frequency, stop_frequency):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ConfigureSpectrumFrequencyStartStop_cfunc is None:
                self.niRFSA_ConfigureSpectrumFrequencyStartStop_cfunc = self._get_library_function('niRFSA_ConfigureSpectrumFrequencyStartStop')
                self.niRFSA_ConfigureSpectrumFrequencyStartStop_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViReal64]  # noqa: F405
                self.niRFSA_ConfigureSpectrumFrequencyStartStop_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ConfigureSpectrumFrequencyStartStop_cfunc(vi, channel_list, start_frequency, stop_frequency)

    def niRFSA_CreateDeembeddingSparameterTableArray(self, vi, port, table_name, frequencies, frequencies_size, sparameter_table, sparameter_table_size, number_of_ports, sparameter_orientation):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_CreateDeembeddingSparameterTableArray_cfunc is None:
                self.niRFSA_CreateDeembeddingSparameterTableArray_cfunc = self._get_library_function('niRFSA_CreateDeembeddingSparameterTableArray')
                self.niRFSA_CreateDeembeddingSparameterTableArray_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViReal64), ViInt32, ctypes.POINTER(NIComplexNumber), ViInt32, ViInt32, ViInt32]  # noqa: F405
                self.niRFSA_CreateDeembeddingSparameterTableArray_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_CreateDeembeddingSparameterTableArray_cfunc(vi, port, table_name, frequencies, frequencies_size, sparameter_table, sparameter_table_size, number_of_ports, sparameter_orientation)

    def niRFSA_CreateDeembeddingSparameterTableS2PFile(self, vi, port, table_name, s2p_file_path, sparameter_orientation):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_CreateDeembeddingSparameterTableS2PFile_cfunc is None:
                self.niRFSA_CreateDeembeddingSparameterTableS2PFile_cfunc = self._get_library_function('niRFSA_CreateDeembeddingSparameterTableS2PFile')
                self.niRFSA_CreateDeembeddingSparameterTableS2PFile_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niRFSA_CreateDeembeddingSparameterTableS2PFile_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_CreateDeembeddingSparameterTableS2PFile_cfunc(vi, port, table_name, s2p_file_path, sparameter_orientation)

    def niRFSA_DeleteAllDeembeddingTables(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_DeleteAllDeembeddingTables_cfunc is None:
                self.niRFSA_DeleteAllDeembeddingTables_cfunc = self._get_library_function('niRFSA_DeleteAllDeembeddingTables')
                self.niRFSA_DeleteAllDeembeddingTables_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSA_DeleteAllDeembeddingTables_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_DeleteAllDeembeddingTables_cfunc(vi)

    def niRFSA_DeleteDeembeddingTable(self, vi, port, table_name):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_DeleteDeembeddingTable_cfunc is None:
                self.niRFSA_DeleteDeembeddingTable_cfunc = self._get_library_function('niRFSA_DeleteDeembeddingTable')
                self.niRFSA_DeleteDeembeddingTable_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSA_DeleteDeembeddingTable_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_DeleteDeembeddingTable_cfunc(vi, port, table_name)

    def niRFSA_DisableAdvanceTrigger(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_DisableAdvanceTrigger_cfunc is None:
                self.niRFSA_DisableAdvanceTrigger_cfunc = self._get_library_function('niRFSA_DisableAdvanceTrigger')
                self.niRFSA_DisableAdvanceTrigger_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSA_DisableAdvanceTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_DisableAdvanceTrigger_cfunc(vi)

    def niRFSA_DisableRefTrigger(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_DisableRefTrigger_cfunc is None:
                self.niRFSA_DisableRefTrigger_cfunc = self._get_library_function('niRFSA_DisableRefTrigger')
                self.niRFSA_DisableRefTrigger_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSA_DisableRefTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_DisableRefTrigger_cfunc(vi)

    def niRFSA_DisableStartTrigger(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_DisableStartTrigger_cfunc is None:
                self.niRFSA_DisableStartTrigger_cfunc = self._get_library_function('niRFSA_DisableStartTrigger')
                self.niRFSA_DisableStartTrigger_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSA_DisableStartTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_DisableStartTrigger_cfunc(vi)

    def niRFSA_EnableSessionAccess(self, vi, enable):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_EnableSessionAccess_cfunc is None:
                self.niRFSA_EnableSessionAccess_cfunc = self._get_library_function('niRFSA_EnableSessionAccess')
                self.niRFSA_EnableSessionAccess_cfunc.argtypes = [ViSession, ViBoolean]  # noqa: F405
                self.niRFSA_EnableSessionAccess_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_EnableSessionAccess_cfunc(vi, enable)

    def niRFSA_ErrorMessage(self, vi, error_code, error_message):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ErrorMessage_cfunc is None:
                self.niRFSA_ErrorMessage_cfunc = self._get_library_function('niRFSA_ErrorMessage')
                self.niRFSA_ErrorMessage_cfunc.argtypes = [ViSession, ViStatus, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSA_ErrorMessage_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ErrorMessage_cfunc(vi, error_code, error_message)

    def niRFSA_FetchIQMultiRecordComplexF32(self, vi, channel_list, starting_record, number_of_records, number_of_samples, timeout, iq_data_arrays, wfm_info):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_FetchIQMultiRecordComplexF32_cfunc is None:
                self.niRFSA_FetchIQMultiRecordComplexF32_cfunc = self._get_library_function('niRFSA_FetchIQMultiRecordComplexF32')
                self.niRFSA_FetchIQMultiRecordComplexF32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt64, ViInt64, ViInt64, ViReal64, ctypes.POINTER(NIComplexNumberF32), ctypes.POINTER(waveform_info.struct_niRFSA_wfmInfo)]  # noqa: F405
                self.niRFSA_FetchIQMultiRecordComplexF32_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_FetchIQMultiRecordComplexF32_cfunc(vi, channel_list, starting_record, number_of_records, number_of_samples, timeout, iq_data_arrays, wfm_info)

    def niRFSA_FetchIQMultiRecordComplexF64(self, vi, channel_list, starting_record, number_of_records, number_of_samples, timeout, iq_data_arrays, wfm_info):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_FetchIQMultiRecordComplexF64_cfunc is None:
                self.niRFSA_FetchIQMultiRecordComplexF64_cfunc = self._get_library_function('niRFSA_FetchIQMultiRecordComplexF64')
                self.niRFSA_FetchIQMultiRecordComplexF64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt64, ViInt64, ViInt64, ViReal64, ctypes.POINTER(NIComplexNumber), ctypes.POINTER(waveform_info.struct_niRFSA_wfmInfo)]  # noqa: F405
                self.niRFSA_FetchIQMultiRecordComplexF64_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_FetchIQMultiRecordComplexF64_cfunc(vi, channel_list, starting_record, number_of_records, number_of_samples, timeout, iq_data_arrays, wfm_info)

    def niRFSA_FetchIQMultiRecordComplexI16(self, vi, channel_list, starting_record, number_of_records, number_of_samples, timeout, iq_data_arrays, wfm_info):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_FetchIQMultiRecordComplexI16_cfunc is None:
                self.niRFSA_FetchIQMultiRecordComplexI16_cfunc = self._get_library_function('niRFSA_FetchIQMultiRecordComplexI16')
                self.niRFSA_FetchIQMultiRecordComplexI16_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt64, ViInt64, ViInt64, ViReal64, ctypes.POINTER(NIComplexI16), ctypes.POINTER(waveform_info.struct_niRFSA_wfmInfo)]  # noqa: F405
                self.niRFSA_FetchIQMultiRecordComplexI16_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_FetchIQMultiRecordComplexI16_cfunc(vi, channel_list, starting_record, number_of_records, number_of_samples, timeout, iq_data_arrays, wfm_info)

    def niRFSA_FetchIQSingleRecordComplexF32(self, vi, channel_list, record_number, number_of_samples, timeout, iq_data_array, wfm_info):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_FetchIQSingleRecordComplexF32_cfunc is None:
                self.niRFSA_FetchIQSingleRecordComplexF32_cfunc = self._get_library_function('niRFSA_FetchIQSingleRecordComplexF32')
                self.niRFSA_FetchIQSingleRecordComplexF32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt64, ViInt64, ViReal64, ctypes.POINTER(NIComplexNumberF32), ctypes.POINTER(waveform_info.struct_niRFSA_wfmInfo)]  # noqa: F405
                self.niRFSA_FetchIQSingleRecordComplexF32_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_FetchIQSingleRecordComplexF32_cfunc(vi, channel_list, record_number, number_of_samples, timeout, iq_data_array, wfm_info)

    def niRFSA_FetchIQSingleRecordComplexF64(self, vi, channel_list, record_number, number_of_samples, timeout, iq_data_array, wfm_info):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_FetchIQSingleRecordComplexF64_cfunc is None:
                self.niRFSA_FetchIQSingleRecordComplexF64_cfunc = self._get_library_function('niRFSA_FetchIQSingleRecordComplexF64')
                self.niRFSA_FetchIQSingleRecordComplexF64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt64, ViInt64, ViReal64, ctypes.POINTER(NIComplexNumber), ctypes.POINTER(waveform_info.struct_niRFSA_wfmInfo)]  # noqa: F405
                self.niRFSA_FetchIQSingleRecordComplexF64_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_FetchIQSingleRecordComplexF64_cfunc(vi, channel_list, record_number, number_of_samples, timeout, iq_data_array, wfm_info)

    def niRFSA_FetchIQSingleRecordComplexI16(self, vi, channel_list, record_number, number_of_samples, timeout, iq_data_array, wfm_info):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_FetchIQSingleRecordComplexI16_cfunc is None:
                self.niRFSA_FetchIQSingleRecordComplexI16_cfunc = self._get_library_function('niRFSA_FetchIQSingleRecordComplexI16')
                self.niRFSA_FetchIQSingleRecordComplexI16_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt64, ViInt64, ViReal64, ctypes.POINTER(NIComplexI16), ctypes.POINTER(waveform_info.struct_niRFSA_wfmInfo)]  # noqa: F405
                self.niRFSA_FetchIQSingleRecordComplexI16_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_FetchIQSingleRecordComplexI16_cfunc(vi, channel_list, record_number, number_of_samples, timeout, iq_data_array, wfm_info)

    def niRFSA_GetAttributeViBoolean(self, vi, channel_name, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetAttributeViBoolean_cfunc is None:
                self.niRFSA_GetAttributeViBoolean_cfunc = self._get_library_function('niRFSA_GetAttributeViBoolean')
                self.niRFSA_GetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niRFSA_GetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetAttributeViBoolean_cfunc(vi, channel_name, attribute_id, value)

    def niRFSA_GetAttributeViInt32(self, vi, channel_name, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetAttributeViInt32_cfunc is None:
                self.niRFSA_GetAttributeViInt32_cfunc = self._get_library_function('niRFSA_GetAttributeViInt32')
                self.niRFSA_GetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niRFSA_GetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetAttributeViInt32_cfunc(vi, channel_name, attribute_id, value)

    def niRFSA_GetAttributeViInt64(self, vi, channel_name, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetAttributeViInt64_cfunc is None:
                self.niRFSA_GetAttributeViInt64_cfunc = self._get_library_function('niRFSA_GetAttributeViInt64')
                self.niRFSA_GetAttributeViInt64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViInt64)]  # noqa: F405
                self.niRFSA_GetAttributeViInt64_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetAttributeViInt64_cfunc(vi, channel_name, attribute_id, value)

    def niRFSA_GetAttributeViReal64(self, vi, channel_name, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetAttributeViReal64_cfunc is None:
                self.niRFSA_GetAttributeViReal64_cfunc = self._get_library_function('niRFSA_GetAttributeViReal64')
                self.niRFSA_GetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niRFSA_GetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetAttributeViReal64_cfunc(vi, channel_name, attribute_id, value)

    def niRFSA_GetAttributeViSession(self, vi, channel_name, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetAttributeViSession_cfunc is None:
                self.niRFSA_GetAttributeViSession_cfunc = self._get_library_function('niRFSA_GetAttributeViSession')
                self.niRFSA_GetAttributeViSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViSession)]  # noqa: F405
                self.niRFSA_GetAttributeViSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetAttributeViSession_cfunc(vi, channel_name, attribute_id, value)

    def niRFSA_GetAttributeViString(self, vi, channel_name, attribute_id, buf_size, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetAttributeViString_cfunc is None:
                self.niRFSA_GetAttributeViString_cfunc = self._get_library_function('niRFSA_GetAttributeViString')
                self.niRFSA_GetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSA_GetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetAttributeViString_cfunc(vi, channel_name, attribute_id, buf_size, value)

    def niRFSA_GetDeembeddingSparameters(self, vi, sparameters, sparameters_array_size, number_of_sparameters, number_of_ports):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetDeembeddingSparameters_cfunc is None:
                self.niRFSA_GetDeembeddingSparameters_cfunc = self._get_library_function('niRFSA_GetDeembeddingSparameters')
                self.niRFSA_GetDeembeddingSparameters_cfunc.argtypes = [ViSession, ctypes.POINTER(NIComplexNumber), ViInt32, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niRFSA_GetDeembeddingSparameters_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetDeembeddingSparameters_cfunc(vi, sparameters, sparameters_array_size, number_of_sparameters, number_of_ports)

    def niRFSA_GetDeembeddingTableNumberOfPorts(self, vi, number_of_ports):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetDeembeddingTableNumberOfPorts_cfunc is None:
                self.niRFSA_GetDeembeddingTableNumberOfPorts_cfunc = self._get_library_function('niRFSA_GetDeembeddingTableNumberOfPorts')
                self.niRFSA_GetDeembeddingTableNumberOfPorts_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niRFSA_GetDeembeddingTableNumberOfPorts_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetDeembeddingTableNumberOfPorts_cfunc(vi, number_of_ports)

    def niRFSA_GetError(self, vi, error_code, error_description_buffer_size, error_description):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetError_cfunc is None:
                self.niRFSA_GetError_cfunc = self._get_library_function('niRFSA_GetError')
                self.niRFSA_GetError_cfunc.argtypes = [ViSession, ctypes.POINTER(ViStatus), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSA_GetError_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetError_cfunc(vi, error_code, error_description_buffer_size, error_description)

    def niRFSA_GetExtCalLastDateAndTime(self, vi, year, month, day, hour, minute):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetExtCalLastDateAndTime_cfunc is None:
                self.niRFSA_GetExtCalLastDateAndTime_cfunc = self._get_library_function('niRFSA_GetExtCalLastDateAndTime')
                self.niRFSA_GetExtCalLastDateAndTime_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niRFSA_GetExtCalLastDateAndTime_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetExtCalLastDateAndTime_cfunc(vi, year, month, day, hour, minute)

    def niRFSA_GetExtCalRecommendedInterval(self, vi, months):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetExtCalRecommendedInterval_cfunc is None:
                self.niRFSA_GetExtCalRecommendedInterval_cfunc = self._get_library_function('niRFSA_GetExtCalRecommendedInterval')
                self.niRFSA_GetExtCalRecommendedInterval_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niRFSA_GetExtCalRecommendedInterval_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetExtCalRecommendedInterval_cfunc(vi, months)

    def niRFSA_GetFetchBacklog(self, vi, channel_list, record_number, backlog):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetFetchBacklog_cfunc is None:
                self.niRFSA_GetFetchBacklog_cfunc = self._get_library_function('niRFSA_GetFetchBacklog')
                self.niRFSA_GetFetchBacklog_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt64, ctypes.POINTER(ViInt64)]  # noqa: F405
                self.niRFSA_GetFetchBacklog_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetFetchBacklog_cfunc(vi, channel_list, record_number, backlog)

    def niRFSA_GetFrequencyResponse(self, vi, channel_list, buffer_size, frequencies, magnitude_response, phase_response, number_of_frequencies):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetFrequencyResponse_cfunc is None:
                self.niRFSA_GetFrequencyResponse_cfunc = self._get_library_function('niRFSA_GetFrequencyResponse')
                self.niRFSA_GetFrequencyResponse_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niRFSA_GetFrequencyResponse_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetFrequencyResponse_cfunc(vi, channel_list, buffer_size, frequencies, magnitude_response, phase_response, number_of_frequencies)

    def niRFSA_GetScalingCoefficients(self, vi, channel_list, array_size, coefficient_info, number_of_coefficient_sets):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetScalingCoefficients_cfunc is None:
                self.niRFSA_GetScalingCoefficients_cfunc = self._get_library_function('niRFSA_GetScalingCoefficients')
                self.niRFSA_GetScalingCoefficients_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(coefficient_info_type.struct_niRFSA_coefficientInfo), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niRFSA_GetScalingCoefficients_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetScalingCoefficients_cfunc(vi, channel_list, array_size, coefficient_info, number_of_coefficient_sets)

    def niRFSA_GetSelfCalLastDateAndTime(self, vi, self_calibration_step, year, month, day, hour, minute):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetSelfCalLastDateAndTime_cfunc is None:
                self.niRFSA_GetSelfCalLastDateAndTime_cfunc = self._get_library_function('niRFSA_GetSelfCalLastDateAndTime')
                self.niRFSA_GetSelfCalLastDateAndTime_cfunc.argtypes = [ViSession, ViInt64, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niRFSA_GetSelfCalLastDateAndTime_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetSelfCalLastDateAndTime_cfunc(vi, self_calibration_step, year, month, day, hour, minute)

    def niRFSA_GetSelfCalLastTemp(self, vi, self_calibration_step, temperature):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetSelfCalLastTemp_cfunc is None:
                self.niRFSA_GetSelfCalLastTemp_cfunc = self._get_library_function('niRFSA_GetSelfCalLastTemp')
                self.niRFSA_GetSelfCalLastTemp_cfunc.argtypes = [ViSession, ViInt64, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niRFSA_GetSelfCalLastTemp_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetSelfCalLastTemp_cfunc(vi, self_calibration_step, temperature)

    def niRFSA_GetTerminalName(self, vi, signal, signal_identifier, buffer_size, terminal_name):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_GetTerminalName_cfunc is None:
                self.niRFSA_GetTerminalName_cfunc = self._get_library_function('niRFSA_GetTerminalName')
                self.niRFSA_GetTerminalName_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSA_GetTerminalName_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_GetTerminalName_cfunc(vi, signal, signal_identifier, buffer_size, terminal_name)

    def niRFSA_InitWithOptions(self, resource_name, id_query, reset_device, option_string, new_vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_InitWithOptions_cfunc is None:
                self.niRFSA_InitWithOptions_cfunc = self._get_library_function('niRFSA_InitWithOptions')
                self.niRFSA_InitWithOptions_cfunc.argtypes = [ctypes.POINTER(ViChar), ViBoolean, ViBoolean, ctypes.POINTER(ViChar), ctypes.POINTER(ViSession)]  # noqa: F405
                self.niRFSA_InitWithOptions_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_InitWithOptions_cfunc(resource_name, id_query, reset_device, option_string, new_vi)

    def niRFSA_Initiate(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_Initiate_cfunc is None:
                self.niRFSA_Initiate_cfunc = self._get_library_function('niRFSA_Initiate')
                self.niRFSA_Initiate_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSA_Initiate_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_Initiate_cfunc(vi)

    def niRFSA_IsSelfCalValid(self, vi, self_cal_valid, valid_steps):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_IsSelfCalValid_cfunc is None:
                self.niRFSA_IsSelfCalValid_cfunc = self._get_library_function('niRFSA_IsSelfCalValid')
                self.niRFSA_IsSelfCalValid_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean), ctypes.POINTER(ViInt64)]  # noqa: F405
                self.niRFSA_IsSelfCalValid_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_IsSelfCalValid_cfunc(vi, self_cal_valid, valid_steps)

    def niRFSA_LoadConfigurationsFromFile(self, vi, channel_name, file_path):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_LoadConfigurationsFromFile_cfunc is None:
                self.niRFSA_LoadConfigurationsFromFile_cfunc = self._get_library_function('niRFSA_LoadConfigurationsFromFile')
                self.niRFSA_LoadConfigurationsFromFile_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSA_LoadConfigurationsFromFile_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_LoadConfigurationsFromFile_cfunc(vi, channel_name, file_path)

    def niRFSA_LockSession(self, vi, caller_has_lock):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_LockSession_cfunc is None:
                self.niRFSA_LockSession_cfunc = self._get_library_function('niRFSA_LockSession')
                self.niRFSA_LockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niRFSA_LockSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_LockSession_cfunc(vi, caller_has_lock)

    def niRFSA_PerformThermalCorrection(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_PerformThermalCorrection_cfunc is None:
                self.niRFSA_PerformThermalCorrection_cfunc = self._get_library_function('niRFSA_PerformThermalCorrection')
                self.niRFSA_PerformThermalCorrection_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSA_PerformThermalCorrection_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_PerformThermalCorrection_cfunc(vi)

    def niRFSA_ReadIQSingleRecordComplexF64(self, vi, channel_list, timeout, iq_data_array, data_array_size, wfm_info):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ReadIQSingleRecordComplexF64_cfunc is None:
                self.niRFSA_ReadIQSingleRecordComplexF64_cfunc = self._get_library_function('niRFSA_ReadIQSingleRecordComplexF64')
                self.niRFSA_ReadIQSingleRecordComplexF64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ctypes.POINTER(NIComplexNumber), ViInt64, ctypes.POINTER(waveform_info.struct_niRFSA_wfmInfo)]  # noqa: F405
                self.niRFSA_ReadIQSingleRecordComplexF64_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ReadIQSingleRecordComplexF64_cfunc(vi, channel_list, timeout, iq_data_array, data_array_size, wfm_info)

    def niRFSA_ReadPowerSpectrumF32(self, vi, channel_list, timeout, power_spectrum_data_array, data_array_size, spectrum_info):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ReadPowerSpectrumF32_cfunc is None:
                self.niRFSA_ReadPowerSpectrumF32_cfunc = self._get_library_function('niRFSA_ReadPowerSpectrumF32')
                self.niRFSA_ReadPowerSpectrumF32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ctypes.POINTER(ViReal32), ViInt32, ctypes.POINTER(spectrum_info_type.struct_niRFSA_spectrumInfo)]  # noqa: F405
                self.niRFSA_ReadPowerSpectrumF32_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ReadPowerSpectrumF32_cfunc(vi, channel_list, timeout, power_spectrum_data_array, data_array_size, spectrum_info)

    def niRFSA_ReadPowerSpectrumF64(self, vi, channel_list, timeout, power_spectrum_data_array, data_array_size, spectrum_info):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ReadPowerSpectrumF64_cfunc is None:
                self.niRFSA_ReadPowerSpectrumF64_cfunc = self._get_library_function('niRFSA_ReadPowerSpectrumF64')
                self.niRFSA_ReadPowerSpectrumF64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ctypes.POINTER(ViReal64), ViInt32, ctypes.POINTER(spectrum_info_type.struct_niRFSA_spectrumInfo)]  # noqa: F405
                self.niRFSA_ReadPowerSpectrumF64_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ReadPowerSpectrumF64_cfunc(vi, channel_list, timeout, power_spectrum_data_array, data_array_size, spectrum_info)

    def niRFSA_ResetDevice(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ResetDevice_cfunc is None:
                self.niRFSA_ResetDevice_cfunc = self._get_library_function('niRFSA_ResetDevice')
                self.niRFSA_ResetDevice_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSA_ResetDevice_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ResetDevice_cfunc(vi)

    def niRFSA_ResetWithOptions(self, vi, steps_to_omit):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_ResetWithOptions_cfunc is None:
                self.niRFSA_ResetWithOptions_cfunc = self._get_library_function('niRFSA_ResetWithOptions')
                self.niRFSA_ResetWithOptions_cfunc.argtypes = [ViSession, ViUInt64]  # noqa: F405
                self.niRFSA_ResetWithOptions_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_ResetWithOptions_cfunc(vi, steps_to_omit)

    def niRFSA_SaveConfigurationsToFile(self, vi, channel_name, file_path):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_SaveConfigurationsToFile_cfunc is None:
                self.niRFSA_SaveConfigurationsToFile_cfunc = self._get_library_function('niRFSA_SaveConfigurationsToFile')
                self.niRFSA_SaveConfigurationsToFile_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSA_SaveConfigurationsToFile_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_SaveConfigurationsToFile_cfunc(vi, channel_name, file_path)

    def niRFSA_SelfCalibrateRange(self, vi, steps_to_omit, minimum_frequency, maximum_frequency, minimum_reference_level, maximum_reference_level):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_SelfCalibrateRange_cfunc is None:
                self.niRFSA_SelfCalibrateRange_cfunc = self._get_library_function('niRFSA_SelfCalibrateRange')
                self.niRFSA_SelfCalibrateRange_cfunc.argtypes = [ViSession, ViInt64, ViReal64, ViReal64, ViReal64, ViReal64]  # noqa: F405
                self.niRFSA_SelfCalibrateRange_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_SelfCalibrateRange_cfunc(vi, steps_to_omit, minimum_frequency, maximum_frequency, minimum_reference_level, maximum_reference_level)

    def niRFSA_SendSoftwareEdgeTrigger(self, vi, trigger, trigger_identifier):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_SendSoftwareEdgeTrigger_cfunc is None:
                self.niRFSA_SendSoftwareEdgeTrigger_cfunc = self._get_library_function('niRFSA_SendSoftwareEdgeTrigger')
                self.niRFSA_SendSoftwareEdgeTrigger_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSA_SendSoftwareEdgeTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_SendSoftwareEdgeTrigger_cfunc(vi, trigger, trigger_identifier)

    def niRFSA_SetAttributeViBoolean(self, vi, channel_name, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_SetAttributeViBoolean_cfunc is None:
                self.niRFSA_SetAttributeViBoolean_cfunc = self._get_library_function('niRFSA_SetAttributeViBoolean')
                self.niRFSA_SetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViBoolean]  # noqa: F405
                self.niRFSA_SetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_SetAttributeViBoolean_cfunc(vi, channel_name, attribute_id, value)

    def niRFSA_SetAttributeViInt32(self, vi, channel_name, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_SetAttributeViInt32_cfunc is None:
                self.niRFSA_SetAttributeViInt32_cfunc = self._get_library_function('niRFSA_SetAttributeViInt32')
                self.niRFSA_SetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32]  # noqa: F405
                self.niRFSA_SetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_SetAttributeViInt32_cfunc(vi, channel_name, attribute_id, value)

    def niRFSA_SetAttributeViInt64(self, vi, channel_name, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_SetAttributeViInt64_cfunc is None:
                self.niRFSA_SetAttributeViInt64_cfunc = self._get_library_function('niRFSA_SetAttributeViInt64')
                self.niRFSA_SetAttributeViInt64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt64]  # noqa: F405
                self.niRFSA_SetAttributeViInt64_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_SetAttributeViInt64_cfunc(vi, channel_name, attribute_id, value)

    def niRFSA_SetAttributeViReal64(self, vi, channel_name, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_SetAttributeViReal64_cfunc is None:
                self.niRFSA_SetAttributeViReal64_cfunc = self._get_library_function('niRFSA_SetAttributeViReal64')
                self.niRFSA_SetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViReal64]  # noqa: F405
                self.niRFSA_SetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_SetAttributeViReal64_cfunc(vi, channel_name, attribute_id, value)

    def niRFSA_SetAttributeViSession(self, vi, channel_name, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_SetAttributeViSession_cfunc is None:
                self.niRFSA_SetAttributeViSession_cfunc = self._get_library_function('niRFSA_SetAttributeViSession')
                self.niRFSA_SetAttributeViSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViSession]  # noqa: F405
                self.niRFSA_SetAttributeViSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_SetAttributeViSession_cfunc(vi, channel_name, attribute_id, value)

    def niRFSA_SetAttributeViString(self, vi, channel_name, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_SetAttributeViString_cfunc is None:
                self.niRFSA_SetAttributeViString_cfunc = self._get_library_function('niRFSA_SetAttributeViString')
                self.niRFSA_SetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSA_SetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_SetAttributeViString_cfunc(vi, channel_name, attribute_id, value)

    def niRFSA_UnlockSession(self, vi, caller_has_lock):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_UnlockSession_cfunc is None:
                self.niRFSA_UnlockSession_cfunc = self._get_library_function('niRFSA_UnlockSession')
                self.niRFSA_UnlockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niRFSA_UnlockSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_UnlockSession_cfunc(vi, caller_has_lock)

    def niRFSA_close(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_close_cfunc is None:
                self.niRFSA_close_cfunc = self._get_library_function('niRFSA_close')
                self.niRFSA_close_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSA_close_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_close_cfunc(vi)

    def niRFSA_reset(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_reset_cfunc is None:
                self.niRFSA_reset_cfunc = self._get_library_function('niRFSA_reset')
                self.niRFSA_reset_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSA_reset_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_reset_cfunc(vi)

    def niRFSA_self_test(self, vi, self_test_result, self_test_message):  # noqa: N802
        with self._func_lock:
            if self.niRFSA_self_test_cfunc is None:
                self.niRFSA_self_test_cfunc = self._get_library_function('niRFSA_self_test')
                self.niRFSA_self_test_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt16), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSA_self_test_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSA_self_test_cfunc(vi, self_test_result, self_test_message)
