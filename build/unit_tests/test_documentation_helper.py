from build.helper.documentation_helper import *


def _remove_trailing_whitespace(s):
    '''Removes trailing whitespace and empty lines in multi-line strings.'''
    initial_lines = s.strip().splitlines()
    fixed_lines = []
    blank_lines = 0
    for line in initial_lines:
        stripped_line = line.strip()
        if len(stripped_line) == 0 and blank_lines == 0:
            fixed_lines.append(stripped_line)
            blank_lines = 1
        if len(stripped_line) > 0:
            fixed_lines.append(stripped_line)
            blank_lines = 0

    return fixed_lines


def assert_rst_strings_are_equal(expected, actual):
    '''Asserts rst formatted strings (multiline) are equal. Ignores trailing whitespace and empty lines.'''
    expected = _remove_trailing_whitespace(expected)
    actual = _remove_trailing_whitespace(actual)
    for expected_line, actual_line in zip(expected, actual):
        assert expected_line == actual_line, 'Difference found:\n{0}\n{1}'.format(expected_line, actual_line)


config = {
    'functions': {
        'GetTurtleID': {
            'codegen_method': 'public',
            'returns': 'ViStatus',
            'method_templates': [{'filename': '/default_method', 'method_python_name_suffix': '', }, ],
            'parameters': [
                {
                    'direction': 'in',
                    'enum': None,
                    'name': 'vi',
                    'type': 'ViSession',
                    'documentation': {
                        'description': 'Identifies a particular instrument session.'
                    },
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
                    'is_buffer': False,
                    'is_string': False,
                    'use_list': False,
                    'use_array': False,
                    'python_name_with_default': 'vi',
                    'python_name_with_doc_default': 'vi',
                    'is_repeated_capability': False,
                    'is_session_handle': True,
                    'interpreter_method_call_snippet': 'self._vi',
                    'use_in_python_api': True,
                },
                {
                    'direction': 'in',
                    'enum': 'Turtle',
                    'name': 'turtleType',
                    'type': 'ViInt32',
                    'documentation': {
                        'description': '''Specifies the type of Turtle type
wanted to choose.''',
                        'note': 'You wont be able to import NIFAKE_VAL_RAPHAEL',
                        'table_body': [
                            ['NIFAKE_VAL_LEONARDO (default)', '0', 'LEONARDO'],
                            ['NIFAKE_VAL_DONATELLO', '1', 'DONATELLO'],
                            ['NIFAKE_VAL_RAPHAEL', '2', 'RAPHAEL'],
                            ['NIFAKE_VAL_MICHELANGELO', '3', 'MICHELANGELO']
                        ]
                    },
                    'python_name': 'turtle_type',
                    'python_type': 'Turtle',
                    'type_in_documentation': 'Turtle',
                    'type_in_documentation_was_calculated': True,
                    'ctypes_variable_name': 'turtle_type_ctype',
                    'ctypes_type': 'ViInt32',
                    'ctypes_type_library_call': 'ViInt32',
                    'size': {
                        'mechanism': 'fixed',
                        'value': 1
                    },
                    'is_buffer': False,
                    'is_string': False,
                    'use_list': False,
                    'use_array': False,
                    'python_name_with_default': 'turtle_type',
                    'python_name_with_doc_default': 'turtle_type',
                    'is_repeated_capability': False,
                    'is_session_handle': False,
                    'interpreter_method_call_snippet': 'turtle_type',
                    'use_in_python_api': True,
                },
                {
                    'direction': 'out',
                    'enum': None,
                    'name': 'turtleId',
                    'type': 'ViReal64',
                    'documentation': {
                        'description': 'Returns the **ID** of selected turtle.'
                    },
                    'python_name': 'turtle_id',
                    'python_type': 'float',
                    'type_in_documentation': 'float',
                    'type_in_documentation_was_calculated': True,
                    'ctypes_variable_name': 'turtleId_ctype',
                    'ctypes_type': 'ViReal64',
                    'ctypes_type_library_call': 'ctypes.POINTER(ViReal64)',
                    'size': {
                        'mechanism': 'fixed',
                        'value': 1
                    },
                    'is_buffer': False,
                    'is_string': False,
                    'use_list': False,
                    'use_array': False,
                    'python_name_with_default': 'turtleId',
                    'python_name_with_doc_default': 'turtleId',
                    'is_repeated_capability': False,
                    'is_session_handle': False,
                    'interpreter_method_call_snippet': 'ctypes.pointer(turtleId_ctype)',
                    'use_in_python_api': True,
                }
            ],
            'documentation': {
                'description': 'Returns the **ID** of selected Turtle Type. See `NIFAKE help <REPLACE_DRIVER_SPECIFIC_URL_1(fake_functional_overview)>`__',
                'note': [
                    'The NIFAKE_VAL_RAPHAEL Turtles dont have an ID.',
                    'DO NOT call niFake_FetchWaveform after calling this function.',
                    'NIFAKE_ATTR_READ_WRITE_BOOL will have an incorrect value after this calling this function',
                ]
            },
            'name': 'GetTurtleID',
            'python_name': 'get_turtle_id',
            'interpreter_name': 'get_turtle_id',
            'is_error_handling': False,
            'has_repeated_capability': False
        },
        'FetchWaveform': {
            'codegen_method': 'public',
            'documentation': {'description': 'Returns waveform data.'},
            'has_repeated_capability': False,
            'is_error_handling': False,
            'method_templates': [{'filename': '/default_method', 'method_python_name_suffix': ''}, {'filename': '/numpy_method', 'method_python_name_suffix': '_into'}],
            'name': 'FetchWaveform',
            'parameters': [
                {
                    'ctypes_type': 'ViSession',
                    'ctypes_type_library_call': 'ViSession',
                    'ctypes_variable_name': 'vi_ctype',
                    'direction': 'in',
                    'documentation': {'description': 'Identifies a particular instrument session.'},
                    'enum': None,
                    'is_buffer': False,
                    'is_string': False,
                    'use_list': False,
                    'use_array': False,
                    'is_repeated_capability': False,
                    'is_session_handle': True,
                    'interpreter_method_call_snippet': 'vi_ctype',
                    'name': 'vi',
                    'numpy': False,
                    'python_name': 'vi',
                    'python_name_with_default': 'vi',
                    'python_name_with_doc_default': 'vi',
                    'python_type': 'int',
                    'type_in_documentation': 'int',
                    'type_in_documentation_was_calculated': True,
                    'size': {'mechanism': 'fixed', 'value': 1},
                    'type': 'ViSession',
                    'use_in_python_api': True,
                },
                {
                    'ctypes_type': 'ViInt32',
                    'ctypes_type_library_call': 'ViInt32',
                    'ctypes_variable_name': 'number_of_samples_ctype',
                    'direction': 'in',
                    'documentation': {'description': 'Number of samples to return'},
                    'enum': None,
                    'is_buffer': False,
                    'is_string': False,
                    'use_list': False,
                    'use_array': False,
                    'is_repeated_capability': False,
                    'is_session_handle': False,
                    'interpreter_method_call_snippet': 'number_of_samples_ctype',
                    'name': 'numberOfSamples',
                    'numpy': False,
                    'python_name': 'number_of_samples',
                    'python_name_with_default': 'number_of_samples',
                    'python_name_with_doc_default': 'number_of_samples',
                    'python_type': 'int',
                    'type_in_documentation': 'int',
                    'type_in_documentation_was_calculated': True,
                    'size': {'mechanism': 'fixed', 'value': 1},
                    'type': 'ViInt32',
                    'use_in_python_api': True,
                },
                {
                    'ctypes_type': 'ViReal64',
                    'ctypes_type_library_call': 'ctypes.POINTER(ViReal64)',
                    'ctypes_variable_name': 'waveform_data_ctype',
                    'direction': 'out',
                    'documentation': {'description': 'Samples fetched from the device. Array should be numberOfSamples big.'},
                    'enum': None,
                    'is_buffer': True,
                    'is_string': False,
                    'use_list': False,
                    'use_array': True,
                    'is_repeated_capability': False,
                    'is_session_handle': False,
                    'interpreter_method_call_snippet': 'waveform_data_ctype',
                    'name': 'waveformData',
                    'numpy': True,
                    'numpy_type': 'float64',
                    'original_type': 'ViReal64[]',
                    'python_name': 'waveform_data',
                    'python_name_with_default': 'waveform_data',
                    'python_name_with_doc_default': 'waveform_data',
                    'python_type': 'float',
                    'type_in_documentation': 'float',
                    'type_in_documentation_was_calculated': True,
                    'size': {'mechanism': 'passed-in', 'value': 'numberOfSamples'},
                    'type': 'ViReal64',
                    'use_in_python_api': True,
                },
                {
                    'ctypes_type': 'ViInt32',
                    'ctypes_type_library_call': 'ctypes.POINTER(ViInt32)',
                    'ctypes_variable_name': 'actual_number_of_samples_ctype',
                    'direction': 'out',
                    'documentation': {'description': 'Number of samples actually fetched.'},
                    'enum': None,
                    'is_buffer': False,
                    'is_string': False,
                    'use_list': False,
                    'use_array': False,
                    'is_repeated_capability': False,
                    'is_session_handle': False,
                    'interpreter_method_call_snippet': 'ctypes.pointer(actual_number_of_samples_ctype)',
                    'name': 'actualNumberOfSamples',
                    'numpy': False,
                    'python_name': 'actual_number_of_samples',
                    'python_name_with_default': 'actual_number_of_samples',
                    'python_name_with_doc_default': 'actual_number_of_samples',
                    'python_type': 'int',
                    'type_in_documentation': 'int',
                    'type_in_documentation_was_calculated': True,
                    'size': {'mechanism': 'fixed', 'value': 1},
                    'type': 'ViInt32',
                    'use_in_python_api': True,
                }
            ],
            'python_name': 'fetch_waveform',
            'interpreter_name': 'fetch_waveform',
            'render_in_session_base': False,
            'returns': 'ViStatus'
        },
    },
    'metadata_version': '1.0',
    'module_name': 'nifake',
    'module_version': '0.3.0.dev0',
    'c_function_prefix': 'niFake_',
    'driver_name': 'NI-FAKE',
    'session_class_description': 'An NI-FAKE session to a fake MI driver whose sole purpose is to test nimi-python code generation',
    'session_handle_parameter_name': 'vi',
    'driver_urls': {
        'REPLACE_DRIVER_SPECIFIC_URL_1': 'http://zone.ni.com/reference/en-XX/help/370384T-01/fake/{0}/',
    },
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
    'attributes': {
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
    },
    'enums': {
        'Turtle': {
            'codegen_method': 'public',
            'python_name': 'Turtle',
            'values': [
                {
                    'name': 'NIFAKE_VAL_LEONARDO',
                    'python_name': 'LEONARDO',
                    'value': 0,
                    'documentation': {
                        'description': 'Wields two katanas.',
                    }
                },
                {
                    'name': 'NIFAKE_VAL_DONATELLO',
                    'python_name': 'DONATELLO',
                    'value': 1,
                    'documentation': {
                        'description': 'Uses a bo staff.',
                    }
                },
                {
                    'name': 'NIFAKE_VAL_RAPHAEL',
                    'python_name': 'RAPHAEL',
                    'value': 2,
                    'documentation': {
                        'description': 'Has a pair of sai.',
                    }
                },
                {
                    'name': 'NIFAKE_VAL_MICHELANGELO',
                    'python_name': 'MICHELANGELO',
                    'value': 3,
                    'documentation': {
                        'description': 'Owns nunchucks.',
                    }
                },
            ],
        },
    },
}


