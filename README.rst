+----------------------+------------------------------------------------------------------------------------------------------------+
| master branch status | |BuildStatus| |Docs| |MITLicense| |CoverageStatus|                                                         |
+----------------------+------------------------------------------------------------------------------------------------------------+
| GitHub status        | |OpenIssues| |OpenPullRequests|                                                                            |
+----------------------+------------+-----------------------------------+----------------------------+------------------------------+
|                      | **Name**   | **Driver Version Tested Against** | **PyPI Version**           | **Supported Python Version** |
|                      +------------+-----------------------------------+----------------------------+------------------------------+
| Versions             | NI-DCPower | 17.6.0                            | |nidcpowerLatestVersion|   | |nidcpowerPythonVersion|     |
|                      +------------+-----------------------------------+----------------------------+------------------------------+
|                      | NI-DMM     | 17.1.0                            | |nidmmLatestVersion|       | |nidmmPythonVersion|         |
|                      +------------+-----------------------------------+----------------------------+------------------------------+
|                      | NI-FGEN    | 17.0.0                            | |nifgenLatestVersion|      | |nifgenPythonVersion|        |
|                      +------------+-----------------------------------+----------------------------+------------------------------+
|                      | NI-SCOPE   | 17.0.2                            | |niscopeLatestVersion|     | |niscopePythonVersion|       |
|                      +------------+-----------------------------------+----------------------------+------------------------------+
|                      | NI-SWITCH  | 17.0.0                            | |niswitchLatestVersion|    | |niswitchPythonVersion|      |
|                      +------------+-----------------------------------+----------------------------+------------------------------+
|                      | NI-ModInst | 17.0.0                            | |nimodinstLatestVersion|   | |nimodinstPythonVersion|     |
+----------------------+------------+-----------------------------------+----------------------------+------------------------------+

===========  ============================================================================================================================
Info         Python bindings for NI Modular Instrument drivers. See `GitHub <https://github.com/ni/nimi-python/>`_ for the latest source.
Author       National Instruments
===========  ============================================================================================================================

.. _about-section:

.. image:: https://raw.githubusercontent.com/ni/nimi-python/master/docs/_static/python-dmm-small.jpg
   :alt: NI Digital Multimeter with Python logo
   :align: center

About
=====

The **nimi-python** repository generates Python bindings (Application Programming Interface) for interacting with the Modular Instrument drivers. Currently, the following drivers are supported:

* NI-DCPower (Python module: nidcpower)
* NI-DMM (Python module: nidmm)
* NI-FGEN (Python module: nifgen)
* NI-SCOPE (Python module: niscope)
* NI-SWITCH (Python module: niswitch)
* NI-ModInst (Python module: nimodinst)

It is implemented as a set of `Mako templates <http://makotemplates.org>`_ and per-driver metafiles that produce a Python module for each driver. The driver is called through its public C API using the
`ctypes <https://docs.python.org/2/library/ctypes.html>`_ Python library.

**nimi-python** supports all the Operating Systems supported by the underlying driver.

**nimi-python** supports Python 2.7, 3.4 and later using CPython or PyPy.

.. _installation-section:

Installation
============

As a prerequisite to using nimi-python modules, you must install the corresponding driver runtime on your system. Visit `ni.com/downloads <http://www.ni.com/downloads/>`_ to download the driver runtime for your devices.

The nimi-python modules (i.e. for **NI-DMM**) can be installed with `pip <http://pypi.python.org/pypi/pip>`_::

  $ python -m pip install nidmm

Or **easy_install** from
`setuptools <http://pypi.python.org/pypi/setuptools>`_::

  $ python -m easy_install nidmm

Contributing
============

We welcome contributions! You can clone the project repository, build it, and install it by `following these instructions <https://github.com/ni/nimi-python/blob/readme-contributing-link/CONTRIBUTING.md>`_.

.. _usage-section:

Usage
=====

The following is a basic example of using the **nidmm** module to open a session to a DMM and perform a 5.5 digits of resolution voltage measurement in the 10 V range.

.. code-block:: python

    import nidmm
    with nidmm.Session("Dev1") as session:
        session.configureMeasurementDigits(nidmm.Function.DC_VOLTS, 10, 5.5)
        print("Measurement: " + str(session.read()))

Repeated capabilities
---------------------

* Repeated capabilities are accessed using a repeated capabilies object for each type of repeated capability that the driver supports. Some drivers do not use repeated capabilities.
* The repeated capabilities object can take integers or strings, a single item or a list, or a slice.
* The repeated capabilities object knows the proper prefix and will add it if needed.
* The following are all legal

    .. code-block:: python

        import nifgen
        session = nifgen.Session('PXI1Slot2')

        # Channel repeated capabilities
        session.channels['0'].channel_enabled = True
        session.channels[0].channel_enabled = True
        session.channels[[0, 1, 3]].channel_enabled = True
        session.channels[range(8)].channel_enabled = True  # channels 0, 1, 2, 3, 4, 5, 6, 7
        session.channels[:8].channel_enabled = True  # channels 0, 1, 2, 3, 4, 5, 6, 7
        wfm = session.channels[[0, 1, 3]].fetch(5000)

        # P2P repeated capabilities
        i = session.script_triggers['0'].SCRIPT_TRIGGERS_COUNT
        i = session.script_triggers[0].SCRIPT_TRIGGERS_COUNT
        i = session.script_triggers[[0, 1, 3]].SCRIPT_TRIGGERS_COUNT
        i = session.script_triggers['ScriptTrigger0'].SCRIPT_TRIGGERS_COUNT

