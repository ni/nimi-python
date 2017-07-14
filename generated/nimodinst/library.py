# This file was generated

import ctypes
import platform

from nimodinst import errors
from nimodinst import ctypes_library

def get_library_name():
    try:
        return {   'Linux': {'64bit': {'name': 'libnimodinst.so', 'type': 'cdll'}},
            'Windows': {   '32bit': {'name': 'nimodinst.dll', 'type': 'windll'},
                           '64bit': {'name': 'nimodinst_64.dll', 'type': 'cdll'}}}[platform.system()][platform.architecture()[0]]['name']
    except KeyError as e:
        raise errors.UnsupportedConfigurationError

def get_library_type():
    try:
        return {   'Linux': {'64bit': {'name': 'libnimodinst.so', 'type': 'cdll'}},
            'Windows': {   '32bit': {'name': 'nimodinst.dll', 'type': 'windll'},
                           '64bit': {'name': 'nimodinst_64.dll', 'type': 'cdll'}}}[platform.system()][platform.architecture()[0]]['type']
    except KeyError as e:
        raise errors.UnsupportedConfigurationError

def get_library():
    try:
        library = ctypes_library.nimodinst_ctypes_library(get_library_name(), get_library_type())
    except OSError as e:
        raise errors.DriverNotInstalledError()

    return library
