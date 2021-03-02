#!/usr/bin/python
# -*- coding: utf-8 -*-
# This file was generated


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


pypi_name = 'nifgen'


def read_contents(file_to_read):
    with open(file_to_read, 'r') as f:
        return f.read()


setup(
    name=pypi_name,
    zip_safe=True,
    version='1.3.3',
    description='NI-FGEN Python API',
    long_description=read_contents('README.rst'),
    long_description_content_type='text/x-rst',
    author='National Instruments',
    author_email="opensource@ni.com",
    url="https://github.com/ni/nimi-python",
    maintainer="National Instruments",
    maintainer_email="opensource@ni.com",
    keywords=['nifgen'],
    license='MIT',
    include_package_data=True,
    packages=['nifgen'],
    install_requires=[
        'enum34;python_version<"3.4"',
        'singledispatch;python_version<"3.4"',
        'hightime>=0.2.0',
        'nitclk',
    ],
    setup_requires=['pytest-runner', ],
    tests_require=['pytest'],
    test_suite='tests',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Manufacturing",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: System :: Hardware :: Hardware Drivers"
    ],
    cmdclass={'test': PyTest},
    package_data={pypi_name: ['VERSION']},
)
