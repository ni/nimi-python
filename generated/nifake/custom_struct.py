import ctypes

from nifake import visatype


class CustomStruct(ctypes.Structure):
    _fields_ = [
        ('struct_int', visatype.ViInt32),
        ('struct_double', visatype.ViReal64),
    ]

    def __init__(self, data=None):
        if data is not None:
            super(ctypes.Structure, self).__init__(data.struct_int, data.struct_double)
        else:
            super(ctypes.Structure, self).__init__(0, 0.0)



class CustomStructPython(object):
    def __init__(self, data=None):
        if data is not None:
            if isinstance(data, custom_struct):
                self.struct_int = data.struct_int
                self.struct_double = data.struct_double
            elif isinstance(data, CustomStruct):
                self.struct_int = data.struct_int
                self.struct_double = data.struct_double
        else:
            self.struct_int = 0
            self.struct_double = 0.0


custom_struct = CustomStructPython

