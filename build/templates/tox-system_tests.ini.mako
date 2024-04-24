<%
    import build.helper as helper
    import os

    grpc_supported = template_parameters['include_grpc_support']

    config = template_parameters['metadata'].config
    module_name = config['module_name']
    driver_name = config['driver_name']
    if config['uses_nitclk'] or module_name == 'nitclk':
        wheel_env_no_py = '{}-wheel_dep'.format(module_name)
        wheel_env = 'py3-' + wheel_env_no_py + ','
        uses_other_wheel = True
        if module_name == 'nitclk':
            # nitclk system tests use niscope
            other_wheel = 'niscope'
        else:
            other_wheel = 'nitclk'
    else:
        wheel_env = ''
        other_wheel = ''
        uses_other_wheel = False
%>\
# Tox (http://tox.testrun.org/) is a tool for running tests
# in multiple virtualenvs. This configuration file will run the
# test suite on all supported python versions. To use it, "pip install tox"
# and then run "tox -c tox-system_tests.ini" from the driver directory. (generated/${module_name})
[tox]
envlist = ${wheel_env}py{38,39,310,311,312}-${module_name}-system_tests, py312-${module_name}-coverage
skip_missing_interpreters=True
ignore_basepython_conflict=True
# We put the .tox directory outside of the Jenkins workspace so that it isn't wiped with the rest of the repo
toxworkdir = ../../../.tox

[testenv]
description =
% if uses_other_wheel:
    ${wheel_env_no_py}: Build the ${other_wheel} wheel because we use it in ${module_name} tests
% endif
    ${module_name}-system_tests: Run ${module_name} system tests (requires ${driver_name} runtime to be installed)
    ${module_name}-coverage: Prepare coverage report for upload to codecov.io  # upload handled by GitHub Actions

changedir =
% if uses_other_wheel:
    ${wheel_env_no_py}: ../${other_wheel}
% endif
    ${module_name}-system_tests: .
    ${module_name}-coverage: .

commands =
% if uses_other_wheel:
    ${wheel_env_no_py}: python -m build --wheel

% endif
    # --disable-pip-version-check prevents pip from telling us we need to upgrade pip, since we are doing that now
    ${module_name}-system_tests: python -m pip install --disable-pip-version-check --upgrade pip
% if uses_other_wheel:
    ${module_name}-system_tests: python ../../tools/install_local_wheel.py --driver ${other_wheel} --start-path ../..
% endif
    ${module_name}-system_tests: python -c "import ${module_name}; ${module_name}.print_diagnostic_information()"
    ${module_name}-system_tests: coverage run --rcfile=../../tools/coverage_system_tests.rc --source ${module_name} --parallel-mode -m pytest ../../src/${module_name}/examples --junitxml=../junit/junit-${module_name}-{envname}-examples-{env:BITNESS:64}.xml {posargs}
    ${module_name}-system_tests: coverage run --rcfile=../../tools/coverage_system_tests.rc --source ${module_name} --parallel-mode -m pytest ../../src/${module_name}/system_tests -c tox-system_tests.ini --junitxml=../junit/junit-${module_name}-{envname}-{env:BITNESS:64}.xml --durations=5 {posargs}

    ${module_name}-coverage: coverage combine --rcfile=../../tools/coverage_system_tests.rc ./
    # Create the report to upload
    ${module_name}-coverage: coverage xml -i --rcfile=../../tools/coverage_system_tests.rc
    # Display the coverage results
    ${module_name}-coverage: coverage report --rcfile=../../tools/coverage_system_tests.rc

deps =
% if uses_other_wheel:
    ${wheel_env_no_py}: build

% endif
    ${module_name}-system_tests: pytest
    ${module_name}-system_tests: coverage
    ${module_name}-system_tests: numpy
    ${module_name}-system_tests: hightime
    ${module_name}-system_tests: fasteners
    ${module_name}-system_tests: pytest-json
% if grpc_supported:
    ${module_name}-system_tests: .[grpc]
% endif

    ${module_name}-coverage: coverage

depends =
    ${module_name}-coverage: py{38,39,310,311,312}-${module_name}-system_tests
% if uses_other_wheel:
    ${module_name}-system_tests: ${wheel_env}
% endif

passenv =
    GIT_BRANCH
    GIT_COMMIT
    BUILD_URL
    BRANCH_NAME
    JENKINS_URL
    BUILD_NUMBER

[pytest]
addopts = --verbose
filterwarnings =
   error::pytest.PytestUnhandledThreadExceptionWarning
norecursedirs = .* build dist CVS _darcs {arch} *.egg venv
junit_suite_name = nimi-python
junit_family = xunit1
% if module_name == 'nidcpower':
markers = # Defines custom markers used by nidcpower system tests. Prevents PytestUnknownMarkWarning.
    include_legacy_session: Include a legacy session in nidcpower system tests.
    legacy_session_only: Exclude an independent channels session in nidcpower system tests.
    resource_name: Overrides the default resource_name argument in the nidcpower session fixture.
    channels: Overrides the default channels argument in the nidcpower session fixture.
    reset: Overrides the default reset argument in the nidcpower session fixture.
    options: Overrides the default options argument in the nidcpower session fixture.
    independent_channels: Overrides the default independent_channels argument in the nidcpower session fixture.
% endif
