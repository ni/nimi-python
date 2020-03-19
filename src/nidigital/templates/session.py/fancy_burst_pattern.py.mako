<%page args="f, config, method_template"/>\
<%
    '''Forwards to _burst_pattern(). If wait_until_done is True, calls get_site_pass_fail() to obtain the pass/fail
    results and returns it to the caller.'''
    import build.helper as helper
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        self._burst_pattern(site_list, start_label, select_digital_function, wait_until_done, timeout)

        if wait_until_done:
            return self.get_site_pass_fail(site_list)
        else:
            return None

