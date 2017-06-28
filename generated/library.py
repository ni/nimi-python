# This file was generated

import ctypes
import platform

from nidmm import errors
from nidmm import ctypes_library

def get_library_name():
    try:
        return {'Windows': {'32bit': 'nidmm_32.dll', '64bit': 'nidmm_64.dll'}, 'Linux': {'64bit': 'libnidmm.so'}}[platform.system()][platform.architecture()[0]]
    except KeyError as e:
        raise errors.UnsupportedConfigurationError


def get_library():
    try:
        library = ctypes_library.nidmm_ctypes_library(get_library_name())
    except OSError as e:
        raise errors.DriverNotInstalledError()

    return library
