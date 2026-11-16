# -*- coding: utf-8 -*-
# This file was generated

import ctypes
import nifgen.errors as errors
import threading

from nifgen._visatype import *  # noqa: F403,H303


class Library(object):
    '''Library

    Wrapper around driver library.
    Class will setup the correct ctypes information for every function on first call.
    '''

    def __init__(self, ctypes_library):
        self._func_lock = threading.Lock()
        self._library = ctypes_library
        # We cache the cfunc object from the ctypes.CDLL object
        self.niFgen_AbortGeneration_cfunc = None
        self.niFgen_AllocateNamedWaveform_cfunc = None
        self.niFgen_AllocateWaveform_cfunc = None
        self.niFgen_ClearArbMemory_cfunc = None
        self.niFgen_ClearArbSequence_cfunc = None
        self.niFgen_ClearArbWaveform_cfunc = None
        self.niFgen_ClearFreqList_cfunc = None
        self.niFgen_ClearUserStandardWaveform_cfunc = None
        self.niFgen_Commit_cfunc = None
        self.niFgen_ConfigureArbSequence_cfunc = None
        self.niFgen_ConfigureArbWaveform_cfunc = None
        self.niFgen_ConfigureFreqList_cfunc = None
        self.niFgen_ConfigureStandardWaveform_cfunc = None
        self.niFgen_CreateAdvancedArbSequence_cfunc = None
        self.niFgen_CreateArbSequence_cfunc = None
        self.niFgen_CreateFreqList_cfunc = None
        self.niFgen_CreateWaveformF64_cfunc = None
        self.niFgen_CreateWaveformFromFileF64_cfunc = None
        self.niFgen_CreateWaveformFromFileI16_cfunc = None
        self.niFgen_CreateWaveformI16_cfunc = None
        self.niFgen_DefineUserStandardWaveform_cfunc = None
        self.niFgen_DeleteNamedWaveform_cfunc = None
        self.niFgen_DeleteScript_cfunc = None
        self.niFgen_Disable_cfunc = None
        self.niFgen_ExportAttributeConfigurationBuffer_cfunc = None
        self.niFgen_ExportAttributeConfigurationFile_cfunc = None
        self.niFgen_GetAttributeViBoolean_cfunc = None
        self.niFgen_GetAttributeViInt32_cfunc = None
        self.niFgen_GetAttributeViReal64_cfunc = None
        self.niFgen_GetAttributeViString_cfunc = None
        self.niFgen_GetChannelName_cfunc = None
        self.niFgen_GetError_cfunc = None
        self.niFgen_GetExtCalLastDateAndTime_cfunc = None
        self.niFgen_GetExtCalLastTemp_cfunc = None
        self.niFgen_GetExtCalRecommendedInterval_cfunc = None
        self.niFgen_GetHardwareState_cfunc = None
        self.niFgen_GetSelfCalLastDateAndTime_cfunc = None
        self.niFgen_GetSelfCalLastTemp_cfunc = None
        self.niFgen_GetSelfCalSupported_cfunc = None
        self.niFgen_ImportAttributeConfigurationBuffer_cfunc = None
        self.niFgen_ImportAttributeConfigurationFile_cfunc = None
        self.niFgen_InitializeWithChannels_cfunc = None
        self.niFgen_InitiateGeneration_cfunc = None
        self.niFgen_IsDone_cfunc = None
        self.niFgen_LockSession_cfunc = None
        self.niFgen_QueryArbSeqCapabilities_cfunc = None
        self.niFgen_QueryArbWfmCapabilities_cfunc = None
        self.niFgen_QueryFreqListCapabilities_cfunc = None
        self.niFgen_ReadCurrentTemperature_cfunc = None
        self.niFgen_ResetDevice_cfunc = None
        self.niFgen_ResetWithDefaults_cfunc = None
        self.niFgen_SelfCal_cfunc = None
        self.niFgen_SendSoftwareEdgeTrigger_cfunc = None
        self.niFgen_SetAttributeViBoolean_cfunc = None
        self.niFgen_SetAttributeViInt32_cfunc = None
        self.niFgen_SetAttributeViReal64_cfunc = None
        self.niFgen_SetAttributeViString_cfunc = None
        self.niFgen_SetNamedWaveformNextWritePosition_cfunc = None
        self.niFgen_SetRuntimeEnvironment_cfunc = None
        self.niFgen_SetWaveformNextWritePosition_cfunc = None
        self.niFgen_UnlockSession_cfunc = None
        self.niFgen_WaitUntilDone_cfunc = None
        self.niFgen_WriteBinary16Waveform_cfunc = None
        self.niFgen_WriteNamedWaveformF64_cfunc = None
        self.niFgen_WriteNamedWaveformI16_cfunc = None
        self.niFgen_WriteScript_cfunc = None
        self.niFgen_WriteWaveform_cfunc = None
        self.niFgen_close_cfunc = None
        self.niFgen_error_message_cfunc = None
        self.niFgen_reset_cfunc = None
        self.niFgen_self_test_cfunc = None

    def _get_library_function(self, name):
        try:
            function = getattr(self._library, name)
        except AttributeError as e:
            raise errors.DriverTooOldError() from e
        return function

    def niFgen_AbortGeneration(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFgen_AbortGeneration_cfunc is None:
                self.niFgen_AbortGeneration_cfunc = self._get_library_function('niFgen_AbortGeneration')
                self.niFgen_AbortGeneration_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFgen_AbortGeneration_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_AbortGeneration_cfunc(vi)

    def niFgen_AllocateNamedWaveform(self, vi, channel_name, waveform_name, waveform_size):  # noqa: N802
        with self._func_lock:
            if self.niFgen_AllocateNamedWaveform_cfunc is None:
                self.niFgen_AllocateNamedWaveform_cfunc = self._get_library_function('niFgen_AllocateNamedWaveform')
                self.niFgen_AllocateNamedWaveform_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niFgen_AllocateNamedWaveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_AllocateNamedWaveform_cfunc(vi, channel_name, waveform_name, waveform_size)

    def niFgen_AllocateWaveform(self, vi, channel_name, waveform_size, waveform_handle):  # noqa: N802
        with self._func_lock:
            if self.niFgen_AllocateWaveform_cfunc is None:
                self.niFgen_AllocateWaveform_cfunc = self._get_library_function('niFgen_AllocateWaveform')
                self.niFgen_AllocateWaveform_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_AllocateWaveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_AllocateWaveform_cfunc(vi, channel_name, waveform_size, waveform_handle)

    def niFgen_ClearArbMemory(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ClearArbMemory_cfunc is None:
                self.niFgen_ClearArbMemory_cfunc = self._get_library_function('niFgen_ClearArbMemory')
                self.niFgen_ClearArbMemory_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFgen_ClearArbMemory_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ClearArbMemory_cfunc(vi)

    def niFgen_ClearArbSequence(self, vi, sequence_handle):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ClearArbSequence_cfunc is None:
                self.niFgen_ClearArbSequence_cfunc = self._get_library_function('niFgen_ClearArbSequence')
                self.niFgen_ClearArbSequence_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niFgen_ClearArbSequence_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ClearArbSequence_cfunc(vi, sequence_handle)

    def niFgen_ClearArbWaveform(self, vi, waveform_handle):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ClearArbWaveform_cfunc is None:
                self.niFgen_ClearArbWaveform_cfunc = self._get_library_function('niFgen_ClearArbWaveform')
                self.niFgen_ClearArbWaveform_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niFgen_ClearArbWaveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ClearArbWaveform_cfunc(vi, waveform_handle)

    def niFgen_ClearFreqList(self, vi, frequency_list_handle):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ClearFreqList_cfunc is None:
                self.niFgen_ClearFreqList_cfunc = self._get_library_function('niFgen_ClearFreqList')
                self.niFgen_ClearFreqList_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niFgen_ClearFreqList_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ClearFreqList_cfunc(vi, frequency_list_handle)

    def niFgen_ClearUserStandardWaveform(self, vi, channel_name):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ClearUserStandardWaveform_cfunc is None:
                self.niFgen_ClearUserStandardWaveform_cfunc = self._get_library_function('niFgen_ClearUserStandardWaveform')
                self.niFgen_ClearUserStandardWaveform_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_ClearUserStandardWaveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ClearUserStandardWaveform_cfunc(vi, channel_name)

    def niFgen_Commit(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFgen_Commit_cfunc is None:
                self.niFgen_Commit_cfunc = self._get_library_function('niFgen_Commit')
                self.niFgen_Commit_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFgen_Commit_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_Commit_cfunc(vi)

    def niFgen_ConfigureArbSequence(self, vi, channel_name, sequence_handle, gain, offset):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ConfigureArbSequence_cfunc is None:
                self.niFgen_ConfigureArbSequence_cfunc = self._get_library_function('niFgen_ConfigureArbSequence')
                self.niFgen_ConfigureArbSequence_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViReal64, ViReal64]  # noqa: F405
                self.niFgen_ConfigureArbSequence_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ConfigureArbSequence_cfunc(vi, channel_name, sequence_handle, gain, offset)

    def niFgen_ConfigureArbWaveform(self, vi, channel_name, waveform_handle, gain, offset):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ConfigureArbWaveform_cfunc is None:
                self.niFgen_ConfigureArbWaveform_cfunc = self._get_library_function('niFgen_ConfigureArbWaveform')
                self.niFgen_ConfigureArbWaveform_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViReal64, ViReal64]  # noqa: F405
                self.niFgen_ConfigureArbWaveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ConfigureArbWaveform_cfunc(vi, channel_name, waveform_handle, gain, offset)

    def niFgen_ConfigureFreqList(self, vi, channel_name, frequency_list_handle, amplitude, dc_offset, start_phase):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ConfigureFreqList_cfunc is None:
                self.niFgen_ConfigureFreqList_cfunc = self._get_library_function('niFgen_ConfigureFreqList')
                self.niFgen_ConfigureFreqList_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViReal64, ViReal64, ViReal64]  # noqa: F405
                self.niFgen_ConfigureFreqList_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ConfigureFreqList_cfunc(vi, channel_name, frequency_list_handle, amplitude, dc_offset, start_phase)

    def niFgen_ConfigureStandardWaveform(self, vi, channel_name, waveform, amplitude, dc_offset, frequency, start_phase):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ConfigureStandardWaveform_cfunc is None:
                self.niFgen_ConfigureStandardWaveform_cfunc = self._get_library_function('niFgen_ConfigureStandardWaveform')
                self.niFgen_ConfigureStandardWaveform_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViReal64, ViReal64, ViReal64, ViReal64]  # noqa: F405
                self.niFgen_ConfigureStandardWaveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ConfigureStandardWaveform_cfunc(vi, channel_name, waveform, amplitude, dc_offset, frequency, start_phase)

    def niFgen_CreateAdvancedArbSequence(self, vi, sequence_length, waveform_handles_array, loop_counts_array, sample_counts_array, marker_location_array, coerced_markers_array, sequence_handle):  # noqa: N802
        with self._func_lock:
            if self.niFgen_CreateAdvancedArbSequence_cfunc is None:
                self.niFgen_CreateAdvancedArbSequence_cfunc = self._get_library_function('niFgen_CreateAdvancedArbSequence')
                self.niFgen_CreateAdvancedArbSequence_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_CreateAdvancedArbSequence_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_CreateAdvancedArbSequence_cfunc(vi, sequence_length, waveform_handles_array, loop_counts_array, sample_counts_array, marker_location_array, coerced_markers_array, sequence_handle)

    def niFgen_CreateArbSequence(self, vi, sequence_length, waveform_handles_array, loop_counts_array, sequence_handle):  # noqa: N802
        with self._func_lock:
            if self.niFgen_CreateArbSequence_cfunc is None:
                self.niFgen_CreateArbSequence_cfunc = self._get_library_function('niFgen_CreateArbSequence')
                self.niFgen_CreateArbSequence_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_CreateArbSequence_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_CreateArbSequence_cfunc(vi, sequence_length, waveform_handles_array, loop_counts_array, sequence_handle)

    def niFgen_CreateFreqList(self, vi, waveform, frequency_list_length, frequency_array, duration_array, frequency_list_handle):  # noqa: N802
        with self._func_lock:
            if self.niFgen_CreateFreqList_cfunc is None:
                self.niFgen_CreateFreqList_cfunc = self._get_library_function('niFgen_CreateFreqList')
                self.niFgen_CreateFreqList_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_CreateFreqList_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_CreateFreqList_cfunc(vi, waveform, frequency_list_length, frequency_array, duration_array, frequency_list_handle)

    def niFgen_CreateWaveformF64(self, vi, channel_name, waveform_size, waveform_data_array, waveform_handle):  # noqa: N802
        with self._func_lock:
            if self.niFgen_CreateWaveformF64_cfunc is None:
                self.niFgen_CreateWaveformF64_cfunc = self._get_library_function('niFgen_CreateWaveformF64')
                self.niFgen_CreateWaveformF64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_CreateWaveformF64_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_CreateWaveformF64_cfunc(vi, channel_name, waveform_size, waveform_data_array, waveform_handle)

    def niFgen_CreateWaveformFromFileF64(self, vi, channel_name, file_name, byte_order, waveform_handle):  # noqa: N802
        with self._func_lock:
            if self.niFgen_CreateWaveformFromFileF64_cfunc is None:
                self.niFgen_CreateWaveformFromFileF64_cfunc = self._get_library_function('niFgen_CreateWaveformFromFileF64')
                self.niFgen_CreateWaveformFromFileF64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_CreateWaveformFromFileF64_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_CreateWaveformFromFileF64_cfunc(vi, channel_name, file_name, byte_order, waveform_handle)

    def niFgen_CreateWaveformFromFileI16(self, vi, channel_name, file_name, byte_order, waveform_handle):  # noqa: N802
        with self._func_lock:
            if self.niFgen_CreateWaveformFromFileI16_cfunc is None:
                self.niFgen_CreateWaveformFromFileI16_cfunc = self._get_library_function('niFgen_CreateWaveformFromFileI16')
                self.niFgen_CreateWaveformFromFileI16_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_CreateWaveformFromFileI16_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_CreateWaveformFromFileI16_cfunc(vi, channel_name, file_name, byte_order, waveform_handle)

    def niFgen_CreateWaveformI16(self, vi, channel_name, waveform_size, waveform_data_array, waveform_handle):  # noqa: N802
        with self._func_lock:
            if self.niFgen_CreateWaveformI16_cfunc is None:
                self.niFgen_CreateWaveformI16_cfunc = self._get_library_function('niFgen_CreateWaveformI16')
                self.niFgen_CreateWaveformI16_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt16), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_CreateWaveformI16_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_CreateWaveformI16_cfunc(vi, channel_name, waveform_size, waveform_data_array, waveform_handle)

    def niFgen_DefineUserStandardWaveform(self, vi, channel_name, waveform_size, waveform_data_array):  # noqa: N802
        with self._func_lock:
            if self.niFgen_DefineUserStandardWaveform_cfunc is None:
                self.niFgen_DefineUserStandardWaveform_cfunc = self._get_library_function('niFgen_DefineUserStandardWaveform')
                self.niFgen_DefineUserStandardWaveform_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFgen_DefineUserStandardWaveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_DefineUserStandardWaveform_cfunc(vi, channel_name, waveform_size, waveform_data_array)

    def niFgen_DeleteNamedWaveform(self, vi, channel_name, waveform_name):  # noqa: N802
        with self._func_lock:
            if self.niFgen_DeleteNamedWaveform_cfunc is None:
                self.niFgen_DeleteNamedWaveform_cfunc = self._get_library_function('niFgen_DeleteNamedWaveform')
                self.niFgen_DeleteNamedWaveform_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_DeleteNamedWaveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_DeleteNamedWaveform_cfunc(vi, channel_name, waveform_name)

    def niFgen_DeleteScript(self, vi, channel_name, script_name):  # noqa: N802
        with self._func_lock:
            if self.niFgen_DeleteScript_cfunc is None:
                self.niFgen_DeleteScript_cfunc = self._get_library_function('niFgen_DeleteScript')
                self.niFgen_DeleteScript_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_DeleteScript_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_DeleteScript_cfunc(vi, channel_name, script_name)

    def niFgen_Disable(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFgen_Disable_cfunc is None:
                self.niFgen_Disable_cfunc = self._get_library_function('niFgen_Disable')
                self.niFgen_Disable_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFgen_Disable_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_Disable_cfunc(vi)

    def niFgen_ExportAttributeConfigurationBuffer(self, vi, size_in_bytes, configuration):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ExportAttributeConfigurationBuffer_cfunc is None:
                self.niFgen_ExportAttributeConfigurationBuffer_cfunc = self._get_library_function('niFgen_ExportAttributeConfigurationBuffer')
                self.niFgen_ExportAttributeConfigurationBuffer_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt8)]  # noqa: F405
                self.niFgen_ExportAttributeConfigurationBuffer_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ExportAttributeConfigurationBuffer_cfunc(vi, size_in_bytes, configuration)

    def niFgen_ExportAttributeConfigurationFile(self, vi, file_path):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ExportAttributeConfigurationFile_cfunc is None:
                self.niFgen_ExportAttributeConfigurationFile_cfunc = self._get_library_function('niFgen_ExportAttributeConfigurationFile')
                self.niFgen_ExportAttributeConfigurationFile_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_ExportAttributeConfigurationFile_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ExportAttributeConfigurationFile_cfunc(vi, file_path)

    def niFgen_GetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFgen_GetAttributeViBoolean_cfunc is None:
                self.niFgen_GetAttributeViBoolean_cfunc = self._get_library_function('niFgen_GetAttributeViBoolean')
                self.niFgen_GetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niFgen_GetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_GetAttributeViBoolean_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFgen_GetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFgen_GetAttributeViInt32_cfunc is None:
                self.niFgen_GetAttributeViInt32_cfunc = self._get_library_function('niFgen_GetAttributeViInt32')
                self.niFgen_GetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_GetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_GetAttributeViInt32_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFgen_GetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFgen_GetAttributeViReal64_cfunc is None:
                self.niFgen_GetAttributeViReal64_cfunc = self._get_library_function('niFgen_GetAttributeViReal64')
                self.niFgen_GetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFgen_GetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_GetAttributeViReal64_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFgen_GetAttributeViString(self, vi, channel_name, attribute_id, array_size, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFgen_GetAttributeViString_cfunc is None:
                self.niFgen_GetAttributeViString_cfunc = self._get_library_function('niFgen_GetAttributeViString')
                self.niFgen_GetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_GetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_GetAttributeViString_cfunc(vi, channel_name, attribute_id, array_size, attribute_value)

    def niFgen_GetChannelName(self, vi, index, buffer_size, channel_string):  # noqa: N802
        with self._func_lock:
            if self.niFgen_GetChannelName_cfunc is None:
                self.niFgen_GetChannelName_cfunc = self._get_library_function('niFgen_GetChannelName')
                self.niFgen_GetChannelName_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_GetChannelName_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_GetChannelName_cfunc(vi, index, buffer_size, channel_string)

    def niFgen_GetError(self, vi, error_code, error_description_buffer_size, error_description):  # noqa: N802
        with self._func_lock:
            if self.niFgen_GetError_cfunc is None:
                self.niFgen_GetError_cfunc = self._get_library_function('niFgen_GetError')
                self.niFgen_GetError_cfunc.argtypes = [ViSession, ctypes.POINTER(ViStatus), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_GetError_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_GetError_cfunc(vi, error_code, error_description_buffer_size, error_description)

    def niFgen_GetExtCalLastDateAndTime(self, vi, year, month, day, hour, minute):  # noqa: N802
        with self._func_lock:
            if self.niFgen_GetExtCalLastDateAndTime_cfunc is None:
                self.niFgen_GetExtCalLastDateAndTime_cfunc = self._get_library_function('niFgen_GetExtCalLastDateAndTime')
                self.niFgen_GetExtCalLastDateAndTime_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_GetExtCalLastDateAndTime_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_GetExtCalLastDateAndTime_cfunc(vi, year, month, day, hour, minute)

    def niFgen_GetExtCalLastTemp(self, vi, temperature):  # noqa: N802
        with self._func_lock:
            if self.niFgen_GetExtCalLastTemp_cfunc is None:
                self.niFgen_GetExtCalLastTemp_cfunc = self._get_library_function('niFgen_GetExtCalLastTemp')
                self.niFgen_GetExtCalLastTemp_cfunc.argtypes = [ViSession, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFgen_GetExtCalLastTemp_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_GetExtCalLastTemp_cfunc(vi, temperature)

    def niFgen_GetExtCalRecommendedInterval(self, vi, months):  # noqa: N802
        with self._func_lock:
            if self.niFgen_GetExtCalRecommendedInterval_cfunc is None:
                self.niFgen_GetExtCalRecommendedInterval_cfunc = self._get_library_function('niFgen_GetExtCalRecommendedInterval')
                self.niFgen_GetExtCalRecommendedInterval_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_GetExtCalRecommendedInterval_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_GetExtCalRecommendedInterval_cfunc(vi, months)

    def niFgen_GetHardwareState(self, vi, state):  # noqa: N802
        with self._func_lock:
            if self.niFgen_GetHardwareState_cfunc is None:
                self.niFgen_GetHardwareState_cfunc = self._get_library_function('niFgen_GetHardwareState')
                self.niFgen_GetHardwareState_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_GetHardwareState_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_GetHardwareState_cfunc(vi, state)

    def niFgen_GetSelfCalLastDateAndTime(self, vi, year, month, day, hour, minute):  # noqa: N802
        with self._func_lock:
            if self.niFgen_GetSelfCalLastDateAndTime_cfunc is None:
                self.niFgen_GetSelfCalLastDateAndTime_cfunc = self._get_library_function('niFgen_GetSelfCalLastDateAndTime')
                self.niFgen_GetSelfCalLastDateAndTime_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_GetSelfCalLastDateAndTime_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_GetSelfCalLastDateAndTime_cfunc(vi, year, month, day, hour, minute)

    def niFgen_GetSelfCalLastTemp(self, vi, temperature):  # noqa: N802
        with self._func_lock:
            if self.niFgen_GetSelfCalLastTemp_cfunc is None:
                self.niFgen_GetSelfCalLastTemp_cfunc = self._get_library_function('niFgen_GetSelfCalLastTemp')
                self.niFgen_GetSelfCalLastTemp_cfunc.argtypes = [ViSession, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFgen_GetSelfCalLastTemp_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_GetSelfCalLastTemp_cfunc(vi, temperature)

    def niFgen_GetSelfCalSupported(self, vi, self_cal_supported):  # noqa: N802
        with self._func_lock:
            if self.niFgen_GetSelfCalSupported_cfunc is None:
                self.niFgen_GetSelfCalSupported_cfunc = self._get_library_function('niFgen_GetSelfCalSupported')
                self.niFgen_GetSelfCalSupported_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niFgen_GetSelfCalSupported_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_GetSelfCalSupported_cfunc(vi, self_cal_supported)

    def niFgen_ImportAttributeConfigurationBuffer(self, vi, size_in_bytes, configuration):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ImportAttributeConfigurationBuffer_cfunc is None:
                self.niFgen_ImportAttributeConfigurationBuffer_cfunc = self._get_library_function('niFgen_ImportAttributeConfigurationBuffer')
                self.niFgen_ImportAttributeConfigurationBuffer_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt8)]  # noqa: F405
                self.niFgen_ImportAttributeConfigurationBuffer_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ImportAttributeConfigurationBuffer_cfunc(vi, size_in_bytes, configuration)

    def niFgen_ImportAttributeConfigurationFile(self, vi, file_path):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ImportAttributeConfigurationFile_cfunc is None:
                self.niFgen_ImportAttributeConfigurationFile_cfunc = self._get_library_function('niFgen_ImportAttributeConfigurationFile')
                self.niFgen_ImportAttributeConfigurationFile_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_ImportAttributeConfigurationFile_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ImportAttributeConfigurationFile_cfunc(vi, file_path)

    def niFgen_InitializeWithChannels(self, resource_name, channel_name, reset_device, option_string, vi):  # noqa: N802
        with self._func_lock:
            if self.niFgen_InitializeWithChannels_cfunc is None:
                self.niFgen_InitializeWithChannels_cfunc = self._get_library_function('niFgen_InitializeWithChannels')
                self.niFgen_InitializeWithChannels_cfunc.argtypes = [ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViBoolean, ctypes.POINTER(ViChar), ctypes.POINTER(ViSession)]  # noqa: F405
                self.niFgen_InitializeWithChannels_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_InitializeWithChannels_cfunc(resource_name, channel_name, reset_device, option_string, vi)

    def niFgen_InitiateGeneration(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFgen_InitiateGeneration_cfunc is None:
                self.niFgen_InitiateGeneration_cfunc = self._get_library_function('niFgen_InitiateGeneration')
                self.niFgen_InitiateGeneration_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFgen_InitiateGeneration_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_InitiateGeneration_cfunc(vi)

    def niFgen_IsDone(self, vi, done):  # noqa: N802
        with self._func_lock:
            if self.niFgen_IsDone_cfunc is None:
                self.niFgen_IsDone_cfunc = self._get_library_function('niFgen_IsDone')
                self.niFgen_IsDone_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niFgen_IsDone_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_IsDone_cfunc(vi, done)

    def niFgen_LockSession(self, vi, caller_has_lock):  # noqa: N802
        with self._func_lock:
            if self.niFgen_LockSession_cfunc is None:
                self.niFgen_LockSession_cfunc = self._get_library_function('niFgen_LockSession')
                self.niFgen_LockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niFgen_LockSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_LockSession_cfunc(vi, caller_has_lock)

    def niFgen_QueryArbSeqCapabilities(self, vi, maximum_number_of_sequences, minimum_sequence_length, maximum_sequence_length, maximum_loop_count):  # noqa: N802
        with self._func_lock:
            if self.niFgen_QueryArbSeqCapabilities_cfunc is None:
                self.niFgen_QueryArbSeqCapabilities_cfunc = self._get_library_function('niFgen_QueryArbSeqCapabilities')
                self.niFgen_QueryArbSeqCapabilities_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_QueryArbSeqCapabilities_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_QueryArbSeqCapabilities_cfunc(vi, maximum_number_of_sequences, minimum_sequence_length, maximum_sequence_length, maximum_loop_count)

    def niFgen_QueryArbWfmCapabilities(self, vi, maximum_number_of_waveforms, waveform_quantum, minimum_waveform_size, maximum_waveform_size):  # noqa: N802
        with self._func_lock:
            if self.niFgen_QueryArbWfmCapabilities_cfunc is None:
                self.niFgen_QueryArbWfmCapabilities_cfunc = self._get_library_function('niFgen_QueryArbWfmCapabilities')
                self.niFgen_QueryArbWfmCapabilities_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_QueryArbWfmCapabilities_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_QueryArbWfmCapabilities_cfunc(vi, maximum_number_of_waveforms, waveform_quantum, minimum_waveform_size, maximum_waveform_size)

    def niFgen_QueryFreqListCapabilities(self, vi, maximum_number_of_freq_lists, minimum_frequency_list_length, maximum_frequency_list_length, minimum_frequency_list_duration, maximum_frequency_list_duration, frequency_list_duration_quantum):  # noqa: N802
        with self._func_lock:
            if self.niFgen_QueryFreqListCapabilities_cfunc is None:
                self.niFgen_QueryFreqListCapabilities_cfunc = self._get_library_function('niFgen_QueryFreqListCapabilities')
                self.niFgen_QueryFreqListCapabilities_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFgen_QueryFreqListCapabilities_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_QueryFreqListCapabilities_cfunc(vi, maximum_number_of_freq_lists, minimum_frequency_list_length, maximum_frequency_list_length, minimum_frequency_list_duration, maximum_frequency_list_duration, frequency_list_duration_quantum)

    def niFgen_ReadCurrentTemperature(self, vi, temperature):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ReadCurrentTemperature_cfunc is None:
                self.niFgen_ReadCurrentTemperature_cfunc = self._get_library_function('niFgen_ReadCurrentTemperature')
                self.niFgen_ReadCurrentTemperature_cfunc.argtypes = [ViSession, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFgen_ReadCurrentTemperature_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ReadCurrentTemperature_cfunc(vi, temperature)

    def niFgen_ResetDevice(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ResetDevice_cfunc is None:
                self.niFgen_ResetDevice_cfunc = self._get_library_function('niFgen_ResetDevice')
                self.niFgen_ResetDevice_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFgen_ResetDevice_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ResetDevice_cfunc(vi)

    def niFgen_ResetWithDefaults(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ResetWithDefaults_cfunc is None:
                self.niFgen_ResetWithDefaults_cfunc = self._get_library_function('niFgen_ResetWithDefaults')
                self.niFgen_ResetWithDefaults_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFgen_ResetWithDefaults_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ResetWithDefaults_cfunc(vi)

    def niFgen_SelfCal(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFgen_SelfCal_cfunc is None:
                self.niFgen_SelfCal_cfunc = self._get_library_function('niFgen_SelfCal')
                self.niFgen_SelfCal_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFgen_SelfCal_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_SelfCal_cfunc(vi)

    def niFgen_SendSoftwareEdgeTrigger(self, vi, trigger, trigger_id):  # noqa: N802
        with self._func_lock:
            if self.niFgen_SendSoftwareEdgeTrigger_cfunc is None:
                self.niFgen_SendSoftwareEdgeTrigger_cfunc = self._get_library_function('niFgen_SendSoftwareEdgeTrigger')
                self.niFgen_SendSoftwareEdgeTrigger_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_SendSoftwareEdgeTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_SendSoftwareEdgeTrigger_cfunc(vi, trigger, trigger_id)

    def niFgen_SetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFgen_SetAttributeViBoolean_cfunc is None:
                self.niFgen_SetAttributeViBoolean_cfunc = self._get_library_function('niFgen_SetAttributeViBoolean')
                self.niFgen_SetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViBoolean]  # noqa: F405
                self.niFgen_SetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_SetAttributeViBoolean_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFgen_SetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFgen_SetAttributeViInt32_cfunc is None:
                self.niFgen_SetAttributeViInt32_cfunc = self._get_library_function('niFgen_SetAttributeViInt32')
                self.niFgen_SetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32]  # noqa: F405
                self.niFgen_SetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_SetAttributeViInt32_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFgen_SetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFgen_SetAttributeViReal64_cfunc is None:
                self.niFgen_SetAttributeViReal64_cfunc = self._get_library_function('niFgen_SetAttributeViReal64')
                self.niFgen_SetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViReal64]  # noqa: F405
                self.niFgen_SetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_SetAttributeViReal64_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFgen_SetAttributeViString(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFgen_SetAttributeViString_cfunc is None:
                self.niFgen_SetAttributeViString_cfunc = self._get_library_function('niFgen_SetAttributeViString')
                self.niFgen_SetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_SetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_SetAttributeViString_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFgen_SetNamedWaveformNextWritePosition(self, vi, channel_name, waveform_name, relative_to, offset):  # noqa: N802
        with self._func_lock:
            if self.niFgen_SetNamedWaveformNextWritePosition_cfunc is None:
                self.niFgen_SetNamedWaveformNextWritePosition_cfunc = self._get_library_function('niFgen_SetNamedWaveformNextWritePosition')
                self.niFgen_SetNamedWaveformNextWritePosition_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ViInt32]  # noqa: F405
                self.niFgen_SetNamedWaveformNextWritePosition_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_SetNamedWaveformNextWritePosition_cfunc(vi, channel_name, waveform_name, relative_to, offset)

    def niFgen_SetRuntimeEnvironment(self, environment, environment_version, reserved1, reserved2):  # noqa: N802
        with self._func_lock:
            if self.niFgen_SetRuntimeEnvironment_cfunc is None:
                self.niFgen_SetRuntimeEnvironment_cfunc = self._get_library_function('niFgen_SetRuntimeEnvironment')
                self.niFgen_SetRuntimeEnvironment_cfunc.argtypes = [ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_SetRuntimeEnvironment_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_SetRuntimeEnvironment_cfunc(environment, environment_version, reserved1, reserved2)

    def niFgen_SetWaveformNextWritePosition(self, vi, channel_name, waveform_handle, relative_to, offset):  # noqa: N802
        with self._func_lock:
            if self.niFgen_SetWaveformNextWritePosition_cfunc is None:
                self.niFgen_SetWaveformNextWritePosition_cfunc = self._get_library_function('niFgen_SetWaveformNextWritePosition')
                self.niFgen_SetWaveformNextWritePosition_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViInt32, ViInt32]  # noqa: F405
                self.niFgen_SetWaveformNextWritePosition_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_SetWaveformNextWritePosition_cfunc(vi, channel_name, waveform_handle, relative_to, offset)

    def niFgen_UnlockSession(self, vi, caller_has_lock):  # noqa: N802
        with self._func_lock:
            if self.niFgen_UnlockSession_cfunc is None:
                self.niFgen_UnlockSession_cfunc = self._get_library_function('niFgen_UnlockSession')
                self.niFgen_UnlockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niFgen_UnlockSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_UnlockSession_cfunc(vi, caller_has_lock)

    def niFgen_WaitUntilDone(self, vi, max_time):  # noqa: N802
        with self._func_lock:
            if self.niFgen_WaitUntilDone_cfunc is None:
                self.niFgen_WaitUntilDone_cfunc = self._get_library_function('niFgen_WaitUntilDone')
                self.niFgen_WaitUntilDone_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niFgen_WaitUntilDone_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_WaitUntilDone_cfunc(vi, max_time)

    def niFgen_WriteBinary16Waveform(self, vi, channel_name, waveform_handle, size, data):  # noqa: N802
        with self._func_lock:
            if self.niFgen_WriteBinary16Waveform_cfunc is None:
                self.niFgen_WriteBinary16Waveform_cfunc = self._get_library_function('niFgen_WriteBinary16Waveform')
                self.niFgen_WriteBinary16Waveform_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViInt32, ctypes.POINTER(ViInt16)]  # noqa: F405
                self.niFgen_WriteBinary16Waveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_WriteBinary16Waveform_cfunc(vi, channel_name, waveform_handle, size, data)

    def niFgen_WriteNamedWaveformF64(self, vi, channel_name, waveform_name, size, data):  # noqa: N802
        with self._func_lock:
            if self.niFgen_WriteNamedWaveformF64_cfunc is None:
                self.niFgen_WriteNamedWaveformF64_cfunc = self._get_library_function('niFgen_WriteNamedWaveformF64')
                self.niFgen_WriteNamedWaveformF64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFgen_WriteNamedWaveformF64_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_WriteNamedWaveformF64_cfunc(vi, channel_name, waveform_name, size, data)

    def niFgen_WriteNamedWaveformI16(self, vi, channel_name, waveform_name, size, data):  # noqa: N802
        with self._func_lock:
            if self.niFgen_WriteNamedWaveformI16_cfunc is None:
                self.niFgen_WriteNamedWaveformI16_cfunc = self._get_library_function('niFgen_WriteNamedWaveformI16')
                self.niFgen_WriteNamedWaveformI16_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt16)]  # noqa: F405
                self.niFgen_WriteNamedWaveformI16_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_WriteNamedWaveformI16_cfunc(vi, channel_name, waveform_name, size, data)

    def niFgen_WriteScript(self, vi, channel_name, script):  # noqa: N802
        with self._func_lock:
            if self.niFgen_WriteScript_cfunc is None:
                self.niFgen_WriteScript_cfunc = self._get_library_function('niFgen_WriteScript')
                self.niFgen_WriteScript_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_WriteScript_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_WriteScript_cfunc(vi, channel_name, script)

    def niFgen_WriteWaveform(self, vi, channel_name, waveform_handle, size, data):  # noqa: N802
        with self._func_lock:
            if self.niFgen_WriteWaveform_cfunc is None:
                self.niFgen_WriteWaveform_cfunc = self._get_library_function('niFgen_WriteWaveform')
                self.niFgen_WriteWaveform_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFgen_WriteWaveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_WriteWaveform_cfunc(vi, channel_name, waveform_handle, size, data)

    def niFgen_close(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFgen_close_cfunc is None:
                self.niFgen_close_cfunc = self._get_library_function('niFgen_close')
                self.niFgen_close_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFgen_close_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_close_cfunc(vi)

    def niFgen_error_message(self, vi, error_code, error_message):  # noqa: N802
        with self._func_lock:
            if self.niFgen_error_message_cfunc is None:
                self.niFgen_error_message_cfunc = self._get_library_function('niFgen_error_message')
                self.niFgen_error_message_cfunc.argtypes = [ViSession, ViStatus, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_error_message_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_error_message_cfunc(vi, error_code, error_message)

    def niFgen_reset(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFgen_reset_cfunc is None:
                self.niFgen_reset_cfunc = self._get_library_function('niFgen_reset')
                self.niFgen_reset_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFgen_reset_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_reset_cfunc(vi)

    def niFgen_self_test(self, vi, self_test_result, self_test_message):  # noqa: N802
        with self._func_lock:
            if self.niFgen_self_test_cfunc is None:
                self.niFgen_self_test_cfunc = self._get_library_function('niFgen_self_test')
                self.niFgen_self_test_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt16), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_self_test_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_self_test_cfunc(vi, self_test_result, self_test_message)
