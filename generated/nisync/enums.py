# -*- coding: utf-8 -*-
# This file was generated

from enum import Enum


class GpsStatus(Enum):
    UNINITIALIZED = 0
    r'''
    Uninitialized
    '''
    ANTENNA_ERROR = 1
    r'''
    Antenna Error
    '''
    NO_USEABLE_SATELLITE = 2
    r'''
    No Useable Satellites
    '''
    ONE_USEABLE_SATELLITE = 3
    r'''
    One Useable Satellite
    '''
    TWO_USEABLE_SATELLITES = 4
    r'''
    Two Useable Satellites
    '''
    THREE_USEABLE_SATELLITES = 5
    r'''
    Three Useable Satellites
    '''
    NO_GPS_TIME = 6
    r'''
    No GPS Time
    '''
    PDOP_TOO_HIGH = 7
    r'''
    PDOP Too High
    '''
    UNUSEABLE_SATELLITE = 8
    r'''
    Unuseable Satellite
    '''
    FIX_REJECTED = 9
    r'''
    Fix Rejected
    '''
    SELF_SURVEY_COMPLETE = 10
    r'''
    Self Survey Complete
    '''
    SELF_SURVEY_NOT_COMPLETE = 11
    r'''
    Self Survey Not Complete
    '''
