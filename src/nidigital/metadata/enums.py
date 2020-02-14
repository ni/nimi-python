# -*- coding: utf-8 -*-
# This file is generated from NI-Digital Pattern Driver API metadata version 19.5.0d7
enums = {
    'ApertureTimeUnits': {
        'values': [
            {
                'name': 'NIDIGITAL_VAL_SECONDS',
                'value': 2100
            }
        ]
    },
    'BitOrder': {
        'values': [
            {
                'name': 'NIDIGITAL_VAL_MSB_FIRST',
                'value': 2500
            },
            {
                'name': 'NIDIGITAL_VAL_LSB_FIRST',
                'value': 2501
            }
        ]
    },
    'ConditionalJumpTrigger': {
        'values': [
            {
                'name': 'NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER0',
                'python_name': 'CONDITIONAL_JUMP_TRIGGER0',
                'value': 'conditionalJumpTrigger0'
            },
            {
                'name': 'NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER1',
                'python_name': 'CONDITIONAL_JUMP_TRIGGER1',
                'value': 'conditionalJumpTrigger1'
            },
            {
                'name': 'NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER2',
                'python_name': 'CONDITIONAL_JUMP_TRIGGER2',
                'value': 'conditionalJumpTrigger2'
            },
            {
                'name': 'NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER3',
                'python_name': 'CONDITIONAL_JUMP_TRIGGER3',
                'value': 'conditionalJumpTrigger3'
            }
        ]
    },
    'DigitalEdge': {
        'values': [
            {
                'name': 'NIDIGITAL_VAL_RISING_EDGE',
                'value': 1800
            },
            {
                'name': 'NIDIGITAL_VAL_FALLING_EDGE',
                'value': 1801
            }
        ]
    },
    'DigitalState': {
        'values': [
            {
                'name': 'NIDIGITAL_VAL_0',
                'python_name': 'ZERO',
                'value': 0
            },
            {
                'name': 'NIDIGITAL_VAL_1',
                'python_name': 'ONE',
                'value': 1
            },
            {
                'name': 'NIDIGITAL_VAL_L',
                'value': 3
            },
            {
                'name': 'NIDIGITAL_VAL_H',
                'value': 4
            },
            {
                'name': 'NIDIGITAL_VAL_X',
                'value': 5
            },
            {
                'name': 'NIDIGITAL_VAL_M',
                'value': 6
            },
            {
                'name': 'NIDIGITAL_VAL_V',
                'value': 7
            },
            {
                'name': 'NIDIGITAL_VAL_D',
                'value': 8
            },
            {
                'name': 'NIDIGITAL_VAL_E',
                'value': 9
            },
            {
                'name': 'NIDIGITAL_VAL_NOT_A_PIN_STATE',
                'value': 254
            },
            {
                'name': 'NIDIGITAL_VAL_PIN_STATE_NOT_ACQUIRED',
                'value': 255
            }
        ]
    },
    'DriveEdgeSetFormat': {
        'values': [
            {
                'name': 'NIDIGITAL_VAL_NR',
                'value': 1500
            },
            {
                'name': 'NIDIGITAL_VAL_RL',
                'value': 1501
            },
            {
                'name': 'NIDIGITAL_VAL_RH',
                'value': 1502
            },
            {
                'name': 'NIDIGITAL_VAL_SBC',
                'value': 1503
            }
        ]
    },
    'HramCyclesToAcquire': {
        'values': [
            {
                'name': 'NIDIGITAL_VAL_FAILED_CYCLES',
                'value': 2303
            },
            {
                'name': 'NIDIGITAL_VAL_ALL_CYCLES',
                'value': 2304
            }
        ]
    },
    'HramTriggerType': {
        'values': [
            {
                'name': 'NIDIGITAL_VAL_FIRST_FAILURE',
                'value': 2200
            },
            {
                'name': 'NIDIGITAL_VAL_CYCLE_NUMBER',
                'value': 2201
            },
            {
                'name': 'NIDIGITAL_VAL_PATTERN_LABEL',
                'value': 2202
            }
        ]
    },
    'MeasurementMode': {
        'values': [
            {
                'name': 'NIDIGITAL_VAL_BANKED',
                'value': 3700
            },
            {
                'name': 'NIDIGITAL_VAL_PARALLEL',
                'value': 3701
            }
        ]
    },
    'PPMUCurrentLimitBehavior': {
        'values': [
            {
                'name': 'NIDIGITAL_VAL_CURRENT_REGULATE',
                'value': 3100
            }
        ]
    },
    'PPMUMeasurementType': {
        'values': [
            {
                'name': 'NIDIGITAL_VAL_MEASURE_CURRENT',
                'value': 2400
            },
            {
                'name': 'NIDIGITAL_VAL_MEASURE_VOLTAGE',
                'value': 2401
            }
        ]
    },
    'PPMUOutputFunction': {
        'values': [
            {
                'name': 'NIDIGITAL_VAL_DC_VOLTAGE',
                'value': 1300
            },
            {
                'name': 'NIDIGITAL_VAL_DC_CURRENT',
                'value': 1301
            }
        ]
    },
    'PatternOpcodeEvent': {
        'values': [
            {
                'name': 'NIDIGITAL_VAL_PATTERN_OPCODE_EVENT0',
                'value': 'patternOpcodeEvent0'
            },
            {
                'name': 'NIDIGITAL_VAL_PATTERN_OPCODE_EVENT1',
                'value': 'patternOpcodeEvent1'
            },
            {
                'name': 'NIDIGITAL_VAL_PATTERN_OPCODE_EVENT2',
                'value': 'patternOpcodeEvent2'
            },
            {
                'name': 'NIDIGITAL_VAL_PATTERN_OPCODE_EVENT3',
                'value': 'patternOpcodeEvent3'
            }
        ]
    },
    'SelectedFunction': {
        'values': [
            {
                'name': 'NIDIGITAL_VAL_DIGITAL',
                'value': 1100
            },
            {
                'name': 'NIDIGITAL_VAL_PPMU',
                'value': 1101
            },
            {
                'name': 'NIDIGITAL_VAL_OFF',
                'value': 1102
            },
            {
                'name': 'NIDIGITAL_VAL_DISCONNECT',
                'value': 1103
            }
        ]
    },
    'SequencerFlag': {
        'values': [
            {
                'name': 'NIDIGITAL_VAL_SEQUENCER_FLAG0',
                'value': 'seqflag0'
            },
            {
                'name': 'NIDIGITAL_VAL_SEQUENCER_FLAG1',
                'value': 'seqflag1'
            },
            {
                'name': 'NIDIGITAL_VAL_SEQUENCER_FLAG2',
                'value': 'seqflag2'
            },
            {
                'name': 'NIDIGITAL_VAL_SEQUENCER_FLAG3',
                'value': 'seqflag3'
            }
        ]
    },
    'SequencerRegister': {
        'values': [
            {
                'name': 'NIDIGITAL_VAL_SEQUENCER_REGISTER0',
                'value': 'reg0'
            },
            {
                'name': 'NIDIGITAL_VAL_SEQUENCER_REGISTER1',
                'value': 'reg1'
            },
            {
                'name': 'NIDIGITAL_VAL_SEQUENCER_REGISTER2',
                'value': 'reg2'
            },
            {
                'name': 'NIDIGITAL_VAL_SEQUENCER_REGISTER3',
                'value': 'reg3'
            },
            {
                'name': 'NIDIGITAL_VAL_SEQUENCER_REGISTER4',
                'value': 'reg4'
            },
            {
                'name': 'NIDIGITAL_VAL_SEQUENCER_REGISTER5',
                'value': 'reg5'
            },
            {
                'name': 'NIDIGITAL_VAL_SEQUENCER_REGISTER6',
                'value': 'reg6'
            },
            {
                'name': 'NIDIGITAL_VAL_SEQUENCER_REGISTER7',
                'value': 'reg7'
            },
            {
                'name': 'NIDIGITAL_VAL_SEQUENCER_REGISTER8',
                'value': 'reg8'
            },
            {
                'name': 'NIDIGITAL_VAL_SEQUENCER_REGISTER9',
                'value': 'reg9'
            },
            {
                'name': 'NIDIGITAL_VAL_SEQUENCER_REGISTER10',
                'value': 'reg10'
            },
            {
                'name': 'NIDIGITAL_VAL_SEQUENCER_REGISTER11',
                'value': 'reg11'
            },
            {
                'name': 'NIDIGITAL_VAL_SEQUENCER_REGISTER12',
                'value': 'reg12'
            },
            {
                'name': 'NIDIGITAL_VAL_SEQUENCER_REGISTER13',
                'value': 'reg13'
            },
            {
                'name': 'NIDIGITAL_VAL_SEQUENCER_REGISTER14',
                'value': 'reg14'
            },
            {
                'name': 'NIDIGITAL_VAL_SEQUENCER_REGISTER15',
                'value': 'reg15'
            }
        ]
    },
    'SessionState': {
        'values': [
            {
                'name': 'NIDIGITAL_VAL_IDLE',
                'value': 1
            },
            {
                'name': 'NIDIGITAL_VAL_VERIFIED',
                'value': 2
            },
            {
                'name': 'NIDIGITAL_VAL_COMMITTED',
                'value': 4
            },
            {
                'name': 'NIDIGITAL_VAL_RUNNING',
                'value': 8
            }
        ]
    },
    'Signal': {
        'values': [
            {
                'name': 'NIDIGITAL_VAL_START_TRIGGER',
                'value': 2000
            },
            {
                'name': 'NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER',
                'value': 2001
            },
            {
                'name': 'NIDIGITAL_VAL_PATTERN_OPCODE_EVENT',
                'value': 2002
            },
            {
                'name': 'NIDIGITAL_VAL_REF_CLOCK',
                'value': 2003
            }
        ]
    },
    'SiteResult': {
        'values': [
            {
                'name': 'NIDIGITAL_VAL_PASS_FAIL',
                'value': 3300
            },
            {
                'name': 'NIDIGITAL_VAL_CAPTURE_WAVEFORM',
                'value': 3301
            }
        ]
    },
    'SourceMemoryDataMapping': {
        'values': [
            {
                'name': 'NIDIGITAL_VAL_BROADCAST',
                'value': 2600
            },
            {
                'name': 'NIDIGITAL_VAL_SITE_UNIQUE',
                'value': 2601
            }
        ]
    },
    'TDREndpointTermination': {
        'values': [
            {
                'name': 'NIDIGITAL_VAL_TDR_TO_OPEN',
                'value': 3600
            },
            {
                'name': 'NIDIGITAL_VAL_TDR_TO_SHORT_TO_GROUND',
                'value': 3601
            }
        ]
    },
    'Terminal': {
        'values': [
            {
                'name': 'NIDIGITAL_VAL_DO_NOT_EXPORT_STR',
                'value': ''
            },
            {
                'name': 'NIDIGITAL_VAL_PXI_TRIG0_STR',
                'value': 'PXI_Trig0'
            },
            {
                'name': 'NIDIGITAL_VAL_PXI_TRIG1_STR',
                'value': 'PXI_Trig1'
            },
            {
                'name': 'NIDIGITAL_VAL_PXI_TRIG2_STR',
                'value': 'PXI_Trig2'
            },
            {
                'name': 'NIDIGITAL_VAL_PXI_TRIG3_STR',
                'value': 'PXI_Trig3'
            },
            {
                'name': 'NIDIGITAL_VAL_PXI_TRIG4_STR',
                'value': 'PXI_Trig4'
            },
            {
                'name': 'NIDIGITAL_VAL_PXI_TRIG5_STR',
                'value': 'PXI_Trig5'
            },
            {
                'name': 'NIDIGITAL_VAL_PXI_TRIG6_STR',
                'value': 'PXI_Trig6'
            },
            {
                'name': 'NIDIGITAL_VAL_PXI_TRIG7_STR',
                'value': 'PXI_Trig7'
            }
        ]
    },
    'TerminationMode': {
        'values': [
            {
                'name': 'NIDIGITAL_VAL_ACTIVE_LOAD',
                'value': 1200
            },
            {
                'name': 'NIDIGITAL_VAL_VTERM',
                'value': 1201
            },
            {
                'name': 'NIDIGITAL_VAL_HIGH_Z',
                'value': 1202
            }
        ]
    },
    'TimeSetEdge': {
        'values': [
            {
                'name': 'NIDIGITAL_VAL_DRIVE_ON',
                'value': 2800
            },
            {
                'name': 'NIDIGITAL_VAL_DRIVE_DATA',
                'value': 2801
            },
            {
                'name': 'NIDIGITAL_VAL_DRIVE_RETURN',
                'value': 2802
            },
            {
                'name': 'NIDIGITAL_VAL_DRIVE_OFF',
                'value': 2803
            },
            {
                'name': 'NIDIGITAL_VAL_COMPARE_STROBE',
                'value': 2804
            },
            {
                'name': 'NIDIGITAL_VAL_DRIVE_DATA2',
                'value': 2805
            },
            {
                'name': 'NIDIGITAL_VAL_DRIVE_RETURN2',
                'value': 2806
            },
            {
                'name': 'NIDIGITAL_VAL_COMPARE_STROBE2',
                'value': 2807
            }
        ]
    },
    'TriggerType': {
        'values': [
            {
                'name': 'NIDIGITAL_VAL_NONE',
                'value': 1700
            },
            {
                'name': 'NIDIGITAL_VAL_DIGITAL_EDGE',
                'value': 1701
            },
            {
                'name': 'NIDIGITAL_VAL_SOFTWARE',
                'value': 1702
            }
        ]
    }
}
