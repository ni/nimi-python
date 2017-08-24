# This file was generated

import platform

from nifake import ctypes_library
from nifake import errors


def get_library_name():
    try:
        return {'Linux': {'64bit': {'name': 'libnifake.so', 'type': 'cdll'}},
                'Windows': {'32bit': {'name': 'nifake_32.dll', 'type': 'windll'},
                            '64bit': {'name': 'nifake_64.dll', 'type': 'cdll'}}}[platform.system()][platform.architecture()[0]]['name']
    except KeyError:
        raise errors.UnsupportedConfigurationError


def get_library_type():
    try:
        return {'Linux': {'64bit': {'name': 'libnifake.so', 'type': 'cdll'}},
                'Windows': {'32bit': {'name': 'nifake_32.dll', 'type': 'windll'},
                            '64bit': {'name': 'nifake_64.dll', 'type': 'cdll'}}}[platform.system()][platform.architecture()[0]]['type']
    except KeyError:
        raise errors.UnsupportedConfigurationError


class LibrarySingleton(object):
    instance = None

    def __init__(self):
        if LibrarySingleton.instance is None:
            try:
                LibrarySingleton.instance = ctypes_library.NifakeCtypesLibrary(get_library_name(), get_library_type())
            except OSError:
                raise errors.DriverNotInstalledError()

        self._library = LibrarySingleton.instance

    def get_library(self):
        return self._library


def get_library():
    return LibrarySingleton().get_library()
