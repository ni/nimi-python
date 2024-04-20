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

The **nimi-python** repository generates Python bindings (Application Programming Interface) for interacting with the Modular Instrument drivers. The
following drivers are supported:

* NI-DCPower (Python module: nidcpower)
* NI-Digital Pattern Driver (Python module: nidigital)
* NI-DMM (Python module: nidmm)
* NI-FGEN (Python module: nifgen)
* NI-ModInst (Python module: nimodinst)
* NI-SCOPE (Python module: niscope)
* NI Switch Executive (Python module: nise)
* NI-SWITCH (Python module: niswitch)
* NI-TClk (Python module: nitclk)

It is implemented as a set of `Mako templates <http://makotemplates.org>`_ and per-driver metafiles that produce a Python module for each driver. The driver is
called through its public C API using the `ctypes <https://docs.python.org/2/library/ctypes.html>`_ Python library.

**nimi-python** supports all the Operating Systems supported by the underlying driver.

**nimi-python** follows `Python Software Foundation <https://devguide.python.org/#status-of-python-branches>`_ support policy for different versions.


NI-DCPower Python API Status
----------------------------

+-------------------------------+--------------------------+
| NI-DCPower (nidcpower)        |                          |
+===============================+==========================+
| Driver Version Tested Against | 2024 Q2                  |
+-------------------------------+--------------------------+
| PyPI Version                  | |nidcpowerLatestVersion| |
+-------------------------------+--------------------------+
| Supported Python Version      | |nidcpowerPythonVersion| |
+-------------------------------+--------------------------+
| Documentation                 | |nidcpowerDocs|          |
+-------------------------------+--------------------------+
| Open Issues                   | |nidcpowerOpenIssues|    |
+-------------------------------+--------------------------+
| Open Pull Requests            | |nidcpowerOpenPRs|       |
+-------------------------------+--------------------------+


.. |nidcpowerLatestVersion| image:: http://img.shields.io/pypi/v/nidcpower.svg
    :alt: Latest NI-DCPower Version
    :target: http://pypi.python.org/pypi/nidcpower


.. |nidcpowerPythonVersion| image:: http://img.shields.io/pypi/pyversions/nidcpower.svg
    :alt: NI-DCPower supported Python versions
    :target: http://pypi.python.org/pypi/nidcpower


.. |nidcpowerDocs| image:: https://readthedocs.org/projects/nidcpower/badge/?version=latest
    :alt: NI-DCPower Python API Documentation Status
    :target: https://nidcpower.readthedocs.io/en/latest


.. |nidcpowerOpenIssues| image:: https://img.shields.io/github/issues/ni/nimi-python/nidcpower.svg
    :alt: Open Issues + Pull Requests for NI-DCPower
    :target: https://github.com/ni/nimi-python/issues?q=is%3Aopen+is%3Aissue+label%3Anidcpower


.. |nidcpowerOpenPRs| image:: https://img.shields.io/github/issues-pr/ni/nimi-python/nidcpower.svg
    :alt: Pull Requests for NI-DCPower
    :target: https://github.com/ni/nimi-python/pulls?q=is%3Aopen+is%3Aissue+label%3Anidcpower



NI-Digital Pattern Driver Python API Status
-------------------------------------------

+---------------------------------------+--------------------------+
| NI-Digital Pattern Driver (nidigital) |                          |
+=======================================+==========================+
| Driver Version Tested Against         | 2024 Q2                  |
+---------------------------------------+--------------------------+
| PyPI Version                          | |nidigitalLatestVersion| |
+---------------------------------------+--------------------------+
| Supported Python Version              | |nidigitalPythonVersion| |
+---------------------------------------+--------------------------+
| Documentation                         | |nidigitalDocs|          |
+---------------------------------------+--------------------------+
| Open Issues                           | |nidigitalOpenIssues|    |
+---------------------------------------+--------------------------+
| Open Pull Requests                    | |nidigitalOpenPRs|       |
+---------------------------------------+--------------------------+


.. |nidigitalLatestVersion| image:: http://img.shields.io/pypi/v/nidigital.svg
    :alt: Latest NI-Digital Pattern Driver Version
    :target: http://pypi.python.org/pypi/nidigital


.. |nidigitalPythonVersion| image:: http://img.shields.io/pypi/pyversions/nidigital.svg
    :alt: NI-Digital Pattern Driver supported Python versions
    :target: http://pypi.python.org/pypi/nidigital


