import cmath
import pytest

import nidcpower


@pytest.mark.parametrize(
    "ctype_members, channel, expected_python_members, expected_python_str",
    [
        (
            # ctype_members
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
                "z_phase": 5.7105931375,
                "y_real": 0.0099009901,
                "y_imaginary": -0.00099009901,
                "y_magnitude": 0.0099503719,
                "y_phase": -5.7105931375,
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
            # channel
            "Dev1/0",
            # expected_python_members
            {
                "channel": "Dev1/0",
                "vdc": 0.1,
                "idc": 0.001,
                "stimulus_frequency": 10_000.0,
                "ac_voltage": complex(1.0, 0.1),
                "ac_current": complex(0.01, 0.001),
                "z": complex(100.0, 10.0),
                "series_lcr": nidcpower.LCRMeasurement.LCR(
                    inductance=10.0,
                    capacitance=20.0,
                    resistance=90.0
                ),
                "parallel_lcr": nidcpower.LCRMeasurement.LCR(
                    inductance=30.0,
                    capacitance=40.0,
                    resistance=110.0
                ),
                "d": 10.0,
                "measurement_mode": nidcpower.InstrumentMode.SMU_PS,
                "in_compliances": nidcpower.LCRMeasurement.InCompliances(dc=True, ac=True),
                "unbalanced": True,
                # Derived properties
                "z_magnitude_and_phase": (100.49876, 5.7105931375),
                "y": complex(0.0099009901, -0.00099009901),
                "y_magnitude_and_phase": (0.0099503719, -5.7105931375),
                "q": 0.1
            },
            # expected_python_str
            (
                "Channel           : Dev1/0\n"
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
            )
        ),
        (
            # ctype_members
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
            # channel
            "1",
            # expected_python_members
            {
                "channel": "1",
                "vdc": 0.0,
                "idc": 0.0,
                "stimulus_frequency": 0.0,
                "ac_voltage": complex(),
                "ac_current": complex(),
                "z": complex(),
                "series_lcr": nidcpower.LCRMeasurement.LCR(
                    inductance=0.0,
                    capacitance=0.0,
                    resistance=0.0
                ),
                "parallel_lcr": nidcpower.LCRMeasurement.LCR(
                    inductance=0.0,
                    capacitance=0.0,
                    resistance=0.0
                ),
                "d": 0.0,
                "measurement_mode": nidcpower.InstrumentMode.LCR,
                "in_compliances": nidcpower.LCRMeasurement.InCompliances(dc=False, ac=False),
                "unbalanced": False,
                # Derived properties
                "z_magnitude_and_phase": (0.0, 0.0),
                "y": complex(cmath.nan, cmath.nan),
                "y_magnitude_and_phase": (cmath.nan, cmath.nan),
                "q": cmath.nan
            },
            # expected_python_str
            (
                "Channel           : 1\n"
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
            )
        ),
    ]
)
def test_lcr_measurement(ctype_members, channel, expected_python_members, expected_python_str):
    ctype_object = nidcpower.struct_NILCRMeasurement(**ctype_members)
    python_object = nidcpower.LCRMeasurement(ctype_object)
    python_object.channel = channel
    for member in expected_python_members:
        assert getattr(python_object, member) == pytest.approx(
            expected_python_members[member],
            nan_ok=True
        )
    assert str(python_object) == expected_python_str


@pytest.mark.parametrize(
    "python_init_params, expected_python_members, expected_ctype_members",
    [
        (
            # python_init_params
            {
                "frequency": 200.0,
                "impedance": complex(3.0, 4.0)
            },
            # expected_python_members
            {
                "frequency": 200.0,
                "reference_value_type": nidcpower.LCRReferenceValueType.IMPEDANCE,
                "reference_value": complex(3.0, 4.0)
            },
            # expected_ctype_members
            {
                "frequency": 200.0,
                "reference_value_type": nidcpower.LCRReferenceValueType.IMPEDANCE.value,
                "reference_value_a": 3.0,
                "reference_value_b": 4.0
            }
        ),
        (
            # python_init_params
            {
                "frequency": 300.0,
                "ideal_capacitance": 5.0
            },
            # expected_python_members
            {
                "frequency": 300.0,
                "reference_value_type": nidcpower.LCRReferenceValueType.IDEAL_CAPACITANCE,
                "reference_value": 5.0
            },
            # expected_ctype_members
            {
                "frequency": 300.0,
                "reference_value_type": nidcpower.LCRReferenceValueType.IDEAL_CAPACITANCE.value,
                "reference_value_a": 5.0,
                "reference_value_b": 0.0
            }
        ),
        (
            # python_init_params
            {
                "frequency": 400.0,
                "ideal_inductance": 6.0
            },
            # expected_python_members
            {
                "frequency": 400.0,
                "reference_value_type": nidcpower.LCRReferenceValueType.IDEAL_INDUCTANCE,
                "reference_value": 6.0
            },
            # expected_ctype_members
            {
                "frequency": 400.0,
                "reference_value_type": nidcpower.LCRReferenceValueType.IDEAL_INDUCTANCE.value,
                "reference_value_a": 6.0,
                "reference_value_b": 0.0
            }
        ),
        (
            # python_init_params
            {
                "frequency": 500.0,
                "ideal_resistance": 7.0
            },
            # expected_python_members
            {
                "frequency": 500.0,
                "reference_value_type": nidcpower.LCRReferenceValueType.IDEAL_RESISTANCE,
                "reference_value": 7.0
            },
            # expected_ctype_members
            {
                "frequency": 500.0,
                "reference_value_type": nidcpower.LCRReferenceValueType.IDEAL_RESISTANCE.value,
                "reference_value_a": 7.0,
                "reference_value_b": 0.0
            },
        ),
    ],
)
def test_lcr_load_compensation_spot(
    python_init_params,
    expected_python_members,
    expected_ctype_members
):
    python_object = nidcpower.LCRLoadCompensationSpot(**python_init_params)
    for member in expected_python_members:
        assert getattr(python_object, member) == pytest.approx(
            expected_python_members[member]
        )

    ctype_object = nidcpower.struct_NILCRLoadCompensationSpot(python_object)
    for member in expected_ctype_members:
        assert getattr(ctype_object, member) == pytest.approx(
            expected_ctype_members[member]
        )


def test_lcr_load_compensation_spot_repr_and_str():
    python_object = nidcpower.LCRLoadCompensationSpot(frequency=100.0, impedance=complex(1.0, 2.0))
    assert repr(python_object) == (
        "nidcpower.lcr_load_compensation_spot.LCRLoadCompensationSpot("
        "frequency=100.0, "
        "impedance=(1+2j))"
    )
    assert str(python_object) == (
        "Frequency           : 100\n"
        "Reference Value Type: IMPEDANCE\n"
        "Reference Value     : 1+2j\n"
    )
    recreated_object = eval(repr(python_object))
    assert str(recreated_object) == str(python_object)


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
