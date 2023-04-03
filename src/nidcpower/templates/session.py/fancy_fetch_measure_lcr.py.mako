<%page args="f, config, method_template"/>\
<%
    '''Forwards to _fetch_multiple_lcr() and _measure_multiple_lcr(), then populate the `channel`
    field of the returned LCRMeasurement objects.
    '''
    import build.helper as helper

    suffix = method_template['method_python_name_suffix']

    # We explicitly only support fetch_multiple_lcr and measure_multiple_lcr
    if f['python_name'] == 'fetch_multiple_lcr':
        param_list = 'count, timeout'
        channel_names_zipped = ''
        channel_name_unpack = ''
        channel_name_value = 'channel_names[0]'
    elif f['python_name'] == 'measure_multiple_lcr':
        param_list = ''
        channel_names_zipped = ', channel_names'
        channel_name_unpack = ' channel_name'
        channel_name_value = 'channel_name'
    else:
        raise ValueError(
            f"Only fetch_multiple_lcr and measure_multiple_lcr are supported. Got {f['python_name']}"
        )
%>\
    def ${f['python_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        lcr_measurements = self._${f['python_name']}(${param_list})

        channel_names = _converters.expand_channel_string(
            self._repeated_capability,
            self._all_channels_in_session
        )
%if f['python_name'] == 'fetch_multiple_lcr':
        assert len(channel_names) == 1, "fetch_multiple_lcr only supports one channel at a time"
%elif f['python_name'] == 'measure_multiple_lcr':
        assert len(channel_names) == len(lcr_measurements), (
            "measure_multiple_lcr should return as many LCR measurements as the number of channels specified through the channel string"
        )
%endif
        for lcr_measurement_object,${channel_name_unpack} in zip(lcr_measurements${channel_names_zipped}):
            lcr_measurement_object.channel = ${channel_name_value}
        return lcr_measurements
