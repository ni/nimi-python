#!/usr/bin/python3
# Default type mapping for API <--> ctypes
# Works for IVI drivers

type_map = {
    'ViStatus': 'c_long',
    'ViRsrc': 'c_char_p',
    'ViBoolean': 'c_ushort',
    'ViSession': 'c_ulong',
    'ViChar': 'c_char_p',
    'ViUInt32': 'c_ulong',
    'ViInt32': 'c_long',
    'ViInt16': 'c_short',
    'ViUInt16': 'c_ushort',
    'ViReal32': 'c_float',
    'ViReal64': 'c_double',
    'ViString': 'c_char_p',
    'ViConstString': 'c_char_p',
    'ViAttr': 'c_long',
}


