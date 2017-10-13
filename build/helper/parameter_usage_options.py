from enum import Enum


class ParameterUsageOptions(Enum):
    '''Different usage options for parameter lists.'''

    SESSION_METHOD_DECLARATION = 1
    '''For declaring a method in Session'''
    SESSION_METHOD_CALL = 2
    '''For calling into a Session method.'''
    DOCUMENTATION_SESSION_METHOD = 3
    '''For documentation (rst) of Session methods'''
    CTYPES_CALL = 4
    '''For Library implementation calling into the DLL via ctypes'''
    LIBRARY_METHOD_CALL = 5
    '''For calling into a method in Library.'''
    CTYPES_ARGTYPES = 6
    '''For setting up the ctypes argument types'''
    LIBRARY_METHOD_DECLARATION = 7
    '''For declaring a method in Library'''
    INPUT_PARAMETERS = 8
    '''Get all input parameters, other than self, rep caps, and size'''
    OUTPUT_PARAMETERS = 9
    '''Get all output parameters, other than ivi-dance'''
    IVI_DANCE_PARAMETER = 10
    '''Get the ivi-dance parameter'''
    LEN_PARAMETER = 11
    '''Get the len parameter'''
    INPUT_ENUM_PARAMETERS = 12
    '''Get any input parameters whose type is enum'''



