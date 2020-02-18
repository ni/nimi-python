<%
    import build.helper as helper

    config = template_parameters['metadata'].config
    module_name = config['module_name']
    driver_name = config['driver_name']
    if config['supports_nitclk'] or module_name == 'nitclk':
        wheel_env_no_py = '{}-wheel_dep'.format(module_name)
        wheel_env = 'py38-' + wheel_env_no_py + ','
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
envlist = ${wheel_env}py{35,36,37,38}-${module_name}-system_tests, py38-${module_name}-coverage
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
    ${module_name}-coverage: Report all coverage results to codecov.io

changedir =
% if uses_other_wheel:
    ${wheel_env_no_py}: ../../generated/${other_wheel}
% endif
    ${module_name}-system_tests: .
    ${module_name}-coverage: .

commands =
% if uses_other_wheel:
    ${wheel_env_no_py}: python.exe setup.py bdist_wheel --universal
% endif
    ${module_name}-system_tests: python --version
    # --disable-pip-version-check prevents pip from telling us we need to upgrade pip, since we are doing that now
    ${module_name}-system_tests: python -m pip install --disable-pip-version-check --upgrade pip
% if uses_other_wheel:
    ${module_name}-system_tests: python ../../tools/install_local_wheel.py --driver ${other_wheel} --start-path ../..
% endif
    ${module_name}-system_tests: python -c "import platform; print(platform.architecture())"
    ${module_name}-system_tests: python -c "import ${module_name}; ${module_name}.print_diagnostic_information()"
    ${module_name}-system_tests: coverage run --rcfile=../../tools/coverage_system_tests.rc --source ${module_name} --parallel-mode -m py.test ../../src/${module_name}/examples --junitxml=../../generated/junit/junit-${module_name}-{envname}-{env:BITNESS:64}.xml {posargs}
    ${module_name}-system_tests: coverage run --rcfile=../../tools/coverage_system_tests.rc --source ${module_name} --parallel-mode -m py.test ../../src/${module_name}/system_tests --junitxml=../../generated/junit/junit-${module_name}-{envname}-{env:BITNESS:64}.xml {posargs} --durations=5
    ${module_name}-coverage: coverage combine --rcfile=../../tools/coverage_system_tests.rc ./
    # Create the report to upload
    ${module_name}-coverage: coverage xml -i --rcfile=../../tools/coverage_system_tests.rc
    # Display the coverage results
    ${module_name}-coverage: coverage report --rcfile=../../tools/coverage_system_tests.rc
    # token is from codecov
    ${module_name}-coverage: codecov -X gcov --token=4c58f03d-b74c-489a-889a-ab0a77b7809f --no-color --flags ${module_name}systemtests --name ${module_name} --root ../.. --file ../../generated/${module_name}/coverage.xml

deps =
% if uses_other_wheel:
    ${wheel_env_no_py}: packaging
% endif
    ${module_name}-system_tests: pytest
    ${module_name}-system_tests: coverage
    ${module_name}-system_tests: numpy
    ${module_name}-system_tests: scipy
    ${module_name}-system_tests: fasteners
    ${module_name}-coverage: coverage
    ${module_name}-coverage: codecov

depends =
    ${module_name}-coverage: py{35,36,37,38}-${module_name}-system_tests
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
junit_family = xunit1

