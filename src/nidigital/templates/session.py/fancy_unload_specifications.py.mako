<%page args="f, config, method_template"/>\
<%
    '''Forwards to _unload_specifications().'''
    import build.helper as helper
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        self._file_helper(self._unload_specifications, file_paths)

