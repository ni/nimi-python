<%page args="f, config, method_template"/>\
<%
    '''Dispatches to the appropriate "fetch IQ multi record" method based on the data type.'''
    import build.helper as helper
    suffix = method_template['method_python_name_suffix']
%>\
    def ${f['python_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        import numpy
        if str(type(iq_data_arrays)).find("'numpy.ndarray'") != -1:
            if number_of_records is None:
                number_of_records = self.number_of_records

            if number_of_samples is None:
                number_of_samples = self.number_of_samples

            if iq_data_arrays.ndim != 2:
                raise ValueError("iq_data_arrays must be a 2D numpy array (number_of_records x number_of_samples), but got {}D array".format(iq_data_arrays.ndim))
            if iq_data_arrays.shape[0] < number_of_records:
                raise ValueError("iq_data_arrays must have at least {} rows (number_of_records), but has {}".format(number_of_records, iq_data_arrays.shape[0]))
            if iq_data_arrays.dtype == numpy.int16:
                expected_buffer_size = 2 * number_of_samples
            else:
                expected_buffer_size = number_of_samples

            if iq_data_arrays.shape[1] < expected_buffer_size:
                try:
                    iq_data_arrays.resize((iq_data_arrays.shape[0], expected_buffer_size), refcheck=False)
                except (MemoryError, ValueError) as e:
                    raise type(e)(
                        "Failed to resize iq_data_arrays from {} to {}: {}".format(
                            iq_data_arrays.shape, (iq_data_arrays.shape[0], expected_buffer_size), e
                        )
                    ) from e
                assert iq_data_arrays.shape[1] == expected_buffer_size, "iq_data_arrays width must match requested number_of_samples after resize"

            if iq_data_arrays.dtype == numpy.complex128:
                wfm_info = self._fetch_iq_multi_record_complex_f64(starting_record, number_of_records, iq_data_arrays, timeout)
            elif iq_data_arrays.dtype == numpy.complex64:
                wfm_info = self._fetch_iq_multi_record_complex_f32(starting_record, number_of_records, iq_data_arrays, timeout)
            elif iq_data_arrays.dtype == numpy.int16:
                wfm_info = self._fetch_iq_multi_record_complex_i16(starting_record, number_of_records, iq_data_arrays, timeout)
            else:
                raise TypeError("Unsupported datatype. Is {}, expected {} or {} or {}".format(iq_data_arrays.dtype, numpy.complex128, numpy.complex64, numpy.int16))
        else:
            raise TypeError("Unsupported datatype. Expected numpy array of {} or {} or {}".format(numpy.complex128, numpy.complex64, numpy.int16))

        waveform_info._populate_samples_info(wfm_info, iq_data_arrays)

        return wfm_info