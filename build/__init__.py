
import os
import sys
from contextlib import contextmanager

pathname = os.path.dirname(os.path.realpath(__file__))

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

with add_to_path(pathname):
    from generate_template import generate_template

    from build_execution import load_build
    from build_execution import exec_build

    from utilities import configure_logging

