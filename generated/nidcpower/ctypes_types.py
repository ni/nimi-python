import ctypes


class ViStatus_ctype(ctypes.c_long):  # noqa: N801
    pass


class ViRsrc_ctype(ctypes.c_char_p):  # noqa: N801
    pass


class ViSession_ctype(ctypes.c_ulong):  # noqa: N801
    pass


class ViChar_ctype(ctypes.c_char):  # noqa: N801
    pass


class ViUInt32_ctype(ctypes.c_ulong):  # noqa: N801
    pass


class ViInt32_ctype(ctypes.c_long):  # noqa: N801
    pass


class ViInt16_ctype(ctypes.c_short):  # noqa: N801
    pass


class ViUInt16_ctype(ctypes.c_ushort):  # noqa: N801
    pass


class ViInt64_ctype(ctypes.c_longlong):  # noqa: N801
    pass


class ViString_ctype(ctypes.c_char_p):  # noqa: N801
    pass


class ViAttr_ctype(ctypes.c_long):  # noqa: N801
    pass


class ViConstString_ctype(ViString_ctype):  # noqa: N801
    @property
    def value(self):  # Makes 'value' readonly
        return super(ViConstString_ctype, ViString_ctype).value


class ViBoolean_ctype(ctypes.c_ushort):  # noqa: N801
    @classmethod
    def from_param(cls, param):
        return ctypes.c_uint16(1) if bool(param) else ctypes.c_uint16(0)


class ViReal32_ctype(ctypes.c_float):  # noqa: N801
    @classmethod
    def from_param(cls, param):
        return ctypes.c_float(param)


class ViReal64_ctype(ctypes.c_double):  # noqa: N801
    @classmethod
    def from_param(cls, param):
        return ctypes.c_double(param)
