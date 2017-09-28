# !python

import argparse
import logging
import os
import pprint
from subprocess import call
import sys

pp = pprint.PrettyPrinter(indent=4, width=100)


def configureLogging(lvl=logging.WARNING, logfile=None):
    root = logging.getLogger()
    root.setLevel(lvl)

    formatter = logging.Formatter("[%(asctime)s] [%(levelname)8s] --- %(message)s (%(filename)s:%(funcName)s:%(lineno)s)", "%Y-%m-%d %H:%M:%S")
    if logfile is None:
        hndlr = logging.StreamHandler(sys.stdout)
    else:
        print("Logging to file %s" % logfile)
        hndlr = logging.FileHandler(logfile)
    hndlr.setFormatter(formatter)
    root.addHandler(hndlr)


def Main():
    # Setup the required arguments for this script
    usage = """
Install the wheel found in bin/<driver>/dist
"""
    parser = argparse.ArgumentParser(description=usage)
    fileGroup = parser.add_argument_group("Input and Output files")
    fileGroup.add_argument
    (
        "--driver",
        action="store", dest="driver", default=None, required=True,  # noqa: E999
        help="Source file"
    )

    verbosityGroup = parser.add_argument_group("Verbosity, Logging & Debugging")
    verbosityGroup.add_argument
    (
        "-v", "--verbose",
        action="count", dest="verbose", default=0,
        help="Verbose output"
    )
    verbosityGroup.add_argument
    (
        "--test",
        action="store_true", dest="test", default=False,
        help="Run doctests and quit"
    )
    verbosityGroup.add_argument
    (
        "--log-file",
        action="store", dest="logfile", default=None,
        help="Send logging to listed file instead of stdout"
    )
    args = parser.parse_args()

    if args.verbose > 1:
        configureLogging(logging.DEBUG, args.logfile)
    elif args.verbose == 1:
        configureLogging(logging.INFO, args.logfile)
    else:
        configureLogging(logging.WARNING, args.logfile)

    logging.info(pp.pformat(args))

    rel_path = os.path.join('bin', args.driver, 'dist')
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
    Main()

