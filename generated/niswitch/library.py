# This file was generated

import platform

from niswitch import ctypes_library
from niswitch import errors


def get_library_name():
    try:
        return {'Linux': {'64bit': {'name': 'libniswitch.so', 'type': 'cdll'}},
                'Windows': {'32bit': {'name': 'niswitch_32.dll', 'type': 'windll'},
                            '64bit': {'name': 'niswitch_64.dll', 'type': 'cdll'}}}[platform.system()][platform.architecture()[0]]['name']
    except KeyError:
        raise errors.UnsupportedConfigurationError


def get_library_type():
    try:
        return {'Linux': {'64bit': {'name': 'libniswitch.so', 'type': 'cdll'}},
                'Windows': {'32bit': {'name': 'niswitch_32.dll', 'type': 'windll'},
                            '64bit': {'name': 'niswitch_64.dll', 'type': 'cdll'}}}[platform.system()][platform.architecture()[0]]['type']
    except KeyError:
        raise errors.UnsupportedConfigurationError


class LibrarySingleton(object):
    instance = None

    def __init__(self):
        if LibrarySingleton.instance is None:
            try:
                LibrarySingleton.instance = ctypes_library.NiswitchCtypesLibrary(get_library_name(), get_library_type())
            except OSError:
                raise errors.DriverNotInstalledError()

        self._library = LibrarySingleton.instance

    def get_library(self):
        return self._library


def get_library():
    return LibrarySingleton().get_library()
