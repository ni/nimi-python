# !python

import argparse
from configure_logging import configure_logging
import logging
import pprint
import re

pp = pprint.PrettyPrinter(indent=4, width=100)


def main():
    # Setup the required arguments for this script
    usage = """
Update version when it is a dev version. I.e. X.Y.Z.devN to X.Y.Z.dev(N+1)
"""
    parser = argparse.ArgumentParser(description=usage)
    file_group = parser.add_argument_group("Input and Output files")
    file_group.add_argument("--src-file", action="store", required=True, help="Source file")
    file_group.add_argument("--release", action="store_true", default=False, help="This is a release build, so only remove '.devN'. Error if not there")

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

    with open(args.src_file, 'r') as content_file:
        contents = content_file.read()

    module_dev_version_re = re.compile(r"'module_version': '(\d+\.\d+\.\d+)\.dev(\d+)'")
    m = module_dev_version_re.search(contents)
    if m:
        if args.release:
            logging.info('Dev version found, updating {0}.dev{1} to {0}'.format(m.group(1), int(m.group(2))))
            contents = module_dev_version_re.sub("'module_version': '{0}'".format(m.group(1)), contents)
        else:
            logging.info('Dev version found, updating {0}.dev{1} to {0}.dev{2}'.format(m.group(1), int(m.group(2)), int(m.group(2)) + 1))
            contents = module_dev_version_re.sub("'module_version': '{0}.dev{1}'".format(m.group(1), int(m.group(2)) + 1), contents)

    module_version_re = re.compile(r"'module_version': '(\d+\.\d+\.)(\d+)'")
    m = module_version_re.search(contents)
    if m and not args.release:
        logging.info('Release version found, updating {0}{1} to {0}{2}.dev0'.format(m.group(1), int(m.group(2)), int(m.group(2)) + 1))
        contents = module_version_re.sub("'module_version': '{0}{1}.dev0'".format(m.group(1), int(m.group(2)) + 1), contents)

    if not args.preview:
        with open(args.src_file, 'w') as content_file:
            content_file.write(contents)


if __name__ == '__main__':
    main()

