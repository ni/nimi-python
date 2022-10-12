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
    '''For declaring a Session method that uses numpy arrays.'''
    LIBRARY_INTERPRETER_NUMPY_INTO_METHOD_DECLARATION = ()
    '''For declaring a LibraryInterpreter method that uses numpy arrays.'''
    LIBRARY_INTERPRETER_NUMPY_INTO_METHOD_CALL = ()
    '''For calling into a LibraryInterpreter method (from Session) that uses numpy arrays.'''
    SESSION_METHOD_CALL = ()
    '''For calling into a regular Session method.'''
    SESSION_INIT_CALL = ()
    '''For calling into an init Session method.'''
    DOCUMENTATION_SESSION_METHOD = ()
    '''For documentation (rst) of Session methods'''
    LIBRARY_METHOD_DECLARATION = ()
    '''For declaring a Library method.'''
    CDLL_METHOD_CALL = ()
    '''For calling into a CDLL method (from Library).'''
    LIBRARY_METHOD_CALL = ()
    '''For calling into a Library method (from LibraryInterpreter).'''
    LIBRARY_INTERPRETER_METHOD_CALL = ()
    '''For calling into a LibraryInterpreter method (from Session).'''
    GRPC_REQUEST_PARAMETERS = ()
    '''For creating a gRPC Request object.'''
    CTYPES_ARGTYPES = ()
    '''For setting up the ctypes argument types'''
    LIBRARY_INTERPRETER_METHOD_DECLARATION = ()
    '''For declaring a LibraryInterpreter method.'''
    INPUT_PARAMETERS = ()
    '''Get all input parameters, other than self, rep caps, and size'''
    LIBRARY_OUTPUT_PARAMETERS = ()
    '''Get all output parameters, other than ivi-dance'''
    API_OUTPUT_PARAMETERS = ()
    '''We also want to skip size parameters'''
    API_NUMPY_OUTPUT_PARAMETERS = ()
    '''Output parameters for numpy function'''
    GRPC_OUTPUT_PARAMETERS = ()
    '''Get all gRPC output parameters'''
    IVI_DANCE_PARAMETER = ()
    '''Get the ivi-dance parameter'''
    NUMPY_PARAMETERS = ()
    '''Get all buffer parameters that support numpy.array in the Python API'''
    LEN_PARAMETER = ()
    '''Get the len parameter'''
    INPUT_ENUM_PARAMETERS = ()
    '''Get any input parameters whose type is enum'''
