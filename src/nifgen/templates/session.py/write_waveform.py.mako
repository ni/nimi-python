<%page args="f, config, method_template"/>\
<%
    '''Dispatches to the appropriate "write waveform" method based on the waveform type.'''
    import build.helper as helper
%>\
    def ${f['session_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['session_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        use_named = isinstance(waveform_name_or_handle, str)
        # Check the type by using string comparison so that we don't import numpy unnecessarily.
        if str(type(data)).find("'numpy.ndarray'") != -1:
            import numpy
            if data.dtype == numpy.float64:
                return self._write_named_waveform_f64_numpy(waveform_name_or_handle, data) if use_named else self._write_waveform_numpy(waveform_name_or_handle, data)
            elif data.dtype == numpy.int16:
                return self._write_named_waveform_i16_numpy(waveform_name_or_handle, data) if use_named else self._write_binary16_waveform_numpy(waveform_name_or_handle, data)
            else:
                raise TypeError("Unsupported dtype. Is {0}, expected {1} or {2}".format(data.dtype, numpy.float64, numpy.int16))
        elif isinstance(data, array.array):
            if data.typecode == 'd':
                return self._write_named_waveform_f64(waveform_name_or_handle, data) if use_named else self._write_waveform(waveform_name_or_handle, data)
            elif data.typecode == 'h':
                return self._write_named_waveform_i16(waveform_name_or_handle, data) if use_named else self._write_binary16_waveform(waveform_name_or_handle, data)
            else:
                raise TypeError("Unsupported dtype. Is {0}, expected {1} or {2}".format(data.typecode, 'd (double)', 'h (16 bit int)'))

        return self._write_named_waveform_f64(waveform_name_or_handle, data) if use_named else self._write_waveform(waveform_name_or_handle, data)
