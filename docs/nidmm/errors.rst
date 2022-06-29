Exceptions and Warnings
=======================

Error
-----

    .. py:currentmodule:: nidmm.errors

    .. exception:: Error

        Base exception type that all NI-DMM exceptions derive from


DriverError
-----------

    .. py:currentmodule:: nidmm.errors

    .. exception:: DriverError

        An error originating from the NI-DMM driver


UnsupportedConfigurationError
-----------------------------

    .. py:currentmodule:: nidmm.errors

    .. exception:: UnsupportedConfigurationError

        An error due to using this module in an usupported platform.

DriverNotInstalledError
-----------------------

    .. py:currentmodule:: nidmm.errors

    .. exception:: DriverNotInstalledError

        An error due to using this module without the driver runtime installed.

DriverTooOldError
-----------------

    .. py:currentmodule:: nidmm.errors

    .. exception:: DriverTooOldError

        An error due to using this module with an older version of the NI-DMM driver runtime.

DriverTooNewError
-----------------

    .. py:currentmodule:: nidmm.errors

    .. exception:: DriverTooNewError

        An error due to the NI-DMM driver runtime being too new for this module.

InvalidRepeatedCapabilityError
------------------------------

    .. py:currentmodule:: nidmm.errors

    .. exception:: InvalidRepeatedCapabilityError

        An error due to an invalid character in a repeated capability


SelfTestError
-------------

    .. py:currentmodule:: nidmm.errors

    .. exception:: SelfTestError

        An error due to a failed self-test


DriverWarning
-------------

    .. py:currentmodule:: nidmm.errors

    .. exception:: DriverWarning

        A warning originating from the NI-DMM driver



