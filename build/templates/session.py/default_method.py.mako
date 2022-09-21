<%page args="f, config, method_template"/>\
<%
    '''Renders a Session method corresponding to the passed-in function metadata.'''

    import build.helper as helper

    suffix = method_template['method_python_name_suffix']

    enum_input_parameters = helper.filter_parameters(f, helper.ParameterUsageOptions.INPUT_ENUM_PARAMETERS)
%>\
    def ${f['python_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        r'''${f['python_name']}${suffix}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
% for parameter in enum_input_parameters:
        ${helper.get_enum_type_check_snippet(parameter, indent=12)}
% endfor
        return self._library_interpreter.${f['library_interpreter_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.LIBRARY_INTERPRETER_METHOD_CALL, config)})
