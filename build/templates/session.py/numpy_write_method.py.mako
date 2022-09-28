<%page args="f, config, method_template"/>\
<%
    '''Renders a Session method for writing numpy.array corresponding to the passed-in function metadata.'''

    import build.helper as helper

    enum_input_parameters = helper.filter_parameters(f['parameters'], helper.ParameterUsageOptions.INPUT_ENUM_PARAMETERS)
    # TODO(marcoskirsch): Retrofit to call filter_parameters(function, parameter_usage_options)
    output_parameters = [p for p in f['parameters'] if p['direction'] == 'out' and p['use_in_python_api'] and not p['numpy']]
    output_parameters_snippet = ', '.join(p['python_name'] for p in output_parameters)
    suffix = method_template['method_python_name_suffix']
%>\
    def ${f['python_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        r'''${f['python_name']}${suffix}

        ${helper.get_function_docstring(f, True, config, indent=8)}
        '''
        import numpy

% for parameter in enum_input_parameters:
        ${helper.get_enum_type_check_snippet(parameter, indent=12)}
% endfor
% for parameter in helper.filter_parameters(f['parameters'], helper.ParameterUsageOptions.NUMPY_PARAMETERS):
        if type(${parameter['python_name']}) is not numpy.ndarray:
            raise TypeError('${parameter['python_name']} must be {0}, is {1}'.format(numpy.ndarray, type(${parameter['python_name']})))
        if numpy.isfortran(${parameter['python_name']}) is True:
            raise TypeError('${parameter['python_name']} must be in C-order')
        if ${parameter['python_name']}.dtype is not numpy.dtype('${parameter['numpy_type']}'):
            raise TypeError('${parameter['python_name']} must be numpy.ndarray of dtype=${parameter['numpy_type']}, is ' + str(${parameter['python_name']}.dtype))
% endfor
% for p in helper.filter_parameters(f['parameters'], helper.ParameterUsageOptions.LIBRARY_INTERPRETER_METHOD_CALL):
%   if 'python_api_converter_name' in p:
        ${p['python_name']} = _converters.${p['python_api_converter_name']}(${p['python_name']})
%   endif
% endfor
% if output_parameters:
        ${output_parameters_snippet} = self._library_interpreter.${f['library_interpreter_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.LIBRARY_INTERPRETER_METHOD_CALL)})
        ${helper.get_session_method_return_snippet(f['parameters'], config, use_numpy_array=True)}
% else:
        self._library_interpreter.${f['library_interpreter_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.LIBRARY_INTERPRETER_METHOD_CALL)})
% endif
