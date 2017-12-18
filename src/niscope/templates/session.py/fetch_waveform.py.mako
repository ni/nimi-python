<%page args="f, config"/>\
<%
    '''Dispatches to the appropriate "create waveform" method based on the waveform type.'''
    import build.helper as helper
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, method_template, False, config, indent=8)}
        '''
        try:
            import numpy
            numpy_imported = True
        except ImportError:
            numpy_imported = False

        if wfm is not None and numpy_imported is True and type(wfm) == numpy.ndarray:
            if wfm.dtype == numpy.float64:
                return self._fetch_double_into(num_samples, wfm, timeout)
            elif wfm.dtype == numpy.int8:
                return self._fetch_binary8_into(num_samples, wfm, timeout)
            elif wfm.dtype == numpy.int16:
                return self._fetch_binary16_into(num_samples, wfm, timeout)
            elif wfm.dtype == numpy.int32:
                return self._fetch_binary32_into(num_samples, wfm, timeout)
            else:
                raise TypeError("Unsupported dtype. Is {0}, expected {1}, {2}, {3}, or {5}".format(wfm.dtype, numpy.float64, numpy.int8, numpy.int16, numpy.int32))
        else:
            return self._fetch_double(num_samples, timeout)

