#!/usr/bin/python3

from contextlib import contextmanager
import importlib
import logging
import os
import sys


# From https://stackoverflow.com/questions/41861427/python-3-5-how-to-dynamically-import-a-module-given-the-full-file-path-in-the
@contextmanager
def add_to_path(p):
    import sys
    logging.debug("Adding path %s" % p)
    old_path = sys.path
    sys.path = sys.path[:]
    sys.path.insert(0, p)
    try:
        yield
    finally:
        logging.debug("Removing path %s" % p)
        sys.path = old_path


def path_import(absolute_path):
    '''implementation taken from https://docs.python.org/3/library/importlib.html#importing-a-source-file-directly'''
    if not os.path.isabs(absolute_path):
        absolute_path = os.path.join(sys.path[0], absolute_path)
    logging.debug("Importing %s" % absolute_path)
    with add_to_path(os.path.dirname(absolute_path)):
        module = importlib.import_module(os.path.basename(absolute_path))
        return module


def configure_logging(lvl=logging.WARNING, logfile=None):
    root = logging.getLogger()
    # Remove all handlers. We will add our own
    while root.handlers:
        root.handlers.pop()
    root.setLevel(lvl)
    formatter = logging.Formatter('%(funcName)s - %(levelname)s - %(message)s')
    if logfile is None:
        hndlr = logging.StreamHandler(sys.stdout)
    else:
        print("Logging to file %s" % logfile)
        hndlr = logging.FileHandler(logfile)
    hndlr.setFormatter(formatter)
    root.addHandler(hndlr)


def load_build(m):
    metadata = path_import(m)

    return metadata


