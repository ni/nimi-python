# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

# If the associated enum represents boolean values only, disconnect
attributes_remove_enum = {
    1150338: { 'enum': None, 'python_type': 'bool', }, # Disconnecting enum since it is a boolean
    1150343: { 'enum': None, 'python_type': 'bool', }, # Disconnecting enum since it is a boolean
    1150354: { 'enum': None, 'python_type': 'bool', }, # Disconnecting enum since it is a boolean
    1250005: { 'enum': None, 'python_type': 'bool', }, # Disconnecting enum since it is a boolean
    1150311: { 'enum': None, 'python_type': 'bool', }, # Disconnecting enum since it is a boolean
    1150004: { 'enum': None, 'python_type': 'bool', }, # Disconnecting enum since it is a boolean
    1150128: { 'enum': None, 'python_type': 'bool', }, # Disconnecting enum since it is a boolean
}

# We are not code genning attributes that have been marked as obsolete prior to the initial
# Python API bindings release
# We also do not need to codegen attributes that apply to P2P since it is not supported in Python
attributes_codegen_method = {
    1050003: { "codegen_method": "no" },  # QUERY_INSTR_STATUS
    1050302: { "codegen_method": "no" },  # SPECIFIC_PREFIX
    1050501: { "codegen_method": "no" },  # ENGINE_MAJOR_VERSION
    1050502: { "codegen_method": "no" },  # ENGINE_MINOR_VERSION
    1050553: { "codegen_method": "no" },  # ENGINE_REVISION
    1050322: { "codegen_method": "no" },  # IO_SESSION
    1050051: { "codegen_method": "no" },  # DEFER_UPDATE
    1050052: { "codegen_method": "no" },  # RETURN_DEFERRED_VALUES
    1050101: { "codegen_method": "no" },  # PRIMARY_ERROR
    1050102: { "codegen_method": "no" },  # SECONDARY_ERROR
    1050103: { "codegen_method": "no" },  # ERROR_ELABORATION
    1150010: { "codegen_method": "no" },  # TRIGGER_OUTPUT_EVENT
    1150011: { "codegen_method": "no" },  # TRIGGER_OUTPUT_SOURCE
    1150091: { "codegen_method": "no" },  # EXPORT_SAMP_CLK_OUTPUT_TERM
    1150054: { "codegen_method": "no" },  # RTSI0_TRIGGER_OUTPUT_EVENT
    1150055: { "codegen_method": "no" },  # RTSI1_TRIGGER_OUTPUT_EVENT
    1150056: { "codegen_method": "no" },  # RTSI2_TRIGGER_OUTPUT_EVENT
    1150057: { "codegen_method": "no" },  # RTSI3_TRIGGER_OUTPUT_EVENT
    1150058: { "codegen_method": "no" },  # RTSI4_TRIGGER_OUTPUT_EVENT
    1150059: { "codegen_method": "no" },  # RTSI5_TRIGGER_OUTPUT_EVENT
    1150060: { "codegen_method": "no" },  # RTSI6_TRIGGER_OUTPUT_EVENT
    1150061: { "codegen_method": "no" },  # PFI1_TRIGGER_OUTPUT_EVENT
    1150062: { "codegen_method": "no" },  # PFI2_TRIGGER_OUTPUT_EVENT
    1150063: { "codegen_method": "no" },  # STAR_TRIGGER_OUTPUT_EVENT
    1151000: { "codegen_method": "no" },  # DDC_NCO_FREQUENCY
    1151001: { "codegen_method": "no" },  # DDC_NCO_PHASE
    1151003: { "codegen_method": "no" },  # DDC_ENABLE
    1151010: { "codegen_method": "no" },  # DDC_CIC_DECIMATION
    1151011: { "codegen_method": "no" },  # DDC_CIC_SHIFT_GAIN
    1151020: { "codegen_method": "no" },  # DDC_DISCRIMINATOR_ENABLED
    1151021: { "codegen_method": "no" },  # DDC_DISCRIMINATOR_FIR_DECIMATION
    1151022: { "codegen_method": "no" },  # DDC_DISCRIMINATOR_FIR_SYMMETRY
    1151023: { "codegen_method": "no" },  # DDC_DISCRIMINATOR_FIR_SYMMETRY_TYPE
    1151024: { "codegen_method": "no" },  # DDC_DISCRIMINATOR_FIR_NUM_TAPS
    1151025: { "codegen_method": "no" },  # DDC_DISCRIMINATOR_DELAY
    1151026: { "codegen_method": "no" },  # DDC_DISCRIMINATOR_FIR_INPUT_SOURCE
    1151027: { "codegen_method": "no" },  # DDC_DISCRIMINATOR_PHASE_MULTIPLIER
    1151030: { "codegen_method": "no" },  # DDC_PFIR_DECIMATION
    1151031: { "codegen_method": "no" },  # DDC_PFIR_SYMMETRY
    1151032: { "codegen_method": "no" },  # DDC_PFIR_SYMMETRY_TYPE
    1151033: { "codegen_method": "no" },  # DDC_PFIR_NUM_TAPS
    1151034: { "codegen_method": "no" },  # DDC_PFIR_REAL_OR_COMPLEX
    1151040: { "codegen_method": "no" },  # DDC_AGC_UPPER_GAIN_LIMIT
    1151041: { "codegen_method": "no" },  # DDC_AGC_LOWER_GAIN_LIMIT
    1151042: { "codegen_method": "no" },  # DDC_AGC_LOOP_GAIN_0_EXPONENT
    1151043: { "codegen_method": "no" },  # DDC_AGC_LOOP_GAIN_0_MANTISSA
    1151044: { "codegen_method": "no" },  # DDC_AGC_LOOP_GAIN_1_EXPONENT
    1151045: { "codegen_method": "no" },  # DDC_AGC_LOOP_GAIN_1_MANTISSA
    1151046: { "codegen_method": "no" },  # DDC_AGC_THRESHOLD
    1151047: { "codegen_method": "no" },  # DDC_AGC_AVERAGE_CONTROL
    1151050: { "codegen_method": "no" },  # DDC_HALFBAND_BYPASSED
    1151051: { "codegen_method": "no" },  # DDC_HALFBAND_1_ENABLED
    1151052: { "codegen_method": "no" },  # DDC_HALFBAND_2_ENABLED
    1151053: { "codegen_method": "no" },  # DDC_HALFBAND_3_ENABLED
    1151054: { "codegen_method": "no" },  # DDC_HALFBAND_4_ENABLED
    1151055: { "codegen_method": "no" },  # DDC_HALFBAND_5_ENABLED
    1151070: { "codegen_method": "no" },  # DDC_AOUT_PARALLEL_OUTPUT_SOURCE
    1151071: { "codegen_method": "no" },  # DDC_BOUT_PARALLEL_OUTPUT_SOURCE
    1151072: { "codegen_method": "no" },  # DDC_TEST_SINE_COSINE
    1151073: { "codegen_method": "no" },  # DDC_COORDINATE_CONVERTER_INPUT
    1151074: { "codegen_method": "no" },  # DDC_Q_INPUT_TO_COORD_CONVERTER_INPUT
    1151080: { "codegen_method": "no" },  # DDC_SYNCOUT_CLK_SELECT
    1151120: { "codegen_method": "no" },  # DDC_TIMING_NCO_PHASE_ACCUM_LOAD
    1151121: { "codegen_method": "no" },  # DDC_TIMING_NCO_CLEAR_PHASE_ACCUM
    1151122: { "codegen_method": "no" },  # DDC_TIMING_NCO_ENABLE_OFFSET_FREQ
    1151123: { "codegen_method": "no" },  # DDC_TIMING_NCO_NUM_OFFSET_FREQ_BITS
    1151124: { "codegen_method": "no" },  # DDC_TIMING_NCO_CENTER_FREQUENCY
    1151125: { "codegen_method": "no" },  # DDC_TIMING_NCO_PHASE_OFFSET
    1151126: { "codegen_method": "no" },  # DDC_RESAMPLER_FILTER_MODE_SELECT
    1151127: { "codegen_method": "no" },  # DDC_RESAMPLER_BYPASS
    1151128: { "codegen_method": "no" },  # DDC_RESAMPLER_OUTPUT_PULSE_DELAY
    1151129: { "codegen_method": "no" },  # DDC_NCO_DIVIDE
    1151130: { "codegen_method": "no" },  # DDC_REFERENCE_DIVIDE
    1151300: { "codegen_method": "no" },  # ENABLE_DITHER
    1151301: { "codegen_method": "no" },  # DDC_COMBINED_DECIMATION
    1151302: { "codegen_method": "no" },  # SERIAL_DAC_CAL_VOLTAGE
    1151304: { "codegen_method": "no" },  # DELAY_BEFORE_INITIATE
    1151305: { "codegen_method": "no" },  # DDC_DIRECT_REGISTER_ADDRESS
    1151306: { "codegen_method": "no" },  # DDC_DIRECT_REGISTER_DATA
    1150328: { "codegen_method": "no" },  # P2P_SAMPLES_AVAIL_IN_ENDPOINT - P2P Attribute
    1150329: { "codegen_method": "no" },  # P2P_DATA_TRANS_PERMISSION_ADDR - P2P Attribute
    1150330: { "codegen_method": "no" },  # P2P_DATA_TRANS_PERMISSION_ADDR_TYPE - P2P Attribute
    1150331: { "codegen_method": "no" },  # P2P_DESTINATION_WINDOW_ADDR - P2P Attribute
    1150332: { "codegen_method": "no" },  # P2P_DESTINATION_WINDOW_ADDR_TYPE - P2P Attribute
    1150333: { "codegen_method": "no" },  # P2P_DESTINATION_WINDOW_SIZE - P2P Attribute
    1150334: { "codegen_method": "no" },  # P2P_NOTIFY_PUSH_MESSAGE_ON - P2P Attribute
    1150335: { "codegen_method": "no" },  # P2P_NOTIFY_MESSAGE_PUSH_ADDR - P2P Attribute
    1150336: { "codegen_method": "no" },  # P2P_NOTIFY_MESSAGE_PUSH_ADDR_TYPE - P2P Attribute
    1150337: { "codegen_method": "no" },  # P2P_NOTIFY_MESSAGE_PUSH_VALUE - P2P Attribute
    1150338: { "codegen_method": "no" },  # P2P_ENABLED - P2P Attribute
    1150339: { "codegen_method": "no" },  # P2P_CHANNELS_TO_STREAM - P2P Attribute
    1150340: { "codegen_method": "no" },  # P2P_SAMPLES_TRANSFERRED - P2P Attribute
    1150341: { "codegen_method": "no" },  # P2P_MOST_SAMPLES_AVAIL_IN_ENDPOINT - P2P Attribute
    1150342: { "codegen_method": "no" },  # P2P_ENDPOINT_SIZE - P2P Attribute
    1150343: { "codegen_method": "no" },  # MANUAL_CONFIGURATION_ENABLED - P2P Attribute
    1150344: { "codegen_method": "no" },  # P2P_ENDPOINT_OVERFLOW - P2P Attribute
    1150345: { "codegen_method": "no" },  # P2P_FIFO_ENDPOINT_COUNT - P2P Attribute
    1150354: { "codegen_method": "no" },  # P2P_ONBOARD_MEMORY_ENABLED - P2P Attribute
    1150380: { "codegen_method": "no" },  # SAMPLES_TRANSFERRED_PER_RECORD - P2P Attribute
}


