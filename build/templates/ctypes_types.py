import ctypes


class ViStatus(ctypes.c_long):  # noqa: N801
    pass


class ViSession(ctypes.c_ulong):  # noqa: N801
    pass


class ViChar(ctypes.c_char):  # noqa: N801
    pass


class ViUInt32(ctypes.c_ulong):  # noqa: N801
    pass


class ViInt32(ctypes.c_long):  # noqa: N801
    pass


class ViInt16(ctypes.c_short):  # noqa: N801
    pass


class ViUInt16(ctypes.c_ushort):  # noqa: N801
    pass


class ViInt64(ctypes.c_longlong):  # noqa: N801
    pass


class ViAttr(ctypes.c_long):  # noqa: N801
    pass


class ViBoolean(ctypes.c_ushort):  # noqa: N801
    @classmethod
    def from_param(cls, param):
        return ctypes.c_uint16(1) if bool(param) else ctypes.c_uint16(0)


class ViReal32(ctypes.c_float):  # noqa: N801
    @classmethod
    def from_param(cls, param):
        return ctypes.c_float(param)


class ViReal64(ctypes.c_double):  # noqa: N801
    @classmethod
    def from_param(cls, param):
        return ctypes.c_double(param)
