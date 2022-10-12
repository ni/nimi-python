<%page args="f, config, method_template"/>\
<%
    '''Renders a grpc LibraryInterpreter method corresponding to the passed-in function metadata.'''

    import build.helper as helper

    full_func_name = f['library_interpreter_name'] + method_template['method_python_name_suffix']
    method_decl_params = helper.get_params_snippet(f, helper.ParameterUsageOptions.LIBRARY_INTERPRETER_METHOD_DECLARATION)
%>\

    def ${full_func_name}(${method_decl_params}):  # noqa: N802
        raise NotImplementedError('Cannot use numpy over grpc')
