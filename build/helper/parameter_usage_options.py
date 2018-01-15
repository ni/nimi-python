from enum import Enum


class ParameterUsageOptions(Enum):
    '''Different usage options for parameter lists.'''

    SESSION_METHOD_DECLARATION = 1
    '''For declaring a regular method in Session'''
    SESSION_INIT_DECLARATION = 2
    '''For declaring an init method in Session'''
    SESSION_NUMPY_INTO_METHOD_DECLARATION = 3
    '''For calling into a Session method that uses numpy arrays.'''
    SESSION_METHOD_CALL = 4
    '''For calling into a regular Session method.'''
    SESSION_INIT_CALL = 5
    '''For calling into an init Session method.'''
    DOCUMENTATION_SESSION_METHOD = 6
    '''For documentation (rst) of Session methods'''
    CTYPES_CALL = 7
    '''For Library implementation calling into the DLL via ctypes'''
    LIBRARY_METHOD_CALL = 8
    '''For calling into a method in Library.'''
    CTYPES_ARGTYPES = 9
    '''For setting up the ctypes argument types'''
    LIBRARY_METHOD_DECLARATION = 10
    '''For declaring a method in Library'''
    INPUT_PARAMETERS = 11
    '''Get all input parameters, other than self, rep caps, and size'''
    OUTPUT_PARAMETERS = 12
    '''Get all output parameters, other than ivi-dance'''
    IVI_DANCE_PARAMETER = 13
    '''Get the ivi-dance parameter'''
    NUMPY_PARAMETERS = 14
    '''Get all buffer parameters that support numpy.array in the Python API'''
    LEN_PARAMETER = 15
    '''Get the len parameter'''
    INPUT_ENUM_PARAMETERS = 16
    '''Get any input parameters whose type is enum'''



