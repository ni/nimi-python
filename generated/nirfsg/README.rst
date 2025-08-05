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

The **nirfsg** module provides a Python API for NI-RFSG. The code is maintained in the Open Source repository for `nimi-python <https://github.com/ni/nimi-python>`_.

Support Policy
--------------
**nirfsg** supports all the Operating Systems supported by NI-RFSG.

It follows `Python Software Foundation <https://devguide.python.org/#status-of-python-branches>`_ support policy for different versions of CPython.

NI created and supports **nirfsg**.


NI-RFSG Python API Status
-------------------------

+-------------------------------+-----------------------+
| NI-RFSG (nirfsg)              |                       |
+===============================+=======================+
| Driver Version Tested Against | 2025 Q2               |
+-------------------------------+-----------------------+
| PyPI Version                  | |nirfsgLatestVersion| |
+-------------------------------+-----------------------+
| Supported Python Version      | |nirfsgPythonVersion| |
+-------------------------------+-----------------------+
| Documentation                 | |nirfsgDocs|          |
+-------------------------------+-----------------------+
| Open Issues                   | |nirfsgOpenIssues|    |
+-------------------------------+-----------------------+
| Open Pull Requests            | |nirfsgOpenPRs|       |
+-------------------------------+-----------------------+


.. |nirfsgLatestVersion| image:: http://img.shields.io/pypi/v/nirfsg.svg
    :alt: Latest NI-RFSG Version
    :target: http://pypi.python.org/pypi/nirfsg


.. |nirfsgPythonVersion| image:: http://img.shields.io/pypi/pyversions/nirfsg.svg
    :alt: NI-RFSG supported Python versions
    :target: http://pypi.python.org/pypi/nirfsg


.. |nirfsgDocs| image:: https://readthedocs.org/projects/nirfsg/badge/?version=latest
    :alt: NI-RFSG Python API Documentation Status
    :target: https://nirfsg.readthedocs.io/en/latest


.. |nirfsgOpenIssues| image:: https://img.shields.io/github/issues/ni/nimi-python/nirfsg.svg
    :alt: Open Issues + Pull Requests for NI-RFSG
    :target: https://github.com/ni/nimi-python/issues?q=is%3Aopen+is%3Aissue+label%3Anirfsg


.. |nirfsgOpenPRs| image:: https://img.shields.io/github/issues-pr/ni/nimi-python/nirfsg.svg
    :alt: Pull Requests for NI-RFSG
    :target: https://github.com/ni/nimi-python/pulls?q=is%3Aopen+is%3Aissue+label%3Anirfsg



.. _nirfsg_installation-section:

Installation
------------

As a prerequisite to using the **nirfsg** module, you must install the NI-RFSG runtime on your system. Visit `ni.com/downloads <http://www.ni.com/downloads/>`_ to download the driver runtime for your devices.

The nimi-python modules (i.e. for **NI-RFSG**) can be installed with `pip <http://pypi.python.org/pypi/pip>`_::

  $ python -m pip install nirfsg~=1.0.0


Contributing
============

We welcome contributions! You can clone the project repository, build it, and install it by `following these instructions <https://github.com/ni/nimi-python/blob/master/CONTRIBUTING.md>`_.

Usage
------

The following is a basic example of using the **nirfsg** module to open a session to an RF Signal Generator and generate a continuous wave (CW) signal.

.. code-block:: python

    import nirfsg

    # Configure the session
    with nirfsg.Session(resource_name='5841', id_query=False, reset_device=False, options='Simulate=1, DriverSetup=Model:5841') as session:
        # Configure RF settings
        session.configure_rf(
            frequency=1e9,  # Frequency in Hz
            power_level=-10.0  # Power level in dBm
        )
        session.generation_mode = nirfsg.GenerationMode.CW

        # Start signal generation
        with session.initiate():
            input("Press Enter to stop generation")

`Other usage examples can be found on GitHub. <https://github.com/ni/nimi-python/tree/master/src/nirfsg/examples>`_.. _support-section:

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

Documentation is available `here <http://nirfsg.readthedocs.io>`_.


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