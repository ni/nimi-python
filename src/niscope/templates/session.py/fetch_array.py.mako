<%page args="f, config, method_template"/>\
<%
    import build.helper as helper

    suffix = method_template['method_python_name_suffix']
%>\
    def fetch_array(self, num_samples, timeout=5.0):
        import array

        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        timeout_ctype = visatype.ViReal64(timeout)  # case 9
        num_samples_ctype = visatype.ViInt32(num_samples)  # case 9
        wfm_array = array.array("d", [0]) * (num_samples * self._actual_num_wfms())
        wfm_info_ctype = (waveform_info.struct_niScope_wfmInfo * self._actual_num_wfms())()  # case 0.4
        error_code = self._library.niScope_Fetch(vi_ctype, channel_list_ctype, timeout_ctype, num_samples_ctype, ctypes.cast(wfm_array.buffer_info()[0], ctypes.POINTER(visatype.ViReal64)), wfm_info_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return wfm_array, [waveform_info.WaveformInfo(wfm_info_ctype[i]) for i in range(self._actual_num_wfms())]

