from build.helper.metadata_add_all import *
from build.helper.metadata_add_all import _add_enum_codegen_method
from build.helper.metadata_add_all import _get_attributes_that_use_enums
from build.helper.metadata_add_all import _get_functions_that_use_enums
from build.helper.metadata_add_all import _get_least_restrictive_codegen_method


def _compare_values(actual, expected, k):
    if type(actual) is dict:
        _compare_dicts(actual, expected)
    elif type(actual) is list:
        _compare_lists(actual, expected)
    else:
        assert actual == expected, f"Value mismatch with key/index '{k}', {actual} != {expected}"


def _compare_lists(actual, expected):
    assert isinstance(actual, type(expected)), f'Type mismatch, {type(actual)} != {type(expected)}'
    assert len(actual) == len(expected), f'Length mismatch, {len(actual)} != {len(expected)}'
    for k in range(len(actual)):
        _compare_values(actual[k], expected[k], k)


def _compare_dicts(actual, expected):
    assert isinstance(actual, type(expected)), f'Type mismatch, {type(actual)} != {type(expected)}'
    for k in actual:
        assert k in expected, f'Key {k} not in expected'
        _compare_values(actual[k], expected[k], k)
    for k in expected:
        assert k in actual, f'Key {k} not in actual'


functions_input = {
    'MakeAFoo': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'method_templates': [{'session_filename': '/cool_template', 'library_interpreter_filename': '/cool_template', 'documentation_filename': '/cool_template', 'method_python_name_suffix': '', }, ],
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session.',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channelName',
                'python_name': 'name',
                'is_repeated_capability': False,
                'type': 'ViString',
                'documentation': {
                    'description': 'The channel to call this on.',
                },
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'buffer size input',
                },
                'enum': None,
                'name': 'pinDataBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'python-code input',
                },
                'enum': None,
                'name': 'pythonCodeInput',
                'size': {
                    'mechanism': 'python-code',
                    'value': '2 ** 14'
                },
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'buffer size output',
                },
                'enum': None,
                'name': 'actualNumPinData',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'buffer',
                },
                'enum': None,
                'name': 'expectedPinStates',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'pinDataBufferSize',
                    'value_twist': 'actualNumPinData'
                },
                'type': 'ViUInt8[]'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'custom type input',
                },
                'enum': None,
                'name': 'customTypeInput',
                'type': 'struct CustomStruct'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'custom type output',
                },
                'enum': None,
                'name': 'customTypeOutput',
                'type': 'struct CustomStruct'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'custom type without struct prefix input',
                },
                'enum': None,
                'name': 'customTypeWithoutStructPrefixInput',
                'type': 'CustomStruct'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'custom type without struct prefix output',
                },
                'enum': None,
                'name': 'customTypeWithoutStructPrefixOutput',
                'type': 'CustomStruct'
            },
        ],
        'documentation': {
            'description': 'Performs a foo, and performs it well.',
        },
    },
    'MakeAPrivateMethod': {
        'codegen_method': 'private',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session.',
                },
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'status',
                'type': 'ViString',
                'documentation': {
                    'description': 'Return a device status',
                },
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'buffer size',
                },
                'enum': None,
                'name': 'dataBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'buffer',
                },
                'enum': None,
                'name': 'data',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'dataBufferSize'
                },
                'type': 'ViUInt32[]'
            },
        ],
        'documentation': {
            'description': 'Perform actions as method defined',
        },
    },
    'MakeANoCodegenMethod': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'This is a method with codegen_method set to no',
        },
        'method_name_for_documentation': 'MakeAPublicMethod',
        'method_templates': [
            {
                'session_filename': '/cool_template',
                'library_interpreter_filename': '/cool_template',
                'documentation_filename': '/cool_template',
                'method_python_name_suffix': '',
            },
        ],
        'parameters': [],
        'returns': 'ViStatus',
    },
}


