<%page args="f, config, method_template"/>\
<%
    '''Forwards to _cal_fetch_temp, with internal calibration pre-selected.'''
    import build.helper as helper
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''

        return self._cal_fetch_temp(0)

