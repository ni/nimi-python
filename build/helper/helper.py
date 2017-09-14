# TODO(marcoskirsch): This file should definitely not live here but I had trouble getting import to work.
# TODO(marcoskirsch): Figure out unit test for this.

from contextlib import contextmanager
import importlib
import pprint
import re
import sys

pp = pprint.PrettyPrinter(indent=4)

# Coding convention transformation functions.


# TODO(marcoskirsch): not being used
def shoutcase_to_camelcase(shout_string):
    '''Converts a C-style SHOUT_CASE string to camelCase'''
    components = shout_string.split('_')
    return components[0].lower() + "".join(component.title() for component in components[1:])


def camelcase_to_snakecase(camelcase_string):
    '''Converts a camelCase string to lower_case_snake_case'''
    # https://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-snake-case
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camelcase_string)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


# TODO(marcoskirsch): not being used
def function_to_method_name(f):
    '''Returns an appropriate session method name for a given function'''
    # Method name is camelCase.
    return f['name'][0].lower() + f['name'][1:]


def sorted_attrs(a):
    return sorted(a, key=lambda k: a[k]['name'])


# We need this to allow us to dynamically add and remove a folder to the search
# path becaise importlib.import_module() won't work with a module hierarchy in python2
@contextmanager
def add_to_path(p):
    import sys
    old_path = sys.path
    sys.path = sys.path[:]
    sys.path.insert(0, p)
    try:
        yield
    finally:
        sys.path = old_path


def get_intrinsic_type_from_visa_type(visa_type):
    '''Returns the underlying intrinsic (python) type from the visa type'''
    if sys.version_info.major < 3:
        with add_to_path('build/templates'):
            p_types = importlib.import_module('python_types')
    else:
        p_types = importlib.import_module('build.templates.python_types')
    v_type = getattr(p_types, visa_type)

    return type(v_type()).__name__