functions_expected = {
    'MakeAFoo': {
        'name': 'MakeAFoo',
        'codegen_method': 'public',
        'use_session_lock': True,
        'documentation': {
            'description': 'Performs a foo, and performs it well.'
        },
        'has_repeated_capability': False,
        'is_error_handling': False,
        'render_in_session_base': False,
        'method_templates': [{'session_filename': '/cool_template', 'library_interpreter_filename': '/cool_template', 'documentation_filename': '/cool_template', 'method_python_name_suffix': '', }, ],
        'parameters': [
            {
                'ctypes_method_call_snippet': 'vi_ctype',
                'ctypes_type': 'ViSession',
                'ctypes_variable_name': 'vi_ctype',
                'ctypes_type_library_call': 'ViSession',
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'is_repeated_capability': False,
                'is_session_handle': True,
                'enum': None,
                'grpc_enum': None,
                'numpy': False,
                'python_type': 'int',
                'type_in_documentation': 'int',
                'type_in_documentation_was_calculated': True,
                'use_array': False,
                'is_buffer': False,
                'use_list': False,
                'is_string': False,
                'name': 'vi',
                'grpc_name': 'vi',
                'python_name': 'vi',
                'python_name_with_default': 'vi',
                'python_name_with_doc_default': 'vi',
                'size': {
                    'mechanism': 'fixed',
                    'value': 1
                },
                'type': 'ViSession',
                'interpreter_method_call_snippet': 'self._vi',
                'grpc_request_snippet': 'vi=self._vi',
                'use_in_python_api': True,
                'python_name_or_default_for_init': 'vi',
            },
            {
                'ctypes_method_call_snippet': 'name_ctype',
                'ctypes_type': 'ViString',
                'ctypes_variable_name': 'name_ctype',
                'ctypes_type_library_call': 'ctypes.POINTER(ViChar)',
                'direction': 'in',
                'documentation': {
                    'description': 'The channel to call this on.'
                },
                'is_repeated_capability': False,
                'is_session_handle': False,
                'enum': None,
                'grpc_enum': None,
                'numpy': False,
                'python_type': 'str',
                'type_in_documentation': 'str',
                'type_in_documentation_was_calculated': True,
                'use_array': False,
                'is_buffer': False,
                'use_list': False,
                'is_string': True,
                'name': 'channelName',
                'grpc_name': 'name',
                'python_name': 'name',
                'python_name_with_default': 'name',
                'python_name_with_doc_default': 'name',
                'size': {'mechanism': 'fixed', 'value': 1},
                'type': 'ViString',
                'interpreter_method_call_snippet': 'name',
                'grpc_request_snippet': 'name=name',
                'use_in_python_api': True,
                'python_name_or_default_for_init': 'name',
            },
            {
                'ctypes_method_call_snippet': 'pin_data_buffer_size_ctype',
                'ctypes_type': 'ViInt32',
                'ctypes_variable_name': 'pin_data_buffer_size_ctype',
                'ctypes_type_library_call': 'ViInt32',
                'direction': 'in',
                'documentation': {
                    'description': 'buffer size input',
                },
                'is_repeated_capability': False,
                'is_session_handle': False,
                'enum': None,
                'grpc_enum': None,
                'numpy': False,
                'python_type': 'int',
                'type_in_documentation': 'int',
                'type_in_documentation_was_calculated': True,
                'use_array': False,
                'is_buffer': False,
                'use_list': False,
                'is_string': False,
                'name': 'pinDataBufferSize',
                'grpc_name': 'pin_data_buffer_size',
                'python_name': 'pin_data_buffer_size',
                'python_name_with_default': 'pin_data_buffer_size',
                'python_name_with_doc_default': 'pin_data_buffer_size',
                'size': {
                    'mechanism': 'fixed',
                    'value': 1
                },
                'type': 'ViInt32',
                'interpreter_method_call_snippet': 'pin_data_buffer_size',
                'grpc_request_snippet': 'pin_data_buffer_size=pin_data_buffer_size',
                'use_in_python_api': False,
                'python_name_or_default_for_init': 'pin_data_buffer_size',
            },
            {
                'ctypes_method_call_snippet': 'python_code_input_ctype',
                'ctypes_type': 'ViInt32',
                'ctypes_variable_name': 'python_code_input_ctype',
                'ctypes_type_library_call': 'ViInt32',
                'direction': 'in',
                'documentation': {
                    'description': 'python-code input',
                },
                'is_repeated_capability': False,
                'is_session_handle': False,
                'enum': None,
                'grpc_enum': None,
                'numpy': False,
                'python_type': 'int',
                'type_in_documentation': 'int',
                'type_in_documentation_was_calculated': True,
                'use_array': False,
                'is_buffer': False,
                'use_list': False,
                'is_string': False,
                'name': 'pythonCodeInput',
                'grpc_name': 'python_code_input',
                'python_name': 'python_code_input',
                'python_name_with_default': 'python_code_input',
                'python_name_with_doc_default': 'python_code_input',
                'size': {
                    'mechanism': 'python-code',
                    'value': '2 ** 14'
                },
                'type': 'ViInt32',
                'interpreter_method_call_snippet': 'python_code_input',
                'grpc_request_snippet': 'python_code_input=2 ** 14',
                'use_in_python_api': True,
                'python_name_or_default_for_init': 'python_code_input',
            },
            {
                'ctypes_method_call_snippet': 'None if actual_num_pin_data_ctype is None else (ctypes.pointer(actual_num_pin_data_ctype))',
                'ctypes_type': 'ViInt32',
                'ctypes_variable_name': 'actual_num_pin_data_ctype',
                'ctypes_type_library_call': 'ctypes.POINTER(ViInt32)',
                'direction': 'out',
                'documentation': {
                    'description': 'buffer size output',
                },
                'is_repeated_capability': False,
                'is_session_handle': False,
                'enum': None,
                'grpc_enum': None,
                'numpy': False,
                'python_type': 'int',
                'type_in_documentation': 'int',
                'type_in_documentation_was_calculated': True,
                'use_array': False,
                'is_buffer': False,
                'use_list': False,
                'is_string': False,
                'name': 'actualNumPinData',
                'grpc_name': 'actual_num_pin_data',
                'python_name': 'actual_num_pin_data',
                'python_name_with_default': 'actual_num_pin_data',
                'python_name_with_doc_default': 'actual_num_pin_data',
                'size': {
                    'mechanism': 'fixed',
                    'value': 1
                },
                'type': 'ViInt32',
                'interpreter_method_call_snippet': 'actual_num_pin_data',
                'grpc_request_snippet': 'actual_num_pin_data=actual_num_pin_data',
                'use_in_python_api': False,
                'python_name_or_default_for_init': 'actual_num_pin_data',
            },
            {
                'ctypes_method_call_snippet': 'expected_pin_states_ctype',
                'ctypes_type': 'ViUInt8',
                'ctypes_variable_name': 'expected_pin_states_ctype',
                'ctypes_type_library_call': 'ctypes.POINTER(ViUInt8)',
                'direction': 'out',
                'documentation': {
                    'description': 'buffer',
                },
                'is_repeated_capability': False,
                'is_session_handle': False,
                'enum': None,
                'grpc_enum': None,
                'numpy': False,
                'python_type': 'int',
                'type_in_documentation': 'int',
                'type_in_documentation_was_calculated': True,
                'use_array': False,
                'is_buffer': True,
                'use_list': True,
                'is_string': False,
                'name': 'expectedPinStates',
                'original_type': 'ViUInt8[]',
                'grpc_name': 'expected_pin_states',
                'python_name': 'expected_pin_states',
                'python_name_with_default': 'expected_pin_states',
                'python_name_with_doc_default': 'expected_pin_states',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'pinDataBufferSize',
                    'value_twist': 'actualNumPinData'
                },
                'type': 'ViUInt8',
                'interpreter_method_call_snippet': 'expected_pin_states',
                'grpc_request_snippet': 'expected_pin_states=expected_pin_states',
                'use_in_python_api': True,
                'python_name_or_default_for_init': 'expected_pin_states',
            },
            {
                'ctypes_method_call_snippet': 'custom_type_input_ctype',
                'ctypes_type': 'struct_CustomStruct',
                'ctypes_variable_name': 'custom_type_input_ctype',
                'ctypes_type_library_call': 'custom_struct.struct_CustomStruct',
                'direction': 'in',
                'documentation': {
                    'description': 'custom type input',
                },
                'is_repeated_capability': False,
                'is_session_handle': False,
                'enum': None,
                'grpc_enum': None,
                'numpy': False,
                'python_type': 'CustomStruct',
                'type_in_documentation': 'CustomStruct',
                'type_in_documentation_was_calculated': True,
                'use_array': False,
                'is_buffer': False,
                'use_list': False,
                'is_string': False,
                'name': 'customTypeInput',
                'grpc_name': 'custom_type_input',
                'python_name': 'custom_type_input',
                'python_name_with_default': 'custom_type_input',
                'python_name_with_doc_default': 'custom_type_input',
                'size': {
                    'mechanism': 'fixed',
                    'value': 1
                },
                'type': 'struct_CustomStruct',
                'interpreter_method_call_snippet': 'custom_type_input',
                'grpc_request_snippet': 'custom_type_input=custom_type_input._create_copy(grpc_types.CustomStruct)',
                'use_in_python_api': True,
                'python_name_or_default_for_init': 'custom_type_input',
            },
            {
                'ctypes_method_call_snippet': 'None if custom_type_output_ctype is None else (ctypes.pointer(custom_type_output_ctype))',
                'ctypes_type': 'struct_CustomStruct',
                'ctypes_variable_name': 'custom_type_output_ctype',
                'ctypes_type_library_call': 'ctypes.POINTER(custom_struct.struct_CustomStruct)',
                'direction': 'out',
                'documentation': {
                    'description': 'custom type output',
                },
                'is_repeated_capability': False,
                'is_session_handle': False,
                'enum': None,
                'grpc_enum': None,
                'numpy': False,
                'python_type': 'CustomStruct',
                'type_in_documentation': 'CustomStruct',
                'type_in_documentation_was_calculated': True,
                'use_array': False,
                'is_buffer': False,
                'use_list': False,
                'is_string': False,
                'name': 'customTypeOutput',
                'grpc_name': 'custom_type_output',
                'python_name': 'custom_type_output',
                'python_name_with_default': 'custom_type_output',
                'python_name_with_doc_default': 'custom_type_output',
                'size': {
                    'mechanism': 'fixed',
                    'value': 1
                },
                'type': 'struct_CustomStruct',
                'interpreter_method_call_snippet': 'custom_type_output',
                'grpc_request_snippet': 'custom_type_output=custom_type_output._create_copy(grpc_types.CustomStruct)',
                'use_in_python_api': True,
                'python_name_or_default_for_init': 'custom_type_output',
            },
            {
                'ctypes_method_call_snippet': 'custom_type_without_struct_prefix_input_ctype',
                'ctypes_type': 'struct_CustomStruct',
                'ctypes_variable_name': 'custom_type_without_struct_prefix_input_ctype',
                'ctypes_type_library_call': 'custom_struct.struct_CustomStruct',
                'direction': 'in',
                'documentation': {
                    'description': 'custom type without struct prefix input',
                },
                'is_repeated_capability': False,
                'is_session_handle': False,
                'enum': None,
                'grpc_enum': None,
                'numpy': False,
                'python_type': 'CustomStruct',
                'type_in_documentation': 'CustomStruct',
                'type_in_documentation_was_calculated': True,
                'use_array': False,
                'is_buffer': False,
                'use_list': False,
                'is_string': False,
                'name': 'customTypeWithoutStructPrefixInput',
                'grpc_name': 'custom_type_without_struct_prefix_input',
                'python_name': 'custom_type_without_struct_prefix_input',
                'python_name_with_default': 'custom_type_without_struct_prefix_input',
                'python_name_with_doc_default': 'custom_type_without_struct_prefix_input',
                'size': {
                    'mechanism': 'fixed',
                    'value': 1
                },
                'type': 'struct_CustomStruct',
                'interpreter_method_call_snippet': 'custom_type_without_struct_prefix_input',
                'grpc_request_snippet': 'custom_type_without_struct_prefix_input=custom_type_without_struct_prefix_input._create_copy(grpc_types.CustomStruct)',
                'use_in_python_api': True,
                'python_name_or_default_for_init': 'custom_type_without_struct_prefix_input',
            },
            {
                'ctypes_method_call_snippet': 'None if custom_type_without_struct_prefix_output_ctype is None else (ctypes.pointer(custom_type_without_struct_prefix_output_ctype))',
                'ctypes_type': 'struct_CustomStruct',
                'ctypes_variable_name': 'custom_type_without_struct_prefix_output_ctype',
                'ctypes_type_library_call': 'ctypes.POINTER(custom_struct.struct_CustomStruct)',
                'direction': 'out',
                'documentation': {
                    'description': 'custom type without struct prefix output',
                },
                'is_repeated_capability': False,
                'is_session_handle': False,
                'enum': None,
                'grpc_enum': None,
                'numpy': False,
                'python_type': 'CustomStruct',
                'type_in_documentation': 'CustomStruct',
                'type_in_documentation_was_calculated': True,
                'use_array': False,
                'is_buffer': False,
                'use_list': False,
                'is_string': False,
                'name': 'customTypeWithoutStructPrefixOutput',
                'grpc_name': 'custom_type_without_struct_prefix_output',
                'python_name': 'custom_type_without_struct_prefix_output',
                'python_name_with_default': 'custom_type_without_struct_prefix_output',
                'python_name_with_doc_default': 'custom_type_without_struct_prefix_output',
                'size': {
                    'mechanism': 'fixed',
                    'value': 1
                },
                'type': 'struct_CustomStruct',
                'interpreter_method_call_snippet': 'custom_type_without_struct_prefix_output',
                'grpc_request_snippet': 'custom_type_without_struct_prefix_output=custom_type_without_struct_prefix_output._create_copy(grpc_types.CustomStruct)',
                'use_in_python_api': True,
                'python_name_or_default_for_init': 'custom_type_without_struct_prefix_output',
            },
        ],
        'python_name': 'make_a_foo',
        'interpreter_name': 'make_a_foo',
        'returns': 'ViStatus',
    },
    'MakeAPrivateMethod': {
        'codegen_method': 'private',
        'returns': 'ViStatus',
        'use_session_lock': True,
        'method_templates': [{'session_filename': '/default_method', 'library_interpreter_filename': '/default_method', 'documentation_filename': '/default_method', 'method_python_name_suffix': '', }, ],
        'parameters': [
            {
                'ctypes_method_call_snippet': 'vi_ctype',
                'direction': 'in',
                'enum': None,
                'grpc_enum': None,
                'numpy': False,
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'grpc_name': 'vi',
                'python_name': 'vi',
                'python_type': 'int',
                'type_in_documentation': 'int',
                'type_in_documentation_was_calculated': True,
                'ctypes_variable_name': 'vi_ctype',
                'ctypes_type': 'ViSession',
                'ctypes_type_library_call': 'ViSession',
                'size': {
                    'mechanism': 'fixed',
                    'value': 1
                },
                'use_array': False,
                'is_buffer': False,
                'use_list': False,
                'is_string': False,
                'python_name_with_default': 'vi',
                'python_name_with_doc_default': 'vi',
                'is_repeated_capability': False,
                'is_session_handle': True,
                'interpreter_method_call_snippet': 'self._vi',
                'grpc_request_snippet': 'vi=self._vi',
                'use_in_python_api': True,
                'python_name_or_default_for_init': 'vi',
            },
            {
                'ctypes_method_call_snippet': 'status_ctype',
                'direction': 'out',
                'enum': None,
                'grpc_enum': None,
                'numpy': False,
                'name': 'status',
                'type': 'ViString',
                'documentation': {
                    'description': 'Return a device status'
                },
                'grpc_name': 'status',
                'python_name': 'status',
                'python_type': 'str',
                'type_in_documentation': 'str',
                'type_in_documentation_was_calculated': True,
                'ctypes_variable_name': 'status_ctype',
                'ctypes_type': 'ViString',
                'ctypes_type_library_call': 'ctypes.POINTER(ViChar)',
                'size': {
                    'mechanism': 'fixed',
                    'value': 1
                },
                'use_array': False,
                'is_buffer': False,
                'use_list': False,
                'is_string': True,
                'python_name_with_default': 'status',
                'python_name_with_doc_default': 'status',
                'is_repeated_capability': False,
                'is_session_handle': False,
                'interpreter_method_call_snippet': 'status',
                'grpc_request_snippet': 'status=status',
                'use_in_python_api': True,
                'python_name_or_default_for_init': 'status',
            },
            {
                'ctypes_method_call_snippet': 'data_buffer_size_ctype',
                'ctypes_type': 'ViInt32',
                'ctypes_variable_name': 'data_buffer_size_ctype',
                'ctypes_type_library_call': 'ViInt32',
                'direction': 'in',
                'documentation': {
                    'description': 'buffer size',
                },
                'is_repeated_capability': False,
                'is_session_handle': False,
                'enum': None,
                'grpc_enum': None,
                'numpy': False,
                'python_type': 'int',
                'type_in_documentation': 'int',
                'type_in_documentation_was_calculated': True,
                'use_array': False,
                'is_buffer': False,
                'use_list': False,
                'is_string': False,
                'name': 'dataBufferSize',
                'grpc_name': 'data_buffer_size',
                'python_name': 'data_buffer_size',
                'python_name_with_default': 'data_buffer_size',
                'python_name_with_doc_default': 'data_buffer_size',
                'size': {
                    'mechanism': 'fixed',
                    'value': 1
                },
                'type': 'ViInt32',
                'interpreter_method_call_snippet': 'data_buffer_size',
                'grpc_request_snippet': 'data_buffer_size=data_buffer_size',
                'use_in_python_api': False,
                'python_name_or_default_for_init': 'data_buffer_size',
            },
            {
                'ctypes_method_call_snippet': 'data_ctype',
                'ctypes_type': 'ViUInt32',
                'ctypes_variable_name': 'data_ctype',
                'ctypes_type_library_call': 'ctypes.POINTER(ViUInt32)',
                'direction': 'out',
                'documentation': {
                    'description': 'buffer',
                },
                'is_repeated_capability': False,
                'is_session_handle': False,
                'enum': None,
                'grpc_enum': None,
                'numpy': False,
                'python_type': 'int',
                'type_in_documentation': 'int',
                'type_in_documentation_was_calculated': True,
                'use_array': False,
                'is_buffer': True,
                'use_list': True,
                'is_string': False,
                'name': 'data',
                'original_type': 'ViUInt32[]',
                'grpc_name': 'data',
                'python_name': 'data',
                'python_name_with_default': 'data',
                'python_name_with_doc_default': 'data',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'dataBufferSize',
                },
                'type': 'ViUInt32',
                'interpreter_method_call_snippet': 'data',
                'grpc_request_snippet': 'data=data',
                'use_in_python_api': True,
                'python_name_or_default_for_init': 'data',
            },
        ],
        'documentation': {
            'description': 'Perform actions as method defined'
        },
        'name': 'MakeAPrivateMethod',
        'python_name': '_make_a_private_method',
        'interpreter_name': 'make_a_private_method',
        'is_error_handling': False,
        'render_in_session_base': False,
        'has_repeated_capability': False
    },
    'MakeANoCodegenMethod': {
        'name': 'MakeANoCodegenMethod',
        'codegen_method': 'no',
        'method_name_for_documentation': 'MakeAPublicMethod',
        'use_session_lock': True,
        'documentation': {
            'description': 'This is a method with codegen_method set to no'
        },
        'has_repeated_capability': False,
        'is_error_handling': False,
        'render_in_session_base': False,
        'method_templates': [
            {
                'session_filename': '/cool_template',
                'library_interpreter_filename': '/cool_template',
                'documentation_filename': '/cool_template',
                'method_python_name_suffix': ''
            }
        ],
        'parameters': [],
        'python_name': 'make_a_no_codegen_method',
        'interpreter_name': 'make_a_no_codegen_method',
        'returns': 'ViStatus',
    }
}


