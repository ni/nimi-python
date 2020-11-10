.. py:module:: nimodinst

Session
=======

.. py:class:: Session(self, driver: str)

    

    Creates a handle to a list of installed devices supported by the
    specified driver. Call this method and pass in the name of a National
    Instruments instrument driver, such as "NI-SCOPE". This method
    searches the system and constructs a list of all the installed devices
    that are supported by that driver, and then returns both a handle to
    this list and the number of devices found. The handle is used with other
    methods to query for properties such as device name and model, and to
    safely discard the list when finished. Note This handle reflects the
    system state when the handle is created (that is, when you call this
    method. If you remove devices from the system or rename them in
    Measurement & Automation Explorer (MAX), this handle may not refer to an
    accurate list of devices. You should destroy the handle using
    :py:meth:`nimodinst.Session._close_installed_devices_session` and create a new handle using
    this method.

    



    :param driver:
        

        A string specifying the driver whose supported devices you want to find.
        This string is not case-sensitive. Some examples are: NI-SCOPE niScope
        NI-FGEN niFgen NI-HSDIO niHSDIO NI-DMM niDMM NI-SWITCH niSwitch Note If
        you use the empty string for this parameter, NI-ModInst creates a list
        of all Modular Instruments devices installed in the system.

        


    :type driver: str


Methods
=======

close
-----

    .. py:currentmodule:: nimodinst.Session

    .. py:method:: close()

            Cleans up the NI-ModInst session created by a call to
            :py:meth:`nimodinst.Session._open_installed_devices_session`. Call this method when you are
            finished using the session handle and do not use this handle again.

            

            .. note:: This method is not needed when using the session context manager




Properties
==========

bus_number
----------

    .. py:attribute:: bus_number

        The bus on which the device has been enumerated.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIMODINST_ATTR_BUS_NUMBER**

chassis_number
--------------

    .. py:attribute:: chassis_number

        The number of the chassis in which the device is installed. This property can only be queried for PXI devices installed in a chassis that has been properly identified in MAX.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIMODINST_ATTR_CHASSIS_NUMBER**

device_model
------------

    .. py:attribute:: device_model

        The model of the device (for example, NI PXI-5122)

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIMODINST_ATTR_DEVICE_MODEL**

device_name
-----------

    .. py:attribute:: device_name

        The name of the device, which can be used to open an instrument driver session for that device

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIMODINST_ATTR_DEVICE_NAME**

max_pciexpress_link_width
-------------------------

    .. py:attribute:: max_pciexpress_link_width

        **MAX_PCIEXPRESS_LINK_WIDTH**

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIMODINST_ATTR_MAX_PCIEXPRESS_LINK_WIDTH**

pciexpress_link_width
---------------------

    .. py:attribute:: pciexpress_link_width

        **PCIEXPRESS_LINK_WIDTH**

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIMODINST_ATTR_PCIEXPRESS_LINK_WIDTH**

serial_number
-------------

    .. py:attribute:: serial_number

        The serial number of the device

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIMODINST_ATTR_SERIAL_NUMBER**

slot_number
-----------

    .. py:attribute:: slot_number

        The slot (for example, in a PXI chassis) in which the device is installed. This property can only be queried for PXI devices installed in a chassis that has been properly identified in MAX.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIMODINST_ATTR_SLOT_NUMBER**

socket_number
-------------

    .. py:attribute:: socket_number

        The socket number on which the device has been enumerated

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIMODINST_ATTR_SOCKET_NUMBER**


.. contents:: Session


