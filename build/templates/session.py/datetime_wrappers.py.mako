<%page args="f, config, method_template"/>\
<%
    import build.helper as helper

    output_params_list = []
    called_function = config['functions'][f['real_datetime_call']]
    for p in called_function['parameters']:
        if p['direction'] == 'out':
            output_params_list.append(p['python_name'])

    output_params = ', '.join(output_params_list)
    include_second = False
    if "second" in output_params_list:
        include_second = True
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        ${output_params} = self.${called_function['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_CALL)})
        %if include_second is False:
        return hightime.datetime(year, month, day, hour, minute)
        %else:
        return hightime.datetime(year, month, day, hour, minute, second)
        %endif