attributes_input = {
    1000000: {
        'access': 'read-write',
        'enum': None,
        'lv_property': 'Fake attributes:Read Write Bool',
        'name': 'READ_WRITE_BOOL',
        'type': 'ViBoolean',
        'documentation': {
            'description': 'An attribute of type bool with read/write access.',
        },
    },
}


attributes_expected = {
    1000000: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {'description': 'An attribute of type bool with read/write access.'},
        'enum': None,
        'grpc_enum': None,
        'lv_property': 'Fake attributes:Read Write Bool',
        'name': 'READ_WRITE_BOOL',
        'python_name': 'read_write_bool',
        'type': 'ViBoolean',
        'python_type': 'bool',
        'type_in_documentation': 'bool',
        'type_in_documentation_was_calculated': True,
        'attribute_class': 'AttributeViBoolean',
    },
}


enums_input = {
    'Color': {
        'values': [
            {
                'name': 'RED',
                'value': 1,
                'documentation': {
                    'description': 'Like blood.',
                }
            },
            {
                'name': 'BLUE',
                'value': 2,
                'documentation': {
                    'description': 'Like the sky.',
                }
            },
            {
                'name': 'YELLOW',
                'value': 2,
                'documentation': {
                    'description': 'Like a banana.',
                }
            },
            {
                'name': 'BLACK',
                'value': 2,
                'documentation': {
                    'description': 'Like this developer\'s conscience.',
                }
            },
        ],
    },
    'EnumWithConverter': {
        'codegen_method': 'private',
        'converted_value_to_enum_function_name': 'convert_to_enum_with_converter_enum',
        'enum_to_converted_value_function_name': 'convert_from_enum_with_converter_enum',
        'values': [
            {
                'converts_to_value': True,
                'name': 'RED',
                'value': 1
            },
            {
                'converts_to_value': False,
                'name': 'BLUE',
                'value': 2
            },
            {
                'converts_to_value': 'yellow',
                'name': 'YELLOW',
                'value': 5
            },
            {
                'converts_to_value': 42,
                'name': 'BLACK',
                'value': 42
            }
        ]
    },
    'EnumWithCommonPrefixInValueNames': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'COLOR_BRIGHT_RED',
                'value': 1
            },
            {
                'name': 'COLOR_BRIGHT_BLUE',
                'value': 2
            }
        ]
    },
    'EnumWithExplicitValueNames': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'THE_COLOR_RED',
                'python_name': 'COLOR_DARK_RED',
                'value': 1
            },
            {
                'name': 'THE_COLOR_BLUE',
                'python_name': 'COLOR_DARK_BLUE',
                'value': 2
            }
        ]
    },
    'EnumWithExplicitValueNamesMixedIn': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'DISTANCE_MILES',
                'value': 1
            },
            {
                'name': 'DISTANCE_KILOMETERS',
                'python_name': 'DISTANCE_KILOMETERS',
                'value': 2
            },
            {
                'name': 'DISTANCE_METERS',
                'python_name': 'DISTANCE_METERS',
                'value': 5
            },
            {
                'name': 'DISTANCE_YARDS',
                'value': 42
            }
        ]
    },
    'EnumWithOneExpandedValueAndCommonPrefixSuffix': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'COMMON_PREFIX_FOOTBALL_COMMON_SUFFIX',
                'value': 1
            },
            {
                'name': 'COMMON_PREFIX_BASEBALL',
                'python_name': 'BASEBALL',  # we want to test that this excludes it from common prefix/suffix calculations
                'value': 2
            },
            {
                'name': 'BASKETBALL_COMMON_SUFFIX',
                'python_name': 'BASKETBALL',  # we want to test that this excludes it from common prefix/suffix calculations
                'value': 3
            },
        ]
    },
}