def test_get_function_rst_default():
    function = config['functions']['GetTurtleID']
    method_template = function['method_templates'][0]
    actual_function_rst = get_function_rst(function, method_template=method_template, numpy=False, config=config, indent=0)
    expected_fuction_rst = '''.. py:method:: get_turtle_id(turtle_type)

    Returns the **ID** of selected Turtle Type. See `NIFAKE help <http://zone.ni.com/reference/en-XX/help/370384T-01/fake/fake_functional_overview/>`__

    .. note:: The :py:data:`~nifake.Turtle.RAPHAEL` Turtles dont have an ID.

    .. note:: DO NOT call :py:meth:`nifake.Session.fetch_waveform` after calling this method.

    .. note:: :py:attr:`nifake.Session.read_write_bool` will have an incorrect value after this calling this method

    :param turtle_type:

    Specifies the type of Turtle type
    wanted to choose.

    +----------------------------------------------+---+--------------+
    | :py:data:`~nifake.Turtle.LEONARDO` (default) | 0 | LEONARDO     |
    +----------------------------------------------+---+--------------+
    | :py:data:`~nifake.Turtle.DONATELLO`          | 1 | DONATELLO    |
    +----------------------------------------------+---+--------------+
    | :py:data:`~nifake.Turtle.RAPHAEL`            | 2 | RAPHAEL      |
    +----------------------------------------------+---+--------------+
    | :py:data:`~nifake.Turtle.MICHELANGELO`       | 3 | MICHELANGELO |
    +----------------------------------------------+---+--------------+

    .. note:: You wont be able to import :py:data:`~nifake.Turtle.RAPHAEL`

    :type turtle_type: :py:data:`nifake.Turtle`

    :rtype: float
    :return:

        Returns the **ID** of selected turtle.
'''
    assert_rst_strings_are_equal(expected_fuction_rst, actual_function_rst)


