<%page args="f, config, method_template"/>\
<%
    '''Forwards to _fetch()/_read() with a nicer interface'''
    import build.helper as helper

    suffix = method_template['method_python_name_suffix']
%>\
    def ${f['python_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        # Set the fetch attributes
        with _NoChannel(session=self):
            self._fetch_relative_to = relative_to
            self._fetch_offset = offset
            self._fetch_record_number = record_number
            self._fetch_num_records = -1 if num_records is None else num_records
            if num_samples is None:
                num_samples = self.horz_record_length

        wfm, wfm_info = self._${f['python_name']}(num_samples, timeout)

        mv = memoryview(wfm)

        for i in range(len(wfm_info)):
            start = i * num_samples
            end = start + wfm_info[i]._actual_samples
            # We use the actual number of samples returned from the device to determine the end of the waveform. We then remove it from the wfm_info
            # since the length of the wfm will tell us that information
            wfm_info[i]._actual_samples = None
            wfm_info[i].samples = mv[start:end]

        lwfm_i = len(wfm_info)
        lrcl = len(self._repeated_capability_list)
        # Should this raise instead? If this asserts, is it the users fault?
        assert lwfm_i % lrcl == 0, 'Number of waveforms should be evenly divisible by the number of channels: len(wfm_info) == {0}, len(self._repeated_capability_list) == {1}'.format(lwfm_i, lrcl)
        actual_num_records = int(lwfm_i / lrcl)
        self._populate_channel_and_record_info(wfm_info, self._repeated_capability_list, range(offset, offset + actual_num_records))
        return wfm_info

