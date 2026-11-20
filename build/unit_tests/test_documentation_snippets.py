from build.helper.documentation_snippets import *


def test_close_function_def_for_doc_note_not_list():
    '''Testing for lack of syntax error - not actual documentation'''
    functions = {
        'close': {
            'documentation': {
                'description': 'test',
                'note': 'test',
            },
        },
    }
    config = {
        'close_function': 'close'
    }
    close_doc = close_function_def_for_doc(functions, config)
    assert type(close_doc) is dict
    return


def test_close_function_def_for_doc_note_list():
    '''Testing for lack of syntax error - not actual documentation'''
    functions = {
        'close': {
            'documentation': {
                'description': 'test',
                'note': ['test'],
            },
        },
    }
    config = {
        'close_function': 'close'
    }
    close_doc = close_function_def_for_doc(functions, config)
    assert type(close_doc) is dict
    return


def test_close_function_def_for_doc_no_note():
    '''Testing for lack of syntax error - not actual documentation'''
    functions = {
        'close': {
            'documentation': {
                'description': 'test',
            },
        },
    }
    config = {
        'close_function': 'close'
    }
    close_doc = close_function_def_for_doc(functions, config)
    assert type(close_doc) is dict


def test_initiate_function_def_for_doc_note_not_list():
    '''Testing for lack of syntax error - not actual documentation'''
    functions = {
        'Initiate': {
            'documentation': {
                'description': 'test',
                'note': 'test',
            },
            'python_name': '_initiate',
        },
    }
    context_manager = {
        'task': 'acquisition',
        'initiate_function': 'Initiate',
        'abort_function': 'Abort',
    }
    initiate_doc = initiate_function_def_for_doc(functions, context_manager)
    assert type(initiate_doc) is dict
    return


def test_initiate_function_def_for_doc_note_list():
    '''Testing for lack of syntax error - not actual documentation'''
    functions = {
        'Initiate': {
            'documentation': {
                'description': 'test',
                'note': ['test'],
            },
            'python_name': '_initiate',
        },
    }
    context_manager = {
        'task': 'acquisition',
        'initiate_function': 'Initiate',
        'abort_function': 'Abort',
    }
    initiate_doc = initiate_function_def_for_doc(functions, context_manager)
    assert type(initiate_doc) is dict
    return


def test_initiate_function_def_for_doc_no_note():
    '''Testing for lack of syntax error - not actual documentation'''
    functions = {
        'Initiate': {
            'documentation': {
                'description': 'test',
            },
            'python_name': '_initiate',
        },
    }
    context_manager = {
        'task': 'acquisition',
        'initiate_function': 'Initiate',
        'abort_function': 'Abort',
    }
    initiate_doc = initiate_function_def_for_doc(functions, context_manager)
    assert type(initiate_doc) is dict


def test_initiate_function_def_for_doc_default_method_name():
    functions = {
        'Initiate': {
            'documentation': {
                'description': 'test',
            },
            'python_name': '_initiate',
        },
    }
    context_manager = {
        'task': 'acquisition',
        'initiate_function': 'Initiate',
        'abort_function': 'Abort',
    }
    initiate_doc = initiate_function_def_for_doc(functions, context_manager)
    assert initiate_doc['python_name'] == 'initiate'


def test_initiate_function_def_for_doc_method_name():
    functions = {
        'InitiateGeneration': {
            'documentation': {
                'description': 'test',
            },
            'python_name': '_initiate_generation',
        },
    }
    context_manager = {
        'task': 'generation',
        'initiate_function': 'InitiateGeneration',
        'abort_function': 'AbortGeneration',
        'method_name': 'initiate_generation',
    }
    initiate_doc = initiate_function_def_for_doc(functions, context_manager)
    assert initiate_doc['python_name'] == 'initiate_generation'


_acquisition_context_manager = {
    'task': 'acquisition',
    'initiate_function': 'Initiate',
    'abort_function': 'Abort',
}

_generation_context_manager = {
    'task': 'generation',
    'initiate_function': 'InitiateGeneration',
    'abort_function': 'AbortGeneration',
    'method_name': 'initiate_generation',
}


def test_get_context_manager_configs_none():
    from build.helper.metadata_filters import get_context_manager_configs
    assert get_context_manager_configs({}) == []
    assert get_context_manager_configs({'context_manager_name': {}}) == []
    assert get_context_manager_configs({'context_manager_name': []}) == []


def test_get_context_manager_configs_singular():
    from build.helper.metadata_filters import get_context_manager_configs
    assert get_context_manager_configs({'context_manager_name': _acquisition_context_manager}) == [_acquisition_context_manager]
    assert get_context_manager_configs({'context_manager_name': [_acquisition_context_manager]}) == [_acquisition_context_manager]


def test_get_context_manager_configs_multiple():
    from build.helper.metadata_filters import get_context_manager_configs
    config = {'context_manager_name': [_acquisition_context_manager, _generation_context_manager]}
    assert get_context_manager_configs(config) == [_acquisition_context_manager, _generation_context_manager]


def test_initiate_function_def_for_doc_no_initiate_function():
    assert initiate_function_def_for_doc({}, {'task': 'acquisition'}) is None


def test_initiate_function_def_for_doc_singular():
    from build.helper.metadata_filters import get_context_manager_configs
    functions = {
        'Initiate': {
            'documentation': {
                'description': 'acquisition',
            },
            'python_name': '_initiate',
        },
    }
    config = {'context_manager_name': _acquisition_context_manager}
    docs = [initiate_function_def_for_doc(functions, cm) for cm in get_context_manager_configs(config)]
    assert [d['python_name'] for d in docs] == ['initiate']
    assert [d['documentation']['description'] for d in docs] == ['acquisition']
    # The source function metadata must not be modified
    assert functions['Initiate']['python_name'] == '_initiate'
    assert 'note' not in functions['Initiate']['documentation']


def test_initiate_function_def_for_doc_multiple():
    from build.helper.metadata_filters import get_context_manager_configs
    functions = {
        'Initiate': {
            'documentation': {
                'description': 'acquisition',
            },
            'python_name': '_initiate',
        },
        'InitiateGeneration': {
            'documentation': {
                'description': 'generation',
            },
            'python_name': '_initiate_generation',
        },
    }
    config = {'context_manager_name': [_acquisition_context_manager, _generation_context_manager]}
    docs = [initiate_function_def_for_doc(functions, cm) for cm in get_context_manager_configs(config)]
    assert [d['python_name'] for d in docs] == ['initiate', 'initiate_generation']
    assert [d['documentation']['description'] for d in docs] == ['acquisition', 'generation']
    # The source function metadata must not be modified
    assert functions['Initiate']['python_name'] == '_initiate'
    assert 'note' not in functions['InitiateGeneration']['documentation']
