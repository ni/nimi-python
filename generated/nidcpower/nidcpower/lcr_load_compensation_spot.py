import ctypes
import platform

import nidcpower._visatype
import nidcpower.enums as enums


# This class is an internal ctypes implementation detail that corresponds to
# NILCRLoadCompensationSpot in the C API
class struct_NILCRLoadCompensationSpot(ctypes.Structure):  # noqa N801
    if platform.system() == "Windows" and platform.architecture()[0] == "64bit":
        _pack_ = 8
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        _pack_ = 4
    else:
        _pack_ = 1
    _fields_ = [
        ("frequency", nidcpower._visatype.ViReal64),
        ("reference_value_type", nidcpower._visatype.ViInt32),
        ("reference_value_a", nidcpower._visatype.ViReal64),
        ("reference_value_b", nidcpower._visatype.ViReal64),
    ]

    def __init__(self, data):
        super(ctypes.Structure, self).__init__()
        self.frequency = data.frequency
        self.reference_value_type = enums.LCRReferenceValueType(data.reference_value_type).value
        if self.reference_value_type == enums.LCRReferenceValueType.IMPEDANCE.value:
            self.reference_value_a = data.reference_value.real
            self.reference_value_b = data.reference_value.imag
        else:
            self.reference_value_a = data.reference_value
            self.reference_value_b = 0.0


class LCRLoadCompensationSpot(object):
    """Specifies a DUT specification for a given frequency to use in LCR load compensation."""

    def __init__(
        self,
        frequency,
        impedance=None,
        ideal_capacitance=None,
        ideal_inductance=None,
        ideal_resistance=None,
    ):
        """LCRLoadCompensationSpot

        Creates and returns an LCRLoadCompensationSpot object. One and only one of impedance,
            ideal_capacitance, ideal_inductance and ideal_resistance can be anything other than
            None. This parameter specifies the known specification value of the DUT to be used as
            the basis for load compensation.

        Args:
            frequency (float): Specifies the spot frequency, in Hz.

            impedance (complex): Specifies the actual impedance, in ohms, of your DUT to be used as
                the basis for load compensation, or None to use another type of DUT specification
                value.

            ideal_capacitance (float): Specifies the ideal capacitance, in farads, of your DUT to be
                used as the basis for load compensation, or None to use another type of DUT
                specification value.

            ideal_inductance (float): Specifies the ideal inductance, in henrys, of your DUT to be
                used as the basis for load compensation, or None to use another type of DUT
                specification value.

            ideal_resistance (float): Specifies the ideal resistance, in ohms, of your DUT to be
                used as the basis for load compensation, or None to use another type of DUT
                specification value.
        """
        self.frequency = frequency
        # Input validation
        none_count = 0
        for uppercase_parameter_name in enums.LCRReferenceValueType.__members__:
            parameter_name = uppercase_parameter_name.lower()
            parameter = locals()[parameter_name]
            if parameter is None:
                none_count += 1
            else:
                self.reference_value_type = getattr(
                    enums.LCRReferenceValueType,
                    uppercase_parameter_name
                )
                self.reference_value = parameter

        if none_count != len(enums.LCRReferenceValueType) - 1:
            raise ValueError(
                "One and only one of {0} parameters can be anything other than None".format(
                    tuple(
                        uppercase_parameter_name.lower()
                        for uppercase_parameter_name in enums.LCRReferenceValueType.__members__
                    )
                )
            )

    def __repr__(self):
        return "{0}.{1}(frequency={2}, {3}={4})".format(
            self.__class__.__module__,
            self.__class__.__qualname__,
            self.frequency,
            self.reference_value_type.name.lower(),
            self.reference_value,
        )

    def __str__(self):
        return "".join(
            [
                "Frequency           : {:,.6g}\n".format(self.frequency),
                "Reference Value Type: {:}\n".format(self.reference_value_type.name),
                "Reference Value     : {:,.6g}\n".format(self.reference_value),
            ]
        )
