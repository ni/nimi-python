
attribute_docs = {
    '0': '''
    **Device Name** the name of the device, which can be used to open an instrument driver session for that device

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
''',
    '1': '''
    **Device Model** the model of the device (for example, NI PXI-5122)

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
''',
    '2': '''
    **Serial Number** the serial number of the device

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
''',
    '10': '''
    **Slot Number** the slot (for example, in a PXI chassis) in which the device is installed. This attribute can only be queried for PXI devices installed in a chassis that has been properly identified in MAX.

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
''',
    '11': '''
    **Chassis Number** the number of the chassis in which the device is installed. This attribute can only be queried for PXI devices installed in a chassis that has been properly identified in MAX.

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
''',
    '12': '''
    **Bus Number** the bus on which the device has been enumerated.

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
''',
    '13': '''
    **Socket Number** the socket number on which the device has been enumerated

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
''',
    '17': '''
    **PCIEXPRESS_LINK_WIDTH**

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
''',
    '18': '''
    **MAX_PCIEXPRESS_LINK_WIDTH**

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
''',
}
