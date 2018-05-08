# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

# If the associated enum represents boolean values only, disconnect
attributes_remove_enum = {
    1150338: { 'enum': None, 'python_type': 'bool', }, # P2P_ENABLED, Don't use the enum because a bool will do
    1150343: { 'enum': None, 'python_type': 'bool', }, # P2P_ADVANCED_ATTRIBUTES_ENABLED, Don't use the enum because a bool will do
    1150354: { 'enum': None, 'python_type': 'bool', }, # P2P_ONBOARD_MEMORY_ENABLED, Don't use the enum because a bool will do
    1250005: { 'enum': None, 'python_type': 'bool', }, # CHANNEL_ENABLED, Don't use the enum because a bool will do
    1150311: { 'enum': None, 'python_type': 'bool', }, # FETCH_INTERLEAVED_IQ_DATA, Don't use the enum because a bool will do
    1150004: { 'enum': None, 'python_type': 'bool', }, # HORZ_ENFORCE_REALTIME, Don't use the enum because a bool will do
    1150128: { 'enum': None, 'python_type': 'bool', }, # ENABLE_TIME_INTERLEAVED_SAMPLING, Don't use the enum because a bool will do
}

# Override names that can't be directly converted from C names into valid Python names
attributes_override_values = {
    1150085: { 'python_name': 'adjust_pretrigger_samples_5102', },
    1150129: { 'python_name': 'five_v_out_output_terminal', },
}

attributes_converters = {
    1150046: { 'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
               'type_in_documentation': 'float in seconds or datetime.timedelta', },  # SLAVE_TRIGGER_DELAY
    1150047: { 'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
               'type_in_documentation': 'float in seconds or datetime.timedelta', },  # TRIGGER_TO_STAR_DELAY
    1150048: { 'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
               'type_in_documentation': 'float in seconds or datetime.timedelta', },  # TRIGGER_TO_RTSI_DELAY
    1150049: { 'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
               'type_in_documentation': 'float in seconds or datetime.timedelta', },  # TRIGGER_TO_PFI_DELAY
    1150050: { 'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
               'type_in_documentation': 'float in seconds or datetime.timedelta', },  # TRIGGER_FROM_STAR_DELAY
    1150051: { 'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
               'type_in_documentation': 'float in seconds or datetime.timedelta', },  # TRIGGER_FROM_RTSI_DELAY
    1150052: { 'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
               'type_in_documentation': 'float in seconds or datetime.timedelta', },  # TRIGGER_FROM_PFI_DELAY
    1151304: { 'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
               'type_in_documentation': 'float in seconds or datetime.timedelta', },  # DELAY_BEFORE_INITIATE
    1250015: { 'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
               'type_in_documentation': 'float in seconds or datetime.timedelta', },  # TRIGGER_DELAY_TIME
    1150103: { 'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
               'type_in_documentation': 'float in seconds or datetime.timedelta', },  # START_TO_REF_TRIGGER_HOLDOFF
    1150366: { 'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
               'type_in_documentation': 'float in seconds or datetime.timedelta', },  # END_OF_RECORD_TO_ADVANCE_TRIGGER_HOLDOFF
    1250016: { 'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
               'type_in_documentation': 'float in seconds or datetime.timedelta', },  # TRIGGER_HOLDOFF
    1150315: { 'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
               'type_in_documentation': 'float in seconds or datetime.timedelta', },  # REF_TRIGGER_MINIMUM_QUIET_TIME
    1150374: { 'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
               'type_in_documentation': 'float in seconds or datetime.timedelta', },  # ABSOLUTE_SAMPLE_CLOCK_OFFSET
    1250007: { 'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
               'type_in_documentation': 'float in seconds or datetime.timedelta', },  # HORZ_TIME_PER_RECORD
    1250109: { 'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
               'type_in_documentation': 'float in seconds or datetime.timedelta', },  # ACQUISITION_START_TIME
}

