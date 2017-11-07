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
functions = helper.filter_codegen_functions(functions)
%>\


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
%>\
        self._defaults['${func_name}'] = {}
        self._defaults['${func_name}']['return'] = 0
% for p in helper.filter_parameters(f, helper.ParameterUsageOptions.OUTPUT_PARAMETERS):
        self._defaults['${func_name}']['${p['name']}'] = None
% endfor
<%
ivi_dance_param = helper.filter_ivi_dance_parameter(f)
%>\
% if ivi_dance_param is not None:
        self._defaults['${func_name}']['${ivi_dance_param['name']}'] = None
% endif
% endfor

    def __getitem__(self, func):
        return self._defaults[func]

    def __setitem__(self, func, val):
        self._defaults[func] = val

% for func_name in sorted(helper.filter_codegen_functions(functions)):
<%
f = functions[func_name]
params = f['parameters']
output_params = helper.filter_parameters(f, helper.ParameterUsageOptions.OUTPUT_PARAMETERS)
ivi_dance_param = helper.filter_ivi_dance_parameter(f)
ivi_dance_size_param = helper.find_size_parameter(ivi_dance_param, params)
%>\
    def ${c_function_prefix}${func_name}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.LIBRARY_METHOD_DECLARATION)}):  # noqa: N802
        if self._defaults['${func_name}']['return'] != 0:
            return self._defaults['${func_name}']['return']
%    for p in output_params:
        if self._defaults['${func_name}']['${p['name']}'] is None:
            raise MockFunctionCallError("${c_function_prefix}${func_name}", param='${p['name']}')
%       if p['is_buffer']:
        a = self._defaults['${func_name}']['${p['name']}']
        import sys
        if sys.version_info.major > 2 and type(a) is str:
            a = a.encode('ascii')
        for i in range(min(len(${p['python_name']}), len(a))):
            ${p['python_name']}[i] = a[i]
%       else:
%           if helper.find_custom_type(p, config) is not None:
        for field in self._defaults['${func_name}']['${p["python_name"]}']._fields_:
            field_name = field[0]
            setattr(cs.contents, field_name, getattr(self._defaults['${func_name}']['${p["python_name"]}'], field_name))
%           else:
        ${p['python_name']}.contents.value = self._defaults['${func_name}']['${p['name']}']
%           endif
%       endif
%    endfor
%    if ivi_dance_param is not None:
        if self._defaults['${func_name}']['${ivi_dance_param['name']}'] is None:
            raise MockFunctionCallError("${c_function_prefix}${func_name}", param='${ivi_dance_param['name']}')
        if ${ivi_dance_size_param['python_name']}.value == 0:
            return len(self._defaults['${func_name}']['${ivi_dance_param['name']}'])
%       if ivi_dance_param['type'] == 'ViChar':  # strings
        ${ivi_dance_param['python_name']}.value = self._defaults['${func_name}']['${ivi_dance_param['name']}'].encode('ascii')
%       else:  # arrays
        for i in range(len(self._defaults['${func_name}']['${ivi_dance_param['name']}'])):
            ${ivi_dance_param['python_name']}[i] = self._defaults['${func_name}']['${ivi_dance_param['name']}'][i]
%       endif
%    endif
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
