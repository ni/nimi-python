# -*- coding: utf-8 -*-
# This file was generated

import array
import ctypes
import hightime  # noqa: F401
import nirfsa._complextype as _complextype
import nirfsa._library_singleton as _library_singleton
import nirfsa._visatype as _visatype
import nirfsa.enums as enums  # noqa: F401
import nirfsa.errors as errors

import nirfsa.coefficient_info_type as coefficient_info_type  # noqa: F401

import nirfsa.waveform_info as waveform_info  # noqa: F401

import nirfsa.spectrum_info_type as spectrum_info_type  # noqa: F401


# Helper functions for creating ctypes needed for calling into the driver DLL
def _get_ctypes_pointer_for_buffer(value=None, library_type=None, size=None):
    if isinstance(value, array.array):
        assert library_type is not None, 'library_type is required for array.array'
        addr, _ = value.buffer_info()
        return ctypes.cast(addr, ctypes.POINTER(library_type))
    elif str(type(value)).find("'numpy.ndarray'") != -1:
        import numpy
        if library_type in (_complextype.NIComplexI16, _complextype.NIComplexNumberF32, _complextype.NIComplexNumber):
            complex_dtype = numpy.dtype(library_type)
            if value.ndim > 1:
                # we create a flattened view of the multi-dimensional numpy array
                restructured_array_view = value.ravel().view(complex_dtype)
            else:
                restructured_array_view = value.view(complex_dtype)
            return restructured_array_view.ctypes.data_as(ctypes.POINTER(library_type))
        else:
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
        return "Failed to retrieve error description."

    def abort(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSA_Abort(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def change_external_calibration_password(self, old_password, new_password):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        old_password_ctype = ctypes.create_string_buffer(old_password.encode(self._encoding))  # case C020
        new_password_ctype = ctypes.create_string_buffer(new_password.encode(self._encoding))  # case C020
        error_code = self._library.niRFSA_ChangeExternalCalibrationPassword(vi_ctype, old_password_ctype, new_password_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def check_acquisition_status(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        is_done_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niRFSA_CheckAcquisitionStatus(vi_ctype, None if is_done_ctype is None else (ctypes.pointer(is_done_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(is_done_ctype.value)

    def clear_self_calibrate_range(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSA_ClearSelfCalibrateRange(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def commit(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSA_Commit(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_deembedding_table_interpolation_linear(self, port, table_name, format):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        port_ctype = ctypes.create_string_buffer(port.encode(self._encoding))  # case C020
        table_name_ctype = ctypes.create_string_buffer(table_name.encode(self._encoding))  # case C020
        format_ctype = _visatype.ViInt32(format.value)  # case S130
        error_code = self._library.niRFSA_ConfigureDeembeddingTableInterpolationLinear(vi_ctype, port_ctype, table_name_ctype, format_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_deembedding_table_interpolation_nearest(self, port, table_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        port_ctype = ctypes.create_string_buffer(port.encode(self._encoding))  # case C020
        table_name_ctype = ctypes.create_string_buffer(table_name.encode(self._encoding))  # case C020
        error_code = self._library.niRFSA_ConfigureDeembeddingTableInterpolationNearest(vi_ctype, port_ctype, table_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_deembedding_table_interpolation_spline(self, port, table_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        port_ctype = ctypes.create_string_buffer(port.encode(self._encoding))  # case C020
        table_name_ctype = ctypes.create_string_buffer(table_name.encode(self._encoding))  # case C020
        error_code = self._library.niRFSA_ConfigureDeembeddingTableInterpolationSpline(vi_ctype, port_ctype, table_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_digital_edge_advance_trigger(self, source, edge):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        source_ctype = ctypes.create_string_buffer(source.encode(self._encoding))  # case C020
        edge_ctype = _visatype.ViInt32(edge.value)  # case S130
        error_code = self._library.niRFSA_ConfigureDigitalEdgeAdvanceTrigger(vi_ctype, source_ctype, edge_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_digital_edge_ref_trigger(self, source, edge, pretrigger_samples):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        source_ctype = ctypes.create_string_buffer(source.encode(self._encoding))  # case C020
        edge_ctype = _visatype.ViInt32(edge.value)  # case S130
        pretrigger_samples_ctype = _visatype.ViInt64(pretrigger_samples)  # case S150
        error_code = self._library.niRFSA_ConfigureDigitalEdgeRefTrigger(vi_ctype, source_ctype, edge_ctype, pretrigger_samples_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_digital_edge_start_trigger(self, source, edge):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        source_ctype = ctypes.create_string_buffer(source.encode(self._encoding))  # case C020
        edge_ctype = _visatype.ViInt32(edge.value)  # case S130
        error_code = self._library.niRFSA_ConfigureDigitalEdgeStartTrigger(vi_ctype, source_ctype, edge_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_iq_power_edge_ref_trigger(self, source, level, slope, pretrigger_samples):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        source_ctype = ctypes.create_string_buffer(source.encode(self._encoding))  # case C020
        level_ctype = _visatype.ViReal64(level)  # case S150
        slope_ctype = _visatype.ViInt32(slope.value)  # case S130
        pretrigger_samples_ctype = _visatype.ViInt64(pretrigger_samples)  # case S150
        error_code = self._library.niRFSA_ConfigureIQPowerEdgeRefTrigger(vi_ctype, source_ctype, level_ctype, slope_ctype, pretrigger_samples_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_ref_clock(self, clock_source, ref_clock_rate):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        clock_source_ctype = ctypes.create_string_buffer(clock_source.value.encode(self._encoding))  # case C030
        ref_clock_rate_ctype = _visatype.ViReal64(ref_clock_rate)  # case S150
        error_code = self._library.niRFSA_ConfigureRefClock(vi_ctype, clock_source_ctype, ref_clock_rate_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_software_edge_advance_trigger(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSA_ConfigureSoftwareEdgeAdvanceTrigger(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_software_edge_ref_trigger(self, pretrigger_samples):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pretrigger_samples_ctype = _visatype.ViInt64(pretrigger_samples)  # case S150
        error_code = self._library.niRFSA_ConfigureSoftwareEdgeRefTrigger(vi_ctype, pretrigger_samples_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_software_edge_start_trigger(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSA_ConfigureSoftwareEdgeStartTrigger(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_spectrum_frequency_center_span(self, channel_list, center_frequency, span):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        center_frequency_ctype = _visatype.ViReal64(center_frequency)  # case S150
        span_ctype = _visatype.ViReal64(span)  # case S150
        error_code = self._library.niRFSA_ConfigureSpectrumFrequencyCenterSpan(vi_ctype, channel_list_ctype, center_frequency_ctype, span_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_spectrum_frequency_start_stop(self, channel_list, start_frequency, stop_frequency):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        start_frequency_ctype = _visatype.ViReal64(start_frequency)  # case S150
        stop_frequency_ctype = _visatype.ViReal64(stop_frequency)  # case S150
        error_code = self._library.niRFSA_ConfigureSpectrumFrequencyStartStop(vi_ctype, channel_list_ctype, start_frequency_ctype, stop_frequency_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_deembedding_sparameter_table_array(self, port, table_name, frequencies, sparameter_table, number_of_ports, sparameter_orientation):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        port_ctype = ctypes.create_string_buffer(port.encode(self._encoding))  # case C020
        table_name_ctype = ctypes.create_string_buffer(table_name.encode(self._encoding))  # case C020
        frequencies_ctype = _get_ctypes_pointer_for_buffer(value=frequencies)  # case B510
        frequencies_size_ctype = _visatype.ViInt32(0 if frequencies is None else len(frequencies))  # case S160
        sparameter_table_ctype = _get_ctypes_pointer_for_buffer(value=sparameter_table, library_type=_complextype.NIComplexNumber)  # case B510
        sparameter_table_size_ctype = _visatype.ViInt32(0 if sparameter_table is None else sparameter_table.size)  # case S161
        number_of_ports_ctype = _visatype.ViInt32(number_of_ports)  # case S150
        sparameter_orientation_ctype = _visatype.ViInt32(sparameter_orientation.value)  # case S130
        error_code = self._library.niRFSA_CreateDeembeddingSparameterTableArray(vi_ctype, port_ctype, table_name_ctype, frequencies_ctype, frequencies_size_ctype, sparameter_table_ctype, sparameter_table_size_ctype, number_of_ports_ctype, sparameter_orientation_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_deembedding_sparameter_table_s2p_file(self, port, table_name, s2p_file_path, sparameter_orientation):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        port_ctype = ctypes.create_string_buffer(port.encode(self._encoding))  # case C020
        table_name_ctype = ctypes.create_string_buffer(table_name.encode(self._encoding))  # case C020
        s2p_file_path_ctype = ctypes.create_string_buffer(s2p_file_path.encode(self._encoding))  # case C020
        sparameter_orientation_ctype = _visatype.ViInt32(sparameter_orientation.value)  # case S130
        error_code = self._library.niRFSA_CreateDeembeddingSparameterTableS2PFile(vi_ctype, port_ctype, table_name_ctype, s2p_file_path_ctype, sparameter_orientation_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def delete_all_deembedding_tables(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSA_DeleteAllDeembeddingTables(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def delete_deembedding_table(self, port, table_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        port_ctype = ctypes.create_string_buffer(port.encode(self._encoding))  # case C020
        table_name_ctype = ctypes.create_string_buffer(table_name.encode(self._encoding))  # case C020
        error_code = self._library.niRFSA_DeleteDeembeddingTable(vi_ctype, port_ctype, table_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disable_advance_trigger(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSA_DisableAdvanceTrigger(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disable_ref_trigger(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSA_DisableRefTrigger(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disable_start_trigger(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSA_DisableStartTrigger(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def enable_session_access(self, enable):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        enable_ctype = _visatype.ViBoolean(enable)  # case S150
        error_code = self._library.niRFSA_EnableSessionAccess(vi_ctype, enable_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def error_message(self, error_code):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code_ctype = _visatype.ViStatus(error_code)  # case S150
        error_message_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library.niRFSA_ErrorMessage(vi_ctype, error_code_ctype, error_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return error_message_ctype.value.decode(self._encoding)

    def fetch_iq_multi_record_complex_f32(self, channel_list, starting_record, number_of_records, iq_data_arrays, timeout):  # noqa: N802
        samples_per_record = 0 if iq_data_arrays is None else (iq_data_arrays.shape[1] if hasattr(iq_data_arrays, 'shape') and len(iq_data_arrays.shape) > 1 else len(iq_data_arrays))
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        starting_record_ctype = _visatype.ViInt64(starting_record)  # case S150
        number_of_records_ctype = _visatype.ViInt64(number_of_records)  # case S150
        number_of_samples_ctype = _visatype.ViInt64(samples_per_record)  # case S160
        timeout_ctype = _visatype.ViReal64(timeout)  # case S150
        iq_data_arrays_ctype = _get_ctypes_pointer_for_buffer(value=iq_data_arrays, library_type=_complextype.NIComplexNumberF32)  # case B510
        wfm_info_ctype = (waveform_info.struct_niRFSA_wfmInfo * number_of_records)()  # case S220
        error_code = self._library.niRFSA_FetchIQMultiRecordComplexF32(vi_ctype, channel_list_ctype, starting_record_ctype, number_of_records_ctype, number_of_samples_ctype, timeout_ctype, iq_data_arrays_ctype, wfm_info_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [waveform_info.WaveformInfo(wfm_info_ctype[i]) for i in range(number_of_records)]

    def fetch_iq_multi_record_complex_f64(self, channel_list, starting_record, number_of_records, iq_data_arrays, timeout):  # noqa: N802
        samples_per_record = 0 if iq_data_arrays is None else (iq_data_arrays.shape[1] if hasattr(iq_data_arrays, 'shape') and len(iq_data_arrays.shape) > 1 else len(iq_data_arrays))
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        starting_record_ctype = _visatype.ViInt64(starting_record)  # case S150
        number_of_records_ctype = _visatype.ViInt64(number_of_records)  # case S150
        number_of_samples_ctype = _visatype.ViInt64(samples_per_record)  # case S160
        timeout_ctype = _visatype.ViReal64(timeout)  # case S150
        iq_data_arrays_ctype = _get_ctypes_pointer_for_buffer(value=iq_data_arrays, library_type=_complextype.NIComplexNumber)  # case B510
        wfm_info_ctype = (waveform_info.struct_niRFSA_wfmInfo * number_of_records)()  # case S220
        error_code = self._library.niRFSA_FetchIQMultiRecordComplexF64(vi_ctype, channel_list_ctype, starting_record_ctype, number_of_records_ctype, number_of_samples_ctype, timeout_ctype, iq_data_arrays_ctype, wfm_info_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [waveform_info.WaveformInfo(wfm_info_ctype[i]) for i in range(number_of_records)]

    def fetch_iq_multi_record_complex_i16(self, channel_list, starting_record, number_of_records, iq_data_arrays, timeout):  # noqa: N802
        samples_per_record = 0 if iq_data_arrays is None else (iq_data_arrays.shape[1] if hasattr(iq_data_arrays, 'shape') and len(iq_data_arrays.shape) > 1 else len(iq_data_arrays))
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        starting_record_ctype = _visatype.ViInt64(starting_record)  # case S150
        number_of_records_ctype = _visatype.ViInt64(number_of_records)  # case S150
        number_of_samples_ctype = _visatype.ViInt64(samples_per_record // 2)  # case S160
        timeout_ctype = _visatype.ViReal64(timeout)  # case S150
        iq_data_arrays_ctype = _get_ctypes_pointer_for_buffer(value=iq_data_arrays, library_type=_complextype.NIComplexI16)  # case B510
        wfm_info_ctype = (waveform_info.struct_niRFSA_wfmInfo * number_of_records)()  # case S220
        error_code = self._library.niRFSA_FetchIQMultiRecordComplexI16(vi_ctype, channel_list_ctype, starting_record_ctype, number_of_records_ctype, number_of_samples_ctype, timeout_ctype, iq_data_arrays_ctype, wfm_info_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [waveform_info.WaveformInfo(wfm_info_ctype[i]) for i in range(number_of_records)]

    def fetch_iq_single_record_complex_f32(self, channel_list, record_number, iq_data_array, timeout):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        record_number_ctype = _visatype.ViInt64(record_number)  # case S150
        number_of_samples_ctype = _visatype.ViInt64(0 if iq_data_array is None else len(iq_data_array))  # case S160
        timeout_ctype = _visatype.ViReal64(timeout)  # case S150
        iq_data_array_ctype = _get_ctypes_pointer_for_buffer(value=iq_data_array, library_type=_complextype.NIComplexNumberF32)  # case B510
        wfm_info_ctype = waveform_info.struct_niRFSA_wfmInfo()  # case S220
        error_code = self._library.niRFSA_FetchIQSingleRecordComplexF32(vi_ctype, channel_list_ctype, record_number_ctype, number_of_samples_ctype, timeout_ctype, iq_data_array_ctype, None if wfm_info_ctype is None else (ctypes.pointer(wfm_info_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return waveform_info.WaveformInfo(wfm_info_ctype)

    def fetch_iq_single_record_complex_f64(self, channel_list, record_number, iq_data_array, timeout):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        record_number_ctype = _visatype.ViInt64(record_number)  # case S150
        number_of_samples_ctype = _visatype.ViInt64(0 if iq_data_array is None else len(iq_data_array))  # case S160
        timeout_ctype = _visatype.ViReal64(timeout)  # case S150
        iq_data_array_ctype = _get_ctypes_pointer_for_buffer(value=iq_data_array, library_type=_complextype.NIComplexNumber)  # case B510
        wfm_info_ctype = waveform_info.struct_niRFSA_wfmInfo()  # case S220
        error_code = self._library.niRFSA_FetchIQSingleRecordComplexF64(vi_ctype, channel_list_ctype, record_number_ctype, number_of_samples_ctype, timeout_ctype, iq_data_array_ctype, None if wfm_info_ctype is None else (ctypes.pointer(wfm_info_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return waveform_info.WaveformInfo(wfm_info_ctype)

    def fetch_iq_single_record_complex_i16(self, channel_list, record_number, iq_data_array, timeout):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        record_number_ctype = _visatype.ViInt64(record_number)  # case S150
        number_of_samples_ctype = _visatype.ViInt64(0 if iq_data_array is None else len(iq_data_array) // 2)  # case S160
        timeout_ctype = _visatype.ViReal64(timeout)  # case S150
        iq_data_array_ctype = _get_ctypes_pointer_for_buffer(value=iq_data_array, library_type=_complextype.NIComplexI16)  # case B510
        wfm_info_ctype = waveform_info.struct_niRFSA_wfmInfo()  # case S220
        error_code = self._library.niRFSA_FetchIQSingleRecordComplexI16(vi_ctype, channel_list_ctype, record_number_ctype, number_of_samples_ctype, timeout_ctype, iq_data_array_ctype, None if wfm_info_ctype is None else (ctypes.pointer(wfm_info_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return waveform_info.WaveformInfo(wfm_info_ctype)

    def get_attribute_vi_boolean(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niRFSA_GetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_id_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(value_ctype.value)

    def get_attribute_vi_int32(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niRFSA_GetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_id_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(value_ctype.value)

    def get_attribute_vi_int64(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViInt64()  # case S220
        error_code = self._library.niRFSA_GetAttributeViInt64(vi_ctype, channel_name_ctype, attribute_id_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(value_ctype.value)

    def get_attribute_vi_real64(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niRFSA_GetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_id_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(value_ctype.value)

    def get_attribute_vi_session(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViSession()  # case S220
        error_code = self._library.niRFSA_GetAttributeViSession(vi_ctype, channel_name_ctype, attribute_id_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(value_ctype.value)

    def get_attribute_vi_string(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        buf_size_ctype = _visatype.ViInt32()  # case S170
        value_ctype = None  # case C050
        error_code = self._library.niRFSA_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, buf_size_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buf_size_ctype = _visatype.ViInt32(error_code)  # case S180
        value_ctype = (_visatype.ViChar * buf_size_ctype.value)()  # case C060
        error_code = self._library.niRFSA_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, buf_size_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return value_ctype.value.decode(self._encoding)

    def get_deembedding_sparameters(self):
        import numpy as np
        number_of_ports = self.get_deembedding_table_number_of_ports()
        sparameters_array_size = number_of_ports ** 2
        sparameters = np.full((number_of_ports, number_of_ports), 0 + 0j, dtype=np.complex128)
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        sparameters_ctype = _get_ctypes_pointer_for_buffer(value=sparameters, library_type=_complextype.NIComplexNumber)  # case B510
        sparameters_array_size_ctype = _visatype.ViInt32(sparameters_array_size)  # case S150
        number_of_sparameters_ctype = _visatype.ViInt32()  # case S220
        number_of_ports_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niRFSA_GetDeembeddingSparameters(vi_ctype, sparameters_ctype, sparameters_array_size_ctype, None if number_of_sparameters_ctype is None else (ctypes.pointer(number_of_sparameters_ctype)), None if number_of_ports_ctype is None else (ctypes.pointer(number_of_ports_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        sparameters = sparameters.reshape((int(number_of_ports_ctype.value), int(number_of_ports_ctype.value)))
        return sparameters

    def get_deembedding_table_number_of_ports(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        number_of_ports_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niRFSA_GetDeembeddingTableNumberOfPorts(vi_ctype, None if number_of_ports_ctype is None else (ctypes.pointer(number_of_ports_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(number_of_ports_ctype.value)

    def get_error(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code_ctype = _visatype.ViStatus()  # case S220
        error_description_buffer_size_ctype = _visatype.ViInt32()  # case S170
        error_description_ctype = None  # case C050
        error_code = self._library.niRFSA_GetError(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), error_description_buffer_size_ctype, error_description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=True)
        error_description_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        error_description_ctype = (_visatype.ViChar * error_description_buffer_size_ctype.value)()  # case C060
        error_code = self._library.niRFSA_GetError(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), error_description_buffer_size_ctype, error_description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return int(error_code_ctype.value), error_description_ctype.value.decode(self._encoding)

    def get_ext_cal_last_date_and_time(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        year_ctype = _visatype.ViInt32()  # case S220
        month_ctype = _visatype.ViInt32()  # case S220
        day_ctype = _visatype.ViInt32()  # case S220
        hour_ctype = _visatype.ViInt32()  # case S220
        minute_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niRFSA_GetExtCalLastDateAndTime(vi_ctype, None if year_ctype is None else (ctypes.pointer(year_ctype)), None if month_ctype is None else (ctypes.pointer(month_ctype)), None if day_ctype is None else (ctypes.pointer(day_ctype)), None if hour_ctype is None else (ctypes.pointer(hour_ctype)), None if minute_ctype is None else (ctypes.pointer(minute_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(year_ctype.value), int(month_ctype.value), int(day_ctype.value), int(hour_ctype.value), int(minute_ctype.value)

    def get_ext_cal_recommended_interval(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        months_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niRFSA_GetExtCalRecommendedInterval(vi_ctype, None if months_ctype is None else (ctypes.pointer(months_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(months_ctype.value)

    def get_fetch_backlog(self, channel_list, record_number):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        record_number_ctype = _visatype.ViInt64(record_number)  # case S150
        backlog_ctype = _visatype.ViInt64()  # case S220
        error_code = self._library.niRFSA_GetFetchBacklog(vi_ctype, channel_list_ctype, record_number_ctype, None if backlog_ctype is None else (ctypes.pointer(backlog_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(backlog_ctype.value)

    def get_frequency_response(self, channel_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        frequencies_ctype = None  # case B610
        magnitude_response_ctype = None  # case B610
        phase_response_ctype = None  # case B610
        number_of_frequencies_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niRFSA_GetFrequencyResponse(vi_ctype, channel_list_ctype, buffer_size_ctype, frequencies_ctype, magnitude_response_ctype, phase_response_ctype, None if number_of_frequencies_ctype is None else (ctypes.pointer(number_of_frequencies_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(number_of_frequencies_ctype.value)  # case S200
        frequencies_size = number_of_frequencies_ctype.value  # case B620
        frequencies_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=frequencies_size)  # case B620
        magnitude_response_size = number_of_frequencies_ctype.value  # case B620
        magnitude_response_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=magnitude_response_size)  # case B620
        phase_response_size = number_of_frequencies_ctype.value  # case B620
        phase_response_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=phase_response_size)  # case B620
        error_code = self._library.niRFSA_GetFrequencyResponse(vi_ctype, channel_list_ctype, buffer_size_ctype, frequencies_ctype, magnitude_response_ctype, phase_response_ctype, None if number_of_frequencies_ctype is None else (ctypes.pointer(number_of_frequencies_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(frequencies_ctype[i]) for i in range(buffer_size_ctype.value)], [float(magnitude_response_ctype[i]) for i in range(buffer_size_ctype.value)], [float(phase_response_ctype[i]) for i in range(buffer_size_ctype.value)]

    def get_scaling_coefficients(self, channel_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        array_size_ctype = _visatype.ViInt32(0)  # case S190
        coefficient_info_ctype = None  # case B610
        number_of_coefficient_sets_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niRFSA_GetScalingCoefficients(vi_ctype, channel_list_ctype, array_size_ctype, coefficient_info_ctype, None if number_of_coefficient_sets_ctype is None else (ctypes.pointer(number_of_coefficient_sets_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        array_size_ctype = _visatype.ViInt32(number_of_coefficient_sets_ctype.value)  # case S200
        coefficient_info_size = number_of_coefficient_sets_ctype.value  # case B620
        coefficient_info_ctype = _get_ctypes_pointer_for_buffer(library_type=coefficient_info_type.struct_niRFSA_coefficientInfo, size=coefficient_info_size)  # case B620
        error_code = self._library.niRFSA_GetScalingCoefficients(vi_ctype, channel_list_ctype, array_size_ctype, coefficient_info_ctype, None if number_of_coefficient_sets_ctype is None else (ctypes.pointer(number_of_coefficient_sets_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [coefficient_info_type.CoefficientInfo(coefficient_info_ctype[i]) for i in range(array_size_ctype.value)]

    def get_self_cal_last_date_and_time(self, self_calibration_step):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        self_calibration_step_ctype = _visatype.ViInt64(self_calibration_step.value)  # case S130
        year_ctype = _visatype.ViInt32()  # case S220
        month_ctype = _visatype.ViInt32()  # case S220
        day_ctype = _visatype.ViInt32()  # case S220
        hour_ctype = _visatype.ViInt32()  # case S220
        minute_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niRFSA_GetSelfCalLastDateAndTime(vi_ctype, self_calibration_step_ctype, None if year_ctype is None else (ctypes.pointer(year_ctype)), None if month_ctype is None else (ctypes.pointer(month_ctype)), None if day_ctype is None else (ctypes.pointer(day_ctype)), None if hour_ctype is None else (ctypes.pointer(hour_ctype)), None if minute_ctype is None else (ctypes.pointer(minute_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(year_ctype.value), int(month_ctype.value), int(day_ctype.value), int(hour_ctype.value), int(minute_ctype.value)

    def get_self_calibration_temperature(self, self_calibration_step):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        self_calibration_step_ctype = _visatype.ViInt64(self_calibration_step.value)  # case S130
        temperature_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niRFSA_GetSelfCalLastTemp(vi_ctype, self_calibration_step_ctype, None if temperature_ctype is None else (ctypes.pointer(temperature_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

    def get_terminal_name(self, signal, signal_identifier):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        signal_ctype = _visatype.ViInt32(signal.value)  # case S130
        signal_identifier_ctype = ctypes.create_string_buffer(signal_identifier.encode(self._encoding))  # case C020
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        terminal_name_ctype = None  # case C050
        error_code = self._library.niRFSA_GetTerminalName(vi_ctype, signal_ctype, signal_identifier_ctype, buffer_size_ctype, terminal_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        terminal_name_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niRFSA_GetTerminalName(vi_ctype, signal_ctype, signal_identifier_ctype, buffer_size_ctype, terminal_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return terminal_name_ctype.value.decode(self._encoding)

    def init_with_options(self, resource_name, id_query, reset_device, option_string):  # noqa: N802
        resource_name_ctype = ctypes.create_string_buffer(resource_name.encode(self._encoding))  # case C020
        id_query_ctype = _visatype.ViBoolean(id_query)  # case S150
        reset_device_ctype = _visatype.ViBoolean(reset_device)  # case S150
        option_string_ctype = ctypes.create_string_buffer(option_string.encode(self._encoding))  # case C020
        new_vi_ctype = _visatype.ViSession()  # case S220
        error_code = self._library.niRFSA_InitWithOptions(resource_name_ctype, id_query_ctype, reset_device_ctype, option_string_ctype, None if new_vi_ctype is None else (ctypes.pointer(new_vi_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(new_vi_ctype.value)

    def initiate(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSA_Initiate(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def is_self_cal_valid(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        self_cal_valid_ctype = _visatype.ViBoolean()  # case S220
        valid_steps_ctype = _visatype.ViInt64()  # case S220
        error_code = self._library.niRFSA_IsSelfCalValid(vi_ctype, None if self_cal_valid_ctype is None else (ctypes.pointer(self_cal_valid_ctype)), None if valid_steps_ctype is None else (ctypes.pointer(valid_steps_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(self_cal_valid_ctype.value), enums.SelfCalSteps(valid_steps_ctype.value)

    def load_configurations_from_file(self, channel_name, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.niRFSA_LoadConfigurationsFromFile(vi_ctype, channel_name_ctype, file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def lock(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSA_LockSession(vi_ctype, None)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def perform_thermal_correction(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSA_PerformThermalCorrection(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def read_iq_single_record_complex_f64(self, channel_list, iq_data_array, timeout):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        timeout_ctype = _visatype.ViReal64(timeout)  # case S150
        iq_data_array_ctype = _get_ctypes_pointer_for_buffer(value=iq_data_array, library_type=_complextype.NIComplexNumber)  # case B510
        data_array_size_ctype = _visatype.ViInt64(0 if iq_data_array is None else len(iq_data_array))  # case S120
        wfm_info_ctype = waveform_info.struct_niRFSA_wfmInfo()  # case S220
        error_code = self._library.niRFSA_ReadIQSingleRecordComplexF64(vi_ctype, channel_list_ctype, timeout_ctype, iq_data_array_ctype, data_array_size_ctype, None if wfm_info_ctype is None else (ctypes.pointer(wfm_info_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return waveform_info.WaveformInfo(wfm_info_ctype)

    def read_power_spectrum_f32(self, channel_list, timeout, power_spectrum_data_array):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        timeout_ctype = _visatype.ViReal64(timeout)  # case S150
        power_spectrum_data_array_ctype = _get_ctypes_pointer_for_buffer(value=power_spectrum_data_array, library_type=_visatype.ViReal32)  # case B550
        data_array_size_ctype = _visatype.ViInt32(len(power_spectrum_data_array))  # case S120
        spectrum_info_ctype = spectrum_info_type.struct_niRFSA_spectrumInfo()  # case S220
        error_code = self._library.niRFSA_ReadPowerSpectrumF32(vi_ctype, channel_list_ctype, timeout_ctype, power_spectrum_data_array_ctype, data_array_size_ctype, None if spectrum_info_ctype is None else (ctypes.pointer(spectrum_info_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return spectrum_info_type.SpectrumInfo(spectrum_info_ctype)

    def read_power_spectrum_f64(self, channel_list, timeout, power_spectrum_data_array):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        timeout_ctype = _visatype.ViReal64(timeout)  # case S150
        power_spectrum_data_array_ctype = _get_ctypes_pointer_for_buffer(value=power_spectrum_data_array, library_type=_visatype.ViReal64)  # case B550
        data_array_size_ctype = _visatype.ViInt32(len(power_spectrum_data_array))  # case S120
        spectrum_info_ctype = spectrum_info_type.struct_niRFSA_spectrumInfo()  # case S220
        error_code = self._library.niRFSA_ReadPowerSpectrumF64(vi_ctype, channel_list_ctype, timeout_ctype, power_spectrum_data_array_ctype, data_array_size_ctype, None if spectrum_info_ctype is None else (ctypes.pointer(spectrum_info_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return spectrum_info_type.SpectrumInfo(spectrum_info_ctype)

    def reset_device(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSA_ResetDevice(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def reset_with_options(self, steps_to_omit):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        steps_to_omit_ctype = _visatype.ViUInt64(steps_to_omit.value)  # case S130
        error_code = self._library.niRFSA_ResetWithOptions(vi_ctype, steps_to_omit_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def save_configurations_to_file(self, channel_name, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.niRFSA_SaveConfigurationsToFile(vi_ctype, channel_name_ctype, file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def self_calibrate_range(self, steps_to_omit, minimum_frequency, maximum_frequency, minimum_reference_level, maximum_reference_level):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        steps_to_omit_ctype = _visatype.ViInt64(steps_to_omit.value)  # case S130
        minimum_frequency_ctype = _visatype.ViReal64(minimum_frequency)  # case S150
        maximum_frequency_ctype = _visatype.ViReal64(maximum_frequency)  # case S150
        minimum_reference_level_ctype = _visatype.ViReal64(minimum_reference_level)  # case S150
        maximum_reference_level_ctype = _visatype.ViReal64(maximum_reference_level)  # case S150
        error_code = self._library.niRFSA_SelfCalibrateRange(vi_ctype, steps_to_omit_ctype, minimum_frequency_ctype, maximum_frequency_ctype, minimum_reference_level_ctype, maximum_reference_level_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def send_software_edge_trigger(self, trigger, trigger_identifier):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        trigger_ctype = _visatype.ViInt32(trigger.value)  # case S130
        trigger_identifier_ctype = ctypes.create_string_buffer(trigger_identifier.encode(self._encoding))  # case C020
        error_code = self._library.niRFSA_SendSoftwareEdgeTrigger(vi_ctype, trigger_ctype, trigger_identifier_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_boolean(self, channel_name, attribute_id, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViBoolean(value)  # case S150
        error_code = self._library.niRFSA_SetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_id_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_int32(self, channel_name, attribute_id, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViInt32(value)  # case S150
        error_code = self._library.niRFSA_SetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_id_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_int64(self, channel_name, attribute_id, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViInt64(value)  # case S150
        error_code = self._library.niRFSA_SetAttributeViInt64(vi_ctype, channel_name_ctype, attribute_id_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_real64(self, channel_name, attribute_id, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViReal64(value)  # case S150
        error_code = self._library.niRFSA_SetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_id_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_session(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSA_SetAttributeViSession(vi_ctype, channel_name_ctype, attribute_id_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_string(self, channel_name, attribute_id, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = ctypes.create_string_buffer(value.encode(self._encoding))  # case C020
        error_code = self._library.niRFSA_SetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def unlock(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSA_UnlockSession(vi_ctype, None)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def close(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSA_close(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def reset(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSA_reset(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def self_test(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        self_test_result_ctype = _visatype.ViInt16()  # case S220
        self_test_message_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library.niRFSA_self_test(vi_ctype, None if self_test_result_ctype is None else (ctypes.pointer(self_test_result_ctype)), self_test_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(self_test_result_ctype.value), self_test_message_ctype.value.decode(self._encoding)
