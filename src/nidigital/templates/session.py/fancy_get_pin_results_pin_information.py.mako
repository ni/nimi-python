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
        PinInfo = collections.namedtuple('PinInformation', ['pin_indexes', 'site_numbers', 'channel_indexes'])

        pin_indexes, site_number, channel_indexes = self._${f['python_name']}()

        return [PinInfo(pin_indexes=pin_indexes[i], site_numbers=site_numbers[i], channel_indexes=channel_indexes) for i in range(len(pin_indexes))]

