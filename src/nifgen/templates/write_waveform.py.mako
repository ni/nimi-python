<%page args="f, config"/>\
<%
    '''Dispatches to the appropriate "write waveform" method based on the waveform type.'''
    import build.helper as helper
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f['name'], config, indent=8)}
        '''
        try:
            import numpy
            numpy_imported = True
        except ImportError:
            numpy_imported = False

        if numpy_imported is True and type(data) == numpy.ndarray:
            if data.dtype == numpy.float64:
                return self._write_waveform_numpy(waveform_handle, data)
            elif data.dtype == numpy.int16:
                return self._write_binary16_waveform_numpy(waveform_handle, data)
            else:
                raise TypeError("Unsupported dtype. Is {0}, expected {1} or {2}".format(data.dtype, numpy.float64, numpy.int16))

        return self._write_waveform(waveform_handle, data)

