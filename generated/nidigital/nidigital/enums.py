# -*- coding: utf-8 -*-
# This file was generated

from enum import Enum


class BitOrder(Enum):
    MSB = 2500
    LSB = 2501


class DigitalEdge(Enum):
    RISING = 1800
    FALLING = 1801


class DriveFormat(Enum):
    NR = 1500
    RL = 1501
    RH = 1502
    SBC = 1503


class HistoryRAMCyclesToAcquire(Enum):
    FAILED = 2303
    ALL = 2304


class HistoryRAMTriggerType(Enum):
    FIRST_FAILURE = 2200
    CYCLE_NUMBER = 2201
    PATTERN_LABEL = 2202


class PPMUApertureTimeUnits(Enum):
    SECONDS = 2100


class PPMUCurrentLimitBehavior(Enum):
    REGULATE = 3100


class PPMUMeasurementType(Enum):
    CURRENT = 2400
    VOLTAGE = 2401


class PPMUOutputFunction(Enum):
    VOLTAGE = 1300
    CURRENT = 1301


class PinState(Enum):
    ZERO = 0
    ONE = 1
    L = 3
    H = 4
    X = 5
    M = 6
    V = 7
    D = 8
    E = 9
    NOT_A_PIN_STATE = 254
    PIN_STATE_NOT_ACQUIRED = 255


class SelectedFunction(Enum):
    DIGITAL = 1100
    PPMU = 1101
    OFF = 1102
    DISCONNECT = 1103


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
    CAPTURE_WAVEFORM = 3301


class SoftwareTrigger(Enum):
    START = 2000
    CONDITIONAL_JUMP = 2001


class SourceDataMapping(Enum):
    BROADCAST = 2600
    SITE_UNIQUE = 2601


class TDREndpointTermination(Enum):
    OPEN = 3600
    SHORT_TO_GROUND = 3601


class TerminationMode(Enum):
    ACTIVE_LOAD = 1200
    VTERM = 1201
    HIGH_Z = 1202


class TimeSetEdgeType(Enum):
    DRIVE_ON = 2800
    DRIVE_DATA = 2801
    DRIVE_RETURN = 2802
    DRIVE_OFF = 2803
    COMPARE_STROBE = 2804
    DRIVE_DATA2 = 2805
    DRIVE_RETURN2 = 2806
    COMPARE_STROBE2 = 2807


class TriggerType(Enum):
    NONE = 1700
    DIGITAL_EDGE = 1701
    SOFTWARE = 1702


class WriteStaticPinState(Enum):
    ZERO = 0
    ONE = 1
    X = 5
