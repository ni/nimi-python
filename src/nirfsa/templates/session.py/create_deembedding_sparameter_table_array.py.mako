<%page args="f, config, method_template"/>\
<%
    '''Ensures that incoming array has appropriate dimension sizes and calculates the number of ports and sparameter table size parameters based on array dimensions before calling into "create_deembedding_sparameter_table_array" method.'''
    import build.helper as helper
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        if (str(type(sparameter_table)).find("'numpy.ndarray'") != -1) or (str(type(frequencies)).find("'numpy.ndarray'") != -1):
            if sparameter_table.ndim == 3:
                if frequencies.size == sparameter_table.shape[0]:
                    if sparameter_table.shape[1] == sparameter_table.shape[2]:
                        number_of_ports = sparameter_table.shape[1]
                        return self._create_deembedding_sparameter_table_array(port, table_name, frequencies, sparameter_table, number_of_ports, sparameter_orientation)
                    else:
                        raise ValueError("Row and column count of sparameter table should be equal. Table row count is {} and column count is {}.".format(sparameter_table.shape[1], sparameter_table.shape[2]))
                else:
                    raise ValueError("Frequencies count does not match the sparameter table count. Frequencies count is {} and sparameter table count is {}.".format(frequencies.size, sparameter_table.shape[0]))
            else:
                raise ValueError("Unsupported array dimension. Is {}, expected 3".format(sparameter_table.ndim))
        else:
            raise TypeError("Unsupported datatype. Expected numpy array.")
