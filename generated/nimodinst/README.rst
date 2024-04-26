Overall Status
--------------

+----------------------+------------------------------------------------------------------------------------------------------------------------------------+
| master branch status | |BuildStatus| |MITLicense| |CoverageStatus|                                                                                        |
+----------------------+------------------------------------------------------------------------------------------------------------------------------------+
| GitHub status        | |OpenIssues| |OpenPullRequests|                                                                                                    |
+----------------------+------------------------------------------------------------------------------------------------------------------------------------+

===========  ============================================================================================================================
Info         Python bindings for NI Modular Instrument drivers. See `GitHub <https://github.com/ni/nimi-python/>`_ for the latest source.
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

The **nimodinst** module provides a Python API for NI-ModInst. The code is maintained in the Open Source repository for `nimi-python <https://github.com/ni/nimi-python>`_.

Support Policy
--------------
**nimodinst** supports all the Operating Systems supported by NI-ModInst.

It follows `Python Software Foundation <https://devguide.python.org/#status-of-python-branches>`_ support policy for different versions of CPython.


NI-ModInst Python API Status
----------------------------

+-------------------------------+--------------------------+
| NI-ModInst (nimodinst)        |                          |
+===============================+==========================+
| Driver Version Tested Against | 2024 Q2                  |
+-------------------------------+--------------------------+
| PyPI Version                  | |nimodinstLatestVersion| |
+-------------------------------+--------------------------+
| Supported Python Version      | |nimodinstPythonVersion| |
+-------------------------------+--------------------------+
| Documentation                 | |nimodinstDocs|          |
+-------------------------------+--------------------------+
| Open Issues                   | |nimodinstOpenIssues|    |
+-------------------------------+--------------------------+
| Open Pull Requests            | |nimodinstOpenPRs|       |
+-------------------------------+--------------------------+


.. |nimodinstLatestVersion| image:: http://img.shields.io/pypi/v/nimodinst.svg
    :alt: Latest NI-ModInst Version
    :target: http://pypi.python.org/pypi/nimodinst


.. |nimodinstPythonVersion| image:: http://img.shields.io/pypi/pyversions/nimodinst.svg
    :alt: NI-ModInst supported Python versions
    :target: http://pypi.python.org/pypi/nimodinst


.. |nimodinstDocs| image:: https://readthedocs.org/projects/nimodinst/badge/?version=latest
    :alt: NI-ModInst Python API Documentation Status
    :target: https://nimodinst.readthedocs.io/en/latest


.. |nimodinstOpenIssues| image:: https://img.shields.io/github/issues/ni/nimi-python/nimodinst.svg
    :alt: Open Issues + Pull Requests for NI-ModInst
    :target: https://github.com/ni/nimi-python/issues?q=is%3Aopen+is%3Aissue+label%3Animodinst


.. |nimodinstOpenPRs| image:: https://img.shields.io/github/issues-pr/ni/nimi-python/nimodinst.svg
    :alt: Pull Requests for NI-ModInst
    :target: https://github.com/ni/nimi-python/pulls?q=is%3Aopen+is%3Aissue+label%3Animodinst



.. _nimodinst_installation-section:

Installation
------------

As a prerequisite to using the **nimodinst** module, you must install the NI-ModInst runtime on your system. Visit `ni.com/downloads <http://www.ni.com/downloads/>`_ to download the driver runtime for your devices.

The nimi-python modules (i.e. for **NI-ModInst**) can be installed with `pip <http://pypi.python.org/pypi/pip>`_::

  $ python -m pip install nimodinst~=1.4.8


Contributing
============

We welcome contributions! You can clone the project repository, build it, and install it by `following these instructions <https://github.com/ni/nimi-python/blob/master/CONTRIBUTING.md>`_.

Usage
------

The following is a basic example of using the **nimodinst** module to retrieve information on all High Speed Digitizers currently in the system.

.. code-block:: python

    import nimodinst
    with nimodinst.Session("niscope") as session:
        for device in session:
            print("{: >20} {: >15} {: >10}".format(device.device_name, device.device_model, device.serial_number))

`Other usage examples can be found on GitHub. <https://github.com/ni/nimi-python/tree/master/src/nimodinst/examples>`_

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

Documentation is available `here <http://nimodinst.readthedocs.io>`_.


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