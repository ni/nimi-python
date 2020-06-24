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
        # Set the fetch attributes
        with _NoChannel(session=self):
            if other_channel is not None:
                self._meas_other_channel = other_channel
            record_length = self.horz_record_length

        meas_wfm, wfm_info = self._${f['python_name']}(array_meas_function, timeout)

        for i in range(len(meas_wfm)):
            start = i * record_length
            end = start + record_length
            wfm_info[i].samples = meas_wfm[start:end]
            wfm_info[i]._actual_samples = None

        num_records = int(len(self._repeated_capability_list) / len(wfm_info))
        i = 0
        for chan in self._repeated_capability_list:
            for rec in range(0, num_records):
                wfm_info[i].channel = chan
                wfm_info[i].record = rec
                i += 1

        return wfm_info

