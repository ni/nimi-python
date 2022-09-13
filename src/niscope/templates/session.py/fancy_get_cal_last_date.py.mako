<%page args="f, config, method_template"/>\
<%
    '''Forwards to _cal_fetch_date, with calibration type pre-selected.'''
    import build.helper as helper
    if f['session_name'] == "get_self_cal_last_date_and_time":
        calibration_type = "SELF"
    else: #f['session_name'] == "get_ext_cal_last_date_and_time"
        calibration_type = "EXTERNAL"
%>\
    def ${f['session_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['session_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''

        year, month, day = self._cal_fetch_date(enums._CalibrationTypes.${calibration_type})
        return hightime.datetime(year, month, day)
