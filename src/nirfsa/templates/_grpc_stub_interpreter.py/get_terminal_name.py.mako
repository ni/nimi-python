<%page args="f, config, method_template"/>\
<%
    '''Renders GetTerminalName with buffer_size=2048 so the server returns the full string.
    Without a non-zero buffer_size the server performs a size-query and returns an empty string.'''
    import build.helper as helper

    full_func_name = f['interpreter_name'] + method_template['method_python_name_suffix']
    method_decl_params = helper.get_params_snippet(f, helper.ParameterUsageOptions.INTERPRETER_METHOD_DECLARATION)
    grpc_name = f.get('grpc_name', f['name'])
%>\

    def ${full_func_name}(${method_decl_params}):  # noqa: N802
        response = self._invoke(
            self._client.${grpc_name},
            grpc_types.${grpc_name}Request(vi=self._vi, signal_raw=signal.value, signal_identifier=signal_identifier, buffer_size=2048),
        )
        return response.terminal_name