enums_expected = {
    'Color': {
        'codegen_method': 'no',
        'python_name': 'Color',
        'values': [
            {'documentation': {'description': 'Like blood.'}, 'name': 'RED', 'value': 1, 'python_name': 'RED'},
            {'documentation': {'description': 'Like the sky.'}, 'name': 'BLUE', 'value': 2, 'python_name': 'BLUE'},
            {'documentation': {'description': 'Like a banana.'}, 'name': 'YELLOW', 'value': 2, 'python_name': 'YELLOW'},
            {'documentation': {'description': "Like this developer's conscience."}, 'name': 'BLACK', 'value': 2, 'python_name': 'BLACK'}
        ]
    },
    'EnumWithConverter': {
        'codegen_method': 'private',
        'python_name': '_EnumWithConverter',
        'converted_value_to_enum_function_name': 'convert_to_enum_with_converter_enum',
        'enum_to_converted_value_function_name': 'convert_from_enum_with_converter_enum',
        'values': [
            {'name': 'RED', 'value': 1, 'converts_to_value': True, 'python_name': 'RED'},
            {'name': 'BLUE', 'value': 2, 'converts_to_value': False, 'python_name': 'BLUE'},
            {'name': 'YELLOW', 'value': 5, 'converts_to_value': 'yellow', 'python_name': 'YELLOW'},
            {'name': 'BLACK', 'value': 42, 'converts_to_value': 42, 'python_name': 'BLACK'}
        ]
    },
    'EnumWithCommonPrefixInValueNames': {
        'codegen_method': 'public',
        'python_name': 'EnumWithCommonPrefixInValueNames',
        'values': [
            {'name': 'COLOR_BRIGHT_RED', 'value': 1, 'python_name': 'RED', 'prefix': 'COLOR_BRIGHT_'},
            {'name': 'COLOR_BRIGHT_BLUE', 'value': 2, 'python_name': 'BLUE', 'prefix': 'COLOR_BRIGHT_'}
        ]
    },
    'EnumWithExplicitValueNames': {
        'codegen_method': 'public',
        'python_name': 'EnumWithExplicitValueNames',
        'values': [
            {'name': 'THE_COLOR_RED', 'value': 1, 'python_name': 'COLOR_DARK_RED'},
            {'name': 'THE_COLOR_BLUE', 'value': 2, 'python_name': 'COLOR_DARK_BLUE'}
        ]
    },
    'EnumWithExplicitValueNamesMixedIn': {
        'codegen_method': 'public',
        'python_name': 'EnumWithExplicitValueNamesMixedIn',
        'values': [
            {'name': 'DISTANCE_MILES', 'value': 1, 'python_name': 'MILES', 'prefix': 'DISTANCE_'},
            {'name': 'DISTANCE_KILOMETERS', 'value': 2, 'python_name': 'DISTANCE_KILOMETERS'},  # explicitly set
            {'name': 'DISTANCE_METERS', 'value': 5, 'python_name': 'DISTANCE_METERS'},  # explicitly set
            {'name': 'DISTANCE_YARDS', 'value': 42, 'python_name': 'YARDS', 'prefix': 'DISTANCE_'}
        ]
    },
    'EnumWithOneExpandedValueAndCommonPrefixSuffix': {
        'codegen_method': 'public',
        'python_name': 'EnumWithOneExpandedValueAndCommonPrefixSuffix',
        'values': [
            {'name': 'COMMON_PREFIX_FOOTBALL_COMMON_SUFFIX', 'value': 1, 'python_name': 'COMMON_PREFIX_FOOTBALL_COMMON_SUFFIX'},
            {'name': 'COMMON_PREFIX_BASEBALL', 'value': 2, 'python_name': 'BASEBALL'},  # explicitly set
            {'name': 'BASKETBALL_COMMON_SUFFIX', 'value': 3, 'python_name': 'BASKETBALL'},  # explicitly set
        ]
    },
}


