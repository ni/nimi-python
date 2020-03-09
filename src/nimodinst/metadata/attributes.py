# -*- coding: utf-8 -*-
# This file is generated from API metadata for NI-ModInst version 255.0.0d4
attributes = {
    0: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'The name of the device, which can be used to open an instrument driver session for that device'
        },
        'name': 'DEVICE_NAME',
        'resettable': False,
        'type': 'ViString'
    },
    1: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'The model of the device (for example, NI PXI-5122)'
        },
        'name': 'DEVICE_MODEL',
        'resettable': False,
        'type': 'ViString'
    },
    2: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'The serial number of the device'
        },
        'name': 'SERIAL_NUMBER',
        'resettable': False,
        'type': 'ViString'
    },
    3: {
        'access': 'read only',
        'channel_based': False,
        'codegen_method': 'no',
        'name': 'IVI_CLASS',
        'resettable': False,
        'type': 'ViString'
    },
    4: {
        'access': 'read only',
        'channel_based': False,
        'codegen_method': 'no',
        'name': 'SPECIFIC_DRIVER_PREFIX',
        'resettable': False,
        'type': 'ViString'
    },
    5: {
        'access': 'read only',
        'channel_based': False,
        'codegen_method': 'no',
        'name': 'DEVICE_GUID',
        'resettable': False,
        'type': 'ViString'
    },
    6: {
        'access': 'read only',
        'channel_based': False,
        'codegen_method': 'no',
        'name': 'DRIVER_VERSION',
        'resettable': False,
        'type': 'ViString'
    },
    10: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'The slot (for example, in a PXI chassis) in which the device is installed. This attribute can only be queried for PXI devices installed in a chassis that has been properly identified in MAX.'
        },
        'name': 'SLOT_NUMBER',
        'resettable': False,
        'type': 'ViInt32'
    },
    11: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'The number of the chassis in which the device is installed. This attribute can only be queried for PXI devices installed in a chassis that has been properly identified in MAX.'
        },
        'name': 'CHASSIS_NUMBER',
        'resettable': False,
        'type': 'ViInt32'
    },
    12: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'The bus on which the device has been enumerated.'
        },
        'name': 'BUS_NUMBER',
        'resettable': False,
        'type': 'ViInt32'
    },
    13: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'The socket number on which the device has been enumerated'
        },
        'name': 'SOCKET_NUMBER',
        'resettable': False,
        'type': 'ViInt32'
    },
    14: {
        'access': 'read only',
        'channel_based': False,
        'codegen_method': 'no',
        'name': 'PRODUCT_CODE',
        'resettable': False,
        'type': 'ViInt32'
    },
    15: {
        'access': 'read only',
        'channel_based': False,
        'codegen_method': 'no',
        'name': 'PXI_SEGMENT_NUMBER',
        'resettable': False,
        'type': 'ViInt32'
    },
    16: {
        'access': 'read only',
        'channel_based': False,
        'codegen_method': 'no',
        'name': 'DEVICE_HANDLE',
        'resettable': False,
        'type': 'ViInt32'
    },
    17: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': '**PCIEXPRESS_LINK_WIDTH**'
        },
        'name': 'PCIEXPRESS_LINK_WIDTH',
        'resettable': False,
        'type': 'ViInt32'
    },
    18: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': '**MAX_PCIEXPRESS_LINK_WIDTH**'
        },
        'name': 'MAX_PCIEXPRESS_LINK_WIDTH',
        'resettable': False,
        'type': 'ViInt32'
    },
    19: {
        'access': 'read only',
        'channel_based': False,
        'codegen_method': 'no',
        'name': 'NUMBER_REGISTERED_DEVICES',
        'resettable': False,
        'type': 'ViInt32'
    },
    20: {
        'access': 'read only',
        'channel_based': False,
        'codegen_method': 'no',
        'name': 'FUNCTION_NUMBER',
        'resettable': False,
        'type': 'ViInt32'
    },
    21: {
        'access': 'read only',
        'channel_based': False,
        'codegen_method': 'no',
        'name': 'SESSION_TYPE',
        'resettable': False,
        'type': 'ViInt32'
    }
}
