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

    attributes = helper.filter_codegen_attributes(config['attributes'])

    session_context_manager = None
    if 'task' in config['context_manager_name']:
        session_context_manager = '_' + config['context_manager_name']['task'].title()
        session_context_manager_initiate = functions[config['context_manager_name']['initiate_function']]['python_name']
        session_context_manager_abort = functions[config['context_manager_name']['abort_function']]['python_name']
%>\
import ctypes

from ${module_name} import _converters  # noqa: F401   TODO(texasaggie97) remove noqa once we are using converters everywhere
from ${module_name} import attributes
from ${module_name} import enums
from ${module_name} import errors
from ${module_name} import library_singleton
from ${module_name} import visatype
% for c in config['custom_types']:

from ${module_name} import ${c['file_name']}  # noqa: F401
% endfor

# Used for __repr__
import pprint
pp = pprint.PrettyPrinter(indent=4)


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
% for rep_cap in config['repeated_capabilities']:
class _${rep_cap['python_class_name']}(object):
    def __init__(self, ${config['session_handle_parameter_name']}, library, encoding):
        self._${config['session_handle_parameter_name']} = ${config['session_handle_parameter_name']}
        self._library = library
        self._encoding = encoding

    def __getitem__(self, repeated_capability):
        '''Set/get properties or call methods with a repeated capability (i.e. channels)'''
        # First try it as a list
        try:
            rep_cap_list = [str(r) if str(r).lower().startswith('${rep_cap["prefix"].lower()}') else '${rep_cap["prefix"]}' + str(r) for r in repeated_capability]
        except TypeError:
            # Then try it as a slice
            try:
                def ifnone(a, b):
                    return b if a is None else a
                # Turn the slice into a list so we can iterate over it
                rep_cap_list = list(range(ifnone(repeated_capability.start, 0), repeated_capability.stop, ifnone(repeated_capability.step, 1)))
                # Add prefix to each entry
                rep_cap_list = ['${rep_cap["prefix"]}' + str(r) for r in rep_cap_list]
            # Otherwise it must be a single item
            except TypeError:
                rep_cap_list = [str(repeated_capability) if str(repeated_capability).lower().startswith('${rep_cap["prefix"].lower()}') else '${rep_cap["prefix"]}' + str(repeated_capability)]

        return _SessionBase(${config['session_handle_parameter_name']}=self._${config['session_handle_parameter_name']}, repeated_capability=','.join(rep_cap_list), library=self._library, encoding=self._encoding, freeze_it=True)


% endfor
class _SessionBase(object):
    '''Base class for all ${config['driver_name']} sessions.'''

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

% for attribute in helper.sorted_attrs(helper.filter_codegen_attributes(attributes)):
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
init_method_params = helper.get_params_snippet(init_function, helper.ParameterUsageOptions.SESSION_INIT_DECLARATION)
init_call_params = helper.get_params_snippet(init_function, helper.ParameterUsageOptions.SESSION_INIT_CALL)
constructor_params = helper.filter_parameters(init_function, helper.ParameterUsageOptions.SESSION_INIT_DECLARATION)
%>\

    def __init__(self, repeated_capability, ${config['session_handle_parameter_name']}=None, library=None, encoding=None, freeze_it=False):
        self._repeated_capability = repeated_capability
        self._${config['session_handle_parameter_name']} = ${config['session_handle_parameter_name']}
        self._library = library
        self._encoding = encoding
        self._param_list = "repeated_capability=" + pp.pformat(repeated_capability)
        self._is_frozen = freeze_it

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

% for func_name in sorted({k: v for k, v in functions.items() if v['render_in_session_base']}):
% for method_template in functions[func_name]['method_templates']:
<%include file="${'/session.py' + method_template['session_filename'] + '.py.mako'}" args="f=functions[func_name], config=config, method_template=method_template" />\
% endfor
% endfor

class Session(_SessionBase):
    '''${config['session_class_description']}'''

    def __init__(${init_method_params}):
        super(Session, self).__init__(repeated_capability='')
        self._library = library_singleton.get()
        self._encoding = 'windows-1251'
        self._${config['session_handle_parameter_name']} = 0  # This must be set before calling ${init_function['python_name']}().
        self._${config['session_handle_parameter_name']} = self.${init_function['python_name']}(${init_call_params})
% for rep_cap in config['repeated_capabilities']:
        self.${rep_cap['python_name']} = _${rep_cap['python_class_name']}(self._${config['session_handle_parameter_name']}, self._library, self._encoding)
% endfor
        param_list = []
%       for param in constructor_params:
        param_list.append("${param['python_name']}=" + pp.pformat(${param['python_name']}))
%       endfor
        self._param_list = ', '.join(param_list)
        self._is_frozen = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

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

% for func_name in sorted({k: v for k, v in functions.items() if not v['render_in_session_base']}):
% for method_template in functions[func_name]['method_templates']:
<%include file="${'/session.py' + method_template['session_filename'] + '.py.mako'}" args="f=functions[func_name], config=config, method_template=method_template" />\
% endfor
% endfor


