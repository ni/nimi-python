<%page args="f, config, method_template"/>\
<%
    '''Renders a GrpcStubInterpreter method for reading repeated NIComplex proto fields into numpy arrays.'''
    import build.helper as helper
    parameters = f['parameters']
    param_names_method = helper.get_params_snippet(f, helper.ParameterUsageOptions.INTERPRETER_NUMPY_INTO_METHOD_DECLARATION)
    grpc_name = f.get('grpc_name', f['name'])
    grpc_request_args = helper.get_params_snippet(f, helper.ParameterUsageOptions.GRPC_REQUEST_PARAMETERS)
    return_statement = helper.get_grpc_interpreter_method_return_snippet(parameters, config, use_numpy_array=True)
    if return_statement == 'return':
        return_statement = None
    capture_response = 'response = ' if return_statement else ''
    included_in_proto = f.get('included_in_proto', True)
    full_func_name = f['interpreter_name'] + method_template['method_python_name_suffix']
    numpy_complex_params = [p for p in helper.filter_parameters(parameters, helper.ParameterUsageOptions.NUMPY_PARAMETERS) if p['complex_type'] is not None]
%>\

    def ${full_func_name}(${param_names_method}):  # noqa: N802
        import numpy
% if included_in_proto:
        ${capture_response}self._invoke(
            self._client.${grpc_name},
            grpc_types.${grpc_name}Request(${grpc_request_args}),
        )
% for p in numpy_complex_params:
% if p['original_type'] == 'NIComplexNumber[]':
        temp_array = numpy.array([(c.real, c.imag) for c in response.${p['python_name']}], dtype=numpy.complex128)
% elif p['original_type'] == 'NIComplexNumberF32[]':
        temp_array = numpy.array([(c.real, c.imag) for c in response.${p['python_name']}], dtype=numpy.complex64)
% elif p['original_type'] == 'NIComplexI16[]':
        temp_array = numpy.array([(c.real, c.imag) for c in response.${p['python_name']}], dtype=numpy.dtype([('real', numpy.int16), ('imag', numpy.int16)]))
% endif
        numpy.copyto(${p['python_name']}, temp_array.view(${p['python_name']}.dtype).reshape(${p['python_name']}.shape))
% endfor
% if return_statement:
        ${return_statement}
% endif
% else:
        raise NotImplementedError('${full_func_name} is not supported over gRPC')
% endif
