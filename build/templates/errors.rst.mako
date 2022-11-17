<%
    import build.helper as helper

    config = template_parameters['metadata'].config
    module_name = config['module_name']
    driver_name = config['driver_name']
    enums = config['enums']
    extra_errors_used = config['extra_errors_used']
    grpc_supported = template_parameters['include_grpc_support']
%>\
${helper.get_rst_header_snippet('Exceptions and Warnings', '=')}

${helper.get_rst_header_snippet('Error', '-')}

    .. py:currentmodule:: ${module_name}.errors

    .. exception:: Error

        Base exception type that all ${driver_name} exceptions derive from


${helper.get_rst_header_snippet('DriverError', '-')}

    .. py:currentmodule:: ${module_name}.errors

    .. exception:: DriverError

        An error originating from the ${driver_name} driver


${helper.get_rst_header_snippet('UnsupportedConfigurationError', '-')}

    .. py:currentmodule:: ${module_name}.errors

    .. exception:: UnsupportedConfigurationError

        An error due to using this module in an usupported platform.

${helper.get_rst_header_snippet('DriverNotInstalledError', '-')}

    .. py:currentmodule:: ${module_name}.errors

    .. exception:: DriverNotInstalledError

        An error due to using this module without the driver runtime installed.

${helper.get_rst_header_snippet('DriverTooOldError', '-')}

    .. py:currentmodule:: ${module_name}.errors

    .. exception:: DriverTooOldError

        An error due to using this module with an older version of the ${driver_name} driver runtime.

${helper.get_rst_header_snippet('DriverTooNewError', '-')}

    .. py:currentmodule:: ${module_name}.errors

    .. exception:: DriverTooNewError

        An error due to the ${driver_name} driver runtime being too new for this module.

% if 'InvalidRepeatedCapabilityError' in extra_errors_used:
${helper.get_rst_header_snippet('InvalidRepeatedCapabilityError', '-')}

    .. py:currentmodule:: ${module_name}.errors

    .. exception:: InvalidRepeatedCapabilityError

        An error due to an invalid character in a repeated capability


% endif
% if 'SelfTestError' in extra_errors_used:
${helper.get_rst_header_snippet('SelfTestError', '-')}

    .. py:currentmodule:: ${module_name}.errors

    .. exception:: SelfTestError

        An error due to a failed self-test


% endif
% if grpc_supported:
${helper.get_rst_header_snippet('RpcError', '-')}

    .. py:currentmodule:: ${module_name}.errors

    .. exception:: RpcError

        An error specific to gRPC sessions


% endif
${helper.get_rst_header_snippet('DriverWarning', '-')}

    .. py:currentmodule:: ${module_name}.errors

    .. exception:: DriverWarning

        A warning originating from the ${driver_name} driver



