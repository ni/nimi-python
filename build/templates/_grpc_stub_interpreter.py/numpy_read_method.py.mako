<%page args="f, config, method_template"/>\
<%
    '''Renders a GrpcStubInterpreter method for numpy write operations with complex number support.'''
    import build.helper as helper
    parameters = f['parameters']
    full_func_name = f['interpreter_name'] + method_template['method_python_name_suffix']
    method_decl_params = helper.get_params_snippet(f, helper.ParameterUsageOptions.INTERPRETER_METHOD_DECLARATION)
    included_in_proto = f.get('included_in_proto', True)
    
    # Identify numpy parameters with complex number types.
    numpy_complex_params = helper.filter_parameters(parameters, helper.ParameterUsageOptions.COMPLEX_NUMBER_PARAMETERS)
    
    # Only generate gRPC implementation if the function has complex parameters and is included in proto
    should_generate_complex_grpc_impl = bool(numpy_complex_params) and included_in_proto
    
    if should_generate_complex_grpc_impl:
        grpc_method_name = f.get('grpc_name', f['name'])
        grpc_request_args_snippet = helper.get_grpc_complex_request_args_snippet(f, numpy_complex_params)
        return_snippet, response_assignment_prefix = helper.get_grpc_response_info(f, config)
%>\

    def ${full_func_name}(${method_decl_params}):  # noqa: N802
% if should_generate_complex_grpc_impl:
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
        ${response_assignment_prefix}self._invoke(
            self._client.${grpc_method_name},
            grpc_types.${grpc_method_name}Request(${grpc_request_args_snippet}),
        )
% if return_snippet:
        ${return_snippet}
% endif
% else:
        raise NotImplementedError('numpy-specific methods are not supported over gRPC')
% endif
