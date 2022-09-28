# This file was generated
<%
    import build.helper as helper

    config            = template_parameters['metadata'].config
    attributes        = helper.filter_codegen_attributes(config['attributes'])
    functions         = config['functions']

    module_name       = config['module_name']
    c_function_prefix = config['c_function_prefix']

    functions = helper.filter_codegen_functions(functions)
%>\

import hightime

import ${module_name}._attributes as _attributes
import ${module_name}._converters as _converters
import ${module_name}._library_interpreter as _library_interpreter

# Used for __repr__ and __str__
import pprint
pp = pprint.PrettyPrinter(indent=4)


class SessionReference(object):
    '''Properties container for NI-TClk attributes.

    Note: Constructing this class is an advanced use case and should not be needed in most circumstances.
    '''

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

% for attribute in helper.sorted_attrs(attributes):
<%
helper.add_attribute_rep_cap_tip(attributes[attribute], config)
%>\
    %if attributes[attribute]['enum']:
    ${attributes[attribute]['python_name']} = _attributes.AttributeEnum(_attributes.Attribute${attributes[attribute]['type']}, enums.${enums[attributes[attribute]['enum']]['python_name']}, ${attribute})
    %else:
    ${attributes[attribute]['python_name']} = _attributes.${attributes[attribute]['attribute_class']}(${attribute})
    %endif
%   if 'documentation' in attributes[attribute] and len(helper.get_documentation_for_node_docstring(attributes[attribute], config, indent=4).strip()) > 0:
    '''Type: ${attributes[attribute]['type_in_documentation']}

    ${helper.get_documentation_for_node_docstring(attributes[attribute], config, indent=4)}
    '''
%   endif
% endfor

    def __init__(self, ${config['session_handle_parameter_name']}, encoding='windows-1251'):
        self._library_interpreter = _library_interpreter.LibraryInterpreter(encoding)
        self._library_interpreter._${config['session_handle_parameter_name']} = ${config['session_handle_parameter_name']}
        # We need a self._repeated_capability string for passing down to function calls on the LibraryInterpreter class. We just need to set it to empty string.
        self._repeated_capability = ''

        # Store the parameter list for later printing in __repr__
        param_list = []
        param_list.append("${config['session_handle_parameter_name']}=" + pp.pformat(${config['session_handle_parameter_name']}))
        param_list.append("encoding=" + pp.pformat(encoding))
        self._param_list = ', '.join(param_list)

        self._is_frozen = True

    def __repr__(self):
        return '{0}.{1}({2})'.format('${module_name}', self.__class__.__name__, self._param_list)

    def __setattr__(self, key, value):
        if self._is_frozen and key not in dir(self):
            raise AttributeError("'{0}' object has no attribute '{1}'".format(type(self).__name__, key))
        object.__setattr__(self, key, value)

    def _get_tclk_session_reference(self):
        return self._library_interpreter._${config['session_handle_parameter_name']}
% for func_name in sorted({k: v for k, v in functions.items() if v['render_in_session_base']}):
% for method_template in functions[func_name]['method_templates']:
% if method_template['session_filename'] != '/none':

<%include file="${'/session.py' + method_template['session_filename'] + '.py.mako'}" args="f=functions[func_name], config=config, method_template=method_template" />\
% endif
% endfor
% endfor


## The main reason for having this class is to allow reusing the default method template.
class _Session(object):
    '''Private class

    This class allows reusing function templates that are used in all other drivers. If
    we don't do this, we would need new template(s) that the only difference is in the
    indentation.
    '''

    def __init__(self):
        self._library_interpreter = _library_interpreter.LibraryInterpreter('windows-1251')

        # Instantiate any repeated capability objects
% for rep_cap in config['repeated_capabilities']:
        self.${rep_cap['python_name']} = _RepeatedCapabilities(self, '${rep_cap["prefix"]}')
% endfor

        # Store the parameter list for later printing in __repr__
        param_list = []
        self._param_list = ', '.join(param_list)

        self._is_frozen = True

    ''' These are code-generated '''
% for func_name in sorted({k: v for k, v in functions.items() if not v['render_in_session_base']}):
% for method_template in functions[func_name]['method_templates']:
% if method_template['session_filename'] != '/none':

<%include file="${'/session.py' + method_template['session_filename'] + '.py.mako'}" args="f=functions[func_name], config=config, method_template=method_template" />\
% endif
% endfor
% endfor
% for func_name in sorted({k: v for k, v in functions.items() if not v['render_in_session_base']}):


<%
f = functions[func_name]
name = f['python_name']
parameter_list = helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_PASSTHROUGH_CALL)
%>\
def ${name}(${parameter_list}):
    '''${name}

    ${helper.get_function_docstring(f, False, config, indent=4)}
    '''
    return _Session().${name}(${parameter_list})
% endfor
