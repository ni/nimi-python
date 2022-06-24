Exceptions and Warnings
=======================

Error
-----

    .. py:currentmodule:: nise.errors

    .. exception:: Error

        Base exception type that all NI Switch Executive exceptions derive from


DriverError
-----------

    .. py:currentmodule:: nise.errors

    .. exception:: DriverError

        An error originating from the NI Switch Executive driver


UnsupportedConfigurationError
-----------------------------

    .. py:currentmodule:: nise.errors

    .. exception:: UnsupportedConfigurationError

        An error due to using this module in an usupported platform.

DriverNotInstalledError
-----------------------

    .. py:currentmodule:: nise.errors

    .. exception:: DriverNotInstalledError

        An error due to using this module without the driver runtime installed.

DriverTooOldError
-----------------

    .. py:currentmodule:: nise.errors

    .. exception:: DriverTooOldError

        An error due to using this module with an older version of the driver runtime.

DriverTooNewError
-----------------

    .. py:currentmodule:: nise.errors

    .. exception:: DriverTooNewError

        An error due to the driver runtime being too new for the Python module.

InvalidRepeatedCapabilityError
------------------------------

    .. py:currentmodule:: nise.errors

    .. exception:: InvalidRepeatedCapabilityError

        An error due to an invalid character in a repeated capability


DriverWarning
-------------

    .. py:currentmodule:: nise.errors

    .. exception:: DriverWarning

        A warning originating from the NI Switch Executive driver