.. |nidigitalDocs| image:: https://readthedocs.org/projects/nidigital/badge/?version=latest
    :alt: NI-Digital Pattern Driver Python API Documentation Status
    :target: https://nidigital.readthedocs.io/en/latest


.. |nidigitalOpenIssues| image:: https://img.shields.io/github/issues/ni/nimi-python/nidigital.svg
    :alt: Open Issues + Pull Requests for NI-Digital Pattern Driver
    :target: https://github.com/ni/nimi-python/issues?q=is%3Aopen+is%3Aissue+label%3Anidigital


.. |nidigitalOpenPRs| image:: https://img.shields.io/github/issues-pr/ni/nimi-python/nidigital.svg
    :alt: Pull Requests for NI-Digital Pattern Driver
    :target: https://github.com/ni/nimi-python/pulls?q=is%3Aopen+is%3Aissue+label%3Anidigital



NI-DMM Python API Status
------------------------

+-------------------------------+----------------------+
| NI-DMM (nidmm)                |                      |
+===============================+======================+
| Driver Version Tested Against | 2023 Q4              |
+-------------------------------+----------------------+
| PyPI Version                  | |nidmmLatestVersion| |
+-------------------------------+----------------------+
| Supported Python Version      | |nidmmPythonVersion| |
+-------------------------------+----------------------+
| Documentation                 | |nidmmDocs|          |
+-------------------------------+----------------------+
| Open Issues                   | |nidmmOpenIssues|    |
+-------------------------------+----------------------+
| Open Pull Requests            | |nidmmOpenPRs|       |
+-------------------------------+----------------------+


.. |nidmmLatestVersion| image:: http://img.shields.io/pypi/v/nidmm.svg
    :alt: Latest NI-DMM Version
    :target: http://pypi.python.org/pypi/nidmm


.. |nidmmPythonVersion| image:: http://img.shields.io/pypi/pyversions/nidmm.svg
    :alt: NI-DMM supported Python versions
    :target: http://pypi.python.org/pypi/nidmm


.. |nidmmDocs| image:: https://readthedocs.org/projects/nidmm/badge/?version=latest
    :alt: NI-DMM Python API Documentation Status
    :target: https://nidmm.readthedocs.io/en/latest


.. |nidmmOpenIssues| image:: https://img.shields.io/github/issues/ni/nimi-python/nidmm.svg
    :alt: Open Issues + Pull Requests for NI-DMM
    :target: https://github.com/ni/nimi-python/issues?q=is%3Aopen+is%3Aissue+label%3Anidmm


.. |nidmmOpenPRs| image:: https://img.shields.io/github/issues-pr/ni/nimi-python/nidmm.svg
    :alt: Pull Requests for NI-DMM
    :target: https://github.com/ni/nimi-python/pulls?q=is%3Aopen+is%3Aissue+label%3Anidmm



NI-FGEN Python API Status
-------------------------

+-------------------------------+-----------------------+
| NI-FGEN (nifgen)              |                       |
+===============================+=======================+
| Driver Version Tested Against | 2023 Q4               |
+-------------------------------+-----------------------+
| PyPI Version                  | |nifgenLatestVersion| |
+-------------------------------+-----------------------+
| Supported Python Version      | |nifgenPythonVersion| |
+-------------------------------+-----------------------+
| Documentation                 | |nifgenDocs|          |
+-------------------------------+-----------------------+
| Open Issues                   | |nifgenOpenIssues|    |
+-------------------------------+-----------------------+
| Open Pull Requests            | |nifgenOpenPRs|       |
+-------------------------------+-----------------------+


.. |nifgenLatestVersion| image:: http://img.shields.io/pypi/v/nifgen.svg
    :alt: Latest NI-FGEN Version
    :target: http://pypi.python.org/pypi/nifgen


.. |nifgenPythonVersion| image:: http://img.shields.io/pypi/pyversions/nifgen.svg
    :alt: NI-FGEN supported Python versions
    :target: http://pypi.python.org/pypi/nifgen


.. |nifgenDocs| image:: https://readthedocs.org/projects/nifgen/badge/?version=latest
    :alt: NI-FGEN Python API Documentation Status
    :target: https://nifgen.readthedocs.io/en/latest


