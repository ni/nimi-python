import cmath
import pytest

import nidcpower


@pytest.mark.parametrize(
    (
        "python_class, ctype_class, init_params, expected_python_members, expected_ctype_members, "
        "expected_repr, expected_str"
    ),
    [
        (
            nidcpower.LCRLoadCompensationSpot,  # python_class
            nidcpower.struct_NILCRLoadCompensationSpot,  # ctype_class
            # init_params
            {},
            # expected_python_members
            {
                "frequency": 0.0,
                "reference_value_type": nidcpower.LCRReferenceValueType.IMPEDANCE,
                "reference_value": complex(),
            },
            # expected_ctype_members
            {
                "frequency": 0.0,
                "reference_value_type": nidcpower.LCRReferenceValueType.IMPEDANCE.value,
                "reference_value_a": 0.0,
                "reference_value_b": 0.0,
            },
            # expected_repr
            "LCRLoadCompensationSpot(data=None, frequency=0.0, impedance=0j)",
            # expected_str
            (
                "Frequency           : 0\n"
                "Reference Value Type: IMPEDANCE\n"
                "Reference Value     : 0+0j\n"
            ),
        ),
        (
            nidcpower.LCRLoadCompensationSpot,  # python_class
            nidcpower.struct_NILCRLoadCompensationSpot,  # ctype_class
            # init_params
            {"frequency": 10_000.0, "ideal_resistance": 100.0},
            # expected_python_members
            {
                "frequency": 10_000.0,
                "reference_value_type": nidcpower.LCRReferenceValueType.IDEAL_RESISTANCE,
                "reference_value": 100.0,
            },
            # expected_ctype_members
            {
                "frequency": 10_000.0,
                "reference_value_type": nidcpower.LCRReferenceValueType.IDEAL_RESISTANCE.value,
                "reference_value_a": 100.0,
                "reference_value_b": 0.0,
            },
            # expected_repr
            "LCRLoadCompensationSpot(data=None, frequency=10000.0, ideal_resistance=100.0)",
            # expected_str
            (
                "Frequency           : 10,000\n"
                "Reference Value Type: IDEAL_RESISTANCE\n"
                "Reference Value     : 100\n"
            ),
        ),
        (
            nidcpower.LCRMeasurement,  # python_class
            nidcpower.struct_NILCRMeasurement,  # ctype_class
            # init_params
            {},
            # expected_python_members
            {
                "vdc": 0.0,
                "idc": 0.0,
                "stimulus_frequency": 0.0,
                "ac_voltage": complex(),
                "ac_current": complex(),
                "z": complex(),
                "series_lcr": nidcpower.LCRMeasurement.LCR(
                    inductance=0.0, capacitance=0.0, resistance=0.0
                ),
                "parallel_lcr": nidcpower.LCRMeasurement.LCR(
                    inductance=0.0, capacitance=0.0, resistance=0.0
                ),
                "d": 0.0,
                "measurement_mode": nidcpower.InstrumentMode.LCR,
                "in_compliances": nidcpower.LCRMeasurement.InCompliances(dc=False, ac=False),
                "unbalanced": False,
            },
            # expected_ctype_members
            {
                "vdc": 0.0,
                "idc": 0.0,
                "stimulus_frequency": 0.0,
                "ac_voltage_real": 0.0,
                "ac_voltage_imaginary": 0.0,
                "ac_current_real": 0.0,
                "ac_current_imaginary": 0.0,
                "z_real": 0.0,
                "z_imaginary": 0.0,
                "z_magnitude": 0.0,
                "z_phase": 0.0,
                "y_real": cmath.nan,
                "y_imaginary": cmath.nan,
                "y_magnitude": cmath.nan,
                "y_phase": cmath.nan,
                "ls": 0.0,
                "cs": 0.0,
                "rs": 0.0,
                "lp": 0.0,
                "cp": 0.0,
                "rp": 0.0,
                "d": 0.0,
                "q": cmath.nan,
                "measurement_mode": nidcpower.InstrumentMode.LCR.value,
                "dc_in_compliance": False,
                "ac_in_compliance": False,
                "unbalanced": False,
            },
            # expected_repr
            (
                "LCRMeasurement(data=None, "
                "vdc=0.0, "
                "idc=0.0, "
                "stimulus_frequency=0.0, "
                "ac_voltage=0j, "
                "ac_current=0j, "
                "z=0j, "
                "series_lcr=LCRMeasurement.LCR(inductance=0.0, capacitance=0.0, resistance=0.0), "
                "parallel_lcr=LCRMeasurement.LCR(inductance=0.0, capacitance=0.0, resistance=0.0), "
                "d=0.0, "
                "measurement_mode=InstrumentMode.LCR, "
                "in_compliances=LCRMeasurement.InCompliances(dc=False, ac=False), "
                "unbalanced=False)"
            ),
            # expected_str
            (
                "V DC              : 0\n"
                "I DC              : 0\n"
                "Stimulus frequency: 0\n"
                "AC voltage        : 0+0j\n"
                "AC current        : 0+0j\n"
                "Z                 : 0+0j\n"
                "Ls                : 0\n"
                "Cs                : 0\n"
                "Rs                : 0\n"
                "Lp                : 0\n"
                "Cp                : 0\n"
                "Rp                : 0\n"
                "D                 : 0\n"
                "Measurement mode  : LCR\n"
                "DC in compliance  : False\n"
                "AC in compliance  : False\n"
                "Unbalanced        : False\n"
            ),
        ),
        (
            nidcpower.LCRMeasurement,  # python_class
            nidcpower.struct_NILCRMeasurement,  # ctype_class
            # init_params
            {
                "vdc": 0.1,
                "idc": 0.001,
                "stimulus_frequency": 10_000.0,
                "ac_voltage": complex(1.0, 0.1),
                "ac_current": complex(0.01, 0.001),
                "z": complex(100, 10),
                "series_lcr": nidcpower.LCRMeasurement.LCR(
                    inductance=10.0, capacitance=20.0, resistance=90.0
                ),
                "parallel_lcr": nidcpower.LCRMeasurement.LCR(
                    inductance=30.0, capacitance=40.0, resistance=110.0
                ),
                "d": 10.0,
                "measurement_mode": nidcpower.InstrumentMode.SMU_PS,
                "in_compliances": nidcpower.LCRMeasurement.InCompliances(dc=True, ac=True),
                "unbalanced": True,
            },
            # expected_python_members
            {
                "vdc": 0.1,
                "idc": 0.001,
                "stimulus_frequency": 10_000.0,
                "ac_voltage": complex(1.0, 0.1),
                "ac_current": complex(0.01, 0.001),
                "z": complex(100.0, 10.0),
                "series_lcr": nidcpower.LCRMeasurement.LCR(
                    inductance=10.0, capacitance=20.0, resistance=90.0
                ),
                "parallel_lcr": nidcpower.LCRMeasurement.LCR(
                    inductance=30.0, capacitance=40.0, resistance=110.0
                ),
                "d": 10.0,
                "measurement_mode": nidcpower.InstrumentMode.SMU_PS,
                "in_compliances": nidcpower.LCRMeasurement.InCompliances(dc=True, ac=True),
                "unbalanced": True,
            },
            # expected_ctype_members
            {
                "vdc": 0.1,
                "idc": 0.001,
                "stimulus_frequency": 10_000.0,
                "ac_voltage_real": 1.0,
                "ac_voltage_imaginary": 0.1,
                "ac_current_real": 0.01,
                "ac_current_imaginary": 0.001,
                "z_real": 100.0,
                "z_imaginary": 10.0,
                "z_magnitude": 100.49876,
                "z_phase": 0.099668652,
                "y_real": 0.0099009901,
                "y_imaginary": -0.00099009901,
                "y_magnitude": 0.0099503719,
                "y_phase": -0.099668652,
                "ls": 10.0,
                "cs": 20.0,
                "rs": 90.0,
                "lp": 30.0,
                "cp": 40.0,
                "rp": 110.0,
                "d": 10.0,
                "q": 0.1,
                "measurement_mode": nidcpower.InstrumentMode.SMU_PS.value,
                "dc_in_compliance": True,
                "ac_in_compliance": True,
                "unbalanced": True,
            },
            # expected_repr
            (
                "LCRMeasurement(data=None, "
                "vdc=0.1, "
                "idc=0.001, "
                "stimulus_frequency=10000.0, "
                "ac_voltage=(1+0.1j), "
                "ac_current=(0.01+0.001j), "
                "z=(100+10j), "
                "series_lcr=LCRMeasurement.LCR(inductance=10.0, capacitance=20.0, resistance=90.0), "
                "parallel_lcr=LCRMeasurement.LCR(inductance=30.0, capacitance=40.0, resistance=110.0), "
                "d=10.0, "
                "measurement_mode=InstrumentMode.SMU_PS, "
                "in_compliances=LCRMeasurement.InCompliances(dc=True, ac=True), "
                "unbalanced=True)"
            ),
            # expected_str
            (
                "V DC              : 0.1\n"
                "I DC              : 0.001\n"
                "Stimulus frequency: 10,000\n"
                "AC voltage        : 1+0.1j\n"
                "AC current        : 0.01+0.001j\n"
                "Z                 : 100+10j\n"
                "Ls                : 10\n"
                "Cs                : 20\n"
                "Rs                : 90\n"
                "Lp                : 30\n"
                "Cp                : 40\n"
                "Rp                : 110\n"
                "D                 : 10\n"
                "Measurement mode  : SMU_PS\n"
                "DC in compliance  : True\n"
                "AC in compliance  : True\n"
                "Unbalanced        : True\n"
            ),
        ),
    ],
)
def test_custom_types(
    python_class,
    ctype_class,
    init_params,
    expected_python_members,
    expected_ctype_members,
    expected_repr,
    expected_str,
):
    initial_python_object = python_class(**init_params)
    copied_python_object = python_class(initial_python_object)
    converted_ctype_object = ctype_class(initial_python_object)
    copied_ctype_object = ctype_class(converted_ctype_object)
    converted_python_object = python_class(converted_ctype_object)

    for python_object in (initial_python_object, copied_python_object, converted_python_object):
        for member in expected_python_members:
            assert getattr(python_object, member) == pytest.approx(
                expected_python_members[member], nan_ok=True
            )
        assert repr(python_object) == expected_repr
        assert str(python_object) == expected_str

    for ctype_object in (converted_ctype_object, copied_ctype_object):
        for member in expected_ctype_members:
            assert getattr(ctype_object, member) == pytest.approx(
                expected_ctype_members[member], nan_ok=True
            )


