# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

# We are not code genning attributes that have been marked as obsolete prior to the initial
# Python API bindings release
attributes_codegen_method = {
    1050003: { "codegen_method": "no" },  # QUERY_INSTR_STATUS
    1050302: { "codegen_method": "no" },  # SPECIFIC_PREFIX
    1050501: { "codegen_method": "no" },  # ENGINE_MAJOR_VERSION
    1050502: { "codegen_method": "no" },  # ENGINE_MINOR_VERSION
    1050553: { "codegen_method": "no" },  # ENGINE_REVISION
    1050101: { "codegen_method": "no" },  # PRIMARY_ERROR
    1050102: { "codegen_method": "no" },  # SECONDARY_ERROR
    1050103: { "codegen_method": "no" },  # ERROR_ELABORATION
    1050324: { "codegen_method": "no" },  # IO_SESSION_TYPE
    1050322: { "codegen_method": "no" },  # IO_SESSION
    1150001: { "codegen_method": "no" },  # SERIAL_NUMBER_I32
}

attributes_converters = {
    1250004: { 'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
               'type_in_documentation': 'float in seconds or datetime.timedelta', },  # SETTLING_TIME
    1250025: { 'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
               'type_in_documentation': 'float in seconds or datetime.timedelta', },  # SCAN_DELAY
}


