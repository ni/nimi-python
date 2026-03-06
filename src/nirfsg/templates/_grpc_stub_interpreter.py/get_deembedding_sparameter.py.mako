<%page args="f, config, method_template"/>\
<%
    '''Retrieves S-parameters from the gRPC call response and converts them to a reshaped numpy array.'''
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
