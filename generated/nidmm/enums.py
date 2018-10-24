# -*- coding: utf-8 -*-
# This file was generated

from enum import Enum


class ADCCalibration(Enum):
    AUTO = -1
    r'''
    The DMM enables or disables ADC calibration for you.
    '''
    OFF = 0
    r'''
    The DMM does not compensate for changes to the gain.
    '''
    ON = 1
    r'''
    The DMM measures an internal reference to calculate the correct gain for the  measurement.
    '''


class AcquisitionStatus(Enum):
    RUNNING = 0
    r'''
    Running
    '''
    FINISHED_WITH_BACKLOG = 1
    r'''
    Finished with **Backlog**
    '''
    FINISHED_WITH_NO_BACKLOG = 2
    r'''
    Finished with no **Backlog**
    '''
    PAUSED = 3
    r'''
    Paused
    '''
    NO_ACQUISITION_IN_PROGRESS = 4
    r'''
    No acquisition in progress
    '''


class ApertureTimeUnits(Enum):
    SECONDS = 0
    r'''
    Seconds
    '''
    POWER_LINE_CYCLES = 1
    r'''
    Powerline Cycles
    '''


class AutoZero(Enum):
    AUTO = -1
    r'''
    The drivers chooses the AutoZero setting based on the configured method  and resolution.
    '''
    OFF = 0
    r'''
    Disables AutoZero.
    '''
    ON = 1
    r'''
    The DMM internally disconnects the input signal following each measurement  and takes a zero reading. It then subtracts the zero reading from the  preceding reading.
    '''
    ONCE = 2
    r'''
    The DMM internally disconnects the input signal for the first measurement  and takes a zero reading. It then subtracts the zero reading from the first  reading and the following readings.
    '''


class CableCompensationType(Enum):
    NONE = 0
    r'''
    No Cable Compensation
    '''
    OPEN = 1
    r'''
    Open Cable Compensation
    '''
    SHORT = 2
    r'''
    Short Cable Compensation
    '''
    OPEN_AND_SHORT = 3
    r'''
    Open and Short Cable Compensation
    '''


class DCNoiseRejection(Enum):
    AUTO = -1
    r'''
    The driver chooses the DC noise rejection setting based on the configured  method and resolution.
    '''
    NORMAL = 0
    r'''
    NI-DMM weighs all samples equally.
    '''
    SECOND_ORDER = 1
    r'''
    NI-DMM weighs the samples taken in the middle of the aperture time more than  samples taken at the beginning and the end of the measurement using a  triangular weighing method.
    '''
    HIGH_ORDER = 2
    r'''
    NI-DMM weighs the samples taken in the middle of the aperture time more than  samples taken at the beginning and the end of the measurement using a  bell-curve weighing method.
    '''


class Function(Enum):
    DC_VOLTS = 1
    r'''
    DC Voltage
    '''
    AC_VOLTS = 2
    r'''
    AC Voltage
    '''
    DC_CURRENT = 3
    r'''
    DC Current
    '''
    AC_CURRENT = 4
    r'''
    AC Current
    '''
    TWO_WIRE_RES = 5
    r'''
    2-Wire Resistance
    '''
    FOUR_WIRE_RES = 101
    r'''
    4-Wire Resistance
    '''
    FREQ = 104
    r'''
    Frequency
    '''
    PERIOD = 105
    r'''
    Period
    '''
    TEMPERATURE = 108
    r'''
    NI 4065, NI 4070/4071/4072, and NI 4080/4081/4182 supported.
    '''
    AC_VOLTS_DC_COUPLED = 1001
    r'''
    AC Voltage with DC Coupling
    '''
    DIODE = 1002
    r'''
    Diode
    '''
    WAVEFORM_VOLTAGE = 1003
    r'''
    Waveform voltage
    '''
    WAVEFORM_CURRENT = 1004
    r'''
    Waveform current
    '''
    CAPACITANCE = 1005
    r'''
    Capacitance
    '''
    INDUCTANCE = 1006
    r'''
    Inductance
    '''


class LCCalculationModel(Enum):
    AUTO = -1
    r'''
    NI-DMM chooses the algorithm based on method and range
    '''
    SERIES = 0
    r'''
    NI-DMM uses the series impedance model to calculate capacitance and inductance
    '''
    PARALLEL = 1
    r'''
    NI-DMM uses the parallel admittance model to calculate capacitance and inductance
    '''


class MeasurementCompleteDest(Enum):
    NONE = -1
    r'''
    No Trigger
    '''
    EXTERNAL = 2
    r'''
    AUX I/O Connector
    '''
    PXI_TRIG0 = 111
    r'''
    PXI Trigger Line 0
    '''
    PXI_TRIG1 = 112
    r'''
    PXI Trigger Line 1
    '''
    PXI_TRIG2 = 113
    r'''
    PXI Trigger Line 2
    '''
    PXI_TRIG3 = 114
    r'''
    PXI Trigger Line 3
    '''
    PXI_TRIG4 = 115
    r'''
    PXI Trigger Line 4
    '''
    PXI_TRIG5 = 116
    r'''
    PXI Trigger Line 5
    '''
    PXI_TRIG6 = 117
    r'''
    PXI Trigger Line 6
    '''
    PXI_TRIG7 = 118
    r'''
    PXI Trigger Line 7
    '''
    LBR_TRIG0 = 1003
    r'''
    Internal Trigger Line of a PXI/SCXI Combination Chassis
    '''


