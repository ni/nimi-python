<%page args="f, config, method_template"/>\
<%
    '''Forwards to _fetch_multiple() with a nicer interface'''
    import build.helper as helper

    suffix = method_template['method_python_name_suffix']

    # We explicitly only support fetch_multiple and measure_multiple
    if f['python_name'] == 'fetch_multiple':
        in_compliance_value = 'in_compliance[i]'
        in_compliance_return = ', in_compliance'
        param_list = 'timeout, count'
        array_size = 'count'  # This is what is used for the array sizes
    elif f['python_name'] == 'measure_multiple':
        in_compliance_value = 'None'
        in_compliance_return = ''
        param_list = ''
        array_size = 'self._parse_channel_count()'  # This is what is used for the array sizes
    else:
        raise ValueError('Only fetch_multiple and measure_multiple are supported. Got {0}'.format(f['python_name']))
%>\
    def ${f['python_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}) -> typing.List[typing.NamedTuple[float, float, bool]]:
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        measurement = typing.NamedTuple('Measurement', [('voltage', 'float'), ('current', 'float'), ('in_compliance', 'bool')])

        voltage_measurements, current_measurements${in_compliance_return} = self._${f['python_name']}(${param_list})

        return [measurement(voltage=voltage_measurements[i], current=current_measurements[i], in_compliance=${in_compliance_value}) for i in range(${array_size})]

