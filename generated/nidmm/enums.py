# This file was generated


from enum import Enum

class ApertureTimeUnits(Enum):
    SECONDS = 0
    POWER_LINE_CYCLES = 1
    RAW_SAMPLES = 2

class AcquisitionStatus(Enum):
    RUNNING = 0
    FINISHED_WITH_BACKLOG = 1
    FINISHED_WITH_NO_BACKLOG = 2
    PAUSED = 3
    NO_ACQUISITION_IN_PROGRESS = 4

class WaveformCouplingMode(Enum):
    WAVEFORM_COUPLING_AC = 0
    WAVEFORM_COUPLING_DC = 1

class OperationMode(Enum):
    DMM_MODE = 0
    WAVEFORM_MODE = 1

class EnabledSetting(Enum):
    AUTO = -1
    OFF = 0
    ON = 1
    ONCE = 2

class Slope(Enum):
    POSITIVE = 0
    NEGATIVE = 1

class TemperatureThermistorType(Enum):
    THERMISTOR_CUSTOM = 0
    THERMISTOR_44004 = 1
    THERMISTOR_44006 = 2
    THERMISTOR_44007 = 3

class CurrentSource(Enum):
    ONE_MICRO_AMP = 1e-06
    TEN_MICRO_AMP = 1e-05
    HUNDRED_MICRO_AMP = 0.0001
    ONE_MILLI_AMP = 0.001

class LCCalculationModel(Enum):
    CALC_MODEL_AUTO = -1
    CALC_MODEL_SERIES = 0
    CALC_MODEL_PARALLEL = 1

class Function(Enum):
    DC_VOLTS = 1
    AC_VOLTS = 2
    DC_CURRENT = 3
    AC_CURRENT = 4
    RES_2_WIRE = 5
    RES_4_WIRE = 101
    FREQ = 104
    PERIOD = 105
    TEMPERATURE = 108
    AC_VOLTS_DC_COUPLED = 1001
    DIODE = 1002
    WAVEFORM_VOLTAGE = 1003
    WAVEFORM_CURRENT = 1004
    CAPACITANCE = 1005
    INDUCTANCE = 1006

class TemperatureThermocoupleType(Enum):
    B = 1
    E = 4
    J = 6
    K = 7
    N = 8
    R = 9
    S = 10
    T = 11

class CableCompensationType(Enum):
    CABLE_COMP_NONE = 0
    CABLE_COMP_OPEN = 1
    CABLE_COMP_SHORT = 2
    CABLE_COMP_OPEN_AND_SHORT = 3

class TemperatureTransducerType(Enum):
    THERMOCOUPLE = 1
    THERMISTOR = 2
    TWO_WIRE_RTD = 3
    FOUR_WIRE_RTD = 4

class TemperatureRTDType(Enum):
    CustomRTD = 0
    PT3750 = 1
    PT3851 = 2
    PT3911 = 3
    PT3916 = 4
    PT3920 = 5
    PT3928 = 6

class TemperatureThermocoupleReferenceJunctionType(Enum):
    Fixed = 2

class DCNoiseRejectionMode(Enum):
    DCNR_AUTO = -1
    DCNR_NORMAL = 0
    DCNR_SECOND_ORDERT = 1
    DCNR_HIGH_ORDER = 2

class Terminal(Enum):
    NONE          = -1
    IMMEDIATE     = 1
    EXTERNAL      = 2
    SOFTWARE_TRIG = 3
    PXI_TRIG0     = 111
    PXI_TRIG1     = 112
    PXI_TRIG2     = 113
    PXI_TRIG3     = 114
    PXI_TRIG4     = 115
    PXI_TRIG5     = 116
    PXI_TRIG6     = 117
    PXI_TRIG7     = 118
    PXI_STAR      = 131
    AUX_TRIG1     = 1001
    INTERVAL      = 10

