<%page args="f, config, method_template"/>\
<%
    import build.helper as helper
    suffix = method_template['method_python_name_suffix']
%>\
    def ${f['python_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_NUMPY_INTO_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        timeout = _converters.convert_timedelta_to_seconds_real64(timeout)
        data, actual_num_waveforms, actual_samples_per_waveform = self._interpreter.fetch_capture_waveform(self._repeated_capability, waveform_name, samples_to_read, timeout)

        # Get the site list
        site_list = self._get_site_results_site_numbers(enums._SiteResultType.CAPTURE_WAVEFORM)
        assert len(site_list) == actual_num_waveforms

        waveforms = {}

        mv = memoryview(data)

        for i in range(actual_num_waveforms):
            start = i * actual_samples_per_waveform
            end = start + actual_samples_per_waveform
            waveforms[site_list[i]] = mv[start:end]

        return waveforms
