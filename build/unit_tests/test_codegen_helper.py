from build.helper.codegen_helper import *
from build.helper.codegen_helper import _get_buffer_parameters_for_size_parameter

# We need a config object for our testing
config_for_testing = {
    'session_handle_parameter_name': 'vi',
    'module_name': 'nifake',
    'functions': {},
    'attributes': {},
    'modules': {
        'metadata.enums_addon': {}
    },
    'custom_types': [
        {'file_name': 'custom_struct', 'python_name': 'CustomStruct', 'ctypes_type': 'custom_struct', },
    ],
}


# We also need some function parameters that cover all cases.
parameters_for_testing = [
    {  # 0
        'ctypes_method_call_snippet': 'vi_ctype',
        'ctypes_type': 'ViSession',
        'ctypes_type_library_call': 'ViSession',
        'ctypes_variable_name': 'vi_ctype',
        'direction': 'in',
        'documentation': {'description': 'Identifies a particular instrument session.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'vi',
        'is_buffer': False,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': True,
        'interpreter_method_call_snippet': 'self._vi',
        'name': 'vi',
        'python_name': 'vi',
        'python_name_with_default': 'vi',
        'python_name_with_doc_default': 'vi',
        'python_type': 'int',
        'size': {'mechanism': 'fixed', 'value': 1},
        'type': 'ViSession',
        'numpy': False,
        'use_in_python_api': True,
    },
    {  # 1
        'ctypes_method_call_snippet': 'ctypes.pointer(output_ctype)',
        'ctypes_type': 'ViInt64',
        'ctypes_type_library_call': 'ctypes.POINTER(ViInt64)',
        'ctypes_variable_name': 'output_ctype',
        'direction': 'out',
        'documentation': {'description': 'A big number on its way out.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'output',
        'is_buffer': False,
        'is_string': False,
        'use_array': False,
        'use_list': False,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'output',
        'name': 'output',
        'python_name': 'output',
        'python_name_with_default': 'output',
        'python_name_with_doc_default': 'output',
        'python_type': 'int',
        'size': {'mechanism': 'fixed', 'value': 1},
        'type': 'ViInt64',
        'numpy': False,
        'use_in_python_api': True,
    },
    {  # 2
        'ctypes_method_call_snippet': 'error_message_ctype',
        'ctypes_type': 'ViString',
        'ctypes_type_library_call': 'ViString',
        'ctypes_variable_name': 'error_message_ctype',
        'direction': 'out',
        'documentation': {'description': 'The error information formatted into a string.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'error_message',
        'is_buffer': False,
        'use_array': False,
        'use_list': False,
        'is_string': True,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'error_message',
        'name': 'errorMessage',
        'python_name': 'error_message',
        'python_name_with_default': 'error_message',
        'python_name_with_doc_default': 'error_message',
        'python_type': 'str',
        'size': {'mechanism': 'fixed', 'value': 256},
        'type': 'ViString',
        'numpy': False,
        'use_in_python_api': True,
    },
    {  # 3
        'ctypes_method_call_snippet': 'array_out_ctype',
        'ctypes_type': 'custom_struct',
        'ctypes_type_library_call': 'ctypes.POINTER(custom_struct)',
        'ctypes_variable_name': 'array_out_ctype',
        'direction': 'out',
        'documentation': {'description': 'Array of custom type using python-code size mechanism'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'array_out',
        'is_buffer': True,
        'use_array': False,
        'use_list': True,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'array_out',
        'name': 'arrayOut',
        'original_type': 'custom_struct[]',
        'python_name': 'array_out',
        'python_name_with_default': 'array_out',
        'python_name_with_doc_default': 'array_out',
        'python_type': 'CustomStruct',
        'size': {'mechanism': 'python-code', 'value': 'self.get_array_size_for_python_code()'},
        'type': 'custom_struct',
        'numpy': False,
        'use_in_python_api': True,
    },
    {  # 4
        'ctypes_method_call_snippet': 'number_of_elements_ctype',
        'ctypes_type': 'ViInt32',
        'ctypes_type_library_call': 'ViInt32',
        'ctypes_variable_name': 'number_of_elements_ctype',
        'direction': 'in',
        'documentation': {'description': 'Number of elements in the array.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'number_of_elements',
        'is_buffer': False,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'number_of_elements',
        'name': 'numberOfElements',
        'python_name': 'number_of_elements',
        'python_name_with_default': 'number_of_elements',
        'python_name_with_doc_default': 'number_of_elements',
        'python_type': 'int',
        'size': {'mechanism': 'fixed', 'value': 1},
        'type': 'ViInt32',
        'numpy': False,
        'use_in_python_api': True,
    },
    {  # 5
        'ctypes_method_call_snippet': 'an_array_ctype',
        'ctypes_type': 'ViInt16',
        'ctypes_type_library_call': 'ctypes.POINTER(ViInt16)',
        'ctypes_variable_name': 'an_array_ctype',
        'direction': 'out',
        'documentation': {'description': 'Contains an array of enums, stored as 16 bit integers under the hood '},
        'enum': 'Turtle',
        'grpc_enum': 'Turtle',
        'grpc_name': 'an_array_raw',
        'is_buffer': True,
        'use_array': False,
        'use_list': True,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'an_array',
        'name': 'anArray',
        'python_name': 'an_array',
        'python_name_with_default': 'an_array',
        'python_name_with_doc_default': 'an_array',
        'python_type': 'enums.Turtle',
        'size': {'mechanism': 'passed-in', 'value': 'numberOfElements'},
        'type': 'ViInt16',
        'numpy': False,
        'use_in_python_api': True,
    },
    {  # 6
        'ctypes_method_call_snippet': 'an_int_enum_ctype',
        'ctypes_type': 'ViInt16',
        'ctypes_type_library_call': 'ViInt16',
        'ctypes_variable_name': 'an_int_enum_ctype',
        'direction': 'in',
        'documentation': {
            'description': 'Indicates a ninja turtle',
            'table_body': [['0', 'Leonardo'], ['1', 'Donatello'], ['2', 'Raphael'], ['3', 'Mich elangelo']]
        },
        'enum': 'Turtle',
        'grpc_enum': 'Turtle',
        'grpc_name': 'an_int_enum_raw',
        'is_buffer': False,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'an_int_enum',
        'name': 'anIntEnum',
        'python_name': 'an_int_enum',
        'python_name_with_default': 'an_int_enum',
        'python_name_with_doc_default': 'an_int_enum',
        'python_type': 'enums.Turtle',
        'size': {'mechanism': 'fixed', 'value': 1},
        'type': 'ViInt16',
        'numpy': False,
        'use_in_python_api': True,
    },
    {  # 7
        'ctypes_method_call_snippet': 'ctypes.pointer(output_ctype)',
        'ctypes_type': 'ViInt64',
        'ctypes_type_library_call': 'ctypes.POINTER(ViInt64)',
        'ctypes_variable_name': 'output_ctype',
        'direction': 'out',
        'documentation': {'description': 'A big number on its way out.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'output',
        'is_buffer': True,
        'use_array': True,
        'use_list': False,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'output',
        'name': 'output',
        'python_name': 'output',
        'python_name_with_default': 'output',
        'python_name_with_doc_default': 'output',
        'python_type': 'int',
        'size': {'mechanism': 'passed-in', 'value': 'numberOfElements'},
        'type': 'ViInt64',
        'numpy': True,
        'numpy_type': 'int64',
        'numpy_type_library_call': 'numpy.int64',
        'use_in_python_api': True,
    },
    {  # 8
        'ctypes_method_call_snippet': 'number_of_elements_python_code_ctype',
        'ctypes_type': 'ViInt32',
        'ctypes_type_library_call': 'ViInt32',
        'ctypes_variable_name': 'number_of_elements_python_code_ctype',
        'direction': 'in',
        'documentation': {'description': 'Number of elements in the array, determined via mechanism python-code.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'number_of_elements_python_code',
        'is_buffer': False,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'number_of_elements_python_code',
        'name': 'numberOfElementsPythonCode',
        'numpy': False,
        'python_name': 'number_of_elements_python_code',
        'python_name_with_default': 'number_of_elements_python_code',
        'python_name_with_doc_default': 'number_of_elements_python_code',
        'python_type': 'int',
        'size': {'mechanism': 'python-code', 'value': 'self.get_array_size_for_python_code()'},
        'type': 'ViInt32',
        'use_in_python_api': True,
    },
    {  # 9
        'ctypes_method_call_snippet': 'input_ctype',
        'ctypes_type': 'ViInt16',
        'ctypes_type_library_call': 'ViInt16',
        'ctypes_variable_name': 'input_ctype',
        'direction': 'in',
        'documentation': {'description': 'An input value.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'input',
        'is_buffer': False,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'input',
        'name': 'input',
        'numpy': False,
        'python_name': 'input',
        'python_name_with_default': 'input',
        'python_name_with_doc_default': 'input',
        'python_type': 'int',
        'size': {'mechanism': 'fixed', 'value': 1},
        'type': 'ViInt16',
        'use_in_python_api': True,
    },
    {  # 10
        'ctypes_method_call_snippet': 'input_array_ctype',
        'ctypes_type': 'ViReal64',
        'ctypes_type_library_call': 'ctypes.POINTER(ViReal64)',
        'ctypes_variable_name': 'input_array_ctype',
        'default_value': None,
        'direction': 'in',
        'documentation': {'description': 'Input array of floats'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'input_array',
        'is_buffer': True,
        'is_string': False,
        'use_array': True,
        'use_list': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'input_array',
        'name': 'inputArray',
        'numpy': False,
        'python_name': 'input_array',
        'python_name_with_default': 'input_array=None',
        'python_name_with_doc_default': 'input_array=None',
        'python_type': 'float',
        'size': {'mechanism': 'len', 'value': 'inputArraySize'},
        'type': 'ViReal64',
        'use_in_python_api': True,
    },
    {  # 11
        'ctypes_method_call_snippet': 'input_array_size_ctype',
        'ctypes_type': 'ViInt32',
        'ctypes_type_library_call': 'ViInt32',
        'ctypes_variable_name': 'input_array_size_ctype',
        'direction': 'in',
        'documentation': {'description': 'Size of inputArray'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'input_array_size',
        'is_buffer': False,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'input_array_size',
        'name': 'inputArraySize',
        'numpy': False,
        'python_name': 'input_array_size',
        'python_name_with_default': 'input_array_size',
        'python_name_with_doc_default': 'input_array_size',
        'python_type': 'int',
        'size': {'mechanism': 'fixed', 'value': 1},
        'type': 'ViInt32',
        'use_in_python_api': True,
    },
    {  # 12
        'ctypes_method_call_snippet': 'string_size_ctype',
        'ctypes_type': 'ViInt32',
        'ctypes_type_library_call': 'ViInt32',
        'ctypes_variable_name': 'string_size_ctype',
        'direction': 'in',
        'documentation': {'description': 'Number of bytes allocated for aString'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'string_size',
        'is_buffer': False,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'string_size',
        'name': 'stringSize',
        'numpy': False,
        'python_name': 'string_size',
        'python_name_with_default': 'string_size',
        'python_name_with_doc_default': 'string_size',
        'python_type': 'int',
        'size': {'mechanism': 'fixed', 'value': 1},
        'type': 'ViInt32',
        'use_in_python_api': True,
    },
    {  # 13
        'ctypes_method_call_snippet': 'a_string_ctype',
        'ctypes_type': 'ViString',
        'ctypes_type_library_call': 'ctypes.POINTER(ViChar)',
        'ctypes_variable_name': 'a_string_ctype',
        'direction': 'out',
        'documentation': {'description': 'An IVI dance string.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'a_string',
        'is_buffer': False,
        'is_string': True,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'a_string',
        'name': 'aString',
        'numpy': False,
        'python_name': 'a_string',
        'python_name_with_default': 'a_string',
        'python_name_with_doc_default': 'a_string',
        'python_type': 'str',
        'size': {'mechanism': 'ivi-dance', 'value': 'stringSize'},
        'type': 'ViString',
        'use_in_python_api': True,
    },
    {  # 14
        'ctypes_method_call_snippet': 'timeout_ctype',
        'ctypes_type': 'ViReal64',
        'ctypes_type_library_call': 'ViReal64',
        'ctypes_variable_name': 'timeout_ctype',
        'default_value': 1.0,
        'direction': 'in',
        'documentation': {'description': 'Timeout in seconds'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'timeout',
        'is_buffer': False,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'timeout',
        'name': 'Timeout',
        'numpy': False,
        'python_name': 'timeout',
        'python_name_with_default': 'timeout=1.0',
        'python_name_with_doc_default': 'timeout=1.0',
        'python_type': 'float',
        'size': {'mechanism': 'fixed', 'value': 1},
        'type': 'ViReal64',
        'use_in_python_api': True,
        'python_api_converter_name': 'timedelta_converter_seconds_real64',
    },
    {  # 15
        'ctypes_method_call_snippet': 'channel_list_ctype',
        'ctypes_type': 'ViString',
        'ctypes_type_library_call': 'ViString',
        'ctypes_variable_name': 'channel_list_ctype',
        'direction': 'in',
        'documentation': {
            'description': 'The channel to configure. For more information, refer to `Channel String'
        },
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'channel_list',
        'is_buffer': False,
        'is_string': True,
        'is_repeated_capability': True,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'self._repeated_capability',
        'name': 'channelList',
        'numpy': False,
        'original_type': 'ViChar[]',
        'python_name': 'channel_list',
        'python_name_with_default': 'channel_list',
        'python_name_with_doc_default': 'channel_list',
        'python_type': 'str',
        'size': {'mechanism': 'fixed', 'value': 1},
        'type': 'ViString',
        'use_in_python_api': True,
    },
    {  # 16
        'ctypes_method_call_snippet': 'a_string_ctype',
        'ctypes_type': 'ViString',
        'ctypes_type_library_call': 'ViString',
        'ctypes_variable_name': 'a_string_ctype',
        'direction': 'in',
        'documentation': {'description': 'An input string.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'a_string',
        'is_buffer': False,
        'is_string': True,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'a_string',
        'name': 'aString',
        'numpy': False,
        'python_name': 'a_string',
        'python_name_with_default': 'a_string',
        'python_name_with_doc_default': 'a_string',
        'python_type': 'int',
        'size': {'mechanism': 'len', 'value': 'a_string'},
        'type': 'ViString',
        'use_in_python_api': True,
    },
    {  # 17
        'ctypes_method_call_snippet': 'array_in_ctype',
        'ctypes_type': 'custom_struct',
        'ctypes_type_library_call': 'ctypes.POINTER(custom_struct)',
        'ctypes_variable_name': 'array_in_ctype',
        'direction': 'in',
        'documentation': {'description': 'Array of custom type using python-code size mechanism'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'array_in',
        'is_buffer': True,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'array_in',
        'name': 'arrayOut',
        'original_type': 'custom_struct[]',
        'python_name': 'array_in',
        'python_name_with_default': 'array_in',
        'python_name_with_doc_default': 'array_in',
        'python_type': 'CustomStruct',
        'size': {'mechanism': 'len', 'value': 'array_in'},
        'type': 'custom_struct',
        'numpy': False,
        'use_in_python_api': True,
    },
    {  # 18
        'ctypes_method_call_snippet': 'an_int_ctype',
        'ctypes_type': 'ViInt16',
        'ctypes_type_library_call': 'ViInt16',
        'ctypes_variable_name': 'an_int_ctype',
        'direction': 'out',
        'documentation': {
            'description': 'Indicates a ninja turtle',
        },
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'an_int',
        'is_buffer': True,
        'use_array': True,
        'use_list': False,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'an_int',
        'name': 'anInt',
        'python_name': 'an_int',
        'python_name_with_default': 'an_int',
        'python_name_with_doc_default': 'an_int',
        'python_type': 'int',
        'size': {'mechanism': 'fixed', 'value': 256},
        'type': 'ViInt16',
        'numpy': False,
        'use_in_python_api': True,
    },
    {  # 19
        'ctypes_method_call_snippet': 'a_string_2_ctype',
        'ctypes_type': 'ViString',
        'ctypes_type_library_call': 'ctypes.POINTER(ViChar)',
        'ctypes_variable_name': 'a_string_2_ctype',
        'direction': 'out',
        'documentation': {'description': 'A fixed size string.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'a_string_2',
        'is_buffer': False,
        'is_string': True,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'a_string_2',
        'name': 'aString2',
        'numpy': False,
        'python_name': 'a_string_2',
        'python_name_with_default': 'a_string_2',
        'python_name_with_doc_default': 'a_string_2',
        'python_type': 'str',
        'size': {'mechanism': 'fixed', 'value': 256},
        'type': 'ViString',
        'use_in_python_api': True,
    },
    {  # 20
        'ctypes_method_call_snippet': 'a_string_3_ctype',
        'ctypes_type': 'ViString',
        'ctypes_type_library_call': 'ctypes.POINTER(ViChar)',
        'ctypes_variable_name': 'a_string_3_ctype',
        'direction': 'out',
        'documentation': {'description': 'A python-code size string.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'a_string_3',
        'is_buffer': False,
        'is_string': True,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'a_string_3',
        'name': 'aStrin3g',
        'numpy': False,
        'python_name': 'a_string_3',
        'python_name_with_default': 'a_string_3',
        'python_name_with_doc_default': 'a_string_3',
        'python_type': 'str',
        'size': {'mechanism': 'python-code', 'value': 'string_size'},
        'type': 'ViString',
        'use_in_python_api': True,
    },
    {  # 21
        'ctypes_method_call_snippet': 'a_string_twist_ctype',
        'ctypes_type': 'ViString',
        'ctypes_type_library_call': 'ctypes.POINTER(ViChar)',
        'ctypes_variable_name': 'a_string_twist_ctype',
        'direction': 'out',
        'documentation': {'description': 'An IVI dance with a twist string.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'a_string_twist',
        'is_buffer': False,
        'is_string': True,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'a_string_twist',
        'name': 'aStringTwist',
        'numpy': False,
        'python_name': 'a_string_twist',
        'python_name_with_default': 'a_string_twist',
        'python_name_with_doc_default': 'a_string_twist',
        'python_type': 'str',
        'size': {'mechanism': 'ivi-dance-with-a-twist', 'value': 'stringSizeTwist', 'value_twist': 'output_twist', },
        'type': 'ViString',
        'use_in_python_api': True,
    },
    {  # 22
        'ctypes_method_call_snippet': 'ctypes.pointer(output_twist_ctype)',
        'ctypes_type': 'ViInt64',
        'ctypes_type_library_call': 'ctypes.POINTER(ViInt64)',
        'ctypes_variable_name': 'output_twist_ctype',
        'direction': 'out',
        'documentation': {'description': 'A big number on its way out.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'output_twist',
        'is_buffer': False,
        'is_string': False,
        'use_array': False,
        'use_list': False,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'output_twist',
        'name': 'output_twist',
        'python_name': 'output_twist',
        'python_name_with_default': 'output_twist',
        'python_name_with_doc_default': 'output_twist',
        'python_type': 'int',
        'size': {'mechanism': 'fixed', 'value': 1},
        'type': 'ViInt64',
        'numpy': False,
        'use_in_python_api': True,
    },
    {  # 23
        'ctypes_method_call_snippet': 'string_size_twist_ctype',
        'ctypes_type': 'ViInt32',
        'ctypes_type_library_call': 'ViInt32',
        'ctypes_variable_name': 'string_size_twist_ctype',
        'direction': 'in',
        'documentation': {'description': 'Number of bytes allocated for aStringTwist'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'string_size_twist',
        'is_buffer': False,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'string_size_twist',
        'name': 'stringSizeTwist',
        'numpy': False,
        'python_name': 'string_size_twist',
        'python_name_with_default': 'string_size_twist',
        'python_name_with_doc_default': 'string_size_twist',
        'python_type': 'int',
        'size': {'mechanism': 'fixed', 'value': 1},
        'type': 'ViInt32',
        'use_in_python_api': True,
    },
    {  # 24
        'ctypes_method_call_snippet': 'a_buffer_ctype',
        'ctypes_type': 'ViInt32',
        'ctypes_type_library_call': 'ctypes.POINTER(ViInt32)',
        'ctypes_variable_name': 'a_buffer_array_ctype',
        'direction': 'out',
        'documentation': {'description': 'An IVI dance buffer using array.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'a_buffer_array',
        'is_buffer': True,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'a_buffer',
        'name': 'aBufferArray',
        'numpy': False,
        'python_name': 'a_buffer_array',
        'python_name_with_default': 'a_buffer_array',
        'python_name_with_doc_default': 'a_buffer_array',
        'python_type': 'int',
        'size': {'mechanism': 'ivi-dance', 'value': 'stringSize'},
        'type': 'ViInt32',
        'use_array': True,
        'use_list': False,
        'use_in_python_api': True,
    },
    {  # 25
        'ctypes_method_call_snippet': 'a_buffer_ctype',
        'ctypes_type': 'ViInt32',
        'ctypes_type_library_call': 'ctypes.POINTER(ViInt32)',
        'ctypes_variable_name': 'a_buffer_list_ctype',
        'direction': 'out',
        'documentation': {'description': 'An IVI dance buffer using a list.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'a_buffer_list',
        'is_buffer': True,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'a_buffer',
        'name': 'aBufferList',
        'numpy': False,
        'python_name': 'a_buffer_list',
        'python_name_with_default': 'a_buffer_list',
        'python_name_with_doc_default': 'a_buffer_list',
        'python_type': 'int',
        'size': {'mechanism': 'ivi-dance', 'value': 'stringSize'},
        'type': 'ViInt32',
        'use_array': False,
        'use_list': True,
        'use_in_python_api': True,
    },
    {  # 26
        'ctypes_method_call_snippet': 'a_buffer_ctype',
        'ctypes_type': 'ViInt32',
        'ctypes_type_library_call': 'ctypes.POINTER(ViInt32)',
        'ctypes_variable_name': 'a_buffer_twist_array_ctype',
        'direction': 'out',
        'documentation': {'description': 'An IVI dance with a twist buffer using an array.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'a_buffer_twist_array',
        'is_buffer': True,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'a_buffer',
        'name': 'aBufferTwistArray',
        'numpy': False,
        'python_name': 'a_buffer_twist_array',
        'python_name_with_default': 'a_buffer_twist_array',
        'python_name_with_doc_default': 'a_buffer_twist_array',
        'python_type': 'int',
        'size': {'mechanism': 'ivi-dance-with-a-twist', 'value': 'stringSizeTwist', 'value_twist': 'output_twist', },
        'type': 'ViInt32',
        'use_array': True,
        'use_list': False,
        'use_in_python_api': True,
    },
    {  # 27
        'ctypes_method_call_snippet': 'a_buffer_ctype',
        'ctypes_type': 'ViInt32',
        'ctypes_type_library_call': 'ctypes.POINTER(ViInt32)',
        'ctypes_variable_name': 'a_buffer_twist_list_ctype',
        'direction': 'out',
        'documentation': {'description': 'An IVI dance with a twist buffer using a list.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'a_buffer_twist_list',
        'is_buffer': True,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'a_buffer',
        'name': 'aBufferTwistList',
        'numpy': False,
        'python_name': 'a_buffer_twist_list',
        'python_name_with_default': 'a_buffer_twist_list',
        'python_name_with_doc_default': 'a_buffer_twist_list',
        'python_type': 'int',
        'size': {'mechanism': 'ivi-dance-with-a-twist', 'value': 'stringSizeTwist', 'value_twist': 'output_twist', },
        'type': 'ViInt32',
        'use_array': False,
        'use_list': True,
        'use_in_python_api': True,
    },
    {  # 28
        'ctypes_method_call_snippet': 'input_array_2_ctype',
        'ctypes_type': 'ViReal64',
        'ctypes_type_library_call': 'ctypes.POINTER(ViReal64)',
        'ctypes_variable_name': 'input_array_2_ctype',
        'default_value': None,
        'direction': 'in',
        'documentation': {'description': 'Input array of floats'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'input_array_2',
        'is_buffer': True,
        'is_string': False,
        'use_array': False,
        'use_list': True,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'input_array_2',
        'name': 'inputArray2',
        'numpy': False,
        'python_name': 'input_array_2',
        'python_name_with_default': 'input_array_2=None',
        'python_name_with_doc_default': 'input_array_2=None',
        'python_type': 'float',
        'size': {'mechanism': 'len', 'value': 'inputArraySize2'},
        'type': 'ViReal64',
        'use_in_python_api': True,
    },
    {  # 29
        'ctypes_method_call_snippet': 'input_array_2_ctype',
        'ctypes_type': 'ViReal64',
        'ctypes_type_library_call': 'ctypes.POINTER(ViReal64)',
        'ctypes_variable_name': 'input_array_2_ctype',
        'default_value': None,
        'direction': 'in',
        'documentation': {'description': 'Input array of floats'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'input_array_2',
        'is_buffer': True,
        'is_string': False,
        'use_array': False,
        'use_list': True,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'input_array_2',
        'name': 'inputArray2',
        'numpy': False,
        'python_api_converter_name': 'convert_to_nitclk_session_num_list',
        'python_name': 'input_array_2',
        'python_name_with_default': 'input_array_2=None',
        'python_name_with_doc_default': 'input_array_2=None',
        'python_type': 'float',
        'size': {'mechanism': 'len', 'value': 'inputArraySize2'},
        'type': 'ViReal64',
        'use_in_python_api': True,
    },
    {  # 30
        'ctypes_method_call_snippet': 'input_array_3_ctype',
        'ctypes_type': 'ViReal64',
        'ctypes_type_library_call': 'ctypes.POINTER(ViReal64)',
        'ctypes_variable_name': 'input_array_3_ctype',
        'default_value': None,
        'direction': 'in',
        'documentation': {'description': 'Input array of floats'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'input_array_3',
        'is_buffer': True,
        'is_string': False,
        'use_array': True,
        'use_list': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'input_array_3',
        'name': 'inputArray3',
        'numpy': False,
        'python_api_converter_name': 'convert_to_nitclk_session_num_list',
        'python_name': 'input_array_3',
        'python_name_with_default': 'input_array_3=None',
        'python_name_with_doc_default': 'input_array_3=None',
        'python_type': 'float',
        'size': {'mechanism': 'len', 'value': 'inputArraySize3'},
        'type': 'ViReal64',
        'use_in_python_api': True,
    },
    {  # 31
        'ctypes_method_call_snippet': 'input_array_3_ctype',
        'ctypes_type': 'custom_struct',
        'ctypes_type_library_call': 'ctypes.POINTER(custom_struct)',
        'ctypes_variable_name': 'input_array_4_ctype',
        'default_value': None,
        'direction': 'in',
        'documentation': {'description': 'Input array of floats'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'input_array_4',
        'is_buffer': True,
        'is_string': False,
        'use_array': False,
        'use_list': True,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'input_array_3',
        'name': 'inputArray4',
        'numpy': False,
        'python_api_converter_name': 'convert_to_nitclk_session_num_list',
        'python_name': 'input_array_4',
        'python_name_with_default': 'input_array_4=None',
        'python_name_with_doc_default': 'input_array_4=None',
        'python_type': 'float',
        'size': {'mechanism': 'len', 'value': 'inputArraySize4'},
        'type': 'ViReal64',
        'use_in_python_api': True,
    },
    {  # 32
        'ctypes_method_call_snippet': 'input_array_3_ctype',
        'ctypes_type': 'custom_struct',
        'ctypes_type_library_call': 'ctypes.POINTER(custom_struct)',
        'ctypes_variable_name': 'input_array_4_ctype',
        'default_value': None,
        'direction': 'in',
        'documentation': {'description': 'Input array of floats'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'input_array_4',
        'is_buffer': True,
        'is_string': False,
        'use_array': False,
        'use_list': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'input_array_3',
        'name': 'inputArray4',
        'numpy': False,
        'python_api_converter_name': 'convert_to_nitclk_session_num_list',
        'python_name': 'input_array_4',
        'python_name_with_default': 'input_array_4=None',
        'python_name_with_doc_default': 'input_array_4=None',
        'python_type': 'float',
        'size': {'mechanism': 'len', 'value': 'inputArraySize4'},
        'type': 'ViReal64',
        'use_in_python_api': True,
    },
    {  # 33
        'ctypes_method_call_snippet': 'a_string_enum_ctype',
        'ctypes_type': 'ViString',
        'ctypes_type_library_call': 'ViString',
        'ctypes_variable_name': 'a_string_enum_ctype',
        'direction': 'in',
        'documentation': {'description': 'An input string-valued enum.'},
        'enum': 'Color',
        'grpc_enum': 'Color',
        'grpc_name': 'a_string_enum_raw',
        'is_buffer': False,
        'is_string': True,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'a_string_enum',
        'name': 'aStringEnum',
        'numpy': False,
        'python_name': 'a_string_enum',
        'python_name_with_default': 'a_string_enum',
        'python_name_with_doc_default': 'a_string_enum',
        'python_type': 'enums.Color',
        'size': {'mechanism': 'len', 'value': 'a_string_enum'},
        'type': 'ViString',
        'use_in_python_api': True,
    },
    {  # 34
        'ctypes_method_call_snippet': 'indices_ctype',
        'ctypes_type': 'ViConstString',
        'ctypes_type_library_call': 'ViConstString',
        'ctypes_variable_name': 'indices_ctype',
        'direction': 'in',
        'documentation': {
            'description': 'Specifies a list of indices for the channels in the session.'
        },
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'indices',
        'is_buffer': False,
        'is_string': True,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'indices',
        'name': 'indices',
        'numpy': False,
        'original_type': 'ViChar[]',
        'python_api_converter_name': 'convert_repeated_capabilities_without_prefix',
        'python_name': 'indices',
        'python_name_with_default': 'indices',
        'python_name_with_doc_default': 'indices',
        'python_type': 'str',
        'size': {'mechanism': 'fixed', 'value': 1},
        'type': 'ViConstString',
        'use_in_python_api': True,
    },
    {  # 35
        'ctypes_method_call_snippet': 'an_array_ctype',
        'ctypes_type': 'ViInt8',
        'ctypes_type_library_call': 'ctypes.POINTER(ViInt8)',
        'ctypes_variable_name': 'an_array_ctype',
        'direction': 'out',
        'documentation': {'description': 'Contains an array of enums, stored as 8 bit integers under the hood '},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'a_grpc_array',
        'is_buffer': True,
        'use_array': False,
        'use_list': True,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'an_array',
        'name': 'anArray',
        'python_api_converter_name': 'convert_to_bytes',
        'python_name': 'an_array',
        'python_name_with_default': 'an_array',
        'python_name_with_doc_default': 'an_array',
        'python_type': 'int',
        'size': {'mechanism': 'passed-in', 'value': 'numberOfElements'},
        'type': 'ViInt8',
        'numpy': False,
        'use_in_python_api': True,
    },
]


def test_get_library_interpreter_method_return_snippet_vi():
    param = [parameters_for_testing[0]]
    assert get_library_interpreter_method_return_snippet(param, config_for_testing) == 'return'


def test_get_library_interpreter_method_return_snippet_int():
    param = [parameters_for_testing[1]]
    assert get_library_interpreter_method_return_snippet(param, config_for_testing) == 'return int(output_ctype.value)'


def test_get_library_interpreter_method_return_snippet_string():
    param = [parameters_for_testing[2]]
    assert get_library_interpreter_method_return_snippet(param, config_for_testing) == 'return error_message_ctype.value.decode(self._encoding)'


def test_get_library_interpreter_method_return_snippet_custom_type():
    param = [parameters_for_testing[3]]
    assert get_library_interpreter_method_return_snippet(param, config_for_testing) == 'return [custom_struct.CustomStruct(array_out_ctype[i]) for i in range(self.get_array_size_for_python_code())]'


def test_get_library_interpreter_method_return_snippet_enum():
    param = [parameters_for_testing[4], parameters_for_testing[5]]
    assert get_library_interpreter_method_return_snippet(param, config_for_testing) == 'return [enums.Turtle(an_array_ctype[i]) for i in range(number_of_elements_ctype.value)]'


def test_get_library_interpreter_method_return_snippet_into():
    param = [parameters_for_testing[4], parameters_for_testing[7]]
    assert get_library_interpreter_method_return_snippet(param, config_for_testing, use_numpy_array=True) == 'return'


def test_get_grpc_interpreter_method_return_snippet_vi():
    param = [parameters_for_testing[0]]
    assert get_grpc_interpreter_method_return_snippet(param, config_for_testing) == 'return'


def test_get_grpc_interpreter_method_return_snippet_int():
    param = [parameters_for_testing[1]]
    assert get_grpc_interpreter_method_return_snippet(param, config_for_testing) == 'return response.output'


def test_get_grpc_interpreter_method_return_snippet_string():
    param = [parameters_for_testing[2]]
    assert get_grpc_interpreter_method_return_snippet(param, config_for_testing) == 'return response.error_message'


def test_get_grpc_interpreter_method_return_snippet_custom_type():
    param = [parameters_for_testing[3]]
    assert get_grpc_interpreter_method_return_snippet(param, config_for_testing) == 'return [custom_struct.CustomStruct(x) for x in response.array_out]'


def test_get_grpc_interpreter_method_return_snippet_enum():
    param = [parameters_for_testing[4], parameters_for_testing[5]]
    assert get_grpc_interpreter_method_return_snippet(param, config_for_testing) == 'return [enums.Turtle(x) for x in response.an_array_raw]'


def test_get_grpc_interpreter_method_return_snippet_bytes():
    param = [parameters_for_testing[35]]
    assert get_grpc_interpreter_method_return_snippet(param, config_for_testing) == 'return response.a_grpc_array'


def test_get_session_method_return_snippet():
    param = [dict(parameters_for_testing[14])]
    param[0]['direction'] = 'out'
    assert get_session_method_return_snippet(param, config_for_testing) == 'return _converters.timedelta_converter_seconds_real64(timeout)'


def test_get_session_method_return_snippet_non_numpy():
    param = [parameters_for_testing[4], parameters_for_testing[7]]
    assert get_session_method_return_snippet(param, config_for_testing) == 'return output'


def test_get_session_method_return_snippet_numpy():
    param = [parameters_for_testing[4], parameters_for_testing[7]]
    assert get_session_method_return_snippet(param, config_for_testing, use_numpy_array=True) == 'return'


def test_get_enum_type_check_snippet():
    param = parameters_for_testing[6]
    assert get_enum_type_check_snippet(param, 0) == "if type(an_int_enum) is not enums.Turtle:\nraise TypeError('Parameter an_int_enum must be of type ' + str(enums.Turtle))"


def test_get_buffer_parameters_for_size_parameter_none():
    params = _get_buffer_parameters_for_size_parameter(parameters_for_testing[0], parameters_for_testing)
    assert len(params) == 0


def test_get_buffer_parameters_for_size_parameter():
    params = _get_buffer_parameters_for_size_parameter(parameters_for_testing[4], parameters_for_testing)
    assert params[0] == parameters_for_testing[5]


def test_get_ctype_variable_declaration_snippet_case_c010():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[15], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    assert snippet == ["channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010"]


def test_get_ctype_variable_declaration_snippet_case_c020():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[16], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    assert snippet == ["a_string_ctype = ctypes.create_string_buffer(a_string.encode(self._encoding))  # case C020"]


def test_get_ctype_variable_declaration_snippet_case_c030():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[33], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    assert snippet == ["a_string_enum_ctype = ctypes.create_string_buffer(a_string_enum.value.encode(self._encoding))  # case C030"]


def test_get_ctype_variable_declaration_snippet_case_c050():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[13], parameters_for_testing, IviDanceStep.QUERY_SIZE, config_for_testing, use_numpy_array=False)
    assert snippet == ["a_string_ctype = None  # case C050"]


def test_get_ctype_variable_declaration_snippet_case_c060():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[13], parameters_for_testing, IviDanceStep.GET_DATA, config_for_testing, use_numpy_array=False)
    assert snippet == ["a_string_ctype = (_visatype.ViChar * string_size_ctype.value)()  # case C060"]


def test_get_ctype_variable_declaration_snippet_case_c070():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[19], parameters_for_testing, IviDanceStep.GET_DATA, config_for_testing, use_numpy_array=False)
    assert snippet == ["a_string_2_ctype = (_visatype.ViChar * 256)()  # case C070"]


def test_get_ctype_variable_declaration_snippet_case_c080():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[20], parameters_for_testing, IviDanceStep.GET_DATA, config_for_testing, use_numpy_array=False)
    assert snippet == ["a_string_3_ctype = (_visatype.ViChar * string_size)()  # case C080"]


def test_get_ctype_variable_declaration_snippet_case_c090():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[21], parameters_for_testing, IviDanceStep.QUERY_SIZE, config_for_testing, use_numpy_array=False)
    assert snippet == ["a_string_twist_ctype = None  # case C090"]


def test_get_ctype_variable_declaration_snippet_case_c100():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[21], parameters_for_testing, IviDanceStep.GET_DATA, config_for_testing, use_numpy_array=False)
    assert snippet == ["a_string_twist_ctype = (_visatype.ViChar * output_twist_ctype.value)()  # case C100"]


def test_get_ctype_variable_declaration_snippet_case_s110():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[0], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    assert snippet == ["vi_ctype = _visatype.ViSession(self._vi)  # case S110"]


def test_get_ctype_variable_declaration_snippet_case_s120():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[8], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    assert snippet == ["number_of_elements_python_code_ctype = _visatype.ViInt32(self.get_array_size_for_python_code())  # case S120"]


def test_get_ctype_variable_declaration_snippet_case_s130():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[6], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    assert snippet == ["an_int_enum_ctype = _visatype.ViInt16(an_int_enum.value)  # case S130"]


def test_get_ctype_variable_declaration_snippet_case_s150():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[9], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    assert snippet == ["input_ctype = _visatype.ViInt16(input)  # case S150"]


def test_get_ctype_variable_declaration_snippet_case_s160():
    actual = get_ctype_variable_declaration_snippet(parameters_for_testing[11], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    assert actual == ["input_array_size_ctype = _visatype.ViInt32(0 if input_array is None else len(input_array))  # case S160"]


def test_get_ctype_variable_declaration_snippet_case_s170():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[12], parameters_for_testing, IviDanceStep.QUERY_SIZE, config_for_testing, use_numpy_array=False)
    assert snippet == ["string_size_ctype = _visatype.ViInt32()  # case S170"]


def test_get_ctype_variable_declaration_snippet_case_s180():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[12], parameters_for_testing, IviDanceStep.GET_DATA, config_for_testing, use_numpy_array=False)
    assert snippet == ["string_size_ctype = _visatype.ViInt32(error_code)  # case S180"]


def test_get_ctype_variable_declaration_snippet_case_s2190():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[23], parameters_for_testing, IviDanceStep.QUERY_SIZE, config_for_testing, use_numpy_array=False)
    assert snippet == ["string_size_twist_ctype = _visatype.ViInt32(0)  # case S190"]


def test_get_ctype_variable_declaration_snippet_case_s200():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[23], parameters_for_testing, IviDanceStep.GET_DATA, config_for_testing, use_numpy_array=False)
    assert snippet == ["string_size_twist_ctype = _visatype.ViInt32(output_twist_ctype.value)  # case S200"]


def test_get_ctype_variable_declaration_snippet_case_s210():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[4], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    assert snippet == ["number_of_elements_ctype = _visatype.ViInt32(number_of_elements)  # case S210"]


def test_get_ctype_variable_declaration_snippet_case_s220():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[1], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    assert snippet == ["output_ctype = _visatype.ViInt64()  # case S220"]


def test_get_ctype_variable_declaration_snippet_case_b510():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[7], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=True)
    assert snippet == ["output_ctype = _get_ctypes_pointer_for_buffer(value=output)  # case B510"]


def test_get_ctype_variable_declaration_snippet_case_b540():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[17], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    assert snippet == ["array_in_ctype = _get_ctypes_pointer_for_buffer([custom_struct.custom_struct(c) for c in array_in], library_type=custom_struct.custom_struct)  # case B540"]


def test_get_ctype_variable_declaration_snippet_case_b550_array():
    actual = get_ctype_variable_declaration_snippet(parameters_for_testing[10], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    expected = [
        'input_array_array = _convert_to_array(value=input_array, array_type="d")  # case B550',
        'input_array_ctype = _get_ctypes_pointer_for_buffer(value=input_array_array, library_type=_visatype.ViReal64)  # case B550',
    ]
    assert len(actual) == len(expected)
    for i in range(max(len(actual), len(expected))):
        assert actual[i] == expected[i]


def test_get_ctype_variable_declaration_snippet_case_b550_list():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[28], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    assert snippet == ["input_array_2_ctype = _get_ctypes_pointer_for_buffer(value=input_array_2, library_type=_visatype.ViReal64)  # case B550"]


def test_get_ctype_variable_declaration_snippet_case_b560():
    actual = get_ctype_variable_declaration_snippet(parameters_for_testing[3], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    expected = [
        'array_out_size = self.get_array_size_for_python_code()  # case B560',
        'array_out_ctype = _get_ctypes_pointer_for_buffer(library_type=custom_struct.custom_struct, size=array_out_size)  # case B560',
    ]
    assert len(actual) == len(expected)
    for i in range(max(len(actual), len(expected))):
        assert actual[i] == expected[i]


def test_get_ctype_variable_declaration_snippet_case_b570():
    actual = get_ctype_variable_declaration_snippet(parameters_for_testing[18], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    expected = [
        'an_int_size = 256  # case B570',
        'an_int_array = array.array("h", [0] * an_int_size)  # case B570',
        'an_int_ctype = _get_ctypes_pointer_for_buffer(value=an_int_array, library_type=_visatype.ViInt16)  # case B570',
    ]
    assert len(actual) == len(expected)
    for i in range(max(len(actual), len(expected))):
        assert actual[i] == expected[i]


def test_get_ctype_variable_declaration_snippet_case_b580_array():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[24], parameters_for_testing, IviDanceStep.QUERY_SIZE, config_for_testing, use_numpy_array=False)
    assert snippet == ["a_buffer_array_ctype = None  # case B580"]


def test_get_ctype_variable_declaration_snippet_case_b590_array():
    actual = get_ctype_variable_declaration_snippet(parameters_for_testing[24], parameters_for_testing, IviDanceStep.GET_DATA, config_for_testing, use_numpy_array=False)
    expected = [
        'a_buffer_array_size = string_size_ctype.value  # case B590',
        'a_buffer_array_array = array.array("l", [0] * a_buffer_array_size)  # case B590',
        'a_buffer_array_ctype = _get_ctypes_pointer_for_buffer(value=a_buffer_array_array, library_type=_visatype.ViInt32)  # case B590',
    ]
    assert len(actual) == len(expected)
    for i in range(max(len(actual), len(expected))):
        assert actual[i] == expected[i]


def test_get_ctype_variable_declaration_snippet_case_b580_list():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[25], parameters_for_testing, IviDanceStep.QUERY_SIZE, config_for_testing, use_numpy_array=False)
    assert snippet == ["a_buffer_list_ctype = None  # case B580"]


def test_get_ctype_variable_declaration_snippet_case_b590_list():
    actual = get_ctype_variable_declaration_snippet(parameters_for_testing[25], parameters_for_testing, IviDanceStep.GET_DATA, config_for_testing, use_numpy_array=False)
    expected = [
        'a_buffer_list_size = string_size_ctype.value  # case B590',
        'a_buffer_list_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViInt32, size=a_buffer_list_size)  # case B590',
    ]
    assert len(actual) == len(expected)
    for i in range(max(len(actual), len(expected))):
        assert actual[i] == expected[i]


def test_get_ctype_variable_declaration_snippet_case_b600():
    actual = get_ctype_variable_declaration_snippet(parameters_for_testing[7], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    expected = [
        'output_size = number_of_elements  # case B600',
        'output_array = array.array("q", [0] * output_size)  # case B600',
        'output_ctype = _get_ctypes_pointer_for_buffer(value=output_array, library_type=_visatype.ViInt64)  # case B600',
    ]
    assert len(actual) == len(expected)
    for i in range(max(len(actual), len(expected))):
        assert actual[i] == expected[i]


def test_get_ctype_variable_declaration_snippet_case_b610_array():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[26], parameters_for_testing, IviDanceStep.QUERY_SIZE, config_for_testing, use_numpy_array=False)
    assert snippet == ["a_buffer_twist_array_ctype = None  # case B610"]


def test_get_ctype_variable_declaration_snippet_case_b620_array():
    actual = get_ctype_variable_declaration_snippet(parameters_for_testing[26], parameters_for_testing, IviDanceStep.GET_DATA, config_for_testing, use_numpy_array=False)
    expected = [
        'a_buffer_twist_array_size = output_twist_ctype.value  # case B620',
        'a_buffer_twist_array_array = array.array("l", [0] * a_buffer_twist_array_size)  # case B620',
        'a_buffer_twist_array_ctype = _get_ctypes_pointer_for_buffer(value=a_buffer_twist_array_array, library_type=_visatype.ViInt32)  # case B620',
    ]
    assert len(actual) == len(expected)
    for i in range(max(len(actual), len(expected))):
        assert actual[i] == expected[i]


def test_get_ctype_variable_declaration_snippet_case_b610_list():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[27], parameters_for_testing, IviDanceStep.QUERY_SIZE, config_for_testing, use_numpy_array=False)
    assert snippet == ["a_buffer_twist_list_ctype = None  # case B610"]


def test_get_ctype_variable_declaration_snippet_case_b620_list():
    actual = get_ctype_variable_declaration_snippet(parameters_for_testing[27], parameters_for_testing, IviDanceStep.GET_DATA, config_for_testing, use_numpy_array=False)
    expected = [
        'a_buffer_twist_list_size = output_twist_ctype.value  # case B620',
        'a_buffer_twist_list_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViInt32, size=a_buffer_twist_list_size)  # case B620',
    ]
    assert len(actual) == len(expected)
    for i in range(max(len(actual), len(expected))):
        assert actual[i] == expected[i]


def test_get_ctype_variable_declaration_snippet_bad_ivi_dance_step():
    try:
        get_ctype_variable_declaration_snippet(parameters_for_testing[12], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
        assert False
    except AssertionError:
        pass


# TODO(marcoskirsch): unit tests for reamining cases of get_ctype_variable_declaration_snippet(): parameter is a buffer.


def test_get_enum_value_snippet():
    assert get_enum_value_snippet(None) == 'None'
    assert get_enum_value_snippet(True) == 'True'
    assert get_enum_value_snippet(0) == '0'
    assert get_enum_value_snippet('True') == "'True'"
    assert get_enum_value_snippet('0') == "'0'"
