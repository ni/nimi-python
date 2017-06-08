import ctypes
import nidmm
import platform


def _is_success(error_code):
    return (error_code == 0)


def _is_error(error_code):
    return (error_code < 0)


def _is_warning(error_code):
    return (error_code > 0)


class _ErrorBase(Exception):

    def __init__(self, library, session_handle, error_code):

        new_error_code = ctypes.c_long(0)
        buffer_size = library.niDMM_GetError(session_handle, ctypes.byref(new_error_code), 0, None)
        assert (new_error_code.value == error_code)

        if (buffer_size > 0):
            '''
            Return code > 0 from first call to GetError represents the size of
            the description.  Call it again.
            Ignore incoming IVI error code and return description from the driver
            (trust that the IVI error code was properly stored in the session
            by the driver)
            '''
            error_code = ctypes.c_long(error_code)
            error_message = ctypes.create_string_buffer(buffer_size)
            library.niDMM_GetError(session_handle, ctypes.byref(error_code), buffer_size, error_message)
        else:
            '''
            Return code <= 0 from GetError indicates a problem.  This is expected
            when the session is invalid (IVI spec requires GetError to fail).
            Use GetErrorMessage instead.  It doesn't require a session.

            Call niDMM_GetErrorMessage, pass VI_NULL for the buffer in order to retrieve
            the length of the error message.
            '''
            error_code = buffer_size
            buffer_size = library.niDMM_GetErrorMessage(session_handle, error_code, 0, None)
            print("buffer_size", buffer_size)
            error_message = ctypes.create_string_buffer(buffer_size)
            library.niDMM_GetErrorMessage(session_handle, error_code, buffer_size, error_message)

        #@TODO: By hardcoding encoding "ascii", internationalized strings will throw.
        #       Which encoding should we be using? https://docs.python.org/3/library/codecs.html#standard-encodings
        self.code = error_code.value
        self.elaboration = error_message.value.decode("ascii")
        super(_ErrorBase, self).__init__(str(self.code) + ": " + self.elaboration)


class Error(_ErrorBase):
    '''An error originating from the NI-DMM driver'''

    def __init__(self, library, session_handle, error_code):
        assert (_is_error(error_code)), "Should not raise Error if error_code is not fatal."
        super(Error, self).__init__(library, session_handle, error_code)


class Warning(_ErrorBase):
    '''A warning originating from the NI-DMM driver'''

    def __init__(self, library, session_handle, error_code):
        assert (_is_warning(error_code)), "Should not raise Warning if error_code is not positive."
        super(Warning, self).__init__(library, session_handle, error_code)


class UnsupportedConfigurationError(Exception):
    '''An error due to using this module in an usupported platform.'''

    def __init__(self):
        super(UnsupportedConfigurationError, self).__init__('System configuration is unsupported: ' + platform.architecture()[0] + ' ' + platform.system())


class DriverNotInstalledError(Exception):
    '''An error due to using this module without the driver runtime installed.'''

    def __init__(self):
        super(DriverNotInstalledError, self).__init__('The NI-DMM runtime is not installed. Please visit http://www.ni.com/downloads/drivers/ to download and install it.')


def _handle_error(library, session_handle, error_code):
    if (_is_success(error_code)):
        return
    if (_is_error(error_code)):
        raise Error(library, session_handle, error_code)
    if (_is_warning(error_code)):
        raise Warning(library, session_handle, error_code)

