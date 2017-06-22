# This file was generated
<%
functions     = template_parameters['metadata'].functions
attributes    = template_parameters['metadata'].attributes
config        = template_parameters['metadata'].config
types         = template_parameters['types']

module_name = config['module_name']
c_function_prefix = config['c_function_prefix']
driver_name = config['driver_name']
%>\

import ctypes
import platform

from ${module_name} import errors
from ${module_name} import ctypes_library


def get_library_name():
    try:
        return ${config['library_name']}[platform.system()][platform.architecture()[0]]
    except KeyError as e:
        raise errors.UnsupportedConfigurationError


def get_library():
    try:
        library = ctypes_library.${module_name}_ctypes_library(get_library_name())
    except OSError as e:
        raise errors.DriverNotInstalledError()

    return library
