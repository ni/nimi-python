#!/usr/bin/python3

import distutils
from distutils import dir_util
import logging
import os
import pkg_resources
import pprint
import shutil
import subprocess
import sys

import generate_template
import utilities

pp = pprint.PrettyPrinter(indent=4)
print(__file__)

# OUTPUT_DIR & SOURCE_DIR are relative to the folder where invoked
OUTPUT_DIR = os.path.join(os.getcwd(), "bin")
SOURCE_DIR = os.path.join(os.getcwd(), "src")

# We need to figure out if we are in a .pyz file or not. If we are, the path to mako
#  templates will be different because they will need to be from resource strings from
#  the zip file istead of a file on the file system
in_zip_file = False
if os.path.splitext(os.path.dirname(os.path.realpath(__file__)))[1] == '.pyz':
    in_zip_file = True

if in_zip_file:
    TEMPLATE_DIR = 'templates'
else:
    TEMPLATE_DIR = os.path.normpath(os.path.join(os.path.dirname(os.path.realpath(__file__)),"templates"))

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

def exec_codegen(metadata, template_name, output_file):
    logging.debug("Generating %s from %s" % (output_file, template_name))
    template_params = {}
    template_params['metadata'] = metadata

    logging.debug(pp.pformat(template_params))

    generate_template.generate_template(template_name, template_params, output_file, in_zip_file)

def exec_copy(src, dest):
    logging.debug("Copying %s to %s" % (src, dest))
    if os.path.isdir(src):
        distutils.dir_util.copy_tree(src, dest)
    elif in_zip_file and not os.path.exists(src):
        file_contents = pkg_resources.resource_string(__name__, src)
        with open(dest, "wb") as text_file:
            text_file.write(file_contents)
    else:
        shutil.copyfile(src, dest)

def exec_sdist(src_dir):
    logging.debug('Create pypi packages in %s' % src_dir)
    # Save the current working directory before changing to src_dir
    old_cwd = os.getcwd()
    os.chdir(src_dir)
    subprocess.call(['python3', 'setup.py', 'sdist'])
    os.chdir(old_cwd)

def exec_wheel(src_dir):
    logging.debug('Create pypi packages in %s' % src_dir)
    # Save the current working directory before changing to src_dir
    old_cwd = os.getcwd()
    os.chdir(src_dir)
    subprocess.call(['python3', 'setup.py', 'bdist_wheel', '--universal'])
    os.chdir(old_cwd)

def exec_setup_test(src_dir):
    logging.debug('Running unit tests in %s' % src_dir)
    # Save the current working directory before changing to src_dir
    old_cwd = os.getcwd()
    os.chdir(src_dir)
    subprocess.call(['python3', 'setup.py', 'pytest'])
    os.chdir(old_cwd)

# end command functions

def load_build(m):
    metadata = utilities.path_import(m)
    # Check to make sure there is build information in the given build file
    try:
        buildinfo = metadata.build_info
    except NameError:
        logging.error("There must be a build_info in the metadata")
        sys.exit(1)

    return metadata

def exec_build(metadata, actions):
    all_vars = globals().copy()
    if 'variables' in metadata.build_info:
        all_vars.update(metadata.build_info['variables'])
    for action in actions:
        logging.info('%s, %s' % (action, metadata.config['driver_name']))
        if action not in metadata.build_info:
            logging.error("'%s' is not supported by %s" %(action, metadata.config['driver_name']))
            sys.exit(1)

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
                exec_codegen(metadata, template, output_file)
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
            elif command == 'setup_test':
                src_dir = (params['src-dir'] % all_vars)
                exec_setup_test(src_dir)
            else:
                logging.error('Unknown command: %s' % command)
                sys.exit(1)


