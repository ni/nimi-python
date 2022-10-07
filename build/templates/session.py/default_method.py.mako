<%page args="f, config, method_template"/>\
<%
    '''Renders a Session method corresponding to the passed-in function metadata.'''

    import build.helper as helper

    suffix = method_template['method_python_name_suffix']

    enum_input_parameters = helper.filter_parameters(f, helper.ParameterUsageOptions.INPUT_ENUM_PARAMETERS)
    # TODO(marcoskirsch): Retrofit to call filter_parameters(function, parameter_usage_options)
    output_parameters = [p for p in f['parameters'] if p['direction'] == 'out' and p['use_in_python_api']]
    output_parameters_snippet = ', '.join(p['python_name'] for p in output_parameters)
%>\
    def ${f['python_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        r'''${f['python_name']}${suffix}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
% for parameter in enum_input_parameters:
        ${helper.get_enum_type_check_snippet(parameter, indent=12)}
% endfor
% for p in helper.filter_parameters(f, helper.ParameterUsageOptions.LIBRARY_INTERPRETER_METHOD_CALL):
%   if 'python_api_converter_name' in p:
        ${p['python_name']} = _converters.${p['python_api_converter_name']}(${p['python_name']})
%   endif
% endfor
% if output_parameters:
        ${output_parameters_snippet} = self._library_interpreter.${f['library_interpreter_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.LIBRARY_INTERPRETER_METHOD_CALL)})
        ${helper.get_session_method_return_snippet(f['parameters'], config)}
% else:
        self._library_interpreter.${f['library_interpreter_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.LIBRARY_INTERPRETER_METHOD_CALL)})
% endif
