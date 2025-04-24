import argparse
from configure_logging import configure_logging
import logging
import os
import pprint
import re

pp = pprint.PrettyPrinter(indent=4, width=100)


# Increment version based on bump type ('major', 'minor', 'patch').
def bump_version(version, bump_type):
    major, minor, patch = map(int, version.split('.'))

    if bump_type == 'patch':
        patch += 1
    elif bump_type == 'minor':
        minor += 1
        patch = 0
    elif bump_type == 'major':
        major += 1
        minor = 0
        patch = 0

    return f"{major}.{minor}.{patch}"


def main():
    usage = """
Update version in files. Example: X.Y.Z.devN to X.Y.Z
"""
    parser = argparse.ArgumentParser(description=usage)
    file_group = parser.add_argument_group("Input and Output files")
    file_group.add_argument("--src-folder", action="store", required=True, help="Source folder")
    file_group.add_argument("--release", action="store_true", default=False, help="This is a release build, so only remove '.devN'. Error if not there")
    file_group.add_argument("--update-type", action="store", default=None, choices=["major", "minor", "patch"], help="Specify the type of update: major, minor or patch. ")

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
    metadata_file = os.path.join(args.src_folder, "metadata", "config_addon.py")
    with open(metadata_file) as content_file:
        contents = content_file.read()

    module_version_re = re.compile(r"'module_version': '(\d+\.\d+\.\d+)(?:\.dev(\d+))?'")
    m = module_version_re.search(contents)
    logging.debug(f"Version regex match: {m}")

    if m:
        base_version = m.group(1)
        dev_number = int(m.group(2)) if m.group(2) else None

        if dev_number is not None:
            logging.info("Dev version found")
            current_version = f"{base_version}.dev{dev_number}"
        else:
            logging.info("Release version found")
            current_version = base_version

        if args.release:
            if dev_number is not None:
                new_version = base_version
            else:
                logging.error("Error: Attempting to release an already released version.")
                return
        else:
            bumped_version = bump_version(base_version, args.update_type)
            new_version = f"{bumped_version}.dev0"

        logging.info(f"Updating {current_version} to {new_version}")
        contents = module_version_re.sub(f"'module_version': '{new_version}'", contents)

    if not args.preview:
        with open(metadata_file, 'w') as content_file:
            content_file.write(contents)

    if args.release and "nifake" not in args.src_folder:
        latest_release_file = os.path.join(args.src_folder, "LATEST_RELEASE")
        logging.info(f'Updating version in {latest_release_file} to {new_version}.')
        if not args.preview:
            with open(latest_release_file, 'w') as content_file:
                content_file.write(f'{new_version}\n')


if __name__ == '__main__':
    main()
