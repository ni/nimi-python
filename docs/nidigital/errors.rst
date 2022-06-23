Exceptions and Warnings
=======================

Error
-----

    .. py:currentmodule:: nidigital.errors

    .. exception:: Error

        Base exception type that all NI-Digital Pattern Driver exceptions derive from


DriverError
-----------

    .. py:currentmodule:: nidigital.errors

    .. exception:: DriverError

        An error originating from the NI-Digital Pattern Driver driver


UnsupportedConfigurationError
-----------------------------

    .. py:currentmodule:: nidigital.errors

    .. exception:: UnsupportedConfigurationError

        An error due to using this module in an usupported platform.

DriverNotInstalledError
-----------------------

    .. py:currentmodule:: nidigital.errors

    .. exception:: DriverNotInstalledError

        An error due to using this module without the driver runtime installed.

DriverTooOldError
-----------------

    .. py:currentmodule:: nidigital.errors

    .. exception:: DriverTooOldError

        An error due to using this module with an older version of the driver runtime.

DriverTooNewError
-----------------

    .. py:currentmodule:: nidigital.errors

    .. exception:: DriverTooNewError

        An error due to the driver runtime being too new for the Python module.

InvalidRepeatedCapabilityError
------------------------------

    .. py:currentmodule:: nidigital.errors

    .. exception:: InvalidRepeatedCapabilityError

        An error due to an invalid character in a repeated capability


SelfTestError
-------------

    .. py:currentmodule:: nidigital.errors

    .. exception:: SelfTestError

        An error due to a failed self-test


DriverWarning
-------------

    .. py:currentmodule:: nidigital.errors

    .. exception:: DriverWarning

        A warning originating from the NI-Digital Pattern Driver driver



