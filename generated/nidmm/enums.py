# This file was generated

from enum import Enum


class ADCCalibration(Enum):
    AUTO = -1
    OFF = 0
    ON = 1


class AcquisitionStatus(Enum):
    RUNNING = 0
    FINISHED_WITH_BACKLOG = 1
    FINISHED_WITH_NO_BACKLOG = 2
    PAUSED = 3
    NO_ACQUISITION_IN_PROGRESS = 4


class ApertureTimeUnits(Enum):
    SECONDS = 0
    POWER_LINE_CYCLES = 1


class AutoZero(Enum):
    AUTO = -1
    OFF = 0
    ON = 1
    ONCE = 2


class CableCompensationType(Enum):
    NONE = 0
    OPEN = 1
    SHORT = 2
    OPEN_AND_SHORT = 3


class CurrentSource(Enum):
    _1_MICROAMP = 1e-06
    _10_MICROAMP = 1e-05
    _100_MICROAMP = 0.0001
    _1_MILLIAMP = 0.001


class DCBias(Enum):
    DC_BIAS_OFF = 0
    DC_BIAS_ON = 1


class DCNoiseRejection(Enum):
    AUTO = -1
    NORMAL = 0
    SECOND_ORDER = 1
    HIGH_ORDER = 2


class DigitsResolution(Enum):
    _3_5 = 3.5
    _4_5 = 4.5
    _5_5 = 5.5
    _6_5 = 6.5
    _7_5 = 7.5


class Function(Enum):
    DC_VOLTS = 1
    AC_VOLTS = 2
    DC_CURRENT = 3
    AC_CURRENT = 4
    _2_WIRE_RESISTANCE = 5
    _4_WIRE_RESISTANCE = 101
    FREQUENCY = 104
    PERIOD = 105
    TEMPERATURE = 108
    _AC_VOLTS_DC_COUPLED = 1001
    DIODE = 1002
    WAVEFORM_VOLTAGE = 1003
    _WAVEFORM_CURRENT = 1004
    CAPACITANCE = 1005
    INDUCTANCE = 1006


class InputResistance(Enum):
    _1_M_OHM = 1000000.0
    _10_M_OHM = 10000000.0
    GREATER_THAN_10_G_OHM = 10000000000.0


class LCCalculationModel(Enum):
    AUTO = -1
    SERIES = 0
    PARALLEL = 1


class MeasurementCompleteDest(Enum):
    NONE = -1
    EXTERNAL = 2
    TTL_0 = 111
    TTL_1 = 112
    TL_2 = 113
    TTL_3 = 114
    TL_4 = 115
    TTL_5 = 116
    TTL_6 = 117
    TTL_7 = 118
    _LBR_TRIG_0 = 1003


class MeasurementDestinationSlope(Enum):
    POSITIVE = 0
    NEGATIVE = 1


class OffsetCompensatedOhms(Enum):
    OFF = 0
    ON = 1


class OperationMode(Enum):
    _IVIDMM_MODE = 0
    WAVEFORM_MODE = 1


class PowerlineFrequency(Enum):
    _50_HZ = 50.0
    _60_HZ = 60.0


class RTDType(Enum):
    CUSTOM = 0
    PT_3750 = 1
    PT_3851 = 2
    PT_3911 = 3
    PT_3916 = 4
    PT_3920 = 5
    PT_3928 = 6


class SampleTrigSlope(Enum):
    POSITIVE = 0
    NEGATIVE = 1


class SampleTrigger(Enum):
    IMMEDIATE = 1
    _EXTERNAL = 2
    SOFTWARE_TRIG = 3
    INTERVAL = 10
    TTL_0 = 111
    TTL_1 = 112
    TTL_2 = 113
    _TTL_3 = 114
    TTL_4 = 115
    TTL_5 = 116
    TTL_6 = 117
    TTL_7 = 118
    PXI_STAR = 131
    AUX_TRIG_1 = 1001
    LBR_TRIG_1 = 1004


class ThermistorType(Enum):
    CUSTOM = 0
    _44004 = 1
    _44006 = 2
    _44007 = 3


class ThermocoupleReferenceJunctionType(Enum):
    FIXED = 2


class ThermocoupleType(Enum):
    B = 1
    E = 4
    J = 6
    K = 7
    N = 8
    R = 9
    S = 10
    T = 11


class TransducerType(Enum):
    THERMOCOUPLE = 1
    THERMISTOR = 2
    _2_WIRE_RTD = 3
    _4_WIRE_RTD = 4


class TriggerSlope(Enum):
    POSITIVE = 0
    NEGATIVE = 1


class TriggerSource(Enum):
    IMMEDIATE = 1
    EXTERNAL = 2
    SOFTWARE_TRIG = 3
    _TTL_0 = 111
    TTL_1 = 112
    TTL_2 = 113
    _TTL_3 = 114
    TTL_4 = 115
    TTL_5 = 116
    TTL_6 = 117
    _TTL_7 = 118
    _PXI_STAR = 131
    AUX_TRIG_1 = 1001
    LBR_TRIG_1 = 1004


class WaveformCoupling(Enum):
    AC = 0
    DC = 1
