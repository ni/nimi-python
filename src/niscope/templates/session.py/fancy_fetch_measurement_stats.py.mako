<%page args="f, config, method_template"/>\
<%
    '''Forwards to _fetch_measurement_stats with cleaner return values.'''
    import build.helper as helper
    suffix = method_template['method_python_name_suffix']
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        r'''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''

        results, means, stdevs, min_vals, max_vals, nums_in_stats = self._${f['python_name']}(scalar_meas_function, timeout)

        output = []
        for result, mean, stdev, min_val, max_val, num_in_stats in zip(results, means, stdevs, min_vals, max_vals, nums_in_stats):
            measurement_stat = measurement_stats.MeasurementStats(result, mean, stdev, min_val, max_val, num_in_stats)
            output.append(measurement_stat)

        num_records = int(len(results) / len(self._repeated_capability_list))
        self._populate_channel_and_record_info(output, self._repeated_capability_list, range(num_records))

        return output

