# This file was generated

from enum import Enum


class ADCCalibration(Enum):
    AUTO = -1
    '''
    The DMM enables or disables ADC calibration based on the configured
    function and resolution.
    '''
    OFF = 0
    '''
    The DMM does not compensate for changes to the gain.
    '''
    ON = 1
    '''
    The DMM measures an internal reference to calculate the correct gain for
    the measurement.
    '''


class AcquisitionStatus(Enum):
    RUNNING = 0
    FINISHED_WITH_BACKLOG = 1
    FINISHED_WITH_NO_BACKLOG = 2
    PAUSED = 3
    NO_ACQUISITION_IN_PROGRESS = 4


class ApertureTimeUnits(Enum):
    SECONDS = 0
    '''
    Units are seconds.
    '''
    POWER_LINE_CYCLES = 1
    '''
    Units are powerline cycles (PLCs).
    '''
    RAW_SAMPLES = 2


class AutoZero(Enum):
    AUTO = -1
    '''
    NI-DMM chooses the Auto Zero setting based on the configured function
    and resolution.
    '''
    OFF = 0
    '''
    Disables AutoZero.
    '''
    ON = 1
    '''
    The DMM internally disconnects the input signal following each
    measurement and takes a zero reading. It then subtracts the zero reading
    from the preceding reading. For NI 4065 devices, Auto Zero is always ON.
    Auto Zero is an integral part of the signal measurement phase and adds
    no extra time to the overall measurement.
    '''
    ONCE = 2
    '''
    The DMM internally disconnects the input signal for the first
    measurement and takes a zero reading. It then subtracts the zero reading
    from the first reading and the following readings. The NI 4060/4065 does
    not support this setting.
    '''


class CableCompensationType(Enum):
    CABLE_COMP_NONE = 0
    '''
    No cable compensation.
    '''
    CABLE_COMP_OPEN = 1
    '''
    Open cable compensation.
    '''
    CABLE_COMP_SHORT = 2
    '''
    Short cable compensation.
    '''
    CABLE_COMP_OPEN_AND_SHORT = 3
    '''
    Open and short cable compensation.
    '''


class CurrentSource(Enum):
    ONE_MICRO_AMP = 1e-06
    '''
    NI 4070/4071/4072 are supported.
    '''
    TEN_MICRO_AMP = 1e-05
    '''
    NI 4080/4081/4082 and NI 4070/4071/4072 are supported.
    '''
    HUNDRED_MICRO_AMP = 0.0001
    '''
    NI 4080/4081/4082, NI 4070/4071/4072, and NI 4065 are supported.
    '''
    ONE_MILLI_AMP = 0.001
    '''
    NI 4080/4081/4082, NI 4070/4071/4072, and NI 4065 are supported.
    '''


class DCNoiseRejectionMode(Enum):
    DCNR_AUTO = -1
    '''
    The driver chooses the DC noise rejection setting based on the
    configured function and resolution.
    '''
    DCNR_NORMAL = 0
    '''
    NI-DMM weighs all samples equally.
    '''
    DCNR_SECOND_ORDERT = 1
    '''
    NI-DMM weighs the samples taken in the middle of the aperture time more
    than samples taken at the beginning and the end of the measurement using
    a triangular weighing function.
    '''
    DCNR_HIGH_ORDER = 2
    '''
    NI-DMM weighs the samples taken in the middle of the aperture time more
    than samples taken at the beginning and the end of the measurement using
    a bell-curve weighing function.
    '''


class Function(Enum):
    DC_VOLTS = 1
    '''
    All devices supported.
    '''
    AC_VOLTS = 2
    '''
    All devices supported.
    '''
    DC_CURRENT = 3
    '''
    All devices supported.
    '''
    AC_CURRENT = 4
    '''
    All devices supported.
    '''
    RES_2_WIRE = 5
    '''
    All devices supported.
    '''
    RES_4_WIRE = 101
    '''
    NI 4065, and NI 4070/4071/4072 supported.
    '''
    FREQ = 104
    '''
    NI 4070/4071/4072 supported.
    '''
    PERIOD = 105
    '''
    NI 4070/4071/4072 supported.
    '''
    TEMPERATURE = 108
    '''
    NI 4065, and NI 4070/4071/4072 supported.
    '''
    AC_VOLTS_DC_COUPLED = 1001
    '''
    NI 4070/4071/4072 supported.
    '''
    DIODE = 1002
    '''
    All devices supported.
    '''
    WAVEFORM_VOLTAGE = 1003
    '''
    NI 4070/4071/4072 supported.
    '''
    WAVEFORM_CURRENT = 1004
    '''
    NI 4070/4071/4072 supported.
    '''
    CAPACITANCE = 1005
    '''
    NI 4072 supported.
    '''
    INDUCTANCE = 1006
    '''
    NI 4072 supported.
    '''


