<%page args="f, config, method_template"/>\
<%
    '''Creates a numpy array based on number of ports queried from driver and passes it to "get_deembedding_sparameters" method.'''
    import build.helper as helper
%>\

    def ${f['python_name']}(self):
        import numpy as np
        number_of_ports = self.get_deembedding_table_number_of_ports()
        sparameters_array_size = number_of_ports ** 2
        sparameters = np.full((number_of_ports, number_of_ports), 0 + 0j, dtype=np.complex128)
        if type(sparameters) is not np.ndarray:
            raise TypeError('sparameters must be {0}, is {1}'.format(np.ndarray, type(sparameters)))
        if np.isfortran(sparameters) is True:
            raise TypeError('sparameters must be in C-order')
        if sparameters.dtype is not np.dtype('complex128'):
            raise TypeError('sparameters must be np.ndarray of dtype=complex128, is ' + str(sparameters.dtype))
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        sparameters_ctype = _get_ctypes_pointer_for_buffer(value=sparameters, library_type=_complextype.NIComplexNumber)  # case B510
        sparameters_array_size_ctype = _visatype.ViInt32(sparameters_array_size)  # case S150
        number_of_sparameters_ctype = _visatype.ViInt32()  # case S220
        number_of_ports_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niRFSG_GetDeembeddingSparameters(vi_ctype, sparameters_ctype, sparameters_array_size_ctype, None if number_of_sparameters_ctype is None else (ctypes.pointer(number_of_sparameters_ctype)), None if number_of_ports_ctype is None else (ctypes.pointer(number_of_ports_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        number_of_ports = int(number_of_ports_ctype.value)
        sparameters = sparameters.reshape((number_of_ports, number_of_ports))
        return sparameters
