#! python

import argparse
import getpass
import logging
import pprint
import readline
from subprocess import call
import sys

pp = pprint.PrettyPrinter(indent=4, width=100)

def configureLogging(lvl = logging.WARNING, logfile = None):
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
Update version when it is a dev version. I.e. X.Y.Z.devN to X.Y.Z.dev(N+1)
"""
    parser = argparse.ArgumentParser(description=usage)
    #fileGroup = parser.add_argument_group("Input and Output files")
    #fileGroup.add_argument(
    #    "--src-file",
    #    action="store", dest="src_file", default=None, required=True,
    #    help="Source file")

    verbosityGroup = parser.add_argument_group("Verbosity, Logging & Debugging")
    verbosityGroup.add_argument(
        "--exporting",
        action="store_true", dest="exporting", default=False,
        help="Are we building an official export? If false, don't actually interact with perforce."
        )
    verbosityGroup.add_argument(
        "-v", "--verbose",
        action="count", dest="verbose", default=0,
        help="Verbose output"
        )
    verbosityGroup.add_argument(
        "--test",
        action="store_true", dest="test", default=False,
        help="Run doctests and quit"
        )
    verbosityGroup.add_argument(
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

    user = raw_input('twine username: ')
    pw = getpass.getpass(prompt='twine password: ')
    logging.debug('Username: '  + user)
    call(['tox', '-e', 'clean'])
    call(['tox'])
    call(['twine', 'upload', 'bin/nidmm/dist/*', 'bin/nimodinst/dist/*'])
    call(['python', 'tools/updateDevVersions.py', '--src-file', 'src/nidmm/metadata/config.py'])
    call(['python', 'tools/updateDevVersions.py', '--src-file', 'src/nimodinst/metadata/config.py'])
    call(['tox'])

if __name__ == '__main__':
    Main()

