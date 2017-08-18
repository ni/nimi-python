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
    '''
    Running
    '''
    FINISHED_WITH_BACKLOG = 1
    '''
    Finished with **Backlog**
    '''
    FINISHED_WITH_NO_BACKLOG = 2
    '''
    Finished with no **Backlog**
    '''
    PAUSED = 3
    '''
    Paused
    '''
    NO_ACQUISITION_IN_PROGRESS = 4
    '''
    No acquisition in progress
    '''


class ApertureTimeUnits(Enum):
    SECONDS = 0
    '''
    Units are seconds.
    '''
    POWER_LINE_CYCLES = 1
    '''
    Units are powerline cycles (PLCs).
    '''


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
    NONE = 0
    '''
    No cable compensation.
    '''
    OPEN = 1
    '''
    Open cable compensation.
    '''
    SHORT = 2
    '''
    Short cable compensation.
    '''
    OPEN_AND_SHORT = 3
    '''
    Open and short cable compensation.
    '''


class CurrentSource(Enum):
    _1_MICROAMP = 1e-06
    '''
    NI 4070/4071/4072 are supported.
    '''
    _10_MICROAMP = 1e-05
    '''
    NI 4080/4081/4082 and NI 4070/4071/4072 are supported.
    '''
    _100_MICROAMP = 0.0001
    '''
    NI 4080/4081/4082, NI 4070/4071/4072, and NI 4065 are supported.
    '''
    _1_MILLIAMP = 0.001
    '''
    NI 4080/4081/4082, NI 4070/4071/4072, and NI 4065 are supported.
    '''


class DCBias(Enum):
    DC_BIAS_OFF = 0
    '''
    NI-DMM programs the device not to use the DC bias.
    '''
    DC_BIAS_ON = 1
    '''
    NI-DMM programs the device to use the DC bias.
    '''


class DCNoiseRejection(Enum):
    AUTO = -1
    '''
    The driver chooses the DC noise rejection setting based on the
    configured function and resolution.
    '''
    NORMAL = 0
    '''
    NI-DMM weighs all samples equally.
    '''
    SECOND_ORDER = 1
    '''
    NI-DMM weighs the samples taken in the middle of the aperture time more
    than samples taken at the beginning and the end of the measurement using
    a triangular weighing function.
    '''
    HIGH_ORDER = 2
    '''
    NI-DMM weighs the samples taken in the middle of the aperture time more
    than samples taken at the beginning and the end of the measurement using
    a bell-curve weighing function.
    '''


