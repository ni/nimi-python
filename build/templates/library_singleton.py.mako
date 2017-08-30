# This file was generated
<%
import build.helper as helper
config        = template_parameters['metadata'].config

module_name = config['module_name']
%>\

import platform

from ${module_name} import library
from ${module_name} import errors


class LibrarySingleton(object):

    _instance = None

    def _get_library_name():
        try:
            return ${helper.get_dictionary_snippet(config['library_info'], indent=19)}[platform.system()][platform.architecture()[0]]['name']
        except KeyError:
            raise errors.UnsupportedConfigurationError

    def _get_library_type():
        try:
            return ${helper.get_dictionary_snippet(config['library_info'], indent=19)}[platform.system()][platform.architecture()[0]]['type']
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

