# -*- coding: utf-8 -*-
# This file was generated

from enum import Enum


class ExpandAction(Enum):
    ROUTES = 0
    r'''
    Expand to routes
    '''
    PATHS = 1
    r'''
    Expand to paths
    '''


class MulticonnectMode(Enum):
    DEFAULT = -1
    r'''
    Default
    '''
    NO_MULTICONNECT = 0
    r'''
    No multiconnect
    '''
    MULTICONNECT = 1
    r'''
    Multiconnect
    '''


class OperationOrder(Enum):
    BEFORE = 1
    r'''
    Break before make
    '''
    AFTER = 2
    r'''
    Break after make
    '''


class PathCapability(Enum):
    PATH_NEEDS_HARDWIRE = -2
    r'''
    Path needs hardwire
    '''
    PATH_NEEDS_CONFIG_CHANNEL = -1
    r'''
    Path needs config channel
    '''
    PATH_AVAILABLE = 1
    r'''
    Path available
    '''
    PATH_EXISTS = 2
    r'''
    Path exists
    '''
    PATH_UNSUPPORTED = 3
    r'''
    Path Unsupported
    '''
    RESOURCE_IN_USE = 4
    r'''
    Resource in use
    '''
    EXCLUSION_CONFLICT = 5
    r'''
    Exclusion conflict
    '''
    CHANNEL_NOT_AVAILABLE = 6
    r'''
    Channel not available
    '''
    CHANNELS_HARDWIRED = 7
    r'''
    Channels hardwired
    '''
