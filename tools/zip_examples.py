# !python

import argparse
import logging
import os
import pprint
import sys
import zipfile

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


def zipdir(path, ziph):
    # ziph is zipfile handle
    extensions_to_skip = ['.pyc']
    os.chdir(path)
    for root, dirs, files in os.walk('.'):
        for file in files:
            _, file_extension = os.path.splitext(file)
            if file_extension not in extensions_to_skip:
                ziph.write(os.path.join(root, file))


def main():
    # Setup the required arguments for this script
    usage = """
Zip folder recursivly into file
"""
    parser = argparse.ArgumentParser(description=usage)
    file_group = parser.add_argument_group("Input and Output files")
    file_group.add_argument("--src-path", action="store", required=True, help="Top level directory to zip")
    file_group.add_argument("--zip-file", action="store", required=True, help="File name of output zip file")

    verbosity_group = parser.add_argument_group("Verbosity, Logging & Debugging")
    verbosity_group.add_argument("-v", "--verbose", action="count", default=0, help="Verbose output")
    verbosity_group.add_argument("--preview", action="store_true", default=False, help="Show what would happen when running with given parameters")
    verbosity_group.add_argument("--log-file", action="store", default=None, help="Send logging to listed file instead of stdout")
    args = parser.parse_args()

    if args.verbose > 1:
        configure_logging(logging.DEBUG, args.log_file)
    elif args.verbose == 1:
        configure_logging(logging.INFO, args.log_file)
    else:
        configure_logging(logging.WARNING, args.log_file)

    logging.info(pp.pformat(args))

    if not args.preview:
        with zipfile.ZipFile(args.zip_file, 'w', compression=zipfile.ZIP_STORED) as ziph:
            zipdir(args.src_path, ziph)


if __name__ == '__main__':
    main()

