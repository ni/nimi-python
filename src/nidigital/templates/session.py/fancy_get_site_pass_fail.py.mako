<%page args="f, config, method_template"/>\
<%
    '''Gets pass/fail results and site numbers corresponding to them, then returns
    dictionary where each key is a site number and value is a bool indicating pass/fail'''
    import build.helper as helper
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        # For site_list, we just use the repeated capability
        result_list = self._get_site_pass_fail()
        site_list = self.get_site_results_site_numbers(enums.SiteResult.PASS_FAIL)
        assert len(site_list) == len(result_list)

        return dict(zip(site_list, result_list))

