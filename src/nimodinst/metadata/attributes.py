# -*- coding: utf-8 -*-
# This file is generated from NI-ModInst API metadata version 23.3.0f82
attributes = {
    0: {
        'access': 'read only',
        'documentation': {
            'description': 'The name of the device, which can be used to open an instrument driver session for that device'
        },
        'name': 'DEVICE_NAME',
        'type': 'ViString'
    },
    1: {
        'access': 'read only',
        'documentation': {
            'description': 'The model of the device (for example, NI PXI-5122)'
        },
        'name': 'DEVICE_MODEL',
        'type': 'ViString'
    },
    2: {
        'access': 'read only',
        'documentation': {
            'description': 'The serial number of the device'
        },
        'name': 'SERIAL_NUMBER',
        'type': 'ViString'
    },
    10: {
        'access': 'read only',
        'documentation': {
            'description': 'The slot (for example, in a PXI chassis) in which the device is installed. This attribute can only be queried for PXI devices installed in a chassis that has been properly identified in MAX.'
        },
        'name': 'SLOT_NUMBER',
        'type': 'ViInt32'
    },
    11: {
        'access': 'read only',
        'documentation': {
            'description': 'The number of the chassis in which the device is installed. This attribute can only be queried for PXI devices installed in a chassis that has been properly identified in MAX.'
        },
        'name': 'CHASSIS_NUMBER',
        'type': 'ViInt32'
    },
    12: {
        'access': 'read only',
        'documentation': {
            'description': 'The bus on which the device has been enumerated.'
        },
        'name': 'BUS_NUMBER',
        'type': 'ViInt32'
    },
    13: {
        'access': 'read only',
        'documentation': {
            'description': 'The socket number on which the device has been enumerated'
        },
        'name': 'SOCKET_NUMBER',
        'type': 'ViInt32'
    },
    17: {
        'access': 'read only',
        'documentation': {
            'description': '**PCIEXPRESS_LINK_WIDTH**'
        },
        'name': 'PCIEXPRESS_LINK_WIDTH',
        'type': 'ViInt32'
    },
    18: {
        'access': 'read only',
        'documentation': {
            'description': '**MAX_PCIEXPRESS_LINK_WIDTH**'
        },
        'name': 'MAX_PCIEXPRESS_LINK_WIDTH',
        'type': 'ViInt32'
    }
}
