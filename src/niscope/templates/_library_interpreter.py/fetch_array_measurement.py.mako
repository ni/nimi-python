
    def fetch_array_measurement(self, channel_list, timeout, array_meas_function, measurement_waveform_size):  # noqa: N802
        if measurement_waveform_size is None:
            measurement_waveform_size = self.actual_meas_wfm_size(array_meas_function)
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        timeout_ctype = _visatype.ViReal64(timeout)  # case S150
        array_meas_function_ctype = _visatype.ViInt32(array_meas_function.value)  # case S130
        measurement_waveform_size_ctype = _visatype.ViInt32(measurement_waveform_size)  # case S150
        meas_wfm_size = (measurement_waveform_size * self.actual_num_wfms(channel_list))  # case B560
        meas_wfm_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=meas_wfm_size)  # case B560
        wfm_info_size = self.actual_num_wfms(channel_list)  # case B560
        wfm_info_ctype = _get_ctypes_pointer_for_buffer(library_type=waveform_info.struct_niScope_wfmInfo, size=wfm_info_size)  # case B560
        error_code = self._library.niScope_FetchArrayMeasurement(vi_ctype, channel_list_ctype, timeout_ctype, array_meas_function_ctype, measurement_waveform_size_ctype, meas_wfm_ctype, wfm_info_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(meas_wfm_ctype[i]) for i in range((measurement_waveform_size * self.actual_num_wfms(channel_list)))], [waveform_info.WaveformInfo(wfm_info_ctype[i]) for i in range(self.actual_num_wfms(channel_list))]
