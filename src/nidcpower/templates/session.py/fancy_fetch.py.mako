<%page args="f, config, method_template"/>\
<%
    '''Forwards to _fetch_multiple() with a nicer interface'''
    import build.helper as helper

    suffix = method_template['method_python_name_suffix']

    # We explicitly only support fetch_multiple and measure_multiple
    if f['python_name'] == 'fetch_multiple':
        param_list = 'timeout, count'
        in_compliances_return = ', in_compliances'
        in_compliance_unpack = ', in_compliance'
        in_compliance_value = 'in_compliance'
        channel_names_zipped = ''
        channel_name_unpack = ''
        channel_name_value = 'channel_names[0]'
    elif f['python_name'] == 'measure_multiple':
        param_list = ''
        in_compliances_return = ''
        in_compliance_unpack = ''
        in_compliance_value = 'None'
        channel_names_zipped = ', channel_names'
        channel_name_unpack = ', channel_name'
        channel_name_value = 'channel_name'
    else:
        raise ValueError('Only fetch_multiple and measure_multiple are supported. Got {0}'.format(f['python_name']))
%>\
    def ${f['python_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        import collections
        Measurement = collections.namedtuple('Measurement', ['voltage', 'current', 'in_compliance', 'channel'])

        voltage_measurements, current_measurements${in_compliances_return} = self._${f['python_name']}(${param_list})

        with _NoChannel(session=self):
            all_channels_in_session = self._get_channel_names(range(self.channel_count))

        channel_names = _converters.expand_channel_string(
            self._repeated_capability,
            all_channels_in_session
        )
%if f['python_name'] == 'fetch_multiple':
        assert len(channel_names) == 1
%endif
        return [
            Measurement(
                voltage=voltage,
                current=current,
                in_compliance=${in_compliance_value},
                channel=${channel_name_value}
            ) for voltage, current${in_compliance_unpack}${channel_name_unpack} in zip(
                voltage_measurements, current_measurements${in_compliances_return}${channel_names_zipped}
            )
        ]

