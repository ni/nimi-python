# This file was generated
<%
import helper

functions     = template_parameters['metadata'].functions
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
import platform

from ${module_name}.ctypes_types import *

class ${module_name}_ctypes_library:

    def __init__(self, library_name):
        # We cache the cfunc object from the ctypes.CDLL object
% for f in functions:
        self.${c_function_prefix}${f['name']}_cfunc = None
% endfor
        self._cdll = ctypes.WinDLL(library_name)


% for f in functions:
<%
    func_name = c_function_prefix + f['name']
    params = f['parameters']
    param_names = helper.get_method_parameters_snippet(params)
%>\
    def ${func_name}(${param_names}):
        if self.${func_name}_cfunc is None:
            self.${func_name}_cfunc = self._cdll.${func_name}
            self.${func_name}_cfunc.argtypes = [${helper.get_library_call_parameter_types_snippet(params)}]
            self.${func_name}_cfunc.restype = ${f['returns_ctype']}
        return self.${func_name}_cfunc(${param_names})

% endfor

