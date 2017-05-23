#!/usr/bin/python

from mako.template import Template
from mako.exceptions import RichTraceback
import logging
import argparse
import sys, os

import pprint
pp = pprint.PrettyPrinter(indent=3)

types = {
    'ViStatus': 'c_long',
    'ViRsrc': 'c_char_p',
    'ViBoolean': 'c_ushort',
    'ViSession': 'c_ulong',
    'ViChar': 'c_char_p',
    'ViInt32': 'c_ulong',
    'ViReal64': 'c_double',
}

def configureLogging(lvl = logging.WARNING, logfile = None):
    root = logging.getLogger()
    root.setLevel(lvl)
    formatter = logging.Formatter('%(funcName)s - %(levelname)s - %(message)s')
    if logfile is None:
        hndlr = logging.StreamHandler(sys.stdout)
    else:
        print("Logging to file %s" % logfile)
        hndlr = logging.FileHandler(logfile)
    hndlr.setFormatter(formatter)
    root.addHandler(hndlr)

def main():
    # Setup the required arguments for this script
    usage = "usage: " + sys.argv[0] + " [options]"

    parser = argparse.ArgumentParser(description=usage)
    fileGroup = parser.add_argument_group("Input and Output files")
    fileGroup.add_argument(
        "--template",
        action="store", dest="template", default=None, required=True,
        help="Mako template to use")
    fileGroup.add_argument(
        "--dest-file",
        action="store", dest="dest", default=None, required=True,
        help="Output file")
    fileGroup.add_argument(
        "--metadata",
        action="store", dest="metadata", default=None, required=True,
        help="Metadata")

    verbosityGroup = parser.add_argument_group("Verbosity, Logging & Debugging")
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

    metadata = dict()
    with open(args.metadata) as f:
        logging.debug("Reading metadata")
        code = compile(f.read(), args.metadata, 'exec')
        exec(code, metadata)

    template = Template(filename=args.template)
    templateParams = {}
    templateParams['functions'] = metadata['functions']
    templateParams['attributes'] = metadata['attributes']
    templateParams['config'] = metadata['config']
    templateParams['types'] = types

    logging.debug(pp.pformat(templateParams))

    try:
        renderedTemplate = template.render(templateParameters=templateParams)

    except:
        # Because mako expands into python, we catch all errors, not just MakoException.
        # Ideally, we'd use text_error_template, but it sucks.  html_error_template,
        # however, is useful.  Unfortunately emitting html isn't acceptable.  So we
        # re-implement using mako.exceptions.RichTraceback here.
        tback = RichTraceback(traceback=None)
        line = tback.lineno
        lines = tback.source.split('\n')

        # The underlying error.
        logging.error("\n%s: %s\n" % ( str(tback.error.__class__.__name__), str(tback.error) ))
        logging.error("Offending Template: %s\n" % args.template)

        # Show a source listing of the template, with offending line marked.
        for index in range(max(0, line - 4), min(len(lines), line + 5)):
            if index + 1 == line:
                logging.error(">> %#08d: %s" % (index + 1, lines[index]))
            else:
                logging.error("   %08d: %s" % (index + 1, lines[index]))

        logging.error("\nTraceback (most recent call last):")
        for (filename, lineno, function, line) in tback.reverse_traceback:
            logging.error("   File %s, line %d, in %s\n     %s" % (filename, lineno, function, line))

        logging.error("\n")
        sys.exit(1)

    print(renderedTemplate)
    fileHandlePublic = open(args.dest, 'w')
    fileHandlePublic.write(renderedTemplate)
    fileHandlePublic.close()


if __name__ == '__main__':
    main()

