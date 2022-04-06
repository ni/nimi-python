# -*- coding: utf-8 -*-
# This file was generated

from enum import Enum


class BitOrder(Enum):
    MSB = 2500
    r'''
    The most significant bit is first. The first bit is in the 2^n place, where n is the number of bits.
    '''
    LSB = 2501
    r'''
    The least significant bit is first. The first bit is in the 2^0 place.
    '''


class DigitalEdge(Enum):
    RISING = 1800
    r'''
    Asserts the trigger when the signal transitions from low level to high level.
    '''
    FALLING = 1801
    r'''
    Asserts the trigger when the signal transitions from high level to low level.
    '''


class DriveFormat(Enum):
    NR = 1500
    r'''
    Drive format remains at logic level after each bit.
    '''
    RL = 1501
    r'''
    Drive format returns to a logic level low after each bit.
    '''
    RH = 1502
    r'''
    Drive format returns to a logic level high after each bit.
    '''
    SBC = 1503
    r'''
    Drive format returns to the complement logic level of the bit after each bit.
    '''


class FrequencyMeasurementMode(Enum):
    BANKED = 3700
    r'''
    Frequency measurements are made serially for groups of channels associated with a single frequency counter for each group.

    Maximum frequency measured: 200 MHz.
    '''
    PARALLEL = 3701
    r'''
    Frequency measurements are made by multiple frequency counters in parallel.

    Maximum frequency measured: 100 MHz.
    '''


class HistoryRAMCyclesToAcquire(Enum):
    FAILED = 2303
    r'''
    Acquires failed cycles.
    '''
    ALL = 2304
    r'''
    Acquires all cycles.
    '''


class HistoryRAMTriggerType(Enum):
    FIRST_FAILURE = 2200
    r'''
    First Failure History RAM trigger
    '''
    CYCLE_NUMBER = 2201
    r'''
    Cycle Number History RAM trigger.
    '''
    PATTERN_LABEL = 2202
    r'''
    Pattern Label History RAM trigger
    '''


class PPMUApertureTimeUnits(Enum):
    SECONDS = 2100
    r'''
    Unit in seconds.
    '''


class PPMUCurrentLimitBehavior(Enum):
    REGULATE = 3100
    r'''
    Controls output current so that it does not exceed the current limit. Power continues to generate even if the current limit is reached.
    '''


class PPMUMeasurementType(Enum):
    CURRENT = 2400
    r'''
    The PPMU measures current.
    '''
    VOLTAGE = 2401
    r'''
    The PPMU measures voltage.
    '''


class PPMUOutputFunction(Enum):
    VOLTAGE = 1300
    r'''
    The PPMU forces voltage to the DUT.
    '''
    CURRENT = 1301
    r'''
    The PPMU forces current to the DUT.
    '''


class PinState(Enum):
    ZERO = 0
    r'''
    A digital state of 0.
    '''
    ONE = 1
    r'''
    A digital state of 1.
    '''
    L = 3
    r'''
    A digital state of L (low).
    '''
    H = 4
    r'''
    A digital state of H (high).
    '''
    X = 5
    r'''
    A digital state of X (non-drive state).
    '''
    M = 6
    r'''
    A digital state of M (midband).
    '''
    V = 7
    r'''
    A digital state of V (compare high or low, not midband; store results from capture functionality if configured).
    '''
    D = 8
    r'''
    A digital state of D (drive data from source functionality if configured).
    '''
    E = 9
    r'''
    A digital state of E (compare data from source functionality if configured).
    '''
    NOT_A_PIN_STATE = 254
    r'''
    Not a pin state is used for non-existent DUT cycles.
    '''
    PIN_STATE_NOT_ACQUIRED = 255
    r'''
    Pin state could not be acquired because none of the pins mapped to the instrument in a multi-instrument session had any failures.
    '''

    def __str__(self):
        return {
            'ZERO': '0',
            'ONE': '1',
            'NOT_A_PIN_STATE': 'Not a Pin State',
            'PIN_STATE_NOT_ACQUIRED': 'Pin State Not Acquired',
        }.get(self.name, self.name)


