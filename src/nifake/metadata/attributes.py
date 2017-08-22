# -*- coding: utf-8 -*-
# This file contains attribute metadata for NI-FAKE, a fake driver
# whose purpose is to test the nimi-python codegenerator.

#TODO(marcoskirsch): We need to expand this metadata, possibly programmatically, to have every combination of:
# (data type) * (access) * (channel based)
# For now, add a handful by hand as a starting point.
#
# Datatypes are:
#     ViInt32
#     ViInt64
#     ViReal64
#     ViString
#     ViBoolean
#     ViSession
#     ViAddr

attributes = {
    1000000: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Fake attributes:Read Write Bool',
        'name': 'READ_WRITE_BOOL',
        'resettable': 'No',
        'short_description': '''An attribute of type bool with read/write access.''',
        'type': 'ViBoolean',
    },
    1000001: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Fake attributes:Read Write Float',
        'name': 'READ_WRITE_DOUBLE',
        'resettable': 'No',
        'short_description': '''An attribute of type float with read/write access.''',
        'type': 'ViReal64',
    },
    1000002: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Fake attributes:Read Write String',
        'name': 'READ_WRITE_STRING',
        'resettable': 'No',
        'short_description': '''An attribute of type string with read/write access.''',
        'type': 'ViString',
    },
    1000003: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'Color',
        'lv_property': 'Fake attributes:Read Write Color',
        'name': 'READ_WRITE_COLOR',
        'resettable': 'No',
        'short_description': '''An attribute of type Color with read/write access.''',
        'type': 'ViInt32',
    },
}
