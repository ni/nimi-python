<%page args="f, config, method_template"/>\
<%
    '''Dispatches to the appropriate "write arb waveform" method based on the waveform type.'''
    import build.helper as helper
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        if str(type(waveform_data_array)).find("'numpy.ndarray'") != -1:
            import numpy
            if waveform_data_array.dtype == numpy.complex128:
                return self._write_arb_waveform_complex_f64(waveform_name, waveform_data_array, more_data_pending)
            elif waveform_data_array.dtype == numpy.complex64:
                return self._write_arb_waveform_complex_f32(waveform_name, waveform_data_array, more_data_pending)
            elif waveform_data_array.dtype == numpy.int16:
                return self._write_arb_waveform_complex_i16(waveform_name, waveform_data_array, more_data_pending)
            else:
                raise TypeError("Unsupported dtype. Is {}, expected {} or {} or {}".format(waveform_data_array.dtype, numpy.complex128, numpy.complex64, numpy.int16))
        else:
            raise TypeError("Unsupported dtype. Is {}, expected {} or {} or {}".format(waveform_data_array.dtype, numpy.complex128, numpy.complex64, numpy.int16))

        return self._write_arb_waveform_complex_f64(waveform_name, waveform_data_array, more_data_pending)
