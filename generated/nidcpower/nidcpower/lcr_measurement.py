import cmath
from collections import namedtuple
import ctypes
import math

import nidcpower._visatype
import nidcpower.enums as enums


# This class is an internal implementation detail
# ctypes definition
# Name must match exactly what the name of the structure type is named in the C API.
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

    def __init__(self, data=None):
        super(ctypes.Structure, self).__init__()
        if data is not None:
            if isinstance(data, LCRMeasurement):
                self.vdc = data.vdc
                self.idc = data.idc
                self.stimulus_frequency = data.stimulus_frequency
                self.ac_voltage_real = data.ac_voltage.real
                self.ac_voltage_imaginary = data.ac_voltage.imag
                self.ac_current_real = data.ac_current.real
                self.ac_current_imaginary = data.ac_current.imag
                self.z_real = data.z.real
                self.z_imaginary = data.z.imag
                self.z_magnitude, self.z_phase = data.get_z_magnitude_and_phase()
                y = data.get_y()
                self.y_real = y.real
                self.y_imaginary = y.imag
                self.y_magnitude, self.y_phase = data.get_y_magnitude_and_phase()
                self.ls, self.cs, self.rs = data.series_lcr
                self.lp, self.cp, self.rp = data.parallel_lcr
                self.d = data.d
                self.q = data.get_q()
                self.measurement_mode = enums.InstrumentMode(data.measurement_mode).value
                self.dc_in_compliance, self.ac_in_compliance = data.in_compliances
                self.unbalanced = data.unbalanced
            else:
                for field_name, _ in struct_NILCRMeasurement._fields_:
                    setattr(self, field_name, getattr(data, field_name))
        else:
            # Assign default value for all fields
            for field_name, _ in struct_NILCRMeasurement._fields_:
                setattr(self, field_name, 0)


