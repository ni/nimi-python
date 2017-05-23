import ctypes
from nidmm import errors
from nidmm import library
from nidmm import enums


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


class Session(object):
    """An NI-DMM session to a National Instruments Digital Multimeter"""

    specificDriverClassSpecMajorVersion = AttributeViInt32(1050515)
    specificDriverClassSpecMinorVersion = AttributeViInt32(1050516)
    sampleCount                         = AttributeViInt32(1250301)
    triggerCount                        = AttributeViInt32(1250304)
    range                               = AttributeViReal64(1250002)
    resolutionDigits                    = AttributeViReal64(1250003)
    serialNumber                        = AttributeViString(1150054)
    simulate                            = AttributeViBoolean(1050005)

    def __init__(self, resourceName, idQuery = 0, reset = False):
        #print("__init__ entered")
        self.sessionHandle = ctypes.c_ulong(0)
        self.library = library.getLibrary()
        errorCode = self.library.niDMM_init(resourceName.encode('ascii'), idQuery, reset, ctypes.byref(self.sessionHandle))
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
        #@TODO: Should we raise an exception on double close? Look at what File does.
        if(self.sessionHandle.value != 0):
            errorCode = self.library.niDMM_close(self.sessionHandle)
            if(errorCode < 0):
                #@TODO: This will occur when session is "stolen". Maybe don't even bother with printing?
                print("Failed to close session.")
            self.sesionHandle = ctypes.c_ulong(0)

    def configureMeasurementDigits(self, mode, range, digitsOfResolution):
        if type(mode) is not enums.Function: raise TypeError('Parameter mode must be of type ' + str(enums.Function))
        errorCode = self.library.niDMM_ConfigureMeasurementDigits(self.sessionHandle, mode.value, range, digitsOfResolution)
        errors._handleError(self.library, self.sessionHandle, errorCode)

    def read(self, timeoutInMilliseconds = 10000):
        measurement = ctypes.c_double(0)
        errorCode = self.library.niDMM_Read(self.sessionHandle, timeoutInMilliseconds, ctypes.byref(measurement))
        errors._handleError(self.library, self.sessionHandle, errorCode)
        return measurement.value

    def setAttributeViInt32(self, attributeId, value):
        errorCode = self.library.niDMM_SetAttributeViInt32(self.sessionHandle, b'', attributeId, value)
        errors._handleError(self.library, self.sessionHandle, errorCode)

    def getAttributeViInt32(self, attributeId):
        value = ctypes.c_long(0)
        errorCode = self.library.niDMM_GetAttributeViInt32(self.sessionHandle, None, attributeId, ctypes.byref(value))
        errors._handleError(self.library, self.sessionHandle, errorCode)
        return value.value

    def setAttributeViReal64(self, attributeId, value):
        errorCode = self.library.niDMM_SetAttributeViReal64(self.sessionHandle, b'', attributeId, value)
        errors._handleError(self.library, self.sessionHandle, errorCode)

    def getAttributeViReal64(self, attributeId):
        value = ctypes.c_double(0)
        errorCode = self.library.niDMM_GetAttributeViReal64(self.sessionHandle, None, attributeId, ctypes.byref(value))
        errors._handleError(self.library, self.sessionHandle, errorCode)
        return value.value

    def setAttributeViString(self, attributeId, value):
        errorCode = self.library.niDMM_SetAttributeViString(self.sessionHandle, b'', attributeId, value.encode('ascii'))
        errors._handleError(self.library, self.sessionHandle, errorCode)

    def getAttributeViString(self, attributeId):
        errorCode = self.library.niDMM_GetAttributeViString(self.sessionHandle, None, attributeId, 0, None)
        # Do the IVI dance
        # Don't use _handleError, because positive value in errorCode means size, not warning.
        if(errors._isError(errorCode)): raise errors.Error(self.library, self.sessionHandle, errorCode)
        bufferSize = errorCode
        value = ctypes.create_string_buffer(bufferSize)
        errorCode = self.library.niDMM_GetAttributeViString(self.sessionHandle, None, attributeId, bufferSize, value)
        errors._handleError(self.library, self.sessionHandle, errorCode)
        return value.value.decode("ascii")

    def setAttributeViBoolean(self, attributeId, value):
        errorCode = self.library.niDMM_SetAttributeViBoolean(self.sessionHandle, b'', attributeId, value)
        errors._handleError(self.library, self.sessionHandle, errorCode)

    def getAttributeViBoolean(self, attributeId):
        value = ctypes.c_ushort(0)
        errorCode = self.library.niDMM_GetAttributeViBoolean(self.sessionHandle, None, attributeId, ctypes.byref(value))
        errors._handleError(self.library, self.sessionHandle, errorCode)
        return value.value

