# This file was generated
<%
functions     = template_parameters['metadata'].functions
attributes    = template_parameters['metadata'].attributes
config        = template_parameters['metadata'].config
types         = template_parameters['types']

module_name = config['module_name']
c_function_prefix = config['c_function_prefix']
driver_name = config['driver_name']
%>

import ctypes
import platform

class ${module_name}_ctypes_library:
    # We cache the cfunc object from the ctypes.CDLL object
% for f in functions:
    ${c_function_prefix}${f['name']}_cfunc = None
% endfor

    def __init__(self, library_name):
        self._cdll = ctypes.CDLL(library_name)


% for f in functions:
<%
    func_name = c_function_prefix + f['name']
    param_types = ""
    param_names = "self"
    for p in f['parameters']:
        param_names += ", "
        if len(param_types) > 0:
            param_types += ", "
        param_names += p['name']
        if p['direction'] == 'out':
            param_types += "ctypes.POINTER(" + "ctypes." + types[p['type']] + ")"
        else:
            param_types += "ctypes." + types[p['type']]
%>\
    def ${func_name}(${param_names}):
        if self.${func_name}_cfunc is None:
            self.${func_name}_cfunc = self._cdll.${func_name}
            self.${func_name}_cfunc.argtypes = [${param_types}]
            self.${func_name}_cfunc.restype = ${types[f['returns']]}
        return self.${func_name}_cfunc(${param_names})

% endfor

