# -*- coding: utf-8 -*-
# This file is generated from NI-Digital Pattern Driver API metadata version 19.0.0a0
attributes = {
    1050002: {
        'access': 'read-write',
        'channel_based': False,
        'name': 'RANGE_CHECK',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1050003: {
        'access': 'read-write',
        'channel_based': False,
        'name': 'QUERY_INSTRUMENT_STATUS',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1050004: {
        'access': 'read-write',
        'channel_based': False,
        'name': 'CACHE',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1050005: {
        'access': 'read only',
        'channel_based': False,
        'name': 'SIMULATE',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1050006: {
        'access': 'read-write',
        'channel_based': False,
        'name': 'RECORD_COERCIONS',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1050007: {
        'access': 'read only',
        'channel_based': False,
        'name': 'DRIVER_SETUP',
        'resettable': False,
        'type': 'ViString'
    },
    1050021: {
        'access': 'read-write',
        'channel_based': False,
        'name': 'INTERCHANGE_CHECK',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1050203: {
        'access': 'read only',
        'channel_based': False,
        'name': 'CHANNEL_COUNT',
        'resettable': False,
        'type': 'ViInt32'
    },
    1050302: {
        'access': 'read only',
        'channel_based': False,
        'name': 'SPECIFIC_DRIVER_PREFIX',
        'resettable': False,
        'type': 'ViString'
    },
    1050304: {
        'access': 'read only',
        'channel_based': False,
        'name': 'IO_RESOURCE_DESCRIPTOR',
        'resettable': False,
        'type': 'ViString'
    },
    1050305: {
        'access': 'read only',
        'channel_based': False,
        'name': 'LOGICAL_NAME',
        'resettable': False,
        'type': 'ViString'
    },
    1050327: {
        'access': 'read only',
        'channel_based': False,
        'name': 'SUPPORTED_INSTRUMENT_MODELS',
        'resettable': False,
        'type': 'ViString'
    },
    1050401: {
        'access': 'read only',
        'channel_based': False,
        'name': 'GROUP_CAPABILITIES',
        'resettable': False,
        'type': 'ViString'
    },
    1050510: {
        'access': 'read only',
        'channel_based': False,
        'name': 'INSTRUMENT_FIRMWARE_REVISION',
        'resettable': False,
        'type': 'ViString'
    },
    1050511: {
        'access': 'read only',
        'channel_based': False,
        'name': 'INSTRUMENT_MANUFACTURER',
        'resettable': False,
        'type': 'ViString'
    },
    1050512: {
        'access': 'read only',
        'channel_based': False,
        'name': 'INSTRUMENT_MODEL',
        'resettable': False,
        'type': 'ViString'
    },
    1050513: {
        'access': 'read only',
        'channel_based': False,
        'name': 'SPECIFIC_DRIVER_VENDOR',
        'resettable': False,
        'type': 'ViString'
    },
    1050514: {
        'access': 'read only',
        'channel_based': False,
        'name': 'SPECIFIC_DRIVER_DESCRIPTION',
        'resettable': False,
        'type': 'ViString'
    },
    1050515: {
        'access': 'read only',
        'channel_based': False,
        'name': 'SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION',
        'resettable': False,
        'type': 'ViInt32'
    },
    1050516: {
        'access': 'read only',
        'channel_based': False,
        'name': 'SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION',
        'resettable': False,
        'type': 'ViInt32'
    },
    1050551: {
        'access': 'read only',
        'channel_based': False,
        'name': 'SPECIFIC_DRIVER_REVISION',
        'resettable': False,
        'type': 'ViString'
    },
    1150001: {
        'access': 'read only',
        'channel_based': False,
        'name': 'SERIAL_NUMBER',
        'resettable': False,
        'type': 'ViString'
    },
    1150004: {
        'access': 'read-write',
        'channel_based': True,
        'enum': 'SelectedFunction',
        'name': 'SELECTED_FUNCTION',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150006: {
        'access': 'read-write',
        'channel_based': True,
        'enum': 'TerminationMode',
        'name': 'TERMINATION_MODE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150007: {
        'access': 'read-write',
        'channel_based': True,
        'name': 'VIL',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150008: {
        'access': 'read-write',
        'channel_based': True,
        'name': 'VIH',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150009: {
        'access': 'read-write',
        'channel_based': True,
        'name': 'VOL',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150010: {
        'access': 'read-write',
        'channel_based': True,
        'name': 'VOH',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150011: {
        'access': 'read-write',
        'channel_based': True,
        'name': 'VTERM',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150012: {
        'access': 'read-write',
        'channel_based': True,
        'name': 'ACTIVE_LOAD_IOL',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150013: {
        'access': 'read-write',
        'channel_based': True,
        'name': 'ACTIVE_LOAD_IOH',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150014: {
        'access': 'read-write',
        'channel_based': True,
        'name': 'ACTIVE_LOAD_VCOM',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150015: {
        'access': 'read-write',
        'channel_based': True,
        'enum': 'PPMUOutputFunction',
        'name': 'PPMU_OUTPUT_FUNCTION',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150016: {
        'access': 'read-write',
        'channel_based': True,
        'name': 'PPMU_VOLTAGE_LEVEL',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150017: {
        'access': 'read-write',
        'channel_based': True,
        'name': 'PPMU_CURRENT_LIMIT_RANGE',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150019: {
        'access': 'read-write',
        'channel_based': True,
        'name': 'PPMU_CURRENT_LEVEL',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150020: {
        'access': 'read-write',
        'channel_based': True,
        'name': 'PPMU_CURRENT_LEVEL_RANGE',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150021: {
        'access': 'read-write',
        'channel_based': True,
        'name': 'PPMU_VOLTAGE_LIMIT_LOW',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150022: {
        'access': 'read-write',
        'channel_based': True,
        'name': 'PPMU_VOLTAGE_LIMIT_HIGH',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150023: {
        'access': 'read-write',
        'channel_based': False,
        'name': 'START_LABEL',
        'resettable': True,
        'type': 'ViString'
    },
    1150028: {
        'access': 'read-write',
        'channel_based': False,
        'name': 'EXPORTED_REF_CLOCK_OUTPUT_TERMINAL',
        'resettable': True,
        'type': 'ViString'
    },
    1150029: {
        'access': 'read-write',
        'channel_based': False,
        'name': 'START_TRIGGER_TYPE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150030: {
        'access': 'read-write',
        'channel_based': False,
        'name': 'DIGITAL_EDGE_START_TRIGGER_SOURCE',
        'resettable': True,
        'type': 'ViString'
    },
    1150031: {
        'access': 'read-write',
        'channel_based': False,
        'enum': 'DigitalEdge',
        'name': 'DIGITAL_EDGE_START_TRIGGER_EDGE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150032: {
        'access': 'read-write',
        'channel_based': False,
        'name': 'EXPORTED_START_TRIGGER_OUTPUT_TERMINAL',
        'resettable': True,
        'type': 'ViString'
    },
    1150033: {
        'access': 'read-write',
        'channel_based': True,
        'name': 'CONDITIONAL_JUMP_TRIGGER_TYPE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150034: {
        'access': 'read-write',
        'channel_based': True,
        'name': 'DIGITAL_EDGE_CONDITIONAL_JUMP_TRIGGER_SOURCE',
        'resettable': True,
        'type': 'ViString'
    },
    1150035: {
        'access': 'read-write',
        'channel_based': True,
        'enum': 'DigitalEdge',
        'name': 'DIGITAL_EDGE_CONDITIONAL_JUMP_TRIGGER_EDGE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150036: {
        'access': 'read-write',
        'channel_based': True,
        'name': 'EXPORTED_CONDITIONAL_JUMP_TRIGGER_OUTPUT_TERMINAL',
        'resettable': True,
        'type': 'ViString'
    },
    1150037: {
        'access': 'read-write',
        'channel_based': True,
        'name': 'PPMU_APERTURE_TIME',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150038: {
        'access': 'read-write',
        'channel_based': True,
        'enum': 'ApertureTimeUnits',
        'name': 'PPMU_APERTURE_TIME_UNITS',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150039: {
        'access': 'read only',
        'channel_based': False,
        'name': 'START_TRIGGER_TERMINAL_NAME',
        'resettable': False,
        'type': 'ViString'
    },
    1150040: {
        'access': 'read only',
        'channel_based': True,
        'name': 'CONDITIONAL_JUMP_TRIGGER_TERMINAL_NAME',
        'resettable': False,
        'type': 'ViString'
    },
    1150041: {
        'access': 'read-write',
        'channel_based': True,
        'name': 'EXPORTED_PATTERN_OPCODE_EVENT_OUTPUT_TERMINAL',
        'resettable': True,
        'type': 'ViString'
    },
    1150042: {
        'access': 'read only',
        'channel_based': False,
        'name': 'PATTERN_OPCODE_EVENT_TERMINAL_NAME',
        'resettable': False,
        'type': 'ViString'
    },
    1150043: {
        'access': 'read-write',
        'channel_based': False,
        'name': 'HISTORY_RAM_TRIGGER_TYPE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150044: {
        'access': 'read-write',
        'channel_based': False,
        'name': 'CYCLE_NUMBER_HISTORY_RAM_TRIGGER_CYCLE_NUMBER',
        'resettable': True,
        'type': 'ViInt64'
    },
    1150045: {
        'access': 'read-write',
        'channel_based': False,
        'name': 'PATTERN_LABEL_HISTORY_RAM_TRIGGER_CYCLE_OFFSET',
        'resettable': True,
        'type': 'ViInt64'
    },
    1150046: {
        'access': 'read-write',
        'channel_based': False,
        'name': 'PATTERN_LABEL_HISTORY_RAM_TRIGGER_LABEL',
        'resettable': True,
        'type': 'ViString'
    },
    1150047: {
        'access': 'read-write',
        'channel_based': False,
        'name': 'HISTORY_RAM_CYCLES_TO_ACQUIRE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150048: {
        'access': 'read-write',
        'channel_based': False,
        'name': 'HISTORY_RAM_PRETRIGGER_SAMPLES',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150049: {
        'access': 'read only',
        'channel_based': False,
        'name': 'CALIBRATION_REPORT',
        'resettable': False,
        'type': 'ViString'
    },
    1150050: {
        'access': 'read only',
        'channel_based': False,
        'name': 'SELF_TEST_REPORT',
        'resettable': False,
        'type': 'ViString'
    },
    1150051: {
        'access': 'read-write',
        'channel_based': True,
        'name': 'TDR_OFFSET',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150052: {
        'access': 'read-write',
        'channel_based': False,
        'name': 'PATTERN_LABEL_HISTORY_RAM_TRIGGER_VECTOR_OFFSET',
        'resettable': True,
        'type': 'ViInt64'
    },
    1150054: {
        'access': 'read-write',
        'channel_based': True,
        'name': 'PPMU_CURRENT_LIMIT',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150055: {
        'access': 'read only',
        'channel_based': True,
        'name': 'PPMU_CURRENT_LIMIT_SUPPORTED',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150056: {
        'access': 'read-write',
        'channel_based': False,
        'name': 'SEQUENCER_FLAG_TRIGGER_TYPE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150057: {
        'access': 'read-write',
        'channel_based': False,
        'name': 'SEQUENCER_FLAG_SOURCE',
        'resettable': True,
        'type': 'ViString'
    },
    1150058: {
        'access': 'read-write',
        'channel_based': False,
        'name': 'EXPORTED_SEQUENCER_FLAG_OUTPUT_TERMINAL',
        'resettable': True,
        'type': 'ViString'
    },
    1150059: {
        'access': 'read only',
        'channel_based': False,
        'name': 'SEQUENCER_FLAG_TERMINAL_NAME',
        'resettable': False,
        'type': 'ViString'
    },
    1150060: {
        'access': 'read-write',
        'channel_based': True,
        'name': 'MASK_COMPARE',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150062: {
        'access': 'read-write',
        'channel_based': False,
        'name': 'HALT_ON_KEEP_ALIVE_OPCODE',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150063: {
        'access': 'read only',
        'channel_based': False,
        'name': 'IS_KEEP_ALIVE_ACTIVE',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150064: {
        'access': 'read-write',
        'channel_based': True,
        'name': 'PPMU_CURRENT_LIMIT_BEHAVIOR',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150069: {
        'access': 'read-write',
        'channel_based': True,
        'name': 'FREQUENCY_COUNTER_MEASUREMENT_TIME',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150071: {
        'access': 'read-write',
        'channel_based': False,
        'name': 'TIMING_ABSOLUTE_DELAY_ENABLED',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150072: {
        'access': 'read-write',
        'channel_based': False,
        'name': 'TIMING_ABSOLUTE_DELAY',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150073: {
        'access': 'read-write',
        'channel_based': True,
        'name': 'CLOCK_GENERATOR_FREQUENCY',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150074: {
        'access': 'read only',
        'channel_based': True,
        'name': 'CLOCK_GENERATOR_IS_RUNNING',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150076: {
        'access': 'read-write',
        'channel_based': True,
        'name': 'PPMU_ALLOW_EXTENDED_VOLTAGE_RANGE',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150077: {
        'access': 'read-write',
        'channel_based': False,
        'name': 'HISTORY_RAM_MAX_SAMPLES_TO_ACQUIRE_PER_SITE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150078: {
        'access': 'read-write',
        'channel_based': False,
        'name': 'HISTORY_RAM_NUMBER_OF_SAMPLES_IS_FINITE',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150079: {
        'access': 'read-write',
        'channel_based': False,
        'name': 'HISTORY_RAM_BUFFER_SIZE_PER_SITE',
        'resettable': True,
        'type': 'ViInt64'
    },
    1150080: {
        'access': 'read-write',
        'channel_based': False,
        'name': 'HISTORY_RAM_SUPPRESS_BUFFER_OVERFLOW',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150081: {
        'access': 'read-write',
        'channel_based': False,
        'enum': 'TDREndpointTermination',
        'name': 'TDR_ENDPOINT_TERMINATION',
        'resettable': True,
        'type': 'ViInt32'
    },
    1200003: {
        'access': 'read only',
        'channel_based': True,
        'name': 'DIGITAL_DRIVER_STATE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1200005: {
        'access': 'read only',
        'channel_based': False,
        'name': 'NUMBER_OF_TIME_SETS',
        'resettable': False,
        'type': 'ViInt32'
    },
    1200007: {
        'access': 'read only',
        'channel_based': False,
        'name': 'NUMBER_OF_LOADED_PATTERNS',
        'resettable': False,
        'type': 'ViInt32'
    },
    1200009: {
        'access': 'read-write',
        'channel_based': True,
        'name': 'PXI_TRIG_IMMEDIATE_ROUTE_SOURCE',
        'resettable': True,
        'type': 'ViString'
    },
    1200010: {
        'access': 'read only',
        'channel_based': False,
        'name': 'TEMPERATURE_LOCAL',
        'resettable': False,
        'type': 'ViReal64'
    },
    1200078: {
        'access': 'read only',
        'channel_based': False,
        'name': 'IS_START_TRIGGER_MASTER',
        'resettable': False,
        'type': 'ViBoolean'
    }
}
