

class ViStatus(int):
    pass


class ViRsrc(str):
    pass


class ViSession(int):
    pass


class ViChar(int):
    pass


class ViUInt32(int):
    pass


class ViInt32(int):
    pass


class ViInt16(int):
    pass


class ViUInt16(int):
    pass


class ViString(str):
    pass


class ViAttr(int):
    pass


class ViConstString(ViString):
    @property
    def value(self):  # Makes 'value' readonly
        return super(ViConstString, ViString)


# Python's bool cannot be subclassed:
# https://mail.python.org/pipermail/python-dev/2002-March/020822.html
class ViBoolean(int):
    @classmethod
    def from_param(cls, param):
        return 1 if bool(param) else 0


class ViReal32(float):
    pass


class ViReal64(float):
    pass
