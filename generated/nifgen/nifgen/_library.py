# -*- coding: utf-8 -*-
# This file was generated

import array  # noqa: F401
import ctypes
import hightime
import nifgen._converters as _converters
import nifgen._visatype as _visatype
import nifgen.enums as enums
import nifgen.errors as errors
import threading

from nifgen._visatype import *  # noqa: F403,H303


# Helper functions for creating ctypes needed for calling into the driver DLL
def get_ctypes_pointer_for_buffer(value=None, library_type=None, size=None):
    if isinstance(value, array.array):
        assert library_type is not None, 'library_type is required for array.array'
        addr, _ = value.buffer_info()
        return ctypes.cast(addr, ctypes.POINTER(library_type))
    elif str(type(value)).find("'numpy.ndarray'") != -1:
        import numpy
        return numpy.ctypeslib.as_ctypes(value)
    elif isinstance(value, bytes):
        return ctypes.cast(value, ctypes.POINTER(library_type))
    elif isinstance(value, list):
        assert library_type is not None, 'library_type is required for list'
        return (library_type * len(value))(*value)
    else:
        if library_type is not None and size is not None:
            return (library_type * size)()
        else:
            return None


def get_ctypes_and_array(value, array_type):
    if value is not None:
        if isinstance(value, array.array):
            value_array = value
        else:
            value_array = array.array(array_type, value)
    else:
        value_array = None

    return value_array


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

    def _get_error_description(self, session, error_code):
        '''_get_error_description

        Returns the error description.
        '''
        try:
            _, error_string = self._get_error(session)
            return error_string
        except errors.Error:
            pass

        try:
            '''
            It is expected for _get_error to raise when the session is invalid
            (IVI spec requires GetError to fail).
            Use _error_message instead. It doesn't require a session.
            '''
            error_string = self._error_message(session, error_code)
            return error_string
        except errors.Error:
            return "Failed to retrieve error description."

    def abort(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niFgen_AbortGeneration_cfunc is None:
                self.niFgen_AbortGeneration_cfunc = self._get_library_function('niFgen_AbortGeneration')
                self.niFgen_AbortGeneration_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFgen_AbortGeneration_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_AbortGeneration_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def allocate_named_waveform(self, session, channel_name, waveform_name, waveform_size):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(session._encoding))  # case C020
        waveform_size_ctype = _visatype.ViInt32(waveform_size)  # case S150
        with self._func_lock:
            if self.niFgen_AllocateNamedWaveform_cfunc is None:
                self.niFgen_AllocateNamedWaveform_cfunc = self._get_library_function('niFgen_AllocateNamedWaveform')
                self.niFgen_AllocateNamedWaveform_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niFgen_AllocateNamedWaveform_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_AllocateNamedWaveform_cfunc(vi_ctype, channel_name_ctype, waveform_name_ctype, waveform_size_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def allocate_waveform(self, session, channel_name, waveform_size):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        waveform_size_ctype = _visatype.ViInt32(waveform_size)  # case S150
        waveform_handle_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niFgen_AllocateWaveform_cfunc is None:
                self.niFgen_AllocateWaveform_cfunc = self._get_library_function('niFgen_AllocateWaveform')
                self.niFgen_AllocateWaveform_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_AllocateWaveform_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_AllocateWaveform_cfunc(vi_ctype, channel_name_ctype, waveform_size_ctype, None if waveform_handle_ctype is None else (ctypes.pointer(waveform_handle_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(waveform_handle_ctype.value)

    def clear_arb_memory(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niFgen_ClearArbMemory_cfunc is None:
                self.niFgen_ClearArbMemory_cfunc = self._get_library_function('niFgen_ClearArbMemory')
                self.niFgen_ClearArbMemory_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFgen_ClearArbMemory_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_ClearArbMemory_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def clear_arb_sequence(self, session, sequence_handle):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        sequence_handle_ctype = _visatype.ViInt32(sequence_handle)  # case S150
        with self._func_lock:
            if self.niFgen_ClearArbSequence_cfunc is None:
                self.niFgen_ClearArbSequence_cfunc = self._get_library_function('niFgen_ClearArbSequence')
                self.niFgen_ClearArbSequence_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niFgen_ClearArbSequence_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_ClearArbSequence_cfunc(vi_ctype, sequence_handle_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _clear_arb_waveform(self, session, waveform_handle):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        waveform_handle_ctype = _visatype.ViInt32(waveform_handle)  # case S150
        with self._func_lock:
            if self.niFgen_ClearArbWaveform_cfunc is None:
                self.niFgen_ClearArbWaveform_cfunc = self._get_library_function('niFgen_ClearArbWaveform')
                self.niFgen_ClearArbWaveform_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niFgen_ClearArbWaveform_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_ClearArbWaveform_cfunc(vi_ctype, waveform_handle_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def clear_freq_list(self, session, frequency_list_handle):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        frequency_list_handle_ctype = _visatype.ViInt32(frequency_list_handle)  # case S150
        with self._func_lock:
            if self.niFgen_ClearFreqList_cfunc is None:
                self.niFgen_ClearFreqList_cfunc = self._get_library_function('niFgen_ClearFreqList')
                self.niFgen_ClearFreqList_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niFgen_ClearFreqList_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_ClearFreqList_cfunc(vi_ctype, frequency_list_handle_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def clear_user_standard_waveform(self, session, channel_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        with self._func_lock:
            if self.niFgen_ClearUserStandardWaveform_cfunc is None:
                self.niFgen_ClearUserStandardWaveform_cfunc = self._get_library_function('niFgen_ClearUserStandardWaveform')
                self.niFgen_ClearUserStandardWaveform_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_ClearUserStandardWaveform_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_ClearUserStandardWaveform_cfunc(vi_ctype, channel_name_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def commit(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niFgen_Commit_cfunc is None:
                self.niFgen_Commit_cfunc = self._get_library_function('niFgen_Commit')
                self.niFgen_Commit_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFgen_Commit_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_Commit_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_arb_sequence(self, session, channel_name, sequence_handle, gain, offset):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        sequence_handle_ctype = _visatype.ViInt32(sequence_handle)  # case S150
        gain_ctype = _visatype.ViReal64(gain)  # case S150
        offset_ctype = _visatype.ViReal64(offset)  # case S150
        with self._func_lock:
            if self.niFgen_ConfigureArbSequence_cfunc is None:
                self.niFgen_ConfigureArbSequence_cfunc = self._get_library_function('niFgen_ConfigureArbSequence')
                self.niFgen_ConfigureArbSequence_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViReal64, ViReal64]  # noqa: F405
                self.niFgen_ConfigureArbSequence_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_ConfigureArbSequence_cfunc(vi_ctype, channel_name_ctype, sequence_handle_ctype, gain_ctype, offset_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_arb_waveform(self, session, channel_name, waveform_handle, gain, offset):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        waveform_handle_ctype = _visatype.ViInt32(waveform_handle)  # case S150
        gain_ctype = _visatype.ViReal64(gain)  # case S150
        offset_ctype = _visatype.ViReal64(offset)  # case S150
        with self._func_lock:
            if self.niFgen_ConfigureArbWaveform_cfunc is None:
                self.niFgen_ConfigureArbWaveform_cfunc = self._get_library_function('niFgen_ConfigureArbWaveform')
                self.niFgen_ConfigureArbWaveform_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViReal64, ViReal64]  # noqa: F405
                self.niFgen_ConfigureArbWaveform_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_ConfigureArbWaveform_cfunc(vi_ctype, channel_name_ctype, waveform_handle_ctype, gain_ctype, offset_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_freq_list(self, session, channel_name, frequency_list_handle, amplitude, dc_offset=0.0, start_phase=0.0):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        frequency_list_handle_ctype = _visatype.ViInt32(frequency_list_handle)  # case S150
        amplitude_ctype = _visatype.ViReal64(amplitude)  # case S150
        dc_offset_ctype = _visatype.ViReal64(dc_offset)  # case S150
        start_phase_ctype = _visatype.ViReal64(start_phase)  # case S150
        with self._func_lock:
            if self.niFgen_ConfigureFreqList_cfunc is None:
                self.niFgen_ConfigureFreqList_cfunc = self._get_library_function('niFgen_ConfigureFreqList')
                self.niFgen_ConfigureFreqList_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViReal64, ViReal64, ViReal64]  # noqa: F405
                self.niFgen_ConfigureFreqList_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_ConfigureFreqList_cfunc(vi_ctype, channel_name_ctype, frequency_list_handle_ctype, amplitude_ctype, dc_offset_ctype, start_phase_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_standard_waveform(self, session, channel_name, waveform, amplitude, frequency, dc_offset=0.0, start_phase=0.0):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        waveform_ctype = _visatype.ViInt32(waveform.value)  # case S130
        amplitude_ctype = _visatype.ViReal64(amplitude)  # case S150
        dc_offset_ctype = _visatype.ViReal64(dc_offset)  # case S150
        frequency_ctype = _visatype.ViReal64(frequency)  # case S150
        start_phase_ctype = _visatype.ViReal64(start_phase)  # case S150
        with self._func_lock:
            if self.niFgen_ConfigureStandardWaveform_cfunc is None:
                self.niFgen_ConfigureStandardWaveform_cfunc = self._get_library_function('niFgen_ConfigureStandardWaveform')
                self.niFgen_ConfigureStandardWaveform_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViReal64, ViReal64, ViReal64, ViReal64]  # noqa: F405
                self.niFgen_ConfigureStandardWaveform_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_ConfigureStandardWaveform_cfunc(vi_ctype, channel_name_ctype, waveform_ctype, amplitude_ctype, dc_offset_ctype, frequency_ctype, start_phase_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_advanced_arb_sequence(self, session, waveform_handles_array, loop_counts_array, sample_counts_array=None, marker_location_array=None):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        sequence_length_ctype = _visatype.ViInt32(0 if waveform_handles_array is None else len(waveform_handles_array))  # case S160
        if loop_counts_array is not None and len(loop_counts_array) != len(waveform_handles_array):  # case S160
            raise ValueError("Length of loop_counts_array and waveform_handles_array parameters do not match.")  # case S160
        if sample_counts_array is not None and len(sample_counts_array) != len(waveform_handles_array):  # case S160
            raise ValueError("Length of sample_counts_array and waveform_handles_array parameters do not match.")  # case S160
        if marker_location_array is not None and len(marker_location_array) != len(waveform_handles_array):  # case S160
            raise ValueError("Length of marker_location_array and waveform_handles_array parameters do not match.")  # case S160
        waveform_handles_array_ctype = get_ctypes_pointer_for_buffer(value=waveform_handles_array, library_type=_visatype.ViInt32)  # case B550
        loop_counts_array_ctype = get_ctypes_pointer_for_buffer(value=loop_counts_array, library_type=_visatype.ViInt32)  # case B550
        sample_counts_array_ctype = get_ctypes_pointer_for_buffer(value=sample_counts_array, library_type=_visatype.ViInt32)  # case B550
        marker_location_array_ctype = get_ctypes_pointer_for_buffer(value=marker_location_array, library_type=_visatype.ViInt32)  # case B550
        coerced_markers_array_size = (0 if marker_location_array is None else len(marker_location_array))  # case B560
        coerced_markers_array_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViInt32, size=coerced_markers_array_size)  # case B560
        sequence_handle_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niFgen_CreateAdvancedArbSequence_cfunc is None:
                self.niFgen_CreateAdvancedArbSequence_cfunc = self._get_library_function('niFgen_CreateAdvancedArbSequence')
                self.niFgen_CreateAdvancedArbSequence_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_CreateAdvancedArbSequence_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_CreateAdvancedArbSequence_cfunc(vi_ctype, sequence_length_ctype, waveform_handles_array_ctype, loop_counts_array_ctype, sample_counts_array_ctype, marker_location_array_ctype, coerced_markers_array_ctype, None if sequence_handle_ctype is None else (ctypes.pointer(sequence_handle_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return [int(coerced_markers_array_ctype[i]) for i in range((0 if marker_location_array is None else len(marker_location_array)))], int(sequence_handle_ctype.value)

    def create_arb_sequence(self, session, waveform_handles_array, loop_counts_array):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        sequence_length_ctype = _visatype.ViInt32(0 if waveform_handles_array is None else len(waveform_handles_array))  # case S160
        if loop_counts_array is not None and len(loop_counts_array) != len(waveform_handles_array):  # case S160
            raise ValueError("Length of loop_counts_array and waveform_handles_array parameters do not match.")  # case S160
        waveform_handles_array_ctype = get_ctypes_pointer_for_buffer(value=waveform_handles_array, library_type=_visatype.ViInt32)  # case B550
        loop_counts_array_ctype = get_ctypes_pointer_for_buffer(value=loop_counts_array, library_type=_visatype.ViInt32)  # case B550
        sequence_handle_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niFgen_CreateArbSequence_cfunc is None:
                self.niFgen_CreateArbSequence_cfunc = self._get_library_function('niFgen_CreateArbSequence')
                self.niFgen_CreateArbSequence_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_CreateArbSequence_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_CreateArbSequence_cfunc(vi_ctype, sequence_length_ctype, waveform_handles_array_ctype, loop_counts_array_ctype, None if sequence_handle_ctype is None else (ctypes.pointer(sequence_handle_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(sequence_handle_ctype.value)

    def create_freq_list(self, session, waveform, frequency_array, duration_array):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        waveform_ctype = _visatype.ViInt32(waveform.value)  # case S130
        frequency_list_length_ctype = _visatype.ViInt32(0 if frequency_array is None else len(frequency_array))  # case S160
        if duration_array is not None and len(duration_array) != len(frequency_array):  # case S160
            raise ValueError("Length of duration_array and frequency_array parameters do not match.")  # case S160
        frequency_array_ctype = get_ctypes_pointer_for_buffer(value=frequency_array, library_type=_visatype.ViReal64)  # case B550
        duration_array_ctype = get_ctypes_pointer_for_buffer(value=duration_array, library_type=_visatype.ViReal64)  # case B550
        frequency_list_handle_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niFgen_CreateFreqList_cfunc is None:
                self.niFgen_CreateFreqList_cfunc = self._get_library_function('niFgen_CreateFreqList')
                self.niFgen_CreateFreqList_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_CreateFreqList_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_CreateFreqList_cfunc(vi_ctype, waveform_ctype, frequency_list_length_ctype, frequency_array_ctype, duration_array_ctype, None if frequency_list_handle_ctype is None else (ctypes.pointer(frequency_list_handle_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(frequency_list_handle_ctype.value)

    def _create_waveform_f64(self, session, channel_name, waveform_data_array):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        waveform_size_ctype = _visatype.ViInt32(0 if waveform_data_array is None else len(waveform_data_array))  # case S160
        waveform_data_array_array = get_ctypes_and_array(value=waveform_data_array, array_type="d")  # case B550
        waveform_data_array_ctype = get_ctypes_pointer_for_buffer(value=waveform_data_array_array, library_type=_visatype.ViReal64)  # case B550
        waveform_handle_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niFgen_CreateWaveformF64_cfunc is None:
                self.niFgen_CreateWaveformF64_cfunc = self._get_library_function('niFgen_CreateWaveformF64')
                self.niFgen_CreateWaveformF64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_CreateWaveformF64_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_CreateWaveformF64_cfunc(vi_ctype, channel_name_ctype, waveform_size_ctype, waveform_data_array_ctype, None if waveform_handle_ctype is None else (ctypes.pointer(waveform_handle_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(waveform_handle_ctype.value)

    def _create_waveform_f64_numpy(self, session, channel_name, waveform_data_array):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        waveform_size_ctype = _visatype.ViInt32(0 if waveform_data_array is None else len(waveform_data_array))  # case S160
        waveform_data_array_ctype = get_ctypes_pointer_for_buffer(value=waveform_data_array)  # case B510
        waveform_handle_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niFgen_CreateWaveformF64_cfunc is None:
                self.niFgen_CreateWaveformF64_cfunc = self._get_library_function('niFgen_CreateWaveformF64')
                self.niFgen_CreateWaveformF64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_CreateWaveformF64_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_CreateWaveformF64_cfunc(vi_ctype, channel_name_ctype, waveform_size_ctype, waveform_data_array_ctype, None if waveform_handle_ctype is None else (ctypes.pointer(waveform_handle_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(waveform_handle_ctype.value)

    def create_waveform_from_file_f64(self, session, channel_name, file_name, byte_order):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        file_name_ctype = ctypes.create_string_buffer(file_name.encode(session._encoding))  # case C020
        byte_order_ctype = _visatype.ViInt32(byte_order.value)  # case S130
        waveform_handle_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niFgen_CreateWaveformFromFileF64_cfunc is None:
                self.niFgen_CreateWaveformFromFileF64_cfunc = self._get_library_function('niFgen_CreateWaveformFromFileF64')
                self.niFgen_CreateWaveformFromFileF64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_CreateWaveformFromFileF64_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_CreateWaveformFromFileF64_cfunc(vi_ctype, channel_name_ctype, file_name_ctype, byte_order_ctype, None if waveform_handle_ctype is None else (ctypes.pointer(waveform_handle_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(waveform_handle_ctype.value)

    def create_waveform_from_file_i16(self, session, channel_name, file_name, byte_order):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        file_name_ctype = ctypes.create_string_buffer(file_name.encode(session._encoding))  # case C020
        byte_order_ctype = _visatype.ViInt32(byte_order.value)  # case S130
        waveform_handle_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niFgen_CreateWaveformFromFileI16_cfunc is None:
                self.niFgen_CreateWaveformFromFileI16_cfunc = self._get_library_function('niFgen_CreateWaveformFromFileI16')
                self.niFgen_CreateWaveformFromFileI16_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_CreateWaveformFromFileI16_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_CreateWaveformFromFileI16_cfunc(vi_ctype, channel_name_ctype, file_name_ctype, byte_order_ctype, None if waveform_handle_ctype is None else (ctypes.pointer(waveform_handle_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(waveform_handle_ctype.value)

    def _create_waveform_i16_numpy(self, session, channel_name, waveform_data_array):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        waveform_size_ctype = _visatype.ViInt32(0 if waveform_data_array is None else len(waveform_data_array))  # case S160
        waveform_data_array_ctype = get_ctypes_pointer_for_buffer(value=waveform_data_array)  # case B510
        waveform_handle_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niFgen_CreateWaveformI16_cfunc is None:
                self.niFgen_CreateWaveformI16_cfunc = self._get_library_function('niFgen_CreateWaveformI16')
                self.niFgen_CreateWaveformI16_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt16), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_CreateWaveformI16_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_CreateWaveformI16_cfunc(vi_ctype, channel_name_ctype, waveform_size_ctype, waveform_data_array_ctype, None if waveform_handle_ctype is None else (ctypes.pointer(waveform_handle_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(waveform_handle_ctype.value)

    def define_user_standard_waveform(self, session, channel_name, waveform_data_array):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        waveform_size_ctype = _visatype.ViInt32(0 if waveform_data_array is None else len(waveform_data_array))  # case S160
        waveform_data_array_ctype = get_ctypes_pointer_for_buffer(value=waveform_data_array, library_type=_visatype.ViReal64)  # case B550
        with self._func_lock:
            if self.niFgen_DefineUserStandardWaveform_cfunc is None:
                self.niFgen_DefineUserStandardWaveform_cfunc = self._get_library_function('niFgen_DefineUserStandardWaveform')
                self.niFgen_DefineUserStandardWaveform_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFgen_DefineUserStandardWaveform_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_DefineUserStandardWaveform_cfunc(vi_ctype, channel_name_ctype, waveform_size_ctype, waveform_data_array_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _delete_named_waveform(self, session, channel_name, waveform_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(session._encoding))  # case C020
        with self._func_lock:
            if self.niFgen_DeleteNamedWaveform_cfunc is None:
                self.niFgen_DeleteNamedWaveform_cfunc = self._get_library_function('niFgen_DeleteNamedWaveform')
                self.niFgen_DeleteNamedWaveform_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_DeleteNamedWaveform_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_DeleteNamedWaveform_cfunc(vi_ctype, channel_name_ctype, waveform_name_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def delete_script(self, session, channel_name, script_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        script_name_ctype = ctypes.create_string_buffer(script_name.encode(session._encoding))  # case C020
        with self._func_lock:
            if self.niFgen_DeleteScript_cfunc is None:
                self.niFgen_DeleteScript_cfunc = self._get_library_function('niFgen_DeleteScript')
                self.niFgen_DeleteScript_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_DeleteScript_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_DeleteScript_cfunc(vi_ctype, channel_name_ctype, script_name_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disable(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niFgen_Disable_cfunc is None:
                self.niFgen_Disable_cfunc = self._get_library_function('niFgen_Disable')
                self.niFgen_Disable_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFgen_Disable_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_Disable_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def export_attribute_configuration_buffer(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        size_in_bytes_ctype = _visatype.ViInt32()  # case S170
        configuration_ctype = None  # case B580
        with self._func_lock:
            if self.niFgen_ExportAttributeConfigurationBuffer_cfunc is None:
                self.niFgen_ExportAttributeConfigurationBuffer_cfunc = self._get_library_function('niFgen_ExportAttributeConfigurationBuffer')
                self.niFgen_ExportAttributeConfigurationBuffer_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt8)]  # noqa: F405
                self.niFgen_ExportAttributeConfigurationBuffer_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_ExportAttributeConfigurationBuffer_cfunc(vi_ctype, size_in_bytes_ctype, configuration_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=False)
        size_in_bytes_ctype = _visatype.ViInt32(error_code)  # case S180
        configuration_size = size_in_bytes_ctype.value  # case B590
        configuration_array = array.array("b", [0] * configuration_size)  # case B590
        configuration_ctype = get_ctypes_pointer_for_buffer(value=configuration_array, library_type=_visatype.ViInt8)  # case B590
        error_code = self.niFgen_ExportAttributeConfigurationBuffer_cfunc(vi_ctype, size_in_bytes_ctype, configuration_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return _converters.convert_to_bytes(configuration_array)

    def export_attribute_configuration_file(self, session, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(session._encoding))  # case C020
        with self._func_lock:
            if self.niFgen_ExportAttributeConfigurationFile_cfunc is None:
                self.niFgen_ExportAttributeConfigurationFile_cfunc = self._get_library_function('niFgen_ExportAttributeConfigurationFile')
                self.niFgen_ExportAttributeConfigurationFile_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_ExportAttributeConfigurationFile_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_ExportAttributeConfigurationFile_cfunc(vi_ctype, file_path_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _get_attribute_vi_boolean(self, session, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViBoolean()  # case S220
        with self._func_lock:
            if self.niFgen_GetAttributeViBoolean_cfunc is None:
                self.niFgen_GetAttributeViBoolean_cfunc = self._get_library_function('niFgen_GetAttributeViBoolean')
                self.niFgen_GetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niFgen_GetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_GetAttributeViBoolean_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(attribute_value_ctype.value)

    def _get_attribute_vi_int32(self, session, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niFgen_GetAttributeViInt32_cfunc is None:
                self.niFgen_GetAttributeViInt32_cfunc = self._get_library_function('niFgen_GetAttributeViInt32')
                self.niFgen_GetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_GetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_GetAttributeViInt32_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(attribute_value_ctype.value)

    def _get_attribute_vi_real64(self, session, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViReal64()  # case S220
        with self._func_lock:
            if self.niFgen_GetAttributeViReal64_cfunc is None:
                self.niFgen_GetAttributeViReal64_cfunc = self._get_library_function('niFgen_GetAttributeViReal64')
                self.niFgen_GetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFgen_GetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_GetAttributeViReal64_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return float(attribute_value_ctype.value)

    def _get_attribute_vi_string(self, session, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        array_size_ctype = _visatype.ViInt32()  # case S170
        attribute_value_ctype = None  # case C050
        with self._func_lock:
            if self.niFgen_GetAttributeViString_cfunc is None:
                self.niFgen_GetAttributeViString_cfunc = self._get_library_function('niFgen_GetAttributeViString')
                self.niFgen_GetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_GetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_GetAttributeViString_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, array_size_ctype, attribute_value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=False)
        array_size_ctype = _visatype.ViInt32(error_code)  # case S180
        attribute_value_ctype = (_visatype.ViChar * array_size_ctype.value)()  # case C060
        error_code = self.niFgen_GetAttributeViString_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, array_size_ctype, attribute_value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return attribute_value_ctype.value.decode(session._encoding)

    def get_channel_name(self, session, index):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        index_ctype = _visatype.ViInt32(index)  # case S150
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        channel_string_ctype = None  # case C050
        with self._func_lock:
            if self.niFgen_GetChannelName_cfunc is None:
                self.niFgen_GetChannelName_cfunc = self._get_library_function('niFgen_GetChannelName')
                self.niFgen_GetChannelName_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_GetChannelName_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_GetChannelName_cfunc(vi_ctype, index_ctype, buffer_size_ctype, channel_string_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        channel_string_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self.niFgen_GetChannelName_cfunc(vi_ctype, index_ctype, buffer_size_ctype, channel_string_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return channel_string_ctype.value.decode(session._encoding)

    def _get_error(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        error_code_ctype = _visatype.ViStatus()  # case S220
        error_description_buffer_size_ctype = _visatype.ViInt32()  # case S170
        error_description_ctype = None  # case C050
        with self._func_lock:
            if self.niFgen_GetError_cfunc is None:
                self.niFgen_GetError_cfunc = self._get_library_function('niFgen_GetError')
                self.niFgen_GetError_cfunc.argtypes = [ViSession, ctypes.POINTER(ViStatus), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_GetError_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_GetError_cfunc(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), error_description_buffer_size_ctype, error_description_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=True)
        error_description_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        error_description_ctype = (_visatype.ViChar * error_description_buffer_size_ctype.value)()  # case C060
        error_code = self.niFgen_GetError_cfunc(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), error_description_buffer_size_ctype, error_description_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=True)
        return int(error_code_ctype.value), error_description_ctype.value.decode(session._encoding)

    def _get_ext_cal_last_date_and_time(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        year_ctype = _visatype.ViInt32()  # case S220
        month_ctype = _visatype.ViInt32()  # case S220
        day_ctype = _visatype.ViInt32()  # case S220
        hour_ctype = _visatype.ViInt32()  # case S220
        minute_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niFgen_GetExtCalLastDateAndTime_cfunc is None:
                self.niFgen_GetExtCalLastDateAndTime_cfunc = self._get_library_function('niFgen_GetExtCalLastDateAndTime')
                self.niFgen_GetExtCalLastDateAndTime_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_GetExtCalLastDateAndTime_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_GetExtCalLastDateAndTime_cfunc(vi_ctype, None if year_ctype is None else (ctypes.pointer(year_ctype)), None if month_ctype is None else (ctypes.pointer(month_ctype)), None if day_ctype is None else (ctypes.pointer(day_ctype)), None if hour_ctype is None else (ctypes.pointer(hour_ctype)), None if minute_ctype is None else (ctypes.pointer(minute_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(year_ctype.value), int(month_ctype.value), int(day_ctype.value), int(hour_ctype.value), int(minute_ctype.value)

    def get_ext_cal_last_temp(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        temperature_ctype = _visatype.ViReal64()  # case S220
        with self._func_lock:
            if self.niFgen_GetExtCalLastTemp_cfunc is None:
                self.niFgen_GetExtCalLastTemp_cfunc = self._get_library_function('niFgen_GetExtCalLastTemp')
                self.niFgen_GetExtCalLastTemp_cfunc.argtypes = [ViSession, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFgen_GetExtCalLastTemp_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_GetExtCalLastTemp_cfunc(vi_ctype, None if temperature_ctype is None else (ctypes.pointer(temperature_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

    def get_ext_cal_recommended_interval(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        months_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niFgen_GetExtCalRecommendedInterval_cfunc is None:
                self.niFgen_GetExtCalRecommendedInterval_cfunc = self._get_library_function('niFgen_GetExtCalRecommendedInterval')
                self.niFgen_GetExtCalRecommendedInterval_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_GetExtCalRecommendedInterval_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_GetExtCalRecommendedInterval_cfunc(vi_ctype, None if months_ctype is None else (ctypes.pointer(months_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return _converters.convert_month_to_timedelta(int(months_ctype.value))

    def get_hardware_state(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        state_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niFgen_GetHardwareState_cfunc is None:
                self.niFgen_GetHardwareState_cfunc = self._get_library_function('niFgen_GetHardwareState')
                self.niFgen_GetHardwareState_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_GetHardwareState_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_GetHardwareState_cfunc(vi_ctype, None if state_ctype is None else (ctypes.pointer(state_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return enums.HardwareState(state_ctype.value)

    def _get_self_cal_last_date_and_time(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        year_ctype = _visatype.ViInt32()  # case S220
        month_ctype = _visatype.ViInt32()  # case S220
        day_ctype = _visatype.ViInt32()  # case S220
        hour_ctype = _visatype.ViInt32()  # case S220
        minute_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niFgen_GetSelfCalLastDateAndTime_cfunc is None:
                self.niFgen_GetSelfCalLastDateAndTime_cfunc = self._get_library_function('niFgen_GetSelfCalLastDateAndTime')
                self.niFgen_GetSelfCalLastDateAndTime_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_GetSelfCalLastDateAndTime_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_GetSelfCalLastDateAndTime_cfunc(vi_ctype, None if year_ctype is None else (ctypes.pointer(year_ctype)), None if month_ctype is None else (ctypes.pointer(month_ctype)), None if day_ctype is None else (ctypes.pointer(day_ctype)), None if hour_ctype is None else (ctypes.pointer(hour_ctype)), None if minute_ctype is None else (ctypes.pointer(minute_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(year_ctype.value), int(month_ctype.value), int(day_ctype.value), int(hour_ctype.value), int(minute_ctype.value)

    def get_self_cal_last_temp(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        temperature_ctype = _visatype.ViReal64()  # case S220
        with self._func_lock:
            if self.niFgen_GetSelfCalLastTemp_cfunc is None:
                self.niFgen_GetSelfCalLastTemp_cfunc = self._get_library_function('niFgen_GetSelfCalLastTemp')
                self.niFgen_GetSelfCalLastTemp_cfunc.argtypes = [ViSession, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFgen_GetSelfCalLastTemp_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_GetSelfCalLastTemp_cfunc(vi_ctype, None if temperature_ctype is None else (ctypes.pointer(temperature_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

    def get_self_cal_supported(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        self_cal_supported_ctype = _visatype.ViBoolean()  # case S220
        with self._func_lock:
            if self.niFgen_GetSelfCalSupported_cfunc is None:
                self.niFgen_GetSelfCalSupported_cfunc = self._get_library_function('niFgen_GetSelfCalSupported')
                self.niFgen_GetSelfCalSupported_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niFgen_GetSelfCalSupported_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_GetSelfCalSupported_cfunc(vi_ctype, None if self_cal_supported_ctype is None else (ctypes.pointer(self_cal_supported_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(self_cal_supported_ctype.value)

    def import_attribute_configuration_buffer(self, session, configuration):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        size_in_bytes_ctype = _visatype.ViInt32(0 if configuration is None else len(configuration))  # case S160
        configuration_converted = _converters.convert_to_bytes(configuration)  # case B520
        configuration_ctype = get_ctypes_pointer_for_buffer(value=configuration_converted, library_type=_visatype.ViInt8)  # case B520
        with self._func_lock:
            if self.niFgen_ImportAttributeConfigurationBuffer_cfunc is None:
                self.niFgen_ImportAttributeConfigurationBuffer_cfunc = self._get_library_function('niFgen_ImportAttributeConfigurationBuffer')
                self.niFgen_ImportAttributeConfigurationBuffer_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt8)]  # noqa: F405
                self.niFgen_ImportAttributeConfigurationBuffer_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_ImportAttributeConfigurationBuffer_cfunc(vi_ctype, size_in_bytes_ctype, configuration_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def import_attribute_configuration_file(self, session, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(session._encoding))  # case C020
        with self._func_lock:
            if self.niFgen_ImportAttributeConfigurationFile_cfunc is None:
                self.niFgen_ImportAttributeConfigurationFile_cfunc = self._get_library_function('niFgen_ImportAttributeConfigurationFile')
                self.niFgen_ImportAttributeConfigurationFile_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_ImportAttributeConfigurationFile_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_ImportAttributeConfigurationFile_cfunc(vi_ctype, file_path_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _initialize_with_channels(self, session, resource_name, channel_name=None, reset_device=False, option_string=""):  # noqa: N802
        resource_name_ctype = ctypes.create_string_buffer(resource_name.encode(session._encoding))  # case C020
        channel_name_ctype = ctypes.create_string_buffer(_converters.convert_repeated_capabilities_without_prefix(channel_name).encode(session._encoding))  # case C040
        reset_device_ctype = _visatype.ViBoolean(reset_device)  # case S150
        option_string_ctype = ctypes.create_string_buffer(_converters.convert_init_with_options_dictionary(option_string).encode(session._encoding))  # case C040
        vi_ctype = _visatype.ViSession()  # case S220
        with self._func_lock:
            if self.niFgen_InitializeWithChannels_cfunc is None:
                self.niFgen_InitializeWithChannels_cfunc = self._get_library_function('niFgen_InitializeWithChannels')
                self.niFgen_InitializeWithChannels_cfunc.argtypes = [ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViBoolean, ctypes.POINTER(ViChar), ctypes.POINTER(ViSession)]  # noqa: F405
                self.niFgen_InitializeWithChannels_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_InitializeWithChannels_cfunc(resource_name_ctype, channel_name_ctype, reset_device_ctype, option_string_ctype, None if vi_ctype is None else (ctypes.pointer(vi_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(vi_ctype.value)

    def _initiate_generation(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niFgen_InitiateGeneration_cfunc is None:
                self.niFgen_InitiateGeneration_cfunc = self._get_library_function('niFgen_InitiateGeneration')
                self.niFgen_InitiateGeneration_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFgen_InitiateGeneration_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_InitiateGeneration_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def is_done(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        done_ctype = _visatype.ViBoolean()  # case S220
        with self._func_lock:
            if self.niFgen_IsDone_cfunc is None:
                self.niFgen_IsDone_cfunc = self._get_library_function('niFgen_IsDone')
                self.niFgen_IsDone_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niFgen_IsDone_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_IsDone_cfunc(vi_ctype, None if done_ctype is None else (ctypes.pointer(done_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(done_ctype.value)

    def lock(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        caller_has_lock_ctype = _visatype.ViBoolean()  # case S220
        with self._func_lock:
            if self.niFgen_LockSession_cfunc is None:
                self.niFgen_LockSession_cfunc = self._get_library_function('niFgen_LockSession')
                self.niFgen_LockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niFgen_LockSession_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_LockSession_cfunc(vi_ctype, None if caller_has_lock_ctype is None else (ctypes.pointer(caller_has_lock_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(caller_has_lock_ctype.value)

    def query_arb_seq_capabilities(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        maximum_number_of_sequences_ctype = _visatype.ViInt32()  # case S220
        minimum_sequence_length_ctype = _visatype.ViInt32()  # case S220
        maximum_sequence_length_ctype = _visatype.ViInt32()  # case S220
        maximum_loop_count_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niFgen_QueryArbSeqCapabilities_cfunc is None:
                self.niFgen_QueryArbSeqCapabilities_cfunc = self._get_library_function('niFgen_QueryArbSeqCapabilities')
                self.niFgen_QueryArbSeqCapabilities_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_QueryArbSeqCapabilities_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_QueryArbSeqCapabilities_cfunc(vi_ctype, None if maximum_number_of_sequences_ctype is None else (ctypes.pointer(maximum_number_of_sequences_ctype)), None if minimum_sequence_length_ctype is None else (ctypes.pointer(minimum_sequence_length_ctype)), None if maximum_sequence_length_ctype is None else (ctypes.pointer(maximum_sequence_length_ctype)), None if maximum_loop_count_ctype is None else (ctypes.pointer(maximum_loop_count_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(maximum_number_of_sequences_ctype.value), int(minimum_sequence_length_ctype.value), int(maximum_sequence_length_ctype.value), int(maximum_loop_count_ctype.value)

    def query_arb_wfm_capabilities(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        maximum_number_of_waveforms_ctype = _visatype.ViInt32()  # case S220
        waveform_quantum_ctype = _visatype.ViInt32()  # case S220
        minimum_waveform_size_ctype = _visatype.ViInt32()  # case S220
        maximum_waveform_size_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niFgen_QueryArbWfmCapabilities_cfunc is None:
                self.niFgen_QueryArbWfmCapabilities_cfunc = self._get_library_function('niFgen_QueryArbWfmCapabilities')
                self.niFgen_QueryArbWfmCapabilities_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_QueryArbWfmCapabilities_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_QueryArbWfmCapabilities_cfunc(vi_ctype, None if maximum_number_of_waveforms_ctype is None else (ctypes.pointer(maximum_number_of_waveforms_ctype)), None if waveform_quantum_ctype is None else (ctypes.pointer(waveform_quantum_ctype)), None if minimum_waveform_size_ctype is None else (ctypes.pointer(minimum_waveform_size_ctype)), None if maximum_waveform_size_ctype is None else (ctypes.pointer(maximum_waveform_size_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(maximum_number_of_waveforms_ctype.value), int(waveform_quantum_ctype.value), int(minimum_waveform_size_ctype.value), int(maximum_waveform_size_ctype.value)

    def query_freq_list_capabilities(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        maximum_number_of_freq_lists_ctype = _visatype.ViInt32()  # case S220
        minimum_frequency_list_length_ctype = _visatype.ViInt32()  # case S220
        maximum_frequency_list_length_ctype = _visatype.ViInt32()  # case S220
        minimum_frequency_list_duration_ctype = _visatype.ViReal64()  # case S220
        maximum_frequency_list_duration_ctype = _visatype.ViReal64()  # case S220
        frequency_list_duration_quantum_ctype = _visatype.ViReal64()  # case S220
        with self._func_lock:
            if self.niFgen_QueryFreqListCapabilities_cfunc is None:
                self.niFgen_QueryFreqListCapabilities_cfunc = self._get_library_function('niFgen_QueryFreqListCapabilities')
                self.niFgen_QueryFreqListCapabilities_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFgen_QueryFreqListCapabilities_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_QueryFreqListCapabilities_cfunc(vi_ctype, None if maximum_number_of_freq_lists_ctype is None else (ctypes.pointer(maximum_number_of_freq_lists_ctype)), None if minimum_frequency_list_length_ctype is None else (ctypes.pointer(minimum_frequency_list_length_ctype)), None if maximum_frequency_list_length_ctype is None else (ctypes.pointer(maximum_frequency_list_length_ctype)), None if minimum_frequency_list_duration_ctype is None else (ctypes.pointer(minimum_frequency_list_duration_ctype)), None if maximum_frequency_list_duration_ctype is None else (ctypes.pointer(maximum_frequency_list_duration_ctype)), None if frequency_list_duration_quantum_ctype is None else (ctypes.pointer(frequency_list_duration_quantum_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(maximum_number_of_freq_lists_ctype.value), int(minimum_frequency_list_length_ctype.value), int(maximum_frequency_list_length_ctype.value), float(minimum_frequency_list_duration_ctype.value), float(maximum_frequency_list_duration_ctype.value), float(frequency_list_duration_quantum_ctype.value)

    def read_current_temperature(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        temperature_ctype = _visatype.ViReal64()  # case S220
        with self._func_lock:
            if self.niFgen_ReadCurrentTemperature_cfunc is None:
                self.niFgen_ReadCurrentTemperature_cfunc = self._get_library_function('niFgen_ReadCurrentTemperature')
                self.niFgen_ReadCurrentTemperature_cfunc.argtypes = [ViSession, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFgen_ReadCurrentTemperature_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_ReadCurrentTemperature_cfunc(vi_ctype, None if temperature_ctype is None else (ctypes.pointer(temperature_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

    def reset_device(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niFgen_ResetDevice_cfunc is None:
                self.niFgen_ResetDevice_cfunc = self._get_library_function('niFgen_ResetDevice')
                self.niFgen_ResetDevice_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFgen_ResetDevice_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_ResetDevice_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def reset_with_defaults(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niFgen_ResetWithDefaults_cfunc is None:
                self.niFgen_ResetWithDefaults_cfunc = self._get_library_function('niFgen_ResetWithDefaults')
                self.niFgen_ResetWithDefaults_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFgen_ResetWithDefaults_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_ResetWithDefaults_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def self_cal(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niFgen_SelfCal_cfunc is None:
                self.niFgen_SelfCal_cfunc = self._get_library_function('niFgen_SelfCal')
                self.niFgen_SelfCal_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFgen_SelfCal_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_SelfCal_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def send_software_edge_trigger(self, session, trigger, trigger_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        trigger_ctype = _visatype.ViInt32(trigger.value)  # case S130
        trigger_id_ctype = ctypes.create_string_buffer(trigger_id.encode(session._encoding))  # case C020
        with self._func_lock:
            if self.niFgen_SendSoftwareEdgeTrigger_cfunc is None:
                self.niFgen_SendSoftwareEdgeTrigger_cfunc = self._get_library_function('niFgen_SendSoftwareEdgeTrigger')
                self.niFgen_SendSoftwareEdgeTrigger_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_SendSoftwareEdgeTrigger_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_SendSoftwareEdgeTrigger_cfunc(vi_ctype, trigger_ctype, trigger_id_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_boolean(self, session, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViBoolean(attribute_value)  # case S150
        with self._func_lock:
            if self.niFgen_SetAttributeViBoolean_cfunc is None:
                self.niFgen_SetAttributeViBoolean_cfunc = self._get_library_function('niFgen_SetAttributeViBoolean')
                self.niFgen_SetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViBoolean]  # noqa: F405
                self.niFgen_SetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_SetAttributeViBoolean_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_int32(self, session, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt32(attribute_value)  # case S150
        with self._func_lock:
            if self.niFgen_SetAttributeViInt32_cfunc is None:
                self.niFgen_SetAttributeViInt32_cfunc = self._get_library_function('niFgen_SetAttributeViInt32')
                self.niFgen_SetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32]  # noqa: F405
                self.niFgen_SetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_SetAttributeViInt32_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_real64(self, session, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViReal64(attribute_value)  # case S150
        with self._func_lock:
            if self.niFgen_SetAttributeViReal64_cfunc is None:
                self.niFgen_SetAttributeViReal64_cfunc = self._get_library_function('niFgen_SetAttributeViReal64')
                self.niFgen_SetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViReal64]  # noqa: F405
                self.niFgen_SetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_SetAttributeViReal64_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_string(self, session, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = ctypes.create_string_buffer(attribute_value.encode(session._encoding))  # case C020
        with self._func_lock:
            if self.niFgen_SetAttributeViString_cfunc is None:
                self.niFgen_SetAttributeViString_cfunc = self._get_library_function('niFgen_SetAttributeViString')
                self.niFgen_SetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_SetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_SetAttributeViString_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_named_waveform_next_write_position(self, session, channel_name, waveform_name, relative_to, offset):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(session._encoding))  # case C020
        relative_to_ctype = _visatype.ViInt32(relative_to.value)  # case S130
        offset_ctype = _visatype.ViInt32(offset)  # case S150
        with self._func_lock:
            if self.niFgen_SetNamedWaveformNextWritePosition_cfunc is None:
                self.niFgen_SetNamedWaveformNextWritePosition_cfunc = self._get_library_function('niFgen_SetNamedWaveformNextWritePosition')
                self.niFgen_SetNamedWaveformNextWritePosition_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ViInt32]  # noqa: F405
                self.niFgen_SetNamedWaveformNextWritePosition_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_SetNamedWaveformNextWritePosition_cfunc(vi_ctype, channel_name_ctype, waveform_name_ctype, relative_to_ctype, offset_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_waveform_next_write_position(self, session, channel_name, waveform_handle, relative_to, offset):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        waveform_handle_ctype = _visatype.ViInt32(waveform_handle)  # case S150
        relative_to_ctype = _visatype.ViInt32(relative_to.value)  # case S130
        offset_ctype = _visatype.ViInt32(offset)  # case S150
        with self._func_lock:
            if self.niFgen_SetWaveformNextWritePosition_cfunc is None:
                self.niFgen_SetWaveformNextWritePosition_cfunc = self._get_library_function('niFgen_SetWaveformNextWritePosition')
                self.niFgen_SetWaveformNextWritePosition_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViInt32, ViInt32]  # noqa: F405
                self.niFgen_SetWaveformNextWritePosition_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_SetWaveformNextWritePosition_cfunc(vi_ctype, channel_name_ctype, waveform_handle_ctype, relative_to_ctype, offset_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def unlock(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        caller_has_lock_ctype = _visatype.ViBoolean()  # case S220
        with self._func_lock:
            if self.niFgen_UnlockSession_cfunc is None:
                self.niFgen_UnlockSession_cfunc = self._get_library_function('niFgen_UnlockSession')
                self.niFgen_UnlockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niFgen_UnlockSession_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_UnlockSession_cfunc(vi_ctype, None if caller_has_lock_ctype is None else (ctypes.pointer(caller_has_lock_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(caller_has_lock_ctype.value)

    def wait_until_done(self, session, max_time=hightime.timedelta(seconds=10.0)):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        max_time_ctype = _converters.convert_timedelta_to_milliseconds_int32(max_time)  # case S140
        with self._func_lock:
            if self.niFgen_WaitUntilDone_cfunc is None:
                self.niFgen_WaitUntilDone_cfunc = self._get_library_function('niFgen_WaitUntilDone')
                self.niFgen_WaitUntilDone_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niFgen_WaitUntilDone_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_WaitUntilDone_cfunc(vi_ctype, max_time_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _write_binary16_waveform_numpy(self, session, channel_name, waveform_handle, data):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        waveform_handle_ctype = _visatype.ViInt32(waveform_handle)  # case S150
        size_ctype = _visatype.ViInt32(0 if data is None else len(data))  # case S160
        data_ctype = get_ctypes_pointer_for_buffer(value=data)  # case B510
        with self._func_lock:
            if self.niFgen_WriteBinary16Waveform_cfunc is None:
                self.niFgen_WriteBinary16Waveform_cfunc = self._get_library_function('niFgen_WriteBinary16Waveform')
                self.niFgen_WriteBinary16Waveform_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViInt32, ctypes.POINTER(ViInt16)]  # noqa: F405
                self.niFgen_WriteBinary16Waveform_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_WriteBinary16Waveform_cfunc(vi_ctype, channel_name_ctype, waveform_handle_ctype, size_ctype, data_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _write_named_waveform_f64(self, session, channel_name, waveform_name, data):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(session._encoding))  # case C020
        size_ctype = _visatype.ViInt32(0 if data is None else len(data))  # case S160
        data_array = get_ctypes_and_array(value=data, array_type="d")  # case B550
        data_ctype = get_ctypes_pointer_for_buffer(value=data_array, library_type=_visatype.ViReal64)  # case B550
        with self._func_lock:
            if self.niFgen_WriteNamedWaveformF64_cfunc is None:
                self.niFgen_WriteNamedWaveformF64_cfunc = self._get_library_function('niFgen_WriteNamedWaveformF64')
                self.niFgen_WriteNamedWaveformF64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFgen_WriteNamedWaveformF64_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_WriteNamedWaveformF64_cfunc(vi_ctype, channel_name_ctype, waveform_name_ctype, size_ctype, data_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _write_named_waveform_f64_numpy(self, session, channel_name, waveform_name, data):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(session._encoding))  # case C020
        size_ctype = _visatype.ViInt32(0 if data is None else len(data))  # case S160
        data_ctype = get_ctypes_pointer_for_buffer(value=data)  # case B510
        with self._func_lock:
            if self.niFgen_WriteNamedWaveformF64_cfunc is None:
                self.niFgen_WriteNamedWaveformF64_cfunc = self._get_library_function('niFgen_WriteNamedWaveformF64')
                self.niFgen_WriteNamedWaveformF64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFgen_WriteNamedWaveformF64_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_WriteNamedWaveformF64_cfunc(vi_ctype, channel_name_ctype, waveform_name_ctype, size_ctype, data_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _write_named_waveform_i16_numpy(self, session, channel_name, waveform_name, data):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(session._encoding))  # case C020
        size_ctype = _visatype.ViInt32(0 if data is None else len(data))  # case S160
        data_ctype = get_ctypes_pointer_for_buffer(value=data)  # case B510
        with self._func_lock:
            if self.niFgen_WriteNamedWaveformI16_cfunc is None:
                self.niFgen_WriteNamedWaveformI16_cfunc = self._get_library_function('niFgen_WriteNamedWaveformI16')
                self.niFgen_WriteNamedWaveformI16_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt16)]  # noqa: F405
                self.niFgen_WriteNamedWaveformI16_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_WriteNamedWaveformI16_cfunc(vi_ctype, channel_name_ctype, waveform_name_ctype, size_ctype, data_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def write_script(self, session, channel_name, script):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        script_ctype = ctypes.create_string_buffer(script.encode(session._encoding))  # case C020
        with self._func_lock:
            if self.niFgen_WriteScript_cfunc is None:
                self.niFgen_WriteScript_cfunc = self._get_library_function('niFgen_WriteScript')
                self.niFgen_WriteScript_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_WriteScript_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_WriteScript_cfunc(vi_ctype, channel_name_ctype, script_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _write_waveform(self, session, channel_name, waveform_handle, data):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        waveform_handle_ctype = _visatype.ViInt32(waveform_handle)  # case S150
        size_ctype = _visatype.ViInt32(0 if data is None else len(data))  # case S160
        data_array = get_ctypes_and_array(value=data, array_type="d")  # case B550
        data_ctype = get_ctypes_pointer_for_buffer(value=data_array, library_type=_visatype.ViReal64)  # case B550
        with self._func_lock:
            if self.niFgen_WriteWaveform_cfunc is None:
                self.niFgen_WriteWaveform_cfunc = self._get_library_function('niFgen_WriteWaveform')
                self.niFgen_WriteWaveform_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFgen_WriteWaveform_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_WriteWaveform_cfunc(vi_ctype, channel_name_ctype, waveform_handle_ctype, size_ctype, data_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _write_waveform_numpy(self, session, channel_name, waveform_handle, data):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        waveform_handle_ctype = _visatype.ViInt32(waveform_handle)  # case S150
        size_ctype = _visatype.ViInt32(0 if data is None else len(data))  # case S160
        data_ctype = get_ctypes_pointer_for_buffer(value=data)  # case B510
        with self._func_lock:
            if self.niFgen_WriteWaveform_cfunc is None:
                self.niFgen_WriteWaveform_cfunc = self._get_library_function('niFgen_WriteWaveform')
                self.niFgen_WriteWaveform_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFgen_WriteWaveform_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_WriteWaveform_cfunc(vi_ctype, channel_name_ctype, waveform_handle_ctype, size_ctype, data_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _close(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niFgen_close_cfunc is None:
                self.niFgen_close_cfunc = self._get_library_function('niFgen_close')
                self.niFgen_close_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFgen_close_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_close_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _error_message(self, session, error_code):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        error_code_ctype = _visatype.ViStatus(error_code)  # case S150
        error_message_ctype = (_visatype.ViChar * 256)()  # case C070
        with self._func_lock:
            if self.niFgen_error_message_cfunc is None:
                self.niFgen_error_message_cfunc = self._get_library_function('niFgen_error_message')
                self.niFgen_error_message_cfunc.argtypes = [ViSession, ViStatus, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_error_message_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_error_message_cfunc(vi_ctype, error_code_ctype, error_message_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=True)
        return error_message_ctype.value.decode(session._encoding)

    def reset(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niFgen_reset_cfunc is None:
                self.niFgen_reset_cfunc = self._get_library_function('niFgen_reset')
                self.niFgen_reset_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFgen_reset_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_reset_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _self_test(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        self_test_result_ctype = _visatype.ViInt16()  # case S220
        self_test_message_ctype = (_visatype.ViChar * 256)()  # case C070
        with self._func_lock:
            if self.niFgen_self_test_cfunc is None:
                self.niFgen_self_test_cfunc = self._get_library_function('niFgen_self_test')
                self.niFgen_self_test_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt16), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_self_test_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niFgen_self_test_cfunc(vi_ctype, None if self_test_result_ctype is None else (ctypes.pointer(self_test_result_ctype)), self_test_message_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(self_test_result_ctype.value), self_test_message_ctype.value.decode(session._encoding)
