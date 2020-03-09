# -*- coding: utf-8 -*-
# This file was generated

from enum import Enum


class ApertureTimeUnits(Enum):
    SECONDS = 2100


class DigitalEdge(Enum):
    RISING = 1800
    FALLING = 1801


class DigitalState(Enum):
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


class PPMUOutputFunction(Enum):
    VOLTAGE = 1300
    CURRENT = 1301


class SelectedFunction(Enum):
    DIGITAL = 1100
    PPMU = 1101
    OFF = 1102
    DISCONNECT = 1103


class SiteResult(Enum):
    PASS_FAIL = 3300
    CAPTURE_WAVEFORM = 3301


class TDREndpointTermination(Enum):
    OPEN = 3600
    SHORT_TO_GROUND = 3601


class TerminationMode(Enum):
    ACTIVE_LOAD = 1200
    VTERM = 1201
    HIGH_Z = 1202
