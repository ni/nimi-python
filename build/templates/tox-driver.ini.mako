<%
    import build.helper as helper

    config = template_parameters['metadata'].config
    module_name = config['module_name']
    if config['supports_nitclk']:
        nitclk_env = 'py38-{}-nitclk_wheel,'.format(module_name)
    else:
        nitclk_env = ''
%>\
# Tox (http://tox.testrun.org/) is a tool for running tests
# in multiple virtualenvs. This configuration file will run the
# test suite on all supported python versions. To use it, "pip install tox"
# and then run "tox" from this directory.
[tox]
envlist = ${nitclk_env}py{35,36,37,38,py3}-${module_name}-system_tests
skip_missing_interpreters=True
ignore_basepython_conflict=True
# We put the .tox directory outside of the workspace so that it isn't wiped with the rest of the repo
toxworkdir = ../../../.tox

[testenv]
description =
% if config['supports_nitclk']:
    ${module_name}-nitclk_wheel: Build the nitclk wheel
% endif
    ${module_name}-system_tests: Run ${module_name} system tests (requires driver runtime to be installed)

changedir =
% if config['supports_nitclk']:
    ${module_name}-nitclk_wheel: ../../generated/nitclk
% endif
    ${module_name}-system_tests: .

commands =
% if config['supports_nitclk']:
    ${module_name}-nitclk_wheel: python.exe setup.py bdist_wheel --universal
% endif
    ${module_name}-system_tests: python --version
    ${module_name}-system_tests: python -c "import platform; print(platform.architecture())"
    ${module_name}-system_tests: python -c "import ${module_name}; ${module_name}.print_diagnostic_information()"
% if config['supports_nitclk']:
    ${module_name}-system_tests: python ../../tools/install_local_wheel.py --driver nitclk --start-path ../..
% endif
    ${module_name}-system_tests: coverage run --rcfile=../../tools/coverage_system_tests.rc --source ${module_name} -m py.test ../../src/${module_name}/examples --junitxml=../../generated/junit/junit-${module_name}-{envname}-{env:BITNESS:64}.xml {posargs}
    ${module_name}-system_tests: coverage run --rcfile=../../tools/coverage_system_tests.rc --source ${module_name} -m py.test ../../src/${module_name}/system_tests --junitxml=../../generated/junit/junit-${module_name}-{envname}-{env:BITNESS:64}.xml {posargs}
    ${module_name}-system_tests: coverage report --rcfile=../../tools/coverage_system_tests.rc
    ${module_name}-system_tests: coverage html --rcfile=../../tools/coverage_system_tests.rc --directory=../../generated/htmlcov/system_tests

deps =
% if config['supports_nitclk']:
    ${module_name}-nitclk_wheel: packaging
% endif
    ${module_name}-system_tests: pytest==4.6.5;platform_python_implementation=='PyPy'
    ${module_name}-system_tests: pytest;platform_python_implementation=='CPython'
    ${module_name}-system_tests: coverage
    ${module_name}-system_tests: numpy
    ${module_name}-system_tests: scipy