class DigitsResolution(Enum):
    _3_5 = 3.5
    '''
    Specifies 3.5 digits resolution.
    '''
    _4_5 = 4.5
    '''
    Specifies 4.5 digits resolution.
    '''
    _5_5 = 5.5
    '''
    Specifies 5.5 digits resolution.
    '''
    _6_5 = 6.5
    '''
    Specifies 6.5 digits resolution.
    '''
    _7_5 = 7.5
    '''
    Specifies 7.5 digits resolution.
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
    _2_WIRE_RESISTANCE = 5
    '''
    All devices supported.
    '''
    _4_WIRE_RESISTANCE = 101
    '''
    NI 4065, and NI 4070/4071/4072 supported.
    '''
    FREQUENCY = 104
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
    _AC_VOLTS_DC_COUPLED = 1001
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
    _WAVEFORM_CURRENT = 1004
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


class InputResistance(Enum):
    _1_M_OHM = 1000000.0
    '''
    Input resistance of 1 M Ohm
    '''
    _10_M_OHM = 10000000.0
    '''
    Input resistance of 10 M Ohm
    '''
    GREATER_THAN_10_G_OHM = 10000000000.0
    '''
    Input resistance greater than 10 G Ohm
    '''


class LCCalculationModel(Enum):
    AUTO = -1
    '''
    NI-DMM chooses the algorithm based on function and range.
    '''
    SERIES = 0
    '''
    NI-DMM uses the series impedance model to calculate capacitance and
    inductance.
    '''
    PARALLEL = 1
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
    TTL_0 = 111
    '''
    PXI Trigger Line 0
    '''
    TTL_1 = 112
    '''
    PXI Trigger Line 1
    '''
    TL_2 = 113
    '''
    PXI Trigger Line 2
    '''
    TTL_3 = 114
    '''
    PXI Trigger Line 3
    '''
    TL_4 = 115
    '''
    PXI Trigger Line 4
    '''
    TTL_5 = 116
    '''
    PXI Trigger Line 5
    '''
    TTL_6 = 117
    '''
    PXI Trigger Line 6
    '''
    TTL_7 = 118
    '''
    PXI Trigger Line 7
    '''
    _LBR_TRIG_0 = 1003
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
    _IVIDMM_MODE = 0
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


class PowerlineFrequency(Enum):
    _50_HZ = 50.0
    '''
    Specifies the powerline frequency as 50 Hz.
    '''
    _60_HZ = 60.0
    '''
    Specifies the powerline frequency as 60 Hz.
    '''


class RTDType(Enum):
    CUSTOM = 0
    '''
    Performs Callendar-Van Dusen RTD scaling with the user-specified A, B,
    and C coefficients.
    '''
    PT_3750 = 1
    '''
    Performs scaling for a Pt 3750 RTD.
    '''
    PT_3851 = 2
    '''
    Performs scaling for a Pt 3851 RTD.
    '''
    PT_3911 = 3
    '''
    Performs scaling for a Pt 3911 RTD.
    '''
    PT_3916 = 4
    '''
    Performs scaling for a Pt 3916 RTD.
    '''
    PT_3920 = 5
    '''
    Performs scaling for a Pt 3920 RTD.
    '''
    PT_3928 = 6
    '''
    Performs scaling for a Pt 3928 RTD.
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
    IMMEDIATE = 1
    '''
    No trigger specified
    '''
    _EXTERNAL = 2
    '''
    Pin 9 on the AUX Connector
    '''
    SOFTWARE_TRIG = 3
    '''
    Configures the DMM to wait until `niDMM Send Software
    Trigger <dmmviref.chm::/niDMM_Send_Software_Trigger.html>`__ is called.
    '''
    INTERVAL = 10
    '''
    Interval trigger
    '''
    TTL_0 = 111
    '''
    PXI Trigger Line 0
    '''
    TTL_1 = 112
    '''
    PXI Trigger Line 1
    '''
    TTL_2 = 113
    '''
    PXI Trigger Line 2
    '''
    _TTL_3 = 114
    '''
    PXI Trigger Line 3
    '''
    TTL_4 = 115
    '''
    PXI Trigger Line 4
    '''
    TTL_5 = 116
    '''
    PXI Trigger Line 5
    '''
    TTL_6 = 117
    '''
    PXI Trigger Line 6
    '''
    TTL_7 = 118
    '''
    PXI Trigger Line 7
    '''
    PXI_STAR = 131
    '''
    PXI Star trigger line
    '''
    AUX_TRIG_1 = 1001
    '''
    Pin 3 on the AUX connector
    '''
    LBR_TRIG_1 = 1004
    '''
    Local Bus Right Trigger Line 1 of PXI/SCXI combination chassis
    '''


class ThermistorType(Enum):
    CUSTOM = 0
    '''
    Performs Steinhart-Hart thermistor scaling with the user-specified A, B,
    and C coefficients.
    '''
    _44004 = 1
    '''
    Performs scaling for an Omega Series 44004 thermistor.
    '''
    _44006 = 2
    '''
    Performs scaling for an Omega Series 44006 thermistor.
    '''
    _44007 = 3
    '''
    Performs scaling for an Omega Series 44007 thermistor.
    '''


class ThermocoupleReferenceJunctionType(Enum):
    FIXED = 2
    '''
    Thermocouple reference juction is fixed at the user-specified
    temperature.
    '''


class ThermocoupleType(Enum):
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


class TransducerType(Enum):
    THERMOCOUPLE = 1
    '''
    Use for thermocouple measurements.
    '''
    THERMISTOR = 2
    '''
    Use for thermistor measurements.
    '''
    _2_WIRE_RTD = 3
    '''
    Use for 2-wire RTD measurements.
    '''
    _4_WIRE_RTD = 4
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
    Waits until `niDMM Send Software
    Trigger <dmmviref.chm::/niDMM_Send_Software_Trigger.html>`__ is called.
    '''
    _TTL_0 = 111
    '''
    PXI Trigger Line 0
    '''
    TTL_1 = 112
    '''
    PXI Trigger Line 1
    '''
    TTL_2 = 113
    '''
    PXI Trigger Line 2
    '''
    _TTL_3 = 114
    '''
    PXI Trigger Line 3
    '''
    TTL_4 = 115
    '''
    PXI Trigger Line 4
    '''
    TTL_5 = 116
    '''
    PXI Trigger Line 5
    '''
    TTL_6 = 117
    '''
    PXI Trigger Line 6
    '''
    _TTL_7 = 118
    '''
    PXI Trigger Line 7
    '''
    _PXI_STAR = 131
    '''
    PXI Star Trigger Line
    '''
    AUX_TRIG_1 = 1001
    '''
    Pin 3 on the AUX connector
    '''
    LBR_TRIG_1 = 1004
    '''
    Local Bus Right Trigger Line 1 of PXI/SCXI combination chassis
    '''


class WaveformCoupling(Enum):
    AC = 0
    '''
    Specifies AC coupling.
    '''
    DC = 1
    '''
    Specifies DC coupling.
    '''
