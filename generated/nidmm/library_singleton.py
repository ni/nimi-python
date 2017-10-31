# This file was generated

import platform

import ctypes
from nidmm import errors
from nidmm import library
import threading


_instance = None
_instance_lock = threading.Lock()


def _get_library_name():
    try:
        return {'Linux': {'64bit': {'name': 'libnidmm.so', 'type': 'cdll'}},
                'Windows': {'32bit': {'name': 'nidmm_32.dll', 'type': 'windll'},
                            '64bit': {'name': 'nidmm_64.dll', 'type': 'cdll'}}}[platform.system()][platform.architecture()[0]]['name']
    except KeyError:  # pragma: no cover
        raise errors.UnsupportedConfigurationError


def _get_library_type():
    try:
        return {'Linux': {'64bit': {'name': 'libnidmm.so', 'type': 'cdll'}},
                'Windows': {'32bit': {'name': 'nidmm_32.dll', 'type': 'windll'},
                            '64bit': {'name': 'nidmm_64.dll', 'type': 'cdll'}}}[platform.system()][platform.architecture()[0]]['type']
    except KeyError:  # pragma: no cover
        raise errors.UnsupportedConfigurationError


def get():
    '''get

    Returns the library.Library singleton for nidmm.
    '''
    global _instance
    global _instance_lock

    with _instance_lock:
        if _instance is None:
            try:
                library_type = _get_library_type()
                if library_type == 'windll':
                    ctypes_library = ctypes.WinDLL(_get_library_name())
                else:  # pragma: no cover
                    assert library_type == 'cdll'
                    ctypes_library = ctypes.CDLL(_get_library_name())
                    _instance = library.Library(ctypes_library)
            except OSError:  # pragma: no cover
                raise errors.DriverNotInstalledError()
        return _instance

