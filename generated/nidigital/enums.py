# -*- coding: utf-8 -*-
# This file was generated

from enum import Enum


class ApertureTimeUnits(Enum):
    SECONDS = 2100


class DigitalEdge(Enum):
    RISING = 1800
    FALLING = 1801


class PpmuOutputFunction(Enum):
    VOLTAGE = 1300
    CURRENT = 1301


class SelectedFunction(Enum):
    DIGITAL = 1100
    PPMU = 1101
    OFF = 1102
    DISCONNECT = 1103


class Signal(Enum):
    START_TRIGGER = 2000
    CONDITIONAL_JUMP_TRIGGER = 2001
    PATTERN_OPCODE_EVENT = 2002
    REF_CLOCK = 2003


class TdrEndpointTermination(Enum):
    OPEN = 3600
    SHORT_TO_GROUND = 3601


class TerminationMode(Enum):
    ACTIVE_LOAD = 1200
    VTERM = 1201
    HIGH_Z = 1202
