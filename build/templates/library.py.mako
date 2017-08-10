# This file was generated
<%
import build.helper as helper
config        = template_parameters['metadata'].config

module_name = config['module_name']
%>\

import platform

from ${module_name} import ctypes_library
from ${module_name} import errors


def get_library_name():
    try:
        return ${helper.get_dictionary_snippet(config['library_info'], indent=15)}[platform.system()][platform.architecture()[0]]['name']
    except KeyError:
        raise errors.UnsupportedConfigurationError


def get_library_type():
    try:
        return ${helper.get_dictionary_snippet(config['library_info'], indent=15)}[platform.system()][platform.architecture()[0]]['type']
    except KeyError:
        raise errors.UnsupportedConfigurationError


class LibrarySingleton(object):
    instance = None

    def __init__(self):
        if LibrarySingleton.instance is None:
            try:
                LibrarySingleton.instance = ctypes_library.${module_name.title()}CtypesLibrary(get_library_name(), get_library_type())
            except OSError:
                raise errors.DriverNotInstalledError()

        self._library = LibrarySingleton.instance

    def get_library(self):
        return self._library


def get_library():
    return LibrarySingleton().get_library()
