<%page args="f, config, method_template"/>\
<%
    '''Creates a numpy array based on number of ports queried from driver and passes it to "get_deembedding_sparameters" method.'''
    import build.helper as helper
%>\
    def ${f['python_name']}(self):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, True, config, indent=8)}
        '''
        sparameters = self._interpreter.get_deembedding_sparameters()
        return sparameters
