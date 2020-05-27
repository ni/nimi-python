<%page args="f, config, method_template"/>\
<%
    '''Forwards to get_cal_date_and_time, with external calibration pre-selected.'''
    import build.helper as helper
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''

        datetime = self.get_cal_date_and_time(1)
        return datetime

