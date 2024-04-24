# !python

import argparse
from configure_logging import configure_logging
import logging
import os
import pprint
from subprocess import check_call

pp = pprint.PrettyPrinter(indent=4, width=100)

default_python_cmd = ['python']
ni_owned_modules = [
    'hightime',
    'nidcpower',
    'nidigital',
    'nidmm',
    'nifake',
    'nifgen',
    'nimodinst',
    'niscope',
    'nise',
    'niswitch',
    'nitclk',
]

class CustomFormatter(argparse.ArgumentDefaultsHelpFormatter, argparse.RawDescriptionHelpFormatter):
    '''We want the description to use the raw formatting but have the parameters be formatted as before

    from stackoverflow:
    https://stackoverflow.com/questions/18462610/argumentparser-epilog-and-description-formatting-in-conjunction-with-argumentdef
    '''
    pass


def main():
    # Setup the required arguments for this script
    usage = """Log and process list of python deps used in the project"""

    parser = argparse.ArgumentParser(description=usage, formatter_class=CustomFormatter)

    report_group = parser.add_argument_group("Reporting Configuration")
    report_group.add_argument("--clean", action="store_true", default=False, help="Clean the dep list file")
    report_group.add_argument("--log", action="store_true", default=False, help="Log the deps installed to the tox env.")
    report_group.add_argument("--env_name", action="store", default=None, help="The name of the tox env used")
    report_group.add_argument("--report", action="store_true", default=False, help="Report all unique deps and versions used.")
    report_group.add_argument("--python-cmd", action="store", default=None, help=f"Command to use for invoking python. Default: {default_python_cmd}")
    report_group.add_argument("--dir", action="store", default=None, help=f"Working directory to change to before running commands")

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

    python_cmd = [args.python_cmd] if args.python_cmd is not None else default_python_cmd
    dep_list_file = 'pip_list.txt'

    passthrough_params = ['-v' for i in range(args.verbose)]
    if args.log_file:
        passthrough_params.append('--log-file').append(args.log_file)

    if args.dir:
        os.chdir(args.dir)

    if args.clean:
        logging.info('Cleaning Logged Deps')
        with open(dep_list_file, 'w') as f:
            f.write('')

    if args.log:
        logging.info('Logging Deps')
        env_label_cmd = ['echo', args.env_name]
        pip_list_cmd = python_cmd + ['-m', 'pip', 'list', '--format=freeze']
        logging.info(pp.pformat(env_label_cmd))
        logging.info(pp.pformat(pip_list_cmd))
        with open(dep_list_file, 'a') as f:
            check_call(env_label_cmd, stdout=f)
            check_call(pip_list_cmd, stdout=f)

    if args.report:
        logging.info('Reporting Deps')
        with open(dep_list_file, 'r') as f:
            deps = f.readlines()

        deps = [dep.strip() for dep in deps if "==" in dep]
        deps = list(set(deps))
        
        with open(f'sorted_{dep_list_file}', 'w') as f:
            for dep in sorted(deps):
                if dep.split('==')[0] in ni_owned_modules:
                    continue
                logging.info(dep)
                f.write(f'{dep}\n')




if __name__ == '__main__':
    main()

