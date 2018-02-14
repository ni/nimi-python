<%page args="f, config, method_template"/>\
<%
    '''Dispatches to the appropriate "fetch waveform into" method based on the waveform type.'''
    import build.helper as helper

    suffix = method_template['method_python_name_suffix']
%>\
    def ${f['python_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_NUMPY_INTO_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        import numpy

        num_samples = int(len(wfm) / self._actual_num_wfms())

        if wfm.dtype == numpy.float64:
            return self._fetch_into(num_samples=num_samples, wfm=wfm, timeout=timeout)
        elif wfm.dtype == numpy.int8:
            return self._fetch_binary8_into(num_samples=num_samples, wfm=wfm, timeout=timeout)
        elif wfm.dtype == numpy.int16:
            return self._fetch_binary16_into(num_samples=num_samples, wfm=wfm, timeout=timeout)
        elif wfm.dtype == numpy.int32:
            return self._fetch_binary32_into(num_samples=num_samples, wfm=wfm, timeout=timeout)
        else:
            raise TypeError("Unsupported dtype. Is {0}, expected {1}, {2}, {3}, or {5}".format(wfm.dtype, numpy.float64, numpy.int8, numpy.int16, numpy.int32))

