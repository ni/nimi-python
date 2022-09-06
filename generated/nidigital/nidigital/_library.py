# -*- coding: utf-8 -*-
# This file was generated

import array  # noqa: F401
import ctypes
import hightime
import nidigital._converters as _converters
import nidigital._visatype as _visatype
import nidigital.enums as enums
import nidigital.errors as errors
import threading

from nidigital._visatype import *  # noqa: F403,H303

import nidigital.history_ram_cycle_information as history_ram_cycle_information  # noqa: F401


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
            if self.niDigital_Abort_cfunc is None:
                self.niDigital_Abort_cfunc = self._get_library_function('niDigital_Abort')
                self.niDigital_Abort_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDigital_Abort_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_Abort_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def abort_keep_alive(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niDigital_AbortKeepAlive_cfunc is None:
                self.niDigital_AbortKeepAlive_cfunc = self._get_library_function('niDigital_AbortKeepAlive')
                self.niDigital_AbortKeepAlive_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDigital_AbortKeepAlive_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_AbortKeepAlive_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def apply_levels_and_timing(self, session, site_list, levels_sheet, timing_sheet, initial_state_high_pins=None, initial_state_low_pins=None, initial_state_tristate_pins=None):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(site_list.encode(session._encoding))  # case C010
        levels_sheet_ctype = ctypes.create_string_buffer(levels_sheet.encode(session._encoding))  # case C020
        timing_sheet_ctype = ctypes.create_string_buffer(timing_sheet.encode(session._encoding))  # case C020
        initial_state_high_pins_ctype = ctypes.create_string_buffer(_converters.convert_repeated_capabilities_without_prefix(initial_state_high_pins).encode(session._encoding))  # case C040
        initial_state_low_pins_ctype = ctypes.create_string_buffer(_converters.convert_repeated_capabilities_without_prefix(initial_state_low_pins).encode(session._encoding))  # case C040
        initial_state_tristate_pins_ctype = ctypes.create_string_buffer(_converters.convert_repeated_capabilities_without_prefix(initial_state_tristate_pins).encode(session._encoding))  # case C040
        with self._func_lock:
            if self.niDigital_ApplyLevelsAndTiming_cfunc is None:
                self.niDigital_ApplyLevelsAndTiming_cfunc = self._get_library_function('niDigital_ApplyLevelsAndTiming')
                self.niDigital_ApplyLevelsAndTiming_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_ApplyLevelsAndTiming_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_ApplyLevelsAndTiming_cfunc(vi_ctype, site_list_ctype, levels_sheet_ctype, timing_sheet_ctype, initial_state_high_pins_ctype, initial_state_low_pins_ctype, initial_state_tristate_pins_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def apply_tdr_offsets(self, session, channel_list, offsets):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(session._encoding))  # case C010
        num_offsets_ctype = _visatype.ViInt32(0 if offsets is None else len(offsets))  # case S160
        offsets_converted = _converters.convert_timedeltas_to_seconds_real64(offsets)  # case B520
        offsets_ctype = get_ctypes_pointer_for_buffer(value=offsets_converted, library_type=_visatype.ViReal64)  # case B520
        with self._func_lock:
            if self.niDigital_ApplyTDROffsets_cfunc is None:
                self.niDigital_ApplyTDROffsets_cfunc = self._get_library_function('niDigital_ApplyTDROffsets')
                self.niDigital_ApplyTDROffsets_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDigital_ApplyTDROffsets_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_ApplyTDROffsets_cfunc(vi_ctype, channel_list_ctype, num_offsets_ctype, offsets_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _burst_pattern(self, session, site_list, start_label, select_digital_function=True, wait_until_done=True, timeout=hightime.timedelta(seconds=10.0)):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(site_list.encode(session._encoding))  # case C010
        start_label_ctype = ctypes.create_string_buffer(start_label.encode(session._encoding))  # case C020
        select_digital_function_ctype = _visatype.ViBoolean(select_digital_function)  # case S150
        wait_until_done_ctype = _visatype.ViBoolean(wait_until_done)  # case S150
        timeout_ctype = _converters.convert_timedelta_to_seconds_real64(timeout)  # case S140
        with self._func_lock:
            if self.niDigital_BurstPattern_cfunc is None:
                self.niDigital_BurstPattern_cfunc = self._get_library_function('niDigital_BurstPattern')
                self.niDigital_BurstPattern_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViBoolean, ViBoolean, ViReal64]  # noqa: F405
                self.niDigital_BurstPattern_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_BurstPattern_cfunc(vi_ctype, site_list_ctype, start_label_ctype, select_digital_function_ctype, wait_until_done_ctype, timeout_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def clock_generator_abort(self, session, channel_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(session._encoding))  # case C010
        with self._func_lock:
            if self.niDigital_ClockGenerator_Abort_cfunc is None:
                self.niDigital_ClockGenerator_Abort_cfunc = self._get_library_function('niDigital_ClockGenerator_Abort')
                self.niDigital_ClockGenerator_Abort_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_ClockGenerator_Abort_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_ClockGenerator_Abort_cfunc(vi_ctype, channel_list_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def clock_generator_generate_clock(self, session, channel_list, frequency, select_digital_function=True):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(session._encoding))  # case C010
        frequency_ctype = _visatype.ViReal64(frequency)  # case S150
        select_digital_function_ctype = _visatype.ViBoolean(select_digital_function)  # case S150
        with self._func_lock:
            if self.niDigital_ClockGenerator_GenerateClock_cfunc is None:
                self.niDigital_ClockGenerator_GenerateClock_cfunc = self._get_library_function('niDigital_ClockGenerator_GenerateClock')
                self.niDigital_ClockGenerator_GenerateClock_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViBoolean]  # noqa: F405
                self.niDigital_ClockGenerator_GenerateClock_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_ClockGenerator_GenerateClock_cfunc(vi_ctype, channel_list_ctype, frequency_ctype, select_digital_function_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def commit(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niDigital_Commit_cfunc is None:
                self.niDigital_Commit_cfunc = self._get_library_function('niDigital_Commit')
                self.niDigital_Commit_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDigital_Commit_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_Commit_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_active_load_levels(self, session, channel_list, iol, ioh, vcom):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(session._encoding))  # case C010
        iol_ctype = _visatype.ViReal64(iol)  # case S150
        ioh_ctype = _visatype.ViReal64(ioh)  # case S150
        vcom_ctype = _visatype.ViReal64(vcom)  # case S150
        with self._func_lock:
            if self.niDigital_ConfigureActiveLoadLevels_cfunc is None:
                self.niDigital_ConfigureActiveLoadLevels_cfunc = self._get_library_function('niDigital_ConfigureActiveLoadLevels')
                self.niDigital_ConfigureActiveLoadLevels_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViReal64, ViReal64]  # noqa: F405
                self.niDigital_ConfigureActiveLoadLevels_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_ConfigureActiveLoadLevels_cfunc(vi_ctype, channel_list_ctype, iol_ctype, ioh_ctype, vcom_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_pattern_burst_sites(self, session, site_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(site_list.encode(session._encoding))  # case C010
        with self._func_lock:
            if self.niDigital_ConfigurePatternBurstSites_cfunc is None:
                self.niDigital_ConfigurePatternBurstSites_cfunc = self._get_library_function('niDigital_ConfigurePatternBurstSites')
                self.niDigital_ConfigurePatternBurstSites_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_ConfigurePatternBurstSites_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_ConfigurePatternBurstSites_cfunc(vi_ctype, site_list_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_time_set_compare_edges_strobe(self, session, pin_list, time_set_name, strobe_edge):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(pin_list.encode(session._encoding))  # case C010
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(session._encoding))  # case C020
        strobe_edge_ctype = _converters.convert_timedelta_to_seconds_real64(strobe_edge)  # case S140
        with self._func_lock:
            if self.niDigital_ConfigureTimeSetCompareEdgesStrobe_cfunc is None:
                self.niDigital_ConfigureTimeSetCompareEdgesStrobe_cfunc = self._get_library_function('niDigital_ConfigureTimeSetCompareEdgesStrobe')
                self.niDigital_ConfigureTimeSetCompareEdgesStrobe_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViReal64]  # noqa: F405
                self.niDigital_ConfigureTimeSetCompareEdgesStrobe_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_ConfigureTimeSetCompareEdgesStrobe_cfunc(vi_ctype, pin_list_ctype, time_set_name_ctype, strobe_edge_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_time_set_compare_edges_strobe2x(self, session, pin_list, time_set_name, strobe_edge, strobe2_edge):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(pin_list.encode(session._encoding))  # case C010
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(session._encoding))  # case C020
        strobe_edge_ctype = _converters.convert_timedelta_to_seconds_real64(strobe_edge)  # case S140
        strobe2_edge_ctype = _converters.convert_timedelta_to_seconds_real64(strobe2_edge)  # case S140
        with self._func_lock:
            if self.niDigital_ConfigureTimeSetCompareEdgesStrobe2x_cfunc is None:
                self.niDigital_ConfigureTimeSetCompareEdgesStrobe2x_cfunc = self._get_library_function('niDigital_ConfigureTimeSetCompareEdgesStrobe2x')
                self.niDigital_ConfigureTimeSetCompareEdgesStrobe2x_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViReal64, ViReal64]  # noqa: F405
                self.niDigital_ConfigureTimeSetCompareEdgesStrobe2x_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_ConfigureTimeSetCompareEdgesStrobe2x_cfunc(vi_ctype, pin_list_ctype, time_set_name_ctype, strobe_edge_ctype, strobe2_edge_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_time_set_drive_edges(self, session, pin_list, time_set_name, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(pin_list.encode(session._encoding))  # case C010
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(session._encoding))  # case C020
        format_ctype = _visatype.ViInt32(format.value)  # case S130
        drive_on_edge_ctype = _converters.convert_timedelta_to_seconds_real64(drive_on_edge)  # case S140
        drive_data_edge_ctype = _converters.convert_timedelta_to_seconds_real64(drive_data_edge)  # case S140
        drive_return_edge_ctype = _converters.convert_timedelta_to_seconds_real64(drive_return_edge)  # case S140
        drive_off_edge_ctype = _converters.convert_timedelta_to_seconds_real64(drive_off_edge)  # case S140
        with self._func_lock:
            if self.niDigital_ConfigureTimeSetDriveEdges_cfunc is None:
                self.niDigital_ConfigureTimeSetDriveEdges_cfunc = self._get_library_function('niDigital_ConfigureTimeSetDriveEdges')
                self.niDigital_ConfigureTimeSetDriveEdges_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ViReal64, ViReal64, ViReal64, ViReal64]  # noqa: F405
                self.niDigital_ConfigureTimeSetDriveEdges_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_ConfigureTimeSetDriveEdges_cfunc(vi_ctype, pin_list_ctype, time_set_name_ctype, format_ctype, drive_on_edge_ctype, drive_data_edge_ctype, drive_return_edge_ctype, drive_off_edge_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_time_set_drive_edges2x(self, session, pin_list, time_set_name, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge, drive_data2_edge, drive_return2_edge):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(pin_list.encode(session._encoding))  # case C010
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(session._encoding))  # case C020
        format_ctype = _visatype.ViInt32(format.value)  # case S130
        drive_on_edge_ctype = _converters.convert_timedelta_to_seconds_real64(drive_on_edge)  # case S140
        drive_data_edge_ctype = _converters.convert_timedelta_to_seconds_real64(drive_data_edge)  # case S140
        drive_return_edge_ctype = _converters.convert_timedelta_to_seconds_real64(drive_return_edge)  # case S140
        drive_off_edge_ctype = _converters.convert_timedelta_to_seconds_real64(drive_off_edge)  # case S140
        drive_data2_edge_ctype = _converters.convert_timedelta_to_seconds_real64(drive_data2_edge)  # case S140
        drive_return2_edge_ctype = _converters.convert_timedelta_to_seconds_real64(drive_return2_edge)  # case S140
        with self._func_lock:
            if self.niDigital_ConfigureTimeSetDriveEdges2x_cfunc is None:
                self.niDigital_ConfigureTimeSetDriveEdges2x_cfunc = self._get_library_function('niDigital_ConfigureTimeSetDriveEdges2x')
                self.niDigital_ConfigureTimeSetDriveEdges2x_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ViReal64, ViReal64, ViReal64, ViReal64, ViReal64, ViReal64]  # noqa: F405
                self.niDigital_ConfigureTimeSetDriveEdges2x_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_ConfigureTimeSetDriveEdges2x_cfunc(vi_ctype, pin_list_ctype, time_set_name_ctype, format_ctype, drive_on_edge_ctype, drive_data_edge_ctype, drive_return_edge_ctype, drive_off_edge_ctype, drive_data2_edge_ctype, drive_return2_edge_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_time_set_drive_format(self, session, pin_list, time_set_name, drive_format):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(pin_list.encode(session._encoding))  # case C010
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(session._encoding))  # case C020
        drive_format_ctype = _visatype.ViInt32(drive_format.value)  # case S130
        with self._func_lock:
            if self.niDigital_ConfigureTimeSetDriveFormat_cfunc is None:
                self.niDigital_ConfigureTimeSetDriveFormat_cfunc = self._get_library_function('niDigital_ConfigureTimeSetDriveFormat')
                self.niDigital_ConfigureTimeSetDriveFormat_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niDigital_ConfigureTimeSetDriveFormat_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_ConfigureTimeSetDriveFormat_cfunc(vi_ctype, pin_list_ctype, time_set_name_ctype, drive_format_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_time_set_edge(self, session, pin_list, time_set_name, edge, time):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(pin_list.encode(session._encoding))  # case C010
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(session._encoding))  # case C020
        edge_ctype = _visatype.ViInt32(edge.value)  # case S130
        time_ctype = _converters.convert_timedelta_to_seconds_real64(time)  # case S140
        with self._func_lock:
            if self.niDigital_ConfigureTimeSetEdge_cfunc is None:
                self.niDigital_ConfigureTimeSetEdge_cfunc = self._get_library_function('niDigital_ConfigureTimeSetEdge')
                self.niDigital_ConfigureTimeSetEdge_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ViReal64]  # noqa: F405
                self.niDigital_ConfigureTimeSetEdge_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_ConfigureTimeSetEdge_cfunc(vi_ctype, pin_list_ctype, time_set_name_ctype, edge_ctype, time_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_time_set_edge_multiplier(self, session, pin_list, time_set_name, edge_multiplier):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(pin_list.encode(session._encoding))  # case C010
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(session._encoding))  # case C020
        edge_multiplier_ctype = _visatype.ViInt32(edge_multiplier)  # case S150
        with self._func_lock:
            if self.niDigital_ConfigureTimeSetEdgeMultiplier_cfunc is None:
                self.niDigital_ConfigureTimeSetEdgeMultiplier_cfunc = self._get_library_function('niDigital_ConfigureTimeSetEdgeMultiplier')
                self.niDigital_ConfigureTimeSetEdgeMultiplier_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niDigital_ConfigureTimeSetEdgeMultiplier_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_ConfigureTimeSetEdgeMultiplier_cfunc(vi_ctype, pin_list_ctype, time_set_name_ctype, edge_multiplier_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_time_set_period(self, session, time_set_name, period):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(session._encoding))  # case C020
        period_ctype = _converters.convert_timedelta_to_seconds_real64(period)  # case S140
        with self._func_lock:
            if self.niDigital_ConfigureTimeSetPeriod_cfunc is None:
                self.niDigital_ConfigureTimeSetPeriod_cfunc = self._get_library_function('niDigital_ConfigureTimeSetPeriod')
                self.niDigital_ConfigureTimeSetPeriod_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64]  # noqa: F405
                self.niDigital_ConfigureTimeSetPeriod_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_ConfigureTimeSetPeriod_cfunc(vi_ctype, time_set_name_ctype, period_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_voltage_levels(self, session, channel_list, vil, vih, vol, voh, vterm):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(session._encoding))  # case C010
        vil_ctype = _visatype.ViReal64(vil)  # case S150
        vih_ctype = _visatype.ViReal64(vih)  # case S150
        vol_ctype = _visatype.ViReal64(vol)  # case S150
        voh_ctype = _visatype.ViReal64(voh)  # case S150
        vterm_ctype = _visatype.ViReal64(vterm)  # case S150
        with self._func_lock:
            if self.niDigital_ConfigureVoltageLevels_cfunc is None:
                self.niDigital_ConfigureVoltageLevels_cfunc = self._get_library_function('niDigital_ConfigureVoltageLevels')
                self.niDigital_ConfigureVoltageLevels_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViReal64, ViReal64, ViReal64, ViReal64]  # noqa: F405
                self.niDigital_ConfigureVoltageLevels_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_ConfigureVoltageLevels_cfunc(vi_ctype, channel_list_ctype, vil_ctype, vih_ctype, vol_ctype, voh_ctype, vterm_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_capture_waveform_from_file_digicapture(self, session, waveform_name, waveform_file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(session._encoding))  # case C020
        waveform_file_path_ctype = ctypes.create_string_buffer(waveform_file_path.encode(session._encoding))  # case C020
        with self._func_lock:
            if self.niDigital_CreateCaptureWaveformFromFileDigicapture_cfunc is None:
                self.niDigital_CreateCaptureWaveformFromFileDigicapture_cfunc = self._get_library_function('niDigital_CreateCaptureWaveformFromFileDigicapture')
                self.niDigital_CreateCaptureWaveformFromFileDigicapture_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_CreateCaptureWaveformFromFileDigicapture_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_CreateCaptureWaveformFromFileDigicapture_cfunc(vi_ctype, waveform_name_ctype, waveform_file_path_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_capture_waveform_parallel(self, session, pin_list, waveform_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(pin_list.encode(session._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(session._encoding))  # case C020
        with self._func_lock:
            if self.niDigital_CreateCaptureWaveformParallel_cfunc is None:
                self.niDigital_CreateCaptureWaveformParallel_cfunc = self._get_library_function('niDigital_CreateCaptureWaveformParallel')
                self.niDigital_CreateCaptureWaveformParallel_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_CreateCaptureWaveformParallel_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_CreateCaptureWaveformParallel_cfunc(vi_ctype, pin_list_ctype, waveform_name_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_capture_waveform_serial(self, session, pin_list, waveform_name, sample_width, bit_order):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(pin_list.encode(session._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(session._encoding))  # case C020
        sample_width_ctype = _visatype.ViUInt32(sample_width)  # case S150
        bit_order_ctype = _visatype.ViInt32(bit_order.value)  # case S130
        with self._func_lock:
            if self.niDigital_CreateCaptureWaveformSerial_cfunc is None:
                self.niDigital_CreateCaptureWaveformSerial_cfunc = self._get_library_function('niDigital_CreateCaptureWaveformSerial')
                self.niDigital_CreateCaptureWaveformSerial_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViUInt32, ViInt32]  # noqa: F405
                self.niDigital_CreateCaptureWaveformSerial_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_CreateCaptureWaveformSerial_cfunc(vi_ctype, pin_list_ctype, waveform_name_ctype, sample_width_ctype, bit_order_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_source_waveform_from_file_tdms(self, session, waveform_name, waveform_file_path, write_waveform_data=True):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(session._encoding))  # case C020
        waveform_file_path_ctype = ctypes.create_string_buffer(waveform_file_path.encode(session._encoding))  # case C020
        write_waveform_data_ctype = _visatype.ViBoolean(write_waveform_data)  # case S150
        with self._func_lock:
            if self.niDigital_CreateSourceWaveformFromFileTDMS_cfunc is None:
                self.niDigital_CreateSourceWaveformFromFileTDMS_cfunc = self._get_library_function('niDigital_CreateSourceWaveformFromFileTDMS')
                self.niDigital_CreateSourceWaveformFromFileTDMS_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViBoolean]  # noqa: F405
                self.niDigital_CreateSourceWaveformFromFileTDMS_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_CreateSourceWaveformFromFileTDMS_cfunc(vi_ctype, waveform_name_ctype, waveform_file_path_ctype, write_waveform_data_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_source_waveform_parallel(self, session, pin_list, waveform_name, data_mapping):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(pin_list.encode(session._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(session._encoding))  # case C020
        data_mapping_ctype = _visatype.ViInt32(data_mapping.value)  # case S130
        with self._func_lock:
            if self.niDigital_CreateSourceWaveformParallel_cfunc is None:
                self.niDigital_CreateSourceWaveformParallel_cfunc = self._get_library_function('niDigital_CreateSourceWaveformParallel')
                self.niDigital_CreateSourceWaveformParallel_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niDigital_CreateSourceWaveformParallel_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_CreateSourceWaveformParallel_cfunc(vi_ctype, pin_list_ctype, waveform_name_ctype, data_mapping_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_source_waveform_serial(self, session, pin_list, waveform_name, data_mapping, sample_width, bit_order):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(pin_list.encode(session._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(session._encoding))  # case C020
        data_mapping_ctype = _visatype.ViInt32(data_mapping.value)  # case S130
        sample_width_ctype = _visatype.ViUInt32(sample_width)  # case S150
        bit_order_ctype = _visatype.ViInt32(bit_order.value)  # case S130
        with self._func_lock:
            if self.niDigital_CreateSourceWaveformSerial_cfunc is None:
                self.niDigital_CreateSourceWaveformSerial_cfunc = self._get_library_function('niDigital_CreateSourceWaveformSerial')
                self.niDigital_CreateSourceWaveformSerial_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ViUInt32, ViInt32]  # noqa: F405
                self.niDigital_CreateSourceWaveformSerial_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_CreateSourceWaveformSerial_cfunc(vi_ctype, pin_list_ctype, waveform_name_ctype, data_mapping_ctype, sample_width_ctype, bit_order_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_time_set(self, session, name):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        name_ctype = ctypes.create_string_buffer(name.encode(session._encoding))  # case C020
        with self._func_lock:
            if self.niDigital_CreateTimeSet_cfunc is None:
                self.niDigital_CreateTimeSet_cfunc = self._get_library_function('niDigital_CreateTimeSet')
                self.niDigital_CreateTimeSet_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_CreateTimeSet_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_CreateTimeSet_cfunc(vi_ctype, name_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def delete_all_time_sets(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niDigital_DeleteAllTimeSets_cfunc is None:
                self.niDigital_DeleteAllTimeSets_cfunc = self._get_library_function('niDigital_DeleteAllTimeSets')
                self.niDigital_DeleteAllTimeSets_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDigital_DeleteAllTimeSets_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_DeleteAllTimeSets_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disable_sites(self, session, site_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(site_list.encode(session._encoding))  # case C010
        with self._func_lock:
            if self.niDigital_DisableSites_cfunc is None:
                self.niDigital_DisableSites_cfunc = self._get_library_function('niDigital_DisableSites')
                self.niDigital_DisableSites_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_DisableSites_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_DisableSites_cfunc(vi_ctype, site_list_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def enable_sites(self, session, site_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(site_list.encode(session._encoding))  # case C010
        with self._func_lock:
            if self.niDigital_EnableSites_cfunc is None:
                self.niDigital_EnableSites_cfunc = self._get_library_function('niDigital_EnableSites')
                self.niDigital_EnableSites_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_EnableSites_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_EnableSites_cfunc(vi_ctype, site_list_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def fetch_capture_waveform_u32(self, session, site_list, waveform_name, samples_to_read, timeout):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(site_list.encode(session._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(session._encoding))  # case C020
        samples_to_read_ctype = _visatype.ViInt32(samples_to_read)  # case S150
        timeout_ctype = _visatype.ViReal64(timeout)  # case S150
        data_buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        data_ctype = None  # case B610
        actual_num_waveforms_ctype = _visatype.ViInt32()  # case S220
        actual_samples_per_waveform_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niDigital_FetchCaptureWaveformU32_cfunc is None:
                self.niDigital_FetchCaptureWaveformU32_cfunc = self._get_library_function('niDigital_FetchCaptureWaveformU32')
                self.niDigital_FetchCaptureWaveformU32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ViReal64, ViInt32, ctypes.POINTER(ViUInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDigital_FetchCaptureWaveformU32_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_FetchCaptureWaveformU32_cfunc(vi_ctype, site_list_ctype, waveform_name_ctype, samples_to_read_ctype, timeout_ctype, data_buffer_size_ctype, data_ctype, None if actual_num_waveforms_ctype is None else (ctypes.pointer(actual_num_waveforms_ctype)), None if actual_samples_per_waveform_ctype is None else (ctypes.pointer(actual_samples_per_waveform_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=False)
        data_buffer_size_ctype = _visatype.ViInt32(actual_num_waveforms_ctype.value)  # case S200
        data_size = actual_num_waveforms_ctype.value  # case B620
        data_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViUInt32, size=data_size)  # case B620
        error_code = self.niDigital_FetchCaptureWaveformU32_cfunc(vi_ctype, site_list_ctype, waveform_name_ctype, samples_to_read_ctype, timeout_ctype, data_buffer_size_ctype, data_ctype, None if actual_num_waveforms_ctype is None else (ctypes.pointer(actual_num_waveforms_ctype)), None if actual_samples_per_waveform_ctype is None else (ctypes.pointer(actual_samples_per_waveform_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return [int(data_ctype[i]) for i in range(data_buffer_size_ctype.value)], int(actual_samples_per_waveform_ctype.value)

    def _fetch_history_ram_cycle_information(self, session, site, sample_index):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        site_ctype = ctypes.create_string_buffer(site.encode(session._encoding))  # case C010
        sample_index_ctype = _visatype.ViInt64(sample_index)  # case S150
        pattern_index_ctype = _visatype.ViInt32()  # case S220
        time_set_index_ctype = _visatype.ViInt32()  # case S220
        vector_number_ctype = _visatype.ViInt64()  # case S220
        cycle_number_ctype = _visatype.ViInt64()  # case S220
        num_dut_cycles_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niDigital_FetchHistoryRAMCycleInformation_cfunc is None:
                self.niDigital_FetchHistoryRAMCycleInformation_cfunc = self._get_library_function('niDigital_FetchHistoryRAMCycleInformation')
                self.niDigital_FetchHistoryRAMCycleInformation_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt64, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt64), ctypes.POINTER(ViInt64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDigital_FetchHistoryRAMCycleInformation_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_FetchHistoryRAMCycleInformation_cfunc(vi_ctype, site_ctype, sample_index_ctype, None if pattern_index_ctype is None else (ctypes.pointer(pattern_index_ctype)), None if time_set_index_ctype is None else (ctypes.pointer(time_set_index_ctype)), None if vector_number_ctype is None else (ctypes.pointer(vector_number_ctype)), None if cycle_number_ctype is None else (ctypes.pointer(cycle_number_ctype)), None if num_dut_cycles_ctype is None else (ctypes.pointer(num_dut_cycles_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(pattern_index_ctype.value), int(time_set_index_ctype.value), int(vector_number_ctype.value), int(cycle_number_ctype.value), int(num_dut_cycles_ctype.value)

    def _fetch_history_ram_cycle_pin_data(self, session, site, pin_list, sample_index, dut_cycle_index):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        site_ctype = ctypes.create_string_buffer(site.encode(session._encoding))  # case C010
        pin_list_ctype = ctypes.create_string_buffer(pin_list.encode(session._encoding))  # case C020
        sample_index_ctype = _visatype.ViInt64(sample_index)  # case S150
        dut_cycle_index_ctype = _visatype.ViInt32(dut_cycle_index)  # case S150
        pin_data_buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        expected_pin_states_ctype = None  # case B610
        actual_pin_states_ctype = None  # case B610
        per_pin_pass_fail_ctype = None  # case B610
        actual_num_pin_data_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niDigital_FetchHistoryRAMCyclePinData_cfunc is None:
                self.niDigital_FetchHistoryRAMCyclePinData_cfunc = self._get_library_function('niDigital_FetchHistoryRAMCyclePinData')
                self.niDigital_FetchHistoryRAMCyclePinData_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt64, ViInt32, ViInt32, ctypes.POINTER(ViUInt8), ctypes.POINTER(ViUInt8), ctypes.POINTER(ViBoolean), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDigital_FetchHistoryRAMCyclePinData_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_FetchHistoryRAMCyclePinData_cfunc(vi_ctype, site_ctype, pin_list_ctype, sample_index_ctype, dut_cycle_index_ctype, pin_data_buffer_size_ctype, expected_pin_states_ctype, actual_pin_states_ctype, per_pin_pass_fail_ctype, None if actual_num_pin_data_ctype is None else (ctypes.pointer(actual_num_pin_data_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=False)
        pin_data_buffer_size_ctype = _visatype.ViInt32(actual_num_pin_data_ctype.value)  # case S200
        expected_pin_states_size = actual_num_pin_data_ctype.value  # case B620
        expected_pin_states_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViUInt8, size=expected_pin_states_size)  # case B620
        actual_pin_states_size = actual_num_pin_data_ctype.value  # case B620
        actual_pin_states_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViUInt8, size=actual_pin_states_size)  # case B620
        per_pin_pass_fail_size = actual_num_pin_data_ctype.value  # case B620
        per_pin_pass_fail_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViBoolean, size=per_pin_pass_fail_size)  # case B620
        error_code = self.niDigital_FetchHistoryRAMCyclePinData_cfunc(vi_ctype, site_ctype, pin_list_ctype, sample_index_ctype, dut_cycle_index_ctype, pin_data_buffer_size_ctype, expected_pin_states_ctype, actual_pin_states_ctype, per_pin_pass_fail_ctype, None if actual_num_pin_data_ctype is None else (ctypes.pointer(actual_num_pin_data_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return [enums.PinState(expected_pin_states_ctype[i]) for i in range(pin_data_buffer_size_ctype.value)], [enums.PinState(actual_pin_states_ctype[i]) for i in range(pin_data_buffer_size_ctype.value)], [bool(per_pin_pass_fail_ctype[i]) for i in range(pin_data_buffer_size_ctype.value)]

    def _fetch_history_ram_scan_cycle_number(self, session, site, sample_index):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        site_ctype = ctypes.create_string_buffer(site.encode(session._encoding))  # case C010
        sample_index_ctype = _visatype.ViInt64(sample_index)  # case S150
        scan_cycle_number_ctype = _visatype.ViInt64()  # case S220
        with self._func_lock:
            if self.niDigital_FetchHistoryRAMScanCycleNumber_cfunc is None:
                self.niDigital_FetchHistoryRAMScanCycleNumber_cfunc = self._get_library_function('niDigital_FetchHistoryRAMScanCycleNumber')
                self.niDigital_FetchHistoryRAMScanCycleNumber_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt64, ctypes.POINTER(ViInt64)]  # noqa: F405
                self.niDigital_FetchHistoryRAMScanCycleNumber_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_FetchHistoryRAMScanCycleNumber_cfunc(vi_ctype, site_ctype, sample_index_ctype, None if scan_cycle_number_ctype is None else (ctypes.pointer(scan_cycle_number_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(scan_cycle_number_ctype.value)

    def frequency_counter_measure_frequency(self, session, channel_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(session._encoding))  # case C010
        frequencies_buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        frequencies_ctype = None  # case B610
        actual_num_frequencies_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niDigital_FrequencyCounter_MeasureFrequency_cfunc is None:
                self.niDigital_FrequencyCounter_MeasureFrequency_cfunc = self._get_library_function('niDigital_FrequencyCounter_MeasureFrequency')
                self.niDigital_FrequencyCounter_MeasureFrequency_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDigital_FrequencyCounter_MeasureFrequency_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_FrequencyCounter_MeasureFrequency_cfunc(vi_ctype, channel_list_ctype, frequencies_buffer_size_ctype, frequencies_ctype, None if actual_num_frequencies_ctype is None else (ctypes.pointer(actual_num_frequencies_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=False)
        frequencies_buffer_size_ctype = _visatype.ViInt32(actual_num_frequencies_ctype.value)  # case S200
        frequencies_size = actual_num_frequencies_ctype.value  # case B620
        frequencies_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=frequencies_size)  # case B620
        error_code = self.niDigital_FrequencyCounter_MeasureFrequency_cfunc(vi_ctype, channel_list_ctype, frequencies_buffer_size_ctype, frequencies_ctype, None if actual_num_frequencies_ctype is None else (ctypes.pointer(actual_num_frequencies_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(frequencies_ctype[i]) for i in range(frequencies_buffer_size_ctype.value)]

    def _get_attribute_vi_boolean(self, session, channel_name, attribute):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViBoolean()  # case S220
        with self._func_lock:
            if self.niDigital_GetAttributeViBoolean_cfunc is None:
                self.niDigital_GetAttributeViBoolean_cfunc = self._get_library_function('niDigital_GetAttributeViBoolean')
                self.niDigital_GetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niDigital_GetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_GetAttributeViBoolean_cfunc(vi_ctype, channel_name_ctype, attribute_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(value_ctype.value)

    def _get_attribute_vi_int32(self, session, channel_name, attribute):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niDigital_GetAttributeViInt32_cfunc is None:
                self.niDigital_GetAttributeViInt32_cfunc = self._get_library_function('niDigital_GetAttributeViInt32')
                self.niDigital_GetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDigital_GetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_GetAttributeViInt32_cfunc(vi_ctype, channel_name_ctype, attribute_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(value_ctype.value)

    def _get_attribute_vi_int64(self, session, channel_name, attribute):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViInt64()  # case S220
        with self._func_lock:
            if self.niDigital_GetAttributeViInt64_cfunc is None:
                self.niDigital_GetAttributeViInt64_cfunc = self._get_library_function('niDigital_GetAttributeViInt64')
                self.niDigital_GetAttributeViInt64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViInt64)]  # noqa: F405
                self.niDigital_GetAttributeViInt64_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_GetAttributeViInt64_cfunc(vi_ctype, channel_name_ctype, attribute_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(value_ctype.value)

    def _get_attribute_vi_real64(self, session, channel_name, attribute):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViReal64()  # case S220
        with self._func_lock:
            if self.niDigital_GetAttributeViReal64_cfunc is None:
                self.niDigital_GetAttributeViReal64_cfunc = self._get_library_function('niDigital_GetAttributeViReal64')
                self.niDigital_GetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDigital_GetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_GetAttributeViReal64_cfunc(vi_ctype, channel_name_ctype, attribute_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return float(value_ctype.value)

    def _get_attribute_vi_string(self, session, channel_name, attribute):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        value_ctype = None  # case C050
        with self._func_lock:
            if self.niDigital_GetAttributeViString_cfunc is None:
                self.niDigital_GetAttributeViString_cfunc = self._get_library_function('niDigital_GetAttributeViString')
                self.niDigital_GetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_GetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_GetAttributeViString_cfunc(vi_ctype, channel_name_ctype, attribute_ctype, buffer_size_ctype, value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        value_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self.niDigital_GetAttributeViString_cfunc(vi_ctype, channel_name_ctype, attribute_ctype, buffer_size_ctype, value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return value_ctype.value.decode(session._encoding)

    def get_channel_names(self, session, indices):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        indices_ctype = ctypes.create_string_buffer(_converters.convert_repeated_capabilities_without_prefix(indices).encode(session._encoding))  # case C040
        name_buffer_size_ctype = _visatype.ViInt32()  # case S170
        names_ctype = None  # case C050
        with self._func_lock:
            if self.niDigital_GetChannelNameFromString_cfunc is None:
                self.niDigital_GetChannelNameFromString_cfunc = self._get_library_function('niDigital_GetChannelNameFromString')
                self.niDigital_GetChannelNameFromString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_GetChannelNameFromString_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_GetChannelNameFromString_cfunc(vi_ctype, indices_ctype, name_buffer_size_ctype, names_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=False)
        name_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        names_ctype = (_visatype.ViChar * name_buffer_size_ctype.value)()  # case C060
        error_code = self.niDigital_GetChannelNameFromString_cfunc(vi_ctype, indices_ctype, name_buffer_size_ctype, names_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return _converters.convert_comma_separated_string_to_list(names_ctype.value.decode(session._encoding))

    def _get_error(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        error_code_ctype = _visatype.ViStatus()  # case S220
        error_description_buffer_size_ctype = _visatype.ViInt32()  # case S170
        error_description_ctype = None  # case C050
        with self._func_lock:
            if self.niDigital_GetError_cfunc is None:
                self.niDigital_GetError_cfunc = self._get_library_function('niDigital_GetError')
                self.niDigital_GetError_cfunc.argtypes = [ViSession, ctypes.POINTER(ViStatus), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_GetError_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_GetError_cfunc(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), error_description_buffer_size_ctype, error_description_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=True)
        error_description_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        error_description_ctype = (_visatype.ViChar * error_description_buffer_size_ctype.value)()  # case C060
        error_code = self.niDigital_GetError_cfunc(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), error_description_buffer_size_ctype, error_description_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=True)
        return int(error_code_ctype.value), error_description_ctype.value.decode(session._encoding)

    def get_fail_count(self, session, channel_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(session._encoding))  # case C010
        buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        failure_count_ctype = None  # case B610
        actual_num_read_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niDigital_GetFailCount_cfunc is None:
                self.niDigital_GetFailCount_cfunc = self._get_library_function('niDigital_GetFailCount')
                self.niDigital_GetFailCount_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDigital_GetFailCount_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_GetFailCount_cfunc(vi_ctype, channel_list_ctype, buffer_size_ctype, failure_count_ctype, None if actual_num_read_ctype is None else (ctypes.pointer(actual_num_read_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(actual_num_read_ctype.value)  # case S200
        failure_count_size = actual_num_read_ctype.value  # case B620
        failure_count_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViInt64, size=failure_count_size)  # case B620
        error_code = self.niDigital_GetFailCount_cfunc(vi_ctype, channel_list_ctype, buffer_size_ctype, failure_count_ctype, None if actual_num_read_ctype is None else (ctypes.pointer(actual_num_read_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return [int(failure_count_ctype[i]) for i in range(buffer_size_ctype.value)]

    def get_history_ram_sample_count(self, session, site):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        site_ctype = ctypes.create_string_buffer(site.encode(session._encoding))  # case C010
        sample_count_ctype = _visatype.ViInt64()  # case S220
        with self._func_lock:
            if self.niDigital_GetHistoryRAMSampleCount_cfunc is None:
                self.niDigital_GetHistoryRAMSampleCount_cfunc = self._get_library_function('niDigital_GetHistoryRAMSampleCount')
                self.niDigital_GetHistoryRAMSampleCount_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViInt64)]  # noqa: F405
                self.niDigital_GetHistoryRAMSampleCount_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_GetHistoryRAMSampleCount_cfunc(vi_ctype, site_ctype, None if sample_count_ctype is None else (ctypes.pointer(sample_count_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(sample_count_ctype.value)

    def _get_pattern_name(self, session, pattern_index):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        pattern_index_ctype = _visatype.ViInt32(pattern_index)  # case S150
        name_buffer_size_ctype = _visatype.ViInt32()  # case S170
        name_ctype = None  # case C050
        with self._func_lock:
            if self.niDigital_GetPatternName_cfunc is None:
                self.niDigital_GetPatternName_cfunc = self._get_library_function('niDigital_GetPatternName')
                self.niDigital_GetPatternName_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_GetPatternName_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_GetPatternName_cfunc(vi_ctype, pattern_index_ctype, name_buffer_size_ctype, name_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=False)
        name_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        name_ctype = (_visatype.ViChar * name_buffer_size_ctype.value)()  # case C060
        error_code = self.niDigital_GetPatternName_cfunc(vi_ctype, pattern_index_ctype, name_buffer_size_ctype, name_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return name_ctype.value.decode(session._encoding)

    def get_pattern_pin_names(self, session, start_label):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        start_label_ctype = ctypes.create_string_buffer(start_label.encode(session._encoding))  # case C020
        pin_list_buffer_size_ctype = _visatype.ViInt32()  # case S170
        pin_list_ctype = None  # case C050
        with self._func_lock:
            if self.niDigital_GetPatternPinList_cfunc is None:
                self.niDigital_GetPatternPinList_cfunc = self._get_library_function('niDigital_GetPatternPinList')
                self.niDigital_GetPatternPinList_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_GetPatternPinList_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_GetPatternPinList_cfunc(vi_ctype, start_label_ctype, pin_list_buffer_size_ctype, pin_list_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=False)
        pin_list_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        pin_list_ctype = (_visatype.ViChar * pin_list_buffer_size_ctype.value)()  # case C060
        error_code = self.niDigital_GetPatternPinList_cfunc(vi_ctype, start_label_ctype, pin_list_buffer_size_ctype, pin_list_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return _converters.convert_comma_separated_string_to_list(pin_list_ctype.value.decode(session._encoding))

    def _get_pin_name(self, session, pin_index):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        pin_index_ctype = _visatype.ViInt32(pin_index)  # case S150
        name_buffer_size_ctype = _visatype.ViInt32()  # case S170
        name_ctype = None  # case C050
        with self._func_lock:
            if self.niDigital_GetPinName_cfunc is None:
                self.niDigital_GetPinName_cfunc = self._get_library_function('niDigital_GetPinName')
                self.niDigital_GetPinName_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_GetPinName_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_GetPinName_cfunc(vi_ctype, pin_index_ctype, name_buffer_size_ctype, name_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=False)
        name_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        name_ctype = (_visatype.ViChar * name_buffer_size_ctype.value)()  # case C060
        error_code = self.niDigital_GetPinName_cfunc(vi_ctype, pin_index_ctype, name_buffer_size_ctype, name_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return name_ctype.value.decode(session._encoding)

    def _get_pin_results_pin_information(self, session, channel_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(session._encoding))  # case C010
        buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        pin_indexes_ctype = None  # case B610
        site_numbers_ctype = None  # case B610
        channel_indexes_ctype = None  # case B610
        actual_num_values_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niDigital_GetPinResultsPinInformation_cfunc is None:
                self.niDigital_GetPinResultsPinInformation_cfunc = self._get_library_function('niDigital_GetPinResultsPinInformation')
                self.niDigital_GetPinResultsPinInformation_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDigital_GetPinResultsPinInformation_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_GetPinResultsPinInformation_cfunc(vi_ctype, channel_list_ctype, buffer_size_ctype, pin_indexes_ctype, site_numbers_ctype, channel_indexes_ctype, None if actual_num_values_ctype is None else (ctypes.pointer(actual_num_values_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(actual_num_values_ctype.value)  # case S200
        pin_indexes_size = actual_num_values_ctype.value  # case B620
        pin_indexes_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViInt32, size=pin_indexes_size)  # case B620
        site_numbers_size = actual_num_values_ctype.value  # case B620
        site_numbers_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViInt32, size=site_numbers_size)  # case B620
        channel_indexes_size = actual_num_values_ctype.value  # case B620
        channel_indexes_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViInt32, size=channel_indexes_size)  # case B620
        error_code = self.niDigital_GetPinResultsPinInformation_cfunc(vi_ctype, channel_list_ctype, buffer_size_ctype, pin_indexes_ctype, site_numbers_ctype, channel_indexes_ctype, None if actual_num_values_ctype is None else (ctypes.pointer(actual_num_values_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return [int(pin_indexes_ctype[i]) for i in range(buffer_size_ctype.value)], [int(site_numbers_ctype[i]) for i in range(buffer_size_ctype.value)], [int(channel_indexes_ctype[i]) for i in range(buffer_size_ctype.value)]

    def _get_site_pass_fail(self, session, site_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(site_list.encode(session._encoding))  # case C010
        pass_fail_buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        pass_fail_ctype = None  # case B610
        actual_num_sites_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niDigital_GetSitePassFail_cfunc is None:
                self.niDigital_GetSitePassFail_cfunc = self._get_library_function('niDigital_GetSitePassFail')
                self.niDigital_GetSitePassFail_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViBoolean), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDigital_GetSitePassFail_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_GetSitePassFail_cfunc(vi_ctype, site_list_ctype, pass_fail_buffer_size_ctype, pass_fail_ctype, None if actual_num_sites_ctype is None else (ctypes.pointer(actual_num_sites_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=False)
        pass_fail_buffer_size_ctype = _visatype.ViInt32(actual_num_sites_ctype.value)  # case S200
        pass_fail_size = actual_num_sites_ctype.value  # case B620
        pass_fail_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViBoolean, size=pass_fail_size)  # case B620
        error_code = self.niDigital_GetSitePassFail_cfunc(vi_ctype, site_list_ctype, pass_fail_buffer_size_ctype, pass_fail_ctype, None if actual_num_sites_ctype is None else (ctypes.pointer(actual_num_sites_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return [bool(pass_fail_ctype[i]) for i in range(pass_fail_buffer_size_ctype.value)]

    def _get_site_results_site_numbers(self, session, site_list, site_result_type):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(site_list.encode(session._encoding))  # case C010
        site_result_type_ctype = _visatype.ViInt32(site_result_type.value)  # case S130
        site_numbers_buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        site_numbers_ctype = None  # case B610
        actual_num_site_numbers_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niDigital_GetSiteResultsSiteNumbers_cfunc is None:
                self.niDigital_GetSiteResultsSiteNumbers_cfunc = self._get_library_function('niDigital_GetSiteResultsSiteNumbers')
                self.niDigital_GetSiteResultsSiteNumbers_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViInt32, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDigital_GetSiteResultsSiteNumbers_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_GetSiteResultsSiteNumbers_cfunc(vi_ctype, site_list_ctype, site_result_type_ctype, site_numbers_buffer_size_ctype, site_numbers_ctype, None if actual_num_site_numbers_ctype is None else (ctypes.pointer(actual_num_site_numbers_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=False)
        site_numbers_buffer_size_ctype = _visatype.ViInt32(actual_num_site_numbers_ctype.value)  # case S200
        site_numbers_size = actual_num_site_numbers_ctype.value  # case B620
        site_numbers_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViInt32, size=site_numbers_size)  # case B620
        error_code = self.niDigital_GetSiteResultsSiteNumbers_cfunc(vi_ctype, site_list_ctype, site_result_type_ctype, site_numbers_buffer_size_ctype, site_numbers_ctype, None if actual_num_site_numbers_ctype is None else (ctypes.pointer(actual_num_site_numbers_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return [int(site_numbers_ctype[i]) for i in range(site_numbers_buffer_size_ctype.value)]

    def get_time_set_drive_format(self, session, pin, time_set_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        pin_ctype = ctypes.create_string_buffer(pin.encode(session._encoding))  # case C010
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(session._encoding))  # case C020
        format_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niDigital_GetTimeSetDriveFormat_cfunc is None:
                self.niDigital_GetTimeSetDriveFormat_cfunc = self._get_library_function('niDigital_GetTimeSetDriveFormat')
                self.niDigital_GetTimeSetDriveFormat_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDigital_GetTimeSetDriveFormat_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_GetTimeSetDriveFormat_cfunc(vi_ctype, pin_ctype, time_set_name_ctype, None if format_ctype is None else (ctypes.pointer(format_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return enums.DriveFormat(format_ctype.value)

    def get_time_set_edge(self, session, pin, time_set_name, edge):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        pin_ctype = ctypes.create_string_buffer(pin.encode(session._encoding))  # case C010
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(session._encoding))  # case C020
        edge_ctype = _visatype.ViInt32(edge.value)  # case S130
        time_ctype = _visatype.ViReal64()  # case S220
        with self._func_lock:
            if self.niDigital_GetTimeSetEdge_cfunc is None:
                self.niDigital_GetTimeSetEdge_cfunc = self._get_library_function('niDigital_GetTimeSetEdge')
                self.niDigital_GetTimeSetEdge_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDigital_GetTimeSetEdge_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_GetTimeSetEdge_cfunc(vi_ctype, pin_ctype, time_set_name_ctype, edge_ctype, None if time_ctype is None else (ctypes.pointer(time_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return _converters.convert_seconds_real64_to_timedelta(float(time_ctype.value))

    def get_time_set_edge_multiplier(self, session, pin, time_set_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        pin_ctype = ctypes.create_string_buffer(pin.encode(session._encoding))  # case C010
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(session._encoding))  # case C020
        edge_multiplier_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niDigital_GetTimeSetEdgeMultiplier_cfunc is None:
                self.niDigital_GetTimeSetEdgeMultiplier_cfunc = self._get_library_function('niDigital_GetTimeSetEdgeMultiplier')
                self.niDigital_GetTimeSetEdgeMultiplier_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDigital_GetTimeSetEdgeMultiplier_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_GetTimeSetEdgeMultiplier_cfunc(vi_ctype, pin_ctype, time_set_name_ctype, None if edge_multiplier_ctype is None else (ctypes.pointer(edge_multiplier_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(edge_multiplier_ctype.value)

    def _get_time_set_name(self, session, time_set_index):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        time_set_index_ctype = _visatype.ViInt32(time_set_index)  # case S150
        name_buffer_size_ctype = _visatype.ViInt32()  # case S170
        name_ctype = None  # case C050
        with self._func_lock:
            if self.niDigital_GetTimeSetName_cfunc is None:
                self.niDigital_GetTimeSetName_cfunc = self._get_library_function('niDigital_GetTimeSetName')
                self.niDigital_GetTimeSetName_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_GetTimeSetName_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_GetTimeSetName_cfunc(vi_ctype, time_set_index_ctype, name_buffer_size_ctype, name_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=False)
        name_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        name_ctype = (_visatype.ViChar * name_buffer_size_ctype.value)()  # case C060
        error_code = self.niDigital_GetTimeSetName_cfunc(vi_ctype, time_set_index_ctype, name_buffer_size_ctype, name_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return name_ctype.value.decode(session._encoding)

    def get_time_set_period(self, session, time_set_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(session._encoding))  # case C020
        period_ctype = _visatype.ViReal64()  # case S220
        with self._func_lock:
            if self.niDigital_GetTimeSetPeriod_cfunc is None:
                self.niDigital_GetTimeSetPeriod_cfunc = self._get_library_function('niDigital_GetTimeSetPeriod')
                self.niDigital_GetTimeSetPeriod_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDigital_GetTimeSetPeriod_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_GetTimeSetPeriod_cfunc(vi_ctype, time_set_name_ctype, None if period_ctype is None else (ctypes.pointer(period_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return _converters.convert_seconds_real64_to_timedelta(float(period_ctype.value))

    def _init_with_options(self, session, resource_name, id_query=False, reset_device=False, option_string=""):  # noqa: N802
        resource_name_ctype = ctypes.create_string_buffer(resource_name.encode(session._encoding))  # case C020
        id_query_ctype = _visatype.ViBoolean(id_query)  # case S150
        reset_device_ctype = _visatype.ViBoolean(reset_device)  # case S150
        option_string_ctype = ctypes.create_string_buffer(_converters.convert_init_with_options_dictionary(option_string).encode(session._encoding))  # case C040
        new_vi_ctype = _visatype.ViSession()  # case S220
        with self._func_lock:
            if self.niDigital_InitWithOptions_cfunc is None:
                self.niDigital_InitWithOptions_cfunc = self._get_library_function('niDigital_InitWithOptions')
                self.niDigital_InitWithOptions_cfunc.argtypes = [ctypes.POINTER(ViChar), ViBoolean, ViBoolean, ctypes.POINTER(ViChar), ctypes.POINTER(ViSession)]  # noqa: F405
                self.niDigital_InitWithOptions_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_InitWithOptions_cfunc(resource_name_ctype, id_query_ctype, reset_device_ctype, option_string_ctype, None if new_vi_ctype is None else (ctypes.pointer(new_vi_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(new_vi_ctype.value)

    def _initiate(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niDigital_Initiate_cfunc is None:
                self.niDigital_Initiate_cfunc = self._get_library_function('niDigital_Initiate')
                self.niDigital_Initiate_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDigital_Initiate_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_Initiate_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def is_done(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        done_ctype = _visatype.ViBoolean()  # case S220
        with self._func_lock:
            if self.niDigital_IsDone_cfunc is None:
                self.niDigital_IsDone_cfunc = self._get_library_function('niDigital_IsDone')
                self.niDigital_IsDone_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niDigital_IsDone_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_IsDone_cfunc(vi_ctype, None if done_ctype is None else (ctypes.pointer(done_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(done_ctype.value)

    def is_site_enabled(self, session, site):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        site_ctype = ctypes.create_string_buffer(site.encode(session._encoding))  # case C010
        enable_ctype = _visatype.ViBoolean()  # case S220
        with self._func_lock:
            if self.niDigital_IsSiteEnabled_cfunc is None:
                self.niDigital_IsSiteEnabled_cfunc = self._get_library_function('niDigital_IsSiteEnabled')
                self.niDigital_IsSiteEnabled_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niDigital_IsSiteEnabled_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_IsSiteEnabled_cfunc(vi_ctype, site_ctype, None if enable_ctype is None else (ctypes.pointer(enable_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(enable_ctype.value)

    def _load_levels(self, session, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(session._encoding))  # case C020
        with self._func_lock:
            if self.niDigital_LoadLevels_cfunc is None:
                self.niDigital_LoadLevels_cfunc = self._get_library_function('niDigital_LoadLevels')
                self.niDigital_LoadLevels_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_LoadLevels_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_LoadLevels_cfunc(vi_ctype, file_path_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def load_pattern(self, session, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(session._encoding))  # case C020
        with self._func_lock:
            if self.niDigital_LoadPattern_cfunc is None:
                self.niDigital_LoadPattern_cfunc = self._get_library_function('niDigital_LoadPattern')
                self.niDigital_LoadPattern_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_LoadPattern_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_LoadPattern_cfunc(vi_ctype, file_path_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def load_pin_map(self, session, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(session._encoding))  # case C020
        with self._func_lock:
            if self.niDigital_LoadPinMap_cfunc is None:
                self.niDigital_LoadPinMap_cfunc = self._get_library_function('niDigital_LoadPinMap')
                self.niDigital_LoadPinMap_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_LoadPinMap_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_LoadPinMap_cfunc(vi_ctype, file_path_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _load_specifications(self, session, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(session._encoding))  # case C020
        with self._func_lock:
            if self.niDigital_LoadSpecifications_cfunc is None:
                self.niDigital_LoadSpecifications_cfunc = self._get_library_function('niDigital_LoadSpecifications')
                self.niDigital_LoadSpecifications_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_LoadSpecifications_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_LoadSpecifications_cfunc(vi_ctype, file_path_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _load_timing(self, session, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(session._encoding))  # case C020
        with self._func_lock:
            if self.niDigital_LoadTiming_cfunc is None:
                self.niDigital_LoadTiming_cfunc = self._get_library_function('niDigital_LoadTiming')
                self.niDigital_LoadTiming_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_LoadTiming_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_LoadTiming_cfunc(vi_ctype, file_path_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def lock(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        caller_has_lock_ctype = _visatype.ViBoolean()  # case S220
        with self._func_lock:
            if self.niDigital_LockSession_cfunc is None:
                self.niDigital_LockSession_cfunc = self._get_library_function('niDigital_LockSession')
                self.niDigital_LockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niDigital_LockSession_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_LockSession_cfunc(vi_ctype, None if caller_has_lock_ctype is None else (ctypes.pointer(caller_has_lock_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(caller_has_lock_ctype.value)

    def ppmu_measure(self, session, channel_list, measurement_type):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(session._encoding))  # case C010
        measurement_type_ctype = _visatype.ViInt32(measurement_type.value)  # case S130
        buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        measurements_ctype = None  # case B610
        actual_num_read_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niDigital_PPMU_Measure_cfunc is None:
                self.niDigital_PPMU_Measure_cfunc = self._get_library_function('niDigital_PPMU_Measure')
                self.niDigital_PPMU_Measure_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDigital_PPMU_Measure_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_PPMU_Measure_cfunc(vi_ctype, channel_list_ctype, measurement_type_ctype, buffer_size_ctype, measurements_ctype, None if actual_num_read_ctype is None else (ctypes.pointer(actual_num_read_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(actual_num_read_ctype.value)  # case S200
        measurements_size = actual_num_read_ctype.value  # case B620
        measurements_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=measurements_size)  # case B620
        error_code = self.niDigital_PPMU_Measure_cfunc(vi_ctype, channel_list_ctype, measurement_type_ctype, buffer_size_ctype, measurements_ctype, None if actual_num_read_ctype is None else (ctypes.pointer(actual_num_read_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(measurements_ctype[i]) for i in range(buffer_size_ctype.value)]

    def ppmu_source(self, session, channel_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(session._encoding))  # case C010
        with self._func_lock:
            if self.niDigital_PPMU_Source_cfunc is None:
                self.niDigital_PPMU_Source_cfunc = self._get_library_function('niDigital_PPMU_Source')
                self.niDigital_PPMU_Source_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_PPMU_Source_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_PPMU_Source_cfunc(vi_ctype, channel_list_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def read_sequencer_flag(self, session, flag):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        flag_ctype = ctypes.create_string_buffer(flag.value.encode(session._encoding))  # case C030
        value_ctype = _visatype.ViBoolean()  # case S220
        with self._func_lock:
            if self.niDigital_ReadSequencerFlag_cfunc is None:
                self.niDigital_ReadSequencerFlag_cfunc = self._get_library_function('niDigital_ReadSequencerFlag')
                self.niDigital_ReadSequencerFlag_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niDigital_ReadSequencerFlag_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_ReadSequencerFlag_cfunc(vi_ctype, flag_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(value_ctype.value)

    def read_sequencer_register(self, session, reg):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        reg_ctype = ctypes.create_string_buffer(reg.value.encode(session._encoding))  # case C030
        value_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niDigital_ReadSequencerRegister_cfunc is None:
                self.niDigital_ReadSequencerRegister_cfunc = self._get_library_function('niDigital_ReadSequencerRegister')
                self.niDigital_ReadSequencerRegister_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDigital_ReadSequencerRegister_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_ReadSequencerRegister_cfunc(vi_ctype, reg_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(value_ctype.value)

    def read_static(self, session, channel_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(session._encoding))  # case C010
        buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        data_ctype = None  # case B610
        actual_num_read_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niDigital_ReadStatic_cfunc is None:
                self.niDigital_ReadStatic_cfunc = self._get_library_function('niDigital_ReadStatic')
                self.niDigital_ReadStatic_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViUInt8), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDigital_ReadStatic_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_ReadStatic_cfunc(vi_ctype, channel_list_ctype, buffer_size_ctype, data_ctype, None if actual_num_read_ctype is None else (ctypes.pointer(actual_num_read_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(actual_num_read_ctype.value)  # case S200
        data_size = actual_num_read_ctype.value  # case B620
        data_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViUInt8, size=data_size)  # case B620
        error_code = self.niDigital_ReadStatic_cfunc(vi_ctype, channel_list_ctype, buffer_size_ctype, data_ctype, None if actual_num_read_ctype is None else (ctypes.pointer(actual_num_read_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return [enums.PinState(data_ctype[i]) for i in range(buffer_size_ctype.value)]

    def reset_device(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niDigital_ResetDevice_cfunc is None:
                self.niDigital_ResetDevice_cfunc = self._get_library_function('niDigital_ResetDevice')
                self.niDigital_ResetDevice_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDigital_ResetDevice_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_ResetDevice_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def self_calibrate(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niDigital_SelfCalibrate_cfunc is None:
                self.niDigital_SelfCalibrate_cfunc = self._get_library_function('niDigital_SelfCalibrate')
                self.niDigital_SelfCalibrate_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDigital_SelfCalibrate_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_SelfCalibrate_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def send_software_edge_trigger(self, session, trigger, trigger_identifier):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        trigger_ctype = _visatype.ViInt32(trigger.value)  # case S130
        trigger_identifier_ctype = ctypes.create_string_buffer(trigger_identifier.encode(session._encoding))  # case C020
        with self._func_lock:
            if self.niDigital_SendSoftwareEdgeTrigger_cfunc is None:
                self.niDigital_SendSoftwareEdgeTrigger_cfunc = self._get_library_function('niDigital_SendSoftwareEdgeTrigger')
                self.niDigital_SendSoftwareEdgeTrigger_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_SendSoftwareEdgeTrigger_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_SendSoftwareEdgeTrigger_cfunc(vi_ctype, trigger_ctype, trigger_identifier_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_boolean(self, session, channel_name, attribute, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViBoolean(value)  # case S150
        with self._func_lock:
            if self.niDigital_SetAttributeViBoolean_cfunc is None:
                self.niDigital_SetAttributeViBoolean_cfunc = self._get_library_function('niDigital_SetAttributeViBoolean')
                self.niDigital_SetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViBoolean]  # noqa: F405
                self.niDigital_SetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_SetAttributeViBoolean_cfunc(vi_ctype, channel_name_ctype, attribute_ctype, value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_int32(self, session, channel_name, attribute, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViInt32(value)  # case S150
        with self._func_lock:
            if self.niDigital_SetAttributeViInt32_cfunc is None:
                self.niDigital_SetAttributeViInt32_cfunc = self._get_library_function('niDigital_SetAttributeViInt32')
                self.niDigital_SetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32]  # noqa: F405
                self.niDigital_SetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_SetAttributeViInt32_cfunc(vi_ctype, channel_name_ctype, attribute_ctype, value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_int64(self, session, channel_name, attribute, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViInt64(value)  # case S150
        with self._func_lock:
            if self.niDigital_SetAttributeViInt64_cfunc is None:
                self.niDigital_SetAttributeViInt64_cfunc = self._get_library_function('niDigital_SetAttributeViInt64')
                self.niDigital_SetAttributeViInt64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt64]  # noqa: F405
                self.niDigital_SetAttributeViInt64_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_SetAttributeViInt64_cfunc(vi_ctype, channel_name_ctype, attribute_ctype, value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_real64(self, session, channel_name, attribute, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViReal64(value)  # case S150
        with self._func_lock:
            if self.niDigital_SetAttributeViReal64_cfunc is None:
                self.niDigital_SetAttributeViReal64_cfunc = self._get_library_function('niDigital_SetAttributeViReal64')
                self.niDigital_SetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViReal64]  # noqa: F405
                self.niDigital_SetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_SetAttributeViReal64_cfunc(vi_ctype, channel_name_ctype, attribute_ctype, value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_string(self, session, channel_name, attribute, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = ctypes.create_string_buffer(value.encode(session._encoding))  # case C020
        with self._func_lock:
            if self.niDigital_SetAttributeViString_cfunc is None:
                self.niDigital_SetAttributeViString_cfunc = self._get_library_function('niDigital_SetAttributeViString')
                self.niDigital_SetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_SetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_SetAttributeViString_cfunc(vi_ctype, channel_name_ctype, attribute_ctype, value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def tdr(self, session, channel_list, apply_offsets=True):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(session._encoding))  # case C010
        apply_offsets_ctype = _visatype.ViBoolean(apply_offsets)  # case S150
        offsets_buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        offsets_ctype = None  # case B610
        actual_num_offsets_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niDigital_TDR_cfunc is None:
                self.niDigital_TDR_cfunc = self._get_library_function('niDigital_TDR')
                self.niDigital_TDR_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViBoolean, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDigital_TDR_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_TDR_cfunc(vi_ctype, channel_list_ctype, apply_offsets_ctype, offsets_buffer_size_ctype, offsets_ctype, None if actual_num_offsets_ctype is None else (ctypes.pointer(actual_num_offsets_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=False)
        offsets_buffer_size_ctype = _visatype.ViInt32(actual_num_offsets_ctype.value)  # case S200
        offsets_size = actual_num_offsets_ctype.value  # case B620
        offsets_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=offsets_size)  # case B620
        error_code = self.niDigital_TDR_cfunc(vi_ctype, channel_list_ctype, apply_offsets_ctype, offsets_buffer_size_ctype, offsets_ctype, None if actual_num_offsets_ctype is None else (ctypes.pointer(actual_num_offsets_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return _converters.convert_seconds_real64_to_timedeltas([float(offsets_ctype[i]) for i in range(offsets_buffer_size_ctype.value)])

    def unload_all_patterns(self, session, unload_keep_alive_pattern=False):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        unload_keep_alive_pattern_ctype = _visatype.ViBoolean(unload_keep_alive_pattern)  # case S150
        with self._func_lock:
            if self.niDigital_UnloadAllPatterns_cfunc is None:
                self.niDigital_UnloadAllPatterns_cfunc = self._get_library_function('niDigital_UnloadAllPatterns')
                self.niDigital_UnloadAllPatterns_cfunc.argtypes = [ViSession, ViBoolean]  # noqa: F405
                self.niDigital_UnloadAllPatterns_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_UnloadAllPatterns_cfunc(vi_ctype, unload_keep_alive_pattern_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _unload_specifications(self, session, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(session._encoding))  # case C020
        with self._func_lock:
            if self.niDigital_UnloadSpecifications_cfunc is None:
                self.niDigital_UnloadSpecifications_cfunc = self._get_library_function('niDigital_UnloadSpecifications')
                self.niDigital_UnloadSpecifications_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_UnloadSpecifications_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_UnloadSpecifications_cfunc(vi_ctype, file_path_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def unlock(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        caller_has_lock_ctype = _visatype.ViBoolean()  # case S220
        with self._func_lock:
            if self.niDigital_UnlockSession_cfunc is None:
                self.niDigital_UnlockSession_cfunc = self._get_library_function('niDigital_UnlockSession')
                self.niDigital_UnlockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niDigital_UnlockSession_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_UnlockSession_cfunc(vi_ctype, None if caller_has_lock_ctype is None else (ctypes.pointer(caller_has_lock_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(caller_has_lock_ctype.value)

    def wait_until_done(self, session, timeout=hightime.timedelta(seconds=10.0)):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        timeout_ctype = _converters.convert_timedelta_to_seconds_real64(timeout)  # case S140
        with self._func_lock:
            if self.niDigital_WaitUntilDone_cfunc is None:
                self.niDigital_WaitUntilDone_cfunc = self._get_library_function('niDigital_WaitUntilDone')
                self.niDigital_WaitUntilDone_cfunc.argtypes = [ViSession, ViReal64]  # noqa: F405
                self.niDigital_WaitUntilDone_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_WaitUntilDone_cfunc(vi_ctype, timeout_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def write_sequencer_flag(self, session, flag, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        flag_ctype = ctypes.create_string_buffer(flag.value.encode(session._encoding))  # case C030
        value_ctype = _visatype.ViBoolean(value)  # case S150
        with self._func_lock:
            if self.niDigital_WriteSequencerFlag_cfunc is None:
                self.niDigital_WriteSequencerFlag_cfunc = self._get_library_function('niDigital_WriteSequencerFlag')
                self.niDigital_WriteSequencerFlag_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViBoolean]  # noqa: F405
                self.niDigital_WriteSequencerFlag_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_WriteSequencerFlag_cfunc(vi_ctype, flag_ctype, value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def write_sequencer_register(self, session, reg, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        reg_ctype = ctypes.create_string_buffer(reg.value.encode(session._encoding))  # case C030
        value_ctype = _visatype.ViInt32(value)  # case S150
        with self._func_lock:
            if self.niDigital_WriteSequencerRegister_cfunc is None:
                self.niDigital_WriteSequencerRegister_cfunc = self._get_library_function('niDigital_WriteSequencerRegister')
                self.niDigital_WriteSequencerRegister_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niDigital_WriteSequencerRegister_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_WriteSequencerRegister_cfunc(vi_ctype, reg_ctype, value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def write_source_waveform_broadcast(self, session, waveform_name, waveform_data):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(session._encoding))  # case C020
        waveform_size_ctype = _visatype.ViInt32(0 if waveform_data is None else len(waveform_data))  # case S160
        waveform_data_ctype = get_ctypes_pointer_for_buffer(value=waveform_data, library_type=_visatype.ViUInt32)  # case B550
        with self._func_lock:
            if self.niDigital_WriteSourceWaveformBroadcastU32_cfunc is None:
                self.niDigital_WriteSourceWaveformBroadcastU32_cfunc = self._get_library_function('niDigital_WriteSourceWaveformBroadcastU32')
                self.niDigital_WriteSourceWaveformBroadcastU32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViUInt32)]  # noqa: F405
                self.niDigital_WriteSourceWaveformBroadcastU32_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_WriteSourceWaveformBroadcastU32_cfunc(vi_ctype, waveform_name_ctype, waveform_size_ctype, waveform_data_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def write_source_waveform_data_from_file_tdms(self, session, waveform_name, waveform_file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(session._encoding))  # case C020
        waveform_file_path_ctype = ctypes.create_string_buffer(waveform_file_path.encode(session._encoding))  # case C020
        with self._func_lock:
            if self.niDigital_WriteSourceWaveformDataFromFileTDMS_cfunc is None:
                self.niDigital_WriteSourceWaveformDataFromFileTDMS_cfunc = self._get_library_function('niDigital_WriteSourceWaveformDataFromFileTDMS')
                self.niDigital_WriteSourceWaveformDataFromFileTDMS_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_WriteSourceWaveformDataFromFileTDMS_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_WriteSourceWaveformDataFromFileTDMS_cfunc(vi_ctype, waveform_name_ctype, waveform_file_path_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _write_source_waveform_site_unique_u32(self, session, site_list, waveform_name, num_waveforms, samples_per_waveform, waveform_data):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(site_list.encode(session._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(session._encoding))  # case C020
        num_waveforms_ctype = _visatype.ViInt32(num_waveforms)  # case S150
        samples_per_waveform_ctype = _visatype.ViInt32(samples_per_waveform)  # case S150
        waveform_data_array = get_ctypes_and_array(value=waveform_data, array_type="L")  # case B550
        waveform_data_ctype = get_ctypes_pointer_for_buffer(value=waveform_data_array, library_type=_visatype.ViUInt32)  # case B550
        with self._func_lock:
            if self.niDigital_WriteSourceWaveformSiteUniqueU32_cfunc is None:
                self.niDigital_WriteSourceWaveformSiteUniqueU32_cfunc = self._get_library_function('niDigital_WriteSourceWaveformSiteUniqueU32')
                self.niDigital_WriteSourceWaveformSiteUniqueU32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ViInt32, ctypes.POINTER(ViUInt32)]  # noqa: F405
                self.niDigital_WriteSourceWaveformSiteUniqueU32_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_WriteSourceWaveformSiteUniqueU32_cfunc(vi_ctype, site_list_ctype, waveform_name_ctype, num_waveforms_ctype, samples_per_waveform_ctype, waveform_data_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def write_static(self, session, channel_list, state):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(session._encoding))  # case C010
        state_ctype = _visatype.ViUInt8(state.value)  # case S130
        with self._func_lock:
            if self.niDigital_WriteStatic_cfunc is None:
                self.niDigital_WriteStatic_cfunc = self._get_library_function('niDigital_WriteStatic')
                self.niDigital_WriteStatic_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViUInt8]  # noqa: F405
                self.niDigital_WriteStatic_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_WriteStatic_cfunc(vi_ctype, channel_list_ctype, state_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _close(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niDigital_close_cfunc is None:
                self.niDigital_close_cfunc = self._get_library_function('niDigital_close')
                self.niDigital_close_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDigital_close_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_close_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _error_message(self, session, error_code):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        error_code_ctype = _visatype.ViStatus(error_code)  # case S150
        error_message_ctype = (_visatype.ViChar * 256)()  # case C070
        with self._func_lock:
            if self.niDigital_error_message_cfunc is None:
                self.niDigital_error_message_cfunc = self._get_library_function('niDigital_error_message')
                self.niDigital_error_message_cfunc.argtypes = [ViSession, ViStatus, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_error_message_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_error_message_cfunc(vi_ctype, error_code_ctype, error_message_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=True)
        return error_message_ctype.value.decode(session._encoding)

    def reset(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niDigital_reset_cfunc is None:
                self.niDigital_reset_cfunc = self._get_library_function('niDigital_reset')
                self.niDigital_reset_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDigital_reset_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_reset_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _self_test(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        test_result_ctype = _visatype.ViInt16()  # case S220
        test_message_ctype = (_visatype.ViChar * 2048)()  # case C070
        with self._func_lock:
            if self.niDigital_self_test_cfunc is None:
                self.niDigital_self_test_cfunc = self._get_library_function('niDigital_self_test')
                self.niDigital_self_test_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt16), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_self_test_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDigital_self_test_cfunc(vi_ctype, None if test_result_ctype is None else (ctypes.pointer(test_result_ctype)), test_message_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(test_result_ctype.value), test_message_ctype.value.decode(session._encoding)
