

class ViStatus(int):
    def python_type(self):
        return 'integer'


class ViRsrc(str):
    def python_type(self):
        return 'string'


class ViSession(int):
    def python_type(self):
        return 'integer'


class ViChar(int):
    def python_type(self):
        return 'integer'


class ViUInt32(int):
    def python_type(self):
        return 'integer'


class ViInt32(int):
    def python_type(self):
        return 'integer'


class ViInt16(int):
    def python_type(self):
        return 'integer'


class ViUInt16(int):
    def python_type(self):
        return 'integer'


class ViString(str):
    def python_type(self):
        return 'string'


class ViAttr(int):
    def python_type(self):
        return 'integer'


class ViConstString(ViString):
    @property
    def value(self):  # Makes 'value' readonly
        return super(ViConstString, ViString)

    def python_type(self):
        return 'string'


# Python's bool cannot be subclassed:
# https://mail.python.org/pipermail/python-dev/2002-March/020822.html
class ViBoolean(int):
    @classmethod
    def from_param(cls, param):
        return 1 if bool(param) else 0

    def python_type(self):
        return 'integer'


class ViReal32(float):
    def python_type(self):
        return 'float'


class ViReal64(float):
    def python_type(self):
        return 'float'