.. |nifgenOpenIssues| image:: https://img.shields.io/github/issues/ni/nimi-python/nifgen.svg
    :alt: Open Issues + Pull Requests for NI-FGEN
    :target: https://github.com/ni/nimi-python/issues?q=is%3Aopen+is%3Aissue+label%3Anifgen


.. |nifgenOpenPRs| image:: https://img.shields.io/github/issues-pr/ni/nimi-python/nifgen.svg
    :alt: Pull Requests for NI-FGEN
    :target: https://github.com/ni/nimi-python/pulls?q=is%3Aopen+is%3Aissue+label%3Anifgen



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



NI-SCOPE Python API Status
--------------------------

+-------------------------------+------------------------+
| NI-SCOPE (niscope)            |                        |
+===============================+========================+
| Driver Version Tested Against | 2023 Q4                |
+-------------------------------+------------------------+
| PyPI Version                  | |niscopeLatestVersion| |
+-------------------------------+------------------------+
| Supported Python Version      | |niscopePythonVersion| |
+-------------------------------+------------------------+
| Documentation                 | |niscopeDocs|          |
+-------------------------------+------------------------+
| Open Issues                   | |niscopeOpenIssues|    |
+-------------------------------+------------------------+
| Open Pull Requests            | |niscopeOpenPRs|       |
+-------------------------------+------------------------+


.. |niscopeLatestVersion| image:: http://img.shields.io/pypi/v/niscope.svg
    :alt: Latest NI-SCOPE Version
    :target: http://pypi.python.org/pypi/niscope


.. |niscopePythonVersion| image:: http://img.shields.io/pypi/pyversions/niscope.svg
    :alt: NI-SCOPE supported Python versions
    :target: http://pypi.python.org/pypi/niscope


.. |niscopeDocs| image:: https://readthedocs.org/projects/niscope/badge/?version=latest
    :alt: NI-SCOPE Python API Documentation Status
    :target: https://niscope.readthedocs.io/en/latest


.. |niscopeOpenIssues| image:: https://img.shields.io/github/issues/ni/nimi-python/niscope.svg
    :alt: Open Issues + Pull Requests for NI-SCOPE
    :target: https://github.com/ni/nimi-python/issues?q=is%3Aopen+is%3Aissue+label%3Aniscope


.. |niscopeOpenPRs| image:: https://img.shields.io/github/issues-pr/ni/nimi-python/niscope.svg
    :alt: Pull Requests for NI-SCOPE
    :target: https://github.com/ni/nimi-python/pulls?q=is%3Aopen+is%3Aissue+label%3Aniscope



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



NI-SWITCH Python API Status
---------------------------

+-------------------------------+-------------------------+
| NI-SWITCH (niswitch)          |                         |
+===============================+=========================+
| Driver Version Tested Against | 2023 Q4                 |
+-------------------------------+-------------------------+
| PyPI Version                  | |niswitchLatestVersion| |
+-------------------------------+-------------------------+
| Supported Python Version      | |niswitchPythonVersion| |
+-------------------------------+-------------------------+
| Documentation                 | |niswitchDocs|          |
+-------------------------------+-------------------------+
| Open Issues                   | |niswitchOpenIssues|    |
+-------------------------------+-------------------------+
| Open Pull Requests            | |niswitchOpenPRs|       |
+-------------------------------+-------------------------+


.. |niswitchLatestVersion| image:: http://img.shields.io/pypi/v/niswitch.svg
    :alt: Latest NI-SWITCH Version
    :target: http://pypi.python.org/pypi/niswitch


.. |niswitchPythonVersion| image:: http://img.shields.io/pypi/pyversions/niswitch.svg
    :alt: NI-SWITCH supported Python versions
    :target: http://pypi.python.org/pypi/niswitch


.. |niswitchDocs| image:: https://readthedocs.org/projects/niswitch/badge/?version=latest
    :alt: NI-SWITCH Python API Documentation Status
    :target: https://niswitch.readthedocs.io/en/latest


.. |niswitchOpenIssues| image:: https://img.shields.io/github/issues/ni/nimi-python/niswitch.svg
    :alt: Open Issues + Pull Requests for NI-SWITCH
    :target: https://github.com/ni/nimi-python/issues?q=is%3Aopen+is%3Aissue+label%3Aniswitch


