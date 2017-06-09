enums = {

    'ApertureTimeUnits': [
        {'name': 'SECONDS', 'value': 0},
        {'name': 'POWER_LINE_CYCLES', 'value': 1},
        {'name': 'RAW_SAMPLES', 'value': 2},
    ],

    'CableCompensationType': [
        {'name': 'CABLE_COMP_NONE', 'value': 0},
        {'name': 'CABLE_COMP_OPEN', 'value': 1},
        {'name': 'CABLE_COMP_SHORT', 'value': 2},
        {'name': 'CABLE_COMP_OPEN_AND_SHORT', 'value': 3},
    ],

    'DCNoiseRejectionMode': [
        {'name': 'DCNR_AUTO', 'value':-1},
        {'name': 'DCNR_NORMAL', 'value':  0},
        {'name': 'DCNR_SECOND_ORDERT', 'value':  1},
        {'name': 'DCNR_HIGH_ORDER', 'value':  2},
    ],

    'EnabledSetting': [
        {'name': 'AUTO', 'value':-1},
        {'name': 'OFF', 'value':  0},
        {'name': 'ON', 'value':  1},
        {'name': 'ONCE', 'value':  2},
    ],

    'Function': [
        {'name': 'DC_VOLTS', 'value':    1},
        {'name': 'AC_VOLTS', 'value':    2},
        {'name': 'DC_CURRENT', 'value':    3},
        {'name': 'AC_CURRENT', 'value':    4},
        # Had to put RES_ in front, rather than in back, so name doesn't start with number.
        {'name': 'RES_2_WIRE', 'value':    5},
        # Had to put RES_ in front, rather than in back, so name doesn't start with number.
        {'name': 'RES_4_WIRE', 'value':  101},
        {'name': 'FREQ', 'value':  104},
        {'name': 'PERIOD', 'value':  105},
        {'name': 'TEMPERATURE', 'value':  108},
        {'name': 'AC_VOLTS_DC_COUPLED', 'value': 1001},
        {'name': 'DIODE', 'value': 1002},
        {'name': 'WAVEFORM_VOLTAGE', 'value': 1003},
        {'name': 'WAVEFORM_CURRENT', 'value': 1004},
        {'name': 'CAPACITANCE', 'value': 1005},
        {'name': 'INDUCTANCE', 'value': 1006},
    ],

    'LCCalculationModel': [
        {'name': 'CALC_MODEL_AUTO', 'value':-1},
        {'name': 'CALC_MODEL_SERIES', 'value':  0},
        {'name': 'CALC_MODEL_PARALLEL', 'value':  1},
    ],

    'OperationMode': [
        {'name': 'DMM_MODE', 'value': 0},
        {'name': 'WAVEFORM_MODE', 'value': 1},
    ],

    'Slope': [
        {'name': 'POSITIVE', 'value': 0},
        {'name': 'NEGATIVE', 'value': 1},
    ],

    'TemperatureRTDType': [
        {'name': 'CustomRTD', 'value': 0},
        {'name': 'PT3750', 'value': 1},
        {'name': 'PT3851', 'value': 2},
        {'name': 'PT3911', 'value': 3},
        {'name': 'PT3916', 'value': 4},
        {'name': 'PT3920', 'value': 5},
        {'name': 'PT3928', 'value': 6},
    ],

    'TemperatureThermistorType': [
        {'name': 'THERMISTOR_CUSTOM', 'value': 0},
        {'name': 'THERMISTOR_44004', 'value': 1},
        {'name': 'THERMISTOR_44006', 'value': 2},
        {'name': 'THERMISTOR_44007', 'value': 3},
    ],

    'TemperatureThermocoupleReferenceJunctionType': [
        {'name': 'Fixed', 'value': 2},
    ],

    'TemperatureThermocoupleType': [
        {'name': 'B', 'value':  1},
        {'name': 'E', 'value':  4},
        {'name': 'J', 'value':  6},
        {'name': 'K', 'value':  7},
        {'name': 'N', 'value':  8},
        {'name': 'R', 'value':  9},
        {'name': 'S', 'value': 10},
        {'name': 'T', 'value': 11},
    ],

    'TemperatureTransducerType': [
        {'name': 'THERMOCOUPLE', 'value':  1},
        {'name': 'THERMISTOR', 'value':  2},
        # Had to put RTD in front, rather than in back, so name doesn't start with number.
        {'name': 'RTD_2_WIRE', 'value':  3},
        # Had to put RTD in front, rather than in back, so name doesn't start with number.
        {'name': 'RTD_4_WIRE', 'value':  4},
    ],

    'WaveformCouplingMode': [
        {'name': 'WAVEFORM_COUPLING_AC', 'value':  0},
        {'name': 'WAVEFORM_COUPLING_DC', 'value':  1},
    ],

}

