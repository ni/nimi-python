attributes = {
    0: {
        'access': 'read only',
        'channel_based': 'False',
        'resettable': 'No',
        'name': 'DEVICE_NAME',
        'type': 'ViString',
        'enum': None,
        'access': 'read',
        'documentation': {
            'description': 'The name of the device, which can be used to open an instrument driver session for that device',
        },
    },
    1: {
        'access': 'read only',
        'channel_based': 'False',
        'resettable': 'No',
        'name': 'DEVICE_MODEL',
        'type': 'ViString',
        'enum': None,
        'access': 'read',
        'documentation': {
            'description': 'The model of the device (for example, NI PXI-5122)',
        },
    },
    2: {
        'access': 'read only',
        'channel_based': 'False',
        'resettable': 'No',
        'name': 'SERIAL_NUMBER',
        'type': 'ViString',
        'enum': None,
        'access': 'read',
        'documentation': {
            'description': 'The serial number of the device',
        },
    },
    10: {
        'access': 'read only',
        'channel_based': 'False',
        'resettable': 'No',
        'name': 'SLOT_NUMBER',
        'type': 'ViInt32',
        'enum': None,
        'access': 'read',
        'documentation': {
            'description': 'The slot (for example, in a PXI chassis) in which the device is installed. This attribute can only be queried for PXI devices installed in a chassis that has been properly identified in MAX.',
        },
    },
    11: {
        'access': 'read only',
        'channel_based': 'False',
        'resettable': 'No',
        'name': 'CHASSIS_NUMBER',
        'type': 'ViInt32',
        'enum': None,
        'access': 'read',
        'documentation': {
            'description': 'The number of the chassis in which the device is installed. This attribute can only be queried for PXI devices installed in a chassis that has been properly identified in MAX.',
        },
    },
    12: {
        'access': 'read only',
        'channel_based': 'False',
        'resettable': 'No',
        'name': 'BUS_NUMBER',
        'type': 'ViInt32',
        'enum': None,
        'access': 'read',
        'documentation': {
            'description': 'The bus on which the device has been enumerated.',
        },
    },
    13: {
        'access': 'read only',
        'channel_based': 'False',
        'resettable': 'No',
        'name': 'SOCKET_NUMBER',
        'type': 'ViInt32',
        'enum': None,
        'access': 'read',
        'documentation': {
            'description': 'The socket number on which the device has been enumerated',
        },
    },
    17: {
        'access': 'read only',
        'channel_based': 'False',
        'resettable': 'No',
        'name': 'PCIEXPRESS_LINK_WIDTH',
        'type': 'ViInt32',
        'enum': None,
        'access': 'read',
        'documentation': {
            'description': '**PCIEXPRESS_LINK_WIDTH**',
        },
    },
    18: {
        'access': 'read only',
        'channel_based': 'False',
        'resettable': 'No',
        'name': 'MAX_PCIEXPRESS_LINK_WIDTH',
        'type': 'ViInt32',
        'enum': None,
        'access': 'read',
        'documentation': {
            'description': '**MAX_PCIEXPRESS_LINK_WIDTH**',
        },
    },
}


