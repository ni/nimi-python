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
        
        results, means, stdevs, min_vals, max_vals, nums_in_stats = self._${f['python_name']}(scalar_meas_function, timeout)
        
        output = []
        for result, mean, stdev, min_val, max_val, num_in_stats in zip(results, means, stdevs, min_vals, max_vals, nums_in_stats):
            measurement_stats = MeasurementStats(result, mean, stdev, min_val, max_val, num_in_stats)
            output.append(measurement_stats)
            
        i = 0
        num_records = int(len(results) / len(self._repeated_capability_list))
        for chan in self._repeated_capability_list:
            for rec in range(0, num_records):
                output[i].channel = chan
                output[i].record = rec
                i += 1
        
        return output