@pytest.mark.parametrize(
    "ctype_class, expected_ctype_members",
    [
        (
            nidcpower.struct_NILCRLoadCompensationSpot,
            {
                "frequency": 0.0,
                "reference_value_type": nidcpower.LCRReferenceValueType.IMPEDANCE.value,
                "reference_value_a": 0.0,
                "reference_value_b": 0.0,
            },
        ),
        (
            nidcpower.struct_NILCRMeasurement,
            {
                "vdc": 0,
                "idc": 0,
                "stimulus_frequency": 0,
                "ac_voltage_real": 0,
                "ac_voltage_imaginary": 0,
                "ac_current_real": 0,
                "ac_current_imaginary": 0,
                "z_real": 0,
                "z_imaginary": 0,
                "z_magnitude": 0,
                "z_phase": 0,
                "y_real": 0,
                "y_imaginary": 0,
                "y_magnitude": 0,
                "y_phase": 0,
                "ls": 0,
                "cs": 0,
                "rs": 0,
                "lp": 0,
                "cp": 0,
                "rp": 0,
                "d": 0,
                "q": 0,
                "measurement_mode": 0,
                "dc_in_compliance": 0,
                "ac_in_compliance": 0,
                "unbalanced": 0,
            },
        ),
    ],
)
def test_custom_type_ctype_default_values(ctype_class, expected_ctype_members):
    ctype_object = ctype_class()
    for member in expected_ctype_members:
        assert getattr(ctype_object, member) == pytest.approx(
            expected_ctype_members[member], nan_ok=True
        )


@pytest.mark.parametrize(
    "init_params, expected_error_type",
    [
        ({"impedance": "1.0"}, TypeError),
        ({"ideal_capacitance": complex()}, TypeError),
        ({"ideal_inductance": complex()}, TypeError),
        ({"ideal_resistance": complex()}, TypeError),
        ({"impedance": complex(), "ideal_capacitance": 1.0}, ValueError),
    ],
)
def test_lcr_load_compensation_spot_input_error(init_params, expected_error_type):
    with pytest.raises(expected_error_type):
        nidcpower.LCRLoadCompensationSpot(**init_params)
