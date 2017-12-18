<%page args="f, config"/>\
<%
    '''Dispatches to the appropriate "create waveform" method based on the waveform type.'''
    import build.helper as helper
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, method_template, False, config, indent=8)}
        '''
        # Check the type by using string comparison so that we don't import numpy unecessarilly.
        if str(type(waveform_data_array)) == "<type 'numpy.ndarray'>":
            import numpy
            if waveform_data_array.dtype == numpy.float64:
                return self._create_waveform_f64_numpy(waveform_data_array)
            elif waveform_data_array.dtype == numpy.int16:
                return self._create_waveform_i16_numpy(waveform_data_array)
            else:
                raise TypeError("Unsupported dtype. Is {0}, expected {1} or {2}".format(waveform_data_array.dtype, numpy.float64, numpy.int16))

        return self._create_waveform_f64(waveform_data_array)

