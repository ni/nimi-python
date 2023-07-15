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

This package, which is maintained in the `**nimi-python** repository <https://github.com/ni/nimi-python>`_, provides a Python API for the associated driver.

Support Policy
--------------
This package supports all the Operating Systems supported by the underlying driver.

It follows `Python Software Foundation <https://devguide.python.org/#status-of-python-branches>`_ support policy for different versions.


NI-DCPower Python API Status
----------------------------

+-------------------------------+--------------------------+
| NI-DCPower (nidcpower)        |                          |
+===============================+==========================+
| Driver Version Tested Against | 2023 Q2                  |
+-------------------------------+--------------------------+
| PyPI Version                  | |nidcpowerLatestVersion| |
+-------------------------------+--------------------------+
| Supported Python Version      | |nidcpowerPythonVersion| |
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


.. |nidcpowerOpenIssues| image:: https://img.shields.io/github/issues/ni/nimi-python/nidcpower.svg
    :alt: Open Issues + Pull Requests for NI-DCPower
    :target: https://github.com/ni/nimi-python/issues?q=is%3Aopen+is%3Aissue+label%3Anidcpower


.. |nidcpowerOpenPRs| image:: https://img.shields.io/github/issues-pr/ni/nimi-python/nidcpower.svg
    :alt: Pull Requests for NI-DCPower
    :target: https://github.com/ni/nimi-python/pulls?q=is%3Aopen+is%3Aissue+label%3Anidcpower



.. _nidcpower_installation-section:

Installation
------------

As a prerequisite to using the nidcpower module, you must install the NI-DCPower runtime on your system. Visit `ni.com/downloads <http://www.ni.com/downloads/>`_ to download the driver runtime for your devices.

The nimi-python modules (i.e. for **NI-DCPower**) can be installed with `pip <http://pypi.python.org/pypi/pip>`_::

  $ python -m pip install nidcpower


Contributing
============

We welcome contributions! You can clone the project repository, build it, and install it by `following these instructions <https://github.com/ni/nimi-python/blob/master/CONTRIBUTING.md>`_.

Usage
------

The following is a basic example of using the **nidcpower** module to open a session to a Source Meter Unit and measure voltage and current.

.. code-block:: python

    import nidcpower
    # Configure the session.

    with nidcpower.Session(resource_name='PXI1Slot2/0') as session:
        session.measure_record_length = 20
        session.measure_record_length_is_finite = True
        session.measure_when = nidcpower.MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE
        session.voltage_level = 5.0

        session.commit()
        print('Effective measurement rate: {0} S/s'.format(session.measure_record_delta_time / 1))

        samples_acquired = 0
        print('Channel           Num  Voltage    Current    In Compliance')
        row_format = '{0:15} {1:3d}    {2:8.6f}   {3:8.6f}   {4}'
        with session.initiate():
            channel_indices = '0-{0}'.format(session.channel_count - 1)
            channels = session.get_channel_names(channel_indices)
            for i, channel_name in enumerate(channels):
                samples_acquired = 0
                while samples_acquired < 20:
                    measurements = session.channels[channel_name].fetch_multiple(count=session.fetch_backlog)
                    samples_acquired += len(measurements)
                    for i in range(len(measurements)):
                        print(row_format.format(channel_name, i, measurements[i].voltage, measurements[i].current, measurements[i].in_compliance))

`Other usage examples can be found on GitHub. <https://github.com/ni/nimi-python/tree/master/src/nidcpower/examples>`_

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

Documentation is available `here <http://nidcpower.readthedocs.io>`_.


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