<%
    import build.helper as helper

    config = template_parameters['metadata'].config
    module_name = config['module_name']
%>\
# Tox (http://tox.testrun.org/) is a tool for running tests
# in multiple virtualenvs. This configuration file will run the
# test suite on all supported python versions. To use it, "pip install tox"
# and then run "tox" from this directory.
[tox]
envlist = py{35,36,37,38,py3}-${module_name}-system_tests
skip_missing_interpreters=True
ignore_basepython_conflict=True
# We put the .tox directory outside of the workspace so that it isn't wiped with the rest of the repo
toxworkdir = ../.tox

[testenv]
description =
    ${module_name}-system_tests: Run ${module_name} system tests (requires driver runtime to be installed)

changedir =
    ${module_name}-system_tests: .

commands =
    ${module_name}-system_tests: python --version
    ${module_name}-system_tests: python -c "import platform; print(platform.architecture())"
    ${module_name}-system_tests: python -c "import ${module_name}; nidcpower.print_diagnostic_information()"
    ${module_name}-system_tests: coverage run --rcfile=tools/coverage_system_tests.rc --source ${module_name} -m py.test src/${module_name}/examples --junitxml=generated/junit/junit-${module_name}-{envname}-{env:BITNESS:64}.xml {posargs}
    ${module_name}-system_tests: coverage run --rcfile=tools/coverage_system_tests.rc --source ${module_name} -m py.test src/${module_name}/system_tests --junitxml=generated/junit/junit-${module_name}-{envname}-{env:BITNESS:64}.xml {posargs}
    ${module_name}-system_tests: coverage report --rcfile=tools/coverage_system_tests.rc
    ${module_name}-system_tests: coverage html --rcfile=tools/coverage_system_tests.rc --directory=generated/htmlcov/system_tests

deps =
    ${module_name}-system_tests: pytest==4.6.5;platform_python_implementation=='PyPy'
    ${module_name}-system_tests: pytest;platform_python_implementation=='CPython'
    ${module_name}-system_tests: coverage
    ${module_name}-system_tests: numpy
    ${module_name}-system_tests: scipy


