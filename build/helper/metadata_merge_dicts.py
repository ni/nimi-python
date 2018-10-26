# Useful functions for use in the metadata modules

import pprint
import re

pp = pprint.PrettyPrinter(indent=4, width=80)


def merge_helper(metadata, metadata_type, config, use_re):
    metadata_module = 'metadata.{0}_addon'.format(metadata_type)
    if 'modules' in config and metadata_module in config['modules']:
        for m in dir(config['modules'][metadata_module]):
            if m.startswith('{0}_'.format(metadata_type)) and m != '{0}_additional_{0}'.format(metadata_type):
                merge_dicts(metadata, config['modules'][metadata_module].__getattribute__(m), use_re, m)
            # We need to explicitly copy new entries
            if m == '{0}_additional_{0}'.format(metadata_type):
                outof = config['modules'][metadata_module].__getattribute__(m)
                for a in outof:
                    metadata[a] = outof[a]

    # Delete any entries that are empty
    # Have to do this in two steps. Otherwise the dictionary changes size and errors
    to_delete = []
    for m in metadata:
        if len(metadata[m]) == 0:
            to_delete.append(m)
    for m in to_delete:
        metadata.pop(m, None)

    return metadata


def merge_dicts(into, outof, use_re, dict_name):
    '''merge_dicts

    Recursively merges the contents of dictionary 'outof' into dictionary 'into'.
    'into' may contain lists as values.
    'outof' may contain regular expressions as keys, in which case values are
    merged with all key matches in into.
    '''
    for item in sorted(outof):
        # If we're not using regex's then this is an easy check
        if not use_re and item not in into and dict_name is not None:
            raise KeyError('Key {0} from {1} is not in the destination'.format(item, dict_name))
        # If we are using regex's we need to seach all keys to see if any match
        if use_re and dict_name is not None:
            key_exists = False
            for item2 in into:
                if re.search(item, item2):
                    key_exists = True
            if not key_exists:
                raise KeyError('Key {0} from {1} is not in the destination'.format(item, dict_name))

        if type(outof[item]) is dict:
            if item in into:
                merge_dicts(into[item], outof[item], use_re, None)
            elif type(into) is list:
                for item2 in outof[item]:
                    into[item][item2] = outof[item][item2]
            else:
                # attributes keys are integers so they do not need the regex check (and
                # in fact will error)
                if type(item) is str:
                    # Handle regex in addon
                    for item2 in into:
                        if use_re is True and re.search(item, item2):
                            assert type(into[item2]) is dict
                            merge_dicts(into[item2], outof[item], use_re, None)
        else:
            into[item] = outof[item]


# Unit Tests
def _do_the_test_merge_dicts(a, b, expected, use_re):
    actual = a.copy()
    merge_dicts(actual, b, use_re, 'test')
    assert expected == actual, "\na = {0}\nb = {1}\nexpected = {2}\nactual = {3}".format(a, b, expected, actual)


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

