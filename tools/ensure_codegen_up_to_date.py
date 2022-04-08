"""
ensure_codegen_up_to_date
-------------------------
Ensure changes to code generation are committed to repository
"""

import os
import sys
import subprocess

def configure_git_user_email():
    """
    Configures git user email with dummy email id
    """
    if os.system('git config user.email "dummy@ni.com"') != 0:
        print("Unable to configure \"user email\" using git", file=sys.stderr)
        sys.exit(-1)

def configure_git_user_name():
    """
    Configures git user email with dummy name
    """
    if os.system('git config user.name "dummy"') != 0:
        print("Unable to configure \"user name\" using git", file=sys.stderr)
        sys.exit(-1)

def get_commit_id():
    """
    Returns the commit id
    Returns:
        [str]: Returns the commit id
    """
    return subprocess.check_output("git log -1 --format=%h", shell=True).decode().strip("b'\\n'")

def clean_codegen_files():
    """
    Before code generation clean the existing codegen files
    """
    if os.system("tox -e clean") != 0:
        print("Unable to clean the repo using \"tox -e clean\"", file=sys.stderr)
        sys.exit(-1)

def create_codegen_files():
    """
    create codegen files
    """
    if os.system("tox -e codegen") != 0:
        print("Unable to generate code using \"tox -e codegen\"", file=sys.stderr)
        sys.exit(-1)

def add_codegen_files_to_git_staging_area():
    """
    Add the codegen files to git staging area.
    No files will be added to git staging area if
      1) No new files are generated
      2) No existing files are modified/deleted.
    """
    if os.system('git add .') != 0:
        print("Unable to add files to git", file=sys.stderr)
        sys.exit(-1)

def commit_git_staging_area_files():
    """
    Commits the staging area files with dummy message
    If no files are present in the staging area then no new commit will be created.
    """
    os.system('git commit -m "dummy"') # return code is 1 if there are no files to commit

def reset_dummy_commit():
    if os.system("git reset --soft HEAD~1") != 0:
        print("Unable to reset dummy commit")
        sys.exit(-1)

if __name__ == "__main__":
    """
    Main
    """
    # Configure git credentials
    configure_git_user_email()
    configure_git_user_name()

    commit_id_before_code_generator = get_commit_id()

    clean_codegen_files()
    create_codegen_files()
    add_codegen_files_to_git_staging_area()
    commit_git_staging_area_files()

    commit_id_after_code_generator = get_commit_id()


    if commit_id_before_code_generator != commit_id_after_code_generator:
        print("Run codegen and include the generated files in the PR", file=sys.stderr)
        reset_dummy_commit()
        sys.exit(-1)

    print("All changes to code generation are committed to repository")