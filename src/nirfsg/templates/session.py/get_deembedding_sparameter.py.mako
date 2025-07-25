<%page args="f, config, method_template"/>\
<%
    '''Creates a numpy array based on number of ports queried from driver and passes it to "get_deembedding_sparameters" method.'''
    import build.helper as helper
%>\
    def ${f['python_name']}(self):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        import numpy as np
        number_of_ports = self._get_deembedding_table_number_of_ports()
        sparameter_table_size = number_of_ports ** 2
        sparameters = np.full((number_of_ports, number_of_ports), 0 + 0j, dtype=np.complex128)
        number_of_ports = self._interpreter.get_deembedding_sparameters(sparameters, sparameter_table_size)
        sparameters = sparameters.reshape((number_of_ports, number_of_ports))
        return sparameters, number_of_ports
