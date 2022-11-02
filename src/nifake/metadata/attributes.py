# -*- coding: utf-8 -*-
# This file is generated from NI-FAKE API metadata version 23.0.0d70
attributes = {
    1000000: {
        'access': 'read-write',
        'documentation': {
            'description': 'An attribute of type bool with read/write access.'
        },
        'lv_property': 'Fake attributes:Read Write Bool',
        'name': 'READ_WRITE_BOOL',
        'type': 'ViBoolean'
    },
    1000001: {
        'access': 'read-write',
        'documentation': {
            'description': 'An attribute of type float with read/write access.'
        },
        'lv_property': 'Fake attributes:Read Write Float',
        'name': 'READ_WRITE_DOUBLE',
        'type': 'ViReal64'
    },
    1000002: {
        'access': 'read-write',
        'documentation': {
            'description': 'An attribute of type string with read/write access.'
        },
        'lv_property': 'Fake attributes:Read Write String',
        'name': 'READ_WRITE_STRING',
        'type': 'ViString'
    },
    1000003: {
        'access': 'read-write',
        'documentation': {
            'description': 'An attribute of type Color with read/write access.'
        },
        'enum': 'Color',
        'lv_property': 'Fake attributes:Read Write Color',
        'name': 'READ_WRITE_COLOR',
        'type': 'ViInt32'
    },
    1000004: {
        'access': 'read-write',
        'documentation': {
            'description': 'An attribute of type integer with read/write access.'
        },
        'lv_property': 'Fake attributes:Read Write Int',
        'name': 'READ_WRITE_INTEGER',
        'type': 'ViInt32'
    },
    1000005: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'An attribute with an enum that is also a float'
        },
        'enum': 'FloatEnum',
        'lv_property': 'Fake attributes:Float enum',
        'name': 'FLOAT_ENUM',
        'type': 'ViReal64'
    },
    1000006: {
        'access': 'read-write',
        'documentation': {
            'description': 'An attribute of type 64-bit integer with read/write access.'
        },
        'lv_property': 'Fake attributes:Read Write long long',
        'name': 'READ_WRITE_INT64',
        'type': 'ViInt64'
    },
    1000007: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'documentation': {
            'description': 'Attribute in seconds'
        },
        'lv_property': 'Fake attributes:Read Write Double with Converter',
        'name': 'READ_WRITE_DOUBLE_WITH_CONVERTER',
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    1000008: {
        'access': 'read-write',
        'attribute_class': 'AttributeViInt32TimeDeltaMilliseconds',
        'documentation': {
            'description': 'Attribute in milliseconds'
        },
        'lv_property': 'Fake attributes:Read Write Int with Converter',
        'name': 'READ_WRITE_INTEGER_WITH_CONVERTER',
        'type': 'ViInt32',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or int in milliseconds'
    },
    1000009: {
        'access': 'read-write',
        'name': 'READ_WRITE_DOUBLE_WITH_REPEATED_CAPABILITY',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1000010: {
        'access': 'read-write',
        'attribute_class': 'AttributeViStringRepeatedCapability',
        'documentation': {
            'description': 'An attribute with read/write access, that represents a repeated capability'
        },
        'lv_property': 'Fake attributes:Read Write String Repeated Capability',
        'name': 'READ_WRITE_STRING_REPEATED_CAPABILITY',
        'supported_rep_caps': [
            'instruments'
        ],
        'type': 'ViString',
        'type_in_documentation': "Any repeated capability type, as defined in nimi-python:\n        - str\n        - str - Comma delimited list\n        - str - Range (using '-' or ':')\n        - int\n        - Basic sequence types (list, tuple, range, slice) of other supported types"
    },
    1000011: {
        'access': 'read-write',
        'enum': 'EnumWithConverter',
        'grpc_enum': None,
        'name': 'READ_WRITE_ENUM_WITH_CONVERTER',
        'type': 'ViInt32'
    }
}
