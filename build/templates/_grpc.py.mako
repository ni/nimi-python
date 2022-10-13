${template_parameters['encoding_tag']}
# This file was generated
<%
import build.helper as helper

config = template_parameters['metadata'].config
module_name = config['module_name']
service_class_prefix = config['grpc_service_class_prefix']
functions = helper.filter_library_functions(config['functions'])
%>\

import grpc
import hightime  # noqa: F401
import threading
import warnings

% if config['enums']:
from . import enums as enums
% endif
from . import errors as errors
from . import ${module_name}_pb2 as grpc_types
from . import ${module_name}_pb2_grpc as grpc_library
% for c in config['custom_types']:

from . import ${c['file_name']} as ${c['file_name']}  # noqa: F401
% endfor


class LibraryInterpreter(object):
    '''LibraryInterpreter

    Wrapper around driver grpc library.
    '''

    def __init__(self, grpc_channel):
        self._lock = threading.RLock()
        self._client = grpc_library.${service_class_prefix}Stub(grpc_channel)
        self._${config['session_handle_parameter_name']} = 0

    def _invoke(self, func, request):
        grpc_error = None
        try:
            response = func(request)
            error_code = response.status
            error_message = ''
        except grpc.RpcError as rpc_error:
            error_code = None
            error_message = rpc_error.details()
            for entry in rpc_error.trailing_metadata() or []:
                if entry.key == 'ni-error':
                    value = entry.value if isinstance(entry.value, str) else entry.value.decode('utf-8')
                    try:
                        error_code = int(value)
                    except ValueError:
                        error_message += f'\nError status: {value}'
            grpc_error = rpc_error.code()

        if grpc_error == grpc.StatusCode.UNAVAILABLE:
            error_message = 'Failed to connect to server'
        elif grpc_error == grpc.StatusCode.UNIMPLEMENTED:
            error_message = (
                'The operation is not implemented or is not supported/enabled in this service'
            )
        elif grpc_error == grpc.StatusCode.NOT_FOUND:
            raise errors.DriverTooOldError()

        if grpc_error == grpc.StatusCode.INVALID_ARGUMENT:
            raise ValueError(error_message)
        elif error_code is None:
            raise errors.Error(error_message)
        elif error_code < 0:
            raise errors.DriverError(error_code, error_message)
        elif error_code > 0:
            if not error_message:
                try:
                    error_message = self.error_message(error_code)
                except errors.Error:
                    error_message = 'Failed to retrieve error description.'
            warnings.warn(errors.DriverWarning(error_code, error_message))
        return response

% for func_name in sorted(functions):
% for method_template in functions[func_name]['method_templates']:
% if method_template['library_interpreter_filename'] != '/none':
<%include file="${'/_grpc.py' + method_template['library_interpreter_filename'] + '.py.mako'}" args="f=functions[func_name], config=config, method_template=method_template" />\
% endif
% endfor
% endfor
