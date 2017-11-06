import ctypes

from nifake import visatype


class CustomStruct(ctypes.Structure):
    _fields_ = [
        ('struct_int', visatype.ViInt32),
        ('struct_double', visatype.ViReal64),
    ]

    def __init__(self, data=None, struct_int=0, struct_double=0.0):
        super(ctypes.Structure, self).__init__()
        if data is not None:
            self.struct_int = data.struct_int
            self.struct_double = data.struct_double
        else:
            self.struct_int = struct_int
            self.struct_double = struct_double


class CustomStructPython(object):
    def __init__(self, data=None, struct_int=0, struct_double=0.0):
        if data is not None:
            self.struct_int = data.struct_int
            self.struct_double = data.struct_double
        else:
            self.struct_int = struct_int
            self.struct_double = struct_double


custom_struct = CustomStructPython

