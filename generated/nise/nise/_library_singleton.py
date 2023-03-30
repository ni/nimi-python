# -*- coding: utf-8 -*-
# This file was generated

import platform

import ctypes
import ctypes.util
import nise._library as _library
import nise.errors as errors
import threading


_instance = None
_instance_lock = threading.Lock()
_library_info = {'Linux': {'64bit': {'name': 'nise', 'type': 'cdll'}},
                 'Windows': {'32bit': {'name': 'nise.dll', 'type': 'windll'},
                             '64bit': {'name': 'nise.dll', 'type': 'cdll'}}}


def _get_library_name():
    try:
        return ctypes.util.find_library(_library_info[platform.system()][platform.architecture()[0]]['name'])  # We find and return full path to the DLL
    except KeyError:
        raise errors.UnsupportedConfigurationError


def _get_library_type():
    try:
        return _library_info[platform.system()][platform.architecture()[0]]['type']
    except KeyError:
        raise errors.UnsupportedConfigurationError


def get():
    '''get

    Returns the library.Library singleton for nise.
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
                raise errors.DriverNotInstalledError()
            _instance = _library.Library(ctypes_library)
            try:
                runtime_env_ctype = ctypes.create_string_buffer(platform.python_implementation().encode('windows-1251'))  # case C010
                version_ctype = ctypes.create_string_buffer(platform.python_version().encode('windows-1251'))  # case C010
                reserved_ctype = ctypes.create_string_buffer(''.encode('windows-1251'))  # case C010
                _instance.niSE_SetRuntimeEnvironment(
                    runtime_env_ctype,
                    version_ctype,
                    reserved_ctype,
                    reserved_ctype
                )
            except errors.DriverTooOldError:
                pass
        return _instance

