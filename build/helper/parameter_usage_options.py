from enum import Enum


class ParameterUsageOptions(Enum):
    '''Different usage options for parameter lists.'''

    SESSION_METHOD_DECLARATION = 1
    '''For declaring a method in Session'''
    SESSION_NUMPY_INTO_METHOD_DECLARATION = 2
    '''For calling into a Session method that uses numpy arrays.'''
    SESSION_METHOD_CALL = 3
    '''For calling into a Session method.'''
    DOCUMENTATION_SESSION_METHOD = 4
    '''For documentation (rst) of Session methods'''
    CTYPES_CALL = 5
    '''For Library implementation calling into the DLL via ctypes'''
    LIBRARY_METHOD_CALL = 6
    '''For calling into a method in Library.'''
    CTYPES_ARGTYPES = 7
    '''For setting up the ctypes argument types'''
    LIBRARY_METHOD_DECLARATION = 8
    '''For declaring a method in Library'''
    INPUT_PARAMETERS = 9
    '''Get all input parameters, other than self, rep caps, and size'''
    OUTPUT_PARAMETERS = 10
    '''Get all output parameters, other than ivi-dance'''
    IVI_DANCE_PARAMETER = 11
    '''Get the ivi-dance parameter'''
    NUMPY_PARAMETERS = 12
    '''Get all buffer parameters that support numpy.array in the Python API'''
    LEN_PARAMETER = 13
    '''Get the len parameter'''
    INPUT_ENUM_PARAMETERS = 14
    '''Get any input parameters whose type is enum'''



