<%page args="f, config, method_template"/>\
<%
    '''Renders a GrpcStubInterpreter initialization method, adding proto-specific fields to the passed-in function metadata.'''

    import build.helper as helper

    full_func_name = f['interpreter_name'] + method_template['method_python_name_suffix']
    method_decl_params = helper.get_params_snippet(f, helper.ParameterUsageOptions.INTERPRETER_METHOD_DECLARATION)
    grpc_name = f.get('grpc_name', f['name'])
    grpc_request_args = helper.get_params_snippet(f, helper.ParameterUsageOptions.GRPC_REQUEST_PARAMETERS)
    return_statement = helper.get_grpc_interpreter_method_return_snippet(f['parameters'], config)
    if return_statement == 'return':
        return_statement = None
    capture_response = 'response = ' if return_statement else ''
%>\

    def ${full_func_name}(${method_decl_params}):  # noqa: N802
        metadata = (
            ('x-api-key', self._grpc_options.api_key),
        )
        ${capture_response}self._invoke(
            self._client.${grpc_name},
            grpc_types.${grpc_name}Request(${grpc_request_args}, session_name=self._grpc_options.session_name, initialization_behavior=self._grpc_options.initialization_behavior),
            metadata=metadata,
        )
        self._close_on_exit = response.new_session_initialized
% if return_statement:
        ${return_statement}
% endif
