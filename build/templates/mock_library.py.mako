#!/usr/bin/python
# This file was generated
<%
functions     = template_parameters['metadata'].functions
attributes    = template_parameters['metadata'].attributes
config        = template_parameters['metadata'].config
types         = template_parameters['types']

module_name = config['module_name']
c_function_prefix = config['c_function_prefix']
driver_name = config['driver_name']
%>

import ctypes
import pprint
from ctypes import *
pp = pprint.PrettyPrinter(indent=4)

def ${c_function_prefix}_InitWithOptions_side_effect(resource, id_query, reset, option_string, session_handle):
    session_handle.contents.value = 42

def set_side_effects_and_return_values(mock_library):
  mock_library.${c_function_prefix}InitWithOptions.side_effect = ${c_function_prefix}_InitWithOptions_side_effect
  mock_library.${c_function_prefix}InitWithOptions.return_value = 0

  mock_library.${c_function_prefix}ConfigureMeasurementDigits.return_value = 0

  mock_library.${c_function_prefix}close.return_value = 0

class mock_library():
    def ${c_function_prefix}InitWithOptions(self, resourceName, idQuery, reset, optionString, session_handle):
        print('resourceName = %s' % resourceName)
        print('idQuery %s' % idQuery)
        print('reset %s' % reset)
        print('optionString %s' % optionString)
        print('session_handle %s' % pp.pformat(cast(session_handle, ctypes.POINTER(c_ulong))[0]))
        ulong_p = cast(session_handle, ctypes.POINTER(c_ulong))
        ulong_p[0] = 42
        return 0

    def ${c_function_prefix}ConfigureMeasurementDigits(self, vi, mode, range, digits_of_resolution):
        print('vi = %s' % vi)
        print('mode %s' % mode)
        print('range %s' % range)
        print('digits_of_resolution %s' % digits_of_resolution)
        return 0

    def ${c_function_prefix}close(self, vi):
        print('vi = %s' % vi)
        return 0





