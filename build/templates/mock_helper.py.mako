# This file was generated
<%
import build.helper as helper

config        = template_parameters['metadata'].config
attributes    = config['attributes']
functions     = config['functions']

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
% for func_name in sorted(helper.extract_codegen_functions(functions)):
<% 
f = functions[func_name]
%>\
        self._defaults['${func_name}'] = {}
        self._defaults['${func_name}']['return'] = 0
% for p in helper.extract_output_parameters(f['parameters']):
        self._defaults['${func_name}']['${p['name']}'] = None
% endfor
<%
ivi_dance_param = helper.extract_ivi_dance_parameter(f['parameters'])
%>\
% if ivi_dance_param is not None:
        self._defaults['${func_name}']['${ivi_dance_param['name']}'] = None
% endif
% endfor

    def __getitem__(self, func):
        return self._defaults[func]

    def __setitem__(self, func, val):
        self._defaults[func] = val

% for func_name in sorted(helper.extract_codegen_functions(functions)):
<% 
f = functions[func_name]
params = f['parameters']
output_params = helper.extract_output_parameters(params)
ivi_dance_param = helper.extract_ivi_dance_parameter(f['parameters'])
%>\
    def ${c_function_prefix}${func_name}(${helper.get_method_parameters_snippet(params)}):  # noqa: N802
%    for p in output_params:
        if self._defaults['${func_name}']['${p['name']}'] is None:
            raise MockFunctionCallError("${c_function_prefix}${func_name}", param='${p['name']}')
        ${p['python_name']}.contents.value = self._defaults['${func_name}']['${p['name']}']
%    endfor
%    if ivi_dance_param is not None:
        if self._defaults['${func_name}']['${ivi_dance_param['name']}'] is None:
            raise MockFunctionCallError("${c_function_prefix}${func_name}", param='${ivi_dance_param['name']}')
        if ${ivi_dance_param['size']} == 0:
            return len(self._defaults['${func_name}']['${ivi_dance_param['name']}'])
        t = ${module_name}.ctypes_types.${ivi_dance_param['ctypes_type']}(self._defaults['${func_name}']['${ivi_dance_param['name']}'].encode('ascii'))
        ${ivi_dance_param['python_name']}.value = ctypes.cast(t, ${module_name}.ctypes_types.${ivi_dance_param['ctypes_type']}).value
%    endif
        return self._defaults['${func_name}']['return']

% endfor
    # Helper function to setup Mock object with default side effects and return values
    def set_side_effects_and_return_values(self, mock_library):
% for func_name in sorted(helper.extract_codegen_functions(functions)):
<% 
f = functions[func_name]
%>\
        mock_library.${c_function_prefix}${func_name}.side_effect = MockFunctionCallError("${c_function_prefix}${func_name}")
        mock_library.${c_function_prefix}${func_name}.return_value = ${module_name}.python_types.${f['returns_python']}(0)
% endfor
