<%page args="f, config, method_template"/>\
<%
    import build.helper as helper

    parameters = f['parameters']
    c_function_prefix = config['c_function_prefix']

    output_params_list = []
    called_function = config['functions'][f['real_datetime_call']]
    for p in called_function['parameters']:
        if p['direction'] == 'out':
            output_params_list.append(p['python_name'])

    output_params = ', '.join(output_params_list)
    lock_indent = '    ' if f['use_session_lock'] else ''
    lock_indent_num = 4 if f['use_session_lock'] else 0

%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
% if f['use_session_lock']:
        with self.lock():
% endif
        ${lock_indent}${output_params} = self.${called_function['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_CALL)})
        ${lock_indent}return datetime.datetime(year, month, day, hour, minute)

