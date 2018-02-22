<%page args="f, config, method_template"/>\
<%
    '''Forwards to _fetch_double()'''
    import build.helper as helper

    suffix = method_template['method_python_name_suffix']
%>\
    def ${f['python_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        import sys

        # Set attributes
        self.fetch_relative_to = fetch_relative_to
        self.fetch_offset = fetch_offset
        self.fetch_record_number = fetch_record_number
        self.fetch_num_records = fetch_num_records

        wfm, wfm_info = self._fetch(num_samples, timeout)

        if sys.version_info.major < 3:
            # memoryview in Python 2 doesn't support numeric types, so we copy into an array.array to put in the wfm. :( You should be using Python 3!
            # Or use the _into version. memoryview in Python 2 only supports string and bytearray, not array.array or numpy.ndarray of arbitrary types.
            for i in range(len(wfm_info)):
                start = i * num_samples
                end = start + num_samples
                wfm_info[i].wfm = array.array('d', wfm[start:end])
        else:
            # In Python 3 and newer we can use memoryview objects to give us pieces of the underlying array. This is much faster
            mv = memoryview(wfm)

            for i in range(len(wfm_info)):
                start = i * num_samples
                end = start + num_samples
                wfm_info[i].wfm = mv[start:end]

        return wfm_info

