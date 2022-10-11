${template_parameters['encoding_tag']}
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
functions = helper.filter_library_functions(functions)
%>\
import sys  # noqa: F401   - Not all mock_helpers will need this


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
% for func_name in sorted(helper.filter_codegen_functions(functions)):
<%
f = functions[func_name]
params = f['parameters']
ivi_dance_params = helper.filter_ivi_dance_parameters(params)
%>\
        self._defaults['${func_name}'] = {}
        self._defaults['${func_name}']['return'] = 0
%   for p in helper.filter_parameters(params, helper.ParameterUsageOptions.LIBRARY_OUTPUT_PARAMETERS):
%     if p not in ivi_dance_params:
        self._defaults['${func_name}']['${p['name']}'] = None
%     endif
%   endfor
%   for param in ivi_dance_params:
        self._defaults['${func_name}']['${param['name']}'] = None
%   endfor
% endfor

    def __getitem__(self, func):
        return self._defaults[func]

    def __setitem__(self, func, val):
        self._defaults[func] = val

% for func_name in sorted(helper.filter_codegen_functions(functions)):
<%
f = functions[func_name]
params = f['parameters']
output_params = helper.filter_parameters(params, helper.ParameterUsageOptions.LIBRARY_OUTPUT_PARAMETERS)
ivi_dance_params = helper.filter_ivi_dance_parameters(params)
ivi_dance_size_param = helper.find_size_parameter(ivi_dance_params, params)
output_params_minus_ivi_dance_params = [p for p in output_params if p not in ivi_dance_params]
%>\
    def ${c_function_prefix}${func_name}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.LIBRARY_METHOD_DECLARATION)}):  # noqa: N802
        if self._defaults['${func_name}']['return'] != 0:
            return self._defaults['${func_name}']['return']
%    for p in output_params_minus_ivi_dance_params:
        # ${p['python_name']}
        if self._defaults['${func_name}']['${p['name']}'] is None:
            raise MockFunctionCallError("${c_function_prefix}${func_name}", param='${p['name']}')
%       if p['is_buffer']:
        test_value = self._defaults['${func_name}']['${p['name']}']
<% param_name = p['python_name'] %>\
        try:
            ${param_name}_ref = ${param_name}.contents
        except AttributeError:
            ${param_name}_ref = ${param_name}
        assert len(${param_name}_ref) >= len(test_value)
        for i in range(len(test_value)):
            ${param_name}_ref[i] = test_value[i]
%       else:
%           if helper.find_custom_type(p, config) is not None:
        for field in self._defaults['${func_name}']['${p["python_name"]}']._fields_:
            field_name = field[0]
            setattr(${p["python_name"]}.contents, field_name, getattr(self._defaults['${func_name}']['${p["python_name"]}'], field_name))
%           elif p['is_string']:
        test_value = self._defaults['${func_name}']['${p['name']}']
        if type(test_value) is str:
            test_value = test_value.encode('ascii')
<%
param_name = p['python_name']
if p['use_array']:
    param_name += '.contents'
%>\
        assert len(${param_name}) >= len(test_value)
        for i in range(len(test_value)):
            ${param_name}[i] = test_value[i]
%           else:
        if ${p['python_name']} is not None:
            ${p['python_name']}.contents.value = self._defaults['${func_name}']['${p['name']}']
%           endif
%       endif
%    endfor
%    for id_param in ivi_dance_params:
        # ${id_param['python_name']}
        if self._defaults['${func_name}']['${id_param['name']}'] is None:
            raise MockFunctionCallError("${c_function_prefix}${func_name}", param='${id_param['name']}')
        if ${ivi_dance_size_param['python_name']}.value == 0:
            return len(self._defaults['${func_name}']['${id_param['name']}'])
%       if id_param['is_string']:  # strings
        ${id_param['python_name']}.value = self._defaults['${func_name}']['${id_param['name']}'].encode('ascii')
%       else:  # arrays
<% param_name = id_param['python_name'] %>\
        try:
            ${param_name}_ref = ${param_name}.contents
        except AttributeError:
            ${param_name}_ref = ${param_name}
        for i in range(len(self._defaults['${func_name}']['${id_param["name"]}'])):
            ${param_name}_ref[i] = self._defaults['${func_name}']['${id_param["name"]}'][i]
%       endif
%    endfor
        return self._defaults['${func_name}']['return']

% endfor
    # Helper function to setup Mock object with default side effects and return values
    def set_side_effects_and_return_values(self, mock_library):
% for func_name in sorted(helper.filter_codegen_functions(functions)):
<%
f = functions[func_name]
%>\
        mock_library.${c_function_prefix}${func_name}.side_effect = MockFunctionCallError("${c_function_prefix}${func_name}")
        mock_library.${c_function_prefix}${func_name}.return_value = 0
% endfor
