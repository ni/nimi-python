# -*- coding: utf-8 -*-
# This file was generated
import ctypes
import nidmm._visatype as _visatype


class ComplexViReal64(ctypes.Structure):
    _fields_ = [("real", _visatype.ViReal64), ("imag", _visatype.ViReal64)]


class ComplexViReal32(ctypes.Structure):
    _fields_ = [("real", _visatype.ViReal32), ("imag", _visatype.ViReal32)]


class ComplexViInt16(ctypes.Structure):
    _fields_ = [("real", _visatype.ViInt16), ("imag", _visatype.ViInt16)]
