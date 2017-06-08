#!/usr/bin/python

import logging
import os
import pprint
import sys
import shutil
import argparse

pp = pprint.PrettyPrinter(indent=3)

DRIVERS = ["nidmm"]
OUTPUT_DIR = os.path.join(sys.path[0], "bin")

from contextlib import contextmanager
import importlib

# From https://stackoverflow.com/questions/41861427/python-3-5-how-to-dynamically-import-a-module-given-the-full-file-path-in-the
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

def path_import(absolute_path):
   '''implementation taken from https://docs.python.org/3/library/importlib.html#importing-a-source-file-directly'''
   with add_to_path(os.path.dirname(absolute_path)):
       module = importlib.import_module(os.path.basename(absolute_path))
       return module

def main():
    # Setup the required arguments for this script
    usage = "usage: " + sys.argv[0] + " [options]"

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
    args = parser.parse_args()

    codegen_path = os.path.join(sys.path[0], 'src', 'codegen')
    print('codegen_path = %s' % codegen_path)
    codegen = path_import(codegen_path)

    if args.verbose > 1:
        codegen.configure_logging(logging.DEBUG, args.logfile)
    elif args.verbose == 1:
        codegen.configure_logging(logging.INFO, args.logfile)
    else:
        codegen.configure_logging(logging.WARNING, args.logfile)

    logging.info(pp.pformat(args))

    # clean up
    shutil.rmtree(OUTPUT_DIR)

    for driver in DRIVERS:
        driver_output_dir = os.path.join(OUTPUT_DIR, driver)
        try: 
            os.makedirs(driver_output_dir)
        except OSError:
            if not os.path.isdir(driver_output_dir):
                raise

        metadata_path = os.path.join(sys.path[0], 'src', driver, 'metadata')
        print(metadata_path)
        metadata = path_import(metadata_path)

        template_params = {}
        template_params['metadata'] = metadata
        template_params['types'] = codegen.type_map

        logging.debug(pp.pformat(template_params))

        config = metadata.config

        for output_file in config['files_to_generate']:
            template_name = os.path.join(sys.path[0], 'src', 'codegen', 'templates', output_file + '.mako')
            dest_file = os.path.join(driver_output_dir, output_file)
            codegen.generate_template(template_name, template_params, dest_file)




if __name__ == '__main__':
    main()

