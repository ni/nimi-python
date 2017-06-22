# This file was generated
<%
    config = template_parameters['metadata'].config
    module_name = config['module_name']
    c_function_prefix = config['c_function_prefix']
    attributes = template_parameters['metadata'].attributes

    def snakecase_to_camelcase(snake_string):
        """Converts a C-style SNAKE_CASE string to camelCase"""
        components = snake_string.split('_')
        return components[0].lower() + "".join(component.title() for component in components[1:])
%>

import ctypes
from ${module_name} import errors
from ${module_name} import library
from ${module_name} import enums


class AttributeViInt32(object):

    def __init__(self, attribute_id):
        self.attribute_id = attribute_id

    def __get__(self, obj, objtype):
        assert objtype is Session
        return obj.getAttributeViInt32(self.attribute_id)

    def __set__(self, obj, value):
        obj.setAttributeViInt32(self.attribute_id, value)


class AttributeViReal64(object):

    def __init__(self, attribute_id):
        self.attribute_id = attribute_id

    def __get__(self, obj, objtype):
        assert objtype is Session
        return obj.getAttributeViReal64(self.attribute_id)

    def __set__(self, obj, value):
        obj.setAttributeViReal64(self.attribute_id, value)


class AttributeViString(object):

    def __init__(self, attribute_id):
        self.attribute_id = attribute_id

    def __get__(self, obj, objtype):
        assert objtype is Session
        return obj.getAttributeViString(self.attribute_id)

    def __set__(self, obj, value):
        obj.setAttributeViString(self.attribute_id, value)


class AttributeViBoolean(object):

    def __init__(self, attribute_id):
        self.attribute_id = attribute_id

    def __get__(self, obj, objtype):
        assert objtype is Session
        return obj.getAttributeViBoolean(self.attribute_id) is not 0

    def __set__(self, obj, value):
        obj.setAttributeViBoolean(self.attribute_id, (value is not 0))


class AttributeEnum(object):

    def __init__(self, attribute_id, enum_meta_class):
        self.attribute_id = attribute_id
        self.attribute_type = enum_meta_class

    def __get__(self, obj, objtype):
        assert objtype is Session
        return self.attribute_type(obj.getAttributeViInt32(self.attribute_id))

    def __set__(self, obj, value):
        if type(value) is not self.attribute_type: raise TypeError('Value mode must be of type ' + str(self.attribute_type))
        obj.setAttributeViInt32(self.attribute_id, value.value)


# TODO(marcoskirsch): We may want to support this, plus a Session constructor that uses an existing ViSession.
class AttributeViSession(object):

    def __init__(self, attribute_id):
        self.attribute_id = attribute_id

    def __get__(self, obj, objtype):
        raise TypeError('Attributes of type ViSession are unsupported in Python')

    def __set__(self, obj, value):
        raise TypeError('Attributes of type ViSession are unsupported in Python')


class Session(object):
    """${config['session_description']}"""

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
        session_handle = ctypes.c_ulong(0)
        error_code = self.library.${c_function_prefix}InitWithOptions(resourceName.encode('ascii'), idQuery, reset, optionString.encode('ascii'), ctypes.pointer(session_handle))
        self.vi = session_handle.value
        errors._handle_error(self.library, self.vi, error_code)

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
            self.sesion_handle = ctypes.c_ulong(0)

    def configure_measurement_digits(self, mode, range, digits_of_resolution):
        if type(mode) is not enums.Function: raise TypeError('Parameter mode must be of type ' + str(enums.Function))
        error_code = self.library.${c_function_prefix}ConfigureMeasurementDigits(self.vi, mode.value, range, digits_of_resolution)
        errors._handle_error(self.library, self.vi, error_code)

    def read(self, timeout_in_milliseconds = 10000):
        measurement = ctypes.c_double(0)
        error_code = self.library.${c_function_prefix}Read(self.vi, timeout_in_milliseconds, ctypes.byref(measurement))
        errors._handle_error(self.library, self.vi, error_code)
        return measurement.value

    def setAttributeViInt32(self, attribute_id, value):
        error_code = self.library.${c_function_prefix}SetAttributeViInt32(self.vi, b'', attribute_id, value)
        errors._handle_error(self.library, self.vi, error_code)

    def getAttributeViInt32(self, attribute_id):
        value = ctypes.c_long(0)
        error_code = self.library.${c_function_prefix}GetAttributeViInt32(self.vi, None, attribute_id, ctypes.byref(value))
        errors._handle_error(self.library, self.vi, error_code)
        return value.value

    def setAttributeViReal64(self, attribute_id, value):
        error_code = self.library.${c_function_prefix}SetAttributeViReal64(self.vi, b'', attribute_id, value)
        errors._handle_error(self.library, self.vi, error_code)

    def getAttributeViReal64(self, attribute_id):
        value = ctypes.c_double(0)
        error_code = self.library.${c_function_prefix}GetAttributeViReal64(self.vi, None, attribute_id, ctypes.byref(value))
        errors._handle_error(self.library, self.vi, error_code)
        return value.value

    def setAttributeViString(self, attribute_id, value):
        error_code = self.library.${c_function_prefix}SetAttributeViString(self.vi, b'', attribute_id, value.encode('ascii'))
        errors._handle_error(self.library, self.vi, error_code)

    def getAttributeViString(self, attribute_id):
        error_code = self.library.${c_function_prefix}GetAttributeViString(self.vi, None, attribute_id, 0, None)
        # Do the IVI dance
        # Don't use _handle_error, because positive value in error_code means size, not warning.
        if(errors._is_error(error_code)): raise errors.Error(self.library, self.vi, error_code)
        buffer_size = error_code
        value = ctypes.create_string_buffer(buffer_size)
        error_code = self.library.${c_function_prefix}GetAttributeViString(self.vi, None, attribute_id, buffer_size, value)
        errors._handle_error(self.library, self.vi, error_code)
        return value.value.decode("ascii")

    def setAttributeViBoolean(self, attribute_id, value):
        error_code = self.library.${c_function_prefix}SetAttributeViBoolean(self.vi, b'', attribute_id, value)
        errors._handle_error(self.library, self.vi, error_code)

    def getAttributeViBoolean(self, attribute_id):
        value = ctypes.c_ushort(0)
        error_code = self.library.${c_function_prefix}GetAttributeViBoolean(self.vi, None, attribute_id, ctypes.byref(value))
        errors._handle_error(self.library, self.vi, error_code)
        return value.value

