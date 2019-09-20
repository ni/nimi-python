#!/usr/bin/python
# -*- coding: utf-8 -*-
# This file was generated
<%
config         = template_parameters['metadata'].config
module_version = config['module_version']

from packaging.version import Version
v = Version(module_version)  
# module_version must be PEP 440 conformant
# See https://packaging.pypa.io/en/latest/version/ and https://www.python.org/dev/peps/pep-0440/
# Arbitrary rules:
# version < 0.5 - alpha
# version >= 0.5 && version < 1.0 - beta
# version >= 1.0
#    .devN or .aN - Alpha
#    .bN, cN, rcN - Beta
#    <nothing> or postN - Stable
if v.release[0] == 0 and v.release[1] < 5:
    dev_status = '3 - Alpha'
elif v.release[0] == 0:
    dev_status = '4 - Beta'
else:
    if v.dev is not None or (v.pre is not None and v.pre[0] == 'a'):
        # .devN or .aN
        dev_status = '3 - Alpha'
    elif v.pre is not None:
        # .bN, .cN, .rcN
        dev_status = '4 - Beta'
    else:
        # <nothing> or .postN
        dev_status = '5 - Production/Stable'
%>

from setuptools.command.test import test as test_command
from setuptools import setup


class PyTest(test_command):
    def finalize_options(self):
        test_command.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        pytest.main(self.test_args)


pypi_name = '${config['module_name']}'


def read_contents(file_to_read):
    with open(file_to_read, 'r') as f:
        return f.read()


setup(
    name=pypi_name,
    zip_safe=True,
    version='${config['module_version']}',
    description='${config['driver_name']} Python API',
    long_description=read_contents('README.rst'),
    long_description_content_type='text/x-rst',
    author='National Instruments',
    author_email="opensource@ni.com",
    url="https://github.com/ni/nimi-python",
    maintainer="National Instruments",
    maintainer_email="opensource@ni.com",
    keywords=['${config['module_name']}'],
    license='MIT',
    include_package_data=True,
    packages=['${config['module_name']}'],
    install_requires=[
        'enum34;python_version<"3.4"',
        'singledispatch;python_version<"3.4"',
        'six',
    ],
    setup_requires=['pytest-runner', ],
    tests_require=['pytest'],
    test_suite='tests',
    classifiers=[
        "Development Status :: ${dev_status}",
        "Intended Audience :: Developers",
        "Intended Audience :: Manufacturing",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: System :: Hardware :: Hardware Drivers"
    ],
    cmdclass={'test': PyTest},
    package_data={pypi_name: ['VERSION']},
)
