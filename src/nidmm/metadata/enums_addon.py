# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

# We are not code genning enums that have been marked as obsolete prior to the initial
# Python API bindings release
# We also do not codegen enums associated with P2P or External Calibration since neither 
# are supported in Python
enums_codegen_method = {
}

enums_additional_enums = {
    'DigitsResolution': {},  # Enum metadata actually contains constants. Also need to remove to generate valid code
    'PowerlineFrequency': {}, # Enum metadata actually contains constants.
    'CurrentSource': {}, # Enum metadata actually contains constants.
    'InputResistance': {}, # Enum metadata actually contains constants.
    'DCBias': {},  # Delete because boolean values only
    'OffsetCompensatedOhms': {},  # Delete because boolean values only
}

