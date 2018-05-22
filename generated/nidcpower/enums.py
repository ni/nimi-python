# This file was generated

from enum import Enum


class ApertureTimeUnits(Enum):
    SECONDS = 1028
    '''
    Specifies aperture time in seconds.
    '''
    POWER_LINE_CYCLES = 1029
    '''
    Specifies aperture time in power line cycles (PLCs).
    '''


class AutoZero(Enum):
    OFF = 0
    '''
    Disables auto zero.
    '''
    ON = 1
    '''
    Makes zero conversions for every measurement.
    '''
    ONCE = 1024
    '''
    Makes zero conversions following the first measurement after initiating the device.  The device uses these zero conversions for the preceding measurement and future  measurements until the device is reinitiated.
    '''


class ComplianceLimitSymmetry(Enum):
    SYMMETRIC = 0
    '''
    Compliance limits are specified symmetrically about 0.
    '''
    ASYMMETRIC = 1
    '''
    Compliance limits can be specified asymmetrically with respect to 0.
    '''


class DCNoiseRejection(Enum):
    SECOND_ORDER = 1043
    '''
    Second-order rejection of DC noise.
    '''
    NORMAL = 1044
    '''
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
    '''
    Acquires a measurement after each Source Complete event completes.
    '''
    ON_DEMAND = 1026
    '''
    Acquires a measurement when the measure method or measure_multiple method is called.
    '''
    ON_MEASURE_TRIGGER = 1027
    '''
    Acquires a measurement when a Measure trigger is received.
    '''


class MeasurementTypes(Enum):
    CURRENT = 0
    '''
    The device measures current.
    '''
    VOLTAGE = 1
    '''
    The device measures voltage.
    '''


class OutputCapacitance(Enum):
    LOW = 1010
    '''
    Output Capacitance is low.
    '''
    HIGH = 1011
    '''
    Output Capacitance is high.
    '''


class OutputFunction(Enum):
    DC_VOLTAGE = 1006
    '''
    Sets the output method to DC voltage.
    '''
    DC_CURRENT = 1007
    '''
    Sets the output method to DC current.
    '''
    PULSE_VOLTAGE = 1049
    '''
    Sets the output method to pulse voltage.
    '''
    PULSE_CURRENT = 1050
    '''
    Sets the output method to pulse current.
    '''


class OutputStates(Enum):
    VOLTAGE = 0
    '''
    The device maintains a constant voltage by adjusting the current
    '''
    CURRENT = 1
    '''
    The device maintains a constant current by adjusting the voltage.
    '''


class Polarity(Enum):
    HIGH = 1018
    '''
    A high pulse occurs when the event is generated.  The exported signal is low level both before and after the event is generated.
    '''
    LOW = 1019
    '''
    A low pulse occurs when the event is generated.  The exported signal is high level both before and after the event is generated.
    '''


class PowerSource(Enum):
    INTERNAL = 1003
    '''
    Uses the PXI chassis power source.
    '''
    AUXILIARY = 1004
    '''
    Uses the auxiliary power source connected to the device.
    '''
    AUTOMATIC = 1005
    '''
    Uses the auxiliary power source if it is available; otherwise uses the PXI chassis power source.
    '''


class PowerSourceInUse(Enum):
    INTERNAL = 1003
    '''
    Uses the PXI chassis power source.
    '''
    AUXILIARY = 1004
    '''
    Uses the auxiliary power source connected to the device. Only the NI PXI-4110,  NI PXIe-4112, NI PXIe-4113, and NI PXI-4130 support this value. This is the only supported value  for the NI PXIe-4112 and NI PXIe-4113.
    '''


class SelfCalibrationPersistence(Enum):
    KEEP_IN_MEMORY = 1045
    '''
    Keep new self calibration values in memory only.
    '''
    WRITE_TO_EEPROM = 1046
    '''
    Write new self calibration values to hardware.
    '''


class SendSoftwareEdgeTriggerType(Enum):
    START = 1034
    SOURCE = 1035
    MEASURE = 1036
    SEQUENCE_ADVANCE = 1037
    PULSE = 1053


class Sense(Enum):
    LOCAL = 1008
    '''
    Local sensing is selected.
    '''
    REMOTE = 1009
    '''
    Remote sensing is selected.
    '''


class SourceMode(Enum):
    SINGLE_POINT = 1020
    '''
    The source unit applies a single source configuration.
    '''
    SEQUENCE = 1021
    '''
    The source unit applies a list of voltage or current configurations sequentially.
    '''


class TransientResponse(Enum):
    NORMAL = 1038
    '''
    The output responds to changes in load at a normal speed.
    '''
    FAST = 1039
    '''
    The output responds to changes in load quickly.
    '''
    SLOW = 1041
    '''
    The output responds to changes in load slowly.
    '''
    CUSTOM = 1042
    '''
    The output responds to changes in load based on specified values.
    '''


class TriggerType(Enum):
    NONE = 1012
    '''
    No trigger is configured.
    '''
    DIGITAL_EDGE = 1014
    '''
    The data operation starts when a digital edge is detected.
    '''
    SOFTWARE_EDGE = 1015
    '''
    The data operation starts when a software trigger occurs.
    '''
