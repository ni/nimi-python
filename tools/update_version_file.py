# !python

import argparse
import logging
import pprint
import sys

from packaging.version import Version

pp = pprint.PrettyPrinter(indent=4, width=100)


def configure_logging(lvl=logging.WARNING, logfile=None):
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


def main():
    # Setup the required arguments for this script
    usage = """
Find the max version in any referenced VERSION file and then write that max version to the output VERSION file
"""
    parser = argparse.ArgumentParser(description=usage)
    file_group = parser.add_argument_group("Input and Output files")
    file_group.add_argument("--output-file", action="store", required=True, help="Output file")
    file_group.add_argument("--input-file", action="append", required=True, help="Input file, multiple allowed")

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

    max_version = Version('0.0.0.dev0')
    for version_file in args.input_file:
        with open(version_file) as f:
            v = Version(f.read().strip())

        if v > max_version:
            max_version = v

    with open(args.output_file, 'w') as f:
        f.write(str(max_version))


if __name__ == '__main__':
    main()

