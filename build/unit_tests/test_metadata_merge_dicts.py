from build.helper.metadata_merge_dicts import *


def _do_the_test_merge_dicts(a, b, expected, use_re):
    actual = a.copy()
    merge_dicts(actual, b, use_re, 'test')
    assert expected == actual, f"\na = {a}\nb = {b}\nexpected = {expected}\nactual = {actual}"


def test_merge_dict_second_is_empty():
    a = {'a': 1, 'b': 2}
    b = {}
    expected = {'a': 1, 'b': 2}
    _do_the_test_merge_dicts(a, b, expected, use_re=True)


def test_merge_dict_key_exists():
    a = {'a': 1, 'b': 2}
    b = {'b': 3}
    expected = {'a': 1, 'b': 3}
    _do_the_test_merge_dicts(a, b, expected, use_re=True)


def test_merge_dict_recurse():
    a = {'a': 1, 'b': {'b1': 5, 'b2': 6}}
    b = {'b': {'b3': 7}}
    expected = {'a': 1, 'b': {'b1': 5, 'b2': 6, 'b3': 7}}
    _do_the_test_merge_dicts(a, b, expected, use_re=True)


def test_merge_dict_replace_in_list():
    a = {'a': 1, 'b': {'b1': 5, 'b2': 6}, 'c': ['x', 'y', 'z']}
    b = {'b': {'b3': 7, 'b1': 8}, 'c': {0: 'r', 1: 's', 2: 't'}}
    expected = {'a': 1, 'b': {'b1': 8, 'b2': 6, 'b3': 7}, 'c': ['r', 's', 't']}
    _do_the_test_merge_dicts(a, b, expected, use_re=True)


def test_merge_dict_replace_in_dict_and_list():
    a = {'a': 1, 'b': {'b1': 2, 'b2': 3}, 'c': ['x', 'y', 'z']}
    b = {'b': {'b3': 7, 'b1': 8}, 'c': {0: 'r', 1: 's', 2: 't'}}
    expected = {'a': 1, 'b': {'b1': 8, 'b2': 3, 'b3': 7}, 'c': ['r', 's', 't']}
    _do_the_test_merge_dicts(a, b, expected, use_re=True)


def test_merge_dict_with_regex():
    a = {'aaa': {}, 'aaaa': {'x': 98}, 'aaaaa': {}, 'bbb': {'bbb1': 2, 'bbb2': 3}, 'ccc': ['x', 'y', 'z']}
    b = {'a+': {'z': 99}}
    expected = {'aaa': {'z': 99}, 'aaaa': {'x': 98, 'z': 99}, 'aaaaa': {'z': 99}, 'bbb': {'bbb1': 2, 'bbb2': 3}, 'ccc': ['x', 'y', 'z']}
    _do_the_test_merge_dicts(a, b, expected, use_re=True)


def test_merge_dict_with_regex_off():
    a = {'aaa': {}, 'aaaa': {'x': 98}, 'aaaaa': {}, 'bbb': {'bbb1': 2, 'bbb2': 3}, 'ccc': ['x', 'y', 'z']}
    b = {'aaa': {'z': 99}}
    expected = {'aaa': {'z': 99}, 'aaaa': {'x': 98}, 'aaaaa': {}, 'bbb': {'bbb1': 2, 'bbb2': 3}, 'ccc': ['x', 'y', 'z']}
    _do_the_test_merge_dicts(a, b, expected, use_re=False)


def test_merge_dict_top_level_key_missing():
    a = {'a': 1, 'b': 2}
    b = {'b': 3, 'c': 4}
    expected = {'a': 1, 'b': 3, 'c': 4}
    try:
        _do_the_test_merge_dicts(a, b, expected, use_re=True)
        assert False
    except KeyError:
        pass

