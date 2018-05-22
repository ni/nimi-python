<%page args="f, config, method_template"/>\
<%
    '''Dispatches to the appropriate "fetch waveform into" method based on the waveform type.'''
    import build.helper as helper

    suffix = method_template['method_python_name_suffix']
%>\
    def ${f['python_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_NUMPY_INTO_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        import numpy
        import sys

        # Set the fetch attributes
        with _NoChannel(session=self):
            self._fetch_relative_to = relative_to
            self._fetch_offset = offset
            self._fetch_record_number = record_number
            self._fetch_num_records = -1 if num_records is None else num_records

        num_samples = int(len(waveform) / self._actual_num_wfms())

        if waveform.dtype == numpy.float64:
            wfm_info = self._fetch_into_numpy(num_samples=num_samples, waveform=waveform, timeout=timeout)
        elif waveform.dtype == numpy.int8:
            wfm_info = self._fetch_binary8_into_numpy(num_samples=num_samples, waveform=waveform, timeout=timeout)
        elif waveform.dtype == numpy.int16:
            wfm_info = self._fetch_binary16_into_numpy(num_samples=num_samples, waveform=waveform, timeout=timeout)
        elif waveform.dtype == numpy.int32:
            wfm_info = self._fetch_binary32_into_numpy(num_samples=num_samples, waveform=waveform, timeout=timeout)
        else:
            raise TypeError("Unsupported dtype. Is {0}, expected {1}, {2}, {3}, or {5}".format(waveform.dtype, numpy.float64, numpy.int8, numpy.int16, numpy.int32))

        if sys.version_info.major >= 3:
            # In Python 3 and newer we can use memoryview objects to give us pieces of the underlying array. This is much faster
            mv = memoryview(waveform)

        i = 0
        lwfm_i = len(wfm_info)
        lrcl = len(self._repeated_capability_list)
        assert lwfm_i % lrcl == 0, 'Number of waveforms should be evenly divisible by the number of channels: len(wfm_infos) == {0}, len(self._repeated_capability_list) == {1}'.format(lwfm_i, lrcl)
        actual_num_records = int(lwfm_i / lrcl)
        for chan in self._repeated_capability_list:
            for rec in range(offset, offset + actual_num_records):
                wfm_info[i].channel = chan
                wfm_info[i].record = rec

                if sys.version_info.major >= 3:
                    start = i * num_samples
                    end = start + wfm_info[i].actual_samples
                    del wfm_info[i].actual_samples
                    wfm_info[i].samples = mv[start:end]

                i += 1

        return wfm_info

