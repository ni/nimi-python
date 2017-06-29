# This file was generated
<%
import helper

functions     = template_parameters['metadata'].functions
attributes    = template_parameters['metadata'].attributes
config        = template_parameters['metadata'].config

module_name = config['module_name']
c_function_prefix = config['c_function_prefix']
driver_name = config['driver_name']

functions = template_parameters['metadata'].functions
functions = helper.extract_codegen_functions(functions)
functions = helper.add_all_metadata(functions)
%>\

import ctypes
import platform

from ${module_name} import errors
from ${module_name}.ctypes_types import * # So we can use the types without module
import ${module_name}.python_types

def get_library_name():
    try:
        return ${config['library_info']}[platform.system()][platform.architecture()[0]]['name']
    except KeyError as e:
        raise errors.UnsupportedConfigurationError

def get_library_type():
    try:
        return ${config['library_info']}[platform.system()][platform.architecture()[0]]['type']
    except KeyError as e:
        raise errors.UnsupportedConfigurationError

def get_library():
    try:
        if get_library_type() == 'windll':
            library = ctypes.WinDLL(get_library_name())
        else:
            library = ctypes.CDLL(get_library_name())
    except OSError as e:
        raise errors.DriverNotInstalledError()


    """
    Specify required argument types (function prototypes) and Return types.
    https://docs.python.org/3/library/ctypes.html#specifying-the-required-argument-types-function-prototypes
    https://docs.python.org/3/library/ctypes.html#return-types
    This provides some automatic conversion and error checking when calling ${driver_name} functions.
    """

% for f in functions:
    library.${c_function_prefix}${f['name']}.restype = ${module_name}.python_types.${f['returns_python']}
    library.${c_function_prefix}${f['name']}.argtypes = [${helper.get_library_call_parameter_types_snippet(f['parameters'])}]

% endfor

    return library
