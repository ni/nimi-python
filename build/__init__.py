from contextlib import contextmanager
import os

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
    from generate_template import generate_template  # noqa: F401

    from utilities import configure_logging  # noqa: F401

