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
    Disables auto-zero.
    '''
    ON = 1
    '''
    Makes zero conversions for every measurement.
    '''
    ONCE = 1024
    '''
    Makes zero conversions following the first measurement after initiating
    the device. The device uses these zero conversions for the preceding
    measurement and future measurements until the device is reinitiated.
    '''


class CurrentLevelAutorange(Enum):
    OFF = 0
    '''
    NI-DCPower does not automatically select the current level range.
    '''
    ON = 1
    '''
    NI-DCPower automatically selects the current level range.
    '''


class CurrentLimitAutorange(Enum):
    OFF = 0
    '''
    NI-DCPower does not automatically select the current limit range.
    '''
    ON = 1
    '''
    NI-DCPower automatically selects the current limit range.
    '''


class CurrentLimitBehavior(Enum):
    CURRENT_REGULATE = 13613
    CURRENT_TRIP = 13614


class DCNoiseRejection(Enum):
    SECOND_ORDER = 1043
    '''
    Second-order DC noise rejection. Refer to `Configuring the Measure
    Unit <NI_DC_Power_Supplies_Help.chm::/ConfiguringTheMeasureUnit.html>`__
    for supported devices.
    '''
    NORMAL = 1044
    '''
    Normal DC noise rejection.
    '''


class DigitalEdge(Enum):
    RISING = 1016
    '''
    Asserts the trigger on the rising edge of the digital signal.
    '''
    FALLING = 1017
    '''
    Asserts the trigger on the falling edge of the digital signal.
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
    Acquires a measurement after each Source Complete event completes. Use
    the `niDCPower Fetch
    Multiple <NIDCPowerVIRef.chm::/niDCPower_Fetch_Multiple.html>`__ VI to
    retrieve the measurements.
    '''
    ON_DEMAND = 1026
    '''
    Acquires a measurement when the `niDCPower
    Measure <NIDCPowerVIRef.chm::/niDCPower_Measure.html>`__ VI or
    `niDCPower Measure
    Multiple <NIDCPowerVIRef.chm::/niDCPower_Measure_Multiple.html>`__ VI is
    called.
    '''
    ON_MEASURE_TRIGGER = 1027
    '''
    Acquires a measurement when a Measure trigger is received. Use the
    `niDCPower Fetch
    Multiple <NIDCPowerVIRef.chm::/niDCPower_Fetch_Multiple.html>`__ VI to
    retrieve the measurements.
    '''


class MeasurementTypes(Enum):
    MEASURE_CURRENT = 0
    '''
    The device measures current.
    '''
    MEASURE_VOLTAGE = 1
    '''
    The device measures voltage.
    '''


class OutputCapacitance(Enum):
    LOW = 1010
    '''
    Output capacitance is low.
    '''
    HIGH = 1011
    '''
    Output capacitance is high.
    '''


class OutputFunction(Enum):
    DC_VOLTAGE = 1006
    '''
    Sets the output function to DC voltage.
    '''
    DC_CURRENT = 1007
    '''
    Sets the output function to DC current.
    '''
    PULSE_VOLTAGE = 1049
    '''
    Sets the output function to pulse voltage.
    '''
    PULSE_CURRENT = 1050
    '''
    Sets the output function to pulse current.
    '''


class OutputStates(Enum):
    OUTPUT_CONSTANT_VOLTAGE = 0
    '''
    The device maintains a constant voltage by adjusting the current
    '''
    OUTPUT_CONSTANT_CURRENT = 1
    '''
    The device maintains a constant current by adjusting the voltage.
    '''


class Polarity(Enum):
    ACTIVE_HIGH = 1018
    '''
    A high pulse occurs when the event is generated. The exported signal is
    low level both before and after the event is generated.
    '''
    ACTIVE_LOW = 1019
    '''
    A low pulse occurs when the event is generated. The exported signal is
    high level both before and after the event is generated.
    '''


class PowerLineFrequency(Enum):
    _50_HERTZ = 50.0
    '''
    Specifies a power line frequency of 50 Hz.
    '''
    _60_HERTZ = 60.0
    '''
    Specifies a power line frequency of 60 Hz.
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
    Uses the auxiliary power source if it is available; otherwise, use the
    PXI chassis power source.
    '''


class PowerSourceInUse(Enum):
    INTERNAL = 1003
    '''
    Uses the PXI chassis power source.
    '''
    AUXILIARY = 1004
    '''
    Uses the auxiliary power source connected to the device. Only the NI
    PXI-4110, NI PXIe-4112, NI PXIe-4113, and NI PXI-4130 support this
    value. This is the only supported value for the NI PXIe-4112 and NI
    PXIe-4113.
    '''


class SelfCalibrationPersistence(Enum):
    KEEP_IN_MEMORY = 1045
    '''
    Keep new self-calibration values in memory only.
    '''
    WRITE_TO_EEPROM = 1046
    '''
    Write new self-calibration values to hardware. Refer to your device
    documentation for more information about the implications of frequent
    writes to the EEPROM.
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
    The source unit sequentially applies a list of voltage or current
    configurations.
    '''


class TransientResponse(Enum):
    NORMAL = 1038
    '''
    Normal transient response time.
    '''
    FAST = 1039
    '''
    Fast transient response time.
    '''
    SLOW = 1041
    '''
    Slow transient response time. Refer to `Configuring Transient
    Response <NI_DC_Power_Supplies_Help.chm::/CompensatingforLoad.html>`__
    for supported devices.
    '''
    CUSTOM = 1042
    '''
    Custom transient response time. If you select this value, you can then
    specify values for the `Voltage Gain
    Bandwidth <pniDCPower_VoltageGainBandwidth.html>`__, `Voltage
    Compensation
    Frequency <pniDCPower_VoltageCompensationFrequency.html>`__, `Voltage
    Pole-Zero Frequency <pniDCPower_VoltagePoleZeroRatio.html>`__, `Current
    Gain Bandwidth <pniDCPower_CurrentGainBandwidth.html>`__, `Current
    Compensation
    Frequency <pniDCPower_CurrentCompensationFrequency.html>`__, and
    `Current Pole-Zero Ratio <pniDCPower_CurrentPoleZeroRatio.html>`__
    properties. Refer to `Configuring Transient
    Response <NI_DC_Power_Supplies_Help.chm::/CompensatingforLoad.html>`__
    for supported devices.
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


class VoltageLevelAutorange(Enum):
    OFF = 0
    '''
    NI-DCPower does not automatically select the voltage level range.
    '''
    ON = 1
    '''
    NI-DCPower automatically selects the voltage level range.
    '''


class VoltageLimitAutorange(Enum):
    OFF = 0
    '''
    NI-DCPower does not automatically select the voltage limit range.
    '''
    ON = 1
    '''
    NI-DCPower automatically selects the voltage limit range.
    '''
