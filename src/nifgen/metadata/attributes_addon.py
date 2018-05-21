# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

# We are not code genning attributes that have been marked as obsolete prior to the initial
# Python API bindings release
# We also do not need to codegen attributes that apply to P2P since it is not supported in Python
attributes_codegen_method = {
    1250350: { "codegen_method": "no" },  # CYCLE_COUNT
    1150248: { "codegen_method": "no" },  # OSP_DATA_RATE
    1150106: { "codegen_method": "no" },  # UPDATE_CLOCK_SOURCE
    1250002: { "codegen_method": "no" },  # REF_CLOCK_SOURCE
    1250005: { "codegen_method": "no" },  # OPERATION_MODE
    1150109: { "codegen_method": "no" },  # ACTUAL_ARB_SAMPLE_RATE
    1150221: { "codegen_method": "no" },  # DAQMX_TASK
    1050322: { "codegen_method": "no" },  # IO_SESSION
    1150391: { "codegen_method": "no" },  # P2P_ENABLED - P2P Attribute
    1150392: { "codegen_method": "no" },  # P2P_DESTINATION_CHANNELS - P2P Attribute
    1150393: { "codegen_method": "no" },  # P2P_ENDPOINT_SIZE - P2P Attribute
    1150394: { "codegen_method": "no" },  # P2P_SPACE_AVAILABLE_IN_ENDPOINT - P2P Attribute
    1150395: { "codegen_method": "no" },  # P2P_MOST_SPACE_AVAILABLE_IN_ENDPOINT - P2P Attribute
    1150396: { "codegen_method": "no" },  # P2P_ENDPOINT_COUNT - P2P Attribute
    1150397: { "codegen_method": "no" },  # P2P_MANUAL_CONFIGURATION_ENABLED - P2P Attribute
    1150398: { "codegen_method": "no" },  # P2P_DATA_TRANSFER_PERMISSION_ADDRESS - P2P Attribute
    1150399: { "codegen_method": "no" },  # P2P_DATA_TRANSFER_PERMISSION_ADDRESS_TYPE - P2P Attribute
    1150400: { "codegen_method": "no" },  # P2P_DATA_TRANSFER_PERMISSION_INTERVAL - P2P Attribute
    1150401: { "codegen_method": "no" },  # P2P_ENDPOINT_WINDOW_ADDRESS - P2P Attribute
    1150402: { "codegen_method": "no" },  # P2P_ENDPOINT_WINDOW_ADDRESS_TYPE - P2P Attribute
    1150403: { "codegen_method": "no" },  # P2P_ENDPOINT_WINDOW_SIZE - P2P Attribute
    1150405: { "codegen_method": "no" },  # P2P_DONE_NOTIFICATION_ADDRESS - P2P Attribute
    1150406: { "codegen_method": "no" },  # P2P_DONE_NOTIFICATION_ADDRESS_TYPE - P2P Attribute
    1150407: { "codegen_method": "no" },  # P2P_DONE_NOTIFICATION_VALUE - P2P Attribute
    1150408: { "codegen_method": "no" },  # P2P_DATA_TRANSFER_PERMISSION_INITIAL_CREDITS - P2P Attribute
    1150227: { "codegen_method": "no" },  # CAL_ADC_INPUT - Calibration Attribute
    1050401: { "codegen_method": "no" },  # GROUP_CAPABILITIES - IVI Attribute - #824
    1050021: { "codegen_method": "no" },  # INTERCHANGE_CHECK - IVI Attribute - #824
    1050002: { "codegen_method": "no" },  # RANGE_CHECK - IVI Attribute - #824
    1050006: { "codegen_method": "no" },  # RECORD_COERCIONS - IVI Attribute - #824
    1050515: { "codegen_method": "no" },  # SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION - IVI Attribute - #824
    1050516: { "codegen_method": "no" },  # SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION - IVI Attribute - #824
    1050302: { "codegen_method": "no" },  # SPECIFIC_PREFIX - IVI Attribute - #824
    1050501: { "codegen_method": "no" },  # ENGINE_MAJOR_VERSION - IVI Attribute - #824
    1050502: { "codegen_method": "no" },  # ENGINE_MINOR_VERSION - IVI Attribute - #824
    1050553: { "codegen_method": "no" },  # ENGINE_REVISION - IVI Attribute - #824
    1050321: { "codegen_method": "no" },  # VISA_RM_SESSION - IVI Attribute - #824
    1050322: { "codegen_method": "no" },  # IO_SESSION - IVI Attribute - #824
    1050051: { "codegen_method": "no" },  # DEFER_UPDATE - IVI Attribute - #824
    1050052: { "codegen_method": "no" },  # RETURN_DEFERRED_VALUES - IVI Attribute - #824
    1050101: { "codegen_method": "no" },  # PRIMARY_ERROR - IVI Attribute - #824
    1050102: { "codegen_method": "no" },  # SECONDARY_ERROR - IVI Attribute - #824
    1050103: { "codegen_method": "no" },  # ERROR_ELABORATION - IVI Attribute - #824
    1050003: { "codegen_method": "no" },  # QUERY_INSTR_STATUS - IVI Attribute - #824
    1050004: { "codegen_method": "no" },  # CACHE - IVI Attribute - #824
    1150256: { "codegen_method": "no" },  # OSP_FIR_FILTER_INTERPOLATION - OSP Attribute - #864
    1150262: { "codegen_method": "no" },  # OSP_FIR_FILTER_GAUSSIAN_BT - OSP Attribute - #864
    1150261: { "codegen_method": "no" },  # OSP_FIR_FILTER_FLAT_PASSBAND - OSP Attribute - #864
    1150255: { "codegen_method": "no" },  # OSP_FIR_FILTER_ENABLED - OSP Attribute - #864
    1150246: { "codegen_method": "no" },  # OSP_ENABLED - OSP Attribute - #864
    1150247: { "codegen_method": "no" },  # OSP_DATA_PROCESSING_MODE - OSP Attribute - #864
    1150389: { "codegen_method": "no" },  # OSP_COMPENSATE_FOR_FILTER_GROUP_DELAY - OSP Attribute - #864
    1150258: { "codegen_method": "no" },  # OSP_CIC_FILTER_INTERPOLATION - OSP Attribute - #864
    1150263: { "codegen_method": "no" },  # OSP_CIC_FILTER_GAIN - OSP Attribute - #864
    1150257: { "codegen_method": "no" },  # OSP_CIC_FILTER_ENABLED - OSP Attribute - #864
    1150252: { "codegen_method": "no" },  # OSP_CARRIER_PHASE_Q - OSP Attribute - #864
    1150251: { "codegen_method": "no" },  # OSP_CARRIER_PHASE_I - OSP Attribute - #864
    1150250: { "codegen_method": "no" },  # OSP_CARRIER_FREQUENCY - OSP Attribute - #864
    1150249: { "codegen_method": "no" },  # OSP_CARRIER_ENABLED - OSP Attribute - #864
    1150267: { "codegen_method": "no" },  # OSP_PRE_FILTER_OFFSET_Q - OSP Attribute - #864
    1150266: { "codegen_method": "no" },  # OSP_PRE_FILTER_OFFSET_I - OSP Attribute - #864
    1150265: { "codegen_method": "no" },  # OSP_PRE_FILTER_GAIN_Q - OSP Attribute - #864
    1150264: { "codegen_method": "no" },  # OSP_PRE_FILTER_GAIN_I - OSP Attribute - #864
    1150269: { "codegen_method": "no" },  # OSP_OVERFLOW_STATUS - OSP Attribute - #864
    1150268: { "codegen_method": "no" },  # OSP_OVERFLOW_ERROR_REPORTING - OSP Attribute - #864
    1150370: { "codegen_method": "no" },  # OSP_MODE - OSP Attribute - #864
    1150371: { "codegen_method": "no" },  # OSP_FREQUENCY_SHIFT - OSP Attribute - #864
    1150253: { "codegen_method": "no" },  # OSP_FIR_FILTER_TYPE - OSP Attribute - #864
    1150259: { "codegen_method": "no" },  # OSP_FIR_FILTER_ROOT_RAISED_COSINE_ALPHA - OSP Attribute - #864
    1150260: { "codegen_method": "no" },  # OSP_FIR_FILTER_RAISED_COSINE_ALPHA - OSP Attribute - #864
}

attributes_converters = {
    1150409: { 'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
               'type_in_documentation': 'float in seconds or datetime.timedelta', },  # STREAMING_WRITE_TIMEOUT
}


