<%page args="f, config, method_template"/>\
<%
    '''Renders a GrpcStubInterpreter method for numpy write operations with complex number support.'''
    import build.helper as helper
    parameters = f['parameters']
    full_func_name = f['interpreter_name'] + method_template['method_python_name_suffix']
    method_decl_params = helper.get_params_snippet(f, helper.ParameterUsageOptions.INTERPRETER_METHOD_DECLARATION)
    included_in_proto = f.get('included_in_proto', True)
    
    # Identify numpy parameters with complex number types
    numpy_complex_params = [
        p for p in helper.filter_parameters(parameters, helper.ParameterUsageOptions.NUMPY_PARAMETERS)
        if p.get('complex_array_representation') is not None and p.get('original_type') in ('NIComplexNumber[]', 'NIComplexNumberF32[]', 'NIComplexI16[]')
    ]
    
    # Only generate gRPC implementation if complex parameters exist and included in proto
    should_generate_grpc_impl = len(numpy_complex_params) > 0 and included_in_proto
    
    if should_generate_grpc_impl:
        # Generate gRPC request with complex number conversion
        grpc_name = f.get('grpc_name', f['name'])
        grpc_request_args = helper.get_params_snippet(f, helper.ParameterUsageOptions.GRPC_REQUEST_PARAMETERS)
        
        # Replace parameter names with _list suffixed versions for complex parameters
        for p in numpy_complex_params:
            grpc_request_args = grpc_request_args.replace(
                p['grpc_name'] + '=' + p['python_name'],
                p['grpc_name'] + '=' + p['python_name'] + '_list'
            )
        
        return_statement = helper.get_grpc_interpreter_method_return_snippet(f['parameters'], config)
        if return_statement == 'return':
            return_statement = None
        capture_response = 'response = ' if return_statement else ''
%>\

    def ${full_func_name}(${method_decl_params}):  # noqa: N802
% if should_generate_grpc_impl:
% for p in numpy_complex_params:
% if p['original_type'] == 'NIComplexNumber[]':
        ${p['python_name']}_list = [
            grpc_complex_types.NIComplexNumber(real=val.real, imaginary=val.imag)
            for val in ${p['python_name']}.ravel()
        ]
% elif p['original_type'] == 'NIComplexNumberF32[]':
        ${p['python_name']}_list = [
            grpc_complex_types.NIComplexNumberF32(real=val.real, imaginary=val.imag)
            for val in ${p['python_name']}.ravel()
        ]
% elif p['original_type'] == 'NIComplexI16[]':
        arr = ${p['python_name']}.ravel()
        if arr.size % 2 != 0:
            raise ValueError("Interleaved int16 array must have even length (real/imag pairs)")
        arr_pairs = arr.reshape(-1, 2)
        ${p['python_name']}_list = [
            grpc_complex_types.NIComplexI16(real=int(pair[0]), imaginary=int(pair[1]))
            for pair in arr_pairs
        ]
% endif
% endfor
        ${capture_response}self._invoke(
            self._client.${grpc_name},
            grpc_types.${grpc_name}Request(${grpc_request_args}),
        )
% if return_statement:
        ${return_statement}
% endif
% else:
        raise NotImplementedError('numpy-specific methods are not supported over gRPC')
% endif