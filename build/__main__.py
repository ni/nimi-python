#!/usr/bin/python3

import argparse
import logging
import os
import pprint
import sys

# Part of this package
import generate_template
import utilities

pp = pprint.PrettyPrinter(indent=4)

# Setup the required arguments for this script
usage = "Codegen driver files"

parser = argparse.ArgumentParser(description=usage, prog='build')
verbosity_group = parser.add_argument_group("Verbosity, Logging & Debugging")
verbosity_group.add_argument(
    "-v", "--verbose",
    action="count", dest="verbose", default=0,
    help="Verbose output")
verbosity_group.add_argument(
    "--test",
    action="store_true", dest="test", default=False,
    help="Run doctests and quit")
verbosity_group.add_argument(
    "--log-file",
    action="store", dest="logfile", default=None,
    help="Send logging to listed file instead of stdout")
build_group = parser.add_argument_group("Build")
build_group.add_argument(
    "--metadata",
    action='append', dest='metadata', default=[],
    help='Absolute or relative path to metadata package. Multiple allowed. Will build in order added to command line.')
utility_group = parser.add_argument_group("Utility")
utility_group.add_argument(
    "--template",
    action="store", dest="template", default=None, required=True,
    help="Mako template to use. Can only be used if no actions.")
utility_group.add_argument(
    "--dest-dir",
    action="store", dest="dest_dir", default=None, required=False,
    help="Output folder.")
utility_group.add_argument(
    "--dest-file",
    action="store", dest="dest_file", default=None, required=False,
    help="Output file name. Optional. If not set, file will be named based on mako template name.")
args = parser.parse_args()

if args.verbose > 1:
    utilities.configure_logging(logging.DEBUG, args.logfile)
elif args.verbose == 1:
    utilities.configure_logging(logging.INFO, args.logfile)
else:
    utilities.configure_logging(logging.WARNING, args.logfile)

logging.info(pp.pformat(args))

for m in args.metadata:
    if not os.path.isabs(m):
        m = os.path.normpath(os.path.join(os.getcwd(), m))
    metadata = utilities.load_build(m)

    if args.dest_dir is None:
        logging.error('--dest-dir is required when using --template')
        sys.exit(1)

    template_params = {}
    template_params['metadata'] = metadata

    logging.debug(pp.pformat(template_params))

    file_name = args.dest_file
    if file_name is None:
        file_name = os.path.basename(args.template).replace('.mako', '')
    dest_file = os.path.join(args.dest_dir, file_name)
    generate_template.generate_template(args.template, template_params, dest_file)

