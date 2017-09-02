#!/usr/bin/python
# This file was generated


import platform


def _is_success(error_code):
    return (error_code == 0)


def _is_error(error_code):
    return (error_code < 0)


def _is_warning(error_code):
    return (error_code > 0)


class _ErrorBase(Exception):

    def __init__(self, error_code, error_description):

        self.code = error_code
        self.description = error_description
        super(_ErrorBase, self).__init__(str(self.code) + ": " + self.description)


class Error(_ErrorBase):
    '''An error originating from the NI-DMM driver'''

    def __init__(self, error_code, error_description):
        assert (_is_error(error_code)), "Should not raise Error if error_code is not fatal."
        super(Error, self).__init__(error_code, error_description)


class Warning(_ErrorBase):
    '''A warning originating from the NI-DMM driver'''

    def __init__(self, error_code, error_description):
        assert (_is_warning(error_code)), "Should not raise Warning if error_code is not positive."
        super(Warning, self).__init__(error_code, error_description)


class UnsupportedConfigurationError(Exception):
    '''An error due to using this module in an usupported platform.'''

    def __init__(self):
        super(UnsupportedConfigurationError, self).__init__('System configuration is unsupported: ' + platform.architecture()[0] + ' ' + platform.system())


class DriverNotInstalledError(Exception):
    '''An error due to using this module without the driver runtime installed.'''

    def __init__(self):
        super(DriverNotInstalledError, self).__init__('The NI-DMM runtime is not installed. Please visit http://www.ni.com/downloads/drivers/ to download and install it.')


def handle_error(session, error_code, ignore_warnings):
    if _is_success(error_code) or (_is_warning(error_code) and ignore_warnings):
        return
    try:
        error_description = session.get_error_description(error_code)
    except Exception as e:
        # TODO(marcoskirsch): Log this exception.
        error_description = ""
    if (_is_error(error_code)):
        raise Error(error_code, error_description)
    if (_is_warning(error_code)):
        # TODO(marcoskirsch): Log instead of raising in the warning case.
        raise Warning(error_code, error_description)
