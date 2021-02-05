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

import array
import ctypes
import datetime
import hightime
import threading
import typing

import ${module_name}._attributes as _attributes
import ${module_name}._converters as _converters
import ${module_name}._library_singleton as _library_singleton
import ${module_name}._visatype as _visatype
import ${module_name}.errors as errors

# Used for __repr__ and __str__
import pprint
pp = pprint.PrettyPrinter(indent=4)

_session_instance = None
_session_instance_lock = threading.Lock()


# Helper functions for creating ctypes needed for calling into the driver DLL
def get_ctypes_pointer_for_buffer(value=None, library_type=None, size=None):
    if isinstance(value, array.array):
        assert library_type is not None, 'library_type is required for array.array'
        addr, _ = value.buffer_info()
        return ctypes.cast(addr, ctypes.POINTER(library_type))
    elif str(type(value)).find("'numpy.ndarray'") != -1:
        import numpy
        return numpy.ctypeslib.as_ctypes(value)
    elif isinstance(value, list):
        assert library_type is not None, 'library_type is required for list'
        return (library_type * len(value))(*value)
    else:
        if library_type is not None and size is not None:
            return (library_type * size)()
        else:
            return None


class SessionReference(object):
    '''Properties container for NI-TClk attributes.

    Note: Constructing this class is an advanced use case and should not be needed in most circumstances.
    '''

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

% for attribute in helper.sorted_attrs(attributes):
<%
helper.add_attribute_rep_cap_tip_docstring(attributes[attribute], config)
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
        self._${config['session_handle_parameter_name']} = ${config['session_handle_parameter_name']}
        self._library = _library_singleton.get()
        self._encoding = encoding
        # We need a self._repeated_capability string for passing down to function calls on _Library class. We just need to set it to empty string.
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

    def _get_error_description(self, error_code):
        '''_get_error_description

        Returns the error description.
        '''
        try:
            '''
            It is expected for _get_error to raise when the session is invalid
            (IVI spec requires GetError to fail).
            Use _error_message instead. It doesn't require a session.
            '''
            error_string = self._get_extended_error_info()
            return error_string
        except errors.Error:
            return "Failed to retrieve error description."

    def _get_tclk_session_reference(self):
        return self._${config['session_handle_parameter_name']}

<%
# We need _get_extended_error_info() to exist in both this class as well as the _Session class, so we will
# Set then unset the 'render_in_session_base' flag to get it added to both
functions['GetExtendedErrorInfo']['render_in_session_base'] = True
%>\
% for func_name in sorted({k: v for k, v in functions.items() if v['render_in_session_base']}):
% for method_template in functions[func_name]['method_templates']:
<%include file="${'/session.py' + method_template['session_filename'] + '.py.mako'}" args="f=functions[func_name], config=config, method_template=method_template" />\
% endfor
% endfor

<%
# The main reason for having this class is to allow reusing the default method template.
%>\
class _Session(object):
    '''Private class

    This class allows reusing function templates that are used in all other drivers. If
    we don't do this, we would need new template(s) that the only difference is in the
    indentation.
    '''

    def __init__(self):
        self._library = _library_singleton.get()
        self._encoding = 'windows-1251'

        # Instantiate any repeated capability objects
% for rep_cap in config['repeated_capabilities']:
        self.${rep_cap['python_name']} = _RepeatedCapabilities(self, '${rep_cap["prefix"]}')
% endfor

        # Store the parameter list for later printing in __repr__
        param_list = []
        self._param_list = ', '.join(param_list)

        self._is_frozen = True

    def _get_error_description(self, error_code):
        '''_get_error_description

        Returns the error description.
        '''
        try:
            '''
            It is expected for _get_error to raise when the session is invalid
            (IVI spec requires GetError to fail).
            Use _error_message instead. It doesn't require a session.
            '''
            error_string = self._get_extended_error_info()
            return error_string
        except errors.Error:
            return "Failed to retrieve error description."

    ''' These are code-generated '''
<%
# We need _get_extended_error_info() to exist in both this class as well as the SessionReference class, so we will
# Set then unset the 'render_in_session_base' flag to get it added to both
functions['GetExtendedErrorInfo']['render_in_session_base'] = False
%>\
% for func_name in sorted({k: v for k, v in functions.items() if not v['render_in_session_base']}):
% for method_template in functions[func_name]['method_templates']:
<%include file="${'/session.py' + method_template['session_filename'] + '.py.mako'}" args="f=functions[func_name], config=config, method_template=method_template" />\
% endfor
% endfor

<%
# We need _get_extended_error_info() to exist in both this class as well as the _Session class, so we will
# Set then unset the 'render_in_session_base' flag to get it added to both. We do not want it in the standalone
# functions so we set it back to True here to remove it from this list
functions['GetExtendedErrorInfo']['render_in_session_base'] = True
%>\
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

