#!/usr/bin/python

import ctypes

class ViStatus_ctype(ctypes.c_long):
    pass

class ViRsrc_ctype(ctypes.c_char_p):
    pass

class ViSession_ctype(ctypes.c_ulong):
    pass

class ViChar_ctype(ctypes.c_char_p):
    pass

class ViUInt32_ctype(ctypes.c_ulong):
    pass

class ViInt32_ctype(ctypes.c_long):
    pass

class ViInt16_ctype(ctypes.c_short):
    pass

class ViUInt16_ctype(ctypes.c_ushort):
    pass

class ViString_ctype(ctypes.c_char_p):
    pass

class ViAttr_ctype(ctypes.c_long):
    pass

class ViConstString_ctype(ViString_ctype):
    @property
    def value(self): # Makes 'value' readonly
        return super(ViConstString_ctype, ViString_ctype).value

class ViBoolean_ctype(ctypes.c_ushort):
    @classmethod
    def from_param(cls, param):
        return ctypes.c_uint16(1) if bool(param) else ctypes.c_uint16(0)

class ViReal32_ctype(ctypes.c_float):
    @classmethod
    def from_param(cls, param):
        return ctypes.c_float(param)

class ViReal64_ctype(ctypes.c_double):
    @classmethod
    def from_param(cls, param):
        return ctypes.c_double(param)


