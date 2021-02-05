<%page args="f, config, method_template"/>\
<%
    '''Renders a Session method corresponding to the passed-in function metadata.'''

    import build.helper as helper

    parameters = f['parameters']
    c_function_prefix = config['c_function_prefix']
    suffix = method_template['method_python_name_suffix']

    enum_input_parameters = helper.filter_parameters(f, helper.ParameterUsageOptions.INPUT_ENUM_PARAMETERS)
    ivi_dance_parameters = helper.filter_ivi_dance_parameters(f)
    ivi_dance_size_parameter = helper.find_size_parameter(ivi_dance_parameters, parameters)
    len_parameters = helper.filter_len_parameters(f)
    len_size_parameter = helper.find_size_parameter(len_parameters, parameters)
    assert ivi_dance_size_parameter is None or len_size_parameter is None
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}) -> ${helper.get_method_return_type_hint(f['parameters'], config)}:
        r'''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
% for parameter in enum_input_parameters:
        ${helper.get_enum_type_check_snippet(parameter, indent=12)}
% endfor
% for p in helper.filter_parameters(f, helper.ParameterUsageOptions.LIBRARY_METHOD_CALL):
<% ivi_dance_step = helper.IviDanceStep.QUERY_SIZE if (p in ivi_dance_parameters or p == ivi_dance_size_parameter) else helper.IviDanceStep.NOT_APPLICABLE %>\
%   for declaration in helper.get_ctype_variable_declaration_snippet(p, parameters, ivi_dance_step, config):
        ${declaration}
%   endfor
% endfor
% if len(ivi_dance_parameters) > 0:
<% ivi_dance_step = helper.IviDanceStep.GET_DATA %>\
        error_code = self._library.${c_function_prefix}${f['name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.LIBRARY_METHOD_CALL)})
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=${f['is_error_handling']})
%   for declaration in helper.get_ctype_variable_declaration_snippet(ivi_dance_size_parameter, parameters, ivi_dance_step, config):
        ${declaration}
%   endfor
%   for param in ivi_dance_parameters:
%       for declaration in helper.get_ctype_variable_declaration_snippet(param, parameters, ivi_dance_step, config):
        ${declaration}
        %   endfor
%   endfor
% endif
        error_code = self._library.${c_function_prefix}${f['name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.LIBRARY_METHOD_CALL)})
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=${f['is_error_handling']})
        ${helper.get_method_return_snippet(parameters, config)}

