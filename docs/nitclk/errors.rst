Exceptions and Warnings
=======================

Error
-----

    .. py:currentmodule:: nitclk.errors

    .. exception:: Error

        Base exception type that all NI-TClk exceptions derive from


DriverError
-----------

    .. py:currentmodule:: nitclk.errors

    .. exception:: DriverError

        An error originating from the NI-TClk driver


UnsupportedConfigurationError
-----------------------------

    .. py:currentmodule:: nitclk.errors

    .. exception:: UnsupportedConfigurationError

        An error due to using this module in an usupported platform.

DriverNotInstalledError
-----------------------

    .. py:currentmodule:: nitclk.errors

    .. exception:: DriverNotInstalledError

        An error due to using this module without the driver runtime installed.

DriverTooOldError
-----------------

    .. py:currentmodule:: nitclk.errors

    .. exception:: DriverTooOldError

        An error due to using this module with an older version of the driver runtime.

DriverTooNewError
-----------------

    .. py:currentmodule:: nitclk.errors

    .. exception:: DriverTooNewError

        An error due to the driver runtime being too new for the Python module.

DriverWarning
-------------

    .. py:currentmodule:: nitclk.errors

    .. exception:: DriverWarning

        A warning originating from the NI-TClk driver



