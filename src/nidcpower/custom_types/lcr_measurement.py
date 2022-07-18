from collections import namedtuple
import ctypes

import nidcpower._visatype
import nidcpower.enums as enums


# This class is an internal ctypes implementation detail that corresponds to
# NILCRMeasurement in the C API
class struct_NILCRMeasurement(ctypes.Structure):  # noqa N801
    _pack_ = 8
    _fields_ = [
        # field_name             field_ctype
        ("vdc"                 , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("idc"                 , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("stimulus_frequency"  , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("ac_voltage_real"     , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("ac_voltage_imaginary", nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("ac_current_real"     , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("ac_current_imaginary", nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("z_real"              , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("z_imaginary"         , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("z_magnitude"         , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("z_phase"             , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("y_real"              , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("y_imaginary"         , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("y_magnitude"         , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("y_phase"             , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("ls"                  , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("cs"                  , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("rs"                  , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("lp"                  , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("cp"                  , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("rp"                  , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("d"                   , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("q"                   , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("measurement_mode"    , nidcpower._visatype.ViUInt16 ),  # noqa: E202,E203
        ("dc_in_compliance"    , nidcpower._visatype.ViBoolean),  # noqa: E202,E203
        ("ac_in_compliance"    , nidcpower._visatype.ViBoolean),  # noqa: E202,E203
        ("unbalanced"          , nidcpower._visatype.ViBoolean),  # noqa: E202,E203
        ("reserved1"           , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("reserved2"           , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("reserved3"           , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("reserved4"           , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("reserved5"           , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("reserved6"           , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("reserved7"           , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
    ]


class LCRMeasurement(object):
    """Specifies an LCR measurement.

    Data attributes:
        channel (str): The channel name associated with this LCRMeasurement.

        vdc (float): The measured DC voltage, in volts.

        idc (float): The measured DC current, in amps.

        stimulus_frequency (float): The frequency of the LCR test signal, in Hz.

        ac_voltage (complex): The measured AC voltage, in volts RMS.

        ac_current (complex): The measured AC current, in amps RMS.

        z (complex): The complex impedance.

        series_lcr (LCR): The inductance, in henrys, the capacitance, in farads, and the resistance,
            in ohms, as measured using a series circuit model.

        parallel_lcr (LCR): The inductance, in henrys, the capacitance, in farads, and the
            resistance, in ohms, as measured using a parallel circuit model.

        d (float): The dissipation factor of the circuit. The dimensionless dissipation factor is
            directly proportional to how quickly an oscillating system loses energy. D is the
            reciprocal of Q, the quality factor.

        measurement_mode (enums.InstrumentMode): The measurement mode.
            **Defined Values**:

            +-----------------------+-----------------------------------------------------+
            | InstrumentMode.SMU_PS | The channel(s) are operating as a power supply/SMU. |
            +-----------------------+-----------------------------------------------------+
            | InstrumentMode.LCR    | The channel(s) are operating as an LCR meter.       |
            +-----------------------+-----------------------------------------------------+

        dc_in_compliance (bool): Indicates whether the output was in DC compliance at the time the
            measurement was taken.

        ac_in_compliance (bool): Indicates whether the output was in AC compliance at the time the
            measurement was taken.

        unbalanced (bool): Indicates whether the bridge was unbalanced at the time the measurement
            was taken.
    """
    LCR = namedtuple(typename="LCR", field_names=("inductance", "capacitance", "resistance"))

    _lcr_measurement_field_metadata = [
        # field_name           label(s)
        ("channel"           , "Channel"                                                             ),  # noqa: E202,E203
        ("vdc"               , "DC voltage"                                                          ),  # noqa: E202,E203
        ("idc"               , "DC current"                                                          ),  # noqa: E202,E203
        ("stimulus_frequency", "Stimulus frequency"                                                  ),  # noqa: E202,E203
        ("ac_voltage"        , "AC voltage"                                                          ),  # noqa: E202,E203
        ("ac_current"        , "AC current"                                                          ),  # noqa: E202,E203
        ("z"                 , "Impedance"                                                           ),  # noqa: E202,E203
        ("series_lcr"        , ("Series inductance", "Series capacitance", "Series resistance")      ),  # noqa: E202,E203
        ("parallel_lcr"      , ("Parallel inductance", "Parallel capacitance", "Parallel resistance")),  # noqa: E202,E203
        ("d"                 , "Dissipation factor"                                                  ),  # noqa: E202,E203
        ("measurement_mode"  , "Measurement mode"                                                    ),  # noqa: E202,E203
        ("dc_in_compliance"  , "DC in compliance"                                                    ),  # noqa: E202,E203
        ("ac_in_compliance"  , "AC in compliance"                                                    ),  # noqa: E202,E203
        ("unbalanced"        , "Unbalanced"                                                          ),  # noqa: E202,E203
    ]

    def __init__(self, data):
        """LCRMeasurement

        Creates and returns an instance of LCRMeasurement.

        Args:
            data (struct_NILCRMeasurement): The LCR measurement ctypes instance returned by the driver.
        """
        self._data = data
        self.channel = ""
        self.vdc = data.vdc
        self.idc = data.idc
        self.stimulus_frequency = data.stimulus_frequency
        self.ac_voltage = complex(data.ac_voltage_real, data.ac_voltage_imaginary)
        self.ac_current = complex(data.ac_current_real, data.ac_current_imaginary)
        self.z = complex(data.z_real, data.z_imaginary)
        self.series_lcr = LCRMeasurement.LCR(
            inductance=data.ls, capacitance=data.cs, resistance=data.rs
        )
        self.parallel_lcr = LCRMeasurement.LCR(
            inductance=data.lp, capacitance=data.cp, resistance=data.rp
        )
        self.d = data.d
        self.measurement_mode = enums.InstrumentMode(data.measurement_mode)
        self.dc_in_compliance = bool(data.dc_in_compliance)
        self.ac_in_compliance = bool(data.ac_in_compliance)
        self.unbalanced = bool(data.unbalanced)

    @property
    def z_magnitude_and_phase(self):
        """z_magnitude_and_phase

        Get the **magnitude** (float), in ohms and **phase angle** (float), in degrees of the
        complex impedance.
        """
        return self._data.z_magnitude, self._data.z_phase

    @property
    def y(self):
        """y

        Get the complex admittance (complex).
        """
        return complex(self._data.y_real, self._data.y_imaginary)

    @property
    def y_magnitude_and_phase(self):
        """y_magnitude_and_phase

        Get the **magnitude** (float), in siemens and **phase angle** (float), in degrees of the
        complex admittance.
        """
        return self._data.y_magnitude, self._data.y_phase

    @property
    def q(self):
        """q

        Get the quality factor (float) of the circuit. The dimensionless quality factor is inversely
        proportional to the degree of damping in a system. Q is the reciprocal of D, the dissipation
        factor.
        """
        return self._data.q

    def __str__(self):
        max_field_label_len = max(
            len(max(field_label, key=len) if isinstance(field_label, tuple) else field_label)
            for _, field_label, in LCRMeasurement._lcr_measurement_field_metadata
        )
        field_value_strings = []
        for field_name, field_label in LCRMeasurement._lcr_measurement_field_metadata:
            # Determines row_format
            if field_name in (
                "channel",
                "measurement_mode",
                "dc_in_compliance",
                "ac_in_compliance",
                "unbalanced"
            ):
                row_format = "{{:<{}}}: {{:}}\n".format(max_field_label_len)
            else:
                row_format = "{{:<{}}}: {{:,.6g}}\n".format(max_field_label_len)
            # Process namedtuple fields
            if isinstance(field_label, tuple):
                for label, value in zip(field_label, getattr(self, field_name)):
                    field_value_strings.append(row_format.format(label, value))
            else:
                field_value = getattr(self, field_name)
                if field_name == "measurement_mode":
                    field_value = enums.InstrumentMode(field_value).name
                elif field_name in ("dc_in_compliance", "ac_in_compliance", "unbalanced"):
                    field_value = bool(field_value)
                field_value_strings.append(row_format.format(field_label, field_value))
        return "".join(field_value_strings)
