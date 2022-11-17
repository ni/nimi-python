<%page args="f, config, method_template"/>\
<%
    '''Renders a GrpcStubInterpreter method corresponding to the passed-in function metadata.'''
    import build.helper as helper
    parameters = f['parameters']
    full_func_name = f['interpreter_name'] + method_template['method_python_name_suffix']
    method_decl_params = helper.get_params_snippet(f, helper.ParameterUsageOptions.INTERPRETER_METHOD_DECLARATION)
    grpc_name = f.get('grpc_name', f['name'])
    grpc_request_args = helper.get_params_snippet(f, helper.ParameterUsageOptions.GRPC_REQUEST_PARAMETERS)
    return_statement = helper.get_grpc_interpreter_method_return_snippet(f['parameters'], config)
    if return_statement == 'return':
        return_statement = None
    capture_response = 'response = ' if return_statement else ''
    included_in_proto = f.get('included_in_proto', True)
%>\

    def ${full_func_name}(${method_decl_params}):  # noqa: N802
% if included_in_proto:
% for p in parameters:
%   for check_snippet in helper.get_grpc_args_check_snippets(p, parameters):
        ${check_snippet}
%   endfor
% endfor
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