def test_get_function_rst_numpy():
    function = config['functions']['FetchWaveform']
    method_template = function['method_templates'][0]
    actual_function_rst = get_function_rst(function, method_template=method_template, numpy=True, config=config, indent=0)
    expected_fuction_rst = '''.. py:method:: fetch_waveform(number_of_samples)

    Returns waveform data.

    :param number_of_samples:

        Number of samples to return

    :type number_of_samples: int
    :param waveform_data:

        Samples fetched from the device. Array should be numberOfSamples big.

    :type waveform_data: numpy.array(dtype=numpy.float64)

    :rtype: int
    :return:

        Number of samples actually fetched.
'''
    assert_rst_strings_are_equal(expected_fuction_rst, actual_function_rst)


def test_get_attribute_repeated_caps():
    attr = {'supported_rep_caps': ['channels', 'instruments', 'pins']}
    expected_caps = 'channels, instruments, pins'
    actual_caps = get_attribute_repeated_caps(attr)
    assert actual_caps == expected_caps

    attr = {'supported_rep_caps': ['channels']}
    expected_caps = 'channels'
    actual_caps = get_attribute_repeated_caps(attr)
    assert actual_caps == expected_caps

    attr = {'supported_rep_caps': []}
    expected_caps = 'None'
    actual_caps = get_attribute_repeated_caps(attr)
    assert actual_caps == expected_caps

    attr = {}
    expected_caps = 'None'
    actual_caps = get_attribute_repeated_caps(attr)
    assert actual_caps == expected_caps


