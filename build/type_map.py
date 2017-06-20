#!/usr/bin/python3
# Default type mapping for API <--> ctypes
# Works for IVI drivers

type_map = {
    'ViStatus':      {'python_type':'int', 'ctypes_type':'c_long'},
    'ViRsrc':        {'python_type':'str', 'ctypes_type':'c_char_p'},
    'ViBoolean':     {'python_type':'bool', 'ctypes_type':'c_ushort'},
    'ViSession':     {'python_type':'int', 'ctypes_type':'c_ulong'},
    'ViChar':        {'python_type':'int', 'ctypes_type':'c_char_p'},
    'ViUInt32':      {'python_type':'int', 'ctypes_type':'c_ulong'},
    'ViInt32':       {'python_type':'int', 'ctypes_type':'c_long'},
    'ViInt16':       {'python_type':'int', 'ctypes_type':'c_short'},
    'ViUInt16':      {'python_type':'int', 'ctypes_type':'c_ushort'},
    'ViReal32':      {'python_type':'float', 'ctypes_type':'c_float'},
    'ViReal64':      {'python_type':'float', 'ctypes_type':'c_double'},
    'ViString':      {'python_type':'str', 'ctypes_type':'c_char_p'},
    'ViConstString': {'python_type':'str', 'ctypes_type':'c_char_p'},
    'ViAttr':        {'python_type':'int', 'ctypes_type':'c_long'},
}

