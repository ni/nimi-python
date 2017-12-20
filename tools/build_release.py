# !python

import argparse
import logging
import pprint
from subprocess import call
import sys

python_cmd = 'py'
tox_cmd = [python_cmd, '-m', 'tox']

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
Update version when it is a dev version. I.e. X.Y.Z.devN to X.Y.Z.dev(N+1)
"""
    parser = argparse.ArgumentParser(description=usage)

    verbosity_group = parser.add_argument_group("Verbosity, Logging & Debugging")
    verbosity_group.add_argument("--release", action="store_true", default=False, help="This is a release build, so only remove '.devN'. build, then update with .dev0")
    verbosity_group.add_argument("--upload", action="store_true", default=False, help="Upload build distributions to PyPI")
    verbosity_group.add_argument("-v", "--verbose", action="count", default=0, help="Verbose output")
    verbosity_group.add_argument("--test", action="store_true", default=False, help="Run doctests and quit")
    verbosity_group.add_argument("--log-file", action="store", default=None, help="Send logging to listed file instead of stdout")
    args = parser.parse_args()

    if args.verbose > 1:
        configure_logging(logging.DEBUG, args.log_file)
    elif args.verbose == 1:
        configure_logging(logging.INFO, args.log_file)
    else:
        configure_logging(logging.WARNING, args.log_file)

    logging.info(pp.pformat(args))


    twine_cmd = [python_cmd, '-m' 'twine']

    passthrough_params = ['-v' for i in range(args.verbose)]
    if args.test:
        passthrough_params.append('--test')
    if args.log_file:
        passthrough_params.append('--log-file').append(args.log_file)

    if args.release:
        logging.info('Updating versions for release')
        call([python_cmd, 'tools/updateReleaseInfo.py', '--src-file', 'src/nidcpower/metadata/config.py', '--release'] + passthrough_params)
        call([python_cmd, 'tools/updateReleaseInfo.py', '--src-file', 'src/nidmm/metadata/config.py', '--release'] + passthrough_params)
        call([python_cmd, 'tools/updateReleaseInfo.py', '--src-file', 'src/niswitch/metadata/config.py', '--release'] + passthrough_params)
        call([python_cmd, 'tools/updateReleaseInfo.py', '--src-file', 'src/nimodinst/metadata/config.py', '--release'] + passthrough_params)
        call([python_cmd, 'tools/updateReleaseInfo.py', '--src-file', 'src/nifgen/metadata/config.py', '--release'] + passthrough_params)
        call([python_cmd, 'tools/updateReleaseInfo.py', '--src-file', 'src/niscope/metadata/config.py', '--release'] + passthrough_params)
        call([python_cmd, 'tools/updateReleaseInfo.py', '--src-file', 'docs/conf.py', '--release'] + passthrough_params)

    logging.info('Clean and build')
    logging.info(pp.pformat(tox_cmd + ['-e', 'clean']))
    logging.info(pp.pformat(tox_cmd))
    call(tox_cmd + ['-e', 'clean'])
    call(tox_cmd)

    if args.upload:
        logging.info('Uploading to PyPI')
        call(twine_cmd + ['upload', 'bin/nidcpower/dist/*', 'bin/nidmm/dist/*', 'bin/nimodinst/dist/*', 'bin/niswitch/dist/*', 'bin/nifgen/dist/*', 'bin/niscope/dist/*'])

    logging.info('Updating versions for next dev release')
    call([python_cmd, 'tools/updateReleaseInfo.py', '--src-file', 'src/nidcpower/metadata/config.py'] + passthrough_params)
    call([python_cmd, 'tools/updateReleaseInfo.py', '--src-file', 'src/nidmm/metadata/config.py'] + passthrough_params)
    call([python_cmd, 'tools/updateReleaseInfo.py', '--src-file', 'src/niswitch/metadata/config.py'] + passthrough_params)
    call([python_cmd, 'tools/updateReleaseInfo.py', '--src-file', 'src/nimodinst/metadata/config.py'] + passthrough_params)
    call([python_cmd, 'tools/updateReleaseInfo.py', '--src-file', 'src/nifgen/metadata/config.py'] + passthrough_params)
    call([python_cmd, 'tools/updateReleaseInfo.py', '--src-file', 'src/niscope/metadata/config.py'] + passthrough_params)
    call([python_cmd, 'tools/updateReleaseInfo.py', '--src-file', 'docs/conf.py'] + passthrough_params)

    logging.info('Rebuild to update generated files')
    call(tox_cmd)


if __name__ == '__main__':
    main()

