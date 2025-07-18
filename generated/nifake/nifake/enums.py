# -*- coding: utf-8 -*-
# This file was generated

from enum import Enum
from enum import IntFlag


class Color(Enum):
    RED = 1
    r'''
    Like blood.
    '''
    BLUE = 2
    r'''
    Like the sky.
    '''
    YELLOW = 5
    r'''
    Like a banana.
    '''
    BLACK = 42
    r'''
    Like this developer's conscience.
    '''


class EnumWithConverter(Enum):
    RED = 1
    BLUE = 2
    YELLOW = 5
    BLACK = 42


class FloatEnum(Enum):
    THREE_POINT_FIVE = 3.5
    r'''
    Specifies 3.5 digits resolution.
    '''
    FOUR_POINT_FIVE = 4.5
    r'''
    Specifies 4.5 digits resolution.
    '''
    FIVE_POINT_FIVE = 5.5
    r'''
    Specifies 5.5 digits resolution.
    '''
    SIX_POINT_FIVE = 6.5
    r'''
    Specifies 6.5 digits resolution.
    '''
    SEVEN_POINT_FIVE = 7.5
    r'''
    Specifies 7.5 digits resolution.
    '''


class IntFlagEnum(IntFlag):
    A = 1
    r'''
    Flag A option.
    '''
    B = 2
    r'''
    Flag B option.
    '''
    C = 9223372036854775808
    r'''
    Flag C option.
    '''


class MobileOSNames(Enum):
    ANDROID = 'Android'
    r'''
    Most popular OS.
    '''
    IOS = 'iOS'
    r'''
    Most secure OS.
    '''
    NONE = 'None'
    r'''
    Remember Symbian?.
    '''


class Turtle(Enum):
    LEONARDO = 0
    r'''
    Wields two katanas.
    '''
    DONATELLO = 1
    r'''
    Uses a bo staff.
    '''
    RAPHAEL = 2
    r'''
    Has a pair of sai.
    '''
    MICHELANGELO = 3
    r'''
    Owns nunchucks.
    '''
