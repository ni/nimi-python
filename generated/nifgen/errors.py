#!/usr/bin/python
# This file was generated


import platform
import warnings


def _is_success(code):
    return (code == 0)


def _is_error(code):
    return (code < 0)


def _is_warning(code):
    return (code > 0)


class _ErrorBase(Exception):

    def __init__(self, code, description):

        self.code = code
        self.description = description
        super(_ErrorBase, self).__init__(str(self.code) + ": " + self.description)


class Error(_ErrorBase):
    '''An error originating from the NI-FGEN driver'''

    def __init__(self, code, description):
        assert (_is_error(code)), "Should not raise Error if code is not fatal."
        super(Error, self).__init__(code, description)


class NifgenWarning(Warning):
    '''A warning originating from the NI-FGEN driver'''

    def __init__(self, code, description):
        assert (_is_warning(code)), "Should not create Warning if code is not positive."
        super(NifgenWarning, self).__init__('Warning {0} occurred.\n\n{1}'.format(code, description))


class UnsupportedConfigurationError(Exception):
    '''An error due to using this module in an usupported platform.'''

    def __init__(self):
        super(UnsupportedConfigurationError, self).__init__('System configuration is unsupported: ' + platform.architecture()[0] + ' ' + platform.system())


class DriverNotInstalledError(Exception):
    '''An error due to using this module without the driver runtime installed.'''

    def __init__(self):
        super(DriverNotInstalledError, self).__init__('The NI-FGEN runtime is not installed. Please visit http://www.ni.com/downloads/drivers/ to download and install it.')


def handle_error(session, code, ignore_warnings, is_error_handling):
    '''handle_error

    Helper function for handling errors returned by nifgen.Library.
    It calls back into the session to get the corresponding error description
    and raises if necessary.
    '''

    if _is_success(code) or (_is_warning(code) and ignore_warnings):
        return

    if is_error_handling:
        # The caller is in the midst of error handling and an error occurred.
        # Don't try to get the description or we'll start recursing until the stack overflows.
        description = ''
    else:
        description = session._get_error_description(code)

    if _is_error(code):
        raise Error(code, description)

    assert _is_warning(code)
    warnings.warn(NifgenWarning(code, description))


warnings.filterwarnings("always", category=NifgenWarning)
