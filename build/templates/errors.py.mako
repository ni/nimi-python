#!/usr/bin/python
# This file was generated
<%
config        = template_parameters['metadata'].config
attributes    = config['attributes']
functions     = config['functions']

module_name = config['module_name']
module_name_class = module_name.title()
c_function_prefix = config['c_function_prefix']
driver_name = config['driver_name']
%>

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
    '''An error originating from the ${driver_name} driver'''

    def __init__(self, code, description):
        assert (_is_error(code)), "Should not raise Error if code is not fatal."
        super(Error, self).__init__(code, description)


class ${module_name_class}Warning(Warning):
    '''A warning originating from the ${driver_name} driver'''

    def __init__(self, code, description):
        assert (_is_warning(code)), "Should not create Warning if code is not positive."
        super(${module_name_class}Warning, self).__init__('Warning {0} occurred.\n\n{1}'.format(code, description))


class UnsupportedConfigurationError(Exception):
    '''An error due to using this module in an usupported platform.'''

    def __init__(self):
        super(UnsupportedConfigurationError, self).__init__('System configuration is unsupported: ' + platform.architecture()[0] + ' ' + platform.system())


class DriverNotInstalledError(Exception):
    '''An error due to using this module without the driver runtime installed.'''

    def __init__(self):
        super(DriverNotInstalledError, self).__init__('The ${driver_name} runtime is not installed. Please visit http://www.ni.com/downloads/drivers/ to download and install it.')


def handle_error(session, code, ignore_warnings):
    if _is_success(code) or (_is_warning(code) and ignore_warnings):
        return
    try:
        description = session.get_error_description(code)
    except Exception as e:
        # TODO(marcoskirsch): Log this exception.
        description = ""
    if (_is_error(code)):
        raise Error(code, description)
    if (_is_warning(code)):
        warnings.warn(${module_name_class}Warning(code, description))


warnings.filterwarnings("always", category=${module_name_class}Warning)
