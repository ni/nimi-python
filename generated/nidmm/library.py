# This file was generated

import platform

from nidmm import ctypes_library
from nidmm import errors


def get_library_name():
    try:
        return {'Linux': {'64bit': {'name': 'libnidmm.so', 'type': 'cdll'}},
                'Windows': {'32bit': {'name': 'nidmm_32.dll', 'type': 'windll'},
                            '64bit': {'name': 'nidmm_64.dll', 'type': 'cdll'}}}[platform.system()][platform.architecture()[0]]['name']
    except KeyError:
        raise errors.UnsupportedConfigurationError


def get_library_type():
    try:
        return {'Linux': {'64bit': {'name': 'libnidmm.so', 'type': 'cdll'}},
                'Windows': {'32bit': {'name': 'nidmm_32.dll', 'type': 'windll'},
                            '64bit': {'name': 'nidmm_64.dll', 'type': 'cdll'}}}[platform.system()][platform.architecture()[0]]['type']
    except KeyError:
        raise errors.UnsupportedConfigurationError


def get_library():
    try:
        library = ctypes_library.NidmmCtypesLibrary(get_library_name(), get_library_type())
    except OSError:
        raise errors.DriverNotInstalledError()

    return library
