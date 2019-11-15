<%page args="f, config, method_template"/>\
<%
    import build.helper as helper
    suffix = method_template['method_python_name_suffix']
%>\
    def ${f['python_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        if len(waveform_data) == 0:
            # Nothing to do
            return

        site_list = []
        # We assume all the entries are the same length (we'll check later) to make the array the correct size
        # Get an entry from the dictionary from https://stackoverflow.com/questions/30362391/how-do-you-find-the-first-key-in-a-dictionary
        actual_samples_per_waveform = len(waveform_data[next(iter(waveform_data))])
        data = array.array('L', [0] * (len(waveform_data) * actual_samples_per_waveform))
        mv = memoryview(data)

        i = 0
        for site in waveform_data:
            if len(waveform_data[site]) != actual_samples_per_waveform:
                raise ValueError('Mismatched length of waveforms. All must be the same length.')
            if waveform_data[site].typecode != 'L':
                raise ValueError('Wrong array element type. Must be unsigned 32 bit int ("L"), was {}'.format(waveform_data[site].typecode))

            site_list.append(str(site))

            start = i * actual_samples_per_waveform
            end = start + actual_samples_per_waveform
            mv[start:end] = waveform_data[site]

            i += 1

        site_list_str = ','.join(site_list)

        self._write_source_waveform_site_unique(site_list_str, waveform_name, len(waveform_data), actual_samples_per_waveform, data)