config_input = {
    'metadata_version': '1.0',
    'module_name': 'nifake',
    'module_version': '1.1.1.dev0',
    'c_function_prefix': 'niFake_',
    'driver_name': 'NI-FAKE',
    'session_class_description': 'An NI-FAKE session to a fake MI driver whose sole purpose is to test nimi-python code generation',
    'session_handle_parameter_name': 'vi',
    'library_info':
    {
        'Windows': {
            '32bit': {'name': 'nifake_32.dll', 'type': 'windll'},
            '64bit': {'name': 'nifake_64.dll', 'type': 'cdll'},
        },
        'Linux': {
            '64bit': {'name': 'libnifake.so', 'type': 'cdll'},
        },
    },
    'context_manager_name': {
        'task': 'acquisition',
        'initiate_function': 'Initiate',
        'abort_function': 'Abort',
    },
    'init_function': 'InitWithOptions',
    'close_function': 'close',
    'custom_types': [
        {
            'ctypes_type': 'struct_CustomStruct',
            'file_name': 'custom_struct',
            'grpc_name': 'CustomStruct',
            'python_name': 'CustomStruct',
        },
    ],
    'enum_whitelist_suffix': ['_POINT_FIVE'],
    'repeated_capabilities': [
        {'python_name': 'channels', 'prefix': '', },
    ],
    # These are added here strictly for testing.
    'functions': {},
    'attributes': {},
    'modules': {
        'metadata.enums_addon': {}
    },
}


