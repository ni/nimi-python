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
        # Set the fetch attributes
        with _NoChannel(session=self):
            self._fetch_relative_to = relative_to
            self._fetch_offset = offset
            self._fetch_record_number = record_number
            self._fetch_num_records = -1 if num_records is None else num_records

        results, means, stdevs, min_vals, max_vals, nums_in_stats = self._${f['python_name']}(scalar_meas_function, timeout)

        output = []
        for result, mean, stdev, min_val, max_val, num_in_stats in zip(results, means, stdevs, min_vals, max_vals, nums_in_stats):
            measurement_stat = measurement_stats.MeasurementStats(result, mean, stdev, min_val, max_val, num_in_stats)
            output.append(measurement_stat)

<%include file="./fetch_waveform_info_population.py.mako" args="results_name='results', results_description='results', output_name='output'"/>

        return output
