# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

# We are not code genning attributes that have been marked as obsolete prior to the initial
# Python API bindings release
attributes_codegen_method = {
    1150001: { "codegen_method": "no" },  # SERIAL_NUMBER_I32
    1050501: { "codegen_method": "no" },  # ENGINE_MAJOR_VERSION - IVI Attribute - #824
    1050502: { "codegen_method": "no" },  # ENGINE_MINOR_VERSION - IVI Attribute - #824
    1050553: { "codegen_method": "no" },  # ENGINE_REVISION - IVI Attribute - #824
    1050101: { "codegen_method": "no" },  # PRIMARY_ERROR - IVI Attribute - #824
    1050102: { "codegen_method": "no" },  # SECONDARY_ERROR - IVI Attribute - #824
    1050103: { "codegen_method": "no" },  # ERROR_ELABORATION - IVI Attribute - #824
    1050324: { "codegen_method": "no" },  # IO_SESSION_TYPE - IVI Attribute - #824
    1050322: { "codegen_method": "no" },  # IO_SESSION - IVI Attribute - #824
    1050401: { "codegen_method": "no" },  # GROUP_CAPABILITIES - IVI Attribute - #824
    1050021: { "codegen_method": "no" },  # INTERCHANGE_CHECK - IVI Attribute - #824
    1050002: { "codegen_method": "no" },  # RANGE_CHECK - IVI Attribute - #824
    1050006: { "codegen_method": "no" },  # RECORD_COERCIONS - IVI Attribute - #824
    1050515: { "codegen_method": "no" },  # SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION - IVI Attribute - #824
    1050516: { "codegen_method": "no" },  # SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION - IVI Attribute - #824
    1050003: { "codegen_method": "no" },  # QUERY_INSTRUMENT_STATUS - IVI Attribute - #824
    1050004: { "codegen_method": "no" },  # CACHE - IVI Attribute - #824
    1050302: { "codegen_method": "no" },  # SPECIFIC_DRIVER_PREFIX - IVI Attribute - #824
    1150009: { "codegen_method": "no" },  # CABLED_MODULE_SCAN_ADVANCED_BUS - EOL HW only - #881
    1150008: { "codegen_method": "no" },  # CABLED_MODULE_TRIGGER_BUS - EOL HW only - #881
    1150007: { "codegen_method": "no" },  # MASTER_SLAVE_SCAN_ADVANCED_BUS - EOL HW only - #881
    1150006: { "codegen_method": "no" },  # MASTER_SLAVE_TRIGGER_BUS - EOL HW only - #881
    1150012: { "codegen_method": "no" },  # PARSED_SCAN_LIST - EOL HW only - #881
    1150005: { "codegen_method": "no" },  # TRIGGER_MODE - EOL HW only - #881
}

attributes_converters = {
    1250004: { 'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
               'type_in_documentation': 'float in seconds or datetime.timedelta', },  # SETTLING_TIME
    1250025: { 'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
               'type_in_documentation': 'float in seconds or datetime.timedelta', },  # SCAN_DELAY
}


