# -*- coding: utf-8 -*-
# This file was generated

import array
import ctypes
import hightime  # noqa: F401
import platform

import nidcpower._library_singleton as _library_singleton
import nidcpower._visatype as _visatype
import nidcpower.enums as enums  # noqa: F401
import nidcpower.errors as errors

import nidcpower.lcr_measurement as lcr_measurement  # noqa: F401

import nidcpower.lcr_load_compensation_spot as lcr_load_compensation_spot  # noqa: F401


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

    def abort(self, channel_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        error_code = self._library.niDCPower_AbortWithChannels(vi_ctype, channel_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def self_cal(self, channel_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        error_code = self._library.niDCPower_CalSelfCalibrate(vi_ctype, channel_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def clear_latched_output_cutoff_state(self, channel_name, output_cutoff_reason):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        output_cutoff_reason_ctype = _visatype.ViInt32(output_cutoff_reason.value)  # case S130
        error_code = self._library.niDCPower_ClearLatchedOutputCutoffState(vi_ctype, channel_name_ctype, output_cutoff_reason_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def commit(self, channel_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        error_code = self._library.niDCPower_CommitWithChannels(vi_ctype, channel_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_aperture_time(self, channel_name, aperture_time, units):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        aperture_time_ctype = _visatype.ViReal64(aperture_time)  # case S150
        units_ctype = _visatype.ViInt32(units.value)  # case S130
        error_code = self._library.niDCPower_ConfigureApertureTime(vi_ctype, channel_name_ctype, aperture_time_ctype, units_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_lcr_compensation(self, channel_name, compensation_data):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        compensation_data_size_ctype = _visatype.ViInt32(0 if compensation_data is None else len(compensation_data))  # case S160
        compensation_data_ctype = _get_ctypes_pointer_for_buffer(value=compensation_data, library_type=_visatype.ViInt8)  # case B550
        error_code = self._library.niDCPower_ConfigureLCRCompensation(vi_ctype, channel_name_ctype, compensation_data_size_ctype, compensation_data_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_lcr_custom_cable_compensation(self, channel_name, custom_cable_compensation_data):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        custom_cable_compensation_data_size_ctype = _visatype.ViInt32(0 if custom_cable_compensation_data is None else len(custom_cable_compensation_data))  # case S160
        custom_cable_compensation_data_ctype = _get_ctypes_pointer_for_buffer(value=custom_cable_compensation_data, library_type=_visatype.ViInt8)  # case B550
        error_code = self._library.niDCPower_ConfigureLCRCustomCableCompensation(vi_ctype, channel_name_ctype, custom_cable_compensation_data_size_ctype, custom_cable_compensation_data_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_advanced_sequence_commit_step(self, channel_name, set_as_active_step):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        set_as_active_step_ctype = _visatype.ViBoolean(set_as_active_step)  # case S150
        error_code = self._library.niDCPower_CreateAdvancedSequenceCommitStepWithChannels(vi_ctype, channel_name_ctype, set_as_active_step_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_advanced_sequence_step(self, channel_name, set_as_active_step):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        set_as_active_step_ctype = _visatype.ViBoolean(set_as_active_step)  # case S150
        error_code = self._library.niDCPower_CreateAdvancedSequenceStepWithChannels(vi_ctype, channel_name_ctype, set_as_active_step_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_advanced_sequence_with_channels(self, channel_name, sequence_name, attribute_ids, set_as_active_sequence):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        sequence_name_ctype = ctypes.create_string_buffer(sequence_name.encode(self._encoding))  # case C020
        attribute_id_count_ctype = _visatype.ViInt32(0 if attribute_ids is None else len(attribute_ids))  # case S160
        attribute_ids_ctype = _get_ctypes_pointer_for_buffer(value=attribute_ids, library_type=_visatype.ViInt32)  # case B550
        set_as_active_sequence_ctype = _visatype.ViBoolean(set_as_active_sequence)  # case S150
        error_code = self._library.niDCPower_CreateAdvancedSequenceWithChannels(vi_ctype, channel_name_ctype, sequence_name_ctype, attribute_id_count_ctype, attribute_ids_ctype, set_as_active_sequence_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def delete_advanced_sequence(self, channel_name, sequence_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        sequence_name_ctype = ctypes.create_string_buffer(sequence_name.encode(self._encoding))  # case C020
        error_code = self._library.niDCPower_DeleteAdvancedSequenceWithChannels(vi_ctype, channel_name_ctype, sequence_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disable(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDCPower_Disable(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def export_attribute_configuration_buffer(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        size_ctype = _visatype.ViInt32()  # case S170
        configuration_ctype = None  # case B580
        error_code = self._library.niDCPower_ExportAttributeConfigurationBuffer(vi_ctype, size_ctype, configuration_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        size_ctype = _visatype.ViInt32(error_code)  # case S180
        configuration_size = size_ctype.value  # case B590
        configuration_array = array.array("b", [0]) * configuration_size  # case B590
        configuration_ctype = _get_ctypes_pointer_for_buffer(value=configuration_array, library_type=_visatype.ViInt8)  # case B590
        error_code = self._library.niDCPower_ExportAttributeConfigurationBuffer(vi_ctype, size_ctype, configuration_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return configuration_array

    def export_attribute_configuration_file(self, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.niDCPower_ExportAttributeConfigurationFile(vi_ctype, file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def fancy_initialize(self, resource_name, channels, reset, option_string, independent_channels):  # noqa: N802
        resource_name_ctype = ctypes.create_string_buffer(resource_name.encode(self._encoding))  # case C020
        channels_ctype = ctypes.create_string_buffer(channels.encode(self._encoding))  # case C020
        reset_ctype = _visatype.ViBoolean(reset)  # case S150
        option_string_ctype = ctypes.create_string_buffer(option_string.encode(self._encoding))  # case C020
        vi_ctype = _visatype.ViSession()  # case S220
        independent_channels_ctype = _visatype.ViBoolean(independent_channels)  # case S150
        error_code = self._library.niDCPower_FancyInitialize(resource_name_ctype, channels_ctype, reset_ctype, option_string_ctype, None if vi_ctype is None else (ctypes.pointer(vi_ctype)), independent_channels_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(vi_ctype.value)

    def fetch_multiple(self, channel_name, timeout, count):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        timeout_ctype = _visatype.ViReal64(timeout)  # case S150
        count_ctype = _visatype.ViInt32(count)  # case S210
        voltage_measurements_size = count  # case B600
        voltage_measurements_array = array.array("d", [0]) * voltage_measurements_size  # case B600
        voltage_measurements_ctype = _get_ctypes_pointer_for_buffer(value=voltage_measurements_array, library_type=_visatype.ViReal64)  # case B600
        current_measurements_size = count  # case B600
        current_measurements_array = array.array("d", [0]) * current_measurements_size  # case B600
        current_measurements_ctype = _get_ctypes_pointer_for_buffer(value=current_measurements_array, library_type=_visatype.ViReal64)  # case B600
        in_compliance_size = count  # case B600
        in_compliance_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViBoolean, size=in_compliance_size)  # case B600
        actual_count_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDCPower_FetchMultiple(vi_ctype, channel_name_ctype, timeout_ctype, count_ctype, voltage_measurements_ctype, current_measurements_ctype, in_compliance_ctype, None if actual_count_ctype is None else (ctypes.pointer(actual_count_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return voltage_measurements_array, current_measurements_array, [bool(in_compliance_ctype[i]) for i in range(count_ctype.value)]

    def fetch_multiple_lcr(self, channel_name, timeout, count):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        timeout_ctype = _visatype.ViReal64(timeout)  # case S150
        count_ctype = _visatype.ViInt32(count)  # case S210
        measurements_size = count  # case B600
        measurements_ctype = _get_ctypes_pointer_for_buffer(library_type=lcr_measurement.struct_NILCRMeasurement, size=measurements_size)  # case B600
        actual_count_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDCPower_FetchMultipleLCR(vi_ctype, channel_name_ctype, timeout_ctype, count_ctype, measurements_ctype, None if actual_count_ctype is None else (ctypes.pointer(actual_count_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [lcr_measurement.LCRMeasurement(measurements_ctype[i]) for i in range(count_ctype.value)]

    def get_attribute_vi_boolean(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niDCPower_GetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(attribute_value_ctype.value)

    def get_attribute_vi_int32(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDCPower_GetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(attribute_value_ctype.value)

    def get_attribute_vi_int64(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt64()  # case S220
        error_code = self._library.niDCPower_GetAttributeViInt64(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(attribute_value_ctype.value)

    def get_attribute_vi_real64(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDCPower_GetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(attribute_value_ctype.value)

    def get_attribute_vi_string(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        attribute_value_ctype = None  # case C050
        error_code = self._library.niDCPower_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, buffer_size_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        attribute_value_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niDCPower_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, buffer_size_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return attribute_value_ctype.value.decode(self._encoding)

    def get_channel_name(self, index):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        index_ctype = _visatype.ViInt32(index)  # case S150
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        channel_name_ctype = None  # case C050
        error_code = self._library.niDCPower_GetChannelName(vi_ctype, index_ctype, buffer_size_ctype, channel_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        channel_name_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niDCPower_GetChannelName(vi_ctype, index_ctype, buffer_size_ctype, channel_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return channel_name_ctype.value.decode(self._encoding)

    def get_channel_names(self, indices):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        indices_ctype = ctypes.create_string_buffer(indices.encode(self._encoding))  # case C020
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        names_ctype = None  # case C050
        error_code = self._library.niDCPower_GetChannelNameFromString(vi_ctype, indices_ctype, buffer_size_ctype, names_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        names_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niDCPower_GetChannelNameFromString(vi_ctype, indices_ctype, buffer_size_ctype, names_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return names_ctype.value.decode(self._encoding)

    def get_error(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        code_ctype = _visatype.ViStatus()  # case S220
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        description_ctype = None  # case C050
        error_code = self._library.niDCPower_GetError(vi_ctype, None if code_ctype is None else (ctypes.pointer(code_ctype)), buffer_size_ctype, description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=True)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        description_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niDCPower_GetError(vi_ctype, None if code_ctype is None else (ctypes.pointer(code_ctype)), buffer_size_ctype, description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return int(code_ctype.value), description_ctype.value.decode(self._encoding)

    def get_ext_cal_last_date_and_time(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        year_ctype = _visatype.ViInt32()  # case S220
        month_ctype = _visatype.ViInt32()  # case S220
        day_ctype = _visatype.ViInt32()  # case S220
        hour_ctype = _visatype.ViInt32()  # case S220
        minute_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDCPower_GetExtCalLastDateAndTime(vi_ctype, None if year_ctype is None else (ctypes.pointer(year_ctype)), None if month_ctype is None else (ctypes.pointer(month_ctype)), None if day_ctype is None else (ctypes.pointer(day_ctype)), None if hour_ctype is None else (ctypes.pointer(hour_ctype)), None if minute_ctype is None else (ctypes.pointer(minute_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(year_ctype.value), int(month_ctype.value), int(day_ctype.value), int(hour_ctype.value), int(minute_ctype.value)

    def get_ext_cal_last_temp(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        temperature_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDCPower_GetExtCalLastTemp(vi_ctype, None if temperature_ctype is None else (ctypes.pointer(temperature_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

    def get_ext_cal_recommended_interval(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        months_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDCPower_GetExtCalRecommendedInterval(vi_ctype, None if months_ctype is None else (ctypes.pointer(months_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(months_ctype.value)

    def get_lcr_compensation_data(self, channel_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        compensation_data_size_ctype = _visatype.ViInt32()  # case S170
        compensation_data_ctype = None  # case B580
        error_code = self._library.niDCPower_GetLCRCompensationData(vi_ctype, channel_name_ctype, compensation_data_size_ctype, compensation_data_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        compensation_data_size_ctype = _visatype.ViInt32(error_code)  # case S180
        compensation_data_size = compensation_data_size_ctype.value  # case B590
        compensation_data_array = array.array("b", [0]) * compensation_data_size  # case B590
        compensation_data_ctype = _get_ctypes_pointer_for_buffer(value=compensation_data_array, library_type=_visatype.ViInt8)  # case B590
        error_code = self._library.niDCPower_GetLCRCompensationData(vi_ctype, channel_name_ctype, compensation_data_size_ctype, compensation_data_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return compensation_data_array

    def get_lcr_compensation_last_date_and_time(self, channel_name, compensation_type):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        compensation_type_ctype = _visatype.ViInt32(compensation_type.value)  # case S130
        year_ctype = _visatype.ViInt32()  # case S220
        month_ctype = _visatype.ViInt32()  # case S220
        day_ctype = _visatype.ViInt32()  # case S220
        hour_ctype = _visatype.ViInt32()  # case S220
        minute_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDCPower_GetLCRCompensationLastDateAndTime(vi_ctype, channel_name_ctype, compensation_type_ctype, None if year_ctype is None else (ctypes.pointer(year_ctype)), None if month_ctype is None else (ctypes.pointer(month_ctype)), None if day_ctype is None else (ctypes.pointer(day_ctype)), None if hour_ctype is None else (ctypes.pointer(hour_ctype)), None if minute_ctype is None else (ctypes.pointer(minute_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(year_ctype.value), int(month_ctype.value), int(day_ctype.value), int(hour_ctype.value), int(minute_ctype.value)

    def get_lcr_custom_cable_compensation_data(self, channel_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        custom_cable_compensation_data_size_ctype = _visatype.ViInt32()  # case S170
        custom_cable_compensation_data_ctype = None  # case B580
        error_code = self._library.niDCPower_GetLCRCustomCableCompensationData(vi_ctype, channel_name_ctype, custom_cable_compensation_data_size_ctype, custom_cable_compensation_data_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        custom_cable_compensation_data_size_ctype = _visatype.ViInt32(error_code)  # case S180
        custom_cable_compensation_data_size = custom_cable_compensation_data_size_ctype.value  # case B590
        custom_cable_compensation_data_array = array.array("b", [0]) * custom_cable_compensation_data_size  # case B590
        custom_cable_compensation_data_ctype = _get_ctypes_pointer_for_buffer(value=custom_cable_compensation_data_array, library_type=_visatype.ViInt8)  # case B590
        error_code = self._library.niDCPower_GetLCRCustomCableCompensationData(vi_ctype, channel_name_ctype, custom_cable_compensation_data_size_ctype, custom_cable_compensation_data_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return custom_cable_compensation_data_array

    def get_self_cal_last_date_and_time(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        year_ctype = _visatype.ViInt32()  # case S220
        month_ctype = _visatype.ViInt32()  # case S220
        day_ctype = _visatype.ViInt32()  # case S220
        hour_ctype = _visatype.ViInt32()  # case S220
        minute_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDCPower_GetSelfCalLastDateAndTime(vi_ctype, None if year_ctype is None else (ctypes.pointer(year_ctype)), None if month_ctype is None else (ctypes.pointer(month_ctype)), None if day_ctype is None else (ctypes.pointer(day_ctype)), None if hour_ctype is None else (ctypes.pointer(hour_ctype)), None if minute_ctype is None else (ctypes.pointer(minute_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(year_ctype.value), int(month_ctype.value), int(day_ctype.value), int(hour_ctype.value), int(minute_ctype.value)

    def get_self_cal_last_temp(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        temperature_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDCPower_GetSelfCalLastTemp(vi_ctype, None if temperature_ctype is None else (ctypes.pointer(temperature_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

    def import_attribute_configuration_buffer(self, configuration):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        size_ctype = _visatype.ViInt32(0 if configuration is None else len(configuration))  # case S160
        configuration_ctype = _get_ctypes_pointer_for_buffer(value=configuration, library_type=_visatype.ViInt8)  # case B550
        error_code = self._library.niDCPower_ImportAttributeConfigurationBuffer(vi_ctype, size_ctype, configuration_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def import_attribute_configuration_file(self, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.niDCPower_ImportAttributeConfigurationFile(vi_ctype, file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def initialize_with_channels(self, resource_name, channels, reset, option_string):  # noqa: N802
        resource_name_ctype = ctypes.create_string_buffer(resource_name.encode(self._encoding))  # case C020
        channels_ctype = ctypes.create_string_buffer(channels.encode(self._encoding))  # case C020
        reset_ctype = _visatype.ViBoolean(reset)  # case S150
        option_string_ctype = ctypes.create_string_buffer(option_string.encode(self._encoding))  # case C020
        vi_ctype = _visatype.ViSession()  # case S220
        error_code = self._library.niDCPower_InitializeWithChannels(resource_name_ctype, channels_ctype, reset_ctype, option_string_ctype, None if vi_ctype is None else (ctypes.pointer(vi_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        self._close_on_exit = True
        return int(vi_ctype.value)

    def initialize_with_independent_channels(self, resource_name, reset, option_string):  # noqa: N802
        resource_name_ctype = ctypes.create_string_buffer(resource_name.encode(self._encoding))  # case C020
        reset_ctype = _visatype.ViBoolean(reset)  # case S150
        option_string_ctype = ctypes.create_string_buffer(option_string.encode(self._encoding))  # case C020
        vi_ctype = _visatype.ViSession()  # case S220
        error_code = self._library.niDCPower_InitializeWithIndependentChannels(resource_name_ctype, reset_ctype, option_string_ctype, None if vi_ctype is None else (ctypes.pointer(vi_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        self._close_on_exit = True
        return int(vi_ctype.value)

    def initiate_with_channels(self, channel_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        error_code = self._library.niDCPower_InitiateWithChannels(vi_ctype, channel_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def lock(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDCPower_LockSession(vi_ctype, None)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def measure(self, channel_name, measurement_type):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        measurement_type_ctype = _visatype.ViInt32(measurement_type.value)  # case S130
        measurement_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDCPower_Measure(vi_ctype, channel_name_ctype, measurement_type_ctype, None if measurement_ctype is None else (ctypes.pointer(measurement_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(measurement_ctype.value)

    def measure_multiple(self, channel_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        voltage_measurements_size = self.parse_channel_count(channel_name)  # case B560
        voltage_measurements_array = array.array("d", [0]) * voltage_measurements_size  # case B560
        voltage_measurements_ctype = _get_ctypes_pointer_for_buffer(value=voltage_measurements_array, library_type=_visatype.ViReal64)  # case B560
        current_measurements_size = self.parse_channel_count(channel_name)  # case B560
        current_measurements_array = array.array("d", [0]) * current_measurements_size  # case B560
        current_measurements_ctype = _get_ctypes_pointer_for_buffer(value=current_measurements_array, library_type=_visatype.ViReal64)  # case B560
        error_code = self._library.niDCPower_MeasureMultiple(vi_ctype, channel_name_ctype, voltage_measurements_ctype, current_measurements_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return voltage_measurements_array, current_measurements_array

    def measure_multiple_lcr(self, channel_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        measurements_size = self.parse_channel_count(channel_name)  # case B560
        measurements_ctype = _get_ctypes_pointer_for_buffer(library_type=lcr_measurement.struct_NILCRMeasurement, size=measurements_size)  # case B560
        error_code = self._library.niDCPower_MeasureMultipleLCR(vi_ctype, channel_name_ctype, measurements_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [lcr_measurement.LCRMeasurement(measurements_ctype[i]) for i in range(self.parse_channel_count(channel_name))]

    def parse_channel_count(self, channels_string):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channels_string_ctype = ctypes.create_string_buffer(channels_string.encode(self._encoding))  # case C010
        number_of_channels_ctype = _visatype.ViUInt32()  # case S220
        error_code = self._library.niDCPower_ParseChannelCount(vi_ctype, channels_string_ctype, None if number_of_channels_ctype is None else (ctypes.pointer(number_of_channels_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(number_of_channels_ctype.value)

    def perform_lcr_load_compensation(self, channel_name, compensation_spots):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        num_compensation_spots_ctype = _visatype.ViInt32(0 if compensation_spots is None else len(compensation_spots))  # case S160
        compensation_spots_ctype = _get_ctypes_pointer_for_buffer([lcr_load_compensation_spot.struct_NILCRLoadCompensationSpot(c) for c in compensation_spots], library_type=lcr_load_compensation_spot.struct_NILCRLoadCompensationSpot)  # case B540
        error_code = self._library.niDCPower_PerformLCRLoadCompensation(vi_ctype, channel_name_ctype, num_compensation_spots_ctype, compensation_spots_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def perform_lcr_open_compensation(self, channel_name, additional_frequencies):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        num_frequencies_ctype = _visatype.ViInt32(0 if additional_frequencies is None else len(additional_frequencies))  # case S160
        additional_frequencies_ctype = _get_ctypes_pointer_for_buffer(value=additional_frequencies, library_type=_visatype.ViReal64)  # case B550
        error_code = self._library.niDCPower_PerformLCROpenCompensation(vi_ctype, channel_name_ctype, num_frequencies_ctype, additional_frequencies_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def perform_lcr_open_custom_cable_compensation(self, channel_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        error_code = self._library.niDCPower_PerformLCROpenCustomCableCompensation(vi_ctype, channel_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def perform_lcr_short_compensation(self, channel_name, additional_frequencies):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        num_frequencies_ctype = _visatype.ViInt32(0 if additional_frequencies is None else len(additional_frequencies))  # case S160
        additional_frequencies_ctype = _get_ctypes_pointer_for_buffer(value=additional_frequencies, library_type=_visatype.ViReal64)  # case B550
        error_code = self._library.niDCPower_PerformLCRShortCompensation(vi_ctype, channel_name_ctype, num_frequencies_ctype, additional_frequencies_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def perform_lcr_short_custom_cable_compensation(self, channel_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        error_code = self._library.niDCPower_PerformLCRShortCustomCableCompensation(vi_ctype, channel_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def query_in_compliance(self, channel_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        in_compliance_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niDCPower_QueryInCompliance(vi_ctype, channel_name_ctype, None if in_compliance_ctype is None else (ctypes.pointer(in_compliance_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(in_compliance_ctype.value)

    def query_latched_output_cutoff_state(self, channel_name, output_cutoff_reason):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        output_cutoff_reason_ctype = _visatype.ViInt32(output_cutoff_reason.value)  # case S130
        output_cutoff_state_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niDCPower_QueryLatchedOutputCutoffState(vi_ctype, channel_name_ctype, output_cutoff_reason_ctype, None if output_cutoff_state_ctype is None else (ctypes.pointer(output_cutoff_state_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(output_cutoff_state_ctype.value)

    def query_max_current_limit(self, channel_name, voltage_level):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        voltage_level_ctype = _visatype.ViReal64(voltage_level)  # case S150
        max_current_limit_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDCPower_QueryMaxCurrentLimit(vi_ctype, channel_name_ctype, voltage_level_ctype, None if max_current_limit_ctype is None else (ctypes.pointer(max_current_limit_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(max_current_limit_ctype.value)

    def query_max_voltage_level(self, channel_name, current_limit):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        current_limit_ctype = _visatype.ViReal64(current_limit)  # case S150
        max_voltage_level_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDCPower_QueryMaxVoltageLevel(vi_ctype, channel_name_ctype, current_limit_ctype, None if max_voltage_level_ctype is None else (ctypes.pointer(max_voltage_level_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(max_voltage_level_ctype.value)

    def query_min_current_limit(self, channel_name, voltage_level):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        voltage_level_ctype = _visatype.ViReal64(voltage_level)  # case S150
        min_current_limit_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDCPower_QueryMinCurrentLimit(vi_ctype, channel_name_ctype, voltage_level_ctype, None if min_current_limit_ctype is None else (ctypes.pointer(min_current_limit_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(min_current_limit_ctype.value)

    def query_output_state(self, channel_name, output_state):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        output_state_ctype = _visatype.ViInt32(output_state.value)  # case S130
        in_state_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niDCPower_QueryOutputState(vi_ctype, channel_name_ctype, output_state_ctype, None if in_state_ctype is None else (ctypes.pointer(in_state_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(in_state_ctype.value)

    def read_current_temperature(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        temperature_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDCPower_ReadCurrentTemperature(vi_ctype, None if temperature_ctype is None else (ctypes.pointer(temperature_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

    def reset_device(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDCPower_ResetDevice(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def reset(self, channel_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        error_code = self._library.niDCPower_ResetWithChannels(vi_ctype, channel_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def reset_with_defaults(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDCPower_ResetWithDefaults(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def send_software_edge_trigger(self, channel_name, trigger):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        trigger_ctype = _visatype.ViInt32(trigger.value)  # case S130
        error_code = self._library.niDCPower_SendSoftwareEdgeTriggerWithChannels(vi_ctype, channel_name_ctype, trigger_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_boolean(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViBoolean(attribute_value)  # case S150
        error_code = self._library.niDCPower_SetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_int32(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt32(attribute_value)  # case S150
        error_code = self._library.niDCPower_SetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_int64(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt64(attribute_value)  # case S150
        error_code = self._library.niDCPower_SetAttributeViInt64(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_real64(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViReal64(attribute_value)  # case S150
        error_code = self._library.niDCPower_SetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_string(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = ctypes.create_string_buffer(attribute_value.encode(self._encoding))  # case C020
        error_code = self._library.niDCPower_SetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_runtime_environment(self, environment, environment_version, reserved1, reserved2):  # noqa: N802
        environment_ctype = ctypes.create_string_buffer(environment.encode(self._encoding))  # case C020
        environment_version_ctype = ctypes.create_string_buffer(environment_version.encode(self._encoding))  # case C020
        reserved1_ctype = ctypes.create_string_buffer(reserved1.encode(self._encoding))  # case C020
        reserved2_ctype = ctypes.create_string_buffer(reserved2.encode(self._encoding))  # case C020
        error_code = self._library.niDCPower_SetRuntimeEnvironment(environment_ctype, environment_version_ctype, reserved1_ctype, reserved2_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_sequence(self, channel_name, values, source_delays):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        values_ctype = _get_ctypes_pointer_for_buffer(value=values, library_type=_visatype.ViReal64)  # case B550
        source_delays_ctype = _get_ctypes_pointer_for_buffer(value=source_delays, library_type=_visatype.ViReal64)  # case B550
        size_ctype = _visatype.ViUInt32(0 if values is None else len(values))  # case S160
        error_code = self._library.niDCPower_SetSequence(vi_ctype, channel_name_ctype, values_ctype, source_delays_ctype, size_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def unlock(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDCPower_UnlockSession(vi_ctype, None)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def wait_for_event(self, channel_name, event_id, timeout):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        event_id_ctype = _visatype.ViInt32(event_id.value)  # case S130
        timeout_ctype = _visatype.ViReal64(timeout)  # case S150
        error_code = self._library.niDCPower_WaitForEventWithChannels(vi_ctype, channel_name_ctype, event_id_ctype, timeout_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def close(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDCPower_close(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def error_message(self, error_code):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code_ctype = _visatype.ViStatus(error_code)  # case S150
        error_message_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library.niDCPower_error_message(vi_ctype, error_code_ctype, error_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return error_message_ctype.value.decode(self._encoding)

    def self_test(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        self_test_result_ctype = _visatype.ViInt16()  # case S220
        self_test_message_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library.niDCPower_self_test(vi_ctype, None if self_test_result_ctype is None else (ctypes.pointer(self_test_result_ctype)), self_test_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(self_test_result_ctype.value), self_test_message_ctype.value.decode(self._encoding)
