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
        self._populate_channel_and_record_info(wfm_info, self._repeated_capability_list, range(num_records))

        return wfm_info

    ## Define the private method below the public method so that lock decorator gets added to the public method
    def _populate_channel_and_record_info(self, objects, channels, records):
        i = 0
        for channel in channels:
            for record in records:
                objects[i].channel = channel
                objects[i].record = record
                i += 1

