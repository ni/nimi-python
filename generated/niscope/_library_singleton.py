# This file was generated

import platform

import ctypes
import niscope._library as _library
import niscope.errors as _errors
import threading


_instance = None
_instance_lock = threading.Lock()
_library_info = {'Linux': {'64bit': {'name': 'libniScope_64.so', 'type': 'cdll'}},
                 'Windows': {'32bit': {'name': 'niscope_32.dll', 'type': 'windll'},
                             '64bit': {'name': 'niscope_64.dll', 'type': 'cdll'}}}


def _get_library_name():
    try:
        return _library_info[platform.system()][platform.architecture()[0]]['name']
    except KeyError:
        raise _errors.UnsupportedConfigurationError


def _get_library_type():
    try:
        return _library_info[platform.system()][platform.architecture()[0]]['type']
    except KeyError:
        raise _errors.UnsupportedConfigurationError


def get():
    '''get

    Returns the library.Library singleton for niscope.
    '''
    global _instance
    global _instance_lock

    with _instance_lock:
        if _instance is None:
            try:
                library_type = _get_library_type()
                if library_type == 'windll':
                    ctypes_library = ctypes.WinDLL(_get_library_name())
                else:
                    assert library_type == 'cdll'
                    ctypes_library = ctypes.CDLL(_get_library_name())
            except OSError:
                raise _errors.DriverNotInstalledError()
            _instance = _library.Library(ctypes_library)
        return _instance

