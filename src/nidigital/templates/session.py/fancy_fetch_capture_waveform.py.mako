<%page args="f, config, method_template"/>\
<%
    '''Dispatches to the appropriate "fetch waveform into" method based on the waveform type.'''
    import build.helper as helper

    suffix = method_template['method_python_name_suffix']
%>\
    def _fetch_capture_waveform(self, site_list, waveform_name, samples_to_read, timeout):
        # This is slightly modified codegen from the function
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(site_list.encode(self._encoding))  # case C020
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        samples_to_read_ctype = _visatype.ViInt32(samples_to_read)  # case S150
        timeout_ctype = _visatype.ViReal64(timeout)  # case S150
        data_buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        data_ctype = None  # case B610
        actual_num_waveforms_ctype = _visatype.ViInt32()  # case S220
        actual_samples_per_waveform_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_FetchCaptureWaveformU32(vi_ctype, site_list_ctype, waveform_name_ctype, samples_to_read_ctype, timeout_ctype, data_buffer_size_ctype, data_ctype, None if actual_num_waveforms_ctype is None else (ctypes.pointer(actual_num_waveforms_ctype)), None if actual_samples_per_waveform_ctype is None else (ctypes.pointer(actual_samples_per_waveform_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        data_buffer_size_ctype = _visatype.ViInt32(actual_num_waveforms_ctype.value)  # case S200
        data_size = actual_num_waveforms_ctype.value * actual_samples_per_waveform_ctype.value  # case B620 (modified)
        data_array = array.array("L", [0] * data_size)  # case B620
        data_ctype = get_ctypes_pointer_for_buffer(value=data_array, library_type=_visatype.ViUInt32)  # case B620
        error_code = self._library.niDigital_FetchCaptureWaveformU32(vi_ctype, site_list_ctype, waveform_name_ctype, samples_to_read_ctype, timeout_ctype, data_buffer_size_ctype, data_ctype, None if actual_num_waveforms_ctype is None else (ctypes.pointer(actual_num_waveforms_ctype)), None if actual_samples_per_waveform_ctype is None else (ctypes.pointer(actual_samples_per_waveform_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return data_array, actual_num_waveforms_ctype.value, actual_samples_per_waveform_ctype.value

    def ${f['python_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_NUMPY_INTO_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        import collections
        import sys

        timeout_secs = _converters.convert_timedelta_to_seconds(timeout, _visatype.ViReal64)
        data, actual_num_waveforms, actual_samples_per_waveform = self._fetch_capture_waveform(site_list, waveform_name, samples_to_read, timeout_secs)

        # Get the site list
        site_list = self.get_site_results_site_numbers(site_list, enums.SiteType.CAPTURE_WAVEFORM)
        assert len(site_list) == actual_num_waveforms

        Measurement = collections.namedtuple('Measurement', ['data', 'site'])

        measurements = []

        if sys.version_info.major >= 3:
            # In Python 3 and newer we can use memoryview objects to give us pieces of the underlying array. This is much faster
            mv = memoryview(data)

        for i in range(actual_num_waveforms):
            start = i * actual_samples_per_waveform
            end = start + actual_samples_per_waveform
            if sys.version_info.major >= 3:
                measurements.append(Measurement(data=mv[start:end], site=site_list[i]))
            else:
                # memoryview in Python 2 doesn't support numeric types, so we copy into an array.array to put in the wfm. :( You should be using Python 3!
                # Or use the _into version. memoryview in Python 2 only supports string and bytearray, not array.array or numpy.ndarray of arbitrary types.
                measurements.append(Measurement(data=array.array('d', data[start:end]), site=site_list[i]))

        return measurements

