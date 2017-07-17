# This file was generated

import ctypes
import platform

from nidmm import errors
from nidmm import ctypes_library

def get_library_name():
    try:
        return {   'Linux': {'64bit': {'name': 'libnidmm.so', 'type': 'cdll'}},
            'Windows': {   '32bit': {'name': 'nidmm_32.dll', 'type': 'windll'},
                           '64bit': {'name': 'nidmm_64.dll', 'type': 'cdll'}}}[platform.system()][platform.architecture()[0]]['name']
    except KeyError as e:
        raise errors.UnsupportedConfigurationError

def get_library_type():
    try:
        return {   'Linux': {'64bit': {'name': 'libnidmm.so', 'type': 'cdll'}},
            'Windows': {   '32bit': {'name': 'nidmm_32.dll', 'type': 'windll'},
                           '64bit': {'name': 'nidmm_64.dll', 'type': 'cdll'}}}[platform.system()][platform.architecture()[0]]['type']
    except KeyError as e:
        raise errors.UnsupportedConfigurationError

def get_library():
    try:
        library = ctypes_library.nidmm_ctypes_library(get_library_name(), get_library_type())
    except OSError as e:
        raise errors.DriverNotInstalledError()

    return library
