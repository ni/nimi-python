#!/usr/bin/python
# This file was generated
<%
functions     = template_parameters['metadata'].functions
attributes    = template_parameters['metadata'].attributes
config        = template_parameters['metadata'].config
types         = template_parameters['types']
%>

import ctypes
import platform
import sys

def get_library_name():
    is_64bits = sys.maxsize > 2**32

% if 'library_linux' in config:
    if platform.system() == "Linux":
        if is_64bits:
            return "${config['library_linux']['64']}"
        else:
            return "${config['library_linux']['32']}"
% endif
% if 'library_mac' in config:
    if platform.system() == "Darwin":
        return "${config['library_mac']['64']}"
% endif
% if 'library_windows' in config:
    if platform.system() == "Windows":
        if is_64bits:
            return "${config['library_windows']['64']}"
        else:
            return "${config['library_windows']['32']}"
% endif


def get_library():
    library = ctypes.CDLL(get_library_name())

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
