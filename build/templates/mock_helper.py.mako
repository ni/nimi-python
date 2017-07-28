# This file was generated
<%
import build.helper as helper

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

import ${module_name}.ctypes_types
import ${module_name}.python_types


class MockFunctionCallError(Exception):
    def __init__(self, function, param=None):
        self.function = function
        self.param = param
        msg = "{0} called without setting side_effect".format(self.function)
        if param is not None:
            msg += " or setting the {0} parameter return value".format(self.param)
        super(Exception, self).__init__(msg)


class SideEffectsHelper(object):
    def __init__(self):
        self._defaults = {}
% for func_name in helper.extract_codegen_functions(functions):
<% 
f = functions[func_name]
%>\
        self._defaults['${func_name}'] = {}
        self._defaults['${func_name}']['return'] = 0
% for param_num in helper.extract_output_parameters(f['parameters']):
<%
p = f['parameters'][param_num]
%>\
        self._defaults['${func_name}']['${p['name']}'] = None
% endfor
% endfor

    def __getitem__(self, func):
        return self._defaults[func]

    def __setitem__(self, func, val):
        self._defaults[func] = val

% for func_name in helper.extract_codegen_functions(functions):
<% 
f = functions[func_name]
params = f['parameters']
output_params = helper.extract_output_parameters(params)
%>\
    def ${c_function_prefix}${func_name}(${helper.get_method_parameters_snippet(params)}):  # noqa: N802
%    for param_num in output_params:
<%
p = output_params[param_num]
%>\
        if self._defaults['${func_name}']['${p['name']}'] is None:
            raise MockFunctionCallError("${c_function_prefix}${func_name}", param='${p['name']}')
        ${p['python_name']}.contents.value = self._defaults['${func_name}']['${p['name']}']
%    endfor
        return self._defaults['${func_name}']['return']

% endfor
    # TODO(texasaggie97) Remove hand coded functions once metadata contains enough information to code generate these
    def ${c_function_prefix}GetAttributeViString(self, vi, channel_name, attribute_id, buf_size, value):  # noqa: N802,F811
        if self._defaults['GetAttributeViString']['value'] is None:
            raise MockFunctionCallError("niDMM_GetAttributeViString", param='value')
        if buf_size == 0:
            return len(self._defaults['GetAttributeViString']['value'])
        t = ${module_name}.ctypes_types.ViString_ctype(self._defaults['GetAttributeViString']['value'].encode('ascii'))
        value.value = ctypes.cast(t, ${module_name}.ctypes_types.ViString_ctype).value
        return self._defaults['GetAttributeViString']['return']

    def ${c_function_prefix}GetError(self, vi, error_code, buffer_size, description):  # noqa: N802,F811
        if self._defaults['GetError']['errorCode'] is None:
            raise MockFunctionCallError("niDMM_GetError", param='errorCode')
        error_code.contents.value = self._defaults['GetError']['errorCode']
        if self._defaults['GetError']['description'] is None:
            raise MockFunctionCallError("niDMM_GetError", param='description')
        if buffer_size == 0:
            return len(self._defaults['GetError'][description])
        t = ${module_name}.ctypes_types.ViString_ctype(self._defaults['GetError'][description].encode('ascii'))
        description.value = ctypes.cast(t, ${module_name}.ctypes_types.ViString_ctype).value
        return self._defaults['GetError']['return']

    # Helper function to setup Mock object with default side effects and return values
    def set_side_effects_and_return_values(self, mock_library):
% for func_name in helper.extract_codegen_functions(functions):
<% 
f = functions[func_name]
%>\
        mock_library.${c_function_prefix}${func_name}.side_effect = MockFunctionCallError("${c_function_prefix}${func_name}")
        mock_library.${c_function_prefix}${func_name}.return_value = ${module_name}.python_types.${f['returns_python']}(0)
% endfor
