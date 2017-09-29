

class ViStatus(int):
    def __new__(cls, val=0):
        return int(val)


class ViRsrc(str):
    def __new__(cls, val=0):
        return str(val)


class ViSession(int):
    def __new__(cls, val=0):
        return int(val)


class ViChar(int):
    def __new__(cls, val=0):
        return int(val)


class ViUInt32(int):
    def __new__(cls, val=0):
        return int(val)


class ViInt32(int):
    def __new__(cls, val=0):
        return int(val)


class ViInt16(int):
    def __new__(cls, val=0):
        return int(val)


class ViUInt16(int):
    def __new__(cls, val=0):
        return int(val)


class ViInt64(int):
    def __new__(cls, val=0):
        return int(val)


class ViString(str):
    def __new__(cls, val=0):
        return str(val)


class ViAttr(int):
    def __new__(cls, val=0):
        return int(val)


class ViConstString(ViString):
    @property
    def value(self):  # Makes 'value' readonly
        return super(ViConstString, ViString)

    def __new__(cls, val=0):
        return str(val)


# Python's bool cannot be subclassed:
# https://mail.python.org/pipermail/python-dev/2002-March/020822.html
class ViBoolean(int):
    @classmethod
    def from_param(cls, param):
        return True if bool(param) else False

    def __new__(cls, val=0):
        return bool(val)


class ViReal32(float):
    def __new__(cls, val=0):
        return float(val)


class ViReal64(float):
    def __new__(cls, val=0):
        return float(val)

