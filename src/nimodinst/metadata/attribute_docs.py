
attribute_docs = {
    '0': {
        'shortDescription': '''
    The name of the device, which can be used to open an instrument driver session for that device
''',
        'longDescription': '''
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
''',
    },
    '1': {
        'shortDescription': '''
    The model of the device (for example, NI PXI-5122)
''',
        'longDescription': '''
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
''',
    },
    '2': {
        'shortDescription': '''
    The serial number of the device
''',
        'longDescription': '''
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
''',
    },
    '10': {
        'shortDescription': '''
    The slot (for example, in a PXI chassis) in which the device is installed. This attribute can only be queried for PXI devices installed in a chassis that has been properly identified in MAX.
''',
        'longDescription': '''
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
''',
    },
    '11': {
        'shortDescription': '''
    The number of the chassis in which the device is installed. This attribute can only be queried for PXI devices installed in a chassis that has been properly identified in MAX.
''',
        'longDescription': '''
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
''',
    },
    '12': {
        'shortDescription': '''
    The bus on which the device has been enumerated.
''',
        'longDescription': '''
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
''',
    },
    '13': {
        'shortDescription': '''
    The socket number on which the device has been enumerated
''',
        'longDescription': '''
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
''',
    },
    '17': {
        'shortDescription': '''
    **PCIEXPRESS_LINK_WIDTH**
''',
        'longDescription': '''

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
    },
    '18': {
        'shortDescription': '''
    **MAX_PCIEXPRESS_LINK_WIDTH**
''',
        'longDescription': '''

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
    },
}
