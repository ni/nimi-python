<%page args="f, config, method_template"/>\
<%
    '''Renders a NotImplemented method for to the passed-in function metadata, because numpy is not supported over grpc.'''

    import build.helper as helper

    full_func_name = f['interpreter_name'] + method_template['method_python_name_suffix']
    method_decl_params = helper.get_params_snippet(f, helper.ParameterUsageOptions.INTERPRETER_METHOD_DECLARATION)
%>\

    def ${full_func_name}(${method_decl_params}):  # noqa: N802
        raise NotImplementedError('numpy-specific methods are not supported over gRPC')
