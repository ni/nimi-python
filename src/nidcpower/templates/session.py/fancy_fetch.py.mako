<%page args="f, config, method_template"/>\
<%
    '''Forwards to _fetch_multiple() with a nicer interface'''
    import build.helper as helper

    suffix = method_template['method_python_name_suffix']
%>\
    def ${f['python_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        import collections
        Measurement = collections.namedtuple('Measurement', ['voltage', 'current', 'in_compliance'])
        if count is None:
            count = self.fetch_backlog

        voltage_measurements, current_measurements, in_compliance = self._fetch_multiple(count, timeout)

        measurements = []
        for i in range(count):
            measurements.append(Measurement(voltage=voltage_measurements[i], current=current_measurements[i], in_compliance=in_compliance[i]))

        return measurements

