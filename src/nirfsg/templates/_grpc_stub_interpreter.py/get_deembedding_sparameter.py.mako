<%page args="f, config, method_template"/>\
<%
    '''Creates a numpy array based on number of ports queried from driver and passes it to "get_deembedding_sparameters" method.'''
    import build.helper as helper
%>\
    def ${f['interpreter_name']}(self):
        import numpy as np
        response = self._invoke(
            self._client.GetDeembeddingSparameters,
            grpc_types.GetDeembeddingSparametersRequest(vi=self._vi),
        )
        number_of_ports = response.number_of_ports
        sparameters = np.array([c.real + 1j * c.imaginary for c in response.sparameters], dtype=np.complex128)
        sparameters = sparameters.reshape((number_of_ports, number_of_ports))
        return sparameters
