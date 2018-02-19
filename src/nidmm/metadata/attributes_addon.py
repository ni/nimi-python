# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

# We are not code genning attributes that have been marked as obsolete prior to the initial
# Python API bindings release
attributes_codegen_method = {
    1050302: { "codegen_method": "no" },  # SPECIFIC_PREFIX
    1050003: { "codegen_method": "no" },  # QUERY_INSTR_STATUS
    1050101: { "codegen_method": "no" },  # PRIMARY_ERROR
    1050102: { "codegen_method": "no" },  # SECONDARY_ERROR
    1050103: { "codegen_method": "no" },  # ERROR_ELABORATION
    1050501: { "codegen_method": "no" },  # ENGINE_MAJOR_VERSION
    1050502: { "codegen_method": "no" },  # ENGINE_MINOR_VERSION
    1050553: { "codegen_method": "no" },  # ENGINE_REVISION
    1050321: { "codegen_method": "no" },  # VISA_RM_SESSION
    1050051: { "codegen_method": "no" },  # DEFER_UPDATE
    1050052: { "codegen_method": "no" },  # RETURN_DEFERRED_VALUES
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
}

attributes_converters = {
    1150028: { 'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
               'python_type': 'datetime.timedelta', },  # SETTLE_TIME
    1250005: { 'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
               'python_type': 'datetime.timedelta', },  # TRIGGER_DELAY
    1250303: { 'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
               'python_type': 'datetime.timedelta', },  # SAMPLE_INTERVAL
}


attributes_remove_enum = {
    1250003: { "enum": None                         },  # RESOLUTION, Don't use enum since simple value will do
    1250333: { "enum": None                         },  # POWER_LINE_FREQUENCY, Don't use enum since simple value will do
    1150025: { "enum": None                         },  # CURRENT_SOURCE, Don't use enum since simple value will do
    1150029: { "enum": None                         },  # INPUT_RESISTANCE, Don't use enum since simple value will do
    1150053: { 'enum': None, 'python_type': 'bool', },  # DC_BIAS, Don't use the enum because a bool will do
    1150023: { 'enum': None, 'python_type': 'bool', },  # OFFSET_COMP_OHMS, Don't use the enum because a bool will do
}

