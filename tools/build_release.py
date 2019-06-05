# !python

import argparse
import logging
import pprint
from subprocess import call
import sys

pp = pprint.PrettyPrinter(indent=4, width=100)

default_python_cmd = ['c://Python27//python.exe']


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
Update version when it is a dev version. I.e. X.Y.Z.devN to X.Y.Z.dev(N+1)
"""
    parser = argparse.ArgumentParser(description=usage)

    build_group = parser.add_argument_group("Build configuration")
    build_group.add_argument("--release", action="store_true", default=False, help="This is a release build, so only remove '.devN'. build, then update with .dev0")
    build_group.add_argument("--upload", action="store_true", default=False, help="Upload build distributions to PyPI")
    build_group.add_argument("--update", action="store_true", default=False, help="Update verion in config.py files")
    build_group.add_argument("--build", action="store_true", default=False, help="Clean and build")
    build_group.add_argument("--python-cmd", action="store", default=None, help="Command to use for invoking python. Default: {}".format(default_python_cmd))

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

    tox_cmd = python_cmd + ['-m', 'tox']
    twine_cmd = python_cmd + ['-m', 'twine']

    passthrough_params = ['-v' for i in range(args.verbose)]
    if args.test:
        passthrough_params.append('--test')
    if args.log_file:
        passthrough_params.append('--log-file').append(args.log_file)
    if args.release:
        passthrough_params.append('--release')

    if args.update:
        logging.info('Updating versions')
        logging.info(pp.pformat(python_cmd + ['tools/updateReleaseInfo.py', '--src-file', 'src/nifake/metadata/config_addon.py', ] + passthrough_params))
        call(python_cmd + ['tools/updateReleaseInfo.py', '--src-file', 'src/nifake/metadata/config_addon.py', ] + passthrough_params)
        logging.info(pp.pformat(python_cmd + ['tools/updateReleaseInfo.py', '--src-file', 'src/nidcpower/metadata/config_addon.py', ] + passthrough_params))
        call(python_cmd + ['tools/updateReleaseInfo.py', '--src-file', 'src/nidcpower/metadata/config_addon.py', ] + passthrough_params)
        logging.info(pp.pformat(python_cmd + ['tools/updateReleaseInfo.py', '--src-file', 'src/nidmm/metadata/config_addon.py', ] + passthrough_params))
        call(python_cmd + ['tools/updateReleaseInfo.py', '--src-file', 'src/nidmm/metadata/config_addon.py', ] + passthrough_params)
        logging.info(pp.pformat(python_cmd + ['tools/updateReleaseInfo.py', '--src-file', 'src/niswitch/metadata/config_addon.py', ] + passthrough_params))
        call(python_cmd + ['tools/updateReleaseInfo.py', '--src-file', 'src/niswitch/metadata/config_addon.py', ] + passthrough_params)
        logging.info(pp.pformat(python_cmd + ['tools/updateReleaseInfo.py', '--src-file', 'src/nimodinst/metadata/config_addon.py', ] + passthrough_params))
        call(python_cmd + ['tools/updateReleaseInfo.py', '--src-file', 'src/nimodinst/metadata/config_addon.py', ] + passthrough_params)
        logging.info(pp.pformat(python_cmd + ['tools/updateReleaseInfo.py', '--src-file', 'src/nifgen/metadata/config_addon.py', ] + passthrough_params))
        call(python_cmd + ['tools/updateReleaseInfo.py', '--src-file', 'src/nifgen/metadata/config_addon.py', ] + passthrough_params)
        logging.info(pp.pformat(python_cmd + ['tools/updateReleaseInfo.py', '--src-file', 'src/niscope/metadata/config_addon.py', ] + passthrough_params))
        call(python_cmd + ['tools/updateReleaseInfo.py', '--src-file', 'src/niscope/metadata/config_addon.py', ] + passthrough_params)
        logging.info(pp.pformat(python_cmd + ['tools/updateReleaseInfo.py', '--src-file', 'src/nise/metadata/config_addon.py', ] + passthrough_params))
        call(python_cmd + ['tools/updateReleaseInfo.py', '--src-file', 'src/nise/metadata/config_addon.py', ] + passthrough_params)

    if args.build:
        logging.info('Clean and build')
        logging.info(pp.pformat(tox_cmd + ['-e', 'clean']))
        logging.info(pp.pformat(tox_cmd))
        if not args.test:
            call(tox_cmd + ['-e', 'clean'])
            call(tox_cmd)

    if args.upload:
        logging.info('Uploading to PyPI')
        complete_twine_cmd = twine_cmd + ['upload', 'bin/nidcpower/dist/*', 'bin/nidmm/dist/*', 'bin/nimodinst/dist/*', 'bin/niswitch/dist/*', 'bin/nifgen/dist/*', 'bin/niscope/dist/*', 'bin/nise/dist/*']
        logging.info(pp.pformat(complete_twine_cmd))
        if not args.test:
            call(complete_twine_cmd)


if __name__ == '__main__':
    main()