config_expected = {
    'metadata_version': '1.0',
    'module_name': 'nifake',
    'module_version': '1.1.1.dev0',
    'c_function_prefix': 'niFake_',
    'driver_name': 'NI-FAKE',
    'session_class_description': 'An NI-FAKE session to a fake MI driver whose sole purpose is to test nimi-python code generation',
    'session_handle_parameter_name': 'vi',
    'library_info':
    {
        'Windows': {
            '32bit': {'name': 'nifake_32.dll', 'type': 'windll'},
            '64bit': {'name': 'nifake_64.dll', 'type': 'cdll'},
        },
        'Linux': {
            '64bit': {'name': 'libnifake.so', 'type': 'cdll'},
        },
    },
    'context_manager_name': {
        'task': 'acquisition',
        'initiate_function': 'Initiate',
        'abort_function': 'Abort',
    },
    'init_function': 'InitWithOptions',
    'close_function': 'close',
    'custom_types': [
        {
            'ctypes_type': 'struct_CustomStruct',
            'file_name': 'custom_struct',
            'grpc_name': 'CustomStruct',
            'python_name': 'CustomStruct',
        },
    ],
    'enum_whitelist_suffix': ['_POINT_FIVE'],
    'repeated_capabilities': [
        {'python_name': 'channels', 'prefix': '', },
    ],
    'use_locking': True,
    'functions': functions_expected,
    'attributes': attributes_expected,
    'enums': enums_expected,
    'modules': {
        'metadata.enums_addon': {}
    },
    'uses_nitclk': False,
}


