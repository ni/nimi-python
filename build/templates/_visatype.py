# -*- coding: utf-8 -*-
import ctypes


'''Definitions of the VISA types used by the C API of the driver runtime.
These are aliased directly to ctypes types so can be used directly to call into the library.
'''


ViStatus = ctypes.c_long
ViRsrc = ctypes.c_char_p
ViSession = ctypes.c_ulong
ViChar = ctypes.c_char
ViInt8 = ctypes.c_int8
ViInt16 = ctypes.c_int16
ViUInt16 = ctypes.c_uint16
ViInt32 = ctypes.c_int32
ViUInt32 = ctypes.c_uint32
ViInt64 = ctypes.c_int64
ViString = ctypes.c_char_p
ViAttr = ctypes.c_long
ViConstString = ViString
ViBoolean = ctypes.c_ushort
ViReal32 = ctypes.c_float
ViReal64 = ctypes.c_double

