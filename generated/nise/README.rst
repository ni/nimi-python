Overall Status
--------------

+----------------------+------------------------------------------------------------------------------------------------------------------------------------+
| master branch status | |BuildStatus| |MITLicense| |CoverageStatus|                                                                                        |
+----------------------+------------------------------------------------------------------------------------------------------------------------------------+
| GitHub status        | |OpenIssues| |OpenPullRequests|                                                                                                    |
+----------------------+------------------------------------------------------------------------------------------------------------------------------------+

===========  ============================================================================================================================
Info         NI Modular Instrument driver APIs for Python.
Author       NI
===========  ============================================================================================================================

.. |BuildStatus| image:: https://api.travis-ci.com/ni/nimi-python.svg
    :alt: Build Status - master branch
    :target: https://travis-ci.org/ni/nimi-python

.. |MITLicense| image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :alt: MIT License
    :target: https://opensource.org/licenses/MIT

.. |CoverageStatus| image:: https://codecov.io/github/ni/nimi-python/graph/badge.svg
    :alt: Test Coverage - master branch
    :target: https://codecov.io/github/ni/nimi-python

.. |OpenIssues| image:: https://img.shields.io/github/issues/ni/nimi-python.svg
    :alt: Open Issues + Pull Requests
    :target: https://github.com/ni/nimi-python/issues

.. |OpenPullRequests| image:: https://img.shields.io/github/issues-pr/ni/nimi-python.svg
    :alt: Open Pull Requests
    :target: https://github.com/ni/nimi-python/pulls


.. _about-section:

About
=====

The **nise** module provides a Python API for NI Switch Executive. The code is maintained in the Open Source repository for `nimi-python <https://github.com/ni/nimi-python>`_.

Support Policy
--------------
**nise** supports all the Operating Systems supported by NI Switch Executive.

It follows `Python Software Foundation <https://devguide.python.org/#status-of-python-branches>`_ support policy for different versions of CPython.

NI created and supports **nise**.


NI Switch Executive Python API Status
-------------------------------------

+-------------------------------+---------------------+
| NI Switch Executive (nise)    |                     |
+===============================+=====================+
| Driver Version Tested Against | 2023 Q1             |
+-------------------------------+---------------------+
| PyPI Version                  | |niseLatestVersion| |
+-------------------------------+---------------------+
| Supported Python Version      | |nisePythonVersion| |
+-------------------------------+---------------------+
| Documentation                 | |niseDocs|          |
+-------------------------------+---------------------+
| Open Issues                   | |niseOpenIssues|    |
+-------------------------------+---------------------+
| Open Pull Requests            | |niseOpenPRs|       |
+-------------------------------+---------------------+


.. |niseLatestVersion| image:: http://img.shields.io/pypi/v/nise.svg
    :alt: Latest NI Switch Executive Version
    :target: http://pypi.python.org/pypi/nise


.. |nisePythonVersion| image:: http://img.shields.io/pypi/pyversions/nise.svg
    :alt: NI Switch Executive supported Python versions
    :target: http://pypi.python.org/pypi/nise


.. |niseDocs| image:: https://readthedocs.org/projects/nise/badge/?version=latest
    :alt: NI Switch Executive Python API Documentation Status
    :target: https://nise.readthedocs.io/en/latest


.. |niseOpenIssues| image:: https://img.shields.io/github/issues/ni/nimi-python/nise.svg
    :alt: Open Issues + Pull Requests for NI Switch Executive
    :target: https://github.com/ni/nimi-python/issues?q=is%3Aopen+is%3Aissue+label%3Anise


.. |niseOpenPRs| image:: https://img.shields.io/github/issues-pr/ni/nimi-python/nise.svg
    :alt: Pull Requests for NI Switch Executive
    :target: https://github.com/ni/nimi-python/pulls?q=is%3Aopen+is%3Aissue+label%3Anise



.. _nise_installation-section:

Installation
------------

As a prerequisite to using the **nise** module, you must install the NI Switch Executive runtime on your system. Visit `ni.com/downloads <http://www.ni.com/downloads/>`_ to download the driver runtime for your devices.

The nimi-python modules (i.e. for **NI Switch Executive**) can be installed with `pip <http://pypi.python.org/pypi/pip>`_::

  $ python -m pip install nise


Contributing
============

We welcome contributions! You can clone the project repository, build it, and install it by `following these instructions <https://github.com/ni/nimi-python/blob/master/CONTRIBUTING.md>`_.

Usage
------

The following is a basic example of using the **nise** module to open a session to a Switch Executive Virtual Device and connect a routegroup.

.. code-block:: python

    import nise
    with nise.Session('SwitchExecutiveExample') as session:
        session.connect('DIOToUUT')

`Other usage examples can be found on GitHub. <https://github.com/ni/nimi-python/tree/master/src/nise/examples>`_

.. _support-section:

Support / Feedback
==================

For support specific to the Python API, follow the processs in `Bugs / Feature Requests`_.
For support with hardware, the driver runtime or any other questions not specific to the Python API, please visit `NI Community Forums <https://forums.ni.com/>`_.

.. _bugs-section:

Bugs / Feature Requests
=======================

To report a bug or submit a feature request specific to Python API, please use the
`GitHub issues page <https://github.com/ni/nimi-python/issues>`_.

Fill in the issue template as completely as possible and we will respond as soon
as we can.


.. _documentation-section:

Documentation
=============

Documentation is available `here <http://nise.readthedocs.io>`_.


.. _license-section:

License
=======

**nimi-python** is licensed under an MIT-style license (`see
LICENSE <https://github.com/ni/nimi-python/blob/master/LICENSE>`_).
Other incorporated projects may be licensed under different licenses. All
licenses allow for non-commercial and commercial use.


**gRPC Features**

For driver APIs that support it, passing a GrpcSessionOptions instance as a parameter to Session.__init__() is
subject to the NI General Purpose EULA (`see NILICENSE <https://github.com/ni/nimi-python/blob/master/NILICENSE>`_).