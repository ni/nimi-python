"""
ensure_codegen_up_to_date
-------------------------
Ensure changes to code generation are committed to repository
"""

import os
import subprocess
import sys


def configure_git_credentials():

    """Configures git user name and email with dummy name and email"""

    if os.system('git config user.email "dummy@ni.com"') != 0:
        sys.exit("Error: Unable to configure \"user email\" using git")

    if os.system('git config user.name "dummy"') != 0:
        sys.exit("Error: Unable to configure \"user name\" using git")


def configure_git_line_endings():
    if os.system('git config --global core.autocrlf false') != 0:
        sys.exit("Error: Unable to turn off line ending conversion")


def clean_codegen_files():

    """Before code generation clean the existing codegen files"""

    if os.system("tox -e clean") != 0:
        sys.exit("Error: Unable to clean the repo using \"tox -e clean\"")


def create_codegen_files():

    """create codegen files"""

    if os.system("tox -e codegen") != 0:
        sys.exit("Error: Unable to generate code using \"tox -e codegen\"")


def check_no_dirty_files():

    '''Checks if there are any modified files'''

    if int(subprocess.check_output("git status -s -uno | wc -l", shell=True).decode().strip("b'\\n'")) != 0:
        list_of_changed_files = subprocess.check_output("git status -s -uno", shell=True).decode()
        file_diffs = subprocess.check_output("git diff", shell=True).decode()
        sys.exit(f"The following code generated files do not match what is commited to Git. Run codegen and include the generated files in the PR.\n{list_of_changed_files}\n File diffs: \n{file_diffs} ")
    print("All changes to code generation are committed to repository")


if __name__ == "__main__":
    """
    Main
    """
    configure_git_credentials()
    configure_git_line_endings()

    clean_codegen_files()
    create_codegen_files()

    check_no_dirty_files()
