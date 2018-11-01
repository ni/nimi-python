${template_parameters['encoding_tag']}
# This file was generated
<%
    import build.helper as helper

    config = template_parameters['metadata'].config
    attributes = config['attributes']
    enums = config['enums']
    functions = helper.filter_codegen_functions(config['functions'])

    module_name = config['module_name']

    attributes = helper.filter_codegen_attributes(config['attributes'])

    close_function_name = helper.camelcase_to_snakecase(config['close_function'])

    session_context_manager = None
    if 'task' in config['context_manager_name']:
        session_context_manager = '_' + config['context_manager_name']['task'].title()
        session_context_manager_initiate = functions[config['context_manager_name']['initiate_function']]['python_name']
        session_context_manager_abort = functions[config['context_manager_name']['abort_function']]['python_name']
%>\
import array  # noqa: F401
import ctypes
import datetime

% if attributes:
import ${module_name}._attributes as _attributes
% endif
import ${module_name}._converters as _converters
import ${module_name}._library_singleton as _library_singleton
import ${module_name}._visatype as _visatype
import ${module_name}.enums as enums
import ${module_name}.errors as errors
% for c in config['custom_types']:

import ${module_name}.${c['file_name']} as ${c['file_name']}  # noqa: F401
% endfor

# Used for __repr__
import pprint
pp = pprint.PrettyPrinter(indent=4)


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


def get_ctypes_and_array(value, array_type):
    if value is not None:
        if isinstance(value, array.array):
            value_array = value
        else:
            value_array = array.array(array_type, value)
    else:
        value_array = None

    return value_array


% if session_context_manager is not None:
class ${session_context_manager}(object):
    def __init__(self, session):
        self._session = session
        self._session.${session_context_manager_initiate}()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._session.${session_context_manager_abort}()


% endif
% if config['use_locking']:
# From https://stackoverflow.com/questions/5929107/decorators-with-parameters
def ivi_synchronized(f):
    def aux(*xs, **kws):
        session = xs[0]  # parameter 0 is 'self' which is the session object
        with session.lock():
            return f(*xs, **kws)
    return aux


class _Lock(object):
    def __init__(self, session):
        self._session = session

    def __enter__(self):
        # _lock_session is called from the lock() function, not here
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self._session._use_locking:
            self._session.unlock()


% endif
% if len(config['repeated_capabilities']) > 0:
class _RepeatedCapabilities(object):
    def __init__(self, session, prefix):
        self._session = session
        self._prefix = prefix

    def __getitem__(self, repeated_capability):
        '''Set/get properties or call methods with a repeated capability (i.e. channels)'''
        rep_caps_list = _converters.convert_repeated_capabilities(repeated_capability, self._prefix)

        return _SessionBase(${config['session_handle_parameter_name']}=self._session._${config['session_handle_parameter_name']}, repeated_capability_list=rep_caps_list, library=self._session._library, encoding=self._session._encoding, freeze_it=True)


# This is a very simple context manager we can use when we need to set/get attributes
# or call functions from _SessionBase that require no channels. It is tied to the specific
# implementation of _SessionBase and how repeated capabilities are handled.
class _NoChannel(object):
    def __init__(self, session):
        self._session = session

    def __enter__(self):
        self._repeated_capability_cache = self._session._repeated_capability
        self._session._repeated_capability = ''

    def __exit__(self, exc_type, exc_value, traceback):
        self._session._repeated_capability = self._repeated_capability_cache


% endif
class _SessionBase(object):
    '''Base class for all ${config['driver_name']} sessions.'''

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

% for attribute in helper.sorted_attrs(helper.filter_codegen_attributes(attributes)):
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
<%
init_function = config['functions']['_init_function']
init_method_params = helper.get_params_snippet(init_function, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)
init_call_params = helper.get_params_snippet(init_function, helper.ParameterUsageOptions.SESSION_METHOD_CALL)
constructor_params = helper.filter_parameters(init_function, helper.ParameterUsageOptions.SESSION_INIT_DECLARATION)
%>\
% if attributes:

