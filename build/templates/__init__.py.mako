${template_parameters['encoding_tag']}
# This file was generated
<%
import build.helper as helper

enums = template_parameters['metadata'].enums
functions = helper.filter_codegen_functions(template_parameters['metadata'].functions)
config = template_parameters['metadata'].config
module_name = config['module_name']
registry_name = config['driver_registry'] if 'driver_registry' in config else config['driver_name']
%>

__version__ = '${config['module_version']}'

% if len(enums) > 0:
from ${module_name}.enums import *  # noqa: F403,F401,H303
% endif
from ${module_name}.errors import DriverWarning  # noqa: F401
from ${module_name}.errors import Error  # noqa: F401
<%
# nitclk is different. It does not have a Session class that we open a session on
# Instead it is a bunch of stateless function calls. So if we are NOT building for
# nitclk, we import the Session class. If it is nitclk then we will
# import each function and the SessionReference class
%>\
% if config['module_name'] == 'nitclk':
from ${module_name}.session import SessionReference  # noqa: F401

# Function imports
<%
# There two types of functions in `nitclk`:
#
# 1. Functions that take a single SessionReference (get/set attribute)
# 2. Functions that take in a list of SessionReference
#
# The second type are the public functions that clients will call, so we need to import them explicitly into
# the `nitclk` namespace. We are using the `render_in_session_base` metadata in order to distinguish them
%>\
%   for func_name in sorted([functions[k]['python_name'] for k in functions if not functions[k]['render_in_session_base']]):
from ${module_name}.session import ${func_name}  # noqa: F401
%   endfor
% else:
from ${module_name}.session import Session  # noqa: F401
% endif
<%
 # Blank lines are to make each import separate so that they do not need to be sorted
 # Otherwise flake8 test fails
%>\
% for c in config['custom_types']:

from ${module_name}.${c['file_name']} import ${c['python_name']}  # noqa: F401

from ${module_name}.${c['file_name']} import ${c['ctypes_type']}  # noqa: F401
% endfor


def get_diagnostic_information():
    '''Get diagnostic information about the system state that is suitable for printing or logging

    returns: dict

    note: Python bitness may be incorrect when running in a virtual environment
    '''
    import os
    import pkg_resources
    import platform
    import struct
    import sys

    def is_python_64bit():
        return (struct.calcsize("P") == 8)

    def is_os_64bit():
        return platform.machine().endswith('64')

    def is_venv():
        return 'VIRTUAL_ENV' in os.environ

    info = {}
    info['os'] = {}
    info['python'] = {}
    info['driver'] = {}
    info['module'] = {}
    if platform.system() == 'Windows':
        try:
            import winreg as winreg
        except ImportError:
            import _winreg as winreg

        os_name = 'Windows'
        try:
            driver_version_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\National Instruments\${registry_name}\CurrentVersion")
            driver_version = winreg.QueryValueEx(driver_version_key, "Version")[0]
        except WindowsError:
            driver_version = 'Unknown'
    elif platform.system() == 'Linux':
        os_name = 'Linux'
        driver_version = 'Unknown'
    else:
        raise SystemError('Unsupported platform: {}'.format(platform.system()))

    installed_packages = pkg_resources.working_set
    installed_packages_list = [{'name': i.key, 'version': i.version, } for i in installed_packages]

    info['os']['name'] = os_name
    info['os']['version'] = platform.version()
    info['os']['bits'] = '64' if is_os_64bit() else '32'
    info['driver']['name'] = "${config['driver_name']}"
    info['driver']['version'] = driver_version
    info['module']['name'] = '${module_name}'
    info['module']['version'] = "${config['module_version']}"
    info['python']['version'] = sys.version
    info['python']['bits'] = '64' if is_python_64bit() else '32'
    info['python']['is_venv'] = is_venv()
    info['python']['packages'] = installed_packages_list

    return info


def print_diagnostic_information():
    '''Print diagnostic information in a format suitable for issue report

    note: Python bitness may be incorrect when running in a virtual environment
    '''
    info = get_diagnostic_information()

    row_format = '    {:<10} {}'
    for type in ['OS', 'Driver', 'Module', 'Python']:
        typename = type.lower()
        print(type + ':')
        for item in info[typename]:
            if item != 'packages':
                print(row_format.format(item.title() + ':', info[typename][item]))
    print('    Installed Packages:')
    for p in info['python']['packages']:
        print((' ' * 8) + p['name'] + '==' + p['version'])

    return info


