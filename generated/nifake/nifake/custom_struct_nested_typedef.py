import ctypes

import nifake.custom_struct as custom_struct
import nifake.custom_struct_typedef as custom_struct_typedef


class struct_CustomStructNestedTypedef(ctypes.Structure):  # noqa N801
    _fields_ = [
        ('struct_custom_struct', custom_struct.struct_CustomStruct),
        ('struct_custom_struct_typedef', custom_struct_typedef.struct_CustomStructTypedef),
    ]

    def __init__(self, data=None):
        super(ctypes.Structure, self).__init__()
        if data is not None:
            self.struct_custom_struct = custom_struct.struct_CustomStruct(data.struct_custom_struct)
            self.struct_custom_struct_typedef = custom_struct_typedef.struct_CustomStructTypedef(
                data.struct_custom_struct_typedef
            )
        else:
            self.struct_custom_struct = custom_struct.struct_CustomStruct()
            self.struct_custom_struct_typedef = custom_struct_typedef.struct_CustomStructTypedef()


class CustomStructNestedTypedef:
    def __init__(
        self,
        data=None,
        struct_custom_struct=custom_struct.CustomStruct(),
        struct_custom_struct_typedef=custom_struct_typedef.CustomStructTypedef()
    ):
        if data is not None:
            self.struct_custom_struct = custom_struct.CustomStruct(data.struct_custom_struct)
            self.struct_custom_struct_typedef = custom_struct_typedef.CustomStructTypedef(
                data.struct_custom_struct_typedef
            )
        else:
            self.struct_custom_struct = struct_custom_struct
            self.struct_custom_struct_typedef = struct_custom_struct_typedef

    def _create_copy(self, target_class):
        sample_object = target_class()
        return target_class(
            struct_custom_struct=self.struct_custom_struct._create_copy(
                type(sample_object.struct_custom_struct)
            ),
            struct_custom_struct_typedef=self.struct_custom_struct_typedef._create_copy(
                type(sample_object.struct_custom_struct_typedef)
            ),
        )

    def __repr__(self):
        return '{}(data=None, struct_custom_struct={}, struct_custom_struct_typedef={})'.format(
            self.__class__.__name__,
            repr(self.struct_custom_struct),
            repr(self.struct_custom_struct_typedef)
        )

    def __str__(self):
        return self.__repr__()
