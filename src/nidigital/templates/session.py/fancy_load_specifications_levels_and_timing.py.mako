<%page args="f, config, method_template"/>\
<%
    '''Forwards to _load_specifications(), _load_levels(), and _load_timing().'''
    import build.helper as helper
%>\
    def ${f['session_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['session_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        self._call_method_with_iterable(self._load_specifications, specifications_file_paths)
        self._call_method_with_iterable(self._load_levels, levels_file_paths)
        self._call_method_with_iterable(self._load_timing, timing_file_paths)

    ## Define the private method below the public method so that lock decorator gets added to the public method
    def _call_method_with_iterable(self, method, files):
        if files is None:
            return
        if isinstance(files, str):
            files = [files]
        for f in files:
            method(f)
