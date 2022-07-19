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
                "dc_in_compliance": True,
                "ac_in_compliance": True,
                "unbalanced": True,
                # Derived properties
                "z_magnitude_and_phase": (100.49876, 5.7105931375),
                "y": complex(0.0099009901, -0.00099009901),
                "y_magnitude_and_phase": (0.0099503719, -5.7105931375),
                "q": 0.1
            },
            # expected_python_str
            (
                "Channel             : Dev1/0\n"
                "DC voltage          : 0.1\n"
                "DC current          : 0.001\n"
                "Stimulus frequency  : 10,000\n"
                "AC voltage          : 1+0.1j\n"
                "AC current          : 0.01+0.001j\n"
                "Impedance           : 100+10j\n"
                "Impedance magnitude : 100.499\n"
                "Impedance phase     : 5.71059\n"
                "Admittance          : 0.00990099-0.000990099j\n"
                "Admittance magnitude: 0.00995037\n"
                "Admittance phase    : -5.71059\n"
                "Series inductance   : 10\n"
                "Series capacitance  : 20\n"
                "Series resistance   : 90\n"
                "Parallel inductance : 30\n"
                "Parallel capacitance: 40\n"
                "Parallel resistance : 110\n"
                "Dissipation factor  : 10\n"
                "Quality factor      : 0.1\n"
                "Measurement mode    : SMU_PS\n"
                "DC in compliance    : True\n"
                "AC in compliance    : True\n"
                "Unbalanced          : True\n"
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
                "dc_in_compliance": False,
                "ac_in_compliance": False,
                "unbalanced": False,
                # Derived properties
                "z_magnitude_and_phase": (0.0, 0.0),
                "y": complex(cmath.nan, cmath.nan),
                "y_magnitude_and_phase": (cmath.nan, cmath.nan),
                "q": cmath.nan
            },
            # expected_python_str
            (
                "Channel             : 1\n"
                "DC voltage          : 0\n"
                "DC current          : 0\n"
                "Stimulus frequency  : 0\n"
                "AC voltage          : 0+0j\n"
                "AC current          : 0+0j\n"
                "Impedance           : 0+0j\n"
                "Impedance magnitude : 0\n"
                "Impedance phase     : 0\n"
                "Admittance          : nan+nanj\n"
                "Admittance magnitude: nan\n"
                "Admittance phase    : nan\n"
                "Series inductance   : 0\n"
                "Series capacitance  : 0\n"
                "Series resistance   : 0\n"
                "Parallel inductance : 0\n"
                "Parallel capacitance: 0\n"
                "Parallel resistance : 0\n"
                "Dissipation factor  : 0\n"
                "Quality factor      : nan\n"
                "Measurement mode    : LCR\n"
                "DC in compliance    : False\n"
                "AC in compliance    : False\n"
                "Unbalanced          : False\n"
            )
        ),
    ]
)
def test_lcr_measurement(ctype_members, channel, expected_python_members, expected_python_str):
    ctype_instance = nidcpower.struct_NILCRMeasurement(**ctype_members)
    python_instance = nidcpower.LCRMeasurement(ctype_instance)
    python_instance.channel = channel
    for member in expected_python_members:
        assert getattr(python_instance, member) == pytest.approx(
            expected_python_members[member],
            nan_ok=True
        )
    assert str(python_instance) == expected_python_str


@pytest.mark.parametrize(
    "python_init_params, expected_repr, expected_str, expected_ctype_members",
    [
        (
            # python_init_params
            {
                "frequency": 200.0,
                "reference_value_type": nidcpower.LCRReferenceValueType.IMPEDANCE,
                "reference_value": complex(3.0, 4.0)
            },
            # expected_repr
            (
                "nidcpower.lcr_load_compensation_spot.LCRLoadCompensationSpot("
                "frequency=200.0, "
                "reference_value_type=nidcpower.enums.LCRReferenceValueType.IMPEDANCE, "
                "reference_value=(3+4j))"
            ),
            # expected_str
            (
                "Frequency        : 200\n"
                "Impedance        : 3+4j ohms\n"
            ),
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
                "reference_value_type": nidcpower.LCRReferenceValueType.IDEAL_CAPACITANCE,
                "reference_value": 5.0
            },
            # expected_repr
            (
                "nidcpower.lcr_load_compensation_spot.LCRLoadCompensationSpot("
                "frequency=300.0, "
                "reference_value_type=nidcpower.enums.LCRReferenceValueType.IDEAL_CAPACITANCE, "
                "reference_value=5.0)"
            ),
            # expected_str
            (
                "Frequency        : 300\n"
                "Ideal Capacitance: 5 farads\n"
            ),
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
                "reference_value_type": nidcpower.LCRReferenceValueType.IDEAL_INDUCTANCE,
                "reference_value": 6.0
            },
            # expected_repr
            (
                "nidcpower.lcr_load_compensation_spot.LCRLoadCompensationSpot("
                "frequency=400.0, "
                "reference_value_type=nidcpower.enums.LCRReferenceValueType.IDEAL_INDUCTANCE, "
                "reference_value=6.0)"
            ),
            # expected_str
            (
                "Frequency        : 400\n"
                "Ideal Inductance : 6 henrys\n"
            ),
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
                "reference_value_type": nidcpower.LCRReferenceValueType.IDEAL_RESISTANCE,
                "reference_value": 7.0
            },
            # expected_repr
            (
                "nidcpower.lcr_load_compensation_spot.LCRLoadCompensationSpot("
                "frequency=500.0, "
                "reference_value_type=nidcpower.enums.LCRReferenceValueType.IDEAL_RESISTANCE, "
                "reference_value=7.0)"
            ),
            # expected_str
            (
                "Frequency        : 500\n"
                "Ideal Resistance : 7 ohms\n"
            ),
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
    expected_repr,
    expected_str,
    expected_ctype_members
):
    python_instance = nidcpower.LCRLoadCompensationSpot(**python_init_params)
    for member in python_init_params:
        assert getattr(python_instance, member) == pytest.approx(python_init_params[member])

    assert repr(python_instance) == expected_repr
    assert str(python_instance) == expected_str
    recreated_instance = eval(repr(python_instance))
    assert str(recreated_instance) == str(python_instance)

    ctype_instance = nidcpower.struct_NILCRLoadCompensationSpot(python_instance)
    for member in expected_ctype_members:
        assert getattr(ctype_instance, member) == pytest.approx(expected_ctype_members[member])
