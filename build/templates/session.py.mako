# This file was generated
<%
    import build.helper as helper

    config = template_parameters['metadata'].config
    module_name = config['module_name']
    c_function_prefix = config['c_function_prefix']
    attributes = template_parameters['metadata'].attributes

    functions = template_parameters['metadata'].functions
    functions = helper.extract_codegen_functions(functions)
    functions = helper.add_all_metadata(functions)
    functions = sorted(functions, key=lambda k: k['name'])
%>\
import ctypes

from ${module_name} import ctypes_types
from ${module_name} import enums
from ${module_name} import errors
from ${module_name} import library


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
        return obj._get_attribute_vi_boolean(self.channel, self.attribute_id) is not 0

    def __set__(self, obj, value):
        obj._set_attribute_vi_boolean(self.channel, self.attribute_id, (value is not 0))


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
            raise TypeError('Value mode must be of type ' + str(self.attribute_type))
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
%   if 'shortDescription' in attributes[attribute]:
    '''
    ${helper.get_indented_docstring_snippet(attributes[attribute]['shortDescription'], indent=4)}
    '''
%   endif
% endfor

    def __init__(self, resource_name, id_query=0, reset_device=False, options_string=""):
        self.library = library.get_library()
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

    def __del__(self):
        pass

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

    # method needed for generic driver exceptions
    def _get_error_description(self, error_code):
        new_error_code = ctypes_types.ViStatus_ctype(0)
        buffer_size = self.library.${c_function_prefix}GetError(self.vi, ctypes.byref(new_error_code), 0, None)
        assert (new_error_code.value == error_code)

        if (buffer_size > 0):
            '''
            Return code > 0 from first call to GetError represents the size of
            the description.  Call it again.
            Ignore incoming IVI error code and return description from the driver
            (trust that the IVI error code was properly stored in the session
            by the driver)
            '''
            error_code = ctypes_types.ViStatus_ctype(error_code)
            error_message = ctypes.create_string_buffer(buffer_size)
            self.library.${c_function_prefix}GetError(self.vi, ctypes.byref(error_code), buffer_size, ctypes.cast(error_message, ctypes.POINTER(ctypes_types.ViChar_ctype)))
        else:
            '''
            Return code <= 0 from GetError indicates a problem.  This is expected
            when the session is invalid (IVI spec requires GetError to fail).
            Use GetErrorMessage instead.  It doesn't require a session.

            Call ${c_function_prefix}GetErrorMessage, pass VI_NULL for the buffer in order to retrieve
            the length of the error message.
            '''
            error_code = buffer_size
            buffer_size = self.library.${c_function_prefix}GetErrorMessage(self.vi, error_code, 0, None)
            error_message = ctypes.create_string_buffer(buffer_size)
            self.library.${c_function_prefix}GetErrorMessage(self.vi, error_code, buffer_size, ctypes.cast(error_message, ctypes.POINTER(ctypes_types.ViChar_ctype)))

        # TODO(marcoskirsch): By hardcoding encoding "ascii", internationalized strings will throw.
        #       Which encoding should we be using? https://docs.python.org/3/library/codecs.html#standard-encodings
        return new_error_code.value, error_message.value.decode("ascii")

    ''' These are code-generated '''
% for f in functions:
<%
    input_parameters = helper.extract_input_parameters(f['parameters'])
    output_parameters = helper.extract_output_parameters(f['parameters'])
    enum_input_parameters = helper.extract_enum_parameters(input_parameters)
%>
    def ${f['python_name']}(${helper.get_method_parameters_snippet(input_parameters)}):
% for parameter in enum_input_parameters:
        ${helper.get_enum_type_check_snippet(parameter, indent=12)}
% endfor
% for output_parameter in output_parameters:
        ${helper.get_ctype_variable_declaration_snippet(output_parameter)}
% endfor
        error_code = self.library.${c_function_prefix}${f['name']}(${helper.get_library_call_parameter_snippet(f['parameters'])})
        errors._handle_error(self, error_code)
        ${helper.get_method_return_snippet(output_parameters)}
% endfor

    ''' These are temporarily hand-coded because the generator can't handle buffers yet '''

    def _get_attribute_vi_string(self, channel_name, attribute_id):  # noqa: F811
        # Do the IVI dance
        # Don't use _handle_error, because positive value in error_code means size, not warning.
        buffer_size = 0
        value_ctype = ctypes.cast(ctypes.create_string_buffer(buffer_size), ctypes_types.ViString_ctype)
        error_code = self.library.niDMM_GetAttributeViString(self.vi, channel_name.encode('ascii'), attribute_id, buffer_size, value_ctype)
        if(errors._is_error(error_code)):
            raise errors.Error(self.library, self.vi, error_code)
        buffer_size = error_code
        value_ctype = ctypes.cast(ctypes.create_string_buffer(buffer_size), ctypes_types.ViString_ctype)
        error_code = self.library.niDMM_GetAttributeViString(self.vi, channel_name.encode('ascii'), attribute_id, buffer_size, value_ctype)
        errors._handle_error(self, error_code)
        return value_ctype.value.decode("ascii")
