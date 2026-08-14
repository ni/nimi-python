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

The **nirfsa** module provides a Python API for NI-RFSA. The code is maintained in the Open Source repository for `nimi-python <https://github.com/ni/nimi-python>`_.

Support Policy
--------------
**nirfsa** supports all the Operating Systems supported by NI-RFSA.

It follows `Python Software Foundation <https://devguide.python.org/#status-of-python-branches>`_ support policy for different versions of CPython.

NI created and supports **nirfsa**.


NI-RFSA Python API Status
-------------------------

+-------------------------------+-----------------------+
| NI-RFSA (nirfsa)              |                       |
+===============================+=======================+
| Driver Version Tested Against | 2026 Q3               |
+-------------------------------+-----------------------+
| PyPI Version                  | |nirfsaLatestVersion| |
+-------------------------------+-----------------------+
| Supported Python Version      | |nirfsaPythonVersion| |
+-------------------------------+-----------------------+
| Documentation                 | |nirfsaDocs|          |
+-------------------------------+-----------------------+
| Open Issues                   | |nirfsaOpenIssues|    |
+-------------------------------+-----------------------+
| Open Pull Requests            | |nirfsaOpenPRs|       |
+-------------------------------+-----------------------+


.. |nirfsaLatestVersion| image:: http://img.shields.io/pypi/v/nirfsa.svg
    :alt: Latest NI-RFSA Version
    :target: http://pypi.python.org/pypi/nirfsa


.. |nirfsaPythonVersion| image:: http://img.shields.io/pypi/pyversions/nirfsa.svg
    :alt: NI-RFSA supported Python versions
    :target: http://pypi.python.org/pypi/nirfsa


.. |nirfsaDocs| image:: https://readthedocs.org/projects/nirfsa/badge/?version=latest
    :alt: NI-RFSA Python API Documentation Status
    :target: https://nirfsa.readthedocs.io/en/latest


.. |nirfsaOpenIssues| image:: https://img.shields.io/github/issues/ni/nimi-python/nirfsa.svg
    :alt: Open Issues + Pull Requests for NI-RFSA
    :target: https://github.com/ni/nimi-python/issues?q=is%3Aopen+is%3Aissue+label%3Anirfsa


.. |nirfsaOpenPRs| image:: https://img.shields.io/github/issues-pr/ni/nimi-python/nirfsa.svg
    :alt: Pull Requests for NI-RFSA
    :target: https://github.com/ni/nimi-python/pulls?q=is%3Aopen+is%3Aissue+label%3Anirfsa



.. _nirfsa_installation-section:

Installation
------------

As a prerequisite to using the **nirfsa** module, you must install the NI-RFSA runtime on your system. Visit `ni.com/downloads <http://www.ni.com/downloads/>`_ to download the driver runtime for your devices.

The nimi-python modules (i.e. for **NI-RFSA**) can be installed with `pip <http://pypi.python.org/pypi/pip>`_::

  $ python -m pip install nirfsa


Contributing
============

We welcome contributions! You can clone the project repository, build it, and install it by `following these instructions <https://github.com/ni/nimi-python/blob/master/CONTRIBUTING.md>`_.

Usage
------

The following is a basic example of using the **nirfsa** module to open a session to an RF Signal Analyzer and perform a spectrum acquisition.

.. code-block:: python

    import nirfsa

    # Configure the session
    with nirfsa.Session(resource_name='5841', id_query=False, reset_device=False, options='Simulate=1, DriverSetup=Model:5841') as rfsa_session:
        rfsa_session.acquisition_type = nirfsa.AcquisitionType.IQ

        rfsa_session.reference_level = -10
        rfsa_session.iq_carrier_frequency = 1e9

        iq_data_array = np.zeros(1024, dtype=np.complex128)

        wfm_info = rfsa_session.read_iq_single_record_into(iq_data_array)
        # Perform measurements...

`Other usage examples can be found on GitHub. <https://github.com/ni/nimi-python/tree/master/src/nirfsa/examples>`_
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

Documentation is available `here <http://nirfsa.readthedocs.io>`_.


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