class LCCalculationModel(Enum):
    CALC_MODEL_AUTO = -1
    '''
    NI-DMM chooses the algorithm based on function and range.
    '''
    CALC_MODEL_SERIES = 0
    '''
    NI-DMM uses the series impedance model to calculate capacitance and
    inductance.
    '''
    CALC_MODEL_PARALLEL = 1
    '''
    NI-DMM uses the parallel admittance model to calculate capacitance and
    inductance.
    '''


class MeasurementCompleteDest(Enum):
    NONE = -1
    '''
    No destination specified.
    '''
    EXTERNAL = 2
    '''
    Pin 6 on the AUX Connector
    '''
    SOFTWARE_TRIG = 3
    PXI_TRIG0 = 111
    '''
    PXI Trigger Line 0
    '''
    PXI_TRIG1 = 112
    '''
    PXI Trigger Line 1
    '''
    PXI_TRIG2 = 113
    '''
    PXI Trigger Line 2
    '''
    PXI_TRIG3 = 114
    '''
    PXI Trigger Line 3
    '''
    PXI_TRIG4 = 115
    '''
    PXI Trigger Line 4
    '''
    PXI_TRIG5 = 116
    '''
    PXI Trigger Line 5
    '''
    PXI_TRIG6 = 117
    '''
    PXI Trigger Line 6
    '''
    PXI_TRIG7 = 118
    '''
    PXI Trigger Line 7
    '''
    LBR_TRIG0 = 1003
    '''
    Local Bus Right Trigger Line 0 of PXI/SCXI combination chassis
    '''


class MeasurementDestinationSlope(Enum):
    POSITIVE = 0
    '''
    The driver triggers on the rising edge of the trigger signal.
    '''
    NEGATIVE = 1
    '''
    The driver triggers on the falling edge of the trigger signal.
    '''


class OffsetCompensatedOhms(Enum):
    OFF = 0
    '''
    Disables Offset Compensated Ohms.
    '''
    ON = 1
    '''
    Enables Offset Compensated Ohms.
    '''


class OperationMode(Enum):
    DMM_MODE = 0
    '''
    Single or multipoint measurements: When the Trigger Count and Sample
    Count properties are both set to 1, the NI 4065, NI 4070/4071/4072, and
    NI 4080/4081/4082 take a single-point measurement; otherwise, NI-DMM
    takes multipoint measurements.
    '''
    WAVEFORM_MODE = 1
    '''
    Configures the NI 4080/4081/4082 and NI 4070/4071/4072 to take waveform
    measurements.
    '''


class SampleTrigSlope(Enum):
    POSITIVE = 0
    '''
    The driver triggers on the rising edge of the trigger signal.
    '''
    NEGATIVE = 1
    '''
    The driver triggers on the falling edge of the trigger signal.
    '''


class SampleTrigger(Enum):
    NONE = -1
    IMMEDIATE = 1
    '''
    No trigger specified
    '''
    EXTERNAL = 2
    '''
    Pin 9 on the AUX Connector
    '''
    SOFTWARE_TRIG = 3
    '''
    Configures the DMM to wait until niDMM Send Software Trigger is called.
    '''
    INTERVAL = 10
    '''
    Interval trigger
    '''
    AUX_TRIG1 = 1001
    '''
    Pin 3 on the AUX connector
    '''
    LBR_TRIG1 = 1004
    '''
    Local Bus Right Trigger Line 1 of PXI/SCXI combination chassis
    '''
    PXI_TRIG0 = 111
    '''
    PXI Trigger Line 0
    '''
    PXI_TRIG1 = 112
    '''
    PXI Trigger Line 1
    '''
    PXI_TRIG2 = 113
    '''
    PXI Trigger Line 2
    '''
    PXI_TRIG3 = 114
    '''
    PXI Trigger Line 3
    '''
    PXI_TRIG4 = 115
    '''
    PXI Trigger Line 4
    '''
    PXI_TRIG5 = 116
    '''
    PXI Trigger Line 5
    '''
    PXI_TRIG6 = 117
    '''
    PXI Trigger Line 6
    '''
    PXI_TRIG7 = 118
    '''
    PXI Trigger Line 7
    '''
    PXI_STAR = 131
    '''
    PXI Star trigger line
    '''


