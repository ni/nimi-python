<%page args="f, config, method_template"/>\
<%
    '''Forwards to _fetch()/_read() with a nicer interface'''
    import build.helper as helper
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        import collections
        PinInfo = collections.namedtuple('PinInformation', ['pin_name', 'site_number', 'channel_name'])

        pin_indexes, site_numbers, channel_indexes = self._${f['python_name']}()
        assert len(pin_indexes) == len(site_numbers), "length of returned arrays don't match"
        assert len(pin_indexes) == len(channel_indexes), "length of returned arrays don't match"

        pin_infos = []
        for i in range(len(pin_indexes)):
            pin_name = "" if pin_indexes[i] == -1 else self._get_pin_name(pin_indexes[i])
            channel_names = self.get_channel_names(channel_indexes[i] - 1)  # channel_indexes are 1-based
            assert 1 == len(channel_names)
            pin_infos.append(PinInfo(pin_name=pin_name, site_number=site_numbers[i], channel_name=channel_names[0]))

        return pin_infos
