Exceptions and Warnings
=======================

Error
-----

    .. py:currentmodule:: nirfsa.errors

    .. exception:: Error

        Base exception type that all NI-RFSA exceptions derive from


DriverError
-----------

    .. py:currentmodule:: nirfsa.errors

    .. exception:: DriverError

        An error originating from the NI-RFSA driver


UnsupportedConfigurationError
-----------------------------

    .. py:currentmodule:: nirfsa.errors

    .. exception:: UnsupportedConfigurationError

        An error due to using this module in an usupported platform.

DriverNotInstalledError
-----------------------

    .. py:currentmodule:: nirfsa.errors

    .. exception:: DriverNotInstalledError

        An error due to using this module without the driver runtime installed.

DriverTooOldError
-----------------

    .. py:currentmodule:: nirfsa.errors

    .. exception:: DriverTooOldError

        An error due to using this module with an older version of the NI-RFSA driver runtime.

DriverTooNewError
-----------------

    .. py:currentmodule:: nirfsa.errors

    .. exception:: DriverTooNewError

        An error due to the NI-RFSA driver runtime being too new for this module.

InvalidRepeatedCapabilityError
------------------------------

    .. py:currentmodule:: nirfsa.errors

    .. exception:: InvalidRepeatedCapabilityError

        An error due to an invalid character in a repeated capability


SelfTestError
-------------

    .. py:currentmodule:: nirfsa.errors

    .. exception:: SelfTestError

        An error due to a failed self-test


DriverWarning
-------------

    .. py:currentmodule:: nirfsa.errors

    .. exception:: DriverWarning

        A warning originating from the NI-RFSA driver



