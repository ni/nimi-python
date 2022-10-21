${template_parameters['encoding_tag']}
# This file was generated
<%
    import build.helper as helper
    import os

    grpc_supported = template_parameters['include_grpc_support']

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
        render_initiate_in_session_base = functions[config['context_manager_name']['initiate_function']]['render_in_session_base']
%>\
import array  # noqa: F401
% if config['use_locking']:
# Used by @ivi_synchronized
from functools import wraps
% endif

% if attributes:
import ${module_name}._attributes as _attributes
% endif
import ${module_name}._converters as _converters
import ${module_name}._library_interpreter as _library_interpreter
import ${module_name}.enums as enums
import ${module_name}.errors as errors
% for c in config['custom_types']:

import ${module_name}.${c['file_name']} as ${c['file_name']}  # noqa: F401
% endfor

import hightime
% if config['uses_nitclk']:
import nitclk
% endif

# Used for __repr__
import pprint
pp = pprint.PrettyPrinter(indent=4)


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
    @wraps(f)
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
        self._session.unlock()


% endif
% if len(config['repeated_capabilities']) > 0:
class _RepeatedCapabilities(object):
    def __init__(self, session, prefix, current_repeated_capability_list):
        self._session = session
        self._prefix = prefix
        # We need at least one element. If we get an empty list, make the one element an empty string
        self._current_repeated_capability_list = current_repeated_capability_list if len(current_repeated_capability_list) > 0 else ['']
        # Now we know there is at lease one entry, so we look if it is an empty string or not
        self._separator = '/' if len(self._current_repeated_capability_list[0]) > 0 else ''

    def __getitem__(self, repeated_capability):
        '''Set/get properties or call methods with a repeated capability (i.e. channels)'''
        rep_caps_list = _converters.convert_repeated_capabilities(repeated_capability, self._prefix)
        complete_rep_cap_list = [current_rep_cap + self._separator + rep_cap for current_rep_cap in self._current_repeated_capability_list for rep_cap in rep_caps_list]

        return _SessionBase(
            repeated_capability_list=complete_rep_cap_list,
            all_channels_in_session=self._session._all_channels_in_session,
            interpreter=self._session._interpreter,
            freeze_it=True
        )


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
helper.add_attribute_rep_cap_tip(attributes[attribute], config)
%>\
    %if attributes[attribute]['enum']:
        %if helper.enum_uses_converter(enums[attributes[attribute]['enum']]):
    ${attributes[attribute]['python_name']} = _attributes.AttributeEnumWithConverter(_attributes.AttributeEnum(_attributes.Attribute${attributes[attribute]['type']}, enums.${enums[attributes[attribute]['enum']]['python_name']}, ${attribute}), _converters.${enums[attributes[attribute]['enum']]['enum_to_converted_value_function_name']}, _converters.${enums[attributes[attribute]['enum']]['converted_value_to_enum_function_name']})
        %else:
    ${attributes[attribute]['python_name']} = _attributes.AttributeEnum(_attributes.Attribute${attributes[attribute]['type']}, enums.${enums[attributes[attribute]['enum']]['python_name']}, ${attribute})
        %endif
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
constructor_params = helper.filter_parameters(init_function['parameters'], helper.ParameterUsageOptions.SESSION_INIT_DECLARATION)
%>\
% if attributes:

% endif
    def __init__(self, repeated_capability_list, all_channels_in_session, interpreter, freeze_it=False):
        self._repeated_capability_list = repeated_capability_list
        self._repeated_capability = ','.join(repeated_capability_list)
        self._all_channels_in_session = all_channels_in_session
        self._interpreter = interpreter

        # Store the parameter list for later printing in __repr__
        param_list = []
        param_list.append("repeated_capability_list=" + pp.pformat(repeated_capability_list))
        param_list.append("interpreter=" + pp.pformat(interpreter))
        self._param_list = ', '.join(param_list)

% if len(config['repeated_capabilities']) > 0:
        # Instantiate any repeated capability objects
%   for rep_cap in config['repeated_capabilities']:
        self.${rep_cap['python_name']} = _RepeatedCapabilities(self, '${rep_cap["prefix"]}', repeated_capability_list)
%   endfor

% endif
        # Finally, set _is_frozen to True which is used to prevent clients from accidentally adding
        # members when trying to set a property with a typo.
        self._is_frozen = freeze_it

    def __repr__(self):
        return '{0}.{1}({2})'.format('${module_name}', self.__class__.__name__, self._param_list)

    def __setattr__(self, key, value):
        if self._is_frozen and key not in dir(self):
            raise AttributeError("'{0}' object has no attribute '{1}'".format(type(self).__name__, key))
        object.__setattr__(self, key, value)

% if session_context_manager is not None and render_initiate_in_session_base:
    def initiate(self):
        '''initiate

        ${helper.get_function_docstring(helper.initiate_function_def_for_doc(functions, config), False, config, indent=8)}
        '''
        return ${session_context_manager}(self)

% endif
    ''' These are code-generated '''
