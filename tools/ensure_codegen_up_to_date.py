"""
ensure_codegen_up_to_date
-------------------------
Ensure changes to code generation are committed to repository
"""

import os
import sys
import subprocess

def configure_git_credentials():
    """
    Configures git user name and email with dummy name and email
    """
    if os.system('git config user.email "dummy@ni.com"') != 0:
        print("Error: Unable to configure \"user email\" using git", file=sys.stderr)
        sys.exit(-1)

    if os.system('git config user.name "dummy"') != 0:
        print("Error: Unable to configure \"user name\" using git", file=sys.stderr)
        sys.exit(-1)

def clean_codegen_files():
    """
    Before code generation clean the existing codegen files
    """
    if os.system("tox -e clean") != 0:
        print("Error: Unable to clean the repo using \"tox -e clean\"", file=sys.stderr)
        sys.exit(-1)

def create_codegen_files():
    """
    create codegen files
    """
    if os.system("tox -e codegen") != 0:
        print("Error: Unable to generate code using \"tox -e codegen\"", file=sys.stderr)
        sys.exit(-1)

def check_file_status():
    '''
    Checks if there are any modified files
    '''
    return int(subprocess.check_output("git status -s -uno | wc -l", shell=True).decode().strip("b'\\n'"))

if __name__ == "__main__":
    """
    Main
    """
    configure_git_credentials()

    clean_codegen_files()
    create_codegen_files()

    if check_file_status() != 0:
        print("Run codegen and include the generated files in the PR", file=sys.stderr)
        sys.exit(-1)

    print("All changes to code generation are committed to repository")