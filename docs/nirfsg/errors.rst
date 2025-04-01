Exceptions and Warnings
=======================

Error
-----

    .. py:currentmodule:: nirfsg.errors

    .. exception:: Error

        Base exception type that all NI-RFSG exceptions derive from


DriverError
-----------

    .. py:currentmodule:: nirfsg.errors

    .. exception:: DriverError

        An error originating from the NI-RFSG driver


UnsupportedConfigurationError
-----------------------------

    .. py:currentmodule:: nirfsg.errors

    .. exception:: UnsupportedConfigurationError

        An error due to using this module in an usupported platform.

DriverNotInstalledError
-----------------------

    .. py:currentmodule:: nirfsg.errors

    .. exception:: DriverNotInstalledError

        An error due to using this module without the driver runtime installed.

DriverTooOldError
-----------------

    .. py:currentmodule:: nirfsg.errors

    .. exception:: DriverTooOldError

        An error due to using this module with an older version of the NI-RFSG driver runtime.

DriverTooNewError
-----------------

    .. py:currentmodule:: nirfsg.errors

    .. exception:: DriverTooNewError

        An error due to the NI-RFSG driver runtime being too new for this module.

InvalidRepeatedCapabilityError
------------------------------

    .. py:currentmodule:: nirfsg.errors

    .. exception:: InvalidRepeatedCapabilityError

        An error due to an invalid character in a repeated capability


SelfTestError
-------------

    .. py:currentmodule:: nirfsg.errors

    .. exception:: SelfTestError

        An error due to a failed self-test


DriverWarning
-------------

    .. py:currentmodule:: nirfsg.errors

    .. exception:: DriverWarning

        A warning originating from the NI-RFSG driver



