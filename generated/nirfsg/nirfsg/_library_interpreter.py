# -*- coding: utf-8 -*-
# This file was generated

import array
import ctypes
import hightime  # noqa: F401
import nirfsg._complextype as _complextype
import nirfsg._library_singleton as _library_singleton
import nirfsg._visatype as _visatype
import nirfsg.enums as enums  # noqa: F401
import nirfsg.errors as errors


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
        error_code = self._library.niRFSG_Abort(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def allocate_arb_waveform(self, waveform_name, size_in_samples):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        size_in_samples_ctype = _visatype.ViInt32(size_in_samples)  # case S150
        error_code = self._library.niRFSG_AllocateArbWaveform(vi_ctype, waveform_name_ctype, size_in_samples_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def change_external_calibration_password(self, old_password, new_password):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        old_password_ctype = ctypes.create_string_buffer(old_password.encode(self._encoding))  # case C020
        new_password_ctype = ctypes.create_string_buffer(new_password.encode(self._encoding))  # case C020
        error_code = self._library.niRFSG_ChangeExternalCalibrationPassword(vi_ctype, old_password_ctype, new_password_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def check_attribute_vi_boolean(self, channel_name, attribute, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViBoolean(value)  # case S150
        error_code = self._library.niRFSG_CheckAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def check_attribute_vi_int32(self, channel_name, attribute, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViInt32(value)  # case S150
        error_code = self._library.niRFSG_CheckAttributeViInt32(vi_ctype, channel_name_ctype, attribute_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def check_attribute_vi_int64(self, channel_name, attribute, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViInt64(value)  # case S150
        error_code = self._library.niRFSG_CheckAttributeViInt64(vi_ctype, channel_name_ctype, attribute_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def check_attribute_vi_real64(self, channel_name, attribute, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViReal64(value)  # case S150
        error_code = self._library.niRFSG_CheckAttributeViReal64(vi_ctype, channel_name_ctype, attribute_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def check_attribute_vi_session(self, channel_name, attribute):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSG_CheckAttributeViSession(vi_ctype, channel_name_ctype, attribute_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def check_attribute_vi_string(self, channel_name, attribute, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = ctypes.create_string_buffer(value.encode(self._encoding))  # case C020
        error_code = self._library.niRFSG_CheckAttributeViString(vi_ctype, channel_name_ctype, attribute_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def check_generation_status(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        is_done_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niRFSG_CheckGenerationStatus(vi_ctype, None if is_done_ctype is None else (ctypes.pointer(is_done_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(is_done_ctype.value)

    def check_if_script_exists(self, script_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        script_name_ctype = ctypes.create_string_buffer(script_name.encode(self._encoding))  # case C020
        script_exists_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niRFSG_CheckIfScriptExists(vi_ctype, script_name_ctype, None if script_exists_ctype is None else (ctypes.pointer(script_exists_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(script_exists_ctype.value)

    def check_if_waveform_exists(self, waveform_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        waveform_exists_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niRFSG_CheckIfWaveformExists(vi_ctype, waveform_name_ctype, None if waveform_exists_ctype is None else (ctypes.pointer(waveform_exists_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(waveform_exists_ctype.value)

    def clear_all_arb_waveforms(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSG_ClearAllArbWaveforms(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def clear_arb_waveform(self, name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        name_ctype = ctypes.create_string_buffer(name.encode(self._encoding))  # case C020
        error_code = self._library.niRFSG_ClearArbWaveform(vi_ctype, name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def clear_error(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSG_ClearError(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def clear_self_calibrate_range(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSG_ClearSelfCalibrateRange(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def commit(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSG_Commit(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_deembedding_table_interpolation_linear(self, port, table_name, format):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        port_ctype = ctypes.create_string_buffer(port.encode(self._encoding))  # case C020
        table_name_ctype = ctypes.create_string_buffer(table_name.encode(self._encoding))  # case C020
        format_ctype = _visatype.ViInt32(format.value)  # case S130
        error_code = self._library.niRFSG_ConfigureDeembeddingTableInterpolationLinear(vi_ctype, port_ctype, table_name_ctype, format_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_deembedding_table_interpolation_nearest(self, port, table_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        port_ctype = ctypes.create_string_buffer(port.encode(self._encoding))  # case C020
        table_name_ctype = ctypes.create_string_buffer(table_name.encode(self._encoding))  # case C020
        error_code = self._library.niRFSG_ConfigureDeembeddingTableInterpolationNearest(vi_ctype, port_ctype, table_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_deembedding_table_interpolation_spline(self, port, table_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        port_ctype = ctypes.create_string_buffer(port.encode(self._encoding))  # case C020
        table_name_ctype = ctypes.create_string_buffer(table_name.encode(self._encoding))  # case C020
        error_code = self._library.niRFSG_ConfigureDeembeddingTableInterpolationSpline(vi_ctype, port_ctype, table_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_digital_edge_script_trigger(self, trigger_id, source, edge):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        trigger_id_ctype = ctypes.create_string_buffer(trigger_id.encode(self._encoding))  # case C010
        source_ctype = ctypes.create_string_buffer(source.encode(self._encoding))  # case C020
        edge_ctype = _visatype.ViInt32(edge.value)  # case S130
        error_code = self._library.niRFSG_ConfigureDigitalEdgeScriptTrigger(vi_ctype, trigger_id_ctype, source_ctype, edge_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_digital_edge_start_trigger(self, source, edge):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        source_ctype = ctypes.create_string_buffer(source.encode(self._encoding))  # case C020
        edge_ctype = _visatype.ViInt32(edge.value)  # case S130
        error_code = self._library.niRFSG_ConfigureDigitalEdgeStartTrigger(vi_ctype, source_ctype, edge_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_digital_level_script_trigger(self, trigger_id, source, level):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        trigger_id_ctype = ctypes.create_string_buffer(trigger_id.encode(self._encoding))  # case C010
        source_ctype = ctypes.create_string_buffer(source.encode(self._encoding))  # case C020
        level_ctype = _visatype.ViInt32(level)  # case S150
        error_code = self._library.niRFSG_ConfigureDigitalLevelScriptTrigger(vi_ctype, trigger_id_ctype, source_ctype, level_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_digital_modulation_user_defined_waveform(self, number_of_samples, user_defined_waveform):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        number_of_samples_ctype = _visatype.ViInt32(0 if user_defined_waveform is None else len(user_defined_waveform))  # case S160
        user_defined_waveform_ctype = _get_ctypes_pointer_for_buffer(value=user_defined_waveform, library_type=_visatype.ViInt8)  # case B550
        error_code = self._library.niRFSG_ConfigureDigitalModulationUserDefinedWaveform(vi_ctype, number_of_samples_ctype, user_defined_waveform_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_pxi_chassis_clk10(self, pxi_clk10_source):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pxi_clk10_source_ctype = ctypes.create_string_buffer(pxi_clk10_source.encode(self._encoding))  # case C020
        error_code = self._library.niRFSG_ConfigurePxiChassisClk10(vi_ctype, pxi_clk10_source_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_rf(self, frequency, power_level):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        frequency_ctype = _visatype.ViReal64(frequency)  # case S150
        power_level_ctype = _visatype.ViReal64(power_level)  # case S150
        error_code = self._library.niRFSG_ConfigureRF(vi_ctype, frequency_ctype, power_level_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_ref_clock(self, ref_clock_source, ref_clock_rate):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        ref_clock_source_ctype = ctypes.create_string_buffer(ref_clock_source.encode(self._encoding))  # case C020
        ref_clock_rate_ctype = _visatype.ViReal64(ref_clock_rate)  # case S150
        error_code = self._library.niRFSG_ConfigureRefClock(vi_ctype, ref_clock_source_ctype, ref_clock_rate_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_software_script_trigger(self, trigger_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        trigger_id_ctype = ctypes.create_string_buffer(trigger_id.encode(self._encoding))  # case C010
        error_code = self._library.niRFSG_ConfigureSoftwareScriptTrigger(vi_ctype, trigger_id_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_software_start_trigger(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSG_ConfigureSoftwareStartTrigger(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_deembedding_sparameter_table_array(self, port, table_name, frequencies, sparameter_table, sparameter_table_size, number_of_ports, sparameter_orientation):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        port_ctype = ctypes.create_string_buffer(port.encode(self._encoding))  # case C020
        table_name_ctype = ctypes.create_string_buffer(table_name.encode(self._encoding))  # case C020
        frequencies_ctype = _get_ctypes_pointer_for_buffer(value=frequencies)  # case B510
        frequencies_size_ctype = _visatype.ViInt32(0 if frequencies is None else len(frequencies))  # case S160
        sparameter_table_ctype = _get_ctypes_pointer_for_buffer(value=sparameter_table, library_type=_complextype.NIComplexNumber)  # case B510
        sparameter_table_size_ctype = _visatype.ViInt32(sparameter_table_size)  # case S150
        number_of_ports_ctype = _visatype.ViInt32(number_of_ports)  # case S150
        sparameter_orientation_ctype = _visatype.ViInt32(sparameter_orientation.value)  # case S130
        error_code = self._library.niRFSG_CreateDeembeddingSparameterTableArray(vi_ctype, port_ctype, table_name_ctype, frequencies_ctype, frequencies_size_ctype, sparameter_table_ctype, sparameter_table_size_ctype, number_of_ports_ctype, sparameter_orientation_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_deembedding_sparameter_table_s2p_file(self, port, table_name, s2p_file_path, sparameter_orientation):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        port_ctype = ctypes.create_string_buffer(port.encode(self._encoding))  # case C020
        table_name_ctype = ctypes.create_string_buffer(table_name.encode(self._encoding))  # case C020
        s2p_file_path_ctype = ctypes.create_string_buffer(s2p_file_path.encode(self._encoding))  # case C020
        sparameter_orientation_ctype = _visatype.ViInt32(sparameter_orientation.value)  # case S130
        error_code = self._library.niRFSG_CreateDeembeddingSparameterTableS2PFile(vi_ctype, port_ctype, table_name_ctype, s2p_file_path_ctype, sparameter_orientation_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def delete_all_deembedding_tables(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSG_DeleteAllDeembeddingTables(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def delete_deembedding_table(self, port, table_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        port_ctype = ctypes.create_string_buffer(port.encode(self._encoding))  # case C020
        table_name_ctype = ctypes.create_string_buffer(table_name.encode(self._encoding))  # case C020
        error_code = self._library.niRFSG_DeleteDeembeddingTable(vi_ctype, port_ctype, table_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disable(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSG_Disable(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disable_script_trigger(self, trigger_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        trigger_id_ctype = ctypes.create_string_buffer(trigger_id.encode(self._encoding))  # case C010
        error_code = self._library.niRFSG_DisableScriptTrigger(vi_ctype, trigger_id_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disable_start_trigger(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSG_DisableStartTrigger(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def error_message(self, error_code, error_message):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code_ctype = _visatype.ViStatus(error_code)  # case S150
        error_message_ctype = ctypes.create_string_buffer(error_message.encode(self._encoding))  # case C020
        error_code = self._library.niRFSG_ErrorMessage(vi_ctype, error_code_ctype, error_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return

    def error_query(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code_ctype = _visatype.ViInt32()  # case S220
        error_message_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library.niRFSG_ErrorQuery(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), error_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(error_code_ctype.value), error_message_ctype.value.decode(self._encoding)

    def get_all_named_waveform_names(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        waveform_names_ctype = None  # case C050
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        actual_buffer_size_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niRFSG_GetAllNamedWaveformNames(vi_ctype, waveform_names_ctype, buffer_size_ctype, None if actual_buffer_size_ctype is None else (ctypes.pointer(actual_buffer_size_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        waveform_names_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niRFSG_GetAllNamedWaveformNames(vi_ctype, waveform_names_ctype, buffer_size_ctype, None if actual_buffer_size_ctype is None else (ctypes.pointer(actual_buffer_size_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return waveform_names_ctype.value.decode(self._encoding), int(actual_buffer_size_ctype.value)

    def get_all_script_names(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        script_names_ctype = None  # case C050
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        actual_buffer_size_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niRFSG_GetAllScriptNames(vi_ctype, script_names_ctype, buffer_size_ctype, None if actual_buffer_size_ctype is None else (ctypes.pointer(actual_buffer_size_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        script_names_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niRFSG_GetAllScriptNames(vi_ctype, script_names_ctype, buffer_size_ctype, None if actual_buffer_size_ctype is None else (ctypes.pointer(actual_buffer_size_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return script_names_ctype.value.decode(self._encoding), int(actual_buffer_size_ctype.value)

    def get_attribute_vi_boolean(self, channel_name, attribute):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niRFSG_GetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(value_ctype.value)

    def get_attribute_vi_int32(self, channel_name, attribute):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niRFSG_GetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(value_ctype.value)

    def get_attribute_vi_int64(self, channel_name, attribute):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViInt64()  # case S220
        error_code = self._library.niRFSG_GetAttributeViInt64(vi_ctype, channel_name_ctype, attribute_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(value_ctype.value)

    def get_attribute_vi_real64(self, channel_name, attribute):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niRFSG_GetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(value_ctype.value)

    def get_attribute_vi_session(self, channel_name, attribute):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViSession()  # case S220
        error_code = self._library.niRFSG_GetAttributeViSession(vi_ctype, channel_name_ctype, attribute_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(value_ctype.value)

    def get_attribute_vi_string(self, channel_name, attribute):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        buf_size_ctype = _visatype.ViInt32()  # case S170
        value_ctype = None  # case C050
        error_code = self._library.niRFSG_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_ctype, buf_size_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buf_size_ctype = _visatype.ViInt32(error_code)  # case S180
        value_ctype = (_visatype.ViChar * buf_size_ctype.value)()  # case C060
        error_code = self._library.niRFSG_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_ctype, buf_size_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return value_ctype.value.decode(self._encoding)

    def get_channel_name(self, index):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        index_ctype = _visatype.ViInt32(index)  # case S150
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        name_ctype = None  # case C050
        error_code = self._library.niRFSG_GetChannelName(vi_ctype, index_ctype, buffer_size_ctype, name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        name_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niRFSG_GetChannelName(vi_ctype, index_ctype, buffer_size_ctype, name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return name_ctype.value.decode(self._encoding)

    def get_deembedding_sparameters(self, sparameters, sparameters_array_size):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        sparameters_ctype = _get_ctypes_pointer_for_buffer(value=sparameters, library_type=_complextype.NIComplexNumber)  # case B510
        sparameters_array_size_ctype = _visatype.ViInt32(sparameters_array_size)  # case S150
        number_of_sparameters_ctype = _visatype.ViInt32()  # case S220
        number_of_ports_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niRFSG_GetDeembeddingSparameters(vi_ctype, sparameters_ctype, sparameters_array_size_ctype, None if number_of_sparameters_ctype is None else (ctypes.pointer(number_of_sparameters_ctype)), None if number_of_ports_ctype is None else (ctypes.pointer(number_of_ports_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(number_of_sparameters_ctype.value), int(number_of_ports_ctype.value)

    def get_deembedding_table_number_of_ports(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        number_of_ports_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niRFSG_GetDeembeddingTableNumberOfPorts(vi_ctype, None if number_of_ports_ctype is None else (ctypes.pointer(number_of_ports_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(number_of_ports_ctype.value)

    def get_error(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code_ctype = _visatype.ViStatus()  # case S220
        error_description_buffer_size_ctype = _visatype.ViInt32()  # case S170
        error_description_ctype = None  # case C050
        error_code = self._library.niRFSG_GetError(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), error_description_buffer_size_ctype, error_description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=True)
        error_description_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        error_description_ctype = (_visatype.ViChar * error_description_buffer_size_ctype.value)()  # case C060
        error_code = self._library.niRFSG_GetError(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), error_description_buffer_size_ctype, error_description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return int(error_code_ctype.value), error_description_ctype.value.decode(self._encoding)

    def get_external_calibration_last_date_and_time(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        year_ctype = _visatype.ViInt32()  # case S220
        month_ctype = _visatype.ViInt32()  # case S220
        day_ctype = _visatype.ViInt32()  # case S220
        hour_ctype = _visatype.ViInt32()  # case S220
        minute_ctype = _visatype.ViInt32()  # case S220
        second_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niRFSG_GetExternalCalibrationLastDateAndTime(vi_ctype, None if year_ctype is None else (ctypes.pointer(year_ctype)), None if month_ctype is None else (ctypes.pointer(month_ctype)), None if day_ctype is None else (ctypes.pointer(day_ctype)), None if hour_ctype is None else (ctypes.pointer(hour_ctype)), None if minute_ctype is None else (ctypes.pointer(minute_ctype)), None if second_ctype is None else (ctypes.pointer(second_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(year_ctype.value), int(month_ctype.value), int(day_ctype.value), int(hour_ctype.value), int(minute_ctype.value), int(second_ctype.value)

    def get_max_settable_power(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        value_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niRFSG_GetMaxSettablePower(vi_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(value_ctype.value)

    def get_self_calibration_date_and_time(self, module):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        module_ctype = _visatype.ViInt32(module.value)  # case S130
        year_ctype = _visatype.ViInt32()  # case S220
        month_ctype = _visatype.ViInt32()  # case S220
        day_ctype = _visatype.ViInt32()  # case S220
        hour_ctype = _visatype.ViInt32()  # case S220
        minute_ctype = _visatype.ViInt32()  # case S220
        second_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niRFSG_GetSelfCalibrationDateAndTime(vi_ctype, module_ctype, None if year_ctype is None else (ctypes.pointer(year_ctype)), None if month_ctype is None else (ctypes.pointer(month_ctype)), None if day_ctype is None else (ctypes.pointer(day_ctype)), None if hour_ctype is None else (ctypes.pointer(hour_ctype)), None if minute_ctype is None else (ctypes.pointer(minute_ctype)), None if second_ctype is None else (ctypes.pointer(second_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(year_ctype.value), int(month_ctype.value), int(day_ctype.value), int(hour_ctype.value), int(minute_ctype.value), int(second_ctype.value)

    def get_self_calibration_temperature(self, module):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        module_ctype = _visatype.ViInt32(module.value)  # case S130
        temperature_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niRFSG_GetSelfCalibrationTemperature(vi_ctype, module_ctype, None if temperature_ctype is None else (ctypes.pointer(temperature_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

    def get_terminal_name(self, signal, signal_identifier):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        signal_ctype = _visatype.ViInt32(signal.value)  # case S130
        signal_identifier_ctype = ctypes.create_string_buffer(signal_identifier.encode(self._encoding))  # case C020
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        terminal_name_ctype = None  # case C050
        error_code = self._library.niRFSG_GetTerminalName(vi_ctype, signal_ctype, signal_identifier_ctype, buffer_size_ctype, terminal_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        terminal_name_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niRFSG_GetTerminalName(vi_ctype, signal_ctype, signal_identifier_ctype, buffer_size_ctype, terminal_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return terminal_name_ctype.value.decode(self._encoding)

    def get_waveform_burst_start_locations(self, channel_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        number_of_locations_ctype = _visatype.ViInt32(0)  # case S190
        locations_ctype = None  # case B610
        required_size_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niRFSG_GetWaveformBurstStartLocations(vi_ctype, channel_name_ctype, number_of_locations_ctype, locations_ctype, None if required_size_ctype is None else (ctypes.pointer(required_size_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        number_of_locations_ctype = _visatype.ViInt32(required_size_ctype.value)  # case S200
        locations_size = required_size_ctype.value  # case B620
        locations_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=locations_size)  # case B620
        error_code = self._library.niRFSG_GetWaveformBurstStartLocations(vi_ctype, channel_name_ctype, number_of_locations_ctype, locations_ctype, None if required_size_ctype is None else (ctypes.pointer(required_size_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(locations_ctype[i]) for i in range(number_of_locations_ctype.value)]

    def get_waveform_burst_stop_locations(self, channel_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        number_of_locations_ctype = _visatype.ViInt32(0)  # case S190
        locations_ctype = None  # case B610
        required_size_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niRFSG_GetWaveformBurstStopLocations(vi_ctype, channel_name_ctype, number_of_locations_ctype, locations_ctype, None if required_size_ctype is None else (ctypes.pointer(required_size_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        number_of_locations_ctype = _visatype.ViInt32(required_size_ctype.value)  # case S200
        locations_size = required_size_ctype.value  # case B620
        locations_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=locations_size)  # case B620
        error_code = self._library.niRFSG_GetWaveformBurstStopLocations(vi_ctype, channel_name_ctype, number_of_locations_ctype, locations_ctype, None if required_size_ctype is None else (ctypes.pointer(required_size_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(locations_ctype[i]) for i in range(number_of_locations_ctype.value)]

    def get_waveform_marker_event_locations(self, channel_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        number_of_locations_ctype = _visatype.ViInt32(0)  # case S190
        locations_ctype = None  # case B610
        required_size_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niRFSG_GetWaveformMarkerEventLocations(vi_ctype, channel_name_ctype, number_of_locations_ctype, locations_ctype, None if required_size_ctype is None else (ctypes.pointer(required_size_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        number_of_locations_ctype = _visatype.ViInt32(required_size_ctype.value)  # case S200
        locations_size = required_size_ctype.value  # case B620
        locations_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=locations_size)  # case B620
        error_code = self._library.niRFSG_GetWaveformMarkerEventLocations(vi_ctype, channel_name_ctype, number_of_locations_ctype, locations_ctype, None if required_size_ctype is None else (ctypes.pointer(required_size_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(locations_ctype[i]) for i in range(number_of_locations_ctype.value)]

    def init_with_options(self, resource_name, id_query, reset_device, option_string):  # noqa: N802
        resource_name_ctype = ctypes.create_string_buffer(resource_name.encode(self._encoding))  # case C020
        id_query_ctype = _visatype.ViBoolean(id_query)  # case S150
        reset_device_ctype = _visatype.ViBoolean(reset_device)  # case S150
        option_string_ctype = ctypes.create_string_buffer(option_string.encode(self._encoding))  # case C020
        new_vi_ctype = _visatype.ViSession()  # case S220
        error_code = self._library.niRFSG_InitWithOptions(resource_name_ctype, id_query_ctype, reset_device_ctype, option_string_ctype, None if new_vi_ctype is None else (ctypes.pointer(new_vi_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(new_vi_ctype.value)

    def initiate(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSG_Initiate(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def load_configurations_from_file(self, channel_name, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.niRFSG_LoadConfigurationsFromFile(vi_ctype, channel_name_ctype, file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def lock(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSG_LockSession(vi_ctype, None)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def perform_power_search(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSG_PerformPowerSearch(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def perform_thermal_correction(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSG_PerformThermalCorrection(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def query_arb_waveform_capabilities(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        max_number_waveforms_ctype = _visatype.ViInt32()  # case S220
        waveform_quantum_ctype = _visatype.ViInt32()  # case S220
        min_waveform_size_ctype = _visatype.ViInt32()  # case S220
        max_waveform_size_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niRFSG_QueryArbWaveformCapabilities(vi_ctype, None if max_number_waveforms_ctype is None else (ctypes.pointer(max_number_waveforms_ctype)), None if waveform_quantum_ctype is None else (ctypes.pointer(waveform_quantum_ctype)), None if min_waveform_size_ctype is None else (ctypes.pointer(min_waveform_size_ctype)), None if max_waveform_size_ctype is None else (ctypes.pointer(max_waveform_size_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(max_number_waveforms_ctype.value), int(waveform_quantum_ctype.value), int(min_waveform_size_ctype.value), int(max_waveform_size_ctype.value)

    def read_and_download_waveform_from_file_tdms(self, waveform_name, file_path, waveform_index):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        waveform_index_ctype = _visatype.ViUInt32(waveform_index)  # case S150
        error_code = self._library.niRFSG_ReadAndDownloadWaveformFromFileTDMS(vi_ctype, waveform_name_ctype, file_path_ctype, waveform_index_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def reset_attribute(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        error_code = self._library.niRFSG_ResetAttribute(vi_ctype, channel_name_ctype, attribute_id_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def reset_device(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSG_ResetDevice(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def reset_with_defaults(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSG_ResetWithDefaults(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def reset_with_options(self, steps_to_omit):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        steps_to_omit_ctype = _visatype.ViUInt64(steps_to_omit.value)  # case S130
        error_code = self._library.niRFSG_ResetWithOptions(vi_ctype, steps_to_omit_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def revision_query(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        instrument_driver_revision_ctype = (_visatype.ViChar * 256)()  # case C070
        firmware_revision_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library.niRFSG_RevisionQuery(vi_ctype, instrument_driver_revision_ctype, firmware_revision_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return instrument_driver_revision_ctype.value.decode(self._encoding), firmware_revision_ctype.value.decode(self._encoding)

    def save_configurations_to_file(self, channel_name, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.niRFSG_SaveConfigurationsToFile(vi_ctype, channel_name_ctype, file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def select_arb_waveform(self, name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        name_ctype = ctypes.create_string_buffer(name.encode(self._encoding))  # case C020
        error_code = self._library.niRFSG_SelectArbWaveform(vi_ctype, name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def self_cal(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSG_SelfCal(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def self_calibrate_range(self, steps_to_omit, min_frequency, max_frequency, min_power_level, max_power_level):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        steps_to_omit_ctype = _visatype.ViInt64(steps_to_omit.value)  # case S130
        min_frequency_ctype = _visatype.ViReal64(min_frequency)  # case S150
        max_frequency_ctype = _visatype.ViReal64(max_frequency)  # case S150
        min_power_level_ctype = _visatype.ViReal64(min_power_level)  # case S150
        max_power_level_ctype = _visatype.ViReal64(max_power_level)  # case S150
        error_code = self._library.niRFSG_SelfCalibrateRange(vi_ctype, steps_to_omit_ctype, min_frequency_ctype, max_frequency_ctype, min_power_level_ctype, max_power_level_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def self_test(self, self_test_message):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        self_test_result_ctype = _visatype.ViInt16()  # case S220
        self_test_message_ctype = ctypes.create_string_buffer(self_test_message.encode(self._encoding))  # case C020
        error_code = self._library.niRFSG_SelfTest(vi_ctype, None if self_test_result_ctype is None else (ctypes.pointer(self_test_result_ctype)), self_test_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(self_test_result_ctype.value)

    def send_software_edge_trigger(self, trigger, trigger_identifier):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        trigger_ctype = _visatype.ViInt32(trigger.value)  # case S130
        trigger_identifier_ctype = ctypes.create_string_buffer(trigger_identifier.encode(self._encoding))  # case C020
        error_code = self._library.niRFSG_SendSoftwareEdgeTrigger(vi_ctype, trigger_ctype, trigger_identifier_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_arb_waveform_next_write_position(self, waveform_name, relative_to, offset):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        relative_to_ctype = _visatype.ViInt32(relative_to.value)  # case S130
        offset_ctype = _visatype.ViInt32(offset)  # case S150
        error_code = self._library.niRFSG_SetArbWaveformNextWritePosition(vi_ctype, waveform_name_ctype, relative_to_ctype, offset_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_boolean(self, channel_name, attribute, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViBoolean(value)  # case S150
        error_code = self._library.niRFSG_SetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_int32(self, channel_name, attribute, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViInt32(value)  # case S150
        error_code = self._library.niRFSG_SetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_int64(self, channel_name, attribute, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViInt64(value)  # case S150
        error_code = self._library.niRFSG_SetAttributeViInt64(vi_ctype, channel_name_ctype, attribute_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_real64(self, channel_name, attribute, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViReal64(value)  # case S150
        error_code = self._library.niRFSG_SetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_session(self, channel_name, attribute):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSG_SetAttributeViSession(vi_ctype, channel_name_ctype, attribute_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_string(self, channel_name, attribute, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = ctypes.create_string_buffer(value.encode(self._encoding))  # case C020
        error_code = self._library.niRFSG_SetAttributeViString(vi_ctype, channel_name_ctype, attribute_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_waveform_burst_start_locations(self, channel_name, locations):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        number_of_locations_ctype = _visatype.ViInt32(0 if locations is None else len(locations))  # case S160
        locations_ctype = _get_ctypes_pointer_for_buffer(value=locations, library_type=_visatype.ViReal64)  # case B550
        error_code = self._library.niRFSG_SetWaveformBurstStartLocations(vi_ctype, channel_name_ctype, number_of_locations_ctype, locations_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_waveform_burst_stop_locations(self, channel_name, locations):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        number_of_locations_ctype = _visatype.ViInt32(0 if locations is None else len(locations))  # case S160
        locations_ctype = _get_ctypes_pointer_for_buffer(value=locations, library_type=_visatype.ViReal64)  # case B550
        error_code = self._library.niRFSG_SetWaveformBurstStopLocations(vi_ctype, channel_name_ctype, number_of_locations_ctype, locations_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_waveform_marker_event_locations(self, channel_name, locations):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        number_of_locations_ctype = _visatype.ViInt32(0 if locations is None else len(locations))  # case S160
        locations_ctype = _get_ctypes_pointer_for_buffer(value=locations, library_type=_visatype.ViReal64)  # case B550
        error_code = self._library.niRFSG_SetWaveformMarkerEventLocations(vi_ctype, channel_name_ctype, number_of_locations_ctype, locations_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def unlock(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSG_UnlockSession(vi_ctype, None)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def wait_until_settled(self, max_time_milliseconds):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        max_time_milliseconds_ctype = _visatype.ViInt32(max_time_milliseconds)  # case S150
        error_code = self._library.niRFSG_WaitUntilSettled(vi_ctype, max_time_milliseconds_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def write_arb_waveform_complex_f32(self, waveform_name, waveform_data_array, more_data_pending):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        number_of_samples_ctype = _visatype.ViInt32(0 if waveform_data_array is None else len(waveform_data_array))  # case S160
        waveform_data_array_ctype = _get_ctypes_pointer_for_buffer(value=waveform_data_array, library_type=_complextype.NIComplexNumberF32)  # case B510
        more_data_pending_ctype = _visatype.ViBoolean(more_data_pending)  # case S150
        error_code = self._library.niRFSG_WriteArbWaveformComplexF32(vi_ctype, waveform_name_ctype, number_of_samples_ctype, waveform_data_array_ctype, more_data_pending_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def write_arb_waveform_complex_f64(self, waveform_name, waveform_data_array, more_data_pending):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        number_of_samples_ctype = _visatype.ViInt32(0 if waveform_data_array is None else len(waveform_data_array))  # case S160
        waveform_data_array_ctype = _get_ctypes_pointer_for_buffer(value=waveform_data_array, library_type=_complextype.NIComplexNumber)  # case B510
        more_data_pending_ctype = _visatype.ViBoolean(more_data_pending)  # case S150
        error_code = self._library.niRFSG_WriteArbWaveformComplexF64(vi_ctype, waveform_name_ctype, number_of_samples_ctype, waveform_data_array_ctype, more_data_pending_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def write_arb_waveform_complex_i16(self, waveform_name, waveform_data_array):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        number_of_samples_ctype = _visatype.ViInt32(0 if waveform_data_array is None else len(waveform_data_array) // 2)  # case S160
        waveform_data_array_ctype = _get_ctypes_pointer_for_buffer(value=waveform_data_array, library_type=_complextype.NIComplexI16)  # case B510
        error_code = self._library.niRFSG_WriteArbWaveformComplexI16(vi_ctype, waveform_name_ctype, number_of_samples_ctype, waveform_data_array_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def write_script(self, script):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        script_ctype = ctypes.create_string_buffer(script.encode(self._encoding))  # case C020
        error_code = self._library.niRFSG_WriteScript(vi_ctype, script_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def close(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSG_close(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def reset(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSG_reset(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return