class OperationMode(Enum):
    IVIDMM = 0
    r'''
    IviDmm Mode
    '''
    WAVEFORM = 1
    r'''
    Waveform acquisition mode
    '''


class RTDType(Enum):
    CUSTOM = 0
    r'''
    Performs Callendar-Van Dusen RTD scaling with the user-specified A, B,
    and C coefficients.
    '''
    PT3750 = 1
    r'''
    Performs scaling for a Pt 3750 RTD.
    '''
    PT3851 = 2
    r'''
    Performs scaling for a Pt 3851 RTD.
    '''
    PT3911 = 3
    r'''
    Performs scaling for a Pt 3911 RTD.
    '''
    PT3916 = 4
    r'''
    Performs scaling for a Pt 3916 RTD.
    '''
    PT3920 = 5
    r'''
    Performs scaling for a Pt 3920 RTD.
    '''
    PT3928 = 6
    r'''
    Performs scaling for a Pt 3928 RTD.
    '''


class SampleTrigger(Enum):
    IMMEDIATE = 1
    r'''
    No Trigger
    '''
    EXTERNAL = 2
    r'''
    AUX I/O Connector Trigger Line 0
    '''
    SOFTWARE_TRIG = 3
    r'''
    Software Trigger
    '''
    INTERVAL = 10
    r'''
    Interval Trigger
    '''
    PXI_TRIG0 = 111
    r'''
    PXI Trigger Line 0
    '''
    PXI_TRIG1 = 112
    r'''
    PXI Trigger Line 1
    '''
    PXI_TRIG2 = 113
    r'''
    PXI Trigger Line 2
    '''
    PXI_TRIG3 = 114
    r'''
    PXI Trigger Line 3
    '''
    PXI_TRIG4 = 115
    r'''
    PXI Trigger Line 4
    '''
    PXI_TRIG5 = 116
    r'''
    PXI Trigger Line 5
    '''
    PXI_TRIG6 = 117
    r'''
    PXI Trigger Line 6
    '''
    PXI_TRIG7 = 118
    r'''
    PXI Trigger Line 7
    '''
    PXI_STAR = 131
    r'''
    PXI Star Trigger Line
    '''
    AUX_TRIG1 = 1001
    r'''
    AUX I/0 Connector Trigger Line 1
    '''
    LBR_TRIG1 = 1004
    r'''
    Internal Trigger Line of a PXI/SCXI Combination Chassis
    '''


class ThermistorType(Enum):
    CUSTOM = 0
    r'''
    Custom
    '''
    THERMISTOR_44004 = 1
    r'''
    44004
    '''
    THERMISTOR_44006 = 2
    r'''
    44006
    '''
    THERMISTOR_44007 = 3
    r'''
    44007
    '''


class ThermocoupleReferenceJunctionType(Enum):
    FIXED = 2
    r'''
    Thermocouple reference juction is fixed at the user-specified
    temperature.
    '''


class ThermocoupleType(Enum):
    B = 1
    r'''
    Thermocouple type B
    '''
    E = 4
    r'''
    Thermocouple type E
    '''
    J = 6
    r'''
    Thermocouple type J
    '''
    K = 7
    r'''
    Thermocouple type K
    '''
    N = 8
    r'''
    Thermocouple type N
    '''
    R = 9
    r'''
    Thermocouple type R
    '''
    S = 10
    r'''
    Thermocouple type S
    '''
    T = 11
    r'''
    Thermocouple type T
    '''


class TransducerType(Enum):
    THERMOCOUPLE = 1
    r'''
    Thermocouple
    '''
    THERMISTOR = 2
    r'''
    Thermistor
    '''
    TWO_WIRE_RTD = 3
    r'''
    2-wire RTD
    '''
    FOUR_WIRE_RTD = 4
    r'''
    4-wire RTD
    '''


class TriggerSource(Enum):
    IMMEDIATE = 1
    r'''
    No Trigger
    '''
    EXTERNAL = 2
    r'''
    AUX I/O Connector Trigger Line 0
    '''
    SOFTWARE_TRIG = 3
    r'''
    Software Trigger
    '''
    PXI_TRIG0 = 111
    r'''
    PXI Trigger Line 0
    '''
    PXI_TRIG1 = 112
    r'''
    PXI Trigger Line 1
    '''
    PXI_TRIG2 = 113
    r'''
    PXI Trigger Line 2
    '''
    PXI_TRIG3 = 114
    r'''
    PXI Trigger Line 3
    '''
    PXI_TRIG4 = 115
    r'''
    PXI Trigger Line 4
    '''
    PXI_TRIG5 = 116
    r'''
    PXI Trigger Line 5
    '''
    PXI_TRIG6 = 117
    r'''
    PXI Trigger Line 6
    '''
    PXI_TRIG7 = 118
    r'''
    PXI Trigger Line 7
    '''
    PXI_STAR = 131
    r'''
    PXI Star Trigger Line
    '''
    AUX_TRIG1 = 1001
    r'''
    AUX I/O Connector Trigger Line 1
    '''
    LBR_TRIG1 = 1004
    r'''
    Internal Trigger Line of a PXI/SCXI Combination Chassis
    '''


class WaveformCoupling(Enum):
    AC = 0
    r'''
    AC Coupled
    '''
    DC = 1
    r'''
    DC Coupled
    '''
