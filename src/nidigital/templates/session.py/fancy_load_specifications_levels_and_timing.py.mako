<%page args="f, config, method_template"/>\
<%
    '''Forwards to _load_specifications(), _load_levels(), and _load_timing().'''
    import build.helper as helper
%>\
    def _load_files(self, loader, files):
        if isinstance(files, str):
            files = [files]
        for f in files:
            loader(f)

    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        if specifications_file_paths is not None:
            self._load_files(self._load_specifications, specifications_file_paths)
        if levels_file_paths is not None:
            self._load_files(self._load_levels, levels_file_paths)
        if timing_file_paths is not None:
            self._load_files(self._load_timing, timing_file_paths)

