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
            return self._delete_named_waveform(waveform_name_or_handle)
        else:
            return self._clear_arb_waveform(waveform_name_or_handle)

