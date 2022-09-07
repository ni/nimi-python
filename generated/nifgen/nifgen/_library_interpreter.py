# -*- coding: utf-8 -*-
# This file was generated

import array  # noqa: F401
import ctypes
import hightime
import nifgen._converters as _converters
import nifgen._library_singleton as _library_singleton
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


class LibraryInterpreter(object):
    '''Library C<->Python interpreter.'''

    def __init__(self, encoding):
        self._encoding = encoding
        self._library = _library_singleton.get()

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
        error_code = self._library.abort(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def allocate_named_waveform(self, session, channel_name, waveform_name, waveform_size):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        waveform_size_ctype = _visatype.ViInt32(waveform_size)  # case S150
        error_code = self._library.allocate_named_waveform(vi_ctype, channel_name_ctype, waveform_name_ctype, waveform_size_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def allocate_waveform(self, session, channel_name, waveform_size):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        waveform_size_ctype = _visatype.ViInt32(waveform_size)  # case S150
        waveform_handle_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.allocate_waveform(vi_ctype, channel_name_ctype, waveform_size_ctype, None if waveform_handle_ctype is None else (ctypes.pointer(waveform_handle_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(waveform_handle_ctype.value)

    def clear_arb_memory(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        error_code = self._library.clear_arb_memory(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def clear_arb_sequence(self, session, sequence_handle):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        sequence_handle_ctype = _visatype.ViInt32(sequence_handle)  # case S150
        error_code = self._library.clear_arb_sequence(vi_ctype, sequence_handle_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _clear_arb_waveform(self, session, waveform_handle):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        waveform_handle_ctype = _visatype.ViInt32(waveform_handle)  # case S150
        error_code = self._library._clear_arb_waveform(vi_ctype, waveform_handle_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def clear_freq_list(self, session, frequency_list_handle):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        frequency_list_handle_ctype = _visatype.ViInt32(frequency_list_handle)  # case S150
        error_code = self._library.clear_freq_list(vi_ctype, frequency_list_handle_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def clear_user_standard_waveform(self, session, channel_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        error_code = self._library.clear_user_standard_waveform(vi_ctype, channel_name_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def commit(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        error_code = self._library.commit(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_arb_sequence(self, session, channel_name, sequence_handle, gain, offset):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        sequence_handle_ctype = _visatype.ViInt32(sequence_handle)  # case S150
        gain_ctype = _visatype.ViReal64(gain)  # case S150
        offset_ctype = _visatype.ViReal64(offset)  # case S150
        error_code = self._library.configure_arb_sequence(vi_ctype, channel_name_ctype, sequence_handle_ctype, gain_ctype, offset_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_arb_waveform(self, session, channel_name, waveform_handle, gain, offset):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        waveform_handle_ctype = _visatype.ViInt32(waveform_handle)  # case S150
        gain_ctype = _visatype.ViReal64(gain)  # case S150
        offset_ctype = _visatype.ViReal64(offset)  # case S150
        error_code = self._library.configure_arb_waveform(vi_ctype, channel_name_ctype, waveform_handle_ctype, gain_ctype, offset_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_freq_list(self, session, channel_name, frequency_list_handle, amplitude, dc_offset=0.0, start_phase=0.0):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        frequency_list_handle_ctype = _visatype.ViInt32(frequency_list_handle)  # case S150
        amplitude_ctype = _visatype.ViReal64(amplitude)  # case S150
        dc_offset_ctype = _visatype.ViReal64(dc_offset)  # case S150
        start_phase_ctype = _visatype.ViReal64(start_phase)  # case S150
        error_code = self._library.configure_freq_list(vi_ctype, channel_name_ctype, frequency_list_handle_ctype, amplitude_ctype, dc_offset_ctype, start_phase_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_standard_waveform(self, session, channel_name, waveform, amplitude, frequency, dc_offset=0.0, start_phase=0.0):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        waveform_ctype = _visatype.ViInt32(waveform.value)  # case S130
        amplitude_ctype = _visatype.ViReal64(amplitude)  # case S150
        dc_offset_ctype = _visatype.ViReal64(dc_offset)  # case S150
        frequency_ctype = _visatype.ViReal64(frequency)  # case S150
        start_phase_ctype = _visatype.ViReal64(start_phase)  # case S150
        error_code = self._library.configure_standard_waveform(vi_ctype, channel_name_ctype, waveform_ctype, amplitude_ctype, dc_offset_ctype, frequency_ctype, start_phase_ctype)
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
        error_code = self._library.create_advanced_arb_sequence(vi_ctype, sequence_length_ctype, waveform_handles_array_ctype, loop_counts_array_ctype, sample_counts_array_ctype, marker_location_array_ctype, coerced_markers_array_ctype, None if sequence_handle_ctype is None else (ctypes.pointer(sequence_handle_ctype)))
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
        error_code = self._library.create_arb_sequence(vi_ctype, sequence_length_ctype, waveform_handles_array_ctype, loop_counts_array_ctype, None if sequence_handle_ctype is None else (ctypes.pointer(sequence_handle_ctype)))
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
        error_code = self._library.create_freq_list(vi_ctype, waveform_ctype, frequency_list_length_ctype, frequency_array_ctype, duration_array_ctype, None if frequency_list_handle_ctype is None else (ctypes.pointer(frequency_list_handle_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(frequency_list_handle_ctype.value)

    def _create_waveform_f64(self, session, channel_name, waveform_data_array):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        waveform_size_ctype = _visatype.ViInt32(0 if waveform_data_array is None else len(waveform_data_array))  # case S160
        waveform_data_array_array = get_ctypes_and_array(value=waveform_data_array, array_type="d")  # case B550
        waveform_data_array_ctype = get_ctypes_pointer_for_buffer(value=waveform_data_array_array, library_type=_visatype.ViReal64)  # case B550
        waveform_handle_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library._create_waveform_f64(vi_ctype, channel_name_ctype, waveform_size_ctype, waveform_data_array_ctype, None if waveform_handle_ctype is None else (ctypes.pointer(waveform_handle_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(waveform_handle_ctype.value)

    def _create_waveform_f64_numpy(self, session, channel_name, waveform_data_array):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        waveform_size_ctype = _visatype.ViInt32(0 if waveform_data_array is None else len(waveform_data_array))  # case S160
        waveform_data_array_ctype = get_ctypes_pointer_for_buffer(value=waveform_data_array)  # case B510
        waveform_handle_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library._create_waveform_f64(vi_ctype, channel_name_ctype, waveform_size_ctype, waveform_data_array_ctype, None if waveform_handle_ctype is None else (ctypes.pointer(waveform_handle_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(waveform_handle_ctype.value)

    def create_waveform_from_file_f64(self, session, channel_name, file_name, byte_order):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        file_name_ctype = ctypes.create_string_buffer(file_name.encode(self._encoding))  # case C020
        byte_order_ctype = _visatype.ViInt32(byte_order.value)  # case S130
        waveform_handle_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.create_waveform_from_file_f64(vi_ctype, channel_name_ctype, file_name_ctype, byte_order_ctype, None if waveform_handle_ctype is None else (ctypes.pointer(waveform_handle_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(waveform_handle_ctype.value)

    def create_waveform_from_file_i16(self, session, channel_name, file_name, byte_order):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        file_name_ctype = ctypes.create_string_buffer(file_name.encode(self._encoding))  # case C020
        byte_order_ctype = _visatype.ViInt32(byte_order.value)  # case S130
        waveform_handle_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.create_waveform_from_file_i16(vi_ctype, channel_name_ctype, file_name_ctype, byte_order_ctype, None if waveform_handle_ctype is None else (ctypes.pointer(waveform_handle_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(waveform_handle_ctype.value)

    def _create_waveform_i16_numpy(self, session, channel_name, waveform_data_array):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        waveform_size_ctype = _visatype.ViInt32(0 if waveform_data_array is None else len(waveform_data_array))  # case S160
        waveform_data_array_ctype = get_ctypes_pointer_for_buffer(value=waveform_data_array)  # case B510
        waveform_handle_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library._create_waveform_i16(vi_ctype, channel_name_ctype, waveform_size_ctype, waveform_data_array_ctype, None if waveform_handle_ctype is None else (ctypes.pointer(waveform_handle_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(waveform_handle_ctype.value)

    def define_user_standard_waveform(self, session, channel_name, waveform_data_array):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        waveform_size_ctype = _visatype.ViInt32(0 if waveform_data_array is None else len(waveform_data_array))  # case S160
        waveform_data_array_ctype = get_ctypes_pointer_for_buffer(value=waveform_data_array, library_type=_visatype.ViReal64)  # case B550
        error_code = self._library.define_user_standard_waveform(vi_ctype, channel_name_ctype, waveform_size_ctype, waveform_data_array_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _delete_named_waveform(self, session, channel_name, waveform_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        error_code = self._library._delete_named_waveform(vi_ctype, channel_name_ctype, waveform_name_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def delete_script(self, session, channel_name, script_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        script_name_ctype = ctypes.create_string_buffer(script_name.encode(self._encoding))  # case C020
        error_code = self._library.delete_script(vi_ctype, channel_name_ctype, script_name_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disable(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        error_code = self._library.disable(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def export_attribute_configuration_buffer(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        size_in_bytes_ctype = _visatype.ViInt32()  # case S170
        configuration_ctype = None  # case B580
        error_code = self._library.export_attribute_configuration_buffer(vi_ctype, size_in_bytes_ctype, configuration_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=False)
        size_in_bytes_ctype = _visatype.ViInt32(error_code)  # case S180
        configuration_size = size_in_bytes_ctype.value  # case B590
        configuration_array = array.array("b", [0] * configuration_size)  # case B590
        configuration_ctype = get_ctypes_pointer_for_buffer(value=configuration_array, library_type=_visatype.ViInt8)  # case B590
        error_code = self._library.export_attribute_configuration_buffer(vi_ctype, size_in_bytes_ctype, configuration_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return _converters.convert_to_bytes(configuration_array)

    def export_attribute_configuration_file(self, session, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.export_attribute_configuration_file(vi_ctype, file_path_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _get_attribute_vi_boolean(self, session, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library._get_attribute_vi_boolean(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(attribute_value_ctype.value)

    def _get_attribute_vi_int32(self, session, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library._get_attribute_vi_int32(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(attribute_value_ctype.value)

    def _get_attribute_vi_real64(self, session, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library._get_attribute_vi_real64(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return float(attribute_value_ctype.value)

    def _get_attribute_vi_string(self, session, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        array_size_ctype = _visatype.ViInt32()  # case S170
        attribute_value_ctype = None  # case C050
        error_code = self._library._get_attribute_vi_string(vi_ctype, channel_name_ctype, attribute_id_ctype, array_size_ctype, attribute_value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=False)
        array_size_ctype = _visatype.ViInt32(error_code)  # case S180
        attribute_value_ctype = (_visatype.ViChar * array_size_ctype.value)()  # case C060
        error_code = self._library._get_attribute_vi_string(vi_ctype, channel_name_ctype, attribute_id_ctype, array_size_ctype, attribute_value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return attribute_value_ctype.value.decode(self._encoding)

    def get_channel_name(self, session, index):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        index_ctype = _visatype.ViInt32(index)  # case S150
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        channel_string_ctype = None  # case C050
        error_code = self._library.get_channel_name(vi_ctype, index_ctype, buffer_size_ctype, channel_string_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        channel_string_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.get_channel_name(vi_ctype, index_ctype, buffer_size_ctype, channel_string_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return channel_string_ctype.value.decode(self._encoding)

    def _get_error(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        error_code_ctype = _visatype.ViStatus()  # case S220
        error_description_buffer_size_ctype = _visatype.ViInt32()  # case S170
        error_description_ctype = None  # case C050
        error_code = self._library._get_error(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), error_description_buffer_size_ctype, error_description_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=True)
        error_description_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        error_description_ctype = (_visatype.ViChar * error_description_buffer_size_ctype.value)()  # case C060
        error_code = self._library._get_error(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), error_description_buffer_size_ctype, error_description_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=True)
        return int(error_code_ctype.value), error_description_ctype.value.decode(self._encoding)

    def _get_ext_cal_last_date_and_time(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        year_ctype = _visatype.ViInt32()  # case S220
        month_ctype = _visatype.ViInt32()  # case S220
        day_ctype = _visatype.ViInt32()  # case S220
        hour_ctype = _visatype.ViInt32()  # case S220
        minute_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library._get_ext_cal_last_date_and_time(vi_ctype, None if year_ctype is None else (ctypes.pointer(year_ctype)), None if month_ctype is None else (ctypes.pointer(month_ctype)), None if day_ctype is None else (ctypes.pointer(day_ctype)), None if hour_ctype is None else (ctypes.pointer(hour_ctype)), None if minute_ctype is None else (ctypes.pointer(minute_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(year_ctype.value), int(month_ctype.value), int(day_ctype.value), int(hour_ctype.value), int(minute_ctype.value)

    def get_ext_cal_last_temp(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        temperature_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.get_ext_cal_last_temp(vi_ctype, None if temperature_ctype is None else (ctypes.pointer(temperature_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

    def get_ext_cal_recommended_interval(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        months_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.get_ext_cal_recommended_interval(vi_ctype, None if months_ctype is None else (ctypes.pointer(months_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return _converters.convert_month_to_timedelta(int(months_ctype.value))

    def get_hardware_state(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        state_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.get_hardware_state(vi_ctype, None if state_ctype is None else (ctypes.pointer(state_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return enums.HardwareState(state_ctype.value)

    def _get_self_cal_last_date_and_time(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        year_ctype = _visatype.ViInt32()  # case S220
        month_ctype = _visatype.ViInt32()  # case S220
        day_ctype = _visatype.ViInt32()  # case S220
        hour_ctype = _visatype.ViInt32()  # case S220
        minute_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library._get_self_cal_last_date_and_time(vi_ctype, None if year_ctype is None else (ctypes.pointer(year_ctype)), None if month_ctype is None else (ctypes.pointer(month_ctype)), None if day_ctype is None else (ctypes.pointer(day_ctype)), None if hour_ctype is None else (ctypes.pointer(hour_ctype)), None if minute_ctype is None else (ctypes.pointer(minute_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(year_ctype.value), int(month_ctype.value), int(day_ctype.value), int(hour_ctype.value), int(minute_ctype.value)

    def get_self_cal_last_temp(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        temperature_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.get_self_cal_last_temp(vi_ctype, None if temperature_ctype is None else (ctypes.pointer(temperature_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

    def get_self_cal_supported(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        self_cal_supported_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.get_self_cal_supported(vi_ctype, None if self_cal_supported_ctype is None else (ctypes.pointer(self_cal_supported_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(self_cal_supported_ctype.value)

    def import_attribute_configuration_buffer(self, session, configuration):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        size_in_bytes_ctype = _visatype.ViInt32(0 if configuration is None else len(configuration))  # case S160
        configuration_converted = _converters.convert_to_bytes(configuration)  # case B520
        configuration_ctype = get_ctypes_pointer_for_buffer(value=configuration_converted, library_type=_visatype.ViInt8)  # case B520
        error_code = self._library.import_attribute_configuration_buffer(vi_ctype, size_in_bytes_ctype, configuration_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def import_attribute_configuration_file(self, session, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.import_attribute_configuration_file(vi_ctype, file_path_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _initialize_with_channels(self, session, resource_name, channel_name=None, reset_device=False, option_string=""):  # noqa: N802
        resource_name_ctype = ctypes.create_string_buffer(resource_name.encode(self._encoding))  # case C020
        channel_name_ctype = ctypes.create_string_buffer(_converters.convert_repeated_capabilities_without_prefix(channel_name).encode(self._encoding))  # case C040
        reset_device_ctype = _visatype.ViBoolean(reset_device)  # case S150
        option_string_ctype = ctypes.create_string_buffer(_converters.convert_init_with_options_dictionary(option_string).encode(self._encoding))  # case C040
        vi_ctype = _visatype.ViSession()  # case S220
        error_code = self._library._initialize_with_channels(resource_name_ctype, channel_name_ctype, reset_device_ctype, option_string_ctype, None if vi_ctype is None else (ctypes.pointer(vi_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(vi_ctype.value)

    def _initiate_generation(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        error_code = self._library._initiate_generation(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def is_done(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        done_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.is_done(vi_ctype, None if done_ctype is None else (ctypes.pointer(done_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(done_ctype.value)

    def lock(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        caller_has_lock_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.lock(vi_ctype, None if caller_has_lock_ctype is None else (ctypes.pointer(caller_has_lock_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(caller_has_lock_ctype.value)

    def query_arb_seq_capabilities(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        maximum_number_of_sequences_ctype = _visatype.ViInt32()  # case S220
        minimum_sequence_length_ctype = _visatype.ViInt32()  # case S220
        maximum_sequence_length_ctype = _visatype.ViInt32()  # case S220
        maximum_loop_count_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.query_arb_seq_capabilities(vi_ctype, None if maximum_number_of_sequences_ctype is None else (ctypes.pointer(maximum_number_of_sequences_ctype)), None if minimum_sequence_length_ctype is None else (ctypes.pointer(minimum_sequence_length_ctype)), None if maximum_sequence_length_ctype is None else (ctypes.pointer(maximum_sequence_length_ctype)), None if maximum_loop_count_ctype is None else (ctypes.pointer(maximum_loop_count_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(maximum_number_of_sequences_ctype.value), int(minimum_sequence_length_ctype.value), int(maximum_sequence_length_ctype.value), int(maximum_loop_count_ctype.value)

    def query_arb_wfm_capabilities(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        maximum_number_of_waveforms_ctype = _visatype.ViInt32()  # case S220
        waveform_quantum_ctype = _visatype.ViInt32()  # case S220
        minimum_waveform_size_ctype = _visatype.ViInt32()  # case S220
        maximum_waveform_size_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.query_arb_wfm_capabilities(vi_ctype, None if maximum_number_of_waveforms_ctype is None else (ctypes.pointer(maximum_number_of_waveforms_ctype)), None if waveform_quantum_ctype is None else (ctypes.pointer(waveform_quantum_ctype)), None if minimum_waveform_size_ctype is None else (ctypes.pointer(minimum_waveform_size_ctype)), None if maximum_waveform_size_ctype is None else (ctypes.pointer(maximum_waveform_size_ctype)))
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
        error_code = self._library.query_freq_list_capabilities(vi_ctype, None if maximum_number_of_freq_lists_ctype is None else (ctypes.pointer(maximum_number_of_freq_lists_ctype)), None if minimum_frequency_list_length_ctype is None else (ctypes.pointer(minimum_frequency_list_length_ctype)), None if maximum_frequency_list_length_ctype is None else (ctypes.pointer(maximum_frequency_list_length_ctype)), None if minimum_frequency_list_duration_ctype is None else (ctypes.pointer(minimum_frequency_list_duration_ctype)), None if maximum_frequency_list_duration_ctype is None else (ctypes.pointer(maximum_frequency_list_duration_ctype)), None if frequency_list_duration_quantum_ctype is None else (ctypes.pointer(frequency_list_duration_quantum_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(maximum_number_of_freq_lists_ctype.value), int(minimum_frequency_list_length_ctype.value), int(maximum_frequency_list_length_ctype.value), float(minimum_frequency_list_duration_ctype.value), float(maximum_frequency_list_duration_ctype.value), float(frequency_list_duration_quantum_ctype.value)

    def read_current_temperature(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        temperature_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.read_current_temperature(vi_ctype, None if temperature_ctype is None else (ctypes.pointer(temperature_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

    def reset_device(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        error_code = self._library.reset_device(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def reset_with_defaults(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        error_code = self._library.reset_with_defaults(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def self_cal(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        error_code = self._library.self_cal(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def send_software_edge_trigger(self, session, trigger, trigger_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        trigger_ctype = _visatype.ViInt32(trigger.value)  # case S130
        trigger_id_ctype = ctypes.create_string_buffer(trigger_id.encode(self._encoding))  # case C020
        error_code = self._library.send_software_edge_trigger(vi_ctype, trigger_ctype, trigger_id_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_boolean(self, session, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViBoolean(attribute_value)  # case S150
        error_code = self._library._set_attribute_vi_boolean(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_int32(self, session, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt32(attribute_value)  # case S150
        error_code = self._library._set_attribute_vi_int32(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_real64(self, session, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViReal64(attribute_value)  # case S150
        error_code = self._library._set_attribute_vi_real64(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_string(self, session, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = ctypes.create_string_buffer(attribute_value.encode(self._encoding))  # case C020
        error_code = self._library._set_attribute_vi_string(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_named_waveform_next_write_position(self, session, channel_name, waveform_name, relative_to, offset):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        relative_to_ctype = _visatype.ViInt32(relative_to.value)  # case S130
        offset_ctype = _visatype.ViInt32(offset)  # case S150
        error_code = self._library._set_named_waveform_next_write_position(vi_ctype, channel_name_ctype, waveform_name_ctype, relative_to_ctype, offset_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_waveform_next_write_position(self, session, channel_name, waveform_handle, relative_to, offset):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        waveform_handle_ctype = _visatype.ViInt32(waveform_handle)  # case S150
        relative_to_ctype = _visatype.ViInt32(relative_to.value)  # case S130
        offset_ctype = _visatype.ViInt32(offset)  # case S150
        error_code = self._library._set_waveform_next_write_position(vi_ctype, channel_name_ctype, waveform_handle_ctype, relative_to_ctype, offset_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def unlock(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        caller_has_lock_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.unlock(vi_ctype, None if caller_has_lock_ctype is None else (ctypes.pointer(caller_has_lock_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(caller_has_lock_ctype.value)

    def wait_until_done(self, session, max_time=hightime.timedelta(seconds=10.0)):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        max_time_ctype = _converters.convert_timedelta_to_milliseconds_int32(max_time)  # case S140
        error_code = self._library.wait_until_done(vi_ctype, max_time_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _write_binary16_waveform_numpy(self, session, channel_name, waveform_handle, data):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        waveform_handle_ctype = _visatype.ViInt32(waveform_handle)  # case S150
        size_ctype = _visatype.ViInt32(0 if data is None else len(data))  # case S160
        data_ctype = get_ctypes_pointer_for_buffer(value=data)  # case B510
        error_code = self._library._write_binary16_waveform(vi_ctype, channel_name_ctype, waveform_handle_ctype, size_ctype, data_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _write_named_waveform_f64(self, session, channel_name, waveform_name, data):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        size_ctype = _visatype.ViInt32(0 if data is None else len(data))  # case S160
        data_array = get_ctypes_and_array(value=data, array_type="d")  # case B550
        data_ctype = get_ctypes_pointer_for_buffer(value=data_array, library_type=_visatype.ViReal64)  # case B550
        error_code = self._library._write_named_waveform_f64(vi_ctype, channel_name_ctype, waveform_name_ctype, size_ctype, data_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _write_named_waveform_f64_numpy(self, session, channel_name, waveform_name, data):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        size_ctype = _visatype.ViInt32(0 if data is None else len(data))  # case S160
        data_ctype = get_ctypes_pointer_for_buffer(value=data)  # case B510
        error_code = self._library._write_named_waveform_f64(vi_ctype, channel_name_ctype, waveform_name_ctype, size_ctype, data_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _write_named_waveform_i16_numpy(self, session, channel_name, waveform_name, data):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        size_ctype = _visatype.ViInt32(0 if data is None else len(data))  # case S160
        data_ctype = get_ctypes_pointer_for_buffer(value=data)  # case B510
        error_code = self._library._write_named_waveform_i16(vi_ctype, channel_name_ctype, waveform_name_ctype, size_ctype, data_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def write_script(self, session, channel_name, script):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        script_ctype = ctypes.create_string_buffer(script.encode(self._encoding))  # case C020
        error_code = self._library.write_script(vi_ctype, channel_name_ctype, script_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _write_waveform(self, session, channel_name, waveform_handle, data):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        waveform_handle_ctype = _visatype.ViInt32(waveform_handle)  # case S150
        size_ctype = _visatype.ViInt32(0 if data is None else len(data))  # case S160
        data_array = get_ctypes_and_array(value=data, array_type="d")  # case B550
        data_ctype = get_ctypes_pointer_for_buffer(value=data_array, library_type=_visatype.ViReal64)  # case B550
        error_code = self._library._write_waveform(vi_ctype, channel_name_ctype, waveform_handle_ctype, size_ctype, data_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _write_waveform_numpy(self, session, channel_name, waveform_handle, data):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        waveform_handle_ctype = _visatype.ViInt32(waveform_handle)  # case S150
        size_ctype = _visatype.ViInt32(0 if data is None else len(data))  # case S160
        data_ctype = get_ctypes_pointer_for_buffer(value=data)  # case B510
        error_code = self._library._write_waveform(vi_ctype, channel_name_ctype, waveform_handle_ctype, size_ctype, data_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _close(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        error_code = self._library._close(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _error_message(self, session, error_code):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        error_code_ctype = _visatype.ViStatus(error_code)  # case S150
        error_message_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library._error_message(vi_ctype, error_code_ctype, error_message_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=True)
        return error_message_ctype.value.decode(self._encoding)

    def reset(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        error_code = self._library.reset(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _self_test(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        self_test_result_ctype = _visatype.ViInt16()  # case S220
        self_test_message_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library._self_test(vi_ctype, None if self_test_result_ctype is None else (ctypes.pointer(self_test_result_ctype)), self_test_message_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(self_test_result_ctype.value), self_test_message_ctype.value.decode(self._encoding)