Additional examples for each driver are located in src/<driver>/examples/ directory.

.. _support-section:

Support / Feedback
==================

The packages included in **nimi-python** package are supported by NI. For support, open
a request through the NI support portal at `ni.com <http://www.ni.com>`_.

.. _bugs-section:

Bugs / Feature Requests
=======================

To report a bug or submit a feature request, please use the
`GitHub issues page <https://github.com/ni/nimi-python/issues>`_.

Information to Include When Asking for Help
-------------------------------------------

Please include **all** of the following information when opening an issue:

- Detailed steps on how to reproduce the problem and full traceback, if
  applicable. Code samples are encouraged!

- The python version used::

  $ python -c "import sys; print(sys.version)"

- The module (i.e. **nidmm**) and its version::

  $ python -m pip list

- The version of the driver used (i.e. **NI-DMM 17.1**). Follow
  `this KB article <http://digital.ni.com/express.nsf/bycode/ex8amn>`_
  to determine the version you have installed.

- The operating system, version, and bitness. For example 64-bit Windows 7.

.. _documentation-section:

Documentation
=============

Documentation is available `here <http://nimi-python.readthedocs.io>`_.

Additional Documentation
========================

Refer to your driver documentation for device-specific information and detailed API documentation.

.. _license-section:

License
=======

**nimi-python** is licensed under an MIT-style license (`see
LICENSE <https://github.com/ni/nimi-python/blob/master/LICENSE>`_).
Other incorporated projects may be licensed under different licenses. All
licenses allow for non-commercial and commercial use.

.. |BuildStatus| image:: https://img.shields.io/travis/ni/nimi-python.svg
    :alt: Build Status - master branch
    :target: https://travis-ci.org/ni/nimi-python

.. |Docs| image:: https://readthedocs.org/projects/nimi-python/badge/?version=latest
    :alt: Documentation Status - master branch
    :target: https://nimi-python.readthedocs.io/en/latest/?badge=latest

.. |MITLicense| image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :alt: MIT License
    :target: https://opensource.org/licenses/MIT

.. |CoverageStatus| image:: https://coveralls.io/repos/github/ni/nimi-python/badge.svg?branch=master&dummy=no_cache_please_1
    :alt: Test Coverage - master branch
    :target: https://coveralls.io/github/ni/nimi-python?branch=master

.. |nidcpowerLatestVersion| image:: http://img.shields.io/pypi/v/nidcpower.svg
    :alt: Latest NI-DMM Version
    :target: http://pypi.python.org/pypi/nidmm

.. |nidcpowerPythonVersion| image:: http://img.shields.io/pypi/pyversions/nidcpower.svg
    :alt: NI-DCPower supported Python versions
    :target: http://pypi.python.org/pypi/nidcpower

.. |nidmmLatestVersion| image:: http://img.shields.io/pypi/v/nidcpower.svg
    :alt: Latest NI-DCPower Version
    :target: http://pypi.python.org/pypi/nidcpower

.. |nidmmPythonVersion| image:: http://img.shields.io/pypi/pyversions/nidmm.svg
    :alt: NI-DMM supported Python versions
    :target: http://pypi.python.org/pypi/nidmm

.. |nimodinstLatestVersion| image:: http://img.shields.io/pypi/v/nimodinst.svg
    :alt: Latest NI-ModInst Version
    :target: http://pypi.python.org/pypi/nimodinst

.. |nimodinstPythonVersion| image:: http://img.shields.io/pypi/pyversions/nimodinst.svg
    :alt: NI-ModInst supported Python versions
    :target: http://pypi.python.org/pypi/nimodinst

.. |niswitchLatestVersion| image:: http://img.shields.io/pypi/v/niswitch.svg
    :alt: Latest NI-SWITCH Version
    :target: http://pypi.python.org/pypi/niswitch

.. |niswitchPythonVersion| image:: http://img.shields.io/pypi/pyversions/niswitch.svg
    :alt: NI-SWITCH supported Python versions
    :target: http://pypi.python.org/pypi/niswitch

.. |niscopeLatestVersion| image:: http://img.shields.io/pypi/v/niscope.svg
    :alt: Latest NI-SCOPE Version
    :target: http://pypi.python.org/pypi/niscope

.. |niscopePythonVersion| image:: http://img.shields.io/pypi/pyversions/niscope.svg
    :alt: NI-SCOPE supported Python versions
    :target: http://pypi.python.org/pypi/niscope

.. |nifgenLatestVersion| image:: http://img.shields.io/pypi/v/nifgen.svg
    :alt: Latest NI-FGEN Version
    :target: http://pypi.python.org/pypi/nifgen

.. |nifgenPythonVersion| image:: http://img.shields.io/pypi/pyversions/nifgen.svg
    :alt: NI-FGEN supported Python versions
    :target: http://pypi.python.org/pypi/nifgen

.. |OpenIssues| image:: https://img.shields.io/github/issues/ni/nimi-python.svg
    :alt: Open Issues + Pull Requests
    :target: https://github.com/ni/nimi-python/issues

.. |OpenPullRequests| image:: https://img.shields.io/github/issues-pr/ni/nimi-python.svg
    :alt: Open Pull Requests
    :target: https://github.com/ni/nimi-python/pulls

