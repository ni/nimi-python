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

The **nidigital** module provides a Python API for NI-Digital Pattern Driver. The code is maintained in the Open Source repository for `nimi-python <https://github.com/ni/nimi-python>`_.

Support Policy
--------------
**nidigital** supports all the Operating Systems supported by NI-Digital Pattern Driver.

It follows `Python Software Foundation <https://devguide.python.org/#status-of-python-branches>`_ support policy for different versions of CPython.


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



.. _nidigital_installation-section:

Installation
------------

As a prerequisite to using the **nidigital** module, you must install the NI-Digital Pattern Driver runtime on your system. Visit `ni.com/downloads <http://www.ni.com/downloads/>`_ to download the driver runtime for your devices.

The nimi-python modules (i.e. for **NI-Digital Pattern Driver**) can be installed with `pip <http://pypi.python.org/pypi/pip>`_::

  $ python -m pip install nidigital~=1.4.8


Contributing
============

We welcome contributions! You can clone the project repository, build it, and install it by `following these instructions <https://github.com/ni/nimi-python/blob/master/CONTRIBUTING.md>`_.

Usage
------

The following is a basic example of using the **nidigital** module to open a session to a digital pattern instrument,
source current, and measure both voltage and current using the PPMU on selected channels.

.. code-block:: python

    import nidigital
    import time

    with nidigital.Session(resource_name='PXI1Slot2') as session:

        channels = 'PXI1Slot2/0,PXI1Slot2/1'

        # Configure PPMU measurements
        session.channels[channels].ppmu_aperture_time = 0.000004
        session.channels[channels].ppmu_aperture_time_units = nidigital.PPMUApertureTimeUnits.SECONDS

        session.channels[channels].ppmu_output_function = nidigital.PPMUOutputFunction.CURRENT

        session.channels[channels].ppmu_current_level_range = 0.000002
        session.channels[channels].ppmu_current_level = 0.000002
        session.channels[channels].ppmu_voltage_limit_high = 3.3
        session.channels[channels].ppmu_voltage_limit_low = 0

        # Sourcing
        session.channels[channels].ppmu_source()

        # Settling time between sourcing and measuring
        time.sleep(0.01)

        # Measuring
        current_measurements = session.channels[channels].ppmu_measure(nidigital.PPMUMeasurementType.CURRENT)
        voltage_measurements = session.channels[channels].ppmu_measure(nidigital.PPMUMeasurementType.VOLTAGE)

        print('{:<20} {:<10} {:<10}'.format('Channel Name', 'Current', 'Voltage'))
        for channel, current, voltage in zip(channels.split(','), current_measurements, voltage_measurements):
            print('{:<20} {:<10f} {:<10f}'.format(channel, current, voltage))

        # Disconnect all channels using programmable onboard switching
        session.channels[channels].selected_function = nidigital.SelectedFunction.DISCONNECT

`Other usage examples can be found on GitHub. <https://github.com/ni/nimi-python/tree/master/src/nidigital/examples>`_

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

Documentation is available `here <http://nidigital.readthedocs.io>`_.


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