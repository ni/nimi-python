# This file was generated
<%
    import helper

    config = template_parameters['metadata'].config
    module_name = config['module_name']
    c_function_prefix = config['c_function_prefix']
    attributes = template_parameters['metadata'].attributes
%>\

import ctypes
from ${module_name} import errors
from ${module_name} import library
from ${module_name} import enums
from ${module_name} import ctypes_types


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
        if type(value) is not self.attribute_type: raise TypeError('Value mode must be of type ' + str(self.attribute_type))
        obj._set_attribute_vi_int32(self.channel, self.attribute_id, value.value)


# TODO(marcoskirsch): We may want to support this, plus a Session constructor that uses an existing ViSession.
class AttributeViSession(object):

    def __init__(self, attribute_id):
        self.attribute_id = attribute_id

    def __get__(self, obj, objtype):
        raise TypeError('Attributes of type ViSession are unsupported in Python')

    def __set__(self, obj, value):
        raise TypeError('Attributes of type ViSession are unsupported in Python')


class Session(object):
    '''${config['session_description']}'''

% for attribute in attributes:
    %if attributes[attribute]['enum']:
    ${attribute.lower()} = AttributeEnum(${attributes[attribute]['id']}, enums.${attributes[attribute]['enum']})
    %else:
    ${attribute.lower()} = Attribute${attributes[attribute]['type']}(${attributes[attribute]['id']})
    %endif
% endfor

    def __init__(self, resourceName, idQuery = 0, reset = False, optionString = ""):
        self.vi = 0
        self.library = library.get_library()
        session_handle = ctypes_types.ViSession_ctype(0)
        error_code = self.library.${c_function_prefix}InitWithOptions(resourceName.encode('ascii'), idQuery, reset, optionString.encode('ascii'), ctypes.pointer(session_handle))
        self.vi = session_handle.value
        errors._handle_error(self, error_code)

    def __del__(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        # TODO(marcoskirsch): Should we raise an exception on double close? Look at what File does.
        if(self.vi != 0):
            error_code = self.library.${c_function_prefix}close(self.vi)
            if(error_code < 0):
                # TODO(marcoskirsch): This will occur when session is "stolen". Maybe don't even bother with printing?
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
            self.library.${c_function_prefix}GetError(self.vi, ctypes.byref(error_code), buffer_size, error_message)
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
            print("buffer_size", buffer_size)
            error_message = ctypes.create_string_buffer(buffer_size)
            self.library.${c_function_prefix}GetErrorMessage(self.vi, error_code, buffer_size, error_message)

        #@TODO: By hardcoding encoding "ascii", internationalized strings will throw.
        #       Which encoding should we be using? https://docs.python.org/3/library/codecs.html#standard-encodings
        return new_error_code.value, error_message.value.decode("ascii")

    ''' These are code-generated '''

    #TODO (marcoskirsch): attribute methods will be like "_set_attribute_vi_boolean", should be _set_attribute_ViBoolean. Open issue about it.
<%
    functions = template_parameters['metadata'].functions
    functions = helper.extract_codegen_functions(functions)
    functions = helper.add_all_metadata(functions)
%>\
% for f in functions:
<%
    input_parameters = helper.extract_input_parameters(f['parameters'])
    output_parameters = helper.extract_output_parameters(f['parameters'])
    enum_input_parameters = helper.extract_enum_parameters(input_parameters)
%>
    def ${f['python_name']}(${helper.get_method_parameters_snippet(input_parameters)}):
% for parameter in enum_input_parameters:
        ${helper.get_enum_type_check_snippet(parameter)}
% endfor
% for output_parameter in output_parameters:
        ${output_parameter['ctypes_variable_name']} = ctypes_types.${output_parameter['ctypes_type']}(0)
% endfor
        error_code = self.library.${c_function_prefix}${f['name']}(${helper.get_library_call_parameter_snippet(f['parameters'])})
        errors._handle_error(self, error_code)
        ${helper.get_method_return_snippet(output_parameters)}
% endfor


    ''' These are temporarily hand-coded because the generator can't handle buffers yet '''

    def _get_attribute_vi_string(self, channel, attribute_id):
        error_code = self.library.${c_function_prefix}GetAttributeViString(self.vi, None, attribute_id, 0, None)
        # Do the IVI dance
        # Don't use _handle_error, because positive value in error_code means size, not warning.
        if(errors._is_error(error_code)): raise errors.Error(self.library, self.vi, error_code)
        buffer_size = error_code
        value = ctypes.create_string_buffer(buffer_size)
        error_code = self.library.${c_function_prefix}GetAttributeViString(self.vi, None, attribute_id, buffer_size, value)
        errors._handle_error(self, error_code)
        return value.value.decode("ascii")
