# This file was generated
<%
import helper

functions     = template_parameters['metadata'].functions
attributes    = template_parameters['metadata'].attributes
config        = template_parameters['metadata'].config

module_name = config['module_name']
c_function_prefix = config['c_function_prefix']
driver_name = config['driver_name']

functions = template_parameters['metadata'].functions
functions = helper.extract_codegen_functions(functions)
functions = helper.add_all_metadata(functions)
%>\

import ctypes
import platform
from unittest.mock import DEFAULT

import ${module_name}.ctypes_types
import ${module_name}.python_types

class IncorrectCall(Exception):
    def __init__(self, function):
        self.function = function
        super(Exception, self).__init__("{0} called when it shouldn't have been".format(self.function))

# Helper function to setup Mock object with default side affects and return values
def set_side_effects_and_return_values(mock_library):
% for f in functions:
    mock_library.${c_function_prefix}${f['name']}.side_effect = IncorrectCall("${c_function_prefix}${f['name']}")
    mock_library.${c_function_prefix}${f['name']}.return_value = ${module_name}.python_types.${f['returns_python']}(0)
% endfor




