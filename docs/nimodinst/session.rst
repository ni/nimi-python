NI-ModInst Session
==================

A NI-ModInst session to get device information

Attributes
----------

BUS_NUMBER
~~~~~~~~~~


    The bus on which the device has been enumerated.

    The following table lists the characteristics of this property.

    +------------------+-------------------------+
    | Characteristic   | Value                   |
    +------------------+-------------------------+
    | Datatype         | 32-bit signed integer   |
    +------------------+-------------------------+
    | Permissions      | Read/Write              |
    +------------------+-------------------------+
    | High Level VI    | N/A                     |
    +------------------+-------------------------+
    | Channel Based    | False                   |
    +------------------+-------------------------+
    | Resettable       | No                      |
    +------------------+-------------------------+


CHASSIS_NUMBER
~~~~~~~~~~~~~~


    The number of the chassis in which the device is installed. This attribute can only be queried for PXI devices installed in a chassis that has been properly identified in MAX.

    The following table lists the characteristics of this property.

    +------------------+-------------------------+
    | Characteristic   | Value                   |
    +------------------+-------------------------+
    | Datatype         | 32-bit signed integer   |
    +------------------+-------------------------+
    | Permissions      | Read/Write              |
    +------------------+-------------------------+
    | High Level VI    | N/A                     |
    +------------------+-------------------------+
    | Channel Based    | False                   |
    +------------------+-------------------------+
    | Resettable       | No                      |
    +------------------+-------------------------+


DEVICE_MODEL
~~~~~~~~~~~~


    The model of the device (for example, NI PXI-5122)

    The following table lists the characteristics of this property.

    +------------------+-------------+
    | Characteristic   | Value       |
    +------------------+-------------+
    | Datatype         | string      |
    +------------------+-------------+
    | Permissions      | Read Only   |
    +------------------+-------------+
    | High Level VI    | N/A         |
    +------------------+-------------+
    | Channel Based    | False       |
    +------------------+-------------+
    | Resettable       | No          |
    +------------------+-------------+


DEVICE_NAME
~~~~~~~~~~~


    The name of the device, which can be used to open an instrument driver session for that device

    The following table lists the characteristics of this property.

    +------------------+-------------+
    | Characteristic   | Value       |
    +------------------+-------------+
    | Datatype         | string      |
    +------------------+-------------+
    | Permissions      | Read Only   |
    +------------------+-------------+
    | High Level VI    | N/A         |
    +------------------+-------------+
    | Channel Based    | False       |
    +------------------+-------------+
    | Resettable       | No          |
    +------------------+-------------+


MAX_PCIEXPRESS_LINK_WIDTH
~~~~~~~~~~~~~~~~~~~~~~~~~



    The following table lists the characteristics of this property.

    +------------------+-------------------------+
    | Characteristic   | Value                   |
    +------------------+-------------------------+
    | Datatype         | 32-bit signed integer   |
    +------------------+-------------------------+
    | Permissions      | Read/Write              |
    +------------------+-------------------------+
    | High Level VI    | N/A                     |
    +------------------+-------------------------+
    | Channel Based    | False                   |
    +------------------+-------------------------+
    | Resettable       | No                      |
    +------------------+-------------------------+


PCIEXPRESS_LINK_WIDTH
~~~~~~~~~~~~~~~~~~~~~



    The following table lists the characteristics of this property.

    +------------------+-------------------------+
    | Characteristic   | Value                   |
    +------------------+-------------------------+
    | Datatype         | 32-bit signed integer   |
    +------------------+-------------------------+
    | Permissions      | Read/Write              |
    +------------------+-------------------------+
    | High Level VI    | N/A                     |
    +------------------+-------------------------+
    | Channel Based    | False                   |
    +------------------+-------------------------+
    | Resettable       | No                      |
    +------------------+-------------------------+


SERIAL_NUMBER
~~~~~~~~~~~~~


    The serial number of the device

    The following table lists the characteristics of this property.

    +------------------+-------------+
    | Characteristic   | Value       |
    +------------------+-------------+
    | Datatype         | string      |
    +------------------+-------------+
    | Permissions      | Read Only   |
    +------------------+-------------+
    | High Level VI    | N/A         |
    +------------------+-------------+
    | Channel Based    | False       |
    +------------------+-------------+
    | Resettable       | No          |
    +------------------+-------------+


SLOT_NUMBER
~~~~~~~~~~~


    The slot (for example, in a PXI chassis) in which the device is installed. This attribute can only be queried for PXI devices installed in a chassis that has been properly identified in MAX.

    The following table lists the characteristics of this property.

    +------------------+-------------------------+
    | Characteristic   | Value                   |
    +------------------+-------------------------+
    | Datatype         | 32-bit signed integer   |
    +------------------+-------------------------+
    | Permissions      | Read/Write              |
    +------------------+-------------------------+
    | High Level VI    | N/A                     |
    +------------------+-------------------------+
    | Channel Based    | False                   |
    +------------------+-------------------------+
    | Resettable       | No                      |
    +------------------+-------------------------+


SOCKET_NUMBER
~~~~~~~~~~~~~


    The socket number on which the device has been enumerated

    The following table lists the characteristics of this property.

    +------------------+-------------------------+
    | Characteristic   | Value                   |
    +------------------+-------------------------+
    | Datatype         | 32-bit signed integer   |
    +------------------+-------------------------+
    | Permissions      | Read/Write              |
    +------------------+-------------------------+
    | High Level VI    | N/A                     |
    +------------------+-------------------------+
    | Channel Based    | False                   |
    +------------------+-------------------------+
    | Resettable       | No                      |
    +------------------+-------------------------+


