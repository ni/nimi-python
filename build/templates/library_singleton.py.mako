# This file was generated
<%
import build.helper as helper
config        = template_parameters['metadata'].config

module_name = config['module_name']
%>\

import platform

import ctypes
from ${module_name} import errors
from ${module_name} import library
import threading


_instance = None
_instance_lock = threading.Lock()


def _get_library_name():
    try:
        return ${helper.get_dictionary_snippet(config['library_info'], indent=15)}[platform.system()][platform.architecture()[0]]['name']
    except KeyError:  # pragma: no cover
        raise errors.UnsupportedConfigurationError


def _get_library_type():
    try:
        return ${helper.get_dictionary_snippet(config['library_info'], indent=15)}[platform.system()][platform.architecture()[0]]['type']
    except KeyError:  # pragma: no cover
        raise errors.UnsupportedConfigurationError


def get():
    '''get

    Returns the library.Library singleton for ${config['module_name']}.
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

