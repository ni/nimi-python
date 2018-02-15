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

        if num_samples is None and wfm is None:
            raise TypeError("Either 'num_samples' or 'wfm' must be set")

        # Check optional parameters
        if fetch_relative_to is not None:
            self.fetch_relative_to = fetch_relative_to
        if fetch_offet is not None:
            self.fetch_offet = fetch_offet
        if fetch_record_number is not None:
            self.fetch_record_number = fetch_record_number
        if fetch_num_records is not None:
            self.fetch_num_records = fetch_num_records

        num_wfms = self._actual_num_wfms()

        if num_samples is None:
            num_samples_to_use = int(len(wfm) / num_wfms)
        else:
            num_samples_to_use = num_samples

        total_wfm_size = num_samples_to_use * num_wfms

        # If the waveform is not passed in, we will use the builtin python array with element type 'double'
        if wfm is None:
            wfm_to_use, wfm_info = self._fetch(num_samples, timeout)
        else:
            if len(wfm) < total_wfm_size:
                raise TypeError('The size of the input array is too small for the acquisition. Needs to be {0}, was {1}'.format(total_wfm_size, len(wfm_to_use)))

            wfm_to_use = wfm
            wfm_info = self.fetch_into(wfm_to_use, timeout)

        # memoryview in Python 2 doesn't support numeric types, so we copy into an array.array to put in the wfm. :( You should be using Python 3! Or use the _into version
        if sys.version_info.major < 3:
            for i in range(len(wfm_info)):
                if isinstance(wfm_to_use, array.array):
                    typecode = wfm_to_use.typecode
                else:
                    import numpy
                    # If we've made it this far we know the numpy type is one of these
                    typecode = {
                        numpy.dtype('int8'): 'b',
                        numpy.dtype('int16'): 'h',
                        numpy.dtype('int32'): 'l',
                        numpy.dtype('float64'): 'd',
                    }[wfm_to_use.dtype]

                start = i * num_samples_to_use
                end = start + num_samples_to_use
                wfm_info[i].wfm = array.array(typecode, wfm_to_use[start:end])
        else:
            # In Python 3 we can use memoryview objects to give us pieces of the underlying array. This is much faster
            mv = memoryview(wfm_to_use)

            for i in range(len(wfm_info)):
                start = i * num_samples_to_use
                end = start + num_samples_to_use
                wfm_info[i].wfm = mv[start:end]

        return wfm_info

