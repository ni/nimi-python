# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

# We are not code genning attributes that have been marked as obsolete prior to the initial
# Python API bindings release
attributes_codegen_method = {
}

attributes_converters = {
}

attributes_name = {
}

attributes_remove_enum = {
}

# I need to have fake attributes so that we do not get errors from flake8 as all other drivers are expected to use attributes.
attributes_additional_attributes = {
    1000000: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Attributes Not Supported',
        'name': 'NOT_SUPPORTED',
        'resettable': 'No',
        'type': 'ViBoolean',
        'documentation': {
            'description':'An attribute of type bool with read/write access.',
        },
    },
}