% for func_name in sorted({k: v for k, v in functions.items() if v['render_in_session_base']}):
% for method_template in functions[func_name]['method_templates']:
% if method_template['session_filename'] != '/none':

% if functions[func_name]['use_session_lock'] and config['use_locking']:
    @ivi_synchronized
% endif
<%include file="${'/session.py' + method_template['session_filename'] + '.py.mako'}" args="f=functions[func_name], config=config, method_template=method_template" />\
% endif
% endfor
% endfor


class Session(_SessionBase):
    '''${config['session_class_description']}'''

<% grpc_channel_param = ', *, _grpc_channel=None' if grpc_supported else '' %>\
    def __init__(${init_method_params}${grpc_channel_param}):
        r'''${config['session_class_description']}

<%
ctor_for_docs = init_function
if grpc_supported:
    import copy
    ctor_for_docs = copy.deepcopy(ctor_for_docs)
    ctor_for_docs['parameters'].append(
        {
            'default_value': None,
            'direction': 'in',
            'documentation': { 'description': 'MeasurementLink gRPC channel' },
            'enum': None,
            'is_repeated_capability': False,
            'is_session_handle': False,
            'python_name': '_grpc_channel',
            'size': {'mechanism': 'fixed', 'value': 1},
            'type_in_documentation': 'grpc.Channel',
            'type_in_documentation_was_calculated': False,
            'use_in_python_api': False,
        },
    )
%>\
        ${helper.get_function_docstring(ctor_for_docs, False, config, indent=8)}
        '''
% if grpc_supported:
        if _grpc_channel:
            import ${module_name}._grpc_stub_interpreter as _grpc_stub_interpreter
            interpreter = _grpc_stub_interpreter.GrpcStubInterpreter(_grpc_channel)
        else:
            interpreter = _library_interpreter.LibraryInterpreter(encoding='windows-1251')
% else:
        interpreter = _library_interpreter.LibraryInterpreter(encoding='windows-1251')
% endif

        # Initialize the superclass with default values first, populate them later
        super(Session, self).__init__(
            repeated_capability_list=[],
            interpreter=interpreter,
            freeze_it=False,
            all_channels_in_session=None
        )
% for p in init_function['parameters']:
%   if 'python_api_converter_name' in p:
        ${p['python_name']} = _converters.${p['python_api_converter_name']}(${p['python_name']})
%   endif
% endfor

        # Call specified init function
        # Note that _library_interpreter sets _${config['session_handle_parameter_name']} to 0 in its constructor, so that if
        # ${init_function['python_name']} fails, the error handler can reference it.
        # And then once ${init_function['python_name']} succeeds, we can update _library_interpreter._${config['session_handle_parameter_name']}
        # with the actual session handle.
        self._interpreter._${config['session_handle_parameter_name']} = self.${init_function['python_name']}(${init_call_params})

% if config['uses_nitclk']:
%   if grpc_supported:
        # NI-TClk does not work over NI gRPC Device Server
        if not _grpc_channel:
            self.tclk = nitclk.SessionReference(self._interpreter._${config['session_handle_parameter_name']})
%   else:
        self.tclk = nitclk.SessionReference(self._interpreter._${config['session_handle_parameter_name']})
%   endif

% endif
        # Store the parameter list for later printing in __repr__
        param_list = []
%       for param in constructor_params:
        param_list.append("${param['python_name']}=" + pp.pformat(${param['python_name']}))
%       endfor
        self._param_list = ', '.join(param_list)

        # Store the list of channels in the Session which is needed by some nimi-python modules.
        # Use try/except because not all the modules support channels.
        # self.get_channel_names() and self.channel_count can only be called after the session
        # handle `self._interpreter._${config['session_handle_parameter_name']}` is set
        try:
            self._all_channels_in_session = self.get_channel_names(range(self.channel_count))
        except AttributeError:
            self._all_channels_in_session = None

        # Finally, set _is_frozen to True which is used to prevent clients from accidentally adding
        # members when trying to set a property with a typo.
        self._is_frozen = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

% if session_context_manager is not None and not render_initiate_in_session_base:
    def initiate(self):
        '''initiate

        ${helper.get_function_docstring(helper.initiate_function_def_for_doc(functions, config), False, config, indent=8)}
        '''
        return ${session_context_manager}(self)

% endif
    def close(self):
        '''close

        ${helper.get_function_docstring(helper.close_function_def_for_doc(functions, config), False, config, indent=8)}
        '''
        try:
            self._${close_function_name}()
        except errors.DriverError:
            self._interpreter._${config['session_handle_parameter_name']} = 0
            raise
        self._interpreter._${config['session_handle_parameter_name']} = 0

    ''' These are code-generated '''
% for func_name in sorted({k: v for k, v in functions.items() if not v['render_in_session_base']}):
% for method_template in functions[func_name]['method_templates']:
% if method_template['session_filename'] != '/none':

% if functions[func_name]['use_session_lock'] and config['use_locking']:
    @ivi_synchronized
% endif
<%include file="${'/session.py' + method_template['session_filename'] + '.py.mako'}" args="f=functions[func_name], config=config, method_template=method_template" />\
% endif
% endfor
% endfor
