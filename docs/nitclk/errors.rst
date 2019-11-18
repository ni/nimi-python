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

InvalidRepeatedCapabilityError
------------------------------

    .. py:currentmodule:: nitclk.errors

    .. exception:: InvalidRepeatedCapabilityError

        An error due to an invalid character in a repeated capability


SelfTestError
-------------

    .. py:currentmodule:: nitclk.errors

    .. exception:: SelfTestError

        An error due to a failed self-test


DriverWarning
-------------

    .. py:currentmodule:: nitclk.errors

    .. exception:: DriverWarning

        A warning originating from the NI-TClk driver



