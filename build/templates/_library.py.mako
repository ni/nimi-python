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
are_complex_parameters_used = helper.are_complex_parameters_used(functions)
%>\

import ctypes
import ${module_name}.errors as errors
import threading

% if are_complex_parameters_used:
from ${module_name}._complextype import *  # noqa: F403
% endif
from ${module_name}._visatype import *  # noqa: F403,H303
% for c in config['custom_types']:

import ${module_name}.${c['file_name']} as ${c['file_name']}  # noqa: F401
% endfor


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
% for func_name in sorted(functions):
<%
    f = functions[func_name]
    c_func_name = c_function_prefix + func_name
    param_names_method = helper.get_params_snippet(f, helper.ParameterUsageOptions.LIBRARY_METHOD_DECLARATION)
    param_names_library = helper.get_params_snippet(f, helper.ParameterUsageOptions.CDLL_METHOD_CALL)
    param_ctypes_library = helper.get_params_snippet(f, helper.ParameterUsageOptions.CTYPES_ARGTYPES)
%>\

    def ${c_func_name}(${param_names_method}):  # noqa: N802
        with self._func_lock:
            if self.${c_func_name}_cfunc is None:
                self.${c_func_name}_cfunc = self._get_library_function('${c_func_name}')
                self.${c_func_name}_cfunc.argtypes = [${param_ctypes_library}]  # noqa: F405
                self.${c_func_name}_cfunc.restype = ${f['returns']}  # noqa: F405
        return self.${c_func_name}_cfunc(${param_names_library})
% endfor
