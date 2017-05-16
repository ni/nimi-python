import nidmm
from ctypes import *


def _isSuccess(errorCode):
    return (errorCode == 0)


def _isError(errorCode):
    return (errorCode < 0)


def _isWarning(errorCode):
    return (errorCode > 0)


class _ErrorBase(Exception):

    def __init__(self, nidmmLib, sessionHandle, errorCode):

        newErrorCode = c_long(0)
        bufferSize = nidmmLib.niDMM_GetError(sessionHandle, byref(newErrorCode), 0, None)
        assert (newErrorCode.value == errorCode)

        if (bufferSize > 0):
            '''
            Return code > 0 from first call to GetError represents the size of
            the description.  Call it again.
            Ignore incoming IVI error code and return description from the driver
            (trust that the IVI error code was properly stored in the session
            by the driver)
            '''
            errorCode = c_long(errorCode)
            errorMessage = create_string_buffer(bufferSize)
            nidmmLib.niDMM_GetError(sessionHandle, byref(errorCode), bufferSize, errorMessage)
        else:
            '''
            Return code <= 0 from GetError indicates a problem.  This is expected
            when the session is invalid (IVI spec requires GetError to fail).
            Use GetErrorMessage instead.  It doesn't require a session.

            Call niDMM_GetErrorMessage, pass VI_NULL for the buffer in order to retrieve
            the length of the error message.
            '''
            errorCode = bufferSize
            bufferSize = nidmmLib.niDMM_GetErrorMessage(sessionHandle, errorCode, 0, None)
            print("bufferSize", bufferSize)
            errorMessage = create_string_buffer(bufferSize)
            nidmmLib.niDMM_GetErrorMessage(sessionHandle, errorCode, bufferSize, errorMessage)

        #@TODO: By hardcoding encoding "ascii", internationalized strings will throw.
        #       Which encoding should we be using? https://docs.python.org/3/library/codecs.html#standard-encodings
        self.code = errorCode.value
        self.elaboration = errorMessage.raw.decode("ascii")
        super(_ErrorBase, self).__init__(str(self.code) + ": " + self.elaboration)


class Error(_ErrorBase):

    def __init__(self, nidmmLib, sessionHandle, errorCode):
        assert (_isError(errorCode)), "Should not raise Error if errorCode is not fatal."
        super(Error, self).__init__(nidmmLib, sessionHandle, errorCode)


class Warning(_ErrorBase):

    def __init__(self, nidmmLib, sessionHandle, errorCode):
        assert (_isWarning(errorCode)), "Should not raise Warning if errorCode is not positive."
        super(Warning, self).__init__(nidmmLib, sessionHandle, errorCode)


def _handleError(nidmmLib, sessionHandle, errorCode):
    if (_isSuccess(errorCode)):
        return
    if (_isError(errorCode)):
        raise Error(nidmmLib, sessionHandle, errorCode)
    if (_isWarning(errorCode)):
        raise Warning(nidmmLib, sessionHandle, errorCode)

