#!/usr/bin/python

from ctypes import *

def getLibraryName():
    #@TODO: Load correct library based on bitness / OS
    return "nidmm_64"

def getLibrary():
    library = CDLL(getLibraryName())

    """ Specify required argument types (function prototypes) and Return types.
        https://docs.python.org/3/library/ctypes.html#specifying-the-required-argument-types-function-prototypes
        https://docs.python.org/3/library/ctypes.html#return-types
        This provides some automatic conversion and error checking when calling NI-DMM functions.
        Strictly speaking, this is not necessary if/when we code-generate the calling code.
        It may have some performance impact as well.
    """

    library.niDMM_init.restype = c_long
    library.niDMM_init.argtypes = [c_char_p, c_ushort, c_ushort, POINTER(c_ulong)]

    library.niDMM_close.restype = c_long
    library.niDMM_close.argtypes = [c_ulong]

    library.niDMM_InitExtCal.restype = c_long
    library.niDMM_InitExtCal.argtypes = [c_char_p, c_char_p, POINTER(c_ulong)]

    library.niDMM_CloseExtCal.restype = c_long
    library.niDMM_CloseExtCal.argtypes = [c_ulong, c_ulong]

    library.niDMM_ConfigureMeasurementDigits.restype = c_long
    library.niDMM_ConfigureMeasurementDigits.argtypes = [c_ulong, c_long, c_double, c_double]

    library.niDMM_Read.restype = c_long
    library.niDMM_Read.argtypes = [c_ulong, c_long, POINTER(c_double)]

    library.niDMM_Read.restype = c_long
    library.niDMM_Read.argtypes = [c_ulong, c_long, POINTER(c_double)]

    library.niDMM_GetError.restype = c_long
    library.niDMM_GetError.argtypes = [c_ulong, POINTER(c_long), c_ulong, c_char_p]

    library.niDMM_GetErrorMessage.restype = c_long
    library.niDMM_GetErrorMessage.argtypes = [c_ulong, c_long, c_long, c_char_p]

    library.niDMM_ClearError.restype = c_long
    library.niDMM_ClearError.argtypes = [c_ulong]

    library.niDMM_GetAttributeViInt32.restype = c_long
    library.niDMM_GetAttributeViInt32.argtypes = [c_ulong, c_char_p, c_long, POINTER(c_long)]

    library.niDMM_SetAttributeViInt32.restype = c_long
    library.niDMM_SetAttributeViInt32.argtypes = [c_ulong, c_char_p, c_long, c_long]

    library.niDMM_GetAttributeViReal64.restype = c_long
    library.niDMM_GetAttributeViReal64.argtypes = [c_ulong, c_char_p, c_long, POINTER(c_double)]

    library.niDMM_SetAttributeViReal64.restype = c_long
    library.niDMM_SetAttributeViReal64.argtypes = [c_ulong, c_char_p, c_long, c_double]

    library.niDMM_GetAttributeViString.restype = c_long
    library.niDMM_GetAttributeViString.argtypes = [c_ulong, c_char_p, c_long, c_long, c_char_p]

    library.niDMM_SetAttributeViString.restype = c_long
    library.niDMM_SetAttributeViString.argtypes = [c_ulong, c_char_p, c_long, c_char_p]

    library.niDMM_GetAttributeViBoolean.restype = c_long
    library.niDMM_GetAttributeViBoolean.argtypes = [c_ulong, c_char_p, c_long, POINTER(c_ushort)]

    library.niDMM_SetAttributeViBoolean.restype = c_long
    library.niDMM_SetAttributeViBoolean.argtypes = [c_ulong, c_char_p, c_long, c_ushort]

    return library

