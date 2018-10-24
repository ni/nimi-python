# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

# We are not code genning attributes that have been marked as obsolete prior to the initial
# Python API bindings release

attributes_codegen_method = {
    1050401: { "codegen_method": "no"      },  # GROUP_CAPABILITIES - IVI Attribute - #824
    1050021: { "codegen_method": "no"      },  # INTERCHANGE_CHECK - IVI Attribute - #824
    1050002: { "codegen_method": "no"      },  # RANGE_CHECK - IVI Attribute - #824
    1050006: { "codegen_method": "no"      },  # RECORD_COERCIONS - IVI Attribute - #824
    1050515: { "codegen_method": "no"      },  # SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION - IVI Attribute - #824
    1050516: { "codegen_method": "no"      },  # SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION - IVI Attribute - #824
    1050004: { "codegen_method": "no"      },  # CACHE - IVI Attribute - #824
    1150074: { "codegen_method": "private" },  # ACTIVE_ADVANCED_SEQUENCE - Advanced Sequence Attribute - #793
    1150075: { "codegen_method": "private" },  # ACTIVE_ADVANCED_SEQUENCE_STEP - Advanced Sequence Attribute - #793
    1150035: { "codegen_method": "no"      },  # DIGITAL_EDGE_MEASURE_TRIGGER_EDGE - Backplane only, always falling edge - #860
    1150096: { "codegen_method": "no"      },  # DIGITAL_EDGE_PULSE_TRIGGER_EDGE - Backplane only, always falling edge - #860
    1150027: { "codegen_method": "no"      },  # DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_EDGE - Backplane only, always falling edge - #860
    1150031: { "codegen_method": "no"      },  # DIGITAL_EDGE_SOURCE_TRIGGER_EDGE - Backplane only, always falling edge - #860
    1150022: { "codegen_method": "no"      },  # DIGITAL_EDGE_START_TRIGGER_EDGE - Backplane only, always falling edge - #860
}

attributes_converters = {
    1150046: { 'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
               'type_in_documentation': 'float in seconds or datetime.timedelta', },  # MEASURE_COMPLETE_EVENT_DELAY
    1150065: { 'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
               'type_in_documentation': 'float in seconds or datetime.timedelta', },  # MEASURE_RECORD_DELTA_TIME
    1150093: { 'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
               'type_in_documentation': 'float in seconds or datetime.timedelta', },  # PULSE_ON_TIME
    1150094: { 'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
               'type_in_documentation': 'float in seconds or datetime.timedelta', },  # PULSE_OFF_TIME
    1150051: { 'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
               'type_in_documentation': 'float in seconds or datetime.timedelta', },  # SOURCE_DELAY
}

attributes_enums = {
    1150020: { "enum": None           },  # POWER_LINE_FREQUENCY, Don't use the enum because a number will do
    1050002: { "enum": None           },  # RANGE_CHECK, Don't use the enum because a bool will do
    1050003: { "enum": None           },  # QUERY_INSTRUMENT_STATUS, Don't use the enum because a bool will do
    1050004: { "enum": None           },  # CACHE, Don't use the enum because a bool will do
    1050005: { "enum": None           },  # SIMULATE, Don't use the enum because a bool will do
    1050006: { "enum": None           },  # RECORD_COERCIONS, Don't use the enum because a bool will do
    1050021: { "enum": None           },  # INTERCHANGE_CHECK, Don't use the enum because a bool will do
    1150002: { "enum": None           },  # AUXILIARY_POWER_SOURCE_AVAILABLE, Don't use the enum because a bool will do
    1150006: { "enum": None           },  # RESET_AVERAGE_BEFORE_MEASUREMENT, Don't use the enum because a bool will do
    1150007: { "enum": None           },  # OVERRANGING_ENABLED, Don't use the enum because a bool will do
    1150060: { "enum": None           },  # OUTPUT_CONNECTED, Don't use the enum because a bool will do
    1150064: { "enum": None           },  # MEASURE_RECORD_LENGTH_IS_FINITE, Don't use the enum because a bool will do
    1150078: { "enum": None           },  # SEQUENCE_LOOP_COUNT_IS_FINITE, Don't use the enum because a bool will do
    1150105: { "enum": None           },  # INTERLOCK_INPUT_OPEN, Don't use the enum because a bool will do
    1250002: { "enum": None           },  # OVP_ENABLED, Don't use the enum because a bool will do
    1250006: { "enum": None           },  # OUTPUT_ENABLED, Don't use the enum because a bool will do
}

# If the associated enum represents boolean values only, disconnect
attributes_remove_enum = {
    1150020: { "enum": None,                        },  # POWER_LINE_FREQUENCY, Don't use enum since simple value will do
    1150016: { 'enum': None, 'python_type': 'bool', },  # CURRENT_LIMIT_AUTORANGE, Don't use the enum because a bool will do
    1150017: { 'enum': None, 'python_type': 'bool', },  # CURRENT_LEVEL_AUTORANGE, Don't use the enum because a bool will do
    1150015: { 'enum': None, 'python_type': 'bool', },  # VOLTAGE_LEVEL_AUTORANGE, Don't use the enum because a bool will do
    1150018: { 'enum': None, 'python_type': 'bool', },  # CURRENT_LIMIT_AUTORANGE, Don't use the enum because a bool will do
}
