import ctypes
import numbers
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
    """Constructs a DUT specification for a given frequency to use in LCR load compensation."""

    def __init__(
        self,
        frequency=0.0,
        impedance=None,
        ideal_capacitance=None,
        ideal_inductance=None,
        ideal_resistance=None,
    ):
        """LCRLoadCompensationSpot

        Creates and returns an LCRLoadCompensationSpot object. At most one of impedance,
            ideal_capacitance, ideal_inductance and ideal_resistance can be set, and the remaining
            parameters (excluding frequency) must be None. The parameter that is not None specifies
            the known specification value of the DUT to be used as the basis for load compensation.
            If all of them are None, then the default value of `impedance=complex()` will be used.

        Args:
            frequency (float): Specifies the spot frequency, in Hz.

            impedance (complex): Specifies the actual impedance of your DUT to be used as the basis
                for load compensation, or None to use another type of DUT specification value.

            ideal_capacitance (float): Specifies the ideal capacitance of your DUT to be used as the
                basis for load compensation, or None to use another type of DUT specification value.

            ideal_inductance (float): Specifies the ideal inductance of your DUT to be used as the
                basis for load compensation, or None to use another type of DUT specification value.

            ideal_resistance (float): Specifies the ideal resistance of your DUT to be used as the
                basis for load compensation, or None to use another type of DUT specification value.
        """
        self.frequency = frequency
        # Set default values
        self.reference_value_type = enums.LCRReferenceValueType.IMPEDANCE
        self.reference_value = complex()
        # Input validations
        none_count = 0
        for uppercase_parameter_name in enums.LCRReferenceValueType.__members__:
            parameter_name = uppercase_parameter_name.lower()
            parameter = locals()[parameter_name]
            if parameter is None:
                none_count += 1
            elif parameter_name == "impedance" and not isinstance(parameter, numbers.Complex):
                raise TypeError("Parameter impedance must be of type complex")
            elif parameter_name != "impedance" and not isinstance(parameter, numbers.Real):
                raise TypeError("Parameter {} must be a real number".format(parameter_name))
            else:
                self.reference_value_type = getattr(
                    enums.LCRReferenceValueType, uppercase_parameter_name
                )
                self.reference_value = parameter

        if none_count < len(enums.LCRReferenceValueType) - 1:
            raise ValueError(
                "At most one of {0} parameters can be set and the remaining parameters must be None".format(
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
