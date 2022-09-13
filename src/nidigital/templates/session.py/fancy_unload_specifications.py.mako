<%page args="f, config, method_template"/>\
<%
    '''Forwards to _unload_specifications().'''
    import build.helper as helper
%>\
    def ${f['session_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['session_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        self._call_method_with_iterable(self._unload_specifications, file_paths)
