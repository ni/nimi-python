#!/usr/bin/python3

import argparse
from contextlib import contextmanager
import distutils
from distutils import dir_util
import importlib
import logging
import os
import pprint
import shutil
import subprocess
import sys

pp = pprint.PrettyPrinter(indent=4)

OUTPUT_DIR = os.path.join(sys.path[0], "bin")
SOURCE_DIR = os.path.join(sys.path[0], "src")
TEMPLATE_DIR = os.path.join(SOURCE_DIR, "codegen", "templates")
possible_actions=["clean","make"]

buildinfo_format = """The buildinfo format is as follows:
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
copy                  {'src': '<source path>', 'dest': '<destination path>'} // Source can be a file or a directory
sdist                 {'src-dir': '<directory that contains setup.py>'}
wheel                 {'src-dir': '<directory that contains setup.py>'}

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

def exec_codegen(codegen, metadata, template_name, output_file):
    logging.debug("Generating %s from %s" % (output_file, template_name))
    template_params = {}
    template_params['metadata'] = metadata
    template_params['types'] = codegen.type_map

    logging.debug(pp.pformat(template_params))

    config = metadata.config

    codegen.generate_template(template_name, template_params, output_file)

def exec_copy(src, dest):
    logging.debug("Copying %s to %s" % (src, dest))
    if os.path.isdir(src):
        distutils.dir_util.copy_tree(src, dest)
    else:
        shutil.copyfile(src, dest)

def exec_sdist(src_dir):
    logging.debug('Create pypi packages in %s' % src_dir)
    # Save the current working directory before changing to src_dir
    old_cwd = os.getcwd()
    os.chdir(src_dir)
    # TODO(texasaggie97) Needs to be python to be generic
    subprocess.call(['py', 'setup.py', 'sdist'])
    os.chdir(old_cwd)

def exec_wheel(src_dir):
    logging.debug('Create pypi packages in %s' % src_dir)
    # Save the current working directory before changing to src_dir
    old_cwd = os.getcwd()
    os.chdir(src_dir)
    # TODO(texasaggie97) Needs to be python to be generic
    subprocess.call(['py', 'setup.py', 'bdist_wheel', '--universal'])
    os.chdir(old_cwd)

# end command functions

def load_build(m):
    metadata = path_import(m)
    # Check to make sure there is build information in the given build file
    try:
        buildinfo = metadata.build_info
    except NameError:
        logging.error("There must be a build variable in %s" % bf)
        sys.exit(1)

    return metadata

def exec_build(codegen, metadata, actions):
    all_vars = globals().copy()
    if 'variables' in metadata.build_info:
        all_vars.update(metadata.build_info['variables'])
    for action in actions:
        logging.info('%s, %s' % (action, metadata.config['driver_name']))
        commands = metadata.build_info[action]
        for c in commands:
            command = c['command']
            params = c['params']
            if command == "mkdir":
                folder = (params['path'] % all_vars)
                exec_mkdir(folder)
            elif command == "rmdir":
                folder = (params['path'] % all_vars)
                exec_rmdir(folder)
            elif command == "codegen":
                template = (params['template'] % all_vars)
                output_file = (params['output_file'] % all_vars)
                exec_codegen(codegen, metadata, template, output_file)
            elif command == 'copy':
                src = (params['src'] % all_vars)
                dest = (params['dest'] % all_vars)
                exec_copy(src, dest)
            elif command == 'sdist':
                src_dir = (params['src-dir'] % all_vars)
                exec_sdist(src_dir)
            elif command == 'wheel':
                src_dir = (params['src-dir'] % all_vars)
                exec_wheel(src_dir)
            else:
                logging.error('Unknown command: %s' % command)
                sys.exit(1)

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

