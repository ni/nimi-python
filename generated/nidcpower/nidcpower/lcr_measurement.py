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


class LCRMeasurement:
    """Specifies an LCR measurement.

    Data attributes:
        channel (str): The channel name associated with this LCRMeasurement.

        vdc (float): The measured DC voltage, in volts.

        idc (float): The measured DC current, in amps.

        stimulus_frequency (float): The frequency of the LCR test signal, in Hz.

        ac_voltage (complex): The measured AC voltage, in volts RMS.

        ac_current (complex): The measured AC current, in amps RMS.

        z (complex): The complex impedance.

        z_magnitude_and_phase (tuple of float): The magnitude, in ohms, and phase angle, in degrees,
            of the complex impedance.

        y (complex): The complex admittance.

        y_magnitude_and_phase (tuple of float): The magnitude, in siemens, and phase angle, in
            degrees, of the complex admittance.

        series_lcr (LCR): The inductance, in henrys, the capacitance, in farads, and the resistance,
            in ohms, as measured using a series circuit model.

        parallel_lcr (LCR): The inductance, in henrys, the capacitance, in farads, and the
            resistance, in ohms, as measured using a parallel circuit model.

        d (float): The dissipation factor of the circuit. The dimensionless dissipation factor is
            directly proportional to how quickly an oscillating system loses energy. D is the
            reciprocal of Q, the quality factor.

        q (float): The quality factor of the circuit. The dimensionless quality factor is inversely
            proportional to the degree of damping in a system. Q is the reciprocal of D, the
            dissipation factor.

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
        # field_name              label(s)                                                                unit(s)
        ("channel"              , "Channel"                                                             , None           ),  # noqa: E202,E203
        ("vdc"                  , "DC voltage"                                                          , "V"            ),  # noqa: E202,E203
        ("idc"                  , "DC current"                                                          , "A"            ),  # noqa: E202,E203
        ("stimulus_frequency"   , "Stimulus frequency"                                                  , "Hz"           ),  # noqa: E202,E203
        ("ac_voltage"           , "AC voltage"                                                          , "V RMS"        ),  # noqa: E202,E203
        ("ac_current"           , "AC current"                                                          , "A RMS"        ),  # noqa: E202,E203
        ("z"                    , "Impedance"                                                           , "Ω"            ),  # noqa: E202,E203
        ("z_magnitude_and_phase", ("Impedance magnitude", "Impedance phase")                            , ("Ω", "°")     ),  # noqa: E202,E203
        ("y"                    , "Admittance"                                                          , "S"            ),  # noqa: E202,E203
        ("y_magnitude_and_phase", ("Admittance magnitude", "Admittance phase")                          , ("S", "°")     ),  # noqa: E202,E203
        ("series_lcr"           , ("Series inductance", "Series capacitance", "Series resistance")      , ("H", "F", "Ω")),  # noqa: E202,E203
        ("parallel_lcr"         , ("Parallel inductance", "Parallel capacitance", "Parallel resistance"), ("H", "F", "Ω")),  # noqa: E202,E203
        ("d"                    , "Dissipation factor"                                                  , None           ),  # noqa: E202,E203
        ("q"                    , "Quality factor"                                                      , None           ),  # noqa: E202,E203
        ("measurement_mode"     , "Measurement mode"                                                    , None           ),  # noqa: E202,E203
        ("dc_in_compliance"     , "DC in compliance"                                                    , None           ),  # noqa: E202,E203
        ("ac_in_compliance"     , "AC in compliance"                                                    , None           ),  # noqa: E202,E203
        ("unbalanced"           , "Unbalanced"                                                          , None           ),  # noqa: E202,E203
    ]

    def __init__(self, data):
        """LCRMeasurement

        Creates and returns an instance of LCRMeasurement.

        Args:
            data (struct_NILCRMeasurement): The LCR measurement ctypes instance returned by the driver.
        """
        self.channel = ""
        self.vdc = data.vdc
        self.idc = data.idc
        self.stimulus_frequency = data.stimulus_frequency
        if hasattr(data, "ac_voltage_real"):
            self.ac_voltage = complex(data.ac_voltage_real, data.ac_voltage_imaginary)
            self.ac_current = complex(data.ac_current_real, data.ac_current_imaginary)
            self.z = complex(data.z_real, data.z_imaginary)
            self.y = complex(data.y_real, data.y_imaginary)
        else:
            self.ac_voltage = complex(data.ac_voltage.real, data.ac_voltage.imaginary)
            self.ac_current = complex(data.ac_current.real, data.ac_current.imaginary)
            self.z = complex(data.z.real, data.z.imaginary)
            self.y = complex(data.y.real, data.y.imaginary)
        self.z_magnitude_and_phase = (data.z_magnitude, data.z_phase)
        self.y_magnitude_and_phase = (data.y_magnitude, data.y_phase)
        self.series_lcr = LCRMeasurement.LCR(
            inductance=data.ls, capacitance=data.cs, resistance=data.rs
        )
        self.parallel_lcr = LCRMeasurement.LCR(
            inductance=data.lp, capacitance=data.cp, resistance=data.rp
        )
        self.d = data.d
        self.q = data.q
        self.measurement_mode = enums.InstrumentMode(data.measurement_mode)
        self.dc_in_compliance = bool(data.dc_in_compliance)
        self.ac_in_compliance = bool(data.ac_in_compliance)
        self.unbalanced = bool(data.unbalanced)

    def __str__(self):
        max_field_label_len = max(
            len(max(field_label, key=len) if isinstance(field_label, tuple) else field_label)
            for _, field_label, _ in LCRMeasurement._lcr_measurement_field_metadata
        )
        field_value_strings = []
        for field_name, field_label, field_unit in LCRMeasurement._lcr_measurement_field_metadata:
            # Determines row_format
            if field_name in (
                "channel",
                "measurement_mode",
                "dc_in_compliance",
                "ac_in_compliance",
                "unbalanced"
            ):
                row_format = f"{{:<{max_field_label_len}}}: {{:}}{{}}\n"
            else:
                row_format = f"{{:<{max_field_label_len}}}: {{:,.6g}}{{}}\n"
            # Process namedtuple fields
            if isinstance(field_label, tuple) and isinstance(field_unit, tuple):
                for label, unit, value in zip(field_label, field_unit, getattr(self, field_name)):
                    unit_string = f" {unit}" if unit is not None else ""
                    field_value_strings.append(row_format.format(label, value, unit_string))
            else:
                field_value = getattr(self, field_name)
                if field_name == "measurement_mode":
                    field_value = enums.InstrumentMode(field_value).name
                elif field_name in ("dc_in_compliance", "ac_in_compliance", "unbalanced"):
                    field_value = bool(field_value)
                unit_string = f" {field_unit}" if field_unit is not None else ""
                field_value_strings.append(row_format.format(field_label, field_value, unit_string))
        return "".join(field_value_strings)
