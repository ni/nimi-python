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
%>\
    def ${full_func_name}(${param_names_method}):  # noqa: N802
% if included_in_proto:
        ${capture_response}self._invoke(
            self._client.${grpc_name},
            grpc_types.${grpc_name}Request(${grpc_request_args}),
        )
% if return_statement:
        ${return_statement}
% endif
% else:
        raise NotImplementedError('${full_func_name} is not supported over gRPC')
% endif
