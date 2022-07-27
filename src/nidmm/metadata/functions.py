# -*- coding: utf-8 -*-
# This file is generated from NI-DMM API metadata version 22.8.0d38
functions = {
    'Abort': {
        'documentation': {
            'description': '\nAborts a previously initiated measurement and returns the DMM to the\nIdle state.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureMeasurementAbsolute': {
        'documentation': {
            'description': '\nConfigures the common attributes of the measurement. These attributes\ninclude NIDMM_ATTR_FUNCTION, NIDMM_ATTR_RANGE, and\nNIDMM_ATTR_RESOLUTION_ABSOLUTE.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **measurement_function** used to acquire the measurement.\nThe driver sets NIDMM_ATTR_FUNCTION to this value.\n'
                },
                'enum': 'Function',
                'name': 'measurementFunction',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **range** for the function specified in the\n**Measurement_Function** parameter. When frequency is specified in the\n**Measurement_Function** parameter, you must supply the minimum\nfrequency expected in the **range** parameter. For example, you must\ntype in 100 Hz if you are measuring 101 Hz or higher.\nFor all other functions, you must supply a **range** that exceeds the\nvalue that you are measuring. For example, you must type in 10 V if you\nare measuring 9 V. **range** values are coerced up to the closest input\n**range**. Refer to the `Devices\nOverview <REPLACE_DRIVER_SPECIFIC_URL_1(devices)>`__ for a list of valid\nranges. The driver sets NIDMM_ATTR_RANGE to this value. The default is\n0.02 V.\n',
                    'note': '\nThe NI 4050, NI 4060, and NI 4065 only support Auto Range when the\ntrigger and sample trigger are set to IMMEDIATE.\n',
                    'table_body': [
                        [
                            'NIDMM_VAL_AUTO_RANGE_ON',
                            '-1.0',
                            'NI-DMM performs an Auto Range before acquiring the measurement.'
                        ],
                        [
                            'NIDMM_VAL_AUTO_RANGE_OFF',
                            '-2.0',
                            'NI-DMM sets the Range to the current NIDMM_ATTR_AUTO_RANGE_VALUE and uses this range for all subsequent measurements until the measurement configuration is changed.'
                        ],
                        [
                            'NIDMM_VAL_AUTO_RANGE_ONCE',
                            '-3.0',
                            'NI-DMM performs an Auto Range before acquiring the measurement. The NIDMM_ATTR_AUTO_RANGE_VALUE is stored and used for all subsequent measurements until the measurement configuration is changed.'
                        ]
                    ]
                },
                'name': 'range',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the absolute resolution for the measurement. NI-DMM sets\nNIDMM_ATTR_RESOLUTION_ABSOLUTE to this value. The PXIe-4080/4081/4082\nuses the resolution you specify. The NI 4065 and NI 4070/4071/4072\nignore this parameter when the **Range** parameter is set to\nNIDMM_VAL_AUTO_RANGE_ON (-1.0) or NIDMM_VAL_AUTO_RANGE_ONCE\n(-3.0). The default is 0.001 V.\n',
                    'note': '\nNI-DMM ignores this parameter for capacitance and inductance\nmeasurements on the NI 4072. To achieve better resolution for such\nmeasurements, use the NIDMM_ATTR_LC_NUMBER_MEAS_TO_AVERAGE\nattribute.\n'
                },
                'name': 'resolutionAbsolute',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureMeasurementDigits': {
        'documentation': {
            'description': '\nConfigures the common attributes of the measurement. These attributes\ninclude NIDMM_ATTR_FUNCTION, NIDMM_ATTR_RANGE, and\nNIDMM_ATTR_RESOLUTION_DIGITS.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **measurement_function** used to acquire the measurement.\nThe driver sets NIDMM_ATTR_FUNCTION to this value.\n'
                },
                'enum': 'Function',
                'name': 'measurementFunction',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the range for the function specified in the\n**Measurement_Function** parameter. When frequency is specified in the\n**Measurement_Function** parameter, you must supply the minimum\nfrequency expected in the **range** parameter. For example, you must\ntype in 100 Hz if you are measuring 101 Hz or higher.\nFor all other functions, you must supply a range that exceeds the value\nthat you are measuring. For example, you must type in 10 V if you are\nmeasuring 9 V. range values are coerced up to the closest input range.\nRefer to the `Devices\nOverview <REPLACE_DRIVER_SPECIFIC_URL_1(devices)>`__ for a list of valid\nranges. The driver sets NIDMM_ATTR_RANGE to this value. The default is\n0.02 V.\n',
                    'note': '\nThe NI 4050, NI 4060, and NI 4065 only support Auto Range when the\ntrigger and sample trigger are set to IMMEDIATE.\n',
                    'table_body': [
                        [
                            'NIDMM_VAL_AUTO_RANGE_ON',
                            '-1.0',
                            'NI-DMM performs an Auto Range before acquiring the measurement.'
                        ],
                        [
                            'NIDMM_VAL_AUTO_RANGE_OFF',
                            '-2.0',
                            'NI-DMM sets the Range to the current NIDMM_ATTR_AUTO_RANGE_VALUE and uses this range for all subsequent measurements until the measurement configuration is changed.'
                        ],
                        [
                            'NIDMM_VAL_AUTO_RANGE_ONCE',
                            '-3.0',
                            'NI-DMM performs an Auto Range before acquiring the measurement. The NIDMM_ATTR_AUTO_RANGE_VALUE is stored and used for all subsequent measurements until the measurement configuration is changed.'
                        ]
                    ]
                },
                'name': 'range',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the resolution of the measurement in digits. The driver sets\nthe `Devices Overview <REPLACE_DRIVER_SPECIFIC_URL_1(devices)>`__ for a\nlist of valid ranges. The driver sets NIDMM_ATTR_RESOLUTION_DIGITS\nattribute to this value. The PXIe-4080/4081/4082 uses the resolution you\nspecify. The NI 4065 and NI 4070/4071/4072 ignore this parameter when\nthe **Range** parameter is set to NIDMM_VAL_AUTO_RANGE_ON (-1.0) or\nNIDMM_VAL_AUTO_RANGE_ONCE (-3.0). The default is 5½.\n',
                    'note': '\nNI-DMM ignores this parameter for capacitance and inductance\nmeasurements on the NI 4072. To achieve better resolution for such\nmeasurements, use the NIDMM_ATTR_LC_NUMBER_MEAS_TO_AVERAGE\nattribute.\n'
                },
                'name': 'resolutionDigits',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureMultiPoint': {
        'documentation': {
            'description': '\nConfigures the attributes for multipoint measurements. These attributes\ninclude NIDMM_ATTR_TRIGGER_COUNT, NIDMM_ATTR_SAMPLE_COUNT,\nNIDMM_ATTR_SAMPLE_TRIGGER, and NIDMM_ATTR_SAMPLE_INTERVAL.\n\nFor continuous acquisitions, set NIDMM_ATTR_TRIGGER_COUNT or\nNIDMM_ATTR_SAMPLE_COUNT to zero. For more information, refer to\n`Multiple Point\nAcquisitions <REPLACE_DRIVER_SPECIFIC_URL_1(multi_point)>`__,\n`Triggering <REPLACE_DRIVER_SPECIFIC_URL_1(trigger)>`__, and `Using\nSwitches <REPLACE_DRIVER_SPECIFIC_URL_1(switch_selection)>`__.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSets the number of triggers you want the DMM to receive before returning\nto the Idle state. The driver sets NIDMM_ATTR_TRIGGER_COUNT to this\nvalue. The default value is 1.\n'
                },
                'name': 'triggerCount',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSets the number of measurements the DMM makes in each measurement\nsequence initiated by a trigger. The driver sets\nNIDMM_ATTR_SAMPLE_COUNT to this value. The default value is 1.\n'
                },
                'name': 'sampleCount',
                'type': 'ViInt32'
            },
            {
                'default_value': 'SampleTrigger.IMMEDIATE',
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **sample_trigger** source you want to use. The driver\nsets NIDMM_ATTR_SAMPLE_TRIGGER to this value. The default is\nImmediate.\n',
                    'note': '\nTo determine which values are supported by each device, refer to the\n`LabWindows/CVI Trigger\nRouting <REPLACE_DRIVER_SPECIFIC_URL_1(cvitrigger_routing)>`__ section.\n'
                },
                'enum': 'SampleTrigger',
                'name': 'sampleTrigger',
                'type': 'ViInt32'
            },
            {
                'default_value': 'hightime.timedelta(seconds=-1)',
                'direction': 'in',
                'documentation': {
                    'description': '\nSets the amount of time in seconds the DMM waits between measurement\ncycles. The driver sets NIDMM_ATTR_SAMPLE_INTERVAL to this value.\nSpecify a sample interval to add settling time between measurement\ncycles or to decrease the measurement rate. **sample_interval** only\napplies when the **Sample_Trigger** is set to INTERVAL.\n\nOn the NI 4060, the **sample_interval** value is used as the settling\ntime. When sample interval is set to 0, the DMM does not settle between\nmeasurement cycles. The NI 4065 and NI 4070/4071/4072 use the value\nspecified in **sample_interval** as additional delay. The default value\n(-1) ensures that the DMM settles for a recommended time. This is the\nsame as using an Immediate trigger.\n',
                    'note': 'This attribute is not used on the NI 4080/4081/4082 and the NI 4050.'
                },
                'name': 'sampleInterval',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureRTDCustom': {
        'documentation': {
            'description': 'Configures the A, B, and C parameters for a custom RTD.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the Callendar-Van Dusen A coefficient for RTD scaling when RTD\nType parameter is set to Custom in the niDMM_ConfigureRTDType function.\nThe default is 3.9083e-3 (Pt3851)\n'
                },
                'name': 'rtdA',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the Callendar-Van Dusen B coefficient for RTD scaling when RTD\nType parameter is set to Custom in the niDMM_ConfigureRTDType function.\nThe default is -5.775e-7 (Pt3851).\n'
                },
                'name': 'rtdB',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the Callendar-Van Dusen C coefficient for RTD scaling when RTD\nType parameter is set to Custom in the niDMM_ConfigureRTDType function.\nThe default is -4.183e-12 (Pt3851).\n'
                },
                'name': 'rtdC',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureRTDType': {
        'documentation': {
            'description': 'Configures the RTD Type and RTD Resistance parameters for an RTD.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the type of RTD used to measure the temperature resistance.\nNI-DMM uses this value to set the RTD Type property. The default is\nNIDMM_VAL_TEMP_RTD_PT3851.\n',
                    'table_body': [
                        [
                            'Callendar-Van Dusen Coefficient'
                        ],
                        [
                            'NIDMM_VAL_TEMP_RTD_PT3851',
                            'IEC-751 DIN 43760 BS 1904 ASTM-E1137 EN-60751',
                            'Platinum',
                            '.003851',
                            '100 Ω 1000 Ω',
                            'A = 3.9083 × 10\\ :sup:`–3` B = –5.775×10:sup:`–7` C = –4.183×10:sup:`–12`',
                            'Most common RTDs'
                        ],
                        [
                            'NIDMM_VAL_TEMP_RTD_PT3750',
                            'Low-cost vendor compliant RTD\\*',
                            'Platinum',
                            '.003750',
                            '1000 Ω',
                            'A = 3.81 × 10\\ :sup:`–3` B = –6.02×10:sup:`–7` C = –6.0×10:sup:`–12`',
                            'Low-cost RTD'
                        ],
                        [
                            'NIDMM_VAL_TEMP_RTD_PT3916',
                            'JISC 1604',
                            'Platinum',
                            '.003916',
                            '100 Ω',
                            'A = 3.9739 × 10\\ :sup:`–3` B = –5.870×10:sup:`–7` C = –4.4 ×10\\ :sup:`–12`',
                            'Used in primarily in Japan'
                        ],
                        [
                            'NIDMM_VAL_TEMP_RTD_PT3920',
                            'US Industrial Standard D-100 American',
                            'Platinum',
                            '.003920',
                            '100 Ω',
                            'A = 3.9787 × 10\\ :sup:`–3` B = –5.8686×10:sup:`–7` C = –4.167 ×10\\ :sup:`–12`',
                            'Low-cost RTD'
                        ],
                        [
                            'NIDMM_VAL_TEMP_RTD_PT3911',
                            'US Industrial Standard American',
                            'Platinum',
                            '.003911',
                            '100 Ω',
                            'A = 3.9692 × 10\\ :sup:`–3` B = –5.8495×10:sup:`–7` C = –4.233 ×10\\ :sup:`–12`',
                            'Low-cost RTD'
                        ],
                        [
                            'NIDMM_VAL_TEMP_RTD_PT3928',
                            'ITS-90',
                            'Platinum',
                            '.003928',
                            '100 Ω',
                            'A = 3.9888 × 10\\ :sup:`–3` B = –5.915×10:sup:`–7` C = –3.85 ×10\\ :sup:`–12`',
                            'The definition of temperature'
                        ],
                        [
                            '\\*No standard. Check the TCR.'
                        ]
                    ],
                    'table_header': [
                        'Enum',
                        'Standards',
                        'Material',
                        'TCR (α)',
                        'Typical R\\ :sub:`0` (Ω)',
                        'Notes'
                    ]
                },
                'enum': 'RTDType',
                'name': 'rtdType',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the RTD resistance in ohms at 0 °C. NI-DMM uses this value to\nset the RTD Resistance property. The default is 100 (Ω).\n'
                },
                'name': 'rtdResistance',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureThermistorCustom': {
        'documentation': {
            'description': 'Configures the A, B, and C parameters for a custom thermistor.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the Steinhart-Hart A coefficient for thermistor scaling when\nThermistor Type is set to Custom in the niDMM_ConfigureThermistorType\nfunction. The default is 1.0295e-3 (44006).\n'
                },
                'name': 'thermistorA',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the Steinhart-Hart B coefficient for thermistor scaling when\nThermistor Type is set to Custom in the niDMM_ConfigureThermistorType\nfunction. The default is 2.391e-4 (44006).\n'
                },
                'name': 'thermistorB',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the Steinhart-Hart C coefficient for thermistor scaling when\nThermistor Type is set to Custom in the niDMM_ConfigureThermistorType\nfunction. The default is 1.568e-7 (44006).\n'
                },
                'name': 'thermistorC',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureThermocouple': {
        'documentation': {
            'description': '\nConfigures the thermocouple type and reference junction type for a\nchosen thermocouple.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the type of thermocouple used to measure the temperature.\nNI-DMM uses this value to set the Thermocouple Type property. The\ndefault is NIDMM_VAL_TEMP_TC_J.\n',
                    'table_body': [
                        [
                            'NIDMM_VAL_TEMP_TC_B',
                            'Thermocouple type B'
                        ],
                        [
                            'NIDMM_VAL_TEMP_TC_E',
                            'Thermocouple type E'
                        ],
                        [
                            'NIDMM_VAL_TEMP_TC_J',
                            'Thermocouple type J'
                        ],
                        [
                            'NIDMM_VAL_TEMP_TC_K',
                            'Thermocouple type K'
                        ],
                        [
                            'NIDMM_VAL_TEMP_TC_N',
                            'Thermocouple type N'
                        ],
                        [
                            'NIDMM_VAL_TEMP_TC_R',
                            'Thermocouple type R'
                        ],
                        [
                            'NIDMM_VAL_TEMP_TC_S',
                            'Thermocouple type S'
                        ],
                        [
                            'NIDMM_VAL_TEMP_TC_T',
                            'Thermocouple type T'
                        ]
                    ]
                },
                'enum': 'ThermocoupleType',
                'name': 'thermocoupleType',
                'type': 'ViInt32'
            },
            {
                'default_value': 'ThermocoupleReferenceJunctionType.FIXED',
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the type of reference junction to be used in the reference\njunction compensation of a thermocouple measurement. NI-DMM uses this\nvalue to set the Reference Junction Type property. The only supported\nvalue is NIDMM_VAL_TEMP_REF_JUNC_FIXED.\n'
                },
                'enum': 'ThermocoupleReferenceJunctionType',
                'name': 'referenceJunctionType',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTrigger': {
        'documentation': {
            'description': '\nConfigures the DMM **Trigger_Source** and **Trigger_Delay**. Refer to\n`Triggering <REPLACE_DRIVER_SPECIFIC_URL_1(trigger)>`__ and `Using\nSwitches <REPLACE_DRIVER_SPECIFIC_URL_1(switch_selection)>`__ for more\ninformation.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **trigger_source** that initiates the acquisition. The\ndriver sets NIDMM_ATTR_TRIGGER_SOURCE to this value. Software\nconfigures the DMM to wait until niDMM_SendSoftwareTrigger is called\nbefore triggering the DMM.\n',
                    'note': '\nTo determine which values are supported by each device, refer to the\n`LabWindows/CVI Trigger\nRouting <REPLACE_DRIVER_SPECIFIC_URL_1(cvitrigger_routing)>`__ section.\n'
                },
                'enum': 'TriggerSource',
                'name': 'triggerSource',
                'type': 'ViInt32'
            },
            {
                'default_value': 'hightime.timedelta(seconds=-1)',
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the time that the DMM waits after it has received a trigger\nbefore taking a measurement. The driver sets the\nNIDMM_ATTR_TRIGGER_DELAY attribute to this value. By default,\n**trigger_delay** is NIDMM_VAL_AUTO_DELAY (-1), which means the DMM\nwaits an appropriate settling time before taking the measurement. On the\nNI 4060, if you set **trigger_delay** to 0, the DMM does not settle\nbefore taking the measurement. The NI 4065 and NI 4070/4071/4072 use the\nvalue specified in **trigger_delay** as additional settling time.\n',
                    'note': '\nWhen using the NI 4050, **Trigger_Delay** must be set to\nNIDMM_VAL_AUTO_DELAY (-1).\n'
                },
                'name': 'triggerDelay',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureWaveformAcquisition': {
        'documentation': {
            'description': '\nConfigures the DMM for waveform acquisitions. This feature is supported\non the NI 4080/4081/4082 and the NI 4070/4071/4072.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **measurement_function** used in a waveform acquisition.\nThe driver sets NIDMM_ATTR_FUNCTION to this value.\n',
                    'table_body': [
                        [
                            'NIDMM_VAL_WAVEFORM_VOLTAGE (default)',
                            '1003',
                            'Voltage Waveform'
                        ],
                        [
                            'NIDMM_VAL_WAVEFORM_CURRENT',
                            '1004',
                            'Current Waveform'
                        ]
                    ]
                },
                'enum': 'Function',
                'name': 'measurementFunction',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the expected maximum amplitude of the input signal and sets\nthe **range** for the **Measurement_Function**. NI-DMM sets\nNIDMM_ATTR_RANGE to this value. **range** values are coerced up to the\nclosest input **range**. The default is 10.0.\n\nFor valid ranges refer to the topics in\n`Devices <REPLACE_DRIVER_SPECIFIC_URL_1(devices)>`__.\n\nAuto-ranging is not supported during waveform acquisitions.\n'
                },
                'name': 'range',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **rate** of the acquisition in samples per second. NI-DMM\nsets NIDMM_ATTR_WAVEFORM_RATE to this value.\n\nThe valid **Range** is 10.0–1,800,000 S/s. **rate** values are coerced\nto the closest integer divisor of 1,800,000. The default value is\n1,800,000.\n'
                },
                'name': 'rate',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of points to acquire before the waveform\nacquisition completes. NI-DMM sets NIDMM_ATTR_WAVEFORM_POINTS to this\nvalue.\n\nTo calculate the maximum and minimum number of waveform points that you\ncan acquire in one acquisition, refer to the `Waveform Acquisition\nMeasurement Cycle <REPLACE_DRIVER_SPECIFIC_URL_1(waveform_cycle)>`__.\n\nThe default value is 500.\n'
                },
                'name': 'waveformPoints',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'Disable': {
        'documentation': {
            'description': '\nPlaces the instrument in a quiescent state where it has minimal or no\nimpact on the system to which it is connected. If a measurement is in\nprogress when this function is called, the measurement is aborted.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ExportAttributeConfigurationBuffer': {
        'documentation': {
            'description': '\nExports the attribute configuration of the session to the specified\nconfiguration buffer.\n\nYou can export and import session attribute configurations only between\ndevices with identical model numbers.\n\nThis function verifies that the attributes you have configured for the\nsession are valid. If the configuration is invalid, NI‑DMM returns an\nerror.\n\n**Coercion Behavior for Certain Devices**\n\nImported and exported attribute configurations contain coerced values\nfor the following NI‑DMM devices:\n\n-  PXI/PCI/PCIe/USB‑4065\n-  PXI/PCI‑4070\n-  PXI‑4071\n-  PXI‑4072\n\nNI‑DMM coerces attribute values when the value you set is within the\nallowed range for the attribute but is not one of the discrete valid\nvalues the attribute supports. For example, for an attribute that\ncoerces values up, if you choose a value of 4 when the adjacent valid\nvalues are 1 and 10, the attribute coerces the value to 10.\n\n**Related Topics:**\n\n`Using Attributes and Properties with\nNI‑DMM <REPLACE_DRIVER_SPECIFIC_URL_1(attributes)>`__\n\n`Setting Attributes Before Reading\nAttributes <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__\n',
            'note': 'Not supported on the PCMCIA‑4050 or the PXI/PCI‑4060.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the size, in bytes, of the byte array to export. If you enter\n0, this function returns the needed size.\n'
                },
                'name': 'size',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nSpecifies the byte array buffer to be populated with the exported\nattribute configuration.\n'
                },
                'name': 'configuration',
                'python_api_converter_name': 'convert_to_bytes',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'size'
                },
                'type': 'ViInt8[]',
                'type_in_documentation': 'bytes',
                'use_array': True
            }
        ],
        'returns': 'ViStatus'
    },
    'ExportAttributeConfigurationFile': {
        'documentation': {
            'description': '\nExports the attribute configuration of the session to the specified\nfile.\n\nYou can export and import session attribute configurations only between\ndevices with identical model numbers.\n\nThis function verifies that the attributes you have configured for the\nsession are valid. If the configuration is invalid, NI‑DMM returns an\nerror.\n\n**Coercion Behavior for Certain Devices**\n\nImported and exported attribute configurations contain coerced values\nfor the following NI‑DMM devices:\n\n-  PXI/PCI/PCIe/USB‑4065\n-  PXI/PCI‑4070\n-  PXI‑4071\n-  PXI‑4072\n\nNI‑DMM coerces attribute values when the value you set is within the\nallowed range for the attribute but is not one of the discrete valid\nvalues the attribute supports. For example, for an attribute that\ncoerces values up, if you choose a value of 4 when the adjacent valid\nvalues are 1 and 10, the attribute coerces the value to 10.\n\n**Related Topics:**\n\n`Using Attributes and Properties with\nNI‑DMM <REPLACE_DRIVER_SPECIFIC_URL_1(attributes)>`__\n\n`Setting Attributes Before Reading\nAttributes <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__\n',
            'note': 'Not supported on the PCMCIA‑4050 or the PXI/PCI‑4060.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the absolute path to the file to contain the exported\nattribute configuration. If you specify an empty or relative path, this\nfunction returns an error.\n**Default file extension:**\\  .nidmmconfig\n'
                },
                'name': 'filePath',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'Fetch': {
        'documentation': {
            'description': '\nReturns the value from a previously initiated measurement. You must call\nniDMM_Initiate before calling this function.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': 'hightime.timedelta(milliseconds=-1)',
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **maximum_time** allowed for this function to complete in\nmilliseconds. If the function does not complete within this time\ninterval, the function returns the NIDMM_ERROR_MAX_TIME_EXCEEDED\nerror code. This may happen if an external trigger has not been\nreceived, or if the specified timeout is not long enough for the\nacquisition to complete.\n\nThe valid range is 0–86400000. The default value is\nNIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout\nautomatically.\n'
                },
                'name': 'maximumTime',
                'python_api_converter_name': 'convert_timedelta_to_milliseconds_int32',
                'type': 'ViInt32',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or int in milliseconds'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The measured value returned from the DMM.'
                },
                'name': 'reading',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchMultiPoint': {
        'documentation': {
            'description': '\nReturns an array of values from a previously initiated multipoint\nmeasurement. The number of measurements the DMM makes is determined by\nthe values you specify for the **Trigger_Count** and **Sample_Count**\nparameters of niDMM_ConfigureMultiPoint. You must first call\nniDMM_Initiate to initiate a measurement before calling this function.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': 'hightime.timedelta(milliseconds=-1)',
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **maximum_time** allowed for this function to complete in\nmilliseconds. If the function does not complete within this time\ninterval, the function returns the NIDMM_ERROR_MAX_TIME_EXCEEDED\nerror code. This may happen if an external trigger has not been\nreceived, or if the specified timeout is not long enough for the\nacquisition to complete.\n\nThe valid range is 0–86400000. The default value is\nNIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout\nautomatically.\n'
                },
                'name': 'maximumTime',
                'python_api_converter_name': 'convert_timedelta_to_milliseconds_int32',
                'type': 'ViInt32',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or int in milliseconds'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of measurements to acquire. The maximum number of\nmeasurements for a finite acquisition is the (**Trigger Count** x\n**Sample Count**) parameters in niDMM_ConfigureMultiPoint.\n\nFor continuous acquisitions, up to 100,000 points can be returned at\nonce. The number of measurements can be a subset. The valid range is any\npositive ViInt32. The default value is 1.\n'
                },
                'name': 'arraySize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'An array of measurement values.',
                    'note': '\nThe size of the **Reading_Array** must be at least the size that you\nspecify for the **Array_Size** parameter.\n'
                },
                'name': 'readingArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arraySize'
                },
                'type': 'ViReal64[]',
                'use_array': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the number of measured values actually retrieved from the DMM.'
                },
                'name': 'actualNumberOfPoints',
                'type': 'ViInt32',
                'use_in_python_api': False
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchWaveform': {
        'documentation': {
            'description': '\nFor the NI 4080/4081/4082 and the NI 4070/4071/4072, returns an array of\nvalues from a previously initiated waveform acquisition. You must call\nniDMM_Initiate before calling this function.\n'
        },
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            },
            {
                'documentation_filename': 'numpy_method',
                'method_python_name_suffix': '_into',
                'session_filename': 'numpy_read_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': 'hightime.timedelta(milliseconds=-1)',
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **maximum_time** allowed for this function to complete in\nmilliseconds. If the function does not complete within this time\ninterval, the function returns the NIDMM_ERROR_MAX_TIME_EXCEEDED\nerror code. This may happen if an external trigger has not been\nreceived, or if the specified timeout is not long enough for the\nacquisition to complete.\n\nThe valid range is 0–86400000. The default value is\nNIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout\nautomatically.\n'
                },
                'name': 'maximumTime',
                'python_api_converter_name': 'convert_timedelta_to_milliseconds_int32',
                'type': 'ViInt32',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or int in milliseconds'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of waveform points to return. You specify the total\nnumber of points that the DMM acquires in the **Waveform Points**\nparameter of niDMM_ConfigureWaveformAcquisition. The default value is\n1.\n'
                },
                'name': 'arraySize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\n**Waveform Array** is an array of measurement values stored in waveform\ndata type.\n'
                },
                'name': 'waveformArray',
                'numpy': True,
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arraySize'
                },
                'type': 'ViReal64[]',
                'use_array': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the number of measured values actually retrieved from the DMM.'
                },
                'name': 'actualNumberOfPoints',
                'type': 'ViInt32',
                'use_in_python_api': False
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViBoolean': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nQueries the value of a ViBoolean attribute. You can use this function to\nget the values of instrument-specific attributes and inherent IVI\nattributes.\n\nIf the attribute represents an instrument state, this function performs\ninstrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled, and the currently cached value is invalid.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis parameter is ignored. NI DMMs do not support\nchannel names since they only have a single channel. This parameter is\nincluded in order to support interchangeability and upgradability to\nmultiple channel DMMs.\n\nThe default value is " " (an empty string).\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the current value of the attribute. Pass the address of a\nViBoolean variable.\n'
                },
                'name': 'attributeValue',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViInt32': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nQueries the value of a ViInt32 attribute. You can use this function to\nget the values of instrument-specific attributes and inherent IVI\nattributes.\n\nIf the attribute represents an instrument state, this function performs\ninstrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled, and the currently cached value is invalid.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis parameter is ignored. NI DMMs do not support\nchannel names since they only have a single channel. This parameter is\nincluded in order to support interchangeability and upgradability to\nmultiple channel DMMs.\n\nThe default value is " " (an empty string).\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the current value of the attribute. Pass the address of a\nViInt32 variable.\n'
                },
                'name': 'attributeValue',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViReal64': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nQueries the value of a ViReal64 attribute. You can use this function to\nget the values of instrument-specific attributes and inherent IVI\nattributes.\n\nIf the attribute represents an instrument state, this function performs\ninstrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled, and the currently cached value is invalid.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis parameter is ignored. NI DMMs do not support\nchannel names since they only have a single channel. This parameter is\nincluded in order to support interchangeability and upgradability to\nmultiple channel DMMs.\n\nThe default value is " " (an empty string).\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the current value of the attribute. Pass the address of a\nViReal64 variable.\n'
                },
                'name': 'attributeValue',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViString': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nQueries the value of a ViString attribute. You can use this function to\nget the values of instrument-specific attributes and inherent IVI\nattributes.\n\nIf the attribute represents an instrument state, this function performs\ninstrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled, and the currently cached value is invalid.\n   You must provide a ViChar array to serve as a buffer for the value.\n   You pass the number of bytes in the buffer as the Array Size\n   parameter.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis parameter is ignored. NI DMMs do not support\nchannel names since they only have a single channel. This parameter is\nincluded in order to support interchangeability and upgradability to\nmultiple channel DMMs.\n\nThe default value is " " (an empty string).\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the number of bytes in the ViChar array you specify for the\n**Attribute_Value** parameter.\n\nIf the current value of the attribute, including the terminating NULL\nbyte, contains more bytes that you indicate in this parameter, the\nfunction copies **buffer_size**—1 bytes into the buffer, places an\nASCII NUL byte at the end of the buffer, and returns the buffer size you\nmust pass to get the entire value. For example, if the value is "123456"\nand the **buffer_size** is 4, the function places "123" into the buffer\nand returns 7.\n\nIf you pass a negative number, the function copies the value to the\nbuffer regardless of the number of bytes in the value. If you pass 0,\nyou can pass VI_NULL for the **Attribute_Value** buffer parameter.\n'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe buffer in which the function returns the current value of the\nattribute. The buffer must be of type ViChar and have at least as many\nbytes as indicated in the **Buffer_Size** parameter.\n\nIf you specify 0 for the **Buffer_Size** parameter, you can pass\nVI_NULL for this parameter.\n'
                },
                'name': 'attributeValue',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetCalDateAndTime': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Returns the date and time of the last calibration performed.',
            'note': 'The NI 4050 and NI 4060 are not supported.'
        },
        'method_name_for_documentation': 'get_cal_date_and_time',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the type of calibration performed (external or\nself-calibration).\n',
                    'note': 'The NI 4065 does not support self-calibration.',
                    'table_body': [
                        [
                            'NIDMM_VAL_INTERNAL_AREA (default)',
                            '0',
                            'Self-Calibration'
                        ],
                        [
                            'NIDMM_VAL_EXTERNAL_AREA',
                            '1',
                            'External Calibration'
                        ]
                    ]
                },
                'name': 'calType',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the **month** of the last calibration.'
                },
                'name': 'month',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the **day** of the last calibration.'
                },
                'name': 'day',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the **year** of the last calibration.'
                },
                'name': 'year',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the **hour** of the last calibration.'
                },
                'name': 'hour',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the **minute** of the last calibration.'
                },
                'name': 'minute',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetDevTemp': {
        'documentation': {
            'description': 'Returns the current **Temperature** of the device.',
            'note': 'The NI 4050 and NI 4060 are not supported.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': '""',
                'direction': 'in',
                'documentation': {
                    'description': 'Reserved.'
                },
                'name': 'options',
                'type': 'ViString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the current **temperature** of the device.'
                },
                'name': 'temperature',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetError': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nReturns the error information associated with the\n**Instrument_Handle**. This function retrieves and then clears the\nerror information for the session. If you leave the\n**Instrument_Handle** unwired, this function retrieves and then clears\nthe error information for the process.\n'
        },
        'is_error_handling': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the **error_code** for the session or execution thread. If you\npass 0 for the **Buffer_Size**, you can pass VI_NULL for this\nparameter.\n'
                },
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPasses the number of bytes in the ViChar array you specify for the\n**Description** parameter. If the error description, including the\nterminating NULL byte, contains more bytes than you indicate in this\nparameter, the function copies **buffer_size** –1 bytes into the\nbuffer, places an ASCII NULL byte at the end of the buffer, and returns\nthe **buffer_size** you must pass to get the entire value.\n\nFor example, if the value is "123456" and the **buffer_size** is 4, the\nfunction places "123" into the buffer and returns 7. If you pass a\nnegative number, the function copies the value to the buffer regardless\nof the number of bytes in the value. If you pass 0, you can pass\nVI_NULL for the **Description** buffer parameter. The default value is\nNone.\n'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the error **description** for the IVI session or execution\nthread. If there is no **description**, the function returns an empty\nstring. The buffer must contain at least as many elements as the value\nyou specify with the **Buffer_Size** parameter. If you pass 0 for the\n**Buffer_Size**, you can pass VI_NULL for this parameter.\n'
                },
                'name': 'description',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'GetExtCalRecommendedInterval': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nReturns the recommended interval between external recalibration in\n**Months**.\n',
            'note': 'The NI 4050 and NI 4060 are not supported.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the recommended number of **months** between external\ncalibrations.\n'
                },
                'name': 'months',
                'python_api_converter_name': 'convert_month_to_timedelta',
                'type': 'ViInt32',
                'type_in_documentation': 'hightime.timedelta'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetLastCalDateAndTime': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': 'Returns the date and time of the last calibration performed.',
            'note': 'The NI 4050 and NI 4060 are not supported.'
        },
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'datetime_wrappers'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. You obtain the **vi** parameter from niDMM_init or niDMM_InitWithOptions. The default is None.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the type of calibration performed (external or self-calibration).',
                    'note': 'The NI 4065 does not support self-calibration.',
                    'table_body': [
                        [
                            'NIDMM_VAL_INTERNAL_AREA (default)',
                            '0',
                            'Self-Calibration'
                        ],
                        [
                            'NIDMM_VAL_EXTERNAL_AREA',
                            '1',
                            'External Calibration'
                        ]
                    ]
                },
                'name': 'calType',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates date and time of the last calibration.'
                },
                'name': 'lastCalDatetime',
                'type': 'hightime.datetime'
            }
        ],
        'python_name': 'get_cal_date_and_time',
        'real_datetime_call': 'GetCalDateAndTime',
        'returns': 'ViStatus'
    },
    'GetLastCalTemp': {
        'documentation': {
            'description': 'Returns the **Temperature** during the last calibration procedure.',
            'note': 'The NI 4050 and NI 4060 are not supported.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the type of calibration performed (external or\nself-calibration).\n',
                    'note': 'The NI 4065 does not support self-calibration.',
                    'table_body': [
                        [
                            'NIDMM_VAL_INTERNAL_AREA (default)',
                            '0',
                            'Self-Calibration'
                        ],
                        [
                            'NIDMM_VAL_EXTERNAL_AREA',
                            '1',
                            'External Calibration'
                        ]
                    ]
                },
                'name': 'calType',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the **temperature** during the last calibration.'
                },
                'name': 'temperature',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetSelfCalSupported': {
        'documentation': {
            'description': '\nReturns a Boolean value that expresses whether or not the DMM that you\nare using can perform self-calibration.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns whether Self Cal is supported for the device specified by the\ngiven session.\n',
                    'table_body': [
                        [
                            'VI_TRUE',
                            '1',
                            'The DMM that you are using can perform self-calibration.'
                        ],
                        [
                            'VI_FALSE',
                            '0',
                            'The DMM that you are using cannot perform self-calibration.'
                        ]
                    ]
                },
                'name': 'selfCalSupported',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'ImportAttributeConfigurationBuffer': {
        'documentation': {
            'description': '\nImports an attribute configuration to the session from the specified\nconfiguration buffer.\n\nYou can export and import session attribute configurations only between\ndevices with identical model numbers.\n\n**Coercion Behavior for Certain Devices**\n\nImported and exported attribute configurations contain coerced values\nfor the following NI‑DMM devices:\n\n-  PXI/PCI/PCIe/USB‑4065\n-  PXI/PCI‑4070\n-  PXI‑4071\n-  PXI‑4072\n\nNI‑DMM coerces attribute values when the value you set is within the\nallowed range for the attribute but is not one of the discrete valid\nvalues the attribute supports. For example, for an attribute that\ncoerces values up, if you choose a value of 4 when the adjacent valid\nvalues are 1 and 10, the attribute coerces the value to 10.\n\n**Related Topics:**\n\n`Using Attributes and Properties with\nNI‑DMM <REPLACE_DRIVER_SPECIFIC_URL_1(attributes)>`__\n\n`Setting Attributes Before Reading\nAttributes <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__\n',
            'note': 'Not supported on the PCMCIA‑4050 or the PXI/PCI‑4060.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the size, in bytes, of the byte array to import. If you enter\n0, this function returns the needed size.\n'
                },
                'name': 'size',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the byte array buffer that contains the attribute\nconfiguration to import.\n'
                },
                'name': 'configuration',
                'python_api_converter_name': 'convert_to_bytes',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'ViInt8[]',
                'type_in_documentation': 'bytes'
            }
        ],
        'returns': 'ViStatus'
    },
    'ImportAttributeConfigurationFile': {
        'documentation': {
            'description': "\nImports an attribute configuration to the session from the specified\nfile.\n\nYou can export and import session attribute configurations only between\ndevices with identical model numbers.\n\n**Coercion Behavior for Certain Devices**\n\nImported and exported attribute configurations contain coerced values\nfor the following NI‑DMM devices:\n\n-  PXI/PCI/PCIe/USB‑4065\n-  PXI/PCI‑4070\n-  PXI‑4071\n-  PXI‑4072\n\nNI‑DMM coerces attribute values when the value you set is within the\nallowed range for the attribute but is not one of the discrete valid\nvalues the attribute supports. For example, for an attribute that\ncoerces values up, if you choose a value of 4 when the adjacent valid\nvalues are 1 and 10, the attribute coerces the value to 10.\n\n**Related Topics:**\n\n`Using Attributes and Properties with\nNI‑DMM <REPLACE_DRIVER_SPECIFIC_URL_1(attributes)>`__\n\n`Setting Attributes Before Reading\nAttributes <javascript:LaunchHelp('DMM.chm::/setting_before_reading_attributes')>`__\n",
            'note': 'Not supported on the PCMCIA‑4050 or the PXI/PCI‑4060.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the absolute path to the file containing the attribute\nconfiguration to import. If you specify an empty or relative path, this\nfunction returns an error.\n**Default File Extension:**\\  .nidmmconfig\n'
                },
                'name': 'filePath',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'InitWithOptions': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nThis function completes the following tasks:\n\n-  Creates a new IVI instrument driver session and, optionally, sets the\n   initial state of the following session attributes:\n   NIDMM_ATTR_RANGE_CHECK, NIDMM_ATTR_QUERY_INSTR_STATUS,\n   NIDMM_ATTR_CACHE, NIDMM_ATTR_SIMULATE,\n   NIDMM_ATTR_RECORD_COERCIONS.\n-  Opens a session to the device you specify for the **Resource_Name**\n   parameter. If the **ID_Query** parameter is set to VI_TRUE, this\n   function queries the instrument ID and checks that it is valid for\n   this instrument driver.\n-  If the **Reset_Device** parameter is set to VI_TRUE, this function\n   resets the instrument to a known state. Sends initialization commands\n   to set the instrument to the state necessary for the operation of the\n   instrument driver.\n-  Returns a ViSession handle that you use to identify the instrument in\n   all subsequent instrument driver function calls.\n'
        },
        'method_name_for_documentation': '__init__',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'caution': '\nAll IVI names for the **Resource_Name**, such as logical names or\nvirtual names, are case-sensitive. If you use logical names, driver\nsession names, or virtual names in your program, you must make sure that\nthe name you use matches the name in the IVI Configuration Store file\nexactly, without any variations in the case of the characters in the\nname.\n',
                    'description': '\n| Contains the **resource_name** of the device to initialize. The\n  **resource_name** is assigned in Measurement & Automation Explorer\n  (MAX). Refer to `Related\n  Documentation <REPLACE_DRIVER_SPECIFIC_URL_1(related_documentation)>`__\n  for the *NI Digital Multimeters Getting Started Guide* for more\n  information about configuring and testing the DMM in MAX.\n| Valid Syntax:\n\n-  NI-DAQmx name\n-  DAQ::NI-DAQmx name[::INSTR]\n-  DAQ::Traditional NI-DAQ device number[::INSTR]\n-  IVI logical name\n'
                },
                'name': 'resourceName',
                'type': 'ViString'
            },
            {
                'default_value': False,
                'direction': 'in',
                'documentation': {
                    'description': '\nVerifies that the device you initialize is one that the driver supports.\nNI-DMM automatically performs this query, so setting this parameter is\nnot necessary.\nDefined Values:\n',
                    'table_body': [
                        [
                            'VI_TRUE (default)',
                            '1',
                            'Perform ID Query'
                        ],
                        [
                            'VI_FALSE',
                            '0',
                            'Skip ID Query'
                        ]
                    ]
                },
                'name': 'idQuery',
                'type': 'ViBoolean',
                'use_in_python_api': False
            },
            {
                'default_value': False,
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies whether to reset the instrument during the initialization\nprocedure.\nDefined Values:\n',
                    'table_body': [
                        [
                            'VI_TRUE (default)',
                            '1',
                            'Reset Device'
                        ],
                        [
                            'VI_FALSE',
                            '0',
                            "Don't Reset"
                        ]
                    ]
                },
                'name': 'resetDevice',
                'type': 'ViBoolean'
            },
            {
                'default_value': '""',
                'direction': 'in',
                'documentation': {
                    'description': '\n| Sets the initial value of certain attributes for the session. The\n  following table specifies the attribute name, attribute constant, and\n  default value for each attribute that you can use in this parameter:\n\nThe format of this string is, "AttributeName=Value." To set multiple\nattributes, separate their assignments with a comma.\n\nIf you pass NULL or an empty string for this parameter, the session uses\nthe default values for the attributes. You can override the default\nvalues by assigning a value explicitly in an **option_string**\nparameter. You do not have to specify all of the attributes and may\nleave any of them out (those left out use the default value).\n\nRefer to `Simulating NI Digital\nMultimeters <REPLACE_DRIVER_SPECIFIC_URL_1(simulation)>`__ for more\ninformation.\n',
                    'table_body': [
                        [
                            'Check',
                            'NIDMM_ATTR_RANGE_CHECK',
                            'VI_TRUE',
                            '1'
                        ],
                        [
                            'QueryInstrStatus',
                            'NIDMM_ATTR_QUERY_INSTR_STATUS',
                            'VI_FALSE',
                            '0'
                        ],
                        [
                            'Cache',
                            'NIDMM_ATTR_CACHE',
                            'VI_TRUE',
                            '1'
                        ],
                        [
                            'Simulate',
                            'NIDMM_ATTR_SIMULATE',
                            'VI_FALSE',
                            '0'
                        ],
                        [
                            'RecordCoercions',
                            'NIDMM_ATTR_RECORD_COERCIONS',
                            'VI_FALSE',
                            '0'
                        ],
                        [
                            'DriverSetup',
                            'NIDMM_ATTR_DRIVER_SETUP',
                            '"" (empty string)',
                            '""'
                        ]
                    ]
                },
                'name': 'optionString',
                'python_api_converter_name': 'convert_init_with_options_dictionary',
                'type': 'ViString',
                'type_in_documentation': 'dict'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns a ViSession handle that you use to identify the instrument in\nall subsequent instrument driver function calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'Initiate': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nInitiates an acquisition. After you call this function, the DMM leaves\nthe Idle state and enters the Wait-for-Trigger state. If trigger is set\nto Immediate mode, the DMM begins acquiring measurement data. Use\nniDMM_Fetch, niDMM_FetchMultiPoint, or niDMM_FetchWaveform to\nretrieve the measurement data.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'LockSession': {
        'documentation': {
            'description': '\nThis function obtains a multithread lock on the instrument session.\nBefore it does so, it waits until all other execution threads have\nreleased their locks on the instrument session.\n\nOther threads might have obtained a lock on this session in the\nfollowing ways:\n\n-  The user application called this function.\n-  A call to the instrument driver locked the session.\n-  A call to the IVI Library locked the session.\n\nAfter your call to this function returns successfully, no other threads\ncan access the instrument session until you call niDMM_UnlockSession.\n\nUse this function and niDMM_UnlockSession around a sequence of calls to\ninstrument driver functions if you require that the instrument retain\nits settings through the end of the sequence. You can safely make nested\ncalls to this function within the same thread.\n\nTo completely unlock the session, you must balance each call to this\nfunction with a call to niDMM_UnlockSession. If, however, you use the\n**Caller_Has_Lock** parameter in all calls to this function and\nniDMM_UnlockSession within a function, the IVI Library locks the\nsession only once within the function regardless of the number of calls\nyou make to this function. This feature allows you to call\nniDMM_UnlockSession just once at the end of the function.\n'
        },
        'method_templates': [
            {
                'documentation_filename': 'lock',
                'method_python_name_suffix': '',
                'session_filename': 'lock'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThis parameter serves as a convenience. If you do not want to use this\nparameter, pass VI_NULL. Use this parameter in complex functions to\nkeep track of whether you obtain a lock and, therefore, need to unlock\nthe session. To use this parameter, complete the following steps:\n\n#. Pass the address of a local ViBoolean variable.\n#. In the declaration of the local variable, initialize it to VI_FALSE\n   (0).\n#. Pass the address of the same local variable to any other calls you\n   make to this function or niDMM_UnlockSession in the same function.\n\nThe parameter is an input/output parameter. This function and\nniDMM_UnlockSession each inspect the current value and take the\nfollowing actions:\n\nIf the value is VI_TRUE (1), this function does not lock the session\nagain. If the value is VI_FALSE, this function obtains the lock and\nsets the value of the parameter to VI_TRUE.\n\nIf the value is VI_FALSE, niDMM_UnlockSession does not attempt to\nunlock the session. If the value is VI_TRUE, niDMM_UnlockSession\nreleases the lock and sets the value of the parameter to VI_FALSE.\nThus, you can, call niDMM_UnlockSession at the end of your function\nwithout worrying about whether you actually have the lock.\n\n**Example**\n\nViStatus TestFunc (ViSession vi, ViInt32 flags)\n\n{\n\n| ViStatus error = VI_SUCCESS;\n| ViBoolean haveLock = VI_FALSE;\n| if (flags & BIT_1)\n\n| {\n| viCheckErr( NIDMM_LockSession(vi, &haveLock;));\n| viCheckErr( TakeAction1(vi));\n| if (flags & BIT_2)\n\n{\n\nviCheckErr( NIDMM_UnlockSession(vi, &haveLock;));\n\nviCheckErr( TakeAction2(vi));\n\nviCheckErr( NIDMM_LockSession(vi, &haveLock;);\n\n}\n\nif (flags & BIT_3)\n\nviCheckErr( TakeAction3(vi));\n\n}\n\nError:\n\n/\\*\n\nAt this point, you cannot really be sure that you have the lock.\nFortunately, the haveLock variable takes care of that for you.\n\n\\*/\n\nniDMM_UnlockSession(vi, &haveLock;);\n\nreturn error;\n\n}\n'
                },
                'name': 'callerHasLock',
                'type': 'ViBoolean'
            }
        ],
        'python_name': 'lock',
        'render_in_session_base': True,
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'PerformOpenCableComp': {
        'documentation': {
            'description': '\nFor the NI 4082 and NI 4072 only, performs the open cable compensation\nmeasurements for the current capacitance/inductance range, and returns\nopen cable compensation **Conductance** and **Susceptance** values. You\ncan use the return values of this function as inputs to\nniDMM_ConfigureOpenCableCompValues.\n\nThis function returns an error if the value of the NIDMM_ATTR_FUNCTION\nattribute is not set to NIDMM_VAL_CAPACITANCE (1005) or\nNIDMM_VAL_INDUCTANCE (1006).\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\n**conductance** is the measured value of open cable compensation\n**conductance**.\n'
                },
                'name': 'conductance',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\n**susceptance** is the measured value of open cable compensation\n**susceptance**.\n'
                },
                'name': 'susceptance',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'PerformShortCableComp': {
        'documentation': {
            'description': '\nPerforms the short cable compensation measurements for the current\ncapacitance/inductance range, and returns short cable compensation\n**Resistance** and **Reactance** values. You can use the return values\nof this function as inputs to niDMM_ConfigureShortCableCompValues.\n\nThis function returns an error if the value of the NIDMM_ATTR_FUNCTION\nattribute is not set to NIDMM_VAL_CAPACITANCE (1005) or\nNIDMM_VAL_INDUCTANCE (1006).\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\n**resistance** is the measured value of short cable compensation\n**resistance**.\n'
                },
                'name': 'resistance',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\n**reactance** is the measured value of short cable compensation\n**reactance**.\n'
                },
                'name': 'reactance',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'Read': {
        'documentation': {
            'description': 'Acquires a single measurement and returns the measured value.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': 'hightime.timedelta(milliseconds=-1)',
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **maximum_time** allowed for this function to complete in\nmilliseconds. If the function does not complete within this time\ninterval, the function returns the NIDMM_ERROR_MAX_TIME_EXCEEDED\nerror code. This may happen if an external trigger has not been\nreceived, or if the specified timeout is not long enough for the\nacquisition to complete.\n\nThe valid range is 0–86400000. The default value is\nNIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout\nautomatically.\n'
                },
                'name': 'maximumTime',
                'python_api_converter_name': 'convert_timedelta_to_milliseconds_int32',
                'type': 'ViInt32',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or int in milliseconds'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The measured value returned from the DMM.'
                },
                'name': 'reading',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadMultiPoint': {
        'documentation': {
            'description': '\nAcquires multiple measurements and returns an array of measured values.\nThe number of measurements the DMM makes is determined by the values you\nspecify for the **Trigger_Count** and **Sample_Count** parameters in\nniDMM_ConfigureMultiPoint.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': 'hightime.timedelta(milliseconds=-1)',
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **maximum_time** allowed for this function to complete in\nmilliseconds. If the function does not complete within this time\ninterval, the function returns the NIDMM_ERROR_MAX_TIME_EXCEEDED\nerror code. This may happen if an external trigger has not been\nreceived, or if the specified timeout is not long enough for the\nacquisition to complete.\n\nThe valid range is 0–86400000. The default value is\nNIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout\nautomatically.\n'
                },
                'name': 'maximumTime',
                'python_api_converter_name': 'convert_timedelta_to_milliseconds_int32',
                'type': 'ViInt32',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or int in milliseconds'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of measurements to acquire. The maximum number of\nmeasurements for a finite acquisition is the (**Trigger Count** x\n**Sample Count**) parameters in niDMM_ConfigureMultiPoint.\n\nFor continuous acquisitions, up to 100,000 points can be returned at\nonce. The number of measurements can be a subset. The valid range is any\npositive ViInt32. The default value is 1.\n'
                },
                'name': 'arraySize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'An array of measurement values.',
                    'note': '\nThe size of the **Reading_Array** must be at least the size that you\nspecify for the **Array_Size** parameter.\n'
                },
                'name': 'readingArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arraySize'
                },
                'type': 'ViReal64[]',
                'use_array': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the number of measured values actually retrieved from the DMM.'
                },
                'name': 'actualNumberOfPoints',
                'type': 'ViInt32',
                'use_in_python_api': False
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadStatus': {
        'documentation': {
            'description': '\nReturns measurement backlog and acquisition status. Use this function to\ndetermine how many measurements are available before calling\nniDMM_Fetch, niDMM_FetchMultiPoint, or niDMM_FetchWaveform.\n',
            'note': 'The NI 4050 is not supported.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe number of measurements available to be read. If the backlog\ncontinues to increase, data is eventually overwritten, resulting in an\nerror.\n',
                    'note': '\nOn the NI 4060, the **Backlog** does not increase when autoranging. On\nthe NI 4065, the **Backlog** does not increase when Range is set to AUTO\nRANGE ON (-1), or before the first point is fetched when Range is set to\nAUTO RANGE ONCE (-3). These behaviors are due to the autorange model of\nthe devices.\n'
                },
                'name': 'acquisitionBacklog',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nIndicates status of the acquisition. The following table shows the\nacquisition states:\n',
                    'table_body': [
                        [
                            '0',
                            'Running'
                        ],
                        [
                            '1',
                            'Finished with backlog'
                        ],
                        [
                            '2',
                            'Finished with no backlog'
                        ],
                        [
                            '3',
                            'Paused'
                        ],
                        [
                            '4',
                            'No acquisition in progress'
                        ]
                    ]
                },
                'enum': 'AcquisitionStatus',
                'name': 'acquisitionStatus',
                'type': 'ViInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadWaveform': {
        'documentation': {
            'description': '\nFor the NI 4080/4081/4082 and the NI 4070/4071/4072, acquires a waveform\nand returns data as an array of values or as a waveform data type. The\nnumber of elements in the **Waveform_Array** is determined by the\nvalues you specify for the **Waveform_Points** parameter in\nniDMM_ConfigureWaveformAcquisition.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': 'hightime.timedelta(milliseconds=-1)',
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **maximum_time** allowed for this function to complete in\nmilliseconds. If the function does not complete within this time\ninterval, the function returns the NIDMM_ERROR_MAX_TIME_EXCEEDED\nerror code. This may happen if an external trigger has not been\nreceived, or if the specified timeout is not long enough for the\nacquisition to complete.\n\nThe valid range is 0–86400000. The default value is\nNIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout\nautomatically.\n'
                },
                'name': 'maximumTime',
                'python_api_converter_name': 'convert_timedelta_to_milliseconds_int32',
                'type': 'ViInt32',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or int in milliseconds'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of waveform points to return. You specify the total\nnumber of points that the DMM acquires in the **Waveform Points**\nparameter of niDMM_ConfigureWaveformAcquisition. The default value is\n1.\n'
                },
                'name': 'arraySize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'An array of measurement values.',
                    'note': '\nThe size of the **Waveform_Array** must be at least the size that you\nspecify for the **Array_Size** parameter.\n'
                },
                'name': 'waveformArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arraySize'
                },
                'type': 'ViReal64[]',
                'use_array': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the number of measured values actually retrieved from the DMM.'
                },
                'name': 'actualNumberOfPoints',
                'type': 'ViInt32',
                'use_in_python_api': False
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetWithDefaults': {
        'documentation': {
            'description': '\nResets the instrument to a known state and sends initialization commands\nto the DMM. The initialization commands set the DMM settings to the\nstate necessary for the operation of NI-DMM. All user-defined default\nvalues associated with a logical name are applied after setting the DMM.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'SelfCal': {
        'documentation': {
            'description': '\nFor the NI 4080/4081/4082 and the NI 4070/4071/4072, executes the\nself-calibration routine to maintain measurement accuracy.\n',
            'note': '\nThis function calls niDMM_reset, and any configurations previous to\nthe call will be lost. All attributes will be set to their default\nvalues after the call returns.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'SendSoftwareTrigger': {
        'documentation': {
            'description': '\nSends a command to trigger the DMM. Call this function if you have\nconfigured either the NIDMM_ATTR_TRIGGER_SOURCE or\nNIDMM_ATTR_SAMPLE_TRIGGER attributes. If the\nNIDMM_ATTR_TRIGGER_SOURCE and/or NIDMM_ATTR_SAMPLE_TRIGGER\nattributes are set to NIDMM_VAL_EXTERNAL or NIDMM_VAL_TTL\\ *n*, you\ncan use this function to override the trigger source that you configured\nand trigger the device. The NI 4050 and NI 4060 are not supported.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViBoolean': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nThis function sets the value of a ViBoolean attribute.\n\nThis is a low-level function that you can use to set the values of\ninstrument-specific attributes and inherent IVI attributes.\n\nIf the attribute represents an instrument state, this function performs\ninstrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled, and the currently cached value is invalid\n   or is different than the value you specify.\n\nThis instrument driver contains high-level functions that set most of\nthe instrument attributes. It is best to use the high-level driver\nfunctions as much as possible. They handle order dependencies and\nmultithread locking for you. In addition, they perform status checking\nonly after setting all of the attributes.\n\nIn contrast, when you set multiple attributes using the SetAttribute\nfunctions, the functions check the instrument status after each call.\nAlso, when state caching is enabled, the high-level functions that\nconfigure multiple attributes perform instrument I/O only for the\nattributes whose value you change. Thus, you can safely call the\nhigh-level functions without the penalty of redundant instrument I/O.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis parameter is ignored. NI DMMs do not support\nchannel names since they only have a single channel. This parameter is\nincluded in order to support interchangeability and upgradability to\nmultiple channel DMMs.\n\nThe default value is " " (an empty string).\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value that you want to set the attribute to.'
                },
                'name': 'attributeValue',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViInt32': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nThis function sets the value of a ViInt32 attribute.\n\nThis is a low-level function that you can use to set the values of\ninstrument-specific attributes and inherent IVI attributes.\n\nIf the attribute represents an instrument state, this function performs\ninstrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled, and the currently cached value is invalid\n   or is different than the value you specify.\n\nThis instrument driver contains high-level functions that set most of\nthe instrument attributes. It is best to use the high-level driver\nfunctions as much as possible. They handle order dependencies and\nmultithread locking for you. In addition, they perform status checking\nonly after setting all of the attributes.\n\nIn contrast, when you set multiple attributes using the SetAttribute\nfunctions, the functions check the instrument status after each call.\nAlso, when state caching is enabled, the high-level functions that\nconfigure multiple attributes perform instrument I/O only for the\nattributes whose value you change. Thus, you can safely call the\nhigh-level functions without the penalty of redundant instrument I/O.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis parameter is ignored. NI DMMs do not support\nchannel names since they only have a single channel. This parameter is\nincluded in order to support interchangeability and upgradability to\nmultiple channel DMMs.\n\nThe default value is " " (an empty string).\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value that you want to set the attribute to.'
                },
                'name': 'attributeValue',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViReal64': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nThis function sets the value of a ViReal64 attribute.\n\nThis is a low-level function that you can use to set the values of\ninstrument-specific attributes and inherent IVI attributes.\n\nIf the attribute represents an instrument state, this function performs\ninstrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled, and the currently cached value is invalid\n   or is different than the value you specify.\n\nThis instrument driver contains high-level functions that set most of\nthe instrument attributes. It is best to use the high-level driver\nfunctions as much as possible. They handle order dependencies and\nmultithread locking for you. In addition, they perform status checking\nonly after setting all of the attributes.\n\nIn contrast, when you set multiple attributes using the SetAttribute\nfunctions, the functions check the instrument status after each call.\nAlso, when state caching is enabled, the high-level functions that\nconfigure multiple attributes perform instrument I/O only for the\nattributes whose value you change. Thus, you can safely call the\nhigh-level functions without the penalty of redundant instrument I/O.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis parameter is ignored. NI DMMs do not support\nchannel names since they only have a single channel. This parameter is\nincluded in order to support interchangeability and upgradability to\nmultiple channel DMMs.\n\nThe default value is " " (an empty string).\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value that you want to set the attribute to.'
                },
                'name': 'attributeValue',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViString': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nThis function sets the value of a ViString attribute.\n\nThis is a low-level function that you can use to set the values of\ninstrument-specific attributes and inherent IVI attributes.\n\nIf the attribute represents an instrument state, this function performs\ninstrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled, and the currently cached value is invalid\n   or is different than the value you specify.\n\nThis instrument driver contains high-level functions that set most of\nthe instrument attributes. It is best to use the high-level driver\nfunctions as much as possible. They handle order dependencies and\nmultithread locking for you. In addition, they perform status checking\nonly after setting all of the attributes.\n\nIn contrast, when you set multiple attributes using the SetAttribute\nfunctions, the functions check the instrument status after each call.\nAlso, when state caching is enabled, the high-level functions that\nconfigure multiple attributes perform instrument I/O only for the\nattributes whose value you change. Thus, you can safely call the\nhigh-level functions without the penalty of redundant instrument I/O.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis parameter is ignored. NI DMMs do not support\nchannel names since they only have a single channel. This parameter is\nincluded in order to support interchangeability and upgradability to\nmultiple channel DMMs.\n\nThe default value is " " (an empty string).\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value that you want to set the attribute to.'
                },
                'name': 'attributeValue',
                'type': 'ViString'
            }
        ],
        'returns': 'ViStatus'
    },
    'UnlockSession': {
        'documentation': {
            'description': '\nThis function releases a lock that you acquired on an instrument session\nusing niDMM_LockSession. Refer to niDMM_LockSession for additional\ninformation on session locks.\n'
        },
        'method_templates': [
            {
                'documentation_filename': 'unlock',
                'method_python_name_suffix': '',
                'session_filename': 'unlock'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThis parameter serves as a convenience. If you do not want to use this\nparameter, pass VI_NULL.\n\nUse this parameter in complex functions to keep track of whether you\nobtain a lock and, therefore, need to unlock the session.\n\nTo use this parameter, complete the following steps:\n\n#. Pass the address of a local ViBoolean variable.\n#. In the declaration of the local variable, initialize it to VI_FALSE\n   (0).\n#. Pass the address of the same local variable to any other calls you\n   make to niDMM_LockSession or this function in the same function.\n\nThe parameter is an input/output parameter. niDMM_LockSession and this\nfunction each inspect the current value and take the following actions:\n\nIf the value is VI_TRUE (1), niDMM_LockSession does not lock the\nsession again. If the value is VI_FALSE, niDMM_LockSession obtains the\nlock and sets the value of the parameter to VI_TRUE.\n\nIf the value is VI_FALSE, this function does not attempt to unlock the\nsession. If the value is VI_TRUE, this function releases the lock and\nsets the value of the parameter to VI_FALSE. Thus, you can, call this\nfunction at the end of your function without worrying about whether you\nactually have the lock.\n\n**Example**\n\nViStatus TestFunc (ViSession vi, ViInt32 flags)\n\n{\n\nViStatus error = VI_SUCCESS;\n\nViBoolean haveLock = VI_FALSE;\n\nif (flags & BIT_1)\n\n{\n\nviCheckErr( NIDMM_LockSession(vi, &haveLock;));\n\nviCheckErr( TakeAction1(vi));\n\nif (flags & BIT_2)\n\n{\n\nviCheckErr( NIDMM_UnlockSession(vi, &haveLock;));\n\nviCheckErr( TakeAction2(vi));\n\nviCheckErr( NIDMM_LockSession(vi, &haveLock;);\n\n}\n\nif (flags & BIT_3)\n\nviCheckErr( TakeAction3(vi));\n\n}\n\nError:\n\n/\\*\n\nAt this point, you cannot really be sure that you have the lock.\nFortunately, the haveLock variable takes care of that for you.\n\n\\*/\n\nniDMM_UnlockSession(vi, &haveLock;);\n\nreturn error;\n\n}\n'
                },
                'name': 'callerHasLock',
                'type': 'ViBoolean'
            }
        ],
        'python_name': 'unlock',
        'render_in_session_base': True,
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'close': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Closes the specified session and deallocates resources that it reserved.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'python_name': '_close',
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'error_message': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nTakes the **Error_Code** returned by the instrument driver functions,\ninterprets it, and returns it as a user-readable string.\n'
        },
        'is_error_handling': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe **error_code** returned from the instrument. The default is 0,\nindicating VI_SUCCESS.\n'
                },
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The error information formatted into a string.'
                },
                'name': 'errorMessage',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'fancy_self_test': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': '\nPerforms a self-test on the DMM to ensure that the DMM is functioning\nproperly. Self-test does not calibrate the DMM. Zero\nindicates success. \n\nOn the NI 4080/4082 and NI 4070/4072, the error code 1013 indicates that\nyou should check the fuse and replace it, if necessary.\n\nRaises `SelfTestError` on self test failure. Attributes on exception object:\n\n- code - failure code from driver\n- message - status message from driver\n',
            'note': [
                'Self-test does not check the fuse on the NI 4065, NI 4071, and NI 4081. Hence, even if the fuse is blown on the device, self-test does not return error code 1013.',
                'This function calls niDMM_reset, and any configurations previous to the call will be lost. All attributes will be set to their default values after the call returns.'
            ]
        },
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_self_test'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. You obtain the **vi** parameter from niDMM_init or niDMM_InitWithOptions.'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'python_name': 'self_test',
        'returns': 'ViStatus'
    },
    'reset': {
        'documentation': {
            'description': '\nResets the instrument to a known state and sends initialization commands\nto the instrument. The initialization commands set instrument settings\nto the state necessary for the operation of the instrument driver.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'self_test': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nPerforms a self-test on the DMM to ensure that the DMM is functioning\nproperly. Self-test does not calibrate the DMM.\n',
            'note': '\nThis function calls niDMM_reset, and any configurations previous to\nthe call will be lost. All attributes will be set to their default\nvalues after the call returns.\n'
        },
        'method_name_for_documentation': 'self_test',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nContains the value returned from the instrument self-test. Zero\nindicates success.\n\nOn the NI 4080/4082 and NI 4070/4072, the error code 1013 indicates that\nyou should check the fuse and replace it, if necessary.\n',
                    'note': '\nSelf-test does not check the fuse on the NI 4065, NI 4071, and\nNI 4081. Hence, even if the fuse is blown on the device, self-test does\nnot return error code 1013.\n'
                },
                'name': 'selfTestResult',
                'type': 'ViInt16'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThis parameter contains the string returned from the instrument\nself-test. The array must contain at least 256 elements.\n\nFor the NI 4050 and NI 4060, the error codes returned for self-test\nfailures include the following:\n\n-  NIDMM_ERROR_AC_TEST_FAILURE\n-  NIDMM_ERROR_DC_TEST_FAILURE\n-  NIDMM_ERROR_RESISTANCE_TEST_FAILURE\n\nThese error codes indicate that the DMM should be repaired.\n\nFor the NI 4080/4081/4082 and the NI 4070/4071/4072, the error code\nreturned for a self-test failure is NIDMM_ERROR_SELF_TEST_FAILURE.\nThis error code indicates that the DMM should be repaired.\n'
                },
                'name': 'selfTestMessage',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    }
}
