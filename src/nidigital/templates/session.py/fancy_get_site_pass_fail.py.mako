<%page args="f, config, method_template"/>\
<%
    '''Forwards to _fetch()/_read() with a nicer interface'''
    import build.helper as helper
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        result_list = self._get_site_pass_fail(site_list)

        site_list = self.get_site_results_site_numbers(site_list, enums.SiteResult.PASS_FAIL)
        assert len(site_list) == len(result_list)

        pass_fail = dict(zip(site_list, result_list))
        return pass_fail