def _do_the_test_add_functions_metadata(functions, expected):
    actual = copy.deepcopy(functions)
    actual = add_all_function_metadata(actual, config_input)
    _compare_dicts(actual, expected)


def test_add_functions_metadata_simple():
    _do_the_test_add_functions_metadata(functions=functions_input, expected=functions_expected)


def _do_the_test_add_attributes_metadata(attributes, expected):
    actual = copy.deepcopy(attributes)
    actual = add_all_attribute_metadata(actual, config_input)
    _compare_dicts(actual, expected)


def test_add_attributes_metadata_simple():
    _do_the_test_add_attributes_metadata(attributes=attributes_input, expected=attributes_expected)


def _do_the_test_add_enums_metadata(enums, expected):
    actual = copy.deepcopy(enums)
    actual = add_all_enum_metadata(actual, config_input)
    _compare_dicts(actual, expected)


def test_add_enums_metadata_simple():
    _do_the_test_add_enums_metadata(enums_input, expected=enums_expected)


def _do_the_test_add_all_metadata(functions, attributes, enums, config, expected):
    actual = add_all_metadata(functions, attributes, enums, config, persist_output=False)
    _compare_dicts(actual, expected)


def test_add_all_metadata_defaults():
    actual_functions = copy.deepcopy(functions_input)
    actual_attributes = copy.deepcopy(attributes_input)
    actual_enums = copy.deepcopy(enums_input)
    actual_config = copy.deepcopy(config_input)
    _do_the_test_add_all_metadata(
        functions=actual_functions,
        attributes=actual_attributes,
        enums=actual_enums,
        config=actual_config,
        expected=config_expected)


