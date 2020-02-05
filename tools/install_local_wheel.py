# !python

import argparse
from configure_logging import configure_logging
import logging
import os
import pprint
from subprocess import call
import sys

pp = pprint.PrettyPrinter(indent=4, width=100)


def main():
    # Setup the required arguments for this script
    usage = """
Install the wheel found in generated/<driver>/dist
"""
    parser = argparse.ArgumentParser(description=usage)
    file_group = parser.add_argument_group("Input and Output files")
    file_group.add_argument("--driver", action="store", default=None, required=True, help="Source file")
    file_group.add_argument("--start-path", action="store", default=None, help="Prepend to path to search")

    verbosity_group = parser.add_argument_group("Verbosity, Logging & Debugging")
    verbosity_group.add_argument("-v", "--verbose", action="count", dest="verbose", default=0, help="Verbose output")
    verbosity_group.add_argument("--test", action="store_true", dest="test", default=False, help="Run doctests and quit")
    verbosity_group.add_argument("--log-file", action="store", dest="logfile", default=None, help="Send logging to listed file instead of stdout")
    args = parser.parse_args()

    if args.verbose > 1:
        configure_logging(logging.DEBUG, args.logfile)
    elif args.verbose == 1:
        configure_logging(logging.INFO, args.logfile)
    else:
        configure_logging(logging.WARNING, args.logfile)

    logging.info(pp.pformat(args))

    rel_path = os.path.join('generated', args.driver, 'dist')
    if args.start_path is not None:
        rel_path = os.path.join(args.start_path, rel_path)
    wheel = None
    for file in os.listdir(rel_path):
        if file.endswith(".whl"):
            if wheel is not None:
                logging.error('More than one wheel has been found: {0} and {1}'.format(wheel, os.path.join(rel_path, file)))
                sys.exit(1)
            wheel = os.path.join(rel_path, file)

    if wheel is None:
        logging.error('No wheel found. Has the build run successfully?')
        sys.exit(2)

    # Install/upgrade the wheel
    call(['pip', 'install', '--upgrade', wheel])


if __name__ == '__main__':
    main()

