<%page args="f, config"/>\
<%
    '''Renders a Session method corresponding to the passed-in function metadata.'''

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
% for p in helper.filter_parameters(f, helper.ParameterUsageOptions.LIBRARY_METHOD_CALL):
        ${helper.get_ctype_variable_declaration_snippet(p, parameters, config)}
% endfor
% if ivi_dance_parameter is not None:
        error_code = self._library.${c_function_prefix}${f['name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.LIBRARY_METHOD_CALL)})
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=${f['is_error_handling']})
        ${ivi_dance_size_parameter['ctypes_variable_name']} = visatype.${ivi_dance_size_parameter['ctypes_type']}(error_code)  # TODO(marcoskirsch): use get_ctype_variable_declaration_snippet()
        ${ivi_dance_parameter['ctypes_variable_name']} = (visatype.${ivi_dance_parameter['ctypes_type']} * ${ivi_dance_size_parameter['ctypes_variable_name']}.value)()  # TODO(marcoskirsch): use get_ctype_variable_declaration_snippet()
% endif
        error_code = self._library.${c_function_prefix}${f['name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.LIBRARY_METHOD_CALL)})
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=${f['is_error_handling']})
        ${helper.get_method_return_snippet(parameters, config)}

