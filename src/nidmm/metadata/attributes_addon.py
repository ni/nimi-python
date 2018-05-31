# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

# We are not code genning attributes that have been marked as obsolete prior to the initial
# Python API bindings release
attributes_codegen_method = {
    1150008: { "codegen_method": "no" },  # START_TRIGGER
    1150009: { "codegen_method": "no" },  # START_TRIG_SLOPE
    1150011: { "codegen_method": "no" },  # SAMPLE_TRIGGER_DELAY
    1150012: { "codegen_method": "no" },  # OLD_TRIGGER_MODEL
    1150004: { "codegen_method": "no" },  # CHAN_NAMES
    1150001: { "codegen_method": "no" },  # ID_QUERY_RESPONSE
    1150005: { "codegen_method": "no" },  # AI_NUM_CHANNELS
    1150006: { "codegen_method": "no" },  # FILTER_NOTCH
    1150007: { "codegen_method": "no" },  # CONVER_PER_SAMPLE
    1150031: { "codegen_method": "no" },  # SAMPLE_DELAY_MODE
    1050401: { "codegen_method": "no" },  # GROUP_CAPABILITIES - IVI Attribute - #824
    1050021: { "codegen_method": "no" },  # INTERCHANGE_CHECK - IVI Attribute - #824
    1050002: { "codegen_method": "no" },  # RANGE_CHECK - IVI Attribute - #824
    1050006: { "codegen_method": "no" },  # RECORD_COERCIONS - IVI Attribute - #824
    1050515: { "codegen_method": "no" },  # SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION - IVI Attribute - #824
    1050516: { "codegen_method": "no" },  # SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION - IVI Attribute - #824
    1050302: { "codegen_method": "no" },  # SPECIFIC_PREFIX - IVI Attribute - #824
    1050003: { "codegen_method": "no" },  # QUERY_INSTR_STATUS - IVI Attribute - #824
    1050101: { "codegen_method": "no" },  # PRIMARY_ERROR - IVI Attribute - #824
    1050102: { "codegen_method": "no" },  # SECONDARY_ERROR - IVI Attribute - #824
    1050103: { "codegen_method": "no" },  # ERROR_ELABORATION - IVI Attribute - #824
    1050501: { "codegen_method": "no" },  # ENGINE_MAJOR_VERSION - IVI Attribute - #824
    1050502: { "codegen_method": "no" },  # ENGINE_MINOR_VERSION - IVI Attribute - #824
    1050553: { "codegen_method": "no" },  # ENGINE_REVISION - IVI Attribute - #824
    1050321: { "codegen_method": "no" },  # VISA_RM_SESSION - IVI Attribute - #824
    1050051: { "codegen_method": "no" },  # DEFER_UPDATE - IVI Attribute - #824
    1050052: { "codegen_method": "no" },  # RETURN_DEFERRED_VALUES - IVI Attribute - #824
    1050004: { "codegen_method": "no" },  # CACHE - IVI Attribute - #824
    1150034: { "codegen_method": "no" },  # LATENCY - EOL hardware only - #875
    1150003: { "codegen_method": "no" },  # SHUNT_VALUE - EOL hardware only - #875
    1150002: { "codegen_method": "no" },  # MEAS_DEST_SLOPE - EOL hardware only - #875
    1150010: { "codegen_method": "no" },  # SAMPLE_TRIGGER_SLOPE - EOL hardware only - #875
    1250334: { "codegen_method": "no" },  # TRIGGER_SLOPE - EOL hardware only - #875
}

attributes_converters = {
    1150028: { 'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
               'type_in_documentation': 'float in seconds or datetime.timedelta', },  # SETTLE_TIME
    1250005: { 'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
               'type_in_documentation': 'float in seconds or datetime.timedelta', },  # TRIGGER_DELAY
    1250303: { 'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
               'type_in_documentation': 'float in seconds or datetime.timedelta', },  # SAMPLE_INTERVAL
}

attributes_name = {
    1150044: { 'name': 'FREQ_VOLTAGE_AUTO_RANGE', },  # extracted metadata has incorrect name #874, internal NI CAR 699520
}

attributes_remove_enum = {
    1250003: { "enum": None                         },  # RESOLUTION, Don't use enum since simple value will do
    1250333: { "enum": None                         },  # POWER_LINE_FREQUENCY, Don't use enum since simple value will do
    1150025: { "enum": None                         },  # CURRENT_SOURCE, Don't use enum since simple value will do
    1150029: { "enum": None                         },  # INPUT_RESISTANCE, Don't use enum since simple value will do
    1150053: { 'enum': None, 'python_type': 'bool', },  # DC_BIAS, Don't use the enum because a bool will do
    1150023: { 'enum': None, 'python_type': 'bool', },  # OFFSET_COMP_OHMS, Don't use the enum because a bool will do
}

