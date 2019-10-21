# !python

import argparse
import logging
import pprint
from subprocess import check_call
import sys

pp = pprint.PrettyPrinter(indent=4, width=100)

default_python_cmd = ['c:/Python27/python.exe']


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


class CustomFormatter(argparse.ArgumentDefaultsHelpFormatter, argparse.RawDescriptionHelpFormatter):
    '''We want the description to use the raw formatting but have the parameters be formatted as before

    from stackoverflow:
    https://stackoverflow.com/questions/18462610/argumentparser-epilog-and-description-formatting-in-conjunction-with-argumentdef
    '''
    pass


def main():
    # Setup the required arguments for this script
    usage = """Release script
Prereqs
    * Be able to build locally
    * `pip install --upgrade twine` into whichever Python 2.7 you use to build

Steps
    * Make sure master is ready for release
        * Update the changelog to show the version of the release
        * Change unreleased in TOC to new version
        * Commit to master
    * `c:\\Python36\\python.exe tools\\build_release.py --update --release`
        * This will update all the versions to remove any '.devN'
        * Commit to master
    * `c:\\Python36\\python.exe tools\\build_release.py --build`
        * Clean and build to update generated files with new version
        * Commit to master
    * `c:\\Python36\\python.exe tools\\build_release.py --upload`
        * Upload to PyPI - you will need to type in your credentials
    * Push all changes to GitHub
    * Create a release on GitHub using the portion from the changelog for this release for the description
    * `c:\\Python36\\python.exe tools\\build_release.py --update`
        * This will update the version to X.X.(N+1).dev0
        * Commit to master
    * `c:\\Python36\\python.exe tools\\build_release.py --build`
        * Clean and Build to update generated files
        * Commit to master
    * Copy Unreleased section from bottom of changelog to the top and add a link to it in the TOC
    * Push to GitHub

"""
    parser = argparse.ArgumentParser(description=usage, formatter_class=CustomFormatter)

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
    if args.preview:
        passthrough_params.append('--preview')
    if args.log_file:
        passthrough_params.append('--log-file').append(args.log_file)
    if args.release:
        passthrough_params.append('--release')

    if args.update:
        logging.info('Updating versions')
        logging.info(pp.pformat(python_cmd + ['tools/updateReleaseInfo.py', '--src-file', 'src/nifake/metadata/config_addon.py', ] + passthrough_params))
        check_call(python_cmd + ['tools/updateReleaseInfo.py', '--src-file', 'src/nifake/metadata/config_addon.py', ] + passthrough_params)
        logging.info(pp.pformat(python_cmd + ['tools/updateReleaseInfo.py', '--src-file', 'src/nidcpower/metadata/config_addon.py', ] + passthrough_params))
        check_call(python_cmd + ['tools/updateReleaseInfo.py', '--src-file', 'src/nidcpower/metadata/config_addon.py', ] + passthrough_params)
        logging.info(pp.pformat(python_cmd + ['tools/updateReleaseInfo.py', '--src-file', 'src/nidmm/metadata/config_addon.py', ] + passthrough_params))
        check_call(python_cmd + ['tools/updateReleaseInfo.py', '--src-file', 'src/nidmm/metadata/config_addon.py', ] + passthrough_params)
        logging.info(pp.pformat(python_cmd + ['tools/updateReleaseInfo.py', '--src-file', 'src/niswitch/metadata/config_addon.py', ] + passthrough_params))
        check_call(python_cmd + ['tools/updateReleaseInfo.py', '--src-file', 'src/niswitch/metadata/config_addon.py', ] + passthrough_params)
        logging.info(pp.pformat(python_cmd + ['tools/updateReleaseInfo.py', '--src-file', 'src/nimodinst/metadata/config_addon.py', ] + passthrough_params))
        check_call(python_cmd + ['tools/updateReleaseInfo.py', '--src-file', 'src/nimodinst/metadata/config_addon.py', ] + passthrough_params)
        logging.info(pp.pformat(python_cmd + ['tools/updateReleaseInfo.py', '--src-file', 'src/nifgen/metadata/config_addon.py', ] + passthrough_params))
        check_call(python_cmd + ['tools/updateReleaseInfo.py', '--src-file', 'src/nifgen/metadata/config_addon.py', ] + passthrough_params)
        logging.info(pp.pformat(python_cmd + ['tools/updateReleaseInfo.py', '--src-file', 'src/niscope/metadata/config_addon.py', ] + passthrough_params))
        check_call(python_cmd + ['tools/updateReleaseInfo.py', '--src-file', 'src/niscope/metadata/config_addon.py', ] + passthrough_params)
        logging.info(pp.pformat(python_cmd + ['tools/updateReleaseInfo.py', '--src-file', 'src/nise/metadata/config_addon.py', ] + passthrough_params))
        check_call(python_cmd + ['tools/updateReleaseInfo.py', '--src-file', 'src/nise/metadata/config_addon.py', ] + passthrough_params)
        logging.info(pp.pformat(python_cmd + ['tools/updateReleaseInfo.py', '--src-file', 'src/nitclk/metadata/config_addon.py', ] + passthrough_params))
        check_call(python_cmd + ['tools/updateReleaseInfo.py', '--src-file', 'src/nitclk/metadata/config_addon.py', ] + passthrough_params)

    if args.build:
        logging.info('Clean and build')
        logging.info(pp.pformat(tox_cmd + ['-e', 'clean']))
        logging.info(pp.pformat(tox_cmd))
        logging.info(pp.pformat(tox_cmd + ['-e', 'pkg']))
        if not args.preview:
            check_call(tox_cmd + ['-e', 'clean'])
            check_call(tox_cmd)

    if args.upload:
        logging.info('Uploading to PyPI')
        complete_twine_cmd = twine_cmd + ['upload', 'bin/nidcpower/dist/*', 'bin/nidigital/dist/*', 'bin/nidmm/dist/*', 'bin/nimodinst/dist/*', 'bin/niswitch/dist/*', 'bin/nifgen/dist/*', 'bin/niscope/dist/*', 'bin/nise/dist/*', 'bin/nitclk/dist/*']
        logging.info(pp.pformat(complete_twine_cmd))
        if not args.preview:
            check_call(complete_twine_cmd)


if __name__ == '__main__':
    main()

