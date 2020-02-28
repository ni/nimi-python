<%page args="f, config, method_template"/>\
<%
    import build.helper as helper
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        pattern_pin_list = self.get_pattern_pin_list(start_label)
        return [x.strip() for x in pattern_pin_list.split(',')]

