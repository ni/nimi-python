# This file was generated
<%
import build.helper as helper

config = template_parameters['metadata'].config
attributes = config['attributes']

module_name = config['module_name']
c_function_prefix = config['c_function_prefix']
driver_name = config['driver_name']

functions = config['functions']
functions = helper.filter_codegen_functions(functions)
%>\

import ctypes
import threading

from ${module_name}.visatype import *  # noqa: F403,H303


class Library(object):
    '''Library

    Wrapper around driver library.
    Class will setup the correct ctypes information for every function on first call.
    '''

    def __init__(self, library_name, library_type):
        self._func_lock = threading.Lock()
        # We cache the cfunc object from the ctypes.CDLL object
% for func_name in sorted(functions):
        self.${c_function_prefix}${func_name}_cfunc = None
% endfor

        if library_type == 'windll':
            self._library = ctypes.WinDLL(library_name)
        else:  # pragma: no cover
            assert library_type == 'cdll'
            self._library = ctypes.CDLL(library_name)
% for func_name in sorted(functions):
<%
    f = functions[func_name]
    c_func_name = c_function_prefix + func_name
    params = f['parameters']
    param_names_method = helper.get_params_snippet(f, helper.ParameterUsageOptions.LIBRARY_METHOD_DECLARATION)
    param_names_library = helper.get_params_snippet(f, helper.ParameterUsageOptions.CTYPES_CALL)
    param_ctypes_library = helper.get_params_snippet(f, helper.ParameterUsageOptions.CTYPES_ARGTYPES)
%>\

    def ${c_func_name}(${param_names_method}):  # noqa: N802
        with self._func_lock:
            if self.${c_func_name}_cfunc is None:
                self.${c_func_name}_cfunc = self._library.${c_func_name}
                self.${c_func_name}_cfunc.argtypes = [${param_ctypes_library}]  # noqa: F405
                self.${c_func_name}_cfunc.restype = ${f['returns']}  # noqa: F405
        return self.${c_func_name}_cfunc(${param_names_library})
% endfor
