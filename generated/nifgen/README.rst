Overall Status
--------------

+----------------------+------------------------------------------------------------------------------------------------------------------------------------+
| master branch status | |BuildStatus| |Docs| |MITLicense| |CoverageStatus|                                                                                 |
+----------------------+------------------------------------------------------------------------------------------------------------------------------------+
| GitHub status        | |OpenIssues| |OpenPullRequests|                                                                                                    |
+----------------------+------------------------------------------------------------------------------------------------------------------------------------+

===========  ============================================================================================================================
Info         Python bindings for NI Modular Instrument drivers. See `GitHub <https://github.com/ni/nimi-python/>`_ for the latest source.
Author       NI
===========  ============================================================================================================================

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

**nimi-python** follows `Python Software Foundation <https://devguide.python.org/#status-of-python-branches>`_ support policy for different versions. At
this time this includes Python 3.6 and above using CPython.


NI-FGEN Python API Status
-------------------------

+-------------------------------+-----------------------+
| NI-FGEN (nifgen)              |                       |
+===============================+=======================+
| Driver Version Tested Against | 21.8.0                |
+-------------------------------+-----------------------+
| PyPI Version                  | |nifgenLatestVersion| |
+-------------------------------+-----------------------+
| Supported Python Version      | |nifgenPythonVersion| |
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


.. |nifgenOpenIssues| image:: https://img.shields.io/github/issues/ni/nimi-python/nifgen.svg
    :alt: Open Issues + Pull Requests for NI-FGEN
    :target: https://github.com/ni/nimi-python/issues?q=is%3Aopen+is%3Aissue+label%3Anifgen


.. |nifgenOpenPRs| image:: https://img.shields.io/github/issues-pr/ni/nimi-python/nifgen.svg
    :alt: Pull Requests for NI-FGEN
    :target: https://github.com/ni/nimi-python/pulls?q=is%3Aopen+is%3Aissue+label%3Anifgen



.. _nifgen_installation-section:

Installation
------------

As a prerequisite to using the nifgen module, you must install the NI-FGEN runtime on your system. Visit `ni.com/downloads <http://www.ni.com/downloads/>`_ to download the driver runtime for your devices.

The nimi-python modules (i.e. for **NI-FGEN**) can be installed with `pip <http://pypi.python.org/pypi/pip>`_::

  $ python -m pip install nifgen~=1.4.2

Or **easy_install** from
`setuptools <http://pypi.python.org/pypi/setuptools>`_::

  $ python -m easy_install nifgen


Contributing
============

We welcome contributions! You can clone the project repository, build it, and install it by `following these instructions <https://github.com/ni/nimi-python/blob/master/CONTRIBUTING.md>`_.

Usage
------

The following is a basic example of using the **nifgen** module to open a session to a Function Generator and generate a sine wave for 5 seconds.

.. code-block:: python

    import nifgen
    import time
    with nifgen.Session("Dev1") as session:
        session.output_mode = nifgen.OutputMode.FUNC
        session.configure_standard_waveform(waveform=nifgen.Waveform.SINE, amplitude=1.0, frequency=10000000, dc_offset=0.0, start_phase=0.0)
        with session.initiate():
            time.sleep(5)

`Other usage examples can be found on GitHub. <https://github.com/ni/nimi-python/tree/master/src/nifgen/examples>`_

.. _support-section:

Support / Feedback
==================

The packages included in **nimi-python** package are supported by NI. For support, open
a request through the NI support portal at `ni.com <http://www.ni.com>`_.

.. _bugs-section:

Bugs / Feature Requests
=======================

To report a bug or submit a feature request specific to NI Modular Instruments Python bindings (nimi-python), please use the
`GitHub issues page <https://github.com/ni/nimi-python/issues>`_.

Fill in the issue template as completely as possible and we will respond as soon
as we can.

For hardware support or any other questions not specific to this GitHub project, please visit `NI Community Forums <https://forums.ni.com/>`_.


.. _documentation-section:

Documentation
=============

Documentation is available `here <http://nimi-python.readthedocs.io>`_.


.. _license-section:

License
=======

**nimi-python** is licensed under an MIT-style license (`see
LICENSE <https://github.com/ni/nimi-python/blob/master/LICENSE>`_).
Other incorporated projects may be licensed under different licenses. All
licenses allow for non-commercial and commercial use.


