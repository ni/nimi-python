<%page args="f, config, method_template"/>\
<%
    '''Renders a Intermediate method corresponding to the passed-in function metadata.'''

    import build.helper as helper

    parameters = f['parameters']
    param_names_method = helper.get_params_snippet(f, helper.ParameterUsageOptions.LIBRARY_METHOD_DECLARATION)
    param_names_library = helper.get_params_snippet(f, helper.ParameterUsageOptions.CTYPES_CALL)

    ivi_dance_parameters = helper.filter_ivi_dance_parameters(f)
    ivi_dance_size_parameter = helper.find_size_parameter(ivi_dance_parameters, parameters)
    len_parameters = helper.filter_len_parameters(f)
    len_size_parameter = helper.find_size_parameter(len_parameters, parameters)
    assert ivi_dance_size_parameter is None or len_size_parameter is None, str(f)

    full_func_name = f['python_name'] + method_template['method_python_name_suffix']

    # If a method uses codegen_method=python-only, it should specify non-default method_templates
    assert f['codegen_method'] != 'python-only', full_func_name + ' uses default_method method_template, but is python-only!'
%>\

    def ${full_func_name}(${param_names_method}):  # noqa: N802
% for p in helper.filter_parameters(f, helper.ParameterUsageOptions.CTYPES_CALL):
<% ivi_dance_step = helper.IviDanceStep.QUERY_SIZE if (p in ivi_dance_parameters or p == ivi_dance_size_parameter) else helper.IviDanceStep.NOT_APPLICABLE %>\
%   for declaration in helper.get_ctype_variable_declaration_snippet(p, parameters, ivi_dance_step, config):
        ${declaration}
%   endfor
% endfor
% if len(ivi_dance_parameters) > 0:
<% ivi_dance_step = helper.IviDanceStep.GET_DATA %>\
        error_code = self._library.${f['python_name']}(${param_names_library})
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=${f['is_error_handling']})
%   for declaration in helper.get_ctype_variable_declaration_snippet(ivi_dance_size_parameter, parameters, ivi_dance_step, config):
        ${declaration}
%   endfor
%   for param in ivi_dance_parameters:
%       for declaration in helper.get_ctype_variable_declaration_snippet(param, parameters, ivi_dance_step, config):
        ${declaration}
%       endfor
%   endfor
% endif
        error_code = self._library.${f['python_name']}(${param_names_library})
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=${f['is_error_handling']})
        ${helper.get_method_return_snippet(parameters, config)}
