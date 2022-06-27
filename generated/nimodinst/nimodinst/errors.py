# -*- coding: utf-8 -*-
# This file was generated


import platform
import warnings


def _is_success(code):
    return (code == 0)


def _is_error(code):
    return (code < 0)


def _is_warning(code):
    return (code > 0)


class Error(Exception):
    '''Base error class for NI-ModInst'''

    def __init__(self, message):
        super(Error, self).__init__(message)


class DriverError(Error):
    '''An error originating from the NI-ModInst driver'''

    def __init__(self, code, description):
        assert (_is_error(code)), "Should not raise Error if code is not fatal."
        self.code = code
        self.description = description
        super(DriverError, self).__init__(str(self.code) + ": " + self.description)


class DriverWarning(Warning):
    '''A warning originating from the NI-ModInst driver'''

    def __init__(self, code, description):
        assert (_is_warning(code)), "Should not create Warning if code is not positive."
        super(DriverWarning, self).__init__('Warning {0} occurred.\n\n{1}'.format(code, description))


class UnsupportedConfigurationError(Error):
    '''An error due to using this module in an usupported platform.'''

    def __init__(self):
        super(UnsupportedConfigurationError, self).__init__('System configuration is unsupported: ' + platform.architecture()[0] + ' ' + platform.system())


class DriverNotInstalledError(Error):
    '''An error due to using this module without the driver runtime installed.'''

    def __init__(self):
        super(DriverNotInstalledError, self).__init__('The NI-ModInst runtime could not be loaded. Make sure it is installed and its bitness matches that of your Python interpreter. Please visit http://www.ni.com/downloads/drivers/ to download and install it.')


class DriverTooOldError(Error):
    '''An error due to using this module with an older version of the NI-ModInst driver runtime.'''

    def __init__(self):
        super(DriverTooOldError, self).__init__('A function was not found in the NI-ModInst runtime. Please visit http://www.ni.com/downloads/drivers/ to download a newer version and install it.')


class DriverTooNewError(Error):
    '''An error due to the NI-ModInst driver runtime being too new for this module.'''

    def __init__(self):
        super(DriverTooNewError, self).__init__('The NI-ModInst runtime returned an unexpected value. This can occur if it is too new for the nimodinst Python module. Upgrade the nimodinst Python module.')


def handle_error(session, code, ignore_warnings, is_error_handling):
    '''handle_error

    Helper function for handling errors returned by nimodinst.Library.
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
        raise DriverError(code, description)

    assert _is_warning(code)
    warnings.warn(DriverWarning(code, description))


