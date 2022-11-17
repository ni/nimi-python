Exceptions and Warnings
=======================

Error
-----

    .. py:currentmodule:: niscope.errors

    .. exception:: Error

        Base exception type that all NI-SCOPE exceptions derive from


DriverError
-----------

    .. py:currentmodule:: niscope.errors

    .. exception:: DriverError

        An error originating from the NI-SCOPE driver


UnsupportedConfigurationError
-----------------------------

    .. py:currentmodule:: niscope.errors

    .. exception:: UnsupportedConfigurationError

        An error due to using this module in an usupported platform.

DriverNotInstalledError
-----------------------

    .. py:currentmodule:: niscope.errors

    .. exception:: DriverNotInstalledError

        An error due to using this module without the driver runtime installed.

DriverTooOldError
-----------------

    .. py:currentmodule:: niscope.errors

    .. exception:: DriverTooOldError

        An error due to using this module with an older version of the NI-SCOPE driver runtime.

DriverTooNewError
-----------------

    .. py:currentmodule:: niscope.errors

    .. exception:: DriverTooNewError

        An error due to the NI-SCOPE driver runtime being too new for this module.

InvalidRepeatedCapabilityError
------------------------------

    .. py:currentmodule:: niscope.errors

    .. exception:: InvalidRepeatedCapabilityError

        An error due to an invalid character in a repeated capability


SelfTestError
-------------

    .. py:currentmodule:: niscope.errors

    .. exception:: SelfTestError

        An error due to a failed self-test


RpcError
--------

    .. py:currentmodule:: niscope.errors

    .. exception:: RpcError

        An error specific to gRPC sessions


DriverWarning
-------------

    .. py:currentmodule:: niscope.errors

    .. exception:: DriverWarning

        A warning originating from the NI-SCOPE driver