def test_get_attribute_repeated_caps_with_conjunction():
    attr = {'supported_rep_caps': ['channels', 'instruments', 'pins']}
    expected_caps = 'channels, instruments or pins'
    actual_caps = get_attribute_repeated_caps_with_conjunction(attr)
    assert actual_caps == expected_caps

    attr = {'supported_rep_caps': ['channels', 'instruments']}
    expected_caps = 'channels or instruments'
    actual_caps = get_attribute_repeated_caps_with_conjunction(attr)
    assert actual_caps == expected_caps

    attr = {'supported_rep_caps': ['channels']}
    expected_caps = 'channels'
    actual_caps = get_attribute_repeated_caps_with_conjunction(attr)
    assert actual_caps == expected_caps

    attr = {'supported_rep_caps': []}
    expected_caps = 'None'
    actual_caps = get_attribute_repeated_caps_with_conjunction(attr)
    assert actual_caps == expected_caps


def test_module_supports_repeated_caps():
    config = {'repeated_capabilities': [{'python_name': 'channels'}]}
    expected_value = True
    actual_value = module_supports_repeated_caps(config)
    assert actual_value == expected_value

    config = {'repeated_capabilities': []}
    expected_value = False
    actual_value = module_supports_repeated_caps(config)
    assert actual_value == expected_value

    config = {}
    expected_value = False
    actual_value = module_supports_repeated_caps(config)
    assert actual_value == expected_value


