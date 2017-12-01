#!/usr/bin/python3

import codecs
import logging
from mako.exceptions import RichTraceback
from mako.lookup import TemplateLookup
from mako.template import Template
import pprint
import sys

pp = pprint.PrettyPrinter(indent=4)


def generate_template(template_name, template_params, dest_file, in_zip_file=False):
    try:
        module_name = template_params['metadata'].config['module_name']
        lookup = TemplateLookup(directories=['build/templates', 'src/{0}/templates'.format(module_name)])
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



