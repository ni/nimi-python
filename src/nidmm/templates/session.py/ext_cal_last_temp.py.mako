<%page args="f, config, method_template"/>\
<%
    '''Forwards to get_cal_last_temp, with external calibration pre-selected.'''
    import build.helper as helper
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''

        return self.get_cal_last_temp(1)

