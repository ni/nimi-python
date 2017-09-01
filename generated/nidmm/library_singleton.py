# This file was generated

import platform

from nidmm import errors
from nidmm import library


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


def get():
    '''get

    Returns the library.Library singleton for nidmm.
    '''
    global _instance
    if _instance is None:
        try:
            _instance = library.Library(_get_library_name(), _get_library_type())
        except OSError:
            raise errors.DriverNotInstalledError()
    return _instance

