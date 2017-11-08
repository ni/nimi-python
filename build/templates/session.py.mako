<%
# Have to put this in a variable and add it that way because mako keeps thinking it is for it, not for the output file
encoding_tag = '# -*- coding: utf-8 -*-'
%>\
${encoding_tag}
# This file was generated
<%
    import build.helper as helper

    config = template_parameters['metadata'].config
    attributes = config['attributes']
    functions = helper.filter_codegen_functions(config['functions'])

    module_name = config['module_name']
    c_function_prefix = config['c_function_prefix']

    attributes = helper.filter_codegen_attributes(config['attributes'])

    session_context_manager = None
    if 'task' in config['context_manager_name']:
        session_context_manager = '_' + config['context_manager_name']['task'].title()
        session_context_manager_initiate = functions[config['context_manager_name']['initiate_function']]['python_name']
        session_context_manager_abort = functions[config['context_manager_name']['abort_function']]['python_name']
%>\
<%def name="render_method(f)">\
<%
    '''Renders a Session method corresponding to the passed-in function metadata.'''

    parameters = f['parameters']
    enum_input_parameters = helper.filter_parameters(f, helper.ParameterUsageOptions.INPUT_ENUM_PARAMETERS)
    ivi_dance_parameter = helper.filter_ivi_dance_parameter(f)
    ivi_dance_size_parameter = helper.find_size_parameter(ivi_dance_parameter, parameters)
    len_parameter = helper.filter_len_parameter(f)
    len_size_parameter = helper.find_size_parameter(len_parameter, parameters)
    assert ivi_dance_size_parameter is None or len_size_parameter is None
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f['name'], config, indent=8)}
        '''
% for parameter in enum_input_parameters:
        ${helper.get_enum_type_check_snippet(parameter, indent=12)}
% endfor
% for p in helper.filter_parameters(f, helper.ParameterUsageOptions.LIBRARY_METHOD_CALL):
        ${helper.get_ctype_variable_declaration_snippet(p, parameters, config)}
% endfor
% if ivi_dance_parameter is not None:
        error_code = self._library.${c_function_prefix}${f['name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.LIBRARY_METHOD_CALL)})
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=${f['is_error_handling']})
        ${ivi_dance_size_parameter['ctypes_variable_name']} = visatype.${ivi_dance_size_parameter['ctypes_type']}(error_code)  # TODO(marcoskirsch): use get_ctype_variable_declaration_snippet()
        ${ivi_dance_parameter['ctypes_variable_name']} = (visatype.${ivi_dance_parameter['ctypes_type']} * ${ivi_dance_size_parameter['ctypes_variable_name']}.value)()  # TODO(marcoskirsch): use get_ctype_variable_declaration_snippet()
% endif
        error_code = self._library.${c_function_prefix}${f['name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.LIBRARY_METHOD_CALL)})
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=${f['is_error_handling']})
        ${helper.get_method_return_snippet(parameters, config)}
</%def>\
import ctypes

from ${module_name} import attributes
from ${module_name} import enums
from ${module_name} import errors
from ${module_name} import library_singleton
from ${module_name} import visatype
% for c in config['custom_types']:

from ${module_name} import ${c['file_name']}  # noqa: F401
% endfor


% if session_context_manager is not None:
class ${session_context_manager}(object):
    def __init__(self, session):
        self._session = session

    def __enter__(self):
        self._session.${session_context_manager_initiate}()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._session.${session_context_manager_abort}()


% endif
class _SessionBase(object):
    '''Base class for all ${config['driver_name']} sessions.'''

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

% for attribute in helper.sorted_attrs(attributes):
<%
rep_cap_attr_desc = '''
This property can use repeated capabilities (usually channels). If set or get directly on the
{0}.Session object, then the set/get will use all repeated capabilities in the session.
You can specify a subset of repeated capabilities using the Python index notation on an
{0}.Session instance, and calling set/get value on the result.:

    session['0,1'].{0} = var
    var = session['0,1'].{0}
'''
if attributes[attribute]['channel_based'] == 'True':
    attributes[attribute]['documentation']['tip'] = rep_cap_attr_desc.format(attributes[attribute]["name"].lower())
%>\
    %if attributes[attribute]['enum']:
    ${attributes[attribute]['python_name']} = attributes.AttributeEnum(attributes.Attribute${attributes[attribute]['type']}, enums.${attributes[attribute]['enum']}, ${attribute})
    %else:
    ${attributes[attribute]['python_name']} = attributes.Attribute${attributes[attribute]['type']}(${attribute})
    %endif
%   if 'documentation' in attributes[attribute] and len(helper.get_documentation_for_node_docstring(attributes[attribute], config, indent=4).strip()) > 0:
    '''
    ${helper.get_documentation_for_node_docstring(attributes[attribute], config, indent=4)}
    '''
%   endif
% endfor
<%
init_function = functions[config['init_function']]
init_method_params = helper.get_params_snippet(init_function, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)
init_call_params = helper.get_params_snippet(init_function, helper.ParameterUsageOptions.SESSION_METHOD_CALL)
%>\

    def __init__(self, repeated_capability):
        self._library = library_singleton.get()
        self._repeated_capability = repeated_capability
        self._encoding = 'windows-1251'

    def __setattr__(self, key, value):
        if self._is_frozen and key not in dir(self):
            raise AttributeError("'{0}' object has no attribute '{1}'".format(type(self).__name__, key))
        object.__setattr__(self, key, value)

    def _get_error_description(self, error_code):
        '''_get_error_description

        Returns the error description.
        '''
        try:
            _, error_string = self._get_error()
            return error_string
        except errors.Error:
            pass

        try:
            '''
            It is expected for _get_error to raise when the session is invalid
            (IVI spec requires GetError to fail).
            Use _error_message instead. It doesn't require a session.
            '''
            error_string = self._error_message(error_code)
            return error_string
        except errors.Error:
            return "Failed to retrieve error description."

    ''' These are code-generated '''

% for func_name in sorted({k: v for k, v in functions.items() if v['has_repeated_capability'] or v['is_error_handling']}):
${render_method(functions[func_name])}
% endfor

class _RepeatedCapability(_SessionBase):
    '''Allows for setting/getting properties and calling methods for specific repeated capabilities (such as channels) on your session.'''

    def __init__(self, ${config['session_handle_parameter_name']}, repeated_capability):
        super(_RepeatedCapability, self).__init__(repeated_capability)
        self._${config['session_handle_parameter_name']} = ${config['session_handle_parameter_name']}
        self._is_frozen = True


class Session(_SessionBase):
    '''${config['session_class_description']}'''

    def __init__(${init_method_params}):
        super(Session, self).__init__(repeated_capability='')
        self._${config['session_handle_parameter_name']} = 0  # This must be set before calling ${init_function['python_name']}().
        self._${config['session_handle_parameter_name']} = self.${init_function['python_name']}(${init_call_params})
        self._is_frozen = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def __getitem__(self, repeated_capability):
        '''Set/get properties or call methods with a repeated capability (i.e. channels)'''
        return _RepeatedCapability(self._${config['session_handle_parameter_name']}, repeated_capability)

    def initiate(self):
        return ${session_context_manager}(self)

    def close(self):
        try:
            self._close()
        except errors.Error as e:
            self._${config['session_handle_parameter_name']} = 0
            raise
        self._${config['session_handle_parameter_name']} = 0

    ''' These are code-generated '''

% for func_name in sorted({k: v for k, v in functions.items() if not v['has_repeated_capability'] and not v['is_error_handling']}):
${render_method(functions[func_name])}
% endfor


