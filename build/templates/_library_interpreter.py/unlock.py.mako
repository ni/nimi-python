<%page args="f, config, method_template"/>\
<%
    '''Renders a LibraryInterpreter unlock method.

    The Session class doesn't keep track of the callerHasLock pointer,
    so we should just pass None.
    '''

    import build.helper as helper

    param_names_method = helper.get_params_snippet(f, helper.ParameterUsageOptions.INTERPRETER_METHOD_DECLARATION)

    full_func_name = f['interpreter_name'] + method_template['method_python_name_suffix']
    c_func_name = config['c_function_prefix'] + f['name']
%>\

    def ${full_func_name}(${param_names_method}):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.${c_func_name}(vi_ctype, None)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=${f['is_error_handling']})
        return
