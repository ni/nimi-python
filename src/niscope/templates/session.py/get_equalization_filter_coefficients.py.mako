<%page args="f, config, method_template"/>\
<%
    '''Forwards to _get_equalization_filter_coefficients() with a nicer interface'''
    import build.helper as helper

    suffix = method_template['method_python_name_suffix']
%>\
    def ${f['python_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        return self._get_equalization_filter_coefficients(self.equalization_num_coefficients)
