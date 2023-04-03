<%page args="f, config, method_template"/>\
<%
    '''Dispatches to the appropriate "write waveform" method based on the waveform type.'''
    import build.helper as helper
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        if isinstance(waveform_name_or_handle, str):
            return self._set_named_waveform_next_write_position(waveform_name_or_handle, relative_to, offset)
        else:
            return self._set_waveform_next_write_position(waveform_name_or_handle, relative_to, offset)
