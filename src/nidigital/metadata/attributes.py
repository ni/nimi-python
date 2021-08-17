# -*- coding: utf-8 -*-
# This file is generated from NI-Digital Pattern Driver API metadata version 21.3.0d40
attributes = {
    1050002: {
        'access': 'read-write',
        'documentation': {
            'description': 'Checks the range and validates parameter and attribute values you pass to NI-Digital Pattern Driver functions. Ranges are always checked, regardless of the attribute setting.\n'
        },
        'name': 'RANGE_CHECK',
        'type': 'ViBoolean'
    },
    1050003: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies whether the NI-Digital Pattern Driver queries the digital pattern instrument status after each operation. The instrument status is always queried, regardless of the attribute setting.\n'
        },
        'name': 'QUERY_INSTRUMENT_STATUS',
        'type': 'ViBoolean'
    },
    1050004: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies whether to cache the value of attributes. When caching is enabled, the instrument driver keeps track of the current instrument settings and avoids sending redundant commands to the instrument. This significantly increases execution speed. Caching is always enabled in the driver, regardless of the value of this attribute.'
        },
        'name': 'CACHE',
        'type': 'ViBoolean'
    },
    1050005: {
        'access': 'read-write',
        'documentation': {
            'description': 'Simulates I/O operations. After you open a session, you cannot change the simulation state. Use the niDigital_InitWithOptions function to enable simulation.\n'
        },
        'name': 'SIMULATE',
        'type': 'ViBoolean'
    },
    1050006: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies whether the IVI engine keeps a list of the value coercions it makes for integer and real type attributes. Enabling record value coercions is not supported.\n'
        },
        'name': 'RECORD_COERCIONS',
        'type': 'ViBoolean'
    },
    1050007: {
        'access': 'read only',
        'documentation': {
            'description': 'This attribute returns initial values for NI-Digital Pattern Driver attributes as a string.\n'
        },
        'name': 'DRIVER_SETUP',
        'type': 'ViString'
    },
    1050021: {
        'access': 'read-write',
        'documentation': {
            'description': 'This attribute is not supported.\n'
        },
        'name': 'INTERCHANGE_CHECK',
        'type': 'ViBoolean'
    },
    1050203: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns the number of channels that the specific digital pattern instrument driver supports.\n'
        },
        'name': 'CHANNEL_COUNT',
        'type': 'ViInt32'
    },
    1050302: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns a string that contains the prefix for the NI-Digital Pattern driver.\n'
        },
        'name': 'SPECIFIC_DRIVER_PREFIX',
        'type': 'ViString'
    },
    1050304: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns a string that contains the resource descriptor that the NI-Digital Pattern Driver uses to identify the digital pattern instrument.\n'
        },
        'name': 'IO_RESOURCE_DESCRIPTOR',
        'type': 'ViString'
    },
    1050305: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns a string containing the logical name that you specified when opening the current IVI session. This attribute is not supported.\n'
        },
        'name': 'LOGICAL_NAME',
        'type': 'ViString'
    },
    1050327: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns a comma delimited string that contains the supported digital pattern instrument models for the specific driver.\n'
        },
        'name': 'SUPPORTED_INSTRUMENT_MODELS',
        'type': 'ViString'
    },
    1050401: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns a string that contains a comma-separated list of class-extension groups that the driver implements.\n'
        },
        'name': 'GROUP_CAPABILITIES',
        'type': 'ViString'
    },
    1050510: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns a string that contains the firmware revision information for the digital pattern instrument.\n'
        },
        'name': 'INSTRUMENT_FIRMWARE_REVISION',
        'supported_rep_caps': [
            'instruments'
        ],
        'type': 'ViString'
    },
    1050511: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns a string ("National Instruments") that contains the name of the manufacturer of the digital pattern instrument.\n'
        },
        'name': 'INSTRUMENT_MANUFACTURER',
        'type': 'ViString'
    },
    1050512: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns a string that contains the model number or name of the digital pattern instrument.\n'
        },
        'name': 'INSTRUMENT_MODEL',
        'type': 'ViString'
    },
    1050513: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns a string ("National Instruments") that contains the name of the vendor that supplies the NI-Digital Pattern Driver.\n'
        },
        'name': 'SPECIFIC_DRIVER_VENDOR',
        'type': 'ViString'
    },
    1050514: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns a string that contains a brief description of the NI-Digital Pattern driver.\n'
        },
        'name': 'SPECIFIC_DRIVER_DESCRIPTION',
        'type': 'ViString'
    },
    1050515: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns the major version number of the class specification with which NI-Digital is compliant. This attribute is not supported.\n'
        },
        'name': 'SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION',
        'type': 'ViInt32'
    },
    1050516: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns the minor version number of the class specification with which NI-Digital is compliant. This attribute is not supported.\n'
        },
        'name': 'SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION',
        'type': 'ViInt32'
    },
    1050551: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns a string that contains additional version information about the NI-Digital Pattern Driver. For example, the driver can return Driver: NI-Digital 16.0 as the value of this attribute.\n'
        },
        'name': 'SPECIFIC_DRIVER_REVISION',
        'type': 'ViString'
    },
    1150001: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns the serial number of the device.\n'
        },
        'name': 'SERIAL_NUMBER',
        'supported_rep_caps': [
            'instruments'
        ],
        'type': 'ViString'
    },
    1150004: {
        'access': 'read-write',
        'documentation': {
            'caution': 'In the Disconnect state, some I/O protection and sensing circuitry remains exposed. Do not subject the instrument to voltage beyond its operating range.\n',
            'description': 'Specifies whether digital pattern instrument channels are controlled by the pattern sequencer or PPMU, disconnected, or off.\n',
            'note': 'You can make PPMU voltage measurements using the niDigital_PPMU_Measure function from within any NIDIGITAL_ATTR_SELECTED_FUNCTION.\n',
            'table_body': [
                [
                    'NIDIGITAL_VAL_DIGITAL',
                    'The pin is connected to the driver, comparator, and active load functions. The PPMU is not sourcing, but can make voltage measurements. The state of the digital pin driver when you change the NIDIGITAL_ATTR_SELECTED_FUNCTION to Digital is determined by the most recent call to the niDigital_WriteStatic function or the last vector of the most recently executed pattern burst, whichever happened last. Use the niDigital_WriteStatic function to control the state of the digital pin driver through software. Use the niDigital_FancyBurstPattern function to control the state of the digital pin driver through a pattern. Set the **selectDigitalFunction** parameter of the niDigital_FancyBurstPattern function to VI_TRUE to automatically switch the NIDIGITAL_ATTR_SELECTED_FUNCTION of the pins in the pattern burst to NIDIGITAL_VAL_DIGITAL.'
                ],
                [
                    'NIDIGITAL_VAL_PPMU',
                    'The pin is connected to the PPMU. The driver, comparator, and active load are off while this function is selected. Call the niDigital_PPMU_Source function to source a voltage or current. The niDigital_PPMU_Source function automatically switches the NIDIGITAL_ATTR_SELECTED_FUNCTION to the PPMU state and starts sourcing from the PPMU. Changing the NIDIGITAL_ATTR_SELECTED_FUNCTION to NIDIGITAL_VAL_DISCONNECT, NIDIGITAL_VAL_OFF, or NIDIGITAL_VAL_DIGITAL causes the PPMU to stop sourcing. If you set the NIDIGITAL_ATTR_SELECTED_FUNCTION attribute to PPMU, the PPMU is initially not sourcing.'
                ],
                [
                    'NIDIGITAL_VAL_OFF',
                    'The pin is electrically connected, and the PPMU and digital pin driver are off while this function is selected.'
                ],
                [
                    'NIDIGITAL_VAL_DISCONNECT',
                    'The pin is electrically disconnected from instrument functions. Selecting this function causes the PPMU to stop sourcing prior to disconnecting the pin.'
                ]
            ],
            'table_header': [
                'Defined Values:'
            ]
        },
        'enum': 'SelectedFunction',
        'name': 'SELECTED_FUNCTION',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViInt32'
    },
    1150006: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the behavior of the pin during non-drive cycles.\n',
            'table_body': [
                [
                    'NIDIGITAL_VAL_ACTIVE_LOAD',
                    'Specifies that, for non-drive pin states (L, H, X, V, M, E), the active load is connected and the instrument sources or sinks a defined amount of current to load the DUT. The amount of current sourced by the instrument and therefore sunk by the DUT is specified by IOL. The amount of current sunk by the instrument and therefore sourced by the DUT is specified by IOH. The voltage at which the instrument changes between sourcing and sinking is specified by VCOM.'
                ],
                [
                    'NIDIGITAL_VAL_VTERM',
                    'Specifies that, for non-drive pin states (L, H, X, V, M, E), the pin driver terminates the pin to the configured VTERM voltage through a 50 Ω impedance. VTERM is adjustable to allow for the pin to terminate at a set level. This is useful for instruments that might operate incorrectly if an instrument pin is unterminated and is allowed to float to any voltage level within the instrument voltage range. To address this issue, enable VTERM by configuring the VTERM pin level to the desired voltage and selecting the VTERM termination mode. Setting VTERM to 0 V and selecting the VTERM termination mode has the effect of connecting a 50 Ω termination to ground, which provides an effective 50 Ω impedance for the pin. This can be useful for improving signal integrity of certain DUTs by reducing reflections while the DUT drives the pin.'
                ],
                [
                    'NIDIGITAL_VAL_HIGH_Z',
                    'Specifies that, for non-drive pin states (L, H, X, V, M, E), the pin driver is put in a high-impedance state and the active load is disabled.'
                ]
            ],
            'table_header': [
                'Defined Values:'
            ]
        },
        'enum': 'TerminationMode',
        'name': 'TERMINATION_MODE',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViInt32'
    },
    1150007: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the voltage that the digital pattern instrument will apply to the input of the DUT when the test instrument drives a logic low (0).\n'
        },
        'name': 'VIL',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViReal64'
    },
    1150008: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the voltage that the digital pattern instrument will apply to the input of the DUT when the test instrument drives a logic high (1).\n'
        },
        'name': 'VIH',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViReal64'
    },
    1150009: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the output voltage from the DUT below which the comparator on the digital pattern test instrument interprets a logic low (L).\n'
        },
        'name': 'VOL',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViReal64'
    },
    1150010: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the output voltage from the DUT above which the comparator on the digital pattern test instrument interprets a logic high (H).\n'
        },
        'name': 'VOH',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViReal64'
    },
    1150011: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the termination voltage the digital pattern instrument applies during non-drive cycles when the termination mode is set to V :sub:`term`. The instrument applies the termination voltage through a 50 Ω parallel termination resistance.\n'
        },
        'name': 'VTERM',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViReal64'
    },
    1150012: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the current that the DUT sinks from the active load while outputting a voltage below VCOM.\n'
        },
        'name': 'ACTIVE_LOAD_IOL',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViReal64'
    },
    1150013: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the current that the DUT sources to the active load while outputting a voltage above VCOM.\n'
        },
        'name': 'ACTIVE_LOAD_IOH',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViReal64'
    },
    1150014: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the voltage level at which the active load circuit switches between sourcing current and sinking current.\n'
        },
        'name': 'ACTIVE_LOAD_VCOM',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViReal64'
    },
    1150015: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies whether the PPMU forces voltage or current to the DUT.\n',
            'table_body': [
                [
                    'NIDIGITAL_VAL_DC_VOLTAGE',
                    'Specifies the output function to DC Voltage.'
                ],
                [
                    'NIDIGITAL_VAL_DC_CURRENT',
                    'Specifies the output function to DC Current.'
                ]
            ],
            'table_header': [
                'Defined Values:'
            ]
        },
        'enum': 'PPMUOutputFunction',
        'name': 'PPMU_OUTPUT_FUNCTION',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViInt32'
    },
    1150016: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the voltage level, in volts, that the PPMU forces to the DUT. This attribute is applicable only when you set the NIDIGITAL_ATTR_PPMU_OUTPUT_FUNCTION attribute to DC Voltage.\n'
        },
        'name': 'PPMU_VOLTAGE_LEVEL',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViReal64'
    },
    1150017: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the valid range, in amps, to which the current limit can be set while the PPMU forces voltage to the DUT. This attribute is applicable only when you set the NIDIGITAL_ATTR_PPMU_OUTPUT_FUNCTION attribute to DC Voltage.\n'
        },
        'name': 'PPMU_CURRENT_LIMIT_RANGE',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViReal64'
    },
    1150019: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the current level, in amps, that the PPMU forces to the DUT. This attribute is applicable only when you set the NIDIGITAL_ATTR_PPMU_OUTPUT_FUNCTION attribute to DC Current. Specify valid values for the current level using the niDigital_PPMU_ConfigureCurrentLevelRange function.\n'
        },
        'name': 'PPMU_CURRENT_LEVEL',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViReal64'
    },
    1150020: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the range of valid values for the current level, in amps, that the PPMU forces to the DUT. This attribute is applicable only when you set the NIDIGITAL_ATTR_PPMU_OUTPUT_FUNCTION attribute to DC Current.\n'
        },
        'name': 'PPMU_CURRENT_LEVEL_RANGE',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViReal64'
    },
    1150021: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the minimum voltage limit, or low clamp voltage (V :sub:`CL` ), in volts, at the pin when the PPMU forces current to the DUT. This attribute is applicable only when you set the NIDIGITAL_ATTR_PPMU_OUTPUT_FUNCTION attribute to DC Current.\n'
        },
        'name': 'PPMU_VOLTAGE_LIMIT_LOW',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViReal64'
    },
    1150022: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the maximum voltage limit, or high clamp voltage (V :sub:`CH` ), in volts, at the pin when the PPMU forces current to the DUT. This attribute is applicable only when you set the NIDIGITAL_ATTR_PPMU_OUTPUT_FUNCTION attribute to DC Current.\n'
        },
        'name': 'PPMU_VOLTAGE_LIMIT_HIGH',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViReal64'
    },
    1150023: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the pattern name or exported pattern label from which to start bursting the pattern.\n'
        },
        'name': 'START_LABEL',
        'type': 'ViString'
    },
    1150029: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the Start trigger type. The digital pattern instrument waits for this trigger after you call the niDigital_init function or the niDigital_FancyBurstPattern function, and does not burst a pattern until this trigger is received.\n',
            'table_body': [
                [
                    'NIDIGITAL_VAL_NONE',
                    'Disables the Start trigger. Pattern bursting starts immediately after you call the niDigital_init function or the niDigital_FancyBurstPattern function.'
                ],
                [
                    'NIDIGITAL_VAL_DIGITAL_EDGE',
                    'Pattern bursting does not start until the digital pattern instrument detects a digital edge.'
                ],
                [
                    'NIDIGITAL_VAL_SOFTWARE',
                    'Pattern bursting does not start until the digital pattern instrument receives a software Start trigger. Create a software Start trigger by calling the niDigital_SendSoftwareEdgeTrigger function and selecting start trigger in the **trigger** parameter.Related information: SendSoftwareEdgeTrigger function.'
                ]
            ],
            'table_header': [
                'Defined Values:'
            ]
        },
        'enum': 'TriggerType',
        'name': 'START_TRIGGER_TYPE',
        'type': 'ViInt32'
    },
    1150030: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the source terminal for the Start trigger. This property is used when the NIDIGITAL_ATTR_START_TRIGGER_TYPE attribute is set to Digital Edge. You can specify source terminals in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0. The source terminal can also be a terminal from another device, in which case the NI-Digital Pattern Driver automatically finds a route (if one is available) from that terminal to the input terminal (going through a physical PXI backplane trigger line). For example, you can set the source terminal on Dev1 to be /Dev2/StartTrigger.\n',
            'table_body': [
                [
                    'PXI_Trig0',
                    'PXI trigger line 0'
                ],
                [
                    'PXI_Trig1',
                    'PXI trigger line 1'
                ],
                [
                    'PXI_Trig2',
                    'PXI trigger line 2'
                ],
                [
                    'PXI_Trig3',
                    'PXI trigger line 3'
                ],
                [
                    'PXI_Trig4',
                    'PXI trigger line 4'
                ],
                [
                    'PXI_Trig5',
                    'PXI trigger line 5'
                ],
                [
                    'PXI_Trig6',
                    'PXI trigger line 6'
                ],
                [
                    'PXI_Trig7',
                    'PXI trigger line 7'
                ]
            ],
            'table_header': [
                'Defined Values:'
            ]
        },
        'name': 'DIGITAL_EDGE_START_TRIGGER_SOURCE',
        'type': 'ViString'
    },
    1150031: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the active edge for the Start trigger. This property is used when the NIDIGITAL_ATTR_START_TRIGGER_TYPE attribute is set to Digital Edge.\n',
            'table_body': [
                [
                    'NIDIGITAL_VAL_RISING_EDGE',
                    'Asserts the trigger when the signal transitions from low level to high level.'
                ],
                [
                    'NIDIGITAL_VAL_FALLING_EDGE',
                    'Asserts the trigger when the signal transitions from high level to low level.'
                ]
            ],
            'table_header': [
                'Defined Values:'
            ]
        },
        'enum': 'DigitalEdge',
        'name': 'DIGITAL_EDGE_START_TRIGGER_EDGE',
        'type': 'ViInt32'
    },
    1150032: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the destination terminal for exporting the Start trigger. Terminals can be specified in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.\n',
            'table_body': [
                [
                    'Do not export signal',
                    'The signal is not exported.'
                ],
                [
                    'PXI_Trig0',
                    'PXI trigger line 0'
                ],
                [
                    'PXI_Trig1',
                    'PXI trigger line 1'
                ],
                [
                    'PXI_Trig2',
                    'PXI trigger line 2'
                ],
                [
                    'PXI_Trig3',
                    'PXI trigger line 3'
                ],
                [
                    'PXI_Trig4',
                    'PXI trigger line 4'
                ],
                [
                    'PXI_Trig5',
                    'PXI trigger line 5'
                ],
                [
                    'PXI_Trig6',
                    'PXI trigger line 6'
                ],
                [
                    'PXI_Trig7',
                    'PXI trigger line 7'
                ]
            ],
            'table_header': [
                'Defined Values:'
            ]
        },
        'name': 'EXPORTED_START_TRIGGER_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150033: {
        'access': 'read-write',
        'documentation': {
            'description': 'Disables the conditional jump trigger or configures it for either hardware triggering or software triggering.  The default value is NIDIGITAL_VAL_NONE.\n',
            'table_body': [
                [
                    'NIDIGITAL_VAL_NONE',
                    'Disables the conditional jump trigger.'
                ],
                [
                    'NIDIGITAL_VAL_DIGITAL_EDGE',
                    'Configures the conditional jump trigger for hardware triggering.'
                ],
                [
                    'NIDIGITAL_VAL_SOFTWARE',
                    'Configures the conditional jump trigger for software triggering.'
                ]
            ],
            'table_header': [
                'Valid Values:'
            ]
        },
        'enum': 'TriggerType',
        'name': 'CONDITIONAL_JUMP_TRIGGER_TYPE',
        'supported_rep_caps': [
            'conditional_jump_triggers'
        ],
        'type': 'ViInt32'
    },
    1150034: {
        'access': 'read-write',
        'documentation': {
            'description': 'Configures the digital trigger source terminal for a conditional jump trigger instance. The PXIe-6570/6571 supports triggering through the PXI trigger bus. You can specify source terminals in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0. The source terminal can also be a terminal from another device, in which case the NI-Digital Pattern Driver automatically finds a route (if one is available) from that terminal to the input terminal (going through a physical PXI backplane trigger line). For example, you can set the source terminal on Dev1 to be /Dev2/ConditionalJumpTrigger0. The default value is VI_NULL.\n',
            'table_body': [
                [
                    'String identifier to any valid terminal name'
                ]
            ],
            'table_header': [
                'Valid Values:'
            ]
        },
        'name': 'DIGITAL_EDGE_CONDITIONAL_JUMP_TRIGGER_SOURCE',
        'supported_rep_caps': [
            'conditional_jump_triggers'
        ],
        'type': 'ViString'
    },
    1150035: {
        'access': 'read-write',
        'documentation': {
            'description': 'Configures the active edge of the incoming trigger signal for the conditional jump trigger instance. The default value is NIDIGITAL_VAL_RISING_EDGE.\n',
            'table_body': [
                [
                    'NIDIGITAL_VAL_RISING_EDGE',
                    'Specifies the signal transition from low level to high level.'
                ],
                [
                    'NIDIGITAL_VAL_FALLING_EDGE',
                    'Specifies the signal transition from high level to low level.'
                ]
            ],
            'table_header': [
                'Valid Values:'
            ]
        },
        'enum': 'DigitalEdge',
        'name': 'DIGITAL_EDGE_CONDITIONAL_JUMP_TRIGGER_EDGE',
        'supported_rep_caps': [
            'conditional_jump_triggers'
        ],
        'type': 'ViInt32'
    },
    1150036: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the terminal to output the exported signal of the specified instance of the conditional jump trigger. The default value is VI_NULL.\n',
            'table_body': [
                [
                    'VI_NULL ("")',
                    'Returns an empty string'
                ],
                [
                    'PXI_Trig0',
                    'PXI trigger line 0'
                ],
                [
                    'PXI_Trig1',
                    'PXI trigger line 1'
                ],
                [
                    'PXI_Trig2',
                    'PXI trigger line 2'
                ],
                [
                    'PXI_Trig3',
                    'PXI trigger line 3'
                ],
                [
                    'PXI_Trig4',
                    'PXI trigger line 4'
                ],
                [
                    'PXI_Trig5',
                    'PXI trigger line 5'
                ],
                [
                    'PXI_Trig6',
                    'PXI trigger line 6'
                ],
                [
                    'PXI_Trig7',
                    'PXI trigger line 7'
                ]
            ],
            'table_header': [
                'Valid Values:'
            ]
        },
        'name': 'EXPORTED_CONDITIONAL_JUMP_TRIGGER_OUTPUT_TERMINAL',
        'supported_rep_caps': [
            'conditional_jump_triggers'
        ],
        'type': 'ViString'
    },
    1150037: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the measurement aperture time for the PPMU. The NIDIGITAL_ATTR_PPMU_APERTURE_TIME_UNITS attribute sets the units of the PPMU aperture time.\n'
        },
        'name': 'PPMU_APERTURE_TIME',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViReal64'
    },
    1150038: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the units of the measurement aperture time for the PPMU.\n',
            'table_body': [
                [
                    'NIDIGITAL_VAL_SECONDS',
                    'Specifies the aperture time in seconds.'
                ]
            ],
            'table_header': [
                'Defined Values:'
            ]
        },
        'enum': 'PPMUApertureTimeUnits',
        'name': 'PPMU_APERTURE_TIME_UNITS',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViInt32'
    },
    1150039: {
        'access': 'read only',
        'documentation': {
            'description': 'Specifies the terminal name for the output trigger signal of the Start trigger. You can use this terminal name as an input signal source for another trigger.\n'
        },
        'name': 'START_TRIGGER_TERMINAL_NAME',
        'type': 'ViString'
    },
    1150040: {
        'access': 'read only',
        'documentation': {
            'description': 'Specifies the terminal name from which the exported conditional jump trigger signal may be routed to other instruments through the PXI trigger bus. You can use this signal to trigger other instruments when the conditional jump trigger instance asserts on the digital pattern instrument.\n'
        },
        'name': 'CONDITIONAL_JUMP_TRIGGER_TERMINAL_NAME',
        'supported_rep_caps': [
            'conditional_jump_triggers'
        ],
        'type': 'ViString'
    },
    1150041: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the destination terminal for exporting the Pattern Opcode Event. Terminals can be specified in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.\n',
            'table_body': [
                [
                    'PXI_Trig0',
                    'PXI trigger line 0'
                ],
                [
                    'PXI_Trig1',
                    'PXI trigger line 1'
                ],
                [
                    'PXI_Trig2',
                    'PXI trigger line 2'
                ],
                [
                    'PXI_Trig3',
                    'PXI trigger line 3'
                ],
                [
                    'PXI_Trig4',
                    'PXI trigger line 4'
                ],
                [
                    'PXI_Trig5',
                    'PXI trigger line 5'
                ],
                [
                    'PXI_Trig6',
                    'PXI trigger line 6'
                ],
                [
                    'PXI_Trig7',
                    'PXI trigger line 7'
                ]
            ],
            'table_header': [
                'Defined Values:'
            ]
        },
        'name': 'EXPORTED_PATTERN_OPCODE_EVENT_OUTPUT_TERMINAL',
        'supported_rep_caps': [
            'pattern_opcode_events'
        ],
        'type': 'ViString'
    },
    1150042: {
        'access': 'read only',
        'documentation': {
            'description': 'Specifies the terminal name for the output trigger signal of the specified instance of a Pattern Opcode Event. You can use this terminal name as an input signal source for another trigger.\n'
        },
        'name': 'PATTERN_OPCODE_EVENT_TERMINAL_NAME',
        'supported_rep_caps': [
            'pattern_opcode_events'
        ],
        'type': 'ViString'
    },
    1150043: {
        'access': 'read-write',
        'enum': 'HistoryRAMTriggerType',
        'documentation': {
            'description': 'Specifies the type of trigger condition on which History RAM starts acquiring pattern information.\n',
            'table_body': [
                [
                    'NIDIGITAL_VAL_FIRST_FAILURE',
                    'Starts acquiring pattern information in History RAM on the first failed cycle in a pattern burst.'
                ],
                [
                    'NIDIGITAL_VAL_CYCLE_NUMBER',
                    'Starts acquiring pattern information in History RAM starting from a specified cycle number.'
                ],
                [
                    'NIDIGITAL_VAL_PATTERN_LABEL',
                    'Starts acquiring pattern information in History RAM starting from a specified pattern label, augmented by vector and cycle offsets.'
                ]
            ],
            'table_header': [
                'Defined Values:'
            ]
        },
        'name': 'HISTORY_RAM_TRIGGER_TYPE',
        'type': 'ViInt32'
    },
    1150044: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the cycle number on which History RAM starts acquiring pattern information when configured for a cycle number trigger.\n'
        },
        'name': 'CYCLE_NUMBER_HISTORY_RAM_TRIGGER_CYCLE_NUMBER',
        'type': 'ViInt64'
    },
    1150045: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the number of cycles that follow the specified pattern label and vector offset, after which History RAM will start acquiring pattern information when configured for a pattern label trigger.\n'
        },
        'name': 'PATTERN_LABEL_HISTORY_RAM_TRIGGER_CYCLE_OFFSET',
        'type': 'ViInt64'
    },
    1150046: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the pattern label, augmented by the vector and cycle offset, to determine the point where History RAM will start acquiring pattern information when configured for a pattern label trigger.\n'
        },
        'name': 'PATTERN_LABEL_HISTORY_RAM_TRIGGER_LABEL',
        'type': 'ViString'
    },
    1150047: {
        'access': 'read-write',
        'enum': 'HistoryRAMCyclesToAcquire',
        'documentation': {
            'description': 'Configures which cycles History RAM acquires after the trigger conditions are met. If you configure History RAM to only acquire failed cycles, you must set the pretrigger samples for History RAM to 0.\n',
            'table_body': [
                [
                    'NIDIGITAL_VAL_FAILED_CYCLES',
                    'Only acquires cycles that fail a compare after the triggering conditions are met.'
                ],
                [
                    'NIDIGITAL_VAL_ALL_CYCLES',
                    'Acquires all cycles after the triggering conditions are met.'
                ]
            ],
            'table_header': [
                'Defined Values:'
            ]
        },
        'name': 'HISTORY_RAM_CYCLES_TO_ACQUIRE',
        'type': 'ViInt32'
    },
    1150048: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the number of samples to acquire before the trigger conditions are met. If you configure History RAM to only acquire failed cycles, you must set the pretrigger samples for History RAM to 0.\n'
        },
        'name': 'HISTORY_RAM_PRETRIGGER_SAMPLES',
        'type': 'ViInt32'
    },
    1150051: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'documentation': {
            'description': 'Specifies the TDR Offset.\n'
        },
        'name': 'TDR_OFFSET',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    1150052: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the number of vectors that follow the specified pattern label, after which History RAM will start acquiring pattern information when configured for a pattern label trigger.\n'
        },
        'name': 'PATTERN_LABEL_HISTORY_RAM_TRIGGER_VECTOR_OFFSET',
        'type': 'ViInt64'
    },
    1150054: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the current limit, in amps, that the output cannot exceed while the PPMU forces voltage to the DUT. This attribute is applicable only when you set the NIDIGITAL_ATTR_PPMU_OUTPUT_FUNCTION attribute to DC Voltage. The PXIe-6570/6571 does not support the NIDIGITAL_ATTR_PPMU_CURRENT_LIMIT attribute and only allows configuration of the NIDIGITAL_ATTR_PPMU_CURRENT_LIMIT_RANGE attribute.\n'
        },
        'name': 'PPMU_CURRENT_LIMIT',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViReal64'
    },
    1150055: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns whether the device supports configuration of a current limit when you set the NIDIGITAL_ATTR_PPMU_OUTPUT_FUNCTION attribute to DC Voltage.\n'
        },
        'name': 'PPMU_CURRENT_LIMIT_SUPPORTED',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViBoolean'
    },
    1150059: {
        'access': 'read only',
        'documentation': {
            'description': 'Specifies the terminal name for the output trigger signal of the Sequencer Flags trigger. You can use this terminal name as an input signal source for another trigger.\n'
        },
        'name': 'SEQUENCER_FLAG_TERMINAL_NAME',
        'type': 'ViString'
    },
    1150060: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies whether the pattern comparisons are masked or not. When set to VI_TRUE for a specified pin, failures on that pin will be masked.\n'
        },
        'name': 'MASK_COMPARE',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViBoolean'
    },
    1150062: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies whether keep_alive opcodes should behave like halt opcodes.\n'
        },
        'name': 'HALT_ON_KEEP_ALIVE_OPCODE',
        'type': 'ViBoolean'
    },
    1150063: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns VI_TRUE if the digital pattern instrument is driving the keep alive pattern.\n'
        },
        'name': 'IS_KEEP_ALIVE_ACTIVE',
        'type': 'ViBoolean'
    },
    1150064: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies how the output should behave when the current limit is reached.\n',
            'table_body': [
                [
                    'NIDIGITAL_VAL_CURRENT_REGULATE',
                    'Controls output current so that it does not exceed the current limit. Power continues to generate even if the current limit is reached.'
                ]
            ],
            'table_header': [
                'Defined Values:'
            ]
        },
        'enum': 'PPMUCurrentLimitBehavior',
        'name': 'PPMU_CURRENT_LIMIT_BEHAVIOR',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViInt32'
    },
    1150069: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'documentation': {
            'description': 'Specifies the measurement time for the frequency counter.\n'
        },
        'name': 'FREQUENCY_COUNTER_MEASUREMENT_TIME',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViReal64',
        'type_in_documentation': 'float in seconds or datetime.timedelta'
    },
    1150071: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies whether the NIDIGITAL_ATTR_TIMING_ABSOLUTE_DELAY attribute should be applied to adjust the digital pattern instrument timing reference relative to other instruments in the system. Do not use this feature with digital pattern instruments in a Semiconductor Test System (STS). Timing absolute delay conflicts with the adjustment performed during STS timing calibration. When set to VI_TRUE, the digital pattern instrument automatically adjusts the timing absolute delay to correct the instrument timing reference relative to other instruments in the system for better timing alignment among synchronized instruments.\n'
        },
        'name': 'TIMING_ABSOLUTE_DELAY_ENABLED',
        'type': 'ViBoolean'
    },
    1150072: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'documentation': {
            'description': 'Specifies a timing delay, measured in seconds, and applies the delay to the digital pattern instrument in addition to TDR and calibration adjustments. If the NIDIGITAL_ATTR_TIMING_ABSOLUTE_DELAY_ENABLED attribute is set to VI_TRUE, this value is the intermodule skew measured by NI-TClk. You can modify this value to override the timing delay and align the I/O timing of this instrument with another instrument that shares the same reference clock. If the NIDIGITAL_ATTR_TIMING_ABSOLUTE_DELAY_ENABLED attribute is VI_FALSE, this attribute will return 0.0. Changing the NIDIGITAL_ATTR_TIMING_ABSOLUTE_DELAY_ENABLED attribute from VI_FALSE to VI_TRUE will set the NIDIGITAL_ATTR_TIMING_ABSOLUTE_DELAY value back to your previously set value.\n'
        },
        'name': 'TIMING_ABSOLUTE_DELAY',
        'supported_rep_caps': [
            'instruments'
        ],
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    1150073: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the frequency for the clock generator.\n'
        },
        'name': 'CLOCK_GENERATOR_FREQUENCY',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViReal64'
    },
    1150074: {
        'access': 'read only',
        'documentation': {
            'description': 'Indicates whether the clock generator is running.\n'
        },
        'name': 'CLOCK_GENERATOR_IS_RUNNING',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViBoolean'
    },
    1150076: {
        'access': 'read-write',
        'documentation': {
            'description': 'Enables the instrument to operate in additional voltage ranges where instrument specifications may differ from standard ranges. When set to VI_TRUE, this attribute enables extended voltage range operation. Review specification deviations for application suitability before using this attribute. NI recommends setting this attribute to VI_FALSE when not using the extended voltage range to avoid unintentional use of this range. The extended voltage range is supported only for PPMU, with the output function set to DC Voltage. A voltage glitch may occur when you change the PPMU output voltage from a standard range to the extended voltage range, or vice-versa, while the PPMU is sourcing. NI recommends temporarily changing the NIDIGITAL_ATTR_SELECTED_FUNCTION attribute to Off before sourcing a voltage level that requires a range change.\n'
        },
        'name': 'PPMU_ALLOW_EXTENDED_VOLTAGE_RANGE',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViBoolean'
    },
    1150077: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the maximum number of History RAM samples to acquire per site. If the property is set to -1, it will acquire until the History RAM buffer is full.\n'
        },
        'name': 'HISTORY_RAM_MAX_SAMPLES_TO_ACQUIRE_PER_SITE',
        'type': 'ViInt32'
    },
    1150078: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies whether the instrument acquires a finite number of History Ram samples or acquires continuously. The maximum number of samples that will be acquired when this property is set to VI_TRUE is determined by the instrument History RAM depth specification and the History RAM Max Samples to Acquire Per Site property. The default value is VI_TRUE.\n',
            'table_body': [
                [
                    'VI_TRUE',
                    'Specifies that History RAM results will not stream into the host buffer until a History RAM fetch API is called.'
                ],
                [
                    'VI_FALSE',
                    'Specifies that History RAM results will automatically start streaming into a host buffer after a pattern is burst and the History RAM has triggered.'
                ]
            ],
            'table_header': [
                'Valid Values:'
            ]
        },
        'name': 'HISTORY_RAM_NUMBER_OF_SAMPLES_IS_FINITE',
        'type': 'ViBoolean'
    },
    1150079: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the size, in samples, of the host memory buffer. The default value is 32000.\n',
            'table_body': [
                [
                    '0-INT64_MAX'
                ]
            ],
            'table_header': [
                'Valid Values:'
            ]
        },
        'name': 'HISTORY_RAM_BUFFER_SIZE_PER_SITE',
        'type': 'ViInt64'
    },
    1150081: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies whether TDR Channels are connected to an open circuit or a short to ground.\n'
        },
        'enum': 'TDREndpointTermination',
        'name': 'TDR_ENDPOINT_TERMINATION',
        'type': 'ViInt32'
    },
    1150084: {
        'access': 'read-write',
        'documentation': {
            'description': 'Determines how the frequency counters of the digital pattern instrument make measurements.\n',
            'table_body': [
                [
                    'NIDIGITAL_VAL_BANKED',
                    'Each discrete frequency counter is mapped to specific channels and makes frequency measurements from only those channels. Use banked mode when you need access to the full measure frequency range of the instrument. **Note:** If you request frequency measurements from multiple channels within the same bank, the measurements are made in series for the channels in that bank.'
                ],
                [
                    'NIDIGITAL_VAL_PARALLEL',
                    'All discrete frequency counters make frequency measurements from all channels in parallel with one another. Use parallel mode to increase the speed of frequency measurements if you do not need access to the full measure frequency range of the instrument; in parallel mode, you can also add NIDIGITAL_ATTR_FREQUENCY_COUNTER_HYSTERESIS_ENABLED to reduce measurement noise.'
                ]
            ],
            'table_header': [
                'Valid Values:'
            ]
        },
        'enum': 'FrequencyMeasurementMode',
        'name': 'FREQUENCY_COUNTER_MEASUREMENT_MODE',
        'type': 'ViInt32'
    },
    1150085: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies whether hysteresis is enabled for the frequency counters of the digital pattern instrument.\n'
        },
        'name': 'FREQUENCY_COUNTER_HYSTERESIS_ENABLED',
        'type': 'ViBoolean'
    },
    1150086: {
        'access': 'read-write',
        'documentation': {
            'description': 'Disables the rio trigger or configures it for hardware triggering.  The default value is NIDIGITAL_VAL_NONE.\n',
            'table_body': [
                [
                    'NIDIGITAL_VAL_NONE',
                    'Disables the conditional jump trigger.'
                ],
                [
                    'NIDIGITAL_VAL_DIGITAL_EDGE',
                    'Configures the conditional jump trigger for hardware triggering.'
                ]
            ],
            'table_header': [
                'Valid Values:'
            ]
        },
        'enum': 'TriggerType',
        'name': 'RIO_TRIGGER_TYPE',
        'supported_rep_caps': [
            'rio_triggers'
        ],
        'type': 'ViInt32'
    },
    1150087: {
        'access': 'read-write',
        'documentation': {
            'description': 'Configures the digital trigger source terminal for a RIO trigger instance. The PXIe-6570/6571 supports triggering through the PXI trigger bus. You can specify source terminals in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0. The source terminal can also be a terminal from another device, in which case the NI-Digital Pattern Driver automatically finds a route (if one is available) from that terminal to the input terminal (going through a physical PXI backplane trigger line). For example, you can set the source terminal on Dev1 to be /Dev2/RIOTrigger0. The default value is VI_NULL.\n',
            'table_body': [
                [
                    'String identifier to any valid terminal name'
                ]
            ],
            'table_header': [
                'Valid Values:'
            ]
        },
        'name': 'DIGITAL_EDGE_RIO_TRIGGER_SOURCE',
        'supported_rep_caps': [
            'rio_triggers'
        ],
        'type': 'ViString'
    },
    1150088: {
        'access': 'read-write',
        'documentation': {
            'description': 'Configures the active edge of the incoming trigger signal for the RIO trigger instance. The default value is NIDIGITAL_VAL_RISING_EDGE.\n',
            'table_body': [
                [
                    'NIDIGITAL_VAL_RISING_EDGE',
                    'Specifies the signal transition from low level to high level.'
                ],
                [
                    'NIDIGITAL_VAL_FALLING_EDGE',
                    'Specifies the signal transition from high level to low level.'
                ]
            ],
            'table_header': [
                'Valid Values:'
            ]
        },
        'enum': 'DigitalEdge',
        'name': 'DIGITAL_EDGE_RIO_TRIGGER_EDGE',
        'supported_rep_caps': [
            'rio_triggers'
        ],
        'type': 'ViInt32'
    },
    1150089: {
        'access': 'read only',
        'documentation': {
            'description': 'Specifies the terminal name from which the exported RIO trigger signal may be routed to other instruments through the PXI trigger bus. You can use this signal to trigger other instruments when the RIO trigger instance asserts on the digital pattern instrument.\n'
        },
        'name': 'RIO_TRIGGER_TERMINAL_NAME',
        'supported_rep_caps': [
            'rio_triggers'
        ],
        'type': 'ViString'
    },
    1150090: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the destination terminal for exporting the RIO Event. Terminals can be specified in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.\n',
            'table_body': [
                [
                    'PXI_Trig0',
                    'PXI trigger line 0'
                ],
                [
                    'PXI_Trig1',
                    'PXI trigger line 1'
                ],
                [
                    'PXI_Trig2',
                    'PXI trigger line 2'
                ],
                [
                    'PXI_Trig3',
                    'PXI trigger line 3'
                ],
                [
                    'PXI_Trig4',
                    'PXI trigger line 4'
                ],
                [
                    'PXI_Trig5',
                    'PXI trigger line 5'
                ],
                [
                    'PXI_Trig6',
                    'PXI trigger line 6'
                ],
                [
                    'PXI_Trig7',
                    'PXI trigger line 7'
                ]
            ],
            'table_header': [
                'Defined Values:'
            ]
        },
        'name': 'EXPORTED_RIO_EVENT_OUTPUT_TERMINAL',
        'supported_rep_caps': [
            'rio_events'
        ],
        'type': 'ViString'
    },
    1150091: {
        'access': 'read only',
        'documentation': {
            'description': 'Specifies the terminal name for the output signal of the specified instance of a RIO Event. You can use this terminal name as an input signal source for another trigger.\n'
        },
        'name': 'RIO_EVENT_TERMINAL_NAME',
        'supported_rep_caps': [
            'rio_events'
        ],
        'type': 'ViString'
    }
}
