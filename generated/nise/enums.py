# -*- coding: utf-8 -*-
# This file was generated

from enum import Enum


class ExpandAction(Enum):
    ROUTES = 0
    '''
    Expand to routes
    '''
    PATHS = 1
    '''
    Expand to paths
    '''


class MulticonnectMode(Enum):
    DEFAULT = -1
    '''
    Default
    '''
    NO_MULTICONNECT = 0
    '''
    No multiconnect
    '''
    MULTICONNECT = 1
    '''
    Multiconnect
    '''


class OperationOrder(Enum):
    BEFORE = 1
    '''
    Break before make
    '''
    AFTER = 2
    '''
    Break after make
    '''


class PathCapability(Enum):
    PATH_NEEDS_HARDWIRE = -2
    '''
    Path needs hardwire
    '''
    PATH_NEEDS_CONFIG_CHANNEL = -1
    '''
    Path needs config channel
    '''
    PATH_AVAILABLE = 1
    '''
    Path available
    '''
    PATH_EXISTS = 2
    '''
    Path exists
    '''
    PATH_UNSUPPORTED = 3
    '''
    Path Unsupported
    '''
    RESOURCE_IN_USE = 4
    '''
    Resource in use
    '''
    EXCLUSION_CONFLICT = 5
    '''
    Exclusion conflict
    '''
    CHANNEL_NOT_AVAILABLE = 6
    '''
    Channel not available
    '''
    CHANNELS_HARDWIRED = 7
    '''
    Channels hardwired
    '''