.. |niswitchOpenPRs| image:: https://img.shields.io/github/issues-pr/ni/nimi-python/niswitch.svg
    :alt: Pull Requests for NI-SWITCH
    :target: https://github.com/ni/nimi-python/pulls?q=is%3Aopen+is%3Aissue+label%3Aniswitch



NI-TClk Python API Status
-------------------------

+-------------------------------+-----------------------+
| NI-TClk (nitclk)              |                       |
+===============================+=======================+
| Driver Version Tested Against | 2024 Q2               |
+-------------------------------+-----------------------+
| PyPI Version                  | |nitclkLatestVersion| |
+-------------------------------+-----------------------+
| Supported Python Version      | |nitclkPythonVersion| |
+-------------------------------+-----------------------+
| Documentation                 | |nitclkDocs|          |
+-------------------------------+-----------------------+
| Open Issues                   | |nitclkOpenIssues|    |
+-------------------------------+-----------------------+
| Open Pull Requests            | |nitclkOpenPRs|       |
+-------------------------------+-----------------------+


.. |nitclkLatestVersion| image:: http://img.shields.io/pypi/v/nitclk.svg
    :alt: Latest NI-TClk Version
    :target: http://pypi.python.org/pypi/nitclk


.. |nitclkPythonVersion| image:: http://img.shields.io/pypi/pyversions/nitclk.svg
    :alt: NI-TClk supported Python versions
    :target: http://pypi.python.org/pypi/nitclk


.. |nitclkDocs| image:: https://readthedocs.org/projects/nitclk/badge/?version=latest
    :alt: NI-TClk Python API Documentation Status
    :target: https://nitclk.readthedocs.io/en/latest


.. |nitclkOpenIssues| image:: https://img.shields.io/github/issues/ni/nimi-python/nitclk.svg
    :alt: Open Issues + Pull Requests for NI-TClk
    :target: https://github.com/ni/nimi-python/issues?q=is%3Aopen+is%3Aissue+label%3Anitclk


.. |nitclkOpenPRs| image:: https://img.shields.io/github/issues-pr/ni/nimi-python/nitclk.svg
    :alt: Pull Requests for NI-TClk
    :target: https://github.com/ni/nimi-python/pulls?q=is%3Aopen+is%3Aissue+label%3Anitclk


.. _installation-section:

Installation
============

Driver specific installation instructions can be found on **Read the Docs**:

* `nidcpower <https://nidcpower.readthedocs.io/en/latest/nidcpower.html#installation>`_
* `nidigital <https://nidigital.readthedocs.io/en/latest/nidigital.html#installation>`_
* `nidmm <https://nidmm.readthedocs.io/en/latest/nidmm.html#installation>`_
* `nifgen <https://nifgen.readthedocs.io/en/latest/nifgen.html#installation>`_
* `nimodinst <https://nimodinst.readthedocs.io/en/latest/nimodinst.html#installation>`_
* `niscope <https://niscope.readthedocs.io/en/latest/niscope.html#installation>`_
* `nise <https://nise.readthedocs.io/en/latest/nise.html#installation>`_
* `niswitch <https://niswitch.readthedocs.io/en/latest/niswitch.html#installation>`_
* `nitclk <https://nitclk.readthedocs.io/en/latest/nitclk.html#installation>`_


Contributing
============

We welcome contributions! You can clone the project repository, build it, and install it by `following these instructions <https://github.com/ni/nimi-python/blob/master/CONTRIBUTING.md>`_.

Usage
------

The following is a basic example of using the **nidmm** module to open a session to a DMM and perform a 5.5 digits of resolution voltage measurement in the 10 V range.

.. code-block:: python

    import nidmm
    with nidmm.Session("Dev1") as session:
        session.configure_measurement_digits(nidmm.Function.DC_VOLTS, 10.0, 5.5)
        print("Measurement: " + str(session.read()))

`Other usage examples can be found on GitHub. <https://github.com/ni/nimi-python/tree/master/src/nidmm/examples>`_

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

Documentation is available on **Read the Docs**:

- https://nidcpower.readthedocs.io/en/stable
- https://nidigital.readthedocs.io/en/stable
- https://nidmm.readthedocs.io/en/stable
- https://nifgen.readthedocs.io/en/stable
- https://nimodinst.readthedocs.io/en/stable
- https://niscope.readthedocs.io/en/stable
- https://nise.readthedocs.io/en/stable
- https://niswitch.readthedocs.io/en/stable
- https://nitclk.readthedocs.io/en/stable


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