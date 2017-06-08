#!/usr/bin/python
# This file was generated
<%
functions     = template_parameters['metadata'].functions
attributes    = template_parameters['metadata'].attributes
config        = template_parameters['metadata'].config
types         = template_parameters['types']
%>

import ctypes
from nidmm import errors
import platform


def get_library_name():
    try:
        return ${config['library_name']}[platform.system()][platform.architecture()[0]]
    except KeyError as e:
        raise errors.UnsupportedConfigurationError


def get_library():
    try:
        library = ctypes.CDLL(get_library_name())
    except OSError as e:
        raise errors.DriverNotInstalledError()


    """ Specify required argument types (function prototypes) and Return types.
        https://docs.python.org/3/library/ctypes.html#specifying-the-required-argument-types-function-prototypes
        https://docs.python.org/3/library/ctypes.html#return-types
        This provides some automatic conversion and error checking when calling NI-DMM functions.
        Strictly speaking, this is not necessary if/when we code-generate the calling code.
        It may have some performance impact as well.
    """
% for f in functions:
<%
    param_types = ""
    for p in f['parameters']:
        if len(param_types) > 0:
            param_types += ", "
        if p['direction'] == 'out':
            param_types += "ctypes.POINTER(" + "ctypes." + types[p['type']] + ")"
        else:
            param_types += "ctypes." + types[p['type']]
%>
    library.${config['c_function_prefix']}${f['name']}.restype = ctypes.${types[f['returns']]}
    library.${config['c_function_prefix']}${f['name']}.argtypes = [${param_types}]
% endfor

    return library