class SelectedFunction(Enum):
    DIGITAL = 1100
    r'''
    The pattern sequencer controls the specified pin(s). If a pattern is currently bursting, the pin immediately switches to bursting the pattern. This option disconnects the PPMU.
    '''
    PPMU = 1101
    r'''
    The PPMU controls the specified pin(s) and connects the PPMU. The pin driver is in a non-drive state, and the active load is disabled. The PPMU does not start sourcing or measuring until Source or Measure(PpmuMeasurementType) is called.
    '''
    OFF = 1102
    r'''
    Puts the digital driver in a non-drive state, disables the active load, disconnects the PPMU, and closes the I/O switch connecting the instrument channel.
    '''
    DISCONNECT = 1103
    r'''
    The I/O switch connecting the instrument channel is open to the I/O connector. If the PPMU is sourcing, it is stopped prior to opening the I/O switch.
    '''
    RIO = 1104
    r'''
    Yields control of the specified pin(s) to LabVIEW FPGA.
    '''


class SequencerFlag(Enum):
    FLAG0 = 'seqflag0'
    FLAG1 = 'seqflag1'
    FLAG2 = 'seqflag2'
    FLAG3 = 'seqflag3'


class SequencerRegister(Enum):
    REGISTER0 = 'reg0'
    REGISTER1 = 'reg1'
    REGISTER2 = 'reg2'
    REGISTER3 = 'reg3'
    REGISTER4 = 'reg4'
    REGISTER5 = 'reg5'
    REGISTER6 = 'reg6'
    REGISTER7 = 'reg7'
    REGISTER8 = 'reg8'
    REGISTER9 = 'reg9'
    REGISTER10 = 'reg10'
    REGISTER11 = 'reg11'
    REGISTER12 = 'reg12'
    REGISTER13 = 'reg13'
    REGISTER14 = 'reg14'
    REGISTER15 = 'reg15'


class _SiteResultType(Enum):
    PASS_FAIL = 3300
    r'''
    Pass/fail site result.
    '''
    CAPTURE_WAVEFORM = 3301
    r'''
    Capture waveform site result.
    '''


class SoftwareTrigger(Enum):
    START = 2000
    r'''
    Overrides the start trigger.
    '''
    CONDITIONAL_JUMP = 2001
    r'''
    Specifies to route a conditional jump trigger.
    '''


class SourceDataMapping(Enum):
    BROADCAST = 2600
    r'''
    Broadcasts the waveform you specify to all sites.
    '''
    SITE_UNIQUE = 2601
    r'''
    Sources unique waveform data to each site.
    '''


class TDREndpointTermination(Enum):
    OPEN = 3600
    r'''
    TDR channels are connected to an open circuit.
    '''
    SHORT_TO_GROUND = 3601
    r'''
    TDR channels are connected to a short to ground.
    '''


class TerminationMode(Enum):
    ACTIVE_LOAD = 1200
    r'''
    The active load provides a constant current to a commutating voltage (Vcom).
    '''
    VTERM = 1201
    r'''
    The pin driver drives Vterm.
    '''
    HIGH_Z = 1202
    r'''
    The pin driver is in a non-drive state (in a high-impedance state) and the active load is disabled.
    '''


class TimeSetEdgeType(Enum):
    DRIVE_ON = 2800
    r'''
    Specifies the drive on edge of the time set.
    '''
    DRIVE_DATA = 2801
    r'''
    Specifies the drive data edge of the time set.
    '''
    DRIVE_RETURN = 2802
    r'''
    Specifies the drive return edge of the time set.
    '''
    DRIVE_OFF = 2803
    r'''
    Specifies the drive off edge of the time set.
    '''
    COMPARE_STROBE = 2804
    r'''
    Specifies the compare strobe of the time set.
    '''
    DRIVE_DATA2 = 2805
    r'''
    Specifies the drive data 2 edge of the time set.
    '''
    DRIVE_RETURN2 = 2806
    r'''
    Specifies the drive return 2 edge of the time set.
    '''
    COMPARE_STROBE2 = 2807
    r'''
    Specifies the compare strobe 2 of the time set.
    '''


class TriggerType(Enum):
    NONE = 1700
    r'''
    Disables the start trigger.
    '''
    DIGITAL_EDGE = 1701
    r'''
    Digital edge trigger.
    '''
    SOFTWARE = 1702
    r'''
    Software start trigger.
    '''


class WriteStaticPinState(Enum):
    ZERO = 0
    r'''
    Specifies to drive low.
    '''
    ONE = 1
    r'''
    Specifies to drive high.
    '''
    X = 5
    r'''
    Specifies to not drive.
    '''

    def __str__(self):
        return {
            'ZERO': '0',
            'ONE': '1',
        }.get(self.name, self.name)
