# This file was generated

# Python ctypes wrapper around driver DLL.
# ctypes is a library to manage calling into C/C++ DLLs. It will ensure the correct
#  number and types of parameters are passed into the different entry points
<%
import build.helper as helper

attributes    = template_parameters['metadata'].attributes
config        = template_parameters['metadata'].config

module_name = config['module_name']
c_function_prefix = config['c_function_prefix']
driver_name = config['driver_name']

functions = template_parameters['metadata'].functions
functions = helper.extract_codegen_functions(functions)
functions = helper.add_all_metadata(functions)
%>\

import ctypes

from ${module_name}.ctypes_types import *  # noqa: F403,H303
import ${module_name}.python_types


class ${module_name.title()}CtypesLibrary(object):
    def __init__(self, library_name, library_type):
        # We cache the cfunc object from the ctypes.CDLL object
% for f in functions:
        self.${c_function_prefix}${f['name']}_cfunc = None
% endfor

        if library_type == 'windll':
            self._library = ctypes.WinDLL(library_name)
        else:
            assert library_type == 'cdll'
            self._library = ctypes.CDLL(library_name)
% for f in functions:
<%
    func_name = c_function_prefix + f['name']
    params = f['parameters']
    param_names_method = helper.get_method_parameters_snippet(params)
    param_names_function = helper.get_function_parameters_snippet(params)
%>\

    def ${func_name}(${param_names_method}):  # noqa: N802
        if self.${func_name}_cfunc is None:
            self.${func_name}_cfunc = self._library.${func_name}
            self.${func_name}_cfunc.argtypes = [${helper.get_library_call_parameter_types_snippet(params)}]  # noqa: F405
            self.${func_name}_cfunc.restype = ${module_name}.python_types.${f['returns_python']}
        return self.${func_name}_cfunc(${param_names_function})
% endfor
