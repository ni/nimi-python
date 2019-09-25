from enum import Enum


class AutoNumber(Enum):
    def __new__(cls):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj


class ParameterUsageOptions(AutoNumber):
    '''Different usage options for parameter lists.'''

    SESSION_METHOD_DECLARATION = ()
    '''For declaring a regular method in Session'''
    SESSION_METHOD_PASSTHROUGH_CALL = ()
    '''Same as SESSION_METHOD_DECLARATION but without default values - For calling into Session using parameters of the same name and order that are simply passed through'''
    SESSION_INIT_DECLARATION = ()
    '''For declaring an init method in Session'''
    SESSION_NUMPY_INTO_METHOD_DECLARATION = ()
    '''For calling into a Session method that uses numpy arrays.'''
    SESSION_METHOD_CALL = ()
    '''For calling into a regular Session method.'''
    SESSION_INIT_CALL = ()
    '''For calling into an init Session method.'''
    DOCUMENTATION_SESSION_METHOD = ()
    '''For documentation (rst) of Session methods'''
    CTYPES_CALL = ()
    '''For Library implementation calling into the DLL via ctypes'''
    LIBRARY_METHOD_CALL = ()
    '''For calling into a method in Library.'''
    CTYPES_ARGTYPES = ()
    '''For setting up the ctypes argument types'''
    LIBRARY_METHOD_DECLARATION = ()
    '''For declaring a method in Library'''
    INPUT_PARAMETERS = ()
    '''Get all input parameters, other than self, rep caps, and size'''
    OUTPUT_PARAMETERS = ()
    '''Get all output parameters, other than ivi-dance'''
    OUTPUT_PARAMETERS_FOR_DOCS = ()
    '''We also want to skip size parameters'''
    IVI_DANCE_PARAMETER = ()
    '''Get the ivi-dance parameter'''
    NUMPY_PARAMETERS = ()
    '''Get all buffer parameters that support numpy.array in the Python API'''
    LEN_PARAMETER = ()
    '''Get the len parameter'''
    INPUT_ENUM_PARAMETERS = ()
    '''Get any input parameters whose type is enum'''



