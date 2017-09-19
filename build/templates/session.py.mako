<%
# Have to put this in a variable and add it that way because mako keeps thinking it is for it, not for the output file
encoding_tag = '# -*- coding: utf-8 -*-'
%>\
${encoding_tag}
# This file was generated
<%
    import build.helper as helper

    config        = template_parameters['metadata'].config
    attributes    = config['attributes']
    functions     = config['functions']

    module_name = config['module_name']
    c_function_prefix = config['c_function_prefix']
    attributes = template_parameters['metadata'].attributes

    functions = helper.extract_codegen_functions(functions)

    session_context_manager = '_' + config['context_manager_name']['task'].title() if 'task' in config['context_manager_name'] else None
%>\
import ctypes

from ${module_name} import attributes
from ${module_name} import ctypes_types
from ${module_name} import enums
from ${module_name} import errors
from ${module_name} import library_singleton
from ${module_name} import python_types


% if session_context_manager is not None:
class ${session_context_manager}(object):
    def __init__(self, session):
        self.session = session

    def __enter__(self):
        self.session._initiate()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.session._abort()


% endif
class _SessionBase(object):
    '''Base class for all ${config['driver_name']} sessions.'''

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

% for attribute in helper.sorted_attrs(attributes):
    %if attributes[attribute]['enum']:
    ${attributes[attribute]['name'].lower()} = attributes.AttributeEnum(attributes.Attribute${attributes[attribute]['type']}, enums.${attributes[attribute]['enum']}, ${attribute})
    %else:
    ${attributes[attribute]['name'].lower()} = attributes.Attribute${attributes[attribute]['type']}(${attribute})
    %endif
%   if 'documentation' in attributes[attribute]:
    '''
    ${helper.get_documentation_for_node_docstring(attributes[attribute], config, indent=4)}
    '''
%   endif
% endfor
<%
init_function = functions[config['init_function']]
init_method_params = helper.get_params_snippet(init_function, helper.ParamListType.API_METHOD_DECLARATION)
init_call_params = helper.get_params_snippet(init_function, helper.ParamListType.API_METHOD_CALL)
%>\

    def __init__(self, repeated_capability):
        # TODO(marcoskirsch): rename to _library.
        self.library = library_singleton.get()
        self._repeated_capability = repeated_capability

    def __setattr__(self, key, value):
        if self._is_frozen and key not in dir(self):
            raise TypeError("%r is a frozen class" % self)
        object.__setattr__(self, key, value)

    def get_error_description(self, error_code):
        '''get_error_description

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
            Use _get_error_message instead. It doesn't require a session.
            '''
            error_string = self._get_error_message(error_code)
            return error_string
        except errors.Error:
            return "Failed to retrieve error description."

    ''' These are code-generated '''
% for func_name in sorted(functions):
<%
    f = functions[func_name]
    parameters = f['parameters']
    input_parameters = helper.extract_input_parameters(parameters)
    output_parameters = helper.extract_output_parameters(parameters)
    enum_input_parameters = helper.extract_enum_parameters(input_parameters)
    ivi_dance_parameter = helper.extract_ivi_dance_parameter(parameters)
    ivi_dance_size_parameter = helper.find_size_parameter(ivi_dance_parameter, parameters)
%>
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParamListType.API_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(func_name, config, indent=8)}
        '''
% for parameter in enum_input_parameters:
        ${helper.get_enum_type_check_snippet(parameter, indent=12)}
% endfor
% for output_parameter in output_parameters:
        ${helper.get_ctype_variable_declaration_snippet(output_parameter, parameters)}
% endfor
% if ivi_dance_parameter is None:
        error_code = self.library.${c_function_prefix}${func_name}(${helper.get_params_snippet(f, helper.ParamListType.LIBRARY_CALL)})
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=${f['is_error_handling']})
        ${helper.get_method_return_snippet(f['parameters'])}
% else:
        ${ivi_dance_size_parameter['python_name']} = 0
        ${ivi_dance_parameter['ctypes_variable_name']} = None
        error_code = self.library.${c_function_prefix}${func_name}(${helper.get_params_snippet(f, helper.ParamListType.LIBRARY_CALL)})
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=${f['is_error_handling']})
        ${ivi_dance_size_parameter['python_name']} = error_code
        ${ivi_dance_parameter['ctypes_variable_name']} = ctypes.cast(ctypes.create_string_buffer(${ivi_dance_size_parameter['python_name']}), ctypes_types.${ivi_dance_parameter['ctypes_type']})
        error_code = self.library.${c_function_prefix}${func_name}(${helper.get_params_snippet(f, helper.ParamListType.LIBRARY_CALL)})
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=${f['is_error_handling']})
        ${helper.get_method_return_snippet(f['parameters'])}
% endif
% endfor


class _RepeatedCapability(_SessionBase):
    '''Allows for setting/getting property values for specific channels in your session.'''

    def __init__(self, vi, channel):
        super(_RepeatedCapability, self).__init__(repeated_capability=channel)
        self.vi = vi
        self._is_frozen = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass


class Session(_SessionBase):
    '''${config['session_class_description']}'''

    def __init__(${init_method_params}):
        super(Session, self).__init__(repeated_capability='')
        # TODO(marcoskirsch): private members should start with _
        self.${config['session_handle_parameter_name']} = 0  # This must be set before calling _init_with_options.
        self.${config['session_handle_parameter_name']} = self.${init_function['python_name']}(${init_call_params})
        self._is_frozen = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def __getitem__(self, repeated_capability):
        '''Set/get properties or call methods with a repeated capabiilty (i.e. channels)'''
        return _RepeatedCapability(self.vi, repeated_capability)

    def initiate(self):
        return ${session_context_manager}(self)

    def close(self):
        # TODO(marcoskirsch): Should we raise an exception on double close? Look at what File does.
        try:
            self._close()
        except errors.Error:
            # TODO(marcoskirsch): This will occur when session is "stolen". Change to log instead
            print("Failed to close session.")
        self.vi = 0


