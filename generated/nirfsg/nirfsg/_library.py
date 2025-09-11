# -*- coding: utf-8 -*-
# This file was generated

import ctypes
import nirfsg.errors as errors
import threading

from nirfsg._complextype import *  # noqa: F403
from nirfsg._visatype import *  # noqa: F403,H303


class Library(object):
    '''Library

    Wrapper around driver library.
    Class will setup the correct ctypes information for every function on first call.
    '''

    def __init__(self, ctypes_library):
        self._func_lock = threading.Lock()
        self._library = ctypes_library
        # We cache the cfunc object from the ctypes.CDLL object
        self.niRFSG_Abort_cfunc = None
        self.niRFSG_AllocateArbWaveform_cfunc = None
        self.niRFSG_ChangeExternalCalibrationPassword_cfunc = None
        self.niRFSG_CheckAttributeViBoolean_cfunc = None
        self.niRFSG_CheckAttributeViInt32_cfunc = None
        self.niRFSG_CheckAttributeViInt64_cfunc = None
        self.niRFSG_CheckAttributeViReal64_cfunc = None
        self.niRFSG_CheckAttributeViSession_cfunc = None
        self.niRFSG_CheckAttributeViString_cfunc = None
        self.niRFSG_CheckGenerationStatus_cfunc = None
        self.niRFSG_CheckIfScriptExists_cfunc = None
        self.niRFSG_CheckIfWaveformExists_cfunc = None
        self.niRFSG_ClearAllArbWaveforms_cfunc = None
        self.niRFSG_ClearArbWaveform_cfunc = None
        self.niRFSG_ClearError_cfunc = None
        self.niRFSG_ClearSelfCalibrateRange_cfunc = None
        self.niRFSG_Commit_cfunc = None
        self.niRFSG_ConfigureDeembeddingTableInterpolationLinear_cfunc = None
        self.niRFSG_ConfigureDeembeddingTableInterpolationNearest_cfunc = None
        self.niRFSG_ConfigureDeembeddingTableInterpolationSpline_cfunc = None
        self.niRFSG_ConfigureDigitalEdgeScriptTrigger_cfunc = None
        self.niRFSG_ConfigureDigitalEdgeStartTrigger_cfunc = None
        self.niRFSG_ConfigureDigitalLevelScriptTrigger_cfunc = None
        self.niRFSG_ConfigureDigitalModulationUserDefinedWaveform_cfunc = None
        self.niRFSG_ConfigurePxiChassisClk10_cfunc = None
        self.niRFSG_ConfigureRF_cfunc = None
        self.niRFSG_ConfigureRefClock_cfunc = None
        self.niRFSG_ConfigureSoftwareScriptTrigger_cfunc = None
        self.niRFSG_ConfigureSoftwareStartTrigger_cfunc = None
        self.niRFSG_CreateDeembeddingSparameterTableArray_cfunc = None
        self.niRFSG_CreateDeembeddingSparameterTableS2PFile_cfunc = None
        self.niRFSG_DeleteAllDeembeddingTables_cfunc = None
        self.niRFSG_DeleteDeembeddingTable_cfunc = None
        self.niRFSG_Disable_cfunc = None
        self.niRFSG_DisableScriptTrigger_cfunc = None
        self.niRFSG_DisableStartTrigger_cfunc = None
        self.niRFSG_ErrorMessage_cfunc = None
        self.niRFSG_ErrorQuery_cfunc = None
        self.niRFSG_GetAllNamedWaveformNames_cfunc = None
        self.niRFSG_GetAllScriptNames_cfunc = None
        self.niRFSG_GetAttributeViBoolean_cfunc = None
        self.niRFSG_GetAttributeViInt32_cfunc = None
        self.niRFSG_GetAttributeViInt64_cfunc = None
        self.niRFSG_GetAttributeViReal64_cfunc = None
        self.niRFSG_GetAttributeViSession_cfunc = None
        self.niRFSG_GetAttributeViString_cfunc = None
        self.niRFSG_GetChannelName_cfunc = None
        self.niRFSG_GetDeembeddingSparameters_cfunc = None
        self.niRFSG_GetDeembeddingTableNumberOfPorts_cfunc = None
        self.niRFSG_GetError_cfunc = None
        self.niRFSG_GetExternalCalibrationLastDateAndTime_cfunc = None
        self.niRFSG_GetMaxSettablePower_cfunc = None
        self.niRFSG_GetSelfCalibrationDateAndTime_cfunc = None
        self.niRFSG_GetSelfCalibrationTemperature_cfunc = None
        self.niRFSG_GetTerminalName_cfunc = None
        self.niRFSG_GetWaveformBurstStartLocations_cfunc = None
        self.niRFSG_GetWaveformBurstStopLocations_cfunc = None
        self.niRFSG_GetWaveformMarkerEventLocations_cfunc = None
        self.niRFSG_InitWithOptions_cfunc = None
        self.niRFSG_Initiate_cfunc = None
        self.niRFSG_LoadConfigurationsFromFile_cfunc = None
        self.niRFSG_LockSession_cfunc = None
        self.niRFSG_PerformPowerSearch_cfunc = None
        self.niRFSG_PerformThermalCorrection_cfunc = None
        self.niRFSG_QueryArbWaveformCapabilities_cfunc = None
        self.niRFSG_ReadAndDownloadWaveformFromFileTDMS_cfunc = None
        self.niRFSG_ResetAttribute_cfunc = None
        self.niRFSG_ResetDevice_cfunc = None
        self.niRFSG_ResetWithDefaults_cfunc = None
        self.niRFSG_ResetWithOptions_cfunc = None
        self.niRFSG_RevisionQuery_cfunc = None
        self.niRFSG_SaveConfigurationsToFile_cfunc = None
        self.niRFSG_SelectArbWaveform_cfunc = None
        self.niRFSG_SelfCal_cfunc = None
        self.niRFSG_SelfCalibrateRange_cfunc = None
        self.niRFSG_SelfTest_cfunc = None
        self.niRFSG_SendSoftwareEdgeTrigger_cfunc = None
        self.niRFSG_SetArbWaveformNextWritePosition_cfunc = None
        self.niRFSG_SetAttributeViBoolean_cfunc = None
        self.niRFSG_SetAttributeViInt32_cfunc = None
        self.niRFSG_SetAttributeViInt64_cfunc = None
        self.niRFSG_SetAttributeViReal64_cfunc = None
        self.niRFSG_SetAttributeViSession_cfunc = None
        self.niRFSG_SetAttributeViString_cfunc = None
        self.niRFSG_SetWaveformBurstStartLocations_cfunc = None
        self.niRFSG_SetWaveformBurstStopLocations_cfunc = None
        self.niRFSG_SetWaveformMarkerEventLocations_cfunc = None
        self.niRFSG_UnlockSession_cfunc = None
        self.niRFSG_WaitUntilSettled_cfunc = None
        self.niRFSG_WriteArbWaveformComplexF32_cfunc = None
        self.niRFSG_WriteArbWaveformComplexF64_cfunc = None
        self.niRFSG_WriteArbWaveformComplexI16_cfunc = None
        self.niRFSG_WriteScript_cfunc = None
        self.niRFSG_close_cfunc = None
        self.niRFSG_reset_cfunc = None

    def _get_library_function(self, name):
        try:
            function = getattr(self._library, name)
        except AttributeError as e:
            raise errors.DriverTooOldError() from e
        return function

    def niRFSG_Abort(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_Abort_cfunc is None:
                self.niRFSG_Abort_cfunc = self._get_library_function('niRFSG_Abort')
                self.niRFSG_Abort_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSG_Abort_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_Abort_cfunc(vi)

    def niRFSG_AllocateArbWaveform(self, vi, waveform_name, size_in_samples):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_AllocateArbWaveform_cfunc is None:
                self.niRFSG_AllocateArbWaveform_cfunc = self._get_library_function('niRFSG_AllocateArbWaveform')
                self.niRFSG_AllocateArbWaveform_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niRFSG_AllocateArbWaveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_AllocateArbWaveform_cfunc(vi, waveform_name, size_in_samples)

    def niRFSG_ChangeExternalCalibrationPassword(self, vi, old_password, new_password):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_ChangeExternalCalibrationPassword_cfunc is None:
                self.niRFSG_ChangeExternalCalibrationPassword_cfunc = self._get_library_function('niRFSG_ChangeExternalCalibrationPassword')
                self.niRFSG_ChangeExternalCalibrationPassword_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSG_ChangeExternalCalibrationPassword_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_ChangeExternalCalibrationPassword_cfunc(vi, old_password, new_password)

    def niRFSG_CheckAttributeViBoolean(self, vi, channel_name, attribute, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_CheckAttributeViBoolean_cfunc is None:
                self.niRFSG_CheckAttributeViBoolean_cfunc = self._get_library_function('niRFSG_CheckAttributeViBoolean')
                self.niRFSG_CheckAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViBoolean]  # noqa: F405
                self.niRFSG_CheckAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_CheckAttributeViBoolean_cfunc(vi, channel_name, attribute, value)

    def niRFSG_CheckAttributeViInt32(self, vi, channel_name, attribute, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_CheckAttributeViInt32_cfunc is None:
                self.niRFSG_CheckAttributeViInt32_cfunc = self._get_library_function('niRFSG_CheckAttributeViInt32')
                self.niRFSG_CheckAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32]  # noqa: F405
                self.niRFSG_CheckAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_CheckAttributeViInt32_cfunc(vi, channel_name, attribute, value)

    def niRFSG_CheckAttributeViInt64(self, vi, channel_name, attribute, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_CheckAttributeViInt64_cfunc is None:
                self.niRFSG_CheckAttributeViInt64_cfunc = self._get_library_function('niRFSG_CheckAttributeViInt64')
                self.niRFSG_CheckAttributeViInt64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt64]  # noqa: F405
                self.niRFSG_CheckAttributeViInt64_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_CheckAttributeViInt64_cfunc(vi, channel_name, attribute, value)

    def niRFSG_CheckAttributeViReal64(self, vi, channel_name, attribute, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_CheckAttributeViReal64_cfunc is None:
                self.niRFSG_CheckAttributeViReal64_cfunc = self._get_library_function('niRFSG_CheckAttributeViReal64')
                self.niRFSG_CheckAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViReal64]  # noqa: F405
                self.niRFSG_CheckAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_CheckAttributeViReal64_cfunc(vi, channel_name, attribute, value)

    def niRFSG_CheckAttributeViSession(self, vi, channel_name, attribute, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_CheckAttributeViSession_cfunc is None:
                self.niRFSG_CheckAttributeViSession_cfunc = self._get_library_function('niRFSG_CheckAttributeViSession')
                self.niRFSG_CheckAttributeViSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViSession]  # noqa: F405
                self.niRFSG_CheckAttributeViSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_CheckAttributeViSession_cfunc(vi, channel_name, attribute, value)

    def niRFSG_CheckAttributeViString(self, vi, channel_name, attribute, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_CheckAttributeViString_cfunc is None:
                self.niRFSG_CheckAttributeViString_cfunc = self._get_library_function('niRFSG_CheckAttributeViString')
                self.niRFSG_CheckAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSG_CheckAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_CheckAttributeViString_cfunc(vi, channel_name, attribute, value)

    def niRFSG_CheckGenerationStatus(self, vi, is_done):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_CheckGenerationStatus_cfunc is None:
                self.niRFSG_CheckGenerationStatus_cfunc = self._get_library_function('niRFSG_CheckGenerationStatus')
                self.niRFSG_CheckGenerationStatus_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niRFSG_CheckGenerationStatus_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_CheckGenerationStatus_cfunc(vi, is_done)

    def niRFSG_CheckIfScriptExists(self, vi, script_name, script_exists):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_CheckIfScriptExists_cfunc is None:
                self.niRFSG_CheckIfScriptExists_cfunc = self._get_library_function('niRFSG_CheckIfScriptExists')
                self.niRFSG_CheckIfScriptExists_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niRFSG_CheckIfScriptExists_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_CheckIfScriptExists_cfunc(vi, script_name, script_exists)

    def niRFSG_CheckIfWaveformExists(self, vi, waveform_name, waveform_exists):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_CheckIfWaveformExists_cfunc is None:
                self.niRFSG_CheckIfWaveformExists_cfunc = self._get_library_function('niRFSG_CheckIfWaveformExists')
                self.niRFSG_CheckIfWaveformExists_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niRFSG_CheckIfWaveformExists_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_CheckIfWaveformExists_cfunc(vi, waveform_name, waveform_exists)

    def niRFSG_ClearAllArbWaveforms(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_ClearAllArbWaveforms_cfunc is None:
                self.niRFSG_ClearAllArbWaveforms_cfunc = self._get_library_function('niRFSG_ClearAllArbWaveforms')
                self.niRFSG_ClearAllArbWaveforms_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSG_ClearAllArbWaveforms_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_ClearAllArbWaveforms_cfunc(vi)

    def niRFSG_ClearArbWaveform(self, vi, name):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_ClearArbWaveform_cfunc is None:
                self.niRFSG_ClearArbWaveform_cfunc = self._get_library_function('niRFSG_ClearArbWaveform')
                self.niRFSG_ClearArbWaveform_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSG_ClearArbWaveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_ClearArbWaveform_cfunc(vi, name)

    def niRFSG_ClearError(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_ClearError_cfunc is None:
                self.niRFSG_ClearError_cfunc = self._get_library_function('niRFSG_ClearError')
                self.niRFSG_ClearError_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSG_ClearError_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_ClearError_cfunc(vi)

    def niRFSG_ClearSelfCalibrateRange(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_ClearSelfCalibrateRange_cfunc is None:
                self.niRFSG_ClearSelfCalibrateRange_cfunc = self._get_library_function('niRFSG_ClearSelfCalibrateRange')
                self.niRFSG_ClearSelfCalibrateRange_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSG_ClearSelfCalibrateRange_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_ClearSelfCalibrateRange_cfunc(vi)

    def niRFSG_Commit(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_Commit_cfunc is None:
                self.niRFSG_Commit_cfunc = self._get_library_function('niRFSG_Commit')
                self.niRFSG_Commit_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSG_Commit_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_Commit_cfunc(vi)

    def niRFSG_ConfigureDeembeddingTableInterpolationLinear(self, vi, port, table_name, format):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_ConfigureDeembeddingTableInterpolationLinear_cfunc is None:
                self.niRFSG_ConfigureDeembeddingTableInterpolationLinear_cfunc = self._get_library_function('niRFSG_ConfigureDeembeddingTableInterpolationLinear')
                self.niRFSG_ConfigureDeembeddingTableInterpolationLinear_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niRFSG_ConfigureDeembeddingTableInterpolationLinear_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_ConfigureDeembeddingTableInterpolationLinear_cfunc(vi, port, table_name, format)

    def niRFSG_ConfigureDeembeddingTableInterpolationNearest(self, vi, port, table_name):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_ConfigureDeembeddingTableInterpolationNearest_cfunc is None:
                self.niRFSG_ConfigureDeembeddingTableInterpolationNearest_cfunc = self._get_library_function('niRFSG_ConfigureDeembeddingTableInterpolationNearest')
                self.niRFSG_ConfigureDeembeddingTableInterpolationNearest_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSG_ConfigureDeembeddingTableInterpolationNearest_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_ConfigureDeembeddingTableInterpolationNearest_cfunc(vi, port, table_name)

    def niRFSG_ConfigureDeembeddingTableInterpolationSpline(self, vi, port, table_name):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_ConfigureDeembeddingTableInterpolationSpline_cfunc is None:
                self.niRFSG_ConfigureDeembeddingTableInterpolationSpline_cfunc = self._get_library_function('niRFSG_ConfigureDeembeddingTableInterpolationSpline')
                self.niRFSG_ConfigureDeembeddingTableInterpolationSpline_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSG_ConfigureDeembeddingTableInterpolationSpline_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_ConfigureDeembeddingTableInterpolationSpline_cfunc(vi, port, table_name)

    def niRFSG_ConfigureDigitalEdgeScriptTrigger(self, vi, trigger_id, source, edge):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_ConfigureDigitalEdgeScriptTrigger_cfunc is None:
                self.niRFSG_ConfigureDigitalEdgeScriptTrigger_cfunc = self._get_library_function('niRFSG_ConfigureDigitalEdgeScriptTrigger')
                self.niRFSG_ConfigureDigitalEdgeScriptTrigger_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niRFSG_ConfigureDigitalEdgeScriptTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_ConfigureDigitalEdgeScriptTrigger_cfunc(vi, trigger_id, source, edge)

    def niRFSG_ConfigureDigitalEdgeStartTrigger(self, vi, source, edge):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_ConfigureDigitalEdgeStartTrigger_cfunc is None:
                self.niRFSG_ConfigureDigitalEdgeStartTrigger_cfunc = self._get_library_function('niRFSG_ConfigureDigitalEdgeStartTrigger')
                self.niRFSG_ConfigureDigitalEdgeStartTrigger_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niRFSG_ConfigureDigitalEdgeStartTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_ConfigureDigitalEdgeStartTrigger_cfunc(vi, source, edge)

    def niRFSG_ConfigureDigitalLevelScriptTrigger(self, vi, trigger_id, source, level):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_ConfigureDigitalLevelScriptTrigger_cfunc is None:
                self.niRFSG_ConfigureDigitalLevelScriptTrigger_cfunc = self._get_library_function('niRFSG_ConfigureDigitalLevelScriptTrigger')
                self.niRFSG_ConfigureDigitalLevelScriptTrigger_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niRFSG_ConfigureDigitalLevelScriptTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_ConfigureDigitalLevelScriptTrigger_cfunc(vi, trigger_id, source, level)

    def niRFSG_ConfigureDigitalModulationUserDefinedWaveform(self, vi, number_of_samples, user_defined_waveform):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_ConfigureDigitalModulationUserDefinedWaveform_cfunc is None:
                self.niRFSG_ConfigureDigitalModulationUserDefinedWaveform_cfunc = self._get_library_function('niRFSG_ConfigureDigitalModulationUserDefinedWaveform')
                self.niRFSG_ConfigureDigitalModulationUserDefinedWaveform_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt8)]  # noqa: F405
                self.niRFSG_ConfigureDigitalModulationUserDefinedWaveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_ConfigureDigitalModulationUserDefinedWaveform_cfunc(vi, number_of_samples, user_defined_waveform)

    def niRFSG_ConfigurePxiChassisClk10(self, vi, pxi_clk10_source):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_ConfigurePxiChassisClk10_cfunc is None:
                self.niRFSG_ConfigurePxiChassisClk10_cfunc = self._get_library_function('niRFSG_ConfigurePxiChassisClk10')
                self.niRFSG_ConfigurePxiChassisClk10_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSG_ConfigurePxiChassisClk10_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_ConfigurePxiChassisClk10_cfunc(vi, pxi_clk10_source)

    def niRFSG_ConfigureRF(self, vi, frequency, power_level):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_ConfigureRF_cfunc is None:
                self.niRFSG_ConfigureRF_cfunc = self._get_library_function('niRFSG_ConfigureRF')
                self.niRFSG_ConfigureRF_cfunc.argtypes = [ViSession, ViReal64, ViReal64]  # noqa: F405
                self.niRFSG_ConfigureRF_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_ConfigureRF_cfunc(vi, frequency, power_level)

    def niRFSG_ConfigureRefClock(self, vi, ref_clock_source, ref_clock_rate):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_ConfigureRefClock_cfunc is None:
                self.niRFSG_ConfigureRefClock_cfunc = self._get_library_function('niRFSG_ConfigureRefClock')
                self.niRFSG_ConfigureRefClock_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64]  # noqa: F405
                self.niRFSG_ConfigureRefClock_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_ConfigureRefClock_cfunc(vi, ref_clock_source, ref_clock_rate)

    def niRFSG_ConfigureSoftwareScriptTrigger(self, vi, trigger_id):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_ConfigureSoftwareScriptTrigger_cfunc is None:
                self.niRFSG_ConfigureSoftwareScriptTrigger_cfunc = self._get_library_function('niRFSG_ConfigureSoftwareScriptTrigger')
                self.niRFSG_ConfigureSoftwareScriptTrigger_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSG_ConfigureSoftwareScriptTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_ConfigureSoftwareScriptTrigger_cfunc(vi, trigger_id)

    def niRFSG_ConfigureSoftwareStartTrigger(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_ConfigureSoftwareStartTrigger_cfunc is None:
                self.niRFSG_ConfigureSoftwareStartTrigger_cfunc = self._get_library_function('niRFSG_ConfigureSoftwareStartTrigger')
                self.niRFSG_ConfigureSoftwareStartTrigger_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSG_ConfigureSoftwareStartTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_ConfigureSoftwareStartTrigger_cfunc(vi)

    def niRFSG_CreateDeembeddingSparameterTableArray(self, vi, port, table_name, frequencies, frequencies_size, sparameter_table, sparameter_table_size, number_of_ports, sparameter_orientation):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_CreateDeembeddingSparameterTableArray_cfunc is None:
                self.niRFSG_CreateDeembeddingSparameterTableArray_cfunc = self._get_library_function('niRFSG_CreateDeembeddingSparameterTableArray')
                self.niRFSG_CreateDeembeddingSparameterTableArray_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViReal64), ViInt32, ctypes.POINTER(NIComplexNumber), ViInt32, ViInt32, ViInt32]  # noqa: F405
                self.niRFSG_CreateDeembeddingSparameterTableArray_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_CreateDeembeddingSparameterTableArray_cfunc(vi, port, table_name, frequencies, frequencies_size, sparameter_table, sparameter_table_size, number_of_ports, sparameter_orientation)

    def niRFSG_CreateDeembeddingSparameterTableS2PFile(self, vi, port, table_name, s2p_file_path, sparameter_orientation):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_CreateDeembeddingSparameterTableS2PFile_cfunc is None:
                self.niRFSG_CreateDeembeddingSparameterTableS2PFile_cfunc = self._get_library_function('niRFSG_CreateDeembeddingSparameterTableS2PFile')
                self.niRFSG_CreateDeembeddingSparameterTableS2PFile_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niRFSG_CreateDeembeddingSparameterTableS2PFile_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_CreateDeembeddingSparameterTableS2PFile_cfunc(vi, port, table_name, s2p_file_path, sparameter_orientation)

    def niRFSG_DeleteAllDeembeddingTables(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_DeleteAllDeembeddingTables_cfunc is None:
                self.niRFSG_DeleteAllDeembeddingTables_cfunc = self._get_library_function('niRFSG_DeleteAllDeembeddingTables')
                self.niRFSG_DeleteAllDeembeddingTables_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSG_DeleteAllDeembeddingTables_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_DeleteAllDeembeddingTables_cfunc(vi)

    def niRFSG_DeleteDeembeddingTable(self, vi, port, table_name):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_DeleteDeembeddingTable_cfunc is None:
                self.niRFSG_DeleteDeembeddingTable_cfunc = self._get_library_function('niRFSG_DeleteDeembeddingTable')
                self.niRFSG_DeleteDeembeddingTable_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSG_DeleteDeembeddingTable_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_DeleteDeembeddingTable_cfunc(vi, port, table_name)

    def niRFSG_Disable(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_Disable_cfunc is None:
                self.niRFSG_Disable_cfunc = self._get_library_function('niRFSG_Disable')
                self.niRFSG_Disable_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSG_Disable_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_Disable_cfunc(vi)

    def niRFSG_DisableScriptTrigger(self, vi, trigger_id):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_DisableScriptTrigger_cfunc is None:
                self.niRFSG_DisableScriptTrigger_cfunc = self._get_library_function('niRFSG_DisableScriptTrigger')
                self.niRFSG_DisableScriptTrigger_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSG_DisableScriptTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_DisableScriptTrigger_cfunc(vi, trigger_id)

    def niRFSG_DisableStartTrigger(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_DisableStartTrigger_cfunc is None:
                self.niRFSG_DisableStartTrigger_cfunc = self._get_library_function('niRFSG_DisableStartTrigger')
                self.niRFSG_DisableStartTrigger_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSG_DisableStartTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_DisableStartTrigger_cfunc(vi)

    def niRFSG_ErrorMessage(self, vi, error_code, error_message):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_ErrorMessage_cfunc is None:
                self.niRFSG_ErrorMessage_cfunc = self._get_library_function('niRFSG_ErrorMessage')
                self.niRFSG_ErrorMessage_cfunc.argtypes = [ViSession, ViStatus, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSG_ErrorMessage_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_ErrorMessage_cfunc(vi, error_code, error_message)

    def niRFSG_ErrorQuery(self, vi, error_code, error_message):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_ErrorQuery_cfunc is None:
                self.niRFSG_ErrorQuery_cfunc = self._get_library_function('niRFSG_ErrorQuery')
                self.niRFSG_ErrorQuery_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSG_ErrorQuery_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_ErrorQuery_cfunc(vi, error_code, error_message)

    def niRFSG_GetAllNamedWaveformNames(self, vi, waveform_names, buffer_size, actual_buffer_size):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_GetAllNamedWaveformNames_cfunc is None:
                self.niRFSG_GetAllNamedWaveformNames_cfunc = self._get_library_function('niRFSG_GetAllNamedWaveformNames')
                self.niRFSG_GetAllNamedWaveformNames_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niRFSG_GetAllNamedWaveformNames_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_GetAllNamedWaveformNames_cfunc(vi, waveform_names, buffer_size, actual_buffer_size)

    def niRFSG_GetAllScriptNames(self, vi, script_names, buffer_size, actual_buffer_size):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_GetAllScriptNames_cfunc is None:
                self.niRFSG_GetAllScriptNames_cfunc = self._get_library_function('niRFSG_GetAllScriptNames')
                self.niRFSG_GetAllScriptNames_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niRFSG_GetAllScriptNames_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_GetAllScriptNames_cfunc(vi, script_names, buffer_size, actual_buffer_size)

    def niRFSG_GetAttributeViBoolean(self, vi, channel_name, attribute, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_GetAttributeViBoolean_cfunc is None:
                self.niRFSG_GetAttributeViBoolean_cfunc = self._get_library_function('niRFSG_GetAttributeViBoolean')
                self.niRFSG_GetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niRFSG_GetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_GetAttributeViBoolean_cfunc(vi, channel_name, attribute, value)

    def niRFSG_GetAttributeViInt32(self, vi, channel_name, attribute, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_GetAttributeViInt32_cfunc is None:
                self.niRFSG_GetAttributeViInt32_cfunc = self._get_library_function('niRFSG_GetAttributeViInt32')
                self.niRFSG_GetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niRFSG_GetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_GetAttributeViInt32_cfunc(vi, channel_name, attribute, value)

    def niRFSG_GetAttributeViInt64(self, vi, channel_name, attribute, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_GetAttributeViInt64_cfunc is None:
                self.niRFSG_GetAttributeViInt64_cfunc = self._get_library_function('niRFSG_GetAttributeViInt64')
                self.niRFSG_GetAttributeViInt64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViInt64)]  # noqa: F405
                self.niRFSG_GetAttributeViInt64_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_GetAttributeViInt64_cfunc(vi, channel_name, attribute, value)

    def niRFSG_GetAttributeViReal64(self, vi, channel_name, attribute, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_GetAttributeViReal64_cfunc is None:
                self.niRFSG_GetAttributeViReal64_cfunc = self._get_library_function('niRFSG_GetAttributeViReal64')
                self.niRFSG_GetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niRFSG_GetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_GetAttributeViReal64_cfunc(vi, channel_name, attribute, value)

    def niRFSG_GetAttributeViSession(self, vi, channel_name, attribute, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_GetAttributeViSession_cfunc is None:
                self.niRFSG_GetAttributeViSession_cfunc = self._get_library_function('niRFSG_GetAttributeViSession')
                self.niRFSG_GetAttributeViSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViSession)]  # noqa: F405
                self.niRFSG_GetAttributeViSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_GetAttributeViSession_cfunc(vi, channel_name, attribute, value)

    def niRFSG_GetAttributeViString(self, vi, channel_name, attribute, buf_size, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_GetAttributeViString_cfunc is None:
                self.niRFSG_GetAttributeViString_cfunc = self._get_library_function('niRFSG_GetAttributeViString')
                self.niRFSG_GetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSG_GetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_GetAttributeViString_cfunc(vi, channel_name, attribute, buf_size, value)

    def niRFSG_GetChannelName(self, vi, index, buffer_size, name):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_GetChannelName_cfunc is None:
                self.niRFSG_GetChannelName_cfunc = self._get_library_function('niRFSG_GetChannelName')
                self.niRFSG_GetChannelName_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSG_GetChannelName_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_GetChannelName_cfunc(vi, index, buffer_size, name)

    def niRFSG_GetDeembeddingSparameters(self, vi, sparameters, sparameters_array_size, number_of_sparameters, number_of_ports):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_GetDeembeddingSparameters_cfunc is None:
                self.niRFSG_GetDeembeddingSparameters_cfunc = self._get_library_function('niRFSG_GetDeembeddingSparameters')
                self.niRFSG_GetDeembeddingSparameters_cfunc.argtypes = [ViSession, ctypes.POINTER(NIComplexNumber), ViInt32, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niRFSG_GetDeembeddingSparameters_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_GetDeembeddingSparameters_cfunc(vi, sparameters, sparameters_array_size, number_of_sparameters, number_of_ports)

    def niRFSG_GetDeembeddingTableNumberOfPorts(self, vi, number_of_ports):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_GetDeembeddingTableNumberOfPorts_cfunc is None:
                self.niRFSG_GetDeembeddingTableNumberOfPorts_cfunc = self._get_library_function('niRFSG_GetDeembeddingTableNumberOfPorts')
                self.niRFSG_GetDeembeddingTableNumberOfPorts_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niRFSG_GetDeembeddingTableNumberOfPorts_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_GetDeembeddingTableNumberOfPorts_cfunc(vi, number_of_ports)

    def niRFSG_GetError(self, vi, error_code, error_description_buffer_size, error_description):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_GetError_cfunc is None:
                self.niRFSG_GetError_cfunc = self._get_library_function('niRFSG_GetError')
                self.niRFSG_GetError_cfunc.argtypes = [ViSession, ctypes.POINTER(ViStatus), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSG_GetError_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_GetError_cfunc(vi, error_code, error_description_buffer_size, error_description)

    def niRFSG_GetExternalCalibrationLastDateAndTime(self, vi, year, month, day, hour, minute, second):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_GetExternalCalibrationLastDateAndTime_cfunc is None:
                self.niRFSG_GetExternalCalibrationLastDateAndTime_cfunc = self._get_library_function('niRFSG_GetExternalCalibrationLastDateAndTime')
                self.niRFSG_GetExternalCalibrationLastDateAndTime_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niRFSG_GetExternalCalibrationLastDateAndTime_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_GetExternalCalibrationLastDateAndTime_cfunc(vi, year, month, day, hour, minute, second)

    def niRFSG_GetMaxSettablePower(self, vi, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_GetMaxSettablePower_cfunc is None:
                self.niRFSG_GetMaxSettablePower_cfunc = self._get_library_function('niRFSG_GetMaxSettablePower')
                self.niRFSG_GetMaxSettablePower_cfunc.argtypes = [ViSession, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niRFSG_GetMaxSettablePower_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_GetMaxSettablePower_cfunc(vi, value)

    def niRFSG_GetSelfCalibrationDateAndTime(self, vi, module, year, month, day, hour, minute, second):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_GetSelfCalibrationDateAndTime_cfunc is None:
                self.niRFSG_GetSelfCalibrationDateAndTime_cfunc = self._get_library_function('niRFSG_GetSelfCalibrationDateAndTime')
                self.niRFSG_GetSelfCalibrationDateAndTime_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niRFSG_GetSelfCalibrationDateAndTime_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_GetSelfCalibrationDateAndTime_cfunc(vi, module, year, month, day, hour, minute, second)

    def niRFSG_GetSelfCalibrationTemperature(self, vi, module, temperature):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_GetSelfCalibrationTemperature_cfunc is None:
                self.niRFSG_GetSelfCalibrationTemperature_cfunc = self._get_library_function('niRFSG_GetSelfCalibrationTemperature')
                self.niRFSG_GetSelfCalibrationTemperature_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niRFSG_GetSelfCalibrationTemperature_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_GetSelfCalibrationTemperature_cfunc(vi, module, temperature)

    def niRFSG_GetTerminalName(self, vi, signal, signal_identifier, buffer_size, terminal_name):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_GetTerminalName_cfunc is None:
                self.niRFSG_GetTerminalName_cfunc = self._get_library_function('niRFSG_GetTerminalName')
                self.niRFSG_GetTerminalName_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSG_GetTerminalName_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_GetTerminalName_cfunc(vi, signal, signal_identifier, buffer_size, terminal_name)

    def niRFSG_GetWaveformBurstStartLocations(self, vi, channel_name, number_of_locations, locations, required_size):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_GetWaveformBurstStartLocations_cfunc is None:
                self.niRFSG_GetWaveformBurstStartLocations_cfunc = self._get_library_function('niRFSG_GetWaveformBurstStartLocations')
                self.niRFSG_GetWaveformBurstStartLocations_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niRFSG_GetWaveformBurstStartLocations_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_GetWaveformBurstStartLocations_cfunc(vi, channel_name, number_of_locations, locations, required_size)

    def niRFSG_GetWaveformBurstStopLocations(self, vi, channel_name, number_of_locations, locations, required_size):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_GetWaveformBurstStopLocations_cfunc is None:
                self.niRFSG_GetWaveformBurstStopLocations_cfunc = self._get_library_function('niRFSG_GetWaveformBurstStopLocations')
                self.niRFSG_GetWaveformBurstStopLocations_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niRFSG_GetWaveformBurstStopLocations_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_GetWaveformBurstStopLocations_cfunc(vi, channel_name, number_of_locations, locations, required_size)

    def niRFSG_GetWaveformMarkerEventLocations(self, vi, channel_name, number_of_locations, locations, required_size):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_GetWaveformMarkerEventLocations_cfunc is None:
                self.niRFSG_GetWaveformMarkerEventLocations_cfunc = self._get_library_function('niRFSG_GetWaveformMarkerEventLocations')
                self.niRFSG_GetWaveformMarkerEventLocations_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niRFSG_GetWaveformMarkerEventLocations_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_GetWaveformMarkerEventLocations_cfunc(vi, channel_name, number_of_locations, locations, required_size)

    def niRFSG_InitWithOptions(self, resource_name, id_query, reset_device, option_string, new_vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_InitWithOptions_cfunc is None:
                self.niRFSG_InitWithOptions_cfunc = self._get_library_function('niRFSG_InitWithOptions')
                self.niRFSG_InitWithOptions_cfunc.argtypes = [ctypes.POINTER(ViChar), ViBoolean, ViBoolean, ctypes.POINTER(ViChar), ctypes.POINTER(ViSession)]  # noqa: F405
                self.niRFSG_InitWithOptions_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_InitWithOptions_cfunc(resource_name, id_query, reset_device, option_string, new_vi)

    def niRFSG_Initiate(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_Initiate_cfunc is None:
                self.niRFSG_Initiate_cfunc = self._get_library_function('niRFSG_Initiate')
                self.niRFSG_Initiate_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSG_Initiate_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_Initiate_cfunc(vi)

    def niRFSG_LoadConfigurationsFromFile(self, vi, channel_name, file_path):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_LoadConfigurationsFromFile_cfunc is None:
                self.niRFSG_LoadConfigurationsFromFile_cfunc = self._get_library_function('niRFSG_LoadConfigurationsFromFile')
                self.niRFSG_LoadConfigurationsFromFile_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSG_LoadConfigurationsFromFile_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_LoadConfigurationsFromFile_cfunc(vi, channel_name, file_path)

    def niRFSG_LockSession(self, vi, caller_has_lock):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_LockSession_cfunc is None:
                self.niRFSG_LockSession_cfunc = self._get_library_function('niRFSG_LockSession')
                self.niRFSG_LockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niRFSG_LockSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_LockSession_cfunc(vi, caller_has_lock)

    def niRFSG_PerformPowerSearch(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_PerformPowerSearch_cfunc is None:
                self.niRFSG_PerformPowerSearch_cfunc = self._get_library_function('niRFSG_PerformPowerSearch')
                self.niRFSG_PerformPowerSearch_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSG_PerformPowerSearch_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_PerformPowerSearch_cfunc(vi)

    def niRFSG_PerformThermalCorrection(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_PerformThermalCorrection_cfunc is None:
                self.niRFSG_PerformThermalCorrection_cfunc = self._get_library_function('niRFSG_PerformThermalCorrection')
                self.niRFSG_PerformThermalCorrection_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSG_PerformThermalCorrection_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_PerformThermalCorrection_cfunc(vi)

    def niRFSG_QueryArbWaveformCapabilities(self, vi, max_number_waveforms, waveform_quantum, min_waveform_size, max_waveform_size):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_QueryArbWaveformCapabilities_cfunc is None:
                self.niRFSG_QueryArbWaveformCapabilities_cfunc = self._get_library_function('niRFSG_QueryArbWaveformCapabilities')
                self.niRFSG_QueryArbWaveformCapabilities_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niRFSG_QueryArbWaveformCapabilities_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_QueryArbWaveformCapabilities_cfunc(vi, max_number_waveforms, waveform_quantum, min_waveform_size, max_waveform_size)

    def niRFSG_ReadAndDownloadWaveformFromFileTDMS(self, vi, waveform_name, file_path, waveform_index):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_ReadAndDownloadWaveformFromFileTDMS_cfunc is None:
                self.niRFSG_ReadAndDownloadWaveformFromFileTDMS_cfunc = self._get_library_function('niRFSG_ReadAndDownloadWaveformFromFileTDMS')
                self.niRFSG_ReadAndDownloadWaveformFromFileTDMS_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViUInt32]  # noqa: F405
                self.niRFSG_ReadAndDownloadWaveformFromFileTDMS_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_ReadAndDownloadWaveformFromFileTDMS_cfunc(vi, waveform_name, file_path, waveform_index)

    def niRFSG_ResetAttribute(self, vi, channel_name, attribute_id):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_ResetAttribute_cfunc is None:
                self.niRFSG_ResetAttribute_cfunc = self._get_library_function('niRFSG_ResetAttribute')
                self.niRFSG_ResetAttribute_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr]  # noqa: F405
                self.niRFSG_ResetAttribute_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_ResetAttribute_cfunc(vi, channel_name, attribute_id)

    def niRFSG_ResetDevice(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_ResetDevice_cfunc is None:
                self.niRFSG_ResetDevice_cfunc = self._get_library_function('niRFSG_ResetDevice')
                self.niRFSG_ResetDevice_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSG_ResetDevice_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_ResetDevice_cfunc(vi)

    def niRFSG_ResetWithDefaults(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_ResetWithDefaults_cfunc is None:
                self.niRFSG_ResetWithDefaults_cfunc = self._get_library_function('niRFSG_ResetWithDefaults')
                self.niRFSG_ResetWithDefaults_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSG_ResetWithDefaults_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_ResetWithDefaults_cfunc(vi)

    def niRFSG_ResetWithOptions(self, vi, steps_to_omit):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_ResetWithOptions_cfunc is None:
                self.niRFSG_ResetWithOptions_cfunc = self._get_library_function('niRFSG_ResetWithOptions')
                self.niRFSG_ResetWithOptions_cfunc.argtypes = [ViSession, ViUInt64]  # noqa: F405
                self.niRFSG_ResetWithOptions_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_ResetWithOptions_cfunc(vi, steps_to_omit)

    def niRFSG_RevisionQuery(self, vi, instrument_driver_revision, firmware_revision):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_RevisionQuery_cfunc is None:
                self.niRFSG_RevisionQuery_cfunc = self._get_library_function('niRFSG_RevisionQuery')
                self.niRFSG_RevisionQuery_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSG_RevisionQuery_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_RevisionQuery_cfunc(vi, instrument_driver_revision, firmware_revision)

    def niRFSG_SaveConfigurationsToFile(self, vi, channel_name, file_path):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_SaveConfigurationsToFile_cfunc is None:
                self.niRFSG_SaveConfigurationsToFile_cfunc = self._get_library_function('niRFSG_SaveConfigurationsToFile')
                self.niRFSG_SaveConfigurationsToFile_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSG_SaveConfigurationsToFile_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_SaveConfigurationsToFile_cfunc(vi, channel_name, file_path)

    def niRFSG_SelectArbWaveform(self, vi, name):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_SelectArbWaveform_cfunc is None:
                self.niRFSG_SelectArbWaveform_cfunc = self._get_library_function('niRFSG_SelectArbWaveform')
                self.niRFSG_SelectArbWaveform_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSG_SelectArbWaveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_SelectArbWaveform_cfunc(vi, name)

    def niRFSG_SelfCal(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_SelfCal_cfunc is None:
                self.niRFSG_SelfCal_cfunc = self._get_library_function('niRFSG_SelfCal')
                self.niRFSG_SelfCal_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSG_SelfCal_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_SelfCal_cfunc(vi)

    def niRFSG_SelfCalibrateRange(self, vi, steps_to_omit, min_frequency, max_frequency, min_power_level, max_power_level):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_SelfCalibrateRange_cfunc is None:
                self.niRFSG_SelfCalibrateRange_cfunc = self._get_library_function('niRFSG_SelfCalibrateRange')
                self.niRFSG_SelfCalibrateRange_cfunc.argtypes = [ViSession, ViInt64, ViReal64, ViReal64, ViReal64, ViReal64]  # noqa: F405
                self.niRFSG_SelfCalibrateRange_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_SelfCalibrateRange_cfunc(vi, steps_to_omit, min_frequency, max_frequency, min_power_level, max_power_level)

    def niRFSG_SelfTest(self, vi, self_test_result, self_test_message):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_SelfTest_cfunc is None:
                self.niRFSG_SelfTest_cfunc = self._get_library_function('niRFSG_SelfTest')
                self.niRFSG_SelfTest_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt16), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSG_SelfTest_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_SelfTest_cfunc(vi, self_test_result, self_test_message)

    def niRFSG_SendSoftwareEdgeTrigger(self, vi, trigger, trigger_identifier):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_SendSoftwareEdgeTrigger_cfunc is None:
                self.niRFSG_SendSoftwareEdgeTrigger_cfunc = self._get_library_function('niRFSG_SendSoftwareEdgeTrigger')
                self.niRFSG_SendSoftwareEdgeTrigger_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSG_SendSoftwareEdgeTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_SendSoftwareEdgeTrigger_cfunc(vi, trigger, trigger_identifier)

    def niRFSG_SetArbWaveformNextWritePosition(self, vi, waveform_name, relative_to, offset):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_SetArbWaveformNextWritePosition_cfunc is None:
                self.niRFSG_SetArbWaveformNextWritePosition_cfunc = self._get_library_function('niRFSG_SetArbWaveformNextWritePosition')
                self.niRFSG_SetArbWaveformNextWritePosition_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViInt32]  # noqa: F405
                self.niRFSG_SetArbWaveformNextWritePosition_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_SetArbWaveformNextWritePosition_cfunc(vi, waveform_name, relative_to, offset)

    def niRFSG_SetAttributeViBoolean(self, vi, channel_name, attribute, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_SetAttributeViBoolean_cfunc is None:
                self.niRFSG_SetAttributeViBoolean_cfunc = self._get_library_function('niRFSG_SetAttributeViBoolean')
                self.niRFSG_SetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViBoolean]  # noqa: F405
                self.niRFSG_SetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_SetAttributeViBoolean_cfunc(vi, channel_name, attribute, value)

    def niRFSG_SetAttributeViInt32(self, vi, channel_name, attribute, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_SetAttributeViInt32_cfunc is None:
                self.niRFSG_SetAttributeViInt32_cfunc = self._get_library_function('niRFSG_SetAttributeViInt32')
                self.niRFSG_SetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32]  # noqa: F405
                self.niRFSG_SetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_SetAttributeViInt32_cfunc(vi, channel_name, attribute, value)

    def niRFSG_SetAttributeViInt64(self, vi, channel_name, attribute, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_SetAttributeViInt64_cfunc is None:
                self.niRFSG_SetAttributeViInt64_cfunc = self._get_library_function('niRFSG_SetAttributeViInt64')
                self.niRFSG_SetAttributeViInt64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt64]  # noqa: F405
                self.niRFSG_SetAttributeViInt64_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_SetAttributeViInt64_cfunc(vi, channel_name, attribute, value)

    def niRFSG_SetAttributeViReal64(self, vi, channel_name, attribute, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_SetAttributeViReal64_cfunc is None:
                self.niRFSG_SetAttributeViReal64_cfunc = self._get_library_function('niRFSG_SetAttributeViReal64')
                self.niRFSG_SetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViReal64]  # noqa: F405
                self.niRFSG_SetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_SetAttributeViReal64_cfunc(vi, channel_name, attribute, value)

    def niRFSG_SetAttributeViSession(self, vi, channel_name, attribute, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_SetAttributeViSession_cfunc is None:
                self.niRFSG_SetAttributeViSession_cfunc = self._get_library_function('niRFSG_SetAttributeViSession')
                self.niRFSG_SetAttributeViSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViSession]  # noqa: F405
                self.niRFSG_SetAttributeViSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_SetAttributeViSession_cfunc(vi, channel_name, attribute, value)

    def niRFSG_SetAttributeViString(self, vi, channel_name, attribute, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_SetAttributeViString_cfunc is None:
                self.niRFSG_SetAttributeViString_cfunc = self._get_library_function('niRFSG_SetAttributeViString')
                self.niRFSG_SetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSG_SetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_SetAttributeViString_cfunc(vi, channel_name, attribute, value)

    def niRFSG_SetWaveformBurstStartLocations(self, vi, channel_name, number_of_locations, locations):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_SetWaveformBurstStartLocations_cfunc is None:
                self.niRFSG_SetWaveformBurstStartLocations_cfunc = self._get_library_function('niRFSG_SetWaveformBurstStartLocations')
                self.niRFSG_SetWaveformBurstStartLocations_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niRFSG_SetWaveformBurstStartLocations_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_SetWaveformBurstStartLocations_cfunc(vi, channel_name, number_of_locations, locations)

    def niRFSG_SetWaveformBurstStopLocations(self, vi, channel_name, number_of_locations, locations):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_SetWaveformBurstStopLocations_cfunc is None:
                self.niRFSG_SetWaveformBurstStopLocations_cfunc = self._get_library_function('niRFSG_SetWaveformBurstStopLocations')
                self.niRFSG_SetWaveformBurstStopLocations_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niRFSG_SetWaveformBurstStopLocations_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_SetWaveformBurstStopLocations_cfunc(vi, channel_name, number_of_locations, locations)

    def niRFSG_SetWaveformMarkerEventLocations(self, vi, channel_name, number_of_locations, locations):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_SetWaveformMarkerEventLocations_cfunc is None:
                self.niRFSG_SetWaveformMarkerEventLocations_cfunc = self._get_library_function('niRFSG_SetWaveformMarkerEventLocations')
                self.niRFSG_SetWaveformMarkerEventLocations_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niRFSG_SetWaveformMarkerEventLocations_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_SetWaveformMarkerEventLocations_cfunc(vi, channel_name, number_of_locations, locations)

    def niRFSG_UnlockSession(self, vi, caller_has_lock):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_UnlockSession_cfunc is None:
                self.niRFSG_UnlockSession_cfunc = self._get_library_function('niRFSG_UnlockSession')
                self.niRFSG_UnlockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niRFSG_UnlockSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_UnlockSession_cfunc(vi, caller_has_lock)

    def niRFSG_WaitUntilSettled(self, vi, max_time_milliseconds):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_WaitUntilSettled_cfunc is None:
                self.niRFSG_WaitUntilSettled_cfunc = self._get_library_function('niRFSG_WaitUntilSettled')
                self.niRFSG_WaitUntilSettled_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niRFSG_WaitUntilSettled_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_WaitUntilSettled_cfunc(vi, max_time_milliseconds)

    def niRFSG_WriteArbWaveformComplexF32(self, vi, waveform_name, number_of_samples, waveform_data_array, more_data_pending):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_WriteArbWaveformComplexF32_cfunc is None:
                self.niRFSG_WriteArbWaveformComplexF32_cfunc = self._get_library_function('niRFSG_WriteArbWaveformComplexF32')
                self.niRFSG_WriteArbWaveformComplexF32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(NIComplexNumberF32), ViBoolean]  # noqa: F405
                self.niRFSG_WriteArbWaveformComplexF32_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_WriteArbWaveformComplexF32_cfunc(vi, waveform_name, number_of_samples, waveform_data_array, more_data_pending)

    def niRFSG_WriteArbWaveformComplexF64(self, vi, waveform_name, number_of_samples, waveform_data_array, more_data_pending):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_WriteArbWaveformComplexF64_cfunc is None:
                self.niRFSG_WriteArbWaveformComplexF64_cfunc = self._get_library_function('niRFSG_WriteArbWaveformComplexF64')
                self.niRFSG_WriteArbWaveformComplexF64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(NIComplexNumber), ViBoolean]  # noqa: F405
                self.niRFSG_WriteArbWaveformComplexF64_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_WriteArbWaveformComplexF64_cfunc(vi, waveform_name, number_of_samples, waveform_data_array, more_data_pending)

    def niRFSG_WriteArbWaveformComplexI16(self, vi, waveform_name, number_of_samples, waveform_data_array):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_WriteArbWaveformComplexI16_cfunc is None:
                self.niRFSG_WriteArbWaveformComplexI16_cfunc = self._get_library_function('niRFSG_WriteArbWaveformComplexI16')
                self.niRFSG_WriteArbWaveformComplexI16_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(NIComplexI16)]  # noqa: F405
                self.niRFSG_WriteArbWaveformComplexI16_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_WriteArbWaveformComplexI16_cfunc(vi, waveform_name, number_of_samples, waveform_data_array)

    def niRFSG_WriteScript(self, vi, script):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_WriteScript_cfunc is None:
                self.niRFSG_WriteScript_cfunc = self._get_library_function('niRFSG_WriteScript')
                self.niRFSG_WriteScript_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSG_WriteScript_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_WriteScript_cfunc(vi, script)

    def niRFSG_close(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_close_cfunc is None:
                self.niRFSG_close_cfunc = self._get_library_function('niRFSG_close')
                self.niRFSG_close_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSG_close_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_close_cfunc(vi)

    def niRFSG_reset(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_reset_cfunc is None:
                self.niRFSG_reset_cfunc = self._get_library_function('niRFSG_reset')
                self.niRFSG_reset_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSG_reset_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_reset_cfunc(vi)
