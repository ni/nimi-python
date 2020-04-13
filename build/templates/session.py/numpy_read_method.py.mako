<%page args="f, config, method_template"/>\
<%
    '''Renders a Session method for reading into a numpy.array corresponding to the passed-in function metadata.'''

    import build.helper as helper

    parameters = f['parameters']
    c_function_prefix = config['c_function_prefix']
    enum_input_parameters = helper.filter_parameters(f, helper.ParameterUsageOptions.INPUT_ENUM_PARAMETERS)
    suffix = method_template['method_python_name_suffix']
%>\
    def ${f['python_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_NUMPY_INTO_METHOD_DECLARATION)}):
        r'''${f['python_name']}

        ${helper.get_function_docstring(f, True, config, indent=8)}
        '''
        import numpy

% for parameter in enum_input_parameters:
        ${helper.get_enum_type_check_snippet(parameter, indent=12)}
% endfor
% for parameter in helper.filter_parameters(f, helper.ParameterUsageOptions.NUMPY_PARAMETERS):
        if type(${parameter['python_name']}) is not numpy.ndarray:
            raise TypeError('${parameter['python_name']} must be {0}, is {1}'.format(numpy.ndarray, type(${parameter['python_name']})))
        if numpy.isfortran(${parameter['python_name']}) is True:
            raise TypeError('${parameter['python_name']} must be in C-order')
        if ${parameter['python_name']}.dtype is not numpy.dtype('${parameter['numpy_type']}'):
            raise TypeError('${parameter['python_name']} must be numpy.ndarray of dtype=${parameter['numpy_type']}, is ' + str(${parameter['python_name']}.dtype))
<%
size_param = None
if parameter['size']['mechanism'] == 'passed-in':
    size_param = helper.find_size_parameter(parameter, f['parameters'])
%>\
% if size_param:
        ${size_param['python_name']} = len(${parameter['python_name']})

% endif
% endfor
% for parameter in helper.filter_parameters(f, helper.ParameterUsageOptions.LIBRARY_METHOD_CALL):
%   for declaration in helper.get_ctype_variable_declaration_snippet(parameter, parameters, None, f['python_name'], config, use_numpy_array=parameter['numpy']):
        ${declaration}
%   endfor
% endfor
        error_code = self._library.${c_function_prefix}${f['name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.LIBRARY_METHOD_CALL)})
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=${f['is_error_handling']})
        ${helper.get_method_return_snippet(parameters, config, use_numpy_array=True)}

