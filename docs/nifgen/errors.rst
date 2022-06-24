Exceptions and Warnings
=======================

Error
-----

    .. py:currentmodule:: nifgen.errors

    .. exception:: Error

        Base exception type that all NI-FGEN exceptions derive from


DriverError
-----------

    .. py:currentmodule:: nifgen.errors

    .. exception:: DriverError

        An error originating from the NI-FGEN driver


UnsupportedConfigurationError
-----------------------------

    .. py:currentmodule:: nifgen.errors

    .. exception:: UnsupportedConfigurationError

        An error due to using this module in an usupported platform.

DriverNotInstalledError
-----------------------

    .. py:currentmodule:: nifgen.errors

    .. exception:: DriverNotInstalledError

        An error due to using this module without the driver runtime installed.

DriverTooOldError
-----------------

    .. py:currentmodule:: nifgen.errors

    .. exception:: DriverTooOldError

        An error due to using this module with an older version of the driver runtime.

DriverTooNewError
-----------------

    .. py:currentmodule:: nifgen.errors

    .. exception:: DriverTooNewError

        An error due to the driver runtime being too new for the Python module.

InvalidRepeatedCapabilityError
------------------------------

    .. py:currentmodule:: nifgen.errors

    .. exception:: InvalidRepeatedCapabilityError

        An error due to an invalid character in a repeated capability


SelfTestError
-------------

    .. py:currentmodule:: nifgen.errors

    .. exception:: SelfTestError

        An error due to a failed self-test


DriverWarning
-------------

    .. py:currentmodule:: nifgen.errors

    .. exception:: DriverWarning

        A warning originating from the NI-FGEN driver