class TemperatureRTDType(Enum):
    CustomRTD = 0
    '''
    Performs Callendar-Van Dusen RTD scaling with the user-specified A, B,
    and C coefficients.
    '''
    PT3750 = 1
    '''
    Performs scaling for a Pt 3750 RTD.
    '''
    PT3851 = 2
    '''
    Performs scaling for a Pt 3851 RTD.
    '''
    PT3911 = 3
    '''
    Performs scaling for a Pt 3911 RTD.
    '''
    PT3916 = 4
    '''
    Performs scaling for a Pt 3916 RTD.
    '''
    PT3920 = 5
    '''
    Performs scaling for a Pt 3920 RTD.
    '''
    PT3928 = 6
    '''
    Performs scaling for a Pt 3928 RTD.
    '''


class TemperatureThermistorType(Enum):
    THERMISTOR_CUSTOM = 0
    '''
    Performs Steinhart-Hart thermistor scaling with the user-specified A, B,
    and C coefficients.
    '''
    THERMISTOR_44004 = 1
    '''
    Performs scaling for an Omega Series 44004 thermistor.
    '''
    THERMISTOR_44006 = 2
    '''
    Performs scaling for an Omega Series 44006 thermistor.
    '''
    THERMISTOR_44007 = 3
    '''
    Performs scaling for an Omega Series 44007 thermistor.
    '''


class TemperatureThermocoupleReferenceJunctionType(Enum):
    Fixed = 2
    '''
    Thermocouple reference juction is fixed at the user-specified
    temperature.
    '''


class TemperatureThermocoupleType(Enum):
    B = 1
    '''
    Thermocouple type B
    '''
    E = 4
    '''
    Thermocouple type E
    '''
    J = 6
    '''
    Thermocouple type J
    '''
    K = 7
    '''
    Thermocouple type K
    '''
    N = 8
    '''
    Thermocouple type N
    '''
    R = 9
    '''
    Thermocouple type R
    '''
    S = 10
    '''
    Thermocouple type S
    '''
    T = 11
    '''
    Thermocouple type T
    '''


class TemperatureTransducerType(Enum):
    THERMOCOUPLE = 1
    '''
    Use for thermocouple measurements.
    '''
    THERMISTOR = 2
    '''
    Use for thermistor measurements.
    '''
    TWO_WIRE_RTD = 3
    '''
    Use for 2-wire RTD measurements.
    '''
    FOUR_WIRE_RTD = 4
    '''
    Use for 4-wire RTD measurements.
    '''


class TriggerSlope(Enum):
    POSITIVE = 0
    '''
    The driver triggers on the rising edge of the trigger signal.
    '''
    NEGATIVE = 1
    '''
    The driver triggers on the falling edge of the trigger signal.
    '''


class TriggerSource(Enum):
    NONE = -1
    IMMEDIATE = 1
    '''
    No trigger specified.
    '''
    EXTERNAL = 2
    '''
    Pin 9 on the AUX Connector
    '''
    SOFTWARE_TRIG = 3
    '''
    Waits until niDMM Send Software Trigger is called.
    '''
    PXI_TRIG0 = 111
    '''
    PXI Trigger Line 0
    '''
    PXI_TRIG1 = 112
    '''
    PXI Trigger Line 1
    '''
    PXI_TRIG2 = 113
    '''
    PXI Trigger Line 2
    '''
    PXI_TRIG3 = 114
    '''
    PXI Trigger Line 3
    '''
    PXI_TRIG4 = 115
    '''
    PXI Trigger Line 4
    '''
    PXI_TRIG5 = 116
    '''
    PXI Trigger Line 5
    '''
    PXI_TRIG6 = 117
    '''
    PXI Trigger Line 6
    '''
    PXI_TRIG7 = 118
    '''
    PXI Trigger Line 7
    '''
    PXI_STAR = 131
    '''
    PXI Star Trigger Line
    '''
    AUX_TRIG1 = 1001
    '''
    Pin 3 on the AUX connector
    '''
    LBR_TRIG1 = 1004
    '''
    Local Bus Right Trigger Line 1 of PXI/SCXI combination chassis
    '''


class WaveformCouplingMode(Enum):
    WAVEFORM_COUPLING_AC = 0
    '''
    Specifies AC coupling.
    '''
    WAVEFORM_COUPLING_DC = 1
    '''
    Specifies DC coupling.
    '''