class LCRMeasurement(object):
    LCR = namedtuple(typename="LCR", field_names=("inductance", "capacitance", "resistance"))
    InCompliances = namedtuple(typename="InCompliances", field_names=("dc", "ac"))

    _lcr_measurement_field_metadata = [
        # field_name           label(s)
        ("channel"           , "Channel"                               ),  # noqa: E202,E203
        ("vdc"               , "V DC"                                  ),  # noqa: E202,E203
        ("idc"               , "I DC"                                  ),  # noqa: E202,E203
        ("stimulus_frequency", "Stimulus frequency"                    ),  # noqa: E202,E203
        ("ac_voltage"        , "AC voltage"                            ),  # noqa: E202,E203
        ("ac_current"        , "AC current"                            ),  # noqa: E202,E203
        ("z"                 , "Z"                                     ),  # noqa: E202,E203
        ("series_lcr"        , ("Ls", "Cs", "Rs")                      ),  # noqa: E202,E203
        ("parallel_lcr"      , ("Lp", "Cp", "Rp")                      ),  # noqa: E202,E203
        ("d"                 , "D"                                     ),  # noqa: E202,E203
        ("measurement_mode"  , "Measurement mode"                      ),  # noqa: E202,E203
        ("in_compliances"    , ("DC in compliance", "AC in compliance")),  # noqa: E202,E203
        ("unbalanced"        , "Unbalanced"                            ),  # noqa: E202,E203
    ]

    def __init__(
        self,
        data=None,
        channel="",
        vdc=0.0,
        idc=0.0,
        stimulus_frequency=0.0,
        ac_voltage=complex(),
        ac_current=complex(),
        z=complex(),
        series_lcr=LCR(inductance=0.0, capacitance=0.0, resistance=0.0),
        parallel_lcr=LCR(inductance=0.0, capacitance=0.0, resistance=0.0),
        d=0.0,
        measurement_mode=enums.InstrumentMode.LCR,
        in_compliances=InCompliances(dc=False, ac=False),
        unbalanced=False,
    ):
        """LCRMeasurement

        Creates and returns an LCRMeasurement object.

        Args:
            channel (str): The channel name associated with this LCRMeasurement.

            data (LCRMeasurement, struct_NILCRMeasurement): Specifies an LCR measurement object to
                copy from. If it is None, the values from the other parameters are used instead.

            vdc (float): Specifies the measured DC voltage, in volts.

            idc (float): Specifies the measured DC current, in amps.

            stimulus_frequency (float): Specifies the frequency of the LCR test signal, in Hz.

            ac_voltage (complex): Specifies the measured AC voltage, in volts RMS.

            ac_current (complex): Specifies the measured AC current, in amps RMS.

            z (complex): Specifies the complex impedance.

            series_lcr (LCR): Specifies the inductance, in henrys, the capacitance, in farads, and
                the resistance, in ohms, as measured using a series circuit model.

            parallel_lcr (LCR): Specifies the inductance, in henrys, the capacitance, in farads, and
                the resistance, in ohms, as measured using a parallel circuit model.

            d (float): The dissipation factor of the circuit.

            measurement_mode (enums.InstrumentMode): Specifies the measurement mode.
                **Defined Values**:

                +-----------------------+-----------------------------------------------------+
                | InstrumentMode.SMU_PS | The channel(s) are operating as a power supply/SMU. |
                +-----------------------+-----------------------------------------------------+
                | InstrumentMode.LCR    | The channel(s) are operating as an LCR meter.       |
                +-----------------------+-----------------------------------------------------+

            in_compliances (InCompliances): Indicates whether the output was in DC compliance and/or
                AC compliance at the time the measurement was taken.

            unbalanced (bool): Indicates whether the output was unbalanced at the time the
                measurement was taken.
        """
        if data is not None:
            if isinstance(data, struct_NILCRMeasurement):
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
                self.in_compliances = LCRMeasurement.InCompliances(
                    dc=bool(data.dc_in_compliance), ac=bool(data.ac_in_compliance)
                )
                self.unbalanced = bool(data.unbalanced)
            else:
                for field_name, _ in LCRMeasurement._lcr_measurement_field_metadata:
                    setattr(
                        self,
                        field_name,
                        enums.InstrumentMode(data.measurement_mode)
                        if field_name == "measurement_mode"
                        else getattr(data, field_name),
                    )
        else:
            for field_name, _ in LCRMeasurement._lcr_measurement_field_metadata:
                setattr(
                    self,
                    field_name,
                    enums.InstrumentMode(measurement_mode)
                    if field_name == "measurement_mode"
                    else locals()[field_name],
                )

    def get_z_magnitude_and_phase(self):
        """get_z_magnitude_and_phase

        Returns a tuple of (z_magnitude, z_phase) of this LCRMeasurement object.

        Returns:
            z_magnitude_and_phase (tuple of (float, float)):

                - **z_magnitude** (float): The magnitude of the complex impedance, in ohms.
                - **z_phase** (float): The impedance phase angle, in degrees.

        """
        return cmath.polar(self.z)

    def get_y(self):
        """get_y

        Returns the admittance of this LCRMeasurement object.

        Returns:
            y (complex): The complex admittance.

        """
        if self.z == 0:
            return complex(cmath.nan, cmath.nan)
        return 1.0 / self.z

    def get_y_magnitude_and_phase(self):
        """get_y_magnitude_and_phase

        Returns a tuple of (y_magnitude, y_phase) of this LCRMeasurement object.

        Returns:
            y_magnitude_and_phase (tuple of (float, float)):

                - **y_magnitude** (float): The magnitude of the complex admittance, in siemens.
                - **y_phase** (float): The admittance phase angle, in degrees.

        """
        return cmath.polar(self.get_y())

    def get_q(self):
        """get_q

        Returns the quality factor of this LCRMeasurement object.

        Returns:
            q (float): The quality factor of the circuit.

        """
        if self.d == 0:
            return math.nan
        return 1.0 / self.d

    def __repr__(self):
        field_value_strings = []
        for field_name, _ in LCRMeasurement._lcr_measurement_field_metadata:
            field_value = getattr(self, field_name)
            if isinstance(field_value, tuple):
                value_string = "{0}.{1}".format(self.__class__.__name__, field_value)
            elif isinstance(field_value, str):
                value_string = '"{0}"'.format(field_value)
            else:
                value_string = str(field_value)
            field_value_strings.append("{0}={1}".format(field_name, value_string))
        return "{0}(data=None, {1})".format(self.__class__.__name__, ", ".join(field_value_strings))

    def __str__(self):
        max_field_label_len = max(
            len(max(field_label, key=len) if isinstance(field_label, tuple) else field_label)
            for _, field_label, in LCRMeasurement._lcr_measurement_field_metadata
        )
        field_value_strings = []
        for field_name, field_label in LCRMeasurement._lcr_measurement_field_metadata:
            # Determines row_format
            if field_name in ("channel", "measurement_mode", "in_compliances", "unbalanced"):
                row_format = "{{:<{}}}: {{:}}\n".format(max_field_label_len)
            else:
                row_format = "{{:<{}}}: {{:,.6g}}\n".format(max_field_label_len)
            # Process namedtuple fields
            if isinstance(field_label, tuple):
                for label, value in zip(field_label, getattr(self, field_name)):
                    field_value_strings.append(
                        row_format.format(
                            label, bool(value) if field_name == "in_compliances" else value
                        )
                    )
            else:
                field_value = getattr(self, field_name)
                if field_name == "measurement_mode":
                    field_value = enums.InstrumentMode(field_value).name
                elif field_name == "unbalanced":
                    field_value = bool(field_value)
                field_value_strings.append(row_format.format(field_label, field_value))
        return "".join(field_value_strings)
