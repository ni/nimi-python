#!/usr/bin/python
# This file was generated
<%
enums = template_parameters['metadata'].enums
config = template_parameters['metadata'].config
module_name = config['module_name']
%>
% if len(enums) > 0:
from ${module_name}.enums import *          # noqa: F403,F401,H303
% endif
from ${module_name}.errors import DriverWarning   # noqa: F401
from ${module_name}.errors import Error     # noqa: F401
from ${module_name}.session import Session  # noqa: F401
<%
 # Blank lines are to make each import separate so that they do not need to be sorted
 # Otherwise flake8 test fails
%>\
% for c in config['custom_types']:

from ${module_name}.${c['file_name']} import ${c['python_name']}  # noqa: F401

from ${module_name}.${c['file_name']} import ${c['ctypes_type']}  # noqa: F401
% endfor


python_package_list = 'Python Installed Packages'


def get_diagnostic_information():
    '''Get diagnostic information about the system state that is suitable for printing or logging

    returns: dict
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
    if platform.system() == 'Windows':
        try:
            import winreg as winreg
        except ImportError:
            import _winreg as winreg

        os_name = 'Windows'
        try:
            driver_version_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\National Instruments\${config['driver_name']}\CurrentVersion")
            driver_version = winreg.QueryValueEx(driver_version_key, "Version")[0]
        except WindowsError:
            driver_version = 'Unknown'
    elif platform.system() == 'Linux':
        os_name = 'Linux'
        driver_version = 'Unknown'
    else:
        os_name = 'Unknown'
        driver_version = 'Unknown'

    installed_packages = pkg_resources.working_set
    installed_packages_list = [{'name': i.key, 'version': i.version, } for i in installed_packages]

    info['OS Name'] = os_name
    info['OS Version'] = platform.version()
    info['OS Bitness'] = ('64' if is_os_64bit() else '32') + ' (May be incorrect if running in a virtual env)'
    info['Driver Name'] = "${config['driver_name']}"
    info['Driver Version'] = driver_version
    info['Python Package'] = '${module_name}'
    info['Python Package Version'] = "${config['module_version']}"
    info['Python Version'] = sys.version
    info['Python Bitness'] = '64' if is_python_64bit() else '32'
    info['Python Virtual Env'] = 'Yes' if is_venv() else 'No'
    info[python_package_list] = installed_packages_list

    return info


def print_diagnostic_information():
    '''Print diagnostic information in a format suitable for issue report'''
    info = get_diagnostic_information()

    row_format = '{:<25}: {}'
    for key in sorted(info):
        if key != python_package_list:  # We are going to format this one special
            print(row_format.format(key, info[key]))
    print(python_package_list + ':')
    for p in info[python_package_list]:
        print((' ' * 12) + p['name'] + '==' + p['version'])

    return info


