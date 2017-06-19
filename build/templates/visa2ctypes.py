#!/usr/bin/python

from ctypes import *

class ViStatus(c_long):
    pass

class ViRsrc(c_char_p):
    pass

class ViSession(c_ulong):
    pass

class ViChar(c_char_p):
    pass

class ViUInt32(c_ulong):
    pass

class ViInt32(c_long):
    pass

class ViInt16(c_short):
    pass

class ViUInt16(c_ushort):
    pass

class ViString(c_char_p):
    pass

class ViAttr(c_long):
    pass

class ViConstString(ViString):
    @property
    def value(self): # Makes 'value' readonly
        return super(ViConstString, ViString).value

class ViBoolean(c_ushort):
    @classmethod
    def from_param(cls, param):
        return ctypes.c_uint16(1) if bool(param) else ctypes.c_uint16(0)

class ViReal32(c_float):
    @classmethod
    def from_param(cls, param):
        return ctypes.c_float(param)

class ViReal64(c_double):
    @classmethod
    def from_param(cls, param):
        return ctypes.c_double(param)