def test_get_function_docstring_default():
    function = config['functions']['GetTurtleID']
    actual_function_docstring = get_function_docstring(function, numpy=False, config=config, indent=0)
    expected_function_docstring = '''Returns the **ID** of selected Turtle Type. See `NIFAKE help <fake_functional_overview>`__

Note: The Turtle.RAPHAEL Turtles dont have an ID.

Note: DO NOT call fetch_waveform after calling this method.

Note: read_write_bool will have an incorrect value after this calling this method

Args:
    turtle_type (Turtle): Specifies the type of Turtle type
        wanted to choose.

        +---------------------------+---+--------------+
        | Turtle.LEONARDO (default) | 0 | LEONARDO     |
        +---------------------------+---+--------------+
        | Turtle.DONATELLO          | 1 | DONATELLO    |
        +---------------------------+---+--------------+
        | Turtle.RAPHAEL            | 2 | RAPHAEL      |
        +---------------------------+---+--------------+
        | Turtle.MICHELANGELO       | 3 | MICHELANGELO |
        +---------------------------+---+--------------+

        Note: You wont be able to import Turtle.RAPHAEL

Returns:
    turtle_id (float): Returns the **ID** of selected turtle.''' # noqa
    assert_rst_strings_are_equal(expected_function_docstring, actual_function_docstring)


def test_get_function_docstring_numpy():
    function = config['functions']['FetchWaveform']
    actual_function_docstring = get_function_docstring(function, numpy=True, config=config, indent=0)
    expected_fuction_docstring = '''Returns waveform data.

    Args:
        number_of_samples (int): Number of samples to return

        waveform_data (numpy.array(dtype=numpy.float64)): Samples fetched from the device. Array should be numberOfSamples big.

    Returns:
        actual_number_of_samples (int): Number of samples actually fetched.
'''
    assert_rst_strings_are_equal(expected_fuction_docstring, actual_function_docstring)


def test_get_rst_header_snippet():
    header = "This will be your method header"
    actual_rst_header = get_rst_header_snippet(header)
    expected_rst_header = """This will be your method header
==============================="""
    assert actual_rst_header == expected_rst_header


def test_get_documentation_for_node_docstring():
    caution = """ this is a very
long string if I had the
energy to type more and more ..."""
    description = """ This string might be
at maximum size I can handle"""
    node = {
        'documentation': {
            'caution': caution,
            'description': description,
            'table_header': ['what', 'how', 'who'],
            'table_body': [
                ['lorem', 'that is a dummy string', 'Place holder string'],
                ['ipsum', 'this is a random strinf', 'Yes, I am a random string']
            ]
        }
    }
    actual_documentation = get_documentation_for_node_docstring(node, config, indent=4)
    expected_documentation = """Caution:  this is a very
    long string if I had the
    energy to type more and more ...

    This string might be
    at maximum size I can handle

    +-------+-------------------------+---------------------------+
    | what  | how                     | who                       |
    +=======+=========================+===========================+
    | lorem | that is a dummy string  | Place holder string       |
    +-------+-------------------------+---------------------------+
    | ipsum | this is a random strinf | Yes, I am a random string |
    +-------+-------------------------+---------------------------+""" # noqa
    assert_rst_strings_are_equal(expected_documentation, actual_documentation)


def test_get_rst_picture_reference():
    actual_pic_ref = get_rst_picture_reference('test1', 'test2', 'test3', 'test4')
    expected_pic_ref = """
    .. |test1| image:: test2
        :alt: test3
        :target: test4
    """
    assert_rst_strings_are_equal(expected_pic_ref, actual_pic_ref)