% endif
    def __init__(self, repeated_capability_list, ${config['session_handle_parameter_name']}, library, encoding, freeze_it=False):
        self._repeated_capability_list = repeated_capability_list
        self._repeated_capability = ','.join(repeated_capability_list)
        self._${config['session_handle_parameter_name']} = ${config['session_handle_parameter_name']}
        self._library = library
        self._encoding = encoding
% if config['use_locking']:
        self._use_locking = True
% endif

        # Store the parameter list for later printing in __repr__
        param_list = []
        param_list.append("repeated_capability_list=" + pp.pformat(repeated_capability_list))
        param_list.append("${config['session_handle_parameter_name']}=" + pp.pformat(${config['session_handle_parameter_name']}))
        param_list.append("library=" + pp.pformat(library))
        param_list.append("encoding=" + pp.pformat(encoding))
        self._param_list = ', '.join(param_list)

        self._is_frozen = freeze_it

    def __repr__(self):
        return '{0}.{1}({2})'.format('${module_name}', self.__class__.__name__, self._param_list)

    def __setattr__(self, key, value):
        if self._is_frozen and key not in dir(self):
            raise AttributeError("'{0}' object has no attribute '{1}'".format(type(self).__name__, key))
        object.__setattr__(self, key, value)

    def __getitem__(self, key):
% if len(config['repeated_capabilities']) > 0:
        rep_caps = []
% for rep_cap in config['repeated_capabilities']:
        rep_caps.append("${rep_cap['python_name']}")
% endfor
        rep_cap_help_text = " You should use the applicable repeated capabilities container(s): {}".format(', '.join(rep_caps))
% else:
        rep_cap_help_text = ''
% endif
        raise TypeError("'Session' object does not support indexing." + rep_cap_help_text)

% if config['use_locking']:
    def _set_use_locking(self, use_locking):
        '''Allow runtime disabling of session locking

        This must be called immediately after creating the Session object and before any
        properties are accessed or methods are called

        Warning: Do not change this setting during a function call.
        '''
        self._use_locking = use_locking

% endif
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
% if functions[func_name]['use_session_lock'] and config['use_locking']:
    @ivi_synchronized
% endif
<%include file="${'/session.py' + method_template['session_filename'] + '.py.mako'}" args="f=functions[func_name], config=config, method_template=method_template" />\
% endfor
% endfor

class Session(_SessionBase):
    '''${config['session_class_description']}'''

    def __init__(${init_method_params}):
        r'''${config['session_class_description']}

        ${helper.get_function_docstring(init_function, False, config, indent=8)}
        '''
        super(Session, self).__init__(repeated_capability_list=[], ${config['session_handle_parameter_name']}=None, library=None, encoding=None, freeze_it=False)
% for p in init_function['parameters']:
%   if 'python_api_converter_name' in p:
        ${p['python_name']} = _converters.${p['python_api_converter_name']}(${p['python_name']}, self._encoding)
%   endif
% endfor
        self._library = _library_singleton.get()
        self._encoding = 'windows-1251'

        # Call specified init function
        self._${config['session_handle_parameter_name']} = 0  # This must be set before calling ${init_function['python_name']}().
        self._${config['session_handle_parameter_name']} = self.${init_function['python_name']}(${init_call_params})

        # Instantiate any repeated capability objects
% for rep_cap in config['repeated_capabilities']:
        self.${rep_cap['python_name']} = _RepeatedCapabilities(self, '${rep_cap["prefix"]}')
% endfor

        # Store the parameter list for later printing in __repr__
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
            self._${close_function_name}()
        except errors.DriverError:
            self._${config['session_handle_parameter_name']} = 0
            raise
        self._${config['session_handle_parameter_name']} = 0

    ''' These are code-generated '''

% for func_name in sorted({k: v for k, v in functions.items() if not v['render_in_session_base']}):
% for method_template in functions[func_name]['method_templates']:
% if functions[func_name]['use_session_lock'] and config['use_locking']:
    @ivi_synchronized
% endif
<%include file="${'/session.py' + method_template['session_filename'] + '.py.mako'}" args="f=functions[func_name], config=config, method_template=method_template" />\
% endfor
% endfor


