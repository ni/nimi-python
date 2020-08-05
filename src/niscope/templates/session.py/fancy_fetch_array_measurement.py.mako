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

        meas_wfm, wfm_info = self._${f['python_name']}(array_meas_function, timeout)
        record_length = int(len(meas_wfm) / len(wfm_info))

        for i in range(len(wfm_info)):
            start = i * record_length
            end = start + wfm_info[i]._actual_samples
            wfm_info[i]._actual_samples = None
            wfm_info[i].samples = meas_wfm[start:end]

        num_records = int(len(wfm_info) / len(self._repeated_capability_list))
        i = 0
        for chan in self._repeated_capability_list:
            for rec in range(0, num_records):
                wfm_info[i].channel = chan
                wfm_info[i].record = rec
                i += 1

        return wfm_info

