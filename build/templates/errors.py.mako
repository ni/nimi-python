${template_parameters['encoding_tag']}
# This file was generated
<%
config            = template_parameters['metadata'].config
grpc_supported    = template_parameters['include_grpc_support']
attributes        = config['attributes']
functions         = config['functions']
extra_errors_used = config['extra_errors_used']

module_name = config['module_name']
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


<%
# All drivers need Error, DriverError, DriverWarning, UnsupportedConfigurationError and DriverNotInstalledError
%>\
class Error(Exception):
    '''Base error class for ${driver_name}'''

    def __init__(self, message):
        super(Error, self).__init__(message)


class DriverError(Error):
    '''An error originating from the ${driver_name} driver'''

    def __init__(self, code, description):
        assert _is_error(code), "Should not raise Error if code is not fatal."
        self.code = code
        self.description = description
        super(DriverError, self).__init__(str(self.code) + ": " + self.description)


class DriverWarning(Warning):
    '''A warning originating from the ${driver_name} driver'''

    def __init__(self, code, description):
        assert _is_warning(code), "Should not create Warning if code is not positive."
        super(DriverWarning, self).__init__('Warning {} occurred.\n\n{}'.format(code, description))


% if grpc_supported:
class RpcError(Error):
    '''An error specific to sessions to the NI gRPC Device Server'''

    def __init__(self, rpc_code, description):
        self.rpc_code = rpc_code
        self.description = description
        try:
            import grpc
            rpc_error = str(grpc.StatusCode(self.rpc_code))
        except Exception:
            rpc_error = str(self.rpc_code)
        super(RpcError, self).__init__(rpc_error + ": " + self.description)


% endif
class UnsupportedConfigurationError(Error):
    '''An error due to using this module in an usupported platform.'''

    def __init__(self):
        super(UnsupportedConfigurationError, self).__init__('System configuration is unsupported: ' + platform.architecture()[0] + ' ' + platform.system())


class DriverNotInstalledError(Error):
    '''An error due to using this module without the driver runtime installed.'''

    def __init__(self):
        super(DriverNotInstalledError, self).__init__('The ${driver_name} runtime could not be loaded. Make sure it is installed and its bitness matches that of your Python interpreter. Please visit http://www.ni.com/downloads/drivers/ to download and install it.')


class DriverTooOldError(Error):
    '''An error due to using this module with an older version of the ${driver_name} driver runtime.'''

    def __init__(self):
        super(DriverTooOldError, self).__init__('A function was not found in the ${driver_name} runtime. Please visit http://www.ni.com/downloads/drivers/ to download a newer version and install it.')


class DriverTooNewError(Error):
    '''An error due to the ${driver_name} driver runtime being too new for this module.'''

    def __init__(self):
        super(DriverTooNewError, self).__init__('The ${driver_name} runtime returned an unexpected value. This can occur if it is too new for the ${module_name} Python module. Upgrade the ${module_name} Python module.')


% if 'InvalidRepeatedCapabilityError' in extra_errors_used:
class InvalidRepeatedCapabilityError(Error):
    '''An error due to an invalid character in a repeated capability'''

    def __init__(self, invalid_character, invalid_string):
        super(InvalidRepeatedCapabilityError, self).__init__('An invalid character ({}) was found in repeated capability string ({})'.format(invalid_character, invalid_string))


% endif
% if 'SelfTestError' in extra_errors_used:
class SelfTestError(Error):
    '''An error due to a failed self-test'''

    def __init__(self, code, msg):
        self.code = code
        self.message = msg
        super(SelfTestError, self).__init__('Self-test failed with code {}: {}'.format(code, msg))


% endif
def handle_error(library_interpreter, code, ignore_warnings, is_error_handling):
    '''handle_error

    Helper function for handling errors returned by ${module_name}.Library.
    It calls back into the LibraryInterpreter to get the corresponding error
    description and raises if necessary.
    '''

    if _is_success(code) or (_is_warning(code) and ignore_warnings):
        return

    if is_error_handling:
        # The caller is in the midst of error handling and an error occurred.
        # Don't try to get the description or we'll start recursing until the stack overflows.
        description = ''
    else:
        description = library_interpreter.get_error_description(code)

    if _is_error(code):
        raise DriverError(code, description)

    assert _is_warning(code)
    warnings.warn(DriverWarning(code, description))
