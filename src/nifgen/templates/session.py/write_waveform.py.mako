<%page args="f, config, method_template"/>\
<%
    '''Dispatches to the appropriate "write waveform" method based on the waveform type.'''
    import build.helper as helper
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, method_template, False, config, indent=8)}
        '''

        use_named = isinstance(waveform_name_or_handle, str)

        try:
            import numpy
            if type(data) == numpy.ndarray:
                if data.dtype == numpy.float64:
                    if use_named:
                        return self._write_named_waveform_f64_numpy(waveform_name_or_handle, data)
                    else:
                        return self._write_waveform_numpy(waveform_name_or_handle, data)
                elif data.dtype == numpy.int16:
                    if use_named:
                        return self._write_named_waveform_i16_numpy(waveform_name_or_handle, data)
                    else:
                        return self._write_binary16_waveform_numpy(waveform_name_or_handle, data)
                else:
                    raise TypeError("Unsupported dtype. Is {0}, expected {1} or {2}".format(data.dtype, numpy.float64, numpy.int16))
        except ImportError:
            pass

        if use_named:
            return self._write_named_waveform_f64(waveform_name_or_handle, data)
        else:
            return self._write_waveform(waveform_name_or_handle, data)

