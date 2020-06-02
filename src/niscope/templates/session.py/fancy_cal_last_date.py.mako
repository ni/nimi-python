<%page args="f, config, method_template"/>\
<%
    '''Forwards to _cal_fetch_date, with calibration type pre-selected.'''
    import build.helper as helper
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''

        year, month, day, hour, minute = self._cal_fetch_date(enums.GetLastCalibrationDateType.${f['python_name'].upper()}.value)
        return hightime.datetime(year, month, day, hour, minute)

