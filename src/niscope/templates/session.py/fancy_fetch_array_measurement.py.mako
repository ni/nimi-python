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
            self._meas_other_channel = other_channel

        meas_wfm, wfm_info = self._${f['python_name']}(array_meas_function, timeout)

        mv = memoryview(meas_wfm)
        record_length = self.horz_record_length
        meas_wfm_array = []

        for i in range(len(meas_wfm)):
            start = i * record_length
            end = start + record_length
            single_record_array = mv[start:end]
            meas_wfm_array.append(single_record_array)

        return meas_wfm_array, wfm_info

