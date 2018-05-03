<%page args="f, config, method_template"/>\
<%
    '''Renders a Session method for reading into a numpy.array corresponding to the passed-in function metadata.'''

    import build.helper as helper

    parameters = f['parameters']
    c_function_prefix = config['c_function_prefix']
    enum_input_parameters = helper.filter_parameters(f, helper.ParameterUsageOptions.INPUT_ENUM_PARAMETERS)
    suffix = method_template['method_python_name_suffix']
    lock_indent = '    ' if f['use_session_lock'] else ''
    lock_indent_num = 4 if f['use_session_lock'] else 0
%>\
    def ${f['python_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_NUMPY_INTO_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, True, config, indent=8)}
        '''
        import numpy

% if f['use_session_lock']:
        with self.lock():
% endif
% for parameter in enum_input_parameters:
        ${lock_indent}${helper.get_enum_type_check_snippet(parameter, indent=12)}
% endfor
% for parameter in helper.filter_parameters(f, helper.ParameterUsageOptions.NUMPY_PARAMETERS):
        ${lock_indent}if type(${parameter['python_name']}) is not numpy.ndarray:
        ${lock_indent}    raise TypeError('${parameter['python_name']} must be {0}, is {1}'.format(numpy.ndarray, type(${parameter['python_name']})))
        ${lock_indent}if numpy.isfortran(${parameter['python_name']}) is True:
        ${lock_indent}    raise TypeError('${parameter['python_name']} must be in C-order')
        ${lock_indent}if ${parameter['python_name']}.dtype is not numpy.dtype('${parameter['numpy_type']}'):
        ${lock_indent}    raise TypeError('${parameter['python_name']} must be numpy.ndarray of dtype=${parameter['numpy_type']}, is ' + str(${parameter['python_name']}.dtype))
<%
size_param = None
if parameter['size']['mechanism'] == 'passed-in':
    size_param = helper.find_size_parameter(parameter, f['parameters'])
%>\
% if size_param:
        ${lock_indent}${size_param['python_name']} = len(${parameter['python_name']})

% endif
% endfor
% for parameter in helper.filter_parameters(f, helper.ParameterUsageOptions.LIBRARY_METHOD_CALL):
%   for declaration in helper.get_ctype_variable_declaration_snippet(parameter, parameters, None, config, use_numpy_array=parameter['numpy']):
        ${lock_indent}${declaration}
%   endfor
% endfor
        ${lock_indent}error_code = self._library.${c_function_prefix}${f['name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.LIBRARY_METHOD_CALL)})
        ${lock_indent}errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=${f['is_error_handling']})
        ${lock_indent}${helper.get_method_return_snippet(parameters, config, use_numpy_array=True)}

