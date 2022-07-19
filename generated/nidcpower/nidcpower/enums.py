# -*- coding: utf-8 -*-
# This file was generated

from enum import Enum


class ApertureTimeAutoMode(Enum):
    OFF = 1135
    r'''
    Disables automatic aperture time scaling. The aperture_time property specifies the aperture time for all ranges.
    '''
    SHORT = 1136
    r'''
    Prioritizes measurement speed over measurement accuracy by quickly scaling down aperture time in larger current ranges. The aperture_time property specifies the aperture time for the minimum range.
    '''
    NORMAL = 1137
    r'''
    Balances measurement accuracy and speed by scaling down aperture time in larger current ranges. The aperture_time property specifies the aperture time for the minimum range.
    '''
    LONG = 1138
    r'''
    Prioritizes accuracy while still decreasing measurement time by slowly scaling down aperture time in larger current ranges. The aperture_time property specifies the aperture time for the minimum range.
    '''


class ApertureTimeUnits(Enum):
    SECONDS = 1028
    r'''
    Specifies aperture time in seconds.
    '''
    POWER_LINE_CYCLES = 1029
    r'''
    Specifies aperture time in power line cycles (PLCs).
    '''


class AutoZero(Enum):
    OFF = 0
    r'''
    Disables auto zero.
    '''
    ON = 1
    r'''
    Makes zero conversions for every measurement.
    '''
    ONCE = 1024
    r'''
    Makes zero conversions following the first measurement after initiating the device.  The device uses these zero conversions for the preceding measurement and future  measurements until the device is reinitiated.
    '''


class AutorangeApertureTimeMode(Enum):
    AUTO = 1110
    r'''
    NI-DCPower optimizes the aperture time for the autorange algorithm based on the module range.
    '''
    CUSTOM = 1111
    r'''
    The user specifies a minimum aperture time for the algorithm using the autorange_minimum_aperture_time property and the corresponding autorange_minimum_aperture_time_units property.
    '''


class AutorangeBehavior(Enum):
    UP_TO_LIMIT_THEN_DOWN = 1107
    r'''
    Go to limit range then range down as needed until measured value is within thresholds.
    '''
    UP = 1108
    r'''
    go up one range when the upper threshold is reached.
    '''
    UP_AND_DOWN = 1109
    r'''
    go up or down one range when the upper/lower threshold is reached.
    '''


class AutorangeThresholdMode(Enum):
    NORMAL = 1112
    r'''
    Thresholds are selected based on a balance between accuracy and hysteresis.
    '''
    FAST_STEP = 1113
    r'''
    Optimized for faster changes in the measured signal. Thresholds are configured to be a smaller percentage of the range.
    '''
    HIGH_HYSTERESIS = 1114
    r'''
    Optimized for noisy signals to minimize frequent and unpredictable range changes. Thresholds are configured to be a larger percentage of the range.
    '''
    MEDIUM_HYSTERESIS = 1115
    r'''
    Optimized for noisy signals to minimize frequent and unpredictable range changes. Thresholds are configured to be a medium percentage of the range.
    '''
    HOLD = 1116
    r'''
    Attempt to maintain the active range. Thresholds will favor the active range.
    '''


class CableLength(Enum):
    ZERO_M = 1121
    r'''
    Uses predefined cable compensation data for a 0m cable (direct connection).
    '''
    NI_STANDARD_1M = 1122
    r'''
    Uses predefined cable compensation data for an NI standard 1m coaxial cable.
    '''
    NI_STANDARD_2M = 1123
    r'''
    Uses predefined cable compensation data for an NI standard 2m coaxial cable.
    '''
    NI_STANDARD_4M = 1124
    r'''
    Uses predefined cable compensation data for an NI standard 4m coaxial cable.
    '''
    CUSTOM_ONBOARD_STORAGE = 1125
    r'''
    Uses previously generated custom cable compensation data from onboard storage. Only the most recently performed compensation data for each custom cable compensation type (open, short) is stored.
    '''
    CUSTOM_AS_CONFIGURED = 1126
    r'''
    Uses the custom cable compensation data supplied to configure_lcr_custom_cable_compensation. Use this option to manage multiple sets of custom cable compensation data.
    '''
    NI_STANDARD_TRIAXIAL_1M = 1139
    r'''
    Uses predefined cable compensation data for an NI standard 1m triaxial cable.
    '''
    NI_STANDARD_TRIAXIAL_2M = 1140
    r'''
    Uses predefined cable compensation data for an NI standard 2m triaxial cable.
    '''
    NI_STANDARD_TRIAXIAL_4M = 1141
    r'''
    Uses predefined cable compensation data for an NI standard 4m triaxial cable.
    '''


