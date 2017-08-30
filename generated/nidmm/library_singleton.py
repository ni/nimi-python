# This file was generated

import platform

from nidmm import library
from nidmm import errors


class LibrarySingleton(object):

    _instance = None

    def _get_library_name():
        try:
            return {'Linux': {'64bit': {'name': 'libnidmm.so', 'type': 'cdll'}},
                    'Windows': {'32bit': {'name': 'nidmm_32.dll', 'type': 'windll'},
                                '64bit': {'name': 'nidmm_64.dll', 'type': 'cdll'}}}[platform.system()][platform.architecture()[0]]['name']
        except KeyError:
            raise errors.UnsupportedConfigurationError

    def _get_library_type():
        try:
            return {'Linux': {'64bit': {'name': 'libnidmm.so', 'type': 'cdll'}},
                    'Windows': {'32bit': {'name': 'nidmm_32.dll', 'type': 'windll'},
                                '64bit': {'name': 'nidmm_64.dll', 'type': 'cdll'}}}[platform.system()][platform.architecture()[0]]['type']
        except KeyError:
            raise errors.UnsupportedConfigurationError

    def __init__(self):
        if LibrarySingleton._instance is None:
            try:
                LibrarySingleton._instance = library.Library(LibrarySingleton._get_library_name(), LibrarySingleton._get_library_type())
            except OSError:
                raise errors.DriverNotInstalledError()

        self._library = LibrarySingleton._instance

    def get(self):
        return self._library

