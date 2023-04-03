<%page args="f, config, method_template"/>\
<%
    '''Renders a Session method corresponding to the passed-in function metadata.'''

    import build.helper as helper

    suffix = method_template['method_python_name_suffix']

    parameters = f['parameters']
    enum_input_parameters = helper.filter_parameters(parameters, helper.ParameterUsageOptions.INPUT_ENUM_PARAMETERS)
    output_parameters = helper.filter_parameters(parameters, helper.ParameterUsageOptions.API_OUTPUT_PARAMETERS)
    output_parameters_snippet = ', '.join(p['python_name'] for p in output_parameters)
%>\
    def ${f['python_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        r'''${f['python_name']}${suffix}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
% for parameter in enum_input_parameters:
        ${helper.get_enum_type_check_snippet(parameter, indent=12)}
% endfor
% for size_check_snippet in helper.get_parameter_size_check_snippets(parameters):
        ${size_check_snippet}
% endfor
% for p in helper.filter_parameters(parameters, helper.ParameterUsageOptions.INTERPRETER_METHOD_CALL):
%   if 'python_api_converter_name' in p:
        ${p['python_name']} = _converters.${p['python_api_converter_name']}(${p['python_name']})
%   endif
% endfor
% if output_parameters:
        ${output_parameters_snippet} = self._interpreter.${f['interpreter_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.INTERPRETER_METHOD_CALL)})
        ${helper.get_session_method_return_snippet(parameters, config)}
% else:
        self._interpreter.${f['interpreter_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.INTERPRETER_METHOD_CALL)})
% endif
