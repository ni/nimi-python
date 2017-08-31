# This file was generated
<%
import build.helper as helper
config        = template_parameters['metadata'].config

module_name = config['module_name']
%>\

import platform

from ${module_name} import errors
from ${module_name} import library


_instance = None

def _get_library_name():
    try:
        return ${helper.get_dictionary_snippet(config['library_info'], indent=15)}[platform.system()][platform.architecture()[0]]['name']
    except KeyError:
        raise errors.UnsupportedConfigurationError

def _get_library_type():
    try:
        return ${helper.get_dictionary_snippet(config['library_info'], indent=15)}[platform.system()][platform.architecture()[0]]['type']
    except KeyError:
        raise errors.UnsupportedConfigurationError

def get():
    '''get

    Returns the library.Library singleton for ${config['module_name']}.
    '''
    global _instance
    if _instance is None:
        try:
            _instance = library.Library(_get_library_name(), _get_library_type())
        except OSError:
            raise errors.DriverNotInstalledError()

    return _instance

