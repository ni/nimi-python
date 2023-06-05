# -*- coding: utf-8 -*-
# This file was generated

import ctypes
import nidigital.errors as errors
import threading

from nidigital._visatype import *  # noqa: F403,H303

import nidigital.history_ram_cycle_information as history_ram_cycle_information  # noqa: F401


class Library(object):
    '''Library

    Wrapper around driver library.
    Class will setup the correct ctypes information for every function on first call.
    '''

    def __init__(self, ctypes_library):
        self._func_lock = threading.Lock()
        self._library = ctypes_library
        # We cache the cfunc object from the ctypes.CDLL object
        self.niDigital_Abort_cfunc = None
        self.niDigital_AbortKeepAlive_cfunc = None
        self.niDigital_ApplyLevelsAndTiming_cfunc = None
        self.niDigital_ApplyTDROffsets_cfunc = None
        self.niDigital_BurstPattern_cfunc = None
        self.niDigital_ClockGenerator_Abort_cfunc = None
        self.niDigital_ClockGenerator_GenerateClock_cfunc = None
        self.niDigital_Commit_cfunc = None
        self.niDigital_ConfigureActiveLoadLevels_cfunc = None
        self.niDigital_ConfigurePatternBurstSites_cfunc = None
        self.niDigital_ConfigureTimeSetCompareEdgesStrobe_cfunc = None
        self.niDigital_ConfigureTimeSetCompareEdgesStrobe2x_cfunc = None
        self.niDigital_ConfigureTimeSetDriveEdges_cfunc = None
        self.niDigital_ConfigureTimeSetDriveEdges2x_cfunc = None
        self.niDigital_ConfigureTimeSetDriveFormat_cfunc = None
        self.niDigital_ConfigureTimeSetEdge_cfunc = None
        self.niDigital_ConfigureTimeSetEdgeMultiplier_cfunc = None
        self.niDigital_ConfigureTimeSetPeriod_cfunc = None
        self.niDigital_ConfigureVoltageLevels_cfunc = None
        self.niDigital_CreateCaptureWaveformFromFileDigicapture_cfunc = None
        self.niDigital_CreateCaptureWaveformParallel_cfunc = None
        self.niDigital_CreateCaptureWaveformSerial_cfunc = None
        self.niDigital_CreateSourceWaveformFromFileTDMS_cfunc = None
        self.niDigital_CreateSourceWaveformParallel_cfunc = None
        self.niDigital_CreateSourceWaveformSerial_cfunc = None
        self.niDigital_CreateTimeSet_cfunc = None
        self.niDigital_DeleteAllTimeSets_cfunc = None
        self.niDigital_DisableSites_cfunc = None
        self.niDigital_EnableSites_cfunc = None
        self.niDigital_FetchCaptureWaveformU32_cfunc = None
        self.niDigital_FetchHistoryRAMCycleInformation_cfunc = None
        self.niDigital_FetchHistoryRAMCyclePinData_cfunc = None
        self.niDigital_FetchHistoryRAMScanCycleNumber_cfunc = None
        self.niDigital_FrequencyCounter_MeasureFrequency_cfunc = None
        self.niDigital_GetAttributeViBoolean_cfunc = None
        self.niDigital_GetAttributeViInt32_cfunc = None
        self.niDigital_GetAttributeViInt64_cfunc = None
        self.niDigital_GetAttributeViReal64_cfunc = None
        self.niDigital_GetAttributeViString_cfunc = None
        self.niDigital_GetChannelNameFromString_cfunc = None
        self.niDigital_GetError_cfunc = None
        self.niDigital_GetFailCount_cfunc = None
        self.niDigital_GetHistoryRAMSampleCount_cfunc = None
        self.niDigital_GetPatternName_cfunc = None
        self.niDigital_GetPatternPinList_cfunc = None
        self.niDigital_GetPinName_cfunc = None
        self.niDigital_GetPinResultsPinInformation_cfunc = None
        self.niDigital_GetSitePassFail_cfunc = None
        self.niDigital_GetSiteResultsSiteNumbers_cfunc = None
        self.niDigital_GetTimeSetDriveFormat_cfunc = None
        self.niDigital_GetTimeSetEdge_cfunc = None
        self.niDigital_GetTimeSetEdgeMultiplier_cfunc = None
        self.niDigital_GetTimeSetName_cfunc = None
        self.niDigital_GetTimeSetPeriod_cfunc = None
        self.niDigital_InitWithOptions_cfunc = None
        self.niDigital_Initiate_cfunc = None
        self.niDigital_IsDone_cfunc = None
        self.niDigital_IsSiteEnabled_cfunc = None
        self.niDigital_LoadLevels_cfunc = None
        self.niDigital_LoadPattern_cfunc = None
        self.niDigital_LoadPinMap_cfunc = None
        self.niDigital_LoadSpecifications_cfunc = None
        self.niDigital_LoadTiming_cfunc = None
        self.niDigital_LockSession_cfunc = None
        self.niDigital_PPMU_Measure_cfunc = None
        self.niDigital_PPMU_Source_cfunc = None
        self.niDigital_ReadSequencerFlag_cfunc = None
        self.niDigital_ReadSequencerRegister_cfunc = None
        self.niDigital_ReadStatic_cfunc = None
        self.niDigital_ResetDevice_cfunc = None
        self.niDigital_SelfCalibrate_cfunc = None
        self.niDigital_SendSoftwareEdgeTrigger_cfunc = None
        self.niDigital_SetAttributeViBoolean_cfunc = None
        self.niDigital_SetAttributeViInt32_cfunc = None
        self.niDigital_SetAttributeViInt64_cfunc = None
        self.niDigital_SetAttributeViReal64_cfunc = None
        self.niDigital_SetAttributeViString_cfunc = None
        self.niDigital_SetRuntimeEnvironment_cfunc = None
        self.niDigital_TDR_cfunc = None
        self.niDigital_UnloadAllPatterns_cfunc = None
        self.niDigital_UnloadSpecifications_cfunc = None
        self.niDigital_UnlockSession_cfunc = None
        self.niDigital_WaitUntilDone_cfunc = None
        self.niDigital_WriteSequencerFlag_cfunc = None
        self.niDigital_WriteSequencerRegister_cfunc = None
        self.niDigital_WriteSourceWaveformBroadcastU32_cfunc = None
        self.niDigital_WriteSourceWaveformDataFromFileTDMS_cfunc = None
        self.niDigital_WriteSourceWaveformSiteUniqueU32_cfunc = None
        self.niDigital_WriteStatic_cfunc = None
        self.niDigital_close_cfunc = None
        self.niDigital_error_message_cfunc = None
        self.niDigital_reset_cfunc = None
        self.niDigital_self_test_cfunc = None

    def _get_library_function(self, name):
        try:
            function = getattr(self._library, name)
        except AttributeError as e:
            raise errors.DriverTooOldError() from e
        return function

    def niDigital_Abort(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDigital_Abort_cfunc is None:
                self.niDigital_Abort_cfunc = self._get_library_function('niDigital_Abort')
                self.niDigital_Abort_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDigital_Abort_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_Abort_cfunc(vi)

    def niDigital_AbortKeepAlive(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDigital_AbortKeepAlive_cfunc is None:
                self.niDigital_AbortKeepAlive_cfunc = self._get_library_function('niDigital_AbortKeepAlive')
                self.niDigital_AbortKeepAlive_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDigital_AbortKeepAlive_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_AbortKeepAlive_cfunc(vi)

    def niDigital_ApplyLevelsAndTiming(self, vi, site_list, levels_sheet, timing_sheet, initial_state_high_pins, initial_state_low_pins, initial_state_tristate_pins):  # noqa: N802
        with self._func_lock:
            if self.niDigital_ApplyLevelsAndTiming_cfunc is None:
                self.niDigital_ApplyLevelsAndTiming_cfunc = self._get_library_function('niDigital_ApplyLevelsAndTiming')
                self.niDigital_ApplyLevelsAndTiming_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_ApplyLevelsAndTiming_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_ApplyLevelsAndTiming_cfunc(vi, site_list, levels_sheet, timing_sheet, initial_state_high_pins, initial_state_low_pins, initial_state_tristate_pins)

    def niDigital_ApplyTDROffsets(self, vi, channel_list, num_offsets, offsets):  # noqa: N802
        with self._func_lock:
            if self.niDigital_ApplyTDROffsets_cfunc is None:
                self.niDigital_ApplyTDROffsets_cfunc = self._get_library_function('niDigital_ApplyTDROffsets')
                self.niDigital_ApplyTDROffsets_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDigital_ApplyTDROffsets_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_ApplyTDROffsets_cfunc(vi, channel_list, num_offsets, offsets)

    def niDigital_BurstPattern(self, vi, site_list, start_label, select_digital_function, wait_until_done, timeout):  # noqa: N802
        with self._func_lock:
            if self.niDigital_BurstPattern_cfunc is None:
                self.niDigital_BurstPattern_cfunc = self._get_library_function('niDigital_BurstPattern')
                self.niDigital_BurstPattern_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViBoolean, ViBoolean, ViReal64]  # noqa: F405
                self.niDigital_BurstPattern_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_BurstPattern_cfunc(vi, site_list, start_label, select_digital_function, wait_until_done, timeout)

    def niDigital_ClockGenerator_Abort(self, vi, channel_list):  # noqa: N802
        with self._func_lock:
            if self.niDigital_ClockGenerator_Abort_cfunc is None:
                self.niDigital_ClockGenerator_Abort_cfunc = self._get_library_function('niDigital_ClockGenerator_Abort')
                self.niDigital_ClockGenerator_Abort_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_ClockGenerator_Abort_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_ClockGenerator_Abort_cfunc(vi, channel_list)

    def niDigital_ClockGenerator_GenerateClock(self, vi, channel_list, frequency, select_digital_function):  # noqa: N802
        with self._func_lock:
            if self.niDigital_ClockGenerator_GenerateClock_cfunc is None:
                self.niDigital_ClockGenerator_GenerateClock_cfunc = self._get_library_function('niDigital_ClockGenerator_GenerateClock')
                self.niDigital_ClockGenerator_GenerateClock_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViBoolean]  # noqa: F405
                self.niDigital_ClockGenerator_GenerateClock_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_ClockGenerator_GenerateClock_cfunc(vi, channel_list, frequency, select_digital_function)

    def niDigital_Commit(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDigital_Commit_cfunc is None:
                self.niDigital_Commit_cfunc = self._get_library_function('niDigital_Commit')
                self.niDigital_Commit_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDigital_Commit_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_Commit_cfunc(vi)

    def niDigital_ConfigureActiveLoadLevels(self, vi, channel_list, iol, ioh, vcom):  # noqa: N802
        with self._func_lock:
            if self.niDigital_ConfigureActiveLoadLevels_cfunc is None:
                self.niDigital_ConfigureActiveLoadLevels_cfunc = self._get_library_function('niDigital_ConfigureActiveLoadLevels')
                self.niDigital_ConfigureActiveLoadLevels_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViReal64, ViReal64]  # noqa: F405
                self.niDigital_ConfigureActiveLoadLevels_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_ConfigureActiveLoadLevels_cfunc(vi, channel_list, iol, ioh, vcom)

    def niDigital_ConfigurePatternBurstSites(self, vi, site_list):  # noqa: N802
        with self._func_lock:
            if self.niDigital_ConfigurePatternBurstSites_cfunc is None:
                self.niDigital_ConfigurePatternBurstSites_cfunc = self._get_library_function('niDigital_ConfigurePatternBurstSites')
                self.niDigital_ConfigurePatternBurstSites_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_ConfigurePatternBurstSites_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_ConfigurePatternBurstSites_cfunc(vi, site_list)

    def niDigital_ConfigureTimeSetCompareEdgesStrobe(self, vi, pin_list, time_set_name, strobe_edge):  # noqa: N802
        with self._func_lock:
            if self.niDigital_ConfigureTimeSetCompareEdgesStrobe_cfunc is None:
                self.niDigital_ConfigureTimeSetCompareEdgesStrobe_cfunc = self._get_library_function('niDigital_ConfigureTimeSetCompareEdgesStrobe')
                self.niDigital_ConfigureTimeSetCompareEdgesStrobe_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViReal64]  # noqa: F405
                self.niDigital_ConfigureTimeSetCompareEdgesStrobe_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_ConfigureTimeSetCompareEdgesStrobe_cfunc(vi, pin_list, time_set_name, strobe_edge)

    def niDigital_ConfigureTimeSetCompareEdgesStrobe2x(self, vi, pin_list, time_set_name, strobe_edge, strobe2_edge):  # noqa: N802
        with self._func_lock:
            if self.niDigital_ConfigureTimeSetCompareEdgesStrobe2x_cfunc is None:
                self.niDigital_ConfigureTimeSetCompareEdgesStrobe2x_cfunc = self._get_library_function('niDigital_ConfigureTimeSetCompareEdgesStrobe2x')
                self.niDigital_ConfigureTimeSetCompareEdgesStrobe2x_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViReal64, ViReal64]  # noqa: F405
                self.niDigital_ConfigureTimeSetCompareEdgesStrobe2x_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_ConfigureTimeSetCompareEdgesStrobe2x_cfunc(vi, pin_list, time_set_name, strobe_edge, strobe2_edge)

    def niDigital_ConfigureTimeSetDriveEdges(self, vi, pin_list, time_set_name, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge):  # noqa: N802
        with self._func_lock:
            if self.niDigital_ConfigureTimeSetDriveEdges_cfunc is None:
                self.niDigital_ConfigureTimeSetDriveEdges_cfunc = self._get_library_function('niDigital_ConfigureTimeSetDriveEdges')
                self.niDigital_ConfigureTimeSetDriveEdges_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ViReal64, ViReal64, ViReal64, ViReal64]  # noqa: F405
                self.niDigital_ConfigureTimeSetDriveEdges_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_ConfigureTimeSetDriveEdges_cfunc(vi, pin_list, time_set_name, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge)

    def niDigital_ConfigureTimeSetDriveEdges2x(self, vi, pin_list, time_set_name, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge, drive_data2_edge, drive_return2_edge):  # noqa: N802
        with self._func_lock:
            if self.niDigital_ConfigureTimeSetDriveEdges2x_cfunc is None:
                self.niDigital_ConfigureTimeSetDriveEdges2x_cfunc = self._get_library_function('niDigital_ConfigureTimeSetDriveEdges2x')
                self.niDigital_ConfigureTimeSetDriveEdges2x_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ViReal64, ViReal64, ViReal64, ViReal64, ViReal64, ViReal64]  # noqa: F405
                self.niDigital_ConfigureTimeSetDriveEdges2x_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_ConfigureTimeSetDriveEdges2x_cfunc(vi, pin_list, time_set_name, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge, drive_data2_edge, drive_return2_edge)

    def niDigital_ConfigureTimeSetDriveFormat(self, vi, pin_list, time_set_name, drive_format):  # noqa: N802
        with self._func_lock:
            if self.niDigital_ConfigureTimeSetDriveFormat_cfunc is None:
                self.niDigital_ConfigureTimeSetDriveFormat_cfunc = self._get_library_function('niDigital_ConfigureTimeSetDriveFormat')
                self.niDigital_ConfigureTimeSetDriveFormat_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niDigital_ConfigureTimeSetDriveFormat_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_ConfigureTimeSetDriveFormat_cfunc(vi, pin_list, time_set_name, drive_format)

    def niDigital_ConfigureTimeSetEdge(self, vi, pin_list, time_set_name, edge, time):  # noqa: N802
        with self._func_lock:
            if self.niDigital_ConfigureTimeSetEdge_cfunc is None:
                self.niDigital_ConfigureTimeSetEdge_cfunc = self._get_library_function('niDigital_ConfigureTimeSetEdge')
                self.niDigital_ConfigureTimeSetEdge_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ViReal64]  # noqa: F405
                self.niDigital_ConfigureTimeSetEdge_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_ConfigureTimeSetEdge_cfunc(vi, pin_list, time_set_name, edge, time)

    def niDigital_ConfigureTimeSetEdgeMultiplier(self, vi, pin_list, time_set_name, edge_multiplier):  # noqa: N802
        with self._func_lock:
            if self.niDigital_ConfigureTimeSetEdgeMultiplier_cfunc is None:
                self.niDigital_ConfigureTimeSetEdgeMultiplier_cfunc = self._get_library_function('niDigital_ConfigureTimeSetEdgeMultiplier')
                self.niDigital_ConfigureTimeSetEdgeMultiplier_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niDigital_ConfigureTimeSetEdgeMultiplier_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_ConfigureTimeSetEdgeMultiplier_cfunc(vi, pin_list, time_set_name, edge_multiplier)

    def niDigital_ConfigureTimeSetPeriod(self, vi, time_set_name, period):  # noqa: N802
        with self._func_lock:
            if self.niDigital_ConfigureTimeSetPeriod_cfunc is None:
                self.niDigital_ConfigureTimeSetPeriod_cfunc = self._get_library_function('niDigital_ConfigureTimeSetPeriod')
                self.niDigital_ConfigureTimeSetPeriod_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64]  # noqa: F405
                self.niDigital_ConfigureTimeSetPeriod_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_ConfigureTimeSetPeriod_cfunc(vi, time_set_name, period)

    def niDigital_ConfigureVoltageLevels(self, vi, channel_list, vil, vih, vol, voh, vterm):  # noqa: N802
        with self._func_lock:
            if self.niDigital_ConfigureVoltageLevels_cfunc is None:
                self.niDigital_ConfigureVoltageLevels_cfunc = self._get_library_function('niDigital_ConfigureVoltageLevels')
                self.niDigital_ConfigureVoltageLevels_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViReal64, ViReal64, ViReal64, ViReal64]  # noqa: F405
                self.niDigital_ConfigureVoltageLevels_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_ConfigureVoltageLevels_cfunc(vi, channel_list, vil, vih, vol, voh, vterm)

    def niDigital_CreateCaptureWaveformFromFileDigicapture(self, vi, waveform_name, waveform_file_path):  # noqa: N802
        with self._func_lock:
            if self.niDigital_CreateCaptureWaveformFromFileDigicapture_cfunc is None:
                self.niDigital_CreateCaptureWaveformFromFileDigicapture_cfunc = self._get_library_function('niDigital_CreateCaptureWaveformFromFileDigicapture')
                self.niDigital_CreateCaptureWaveformFromFileDigicapture_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_CreateCaptureWaveformFromFileDigicapture_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_CreateCaptureWaveformFromFileDigicapture_cfunc(vi, waveform_name, waveform_file_path)

    def niDigital_CreateCaptureWaveformParallel(self, vi, pin_list, waveform_name):  # noqa: N802
        with self._func_lock:
            if self.niDigital_CreateCaptureWaveformParallel_cfunc is None:
                self.niDigital_CreateCaptureWaveformParallel_cfunc = self._get_library_function('niDigital_CreateCaptureWaveformParallel')
                self.niDigital_CreateCaptureWaveformParallel_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_CreateCaptureWaveformParallel_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_CreateCaptureWaveformParallel_cfunc(vi, pin_list, waveform_name)

    def niDigital_CreateCaptureWaveformSerial(self, vi, pin_list, waveform_name, sample_width, bit_order):  # noqa: N802
        with self._func_lock:
            if self.niDigital_CreateCaptureWaveformSerial_cfunc is None:
                self.niDigital_CreateCaptureWaveformSerial_cfunc = self._get_library_function('niDigital_CreateCaptureWaveformSerial')
                self.niDigital_CreateCaptureWaveformSerial_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViUInt32, ViInt32]  # noqa: F405
                self.niDigital_CreateCaptureWaveformSerial_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_CreateCaptureWaveformSerial_cfunc(vi, pin_list, waveform_name, sample_width, bit_order)

    def niDigital_CreateSourceWaveformFromFileTDMS(self, vi, waveform_name, waveform_file_path, write_waveform_data):  # noqa: N802
        with self._func_lock:
            if self.niDigital_CreateSourceWaveformFromFileTDMS_cfunc is None:
                self.niDigital_CreateSourceWaveformFromFileTDMS_cfunc = self._get_library_function('niDigital_CreateSourceWaveformFromFileTDMS')
                self.niDigital_CreateSourceWaveformFromFileTDMS_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViBoolean]  # noqa: F405
                self.niDigital_CreateSourceWaveformFromFileTDMS_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_CreateSourceWaveformFromFileTDMS_cfunc(vi, waveform_name, waveform_file_path, write_waveform_data)

    def niDigital_CreateSourceWaveformParallel(self, vi, pin_list, waveform_name, data_mapping):  # noqa: N802
        with self._func_lock:
            if self.niDigital_CreateSourceWaveformParallel_cfunc is None:
                self.niDigital_CreateSourceWaveformParallel_cfunc = self._get_library_function('niDigital_CreateSourceWaveformParallel')
                self.niDigital_CreateSourceWaveformParallel_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niDigital_CreateSourceWaveformParallel_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_CreateSourceWaveformParallel_cfunc(vi, pin_list, waveform_name, data_mapping)

    def niDigital_CreateSourceWaveformSerial(self, vi, pin_list, waveform_name, data_mapping, sample_width, bit_order):  # noqa: N802
        with self._func_lock:
            if self.niDigital_CreateSourceWaveformSerial_cfunc is None:
                self.niDigital_CreateSourceWaveformSerial_cfunc = self._get_library_function('niDigital_CreateSourceWaveformSerial')
                self.niDigital_CreateSourceWaveformSerial_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ViUInt32, ViInt32]  # noqa: F405
                self.niDigital_CreateSourceWaveformSerial_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_CreateSourceWaveformSerial_cfunc(vi, pin_list, waveform_name, data_mapping, sample_width, bit_order)

    def niDigital_CreateTimeSet(self, vi, name):  # noqa: N802
        with self._func_lock:
            if self.niDigital_CreateTimeSet_cfunc is None:
                self.niDigital_CreateTimeSet_cfunc = self._get_library_function('niDigital_CreateTimeSet')
                self.niDigital_CreateTimeSet_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_CreateTimeSet_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_CreateTimeSet_cfunc(vi, name)

    def niDigital_DeleteAllTimeSets(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDigital_DeleteAllTimeSets_cfunc is None:
                self.niDigital_DeleteAllTimeSets_cfunc = self._get_library_function('niDigital_DeleteAllTimeSets')
                self.niDigital_DeleteAllTimeSets_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDigital_DeleteAllTimeSets_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_DeleteAllTimeSets_cfunc(vi)

    def niDigital_DisableSites(self, vi, site_list):  # noqa: N802
        with self._func_lock:
            if self.niDigital_DisableSites_cfunc is None:
                self.niDigital_DisableSites_cfunc = self._get_library_function('niDigital_DisableSites')
                self.niDigital_DisableSites_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_DisableSites_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_DisableSites_cfunc(vi, site_list)

    def niDigital_EnableSites(self, vi, site_list):  # noqa: N802
        with self._func_lock:
            if self.niDigital_EnableSites_cfunc is None:
                self.niDigital_EnableSites_cfunc = self._get_library_function('niDigital_EnableSites')
                self.niDigital_EnableSites_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_EnableSites_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_EnableSites_cfunc(vi, site_list)

    def niDigital_FetchCaptureWaveformU32(self, vi, site_list, waveform_name, samples_to_read, timeout, data_buffer_size, data, actual_num_waveforms, actual_samples_per_waveform):  # noqa: N802
        with self._func_lock:
            if self.niDigital_FetchCaptureWaveformU32_cfunc is None:
                self.niDigital_FetchCaptureWaveformU32_cfunc = self._get_library_function('niDigital_FetchCaptureWaveformU32')
                self.niDigital_FetchCaptureWaveformU32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ViReal64, ViInt32, ctypes.POINTER(ViUInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDigital_FetchCaptureWaveformU32_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_FetchCaptureWaveformU32_cfunc(vi, site_list, waveform_name, samples_to_read, timeout, data_buffer_size, data, actual_num_waveforms, actual_samples_per_waveform)

    def niDigital_FetchHistoryRAMCycleInformation(self, vi, site, sample_index, pattern_index, time_set_index, vector_number, cycle_number, num_dut_cycles):  # noqa: N802
        with self._func_lock:
            if self.niDigital_FetchHistoryRAMCycleInformation_cfunc is None:
                self.niDigital_FetchHistoryRAMCycleInformation_cfunc = self._get_library_function('niDigital_FetchHistoryRAMCycleInformation')
                self.niDigital_FetchHistoryRAMCycleInformation_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt64, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt64), ctypes.POINTER(ViInt64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDigital_FetchHistoryRAMCycleInformation_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_FetchHistoryRAMCycleInformation_cfunc(vi, site, sample_index, pattern_index, time_set_index, vector_number, cycle_number, num_dut_cycles)

    def niDigital_FetchHistoryRAMCyclePinData(self, vi, site, pin_list, sample_index, dut_cycle_index, pin_data_buffer_size, expected_pin_states, actual_pin_states, per_pin_pass_fail, actual_num_pin_data):  # noqa: N802
        with self._func_lock:
            if self.niDigital_FetchHistoryRAMCyclePinData_cfunc is None:
                self.niDigital_FetchHistoryRAMCyclePinData_cfunc = self._get_library_function('niDigital_FetchHistoryRAMCyclePinData')
                self.niDigital_FetchHistoryRAMCyclePinData_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt64, ViInt32, ViInt32, ctypes.POINTER(ViUInt8), ctypes.POINTER(ViUInt8), ctypes.POINTER(ViBoolean), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDigital_FetchHistoryRAMCyclePinData_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_FetchHistoryRAMCyclePinData_cfunc(vi, site, pin_list, sample_index, dut_cycle_index, pin_data_buffer_size, expected_pin_states, actual_pin_states, per_pin_pass_fail, actual_num_pin_data)

    def niDigital_FetchHistoryRAMScanCycleNumber(self, vi, site, sample_index, scan_cycle_number):  # noqa: N802
        with self._func_lock:
            if self.niDigital_FetchHistoryRAMScanCycleNumber_cfunc is None:
                self.niDigital_FetchHistoryRAMScanCycleNumber_cfunc = self._get_library_function('niDigital_FetchHistoryRAMScanCycleNumber')
                self.niDigital_FetchHistoryRAMScanCycleNumber_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt64, ctypes.POINTER(ViInt64)]  # noqa: F405
                self.niDigital_FetchHistoryRAMScanCycleNumber_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_FetchHistoryRAMScanCycleNumber_cfunc(vi, site, sample_index, scan_cycle_number)

    def niDigital_FrequencyCounter_MeasureFrequency(self, vi, channel_list, frequencies_buffer_size, frequencies, actual_num_frequencies):  # noqa: N802
        with self._func_lock:
            if self.niDigital_FrequencyCounter_MeasureFrequency_cfunc is None:
                self.niDigital_FrequencyCounter_MeasureFrequency_cfunc = self._get_library_function('niDigital_FrequencyCounter_MeasureFrequency')
                self.niDigital_FrequencyCounter_MeasureFrequency_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDigital_FrequencyCounter_MeasureFrequency_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_FrequencyCounter_MeasureFrequency_cfunc(vi, channel_list, frequencies_buffer_size, frequencies, actual_num_frequencies)

    def niDigital_GetAttributeViBoolean(self, vi, channel_name, attribute, value):  # noqa: N802
        with self._func_lock:
            if self.niDigital_GetAttributeViBoolean_cfunc is None:
                self.niDigital_GetAttributeViBoolean_cfunc = self._get_library_function('niDigital_GetAttributeViBoolean')
                self.niDigital_GetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niDigital_GetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_GetAttributeViBoolean_cfunc(vi, channel_name, attribute, value)

    def niDigital_GetAttributeViInt32(self, vi, channel_name, attribute, value):  # noqa: N802
        with self._func_lock:
            if self.niDigital_GetAttributeViInt32_cfunc is None:
                self.niDigital_GetAttributeViInt32_cfunc = self._get_library_function('niDigital_GetAttributeViInt32')
                self.niDigital_GetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDigital_GetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_GetAttributeViInt32_cfunc(vi, channel_name, attribute, value)

    def niDigital_GetAttributeViInt64(self, vi, channel_name, attribute, value):  # noqa: N802
        with self._func_lock:
            if self.niDigital_GetAttributeViInt64_cfunc is None:
                self.niDigital_GetAttributeViInt64_cfunc = self._get_library_function('niDigital_GetAttributeViInt64')
                self.niDigital_GetAttributeViInt64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViInt64)]  # noqa: F405
                self.niDigital_GetAttributeViInt64_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_GetAttributeViInt64_cfunc(vi, channel_name, attribute, value)

    def niDigital_GetAttributeViReal64(self, vi, channel_name, attribute, value):  # noqa: N802
        with self._func_lock:
            if self.niDigital_GetAttributeViReal64_cfunc is None:
                self.niDigital_GetAttributeViReal64_cfunc = self._get_library_function('niDigital_GetAttributeViReal64')
                self.niDigital_GetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDigital_GetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_GetAttributeViReal64_cfunc(vi, channel_name, attribute, value)

    def niDigital_GetAttributeViString(self, vi, channel_name, attribute, buffer_size, value):  # noqa: N802
        with self._func_lock:
            if self.niDigital_GetAttributeViString_cfunc is None:
                self.niDigital_GetAttributeViString_cfunc = self._get_library_function('niDigital_GetAttributeViString')
                self.niDigital_GetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_GetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_GetAttributeViString_cfunc(vi, channel_name, attribute, buffer_size, value)

    def niDigital_GetChannelNameFromString(self, vi, indices, name_buffer_size, names):  # noqa: N802
        with self._func_lock:
            if self.niDigital_GetChannelNameFromString_cfunc is None:
                self.niDigital_GetChannelNameFromString_cfunc = self._get_library_function('niDigital_GetChannelNameFromString')
                self.niDigital_GetChannelNameFromString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_GetChannelNameFromString_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_GetChannelNameFromString_cfunc(vi, indices, name_buffer_size, names)

    def niDigital_GetError(self, vi, error_code, error_description_buffer_size, error_description):  # noqa: N802
        with self._func_lock:
            if self.niDigital_GetError_cfunc is None:
                self.niDigital_GetError_cfunc = self._get_library_function('niDigital_GetError')
                self.niDigital_GetError_cfunc.argtypes = [ViSession, ctypes.POINTER(ViStatus), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_GetError_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_GetError_cfunc(vi, error_code, error_description_buffer_size, error_description)

    def niDigital_GetFailCount(self, vi, channel_list, buffer_size, failure_count, actual_num_read):  # noqa: N802
        with self._func_lock:
            if self.niDigital_GetFailCount_cfunc is None:
                self.niDigital_GetFailCount_cfunc = self._get_library_function('niDigital_GetFailCount')
                self.niDigital_GetFailCount_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDigital_GetFailCount_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_GetFailCount_cfunc(vi, channel_list, buffer_size, failure_count, actual_num_read)

    def niDigital_GetHistoryRAMSampleCount(self, vi, site, sample_count):  # noqa: N802
        with self._func_lock:
            if self.niDigital_GetHistoryRAMSampleCount_cfunc is None:
                self.niDigital_GetHistoryRAMSampleCount_cfunc = self._get_library_function('niDigital_GetHistoryRAMSampleCount')
                self.niDigital_GetHistoryRAMSampleCount_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViInt64)]  # noqa: F405
                self.niDigital_GetHistoryRAMSampleCount_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_GetHistoryRAMSampleCount_cfunc(vi, site, sample_count)

    def niDigital_GetPatternName(self, vi, pattern_index, name_buffer_size, name):  # noqa: N802
        with self._func_lock:
            if self.niDigital_GetPatternName_cfunc is None:
                self.niDigital_GetPatternName_cfunc = self._get_library_function('niDigital_GetPatternName')
                self.niDigital_GetPatternName_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_GetPatternName_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_GetPatternName_cfunc(vi, pattern_index, name_buffer_size, name)

    def niDigital_GetPatternPinList(self, vi, start_label, pin_list_buffer_size, pin_list):  # noqa: N802
        with self._func_lock:
            if self.niDigital_GetPatternPinList_cfunc is None:
                self.niDigital_GetPatternPinList_cfunc = self._get_library_function('niDigital_GetPatternPinList')
                self.niDigital_GetPatternPinList_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_GetPatternPinList_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_GetPatternPinList_cfunc(vi, start_label, pin_list_buffer_size, pin_list)

    def niDigital_GetPinName(self, vi, pin_index, name_buffer_size, name):  # noqa: N802
        with self._func_lock:
            if self.niDigital_GetPinName_cfunc is None:
                self.niDigital_GetPinName_cfunc = self._get_library_function('niDigital_GetPinName')
                self.niDigital_GetPinName_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_GetPinName_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_GetPinName_cfunc(vi, pin_index, name_buffer_size, name)

    def niDigital_GetPinResultsPinInformation(self, vi, channel_list, buffer_size, pin_indexes, site_numbers, channel_indexes, actual_num_values):  # noqa: N802
        with self._func_lock:
            if self.niDigital_GetPinResultsPinInformation_cfunc is None:
                self.niDigital_GetPinResultsPinInformation_cfunc = self._get_library_function('niDigital_GetPinResultsPinInformation')
                self.niDigital_GetPinResultsPinInformation_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDigital_GetPinResultsPinInformation_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_GetPinResultsPinInformation_cfunc(vi, channel_list, buffer_size, pin_indexes, site_numbers, channel_indexes, actual_num_values)

    def niDigital_GetSitePassFail(self, vi, site_list, pass_fail_buffer_size, pass_fail, actual_num_sites):  # noqa: N802
        with self._func_lock:
            if self.niDigital_GetSitePassFail_cfunc is None:
                self.niDigital_GetSitePassFail_cfunc = self._get_library_function('niDigital_GetSitePassFail')
                self.niDigital_GetSitePassFail_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViBoolean), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDigital_GetSitePassFail_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_GetSitePassFail_cfunc(vi, site_list, pass_fail_buffer_size, pass_fail, actual_num_sites)

    def niDigital_GetSiteResultsSiteNumbers(self, vi, site_list, site_result_type, site_numbers_buffer_size, site_numbers, actual_num_site_numbers):  # noqa: N802
        with self._func_lock:
            if self.niDigital_GetSiteResultsSiteNumbers_cfunc is None:
                self.niDigital_GetSiteResultsSiteNumbers_cfunc = self._get_library_function('niDigital_GetSiteResultsSiteNumbers')
                self.niDigital_GetSiteResultsSiteNumbers_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViInt32, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDigital_GetSiteResultsSiteNumbers_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_GetSiteResultsSiteNumbers_cfunc(vi, site_list, site_result_type, site_numbers_buffer_size, site_numbers, actual_num_site_numbers)

    def niDigital_GetTimeSetDriveFormat(self, vi, pin, time_set_name, format):  # noqa: N802
        with self._func_lock:
            if self.niDigital_GetTimeSetDriveFormat_cfunc is None:
                self.niDigital_GetTimeSetDriveFormat_cfunc = self._get_library_function('niDigital_GetTimeSetDriveFormat')
                self.niDigital_GetTimeSetDriveFormat_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDigital_GetTimeSetDriveFormat_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_GetTimeSetDriveFormat_cfunc(vi, pin, time_set_name, format)

    def niDigital_GetTimeSetEdge(self, vi, pin, time_set_name, edge, time):  # noqa: N802
        with self._func_lock:
            if self.niDigital_GetTimeSetEdge_cfunc is None:
                self.niDigital_GetTimeSetEdge_cfunc = self._get_library_function('niDigital_GetTimeSetEdge')
                self.niDigital_GetTimeSetEdge_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDigital_GetTimeSetEdge_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_GetTimeSetEdge_cfunc(vi, pin, time_set_name, edge, time)

    def niDigital_GetTimeSetEdgeMultiplier(self, vi, pin, time_set_name, edge_multiplier):  # noqa: N802
        with self._func_lock:
            if self.niDigital_GetTimeSetEdgeMultiplier_cfunc is None:
                self.niDigital_GetTimeSetEdgeMultiplier_cfunc = self._get_library_function('niDigital_GetTimeSetEdgeMultiplier')
                self.niDigital_GetTimeSetEdgeMultiplier_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDigital_GetTimeSetEdgeMultiplier_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_GetTimeSetEdgeMultiplier_cfunc(vi, pin, time_set_name, edge_multiplier)

    def niDigital_GetTimeSetName(self, vi, time_set_index, name_buffer_size, name):  # noqa: N802
        with self._func_lock:
            if self.niDigital_GetTimeSetName_cfunc is None:
                self.niDigital_GetTimeSetName_cfunc = self._get_library_function('niDigital_GetTimeSetName')
                self.niDigital_GetTimeSetName_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_GetTimeSetName_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_GetTimeSetName_cfunc(vi, time_set_index, name_buffer_size, name)

    def niDigital_GetTimeSetPeriod(self, vi, time_set_name, period):  # noqa: N802
        with self._func_lock:
            if self.niDigital_GetTimeSetPeriod_cfunc is None:
                self.niDigital_GetTimeSetPeriod_cfunc = self._get_library_function('niDigital_GetTimeSetPeriod')
                self.niDigital_GetTimeSetPeriod_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDigital_GetTimeSetPeriod_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_GetTimeSetPeriod_cfunc(vi, time_set_name, period)

    def niDigital_InitWithOptions(self, resource_name, id_query, reset_device, option_string, new_vi):  # noqa: N802
        with self._func_lock:
            if self.niDigital_InitWithOptions_cfunc is None:
                self.niDigital_InitWithOptions_cfunc = self._get_library_function('niDigital_InitWithOptions')
                self.niDigital_InitWithOptions_cfunc.argtypes = [ctypes.POINTER(ViChar), ViBoolean, ViBoolean, ctypes.POINTER(ViChar), ctypes.POINTER(ViSession)]  # noqa: F405
                self.niDigital_InitWithOptions_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_InitWithOptions_cfunc(resource_name, id_query, reset_device, option_string, new_vi)

    def niDigital_Initiate(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDigital_Initiate_cfunc is None:
                self.niDigital_Initiate_cfunc = self._get_library_function('niDigital_Initiate')
                self.niDigital_Initiate_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDigital_Initiate_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_Initiate_cfunc(vi)

    def niDigital_IsDone(self, vi, done):  # noqa: N802
        with self._func_lock:
            if self.niDigital_IsDone_cfunc is None:
                self.niDigital_IsDone_cfunc = self._get_library_function('niDigital_IsDone')
                self.niDigital_IsDone_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niDigital_IsDone_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_IsDone_cfunc(vi, done)

    def niDigital_IsSiteEnabled(self, vi, site, enable):  # noqa: N802
        with self._func_lock:
            if self.niDigital_IsSiteEnabled_cfunc is None:
                self.niDigital_IsSiteEnabled_cfunc = self._get_library_function('niDigital_IsSiteEnabled')
                self.niDigital_IsSiteEnabled_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niDigital_IsSiteEnabled_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_IsSiteEnabled_cfunc(vi, site, enable)

    def niDigital_LoadLevels(self, vi, file_path):  # noqa: N802
        with self._func_lock:
            if self.niDigital_LoadLevels_cfunc is None:
                self.niDigital_LoadLevels_cfunc = self._get_library_function('niDigital_LoadLevels')
                self.niDigital_LoadLevels_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_LoadLevels_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_LoadLevels_cfunc(vi, file_path)

    def niDigital_LoadPattern(self, vi, file_path):  # noqa: N802
        with self._func_lock:
            if self.niDigital_LoadPattern_cfunc is None:
                self.niDigital_LoadPattern_cfunc = self._get_library_function('niDigital_LoadPattern')
                self.niDigital_LoadPattern_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_LoadPattern_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_LoadPattern_cfunc(vi, file_path)

    def niDigital_LoadPinMap(self, vi, file_path):  # noqa: N802
        with self._func_lock:
            if self.niDigital_LoadPinMap_cfunc is None:
                self.niDigital_LoadPinMap_cfunc = self._get_library_function('niDigital_LoadPinMap')
                self.niDigital_LoadPinMap_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_LoadPinMap_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_LoadPinMap_cfunc(vi, file_path)

    def niDigital_LoadSpecifications(self, vi, file_path):  # noqa: N802
        with self._func_lock:
            if self.niDigital_LoadSpecifications_cfunc is None:
                self.niDigital_LoadSpecifications_cfunc = self._get_library_function('niDigital_LoadSpecifications')
                self.niDigital_LoadSpecifications_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_LoadSpecifications_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_LoadSpecifications_cfunc(vi, file_path)

    def niDigital_LoadTiming(self, vi, file_path):  # noqa: N802
        with self._func_lock:
            if self.niDigital_LoadTiming_cfunc is None:
                self.niDigital_LoadTiming_cfunc = self._get_library_function('niDigital_LoadTiming')
                self.niDigital_LoadTiming_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_LoadTiming_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_LoadTiming_cfunc(vi, file_path)

    def niDigital_LockSession(self, vi, caller_has_lock):  # noqa: N802
        with self._func_lock:
            if self.niDigital_LockSession_cfunc is None:
                self.niDigital_LockSession_cfunc = self._get_library_function('niDigital_LockSession')
                self.niDigital_LockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niDigital_LockSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_LockSession_cfunc(vi, caller_has_lock)

    def niDigital_PPMU_Measure(self, vi, channel_list, measurement_type, buffer_size, measurements, actual_num_read):  # noqa: N802
        with self._func_lock:
            if self.niDigital_PPMU_Measure_cfunc is None:
                self.niDigital_PPMU_Measure_cfunc = self._get_library_function('niDigital_PPMU_Measure')
                self.niDigital_PPMU_Measure_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDigital_PPMU_Measure_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_PPMU_Measure_cfunc(vi, channel_list, measurement_type, buffer_size, measurements, actual_num_read)

    def niDigital_PPMU_Source(self, vi, channel_list):  # noqa: N802
        with self._func_lock:
            if self.niDigital_PPMU_Source_cfunc is None:
                self.niDigital_PPMU_Source_cfunc = self._get_library_function('niDigital_PPMU_Source')
                self.niDigital_PPMU_Source_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_PPMU_Source_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_PPMU_Source_cfunc(vi, channel_list)

    def niDigital_ReadSequencerFlag(self, vi, flag, value):  # noqa: N802
        with self._func_lock:
            if self.niDigital_ReadSequencerFlag_cfunc is None:
                self.niDigital_ReadSequencerFlag_cfunc = self._get_library_function('niDigital_ReadSequencerFlag')
                self.niDigital_ReadSequencerFlag_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niDigital_ReadSequencerFlag_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_ReadSequencerFlag_cfunc(vi, flag, value)

    def niDigital_ReadSequencerRegister(self, vi, reg, value):  # noqa: N802
        with self._func_lock:
            if self.niDigital_ReadSequencerRegister_cfunc is None:
                self.niDigital_ReadSequencerRegister_cfunc = self._get_library_function('niDigital_ReadSequencerRegister')
                self.niDigital_ReadSequencerRegister_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDigital_ReadSequencerRegister_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_ReadSequencerRegister_cfunc(vi, reg, value)

    def niDigital_ReadStatic(self, vi, channel_list, buffer_size, data, actual_num_read):  # noqa: N802
        with self._func_lock:
            if self.niDigital_ReadStatic_cfunc is None:
                self.niDigital_ReadStatic_cfunc = self._get_library_function('niDigital_ReadStatic')
                self.niDigital_ReadStatic_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViUInt8), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDigital_ReadStatic_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_ReadStatic_cfunc(vi, channel_list, buffer_size, data, actual_num_read)

    def niDigital_ResetDevice(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDigital_ResetDevice_cfunc is None:
                self.niDigital_ResetDevice_cfunc = self._get_library_function('niDigital_ResetDevice')
                self.niDigital_ResetDevice_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDigital_ResetDevice_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_ResetDevice_cfunc(vi)

    def niDigital_SelfCalibrate(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDigital_SelfCalibrate_cfunc is None:
                self.niDigital_SelfCalibrate_cfunc = self._get_library_function('niDigital_SelfCalibrate')
                self.niDigital_SelfCalibrate_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDigital_SelfCalibrate_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_SelfCalibrate_cfunc(vi)

    def niDigital_SendSoftwareEdgeTrigger(self, vi, trigger, trigger_identifier):  # noqa: N802
        with self._func_lock:
            if self.niDigital_SendSoftwareEdgeTrigger_cfunc is None:
                self.niDigital_SendSoftwareEdgeTrigger_cfunc = self._get_library_function('niDigital_SendSoftwareEdgeTrigger')
                self.niDigital_SendSoftwareEdgeTrigger_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_SendSoftwareEdgeTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_SendSoftwareEdgeTrigger_cfunc(vi, trigger, trigger_identifier)

    def niDigital_SetAttributeViBoolean(self, vi, channel_name, attribute, value):  # noqa: N802
        with self._func_lock:
            if self.niDigital_SetAttributeViBoolean_cfunc is None:
                self.niDigital_SetAttributeViBoolean_cfunc = self._get_library_function('niDigital_SetAttributeViBoolean')
                self.niDigital_SetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViBoolean]  # noqa: F405
                self.niDigital_SetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_SetAttributeViBoolean_cfunc(vi, channel_name, attribute, value)

    def niDigital_SetAttributeViInt32(self, vi, channel_name, attribute, value):  # noqa: N802
        with self._func_lock:
            if self.niDigital_SetAttributeViInt32_cfunc is None:
                self.niDigital_SetAttributeViInt32_cfunc = self._get_library_function('niDigital_SetAttributeViInt32')
                self.niDigital_SetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32]  # noqa: F405
                self.niDigital_SetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_SetAttributeViInt32_cfunc(vi, channel_name, attribute, value)

    def niDigital_SetAttributeViInt64(self, vi, channel_name, attribute, value):  # noqa: N802
        with self._func_lock:
            if self.niDigital_SetAttributeViInt64_cfunc is None:
                self.niDigital_SetAttributeViInt64_cfunc = self._get_library_function('niDigital_SetAttributeViInt64')
                self.niDigital_SetAttributeViInt64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt64]  # noqa: F405
                self.niDigital_SetAttributeViInt64_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_SetAttributeViInt64_cfunc(vi, channel_name, attribute, value)

    def niDigital_SetAttributeViReal64(self, vi, channel_name, attribute, value):  # noqa: N802
        with self._func_lock:
            if self.niDigital_SetAttributeViReal64_cfunc is None:
                self.niDigital_SetAttributeViReal64_cfunc = self._get_library_function('niDigital_SetAttributeViReal64')
                self.niDigital_SetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViReal64]  # noqa: F405
                self.niDigital_SetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_SetAttributeViReal64_cfunc(vi, channel_name, attribute, value)

    def niDigital_SetAttributeViString(self, vi, channel_name, attribute, value):  # noqa: N802
        with self._func_lock:
            if self.niDigital_SetAttributeViString_cfunc is None:
                self.niDigital_SetAttributeViString_cfunc = self._get_library_function('niDigital_SetAttributeViString')
                self.niDigital_SetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_SetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_SetAttributeViString_cfunc(vi, channel_name, attribute, value)

    def niDigital_SetRuntimeEnvironment(self, environment, environment_version, reserved1, reserved2):  # noqa: N802
        with self._func_lock:
            if self.niDigital_SetRuntimeEnvironment_cfunc is None:
                self.niDigital_SetRuntimeEnvironment_cfunc = self._get_library_function('niDigital_SetRuntimeEnvironment')
                self.niDigital_SetRuntimeEnvironment_cfunc.argtypes = [ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_SetRuntimeEnvironment_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_SetRuntimeEnvironment_cfunc(environment, environment_version, reserved1, reserved2)

    def niDigital_TDR(self, vi, channel_list, apply_offsets, offsets_buffer_size, offsets, actual_num_offsets):  # noqa: N802
        with self._func_lock:
            if self.niDigital_TDR_cfunc is None:
                self.niDigital_TDR_cfunc = self._get_library_function('niDigital_TDR')
                self.niDigital_TDR_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViBoolean, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDigital_TDR_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_TDR_cfunc(vi, channel_list, apply_offsets, offsets_buffer_size, offsets, actual_num_offsets)

    def niDigital_UnloadAllPatterns(self, vi, unload_keep_alive_pattern):  # noqa: N802
        with self._func_lock:
            if self.niDigital_UnloadAllPatterns_cfunc is None:
                self.niDigital_UnloadAllPatterns_cfunc = self._get_library_function('niDigital_UnloadAllPatterns')
                self.niDigital_UnloadAllPatterns_cfunc.argtypes = [ViSession, ViBoolean]  # noqa: F405
                self.niDigital_UnloadAllPatterns_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_UnloadAllPatterns_cfunc(vi, unload_keep_alive_pattern)

    def niDigital_UnloadSpecifications(self, vi, file_path):  # noqa: N802
        with self._func_lock:
            if self.niDigital_UnloadSpecifications_cfunc is None:
                self.niDigital_UnloadSpecifications_cfunc = self._get_library_function('niDigital_UnloadSpecifications')
                self.niDigital_UnloadSpecifications_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_UnloadSpecifications_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_UnloadSpecifications_cfunc(vi, file_path)

    def niDigital_UnlockSession(self, vi, caller_has_lock):  # noqa: N802
        with self._func_lock:
            if self.niDigital_UnlockSession_cfunc is None:
                self.niDigital_UnlockSession_cfunc = self._get_library_function('niDigital_UnlockSession')
                self.niDigital_UnlockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niDigital_UnlockSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_UnlockSession_cfunc(vi, caller_has_lock)

    def niDigital_WaitUntilDone(self, vi, timeout):  # noqa: N802
        with self._func_lock:
            if self.niDigital_WaitUntilDone_cfunc is None:
                self.niDigital_WaitUntilDone_cfunc = self._get_library_function('niDigital_WaitUntilDone')
                self.niDigital_WaitUntilDone_cfunc.argtypes = [ViSession, ViReal64]  # noqa: F405
                self.niDigital_WaitUntilDone_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_WaitUntilDone_cfunc(vi, timeout)

    def niDigital_WriteSequencerFlag(self, vi, flag, value):  # noqa: N802
        with self._func_lock:
            if self.niDigital_WriteSequencerFlag_cfunc is None:
                self.niDigital_WriteSequencerFlag_cfunc = self._get_library_function('niDigital_WriteSequencerFlag')
                self.niDigital_WriteSequencerFlag_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViBoolean]  # noqa: F405
                self.niDigital_WriteSequencerFlag_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_WriteSequencerFlag_cfunc(vi, flag, value)

    def niDigital_WriteSequencerRegister(self, vi, reg, value):  # noqa: N802
        with self._func_lock:
            if self.niDigital_WriteSequencerRegister_cfunc is None:
                self.niDigital_WriteSequencerRegister_cfunc = self._get_library_function('niDigital_WriteSequencerRegister')
                self.niDigital_WriteSequencerRegister_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niDigital_WriteSequencerRegister_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_WriteSequencerRegister_cfunc(vi, reg, value)

    def niDigital_WriteSourceWaveformBroadcastU32(self, vi, waveform_name, waveform_size, waveform_data):  # noqa: N802
        with self._func_lock:
            if self.niDigital_WriteSourceWaveformBroadcastU32_cfunc is None:
                self.niDigital_WriteSourceWaveformBroadcastU32_cfunc = self._get_library_function('niDigital_WriteSourceWaveformBroadcastU32')
                self.niDigital_WriteSourceWaveformBroadcastU32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViUInt32)]  # noqa: F405
                self.niDigital_WriteSourceWaveformBroadcastU32_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_WriteSourceWaveformBroadcastU32_cfunc(vi, waveform_name, waveform_size, waveform_data)

    def niDigital_WriteSourceWaveformDataFromFileTDMS(self, vi, waveform_name, waveform_file_path):  # noqa: N802
        with self._func_lock:
            if self.niDigital_WriteSourceWaveformDataFromFileTDMS_cfunc is None:
                self.niDigital_WriteSourceWaveformDataFromFileTDMS_cfunc = self._get_library_function('niDigital_WriteSourceWaveformDataFromFileTDMS')
                self.niDigital_WriteSourceWaveformDataFromFileTDMS_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_WriteSourceWaveformDataFromFileTDMS_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_WriteSourceWaveformDataFromFileTDMS_cfunc(vi, waveform_name, waveform_file_path)

    def niDigital_WriteSourceWaveformSiteUniqueU32(self, vi, site_list, waveform_name, num_waveforms, samples_per_waveform, waveform_data):  # noqa: N802
        with self._func_lock:
            if self.niDigital_WriteSourceWaveformSiteUniqueU32_cfunc is None:
                self.niDigital_WriteSourceWaveformSiteUniqueU32_cfunc = self._get_library_function('niDigital_WriteSourceWaveformSiteUniqueU32')
                self.niDigital_WriteSourceWaveformSiteUniqueU32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ViInt32, ctypes.POINTER(ViUInt32)]  # noqa: F405
                self.niDigital_WriteSourceWaveformSiteUniqueU32_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_WriteSourceWaveformSiteUniqueU32_cfunc(vi, site_list, waveform_name, num_waveforms, samples_per_waveform, waveform_data)

    def niDigital_WriteStatic(self, vi, channel_list, state):  # noqa: N802
        with self._func_lock:
            if self.niDigital_WriteStatic_cfunc is None:
                self.niDigital_WriteStatic_cfunc = self._get_library_function('niDigital_WriteStatic')
                self.niDigital_WriteStatic_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViUInt8]  # noqa: F405
                self.niDigital_WriteStatic_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_WriteStatic_cfunc(vi, channel_list, state)

    def niDigital_close(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDigital_close_cfunc is None:
                self.niDigital_close_cfunc = self._get_library_function('niDigital_close')
                self.niDigital_close_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDigital_close_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_close_cfunc(vi)

    def niDigital_error_message(self, vi, error_code, error_message):  # noqa: N802
        with self._func_lock:
            if self.niDigital_error_message_cfunc is None:
                self.niDigital_error_message_cfunc = self._get_library_function('niDigital_error_message')
                self.niDigital_error_message_cfunc.argtypes = [ViSession, ViStatus, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_error_message_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_error_message_cfunc(vi, error_code, error_message)

    def niDigital_reset(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDigital_reset_cfunc is None:
                self.niDigital_reset_cfunc = self._get_library_function('niDigital_reset')
                self.niDigital_reset_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDigital_reset_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_reset_cfunc(vi)

    def niDigital_self_test(self, vi, test_result, test_message):  # noqa: N802
        with self._func_lock:
            if self.niDigital_self_test_cfunc is None:
                self.niDigital_self_test_cfunc = self._get_library_function('niDigital_self_test')
                self.niDigital_self_test_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt16), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_self_test_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_self_test_cfunc(vi, test_result, test_message)
