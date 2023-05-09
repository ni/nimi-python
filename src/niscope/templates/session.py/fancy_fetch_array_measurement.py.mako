<%page args="f, config, method_template"/>\
<%
    '''Forwards to _fetch_array_measurement with cleaner return values.'''
    import build.helper as helper
    suffix = method_template['method_python_name_suffix']
%>\
    def ${f['python_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        r'''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        # Set the fetch attributes
        with _NoChannel(session=self):
            self._fetch_relative_to = relative_to
            self._fetch_offset = offset
            self._fetch_record_number = record_number
            self._fetch_num_records = -1 if num_records is None else num_records
            self._fetch_meas_num_samples = -1 if meas_num_samples is None else meas_num_samples

        # For GrpcStubInterpreter, the server will automatically get _actual_meas_wfm_size, if needed.
        if isinstance(self._interpreter, _library_interpreter.LibraryInterpreter):
            if meas_wfm_size is None:
                meas_wfm_size = self._actual_meas_wfm_size(array_meas_function)

        meas_wfm, wfm_info = self._${f['python_name']}(array_meas_function, meas_wfm_size, timeout)

        record_length = int(len(meas_wfm) / len(wfm_info))
        waveform_info._populate_samples_info(wfm_info, meas_wfm, record_length)

<%include file="./fetch_waveform_info_population.py.mako"/>

        return wfm_info
