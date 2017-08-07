#!/usr/bin/python
# This file was generated
<%
config        = template_parameters['metadata'].config
attributes    = config['attributes']
functions     = config['functions']

module_name = config['module_name']
c_function_prefix = config['c_function_prefix']
driver_name = config['driver_name']
%>

import platform


def _is_success(error_code):
    return (error_code == 0)


def _is_error(error_code):
    return (error_code < 0)


def _is_warning(error_code):
    return (error_code > 0)


class _ErrorBase(Exception):

    def __init__(self, session, error_code):

        self.code, self.description = session._get_error_description(error_code)
        super(_ErrorBase, self).__init__(str(self.code) + ": " + self.description)


class Error(_ErrorBase):
    '''An error originating from the ${driver_name} driver'''

    def __init__(self, session, error_code):
        assert (_is_error(error_code)), "Should not raise Error if error_code is not fatal."
        super(Error, self).__init__(session, error_code)


class Warning(_ErrorBase):
    '''A warning originating from the ${driver_name} driver'''

    def __init__(self, session, error_code):
        assert (_is_warning(error_code)), "Should not raise Warning if error_code is not positive."
        super(Warning, self).__init__(session, error_code)


class UnsupportedConfigurationError(Exception):
    '''An error due to using this module in an usupported platform.'''

    def __init__(self):
        super(UnsupportedConfigurationError, self).__init__('System configuration is unsupported: ' + platform.architecture()[0] + ' ' + platform.system())


class DriverNotInstalledError(Exception):
    '''An error due to using this module without the driver runtime installed.'''

    def __init__(self):
        super(DriverNotInstalledError, self).__init__('The ${driver_name} runtime is not installed. Please visit http://www.ni.com/downloads/drivers/ to download and install it.')


def _handle_error(session, error_code):
    if (_is_success(error_code)):
        return
    if (_is_error(error_code)):
        raise Error(session, error_code)
    if (_is_warning(error_code)):
        raise Warning(session, error_code)
