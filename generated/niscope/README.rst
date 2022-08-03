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


NI-SCOPE Python API Status
--------------------------

+-------------------------------+------------------------+
| NI-SCOPE (niscope)            |                        |
+===============================+========================+
| Driver Version Tested Against | 2022 Q3                |
+-------------------------------+------------------------+
| PyPI Version                  | |niscopeLatestVersion| |
+-------------------------------+------------------------+
| Supported Python Version      | |niscopePythonVersion| |
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


.. |niscopeOpenIssues| image:: https://img.shields.io/github/issues/ni/nimi-python/niscope.svg
    :alt: Open Issues + Pull Requests for NI-SCOPE
    :target: https://github.com/ni/nimi-python/issues?q=is%3Aopen+is%3Aissue+label%3Aniscope


.. |niscopeOpenPRs| image:: https://img.shields.io/github/issues-pr/ni/nimi-python/niscope.svg
    :alt: Pull Requests for NI-SCOPE
    :target: https://github.com/ni/nimi-python/pulls?q=is%3Aopen+is%3Aissue+label%3Aniscope



.. _niscope_installation-section:

Installation
------------

As a prerequisite to using the niscope module, you must install the NI-SCOPE runtime on your system. Visit `ni.com/downloads <http://www.ni.com/downloads/>`_ to download the driver runtime for your devices.

The nimi-python modules (i.e. for **NI-SCOPE**) can be installed with `pip <http://pypi.python.org/pypi/pip>`_::

  $ python -m pip install niscope~=1.4.2

Or **easy_install** from
`setuptools <http://pypi.python.org/pypi/setuptools>`_::

  $ python -m easy_install niscope


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
            print('Channel {0}, record {1} samples acquired: {2:,}\n'.format(wfm.channel, wfm.record, len(wfm.samples)))

        # Find all channel 1 records (Note channel name is always a string even if integers used in channel[])
        chan1 = [wfm for wfm in waveforms if wfm.channel == '0']

        # Find all record number 3
        rec3 = [wfm for wfm in waveforms if wfm.record == 3]

The waveform returned from `fetch <niscope/class.html#fetch>`_ is a flat list of Python objects

    - Attributes:

        -  **relative_initial_x** (float) the time (in seconds) from the trigger to the first sample in the fetched waveform
        -  **absolute_initial_x** (float) timestamp (in seconds) of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output.
        -  **x_increment** (float) the time between points in the acquired waveform in seconds
        -  **channel** (str) channel name this waveform was acquired from
        -  **record** (int) record number of this waveform
        -  **gain** (float) the gain factor of the given channel; useful for scaling binary data with the following formula:

                voltage = binary data * gain factor + offset

        -  **offset** (float) the offset factor of the given channel; useful for scaling binary data with the following formula:

                voltage = binary data * gain factor + offset

        - **samples** (array of float) floating point array of samples. Length will be of the actual samples acquired

    - Such that all record 0 waveforms are first. For example, with a channel list of 0,1, you would have the following index values:

        - index 0 = record 0, channel 0
        - index 1 = record 0, channel 1
        - index 2 = record 1, channel 0
        - index 3 = record 1, channel 1
        - etc.


If you need more performance or need to work with `SciPy <https://www.scipy.org/>`_, you can use the `fetch_into()` method instead of `fetch()`. This
method takes an already allocated `numpy <http://www.numpy.org/>`_ array and puts the acquired samples in it. Data types supported:

    - `numpy.float64`
    - `numpy.int8`
    - `numpy.in16`
    - `numpy.int32`

.. code-block:: python

    voltage_range = 1.0
    record_length = 2000
    channels = [0, 1]
    num_channels = len(channels)
    num_records = 5
    wfm = numpy.ndarray(num_channels * record_length, dtype=numpy.int8)
    session.configure_vertical(voltage_range, niscope.VerticalCoupling.AC)
    session.configure_horizontal_timing(50000000, record_length, 50.0, num_records, True)
    with session.initiate():
        waveform_infos = session.channels[channels].fetch_into(wfm=wfm, num_records=num_records)

The waveform_infos returned from `fetch_into <niscope/class.html#fetch-into>`_ is a 1D list of Python objects

    - Attributes:

        -  **relative_initial_x** (float) the time (in seconds) from the trigger to the first sample in the fetched waveform
        -  **absolute_initial_x** (float) timestamp (in seconds) of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output.
        -  **x_increment** (float) the time between points in the acquired waveform in seconds
        -  **channel** (str) channel name this waveform was asquire from
        -  **record** (int) record number of this waveform
        -  **gain** (float) the gain factor of the given channel; useful for scaling binary data with the following formula:

                voltage = binary data * gain factor + offset

        -  **offset** (float) the offset factor of the given channel; useful for scaling binary data with the following formula:

                voltage = binary data * gain factor + offset

        - **samples** (numpy array of datatype used) floating point array of samples. Length will be of the actual samples acquired

            .. note::

                Python 3 only

    - Such that all record 0 waveforms are first. For example, with a channel list of 0,1, you would have the following index values:

        - index 0 = record 0, channel 0
        - index 1 = record 0, channel 1
        - index 2 = record 1, channel 0
        - index 3 = record 1, channel 1
        - etc.


.. note:: When using Python 2, the waveform_infos objects do not include the waveform for that record. Instead, samples are in the waveform passed into the function using the following layout:

    - index 0 = record 0, channel 0
    - index *x* = record 0, channel 1
    - index 2\ *x* = record 1, channel 0
    - index 3\ *x* = record 1, channel 1
    - etc.
    - Where *x* = the record length


`Other usage examples can be found on GitHub. <https://github.com/ni/nimi-python/tree/master/src/niscope/examples>`_


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


