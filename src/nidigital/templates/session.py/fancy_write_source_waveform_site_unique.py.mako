<%page args="f, config, method_template"/>\
<%
    import build.helper as helper
    suffix = method_template['method_python_name_suffix']
%>\
    def ${f['session_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['session_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        from collections.abc import Mapping
        if not isinstance(waveform_data, Mapping):
            raise TypeError("Expecting waveform_data to be a dictionary but got {}".format(type(waveform_data)))
        site_list = []
        # We assume all the entries are the same length (we'll check later) to make the array the correct size
        # Get an entry from the dictionary from https://stackoverflow.com/questions/30362391/how-do-you-find-the-first-key-in-a-dictionary
        if len(waveform_data) == 0:
            actual_samples_per_waveform = 0
        else:
            actual_samples_per_waveform = len(waveform_data[next(iter(waveform_data))])
        data = array.array('L', [0] * (len(waveform_data) * actual_samples_per_waveform))
        mv = memoryview(data)

        i = 0
        for site in waveform_data:
            if len(waveform_data[site]) != actual_samples_per_waveform:
                raise ValueError('Mismatched length of waveforms. All must be the same length.')
            # Check the type by using string comparison so that we don't import numpy unnecessarily.
            if str(type(waveform_data[site])).find("'numpy.ndarray'") != -1:
                import numpy
                if waveform_data[site].dtype == numpy.uint32:
                    wfm = array.array('L', waveform_data[site])
                else:
                    raise TypeError("Unsupported dtype for waveform_data array element type. Is {0}, expected {1}".format(waveform_data[site].dtype, numpy.int32))

            elif isinstance(waveform_data[site], array.array):
                if waveform_data[site].typecode == 'L':
                    wfm = waveform_data[site]
                else:
                    raise TypeError('Wrong waveform_data array element type. Must be unsigned 32 bit int ("L"), was {}'.format(waveform_data[site].typecode))

            elif isinstance(waveform_data[site], list):
                wfm = array.array('L', waveform_data[site])

            else:
                raise TypeError('Unknown array type: {}'.format(type(waveform_data[site])))

            site_list.append(site)

            start = i * actual_samples_per_waveform
            end = start + actual_samples_per_waveform
            mv[start:end] = wfm

            i += 1

        self.sites[site_list]._write_source_waveform_site_unique_u32(waveform_name, len(waveform_data), actual_samples_per_waveform, data)
