#!/usr/bin/python
# This file was generated
<%
import build.helper as helper

config         = template_parameters['metadata'].config
grpc_supported = template_parameters['include_grpc_support']
module_version = config['module_version']
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
    author='NI',
    author_email="opensource@ni.com",
    url="https://github.com/ni/nimi-python",
    maintainer="NI",
    maintainer_email="opensource@ni.com",
    keywords=['${config['module_name']}'],
    license='MIT',
    include_package_data=True,
    packages=['${config['module_name']}'],
    install_requires=[
        'hightime>=0.2.0',
        % if config['uses_nitclk']:
        'nitclk',
        % endif
    ],
    % if grpc_supported:
    extras_require={
        'grpc': [
            'grpcio>=1.59.0,<2.0',
            'protobuf>=4.21.6,<5.0'
        ],
    },
    % endif
    setup_requires=['pytest-runner', ],
    tests_require=['pytest'],
    test_suite='tests',
    classifiers=[
        "Development Status :: ${helper.get_development_status(config)}",
        "Intended Audience :: Developers",
        "Intended Audience :: Manufacturing",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: System :: Hardware :: Hardware Drivers"
    ],
    cmdclass={'test': PyTest},
    package_data={pypi_name: ['VERSION']},
)