def test_square_up_tables():
    local_config = config_for_testing.copy()
    functions = {
        'MakeAFoo': {
            'codegen_method': 'public',
            'returns': 'ViStatus',
            'method_templates': [{'session_filename': '/cool_template', 'documentation_filename': '/cool_template', 'method_python_name_suffix': '', }, ],
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
                    'type': 'ViString',
                    'documentation': {
                        'description': 'The channel to call this on.',
                    },
                },
            ],
            'documentation': {
                'description': 'Performs a foo, and performs it well.',
                'table_header': ['Just one'],
                'table_body': [['Just', 'two'], ['this', 'has', 'three']],
            },
        },
    }
    local_config['functions'] = functions
    local_config['attributes'] = {}
    local_config['enums'] = {}

    square_up_tables(local_config)
    assert len(local_config['functions']['MakeAFoo']['documentation']['table_header']) == 3
    for line in local_config['functions']['MakeAFoo']['documentation']['table_body']:
        assert len(line) == 3


config_for_testing = {
    'session_handle_parameter_name': 'vi',
    'module_name': 'nifake',
    'functions': {},
    'attributes': {},
    'modules': {
        'metadata.enums_addon': {}
    },
    'custom_types': [],
}


def test_add_notes_re_links():
    local_config = config_for_testing.copy()
    local_config['c_function_prefix'] = 'niFake'
    functions = {
        'MakeAFoo': {
            'codegen_method': 'public',
            'returns': 'ViStatus',
            'method_templates': [{'session_filename': '/cool_template', 'documentation_filename': '/cool_template', 'method_python_name_suffix': '', }, ],
            'parameters': [
                {
                    'direction': 'in',
                    'enum': None,
                    'name': 'vi',
                    'type': 'ViSession',
                    'documentation': {
                        'description': 'Identifies a particular instrument session for niFake_MakeAFoo using NIFAKE_ATTR_READ_WRITE_BOOL. You should use NIFAKE_VAL_BLUE',
                    },
                },
                {
                    'direction': 'in',
                    'enum': None,
                    'name': 'channelName',
                    'type': 'ViString',
                    'documentation': {
                        'description': 'The channel to call this on. Similar to niFake_TakeAFoo using NIFAKE_ATTR_NOT_HERE. Use NIFAKE_VAL_PURPLE',
                    },
                },
            ],
            'documentation': {
                'description': 'Performs a foo, and performs it well.',
            },
            'python_name': 'make_a_foo',
            'interpreter_name': 'make_a_foo',
        },
    }
    attributes = {
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
    enums = {
        'Color': {
            'values': [
                {
                    'name': 'NIFAKE_VAL_RED',
                    'value': 1,
                    'documentation': {
                        'description': 'Like blood.',
                    }
                },
                {
                    'name': 'NIFAKE_VAL_BLUE',
                    'value': 2,
                    'documentation': {
                        'description': 'Like the sky.',
                    }
                },
                {
                    'name': 'NIFAKE_VAL_YELLOW',
                    'value': 2,
                    'documentation': {
                        'description': 'Like a banana.',
                    }
                },
                {
                    'name': 'NIFAKE_VAL_BLACK',
                    'value': 2,
                    'documentation': {
                        'description': 'Like this developer\'s conscience.',
                    }
                },
            ],
            'codegen_method': 'public',
        },
    }
    local_config['functions'] = functions
    local_config['attributes'] = attributes
    local_config['enums'] = enums

    add_notes_re_links(local_config)

    assert 'note' not in local_config['functions']['MakeAFoo']['parameters'][0]['documentation']
    assert func_note_text in local_config['functions']['MakeAFoo']['parameters'][1]['documentation']['note']
    assert attr_note_text in local_config['functions']['MakeAFoo']['parameters'][1]['documentation']['note']
    assert enum_note_text in local_config['functions']['MakeAFoo']['parameters'][1]['documentation']['note']


def test_get_repeated_capability_single_index_python_example():
    basic_rep_cap = {'prefix': '', 'python_name': 'channels'}
    basic_snippet = 'session.channels[0].channel_enabled = True'
    basic_explanation = 'sets :py:attr:`channel_enabled` to :python:`True` for channels 0.'
    assert (basic_snippet, basic_explanation) == get_repeated_capability_single_index_python_example(basic_rep_cap)

    property_with_string_val_rep_cap = {
        'attr_for_docs_example': 'exported_pattern_opcode_event_output_terminal',
        'attr_type_for_docs_example': 'property',
        'prefix': 'patternOpcodeEvent',
        'python_name': 'pattern_opcode_events',
        'value_for_docs_example': '/Dev1/PXI_Trig0',
    }
    property_with_string_val_snippet = "session.pattern_opcode_events[0].exported_pattern_opcode_event_output_terminal = '/Dev1/PXI_Trig0'"
    property_with_string_val_explanation = "sets :py:attr:`exported_pattern_opcode_event_output_terminal` to :python:`'/Dev1/PXI_Trig0'` for pattern_opcode_events 0."
    assert (property_with_string_val_snippet, property_with_string_val_explanation) == get_repeated_capability_single_index_python_example(property_with_string_val_rep_cap)

    string_indices_with_numerical_val_rep_cap = {
        'attr_for_docs_example': 'vil',
        'attr_type_for_docs_example': 'property',
        'prefix': '',
        'python_name': 'pins',
        'string_indices_for_docs_example': ["PinA", "PinB", "CPin"],
        'value_for_docs_example': 2,
    }
    string_indices_with_numerical_val_snippet = "session.pins['PinA'].vil = 2"
    string_indices_with_numerical_val_explanation = "sets :py:attr:`vil` to :python:`2` for pins 'PinA'."
    assert (string_indices_with_numerical_val_snippet, string_indices_with_numerical_val_explanation) == get_repeated_capability_single_index_python_example(string_indices_with_numerical_val_rep_cap)

    method_no_val_rep_cap = {
        'attr_for_docs_example': 'disable_sites',
        'attr_type_for_docs_example': 'method',
        'prefix': 'site',
        'python_name': 'sites',
        'value_for_docs_example': None,
    }
    method_no_val_snippet = "session.sites[0].disable_sites()"
    method_no_val_explanation = "calls :py:meth:`disable_sites` for sites 0."
    assert (method_no_val_snippet, method_no_val_explanation) == get_repeated_capability_single_index_python_example(method_no_val_rep_cap)

    property_no_val_rep_cap = {
        'attr_for_docs_example': 'serial_number',
        'attr_type_for_docs_example': 'property',
        'prefix': '',
        'python_name': 'instruments',
        'string_indices_for_docs_example': ["Dev1", "Dev2", "3rdDevice"],
        'value_for_docs_example': None,
    }
    property_no_val_snippet = "print(session.instruments['Dev1'].serial_number)"
    property_no_val_explanation = "prints :py:attr:`serial_number` for instruments 'Dev1'."
    assert (property_no_val_snippet, property_no_val_explanation) == get_repeated_capability_single_index_python_example(property_no_val_rep_cap)

    enum_val_rep_cap = {
        'attr_for_docs_example': 'conditional_jump_trigger_type',
        'attr_type_for_docs_example': 'property',
        'prefix': 'conditionalJumpTrigger',
        'python_name': 'conditional_jump_triggers',
        'value_for_docs_example': 'nidigital.TriggerType.DIGITAL_EDGE',
        'value_type_for_docs_example': 'enum',
    }
    enum_val_snippet = "session.conditional_jump_triggers[0].conditional_jump_trigger_type = nidigital.TriggerType.DIGITAL_EDGE"
    enum_val_explanation = "sets :py:attr:`conditional_jump_trigger_type` to :py:data:`~nidigital.TriggerType.DIGITAL_EDGE` for conditional_jump_triggers 0."
    assert (enum_val_snippet, enum_val_explanation) == get_repeated_capability_single_index_python_example(enum_val_rep_cap)


def test_get_repeated_capability_tuple_index_python_example():
    basic_rep_cap = {'prefix': '', 'python_name': 'channels'}
    basic_snippet = 'session.channels[0, 2].channel_enabled = True'
    basic_explanation = 'sets :py:attr:`channel_enabled` to :python:`True` for channels 0, 2.'
    assert (basic_snippet, basic_explanation) == get_repeated_capability_tuple_index_python_example(basic_rep_cap)

    property_with_string_val_rep_cap = {
        'attr_for_docs_example': 'exported_pattern_opcode_event_output_terminal',
        'attr_type_for_docs_example': 'property',
        'prefix': 'patternOpcodeEvent',
        'python_name': 'pattern_opcode_events',
        'value_for_docs_example': '/Dev1/PXI_Trig0',
    }
    property_with_string_val_snippet = "session.pattern_opcode_events[0, 2].exported_pattern_opcode_event_output_terminal = '/Dev1/PXI_Trig0'"
    property_with_string_val_explanation = "sets :py:attr:`exported_pattern_opcode_event_output_terminal` to :python:`'/Dev1/PXI_Trig0'` for pattern_opcode_events 0, 2."
    assert (property_with_string_val_snippet, property_with_string_val_explanation) == get_repeated_capability_tuple_index_python_example(property_with_string_val_rep_cap)

    string_indices_with_numerical_val_rep_cap = {
        'attr_for_docs_example': 'vil',
        'attr_type_for_docs_example': 'property',
        'prefix': '',
        'python_name': 'pins',
        'string_indices_for_docs_example': ["PinA", "PinB", "CPin"],
        'value_for_docs_example': 2,
    }
    string_indices_with_numerical_val_snippet = "session.pins['PinA', 'PinB', 'CPin'].vil = 2"
    string_indices_with_numerical_val_explanation = "sets :py:attr:`vil` to :python:`2` for pins 'PinA', 'PinB', 'CPin'."
    assert (string_indices_with_numerical_val_snippet, string_indices_with_numerical_val_explanation) == get_repeated_capability_tuple_index_python_example(string_indices_with_numerical_val_rep_cap)

    method_no_val_rep_cap = {
        'attr_for_docs_example': 'disable_sites',
        'attr_type_for_docs_example': 'method',
        'prefix': 'site',
        'python_name': 'sites',
        'value_for_docs_example': None,
    }
    method_no_val_snippet = "session.sites[0, 2].disable_sites()"
    method_no_val_explanation = "calls :py:meth:`disable_sites` for sites 0, 2."
    assert (method_no_val_snippet, method_no_val_explanation) == get_repeated_capability_tuple_index_python_example(method_no_val_rep_cap)

    property_no_val_rep_cap = {
        'attr_for_docs_example': 'serial_number',
        'attr_type_for_docs_example': 'property',
        'prefix': '',
        'python_name': 'instruments',
        'string_indices_for_docs_example': ["Dev1", "Dev2", "3rdDevice"],
        'value_for_docs_example': None,
    }
    property_no_val_snippet = "print(session.instruments['Dev1', 'Dev2', '3rdDevice'].serial_number)"
    property_no_val_explanation = "prints :py:attr:`serial_number` for instruments 'Dev1', 'Dev2', '3rdDevice' or errors if the value is not the same for all."
    assert (property_no_val_snippet, property_no_val_explanation) == get_repeated_capability_tuple_index_python_example(property_no_val_rep_cap)

    enum_val_rep_cap = {
        'attr_for_docs_example': 'conditional_jump_trigger_type',
        'attr_type_for_docs_example': 'property',
        'prefix': 'conditionalJumpTrigger',
        'python_name': 'conditional_jump_triggers',
        'value_for_docs_example': 'nidigital.TriggerType.DIGITAL_EDGE',
        'value_type_for_docs_example': 'enum',
    }
    enum_val_snippet = "session.conditional_jump_triggers[0, 2].conditional_jump_trigger_type = nidigital.TriggerType.DIGITAL_EDGE"
    enum_val_explanation = "sets :py:attr:`conditional_jump_trigger_type` to :py:data:`~nidigital.TriggerType.DIGITAL_EDGE` for conditional_jump_triggers 0, 2."
    assert (enum_val_snippet, enum_val_explanation) == get_repeated_capability_tuple_index_python_example(enum_val_rep_cap)

