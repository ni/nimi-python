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

    import pprint

    pp = pprint.PrettyPrinter(indent=4)

    functions = helper.extract_codegen_functions(functions)
%>\
import ctypes

from ${module_name} import ctypes_types
from ${module_name} import enums
from ${module_name} import errors
from ${module_name} import library_singleton
from ${module_name} import python_types


class AttributeViInt32(object):

    def __init__(self, attribute_id):
        self.attribute_id = attribute_id
        self.channel = ''

    def __get__(self, obj, objtype):
        assert objtype is Session
        return obj._get_attribute_vi_int32(self.channel, self.attribute_id)

    def __set__(self, obj, value):
        obj._set_attribute_vi_int32(self.channel, self.attribute_id, value)


class AttributeViReal64(object):

    def __init__(self, attribute_id):
        self.attribute_id = attribute_id
        self.channel = ''

    def __get__(self, obj, objtype):
        assert objtype is Session
        return obj._get_attribute_vi_real64(self.channel, self.attribute_id)

    def __set__(self, obj, value):
        obj._set_attribute_vi_real64(self.channel, self.attribute_id, value)


class AttributeViString(object):

    def __init__(self, attribute_id):
        self.attribute_id = attribute_id
        self.channel = ''

    def __get__(self, obj, objtype):
        assert objtype is Session
        return obj._get_attribute_vi_string(self.channel, self.attribute_id)

    def __set__(self, obj, value):
        obj._set_attribute_vi_string(self.channel, self.attribute_id, value)


class AttributeViBoolean(object):

    def __init__(self, attribute_id):
        self.attribute_id = attribute_id
        self.channel = ''

    def __get__(self, obj, objtype):
        assert objtype is Session
        return obj._get_attribute_vi_boolean(self.channel, self.attribute_id)

    def __set__(self, obj, value):
        obj._set_attribute_vi_boolean(self.channel, self.attribute_id, value)


class AttributeEnum(object):

    def __init__(self, attribute_id, enum_meta_class):
        self.attribute_id = attribute_id
        self.attribute_type = enum_meta_class
        self.channel = ''

    def __get__(self, obj, objtype):
        assert objtype is Session
        return self.attribute_type(obj._get_attribute_vi_int32(self.channel, self.attribute_id))

    def __set__(self, obj, value):
        if type(value) is not self.attribute_type:
            raise TypeError('must be ${module_name}.' + str(self.attribute_type.__name__) + ' not ' + str(type(value).__name__))
        obj._set_attribute_vi_int32(self.channel, self.attribute_id, value.value)
% for c in config['context_manager']:
<%
context_name = 'acquisition' if c['direction'] == 'input' else 'generation'
%>\


class ${context_name.title()}(object):
    def __init__(self, session):
        self.session = session

    def __enter__(self):
        self.session._initiate()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.session._abort()
% endfor


class Session(object):
    '''${config['session_description']}'''

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

% for attribute in helper.sorted_attrs(attributes):
    %if attributes[attribute]['enum']:
    ${attributes[attribute]['name'].lower()} = AttributeEnum(${attribute}, enums.${attributes[attribute]['enum']})
    %else:
    ${attributes[attribute]['name'].lower()} = Attribute${attributes[attribute]['type']}(${attribute})
    %endif
%   if 'documentation' in attributes[attribute]:
    '''
    ${helper.get_documentation_for_node_docstring(attributes[attribute], config, indent=4)}
    '''
%   endif
% endfor

    def __init__(self, resource_name, id_query=False, reset_device=False, options_string=""):
        self.library = library_singleton.get()
        self.vi = 0  # This must be set before calling _init_with_options.
        self.vi = self._init_with_options(resource_name, id_query, reset_device, options_string)

        self._is_frozen = True

    def __setattr__(self, key, value):
        if self._is_frozen and key not in dir(self):
            raise TypeError("%r is a frozen class" % self)
        object.__setattr__(self, key, value)
% for c in config['context_manager']:
<%
context_name = 'acquisition' if c['direction'] == 'input' else 'generation'
%>\

    def initiate(self):
        return ${context_name.title()}(self)
% endfor

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        # TODO(marcoskirsch): Should we raise an exception on double close? Look at what File does.
        try:
            self._close()
        except errors.Error:
            # TODO(marcoskirsch): This will occur when session is "stolen". Change to log instead
            print("Failed to close session.")
        self.vi = 0

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
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParamListType.METHOD)}):
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
        error_code = self.library.${c_function_prefix}${func_name}(${helper.get_library_call_parameter_snippet(f['parameters'])})
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=${f['is_error_handling']})
        ${helper.get_method_return_snippet(f['parameters'])}
% else:
        ${ivi_dance_size_parameter['python_name']} = 0
        ${ivi_dance_parameter['ctypes_variable_name']} = None
        error_code = self.library.${c_function_prefix}${func_name}(${helper.get_library_call_parameter_snippet(f['parameters'])})
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=${f['is_error_handling']})
        ${ivi_dance_size_parameter['python_name']} = error_code
        ${ivi_dance_parameter['ctypes_variable_name']} = ctypes.cast(ctypes.create_string_buffer(${ivi_dance_size_parameter['python_name']}), ctypes_types.${ivi_dance_parameter['ctypes_type']})
        error_code = self.library.${c_function_prefix}${func_name}(${helper.get_library_call_parameter_snippet(f['parameters'])})
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=${f['is_error_handling']})
        ${helper.get_method_return_snippet(f['parameters'])}
% endif
% endfor

