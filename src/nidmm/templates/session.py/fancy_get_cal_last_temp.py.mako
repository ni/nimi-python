<%page args="f, config, method_template"/>\
<%
    '''Forwards to get_last_cal_temp, with calibration type pre-selected.'''
    import build.helper as helper
    SELF = 0
    EXTERNAL = 1
    if f['python_name'] == "get_self_cal_last_temp":
        calibration_type = SELF
    else: # f['python_name'] == "get_ext_cal_last_temp"
        calibration_type = EXTERNAL
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''

        return self.get_last_cal_temp(${calibration_type})

