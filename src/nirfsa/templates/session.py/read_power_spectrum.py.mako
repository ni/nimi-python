<%page args="f, config, method_template"/>\
<%
    '''Dispatches to the appropriate "read power spectrum" method based on the data type.'''
    import build.helper as helper
    suffix = method_template['method_python_name_suffix']
%>\
    def ${f['python_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        import numpy
        if str(type(power_spectrum_data_array)).find("'numpy.ndarray'") != -1:
            expected_buffer_size = self.number_of_spectral_lines

            if len(power_spectrum_data_array) < expected_buffer_size:
                try:
                    power_spectrum_data_array.resize(expected_buffer_size, refcheck=False)
                except (MemoryError, ValueError) as e:
                    raise type(e)(
                        "Failed to resize power_spectrum_data_array from {} to {}: {}".format(
                            len(power_spectrum_data_array), expected_buffer_size, e
                        )
                    ) from e
                assert len(power_spectrum_data_array) == expected_buffer_size, "power_spectrum_data_array length must match number_of_spectral_lines after resize"

            if power_spectrum_data_array.dtype == numpy.float64:
                spectrum_info = self._read_power_spectrum_f64(power_spectrum_data_array, timeout)
            elif power_spectrum_data_array.dtype == numpy.float32:
                spectrum_info = self._read_power_spectrum_f32(power_spectrum_data_array, timeout)
            else:
                raise TypeError("Unsupported dtype. Is {}, expected {} or {}".format(power_spectrum_data_array.dtype, numpy.float64, numpy.float32))
        else:
            raise TypeError("Unsupported datatype. Expected numpy array of {} or {}".format(numpy.float64, numpy.float32))

        mv = memoryview(power_spectrum_data_array)

        spectrum_info_type._populate_samples_info(spectrum_info, mv)

        return spectrum_info
