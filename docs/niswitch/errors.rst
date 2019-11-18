Exceptions and Warnings
=======================

Error
-----

    .. py:currentmodule:: niswitch.errors

    .. exception:: Error

        Base exception type that all NI-SWITCH exceptions derive from


DriverError
-----------

    .. py:currentmodule:: niswitch.errors

    .. exception:: DriverError

        An error originating from the NI-SWITCH driver


UnsupportedConfigurationError
-----------------------------

    .. py:currentmodule:: niswitch.errors

    .. exception:: UnsupportedConfigurationError

        An error due to using this module in an usupported platform.

DriverNotInstalledError
-----------------------

    .. py:currentmodule:: niswitch.errors

    .. exception:: DriverNotInstalledError

        An error due to using this module without the driver runtime installed.

InvalidRepeatedCapabilityError
------------------------------

    .. py:currentmodule:: niswitch.errors

    .. exception:: InvalidRepeatedCapabilityError

        An error due to an invalid character in a repeated capability


SelfTestError
-------------

    .. py:currentmodule:: niswitch.errors

    .. exception:: SelfTestError

        An error due to a failed self-test


DriverWarning
-------------

    .. py:currentmodule:: niswitch.errors

    .. exception:: DriverWarning

        A warning originating from the NI-SWITCH driver



