# -*- coding: utf-8 -*-
# This file was generated

from enum import Enum


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
