<%page args="f, config, method_template"/>\
<%
    '''Dispatches to the appropriate "read IQ single record" method based on the data type.'''
    import build.helper as helper
    suffix = method_template['method_python_name_suffix']
%>\
    def ${f['python_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        import numpy
        if str(type(iq_data_array)).find("'numpy.ndarray'") != -1:
            if iq_data_array.dtype != numpy.complex128:
                raise TypeError("Unsupported dtype. Is {}, expected {}".format(iq_data_array.dtype, numpy.complex128))

            expected_buffer_size = self.number_of_samples
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

            wfm_info = self._read_iq_single_record_complex_f64(iq_data_array, timeout)
        else:
            raise TypeError("Unsupported datatype. Expected numpy array of {}".format(numpy.complex128))

        mv = memoryview(iq_data_array)

        wfm_info.samples = mv[0:self.number_of_samples]

        return wfm_info