# We are not code genning attributes that have been marked as obsolete prior to the initial
# Python API bindings release
# We also do not need to codegen attributes that apply to P2P since it is not supported in Python
attributes_codegen_method = {
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
    1150373: { "codegen_method": "no" },  # STREAM_RELATIVE_TO - P2P Attribute - #825
    1150105: { "codegen_method": "no" },  # OSCILLATOR_PHASE_DAC_VALUE - NI-TClk Attribute - #825
    1151002: { "codegen_method": "no" },  # MUX_MODE_REGISTER - Internal Attribute - #825
    1150303: { "codegen_method": "no" },  # DDC_CENTER_FREQUENCY - Onboard Signal Processing Attribute - #823
    1150304: { "codegen_method": "no" },  # DDC_DATA_PROCESSING_MODE - Onboard Signal Processing Attribute - #823
    1150300: { "codegen_method": "no" },  # DDC_ENABLED - Onboard Signal Processing Attribute - #823
    1150302: { "codegen_method": "no" },  # DDC_FREQUENCY_TRANSLATION_ENABLED - Onboard Signal Processing Attribute - #823
    1150305: { "codegen_method": "no" },  # DDC_FREQUENCY_TRANSLATION_PHASE_I - Onboard Signal Processing Attribute - #823
    1150306: { "codegen_method": "no" },  # DDC_FREQUENCY_TRANSLATION_PHASE_Q - Onboard Signal Processing Attribute - #823
    1150310: { "codegen_method": "no" },  # DDC_Q_SOURCE - Onboard Signal Processing Attribute - #823
    1150307: { "codegen_method": "no" },  # DIGITAL_GAIN - Onboard Signal Processing Attribute - #823
    1150308: { "codegen_method": "no" },  # DIGITAL_OFFSET - Onboard Signal Processing Attribute - #823
    1150319: { "codegen_method": "no" },  # DITHER_ENABLED - Onboard Signal Processing Attribute - #823
    1150311: { "codegen_method": "no" },  # FETCH_INTERLEAVED_IQ_DATA - Onboard Signal Processing Attribute - #823
    1150320: { "codegen_method": "no" },  # FRACTIONAL_RESAMPLE_ENABLED - Onboard Signal Processing Attribute - #823
    1150309: { "codegen_method": "no" },  # OVERFLOW_ERROR_REPORTING - Onboard Signal Processing Attribute - #823
    1150085: { "codegen_method": "no" },  # 5102_ADJUST_PRETRIGGER_SAMPLES - Onboard Signal Processing Attribute - #822
    1150129: { "codegen_method": "no" },  # 5V_OUT_OUTPUT_TERMINAL - Onboard Signal Processing Attribute - #822
    1150007: { "codegen_method": "no" },  # CLOCK_SYNC_PULSE_SOURCE - Onboard Signal Processing Attribute - #822
    1150076: { "codegen_method": "no" },  # DEVICE_NUMBER - Onboard Signal Processing Attribute - #822
    1150072: { "codegen_method": "no" },  # FETCH_INTERLEAVED_DATA - Onboard Signal Processing Attribute - #822
    1150052: { "codegen_method": "no" },  # TRIGGER_FROM_PFI_DELAY - Onboard Signal Processing Attribute - #822
    1150051: { "codegen_method": "no" },  # TRIGGER_FROM_RTSI_DELAY - Onboard Signal Processing Attribute - #822
    1150050: { "codegen_method": "no" },  # TRIGGER_FROM_STAR_DELAY - Onboard Signal Processing Attribute - #822
    1150049: { "codegen_method": "no" },  # TRIGGER_TO_PFI_DELAY - Onboard Signal Processing Attribute - #822
    1150048: { "codegen_method": "no" },  # TRIGGER_TO_RTSI_DELAY - Onboard Signal Processing Attribute - #822
    1150047: { "codegen_method": "no" },  # TRIGGER_TO_STAR_DELAY - Onboard Signal Processing Attribute - #822
    1150046: { "codegen_method": "no" },  # SLAVE_TRIGGER_DELAY - Onboard Signal Processing Attribute - #822
    1050401: { "codegen_method": "no" },  # GROUP_CAPABILITIES - IVI Attribute - #824
    1050021: { "codegen_method": "no" },  # INTERCHANGE_CHECK - IVI Attribute - #824
    1050002: { "codegen_method": "no" },  # RANGE_CHECK - IVI Attribute - #824
    1050006: { "codegen_method": "no" },  # RECORD_COERCIONS - IVI Attribute - #824
    1050515: { "codegen_method": "no" },  # SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION - IVI Attribute - #824
    1050516: { "codegen_method": "no" },  # SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION - IVI Attribute - #824
    1050003: { "codegen_method": "no" },  # QUERY_INSTR_STATUS - IVI Attribute - #824
    1050302: { "codegen_method": "no" },  # SPECIFIC_PREFIX - IVI Attribute - #824
    1050501: { "codegen_method": "no" },  # ENGINE_MAJOR_VERSION - IVI Attribute - #824
    1050502: { "codegen_method": "no" },  # ENGINE_MINOR_VERSION - IVI Attribute - #824
    1050553: { "codegen_method": "no" },  # ENGINE_REVISION - IVI Attribute - #824
    1050322: { "codegen_method": "no" },  # IO_SESSION - IVI Attribute - #824
    1050051: { "codegen_method": "no" },  # DEFER_UPDATE - IVI Attribute - #824
    1050052: { "codegen_method": "no" },  # RETURN_DEFERRED_VALUES - IVI Attribute - #824
    1050101: { "codegen_method": "no" },  # PRIMARY_ERROR - IVI Attribute - #824
    1050102: { "codegen_method": "no" },  # SECONDARY_ERROR - IVI Attribute - #824
    1050103: { "codegen_method": "no" },  # ERROR_ELABORATION - IVI Attribute - #824
    1050004: { "codegen_method": "no" },  # CACHE - IVI Attribute - #824
    1150077: { "codegen_method": "private" },  # FETCH_RELATIVE_TO - Fetch attribute
    1150078: { "codegen_method": "private" },  # FETCH_OFFSET - Fetch attribute
    1150079: { "codegen_method": "private" },  # FETCH_RECORD_NUMBER - Fetch attribute
    1150080: { "codegen_method": "private" },  # FETCH_NUM_RECORDS - Fetch attribute
    1150016: { "codegen_method": "private" },  # MEAS_REF_LEVEL_UNITS - Measurement library private - #810
    1150018: { "codegen_method": "private" },  # MEAS_OTHER_CHANNEL - Measurement library private - #810
    1150019: { "codegen_method": "private" },  # MEAS_HYSTERESIS_PERCENT - Measurement library private - #810
    1150020: { "codegen_method": "private" },  # MEAS_LAST_ACQ_HISTOGRAM_SIZE - Measurement library private - #810
    1150021: { "codegen_method": "private" },  # MEAS_VOLTAGE_HISTOGRAM_SIZE - Measurement library private - #810
    1150022: { "codegen_method": "private" },  # MEAS_VOLTAGE_HISTOGRAM_LOW_VOLTS - Measurement library private - #810
    1150023: { "codegen_method": "private" },  # MEAS_VOLTAGE_HISTOGRAM_HIGH_VOLTS - Measurement library private - #810
    1150024: { "codegen_method": "private" },  # MEAS_TIME_HISTOGRAM_SIZE - Measurement library private - #810
    1150025: { "codegen_method": "private" },  # MEAS_TIME_HISTOGRAM_LOW_VOLTS - Measurement library private - #810
    1150026: { "codegen_method": "private" },  # MEAS_TIME_HISTOGRAM_HIGH_VOLTS - Measurement library private - #810
    1150027: { "codegen_method": "private" },  # MEAS_TIME_HISTOGRAM_LOW_TIME - Measurement library private - #810
    1150028: { "codegen_method": "private" },  # MEAS_TIME_HISTOGRAM_HIGH_TIME - Measurement library private - #810
    1150029: { "codegen_method": "private" },  # MEAS_POLYNOMIAL_INTERPOLATION_ORDER - Measurement library private - #810
    1150030: { "codegen_method": "private" },  # MEAS_INTERPOLATION_SAMPLING_FACTOR - Measurement library private - #810
    1150031: { "codegen_method": "private" },  # MEAS_FILTER_CUTOFF_FREQ - Measurement library private - #810
    1150032: { "codegen_method": "private" },  # MEAS_FILTER_CENTER_FREQ - Measurement library private - #810
    1150033: { "codegen_method": "private" },  # MEAS_FILTER_RIPPLE - Measurement library private - #810
    1150034: { "codegen_method": "private" },  # MEAS_FILTER_TRANSIENT_WAVEFORM_PERCENT - Measurement library private - #810
    1150035: { "codegen_method": "private" },  # MEAS_FILTER_TYPE - Measurement library private - #810
    1150036: { "codegen_method": "private" },  # MEAS_FILTER_ORDER - Measurement library private - #810
    1150037: { "codegen_method": "private" },  # MEAS_FILTER_TAPS - Measurement library private - #810
    1150038: { "codegen_method": "private" },  # MEAS_CHAN_LOW_REF_LEVEL - Measurement library private - #810
    1150039: { "codegen_method": "private" },  # MEAS_CHAN_MID_REF_LEVEL - Measurement library private - #810
    1150040: { "codegen_method": "private" },  # MEAS_CHAN_HIGH_REF_LEVEL - Measurement library private - #810
    1150041: { "codegen_method": "private" },  # MEAS_FILTER_WIDTH - Measurement library private - #810
    1150042: { "codegen_method": "private" },  # MEAS_FIR_FILTER_WINDOW - Measurement library private - #810
    1150043: { "codegen_method": "private" },  # MEAS_ARRAY_GAIN - Measurement library private - #810
    1150044: { "codegen_method": "private" },  # MEAS_ARRAY_OFFSET - Measurement library private - #810
    1150045: { "codegen_method": "private" },  # MEAS_PERCENTAGE_METHOD - Measurement library private - #810
    1150081: { "codegen_method": "private" },  # FETCH_MEAS_NUM_SAMPLES - Measurement library private - #810
}


