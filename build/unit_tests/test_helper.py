from build.helper.helper import *


def test_get_development_status():
    config = {}

    config['module_version'] = '0.0.0.dev0'
    assert get_development_status(config) == '3 - Alpha'

    config['module_version'] = '0.0.0'
    assert get_development_status(config) == '3 - Alpha'

    config['module_version'] = '0.4.9.dev0'
    assert get_development_status(config) == '3 - Alpha'

    config['module_version'] = '0.4.9'
    assert get_development_status(config) == '3 - Alpha'

    config['module_version'] = '0.5.0.dev0'
    assert get_development_status(config) == '4 - Beta'

    config['module_version'] = '0.5.0'
    assert get_development_status(config) == '4 - Beta'

    config['module_version'] = '0.9.9.dev0'
    assert get_development_status(config) == '4 - Beta'

    config['module_version'] = '0.9.9'
    assert get_development_status(config) == '4 - Beta'

    config['module_version'] = '1.0.0.dev0'
    assert get_development_status(config) == '3 - Alpha'

    config['module_version'] = '1.0.0.a0'
    assert get_development_status(config) == '3 - Alpha'

    config['module_version'] = '1.0.0.b0'
    assert get_development_status(config) == '4 - Beta'

    config['module_version'] = '1.0.0.c0'
    assert get_development_status(config) == '4 - Beta'

    config['module_version'] = '1.0.0.rc0'
    assert get_development_status(config) == '4 - Beta'

    config['module_version'] = '1.0.0'
    assert get_development_status(config) == '5 - Production/Stable'

    config['module_version'] = '1.9.9.dev0'
    assert get_development_status(config) == '3 - Alpha'

    config['module_version'] = '1.9.9.a0'
    assert get_development_status(config) == '3 - Alpha'

    config['module_version'] = '1.9.9.b0'
    assert get_development_status(config) == '4 - Beta'

    config['module_version'] = '1.9.9.c0'
    assert get_development_status(config) == '4 - Beta'

    config['module_version'] = '1.9.9.rc0'
    assert get_development_status(config) == '4 - Beta'

    config['module_version'] = '1.9.9'
    assert get_development_status(config) == '5 - Production/Stable'

    config['module_version'] = '9.9.9.dev0'
    assert get_development_status(config) == '3 - Alpha'

    config['module_version'] = '9.9.9.a0'
    assert get_development_status(config) == '3 - Alpha'

    config['module_version'] = '9.9.9.b0'
    assert get_development_status(config) == '4 - Beta'

    config['module_version'] = '9.9.9.c0'
    assert get_development_status(config) == '4 - Beta'

    config['module_version'] = '9.9.9.rc0'
    assert get_development_status(config) == '4 - Beta'

    config['module_version'] = '9.9.9'
    assert get_development_status(config) == '5 - Production/Stable'

    config['module_version'] = '19.9.9.dev0'
    assert get_development_status(config) == '3 - Alpha'

    config['module_version'] = '19.9.9.a0'
    assert get_development_status(config) == '3 - Alpha'

    config['module_version'] = '19.9.9.b0'
    assert get_development_status(config) == '4 - Beta'

    config['module_version'] = '19.9.9.c0'
    assert get_development_status(config) == '4 - Beta'

    config['module_version'] = '19.9.9.rc0'
    assert get_development_status(config) == '4 - Beta'

    config['module_version'] = '19.9.9'
    assert get_development_status(config) == '5 - Production/Stable'


def test_enum_uses_converter():
    import pytest

    assert not enum_uses_converter({})
    assert not enum_uses_converter({
        'enum_to_converted_value_function_name': None,
        'converted_value_to_enum_function_name': None
    })

    assert enum_uses_converter({
        'enum_to_converted_value_function_name': lambda x: x,
        'converted_value_to_enum_function_name': lambda x: x
    })

    with pytest.raises(AssertionError):
        enum_uses_converter({
            'enum_to_converted_value_function_name': lambda x: x
        })
    with pytest.raises(AssertionError):
        enum_uses_converter({
            'converted_value_to_enum_function_name': lambda x: x
        })
    with pytest.raises(AssertionError):
        enum_uses_converter({
            'enum_to_converted_value_function_name': None,
            'converted_value_to_enum_function_name': lambda x: x
        })
    with pytest.raises(AssertionError):
        enum_uses_converter({
            'enum_to_converted_value_function_name': lambda x: x,
            'converted_value_to_enum_function_name': None
        })
