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


def test_filter_context_managers():
    from build.helper.metadata_filters import filter_context_managers
    acquisition = {'task': 'acquisition', 'initiate_function': 'Initiate', 'abort_function': 'Abort'}
    generation = {'task': 'generation', 'initiate_function': 'InitiateGeneration', 'abort_function': 'AbortGeneration'}
    assert filter_context_managers({}) == []
    assert filter_context_managers({'context_manager_name': {}}) == []
    assert filter_context_managers({'context_manager_name': acquisition}) == [acquisition]
    assert filter_context_managers({'context_manager_name': [acquisition, generation]}) == [acquisition, generation]
