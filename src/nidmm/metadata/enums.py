enums = {

    'ApertureTimeUnits': {
        'values': [
            {'name': 'SECONDS', 'value': 0},
            {'name': 'POWER_LINE_CYCLES', 'value': 1},
            {'name': 'RAW_SAMPLES', 'value': 2},
        ],
    },

    'CableCompensationType': {
        'values': [
            {'name': 'CABLE_COMP_NONE', 'value': 0},
            {'name': 'CABLE_COMP_OPEN', 'value': 1},
            {'name': 'CABLE_COMP_SHORT', 'value': 2},
            {'name': 'CABLE_COMP_OPEN_AND_SHORT', 'value': 3},
        ],
    },

    'DCNoiseRejectionMode': {
        'documentation_lookup': 'DCNoiseRejection',
        'values': [
            {'name': 'DCNR_AUTO', 'value':-1},
            {'name': 'DCNR_NORMAL', 'value':  0},
            {'name': 'DCNR_SECOND_ORDERT', 'value':  1},
            {'name': 'DCNR_HIGH_ORDER', 'value':  2},
        ],
    },

    'OffsetCompensatedOhms': {
        'values': [
            {'name': 'OFF', 'value':  0},
            {'name': 'ON', 'value':  1},
        ],
    },

    'ADCCalibration': {
        'values': [
            {'name': 'AUTO', 'value':-1},
            {'name': 'OFF', 'value':  0},
            {'name': 'ON', 'value':  1},
        ],
    },

    'AutoZero': {
        'values': [
            {'name': 'AUTO', 'value':-1},
            {'name': 'OFF', 'value':  0},
            {'name': 'ON', 'value':  1},
            {'name': 'ONCE', 'value':  2},
        ],
    },

    'Function': {
        'values': [
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
    },

    'LCCalculationModel': {
        'values': [
            {'name': 'CALC_MODEL_AUTO', 'value':-1},
            {'name': 'CALC_MODEL_SERIES', 'value':  0},
            {'name': 'CALC_MODEL_PARALLEL', 'value':  1},
        ],
    },

    'OperationMode': {
        'values': [
            {'name': 'DMM_MODE', 'value': 0},
            {'name': 'WAVEFORM_MODE', 'value': 1},
        ],
    },

    'MeasurementDestinationSlope': {
        'values': [
            {'name': 'POSITIVE', 'value': 0},
            {'name': 'NEGATIVE', 'value': 1},
        ],
    },

    'SampleTrigSlope': {
        'values': [
            {'name': 'POSITIVE', 'value': 0},
            {'name': 'NEGATIVE', 'value': 1},
        ],
    },

    'TriggerSlope': {
        'values': [
            {'name': 'POSITIVE', 'value': 0},
            {'name': 'NEGATIVE', 'value': 1},
        ],
    },

    'TemperatureRTDType': {
        'documentation_lookup': 'RTDType',
        'values': [
            {'name': 'CustomRTD', 'value': 0},
            {'name': 'PT3750', 'value': 1},
            {'name': 'PT3851', 'value': 2},
            {'name': 'PT3911', 'value': 3},
            {'name': 'PT3916', 'value': 4},
            {'name': 'PT3920', 'value': 5},
            {'name': 'PT3928', 'value': 6},
        ],
    },

    'TemperatureThermistorType': {
        'documentation_lookup': 'ThermistorType',
        'values': [
            {'name': 'THERMISTOR_CUSTOM', 'value': 0},
            {'name': 'THERMISTOR_44004', 'value': 1},
            {'name': 'THERMISTOR_44006', 'value': 2},
            {'name': 'THERMISTOR_44007', 'value': 3},
        ],
    },

    'TemperatureThermocoupleReferenceJunctionType': {
        'documentation_lookup': 'ThermocoupleReferenceJunctionType',
        'values': [
            {'name': 'Fixed', 'value': 2},
        ],
    },

    'TemperatureThermocoupleType': {
        'documentation_lookup': 'ThermocoupleType',
        'values': [
            {'name': 'B', 'value':  1},
            {'name': 'E', 'value':  4},
            {'name': 'J', 'value':  6},
            {'name': 'K', 'value':  7},
            {'name': 'N', 'value':  8},
            {'name': 'R', 'value':  9},
            {'name': 'S', 'value': 10},
            {'name': 'T', 'value': 11},
        ],
    },

    'TemperatureTransducerType': {
        'documentation_lookup': 'TransducerType',
        'values': [
            {'name': 'THERMOCOUPLE', 'value': 1},
            {'name': 'THERMISTOR', 'value': 2},
            # TODO(marcoskirsch): annoying, C constants start with numbers. Replaced with spelled out values.
            {'name': 'TWO_WIRE_RTD', 'value': 3},
            {'name': 'FOUR_WIRE_RTD', 'value': 4},
        ],
    },

    'WaveformCouplingMode': {
        'documentation_lookup': 'WaveformCoupling',
        'values': [
            {'name': 'WAVEFORM_COUPLING_AC', 'value': 0},
            {'name': 'WAVEFORM_COUPLING_DC', 'value': 1},
        ],
    },

    'SampleTrigger': {
        'values': [
            {'name': 'NONE', 'value':-1},
            {'name': 'IMMEDIATE', 'value': 1},
            {'name': 'EXTERNAL', 'value': 2},
            {'name': 'SOFTWARE_TRIG', 'value': 3},
            {'name': 'INTERVAL', 'value': 10},
            {'name': 'AUX_TRIG1', 'value': 1001},
            {'name': 'LBR_TRIG1', 'value':1004}, # TODO: Internal Trigger Line of a PXI/SCXI Combination Chassis
            {'name': 'PXI_TRIG0', 'value': 111},
            {'name': 'PXI_TRIG1', 'value': 112},
            {'name': 'PXI_TRIG2', 'value': 113},
            {'name': 'PXI_TRIG3', 'value': 114},
            {'name': 'PXI_TRIG4', 'value': 115},
            {'name': 'PXI_TRIG5', 'value': 116},
            {'name': 'PXI_TRIG6', 'value': 117},
            {'name': 'PXI_TRIG7', 'value': 118},
            {'name': 'PXI_STAR', 'value': 131},
        ],
    },

    'TriggerSource': {
        'values': [
            {'name': 'NONE', 'value':-1},
            {'name': 'IMMEDIATE', 'value': 1},
            {'name': 'EXTERNAL', 'value': 2},
            {'name': 'SOFTWARE_TRIG', 'value': 3},
            {'name': 'PXI_TRIG0', 'value': 111},
            {'name': 'PXI_TRIG1', 'value': 112},
            {'name': 'PXI_TRIG2', 'value': 113},
            {'name': 'PXI_TRIG3', 'value': 114},
            {'name': 'PXI_TRIG4', 'value': 115},
            {'name': 'PXI_TRIG5', 'value': 116},
            {'name': 'PXI_TRIG6', 'value': 117},
            {'name': 'PXI_TRIG7', 'value': 118},
            {'name': 'PXI_STAR', 'value': 131},
            {'name': 'AUX_TRIG1', 'value': 1001},
            {'name': 'LBR_TRIG1', 'value':1004}, # TODO: Internal Trigger Line of a PXI/SCXI Combination Chassis
        ],
    },

    'MeasurementCompleteDest': {
        'values': [
            {'name': 'NONE', 'value':-1},
            {'name': 'EXTERNAL', 'value': 2},
            {'name': 'SOFTWARE_TRIG', 'value': 3},
            {'name': 'PXI_TRIG0', 'value': 111},
            {'name': 'PXI_TRIG1', 'value': 112},
            {'name': 'PXI_TRIG2', 'value': 113},
            {'name': 'PXI_TRIG3', 'value': 114},
            {'name': 'PXI_TRIG4', 'value': 115},
            {'name': 'PXI_TRIG5', 'value': 116},
            {'name': 'PXI_TRIG6', 'value': 117},
            {'name': 'PXI_TRIG7', 'value': 118},
            {'name': 'LBR_TRIG0', 'value':1003}, # TODO: Internal Trigger Line of a PXI/SCXI Combination Chassis
        ],
    },

    'AcquisitionStatus': {
        'documentation_lookup': None,
        'values': [
            {'name': 'RUNNING', 'value': 0},
            {'name': 'FINISHED_WITH_BACKLOG', 'value': 1},
            {'name': 'FINISHED_WITH_NO_BACKLOG', 'value': 2},
            {'name': 'PAUSED', 'value': 3},
            {'name': 'NO_ACQUISITION_IN_PROGRESS', 'value': 4},
        ],
    },

    # TODO(marcoskirsch): annoying, C constants start with numbers. Replaced with spelled out values.
    'CurrentSource': {
        'values': [
            {'name': 'ONE_MICRO_AMP', 'value': 0.000001},
            {'name': 'TEN_MICRO_AMP', 'value': 0.00001},
            {'name': 'HUNDRED_MICRO_AMP', 'value': 0.0001},
            {'name': 'ONE_MILLI_AMP', 'value': 0.001},
        ],
    },

}

