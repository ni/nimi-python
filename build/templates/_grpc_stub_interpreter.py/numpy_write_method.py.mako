<%page args="f, config, method_template"/>\
<%
    '''Renders a GrpcStubInterpreter method for numpy write operations with complex number support.'''
    
    import build.helper as helper
    
    full_func_name = f['interpreter_name'] + method_template['method_python_name_suffix']
    method_decl_params = helper.get_params_snippet(f, helper.ParameterUsageOptions.INTERPRETER_METHOD_DECLARATION)
    grpc_name = f.get('grpc_name', f['name'])
    grpc_request_args = helper.get_params_snippet(f, helper.ParameterUsageOptions.GRPC_REQUEST_PARAMETERS)
    return_statement = helper.get_grpc_interpreter_method_return_snippet(f['parameters'], config)
    if return_statement == 'return':
        return_statement = None
    capture_response = 'response = ' if return_statement else ''
    included_in_proto = f.get('included_in_proto', True)
    numpy_complex_params = helper.filter_parameters(f['parameters'], helper.ParameterUsageOptions.COMPLEX_NUMBER_PARAMETERS)
    for param in numpy_complex_params:
        grpc_request_args = grpc_request_args.replace(
            param['grpc_name'] + '=' + param['python_name'],
            param['grpc_name'] + '=' + param['python_name'] + '_list'
        )
%>\

    def ${full_func_name}(${method_decl_params}):  # noqa: N802
% if included_in_proto:
%   if numpy_complex_params:
        # Use ravel() so that gRPC always receives a flat numpy array, regardless of input dimensions.
%     for param in numpy_complex_params:
%       if param['original_type'] == 'NIComplexNumber[]':
        ${param['python_name']}_list = [
            grpc_complex_types.NIComplexNumber(real=val.real, imaginary=val.imag)
            for val in ${param['python_name']}.ravel()
        ]
%       elif param['original_type'] == 'NIComplexNumberF32[]':
        ${param['python_name']}_list = [
            grpc_complex_types.NIComplexNumberF32(real=val.real, imaginary=val.imag)
            for val in ${param['python_name']}.ravel()
        ]
%       elif param['original_type'] == 'NIComplexI16[]':
        arr = ${param['python_name']}.ravel()
        if arr.size % 2 != 0:
            raise ValueError("Interleaved int16 array must have even length (real/imag pairs)")
        arr_pairs = arr.reshape(-1, 2)
        ${param['python_name']}_list = [
            grpc_complex_types.NIComplexI16(real=int(pair[0]), imaginary=int(pair[1]))
            for pair in arr_pairs
        ]
%       endif
%     endfor
        ${capture_response}self._invoke(
            self._client.${grpc_name},
            grpc_types.${grpc_name}Request(${grpc_request_args}),
        )
%     if return_statement:
        ${return_statement}
%     endif
%   else:
        raise NotImplementedError('numpy-specific methods are not supported over gRPC')
%   endif
% else:
        raise NotImplementedError('${full_func_name} is not supported over gRPC')
% endif
