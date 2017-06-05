<%
    module_name = config = templateParameters['config']['module_name']
    c_function_prefix = config = templateParameters['config']['c_function_prefix']
    attributes = templateParameters['attributes']

    def snakecase_to_camelcase(snake_string):
        """Converts a C-style SNAKE_CASE string to camelCase"""
        components = snake_string.split('_')
        return components[0].lower() + "".join(component.title() for component in components[1:])
%>
# This file was generated

import ctypes
from ${module_name} import errors
from ${module_name} import library
from ${module_name} import enums


class AttributeViInt32(object):

    def __init__(self, attributeId):
        self.attributeId = attributeId

    def __get__(self, obj, objtype):
        assert objtype is Session
        return obj.getAttributeViInt32(self.attributeId)

    def __set__(self, obj, value):
        obj.setAttributeViInt32(self.attributeId, value)


class AttributeViReal64(object):

    def __init__(self, attributeId):
        self.attributeId = attributeId

    def __get__(self, obj, objtype):
        assert objtype is Session
        return obj.getAttributeViReal64(self.attributeId)

    def __set__(self, obj, value):
        obj.setAttributeViReal64(self.attributeId, value)


class AttributeViString(object):

    def __init__(self, attributeId):
        self.attributeId = attributeId

    def __get__(self, obj, objtype):
        assert objtype is Session
        return obj.getAttributeViString(self.attributeId)

    def __set__(self, obj, value):
        obj.setAttributeViString(self.attributeId, value)


class AttributeViBoolean(object):

    def __init__(self, attributeId):
        self.attributeId = attributeId

    def __get__(self, obj, objtype):
        assert objtype is Session
        return obj.getAttributeViBoolean(self.attributeId) is not 0

    def __set__(self, obj, value):
        obj.setAttributeViBoolean(self.attributeId, (value is not 0))


class AttributeEnum(object):

    def __init__(self, attributeId, enumMetaClass):
        self.attributeId = attributeId
        self.attributeType = enumMetaClass

    def __get__(self, obj, objtype):
        assert objtype is Session
        return self.attributeType(obj.getAttributeViInt32(self.attributeId))

    def __set__(self, obj, value):
        if type(value) is not self.attributeType: raise TypeError('Value mode must be of type ' + str(self.attributeType))
        obj.setAttributeViInt32(self.attributeId, value.value)


class AttributeViSession(object):

    def __init__(self, attributeId):
        self.attributeId = attributeId

    def __get__(self, obj, objtype):
        raise TypeError('Attributes of type ViSession are unsupported in Python')

    def __set__(self, obj, value):
        raise TypeError('Attributes of type ViSession are unsupported in Python')


class Session(object):
    """${templateParameters['config']['session_description']}"""

% for attribute in attributes:
    %if attributes[attribute]['enum']:
    ${snakecase_to_camelcase(attribute)} = AttributeEnum(${attributes[attribute]['id']}, enums.${attributes[attribute]['enum']})
    %else:
    ${snakecase_to_camelcase(attribute)} = Attribute${attributes[attribute]['type']}(${attributes[attribute]['id']})
    %endif
% endfor

    def __init__(self, resourceName, idQuery = 0, reset = False):
        #print("__init__ entered")
        self.sessionHandle = ctypes.c_ulong(0)
        self.library = library.getLibrary()
        errorCode = self.library.${c_function_prefix}init(resourceName.encode('ascii'), idQuery, reset, ctypes.byref(self.sessionHandle))
        errors._handleError(self.library, self.sessionHandle, errorCode)

    def __del__(self):
        #print("__del__ entered")
        pass

    def __enter__(self):
        #print("__enter__ entered")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        #print("__exit__ entered")
        self.close()

    def close(self):
        # TODO(marcoskirsch): Should we raise an exception on double close? Look at what File does.
        if(self.sessionHandle.value != 0):
            errorCode = self.library.${c_function_prefix}close(self.sessionHandle)
            if(errorCode < 0):
                # TODO(marcoskirsch): This will occur when session is "stolen". Maybe don't even bother with printing?
                print("Failed to close session.")
            self.sesionHandle = ctypes.c_ulong(0)

    def configureMeasurementDigits(self, mode, range, digitsOfResolution):
        if type(mode) is not enums.Function: raise TypeError('Parameter mode must be of type ' + str(enums.Function))
        errorCode = self.library.${c_function_prefix}ConfigureMeasurementDigits(self.sessionHandle, mode.value, range, digitsOfResolution)
        errors._handleError(self.library, self.sessionHandle, errorCode)

    def read(self, timeoutInMilliseconds = 10000):
        measurement = ctypes.c_double(0)
        errorCode = self.library.${c_function_prefix}Read(self.sessionHandle, timeoutInMilliseconds, ctypes.byref(measurement))
        errors._handleError(self.library, self.sessionHandle, errorCode)
        return measurement.value

    def setAttributeViInt32(self, attributeId, value):
        errorCode = self.library.${c_function_prefix}SetAttributeViInt32(self.sessionHandle, b'', attributeId, value)
        errors._handleError(self.library, self.sessionHandle, errorCode)

    def getAttributeViInt32(self, attributeId):
        value = ctypes.c_long(0)
        errorCode = self.library.${c_function_prefix}GetAttributeViInt32(self.sessionHandle, None, attributeId, ctypes.byref(value))
        errors._handleError(self.library, self.sessionHandle, errorCode)
        return value.value

    def setAttributeViReal64(self, attributeId, value):
        errorCode = self.library.${c_function_prefix}SetAttributeViReal64(self.sessionHandle, b'', attributeId, value)
        errors._handleError(self.library, self.sessionHandle, errorCode)

    def getAttributeViReal64(self, attributeId):
        value = ctypes.c_double(0)
        errorCode = self.library.${c_function_prefix}GetAttributeViReal64(self.sessionHandle, None, attributeId, ctypes.byref(value))
        errors._handleError(self.library, self.sessionHandle, errorCode)
        return value.value

    def setAttributeViString(self, attributeId, value):
        errorCode = self.library.${c_function_prefix}SetAttributeViString(self.sessionHandle, b'', attributeId, value.encode('ascii'))
        errors._handleError(self.library, self.sessionHandle, errorCode)

    def getAttributeViString(self, attributeId):
        errorCode = self.library.${c_function_prefix}GetAttributeViString(self.sessionHandle, None, attributeId, 0, None)
        # Do the IVI dance
        # Don't use _handleError, because positive value in errorCode means size, not warning.
        if(errors._isError(errorCode)): raise errors.Error(self.library, self.sessionHandle, errorCode)
        bufferSize = errorCode
        value = ctypes.create_string_buffer(bufferSize)
        errorCode = self.library.${c_function_prefix}GetAttributeViString(self.sessionHandle, None, attributeId, bufferSize, value)
        errors._handleError(self.library, self.sessionHandle, errorCode)
        return value.value.decode("ascii")

    def setAttributeViBoolean(self, attributeId, value):
        errorCode = self.library.${c_function_prefix}SetAttributeViBoolean(self.sessionHandle, b'', attributeId, value)
        errors._handleError(self.library, self.sessionHandle, errorCode)

    def getAttributeViBoolean(self, attributeId):
        value = ctypes.c_ushort(0)
        errorCode = self.library.${c_function_prefix}GetAttributeViBoolean(self.sessionHandle, None, attributeId, ctypes.byref(value))
        errors._handleError(self.library, self.sessionHandle, errorCode)
        return value.value

