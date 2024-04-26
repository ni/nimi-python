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

The **niscope** module provides a Python API for NI-SCOPE. The code is maintained in the Open Source repository for `nimi-python <https://github.com/ni/nimi-python>`_.

Support Policy
--------------
**niscope** supports all the Operating Systems supported by NI-SCOPE.

It follows `Python Software Foundation <https://devguide.python.org/#status-of-python-branches>`_ support policy for different versions of CPython.


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



.. _niscope_installation-section:

Installation
------------

As a prerequisite to using the **niscope** module, you must install the NI-SCOPE runtime on your system. Visit `ni.com/downloads <http://www.ni.com/downloads/>`_ to download the driver runtime for your devices.

The nimi-python modules (i.e. for **NI-SCOPE**) can be installed with `pip <http://pypi.python.org/pypi/pip>`_::

  $ python -m pip install niscope~=1.4.8


Contributing
============

We welcome contributions! You can clone the project repository, build it, and install it by `following these instructions <https://github.com/ni/nimi-python/blob/master/CONTRIBUTING.md>`_.

Usage
------

The following is a basic example of using the **niscope** module to open a session to a High Speed Digitizer and capture a single record of 1000 points.

.. code-block:: python

    import niscope
    with niscope.Session("Dev1") as session:
        session.channels[0].configure_vertical(range=1.0, coupling=niscope.VerticalCoupling.AC)
        session.channels[1].configure_vertical(range=10.0, coupling=niscope.VerticalCoupling.DC)
        session.configure_horizontal_timing(min_sample_rate=50000000, min_num_pts=1000, ref_position=50.0, num_records=5, enforce_realtime=True)
        with session.initiate():
            waveforms = session.channels[0,1].fetch(num_records=5)
        for wfm in waveforms:
            print('Channel {}, record {} samples acquired: {:,}\n'.format(wfm.channel, wfm.record, len(wfm.samples)))

        # Find all channel 1 records (Note channel name is always a string even if integers used in channel[])
        chan1 = [wfm for wfm in waveforms if wfm.channel == '0']

        # Find all record number 3
        rec3 = [wfm for wfm in waveforms if wfm.record == 3]

If you need faster fetch performance, or to directly interface with `SciPy <https://www.scipy.org/>`_, you can use the **fetch_into()** method instead of **fetch()**. See the fetch_into example.


`Other usage examples can be found on GitHub. <https://github.com/ni/nimi-python/tree/master/src/niscope/examples>`_


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

Documentation is available `here <http://niscope.readthedocs.io>`_.


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