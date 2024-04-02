import ctypes

import nifake._visatype


# This class is an internal implementation detail
# ctypes definition
# Name must match exactly what the name of the structure type is named in the C API.
class struct_CustomStruct(ctypes.Structure):  # noqa N801
    _fields_ = [
        ('struct_int', nifake._visatype.ViInt32),
        ('struct_double', nifake._visatype.ViReal64),
    ]

    def __init__(self, data=None, struct_int=0, struct_double=0.0):
        super(ctypes.Structure, self).__init__()
        if data is not None:
            self.struct_int = data.struct_int
            self.struct_double = data.struct_double
        else:
            self.struct_int = struct_int
            self.struct_double = struct_double

    def __repr__(self):
        return f'{self.__class__.__name__}(data=None, struct_int={self.struct_int}, struct_double={self.struct_double})'

    def __str__(self):
        return self.__repr__()


class CustomStruct:
    def __init__(self, data=None, struct_int=0, struct_double=0.0):
        if data is not None:
            self.struct_int = data.struct_int
            self.struct_double = data.struct_double
        else:
            self.struct_int = struct_int
            self.struct_double = struct_double

    def _create_copy(self, target_class):
        return target_class(struct_int=self.struct_int, struct_double=self.struct_double)

    def __repr__(self):
        return f'{self.__class__.__name__}(data=None, struct_int={self.struct_int}, struct_double={self.struct_double})'

    def __str__(self):
        return self.__repr__()
