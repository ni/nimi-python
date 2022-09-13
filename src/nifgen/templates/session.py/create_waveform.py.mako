<%page args="f, config"/>\
<%
    '''Dispatches to the appropriate "create waveform" method based on the waveform type.'''
    import build.helper as helper
%>\
    def ${f['session_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['session_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        # Check the type by using string comparison so that we don't import numpy unnecessarily.
        if str(type(waveform_data_array)).find("'numpy.ndarray'") != -1:
            import numpy
            if waveform_data_array.dtype == numpy.float64:
                return self._create_waveform_f64_numpy(waveform_data_array)
            elif waveform_data_array.dtype == numpy.int16:
                return self._create_waveform_i16_numpy(waveform_data_array)
            else:
                raise TypeError("Unsupported dtype. Is {0}, expected {1} or {2}".format(waveform_data_array.dtype, numpy.float64, numpy.int16))
        elif isinstance(waveform_data_array, array.array):
            if waveform_data_array.typecode == 'd':
                return self._create_waveform_f64(waveform_data_array)
            elif waveform_data_array.typecode == 'h':
                return self._create_waveform_i16(waveform_data_array)
            else:
                raise TypeError("Unsupported dtype. Is {0}, expected {1} or {2}".format(waveform_data_array.typecode, 'd (double)', 'h (16 bit int)'))

        return self._create_waveform_f64(waveform_data_array)
