<%page args="f, config, method_template"/>\
<%
    '''Dispatches to the appropriate configure spectrum frequency method based on provided parameters.'''
    import build.helper as helper
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        if center_frequency is not None and span is not None:
            self._configure_spectrum_frequency_center_span(center_frequency, span)
        elif start_frequency is not None and stop_frequency is not None:
            self._configure_spectrum_frequency_start_stop(start_frequency, stop_frequency)
        else:
            raise ValueError(
                "Provide either (center_frequency & span) "
                "or (start_frequency & stop_frequency)"
            )
