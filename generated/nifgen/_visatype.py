import ctypes


'''Definitions of the VISA types used by the C API of the driver runtime.
These are aliased directly to ctypes types so can be used directly to call into the library.
'''


ViStatus = ctypes.c_long
ViRsrc = ctypes.c_char_p
ViSession = ctypes.c_ulong
ViChar = ctypes.c_char
ViUInt32 = ctypes.c_ulong
ViInt32 = ctypes.c_long
ViInt16 = ctypes.c_short
ViInt8 = ctypes.c_int8
ViUInt16 = ctypes.c_ushort
ViInt64 = ctypes.c_longlong
ViString = ctypes.c_char_p
ViAttr = ctypes.c_long
ViConstString = ViString
ViBoolean = ctypes.c_ushort
ViReal32 = ctypes.c_float
ViReal64 = ctypes.c_double