class ComplianceLimitSymmetry(Enum):
    SYMMETRIC = 0
    r'''
    Compliance limits are specified symmetrically about 0.
    '''
    ASYMMETRIC = 1
    r'''
    Compliance limits can be specified asymmetrically with respect to 0.
    '''


class DCNoiseRejection(Enum):
    SECOND_ORDER = 1043
    r'''
    Second-order rejection of DC noise.
    '''
    NORMAL = 1044
    r'''
    Normal rejection of DC noise.
    '''


class Event(Enum):
    SOURCE_COMPLETE = 1030
    MEASURE_COMPLETE = 1031
    SEQUENCE_ITERATION_COMPLETE = 1032
    SEQUENCE_ENGINE_DONE = 1033
    PULSE_COMPLETE = 1051
    READY_FOR_PULSE_TRIGGER = 1052


class InstrumentMode(Enum):
    SMU_PS = 1061
    r'''
    The channel operates as an SMU/power supply.
    '''
    LCR = 1062
    r'''
    The channel operates as an LCR meter.
    '''


class _IsolationState(Enum):
    ISOLATED = 1128
    r'''
    The channel is disconnected from chassis ground.
    '''
    NON_ISOLATED = 1129
    r'''
    The channel is connected to chassis ground.
    '''


class LCRCompensationType(Enum):
    OPEN = 1130
    r'''
    Open LCR compensation.
    '''
    SHORT = 1131
    r'''
    Short LCR compensation.
    '''
    LOAD = 1132
    r'''
    Load LCR compensation.
    '''
    OPEN_CUSTOM_CABLE = 1133
    r'''
    Open custom cable compensation.
    '''
    SHORT_CUSTOM_CABLE = 1134
    r'''
    Short custom cable compensation.
    '''


class LCRDCBiasSource(Enum):
    OFF = 1065
    r'''
    Disables DC bias in LCR mode.
    '''
    VOLTAGE = 1066
    r'''
    Applies a constant voltage bias, as defined by the lcr_dc_bias_voltage_level property.
    '''
    CURRENT = 1067
    r'''
    Applies a constant current bias, as defined by the lcr_dc_bias_current_level property.
    '''


class _LCRImpedanceAutoRange(Enum):
    OFF = 1068
    ON = 1070


class LCRImpedanceRangeSource(Enum):
    IMPEDANCE_RANGE = 1142
    r'''
    Uses the impedance range you specify with the lcr_impedance_range property.
    '''
    LOAD_CONFIGURATION = 1143
    r'''
    Computes the impedance range to select based on the values you supply to the lcr_load_resistance, lcr_load_inductance, and lcr_load_capacitance properties. NI-DCPower uses a series model of load resistance, load inductance, and load capacitance to compute the impedance range.
    '''


class LCRMeasurementTime(Enum):
    SHORT = 1071
    r'''
    Uses a short aperture time for LCR measurements.
    '''
    MEDIUM = 1072
    r'''
    Uses a medium aperture time for LCR measurements.
    '''
    LONG = 1073
    r'''
    Uses a long aperture time for LCR measurements.
    '''
    CUSTOM = 1117
    r'''
    Uses a custom aperture time for LCR measurements as specified by the lcr_custom_measurement_time property.
    '''


class LCROpenShortLoadCompensationDataSource(Enum):
    ONBOARD_STORAGE = 1074
    r'''
    Uses previously generated LCR compensation data. Only the most recently performed compensation data for each LCR compensation type (open, short, and load) is stored.
    '''
    AS_DEFINED = 1075
    r'''
    Uses the LCR compensation data represented by the relevant LCR compensation properties as generated by perform_lcr_open_compensation, perform_lcr_short_compensation, and perform_lcr_load_compensation. Use this option to manage multiple sets of LCR compensation data. This option applies compensation data from the following properties: lcr_open_conductance, lcr_open_susceptance, lcr_short_resistance, lcr_short_reactance, lcr_measured_load_resistance, lcr_measured_load_reactance, lcr_actual_load_resistance, lcr_actual_load_reactance.
    '''


