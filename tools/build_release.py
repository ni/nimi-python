# !python

import argparse
from configure_logging import configure_logging
import logging
import pprint
from subprocess import check_call

pp = pprint.PrettyPrinter(indent=4, width=100)

default_python_cmd = ['python']
drivers_to_upload = ['nidcpower', 'nidigital', 'nidmm', 'niswitch', 'nimodinst', 'nifgen', 'niscope', 'nise', 'nitclk']
drivers_to_update = ['nifake'] + drivers_to_upload


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
    * `pip install --upgrade twine tox` into whichever Python 2.7 you use to build

Steps
    * Build master to ensure it is in a good state and ready for release
    * Ensure no commits are made on master until the release is complete
    * Create and checkout a branch for release-related changes
    * Update CHANGELOG.md
        * Delete empty (i.e. No changes) sub-sections under "Unreleased" section
        * Change the "Unreleased" header to the version of the release
        * Change [Unreleased] in TOC to the version of the release
        * Commit to branch
* Update contents of src/<driver>/LATEST_RELEASE with the versions of each module being released by dropping the `'.dev0' suffix.
    * `python3 tools/build_release.py --update --release`
        * This will update all the versions to remove any '.devN'
        * Commit to branch
    * `python3 tools/build_release.py --build`
        * Clean and build to update generated files with new version
        * Commit to branch
    * Create a pull request
        * It should contain all the changes made so far
        * Get the pull request reviewed but DO NOT merge to master yet
    * `python3 tools/build_release.py --upload`
        * Upload to PyPI - you will need to type in your credentials
    * Merge the pull request to origin/master
    * Create a release on GitHub using the portion from the changelog for this release for the description
        * Add the ZIP files under `generated/examples` for each module as a release artifact.
    * Create and checkout another branch for post-release changes
    * `python3 tools/build_release.py --update`
        * This will update the version to X.X.(N+1).dev0
        * Commit to branch
    * `python3 tools/build_release.py --build`
        * Clean and Build to update generated files
        * Commit to branch
    * Update changelog
        * Copy Unreleased section from bottom of changelog to the top and add a link to it in the TOC
        * Commit to branch
    * Create a pull request containing post-release changes and get it merged

"""
    parser = argparse.ArgumentParser(description=usage, formatter_class=CustomFormatter)

    build_group = parser.add_argument_group("Build configuration")
    build_group.add_argument("--release", action="store_true", default=False, help="This is a release build, so only remove '.devN'. build, then update with .dev0")
    build_group.add_argument("--upload", action="store_true", default=False, help="Upload build distributions to PyPI")
    build_group.add_argument("--update", action="store_true", default=False, help="Update version in config.py files")
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

        for d in drivers_to_update:
            logging.info(pp.pformat(python_cmd + ['tools/updateReleaseInfo.py', '--src-file', 'src/{}/metadata/config_addon.py'.format(d), ] + passthrough_params))
            check_call(python_cmd + ['tools/updateReleaseInfo.py', '--src-file', 'src/{}/metadata/config_addon.py'.format(d), ] + passthrough_params)

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
        for d in drivers_to_upload:
            complete_twine_cmd += ['generated/{}/dist/*'.format(d)]

        logging.info(pp.pformat(complete_twine_cmd))
        if not args.preview:
            check_call(complete_twine_cmd)


if __name__ == '__main__':
    main()

