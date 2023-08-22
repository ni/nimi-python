# -*- coding: utf-8 -*-
# This file was generated

import array
import ctypes
import hightime  # noqa: F401
import platform

import nidigital._library_singleton as _library_singleton
import nidigital._visatype as _visatype
import nidigital.enums as enums  # noqa: F401
import nidigital.errors as errors

import nidigital.history_ram_cycle_information as history_ram_cycle_information  # noqa: F401


_was_runtime_environment_set = None


# Helper functions for creating ctypes needed for calling into the driver DLL
def _get_ctypes_pointer_for_buffer(value=None, library_type=None, size=None):
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


def _convert_to_array(value, array_type):
    if value is not None:
        if isinstance(value, array.array):
            value_array = value
        else:
            value_array = array.array(array_type, value)
    else:
        value_array = None

    return value_array


class LibraryInterpreter(object):
    '''Library C<->Python interpreter.

    This class is responsible for interpreting the Library's C API. It is responsible for:
    * Converting ctypes to native Python types.
    * Dealing with string encoding.
    * Allocating memory.
    * Converting errors returned by Library into Python exceptions.
    '''

    def __init__(self, encoding):
        self._encoding = encoding
        self._library = _library_singleton.get()
        global _was_runtime_environment_set
        if _was_runtime_environment_set is None:
            try:
                runtime_env = platform.python_implementation()
                version = platform.python_version()
                self.set_runtime_environment(
                    runtime_env,
                    version,
                    '',
                    ''
                )
            except errors.DriverTooOldError:
                pass
            finally:
                _was_runtime_environment_set = True
        # Initialize _vi to 0 for now.
        # Session will directly update it once the driver runtime init function has been called and
        # we have a valid session handle.
        self.set_session_handle()

    def set_session_handle(self, value=0):
        self._vi = value

    def get_session_handle(self):
        return self._vi

    def get_error_description(self, error_code):
        '''get_error_description

        Returns the error description.
        '''
        try:
            returned_error_code, error_string = self.get_error()
            if returned_error_code == error_code:
                return error_string
        except errors.Error:
            pass

        try:
            '''
            It is expected for get_error to raise when the session is invalid
            (IVI spec requires GetError to fail).
            Use error_message instead. It doesn't require a session.
            '''
            error_string = self.error_message(error_code)
            return error_string
        except errors.Error:
            pass
        return "Failed to retrieve error description."

    def abort(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDigital_Abort(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def abort_keep_alive(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDigital_AbortKeepAlive(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def apply_levels_and_timing(self, site_list, levels_sheet, timing_sheet, initial_state_high_pins, initial_state_low_pins, initial_state_tristate_pins):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(site_list.encode(self._encoding))  # case C010
        levels_sheet_ctype = ctypes.create_string_buffer(levels_sheet.encode(self._encoding))  # case C020
        timing_sheet_ctype = ctypes.create_string_buffer(timing_sheet.encode(self._encoding))  # case C020
        initial_state_high_pins_ctype = ctypes.create_string_buffer(initial_state_high_pins.encode(self._encoding))  # case C020
        initial_state_low_pins_ctype = ctypes.create_string_buffer(initial_state_low_pins.encode(self._encoding))  # case C020
        initial_state_tristate_pins_ctype = ctypes.create_string_buffer(initial_state_tristate_pins.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_ApplyLevelsAndTiming(vi_ctype, site_list_ctype, levels_sheet_ctype, timing_sheet_ctype, initial_state_high_pins_ctype, initial_state_low_pins_ctype, initial_state_tristate_pins_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def apply_tdr_offsets(self, channel_list, offsets):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        num_offsets_ctype = _visatype.ViInt32(0 if offsets is None else len(offsets))  # case S160
        offsets_ctype = _get_ctypes_pointer_for_buffer(value=offsets, library_type=_visatype.ViReal64)  # case B550
        error_code = self._library.niDigital_ApplyTDROffsets(vi_ctype, channel_list_ctype, num_offsets_ctype, offsets_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def burst_pattern(self, site_list, start_label, select_digital_function, wait_until_done, timeout):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(site_list.encode(self._encoding))  # case C010
        start_label_ctype = ctypes.create_string_buffer(start_label.encode(self._encoding))  # case C020
        select_digital_function_ctype = _visatype.ViBoolean(select_digital_function)  # case S150
        wait_until_done_ctype = _visatype.ViBoolean(wait_until_done)  # case S150
        timeout_ctype = _visatype.ViReal64(timeout)  # case S150
        error_code = self._library.niDigital_BurstPattern(vi_ctype, site_list_ctype, start_label_ctype, select_digital_function_ctype, wait_until_done_ctype, timeout_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def clock_generator_abort(self, channel_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        error_code = self._library.niDigital_ClockGenerator_Abort(vi_ctype, channel_list_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def clock_generator_generate_clock(self, channel_list, frequency, select_digital_function):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        frequency_ctype = _visatype.ViReal64(frequency)  # case S150
        select_digital_function_ctype = _visatype.ViBoolean(select_digital_function)  # case S150
        error_code = self._library.niDigital_ClockGenerator_GenerateClock(vi_ctype, channel_list_ctype, frequency_ctype, select_digital_function_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def commit(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDigital_Commit(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_active_load_levels(self, channel_list, iol, ioh, vcom):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        iol_ctype = _visatype.ViReal64(iol)  # case S150
        ioh_ctype = _visatype.ViReal64(ioh)  # case S150
        vcom_ctype = _visatype.ViReal64(vcom)  # case S150
        error_code = self._library.niDigital_ConfigureActiveLoadLevels(vi_ctype, channel_list_ctype, iol_ctype, ioh_ctype, vcom_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_pattern_burst_sites(self, site_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(site_list.encode(self._encoding))  # case C010
        error_code = self._library.niDigital_ConfigurePatternBurstSites(vi_ctype, site_list_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_time_set_compare_edges_strobe(self, pin_list, time_set_name, strobe_edge):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(pin_list.encode(self._encoding))  # case C010
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(self._encoding))  # case C020
        strobe_edge_ctype = _visatype.ViReal64(strobe_edge)  # case S150
        error_code = self._library.niDigital_ConfigureTimeSetCompareEdgesStrobe(vi_ctype, pin_list_ctype, time_set_name_ctype, strobe_edge_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_time_set_compare_edges_strobe2x(self, pin_list, time_set_name, strobe_edge, strobe2_edge):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(pin_list.encode(self._encoding))  # case C010
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(self._encoding))  # case C020
        strobe_edge_ctype = _visatype.ViReal64(strobe_edge)  # case S150
        strobe2_edge_ctype = _visatype.ViReal64(strobe2_edge)  # case S150
        error_code = self._library.niDigital_ConfigureTimeSetCompareEdgesStrobe2x(vi_ctype, pin_list_ctype, time_set_name_ctype, strobe_edge_ctype, strobe2_edge_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_time_set_drive_edges(self, pin_list, time_set_name, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(pin_list.encode(self._encoding))  # case C010
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(self._encoding))  # case C020
        format_ctype = _visatype.ViInt32(format.value)  # case S130
        drive_on_edge_ctype = _visatype.ViReal64(drive_on_edge)  # case S150
        drive_data_edge_ctype = _visatype.ViReal64(drive_data_edge)  # case S150
        drive_return_edge_ctype = _visatype.ViReal64(drive_return_edge)  # case S150
        drive_off_edge_ctype = _visatype.ViReal64(drive_off_edge)  # case S150
        error_code = self._library.niDigital_ConfigureTimeSetDriveEdges(vi_ctype, pin_list_ctype, time_set_name_ctype, format_ctype, drive_on_edge_ctype, drive_data_edge_ctype, drive_return_edge_ctype, drive_off_edge_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_time_set_drive_edges2x(self, pin_list, time_set_name, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge, drive_data2_edge, drive_return2_edge):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(pin_list.encode(self._encoding))  # case C010
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(self._encoding))  # case C020
        format_ctype = _visatype.ViInt32(format.value)  # case S130
        drive_on_edge_ctype = _visatype.ViReal64(drive_on_edge)  # case S150
        drive_data_edge_ctype = _visatype.ViReal64(drive_data_edge)  # case S150
        drive_return_edge_ctype = _visatype.ViReal64(drive_return_edge)  # case S150
        drive_off_edge_ctype = _visatype.ViReal64(drive_off_edge)  # case S150
        drive_data2_edge_ctype = _visatype.ViReal64(drive_data2_edge)  # case S150
        drive_return2_edge_ctype = _visatype.ViReal64(drive_return2_edge)  # case S150
        error_code = self._library.niDigital_ConfigureTimeSetDriveEdges2x(vi_ctype, pin_list_ctype, time_set_name_ctype, format_ctype, drive_on_edge_ctype, drive_data_edge_ctype, drive_return_edge_ctype, drive_off_edge_ctype, drive_data2_edge_ctype, drive_return2_edge_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_time_set_drive_format(self, pin_list, time_set_name, drive_format):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(pin_list.encode(self._encoding))  # case C010
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(self._encoding))  # case C020
        drive_format_ctype = _visatype.ViInt32(drive_format.value)  # case S130
        error_code = self._library.niDigital_ConfigureTimeSetDriveFormat(vi_ctype, pin_list_ctype, time_set_name_ctype, drive_format_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_time_set_edge(self, pin_list, time_set_name, edge, time):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(pin_list.encode(self._encoding))  # case C010
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(self._encoding))  # case C020
        edge_ctype = _visatype.ViInt32(edge.value)  # case S130
        time_ctype = _visatype.ViReal64(time)  # case S150
        error_code = self._library.niDigital_ConfigureTimeSetEdge(vi_ctype, pin_list_ctype, time_set_name_ctype, edge_ctype, time_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_time_set_edge_multiplier(self, pin_list, time_set_name, edge_multiplier):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(pin_list.encode(self._encoding))  # case C010
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(self._encoding))  # case C020
        edge_multiplier_ctype = _visatype.ViInt32(edge_multiplier)  # case S150
        error_code = self._library.niDigital_ConfigureTimeSetEdgeMultiplier(vi_ctype, pin_list_ctype, time_set_name_ctype, edge_multiplier_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_time_set_period(self, time_set_name, period):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(self._encoding))  # case C020
        period_ctype = _visatype.ViReal64(period)  # case S150
        error_code = self._library.niDigital_ConfigureTimeSetPeriod(vi_ctype, time_set_name_ctype, period_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_voltage_levels(self, channel_list, vil, vih, vol, voh, vterm):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        vil_ctype = _visatype.ViReal64(vil)  # case S150
        vih_ctype = _visatype.ViReal64(vih)  # case S150
        vol_ctype = _visatype.ViReal64(vol)  # case S150
        voh_ctype = _visatype.ViReal64(voh)  # case S150
        vterm_ctype = _visatype.ViReal64(vterm)  # case S150
        error_code = self._library.niDigital_ConfigureVoltageLevels(vi_ctype, channel_list_ctype, vil_ctype, vih_ctype, vol_ctype, voh_ctype, vterm_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_capture_waveform_from_file_digicapture(self, waveform_name, waveform_file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        waveform_file_path_ctype = ctypes.create_string_buffer(waveform_file_path.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_CreateCaptureWaveformFromFileDigicapture(vi_ctype, waveform_name_ctype, waveform_file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_capture_waveform_parallel(self, pin_list, waveform_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(pin_list.encode(self._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_CreateCaptureWaveformParallel(vi_ctype, pin_list_ctype, waveform_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_capture_waveform_serial(self, pin_list, waveform_name, sample_width, bit_order):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(pin_list.encode(self._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        sample_width_ctype = _visatype.ViUInt32(sample_width)  # case S150
        bit_order_ctype = _visatype.ViInt32(bit_order.value)  # case S130
        error_code = self._library.niDigital_CreateCaptureWaveformSerial(vi_ctype, pin_list_ctype, waveform_name_ctype, sample_width_ctype, bit_order_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_source_waveform_from_file_tdms(self, waveform_name, waveform_file_path, write_waveform_data):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        waveform_file_path_ctype = ctypes.create_string_buffer(waveform_file_path.encode(self._encoding))  # case C020
        write_waveform_data_ctype = _visatype.ViBoolean(write_waveform_data)  # case S150
        error_code = self._library.niDigital_CreateSourceWaveformFromFileTDMS(vi_ctype, waveform_name_ctype, waveform_file_path_ctype, write_waveform_data_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_source_waveform_parallel(self, pin_list, waveform_name, data_mapping):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(pin_list.encode(self._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        data_mapping_ctype = _visatype.ViInt32(data_mapping.value)  # case S130
        error_code = self._library.niDigital_CreateSourceWaveformParallel(vi_ctype, pin_list_ctype, waveform_name_ctype, data_mapping_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_source_waveform_serial(self, pin_list, waveform_name, data_mapping, sample_width, bit_order):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(pin_list.encode(self._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        data_mapping_ctype = _visatype.ViInt32(data_mapping.value)  # case S130
        sample_width_ctype = _visatype.ViUInt32(sample_width)  # case S150
        bit_order_ctype = _visatype.ViInt32(bit_order.value)  # case S130
        error_code = self._library.niDigital_CreateSourceWaveformSerial(vi_ctype, pin_list_ctype, waveform_name_ctype, data_mapping_ctype, sample_width_ctype, bit_order_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_time_set(self, name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        name_ctype = ctypes.create_string_buffer(name.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_CreateTimeSet(vi_ctype, name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def delete_all_time_sets(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDigital_DeleteAllTimeSets(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disable_sites(self, site_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(site_list.encode(self._encoding))  # case C010
        error_code = self._library.niDigital_DisableSites(vi_ctype, site_list_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def enable_sites(self, site_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(site_list.encode(self._encoding))  # case C010
        error_code = self._library.niDigital_EnableSites(vi_ctype, site_list_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def fetch_capture_waveform(self, site_list, waveform_name, samples_to_read, timeout):
        # This is slightly modified codegen from the function
        # We cannot use codegen without major modifications to the code generator
        # This function uses two 'ivi-dance' parameters and then multiplies them together - see
        # the (modified) line below
        # Also, we want to return the two sizes that normally wouldn't be returned
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(site_list.encode(self._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        samples_to_read_ctype = _visatype.ViInt32(samples_to_read)  # case S150
        timeout_ctype = _visatype.ViReal64(timeout)  # case S150
        data_buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        data_ctype = None  # case B610
        actual_num_waveforms_ctype = _visatype.ViInt32()  # case S220
        actual_samples_per_waveform_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_FetchCaptureWaveformU32(vi_ctype, site_list_ctype, waveform_name_ctype, samples_to_read_ctype, timeout_ctype, data_buffer_size_ctype, data_ctype, None if actual_num_waveforms_ctype is None else (ctypes.pointer(actual_num_waveforms_ctype)), None if actual_samples_per_waveform_ctype is None else (ctypes.pointer(actual_samples_per_waveform_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        data_buffer_size_ctype = _visatype.ViInt32(actual_num_waveforms_ctype.value * actual_samples_per_waveform_ctype.value)  # case S200 (modified)
        data_size = actual_num_waveforms_ctype.value * actual_samples_per_waveform_ctype.value  # case B620 (modified)
        data_array = array.array("L", [0]) * data_size  # case B620
        data_ctype = _get_ctypes_pointer_for_buffer(value=data_array, library_type=_visatype.ViUInt32)  # case B620
        error_code = self._library.niDigital_FetchCaptureWaveformU32(vi_ctype, site_list_ctype, waveform_name_ctype, samples_to_read_ctype, timeout_ctype, data_buffer_size_ctype, data_ctype, None if actual_num_waveforms_ctype is None else (ctypes.pointer(actual_num_waveforms_ctype)), None if actual_samples_per_waveform_ctype is None else (ctypes.pointer(actual_samples_per_waveform_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return data_array, actual_num_waveforms_ctype.value, actual_samples_per_waveform_ctype.value  # (modified)

    def fetch_history_ram_cycle_information(self, site, sample_index):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_ctype = ctypes.create_string_buffer(site.encode(self._encoding))  # case C010
        sample_index_ctype = _visatype.ViInt64(sample_index)  # case S150
        pattern_index_ctype = _visatype.ViInt32()  # case S220
        time_set_index_ctype = _visatype.ViInt32()  # case S220
        vector_number_ctype = _visatype.ViInt64()  # case S220
        cycle_number_ctype = _visatype.ViInt64()  # case S220
        num_dut_cycles_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_FetchHistoryRAMCycleInformation(vi_ctype, site_ctype, sample_index_ctype, None if pattern_index_ctype is None else (ctypes.pointer(pattern_index_ctype)), None if time_set_index_ctype is None else (ctypes.pointer(time_set_index_ctype)), None if vector_number_ctype is None else (ctypes.pointer(vector_number_ctype)), None if cycle_number_ctype is None else (ctypes.pointer(cycle_number_ctype)), None if num_dut_cycles_ctype is None else (ctypes.pointer(num_dut_cycles_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(pattern_index_ctype.value), int(time_set_index_ctype.value), int(vector_number_ctype.value), int(cycle_number_ctype.value), int(num_dut_cycles_ctype.value)

    def fetch_history_ram_cycle_pin_data(self, site, pin_list, sample_index, dut_cycle_index):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_ctype = ctypes.create_string_buffer(site.encode(self._encoding))  # case C010
        pin_list_ctype = ctypes.create_string_buffer(pin_list.encode(self._encoding))  # case C020
        sample_index_ctype = _visatype.ViInt64(sample_index)  # case S150
        dut_cycle_index_ctype = _visatype.ViInt32(dut_cycle_index)  # case S150
        pin_data_buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        expected_pin_states_ctype = None  # case B610
        actual_pin_states_ctype = None  # case B610
        per_pin_pass_fail_ctype = None  # case B610
        actual_num_pin_data_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_FetchHistoryRAMCyclePinData(vi_ctype, site_ctype, pin_list_ctype, sample_index_ctype, dut_cycle_index_ctype, pin_data_buffer_size_ctype, expected_pin_states_ctype, actual_pin_states_ctype, per_pin_pass_fail_ctype, None if actual_num_pin_data_ctype is None else (ctypes.pointer(actual_num_pin_data_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        pin_data_buffer_size_ctype = _visatype.ViInt32(actual_num_pin_data_ctype.value)  # case S200
        expected_pin_states_size = actual_num_pin_data_ctype.value  # case B620
        expected_pin_states_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViUInt8, size=expected_pin_states_size)  # case B620
        actual_pin_states_size = actual_num_pin_data_ctype.value  # case B620
        actual_pin_states_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViUInt8, size=actual_pin_states_size)  # case B620
        per_pin_pass_fail_size = actual_num_pin_data_ctype.value  # case B620
        per_pin_pass_fail_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViBoolean, size=per_pin_pass_fail_size)  # case B620
        error_code = self._library.niDigital_FetchHistoryRAMCyclePinData(vi_ctype, site_ctype, pin_list_ctype, sample_index_ctype, dut_cycle_index_ctype, pin_data_buffer_size_ctype, expected_pin_states_ctype, actual_pin_states_ctype, per_pin_pass_fail_ctype, None if actual_num_pin_data_ctype is None else (ctypes.pointer(actual_num_pin_data_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [enums.PinState(expected_pin_states_ctype[i]) for i in range(pin_data_buffer_size_ctype.value)], [enums.PinState(actual_pin_states_ctype[i]) for i in range(pin_data_buffer_size_ctype.value)], [bool(per_pin_pass_fail_ctype[i]) for i in range(pin_data_buffer_size_ctype.value)]

    def fetch_history_ram_scan_cycle_number(self, site, sample_index):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_ctype = ctypes.create_string_buffer(site.encode(self._encoding))  # case C010
        sample_index_ctype = _visatype.ViInt64(sample_index)  # case S150
        scan_cycle_number_ctype = _visatype.ViInt64()  # case S220
        error_code = self._library.niDigital_FetchHistoryRAMScanCycleNumber(vi_ctype, site_ctype, sample_index_ctype, None if scan_cycle_number_ctype is None else (ctypes.pointer(scan_cycle_number_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(scan_cycle_number_ctype.value)

    def frequency_counter_measure_frequency(self, channel_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        frequencies_buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        frequencies_ctype = None  # case B610
        actual_num_frequencies_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_FrequencyCounter_MeasureFrequency(vi_ctype, channel_list_ctype, frequencies_buffer_size_ctype, frequencies_ctype, None if actual_num_frequencies_ctype is None else (ctypes.pointer(actual_num_frequencies_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        frequencies_buffer_size_ctype = _visatype.ViInt32(actual_num_frequencies_ctype.value)  # case S200
        frequencies_size = actual_num_frequencies_ctype.value  # case B620
        frequencies_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=frequencies_size)  # case B620
        error_code = self._library.niDigital_FrequencyCounter_MeasureFrequency(vi_ctype, channel_list_ctype, frequencies_buffer_size_ctype, frequencies_ctype, None if actual_num_frequencies_ctype is None else (ctypes.pointer(actual_num_frequencies_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(frequencies_ctype[i]) for i in range(frequencies_buffer_size_ctype.value)]

    def get_attribute_vi_boolean(self, channel_name, attribute):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niDigital_GetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(value_ctype.value)

    def get_attribute_vi_int32(self, channel_name, attribute):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_GetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(value_ctype.value)

    def get_attribute_vi_int64(self, channel_name, attribute):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViInt64()  # case S220
        error_code = self._library.niDigital_GetAttributeViInt64(vi_ctype, channel_name_ctype, attribute_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(value_ctype.value)

    def get_attribute_vi_real64(self, channel_name, attribute):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDigital_GetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(value_ctype.value)

    def get_attribute_vi_string(self, channel_name, attribute):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        value_ctype = None  # case C050
        error_code = self._library.niDigital_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_ctype, buffer_size_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        value_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niDigital_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_ctype, buffer_size_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return value_ctype.value.decode(self._encoding)

    def get_channel_names(self, indices):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        indices_ctype = ctypes.create_string_buffer(indices.encode(self._encoding))  # case C020
        name_buffer_size_ctype = _visatype.ViInt32()  # case S170
        names_ctype = None  # case C050
        error_code = self._library.niDigital_GetChannelNameFromString(vi_ctype, indices_ctype, name_buffer_size_ctype, names_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        name_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        names_ctype = (_visatype.ViChar * name_buffer_size_ctype.value)()  # case C060
        error_code = self._library.niDigital_GetChannelNameFromString(vi_ctype, indices_ctype, name_buffer_size_ctype, names_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return names_ctype.value.decode(self._encoding)

    def get_error(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code_ctype = _visatype.ViStatus()  # case S220
        error_description_buffer_size_ctype = _visatype.ViInt32()  # case S170
        error_description_ctype = None  # case C050
        error_code = self._library.niDigital_GetError(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), error_description_buffer_size_ctype, error_description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=True)
        error_description_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        error_description_ctype = (_visatype.ViChar * error_description_buffer_size_ctype.value)()  # case C060
        error_code = self._library.niDigital_GetError(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), error_description_buffer_size_ctype, error_description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return int(error_code_ctype.value), error_description_ctype.value.decode(self._encoding)

    def get_fail_count(self, channel_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        failure_count_ctype = None  # case B610
        actual_num_read_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_GetFailCount(vi_ctype, channel_list_ctype, buffer_size_ctype, failure_count_ctype, None if actual_num_read_ctype is None else (ctypes.pointer(actual_num_read_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(actual_num_read_ctype.value)  # case S200
        failure_count_size = actual_num_read_ctype.value  # case B620
        failure_count_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViInt64, size=failure_count_size)  # case B620
        error_code = self._library.niDigital_GetFailCount(vi_ctype, channel_list_ctype, buffer_size_ctype, failure_count_ctype, None if actual_num_read_ctype is None else (ctypes.pointer(actual_num_read_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [int(failure_count_ctype[i]) for i in range(buffer_size_ctype.value)]

    def get_history_ram_sample_count(self, site):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_ctype = ctypes.create_string_buffer(site.encode(self._encoding))  # case C010
        sample_count_ctype = _visatype.ViInt64()  # case S220
        error_code = self._library.niDigital_GetHistoryRAMSampleCount(vi_ctype, site_ctype, None if sample_count_ctype is None else (ctypes.pointer(sample_count_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(sample_count_ctype.value)

    def get_pattern_name(self, pattern_index):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pattern_index_ctype = _visatype.ViInt32(pattern_index)  # case S150
        name_buffer_size_ctype = _visatype.ViInt32()  # case S170
        name_ctype = None  # case C050
        error_code = self._library.niDigital_GetPatternName(vi_ctype, pattern_index_ctype, name_buffer_size_ctype, name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        name_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        name_ctype = (_visatype.ViChar * name_buffer_size_ctype.value)()  # case C060
        error_code = self._library.niDigital_GetPatternName(vi_ctype, pattern_index_ctype, name_buffer_size_ctype, name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return name_ctype.value.decode(self._encoding)

    def get_pattern_pin_names(self, start_label):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        start_label_ctype = ctypes.create_string_buffer(start_label.encode(self._encoding))  # case C020
        pin_list_buffer_size_ctype = _visatype.ViInt32()  # case S170
        pin_list_ctype = None  # case C050
        error_code = self._library.niDigital_GetPatternPinList(vi_ctype, start_label_ctype, pin_list_buffer_size_ctype, pin_list_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        pin_list_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        pin_list_ctype = (_visatype.ViChar * pin_list_buffer_size_ctype.value)()  # case C060
        error_code = self._library.niDigital_GetPatternPinList(vi_ctype, start_label_ctype, pin_list_buffer_size_ctype, pin_list_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return pin_list_ctype.value.decode(self._encoding)

    def get_pin_name(self, pin_index):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_index_ctype = _visatype.ViInt32(pin_index)  # case S150
        name_buffer_size_ctype = _visatype.ViInt32()  # case S170
        name_ctype = None  # case C050
        error_code = self._library.niDigital_GetPinName(vi_ctype, pin_index_ctype, name_buffer_size_ctype, name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        name_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        name_ctype = (_visatype.ViChar * name_buffer_size_ctype.value)()  # case C060
        error_code = self._library.niDigital_GetPinName(vi_ctype, pin_index_ctype, name_buffer_size_ctype, name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return name_ctype.value.decode(self._encoding)

    def get_pin_results_pin_information(self, channel_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        pin_indexes_ctype = None  # case B610
        site_numbers_ctype = None  # case B610
        channel_indexes_ctype = None  # case B610
        actual_num_values_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_GetPinResultsPinInformation(vi_ctype, channel_list_ctype, buffer_size_ctype, pin_indexes_ctype, site_numbers_ctype, channel_indexes_ctype, None if actual_num_values_ctype is None else (ctypes.pointer(actual_num_values_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(actual_num_values_ctype.value)  # case S200
        pin_indexes_size = actual_num_values_ctype.value  # case B620
        pin_indexes_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViInt32, size=pin_indexes_size)  # case B620
        site_numbers_size = actual_num_values_ctype.value  # case B620
        site_numbers_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViInt32, size=site_numbers_size)  # case B620
        channel_indexes_size = actual_num_values_ctype.value  # case B620
        channel_indexes_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViInt32, size=channel_indexes_size)  # case B620
        error_code = self._library.niDigital_GetPinResultsPinInformation(vi_ctype, channel_list_ctype, buffer_size_ctype, pin_indexes_ctype, site_numbers_ctype, channel_indexes_ctype, None if actual_num_values_ctype is None else (ctypes.pointer(actual_num_values_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [int(pin_indexes_ctype[i]) for i in range(buffer_size_ctype.value)], [int(site_numbers_ctype[i]) for i in range(buffer_size_ctype.value)], [int(channel_indexes_ctype[i]) for i in range(buffer_size_ctype.value)]

    def get_site_pass_fail(self, site_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(site_list.encode(self._encoding))  # case C010
        pass_fail_buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        pass_fail_ctype = None  # case B610
        actual_num_sites_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_GetSitePassFail(vi_ctype, site_list_ctype, pass_fail_buffer_size_ctype, pass_fail_ctype, None if actual_num_sites_ctype is None else (ctypes.pointer(actual_num_sites_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        pass_fail_buffer_size_ctype = _visatype.ViInt32(actual_num_sites_ctype.value)  # case S200
        pass_fail_size = actual_num_sites_ctype.value  # case B620
        pass_fail_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViBoolean, size=pass_fail_size)  # case B620
        error_code = self._library.niDigital_GetSitePassFail(vi_ctype, site_list_ctype, pass_fail_buffer_size_ctype, pass_fail_ctype, None if actual_num_sites_ctype is None else (ctypes.pointer(actual_num_sites_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [bool(pass_fail_ctype[i]) for i in range(pass_fail_buffer_size_ctype.value)]

    def get_site_results_site_numbers(self, site_list, site_result_type):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(site_list.encode(self._encoding))  # case C010
        site_result_type_ctype = _visatype.ViInt32(site_result_type.value)  # case S130
        site_numbers_buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        site_numbers_ctype = None  # case B610
        actual_num_site_numbers_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_GetSiteResultsSiteNumbers(vi_ctype, site_list_ctype, site_result_type_ctype, site_numbers_buffer_size_ctype, site_numbers_ctype, None if actual_num_site_numbers_ctype is None else (ctypes.pointer(actual_num_site_numbers_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        site_numbers_buffer_size_ctype = _visatype.ViInt32(actual_num_site_numbers_ctype.value)  # case S200
        site_numbers_size = actual_num_site_numbers_ctype.value  # case B620
        site_numbers_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViInt32, size=site_numbers_size)  # case B620
        error_code = self._library.niDigital_GetSiteResultsSiteNumbers(vi_ctype, site_list_ctype, site_result_type_ctype, site_numbers_buffer_size_ctype, site_numbers_ctype, None if actual_num_site_numbers_ctype is None else (ctypes.pointer(actual_num_site_numbers_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [int(site_numbers_ctype[i]) for i in range(site_numbers_buffer_size_ctype.value)]

    def get_time_set_drive_format(self, pin, time_set_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_ctype = ctypes.create_string_buffer(pin.encode(self._encoding))  # case C010
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(self._encoding))  # case C020
        format_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_GetTimeSetDriveFormat(vi_ctype, pin_ctype, time_set_name_ctype, None if format_ctype is None else (ctypes.pointer(format_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return enums.DriveFormat(format_ctype.value)

    def get_time_set_edge(self, pin, time_set_name, edge):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_ctype = ctypes.create_string_buffer(pin.encode(self._encoding))  # case C010
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(self._encoding))  # case C020
        edge_ctype = _visatype.ViInt32(edge.value)  # case S130
        time_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDigital_GetTimeSetEdge(vi_ctype, pin_ctype, time_set_name_ctype, edge_ctype, None if time_ctype is None else (ctypes.pointer(time_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(time_ctype.value)

    def get_time_set_edge_multiplier(self, pin, time_set_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_ctype = ctypes.create_string_buffer(pin.encode(self._encoding))  # case C010
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(self._encoding))  # case C020
        edge_multiplier_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_GetTimeSetEdgeMultiplier(vi_ctype, pin_ctype, time_set_name_ctype, None if edge_multiplier_ctype is None else (ctypes.pointer(edge_multiplier_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(edge_multiplier_ctype.value)

    def get_time_set_name(self, time_set_index):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        time_set_index_ctype = _visatype.ViInt32(time_set_index)  # case S150
        name_buffer_size_ctype = _visatype.ViInt32()  # case S170
        name_ctype = None  # case C050
        error_code = self._library.niDigital_GetTimeSetName(vi_ctype, time_set_index_ctype, name_buffer_size_ctype, name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        name_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        name_ctype = (_visatype.ViChar * name_buffer_size_ctype.value)()  # case C060
        error_code = self._library.niDigital_GetTimeSetName(vi_ctype, time_set_index_ctype, name_buffer_size_ctype, name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return name_ctype.value.decode(self._encoding)

    def get_time_set_period(self, time_set_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(self._encoding))  # case C020
        period_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDigital_GetTimeSetPeriod(vi_ctype, time_set_name_ctype, None if period_ctype is None else (ctypes.pointer(period_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(period_ctype.value)

    def init_with_options(self, resource_name, id_query, reset_device, option_string):  # noqa: N802
        resource_name_ctype = ctypes.create_string_buffer(resource_name.encode(self._encoding))  # case C020
        id_query_ctype = _visatype.ViBoolean(id_query)  # case S150
        reset_device_ctype = _visatype.ViBoolean(reset_device)  # case S150
        option_string_ctype = ctypes.create_string_buffer(option_string.encode(self._encoding))  # case C020
        new_vi_ctype = _visatype.ViSession()  # case S220
        error_code = self._library.niDigital_InitWithOptions(resource_name_ctype, id_query_ctype, reset_device_ctype, option_string_ctype, None if new_vi_ctype is None else (ctypes.pointer(new_vi_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        self._close_on_exit = True
        return int(new_vi_ctype.value)

    def initiate(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDigital_Initiate(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def is_done(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        done_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niDigital_IsDone(vi_ctype, None if done_ctype is None else (ctypes.pointer(done_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(done_ctype.value)

    def is_site_enabled(self, site):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_ctype = ctypes.create_string_buffer(site.encode(self._encoding))  # case C010
        enable_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niDigital_IsSiteEnabled(vi_ctype, site_ctype, None if enable_ctype is None else (ctypes.pointer(enable_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(enable_ctype.value)

    def load_levels(self, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_LoadLevels(vi_ctype, file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def load_pattern(self, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_LoadPattern(vi_ctype, file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def load_pin_map(self, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_LoadPinMap(vi_ctype, file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def load_specifications(self, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_LoadSpecifications(vi_ctype, file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def load_timing(self, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_LoadTiming(vi_ctype, file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def lock(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDigital_LockSession(vi_ctype, None)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def ppmu_measure(self, channel_list, measurement_type):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        measurement_type_ctype = _visatype.ViInt32(measurement_type.value)  # case S130
        buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        measurements_ctype = None  # case B610
        actual_num_read_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_PPMU_Measure(vi_ctype, channel_list_ctype, measurement_type_ctype, buffer_size_ctype, measurements_ctype, None if actual_num_read_ctype is None else (ctypes.pointer(actual_num_read_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(actual_num_read_ctype.value)  # case S200
        measurements_size = actual_num_read_ctype.value  # case B620
        measurements_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=measurements_size)  # case B620
        error_code = self._library.niDigital_PPMU_Measure(vi_ctype, channel_list_ctype, measurement_type_ctype, buffer_size_ctype, measurements_ctype, None if actual_num_read_ctype is None else (ctypes.pointer(actual_num_read_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(measurements_ctype[i]) for i in range(buffer_size_ctype.value)]

    def ppmu_source(self, channel_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        error_code = self._library.niDigital_PPMU_Source(vi_ctype, channel_list_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def read_sequencer_flag(self, flag):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        flag_ctype = ctypes.create_string_buffer(flag.value.encode(self._encoding))  # case C030
        value_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niDigital_ReadSequencerFlag(vi_ctype, flag_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(value_ctype.value)

    def read_sequencer_register(self, reg):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        reg_ctype = ctypes.create_string_buffer(reg.value.encode(self._encoding))  # case C030
        value_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_ReadSequencerRegister(vi_ctype, reg_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(value_ctype.value)

    def read_static(self, channel_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        data_ctype = None  # case B610
        actual_num_read_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_ReadStatic(vi_ctype, channel_list_ctype, buffer_size_ctype, data_ctype, None if actual_num_read_ctype is None else (ctypes.pointer(actual_num_read_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(actual_num_read_ctype.value)  # case S200
        data_size = actual_num_read_ctype.value  # case B620
        data_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViUInt8, size=data_size)  # case B620
        error_code = self._library.niDigital_ReadStatic(vi_ctype, channel_list_ctype, buffer_size_ctype, data_ctype, None if actual_num_read_ctype is None else (ctypes.pointer(actual_num_read_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [enums.PinState(data_ctype[i]) for i in range(buffer_size_ctype.value)]

    def reset_device(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDigital_ResetDevice(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def self_calibrate(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDigital_SelfCalibrate(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def send_software_edge_trigger(self, trigger, trigger_identifier):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        trigger_ctype = _visatype.ViInt32(trigger.value)  # case S130
        trigger_identifier_ctype = ctypes.create_string_buffer(trigger_identifier.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_SendSoftwareEdgeTrigger(vi_ctype, trigger_ctype, trigger_identifier_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_boolean(self, channel_name, attribute, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViBoolean(value)  # case S150
        error_code = self._library.niDigital_SetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_int32(self, channel_name, attribute, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViInt32(value)  # case S150
        error_code = self._library.niDigital_SetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_int64(self, channel_name, attribute, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViInt64(value)  # case S150
        error_code = self._library.niDigital_SetAttributeViInt64(vi_ctype, channel_name_ctype, attribute_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_real64(self, channel_name, attribute, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViReal64(value)  # case S150
        error_code = self._library.niDigital_SetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_string(self, channel_name, attribute, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = ctypes.create_string_buffer(value.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_SetAttributeViString(vi_ctype, channel_name_ctype, attribute_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_runtime_environment(self, environment, environment_version, reserved1, reserved2):  # noqa: N802
        environment_ctype = ctypes.create_string_buffer(environment.encode(self._encoding))  # case C020
        environment_version_ctype = ctypes.create_string_buffer(environment_version.encode(self._encoding))  # case C020
        reserved1_ctype = ctypes.create_string_buffer(reserved1.encode(self._encoding))  # case C020
        reserved2_ctype = ctypes.create_string_buffer(reserved2.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_SetRuntimeEnvironment(environment_ctype, environment_version_ctype, reserved1_ctype, reserved2_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def tdr(self, channel_list, apply_offsets):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        apply_offsets_ctype = _visatype.ViBoolean(apply_offsets)  # case S150
        offsets_buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        offsets_ctype = None  # case B610
        actual_num_offsets_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_TDR(vi_ctype, channel_list_ctype, apply_offsets_ctype, offsets_buffer_size_ctype, offsets_ctype, None if actual_num_offsets_ctype is None else (ctypes.pointer(actual_num_offsets_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        offsets_buffer_size_ctype = _visatype.ViInt32(actual_num_offsets_ctype.value)  # case S200
        offsets_size = actual_num_offsets_ctype.value  # case B620
        offsets_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=offsets_size)  # case B620
        error_code = self._library.niDigital_TDR(vi_ctype, channel_list_ctype, apply_offsets_ctype, offsets_buffer_size_ctype, offsets_ctype, None if actual_num_offsets_ctype is None else (ctypes.pointer(actual_num_offsets_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(offsets_ctype[i]) for i in range(offsets_buffer_size_ctype.value)]

    def unload_all_patterns(self, unload_keep_alive_pattern):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        unload_keep_alive_pattern_ctype = _visatype.ViBoolean(unload_keep_alive_pattern)  # case S150
        error_code = self._library.niDigital_UnloadAllPatterns(vi_ctype, unload_keep_alive_pattern_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def unload_specifications(self, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_UnloadSpecifications(vi_ctype, file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def unlock(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDigital_UnlockSession(vi_ctype, None)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def wait_until_done(self, timeout):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        timeout_ctype = _visatype.ViReal64(timeout)  # case S150
        error_code = self._library.niDigital_WaitUntilDone(vi_ctype, timeout_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def write_sequencer_flag(self, flag, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        flag_ctype = ctypes.create_string_buffer(flag.value.encode(self._encoding))  # case C030
        value_ctype = _visatype.ViBoolean(value)  # case S150
        error_code = self._library.niDigital_WriteSequencerFlag(vi_ctype, flag_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def write_sequencer_register(self, reg, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        reg_ctype = ctypes.create_string_buffer(reg.value.encode(self._encoding))  # case C030
        value_ctype = _visatype.ViInt32(value)  # case S150
        error_code = self._library.niDigital_WriteSequencerRegister(vi_ctype, reg_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def write_source_waveform_broadcast(self, waveform_name, waveform_data):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        waveform_size_ctype = _visatype.ViInt32(0 if waveform_data is None else len(waveform_data))  # case S160
        waveform_data_ctype = _get_ctypes_pointer_for_buffer(value=waveform_data, library_type=_visatype.ViUInt32)  # case B550
        error_code = self._library.niDigital_WriteSourceWaveformBroadcastU32(vi_ctype, waveform_name_ctype, waveform_size_ctype, waveform_data_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def write_source_waveform_data_from_file_tdms(self, waveform_name, waveform_file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        waveform_file_path_ctype = ctypes.create_string_buffer(waveform_file_path.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_WriteSourceWaveformDataFromFileTDMS(vi_ctype, waveform_name_ctype, waveform_file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def write_source_waveform_site_unique_u32(self, site_list, waveform_name, num_waveforms, samples_per_waveform, waveform_data):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(site_list.encode(self._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        num_waveforms_ctype = _visatype.ViInt32(num_waveforms)  # case S150
        samples_per_waveform_ctype = _visatype.ViInt32(samples_per_waveform)  # case S150
        waveform_data_array = _convert_to_array(value=waveform_data, array_type="L")  # case B550
        waveform_data_ctype = _get_ctypes_pointer_for_buffer(value=waveform_data_array, library_type=_visatype.ViUInt32)  # case B550
        error_code = self._library.niDigital_WriteSourceWaveformSiteUniqueU32(vi_ctype, site_list_ctype, waveform_name_ctype, num_waveforms_ctype, samples_per_waveform_ctype, waveform_data_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def write_static(self, channel_list, state):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        state_ctype = _visatype.ViUInt8(state.value)  # case S130
        error_code = self._library.niDigital_WriteStatic(vi_ctype, channel_list_ctype, state_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def close(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDigital_close(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def error_message(self, error_code):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code_ctype = _visatype.ViStatus(error_code)  # case S150
        error_message_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library.niDigital_error_message(vi_ctype, error_code_ctype, error_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return error_message_ctype.value.decode(self._encoding)

    def reset(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDigital_reset(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def self_test(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        test_result_ctype = _visatype.ViInt16()  # case S220
        test_message_ctype = (_visatype.ViChar * 2048)()  # case C070
        error_code = self._library.niDigital_self_test(vi_ctype, None if test_result_ctype is None else (ctypes.pointer(test_result_ctype)), test_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(test_result_ctype.value), test_message_ctype.value.decode(self._encoding)
