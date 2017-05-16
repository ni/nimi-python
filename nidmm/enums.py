#@TODO: Names follow C constant names exactly minus prefix (with a few exceptions).

from enum import Enum

'''
# NIDMM_ATTR_APERTURE_TIME_UNITS
class ApertureTimeUnit(Enum):
    SECONDS           = 0
    POWER_LINE_CYCLES = 1
    RAW_SAMPLES       = 2

# NIDMM_ATTR_CABLE_COMP_TYPE
class CableCompensationType(Enum):
    CABLE_COMP_NONE           = 0
    CABLE_COMP_OPEN           = 1
    CABLE_COMP_SHORT          = 2
    CABLE_COMP_OPEN_AND_SHORT = 3

# NIDMM_ATTR_DC_NOISE_REJECTION
class DCNoiseRejectionMode(Enum):
    DCNR_AUTO         = -1
    DCNR_NORMAL       =  0
    DCNR_SECOND_ORDER =  1
    DCNR_HIGH_ORDER   =  2

# NIDMM_ATTR_ADC_CALIBRATION
# NIDMM_ATTR_OFFSET_COMP_OHMS
# NIDMM_ATTR_AUTO_ZERO
class EnabledSetting(Enum):
    AUTO = -1
    OFF  =  0
    ON   =  1
    ONCE =  2
'''

# NIDMM_ATTR_FUNCTION
class Function(Enum):
    DC_VOLTS            =    1
    AC_VOLTS            =    2
    DC_CURRENT          =    3
    AC_CURRENT          =    4
    RES_2_WIRE          =    5 # Had to put RES_ in front, rather than in back, so name doesn't start with number.
    RES_4_WIRE          =  101 # Had to put RES_ in front, rather than in back, so name doesn't start with number.
    FREQ                =  104
    PERIOD              =  105
    TEMPERATURE         =  108
    AC_VOLTS_DC_COUPLED = 1001
    DIODE               = 1002
    WAVEFORM_VOLTAGE    = 1003
    WAVEFORM_CURRENT    = 1004
    CAPACITANCE         = 1005
    INDUCTANCE          = 1006


'''
# NIDMM_ATTR_LC_CALCULATION_MODEL
class LCCalculationModel(Enum):
    CALC_MODEL_AUTO     = -1
    CALC_MODEL_SERIES   =  0
    CALC_MODEL_PARALLEL =  1

# NIDMM_ATTR_OPERATION_MODE
class OperationMode(Enum):
    DMM_MODE      = 0
    WAVEFORM_MODE = 1

# NIDMM_ATTR_DONE_EVENT_SLOPE
# NIDMM_ATTR_LIST_COMPLETE_EVENT_SLOPE
# NIDMM_ATTR_LIST_TRIGGER_SLOPE
# NIDMM_ATTR_MEAS_DEST_SLOPE
# NIDMM_ATTR_SAMPLE_TRIGGER_SLOPE
# NIDMM_ATTR_STEP_COMPLETE_EVENT_SLOPE
# NIDMM_ATTR_EVENT_COUNTER_TRIGGER_SLOPE
# NIDMM_ATTR_FRONT_END_SCRATCH_MODE_UPDATED_EVENT_SLOPE
# NIDMM_ATTR_INTERNAL_FRONT_END_READY_TRIGGER_SLOPE
# NIDMM_ATTR_INTERNAL_MEASURE_COMPLETE_TRIGGER_SLOPE
# NIDMM_ATTR_INTERNAL_MEASURE_TRIGGER_SLOPE
# NIDMM_ATTR_TRIGGER_SLOPE
class Slope(Enum):
    POSITIVE = 0
    NEGATIVE = 1

# NIDMM_ATTR_TEMP_RTD_TYPE
class TemperatureRTDType(Enum):
    CustomRTD = 0
    PT3750    = 1
    PT3851    = 2
    PT3911    = 3
    PT3916    = 4
    PT3920    = 5
    PT3928    = 6

# NIDMM_ATTR_TEMP_THERMISTOR_TYPE
class TemperatureThermistorType(Enum):
    THERMISTOR_CUSTOM = 0
    THERMINSTOR_44004 = 1
    THERMINSTOR_44006 = 2
    THERMINSTOR_44007 = 3

# NIDMM_ATTR_TEMP_TC_REF_JUNC_TYPE
class TemperatureThermocoupleReferenceJunctionType(Enum):
    Fixed = 2

# NIDMM_ATTR_TEMP_TC_TYPE
class TemperatureThermocoupleType(Enum):
    B =  1
    E =  4
    J =  6
    K =  7
    N =  8
    R =  9
    S = 10
    T = 11

# NIDMM_ATTR_TEMP_TRANSDUCER_TYPE
class TemperatureTransducerType(Enum):
    THERMOCOUPLE = 1
    THERMISTOR   = 2
    RTD_2_WIRE   = 3 # Had to put RTD in front, rather than in back, so name doesn't start with number.
    RTD_4_WIRE   = 4 # Had to put RTD in front, rather than in back, so name doesn't start with number.

# NIDMM_ATTR_WAVEFORM_COUPLING
class WaveformCouplingMode(Enum):
    WAVEFORM_COUPLING_AC = 0
    WAVEFORM_COUPLING_DC = 1
'''
