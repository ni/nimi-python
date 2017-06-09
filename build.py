#!/usr/bin/python

import argparse
from contextlib import contextmanager
import importlib
import logging
import os
import pprint
import shutil
import sys

pp = pprint.PrettyPrinter(indent=4)

OUTPUT_DIR = os.path.join(sys.path[0], "bin")
SOURCE_DIR = os.path.join(sys.path[0], "src")
TEMPLATE_DIR = os.path.join(SOURCE_DIR, "codegen", "templates")
possible_actions=["clean","make"]

buildinfo_format = """
The buildinfo format is as follows:
buildinfo = {
  'variables': {<vars>},
  "<action>": [<commands>],
  "<action>": [<commands>],
  "<action>": [<commands>],
}

<action> can be one of possible_actions
Each <commands> looks like:
{"command": "<command>", "params": {<command specific parameters>}}

Command               Parameters
mkdir                 {'path': '<path to create>'}
rmdir                 {'path': '<path to delete>'}
template              {'template': '<path to mako template>', 'output_file': '<output file path>'}

Variables will be substitued in all param strings. Format in the string is %(varname)s.

Variables come from the global namespace as well as the variable section of buildinfo
"""

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

# command functions
def exec_mkdir(folder):
    logging.debug("Creating directory %s" % folder)
    try: 
        os.makedirs(folder)
    except OSError:
        if not os.path.isdir(folder):
            raise

def exec_rmdir(folder):
    logging.debug("Removing directory %s" % folder)
    if os.path.exists(folder):
        shutil.rmtree(folder)

def exec_template(codegen, metadata, template_name, output_file):
    logging.debug("Generating %s from %s" % (output_file, template_name))
    template_params = {}
    template_params['metadata'] = metadata
    if metadata.type_map is None:
        template_params['types'] = codegen.type_map
    else:
        template_params['types'] = metadata.type_map

    logging.debug(pp.pformat(template_params))

    config = metadata.config

    codegen.generate_template(template_name, template_params, output_file)

def load_build(m):
    metadata = path_import(m)
    # Check to make sure there is build information in the given build file
    try:
        buildinfo = metadata.buildinfo
    except NameError:
        logging.error("There must be a build variable in %s" % bf)
        sys.exit(1)

    return metadata

def exec_build(codegen, metadata, actions):
    all_vars = globals().copy()
    if 'variables' in metadata.buildinfo:
        all_vars.update(metadata.buildinfo['variables'])
    for action in actions:
        logging.info('%s, %s' % (action, metadata.config['driver_name']))
        commands = metadata.buildinfo[action]
        for c in commands:
            command = c['command']
            params = c['params']
            if command == "mkdir":
                folder = (params['path'] % all_vars)
                exec_mkdir(folder)
            elif command == "rmdir":
                folder = (params['path'] % all_vars)
                exec_rmdir(folder)
            elif command == "template":
                template = (params['template'] % all_vars)
                output_file = (params['output_file'] % all_vars)
                exec_template(codegen, metadata, template, output_file)

def main():
    # Setup the required arguments for this script
    usage = "Codegen driver files"

    parser = argparse.ArgumentParser(description=usage)
    verbosity_group = parser.add_argument_group("Verbosity, Logging & Debugging")
    verbosity_group.add_argument(
        "-v", "--verbose",
        action="count", dest="verbose", default=0,
        help="Verbose output"
        )
    verbosity_group.add_argument(
        "--test",
        action="store_true", dest="test", default=False,
        help="Run doctests and quit"
        )
    verbosity_group.add_argument(
        "--log-file",
        action="store", dest="logfile", default=None,
        help="Send logging to listed file instead of stdout"
        )
    parser.add_argument(
        "--metadata", 
        action='append', dest='metadata', default=[],
        help='Absolute or relative path to metadata package. Multiple allowed. ' +
             'Will build in order added to command line.'
        )
    parser.add_argument(
        "actions", metavar = "ACTIONS", type=str, choices=possible_actions,
        nargs="+", help="Possible actions: " + ', '.join(possible_actions)
        )
    args = parser.parse_args()

    codegen_path = os.path.join(sys.path[0], 'src', 'codegen')
    codegen = path_import(codegen_path)

    if args.verbose > 1:
        codegen.configure_logging(logging.DEBUG, args.logfile)
    elif args.verbose == 1:
        codegen.configure_logging(logging.INFO, args.logfile)
    else:
        codegen.configure_logging(logging.WARNING, args.logfile)

    logging.info(pp.pformat(args))

    for m in args.metadata:
        metadata = load_build(m)

        exec_build(codegen, metadata, args.actions)


if __name__ == '__main__':
    main()

