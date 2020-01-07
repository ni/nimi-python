# !python

import argparse
import codecs
import logging
from mako.exceptions import RichTraceback
from mako.lookup import TemplateLookup
from mako.template import Template
import pprint
import sys


pp = pprint.PrettyPrinter(indent=4, width=100)


def generate_template(template_name, template_params, dest_file):
    try:
        template_params['encoding_tag'] = '# -*- coding: utf-8 -*-'
        lookup = TemplateLookup(directories=['build/templates'])
        template = Template(filename=template_name, lookup=lookup)
        rendered_template = template.render(template_parameters=template_params)

    except Exception:
        # Because mako expands into python, we catch all errors, not just MakoException.
        # Ideally, we'd use text_error_template, but it sucks.  html_error_template,
        # however, is useful.  Unfortunately emitting html isn't acceptable.  So we
        # re-implement using mako.exceptions.RichTraceback here.
        tback = RichTraceback(traceback=None)
        line = tback.lineno
        lines = tback.source.split('\n')

        # The underlying error.
        logging.error("\n%s: %s\n" % (str(tback.error.__class__.__name__), str(tback.error)))
        logging.error("Offending Template: %s\n" % template_name)

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

    logging.debug(rendered_template)
    if sys.version_info.major < 3:
        file_handle_public = codecs.open(dest_file, mode="w", encoding='utf-8')
        file_handle_public.write(rendered_template)
        file_handle_public.close()
    else:
        file_handle_public = open(dest_file, 'wb')
        file_handle_public.write(bytes(rendered_template, "UTF-8"))
        file_handle_public.close()


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
Run generate_template on the requested mako template
"""
    parser = argparse.ArgumentParser(description=usage)
    file_group = parser.add_argument_group("Input and Output files")
    file_group.add_argument("--output-file", action="store", required=True, help="Output file")
    file_group.add_argument("--template", action="store", required=True, help="Template file")

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

    template_params = {}
    generate_template(args.template, template_params, args.output_file)


if __name__ == '__main__':
    main()