class LCRReferenceValueType(Enum):
    IMPEDANCE = 1076
    r'''
    The actual impedance, comprising real resistance and imaginary reactance, of your DUT. Supply resistance, in ohms, to reference value A; supply reactance, in ohms, to reference value B.
    '''
    IDEAL_CAPACITANCE = 1077
    r'''
    The ideal capacitance of your DUT. Supply capacitance, in farads, to reference value A.
    '''
    IDEAL_INDUCTANCE = 1078
    r'''
    The ideal inductance of your DUT. Supply inductance, in henrys, to reference value A.
    '''
    IDEAL_RESISTANCE = 1079
    r'''
    The ideal resistance of your DUT. Supply resistance, in ohms, to reference value A.
    '''


class LCRSourceDelayMode(Enum):
    AUTOMATIC = 1144
    r'''
    NI-DCPower automatically applies source delay of sufficient duration to account for settling time.
    '''
    MANUAL = 1145
    r'''
    NI-DCPower applies the source delay that you set manually with source_delay. You can use this option to set a shorter delay to reduce measurement time at the possible expense of measurement accuracy.
    '''


class LCRStimulusFunction(Enum):
    VOLTAGE = 1063
    r'''
    Applies an AC voltage for LCR stimulus.
    '''
    CURRENT = 1064
    r'''
    Applies an AC current for LCR stimulus.
    '''


class MeasureWhen(Enum):
    AUTOMATICALLY_AFTER_SOURCE_COMPLETE = 1025
    r'''
    Acquires a measurement after each Source Complete event completes.
    '''
    ON_DEMAND = 1026
    r'''
    Acquires a measurement when the measure method or measure_multiple method is called.
    '''
    ON_MEASURE_TRIGGER = 1027
    r'''
    Acquires a measurement when a Measure trigger is received.
    '''


class MeasurementTypes(Enum):
    CURRENT = 0
    r'''
    The device measures current.
    '''
    VOLTAGE = 1
    r'''
    The device measures voltage.
    '''


class OutputCapacitance(Enum):
    LOW = 1010
    r'''
    Output Capacitance is low.
    '''
    HIGH = 1011
    r'''
    Output Capacitance is high.
    '''


class OutputCutoffReason(Enum):
    ALL = -1
    r'''
    Queries any output cutoff condition; clears all output cutoff conditions.
    '''
    VOLTAGE_OUTPUT_HIGH = 1
    r'''
    Queries or clears cutoff conditions when the output exceeded the high cutoff limit for voltage output.
    '''
    VOLTAGE_OUTPUT_LOW = 2
    r'''
    Queries or clears cutoff conditions when the output fell below the low cutoff limit for voltage output.
    '''
    CURRENT_MEASURE_HIGH = 4
    r'''
    Queries or clears cutoff conditions when the measured current exceeded the high cutoff limit for current output.
    '''
    CURRENT_MEASURE_LOW = 8
    r'''
    Queries or clears cutoff conditions when the measured current fell below the low cutoff limit for current output.
    '''
    VOLTAGE_CHANGE_HIGH = 16
    r'''
    Queries or clears cutoff conditions when the voltage slew rate increased beyond the positive change cutoff for voltage output.
    '''
    VOLTAGE_CHANGE_LOW = 32
    r'''
    Queries or clears cutoff conditions when the voltage slew rate decreased beyond the negative change cutoff for voltage output.
    '''
    CURRENT_CHANGE_HIGH = 64
    r'''
    Queries or clears cutoff conditions when the current slew rate increased beyond the positive change cutoff for current output.
    '''
    CURRENT_CHANGE_LOW = 128
    r'''
    Queries or clears cutoff conditions when the current slew rate decreased beyond the negative change cutoff for current output.
    '''


