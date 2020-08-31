<%page args="f, config, method_template"/>\
<%
    '''Forwards to _fetch_array_measurement with cleaner return values.'''
    import build.helper as helper
    suffix = method_template['method_python_name_suffix']
%>\
    def ${f['python_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        r'''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        if meas_wfm_size is None:
            meas_wfm_size = self.actual_meas_wfm_size(array_meas_function)

        meas_wfm, wfm_info = self._${f['python_name']}(array_meas_function, meas_wfm_size, timeout)

        record_length = int(len(meas_wfm) / len(wfm_info))
        waveform_info._populate_samples_info(wfm_info, meas_wfm, record_length)

        num_records = int(len(wfm_info) / len(self._repeated_capability_list))
        waveform_info._populate_channel_and_record_info(wfm_info, self._repeated_capability_list, range(num_records))

        return wfm_info

