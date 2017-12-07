<%page args="f, config"/>\
<%
    '''Renders a Session method corresponding to the passed-in function metadata using numpy.array for buffers.'''

    import build.helper as helper

    parameters = f['parameters']
    c_function_prefix = config['c_function_prefix']

    enum_input_parameters = helper.filter_parameters(f, helper.ParameterUsageOptions.INPUT_ENUM_PARAMETERS)
    ivi_dance_parameter = helper.filter_ivi_dance_parameter(f)
    ivi_dance_size_parameter = helper.find_size_parameter(ivi_dance_parameter, parameters)
    len_parameter = helper.filter_len_parameter(f)
    len_size_parameter = helper.find_size_parameter(len_parameter, parameters)
    assert ivi_dance_size_parameter is None or len_size_parameter is None
%>\
    def ${f['python_name']}_numpy(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f['name'], config, indent=8)}
        '''
        import numpy

% for parameter in enum_input_parameters:
        ${helper.get_enum_type_check_snippet(parameter, indent=12)}
% endfor
% for parameter in helper.filter_parameters(f, helper.ParameterUsageOptions.NUMPY_PARAMETERS):
        ${helper.get_numpy_array_declaration_snippet(parameter, parameters)}
% endfor
% for parameter in helper.filter_parameters(f, helper.ParameterUsageOptions.LIBRARY_METHOD_CALL):
        ${helper.get_ctype_variable_declaration_snippet(parameter, parameters, None, config, use_numpy_array=parameter['numpy'])}
% endfor
        error_code = self._library.${c_function_prefix}${f['name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.LIBRARY_METHOD_CALL)})
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=${f['is_error_handling']})
        ${helper.get_method_return_snippet(parameters, config, use_numpy_array=True)}

