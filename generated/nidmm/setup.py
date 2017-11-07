#!/usr/bin/python
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


pypi_name = 'nidmm'


def read_contents(file_to_read):
    with open(file_to_read, 'r') as f:
        return f.read()


setup(
    name=pypi_name,
    zip_safe=True,
    version='0.4.0',
    description='NI-DMM Python API',
    long_description=read_contents('README.rst'),
    author='National Instruments',
    author_email="opensource@ni.com",
    url="https://github.com/ni/nimi-python",
    maintainer="National Instruments",
    maintainer_email="opensource@ni.com",
    keywords=['nidmm'],
    license='MIT',
    include_package_data=True,
    packages=['nidmm'],
    install_requires=[
        'enum34;python_version<"3.4"',
    ],
    setup_requires=['pytest-runner', ],
    tests_require=['pytest'],
    test_suite='tests',
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
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
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: System :: Hardware :: Hardware Drivers"
    ],
    cmdclass={'test': PyTest},
    package_data={pypi_name: ['VERSION']},
)
