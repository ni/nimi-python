# This file was generated
<%
config        = template_parameters['metadata'].config

module_name = config['module_name']
%>\

import platform

from ${module_name} import ctypes_library
from ${module_name} import errors


def get_library_name():
    try:
        return ${config['library_info']}[platform.system()][platform.architecture()[0]]['name']
    except KeyError:
        raise errors.UnsupportedConfigurationError


def get_library_type():
    try:
        return ${config['library_info']}[platform.system()][platform.architecture()[0]]['type']
    except KeyError:
        raise errors.UnsupportedConfigurationError


def get_library():
    try:
        library = ctypes_library.${module_name.title()}CtypesLibrary(get_library_name(), get_library_type())
    except OSError:
        raise errors.DriverNotInstalledError()

    return library
