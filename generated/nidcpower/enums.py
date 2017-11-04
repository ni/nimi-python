# This file was generated

from enum import Enum


class ApertureTimeUnits(Enum):
    SECONDS = 1028
    '''
    Specifies aperture time in seconds. NIDCPOWER_VAL_POWER_LINE_CYCLES (1029) Specifies aperture time in power line cycles (PLCs).
    '''
    POWER_LINE_CYCLES = 1029
    '''
    Specifies aperture time in power line cycles (PLCs).
    '''


class AutoZero(Enum):
    OFF = 0
    '''
    Disables auto zero. NIDCPOWER_VAL_ONCE (1024) Makes zero conversions following the first measurement after initiating the device.  The device uses these zero conversions for the preceding measurement and future  measurements until the device is reinitiated.
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
    Autoranging is disabled.
    '''
    ON = 1
    '''
    Autoranging is enabled.
    '''


class CurrentLimitAutorange(Enum):
    OFF = 0
    '''
    Autoranging is disabled.
    '''
    ON = 1
    '''
    Autoranging is enabled.
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
    DC_NOISE_REJECTION_NORMAL = 1044
    '''
    Normal rejection of DC noise. NIDCPOWER_VAL_DC_NOISE_REJECTION_SECOND_ORDER (1043) Second-order rejection of DC noise.
    '''


class DigitalEdge(Enum):
    RISING = 1016
    '''
    Asserts the trigger on the rising edge of the digital signal. NIDCPOWER_VAL_FALLING (1017) Asserts the trigger on the falling edge of the digital signal.
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
    Acquires a measurement after each Source Complete event completes. NIDCPOWER_VAL_ON_DEMAND (1026) Acquires a measurement when the niDCPower_Measure function or niDCPower_MeasureMultiple function is called. NIDCPOWER_VAL_ON_MEASURE_TRIGGER (1027) Acquires a measurement when a Measure trigger is received.
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


class OutputCapacitance(Enum):
    LOW = 1010
    '''
    Output Capacitance is low. NIDCPOWER_VAL_HIGH (1011) Output Capacitance is high.
    '''
    HIGH = 1011
    '''
    Output capacitance is high.
    '''


class OutputFunction(Enum):
    DC_VOLTAGE = 1006
    '''
    Sets the output function to DC voltage. NIDCPOWER_VAL_DC_CURRENT (1007) Sets the output function to DC current. NIDCPOWER_VAL_PULSE_VOLTAGE (1049)   NIDCPOWER_VAL_PULSE_CURRENT (1050)
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


class Polarity(Enum):
    ACTIVE_HIGH = 1018
    '''
    A high pulse occurs when the event is generated.  The exported signal is low level both before and after the event is generated. NIDCPOWER_VAL_ACTIVE_LOW (1019) A low pulse occurs when the event is generated.  The exported signal is high level both before and after the event is generated.
    '''
    ACTIVE_LOW = 1019
    '''
    A low pulse occurs when the event is generated. The exported signal is
    high level both before and after the event is generated.
    '''


class PowerLineFrequency(Enum):
    _50_HERTZ = 50.0
    '''
    Specifies a power line frequency of 50 Hz. NIDCPOWER_VAL_60_HERTZ (60.0) Specifies a power line frequency of 60 Hz.
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
    Local sensing is selected. NIDCPOWER_VAL_REMOTE (1009) Remote sensing is selected.
    '''
    REMOTE = 1009
    '''
    Remote sensing is selected.
    '''


class SourceMode(Enum):
    SINGLE_POINT = 1020
    '''
    The source unit applies a single source configuration. NIDCPOWER_VAL_SEQUENCE (1021) The source unit applies a list of voltage or current configurations sequentially.
    '''
    SEQUENCE = 1021
    '''
    The source unit sequentially applies a list of voltage or current
    configurations.
    '''


class TransientResponse(Enum):
    NORMAL = 1038
    '''
    The output responds to changes in load at a normal speed. NIDCPOWER_VAL_FAST (1039) The output responds to changes in load quickly. NIDCPOWER_VAL_SLOW (1041) The output responds to changes in load slowly. NIDCPOWER_VAL_CUSTOM (1042) The output responds to changes in load based on specified values.
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
    No trigger is configured. NIDCPOWER_VAL_DIGITAL_EDGE (1014) The data operation starts when a digital edge is detected. NIDCPOWER_VAL_SOFTWARE_EDGE (1015) The data operation starts when a software trigger occurs.
    '''
    DIGITAL_EDGE = 1014
    '''
    The data operation starts when a digital edge is detected. NIDCPOWER_VAL_SOFTWARE_EDGE (1015) The data operation starts when a software trigger occurs.
    '''
    SOFTWARE_EDGE = 1015
    '''
    The data operation starts when a software trigger occurs.
    '''


class VoltageLevelAutorange(Enum):
    OFF = 0
    '''
    Autoranging is disabled.
    '''
    ON = 1
    '''
    Autoranging is enabled.
    '''


class VoltageLimitAutorange(Enum):
    OFF = 0
    '''
    Autoranging is disabled.
    '''
    ON = 1
    '''
    Autoranging is enabled.
    '''
