<%page args="f, config, method_template"/>\
<%
    import build.helper as helper

    parameters = f['parameters']
    c_function_prefix = config['c_function_prefix']

%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, method_template, False, config, indent=8)}
        '''
        month, day, year, hour, minute = self._${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_CALL)})
        return datetime.datetime(year, month, day, hour, minute)

