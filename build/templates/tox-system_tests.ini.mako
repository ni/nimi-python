<%
    import build.helper as helper

    config = template_parameters['metadata'].config
    module_name = config['module_name']
    driver_name = config['driver_name']
    if config['supports_nitclk']:
        nitclk_env = 'py38-{}-nitclk_wheel,'.format(module_name)
    else:
        nitclk_env = ''
%>\
# Tox (http://tox.testrun.org/) is a tool for running tests
# in multiple virtualenvs. This configuration file will run the
# test suite on all supported python versions. To use it, "pip install tox"
# and then run "tox -c tox-system_tests.ini" from the driver directory. (generated/${module_name})
[tox]
envlist = ${nitclk_env}py{35,36,37,38,py3}-${module_name}-system_tests, py38-${module_name}-coverage
skip_missing_interpreters=True
ignore_basepython_conflict=True
# We put the .tox directory outside of the Jenkins workspace so that it isn't wiped with the rest of the repo
toxworkdir = ../../../.tox

[testenv]
description =
% if config['supports_nitclk']:
    ${module_name}-nitclk_wheel: Build the nitclk wheel
% endif
    ${module_name}-system_tests: Run ${module_name} system tests (requires ${driver_name} runtime to be installed)
    ${module_name}-coverage: Report all coverage results to codecov.io

changedir =
% if config['supports_nitclk']:
    ${module_name}-nitclk_wheel: ../../generated/nitclk
% endif
    ${module_name}-system_tests: .
    ${module_name}-coverage: .

commands =
% if config['supports_nitclk']:
    ${module_name}-nitclk_wheel: python.exe setup.py bdist_wheel --universal
% endif
    ${module_name}-system_tests: python --version
    ${module_name}-system_tests: python -m pip install --disable-pip-version-check --upgrade pip
% if config['supports_nitclk']:
    ${module_name}-system_tests: python ../../tools/install_local_wheel.py --driver nitclk --start-path ../..
% endif
    ${module_name}-system_tests: python -c "import platform; print(platform.architecture())"
    ${module_name}-system_tests: python -c "import ${module_name}; ${module_name}.print_diagnostic_information()"
    ${module_name}-system_tests: coverage run --rcfile=../../tools/coverage_system_tests.rc --source ${module_name} --parallel-mode -m py.test ../../src/${module_name}/examples --junitxml=../../junit/junit-${module_name}-{envname}-{env:BITNESS:64}.xml {posargs}
    ${module_name}-system_tests: coverage run --rcfile=../../tools/coverage_system_tests.rc --source ${module_name} --parallel-mode -m py.test ../../src/${module_name}/system_tests --junitxml=../../junit/junit-${module_name}-{envname}-{env:BITNESS:64}.xml {posargs}
    ${module_name}-coverage: coverage combine --rcfile=../../tools/coverage_system_tests.rc ./
    # Create the report to upload
    ${module_name}-coverage: coverage xml -i --rcfile=../../tools/coverage_system_tests.rc
    # Display the coverage results
    ${module_name}-coverage: coverage report --rcfile=../../tools/coverage_system_tests.rc
    # token is from codecov
    ${module_name}-coverage: codecov -X gcov --token=4c58f03d-b74c-489a-889a-ab0a77b7809f --no-color --flags ${module_name}systemtests --name ${module_name} --root ../.. --file ../../generated/${module_name}/coverage.xml

deps =
% if config['supports_nitclk']:
    ${module_name}-nitclk_wheel: packaging
% endif
    ${module_name}-system_tests: pytest==4.6.5;platform_python_implementation=='PyPy'
    ${module_name}-system_tests: pytest;platform_python_implementation=='CPython'
    ${module_name}-system_tests: coverage
    ${module_name}-system_tests: numpy
    ${module_name}-system_tests: scipy
    ${module_name}-system_tests: fasteners
% if module_name != 'nimodinst':
    # Only add this dependency if we are not testing nimodinst
    ${module_name}-system_tests: nimodinst
% endif
    ${module_name}-coverage: coverage
    ${module_name}-coverage: codecov

depends =
    ${module_name}-coverage: py{35,36,37,38,py3}-${module_name}-system_tests
% if config['supports_nitclk']:
    ${module_name}-system_tests: ${nitclk_env}
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

