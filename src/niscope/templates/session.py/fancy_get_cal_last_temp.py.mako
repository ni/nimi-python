<%page args="f, config, method_template"/>\
<%
    '''Forwards to _cal_fetch_temp, with calibration type pre-selected.'''
    import build.helper as helper
    if f['python_name'] == "get_self_cal_last_temp":
        calibration_type = "SELF"
    else: # f['python_name'] == "get_ext_cal_last_temp"
        calibration_type = "EXTERNAL"
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''

        return self._cal_fetch_temperature(enums._CalibrationTypes.${calibration_type}.value)
