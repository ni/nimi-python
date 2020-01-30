# -*- coding: utf-8 -*-
# This file is generated from NI-FAKE API metadata version 1.2.0d4
attributes = {
    1000000: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'An attribute of type bool with read/write access.'
        },
        'lv_property': 'Fake attributes:Read Write Bool',
        'name': 'READ_WRITE_BOOL',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1000001: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'An attribute of type float with read/write access.'
        },
        'lv_property': 'Fake attributes:Read Write Float',
        'name': 'READ_WRITE_DOUBLE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1000002: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'An attribute of type string with read/write access.'
        },
        'lv_property': 'Fake attributes:Read Write String',
        'name': 'READ_WRITE_STRING',
        'resettable': False,
        'type': 'ViString'
    },
    1000003: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'An attribute of type Color with read/write access.'
        },
        'enum': 'Color',
        'lv_property': 'Fake attributes:Read Write Color',
        'name': 'READ_WRITE_COLOR',
        'resettable': False,
        'type': 'ViInt32'
    },
    1000004: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'An attribute of type integer with read/write access.'
        },
        'lv_property': 'Fake attributes:Read Write Int',
        'name': 'READ_WRITE_INTEGER',
        'resettable': True,
        'type': 'ViInt32'
    },
    1000005: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'An attribute with an enum that is also a float'
        },
        'enum': 'FloatEnum',
        'lv_property': 'Fake attributes:Float enum',
        'name': 'FLOAT_ENUM',
        'resettable': False,
        'type': 'ViReal64'
    },
    1000006: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'An attribute of type 64-bit integer with read/write access.'
        },
        'lv_property': 'Fake attributes:Read Write long long',
        'name': 'READ_WRITE_INT64',
        'resettable': False,
        'type': 'ViInt64'
    },
    1000007: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'channel_based': False,
        'documentation': {
            'description': 'Attribute in seconds'
        },
        'lv_property': 'Fake attributes:Read Write Double with Converter',
        'name': 'READ_WRITE_DOUBLE_WITH_CONVERTER',
        'resettable': False,
        'type': 'ViReal64',
        'type_in_documentation': 'float in seconds or datetime.timedelta'
    },
    1000008: {
        'access': 'read-write',
        'attribute_class': 'AttributeViInt32TimeDeltaMilliseconds',
        'channel_based': False,
        'documentation': {
            'description': 'Attribute in milliseconds'
        },
        'lv_property': 'Fake attributes:Read Write Int with Converter',
        'name': 'READ_WRITE_INTEGER_WITH_CONVERTER',
        'resettable': False,
        'type': 'ViInt32',
        'type_in_documentation': 'float in seconds or datetime.timedelta'
    },
    1000009: {
        'access': 'read-write',
        'channel_based': True,
        'name': 'READ_WRITE_DOUBLE_WITH_REPEATED_CAPABILITY',
        'resettable': False,
        'type': 'ViReal64'
    }
}
