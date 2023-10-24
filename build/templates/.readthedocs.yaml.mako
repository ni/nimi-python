# .readthedocs.yaml
# Read the Docs configuration file
# See https://docs.readthedocs.io/en/stable/config-file/v2.html for details
<%
    config        = template_parameters['metadata'].config
    module_name   = config['module_name']
    # All of the files used to configure and build docs and readthedocs are in these 2 folders
    build_trigger_paths = f'docs/_static/ docs/{module_name}/'
    conf_py_path = f'docs/{module_name}/conf.py'
%>\

# Why Use A Configuration File?
# https://docs.readthedocs.io/en/stable/config-file/index.html
# The main advantages of using a configuration file over the web interface are:
# * Settings are per version rather than per project.
# * Settings live in your VCS.
# * They enable reproducible build environments over time.
# * Some settings are only available using a configuration file

# Required
version: 2

# Set the version of Python and other tools you might need
build:
  os: ubuntu-22.04
  tools:
    python: "3.11"
  jobs:
    # pre_build:
    #   # Check for broken external links
    #   - python -m sphinx -b linkcheck -D linkcheck_timeout=1 docs/ _build/linkcheck
    post_checkout:
      # https://docs.readthedocs.io/en/stable/build-customization.html#cancel-build-based-on-a-condition
      # Build-cancellation rules are recommended for monorepos.
      # Cancel building pull requests when there aren't changes in any of these paths: ${build_trigger_paths}.
      #
      # If there are no changes (git diff exits with 0) we force the command to return with 183.
      # This is a special exit code on Read the Docs that will cancel the build immediately.
      - |
        if [ "$READTHEDOCS_VERSION_TYPE" = "external" ] && git diff --quiet origin/master -- ${build_trigger_paths};
        then
          exit 183;
        fi

# Have Read the Docs build documentation with Sphinx
sphinx:
  builder: html
  configuration: ${conf_py_path}

# If using Sphinx, optionally build your docs in additional formats such as PDF
formats:
  - epub
  - pdf

# Declare the Python requirements required to build your docs
## TODO(ni-jfitzger): Create requirements file for docs to make builds reproducible. See https://github.com/ni/nimi-python/issues/1968
## Note: Our nimi-python readthedocs project used the defaults here: https://docs.readthedocs.io/en/stable/build-default-versions.html#external-dependencies
python:
  install:
  - requirements: docs/requirements.txt
