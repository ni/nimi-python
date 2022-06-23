Exceptions and Warnings
=======================

Error
-----

    .. py:currentmodule:: nidcpower.errors

    .. exception:: Error

        Base exception type that all NI-DCPower exceptions derive from


DriverError
-----------

    .. py:currentmodule:: nidcpower.errors

    .. exception:: DriverError

        An error originating from the NI-DCPower driver


UnsupportedConfigurationError
-----------------------------

    .. py:currentmodule:: nidcpower.errors

    .. exception:: UnsupportedConfigurationError

        An error due to using this module in an usupported platform.

DriverNotInstalledError
-----------------------

    .. py:currentmodule:: nidcpower.errors

    .. exception:: DriverNotInstalledError

        An error due to using this module without the driver runtime installed.

DriverTooOldError
-----------------

    .. py:currentmodule:: nidcpower.errors

    .. exception:: DriverTooOldError

        An error due to using this module with an older version of the driver runtime.

DriverTooNewError
-----------------

    .. py:currentmodule:: nidcpower.errors

    .. exception:: DriverTooNewError

        An error due to the driver runtime being too new for the Python module.

InvalidRepeatedCapabilityError
------------------------------

    .. py:currentmodule:: nidcpower.errors

    .. exception:: InvalidRepeatedCapabilityError

        An error due to an invalid character in a repeated capability


SelfTestError
-------------

    .. py:currentmodule:: nidcpower.errors

    .. exception:: SelfTestError

        An error due to a failed self-test


DriverWarning
-------------

    .. py:currentmodule:: nidcpower.errors

    .. exception:: DriverWarning

        A warning originating from the NI-DCPower driver



