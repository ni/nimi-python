# !python

import argparse
from configure_logging import configure_logging
import logging
import pprint
from subprocess import check_call

pp = pprint.PrettyPrinter(indent=4, width=100)

default_python_cmd = ['python']

class CustomFormatter(argparse.ArgumentDefaultsHelpFormatter, argparse.RawDescriptionHelpFormatter):
    '''We want the description to use the raw formatting but have the parameters be formatted as before

    from stackoverflow:
    https://stackoverflow.com/questions/18462610/argumentparser-epilog-and-description-formatting-in-conjunction-with-argumentdef
    '''
    pass


def main():
    drivers_to_update = ['nidcpower', 'nidigital', 'nidmm', 'nifake','niswitch', 'nimodinst', 'nifgen', 'niscope', 'nise', 'nitclk']


    # Setup the required arguments for this script
    usage = """Release script
Prereqs
    * Be able to build locally
    * `pip install --upgrade twine tox` into whichever Python you use to build
Steps: see "Release Process" section of CONTRIBUTING.md
"""
    parser = argparse.ArgumentParser(description=usage, formatter_class=CustomFormatter)

    build_group = parser.add_argument_group("Build configuration")
    build_group.add_argument("--upload", action="store_true", default=False, help="Upload build distributions to PyPI")
    build_group.add_argument("--build", action="store_true", default=False, help="Clean and build")
    build_group.add_argument("--python-cmd", action="store", default=None, help=f"Command to use for invoking python. Default: {default_python_cmd}")
    build_group.add_argument("--drivers",action="store",default=None,help="Comma-separated list of drivers to update. Default: All Drivers")
    build_group.add_argument("--increment-major-version", action="store_true", default=False, help="Increment the major version")
    build_group.add_argument("--increment-minor-version", action="store_true", default=False, help="Increment the minor version")
    build_group.add_argument("--increment-patch-version", action="store_true", default=False, help="Increment the patch version")
    build_group.add_argument("--increment-build-number", action="store_true", default=False, help="Increment the build number")
    build_group.add_argument("--update-for-release", action="store_true", default=False, help="This is a release build, so only remove '.devN'. build, then update with .dev0")

    verbosity_group = parser.add_argument_group("Verbosity, Logging & Debugging")
    verbosity_group.add_argument("-v", "--verbose", action="count", default=0, help="Verbose output")
    verbosity_group.add_argument("--preview", action="store_true", default=False, help="Show what would happen when running with given parameters")
    verbosity_group.add_argument("--log-file", action="store", default=None, help="Send logging to listed file instead of stdout")
    args = parser.parse_args()

    # Validate that only one of the version-related flags is provided
    version_flags = [
        args.increment_major_version,
        args.increment_minor_version,
        args.increment_patch_version,
        args.increment_build_number,
    ]
    if sum(version_flags) > 1:
        raise ValueError("Only one of --increment-major-version, --increment-minor-version, --increment-patch-version or --increment-build-number can be provided.")


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
    if args.update_for_release:
        passthrough_params.append('--release')
    if args.increment_build_number:
        passthrough_params.append(f'--update-type=build')
    if args.increment_patch_version:
        passthrough_params.append(f'--update-type=patch')
    if args.increment_minor_version:
        passthrough_params.append(f'--update-type=minor')
    if args.increment_major_version:
        passthrough_params.append(f'--update-type=major')


    if args.drivers:
        provided_drivers = args.drivers.split(",")
        invalid_drivers = [driver for driver in provided_drivers if driver not in drivers_to_update]

        if invalid_drivers:
            raise ValueError(f"The following drivers are invalid: {', '.join(invalid_drivers)}. Valid drivers are: {','.join(drivers_to_update)}")
        drivers_to_update = provided_drivers
          
    
    
    if any([args.increment_major_version, args.increment_minor_version, args.increment_patch_version, args.increment_build_number, args.update_for_release]):
        logging.info('Updating versions')

        for d in drivers_to_update:
            logging.info(pp.pformat(python_cmd + ['tools/updateReleaseInfo.py','--src-folder', f'src/{d}',] + passthrough_params))
            check_call(python_cmd + ['tools/updateReleaseInfo.py','--src-folder', f'src/{d}', ] + passthrough_params)

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
        complete_twine_cmd = twine_cmd + ['upload']
        drivers_to_upload = [driver for driver in drivers_to_update if driver != 'nifake']
        for d in drivers_to_upload:
            complete_twine_cmd += [f'generated/{d}/dist/*']

        logging.info(pp.pformat(complete_twine_cmd))
        if not args.preview:
            check_call(complete_twine_cmd)


if __name__ == '__main__':
    main()