def test_add_all_metadata():
    actual_functions = copy.deepcopy(functions_input)
    actual_attributes = copy.deepcopy(attributes_input)
    actual_enums = copy.deepcopy(enums_input)
    actual_config = copy.deepcopy(config_input)
    actual_config['use_locking'] = False
    expected = copy.deepcopy(config_expected)
    expected['use_locking'] = False
    _do_the_test_add_all_metadata(
        functions=actual_functions,
        attributes=actual_attributes,
        enums=actual_enums,
        config=actual_config,
        expected=expected)


def _setup_inputs_for_enum_codegen_method_tests():
    actual_enums = copy.deepcopy(enums_input)
    actual_config = copy.deepcopy(config_input)
    # Set up minimal input functions metadata
    actual_config['functions'] = {
        'PublicMethod': {
            'codegen_method': 'public',
            'parameters': [{'enum': None}, {'enum': 'EnumWithConverter'}],
        },
        'PythonOnlyMethod': {
            'codegen_method': 'python-only',
            'parameters': [{'enum': 'Color'}, {'enum': None}],
        },
        'PrivateMethod': {
            'codegen_method': 'private',
            'parameters': [{'enum': 'EnumWithConverter'}],
        },
        'NoCodegenMethod': {
            'codegen_method': 'no',
            'parameters': [{'enum': 'Color'}],
        },
    }
    # Set up minimal input attributes metadata
    actual_config['attributes'] = {
        '1000000': {'codegen_method': 'public', 'name': 'PUBLIC_ATTR', 'enum': None},
        '1000001': {'codegen_method': 'public', 'name': 'PUBLIC_ATTR_2', 'enum': 'EnumWithConverter'},
        '1000002': {'codegen_method': 'private', 'name': 'PRIVATE_ATTR', 'enum': 'Color'},
        '1000003': {'codegen_method': 'private', 'name': 'PRIVATE_ATTR_2', 'enum': 'EnumWithConverter'},
        '1000004': {'codegen_method': 'no', 'name': 'NO_CODEGEN_ATTR', 'enum': 'Color'},
    }
    return actual_enums, actual_config


def test_add_enum_codegen_method():
    actual_enums, actual_config = _setup_inputs_for_enum_codegen_method_tests()
    _add_enum_codegen_method(actual_enums, actual_config)
    assert actual_enums['Color']['codegen_method'] == 'public'
    assert actual_enums['EnumWithConverter']['codegen_method'] == 'private'


def test_add_enum_codegen_method_error():
    actual_enums, actual_config = _setup_inputs_for_enum_codegen_method_tests()
    actual_enums['Color']['codegen_method'] = 'private'
    expected_error_description = "Codegen_method of enum Color used by functions ['PythonOnlyMethod'] and attributes ['PRIVATE_ATTR'] must be public, is private"
    try:
        _add_enum_codegen_method(actual_enums, actual_config)
    except ValueError as actual_error:
        actual_error_message = actual_error.args[0]
        assert actual_error_message == expected_error_description


def test_get_functions_that_use_enums():
    actual_enums, actual_config = _setup_inputs_for_enum_codegen_method_tests()
    expected_output = {
        'Color': ['PythonOnlyMethod'],
        'EnumWithConverter': ['PublicMethod', 'PrivateMethod'],
        'EnumWithCommonPrefixInValueNames': [],
        'EnumWithExplicitValueNames': [],
        'EnumWithExplicitValueNamesMixedIn': [],
        'EnumWithOneExpandedValueAndCommonPrefixSuffix': [],
    }
    actual_output = _get_functions_that_use_enums(actual_enums, actual_config)
    _compare_dicts(actual_output, expected_output)


def test_get_attributes_that_use_enums():
    actual_enums, actual_config = _setup_inputs_for_enum_codegen_method_tests()
    expected_output = {
        'Color': ['1000002'],
        'EnumWithConverter': ['1000001', '1000003'],
        'EnumWithCommonPrefixInValueNames': [],
        'EnumWithExplicitValueNames': [],
        'EnumWithExplicitValueNamesMixedIn': [],
        'EnumWithOneExpandedValueAndCommonPrefixSuffix': [],
    }
    actual_output = _get_attributes_that_use_enums(actual_enums, actual_config)
    _compare_dicts(actual_output, expected_output)


def test_get_least_restrictive_codegen_method():
    for codegen_methods, expected_least_restrictive_codegen_method in (
        ([], 'no'),
        (['no'], 'no'),
        (['private', 'private'], 'private'),
        (['no', 'private'], 'private'),
        (['public', 'private'], 'public'),
        (['private', 'python-only', 'private', 'no'], 'public'),
        (['public', 'python-only', 'public'], 'public')
    ):
        assert _get_least_restrictive_codegen_method(
            codegen_methods
        ) == expected_least_restrictive_codegen_method
