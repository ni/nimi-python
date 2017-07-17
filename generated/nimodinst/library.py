# This file was generated

import platform

from nimodinst import ctypes_library
from nimodinst import errors


def get_library_name():
    try:
        return {'Linux': {'64bit': {'name': 'libnimodinst.so', 'type': 'cdll'}},
                'Windows': {'32bit': {'name': 'nimodinst.dll', 'type': 'windll'},
                            '64bit': {'name': 'nimodinst_64.dll', 'type': 'cdll'}}}[platform.system()][platform.architecture()[0]]['name']
    except KeyError as e:
        raise errors.UnsupportedConfigurationError


def get_library_type():
    try:
        return {'Linux': {'64bit': {'name': 'libnimodinst.so', 'type': 'cdll'}},
                'Windows': {'32bit': {'name': 'nimodinst.dll', 'type': 'windll'},
                            '64bit': {'name': 'nimodinst_64.dll', 'type': 'cdll'}}}[platform.system()][platform.architecture()[0]]['type']
    except KeyError as e:
        raise errors.UnsupportedConfigurationError


def get_library():
    try:
        library = ctypes_library.NimodinstCtypesLibrary(get_library_name(), get_library_type())
    except OSError:
        raise errors.DriverNotInstalledError()

    return library
