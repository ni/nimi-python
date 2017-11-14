# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

# We are not code genning attributes that have been marked as obsolete prior to the initial
# Python API bindings release
# We also do not need to codegen attributes that apply to P2P since it is not supported in Python
attributes_codegen_method = {
    1050302: { "codegen_method": "no" },  # SPECIFIC_PREFIX
    1050503: { "codegen_method": "no" },  # DRIVER_MAJOR_VERSION
    1050504: { "codegen_method": "no" },  # DRIVER_MINOR_VERSION
    1050551: { "codegen_method": "no" },  # DRIVER_REVISION
    1050501: { "codegen_method": "no" },  # ENGINE_MAJOR_VERSION
    1050502: { "codegen_method": "no" },  # ENGINE_MINOR_VERSION
    1050553: { "codegen_method": "no" },  # ENGINE_REVISION
    1050321: { "codegen_method": "no" },  # VISA_RM_SESSION
    1050322: { "codegen_method": "no" },  # IO_SESSION
    1050051: { "codegen_method": "no" },  # DEFER_UPDATE
    1050052: { "codegen_method": "no" },  # RETURN_DEFERRED_VALUES
    1050101: { "codegen_method": "no" },  # PRIMARY_ERROR
    1050102: { "codegen_method": "no" },  # SECONDARY_ERROR
    1050103: { "codegen_method": "no" },  # ERROR_ELABORATION
    1250350: { "codegen_method": "no" },  # CYCLE_COUNT
    1050003: { "codegen_method": "no" },  # QUERY_INSTR_STATUS
    1050503: { "codegen_method": "no" },  # SPECIFIC_DRIVER_MAJOR_VERSION
    1050504: { "codegen_method": "no" },  # SPECIFIC_DRIVER_MINOR_VERSION
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
}


