import metadata_utilities

def do_the_test(a, b, expected):
    actual   = a.copy()
    metadata_utilities.merge_dicts(actual, b)
    assert expected == actual, "\na = {0}\nb = {1}\nexpected = {2}\nactual = {3}".format(a, b, expected, actual)

def test_merge_dict_second_is_empty():
    a        = {'a':1, 'b':2}
    b        = {}
    expected = {'a':1, 'b':2}
    do_the_test(a,b, expected)

def test_merge_dict_simple():
    a        = {'a':1, 'b':2}
    b        = {'c':3}
    expected = {'a':1, 'b':2, 'c':3}
    do_the_test(a,b, expected)

def test_merge_dict_first_is_empty():
    a        = {}
    b        = {'a':1, 'b':2}
    expected = {'a':1, 'b':2}
    do_the_test(a,b, expected)

def test_merge_dict_key_exists():
    a        = {'a':1, 'b':2}
    b        = {'b':3, 'c':4}
    expected = {'a':1, 'b':3, 'c':4}
    do_the_test(a,b, expected)

def test_merge_dict_recurse():
    a        = {'a':1, 'b':{'b1':5, 'b2':6}}
    b        = {'b':{'b3':7}, 'c':4}
    expected = {'a':1, 'b':{'b1':5, 'b2':6, 'b3':7}, 'c':4}
    do_the_test(a,b, expected)

def test_merge_dict_replace_in_list():
    a        = {'a':1, 'b':{'b1':5, 'b2':6}, 'c':['x', 'y', 'z']}
    b        = {'b':{'b3':7, 'b1':8}, 'c':{0:'r', 1:'s', 2:'t'}}
    expected = {'a':1, 'b':{'b1':8, 'b2':6, 'b3':7}, 'c':['r', 's', 't']}
    do_the_test(a,b, expected)

def test_merge_dict_replace_in_dict_and_list():
    a        = {'a':1, 'b':{'b1':2, 'b2':3}, 'c':['x', 'y', 'z']}
    b        = {'b':{'b3':7, 'b1':8}, 'c':{0:'r', 1:'s', 2:'t'}}
    expected = {'a':1, 'b':{'b1':8, 'b2':3, 'b3':7}, 'c':['r', 's', 't']}
    do_the_test(a,b, expected)

def test_merge_dict_with_regex():
    a        = {'aaa':{}, 'aaaa':{'x':98}, 'aaaaa':{}, 'bbb':{'bbb1':2, 'bbb2':3}, 'ccc':['x', 'y', 'z']}
    b        = {'a+':{'z':99}}
    expected = {'aaa':{'z':99}, 'aaaa':{'x':98, 'z':99}, 'aaaaa':{'z':99}, 'bbb':{'bbb1':2, 'bbb2':3}, 'ccc':['x', 'y', 'z']}
    do_the_test(a,b, expected)
