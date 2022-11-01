${template_parameters['encoding_tag']}
# This file was generated
<%
import build.helper as helper

config = template_parameters['metadata'].config
attributes = config['attributes']

module_name = config['module_name']
c_function_prefix = config['c_function_prefix']
driver_name = config['driver_name']

functions = config['functions']
functions = helper.filter_codegen_functions(functions)
%>\

import array
import ctypes
import hightime  # noqa: F401
import ${module_name}._library_singleton as _library_singleton
import ${module_name}._visatype as _visatype
% if config['enums']:
import ${module_name}.enums as enums  # noqa: F401
% endif
import ${module_name}.errors as errors
% for c in config['custom_types']:

import ${module_name}.${c['file_name']} as ${c['file_name']}  # noqa: F401
% endfor


# Helper functions for creating ctypes needed for calling into the driver DLL
def _get_ctypes_pointer_for_buffer(value=None, library_type=None, size=None):
    if isinstance(value, array.array):
        assert library_type is not None, 'library_type is required for array.array'
        addr, _ = value.buffer_info()
        return ctypes.cast(addr, ctypes.POINTER(library_type))
    elif str(type(value)).find("'numpy.ndarray'") != -1:
        import numpy
        return numpy.ctypeslib.as_ctypes(value)
    elif isinstance(value, bytes):
        return ctypes.cast(value, ctypes.POINTER(library_type))
    elif isinstance(value, list):
        assert library_type is not None, 'library_type is required for list'
        return (library_type * len(value))(*value)
    else:
        if library_type is not None and size is not None:
            return (library_type * size)()
        else:
            return None


def _convert_to_array(value, array_type):
    if value is not None:
        if isinstance(value, array.array):
            value_array = value
        else:
            value_array = array.array(array_type, value)
    else:
        value_array = None

    return value_array


class LibraryInterpreter(object):
    '''Library C<->Python interpreter.

    This class is responsible for interpreting the Library's C API. It is responsible for:
    * Converting ctypes to native Python types.
    * Dealing with string encoding.
    * Allocating memory.
    * Converting errors returned by Library into Python exceptions.
    '''

    def __init__(self, encoding):
        self._encoding = encoding
        self._library = _library_singleton.get()
        # Initialize _${config['session_handle_parameter_name']} to 0 for now.
        # Session will directly update it once the driver runtime init function has been called and
        # we have a valid session handle.
        self._set_session_handle()

    def _set_session_handle(self, value=0):
        self._${config['session_handle_parameter_name']} = value

    def _get_session_handle(self):
        return self._${config['session_handle_parameter_name']}

<%include file="/_library_interpreter.py/_get_error_description.py.mako" args="config=config" />\
% for func_name in sorted(functions):
% for method_template in functions[func_name]['method_templates']:
% if method_template['library_interpreter_filename'] != '/none':
<%include file="${'/_library_interpreter.py' + method_template['library_interpreter_filename'] + '.py.mako'}" args="f=functions[func_name], config=config, method_template=method_template" />\
% endif
% endfor
% endfor
