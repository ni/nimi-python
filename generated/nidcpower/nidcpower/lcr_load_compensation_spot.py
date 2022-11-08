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

    _lcr_reference_value_type_to_label_and_units = {
        enums.LCRReferenceValueType.IMPEDANCE: {
            "label": "Impedance        ",
            "unit": "Ω"
        },
        enums.LCRReferenceValueType.IDEAL_CAPACITANCE: {
            "label": "Ideal Capacitance",
            "unit": "F"
        },
        enums.LCRReferenceValueType.IDEAL_INDUCTANCE: {
            "label": "Ideal Inductance ",
            "unit": "H"
        },
        enums.LCRReferenceValueType.IDEAL_RESISTANCE: {
            "label": "Ideal Resistance ",
            "unit": "Ω"
        },
    }

    def __init__(self, frequency, reference_value_type, reference_value):
        """LCRLoadCompensationSpot

        Creates and returns an instance of LCRLoadCompensationSpot.

        Args:
            frequency (float): The spot frequency, in Hz.

            reference_value_type (enums.LCRReferenceValueType): A known specification value of your
                DUT to use as the basis for load compensation.

            reference_value (complex or float): A value that describes the reference_value_type
                specification. Use as indicated by the reference_value_type option you choose.
        """
        self.frequency = frequency
        self.reference_value_type = enums.LCRReferenceValueType(reference_value_type)
        self.reference_value = reference_value

    def __repr__(self):
        return "{0}.{1}(frequency={2}, reference_value_type={3}.{4}.{5}, reference_value={6})".format(
            self.__class__.__module__,
            self.__class__.__qualname__,
            self.frequency,
            enums.LCRReferenceValueType.__module__,
            enums.LCRReferenceValueType.__qualname__,
            self.reference_value_type.name,
            self.reference_value,
        )

    def __str__(self):
        return "".join(
            [
                "Frequency        : {:,.6g} Hz\n{}: {:,.6g} {}\n".format(
                    self.frequency,
                    LCRLoadCompensationSpot._lcr_reference_value_type_to_label_and_units[
                        self.reference_value_type
                    ]["label"],
                    self.reference_value,
                    LCRLoadCompensationSpot._lcr_reference_value_type_to_label_and_units[
                        self.reference_value_type
                    ]["unit"],
                ),
            ]
        )
