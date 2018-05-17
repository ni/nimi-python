#!/usr/bin/python
# This file was generated

from nidmm.enums import *          # noqa: F403,F401,H303
from nidmm.errors import DriverWarning   # noqa: F401
from nidmm.errors import Error     # noqa: F401
from nidmm.session import Session  # noqa: F401


python_package_list = 'Python Installed Packages'


def get_diagnostic_information():
    '''Get diagnostic information about the system state that is suitable for printing or logging

    returns: dict
    '''
    import os
    import pip
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
            driver_version_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\National Instruments\NI-DMM\CurrentVersion")
            driver_version = winreg.QueryValueEx(driver_version_key, "Version")[0]
        except WindowsError:
            driver_version = 'Unknown'
    elif platform.system() == 'Linux':
        os_name = 'Linux'
        driver_version = 'Unknown'
    else:
        os_name = 'Unknown'
        driver_version = 'Unknown'

    installed_packages = pip.get_installed_distributions()
    installed_packages_list = sorted(["%s==%s" % (i.key, i.version) for i in installed_packages])

    info['OS Name'] = os_name
    info['OS Version'] = platform.version()
    info['OS Bitness'] = ('64' if is_os_64bit() else '32') + ' (May be incorrect if running in a virtual env)'
    info['Driver Name'] = "NI-DMM"
    info['Driver Version'] = driver_version
    info['Python Package'] = 'nidmm'
    info['Python Package Version'] = "0.8.0"
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
        print((' ' * 12) + p)

    return info


