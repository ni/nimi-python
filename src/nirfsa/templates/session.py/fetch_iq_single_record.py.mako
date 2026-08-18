<%page args="f, config, method_template"/>\
<%
    '''Dispatches to the appropriate "fetch IQ single record" method based on the data type.'''
    import build.helper as helper
    suffix = method_template['method_python_name_suffix']
%>\

    def ${f['python_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_NUMPY_INTO_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        import numpy
        if str(type(iq_data_array)).find("'numpy.ndarray'") != -1:
            if number_of_samples is None:
                number_of_samples = self.number_of_samples

            if iq_data_array.dtype == numpy.int16:
                expected_buffer_size = 2 * number_of_samples
            else:
                expected_buffer_size = number_of_samples

            if len(iq_data_array) < expected_buffer_size:
                try:
                    iq_data_array.resize(expected_buffer_size, refcheck=False)
                except (MemoryError, ValueError) as e:
                    raise type(e)(
                        "Failed to resize iq_data_array from {} to {}: {}".format(
                            len(iq_data_array), expected_buffer_size, e
                        )
                    ) from e
                assert len(iq_data_array) == expected_buffer_size, "iq_data_array length must match requested number_of_samples after resize"

            if iq_data_array.dtype == numpy.complex128:
                wfm_info = self._fetch_iq_single_record_complex_f64(record_number, iq_data_array, timeout)
            elif iq_data_array.dtype == numpy.complex64:
                wfm_info = self._fetch_iq_single_record_complex_f32(record_number, iq_data_array, timeout)
            elif iq_data_array.dtype == numpy.int16:
                wfm_info = self._fetch_iq_single_record_complex_i16(record_number, iq_data_array, timeout)
            else:
                raise TypeError("Unsupported datatype. Is {}, expected {} or {} or {}".format(iq_data_array.dtype, numpy.complex128, numpy.complex64, numpy.int16))
        else:
            raise TypeError("Unsupported datatype. Expected numpy array of {} or {} or {}".format(numpy.complex128, numpy.complex64, numpy.int16))

        mv = memoryview(iq_data_array)

        wfm_info.samples = mv[0:wfm_info.actual_samples]

        return wfm_info