class OutputFunction(Enum):
    DC_VOLTAGE = 1006
    r'''
    Sets the output method to DC voltage.
    '''
    DC_CURRENT = 1007
    r'''
    Sets the output method to DC current.
    '''
    PULSE_VOLTAGE = 1049
    r'''
    Sets the output method to pulse voltage.
    '''
    PULSE_CURRENT = 1050
    r'''
    Sets the output method to pulse current.
    '''


class OutputStates(Enum):
    VOLTAGE = 0
    r'''
    The device maintains a constant voltage by adjusting the current
    '''
    CURRENT = 1
    r'''
    The device maintains a constant current by adjusting the voltage.
    '''


class Polarity(Enum):
    HIGH = 1018
    r'''
    A high pulse occurs when the event is generated.  The exported signal is low level both before and after the event is generated.
    '''
    LOW = 1019
    r'''
    A low pulse occurs when the event is generated.  The exported signal is high level both before and after the event is generated.
    '''


class PowerAllocationMode(Enum):
    DISABLED = 1058
    r'''
    The device attempts to source, on each active channel, the power that the present source configuration requires; NI-DCPower does not perform a sourcing power check. If the required power is greater than the maximum sourcing power, the device attempts to source the required amount and may shut down to prevent damage.
    '''
    AUTOMATIC = 1059
    r'''
    The device attempts to source, on each active channel, the power that the present source configuration requires; NI-DCPower performs a sourcing power check. If the required power is greater than the maximum sourcing power, the device does not exceed the maximum power, and NI-DCPower returns an error.
    '''
    MANUAL = 1060
    r'''
    The device attempts to source, on each active channel, the power you request with the requested_power_allocation property; NI-DCPower performs a sourcing power check. If the requested power is either less than the required power for the present source configuration or greater than the maximum sourcing power, the device does not exceed the requested or allowed power, respectively, and NI-DCPower returns an error.
    '''


class PowerSource(Enum):
    INTERNAL = 1003
    r'''
    Uses the PXI chassis power source.
    '''
    AUXILIARY = 1004
    r'''
    Uses the auxiliary power source connected to the device.
    '''
    AUTOMATIC = 1005
    r'''
    Uses the auxiliary power source if it is available; otherwise uses the PXI chassis power source.
    '''


class PowerSourceInUse(Enum):
    INTERNAL = 1003
    r'''
    Uses the PXI chassis power source.
    '''
    AUXILIARY = 1004
    r'''
    Uses the auxiliary power source connected to the device. Only the NI PXI-4110,  NI PXIe-4112, NI PXIe-4113, and NI PXI-4130 support this value. This is the only supported value  for the NI PXIe-4112 and NI PXIe-4113.
    '''


class SelfCalibrationPersistence(Enum):
    KEEP_IN_MEMORY = 1045
    r'''
    Keep new self calibration values in memory only.
    '''
    WRITE_TO_EEPROM = 1046
    r'''
    Write new self calibration values to hardware.
    '''


class SendSoftwareEdgeTriggerType(Enum):
    START = 1034
    SOURCE = 1035
    MEASURE = 1036
    SEQUENCE_ADVANCE = 1037
    PULSE = 1053
    SHUTDOWN = 1118


class Sense(Enum):
    LOCAL = 1008
    r'''
    Local sensing is selected.
    '''
    REMOTE = 1009
    r'''
    Remote sensing is selected.
    '''


class SourceMode(Enum):
    SINGLE_POINT = 1020
    r'''
    The source unit applies a single source configuration.
    '''
    SEQUENCE = 1021
    r'''
    The source unit applies a list of voltage or current configurations sequentially.
    '''


class TransientResponse(Enum):
    NORMAL = 1038
    r'''
    The output responds to changes in load at a normal speed.
    '''
    FAST = 1039
    r'''
    The output responds to changes in load quickly.
    '''
    SLOW = 1041
    r'''
    The output responds to changes in load slowly.
    '''
    CUSTOM = 1042
    r'''
    The output responds to changes in load based on specified values.
    '''


class TriggerType(Enum):
    NONE = 1012
    r'''
    No trigger is configured.
    '''
    DIGITAL_EDGE = 1014
    r'''
    The data operation starts when a digital edge is detected.
    '''
    SOFTWARE_EDGE = 1015
    r'''
    The data operation starts when a software trigger occurs.
    '''
