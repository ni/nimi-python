${template_parameters['encoding_tag']}
# This file was generated
<%
import build.helper as helper

config = template_parameters['metadata'].config
attributes = config['attributes']

module_name = config['module_name']
c_function_prefix = config['c_function_prefix']
driver_name = config['driver_name']

functions = config['functions']
functions = helper.filter_library_functions(functions)
%>\

import array  # noqa: F401
import ctypes
import ${module_name}._converters as _converters
import ${module_name}._visatype as _visatype
% if config['enums']:
import ${module_name}.enums as enums
% endif
import ${module_name}.errors as errors
import threading

from ${module_name}._visatype import *  # noqa: F403,H303
% for c in config['custom_types']:

import ${module_name}.${c['file_name']} as ${c['file_name']}  # noqa: F401
% endfor


# Helper functions for creating ctypes needed for calling into the driver DLL
def get_ctypes_pointer_for_buffer(value=None, library_type=None, size=None):
    if isinstance(value, array.array):
        assert library_type is not None, 'library_type is required for array.array'
        addr, _ = value.buffer_info()
        return ctypes.cast(addr, ctypes.POINTER(library_type))
    elif str(type(value)).find("'numpy.ndarray'") != -1:
        import numpy
        return numpy.ctypeslib.as_ctypes(value)
    elif isinstance(value, bytes):
        return ctypes.cast(value, ctypes.POINTER(library_type))
    elif isinstance(value, list):
        assert library_type is not None, 'library_type is required for list'
        return (library_type * len(value))(*value)
    else:
        if library_type is not None and size is not None:
            return (library_type * size)()
        else:
            return None


def get_ctypes_and_array(value, array_type):
    if value is not None:
        if isinstance(value, array.array):
            value_array = value
        else:
            value_array = array.array(array_type, value)
    else:
        value_array = None

    return value_array


class Library(object):
    '''Library

    Wrapper around driver library.
    Class will setup the correct ctypes information for every function on first call.
    '''

    def __init__(self, ctypes_library):
        self._func_lock = threading.Lock()
        self._library = ctypes_library
        # We cache the cfunc object from the ctypes.CDLL object
% for func_name in sorted(functions):
        self.${c_function_prefix}${func_name}_cfunc = None
% endfor

    def _get_library_function(self, name):
        try:
            function = getattr(self._library, name)
        except AttributeError as e:
            raise errors.DriverTooOldError() from e
        return function

<%include file="/_get_error_description.py.mako" />\
% for func_name in sorted(functions):
<%
    f = functions[func_name]
    c_func_name = c_function_prefix + func_name
    parameters = f['parameters']
    param_names_method = helper.get_params_snippet(f, helper.ParameterUsageOptions.LIBRARY_METHOD_DECLARATION)
    param_names_library = helper.get_params_snippet(f, helper.ParameterUsageOptions.CTYPES_CALL)
    param_ctypes_library = helper.get_params_snippet(f, helper.ParameterUsageOptions.CTYPES_ARGTYPES)

    ivi_dance_parameters = helper.filter_ivi_dance_parameters(f)
    ivi_dance_size_parameter = helper.find_size_parameter(ivi_dance_parameters, parameters)
    len_parameters = helper.filter_len_parameters(f)
    len_size_parameter = helper.find_size_parameter(len_parameters, parameters)
    assert ivi_dance_size_parameter is None or len_size_parameter is None, str(f)
%>\
% for method_template in f['method_templates']:
<%
    full_func_name = f['python_name'] + method_template['method_python_name_suffix']
    use_numpy = 'numpy' in method_template['session_filename']
    use_numpy_read = 'numpy_read' in method_template['session_filename']
    if use_numpy_read:
        param_names_method = helper.get_params_snippet(f, helper.ParameterUsageOptions.LIBRARY_NUMPY_INTO_METHOD_DECLARATION)
%>\

    def ${full_func_name}(${param_names_method}):  # noqa: N802
% if use_numpy_read:
%   for p in helper.filter_parameters(f, helper.ParameterUsageOptions.NUMPY_PARAMETERS):
<% size_param = helper.find_size_parameter(p, f['parameters']) if p['size']['mechanism'] == 'passed-in' else None %>\
%     if size_param:
        ${size_param['python_name']} = len(${p['python_name']})
%     endif
%   endfor
% endif
% for p in helper.filter_parameters(f, helper.ParameterUsageOptions.CTYPES_CALL):
<% ivi_dance_step = helper.IviDanceStep.QUERY_SIZE if (p in ivi_dance_parameters or p == ivi_dance_size_parameter) else helper.IviDanceStep.NOT_APPLICABLE %>\
%   for declaration in helper.get_ctype_variable_declaration_snippet(p, parameters, ivi_dance_step, config, use_numpy_array=use_numpy and p['numpy']):
        ${declaration}
%   endfor
% endfor
        with self._func_lock:
            if self.${c_func_name}_cfunc is None:
                self.${c_func_name}_cfunc = self._get_library_function('${c_func_name}')
                self.${c_func_name}_cfunc.argtypes = [${param_ctypes_library}]  # noqa: F405
                self.${c_func_name}_cfunc.restype = ${f['returns']}  # noqa: F405
% if len(ivi_dance_parameters) > 0:
<% ivi_dance_step = helper.IviDanceStep.GET_DATA %>\
        error_code = self.${c_func_name}_cfunc(${param_names_library})
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=${f['is_error_handling']})
%   for declaration in helper.get_ctype_variable_declaration_snippet(ivi_dance_size_parameter, parameters, ivi_dance_step, config):
        ${declaration}
%   endfor
%   for param in ivi_dance_parameters:
%       for declaration in helper.get_ctype_variable_declaration_snippet(param, parameters, ivi_dance_step, config):
        ${declaration}
%       endfor
%   endfor
% endif
        error_code = self.${c_func_name}_cfunc(${param_names_library})
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=${f['is_error_handling']})
        ${helper.get_method_return_snippet(parameters, config, use_numpy_array=use_numpy)}
% endfor
% endfor
