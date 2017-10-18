# This file was generated

import ctypes
import threading

from nifgen.visatype import *  # noqa: F403,H303


class Library(object):
    '''Library

    Wrapper around driver library.
    Class will setup the correct ctypes information for every function on first call.
    '''

    def __init__(self, library_name, library_type):
        self._func_lock = threading.Lock()
        # We cache the cfunc object from the ctypes.CDLL object
        self.niFgen_AbortGeneration_cfunc = None
        self.niFgen_AdjustSampleClockRelativeDelay_cfunc = None
        self.niFgen_AllocateNamedWaveform_cfunc = None
        self.niFgen_AllocateWaveform_cfunc = None
        self.niFgen_CheckAttributeViBoolean_cfunc = None
        self.niFgen_CheckAttributeViInt32_cfunc = None
        self.niFgen_CheckAttributeViInt64_cfunc = None
        self.niFgen_CheckAttributeViReal64_cfunc = None
        self.niFgen_CheckAttributeViSession_cfunc = None
        self.niFgen_CheckAttributeViString_cfunc = None
        self.niFgen_ClearArbMemory_cfunc = None
        self.niFgen_ClearArbSequence_cfunc = None
        self.niFgen_ClearArbWaveform_cfunc = None
        self.niFgen_ClearFreqList_cfunc = None
        self.niFgen_ClearUserStandardWaveform_cfunc = None
        self.niFgen_Commit_cfunc = None
        self.niFgen_ConfigureAmplitude_cfunc = None
        self.niFgen_ConfigureArbSequence_cfunc = None
        self.niFgen_ConfigureArbWaveform_cfunc = None
        self.niFgen_ConfigureChannels_cfunc = None
        self.niFgen_ConfigureClockMode_cfunc = None
        self.niFgen_ConfigureCustomFIRFilterCoefficients_cfunc = None
        self.niFgen_ConfigureDigitalEdgeScriptTrigger_cfunc = None
        self.niFgen_ConfigureDigitalEdgeStartTrigger_cfunc = None
        self.niFgen_ConfigureDigitalLevelScriptTrigger_cfunc = None
        self.niFgen_ConfigureFreqList_cfunc = None
        self.niFgen_ConfigureFrequency_cfunc = None
        self.niFgen_ConfigureGain_cfunc = None
        self.niFgen_ConfigureOperationMode_cfunc = None
        self.niFgen_ConfigureOutputEnabled_cfunc = None
        self.niFgen_ConfigureOutputImpedance_cfunc = None
        self.niFgen_ConfigureOutputMode_cfunc = None
        self.niFgen_ConfigureP2PEndpointFullnessStartTrigger_cfunc = None
        self.niFgen_ConfigureRefClockFrequency_cfunc = None
        self.niFgen_ConfigureRefClockSource_cfunc = None
        self.niFgen_ConfigureReferenceClock_cfunc = None
        self.niFgen_ConfigureSampleClockSource_cfunc = None
        self.niFgen_ConfigureSampleRate_cfunc = None
        self.niFgen_ConfigureSoftwareEdgeScriptTrigger_cfunc = None
        self.niFgen_ConfigureSoftwareEdgeStartTrigger_cfunc = None
        self.niFgen_ConfigureStandardWaveform_cfunc = None
        self.niFgen_ConfigureSynchronization_cfunc = None
        self.niFgen_ConfigureTriggerMode_cfunc = None
        self.niFgen_ConfigureTriggerSource_cfunc = None
        self.niFgen_ConfigureUpdateClockSource_cfunc = None
        self.niFgen_CreateAdvancedArbSequence_cfunc = None
        self.niFgen_CreateArbSequence_cfunc = None
        self.niFgen_CreateArbWaveform_cfunc = None
        self.niFgen_CreateBinary16ArbWaveform_cfunc = None
        self.niFgen_CreateFreqList_cfunc = None
        self.niFgen_CreateWaveformF64_cfunc = None
        self.niFgen_CreateWaveformFromFileF64_cfunc = None
        self.niFgen_CreateWaveformFromFileHWS_cfunc = None
        self.niFgen_CreateWaveformFromFileI16_cfunc = None
        self.niFgen_CreateWaveformI16_cfunc = None
        self.niFgen_DefineUserStandardWaveform_cfunc = None
        self.niFgen_DeleteNamedWaveform_cfunc = None
        self.niFgen_DeleteScript_cfunc = None
        self.niFgen_Disable_cfunc = None
        self.niFgen_DisableAnalogFilter_cfunc = None
        self.niFgen_DisableDigitalFilter_cfunc = None
        self.niFgen_DisableDigitalPatterning_cfunc = None
        self.niFgen_DisableScriptTrigger_cfunc = None
        self.niFgen_DisableStartTrigger_cfunc = None
        self.niFgen_EnableAnalogFilter_cfunc = None
        self.niFgen_EnableDigitalFilter_cfunc = None
        self.niFgen_EnableDigitalPatterning_cfunc = None
        self.niFgen_ErrorHandler_cfunc = None
        self.niFgen_ExportSignal_cfunc = None
        self.niFgen_GetAttributeViBoolean_cfunc = None
        self.niFgen_GetAttributeViInt32_cfunc = None
        self.niFgen_GetAttributeViInt64_cfunc = None
        self.niFgen_GetAttributeViReal64_cfunc = None
        self.niFgen_GetAttributeViString_cfunc = None
        self.niFgen_GetError_cfunc = None
        self.niFgen_GetFIRFilterCoefficients_cfunc = None
        self.niFgen_GetHardwareState_cfunc = None
        self.niFgen_GetSelfCalLastDateAndTime_cfunc = None
        self.niFgen_GetSelfCalLastTemp_cfunc = None
        self.niFgen_GetSelfCalSupported_cfunc = None
        self.niFgen_InitWithOptions_cfunc = None
        self.niFgen_InitializeAnalogOutputCalibration_cfunc = None
        self.niFgen_InitializeCalADCCalibration_cfunc = None
        self.niFgen_InitializeFlatnessCalibration_cfunc = None
        self.niFgen_InitializeOscillatorFrequencyCalibration_cfunc = None
        self.niFgen_InitializeWithChannels_cfunc = None
        self.niFgen_InitiateGeneration_cfunc = None
        self.niFgen_IsDone_cfunc = None
        self.niFgen_ManualEnableP2PStream_cfunc = None
        self.niFgen_QueryArbSeqCapabilities_cfunc = None
        self.niFgen_QueryArbWfmCapabilities_cfunc = None
        self.niFgen_QueryFreqListCapabilities_cfunc = None
        self.niFgen_ReadCalADC_cfunc = None
        self.niFgen_ReadCurrentTemperature_cfunc = None
        self.niFgen_ResetAttribute_cfunc = None
        self.niFgen_ResetDevice_cfunc = None
        self.niFgen_ResetWithDefaults_cfunc = None
        self.niFgen_RouteSignalOut_cfunc = None
        self.niFgen_SelfCal_cfunc = None
        self.niFgen_SendSoftwareEdgeTrigger_cfunc = None
        self.niFgen_SendSoftwareTrigger_cfunc = None
        self.niFgen_SetAttributeViBoolean_cfunc = None
        self.niFgen_SetAttributeViInt32_cfunc = None
        self.niFgen_SetAttributeViInt64_cfunc = None
        self.niFgen_SetAttributeViReal64_cfunc = None
        self.niFgen_SetAttributeViString_cfunc = None
        self.niFgen_SetNamedWaveformNextWritePosition_cfunc = None
        self.niFgen_SetWaveformNextWritePosition_cfunc = None
        self.niFgen_WaitUntilDone_cfunc = None
        self.niFgen_WriteBinary16AnalogStaticValue_cfunc = None
        self.niFgen_WriteBinary16Waveform_cfunc = None
        self.niFgen_WriteNamedWaveformF64_cfunc = None
        self.niFgen_WriteNamedWaveformI16_cfunc = None
        self.niFgen_WriteP2PEndpointI16_cfunc = None
        self.niFgen_WriteScript_cfunc = None
        self.niFgen_WriteWaveform_cfunc = None
        self.niFgen_close_cfunc = None
        self.niFgen_error_message_cfunc = None
        self.niFgen_reset_cfunc = None
        self.niFgen_self_test_cfunc = None

        if library_type == 'windll':
            self._library = ctypes.WinDLL(library_name)
        else:  # pragma: no cover
            assert library_type == 'cdll'
            self._library = ctypes.CDLL(library_name)

    def niFgen_AbortGeneration(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFgen_AbortGeneration_cfunc is None:
                self.niFgen_AbortGeneration_cfunc = self._library.niFgen_AbortGeneration
                self.niFgen_AbortGeneration_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFgen_AbortGeneration_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_AbortGeneration_cfunc(vi)

    def niFgen_AdjustSampleClockRelativeDelay(self, vi, adjustment_time):  # noqa: N802
        with self._func_lock:
            if self.niFgen_AdjustSampleClockRelativeDelay_cfunc is None:
                self.niFgen_AdjustSampleClockRelativeDelay_cfunc = self._library.niFgen_AdjustSampleClockRelativeDelay
                self.niFgen_AdjustSampleClockRelativeDelay_cfunc.argtypes = [ViSession, ViReal64]  # noqa: F405
                self.niFgen_AdjustSampleClockRelativeDelay_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_AdjustSampleClockRelativeDelay_cfunc(vi, adjustment_time)

    def niFgen_AllocateNamedWaveform(self, vi, channel_name, waveform_name, waveform_size):  # noqa: N802
        with self._func_lock:
            if self.niFgen_AllocateNamedWaveform_cfunc is None:
                self.niFgen_AllocateNamedWaveform_cfunc = self._library.niFgen_AllocateNamedWaveform
                self.niFgen_AllocateNamedWaveform_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niFgen_AllocateNamedWaveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_AllocateNamedWaveform_cfunc(vi, channel_name, waveform_name, waveform_size)

    def niFgen_AllocateWaveform(self, vi, channel_name, waveform_size, waveform_handle):  # noqa: N802
        with self._func_lock:
            if self.niFgen_AllocateWaveform_cfunc is None:
                self.niFgen_AllocateWaveform_cfunc = self._library.niFgen_AllocateWaveform
                self.niFgen_AllocateWaveform_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_AllocateWaveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_AllocateWaveform_cfunc(vi, channel_name, waveform_size, waveform_handle)

    def niFgen_CheckAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFgen_CheckAttributeViBoolean_cfunc is None:
                self.niFgen_CheckAttributeViBoolean_cfunc = self._library.niFgen_CheckAttributeViBoolean
                self.niFgen_CheckAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViBoolean]  # noqa: F405
                self.niFgen_CheckAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_CheckAttributeViBoolean_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFgen_CheckAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFgen_CheckAttributeViInt32_cfunc is None:
                self.niFgen_CheckAttributeViInt32_cfunc = self._library.niFgen_CheckAttributeViInt32
                self.niFgen_CheckAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32]  # noqa: F405
                self.niFgen_CheckAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_CheckAttributeViInt32_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFgen_CheckAttributeViInt64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFgen_CheckAttributeViInt64_cfunc is None:
                self.niFgen_CheckAttributeViInt64_cfunc = self._library.niFgen_CheckAttributeViInt64
                self.niFgen_CheckAttributeViInt64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt64]  # noqa: F405
                self.niFgen_CheckAttributeViInt64_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_CheckAttributeViInt64_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFgen_CheckAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFgen_CheckAttributeViReal64_cfunc is None:
                self.niFgen_CheckAttributeViReal64_cfunc = self._library.niFgen_CheckAttributeViReal64
                self.niFgen_CheckAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViReal64]  # noqa: F405
                self.niFgen_CheckAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_CheckAttributeViReal64_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFgen_CheckAttributeViSession(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFgen_CheckAttributeViSession_cfunc is None:
                self.niFgen_CheckAttributeViSession_cfunc = self._library.niFgen_CheckAttributeViSession
                self.niFgen_CheckAttributeViSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViSession]  # noqa: F405
                self.niFgen_CheckAttributeViSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_CheckAttributeViSession_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFgen_CheckAttributeViString(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFgen_CheckAttributeViString_cfunc is None:
                self.niFgen_CheckAttributeViString_cfunc = self._library.niFgen_CheckAttributeViString
                self.niFgen_CheckAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_CheckAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_CheckAttributeViString_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFgen_ClearArbMemory(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ClearArbMemory_cfunc is None:
                self.niFgen_ClearArbMemory_cfunc = self._library.niFgen_ClearArbMemory
                self.niFgen_ClearArbMemory_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFgen_ClearArbMemory_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ClearArbMemory_cfunc(vi)

    def niFgen_ClearArbSequence(self, vi, sequence_handle):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ClearArbSequence_cfunc is None:
                self.niFgen_ClearArbSequence_cfunc = self._library.niFgen_ClearArbSequence
                self.niFgen_ClearArbSequence_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niFgen_ClearArbSequence_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ClearArbSequence_cfunc(vi, sequence_handle)

    def niFgen_ClearArbWaveform(self, vi, waveform_handle):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ClearArbWaveform_cfunc is None:
                self.niFgen_ClearArbWaveform_cfunc = self._library.niFgen_ClearArbWaveform
                self.niFgen_ClearArbWaveform_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niFgen_ClearArbWaveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ClearArbWaveform_cfunc(vi, waveform_handle)

    def niFgen_ClearFreqList(self, vi, frequency_list_handle):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ClearFreqList_cfunc is None:
                self.niFgen_ClearFreqList_cfunc = self._library.niFgen_ClearFreqList
                self.niFgen_ClearFreqList_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niFgen_ClearFreqList_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ClearFreqList_cfunc(vi, frequency_list_handle)

    def niFgen_ClearUserStandardWaveform(self, vi, channel_name):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ClearUserStandardWaveform_cfunc is None:
                self.niFgen_ClearUserStandardWaveform_cfunc = self._library.niFgen_ClearUserStandardWaveform
                self.niFgen_ClearUserStandardWaveform_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_ClearUserStandardWaveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ClearUserStandardWaveform_cfunc(vi, channel_name)

    def niFgen_Commit(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFgen_Commit_cfunc is None:
                self.niFgen_Commit_cfunc = self._library.niFgen_Commit
                self.niFgen_Commit_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFgen_Commit_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_Commit_cfunc(vi)

    def niFgen_ConfigureAmplitude(self, vi, channel_name, amplitude):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ConfigureAmplitude_cfunc is None:
                self.niFgen_ConfigureAmplitude_cfunc = self._library.niFgen_ConfigureAmplitude
                self.niFgen_ConfigureAmplitude_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64]  # noqa: F405
                self.niFgen_ConfigureAmplitude_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ConfigureAmplitude_cfunc(vi, channel_name, amplitude)

    def niFgen_ConfigureArbSequence(self, vi, channel_name, sequence_handle, gain, offset):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ConfigureArbSequence_cfunc is None:
                self.niFgen_ConfigureArbSequence_cfunc = self._library.niFgen_ConfigureArbSequence
                self.niFgen_ConfigureArbSequence_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViReal64, ViReal64]  # noqa: F405
                self.niFgen_ConfigureArbSequence_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ConfigureArbSequence_cfunc(vi, channel_name, sequence_handle, gain, offset)

    def niFgen_ConfigureArbWaveform(self, vi, channel_name, waveform_handle, gain, offset):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ConfigureArbWaveform_cfunc is None:
                self.niFgen_ConfigureArbWaveform_cfunc = self._library.niFgen_ConfigureArbWaveform
                self.niFgen_ConfigureArbWaveform_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViReal64, ViReal64]  # noqa: F405
                self.niFgen_ConfigureArbWaveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ConfigureArbWaveform_cfunc(vi, channel_name, waveform_handle, gain, offset)

    def niFgen_ConfigureChannels(self, vi, channels):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ConfigureChannels_cfunc is None:
                self.niFgen_ConfigureChannels_cfunc = self._library.niFgen_ConfigureChannels
                self.niFgen_ConfigureChannels_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_ConfigureChannels_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ConfigureChannels_cfunc(vi, channels)

    def niFgen_ConfigureClockMode(self, vi, clock_mode):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ConfigureClockMode_cfunc is None:
                self.niFgen_ConfigureClockMode_cfunc = self._library.niFgen_ConfigureClockMode
                self.niFgen_ConfigureClockMode_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niFgen_ConfigureClockMode_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ConfigureClockMode_cfunc(vi, clock_mode)

    def niFgen_ConfigureCustomFIRFilterCoefficients(self, vi, channel_name, number_of_coefficients, coefficients_array):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ConfigureCustomFIRFilterCoefficients_cfunc is None:
                self.niFgen_ConfigureCustomFIRFilterCoefficients_cfunc = self._library.niFgen_ConfigureCustomFIRFilterCoefficients
                self.niFgen_ConfigureCustomFIRFilterCoefficients_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFgen_ConfigureCustomFIRFilterCoefficients_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ConfigureCustomFIRFilterCoefficients_cfunc(vi, channel_name, number_of_coefficients, coefficients_array)

    def niFgen_ConfigureDigitalEdgeScriptTrigger(self, vi, trigger_id, source, edge):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ConfigureDigitalEdgeScriptTrigger_cfunc is None:
                self.niFgen_ConfigureDigitalEdgeScriptTrigger_cfunc = self._library.niFgen_ConfigureDigitalEdgeScriptTrigger
                self.niFgen_ConfigureDigitalEdgeScriptTrigger_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niFgen_ConfigureDigitalEdgeScriptTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ConfigureDigitalEdgeScriptTrigger_cfunc(vi, trigger_id, source, edge)

    def niFgen_ConfigureDigitalEdgeStartTrigger(self, vi, source, edge):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ConfigureDigitalEdgeStartTrigger_cfunc is None:
                self.niFgen_ConfigureDigitalEdgeStartTrigger_cfunc = self._library.niFgen_ConfigureDigitalEdgeStartTrigger
                self.niFgen_ConfigureDigitalEdgeStartTrigger_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niFgen_ConfigureDigitalEdgeStartTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ConfigureDigitalEdgeStartTrigger_cfunc(vi, source, edge)

    def niFgen_ConfigureDigitalLevelScriptTrigger(self, vi, trigger_id, source, trigger_when):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ConfigureDigitalLevelScriptTrigger_cfunc is None:
                self.niFgen_ConfigureDigitalLevelScriptTrigger_cfunc = self._library.niFgen_ConfigureDigitalLevelScriptTrigger
                self.niFgen_ConfigureDigitalLevelScriptTrigger_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niFgen_ConfigureDigitalLevelScriptTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ConfigureDigitalLevelScriptTrigger_cfunc(vi, trigger_id, source, trigger_when)

    def niFgen_ConfigureFreqList(self, vi, channel_name, frequency_list_handle, amplitude, dc_offset, start_phase):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ConfigureFreqList_cfunc is None:
                self.niFgen_ConfigureFreqList_cfunc = self._library.niFgen_ConfigureFreqList
                self.niFgen_ConfigureFreqList_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViReal64, ViReal64, ViReal64]  # noqa: F405
                self.niFgen_ConfigureFreqList_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ConfigureFreqList_cfunc(vi, channel_name, frequency_list_handle, amplitude, dc_offset, start_phase)

    def niFgen_ConfigureFrequency(self, vi, channel_name, frequency):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ConfigureFrequency_cfunc is None:
                self.niFgen_ConfigureFrequency_cfunc = self._library.niFgen_ConfigureFrequency
                self.niFgen_ConfigureFrequency_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64]  # noqa: F405
                self.niFgen_ConfigureFrequency_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ConfigureFrequency_cfunc(vi, channel_name, frequency)

    def niFgen_ConfigureGain(self, vi, channel_name, gain):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ConfigureGain_cfunc is None:
                self.niFgen_ConfigureGain_cfunc = self._library.niFgen_ConfigureGain
                self.niFgen_ConfigureGain_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64]  # noqa: F405
                self.niFgen_ConfigureGain_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ConfigureGain_cfunc(vi, channel_name, gain)

    def niFgen_ConfigureOperationMode(self, vi, channel_name, operation_mode):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ConfigureOperationMode_cfunc is None:
                self.niFgen_ConfigureOperationMode_cfunc = self._library.niFgen_ConfigureOperationMode
                self.niFgen_ConfigureOperationMode_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niFgen_ConfigureOperationMode_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ConfigureOperationMode_cfunc(vi, channel_name, operation_mode)

    def niFgen_ConfigureOutputEnabled(self, vi, channel_name, enabled):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ConfigureOutputEnabled_cfunc is None:
                self.niFgen_ConfigureOutputEnabled_cfunc = self._library.niFgen_ConfigureOutputEnabled
                self.niFgen_ConfigureOutputEnabled_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViBoolean]  # noqa: F405
                self.niFgen_ConfigureOutputEnabled_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ConfigureOutputEnabled_cfunc(vi, channel_name, enabled)

    def niFgen_ConfigureOutputImpedance(self, vi, channel_name, impedance):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ConfigureOutputImpedance_cfunc is None:
                self.niFgen_ConfigureOutputImpedance_cfunc = self._library.niFgen_ConfigureOutputImpedance
                self.niFgen_ConfigureOutputImpedance_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64]  # noqa: F405
                self.niFgen_ConfigureOutputImpedance_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ConfigureOutputImpedance_cfunc(vi, channel_name, impedance)

    def niFgen_ConfigureOutputMode(self, vi, output_mode):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ConfigureOutputMode_cfunc is None:
                self.niFgen_ConfigureOutputMode_cfunc = self._library.niFgen_ConfigureOutputMode
                self.niFgen_ConfigureOutputMode_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niFgen_ConfigureOutputMode_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ConfigureOutputMode_cfunc(vi, output_mode)

    def niFgen_ConfigureP2PEndpointFullnessStartTrigger(self, vi, p2p_endpoint_fullness_level):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ConfigureP2PEndpointFullnessStartTrigger_cfunc is None:
                self.niFgen_ConfigureP2PEndpointFullnessStartTrigger_cfunc = self._library.niFgen_ConfigureP2PEndpointFullnessStartTrigger
                self.niFgen_ConfigureP2PEndpointFullnessStartTrigger_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niFgen_ConfigureP2PEndpointFullnessStartTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ConfigureP2PEndpointFullnessStartTrigger_cfunc(vi, p2p_endpoint_fullness_level)

    def niFgen_ConfigureRefClockFrequency(self, vi, reference_clock_frequency):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ConfigureRefClockFrequency_cfunc is None:
                self.niFgen_ConfigureRefClockFrequency_cfunc = self._library.niFgen_ConfigureRefClockFrequency
                self.niFgen_ConfigureRefClockFrequency_cfunc.argtypes = [ViSession, ViReal64]  # noqa: F405
                self.niFgen_ConfigureRefClockFrequency_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ConfigureRefClockFrequency_cfunc(vi, reference_clock_frequency)

    def niFgen_ConfigureRefClockSource(self, vi, reference_clock_source):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ConfigureRefClockSource_cfunc is None:
                self.niFgen_ConfigureRefClockSource_cfunc = self._library.niFgen_ConfigureRefClockSource
                self.niFgen_ConfigureRefClockSource_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niFgen_ConfigureRefClockSource_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ConfigureRefClockSource_cfunc(vi, reference_clock_source)

    def niFgen_ConfigureReferenceClock(self, vi, reference_clock_source, reference_clock_frequency):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ConfigureReferenceClock_cfunc is None:
                self.niFgen_ConfigureReferenceClock_cfunc = self._library.niFgen_ConfigureReferenceClock
                self.niFgen_ConfigureReferenceClock_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64]  # noqa: F405
                self.niFgen_ConfigureReferenceClock_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ConfigureReferenceClock_cfunc(vi, reference_clock_source, reference_clock_frequency)

    def niFgen_ConfigureSampleClockSource(self, vi, sample_clock_source):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ConfigureSampleClockSource_cfunc is None:
                self.niFgen_ConfigureSampleClockSource_cfunc = self._library.niFgen_ConfigureSampleClockSource
                self.niFgen_ConfigureSampleClockSource_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_ConfigureSampleClockSource_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ConfigureSampleClockSource_cfunc(vi, sample_clock_source)

    def niFgen_ConfigureSampleRate(self, vi, sample_rate):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ConfigureSampleRate_cfunc is None:
                self.niFgen_ConfigureSampleRate_cfunc = self._library.niFgen_ConfigureSampleRate
                self.niFgen_ConfigureSampleRate_cfunc.argtypes = [ViSession, ViReal64]  # noqa: F405
                self.niFgen_ConfigureSampleRate_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ConfigureSampleRate_cfunc(vi, sample_rate)

    def niFgen_ConfigureSoftwareEdgeScriptTrigger(self, vi, trigger_id):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ConfigureSoftwareEdgeScriptTrigger_cfunc is None:
                self.niFgen_ConfigureSoftwareEdgeScriptTrigger_cfunc = self._library.niFgen_ConfigureSoftwareEdgeScriptTrigger
                self.niFgen_ConfigureSoftwareEdgeScriptTrigger_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_ConfigureSoftwareEdgeScriptTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ConfigureSoftwareEdgeScriptTrigger_cfunc(vi, trigger_id)

    def niFgen_ConfigureSoftwareEdgeStartTrigger(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ConfigureSoftwareEdgeStartTrigger_cfunc is None:
                self.niFgen_ConfigureSoftwareEdgeStartTrigger_cfunc = self._library.niFgen_ConfigureSoftwareEdgeStartTrigger
                self.niFgen_ConfigureSoftwareEdgeStartTrigger_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFgen_ConfigureSoftwareEdgeStartTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ConfigureSoftwareEdgeStartTrigger_cfunc(vi)

    def niFgen_ConfigureStandardWaveform(self, vi, channel_name, waveform, amplitude, dc_offset, frequency, start_phase):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ConfigureStandardWaveform_cfunc is None:
                self.niFgen_ConfigureStandardWaveform_cfunc = self._library.niFgen_ConfigureStandardWaveform
                self.niFgen_ConfigureStandardWaveform_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViReal64, ViReal64, ViReal64, ViReal64]  # noqa: F405
                self.niFgen_ConfigureStandardWaveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ConfigureStandardWaveform_cfunc(vi, channel_name, waveform, amplitude, dc_offset, frequency, start_phase)

    def niFgen_ConfigureSynchronization(self, vi, channel_name, synchronization_source):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ConfigureSynchronization_cfunc is None:
                self.niFgen_ConfigureSynchronization_cfunc = self._library.niFgen_ConfigureSynchronization
                self.niFgen_ConfigureSynchronization_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niFgen_ConfigureSynchronization_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ConfigureSynchronization_cfunc(vi, channel_name, synchronization_source)

    def niFgen_ConfigureTriggerMode(self, vi, channel_name, trigger_mode):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ConfigureTriggerMode_cfunc is None:
                self.niFgen_ConfigureTriggerMode_cfunc = self._library.niFgen_ConfigureTriggerMode
                self.niFgen_ConfigureTriggerMode_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niFgen_ConfigureTriggerMode_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ConfigureTriggerMode_cfunc(vi, channel_name, trigger_mode)

    def niFgen_ConfigureTriggerSource(self, vi, channel_name, trigger_source):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ConfigureTriggerSource_cfunc is None:
                self.niFgen_ConfigureTriggerSource_cfunc = self._library.niFgen_ConfigureTriggerSource
                self.niFgen_ConfigureTriggerSource_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niFgen_ConfigureTriggerSource_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ConfigureTriggerSource_cfunc(vi, channel_name, trigger_source)

    def niFgen_ConfigureUpdateClockSource(self, vi, update_clock_source):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ConfigureUpdateClockSource_cfunc is None:
                self.niFgen_ConfigureUpdateClockSource_cfunc = self._library.niFgen_ConfigureUpdateClockSource
                self.niFgen_ConfigureUpdateClockSource_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niFgen_ConfigureUpdateClockSource_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ConfigureUpdateClockSource_cfunc(vi, update_clock_source)

    def niFgen_CreateAdvancedArbSequence(self, vi, sequence_length, waveform_handles_array, loop_counts_array, sample_counts_array, marker_location_array, coerced_markers_array, sequence_handle):  # noqa: N802
        with self._func_lock:
            if self.niFgen_CreateAdvancedArbSequence_cfunc is None:
                self.niFgen_CreateAdvancedArbSequence_cfunc = self._library.niFgen_CreateAdvancedArbSequence
                self.niFgen_CreateAdvancedArbSequence_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_CreateAdvancedArbSequence_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_CreateAdvancedArbSequence_cfunc(vi, sequence_length, waveform_handles_array, loop_counts_array, sample_counts_array, marker_location_array, coerced_markers_array, sequence_handle)

    def niFgen_CreateArbSequence(self, vi, sequence_length, waveform_handles_array, loop_counts_array, sequence_handle):  # noqa: N802
        with self._func_lock:
            if self.niFgen_CreateArbSequence_cfunc is None:
                self.niFgen_CreateArbSequence_cfunc = self._library.niFgen_CreateArbSequence
                self.niFgen_CreateArbSequence_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_CreateArbSequence_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_CreateArbSequence_cfunc(vi, sequence_length, waveform_handles_array, loop_counts_array, sequence_handle)

    def niFgen_CreateArbWaveform(self, vi, waveform_size, waveform_data_array, waveform_handle):  # noqa: N802
        with self._func_lock:
            if self.niFgen_CreateArbWaveform_cfunc is None:
                self.niFgen_CreateArbWaveform_cfunc = self._library.niFgen_CreateArbWaveform
                self.niFgen_CreateArbWaveform_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_CreateArbWaveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_CreateArbWaveform_cfunc(vi, waveform_size, waveform_data_array, waveform_handle)

    def niFgen_CreateBinary16ArbWaveform(self, vi, waveform_size, waveform_data_array, waveform_handle):  # noqa: N802
        with self._func_lock:
            if self.niFgen_CreateBinary16ArbWaveform_cfunc is None:
                self.niFgen_CreateBinary16ArbWaveform_cfunc = self._library.niFgen_CreateBinary16ArbWaveform
                self.niFgen_CreateBinary16ArbWaveform_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt16), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_CreateBinary16ArbWaveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_CreateBinary16ArbWaveform_cfunc(vi, waveform_size, waveform_data_array, waveform_handle)

    def niFgen_CreateFreqList(self, vi, waveform, frequency_list_length, frequency_array, duration_array, frequency_list_handle):  # noqa: N802
        with self._func_lock:
            if self.niFgen_CreateFreqList_cfunc is None:
                self.niFgen_CreateFreqList_cfunc = self._library.niFgen_CreateFreqList
                self.niFgen_CreateFreqList_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_CreateFreqList_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_CreateFreqList_cfunc(vi, waveform, frequency_list_length, frequency_array, duration_array, frequency_list_handle)

    def niFgen_CreateWaveformF64(self, vi, channel_name, waveform_size, waveform_data_array, waveform_handle):  # noqa: N802
        with self._func_lock:
            if self.niFgen_CreateWaveformF64_cfunc is None:
                self.niFgen_CreateWaveformF64_cfunc = self._library.niFgen_CreateWaveformF64
                self.niFgen_CreateWaveformF64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_CreateWaveformF64_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_CreateWaveformF64_cfunc(vi, channel_name, waveform_size, waveform_data_array, waveform_handle)

    def niFgen_CreateWaveformFromFileF64(self, vi, channel_name, file_name, byte_order, waveform_handle):  # noqa: N802
        with self._func_lock:
            if self.niFgen_CreateWaveformFromFileF64_cfunc is None:
                self.niFgen_CreateWaveformFromFileF64_cfunc = self._library.niFgen_CreateWaveformFromFileF64
                self.niFgen_CreateWaveformFromFileF64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_CreateWaveformFromFileF64_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_CreateWaveformFromFileF64_cfunc(vi, channel_name, file_name, byte_order, waveform_handle)

    def niFgen_CreateWaveformFromFileHWS(self, vi, channel_name, file_name, use_rate_from_waveform, use_gain_and_offset_from_waveform, waveform_handle):  # noqa: N802
        with self._func_lock:
            if self.niFgen_CreateWaveformFromFileHWS_cfunc is None:
                self.niFgen_CreateWaveformFromFileHWS_cfunc = self._library.niFgen_CreateWaveformFromFileHWS
                self.niFgen_CreateWaveformFromFileHWS_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViBoolean, ViBoolean, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_CreateWaveformFromFileHWS_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_CreateWaveformFromFileHWS_cfunc(vi, channel_name, file_name, use_rate_from_waveform, use_gain_and_offset_from_waveform, waveform_handle)

    def niFgen_CreateWaveformFromFileI16(self, vi, channel_name, file_name, byte_order, waveform_handle):  # noqa: N802
        with self._func_lock:
            if self.niFgen_CreateWaveformFromFileI16_cfunc is None:
                self.niFgen_CreateWaveformFromFileI16_cfunc = self._library.niFgen_CreateWaveformFromFileI16
                self.niFgen_CreateWaveformFromFileI16_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_CreateWaveformFromFileI16_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_CreateWaveformFromFileI16_cfunc(vi, channel_name, file_name, byte_order, waveform_handle)

    def niFgen_CreateWaveformI16(self, vi, channel_name, waveform_size, waveform_data_array, waveform_handle):  # noqa: N802
        with self._func_lock:
            if self.niFgen_CreateWaveformI16_cfunc is None:
                self.niFgen_CreateWaveformI16_cfunc = self._library.niFgen_CreateWaveformI16
                self.niFgen_CreateWaveformI16_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt16), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_CreateWaveformI16_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_CreateWaveformI16_cfunc(vi, channel_name, waveform_size, waveform_data_array, waveform_handle)

    def niFgen_DefineUserStandardWaveform(self, vi, channel_name, waveform_size, waveform_data_array):  # noqa: N802
        with self._func_lock:
            if self.niFgen_DefineUserStandardWaveform_cfunc is None:
                self.niFgen_DefineUserStandardWaveform_cfunc = self._library.niFgen_DefineUserStandardWaveform
                self.niFgen_DefineUserStandardWaveform_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFgen_DefineUserStandardWaveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_DefineUserStandardWaveform_cfunc(vi, channel_name, waveform_size, waveform_data_array)

    def niFgen_DeleteNamedWaveform(self, vi, channel_name, waveform_name):  # noqa: N802
        with self._func_lock:
            if self.niFgen_DeleteNamedWaveform_cfunc is None:
                self.niFgen_DeleteNamedWaveform_cfunc = self._library.niFgen_DeleteNamedWaveform
                self.niFgen_DeleteNamedWaveform_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_DeleteNamedWaveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_DeleteNamedWaveform_cfunc(vi, channel_name, waveform_name)

    def niFgen_DeleteScript(self, vi, channel_name, script_name):  # noqa: N802
        with self._func_lock:
            if self.niFgen_DeleteScript_cfunc is None:
                self.niFgen_DeleteScript_cfunc = self._library.niFgen_DeleteScript
                self.niFgen_DeleteScript_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_DeleteScript_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_DeleteScript_cfunc(vi, channel_name, script_name)

    def niFgen_Disable(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFgen_Disable_cfunc is None:
                self.niFgen_Disable_cfunc = self._library.niFgen_Disable
                self.niFgen_Disable_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFgen_Disable_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_Disable_cfunc(vi)

    def niFgen_DisableAnalogFilter(self, vi, channel_name):  # noqa: N802
        with self._func_lock:
            if self.niFgen_DisableAnalogFilter_cfunc is None:
                self.niFgen_DisableAnalogFilter_cfunc = self._library.niFgen_DisableAnalogFilter
                self.niFgen_DisableAnalogFilter_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_DisableAnalogFilter_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_DisableAnalogFilter_cfunc(vi, channel_name)

    def niFgen_DisableDigitalFilter(self, vi, channel_name):  # noqa: N802
        with self._func_lock:
            if self.niFgen_DisableDigitalFilter_cfunc is None:
                self.niFgen_DisableDigitalFilter_cfunc = self._library.niFgen_DisableDigitalFilter
                self.niFgen_DisableDigitalFilter_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_DisableDigitalFilter_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_DisableDigitalFilter_cfunc(vi, channel_name)

    def niFgen_DisableDigitalPatterning(self, vi, channel_name):  # noqa: N802
        with self._func_lock:
            if self.niFgen_DisableDigitalPatterning_cfunc is None:
                self.niFgen_DisableDigitalPatterning_cfunc = self._library.niFgen_DisableDigitalPatterning
                self.niFgen_DisableDigitalPatterning_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_DisableDigitalPatterning_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_DisableDigitalPatterning_cfunc(vi, channel_name)

    def niFgen_DisableScriptTrigger(self, vi, trigger_id):  # noqa: N802
        with self._func_lock:
            if self.niFgen_DisableScriptTrigger_cfunc is None:
                self.niFgen_DisableScriptTrigger_cfunc = self._library.niFgen_DisableScriptTrigger
                self.niFgen_DisableScriptTrigger_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_DisableScriptTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_DisableScriptTrigger_cfunc(vi, trigger_id)

    def niFgen_DisableStartTrigger(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFgen_DisableStartTrigger_cfunc is None:
                self.niFgen_DisableStartTrigger_cfunc = self._library.niFgen_DisableStartTrigger
                self.niFgen_DisableStartTrigger_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFgen_DisableStartTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_DisableStartTrigger_cfunc(vi)

    def niFgen_EnableAnalogFilter(self, vi, channel_name, filter_correction_frequency):  # noqa: N802
        with self._func_lock:
            if self.niFgen_EnableAnalogFilter_cfunc is None:
                self.niFgen_EnableAnalogFilter_cfunc = self._library.niFgen_EnableAnalogFilter
                self.niFgen_EnableAnalogFilter_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64]  # noqa: F405
                self.niFgen_EnableAnalogFilter_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_EnableAnalogFilter_cfunc(vi, channel_name, filter_correction_frequency)

    def niFgen_EnableDigitalFilter(self, vi, channel_name):  # noqa: N802
        with self._func_lock:
            if self.niFgen_EnableDigitalFilter_cfunc is None:
                self.niFgen_EnableDigitalFilter_cfunc = self._library.niFgen_EnableDigitalFilter
                self.niFgen_EnableDigitalFilter_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_EnableDigitalFilter_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_EnableDigitalFilter_cfunc(vi, channel_name)

    def niFgen_EnableDigitalPatterning(self, vi, channel_name):  # noqa: N802
        with self._func_lock:
            if self.niFgen_EnableDigitalPatterning_cfunc is None:
                self.niFgen_EnableDigitalPatterning_cfunc = self._library.niFgen_EnableDigitalPatterning
                self.niFgen_EnableDigitalPatterning_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_EnableDigitalPatterning_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_EnableDigitalPatterning_cfunc(vi, channel_name)

    def niFgen_ErrorHandler(self, vi, error_code, error_message):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ErrorHandler_cfunc is None:
                self.niFgen_ErrorHandler_cfunc = self._library.niFgen_ErrorHandler
                self.niFgen_ErrorHandler_cfunc.argtypes = [ViSession, ViStatus, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_ErrorHandler_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ErrorHandler_cfunc(vi, error_code, error_message)

    def niFgen_ExportSignal(self, vi, signal, signal_identifier, output_terminal):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ExportSignal_cfunc is None:
                self.niFgen_ExportSignal_cfunc = self._library.niFgen_ExportSignal
                self.niFgen_ExportSignal_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_ExportSignal_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ExportSignal_cfunc(vi, signal, signal_identifier, output_terminal)

    def niFgen_GetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFgen_GetAttributeViBoolean_cfunc is None:
                self.niFgen_GetAttributeViBoolean_cfunc = self._library.niFgen_GetAttributeViBoolean
                self.niFgen_GetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niFgen_GetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_GetAttributeViBoolean_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFgen_GetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFgen_GetAttributeViInt32_cfunc is None:
                self.niFgen_GetAttributeViInt32_cfunc = self._library.niFgen_GetAttributeViInt32
                self.niFgen_GetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_GetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_GetAttributeViInt32_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFgen_GetAttributeViInt64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFgen_GetAttributeViInt64_cfunc is None:
                self.niFgen_GetAttributeViInt64_cfunc = self._library.niFgen_GetAttributeViInt64
                self.niFgen_GetAttributeViInt64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViInt64)]  # noqa: F405
                self.niFgen_GetAttributeViInt64_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_GetAttributeViInt64_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFgen_GetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFgen_GetAttributeViReal64_cfunc is None:
                self.niFgen_GetAttributeViReal64_cfunc = self._library.niFgen_GetAttributeViReal64
                self.niFgen_GetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFgen_GetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_GetAttributeViReal64_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFgen_GetAttributeViString(self, vi, channel_name, attribute_id, array_size, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFgen_GetAttributeViString_cfunc is None:
                self.niFgen_GetAttributeViString_cfunc = self._library.niFgen_GetAttributeViString
                self.niFgen_GetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_GetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_GetAttributeViString_cfunc(vi, channel_name, attribute_id, array_size, attribute_value)

    def niFgen_GetError(self, vi, error_code, error_description_buffer_size, error_description):  # noqa: N802
        with self._func_lock:
            if self.niFgen_GetError_cfunc is None:
                self.niFgen_GetError_cfunc = self._library.niFgen_GetError
                self.niFgen_GetError_cfunc.argtypes = [ViSession, ctypes.POINTER(ViStatus), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_GetError_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_GetError_cfunc(vi, error_code, error_description_buffer_size, error_description)

    def niFgen_GetFIRFilterCoefficients(self, vi, channel_name, array_size, coefficients_array, number_of_coefficients_read):  # noqa: N802
        with self._func_lock:
            if self.niFgen_GetFIRFilterCoefficients_cfunc is None:
                self.niFgen_GetFIRFilterCoefficients_cfunc = self._library.niFgen_GetFIRFilterCoefficients
                self.niFgen_GetFIRFilterCoefficients_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_GetFIRFilterCoefficients_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_GetFIRFilterCoefficients_cfunc(vi, channel_name, array_size, coefficients_array, number_of_coefficients_read)

    def niFgen_GetHardwareState(self, vi, state):  # noqa: N802
        with self._func_lock:
            if self.niFgen_GetHardwareState_cfunc is None:
                self.niFgen_GetHardwareState_cfunc = self._library.niFgen_GetHardwareState
                self.niFgen_GetHardwareState_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_GetHardwareState_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_GetHardwareState_cfunc(vi, state)

    def niFgen_GetSelfCalLastDateAndTime(self, vi, year, month, day, hour, minute):  # noqa: N802
        with self._func_lock:
            if self.niFgen_GetSelfCalLastDateAndTime_cfunc is None:
                self.niFgen_GetSelfCalLastDateAndTime_cfunc = self._library.niFgen_GetSelfCalLastDateAndTime
                self.niFgen_GetSelfCalLastDateAndTime_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_GetSelfCalLastDateAndTime_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_GetSelfCalLastDateAndTime_cfunc(vi, year, month, day, hour, minute)

    def niFgen_GetSelfCalLastTemp(self, vi, temperature):  # noqa: N802
        with self._func_lock:
            if self.niFgen_GetSelfCalLastTemp_cfunc is None:
                self.niFgen_GetSelfCalLastTemp_cfunc = self._library.niFgen_GetSelfCalLastTemp
                self.niFgen_GetSelfCalLastTemp_cfunc.argtypes = [ViSession, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFgen_GetSelfCalLastTemp_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_GetSelfCalLastTemp_cfunc(vi, temperature)

    def niFgen_GetSelfCalSupported(self, vi, self_cal_supported):  # noqa: N802
        with self._func_lock:
            if self.niFgen_GetSelfCalSupported_cfunc is None:
                self.niFgen_GetSelfCalSupported_cfunc = self._library.niFgen_GetSelfCalSupported
                self.niFgen_GetSelfCalSupported_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niFgen_GetSelfCalSupported_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_GetSelfCalSupported_cfunc(vi, self_cal_supported)

    def niFgen_InitWithOptions(self, resource_name, id_query, reset_device, option_string, vi):  # noqa: N802
        with self._func_lock:
            if self.niFgen_InitWithOptions_cfunc is None:
                self.niFgen_InitWithOptions_cfunc = self._library.niFgen_InitWithOptions
                self.niFgen_InitWithOptions_cfunc.argtypes = [ctypes.POINTER(ViChar), ViBoolean, ViBoolean, ctypes.POINTER(ViChar), ctypes.POINTER(ViSession)]  # noqa: F405
                self.niFgen_InitWithOptions_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_InitWithOptions_cfunc(resource_name, id_query, reset_device, option_string, vi)

    def niFgen_InitializeAnalogOutputCalibration(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFgen_InitializeAnalogOutputCalibration_cfunc is None:
                self.niFgen_InitializeAnalogOutputCalibration_cfunc = self._library.niFgen_InitializeAnalogOutputCalibration
                self.niFgen_InitializeAnalogOutputCalibration_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFgen_InitializeAnalogOutputCalibration_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_InitializeAnalogOutputCalibration_cfunc(vi)

    def niFgen_InitializeCalADCCalibration(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFgen_InitializeCalADCCalibration_cfunc is None:
                self.niFgen_InitializeCalADCCalibration_cfunc = self._library.niFgen_InitializeCalADCCalibration
                self.niFgen_InitializeCalADCCalibration_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFgen_InitializeCalADCCalibration_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_InitializeCalADCCalibration_cfunc(vi)

    def niFgen_InitializeFlatnessCalibration(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFgen_InitializeFlatnessCalibration_cfunc is None:
                self.niFgen_InitializeFlatnessCalibration_cfunc = self._library.niFgen_InitializeFlatnessCalibration
                self.niFgen_InitializeFlatnessCalibration_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFgen_InitializeFlatnessCalibration_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_InitializeFlatnessCalibration_cfunc(vi)

    def niFgen_InitializeOscillatorFrequencyCalibration(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFgen_InitializeOscillatorFrequencyCalibration_cfunc is None:
                self.niFgen_InitializeOscillatorFrequencyCalibration_cfunc = self._library.niFgen_InitializeOscillatorFrequencyCalibration
                self.niFgen_InitializeOscillatorFrequencyCalibration_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFgen_InitializeOscillatorFrequencyCalibration_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_InitializeOscillatorFrequencyCalibration_cfunc(vi)

    def niFgen_InitializeWithChannels(self, resource_name, channel_name, reset_device, option_string, vi):  # noqa: N802
        with self._func_lock:
            if self.niFgen_InitializeWithChannels_cfunc is None:
                self.niFgen_InitializeWithChannels_cfunc = self._library.niFgen_InitializeWithChannels
                self.niFgen_InitializeWithChannels_cfunc.argtypes = [ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViBoolean, ctypes.POINTER(ViChar), ctypes.POINTER(ViSession)]  # noqa: F405
                self.niFgen_InitializeWithChannels_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_InitializeWithChannels_cfunc(resource_name, channel_name, reset_device, option_string, vi)

    def niFgen_InitiateGeneration(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFgen_InitiateGeneration_cfunc is None:
                self.niFgen_InitiateGeneration_cfunc = self._library.niFgen_InitiateGeneration
                self.niFgen_InitiateGeneration_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFgen_InitiateGeneration_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_InitiateGeneration_cfunc(vi)

    def niFgen_IsDone(self, vi, done):  # noqa: N802
        with self._func_lock:
            if self.niFgen_IsDone_cfunc is None:
                self.niFgen_IsDone_cfunc = self._library.niFgen_IsDone
                self.niFgen_IsDone_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niFgen_IsDone_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_IsDone_cfunc(vi, done)

    def niFgen_ManualEnableP2PStream(self, vi, endpoint_name):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ManualEnableP2PStream_cfunc is None:
                self.niFgen_ManualEnableP2PStream_cfunc = self._library.niFgen_ManualEnableP2PStream
                self.niFgen_ManualEnableP2PStream_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_ManualEnableP2PStream_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ManualEnableP2PStream_cfunc(vi, endpoint_name)

    def niFgen_QueryArbSeqCapabilities(self, vi, maximum_number_of_sequences, minimum_sequence_length, maximum_sequence_length, maximum_loop_count):  # noqa: N802
        with self._func_lock:
            if self.niFgen_QueryArbSeqCapabilities_cfunc is None:
                self.niFgen_QueryArbSeqCapabilities_cfunc = self._library.niFgen_QueryArbSeqCapabilities
                self.niFgen_QueryArbSeqCapabilities_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_QueryArbSeqCapabilities_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_QueryArbSeqCapabilities_cfunc(vi, maximum_number_of_sequences, minimum_sequence_length, maximum_sequence_length, maximum_loop_count)

    def niFgen_QueryArbWfmCapabilities(self, vi, maximum_number_of_waveforms, waveform_quantum, minimum_waveform_size, maximum_waveform_size):  # noqa: N802
        with self._func_lock:
            if self.niFgen_QueryArbWfmCapabilities_cfunc is None:
                self.niFgen_QueryArbWfmCapabilities_cfunc = self._library.niFgen_QueryArbWfmCapabilities
                self.niFgen_QueryArbWfmCapabilities_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_QueryArbWfmCapabilities_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_QueryArbWfmCapabilities_cfunc(vi, maximum_number_of_waveforms, waveform_quantum, minimum_waveform_size, maximum_waveform_size)

    def niFgen_QueryFreqListCapabilities(self, vi, maximum_number_of_freq_lists, minimum_frequency_list_length, maximum_frequency_list_length, minimum_frequency_list_duration, maximum_frequency_list_duration, frequency_list_duration_quantum):  # noqa: N802
        with self._func_lock:
            if self.niFgen_QueryFreqListCapabilities_cfunc is None:
                self.niFgen_QueryFreqListCapabilities_cfunc = self._library.niFgen_QueryFreqListCapabilities
                self.niFgen_QueryFreqListCapabilities_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFgen_QueryFreqListCapabilities_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_QueryFreqListCapabilities_cfunc(vi, maximum_number_of_freq_lists, minimum_frequency_list_length, maximum_frequency_list_length, minimum_frequency_list_duration, maximum_frequency_list_duration, frequency_list_duration_quantum)

    def niFgen_ReadCalADC(self, vi, number_of_reads_to_average, return_calibrated_value, cal_adc_value):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ReadCalADC_cfunc is None:
                self.niFgen_ReadCalADC_cfunc = self._library.niFgen_ReadCalADC
                self.niFgen_ReadCalADC_cfunc.argtypes = [ViSession, ViInt32, ViBoolean, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFgen_ReadCalADC_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ReadCalADC_cfunc(vi, number_of_reads_to_average, return_calibrated_value, cal_adc_value)

    def niFgen_ReadCurrentTemperature(self, vi, temperature):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ReadCurrentTemperature_cfunc is None:
                self.niFgen_ReadCurrentTemperature_cfunc = self._library.niFgen_ReadCurrentTemperature
                self.niFgen_ReadCurrentTemperature_cfunc.argtypes = [ViSession, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFgen_ReadCurrentTemperature_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ReadCurrentTemperature_cfunc(vi, temperature)

    def niFgen_ResetAttribute(self, vi, channel_name, attribute_id):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ResetAttribute_cfunc is None:
                self.niFgen_ResetAttribute_cfunc = self._library.niFgen_ResetAttribute
                self.niFgen_ResetAttribute_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr]  # noqa: F405
                self.niFgen_ResetAttribute_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ResetAttribute_cfunc(vi, channel_name, attribute_id)

    def niFgen_ResetDevice(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ResetDevice_cfunc is None:
                self.niFgen_ResetDevice_cfunc = self._library.niFgen_ResetDevice
                self.niFgen_ResetDevice_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFgen_ResetDevice_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ResetDevice_cfunc(vi)

    def niFgen_ResetWithDefaults(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ResetWithDefaults_cfunc is None:
                self.niFgen_ResetWithDefaults_cfunc = self._library.niFgen_ResetWithDefaults
                self.niFgen_ResetWithDefaults_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFgen_ResetWithDefaults_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ResetWithDefaults_cfunc(vi)

    def niFgen_RouteSignalOut(self, vi, channel_name, route_signal_from, route_signal_to):  # noqa: N802
        with self._func_lock:
            if self.niFgen_RouteSignalOut_cfunc is None:
                self.niFgen_RouteSignalOut_cfunc = self._library.niFgen_RouteSignalOut
                self.niFgen_RouteSignalOut_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViInt32]  # noqa: F405
                self.niFgen_RouteSignalOut_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_RouteSignalOut_cfunc(vi, channel_name, route_signal_from, route_signal_to)

    def niFgen_SelfCal(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFgen_SelfCal_cfunc is None:
                self.niFgen_SelfCal_cfunc = self._library.niFgen_SelfCal
                self.niFgen_SelfCal_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFgen_SelfCal_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_SelfCal_cfunc(vi)

    def niFgen_SendSoftwareEdgeTrigger(self, vi, trigger, trigger_id):  # noqa: N802
        with self._func_lock:
            if self.niFgen_SendSoftwareEdgeTrigger_cfunc is None:
                self.niFgen_SendSoftwareEdgeTrigger_cfunc = self._library.niFgen_SendSoftwareEdgeTrigger
                self.niFgen_SendSoftwareEdgeTrigger_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_SendSoftwareEdgeTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_SendSoftwareEdgeTrigger_cfunc(vi, trigger, trigger_id)

    def niFgen_SendSoftwareTrigger(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFgen_SendSoftwareTrigger_cfunc is None:
                self.niFgen_SendSoftwareTrigger_cfunc = self._library.niFgen_SendSoftwareTrigger
                self.niFgen_SendSoftwareTrigger_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFgen_SendSoftwareTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_SendSoftwareTrigger_cfunc(vi)

    def niFgen_SetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFgen_SetAttributeViBoolean_cfunc is None:
                self.niFgen_SetAttributeViBoolean_cfunc = self._library.niFgen_SetAttributeViBoolean
                self.niFgen_SetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViBoolean]  # noqa: F405
                self.niFgen_SetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_SetAttributeViBoolean_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFgen_SetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFgen_SetAttributeViInt32_cfunc is None:
                self.niFgen_SetAttributeViInt32_cfunc = self._library.niFgen_SetAttributeViInt32
                self.niFgen_SetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32]  # noqa: F405
                self.niFgen_SetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_SetAttributeViInt32_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFgen_SetAttributeViInt64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFgen_SetAttributeViInt64_cfunc is None:
                self.niFgen_SetAttributeViInt64_cfunc = self._library.niFgen_SetAttributeViInt64
                self.niFgen_SetAttributeViInt64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt64]  # noqa: F405
                self.niFgen_SetAttributeViInt64_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_SetAttributeViInt64_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFgen_SetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFgen_SetAttributeViReal64_cfunc is None:
                self.niFgen_SetAttributeViReal64_cfunc = self._library.niFgen_SetAttributeViReal64
                self.niFgen_SetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViReal64]  # noqa: F405
                self.niFgen_SetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_SetAttributeViReal64_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFgen_SetAttributeViString(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFgen_SetAttributeViString_cfunc is None:
                self.niFgen_SetAttributeViString_cfunc = self._library.niFgen_SetAttributeViString
                self.niFgen_SetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_SetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_SetAttributeViString_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFgen_SetNamedWaveformNextWritePosition(self, vi, channel_name, waveform_name, relative_to, offset):  # noqa: N802
        with self._func_lock:
            if self.niFgen_SetNamedWaveformNextWritePosition_cfunc is None:
                self.niFgen_SetNamedWaveformNextWritePosition_cfunc = self._library.niFgen_SetNamedWaveformNextWritePosition
                self.niFgen_SetNamedWaveformNextWritePosition_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ViInt32]  # noqa: F405
                self.niFgen_SetNamedWaveformNextWritePosition_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_SetNamedWaveformNextWritePosition_cfunc(vi, channel_name, waveform_name, relative_to, offset)

    def niFgen_SetWaveformNextWritePosition(self, vi, channel_name, waveform_handle, relative_to, offset):  # noqa: N802
        with self._func_lock:
            if self.niFgen_SetWaveformNextWritePosition_cfunc is None:
                self.niFgen_SetWaveformNextWritePosition_cfunc = self._library.niFgen_SetWaveformNextWritePosition
                self.niFgen_SetWaveformNextWritePosition_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViInt32, ViInt32]  # noqa: F405
                self.niFgen_SetWaveformNextWritePosition_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_SetWaveformNextWritePosition_cfunc(vi, channel_name, waveform_handle, relative_to, offset)

    def niFgen_WaitUntilDone(self, vi, max_time):  # noqa: N802
        with self._func_lock:
            if self.niFgen_WaitUntilDone_cfunc is None:
                self.niFgen_WaitUntilDone_cfunc = self._library.niFgen_WaitUntilDone
                self.niFgen_WaitUntilDone_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niFgen_WaitUntilDone_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_WaitUntilDone_cfunc(vi, max_time)

    def niFgen_WriteBinary16AnalogStaticValue(self, vi, channel_name, value):  # noqa: N802
        with self._func_lock:
            if self.niFgen_WriteBinary16AnalogStaticValue_cfunc is None:
                self.niFgen_WriteBinary16AnalogStaticValue_cfunc = self._library.niFgen_WriteBinary16AnalogStaticValue
                self.niFgen_WriteBinary16AnalogStaticValue_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt16]  # noqa: F405
                self.niFgen_WriteBinary16AnalogStaticValue_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_WriteBinary16AnalogStaticValue_cfunc(vi, channel_name, value)

    def niFgen_WriteBinary16Waveform(self, vi, channel_name, waveform_handle, size, data):  # noqa: N802
        with self._func_lock:
            if self.niFgen_WriteBinary16Waveform_cfunc is None:
                self.niFgen_WriteBinary16Waveform_cfunc = self._library.niFgen_WriteBinary16Waveform
                self.niFgen_WriteBinary16Waveform_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViInt32, ctypes.POINTER(ViInt16)]  # noqa: F405
                self.niFgen_WriteBinary16Waveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_WriteBinary16Waveform_cfunc(vi, channel_name, waveform_handle, size, data)

    def niFgen_WriteNamedWaveformF64(self, vi, channel_name, waveform_name, size, data):  # noqa: N802
        with self._func_lock:
            if self.niFgen_WriteNamedWaveformF64_cfunc is None:
                self.niFgen_WriteNamedWaveformF64_cfunc = self._library.niFgen_WriteNamedWaveformF64
                self.niFgen_WriteNamedWaveformF64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFgen_WriteNamedWaveformF64_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_WriteNamedWaveformF64_cfunc(vi, channel_name, waveform_name, size, data)

    def niFgen_WriteNamedWaveformI16(self, vi, channel_name, waveform_name, size, data):  # noqa: N802
        with self._func_lock:
            if self.niFgen_WriteNamedWaveformI16_cfunc is None:
                self.niFgen_WriteNamedWaveformI16_cfunc = self._library.niFgen_WriteNamedWaveformI16
                self.niFgen_WriteNamedWaveformI16_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt16)]  # noqa: F405
                self.niFgen_WriteNamedWaveformI16_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_WriteNamedWaveformI16_cfunc(vi, channel_name, waveform_name, size, data)

    def niFgen_WriteP2PEndpointI16(self, vi, endpoint_name, number_of_samples, endpoint_data):  # noqa: N802
        with self._func_lock:
            if self.niFgen_WriteP2PEndpointI16_cfunc is None:
                self.niFgen_WriteP2PEndpointI16_cfunc = self._library.niFgen_WriteP2PEndpointI16
                self.niFgen_WriteP2PEndpointI16_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt16)]  # noqa: F405
                self.niFgen_WriteP2PEndpointI16_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_WriteP2PEndpointI16_cfunc(vi, endpoint_name, number_of_samples, endpoint_data)

    def niFgen_WriteScript(self, vi, channel_name, script):  # noqa: N802
        with self._func_lock:
            if self.niFgen_WriteScript_cfunc is None:
                self.niFgen_WriteScript_cfunc = self._library.niFgen_WriteScript
                self.niFgen_WriteScript_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_WriteScript_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_WriteScript_cfunc(vi, channel_name, script)

    def niFgen_WriteWaveform(self, vi, channel_name, waveform_handle, size, data):  # noqa: N802
        with self._func_lock:
            if self.niFgen_WriteWaveform_cfunc is None:
                self.niFgen_WriteWaveform_cfunc = self._library.niFgen_WriteWaveform
                self.niFgen_WriteWaveform_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFgen_WriteWaveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_WriteWaveform_cfunc(vi, channel_name, waveform_handle, size, data)

    def niFgen_close(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFgen_close_cfunc is None:
                self.niFgen_close_cfunc = self._library.niFgen_close
                self.niFgen_close_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFgen_close_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_close_cfunc(vi)

    def niFgen_error_message(self, vi, error_code, error_message):  # noqa: N802
        with self._func_lock:
            if self.niFgen_error_message_cfunc is None:
                self.niFgen_error_message_cfunc = self._library.niFgen_error_message
                self.niFgen_error_message_cfunc.argtypes = [ViSession, ViStatus, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_error_message_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_error_message_cfunc(vi, error_code, error_message)

    def niFgen_reset(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFgen_reset_cfunc is None:
                self.niFgen_reset_cfunc = self._library.niFgen_reset
                self.niFgen_reset_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFgen_reset_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_reset_cfunc(vi)

    def niFgen_self_test(self, vi, self_test_result, self_test_message):  # noqa: N802
        with self._func_lock:
            if self.niFgen_self_test_cfunc is None:
                self.niFgen_self_test_cfunc = self._library.niFgen_self_test
                self.niFgen_self_test_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt16), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_self_test_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_self_test_cfunc(vi, self_test_result, self_test_message)
