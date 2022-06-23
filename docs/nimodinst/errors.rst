Exceptions and Warnings
=======================

Error
-----

    .. py:currentmodule:: nimodinst.errors

    .. exception:: Error

        Base exception type that all NI-ModInst exceptions derive from


DriverError
-----------

    .. py:currentmodule:: nimodinst.errors

    .. exception:: DriverError

        An error originating from the NI-ModInst driver


UnsupportedConfigurationError
-----------------------------

    .. py:currentmodule:: nimodinst.errors

    .. exception:: UnsupportedConfigurationError

        An error due to using this module in an usupported platform.

DriverNotInstalledError
-----------------------

    .. py:currentmodule:: nimodinst.errors

    .. exception:: DriverNotInstalledError

        An error due to using this module without the driver runtime installed.

DriverTooOldError
-----------------

    .. py:currentmodule:: nimodinst.errors

    .. exception:: DriverTooOldError

        An error due to using this module with an older version of the driver runtime.

DriverTooNewError
-----------------

    .. py:currentmodule:: nimodinst.errors

    .. exception:: DriverTooNewError

        An error due to the driver runtime being too new for the Python module.

DriverWarning
-------------

    .. py:currentmodule:: nimodinst.errors

    .. exception:: DriverWarning

        A warning originating from the NI-ModInst driver



