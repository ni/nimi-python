# -*- coding: utf-8 -*-
# This file is generated from NI-RFSG API metadata version 25.5.0d9999
attributes = {
    1050002: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies whether to validate attribute values and function parameters. Range checking parameters is very useful for debugging. After you validate your program, set this attribute to VI_FALSE to disable range checking and maximize performance. NI-RFSG can choose to ignore range checking for particular attributes, regardless of the setting of this attribute. Use the nirfsg_InitWithOptions function to override the default value.\n\n                **Default Value:** VI_TRUE\n\n                **Supported Devices:** PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n            \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'VI_TRUE',
                    'Enable range checking.'
                ],
                [
                    'VI_FALSE',
                    'Disable range checking.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'lv_property': 'Inherent IVI Attributes:User Options:Range Check',
        'name': 'RANGE_CHECK',
        'type': 'ViBoolean'
    },
    1050003: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies whether NI-RFSG queries the NI-RFSG device status after each operation. Querying the device status is useful for debugging. After you validate your program, set this attribute to VI_FALSE to disable status checking and maximize performance.\n\n                NI-RFSG can choose to ignore status checking for particular attributes, regardless of the setting of this attribute. Use the nirfsg_InitWithOptions function to override the default value.\n\n                **Default Value:** VI_FALSE\n\n                **Supported Devices:** PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n            \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'VI_TRUE',
                    'NI-RFSG queries the instrument status after each operation.'
                ],
                [
                    'VI_FALSE',
                    'NI-RFSG does not query the instrument status.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'lv_property': 'Inherent IVI Attributes:User Options:Query Instrument Status',
        'name': 'QUERY_INSTRUMENT_STATUS',
        'type': 'ViBoolean'
    },
    1050004: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies whether to cache the value of attributes. When caching is enabled, NI-RFSG tracks the current NI-RFSG device settings and avoids sending redundant commands to the device. NI-RFSG can always cache or never cache particular attributes, regardless of the setting of this attribute. Call the nirfsg_InitWithOptions function to override the default value.\n\n                **Default Value:** VI_TRUE\n\n                **Supported Devices:** PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'VI_TRUE',
                    'Enables caching.'
                ],
                [
                    'VI_FALSE',
                    'Disables caching.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'lv_property': 'Inherent IVI Attributes:User Options:Cache',
        'name': 'CACHE',
        'type': 'ViBoolean'
    },
    1050005: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns whether NI-RFSG simulates I/O operations. This attribute is useful for debugging applications without using hardware. After a session is opened, you cannot change the simulation state. Use the nirfsg_InitWithOptions function to enable simulation.\n\n                **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n            \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'VI_TRUE',
                    'Simulation is enabled.'
                ],
                [
                    'VI_FALSE',
                    'Simulation is disabled.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'lv_property': 'Inherent IVI Attributes:User Options:Simulate',
        'name': 'SIMULATE',
        'type': 'ViBoolean'
    },
    1050006: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies whether the IVI engine keeps a list of the value coercions it makes for integer and real type attributes.\n\n                **Default Value:** VI_FALSE\n\n                **Supported Devices:** PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n            \n            **Defined Values**:\n            ',
            'note': 'Enabling record value coercions is not supported.',
            'table_body': [
                [
                    'VI_TRUE',
                    'The IVI engine keeps a list of coercions.'
                ],
                [
                    'VI_FALSE',
                    'The IVI engine does not keep a list of coercions.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'lv_property': 'Inherent IVI Attributes:User Options:Record Value Coercions',
        'name': 'RECORD_COERCIONS',
        'type': 'ViBoolean'
    },
    1050021: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies whether to perform interchangeability checking and retrieve interchangeability warnings.\n\n                **Default Value:** VI_FALSE\n\n                **Supported Devices:** PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n            **Defined Values**:\n            ',
            'note': 'Enabling interchangeability check is not supported.',
            'table_body': [
                [
                    'VI_TRUE',
                    'Interchange check is enabled.'
                ],
                [
                    'VI_FALSE',
                    'Interchange check is disabled.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'lv_property': 'Inherent IVI Attributes:User Options:Interchange Check',
        'name': 'INTERCHANGE_CHECK',
        'type': 'ViBoolean'
    },
    1050302: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns a string that contains the prefix for NI-RFSG. The name of each user-callable function in NI-RFSG starts with this prefix. This attribute returns\n\n                niRFSG.\n\n                **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n                '
        },
        'lv_property': 'Inherent IVI Attributes:Driver Identification:Driver Prefix',
        'name': 'SPECIFIC_DRIVER_PREFIX',
        'type': 'ViString'
    },
    1050304: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns a string that contains the resource name NI-RFSG uses to identify the physical device. If you initialize NI-RFSG with a logical name, this attribute contains the resource name that corresponds to the entry in the IVI Configuration Utility. If you initialize NI-RFSG with the resource name, this attribute contains that value.\n\n                **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n                '
        },
        'lv_property': 'Inherent IVI Attributes:Advanced Session Information:Resource Descriptor',
        'name': 'IO_RESOURCE_DESCRIPTOR',
        'type': 'ViString'
    },
    1050305: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns a string that contains the logical name you specified when opening the current IVI session. You can pass a logical name to the nirfsg_Init function or the nirfsg_InitWithOptions function. The IVI Configuration Utility must contain an entry for the logical name. The logical name entry refers to a driver session section in the IVI Configuration file. The driver session section specifies a physical device and initial user options.\n\n                **Supported Devices:** PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n                '
        },
        'lv_property': 'Inherent IVI Attributes:Advanced Session Information:Logical Name',
        'name': 'LOGICAL_NAME',
        'type': 'ViString'
    },
    1050327: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns a string that contains a model code of the NI-RFSG device. For drivers that support more than one device, this attribute contains a comma-separated list of supported devices.\n\n                **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n                '
        },
        'lv_property': 'Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models',
        'name': 'SUPPORTED_INSTRUMENT_MODELS',
        'type': 'ViString'
    },
    1050401: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns a string that contains a comma-separated list of class-extension groups that NI-RFSG implements.\n\n                **Supported Devices:** PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n                '
        },
        'lv_property': 'Inherent IVI Attributes:Driver Capabilities:Class Group Capabilities',
        'name': 'GROUP_CAPABILITIES',
        'type': 'ViString'
    },
    1050510: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns a string that contains the firmware revision information for the NI-RFSG device you are currently using.\n\n                **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n                \n                **High-Level Functions**:\n\n                - nirfsg_RevisionQuery'
        },
        'lv_property': 'Inherent IVI Attributes:Instrument Identification:Firmware Revision',
        'name': 'INSTRUMENT_FIRMWARE_REVISION',
        'type': 'ViString'
    },
    1050511: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns a string that contains the name of the manufacturer of the NI-RFSG device you are currently using.\n\n                **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n                '
        },
        'lv_property': 'Inherent IVI Attributes:Instrument Identification:Manufacturer',
        'name': 'INSTRUMENT_MANUFACTURER',
        'type': 'ViString'
    },
    1050512: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns a string that contains the model number or name of the NI-RFSG device that you are currently using. For drivers that support more than one device, this attribute returns a comma-separated list of supported devices.\n\n                **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n                '
        },
        'lv_property': 'Inherent IVI Attributes:Instrument Identification:Model',
        'name': 'INSTRUMENT_MODEL',
        'type': 'ViString'
    },
    1050513: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns a string that contains the name of the vendor that supplies NI-RFSG. This attribute returns\n\n                National Instruments.\n\n                **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n                '
        },
        'lv_property': 'Inherent IVI Attributes:Driver Identification:Driver Vendor',
        'name': 'SPECIFIC_DRIVER_VENDOR',
        'type': 'ViString'
    },
    1050514: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns a string that contains a brief description of NI-RFSG. This attribute returns\n\n                National Instruments RF Signal Generator Instrument Driver.\n\n                **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n                '
        },
        'lv_property': 'Inherent IVI Attributes:Driver Identification:Description',
        'name': 'SPECIFIC_DRIVER_DESCRIPTION',
        'type': 'ViString'
    },
    1050515: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns the major version number of the class specification with which NI-RFSG is compliant.\n\n                **Supported Devices:** PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n                '
        },
        'lv_property': 'Inherent IVI Attributes:Driver Identification:Class Specification Major Version',
        'name': 'SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION',
        'type': 'ViInt32'
    },
    1050516: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns the minor version number of the class specification with which NI-RFSG is compliant.\n\n                **Supported Devices:** PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n                '
        },
        'lv_property': 'Inherent IVI Attributes:Driver Identification:Class Specification Minor Version',
        'name': 'SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION',
        'type': 'ViInt32'
    },
    1050551: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns a string that contains additional version information about NI-RFSG. For example, NI-RFSG can return\n\n                Driver: NI-RFSG14.5.0, Compiler: MSVC9.00, Components: IVI Engine4.00, VISA-Spec4.00 as the value of this attribute.\n\n                **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n                '
        },
        'lv_property': 'Inherent IVI Attributes:Driver Identification:Revision',
        'name': 'SPECIFIC_DRIVER_REVISION',
        'type': 'ViString'
    },
    1150001: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the Reference Clock source. To set this attribute, the NI-RFSG device must be in the Configuration state. Only certain combinations of this attribute and the NIRFSG_ATTR_PXI_CHASSIS_CLK10_SOURCE attribute are valid, as shown in the following table.\n\n                **Default Value:** NIRFSG_VAL_ONBOARD_CLOCK_STR\n\n                **Supported Devices:** PXI-5610, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Timing Configurations <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/timing_configurations.html>`_\n                \n                **High-Level Functions**:\n\n                - nirfsg_ConfigureRefClock\n            \n            **Defined Values**:\n            ',
            'note': 'The PXI-5670/5671 and PXIe-5672 devices also allow you to drive the PXI 10 MHz backplane clock on PXI chassis *only* using the NIRFSG_ATTR_PXI_CHASSIS_CLK10_SOURCE attribute.',
            'table_body': [
                [
                    'NIRFSG_VAL_ONBOARD_CLOCK_STR',
                    'OnboardClock',
                    'Uses the onboard Reference Clock as the clock source. **PXIe-5830/5831** —For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For the PXIe-5831/5832, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. ** PXIe-5831/5832 with PXIe-5653** —Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. **PXIe-5841 with PXIe-5655** —Lock to the PXIe-5655 onboard clock. Connect the REF OUT connector on the PXIe-5655 to the PXIe-5841 REF IN connector.'
                ],
                [
                    'NIRFSG_VAL_CLK_IN_STR',
                    'ClkIn',
                    'Uses the clock signal present at the front panel CLK IN connector as the Reference Clock source. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5831 with PXIe-5653/5832/5832 with PXIe-5653/5840/5841/5841 with PXIe-5655.'
                ],
                [
                    'NIRFSG_VAL_REF_IN_STR',
                    'RefIn',
                    'Uses the clock signal present at the front panel REF IN connector as the Reference Clock source. **PXIe-5830/5831** —For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For the PXIe-5831/5832, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For the PXIe-5830, lock the external signal to the PXIe-3621 REF IN connector. For the PXIe-5831/5832, lock the external signal to the PXIe-3622 REF IN connector. **PXIe-5831/5832 with PXIe-5653** —Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector. **PXIe-5841 with PXIe-5655** —Lock to the signal at the REF IN connector on the associated PXIe-5655. Connect the PXIe-5655 REF OUT connector to the PXIe-5841 REF IN connector.'
                ],
                [
                    'NIRFSG_VAL_PXI_CLK_STR',
                    'PXI_CLK',
                    'Uses the PXI_CLK signal, which is present on the PXI backplane, as the Reference Clock source.'
                ],
                [
                    'NIRFSG_VAL_REF_IN_2_STR',
                    'RefIn2',
                    'This value is not valid on any supported devices.'
                ],
                [
                    'NIRFSG_VAL_PXI_CLK_MASTER_STR',
                    'PXI_ClkMaster',
                    'This value is valid on only the PXIe-5831/5832 with PXIe-5653. **PXIe-5831/5832 with PXIe-5653** —NI-RFSG configures the PXIe-5653 to export the Reference clock and configures the PXIe-5820 and PXIe-3622 to use NIRFSG_VAL_PXI_CLK_STR as the Reference Clock source. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'ReferenceClockSource',
        'lv_property': 'Clock:Reference Clock Source',
        'name': 'REF_CLOCK_SOURCE',
        'type': 'ViString'
    },
    1150002: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the source terminal for the Start Trigger. This attribute is used when the NIRFSG_ATTR_START_TRIGGER_TYPE attribute is set to digital edge. The NIRFSG_ATTR_DIGITAL_EDGE_START_TRIGGER_SOURCE attribute is not case-sensitive. To set the NIRFSG_ATTR_DIGITAL_EDGE_START_TRIGGER_SOURCE attribute, the NI-RFSG device must be in the Configuration state.\n\n                PXIe-5654/5654 with PXIe-5696: The Start Trigger is valid only with a timer-based list when RF list mode is enabled.\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_\n\n                `PFI Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pfi_lines.html>`_\n\n                `PXI Trigger Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_trigger.html>`_\n                \n                **High-Level Functions**:\n\n                - nirfsg_ConfigureDigitalEdgeStartTrigger\n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_PFI0_STR',
                    'PFI0',
                    'The trigger is received on PFI 0.'
                ],
                [
                    'NIRFSG_VAL_PFI1_STR',
                    'PFI1',
                    'The trigger is received on PFI 1.'
                ],
                [
                    'NIRFSG_VAL_PFI2_STR',
                    'PFI2',
                    'The trigger is received on PFI 2.'
                ],
                [
                    'NIRFSG_VAL_PFI3_STR',
                    'PFI3',
                    'The trigger is received on PFI 3.'
                ],
                [
                    'NIRFSG_VAL_PXI_STAR_STR',
                    'PXI_Star',
                    'The trigger is received on the PXI star trigger line. This value is not valid for the PXIe-5644/5645/5646.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG0_STR',
                    'PXI_Trig0',
                    'The trigger is received on PXI trigger line 0.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG1_STR',
                    'PXI_Trig1',
                    'The trigger is received on PXI trigger line 1.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG2_STR',
                    'PXI_Trig2',
                    'The trigger is received on PXI trigger line 2.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG3_STR',
                    'PXI_Trig3',
                    'The trigger is received on PXI trigger line 3.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG4_STR',
                    'PXI_Trig4',
                    'The trigger is received on PXI trigger line 4.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG5_STR',
                    'PXI_Trig5',
                    'The trigger is received on PXI trigger line 5.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG6_STR',
                    'PXI_Trig6',
                    'The trigger is received on PXI trigger line 6.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG7_STR',
                    'PXI_Trig7',
                    'The trigger is received on PXI trigger line 7.'
                ],
                [
                    'NIRFSG_VAL_PXIE_DSTARB_STR',
                    'PXIe_DStarB',
                    'The trigger is received on the PXI DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860.'
                ],
                [
                    'NIRFSG_VAL_TRIG_IN_STR',
                    'TrigIn',
                    'The trigger is received on the TRIG IN/OUT terminal. This value is valid on only the PXIe-5654/5654 with PXIe-5696.'
                ],
                [
                    'NIRFSG_VAL_DIO0_STR',
                    'DIO/PFI0',
                    'The trigger is received on PFI0 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO1_STR',
                    'DIO/PFI1',
                    'The trigger is received on PFI1 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO2_STR',
                    'DIO/PFI2',
                    'The trigger is received on PFI2 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO3_STR',
                    'DIO/PFI3',
                    'The trigger is received on PFI3 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO4_STR',
                    'DIO/PFI4',
                    'The trigger is received on PFI4 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO5_STR',
                    'DIO/PFI5',
                    'The trigger is received on PFI5 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO6_STR',
                    'DIO/PFI6',
                    'The trigger is received on PFI6 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO7_STR',
                    'DIO/PFI7',
                    'The trigger is received on PFI7 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_SYNC_SCRIPT_TRIGGER_STR',
                    'Sync_Script',
                    'The trigger is received on the Sync Script trigger line. This value is valid on only the PXIe-5644/5645/5646.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'StartTrigDigEdgeSource',
        'lv_property': 'Triggers:Start:Digital Edge:Source',
        'name': 'DIGITAL_EDGE_START_TRIGGER_SOURCE',
        'type': 'ViString'
    },
    1150003: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the destination terminal for exporting the Start Trigger. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                PXIe-5654/5654 with PXIe-5696: The Start Trigger is valid only with a timer-based list when RF list mode is enabled.\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_\n\n                `PFI Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pfi_lines.html>`_\n\n                `PXI Trigger Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_trigger.html>`_\n            \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_DO_NOT_EXPORT_STR',
                    '',
                    'The signal is not exported.'
                ],
                [
                    'NIRFSG_VAL_PFI0_STR',
                    'PFI0',
                    'The signal is exported to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0.'
                ],
                [
                    'NIRFSG_VAL_PFI1_STR',
                    'PFI1',
                    'The signal is exported to the PFI 1 connector.'
                ],
                [
                    'NIRFSG_VAL_PFI4_STR',
                    'PFI4',
                    'The signal is exported to the PFI 4 connector.'
                ],
                [
                    'NIRFSG_VAL_PFI5_STR',
                    'PFI5',
                    'The signal is exported to the PFI 5 connector.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG0_STR',
                    'PXI_Trig0',
                    'The trigger is received on PXI trigger line 0.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG1_STR',
                    'PXI_Trig1',
                    'The trigger is received on PXI trigger line 1.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG2_STR',
                    'PXI_Trig2',
                    'The trigger is received on PXI trigger line 2.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG3_STR',
                    'PXI_Trig3',
                    'The trigger is received on PXI trigger line 3.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG4_STR',
                    'PXI_Trig4',
                    'The trigger is received on PXI trigger line 4.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG5_STR',
                    'PXI_Trig5',
                    'The trigger is received on PXI trigger line 5.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG6_STR',
                    'PXI_Trig6',
                    'The trigger is received on PXI trigger line 6.'
                ],
                [
                    'NIRFSG_VAL_PXIE_DSTARC_STR',
                    'PXIe_DStarC',
                    'The signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860.'
                ],
                [
                    'NIRFSG_VAL_TRIG_OUT_STR',
                    'TrigOut',
                    'The signal is exported to the TRIG IN/OUT terminal. This value is valid on only the PXIe-5654/5654 with PXIe-5696.'
                ],
                [
                    'NIRFSG_VAL_DIO0_STR',
                    'DIO/PFI0',
                    'The trigger is received on PFI0 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO1_STR',
                    'DIO/PFI1',
                    'The trigger is received on PFI1 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO2_STR',
                    'DIO/PFI2',
                    'The trigger is received on PFI2 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO3_STR',
                    'DIO/PFI3',
                    'The trigger is received on PFI3 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO4_STR',
                    'DIO/PFI4',
                    'The trigger is received on PFI4 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO5_STR',
                    'DIO/PFI5',
                    'The trigger is received on PFI5 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO6_STR',
                    'DIO/PFI6',
                    'The trigger is received on PFI6 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO7_STR',
                    'DIO/PFI7',
                    'The trigger is received on PFI7 from the front panel DIO terminal.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'StartTrigExportOutputTerm',
        'lv_property': 'Triggers:Start:Export Output Terminal',
        'name': 'EXPORTED_START_TRIGGER_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150004: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the clock source for driving the PXI 10 MHz backplane Reference Clock. This attribute is configurable if the PXI-5610 upconverter module is installed in *only* Slot 2 of a PXI chassis. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                **Defined Values**:\n\nName (Value): Description\n\nNIRFSG_VAL_NONE (0) :Do not drive the PXI_CLK10 signal.\n\nNIRFSG_VAL_ONBOARD_CLOCK_STR (OnboardClock) :Uses the highly stable oven-controlled onboard Reference Clock to drive the PXI_CLK signal.\n\nNIRFSG_VAL_REF_IN_STR (RefIn) :Uses the clock present at the front panel REF IN connector to drive the PXI_CLK signal.\n\n                **Default Value:** NIRFSG_VAL_NONE\n\n                **Supported Devices:** PXI-5610, PXI-5670/5671\n\n                **Related Topics**\n\n                `Timing Configurations <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/timing_configurations.html>`_\n\n                `System Reference Clock <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_clk10.html>`_\n                \n                **High-Level Functions**:\n\n                - nirfsg_ConfigurePxiChassisClk10\n            \n            \n                Only certain combinations of this attribute and the NIRFSG_ATTR_REF_CLOCK_SOURCE attribute are valid, as shown in the following table.\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_NONE, NIRFSG_VAL_ONBOARD_CLOCK_STR',
                    'NIRFSG_VAL_ONBOARD_CLOCK_STR'
                ],
                [
                    'NIRFSG_VAL_NONE, NIRFSG_VAL_REF_IN_STR',
                    'NIRFSG_VAL_REF_IN_STR'
                ],
                [
                    'NIRFSG_VAL_NONE, NIRFSG_VAL_REF_IN_STR',
                    'NIRFSG_VAL_PXI_CLK_STR'
                ]
            ],
            'table_header': [
                'NIRFSG_ATTR_PXI_CHASSIS_CLK10_SOURCE Setting',
                'NIRFSG_ATTR_REF_CLOCK_SOURCE Setting'
            ]
        },
        'enum': 'PxiChassisClk10Source',
        'lv_property': 'Clock:PXI Chassis Clk 10 Source',
        'name': 'PXI_CHASSIS_CLK10_SOURCE',
        'type': 'ViString'
    },
    1150005: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies whether the driver maintains phase continuity in the arbitrary waveforms. When this attribute is set to NIRFSG_VAL_ENABLE, NI-RFSG may increase the waveform size. When this attribute is set to NIRFSG_VAL_ENABLE, the NIRFSG_ATTR_FREQUENCY_TOLERANCE attribute specifies the maximum allowable frequency error that can be introduced when keeping the signal phase-continuous. To set the NIRFSG_ATTR_PHASE_CONTINUITY_ENABLED attribute, the NI-RFSG device must be in the Configuration state. NIRFSG_ATTR_PHASE_CONTINUITY_ENABLED applies only when the NIRFSG_ATTR_GENERATION_MODE attribute is set to NIRFSG_VAL_ARB_WAVEFORM or NIRFSG_VAL_SCRIPT.\n\n                PXI-5671: When using the PXI-5671 with I/Q rates less than or equal to 8.33MS/s, an input phase-continuous signal is always phase-continuous upon output, and this attribute has no effect.\n\n                PXIe-5644/5645/5646, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860: Phase continuity is *always* enabled on this device.\n\n                **Default Value:** NIRFSG_VAL_AUTO\n                \n                **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n                \n                **Related Topics**\n\n                `Phase Continuity <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/phasecontinuity.html>`_\n\n                `Arb Waveform Mode Tuning Speed Factors <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5670_arb_waveform_mode_tuning_speed_factors.html>`_\n            \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_AUTO',
                    '-1 (-0x1)',
                    'When the Generation Mode property is set to Arb Waveform, the arbitrary waveform may be repeated to ensure phase continuity after upconversion. This setting could cause waveform size to increase. When the Generation Mode property is set to Script, the Phase Continuity Enabled property indicates a warning condition. NI-RFSG cannot guarantee a phase-continuous output signal in Script mode. Phase continuity is automatically disabled in script mode, and the arbitrary waveform plays back without regard to any possible phase discontinuities introduced by upconversion.'
                ],
                [
                    'NIRFSG_VAL_DISABLE',
                    '0 (0x0)',
                    'When the Generation Mode property is set to Arb Waveform, the arbitrary waveform is played back without regard to any possible phase discontinuities introduced by upconversion. The time duration of the original waveform is maintained. When the Generation Mode property is set to Script, the arbitrary waveform plays back without regard to any possible phase discontinuities introduced by upconversion. The time duration of the original waveform is maintained.'
                ],
                [
                    'NIRFSG_VAL_ENABLE',
                    '1 (0x1)',
                    'When the Generation Mode property is set to Arb Waveform, the arbitrary waveform may be repeated to ensure phase continuity after upconversion. Enabling this property could cause waveform size to increase. When the Generation Mode property is set to Script, the arbitrary waveform plays back without regard to any possible phase discontinuities introduced by upconversion. The time duration of the original waveform is maintained.'
                ]
            ],
            'table_header': [
                'NIRFSG_ATTR_PHASE_CONTINUITY_ENABLED Attribute Setting',
                'Value',
                'With I/Q Rates > 8.33 MS/s.'
            ]
        },
        'enum': 'PhaseContinuityEnabled',
        'lv_property': 'Arb:Phase Continuity Enabled',
        'name': 'PHASE_CONTINUITY_ENABLED',
        'type': 'ViInt32'
    },
    1150006: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the allowable frequency error introduced during the software upconversion process. NI-RFSG may introduce a frequency error up to the specified amount to optimize computational speed and onboard memory usage while upconverting phase-continuous signals.\n\n                If the NIRFSG_ATTR_PHASE_CONTINUITY_ENABLED attribute is set to NIRFSG_VAL_DISABLE, the NIRFSG_ATTR_FREQUENCY_TOLERANCE attribute is ignored, and the driver does not introduce a frequency error. On devices that do not use software upconversion, this attribute is ignored. The PXI-5670 always uses software upconversion, and the PXI-5671 uses software upconversion for I/Q rates greater than 8.33MS/s.\n\n                To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                **Units**: hertz (Hz)\n\n                **Default Value:** 50\n\n                **Supported Devices:** PXI-5670/5671\n\n                **Related Topics**\n\n                `Phase Continuity <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/phasecontinuity.html>`_\n                '
        },
        'lv_property': 'RF:Frequency Tolerance (Hz)',
        'name': 'FREQUENCY_TOLERANCE',
        'type': 'ViReal64'
    },
    1150007: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': "                Specifies the bandwidth of the arbitrary signal. This value must be less than or equal to (0.8× NIRFSG_ATTR_IQ_RATE).\n\n                NI-RFSG defines *signal bandwidth* as twice the maximum baseband signal deviation from 0 Hz. Usually, the baseband signal center frequency is 0 Hz. In such cases, the signal bandwidth is simply the baseband signal's minimum frequency subtracted from its maximum frequency, or *f*\\ :sub:`max`\\ - *f*\\ :sub:`min`\\ .\n\n                This attribute applies only when the NIRFSG_ATTR_GENERATION_MODE attribute is set to NIRFSG_VAL_ARB_WAVEFORM or NIRFSG_VAL_SCRIPT, except for when using the PXIe-5830/5831/5832/5840/5841, which supports setting this attribute in all supported generation modes. To set the NIRFSG_ATTR_SIGNAL_BANDWIDTH attribute, the NI-RFSG device must be in the Configuration state.\n\n                PXI-5670/5671, PXIe-5672: Based on your signal bandwidth, NI-RFSG determines whether to configure the upconverter center frequency in increments of 1MHz or 5MHz. Failure to configure this attribute may result in the signal being placed outside the upconverter passband.\n\n                PXIe-5644/5645/5646, PXIe-5673/5673E: This attribute is used only for error-checking purposes. Otherwise, this attribute is ignored.\n\n                PXIe-5820/5830/5831/5832/5840/5841/5842/5860: Based on your signal bandwidth, NI-RFSG decides the equalized bandwidth. If this attribute is not set, NI-RFSG uses the maximum available signal bandwidth. For the PXIe-5840/5841, the maximum allowed signal bandwidth depends on the upconverter center frequency. Refer to the specifications document for your device for more information about signal bandwidth. The device specifications depend on the signal bandwidth.\n\n                **Units**: hertz (Hz)\n\n                **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Phase-Locked Loop Bandwidth <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/phased_lock_loop_bandwidth.html>`_\n\n                `Frequency Tuning Times <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_tuning_times.html>`_\n\n                `PXIe-5830 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_selection.html>`_\n\n                `PXIe-5831/5832 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_selection.html>`_\n\n                `PXIe-5841 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_selection.html>`_\n                "
        },
        'lv_property': 'Arb:Signal Bandwidth (Hz)',
        'name': 'SIGNAL_BANDWIDTH',
        'type': 'ViReal64'
    },
    1150008: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Enables or disables automatic thermal correction. When this attribute is enabled, changes to settings cause NI-RFSG to check whether the device temperature has changed and adjusts the settings as needed. When this attribute is disabled, you must explicitly call the nirfsg_PerformThermalCorrection function to adjust the device for temperature changes.\n\n                **Default Value:** NIRFSG_VAL_ENABLE\n\n                **Supported Devices:** PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Temperature Monitoring <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5611_temperature_monitoring.html>`_\n\n                `Settling Times <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/settling_times.html>`_\n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_DISABLE',
                    '0 (0x0)',
                    'Automatic thermal correction is disabled.'
                ],
                [
                    'NIRFSG_VAL_ENABLE',
                    '1 (0x1)',
                    'Automatic thermal correction is enabled.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'AutomaticThermalCorrection',
        'lv_property': 'RF:Automatic Thermal Correction',
        'name': 'AUTOMATIC_THERMAL_CORRECTION',
        'type': 'ViInt32'
    },
    1150009: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies whether attenuator hold is enabled. While this attribute is set to VI_TRUE, changing the power level causes NI-RFSG to scale the digital data sent to the AWG instead of adjusting the attenuators. Changing power levels in this manner allows the device to increase or decrease the power level in more accurate increments, but it may affect signal-to-noise ratios (noise density).\n\n\n                Setting the NIRFSG_ATTR_ATTENUATOR_HOLD_ENABLED attribute to VI_TRUE limits the power levels that can be attained. With attenuator hold enabled, the power level must satisfy the following conditions:\n\n                - Power level less than or equal to NIRFSG_ATTR_ATTENUATOR_HOLD_MAX_POWER\n                - Power level greater than or equal to (maximum power level -70dB)\n                - Power level greater than or equal to -145dBm\n\n                To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                **Default Value:** VI_FALSE\n\n                **Supported Devices:** PXI-5670/5671, PXIe-5672/5673/5673E\n\n                **Related Topics**\n\n                `Attenuator Hold <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/attenuator_hold_mode.html>`_\n\n                `Settling Times <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/settling_times.html>`_\n\n            **Defined Values**:\n            ',
            'note': 'The frequency cannot be changed on the PXI-5670/5671 or PXIe-5672 while this attribute is set to VI_TRUE.',
            'table_body': [
                [
                    'VI_TRUE',
                    'Enables attenuator hold.'
                ],
                [
                    'VI_FALSE',
                    'Disables attenuator hold.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'lv_property': 'RF:Attenuator Hold Enabled',
        'name': 'ATTENUATOR_HOLD_ENABLED',
        'type': 'ViBoolean'
    },
    1150010: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the maximum power level of the RF output signal when the NIRFSG_ATTR_ATTENUATOR_HOLD_ENABLED attribute is set to VI_TRUE.\n\n                To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                **Units**: dBm\n\n                **Defined Values**:\n                Refer to the specifications document for your device for allowable maximum power levels.\n\n                **Default Value:**\n\n                PXI-5670/5671, PXIe-5672: 17\n\n                PXIe-5673/5673E: 10\n\n                **Supported Devices:** PXI-5670/5671, PXIe-5672/5673/5673E\n\n                **Related Topics**\n\n                `Attenuator Hold <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/attenuator_hold_mode.html>`_\n\n                `Settling Times <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/settling_times.html>`_\n                '
        },
        'lv_property': 'RF:Attenuator Hold Max Power (dBm)',
        'name': 'ATTENUATOR_HOLD_MAX_POWER',
        'type': 'ViReal64'
    },
    1150011: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns the maximum instantaneous power of the RF output signal.\n\n                **Units**: dBm\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n            ',
            'note': '- This attribute is valid only when the NIRFSG_ATTR_POWER_LEVEL_TYPE attribute is set to NIRFSG_VAL_AVERAGE_POWER.\n\n - The NIRFSG_ATTR_ARB_DIGITAL_GAIN attribute is not included in the calculation of the NIRFSG_ATTR_PEAK_ENVELOPE_POWER attribute.'
        },
        'lv_property': 'RF:Peak Envelope Power (dBm)',
        'name': 'PEAK_ENVELOPE_POWER',
        'type': 'ViReal64'
    },
    1150012: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                When this attribute is enabled, NI-RFSG equalizes the waveform data to correct for variations in the response of the NI-RFSG device. Enabling digital equalization improves the modulation error rates (MER) and error vector magnitude (EVM) for signals with large bandwidths (\\>500 kHz), but it increases tuning times.\n\n                On the PXI-5670/5671, equalization is performed in the software, so tuning time is increased. On the PXIe-5672, equalization is performed in the hardware so that there is no compromise in performance.\n\n                This attribute applies only when the NIRFSG_ATTR_GENERATION_MODE attribute is set to NIRFSG_VAL_ARB_WAVEFORM or NIRFSG_VAL_SCRIPT. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860: NIRFSG_VAL_ENABLE is the only supported value for this device.\n\n                **Default Value:**\n\n                PXI-5670/5671: NIRFSG_VAL_DISABLE\n\n                PXIe-5644/5645/5646, PXIe-5672, PXIe-5820/5830/5831/5832/5840/5841/5842/5860: NIRFSG_VAL_ENABLE\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Response and Software Equalization <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/if_response_and_equalizer.html>`_—Refer to this topic for more information about equalization performed in software.\n\n                `Frequency Tuning Times <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_tuning_times.html>`_\n\n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_DISABLE',
                    '0 (0x0)',
                    'Filter is not applied'
                ],
                [
                    'NIRFSG_VAL_ENABLE',
                    '1 (0x1)',
                    'Filter is applied.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'DigitalEqualizationEnabled',
        'lv_property': 'Arb:Digital Equalization Enabled',
        'name': 'DIGITAL_EQUALIZATION_ENABLED',
        'type': 'ViInt32'
    },
    1150013: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies whether the local oscillator signal is present at the LO OUT front panel connector. The local oscillator signal remains at the LO OUT front panel connector until this attribute is set to VI_FALSE, even if the NIRFSG_ATTR_OUTPUT_ENABLED attribute is set to VI_FALSE, the nirfsg_Abort function is called, or the NI-RFSG session is closed.\n\n                To use this attribute for the PXIe-5830/5831/5832, you must use the channelName parameter of the nirfsg_SetAttributeViBoolean function to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).\n\n                **Default Value:** NIRFSG_VAL_DISABLE\n\n                **Supported Devices:** PXI-5610, PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5830/5831/5832/5840/5841/5842\n\n                **Related Topics**\n\n                `LO OUT <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/loout.html>`_\n            \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_ENABLE',
                    'The local oscillator signal is present at the LO OUT front panel connector.'
                ],
                [
                    'NIRFSG_VAL_DISABLE',
                    'The local oscillator signal is not present at the LO OUT front panel connector.'
                ]
            ],
            'table_header': [
                'Name',
                'Description'
            ]
        },
        'lv_property': 'RF:LO Out Enabled',
        'name': 'LO_OUT_ENABLED',
        'type': 'ViBoolean'
    },
    1150014: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Enables or disables warnings or errors when you set the frequency, power, and bandwidth values beyond the limits of the NI-RFSG device specifications. When you enable the NIRFSG_ATTR_ALLOW_OUT_OF_SPECIFICATION_USER_SETTINGS attribute, the driver does not report out-of-specification warnings or errors.\n\n                To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                **Default Value:** NIRFSG_VAL_DISABLE\n\n                **Supported Devices:** PXI/PXIe-5650/5651/5652, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n            **Defined Values**:\n            ',
            'note': 'Accuracy cannot be guaranteed outside of device specifications, and results may vary by module.',
            'table_body': [
                [
                    'NIRFSG_VAL_DISABLE',
                    '0 (0x0)',
                    'Disables out-of-specification user settings.'
                ],
                [
                    'NIRFSG_VAL_ENABLE',
                    '1 (0x1)',
                    'Enables out-of-specification user settings.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'AllowOutOfSpecificationUserSettings',
        'lv_property': 'RF:Allow Out Of Specification User Settings',
        'name': 'ALLOW_OUT_OF_SPECIFICATION_USER_SETTINGS',
        'type': 'ViInt32'
    },
    1150015: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '\n                **Units**: hertz (Hz)\n\n                **Supported Devices:** PXI-5610, PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Assigning Properties or Attributes to a Waveform <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/assigning_properties_or_attributes_to_a_waveform.html>`_—Refer to this topic for more information about using this attribute to associate a carrier frequency with a waveform.\n                Indicates the carrier frequency generated by the arbitrary waveform generator (AWG) module. The specified carrier frequency is related to the RF output as shown in the following equations:\n            ',
            'note': '- Use this attribute to associate a carrier frequency with a waveform.\n\n - This attribute is read-only on the PXI-5670/5671 and PXIe-5672.',
            'table_body': [
                [
                    'PXI-5610, PXI-5670/5671, PXIe-5672',
                    'RF Frequency (MHz) = *Upconverter Center Frequency* + *Arb Carrier Frequency* – 25 MHz'
                ],
                [
                    'PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5830/5831/5832/5840/5841/5842/5860',
                    'RF Frequency (MHz) = *Upconverter Center Frequency* + *Arb Carrier Frequency*.Note that - the NIRFSG_ATTR_UPCONVERTER_CENTER_FREQUENCY attribute and the NIRFSG_ATTR_ARB_CARRIER_FREQUENCY attribute cannot be set at the same time. The only time the carrier frequency is nonzero on these devices is when in-band retuning is used. '
                ]
            ],
            'table_header': [
                'Device',
                'Equations'
            ]
        },
        'lv_property': 'Arb:Arb Carrier Frequency (Hz)',
        'name': 'ARB_CARRIER_FREQUENCY',
        'type': 'ViReal64'
    },
    1150016: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Indicates the average output power from the PXI-5421, PXI-5441, PXIe-5442, and PXIe-5450 AWG module. If an arbitrary waveform is being generated, this attribute specifies either the average power or the peak power of the signal, depending on the NIRFSG_ATTR_POWER_LEVEL_TYPE attribute setting.\n\n                **Units**: dBm\n\n                **Supported Devices:** PXI-5670/5671, PXIe-5672/5673/5673E\n                '
        },
        'lv_property': 'Arb:Arb Power (dBm)',
        'name': 'ARB_POWER',
        'type': 'ViReal64'
    },
    1150017: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns the device temperature. If the NI-RFSG session is controlling multiple devices, this attribute returns the temperature of the primary NI RF device. The NI-RFSG session is opened using the primary RF device name.\n\n                Serial signals between the sensor and the system control unit could modulate the signal being generated, thus causing phase spurs. After the device thoroughly warms up, its temperature varies only slightly (less than 1 degree Celsius) and slowly, and it is not necessary to constantly poll this temperature sensor.\n\n                PXIe-5644/5645/5646, PXIe-5820/5840/5841: If you query this attribute during RF list mode, list steps may take longer to complete during list execution.\n\n                PXIe-5830/5831/5832: To use this attribute, you must first set the channelName parameter of the nirfsg_SetAttributeViReal64 function to using the appropriate string for your instrument configuration. Setting the nirfsg_SetAttributeViReal64 function is not required for the PXIe-3621/3622. Refer to the following table to determine which strings are valid for your configuration.\n\n                **Units**: degrees Celsius (°C)\n\n                **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Temperature Monitoring <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5611_temperature_monitoring.html>`_\n\n                `Thermal Shutdown <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/thermal_shutdown_monitoring_5650_5651_5652.html>`_\n            ',
            'table_body': [
                [
                    'PXIe-3621/3622',
                    '—',
                    'if or "" (empty string)'
                ],
                [
                    'PXIe-5820',
                    '—',
                    'fpga'
                ],
                [
                    'First connected mmRH-5582',
                    'DIRECT TRX PORTS Only',
                    'rf0'
                ],
                [
                    'First connected mmRH-5582',
                    'SWITCHED TRX PORTS [0-7]',
                    'rf0switch0'
                ],
                [
                    'First connected mmRH-5582',
                    'SWITCHED TRX PORTS [0-7]',
                    'rf0switch1'
                ],
                [
                    'Second connected mmRH-5582',
                    'DIRECT TRX PORTS Only',
                    'rf1'
                ],
                [
                    'Second connected mmRH-5582',
                    'SWITCHED TRX PORTS [0-7]',
                    'rf1switch0'
                ],
                [
                    'Second connected mmRH-5582',
                    'SWITCHED TRX PORTS [0-7]',
                    'rf1switch1'
                ]
            ],
            'table_header': [
                'Hardware Module',
                'TRX Port Type',
                'Active Channel String'
            ]
        },
        'lv_property': 'Device Characteristics:Device Temperature (Degrees C)',
        'name': 'DEVICE_TEMPERATURE',
        'type': 'ViReal64'
    },
    1150018: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies whether to generate a continuous wave (CW) signal, the arbitrary waveform specified by the NIRFSG_ATTR_ARB_SELECTED_WAVEFORM attribute, or the script specified by the NIRFSG_ATTR_SELECTED_SCRIPT attribute, upon calling the nirfsg_Initiate function.\n\n                To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                **Default Value:** NIRFSG_VAL_CW\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696 (CW support only), PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Assigning Properties or Attributes to a Waveform <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/assigning_properties_or_attributes_to_a_waveform.html>`_\n\n                `Scripting Instructions <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/scripting_instructions.html>`_—Refer to this topic for more information about scripting.\n                \n                **High-Level Functions**:\n\n                - nirfsg_ConfigureGenerationMode\n            \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_ARB_WAVEFORM',
                    '1001 (0x3e9)',
                    'Configures the RF signal generator to generate the arbitrary waveform specified by the NIRFSG_ATTR_ARB_SELECTED_WAVEFORM attribute.'
                ],
                [
                    'NIRFSG_VAL_CW',
                    '1000 (0x3e8)',
                    'Configures the RF signal generator to generate a CW signal.'
                ],
                [
                    'NIRFSG_VAL_SCRIPT',
                    '1002 (0x3ea)',
                    'Configures the RF signal generator to generate arbitrary waveforms as directed by the NIRFSG_ATTR_SELECTED_SCRIPT attribute..'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'GenerationMode',
        'lv_property': 'Arb:Generation Mode',
        'name': 'GENERATION_MODE',
        'type': 'ViInt32'
    },
    1150019: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the Script Trigger type. Depending upon the value of this attribute, more attributes may be needed to fully configure the trigger. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                **Default Value:** NIRFSG_VAL_NONE\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_\n\n                `Trigger Types <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_types.html>`_\n\n                **High-Level Functions**:\n\n                - nirfsg_ConfigureDigitalEdgeScriptTrigger\n            \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_NONE',
                    'No trigger is configured. Signal generation starts immediately.'
                ],
                [
                    'NIRFSG_VAL_DIGITAL_EDGE',
                    'The data operation does not start until a digital edge is detected. The source of the digital edge is specified with the NIRFSG_ATTR_DIGITAL_EDGE_START_TRIGGER_SOURCE attribute, and the active edge is specified with the NIRFSG_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE attribute.'
                ],
                [
                    'NIRFSG_VAL_DIGITAL_LEVEL',
                    'The data operation does not start until the digital level is detected. The source of the digital level is specified in the NIRFSG_ATTR_DIGITAL_LEVEL_SCRIPT_TRIGGER_SOURCE attribute, and the active level is specified in the NIRFSG_ATTR_DIGITAL_LEVEL_SCRIPT_TRIGGER_ACTIVE_LEVEL attribute.'
                ],
                [
                    'NIRFSG_VAL_SOFTWARE',
                    'The data operation does not start until a software trigger occurs. You can create a software event by calling the niRFSG_SendSoftwareEdgeTrigger function.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'enum': 'ScriptTrigType',
        'lv_property': 'Triggers:Script:Type',
        'name': 'SCRIPT_TRIGGER_TYPE',
        'supported_rep_caps': [
            'script_triggers'
        ],
        'type': 'ViInt32'
    },
    1150020: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the source terminal for the Script Trigger. This attribute is used when the NIRFSG_ATTR_SCRIPT_TRIGGER_TYPE attribute is set to digital edge. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_\n\n                `PFI Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pfi_lines.html>`_\n\n                `PXI Trigger Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_trigger.html>`_\n                \n                **High-Level Functions**:\n\n                - nirfsg_ConfigureDigitalEdgeScriptTrigger\n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_PFI0_STR',
                    'PFI0',
                    'The trigger is received on PFI 0.'
                ],
                [
                    'NIRFSG_VAL_PFI1_STR',
                    'PFI1',
                    'The trigger is received on PFI 1.'
                ],
                [
                    'NIRFSG_VAL_PFI2_STR',
                    'PFI2',
                    'The trigger is received on PFI 2.'
                ],
                [
                    'NIRFSG_VAL_PFI3_STR',
                    'PFI3',
                    'The trigger is received on PFI 3.'
                ],
                [
                    'NIRFSG_VAL_PXI_STAR_STR',
                    'PXI_Star',
                    'The trigger is received on the PXI star trigger line. This value is not valid for the PXIe-5644/5645/5646.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG0_STR',
                    'PXI_Trig0',
                    'The trigger is received on PXI trigger line 0.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG1_STR',
                    'PXI_Trig1',
                    'The trigger is received on PXI trigger line 1.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG2_STR',
                    'PXI_Trig2',
                    'The trigger is received on PXI trigger line 2.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG3_STR',
                    'PXI_Trig3',
                    'The trigger is received on PXI trigger line 3.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG4_STR',
                    'PXI_Trig4',
                    'The trigger is received on PXI trigger line 4.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG5_STR',
                    'PXI_Trig5',
                    'The trigger is received on PXI trigger line 5.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG6_STR',
                    'PXI_Trig6',
                    'The trigger is received on PXI trigger line 6.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG7_STR',
                    'PXI_Trig7',
                    'The trigger is received on PXI trigger line 7.'
                ],
                [
                    'NIRFSG_VAL_PXIE_DSTARB_STR',
                    'PXIe_DStarB',
                    'The trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860.'
                ],
                [
                    'NIRFSG_VAL_PULSE_IN_STR',
                    'PulseIn',
                    'The trigger is received on the PULSE IN terminal. This value is valid on only the PXIe-5842.'
                ],
                [
                    'NIRFSG_VAL_DIO0_STR',
                    'DIO/PFI0',
                    'The trigger is received on PFI0 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO1_STR',
                    'DIO/PFI1',
                    'The trigger is received on PFI1 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO2_STR',
                    'DIO/PFI2',
                    'The trigger is received on PFI2 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO3_STR',
                    'DIO/PFI3',
                    'The trigger is received on PFI3 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO4_STR',
                    'DIO/PFI4',
                    'The trigger is received on PFI4 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO5_STR',
                    'DIO/PFI5',
                    'The trigger is received on PFI5 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO6_STR',
                    'DIO/PFI6',
                    'The trigger is received on PFI6 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO7_STR',
                    'DIO/PFI7',
                    'The trigger is received on PFI7 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_SYNC_SCRIPT_TRIGGER_STR',
                    'Sync_Script',
                    'The trigger is received on the Sync Script trigger line. This value is valid on only the PXIe-5644/5645/5646.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'ScriptTrigDigEdgeSource',
        'lv_property': 'Triggers:Script:Digital Edge:Source',
        'name': 'DIGITAL_EDGE_SCRIPT_TRIGGER_SOURCE',
        'supported_rep_caps': [
            'script_triggers'
        ],
        'type': 'ViString'
    },
    1150021: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the active edge for the Script Trigger. This attribute is used when the NIRFSG_ATTR_SCRIPT_TRIGGER_TYPE attribute is set to digital edge. To set the NIRFSG_ATTR_DIGITAL_EDGE_SCRIPT_TRIGGER_EDGE attribute, the NI-RFSG device must be in the Configuration state.\n\n                **Default Value:** NIRFSG_VAL_RISING_EDGE\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_\n\n                `Digital Edge Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_edge.html>`_\n                \n                **High-Level Functions**:\n\n                - nirfsg_ConfigureDigitalEdgeScriptTrigger\n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_FALLING_EDGE',
                    '1 (0x1)',
                    'Asserts the trigger when the signal transitions from high level to low level.'
                ],
                [
                    'NIRFSG_VAL_RISING_EDGE',
                    '0 (0x0)',
                    'Asserts the trigger when the signal transitions from low level to high level.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'ScriptTrigDigEdgeEdge',
        'lv_property': 'Triggers:Script:Digital Edge:Edge',
        'name': 'DIGITAL_EDGE_SCRIPT_TRIGGER_EDGE',
        'supported_rep_caps': [
            'script_triggers'
        ],
        'type': 'ViInt32'
    },
    1150022: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the destination terminal for exporting the Script Trigger. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_ —Refer to this topic for information about trigger delay.\n\n                `PFI Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pfi_lines.html>`_\n\n                `PXI Trigger Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_trigger.html>`_\n                \n                **High-Level Functions**:\n\n                - nirfsg_ExportSignal\n                \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_DO_NOT_EXPORT_STR',
                    '',
                    'The signal is not exported.'
                ],
                [
                    'NIRFSG_VAL_PFI0_STR',
                    'PFI0',
                    'The signal is exported to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0.'
                ],
                [
                    'NIRFSG_VAL_PFI1_STR',
                    'PFI1',
                    'The signal is exported to the PFI 1 connector.'
                ],
                [
                    'NIRFSG_VAL_PFI4_STR',
                    'PFI4',
                    'The signal is exported to the PFI 4 connector.'
                ],
                [
                    'NIRFSG_VAL_PFI5_STR',
                    'PFI5',
                    'The signal is exported to the PFI 5 connector.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG0_STR',
                    'PXI_Trig0',
                    'The trigger is received on PXI trigger line 0.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG1_STR',
                    'PXI_Trig1',
                    'The trigger is received on PXI trigger line 1.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG2_STR',
                    'PXI_Trig2',
                    'The trigger is received on PXI trigger line 2.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG3_STR',
                    'PXI_Trig3',
                    'The trigger is received on PXI trigger line 3.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG4_STR',
                    'PXI_Trig4',
                    'The trigger is received on PXI trigger line 4.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG5_STR',
                    'PXI_Trig5',
                    'The trigger is received on PXI trigger line 5.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG6_STR',
                    'PXI_Trig6',
                    'The trigger is received on PXI trigger line 6.'
                ],
                [
                    'NIRFSG_VAL_PXIE_DSTARC_STR',
                    'PXIe_DStarC',
                    'The signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841.'
                ],
                [
                    'NIRFSG_VAL_DIO0_STR',
                    'DIO/PFI0',
                    'The trigger is received on PFI0 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO1_STR',
                    'DIO/PFI1',
                    'The trigger is received on PFI1 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO2_STR',
                    'DIO/PFI2',
                    'The trigger is received on PFI2 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO3_STR',
                    'DIO/PFI3',
                    'The trigger is received on PFI3 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO4_STR',
                    'DIO/PFI4',
                    'The trigger is received on PFI4 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO5_STR',
                    'DIO/PFI5',
                    'The trigger is received on PFI5 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO6_STR',
                    'DIO/PFI6',
                    'The trigger is received on PFI6 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO7_STR',
                    'DIO/PFI7',
                    'The trigger is received on PFI7 from the front panel DIO terminal.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'ScriptTrigExportOutputTerm',
        'lv_property': 'Triggers:Script:Export Output Terminal',
        'name': 'EXPORTED_SCRIPT_TRIGGER_OUTPUT_TERMINAL',
        'supported_rep_caps': [
            'script_triggers'
        ],
        'type': 'ViString'
    },
    1150023: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the script in onboard memory to generate upon calling the nirfsg_Initiate function when the NIRFSG_ATTR_GENERATION_MODE attribute is set to NIRFSG_VAL_SCRIPT.\n\n                The NIRFSG_ATTR_SELECTED_SCRIPT attribute is ignored when the NIRFSG_ATTR_GENERATION_MODE attribute is set to NIRFSG_VAL_ARB_WAVEFORM or NIRFSG_VAL_CW. To set the NIRFSG_ATTR_SELECTED_SCRIPT attribute, the NI-RFSG device must be in the Configuration state.\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Assigning Properties or Attributes to a Waveform <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/assigning_properties_or_attributes_to_a_waveform.html>`_\n\n                `Scripting Instructions <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/scripting_instructions.html>`_\n                '
        },
        'lv_property': 'Arb:Selected Script',
        'name': 'SELECTED_SCRIPT',
        'type': 'ViString'
    },
    1150024: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the phase of the RF output signal. Use this attribute to align the phase of the RF output with the phase of the RF output of another device, as long as the two devices are phase-coherent.\n\n                **Units**: degrees (°)\n\n                **Default Value:** 0\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842\n\n                **Related Topics**\n\n                `Phase Synchronization and Phase Coherency <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/phase_synchronization_and_phase_coherency.html>`_\n                '
        },
        'lv_property': 'RF:Phase Offset (Degrees)',
        'name': 'PHASE_OFFSET',
        'type': 'ViReal64'
    },
    1150025: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the AWG prefilter gain. The prefilter gain is applied to the waveform data before any other signal processing. Reduce this value to prevent overflow in the AWG interpolation filters. Other gains on the NI-RFSG device are automatically adjusted to compensate for nonunity AWG prefilter gain. The PXI-5671, PXIe-5672 must be in the Configuration state to use this attribute. However, the PXIe-5644/5645/5646, PXIe-5673/5673E, and PXIe-5820/5830/5831/5832/5840/5841/5842 can be in either the Configuration or the Generation state to use this attribute. PXIe-5860 can only be in the Configuration state to use this attribute.\n\n                On the PXI-5671, this attribute applies only when the NIRFSG_ATTR_IQ_RATE attribute is set to a value less than or equal to 8.33MS/s. On the PXIe-5644/5645/5646, PXIe-5672/5673/5673E, and PXIe-5820/5830/5831/5832/5840/5841/5842/5860, this attribute is always applicable.\n\n                **Units**: dB\n\n                **Default Value:** 0dB\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXI-5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n                '
        },
        'lv_property': 'Arb:Pre-filter Gain (dB)',
        'name': 'ARB_PRE_FILTER_GAIN',
        'type': 'ViReal64'
    },
    1150026: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns the serial number of the RF module. If the NI-RFSG session is controlling multiple modules, this attribute returns the serial number of the primary RF module.\n\n                **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n                '
        },
        'lv_property': 'Device Characteristics:Serial Number',
        'name': 'SERIAL_NUMBER',
        'type': 'ViString'
    },
    1150027: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Configures the loop bandwidth of the tuning PLLs. This attribute is ignored on the PXI-5610, PXI-5670/5671, and PXIe-5672 for signal bandwidths greater than or equal to 10MHz. This attribute is ignored on the PXI/PXIe-5650/5651/5652 for RF frequencies less than 50MHz.\n\n                To use this attribute for the PXIe-5830/5831/5832, you must use the channelName parameter of the nirfsg_SetAttributeViInt32 function to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).\n\n                **Default Value:**\n\n                PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842: NIRFSG_VAL_MEDIUM\n\n                PXI/PXIe-5650/5651/5652, PXIe-5673/5673E: NIRFSG_VAL_NARROW\n\n                **Supported Devices:** PXI-5610, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5830/5831/5832/5840/5841/5842\n\n                **Related Topics**\n\n                `Phase-Locked Loop Bandwidth <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/phased_lock_loop_bandwidth.html>`_\n\n                `Modulation Implementation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5650_5651_5652_modulation_implementation.html>`_\n\n                `Sinusoidal Tone Versus Modulation Operation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/sinusoidal_tone_versus_modulation_implementation.html>`_\n            \n            **Defined Values**:\n            ',
            'note': 'Setting this attribute to NIRFSG_VAL_WIDE on the PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, or the PXIe-5673/5673E allows the frequency to settle significantly faster at the expense of increased phase noise. Setting this attribute to NIRFSG_VAL_MEDIUM is not a valid option on the PXI/PXIe-5650/5651/5652 or PXIe-5673/5673E. NIRFSG_VAL_MEDIUM is the only supported value for the PXIe-5840/5841/5842.',
            'table_body': [
                [
                    'NIRFSG_VAL_MEDIUM',
                    '1 (0x1)',
                    'Uses the medium loop bandwidth setting for the PLL.'
                ],
                [
                    'NIRFSG_VAL_NARROW',
                    '0 (0x0)',
                    'Uses the narrowest loop bandwidth setting for the PLL.'
                ],
                [
                    'NIRFSG_VAL_WIDE',
                    '2 (0x2)',
                    'Uses the widest loop bandwidth setting for the PLL.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'LoopBandwidth',
        'lv_property': 'RF:Loop Bandwidth',
        'name': 'LOOP_BANDWIDTH',
        'type': 'ViInt32'
    },
    1150029: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the Sample Clock mode on the device. To set this attribute, the device must be in the Configuration state.\n\n                PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860: NIRFSG_VAL_DIVIDE_DOWN is the only supported value for this device.\n\n                **Default Values:**\n\n                PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672, PXIe-5820/5830/5831/5832/5840/5841/5842/5860: NIRFSG_VAL_DIVIDE_DOWN\n\n                PXIe-5673/5673E: NIRFSG_VAL_HIGH_RESOLUTION\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Clocking Modes <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/clocking.html>`_\n\n            **Valid Values**:\n            ',
            'note': 'Using the high resolution clock may result in increased phase noise.',
            'table_body': [
                [
                    'NIRFSG_VAL_HIGH_RESOLUTION',
                    'Sample rates are generated by a high-resolution clock.'
                ],
                [
                    'NIRFSG_VAL_DIVIDE_DOWN',
                    'Sample rates are generated by dividing the source frequency.'
                ]
            ],
            'table_header': [
                'Name',
                'Description'
            ]
        },
        'enum': 'ArbOnboardSampleClockMode',
        'lv_property': 'Clock:Arb Onboard Sample Clock Mode',
        'name': 'ARB_ONBOARD_SAMPLE_CLOCK_MODE',
        'type': 'ViInt32'
    },
    1150030: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the Sample Clock source for the device. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860: NIRFSG_VAL_ONBOARD_CLOCK_STR is the only supported value for this device.\n\n                **Default Value:** NIRFSG_VAL_ONBOARD_CLOCK_STR\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Timing Configurations <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/timing_configurations.html>`_\n            \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_CLK_IN_STR',
                    'ClkIn',
                    'Uses the external clock as the Sample Clock source.'
                ],
                [
                    'NIRFSG_VAL_ONBOARD_CLOCK_STR',
                    'OnboardClock',
                    'Uses the AWG module onboard clock as the Sample Clock source.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'ArbSampleClockSource',
        'lv_property': 'Clock:Arb Sample Clock Source',
        'name': 'ARB_SAMPLE_CLOCK_SOURCE',
        'type': 'ViString'
    },
    1150031: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns the rate of the Sample Clock on the device.\n\n                **Units**: hertz (Hz)\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n                '
        },
        'lv_property': 'Clock:Arb Sample Clock Rate (Hz)',
        'name': 'ARB_SAMPLE_CLOCK_RATE',
        'type': 'ViReal64'
    },
    1150032: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the analog modulation format to use.\n\n                **Default Value:** NIRFSG_VAL_NONE\n\n                **Supported Devices:** PXI/PXIe-5650/5651/5652, PXIe-5654/5654 with PXIe-5696\n\n                **Related Topics**\n\n                `Modulation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/modulation.html>`_\n\n                `PXI/PXIe-5650/5651/5652 Modulation Schemes <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/modulation_modes.html>`_\n\n                `PXIe-5654/5654 with PXIe-5696 Modulation Schemes <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_5696_modulation_modes.html>`_\n                \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_AM',
                    '2002 (0x7d2)',
                    'Specifies that the analog modulation type is AM.'
                ],
                [
                    'NIRFSG_VAL_FM',
                    '2000 (0x7d0)',
                    'Specifies that the analog modulation type is FM.'
                ],
                [
                    'NIRFSG_VAL_NONE',
                    '0 (0x0)',
                    'Disables analog modulation.'
                ],
                [
                    'NIRFSG_VAL_PM',
                    '2001 (0x7d1)',
                    'Specifies that the analog modulation type is PM.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'AnlgModType',
        'lv_property': 'Modulation:Analog:Modulation Type',
        'name': 'ANALOG_MODULATION_TYPE',
        'type': 'ViInt32'
    },
    1150033: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the type of waveform to use as the message signal for analog modulation.\n\n                **Default Value:** NIRFSG_VAL_SINE\n\n                **Supported Devices:** PXI/PXIe-5650/5651/5652\n\n                **Related Topics**\n\n                `Modulation Schemes <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/modulation_modes.html>`_\n            \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_SINE',
                    '3000 (0xbb8)',
                    'Specifies that the analog modulation waveform type is sine.'
                ],
                [
                    'NIRFSG_VAL_SQUARE',
                    '3001 (0xbb9)',
                    'Specifies that the analog modulation waveform type is square.'
                ],
                [
                    'NIRFSG_VAL_TRIANGLE',
                    '3002 (0xbba)',
                    'Specifies that the analog modulation waveform type is triangle.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'AnlgModWfmType',
        'lv_property': 'Modulation:Analog:Waveform Type',
        'name': 'ANALOG_MODULATION_WAVEFORM_TYPE',
        'type': 'ViInt32'
    },
    1150034: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the frequency of the waveform to use as the message signal in analog modulation.\n\n                **Units:** hertz (Hz)\n\n                **Default Value:** 1kHz\n\n                **Supported Devices:** PXI/PXIe-5650/5651/5652\n\n                **Related Topics**\n\n                `Modulation Schemes <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/modulation_modes.html>`_\n                '
        },
        'lv_property': 'Modulation:Analog:Waveform Frequency (Hz)',
        'name': 'ANALOG_MODULATION_WAVEFORM_FREQUENCY',
        'type': 'ViReal64'
    },
    1150035: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the frequency deviation to use in frequency modulation.\n\n                **Units**: hertz (Hz)\n\n                **Default Value:** 1kHz\n\n                **Supported Devices:** PXI/PXIe-5650/5651/5652\n\n                **Related Topics**\n\n                `Modulation Schemes <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/modulation_modes.html>`_\n                '
        },
        'lv_property': 'Modulation:Analog:FM Deviation (Hz)',
        'name': 'ANALOG_MODULATION_FM_DEVIATION',
        'type': 'ViReal64'
    },
    1150036: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the digital modulation format to use.\n\n                **Default Value:** NIRFSG_VAL_NONE\n\n                **Supported Devices:** PXI/PXIe-5650/5651/5652\n\n                **Related Topics**\n\n                `Modulation Schemes <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/modulation_modes.html>`_\n            \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_FSK',
                    '4000 (0xfa0)',
                    'Specifies that the digital modulation type is frequency-shift keying (FSK).'
                ],
                [
                    'NIRFSG_VAL_NONE',
                    '0 (0x0)',
                    'Disables digital modulation.'
                ],
                [
                    'NIRFSG_VAL_OOK',
                    '4001 (0xfa1)',
                    'Specifies that the digital modulation type is on-off keying (OOK).'
                ],
                [
                    'NIRFSG_VAL_PSK',
                    '4002 (0xfa2)',
                    'Specifies that the digital modulation type is phase-shift keying (PSK).'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'DigModType',
        'lv_property': 'Modulation:Digital:Modulation Type',
        'name': 'DIGITAL_MODULATION_TYPE',
        'type': 'ViInt32'
    },
    1150037: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the symbol rate of the bit stream for digital modulation.\n\n                **Units**: hertz (Hz)\n\n                **Default Value:** 1kHz\n\n                **Supported Devices:** PXI/PXIe-5650/5651/5652\n\n                **Related Topics**\n\n                `Modulation Schemes <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/modulation_modes.html>`_\n                '
        },
        'lv_property': 'Modulation:Digital:Symbol Rate',
        'name': 'DIGITAL_MODULATION_SYMBOL_RATE',
        'type': 'ViReal64'
    },
    1150038: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the type of waveform to use as the message signal in digital modulation.\n\n                **Default Value:** NIRFSG_VAL_PRBS\n\n                **Supported Devices:** PXI/PXIe-5650/5651/5652\n\n                **Related Topics**\n\n                `Modulation Schemes <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/modulation_modes.html>`_\n            \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_PRBS',
                    '5000 (0x1388)',
                    'Specifies that the digital modulation waveform type is pseudorandom bit sequence (PRBS).'
                ],
                [
                    'NIRFSG_VAL_USER_DEFINED',
                    '5001 (0x1389)',
                    'Specifies that the digital modulation waveform type is user defined. To specify the user-defined waveform, call the niRFSG_ConfigureDigitalModulationUserDefinedWaveform function.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'DigModWfmType',
        'lv_property': 'Modulation:Digital:Waveform Type',
        'name': 'DIGITAL_MODULATION_WAVEFORM_TYPE',
        'type': 'ViInt32'
    },
    1150039: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the order of pseudorandom bit sequence (PRBS) internally generated by hardware and used as the message signal in digital modulation.\n\n                **Default Value:** 16\n\n                **Supported Devices:** PXI/PXIe-5650/5651/5652\n\n                **Related Topics**\n\n                `Modulation Schemes <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/modulation_modes.html>`_\n                '
        },
        'lv_property': 'Modulation:Digital:PRBS Order',
        'name': 'DIGITAL_MODULATION_PRBS_ORDER',
        'type': 'ViInt32'
    },
    1150040: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the seed of the internally generated pseudorandom bit sequence (PRBS).\n\n                **Default Value:** 1\n\n                **Supported Devices:** PXI/PXIe-5650/5651/5652\n\n                **Related Topics**\n\n                `Modulation Schemes <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/modulation_modes.html>`_\n                '
        },
        'lv_property': 'Modulation:Digital:PRBS Seed',
        'name': 'DIGITAL_MODULATION_PRBS_SEED',
        'type': 'ViInt32'
    },
    1150041: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the deviation to use in FSK modulation.\n\n                **Units**: hertz (Hz)\n\n                **Default Value:** 1,000\n\n                **Supported Devices:** PXI/PXIe-5650/5651/5652\n\n                **Related Topics**\n\n                `Modulation Schemes <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/modulation_modes.html>`_\n                '
        },
        'lv_property': 'Modulation:Digital:FSK Deviation (Hz)',
        'name': 'DIGITAL_MODULATION_FSK_DEVIATION',
        'type': 'ViReal64'
    },
    1150042: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies whether the nirfsg_WriteArbWaveform function immediately writes waveforms to the device or copies the waveform to host memory for later download. NI-RFSG reads and validates this attribute when an arbitrary waveform is first allocated.\n\n                For the PXI-5670, direct download is always disabled. For all other devices, direct download is always enabled.\n\n                PXI-5671: To increase performance when using large waveforms, enable direct download. To maximize reconfigurability, disable direct download.\n\n                Perform the following steps to enable direct download:\n\n\n\n                1\\. Set the I/Q rate to less than or equal to 8.33MS/s with the NIRFSG_ATTR_IQ_RATE attribute.\n\n                2\\. Set the NIRFSG_ATTR_POWER_LEVEL_TYPE attribute to NIRFSG_VAL_PEAK_POWER.\n\n                3\\. Disable the NIRFSG_ATTR_IQ_SWAP_ENABLED attribute.\n\n                4\\. Disable the NIRFSG_ATTR_DIGITAL_EQUALIZATION_ENABLED attribute.\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5840/5841/5842/5860\n\n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_DISABLE',
                    '0 (0x0)',
                    'The RF In local oscillator signal is not present at the front panel LO OUT connector.'
                ],
                [
                    'NIRFSG_VAL_ENABLE',
                    '1 (0x1)',
                    'The RF In local oscillator signal is present at the front panel LO OUT connector.'
                ],
                [
                    'NIRFSG_VAL_UNSPECIFIED',
                    '-2 (-0x2)',
                    'The RF IN local oscillator signal may or may not be present at the front panel LO OUT connector, because NI-RFSA may be controlling it.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'DirectDownload',
        'lv_property': 'Arb:Data Transfer:Direct Download',
        'name': 'DIRECT_DOWNLOAD',
        'type': 'ViInt32'
    },
    1150043: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies how NI-RFSG interprets the value of the NIRFSG_ATTR_POWER_LEVEL attribute. The NIRFSG_ATTR_POWER_LEVEL_TYPE attribute also affects how waveforms are scaled.\n\n                PXI-5670/5671: While in Script generation mode, if this attribute is set to NIRFSG_VAL_AVERAGE_POWER, NI-RFSG scales each waveform so that all waveforms have the same average power. The average power level of each waveform matches the value set with the NIRFSG_ATTR_POWER_LEVEL attribute. You can disable this scaling operation by setting the NIRFSG_ATTR_POWER_LEVEL_TYPE attribute to NIRFSG_VAL_PEAK_POWER.\n\n                PXIe-5644/5645/5646, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860: While in Script generation mode, this attribute must be set to NIRFSG_VAL_PEAK_POWER.\n\n                Converting from Average Power to Peak Power\n\n                Typically, this attribute is set to NIRFSG_VAL_AVERAGE_POWER. However, some instrument modes require this attribute to be set to NIRFSG_VAL_PEAK_POWER. Use the following equations to calculate the equivalent peak power given the desired average power for your waveform:\n\n\n                Where 1 is the highest possible magnitude in the waveform.\n\n\n\n                **Default Value:**\n\n                PXIe-5820: NIRFSG_VAL_PEAK_POWER\n\n                All other devices: NIRFSG_VAL_AVERAGE_POWER\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Spurious Performance <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/spurious_performance.html>`_\n\n                `Optimizing for Low Power Generation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/optimizing_for_low_power_generation.html>`_\n                \n                **High-Level Functions**:\n\n                - nirfsg_ConfigurePowerLevelType   \n            \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_AVERAGE_POWER',
                    'Indicates the desired power averaged in time. The driver maximizes the dynamic range by scaling the I/Q waveform so that its peak magnitude is equal to one. If your write more than one waveform, NI-RFSG scales each waveform without preserving the power level ratio between the waveforms. This value is not valid for the PXIe-5820.'
                ],
                [
                    'NIRFSG_VAL_PEAK_POWER',
                    'Indicates the maximum power level of the RF signal averaged over one period of the RF carrier frequency (the peak envelope power). This setting requires that the magnitude of the I/Q waveform must always be less than or equal to one. When using peak power, the power level of the RF signal matches the specified power level at moments when the magnitude of the I/Q waveform equals one. If you write more than one waveform, the relative scaling between waveforms is preserved. In peak power mode, waveforms are scaled according to the NIRFSG_ATTR_ARB_WAVEFORM_SOFTWARE_SCALING_FACTOR attribute. You can use the NIRFSG_ATTR_PEAK_POWER_ADJUSTMENT attribute in conjunction with the NIRFSG_ATTR_POWER_LEVEL attribute when the NIRFSG_ATTR_POWER_LEVEL_TYPE attribute is set to NIRFSG_VAL_PEAK_POWER.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'enum': 'PowerLevelType',
        'lv_property': 'RF:Power Level Type',
        'name': 'POWER_LEVEL_TYPE',
        'type': 'ViInt32'
    },
    1150044: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Enables or disables digital pattern on the PXI-5421/5441 AWG module. This attribute must be set to VI_TRUE to enable signal routing to and from the Digital Data & Control connector.\n\n                To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                **Default Value:** VI_FALSE\n\n                **Supported Devices:** PXI-5670/5671\n            \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'VI_TRUE',
                    'Signal routing enabled.'
                ],
                [
                    'VI_FALSE',
                    'Signal routing disabled.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'lv_property': 'Arb:Digital Pattern',
        'name': 'DIGITAL_PATTERN',
        'type': 'ViBoolean'
    },
    1150045: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Enables and disables continuous streaming of waveform data.\n\n                **Default Value:** VI_FALSE\n\n                **Supported Devices:** PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Streaming <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/streaming.html>`_\n            \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'VI_TRUE',
                    'Streaming is enabled.'
                ],
                [
                    'VI_FALSE',
                    'Streaming is disabled.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'lv_property': 'Arb:Data Transfer:Streaming:Streaming Enabled',
        'name': 'STREAMING_ENABLED',
        'type': 'ViBoolean'
    },
    1150046: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the name of the waveform used to continually stream data during generation.\n\n                **Default Value:** "" (empty string)\n\n                **Supported Devices:** PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Streaming <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/streaming.html>`_\n\n                `Streaming Waveform Data <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/streaming_waveform_data.html>`_\n                '
        },
        'lv_property': 'Arb:Data Transfer:Streaming:Streaming Waveform Name',
        'name': 'STREAMING_WAVEFORM_NAME',
        'type': 'ViString'
    },
    1150047: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Indicates the space available, in samples, in the streaming waveform for writing new data. For optimal performance, write new data to the waveform in a fixed size that is an integer divisor of the total size of the streaming waveform. This waveform size ensures that writes do not have to wrap around from the end to the beginning of the waveform buffer.\n\n                To read this attribute, the NI-RFSG device must be in the Committed state.\n\n                **Units**: samples\n\n                **Supported Devices:** PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Streaming <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/streaming.html>`_\n                '
        },
        'lv_property': 'Arb:Data Transfer:Streaming:Space Available In Streaming Waveform (Samples)',
        'name': 'STREAMING_SPACE_AVAILABLE_IN_WAVEFORM',
        'type': 'ViInt64'
    },
    1150048: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Indicates the number of samples to transfer at one time from the device to host memory. This attribute is useful when the total data to be transferred to onboard memory is large.\n\n                **Units**: samples (s)\n\n                **Default Value**: 1Ms\n\n                **Supported Devices:** PXIe-5672/5673/5673E\n                '
        },
        'lv_property': 'Arb:Data Transfer:Data Transfer Block Size',
        'name': 'DATA_TRANSFER_BLOCK_SIZE',
        'type': 'ViInt32'
    },
    1150052: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies how much to scale the data before writing it with the nirfsg_WriteArbWaveform function. The resulting waveform must be smaller than 1.0 in complex magnitude. This attribute is supported only if you set the NIRFSG_ATTR_POWER_LEVEL_TYPE attribute to NIRFSG_VAL_PEAK_POWER.\n\n                **Default Value:** 1.0\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Spurious Performance <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/spurious_performance.html>`_\n                '
        },
        'lv_property': 'Arb:Software Scaling Factor',
        'name': 'ARB_WAVEFORM_SOFTWARE_SCALING_FACTOR',
        'type': 'ViReal64'
    },
    1150053: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the destination terminal for exporting the Reference Clock on the RF signal generators. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                **Default Value:** NIRFSG_VAL_DO_NOT_EXPORT_STR\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Interconnecting Multiple NI 5673E Modules <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/interconnecting_multiple_ni_5673_modules.html>`_\n             \n            **Defined Values**:\n\nName (Value): Description\n\nNIRFSG_VAL_DO_NOT_EXPORT_STR () :The Reference Clock signal is not exported.\n\nNIRFSG_VAL_REF_OUT_STR (RefOut) :Exports the Reference Clock signal to the REF OUT connector of the device.\n\nNIRFSG_VAL_REF_OUT2_STR (RefOut2) :Exports the Reference Clock signal to the REF OUT2 connector of the device, if applicable.\n\nNIRFSG_VAL_CLK_OUT_STR (ClkOut) :Exports the Reference Clock signal to the CLK OUT connector of the device.\n            ',
            'note': 'The NIRFSG_VAL_REF_OUT2_STR output terminal value is valid for only the PXIe-5650/5651/5652, not the PXI-5650/5651/5652.',
            'table_body': [
                [
                    'NIRFSG_VAL_CLK_OUT_STR',
                    'ClkOut',
                    'Exports the Reference Clock signal to the CLK OUT connector of the device.',
                    'Supported on PXIe-5673, 5673E'
                ],
                [
                    'NIRFSG_VAL_DO_NOT_EXPORT_STR',
                    '',
                    'The Reference Clock signal is not exported.',
                    'Supported on PXIe-5644/5645/5646, 5820/5830/5831/5832/5840/5841/5842/5860, 5650/5651/5652, 5654, 5673, 5673E, PXIe-5654 with PXIe-5696, PXI-5650/5651/5652 (See Note)'
                ],
                [
                    'NIRFSG_VAL_REF_OUT_STR',
                    'RefOut',
                    'Exports the Reference Clock signal to the REF OUT connector of the device.',
                    'Supported on PXIe-5644/5645/5646, 5820/5830/5831/5832/5840/5841/5842/5860, 5650/5651/5653, 5653, 5654, 5673, 5673E, PXIe-5654 with PXIe-5696, PXI-5650/5651/5653, '
                ],
                [
                    'NIRFSG_VAL_REF_OUT2_STR',
                    'RefOut2',
                    'Exports the Reference Clock signal to the REF OUT2 connector of the device, if applicable.',
                    'Supported on PXIe-5650/5651/5652, 5654, 5673E, PXIe-5654 with PXIe-5696'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description',
                'Supported devices'
            ]
        },
        'enum': 'ReferenceClockExportOutputTerminal',
        'lv_property': 'Clock:Reference Clock Export Output Terminal',
        'name': 'EXPORTED_REF_CLOCK_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150054: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the source terminal for the Script Trigger. This attribute is used when the NIRFSG_ATTR_SCRIPT_TRIGGER_TYPE attribute is set to NIRFSG_VAL_DIGITAL_LEVEL. The NIRFSG_ATTR_DIGITAL_LEVEL_SCRIPT_TRIGGER_SOURCE attribute is not case-sensitive.\n\n                To set the NIRFSG_ATTR_DIGITAL_LEVEL_SCRIPT_TRIGGER_SOURCE attribute, the NI-RFSG device must be in the Configuration state.\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_\n\n                `PFI Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pfi_lines.html>`_\n\n                `PXI Trigger Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_trigger.html>`_\n            \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_PFI0_STR',
                    'PFI0',
                    'The trigger is received on PFI 0.'
                ],
                [
                    'NIRFSG_VAL_PFI1_STR',
                    'PFI1',
                    'The trigger is received on PFI 1.'
                ],
                [
                    'NIRFSG_VAL_PFI2_STR',
                    'PFI2',
                    'The trigger is received on PFI 2.'
                ],
                [
                    'NIRFSG_VAL_PFI3_STR',
                    'PFI3',
                    'The trigger is received on PFI 3.'
                ],
                [
                    'NIRFSG_VAL_PXI_STAR_STR',
                    'PXI_Star',
                    'The trigger is received on the PXI star trigger line. This value is not valid for the PXIe-5644/5645/5646.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG0_STR',
                    'PXI_Trig0',
                    'The trigger is received on PXI trigger line 0.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG1_STR',
                    'PXI_Trig1',
                    'The trigger is received on PXI trigger line 1.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG2_STR',
                    'PXI_Trig2',
                    'The trigger is received on PXI trigger line 2.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG3_STR',
                    'PXI_Trig3',
                    'The trigger is received on PXI trigger line 3.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG4_STR',
                    'PXI_Trig4',
                    'The trigger is received on PXI trigger line 4.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG5_STR',
                    'PXI_Trig5',
                    'The trigger is received on PXI trigger line 5.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG6_STR',
                    'PXI_Trig6',
                    'The trigger is received on PXI trigger line 6.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG7_STR',
                    'PXI_Trig7',
                    'The trigger is received on PXI trigger line 7.'
                ],
                [
                    'NIRFSG_VAL_PXIE_DSTARB_STR',
                    'PXIe_DStarB',
                    'The trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860.'
                ],
                [
                    'NIRFSG_VAL_PULSE_IN_STR',
                    'PulseIn',
                    'The trigger is received on the PULSE IN terminal. This value is valid on only the PXIe-5842.'
                ],
                [
                    'NIRFSG_VAL_DIO0_STR',
                    'DIO/PFI0',
                    'The trigger is received on PFI0 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO1_STR',
                    'DIO/PFI1',
                    'The trigger is received on PFI1 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO2_STR',
                    'DIO/PFI2',
                    'The trigger is received on PFI2 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO3_STR',
                    'DIO/PFI3',
                    'The trigger is received on PFI3 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO4_STR',
                    'DIO/PFI4',
                    'The trigger is received on PFI4 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO5_STR',
                    'DIO/PFI5',
                    'The trigger is received on PFI5 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO6_STR',
                    'DIO/PFI6',
                    'The trigger is received on PFI6 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO7_STR',
                    'DIO/PFI7',
                    'The trigger is received on PFI7 from the front panel DIO terminal.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'ScriptTrigDigLevelSource',
        'lv_property': 'Triggers:Script:Digital Level:Source',
        'name': 'DIGITAL_LEVEL_SCRIPT_TRIGGER_SOURCE',
        'supported_rep_caps': [
            'script_triggers'
        ],
        'type': 'ViString'
    },
    1150055: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the active level for the Script Trigger. This attribute is used when the NIRFSG_ATTR_SCRIPT_TRIGGER_TYPE attribute is set to NIRFSG_VAL_DIGITAL_LEVEL.\n\n                **Default Value:** NIRFSG_VAL_ACTIVE_HIGH\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n\n\n                **Related Topics**\n\n                `Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_\n\n                `Digital Level Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_level.html>`_\n            \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_ACTIVE_HIGH',
                    '9000 (0x2328)',
                    'Trigger when the digital trigger signal is high.'
                ],
                [
                    'NIRFSG_VAL_ACTIVE_LOW',
                    '9001 (0x2329)',
                    'Trigger when the digital trigger signal is low.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'ScriptTrigDigLevelActiveLevel',
        'lv_property': 'Triggers:Script:Digital Level:Active Level',
        'name': 'DIGITAL_LEVEL_SCRIPT_TRIGGER_ACTIVE_LEVEL',
        'supported_rep_caps': [
            'script_triggers'
        ],
        'type': 'ViInt32'
    },
    1150056: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the pulse-shaping filter type for the FIR filter. You can use this attribute only with signal generators that support onboard signal processing (OSP). NI-RFSG returns an error if you use this attribute with a device that does not support OSP.\n\n                **Default Value:** NIRFSG_VAL_NONE\n\n                **Supported Devices:** PXI-5670/5671, PXIe-5672/5673/5673E\n\n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_NONE',
                    '0 (0x0)',
                    'Disables analog modulation.'
                ],
                [
                    'NIRFSG_VAL_ARB_FILTER_TYPE_RAISED_COSINE',
                    '10002 (0x2712)',
                    'Applies a raised cosine filter to the data with the alpha value specified with the NIRFSG_ATTR_ARB_FILTER_RAISED_COSINE_ALPHA attribute.'
                ],
                [
                    'NIRFSG_VAL_ARB_FILTER_TYPE_ROOT_RAISED_COSINE',
                    '10001 (0x2711)',
                    'Applies a root-raised cosine filter to the data with the alpha value specified with the NIRFSG_ATTR_ARB_FILTER_ROOT_RAISED_COSINE_ALPHA attribute.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'FilterType',
        'lv_property': 'Arb:Pulse Shaping:Filter Type',
        'name': 'ARB_FILTER_TYPE',
        'type': 'ViInt32'
    },
    1150057: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the alpha value to use when calculating the pulse-shaping FIR filter coefficients. You can use this attribute only when the NIRFSG_ATTR_ARB_FILTER_TYPE attribute is set to NIRFSG_VAL_ARB_FILTER_TYPE_ROOT_RAISED_COSINE and with signal generators that support onboard signal processing (OSP). NI-RFSG returns an error if you use this attribute with a device that does not support OSP.\n\n                **Supported Devices:** PXI-5671, PXIe-5672/5673/5673E\n                '
        },
        'lv_property': 'Arb:Pulse Shaping:Root Raised Cosine Alpha',
        'name': 'ARB_FILTER_ROOT_RAISED_COSINE_ALPHA',
        'type': 'ViReal64'
    },
    1150060: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the alpha value to use when calculating the pulse-shaping filter coefficients. You can use this attribute only when the NIRFSG_ATTR_ARB_FILTER_TYPE attribute is set to NIRFSG_VAL_ARB_FILTER_TYPE_RAISED_COSINE and with signal generators that support onboard signal processing (OSP). NI-RFSG returns an error if you use this attribute with a device that does not support OSP.\n\n                **Supported Devices:** PXI-5671, PXIe-5672/5673/5673E\n                '
        },
        'lv_property': 'Arb:Pulse Shaping:Raised Cosine Alpha',
        'name': 'ARB_FILTER_RAISED_COSINE_ALPHA',
        'type': 'ViReal64'
    },
    1150061: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                The total amount of memory on the signal generator in bytes.\n\n                **Units:** bytes\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Memory Options <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/memory_options.html>`_\n\n                `Phase Continuity <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/phasecontinuity.html>`_\n            ',
            'note': 'Not all onboard memory is available for waveform storage. A portion of onboard memory stores scripts that specify how the waveforms are generated. These scripts typically require less than 1KB of onboard memory.'
        },
        'lv_property': 'Arb:Memory Size',
        'name': 'MEMORY_SIZE',
        'type': 'ViInt64'
    },
    1150062: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the `deviation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/glossary.html>`_ to use in phase modulation, in degrees.\n\n                **Units**: degrees (°)\n\n                **Default Value:** 90°\n\n                **Supported Devices:** PXI/PXIe-5650/5651/5652, PXIe-5653\n\n                **Related Topics**\n\n                `Modulation Schemes <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/modulation_modes.html>`_\n                '
        },
        'lv_property': 'Modulation:Analog:PM Deviation (Degrees)',
        'name': 'ANALOG_MODULATION_PM_DEVIATION',
        'type': 'ViReal64'
    },
    1150063: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the destination terminal for exporting the Done event. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Triggers <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/triggers.html>`_\n\n                `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_\n\n                `PFI Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pfi_lines.html>`_\n\n                `PXI Trigger Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_trigger.html>`_\n                \n                **High-Level Functions**:\n\n                - nirfsg_ExportSignal\n                \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_DO_NOT_EXPORT_STR',
                    '',
                    'The signal is not exported.'
                ],
                [
                    'NIRFSG_VAL_PFI0_STR',
                    'PFI0',
                    'The signal is exported to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0.'
                ],
                [
                    'NIRFSG_VAL_PFI1_STR',
                    'PFI1',
                    'The signal is exported to the PFI 1 connector.'
                ],
                [
                    'NIRFSG_VAL_PFI4_STR',
                    'PFI4',
                    'The signal is exported to the PFI 4 connector.'
                ],
                [
                    'NIRFSG_VAL_PFI5_STR',
                    'PFI5',
                    'The signal is exported to the PFI 5 connector.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG0_STR',
                    'PXI_Trig0',
                    'The trigger is received on PXI trigger line 0.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG1_STR',
                    'PXI_Trig1',
                    'The trigger is received on PXI trigger line 1.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG2_STR',
                    'PXI_Trig2',
                    'The trigger is received on PXI trigger line 2.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG3_STR',
                    'PXI_Trig3',
                    'The trigger is received on PXI trigger line 3.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG4_STR',
                    'PXI_Trig4',
                    'The trigger is received on PXI trigger line 4.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG5_STR',
                    'PXI_Trig5',
                    'The trigger is received on PXI trigger line 5.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG6_STR',
                    'PXI_Trig6',
                    'The trigger is received on PXI trigger line 6.'
                ],
                [
                    'NIRFSG_VAL_PXIE_DSTARC_STR',
                    'PXIe_DStarC',
                    'The signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841.'
                ],
                [
                    'NIRFSG_VAL_DIO0_STR',
                    'DIO/PFI0',
                    'The trigger is received on PFI0 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO1_STR',
                    'DIO/PFI1',
                    'The trigger is received on PFI1 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO2_STR',
                    'DIO/PFI2',
                    'The trigger is received on PFI2 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO3_STR',
                    'DIO/PFI3',
                    'The trigger is received on PFI3 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO4_STR',
                    'DIO/PFI4',
                    'The trigger is received on PFI4 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO5_STR',
                    'DIO/PFI5',
                    'The trigger is received on PFI5 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO6_STR',
                    'DIO/PFI6',
                    'The trigger is received on PFI6 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO7_STR',
                    'DIO/PFI7',
                    'The trigger is received on PFI7 from the front panel DIO terminal.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'DoneEventExportOutputTerm',
        'lv_property': 'Events:Done Event Export Output Terminal',
        'name': 'EXPORTED_DONE_EVENT_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150064: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the destination terminal for exporting the Marker Event. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Marker Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/marker_events.html>`_\n\n                `PFI Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pfi_lines.html>`_\n\n                `PXI Trigger Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_trigger.html>`_\n                \n                **High-Level Functions**:\n\n                - nirfsg_ExportSignal\n                \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_DO_NOT_EXPORT_STR',
                    '',
                    'The signal is not exported.'
                ],
                [
                    'NIRFSG_VAL_PFI0_STR',
                    'PFI0',
                    'The signal is exported to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0.'
                ],
                [
                    'NIRFSG_VAL_PFI1_STR',
                    'PFI1',
                    'The signal is exported to the PFI 1 connector.'
                ],
                [
                    'NIRFSG_VAL_PFI4_STR',
                    'PFI4',
                    'The signal is exported to the PFI 4 connector.'
                ],
                [
                    'NIRFSG_VAL_PFI5_STR',
                    'PFI5',
                    'The signal is exported to the PFI 5 connector.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG0_STR',
                    'PXI_Trig0',
                    'The trigger is received on PXI trigger line 0.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG1_STR',
                    'PXI_Trig1',
                    'The trigger is received on PXI trigger line 1.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG2_STR',
                    'PXI_Trig2',
                    'The trigger is received on PXI trigger line 2.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG3_STR',
                    'PXI_Trig3',
                    'The trigger is received on PXI trigger line 3.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG4_STR',
                    'PXI_Trig4',
                    'The trigger is received on PXI trigger line 4.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG5_STR',
                    'PXI_Trig5',
                    'The trigger is received on PXI trigger line 5.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG6_STR',
                    'PXI_Trig6',
                    'The trigger is received on PXI trigger line 6.'
                ],
                [
                    'NIRFSG_VAL_PXIE_DSTARC_STR',
                    'PXIe_DStarC',
                    'The signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841.'
                ],
                [
                    'NIRFSG_VAL_DIO0_STR',
                    'DIO/PFI0',
                    'The trigger is received on PFI0 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO1_STR',
                    'DIO/PFI1',
                    'The trigger is received on PFI1 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO2_STR',
                    'DIO/PFI2',
                    'The trigger is received on PFI2 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO3_STR',
                    'DIO/PFI3',
                    'The trigger is received on PFI3 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO4_STR',
                    'DIO/PFI4',
                    'The trigger is received on PFI4 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO5_STR',
                    'DIO/PFI5',
                    'The trigger is received on PFI5 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO6_STR',
                    'DIO/PFI6',
                    'The trigger is received on PFI6 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO7_STR',
                    'DIO/PFI7',
                    'The trigger is received on PFI7 from the front panel DIO terminal.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'MarkerEventExportOutputTerm',
        'lv_property': 'Events:Marker:Output Terminal',
        'name': 'EXPORTED_MARKER_EVENT_OUTPUT_TERMINAL',
        'repeated_capability_type': 'markers',
        'supported_rep_caps': [
            'markers'
        ],
        'type': 'ViString'
    },
    1150065: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the destination terminal for exporting the Started event. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_\n\n                `PFI Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pfi_lines.html>`_\n\n                `PXI Trigger Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_trigger.html>`_\n                \n                **High-Level Functions**:\n\n                - nirfsg_ExportSignal\n                \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_DO_NOT_EXPORT_STR',
                    '',
                    'The signal is not exported.'
                ],
                [
                    'NIRFSG_VAL_PFI0_STR',
                    'PFI0',
                    'The signal is exported to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0.'
                ],
                [
                    'NIRFSG_VAL_PFI1_STR',
                    'PFI1',
                    'The signal is exported to the PFI 1 connector.'
                ],
                [
                    'NIRFSG_VAL_PFI4_STR',
                    'PFI4',
                    'The signal is exported to the PFI 4 connector.'
                ],
                [
                    'NIRFSG_VAL_PFI5_STR',
                    'PFI5',
                    'The signal is exported to the PFI 5 connector.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG0_STR',
                    'PXI_Trig0',
                    'The trigger is received on PXI trigger line 0.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG1_STR',
                    'PXI_Trig1',
                    'The trigger is received on PXI trigger line 1.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG2_STR',
                    'PXI_Trig2',
                    'The trigger is received on PXI trigger line 2.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG3_STR',
                    'PXI_Trig3',
                    'The trigger is received on PXI trigger line 3.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG4_STR',
                    'PXI_Trig4',
                    'The trigger is received on PXI trigger line 4.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG5_STR',
                    'PXI_Trig5',
                    'The trigger is received on PXI trigger line 5.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG6_STR',
                    'PXI_Trig6',
                    'The trigger is received on PXI trigger line 6.'
                ],
                [
                    'NIRFSG_VAL_PXIE_DSTARC_STR',
                    'PXIe_DStarC',
                    'The signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860.'
                ],
                [
                    'NIRFSG_VAL_DIO0_STR',
                    'DIO/PFI0',
                    'The trigger is received on PFI0 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO1_STR',
                    'DIO/PFI1',
                    'The trigger is received on PFI1 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO2_STR',
                    'DIO/PFI2',
                    'The trigger is received on PFI2 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO3_STR',
                    'DIO/PFI3',
                    'The trigger is received on PFI3 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO4_STR',
                    'DIO/PFI4',
                    'The trigger is received on PFI4 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO5_STR',
                    'DIO/PFI5',
                    'The trigger is received on PFI5 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO6_STR',
                    'DIO/PFI6',
                    'The trigger is received on PFI6 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO7_STR',
                    'DIO/PFI7',
                    'The trigger is received on PFI7 from the front panel DIO terminal.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'StartedEventExportOutputTerm',
        'lv_property': 'Events:Started Event Export Output Terminal',
        'name': 'EXPORTED_STARTED_EVENT_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150066: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the power level of the signal at the LO OUT front panel connector.\n\n                To use this attribute for the PXIe-5830/5831/5832, you must use the channelName parameter of the nirfsg_SetAttributeViReal64 function to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).\n\n                **Units**: dBm\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5830/5831/5832/5840/5841/5842\n\n                **Related Topics**\n\n                `LO OUT <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/loout.html>`_\n            ',
            'note': 'For the PXIe-5644/5645/5646 and PXIe-5673/5673E, this attribute is always read-only.'
        },
        'lv_property': 'RF:LO Out Power (dBm)',
        'name': 'LO_OUT_POWER',
        'type': 'ViReal64'
    },
    1150067: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the power level of the signal at the LO IN front panel connector.\n\n                To use this attribute for the PXIe-5830/5831/5832, you must use the channelName parameter of the nirfsg_SetAttributeViReal64 function to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).\n\n                **Units**: dBm\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5830/5831/5832/5840/5841/5842\n\n                **Related Topics**\n\n                `LO OUT <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/loout.html>`_\n            ',
            'note': '- This attribute is read/write if you are using an external LO. Otherwise, this attribute is read-only.\n\n - For the PXIe-5644/5645/5646, this attribute is always read-only.'
        },
        'lv_property': 'RF:LO In Power (dBm)',
        'name': 'LO_IN_POWER',
        'type': 'ViReal64'
    },
    1150068: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns the AWG module temperature in degrees Celsius.\n\n                PXIe-5820/5840/5841/5842: If you query this attribute during RF list mode, list steps may take longer to complete during list execution.\n\n                **Units**: degrees Celsius (°C)\n\n                **Supported Devices:** PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5840/5841/5842/5860\n                '
        },
        'lv_property': 'Device Characteristics:AWG Temperature (Degrees C)',
        'name': 'ARB_TEMPERATURE',
        'type': 'ViReal64'
    },
    1150069: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Enables or disables I/Q impairment. The NIRFSG_ATTR_IQ_I_OFFSET, NIRFSG_ATTR_IQ_Q_OFFSET, NIRFSG_ATTR_IQ_GAIN_IMBALANCE, and NIRFSG_ATTR_IQ_SKEW attributes are ignored when the NIRFSG_ATTR_IQ_IMPAIRMENT_ENABLED attribute is disabled.\n\n                **Default Value:** VI_TRUE\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842\n            \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'VI_TRUE',
                    'I/Q impairment is enabled.'
                ],
                [
                    'VI_FALSE',
                    'I/Q impairment is disabled.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'lv_property': 'IQ Impairment:Enabled',
        'name': 'IQ_IMPAIRMENT_ENABLED',
        'type': 'ViBoolean'
    },
    1150070: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                When using a National Instruments AWG module or vector signal transceiver (VST), this attribute specifies the I-signal DC offset. Units are either percent (%) or volts (V), depending on the NIRFSG_ATTR_IQ_OFFSET_UNITS attribute setting.\n\n                PXIe-5673/5673E: Actual AWG signal offset is equal to the I/Q modulator offset correction plus the value specified by this attribute. When using an external AWG (non–National Instruments AWG), this attribute is read-only and indicates the I/Q modulator I-offset. Units are volts, as specified by the NIRFSG_ATTR_IQ_OFFSET_UNITS attribute.\n\n                **Valid Values:**-100 to 100% or -0.2V to 0.2V\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842\n\n                **Related Topics**\n\n                `Impairment Calibration <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/vector_calibration.html>`_\n                '
        },
        'lv_property': 'IQ Impairment:I Offset',
        'name': 'IQ_I_OFFSET',
        'type': 'ViReal64'
    },
    1150071: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                When using a National Instruments AWG module or VST device, this attribute specifies the Q-signal DC offset. Units are either percent (%) or volts (V), depending on the NIRFSG_ATTR_IQ_OFFSET_UNITS attribute setting.\n\n                PXIe-5673/5673E: Actual AWG signal offset is equal to the I/Q modulator offset correction plus the value specified by this attribute. When using an external AWG (non–National Instruments AWG), the NIRFSG_ATTR_IQ_Q_OFFSET attribute is read-only and indicates the I/Q modulator Q-offset. Units are volts, as indicated by the NIRFSG_ATTR_IQ_OFFSET_UNITS attribute.\n\n                **Valid Values**: -100% to 100% or -0.2V to 0.2V\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842\n\n                **Related Topics**\n\n                `Impairment Calibration <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/vector_calibration.html>`_\n                '
        },
        'lv_property': 'IQ Impairment:Q Offset',
        'name': 'IQ_Q_OFFSET',
        'type': 'ViReal64'
    },
    1150072: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the gain imbalance of the I/Q modulator (I versus Q).\n\n                Gain imbalance is calculated with the following equation:\n\n\n                **Units**: dB\n\n                **Valid Values:**-6dB to 6dB\n\n                **Default Value:** 0dB\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842\n\n                **Related Topics**\n\n                `Impairment Calibration <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/vector_calibration.html>`_\n\n                `Spurious Performance <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/spurious_performance.html>`_\n                '
        },
        'lv_property': 'IQ Impairment:Gain Imbalance (dB)',
        'name': 'IQ_GAIN_IMBALANCE',
        'type': 'ViReal64'
    },
    1150073: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the adjustment of the phase angle between the I and Q vectors. If the skew is zero, the phase angle is 90 degrees.\n\n                This attribute is ignored when the NIRFSG_ATTR_IQ_IMPAIRMENT_ENABLED attribute is disabled.\n\n                **Units**: degrees (°)\n\n                **Valid Values:**-30° to 30°\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842\n\n                **Related Topics**\n\n                `Impairment Calibration <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/vector_calibration.html>`_\n                '
        },
        'lv_property': 'IQ Impairment:IQ Skew (Degrees)',
        'name': 'IQ_SKEW',
        'type': 'ViReal64'
    },
    1150075: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns the LO module temperature in degrees Celsius.\n\n                PXIe-5840/5841: If you query this attribute during RF list mode, list steps may take longer to complete during list execution.\n\n                **Units**: degrees Celsius (°C)\n\n                **Supported Devices:** PXIe-5673/5673E, PXIe-5840/5841/5842\n                '
        },
        'lv_property': 'Device Characteristics:LO Temperature (Degrees C)',
        'name': 'LO_TEMPERATURE',
        'type': 'ViReal64'
    },
    1150076: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns the recommended interval between each external calibration of the device.\n\n                **Units**: months\n\n                **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n                '
        },
        'lv_property': 'External Calibration:Recommended Interval',
        'name': 'EXTERNAL_CALIBRATION_RECOMMENDED_INTERVAL',
        'type': 'ViInt32'
    },
    1150077: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns the temperature of the device at the time of the last external calibration.\n\n                **Units**: degrees Celsius (°C)\n\n                **Supported Devices:** PXI-5610, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E\n                '
        },
        'lv_property': 'External Calibration:Last External Calibration Temperature',
        'name': 'EXTERNAL_CALIBRATION_TEMPERATURE',
        'type': 'ViReal64'
    },
    1150081: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the units of the NIRFSG_ATTR_IQ_I_OFFSET attribute and NIRFSG_ATTR_IQ_Q_OFFSET attribute. Offset units are either percent or volts.\n\n                The AWG or VST offset is the specified percentage of the AWG or VST peak power level when the NIRFSG_ATTR_IQ_OFFSET_UNITS attribute is set to NIRFSG_VAL_PERCENT. Given perfect carrier leakage suppression, the following equation is satisfied\n                \n\n                or equivalently\n\n\n                If the NIRFSG_ATTR_IQ_I_OFFSET attribute is set to 100%, NIRFSG_ATTR_IQ_Q_OFFSET attribute is set to 0%, and NIRFSG_ATTR_POWER_LEVEL attribute set to 0 dBm, the desired RF signal is at 0 dBm and the carrier leakage is also at 0 dBm.\n\n                The AWG or VST peak power level changes when settings change in other attributes such as the NIRFSG_ATTR_POWER_LEVEL, NIRFSG_ATTR_FREQUENCY, NIRFSG_ATTR_IQ_SKEW, NIRFSG_ATTR_IQ_GAIN_IMBALANCE, NIRFSG_ATTR_ATTENUATOR_HOLD_ENABLED, and NIRFSG_ATTR_ARB_PRE_FILTER_GAIN attributes. When the NIRFSG_ATTR_IQ_OFFSET_UNITS attribute is set to NIRFSG_VAL_PERCENT, the actual AWG or VST offset changes as the AWG or VST peak power level changes to satisfy the preceding equations. These changes are useful if you are intentionally adding carrier leakage to test the tolerance of a receiver. When the NIRFSG_ATTR_IQ_OFFSET_UNITS attribute is set to NIRFSG_VAL_PERCENT, the carrier leakage, in dBc, remains at a consistent level.\n\n                If you are trying to eliminate residual carrier leakage due to calibration inaccuracies or drift, set the NIRFSG_ATTR_IQ_OFFSET_UNITS attribute to NIRFSG_VAL_VOLTS. Offset correction voltage is applied to the I/Q modulator or VST, regardless of changes to the AWG or VST peak power level.\n\n                **Default Value**: NIRFSG_VAL_PERCENT\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842\n            \n            **Defined Values**:\n            ',
            'note': 'For any devices except PXIe-5820, if the NIRFSG_ATTR_IQ_OFFSET_UNITS attribute is set to NIRFSG_VAL_VOLTS, a 0.1 I offset results in a 0.1 V offset in the output. For PXIe-5820 devices, 0.1 I offset results in a 10% offset in the output.',
            'table_body': [
                [
                    'NIRFSG_VAL_PERCENT',
                    'Specifies the NIRFSG_ATTR_IQ_I_OFFSET and NIRFSG_ATTR_IQ_Q_OFFSET attribute units as percent.'
                ],
                [
                    'NIRFSG_VAL_VOLTS',
                    'Specifies the NIRFSG_ATTR_IQ_I_OFFSET and NIRFSG_ATTR_IQ_Q_OFFSET attribute units as volts.'
                ]
            ],
            'table_header': [
                'Name',
                'Description'
            ]
        },
        'enum': 'OffsetUnits',
        'lv_property': 'IQ Impairment:Offset Units',
        'name': 'IQ_OFFSET_UNITS',
        'type': 'ViInt32'
    },
    1150082: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the interpretation of the value passed to the NIRFSG_ATTR_FREQUENCY_SETTLING attribute.\n\n                PXIe-5650/5651/5652/5653, PXIe-5673E: When the NIRFSG_ATTR_ACTIVE_CONFIGURATION_LIST attribute is set to a valid list name, the NIRFSG_ATTR_FREQUENCY_SETTLING_UNITS attribute supports only NIRFSG_VAL_TIME_AFTER_IO as a valid value.\n\n                PXIe-5654/5654 with PXIe-5696: The NIRFSG_ATTR_FREQUENCY_SETTLING_UNITS attribute supports only NIRFSG_VAL_TIME_AFTER_IO and NIRFSG_VAL_PPM as valid values.\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXIe-5673/5673E, PXIe-5830/5831/5832/5840/5841/5842\n\n                **Default Value**: NIRFSG_VAL_PPM\n\n                **Related Topics**\n\n                `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_\n\n            **Defined Values**:\n            ',
            'note': 'If you set this attribute to NIRFSG_VAL_TIME_AFTER_IO, the definition of settled for the Configuration Settled event changes.',
            'table_body': [
                [
                    'NIRFSG_VAL_TIME_AFTER_LOCK',
                    'Specifies the time to wait after the frequency PLL locks.'
                ],
                [
                    'NIRFSG_VAL_TIME_AFTER_IO',
                    'Specifies the time to wait after all writes occur to change the frequency.'
                ],
                [
                    'NIRFSG_VAL_PPM',
                    'Specifies the minimum frequency accuracy when settling completes. Units are in parts per million (PPM or 1E-6).'
                ]
            ],
            'table_header': [
                'Name',
                'Description'
            ]
        },
        'enum': 'FrequencySettlingUnits',
        'lv_property': 'RF:Frequency Settling Units',
        'name': 'FREQUENCY_SETTLING_UNITS',
        'type': 'ViInt32'
    },
    1150083: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the frequency settling time. Interpretation of this value depends on the NIRFSG_ATTR_FREQUENCY_SETTLING_UNITS attribute.\n\n                **Valid Values:**\n\n                The valid values for this attribute depend on the NIRFSG_ATTR_FREQUENCY_SETTLING_UNITS attribute.\n\n                \n\n\n                **Default Value**: 1.0\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXIe-5673/5673E, PXIe-5830/5831/5832/5840/5841/5842\n\n                **Related Topics**\n\n                `Settling Times <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/settling_times.html>`_\n\n                `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_\n                '
        },
        'lv_property': 'RF:Frequency Settling',
        'name': 'FREQUENCY_SETTLING',
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    1150084: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns the module revision letter. If the NI-RFSG session is controlling multiple modules, this attribute returns the revision letter of the primary RF module. The NI-RFSG session is opened using the primary RF device name.\n\n                **Supported Devices:** PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Identifying Module Revision <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/identifying_device_revision.html>`_\n                '
        },
        'lv_property': 'Device Characteristics:Module Revision',
        'name': 'MODULE_REVISION',
        'type': 'ViString'
    },
    1150085: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the external amplification or attenuation, if any, between the RF signal generator and the device under test.\n\n                Positive values for this attribute represent amplification, and negative values for this attribute represent attenuation.\n\n                **Valid Values:** -INF dB to +INF dB\n\n                **Default Value:** 0dB\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXIe-5654/5654 with PXIe-5696, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n            ',
            'note': '- Setting this attribute adjusts the actual device output power to compensate for any amplification or attenuation between the RF signal generator and the device under test.\n\n - For the PXIe-5645, this attribute is ignored if you are using the I/Q ports.'
        },
        'lv_property': 'RF:External Gain (dB)',
        'name': 'EXTERNAL_GAIN',
        'type': 'ViReal64'
    },
    1150086: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the maximum amount of bus bandwidth to use for data transfers.\n\n                **Units**: bytes per second\n\n                **Default Value**: Device maximum\n\n                **Supported Devices:** PXI-5670/5671, PXIe-5672/5673/5673E\n\n                **Related Topics**\n\n                `Improving Streaming Performance <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/improving_streaming_performance.html>`_\n                '
        },
        'lv_property': 'Arb:Data Transfer:Maximum Bandwidth',
        'name': 'DATA_TRANSFER_MAXIMUM_BANDWIDTH',
        'type': 'ViReal64'
    },
    1150087: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the preferred size of the data field in a PCI Express read request packet.\n\n                In general, the larger the packet size, the more efficiently the device uses the bus. By default, NI RF signal generators use the largest packet size allowed by the system. However, due to different system implementations, some systems may perform better with smaller packet sizes.\n\n                Recommended values for this attribute are powers of two between 64 and 512.\n\n                **Units**: bytes\n\n                **Default Value**: Device maximum\n\n                **Supported Devices:** PXI-5670/5671, PXIe-5672/5673/5673E\n\n                **Related Topics**\n\n                `Improving Streaming Performance <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/improving_streaming_performance.html>`_\n            ',
            'note': 'In some cases, the RF signal generator generates packets smaller than the preferred size you set with this attribute.'
        },
        'lv_property': 'Arb:Data Transfer:Advanced:Preferred Packet Size',
        'name': 'DATA_TRANSFER_PREFERRED_PACKET_SIZE',
        'type': 'ViInt32'
    },
    1150088: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the maximum number of concurrent PCI Express read requests the RF signal generator can issue.\n\n                When transferring data from computer memory to device onboard memory across the PCI Express bus, the signal generator can issue multiple memory reads at the same time. In general, the larger the number of read requests, the more efficiently the device uses the bus because the multiple read requests keep the data flowing, even in a PCI Express topology that has high latency due to PCI Express switches in the data path. Most NI devices can issue a large number of read requests (typically 8 or 16). By default, this attribute is set to the highest value the RF signal generator supports.\n\n                If other devices in your system cannot tolerate long data latencies, it may be helpful to decrease the number of in-flight read requests the RF signal generator issues. This helps to reduce the amount of data the signal generator reads at one time.\n\n                **Units**: number of packets\n\n                **Default Value**: Device maximum\n\n                **Supported Devices:** PXI-5670/5671, PXIe-5672/5673/5673E\n\n                **Related Topics**\n\n                `Improving Streaming Performance <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/improving_streaming_performance.html>`_\n                '
        },
        'lv_property': 'Arb:Data Transfer:Advanced:Maximum In-Flight Read Requests',
        'name': 'DATA_TRANSFER_MAXIMUM_IN_FLIGHT_READS',
        'type': 'ViInt32'
    },
    1150089: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': "                Specifies the oscillator phase digital-to-analog converter (DAC) value on the arbitrary waveform generator (AWG). Use this attribute to reduce the trigger jitter when synchronizing multiple devices with NI-TClk. This attribute can also help maintain synchronization repeatability by writing a previous measurement's phase DAC value to the current session. This attribute is applicable only when using the NIRFSG_ATTR_ARB_SAMPLE_CLOCK_SOURCE attribute set to NIRFSG_VAL_CLK_IN_STR.\n\n                **Supported Devices:** PXIe-5673/5673E\n\n                **Related Topics**\n\n                `NI-TClk Overview <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_tclk_help.html>`_\n                "
        },
        'lv_property': 'Clock:Advanced:Arb Oscillator Phase DAC Value',
        'name': 'ARB_OSCILLATOR_PHASE_DAC_VALUE',
        'type': 'ViInt32'
    },
    1150096: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the name of the configuration list to make active. When you get or set an attribute and it is in the configuration list configuration, the attribute is set to or read from the active list step of the active configuration list.\n\n                If the NIRFSG_ATTR_ACTIVE_CONFIGURATION_LIST attribute is set to "" (empty string), no list is active.\n\n                **Default Value:** ""\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXIe-5673E, PXIe-5820/5830/5831/5832/5840/5841/5842\n\n                **Related Topics**\n\n                `RF List Mode <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/rf_list_mode_overview.html>`_\n\n                `Using RF List Mode <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/rf_list_mode.html>`_\n                \n                **High-Level Functions**:\n\n                - nirfsg_CreateConfigurationList\n                ',
            'note': 'For the PXIe-5650/5651/5652 and PXIe-5673E, when this attribute is set to a valid list name, the NIRFSG_ATTR_FREQUENCY_SETTLING_UNITS attribute supports only NIRFSG_VAL_TIME_AFTER_IO as a valid value.'
        },
        'lv_property': 'Configuration List:Active List',
        'name': 'ACTIVE_CONFIGURATION_LIST',
        'type': 'ViString'
    },
    1150097: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the step in the configuration list for `RF list mode <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/rf_list_mode.html>`_ that you want to make active for configuration or initiation.\n\n                Activating a list makes all attributes in the list reflect the value of the attributes that correspond to the set specified by the NIRFSG_ATTR_ACTIVE_CONFIGURATION_LIST and the NIRFSG_ATTR_ACTIVE_CONFIGURATION_LIST_STEP attributes.\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXIe-5673E, PXIe-5820/5830/5831/5832/5840/5841/5842\n\n                **Related Topics**\n\n                `RF List Mode <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/rf_list_mode_overview.html>`_\n\n                `Using RF List Mode <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/rf_list_mode.html>`_\n                \n                **High-Level Functions**:\n\n                - nirfsg_CreateConfigurationListStep'
        },
        'lv_property': 'Configuration List:Active Step',
        'name': 'ACTIVE_CONFIGURATION_LIST_STEP',
        'type': 'ViInt64'
    },
    1150098: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the type of trigger to use as the Configuration List Step Trigger. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                **Default Value:** NIRFSG_VAL_NONE\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXIe-5673E, PXIe-5820/5830/5831/5832/5840/5841/5842\n\n                **Related Topics**\n\n                `RF List Mode <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/rf_list_mode_overview.html>`_\n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_DIGITAL_EDGE',
                    '1 (0x1)',
                    'Data operation does not start until a digital edge is detected. The source of the digital edge is specified in the NIRFSG_ATTR_DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE attribute, and the active edge is always rising.'
                ],
                [
                    'NIRFSG_VAL_NONE',
                    '0 (0x0)',
                    'Generation starts immediately, but the list does not advance.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'ConfigListTrigType',
        'lv_property': 'Triggers:Configuration List Step:Edge',
        'name': 'CONFIGURATION_LIST_STEP_TRIGGER_TYPE',
        'type': 'ViInt32'
    },
    1150099: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the source terminal for the Configuration List Step Trigger. This attribute is valid only when the configuration list step type attribute is set to digital edge.\n\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXIe-5673E, PXIe-5820/5830/5831/5832/5840/5841/5842\n\n                **Related Topics**\n\n                `RF List Mode <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/rf_list_mode_overview.html>`_\n\n                `PFI Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pfi_lines.html>`_\n\n                `PXI Trigger Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_trigger.html>`_\n\n                `Marker Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/marker_events.html>`_\n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_MARKER0_EVENT_STR',
                    'Marker0Event',
                    'The trigger is received from the Marker Event 0.'
                ],
                [
                    'NIRFSG_VAL_MARKER1_EVENT_STR',
                    'Marker1Event',
                    'The trigger is received from the Marker Event 1.'
                ],
                [
                    'NIRFSG_VAL_MARKER2_EVENT_STR',
                    'Marker2Event',
                    'The trigger is received from the Marker Event 2.'
                ],
                [
                    'NIRFSG_VAL_MARKER3_EVENT_STR',
                    'Marker3Event',
                    'The trigger is received from the Marker Event 3.'
                ],
                [
                    'NIRFSG_VAL_PFI0_STR',
                    'PFI0',
                    'The trigger is received on PFI 0.'
                ],
                [
                    'NIRFSG_VAL_PFI1_STR',
                    'PFI1',
                    'The trigger is received on PFI 1.'
                ],
                [
                    'NIRFSG_VAL_PXI_STAR_STR',
                    'PXI_Star',
                    'The trigger is received on the PXI star trigger line. This value is not valid for the PXIe-5644/5645/5646.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG0_STR',
                    'PXI_Trig0',
                    'The trigger is received on PXI trigger line 0.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG1_STR',
                    'PXI_Trig1',
                    'The trigger is received on PXI trigger line 1.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG2_STR',
                    'PXI_Trig2',
                    'The trigger is received on PXI trigger line 2.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG3_STR',
                    'PXI_Trig3',
                    'The trigger is received on PXI trigger line 3.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG4_STR',
                    'PXI_Trig4',
                    'The trigger is received on PXI trigger line 4.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG5_STR',
                    'PXI_Trig5',
                    'The trigger is received on PXI trigger line 5.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG6_STR',
                    'PXI_Trig6',
                    'The trigger is received on PXI trigger line 6.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG7_STR',
                    'PXI_Trig7',
                    'The trigger is received on PXI trigger line 7.'
                ],
                [
                    'NIRFSG_VAL_PXIE_DSTARB_STR',
                    'PXIe_DStarB',
                    'The trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5840/5841/5842.'
                ],
                [
                    'NIRFSG_VAL_TIMER_EVENT_STR',
                    'TimerEvent',
                    'The trigger is received from the Timer Event.'
                ],
                [
                    'NIRFSG_VAL_TRIG_IN_STR',
                    'TrigIn',
                    'The trigger is received on the TRIG IN/OUT terminal. This value is valid on only the PXIe-5654/5654 with PXIe-5696.'
                ],
                [
                    'NIRFSG_VAL_DIO0_STR',
                    'DIO/PFI0',
                    'The trigger is received on PFI0 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO1_STR',
                    'DIO/PFI1',
                    'The trigger is received on PFI1 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO2_STR',
                    'DIO/PFI2',
                    'The trigger is received on PFI2 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO3_STR',
                    'DIO/PFI3',
                    'The trigger is received on PFI3 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO4_STR',
                    'DIO/PFI4',
                    'The trigger is received on PFI4 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO5_STR',
                    'DIO/PFI5',
                    'The trigger is received on PFI5 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO6_STR',
                    'DIO/PFI6',
                    'The trigger is received on PFI6 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO7_STR',
                    'DIO/PFI7',
                    'The trigger is received on PFI7 from the front panel DIO terminal.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'ConfigListTrigDigEdgeSource',
        'lv_property': 'Triggers:Configuration List Step:Digital Edge:Source',
        'name': 'DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE',
        'type': 'ViString'
    },
    1150100: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the time before the timer emits an event after the task is started and specifies the time interval between Timer events after the first event.\n\n                **Units**: seconds (s)\n\n                **Default Value:** 0\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5654/5654 with PXIe-5696, PXIe-5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_\n            ',
            'note': 'For the PXIe-5820/5840/5841/5842/5860, this attribute must be set for the timer to start. If you do not set this attribute, the timer is disabled.'
        },
        'lv_property': 'Events:Timer:Interval',
        'name': 'TIMER_EVENT_INTERVAL',
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    1150102: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies whether the configuration list runs only once or continuously.\n\n                **Default Value:** NIRFSG_VAL_CONTINUOUS\n\n                **Supported Devices:** PXIe-5650/5651/5652, PXIe-5654/5654 with PXIe-5696, PXIe-5673E\n\n                **Related Topics**\n\n                `RF List Mode <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/rf_list_mode_overview.html>`_\n\n                `Using RF List Mode <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/rf_list_mode.html>`_\n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_CONTINUOUS',
                    '0',
                    'NI-RFSG runs the configuration list continuously.'
                ],
                [
                    'NIRFSG_VAL_SINGLE',
                    '1',
                    'NI-RFSG runs the configuration list only once.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'ConfigurationListRepeat',
        'lv_property': 'Configuration List:Configuration List Repeat',
        'name': 'CONFIGURATION_LIST_REPEAT',
        'type': 'ViInt32'
    },
    1150103: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the active edge for the Configuration List Step trigger. This attribute is valid only when the NIRFSG_ATTR_CONFIGURATION_LIST_STEP_TRIGGER_TYPE attribute is set to digital edge. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXIe-5673E, PXIe-5820/5830/5831/5832/5840/5841/5842\n\n                **Related Topics**\n\n                `RF List Mode <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/rf_list_mode_overview.html>`_\n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_RISING_EDGE',
                    'Specifies the rising edge as the active edge. The rising edge occurs when the signal transitions from low level to high level.'
                ]
            ],
            'table_header': [
                'Name',
                'Description'
            ]
        },
        'enum': 'ConfigListTrigDigEdgeEdge',
        'lv_property': 'Triggers:Configuration List Step:Digital Edge:Edge',
        'name': 'DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_EDGE',
        'type': 'ViInt32'
    },
    1150104: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the temperature, in degrees Celsius, to use for adjusting the device settings to correct for temperature changes. If you set this attribute, NI-RFSG uses the value you specify and therefore no longer uses the actual device temperature as the correction temperature. If you do not set this attribute, NI-RFSG checks the current device temperature in the Committed state and automatically sets the value of this attribute.\n\n                PXIe-5820/5830/5831/5832/5840/5841/5842/5860: This attribute is read only.\n\n                **Units**: Degrees Celsius\n\n                **Supported Devices**: PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n            ',
            'note': '- Resetting this attribute reverts back to the default unset behavior.\n\n - Use this attribute only when your application requires the same settings to be used every time, regardless of the temperature variation. In these cases, it is best to ensure that the temperature does not vary too much.'
        },
        'lv_property': 'RF:Advanced:Correction Temperature',
        'name': 'CORRECTION_TEMPERATURE',
        'type': 'ViReal64'
    },
    1150105: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the destination terminal for exporting the Configuration List Step trigger. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXIe-5654/5654 with PXIe-5696, PXIe-5673E, PXIe-5820/5830/5831/5832/5840/5841/5842\n\n                **Related Topics**\n\n                [RF List Mode](RFSG.chm/RF_List_Mode_Overview.html)\n\n                [PFI Lines](RFSG.chm/integration_PFI_Lines.html)\n\n                [PXI Trigger Lines](RFSG.chm/integration_PXI_Trigger.html)\n\n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_DO_NOT_EXPORT_STR',
                    '',
                    'The signal is not exported.'
                ],
                [
                    'NIRFSG_VAL_PFI0_STR',
                    'PFI0',
                    'The signal is exported to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0.'
                ],
                [
                    'NIRFSG_VAL_PFI1_STR',
                    'PFI1',
                    'The signal is exported to the PFI 1 connector.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG0_STR',
                    'PXI_Trig0',
                    'The trigger is received on PXI trigger line 0.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG1_STR',
                    'PXI_Trig1',
                    'The trigger is received on PXI trigger line 1.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG2_STR',
                    'PXI_Trig2',
                    'The trigger is received on PXI trigger line 2.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG3_STR',
                    'PXI_Trig3',
                    'The trigger is received on PXI trigger line 3.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG4_STR',
                    'PXI_Trig4',
                    'The trigger is received on PXI trigger line 4.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG5_STR',
                    'PXI_Trig5',
                    'The trigger is received on PXI trigger line 5.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG6_STR',
                    'PXI_Trig6',
                    'The trigger is received on PXI trigger line 6.'
                ],
                [
                    'NIRFSG_VAL_PXIE_DSTARC_STR',
                    'PXIe_DStarC',
                    'The signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5840/5841/5842.'
                ],
                [
                    'NIRFSG_VAL_TRIG_OUT_STR',
                    'TrigOut',
                    'The signal is exported to the TRIG IN/OUT terminal. This value is valid on only the PXIe-5654/5654 with PXIe-5696.'
                ],
                [
                    'NIRFSG_VAL_DIO0_STR',
                    'DIO/PFI0',
                    'The trigger is received on PFI0 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO1_STR',
                    'DIO/PFI1',
                    'The trigger is received on PFI1 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO2_STR',
                    'DIO/PFI2',
                    'The trigger is received on PFI2 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO3_STR',
                    'DIO/PFI3',
                    'The trigger is received on PFI3 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO4_STR',
                    'DIO/PFI4',
                    'The trigger is received on PFI4 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO5_STR',
                    'DIO/PFI5',
                    'The trigger is received on PFI5 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO6_STR',
                    'DIO/PFI6',
                    'The trigger is received on PFI6 from the front panel DIO terminal.'
                ],
                [
                    'NIRFSG_VAL_DIO7_STR',
                    'DIO/PFI7',
                    'The trigger is received on PFI7 from the front panel DIO terminal.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'ConfigListTrigExportOutputTerm',
        'lv_property': 'Triggers:Configuration List Step:Export Output Terminal',
        'name': 'EXPORTED_CONFIGURATION_LIST_STEP_TRIGGER_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150112: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns the name of the fully qualified signal name as a string.\n\n                **Default Values**:\n\n                PXI-5670/5671, PXIe-5672/5673/5673E: /*AWGName*/StartedEvent, where *AWGName* is the name of your associated AWG module in MAX.\n\n                PXIe-5830/5831/5832: /*BasebandModule*/ao/0/StartedEvent, where *BasebandModule* is the name of the baseband module of your device in MAX.\n\n                PXIe-5820/5840/5841: /*ModuleName*/ao/0/StartedEvent, where *ModuleName* is the name of your device in MAX.\n\n                PXIe-5860: /*ModuleName*/ao/*ChannelNumber*/StartedEvent, where *ModuleName* is the name of your device in MAX and *ChannelNumber* is the channel number (0 or 1).\n\n                **Supported Devices:** PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_\n\n                `Syntax for Terminal Names <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/syntax_for_terminal_names.html>`_\n\n                **High-Level Functions**:\n\n                - nirfsg_GetTerminalName\n                '
        },
        'lv_property': 'Events:Started Event Terminal Name',
        'name': 'STARTED_EVENT_TERMINAL_NAME',
        'type': 'ViString'
    },
    1150113: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns the name of the fully qualified signal name as a string.\n\n                **Default Values**:\n\n                PXI-5670/5671, PXIe-5672/5673/5673E: /*AWGName*/DoneEvent, where *AWGName* is the name of your associated AWG module in MAX.\n\n                PXIe-5830/5831/5832: /*BasebandModule*/ao/0/DoneEvent, where *BasebandModule* is the name of the baseband module of your device in MAX.\n\n                PXIe-5820/5840/5841: /*ModuleName*/ao/0/DoneEvent, where *ModuleName* is the name of your device in MAX.\n\n                PXIe-5860: /*ModuleName*/ao/*ChannelNumber*/DoneEvent, where *ModuleName* is the name of your device in MAX and *ChannelNumber* is the channel number (0 or 1).\n\n                **Supported Devices:** PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_\n\n                `Syntax for Terminal Names <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/syntax_for_terminal_names.html>`_\n                \n                **High-Level Functions**:\n\n                - nirfsg_GetTerminalName'
        },
        'lv_property': 'Events:Done Event Terminal Name',
        'name': 'DONE_EVENT_TERMINAL_NAME',
        'type': 'ViString'
    },
    1150114: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns the name of the fully qualified signal name as a string.\n\n                **Default Values**:\n\n                PXIe-5654/5654 with PXIe-5696: /*ModuleName*/StartTrigger, where *ModuleName* is the name of your device in MAX.\n\n                PXI-5670/5671, PXIe-5672/5673/5673E: /*AWGName*/StartTrigger, where *ModuleName* is the name of your associated AWG module in MAX.\n\n                PXIe-5830/5831/5832: /*BasebandModule*/ao/0/StartTrigger, where *BasebandModule* is the name of the baseband module of your device in MAX.\n\n                PXIe-5820/5840/5841/5842: /*ModuleName*/ao/0/StartTrigger, where *ModuleName* is the name of your device in MAX.\n\n                PXIe-5860: /*ModuleName*/ao/*ChannelNumber*/StartTrigger, where *ModuleName* is the name of your device in MAX and *ChannelNumber* is the channel number (0 or 1).\n\n                **Supported Devices:** PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_\n\n                `Syntax for Terminal Names <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/syntax_for_terminal_names.html>`_\n\n                **High-Level Functions**:\n\n                - nirfsg_GetTerminalName\n                '
        },
        'lv_property': 'Triggers:Start:Terminal Name',
        'name': 'START_TRIGGER_TERMINAL_NAME',
        'type': 'ViString'
    },
    1150115: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns the name of the fully qualified signal name as a string.\n\n                **Default Values**:\n\n                PXI-5670/5671, PXIe-5672/5673/5673E: /*AWGName*/Marker *X* Event, where *AWGName* is the name of your associated AWG module in MAX and *X* is Marker Event 0 through 3.\n\n                PXIe-5830/5831/5832: /*BasebandModule*/ao/0/Marker *X* Event, where *BasebandModule* is the name of the baseband module of your device in MAX and *X* is Marker Event 0 through 3.\n\n                PXIe-5820/5840/5841: /*ModuleName*/ao/0/Marker *X* Event, where *ModuleName* is the name of your device in MAX and *X* is Marker Event 0 through 3.\n\n                **Supported Devices:** PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842\n\n                **Related Topics**\n\n                `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_\n\n                `Syntax for Terminal Names <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/syntax_for_terminal_names.html>`_\n                \n                **High-Level Functions**:\n\n                - nirfsg_GetTerminalName'
        },
        'lv_property': 'Events:Marker:Terminal Name',
        'name': 'MARKER_EVENT_TERMINAL_NAME',
        'repeated_capability_type': 'markers',
        'supported_rep_caps': [
            'markers'
        ],
        'type': 'ViString'
    },
    1150116: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns the name of the fully qualified signal name as a string.\n\n                **Default Values**:\n\n                PXI-5670/5671, PXIe-5672/5673/5673E: /*AWGName*/ScriptTrigger *X*, where *AWGName* is the name of your associated AWG module in MAX and *X* is Script Trigger 0 through 3.\n\n                PXIe-5830/5831/5832: /*BasebandModule*/ao/0/ScriptTrigger *X*, where *BasebandModule* is the name of the baseband module of your device in MAX and *X* is Script Trigger 0 through 3.\n\n                PXIe-5820/5840/5841/5842: /*ModuleName*/ao/0/ScriptTrigger *X*, where *ModuleName* is the name of your device in MAX and *X* is Script Trigger 0 through 3.\n\n                PXIe-5860: /*ModuleName*/ao/*ChannelNumber*/ScriptTrigger *X*, where *ModuleName* is the name of your device in MAX, *ChannelNumber* is the channel number (0 or 1), and *X* is Script Trigger 0 through 3.\n\n                **Supported Devices:** PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Triggers <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/triggers.html>`_\n\n                `Syntax for Terminal Names <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/syntax_for_terminal_names.html>`_\n\n                **High-Level Functions**:\n\n                - nirfsg_GetTerminalName\n                '
        },
        'lv_property': 'Triggers:Script:Terminal Name',
        'name': 'SCRIPT_TRIGGER_TERMINAL_NAME',
        'supported_rep_caps': [
            'script_triggers'
        ],
        'type': 'ViString'
    },
    1150117: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns the fully-qualified signal name as a string.\n\n                **Default Values**:\n\n                PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696: /*ModuleName*/ConfigurationListStepTrigger, where *ModuleName* is the name of your device in MAX.\n\n                PXIe-5673E: /*AWGName*/ConfigurationListStepTrigger, where *AWGName* is the name of your associated AWG module in MAX.\n\n                PXIe-5820/5830/5831/5832/5840/5841/5842: /*ModuleName*/ao/0/ConfigurationListStepTrigger, where *ModuleName* is the name of your device in MAX.\n\n                **Supported Devices:** PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXIe-5673E, PXIe-5820/5830/5831/5832/5840/5841/5842\n\n                **Related Topics**\n\n                `Triggers <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/triggers.html>`_\n\n                `Syntax for Terminal Names <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/syntax_for_terminal_names.html>`_\n                \n                **High-Level Functions**:\n\n                - nirfsg_GetTerminalName'
        },
        'lv_property': 'Triggers:Configuration List Step:Terminal Name',
        'name': 'CONFIGURATION_LIST_STEP_TRIGGER_TERMINAL_NAME',
        'type': 'ViString'
    },
    1150118: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Adjusts the dynamics of the current driving the YIG main coil.\n\n                **Default Value:** NIRFSG_VAL_MANUAL\n\n                **Supported Devices:** PXIe-5653\n            \n            **Defined Values**:\n            ',
            'note': 'Setting this attribute to NIRFSG_VAL_FAST on the PXIe-5653 allows the frequency to settle significantly faster for some frequency transitions at the expense of increased phase noise.',
            'table_body': [
                [
                    'NIRFSG_VAL_SLOW',
                    'Adjusts the YIG main coil for an underdamped response.'
                ],
                [
                    'NIRFSG_VAL_FAST',
                    'Adjusts the YIG main coil for an overdamped response.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'enum': 'YigMainCoilDrive',
        'lv_property': 'RF:Advanced:YIG Main Coil Drive',
        'name': 'YIG_MAIN_COIL_DRIVE',
        'type': 'ViInt32'
    },
    1150122: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns the configuration list step that is currently programmed to the hardware. The list is zero-indexed. You can query this attribute only when a list is executed.\n\n                PXIe-5650/5651/5652, PXIe-5654/5654 with PXIe-5696, PXIe-5673E: This attribute can be read only when a configuration list is running.\n\n                PXIe-5644/5645/5646: This attribute always returns 0 when the configuration list is not running.\n\n                PXIe-5820/5830/5831/5832/5840/5841/5842: If the configuration list is not running, this attribute returns the last step of a configuration list that is programmed to the hardware. If the device was last initiated without an active configuration list, this attribute returns 0.\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXIe-5673E, PXIe-5820/5830/5831/5832/5840/5841/5842\n\n                **Related Topics**\n\n                `RF List Mode <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/rf_list_mode_overview.html>`_\n                '
        },
        'lv_property': 'Configuration List:Step In Progress',
        'name': 'CONFIGURATION_LIST_STEP_IN_PROGRESS',
        'type': 'ViInt64'
    },
    1150123: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies whether the RF signal generator reads data from the peer-to-peer endpoint. This attribute is endpoint-based.\n\n                **Default Value**: VI_FALSE\n\n                **Supported Devices:** PXIe-5673E, PXIe-5820/5830/5831/5832/5840/5841/5842\n\n                **Related Topics**\n\n                `Configuring a Peer-to-Peer Endpoint <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/p2p_configuring_an_endpoint.html>`_\n            \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'VI_TRUE',
                    'Peer-to-peer data streaming is enabled.'
                ],
                [
                    'VI_FALSE',
                    'Peer-to-peer data streaming is disabled.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'lv_property': 'Peer-to-Peer:Enabled',
        'name': 'P2P_ENABLED',
        'type': 'ViBoolean'
    },
    1150124: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns the size, in samples, of the device endpoint. This attribute is endpoint-based.\n\n                **Units**: samples (s)\n\n                **Supported Devices:** PXIe-5673E, PXIe-5820/5830/5831/5832/5840/5841/5842\n\n                **Related Topics**\n\n                `Configuring a Peer-to-Peer Endpoint <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/p2p_configuring_an_endpoint.html>`_\n                '
        },
        'lv_property': 'Peer-to-Peer:Endpoint Size',
        'name': 'P2P_ENDPOINT_SIZE',
        'type': 'ViInt64'
    },
    1150125: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns the current space available in the endpoint. You can use this attribute when priming the endpoint with initial data using the nirfsg_WriteP2pEndpointI16 function to determine how many samples you can write. You also can use this attribute to characterize the performance and measure the latency of the peer-to-peer stream as data moves across the bus. This attribute is endpoint-based.\n\n                **Units**: samples per channel\n\n                **Supported Devices:** PXIe-5673E, PXIe-5820/5830/5831/5832/5840/5841/5842\n\n                **Related Topics**\n\n                `Configuring a Peer-to-Peer Endpoint <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/p2p_configuring_an_endpoint.html>`_\n\n                `Starting Peer-to-Peer Generation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/p2p_starting_generation.html>`_\n                '
        },
        'lv_property': 'Peer-to-Peer:Space Available In Endpoint',
        'name': 'P2P_SPACE_AVAILABLE_IN_ENDPOINT',
        'type': 'ViInt64'
    },
    1150126: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns the largest number of samples per channel available in the endpoint since this attribute was last read. You can use this attribute to determine how much endpoint space to use as a buffer against bus traffic latencies by reading the attribute and keeping track of the largest value returned. This attribute is endpoint-based.\n\n                If you want to minimize the latency for data to move through the endpoint and be generated by the RF signal generator, use the NIRFSG_ATTR_P2P_DATA_TRANSFER_PERMISSION_INITIAL_CREDITS attribute to grant fewer initial credits than the default of the entire endpoint size.\n\n                **Units**: samples per channel\n\n                **Supported Devices:** PXIe-5673E, PXIe-5820/5830/5831/5832/5840/5841/5842\n\n                **Related Topics**\n\n                `Configuring a Peer-to-Peer Endpoint <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/p2p_configuring_an_endpoint.html>`_\n                '
        },
        'lv_property': 'Peer-to-Peer:Most Space Available in Endpoint',
        'name': 'P2P_MOST_SPACE_AVAILABLE_IN_ENDPOINT',
        'type': 'ViInt64'
    },
    1150127: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns the number of peer-to-peer FIFO endpoints supported by the device.\n\n                **Supported Devices:** PXIe-5673E, PXIe-5820/5830/5831/5832/5840/5841/5842\n\n                **Related Topics**\n\n                `Configuring a Peer-to-Peer Endpoint <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/p2p_configuring_an_endpoint.html>`_\n                '
        },
        'lv_property': 'Peer-to-Peer:Endpoint Count',
        'name': 'P2P_ENDPOINT_COUNT',
        'type': 'ViInt32'
    },
    1150128: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the number of samples the endpoint must receive before the device starts generation. If no level is specified, NI-RFSG automatically sets this value to -1. This attribute applies only when the NIRFSG_ATTR_START_TRIGGER_TYPE attribute is set to NIRFSG_VAL_P2P_ENDPOINT_FULLNESS\n\n                **Default Value:** -1, which allows NI-RFSG to select the appropriate fullness value.\n\n                **Supported Devices:** PXIe-5673E, PXIe-5820/5830/5831/5832/5840/5841/5842\n\n                **Related Topics**\n\n                `Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_\n            ',
            'note': 'Due to an additional internal FIFO in the RF signal generator, the writer peer actually needs to write 2,304 bytes more than the quantity of data specified by this attribute to satisfy the trigger level.'
        },
        'lv_property': 'Triggers:Start:P2P Endpoint Fullness:Level',
        'name': 'P2P_ENDPOINT_FULLNESS_START_TRIGGER_LEVEL',
        'type': 'ViInt64'
    },
    1150129: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the destination terminal for exporting the Configuration Settled event. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                **Supported Devices:** PXIe-5654/5654 with PXIe-5696, PXIe-5820/5830/5831/5832/5840/5841/5842\n\n                **Related Topics**\n\n                `Triggers <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/triggers.html>`_\n\n                `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_\n\n                `PFI Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pfi_lines.html>`_\n\n                `PXI Trigger Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_trigger.html>`_\n\n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_DO_NOT_EXPORT_STR',
                    '',
                    'The signal is not exported.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG0_STR',
                    'PXI_Trig0',
                    'The trigger is received on PXI trigger line 0.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG1_STR',
                    'PXI_Trig1',
                    'The trigger is received on PXI trigger line 1.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG2_STR',
                    'PXI_Trig2',
                    'The trigger is received on PXI trigger line 2.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG3_STR',
                    'PXI_Trig3',
                    'The trigger is received on PXI trigger line 3.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG4_STR',
                    'PXI_Trig4',
                    'The trigger is received on PXI trigger line 4.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG5_STR',
                    'PXI_Trig5',
                    'The trigger is received on PXI trigger line 5.'
                ],
                [
                    'NIRFSG_VAL_PXI_TRIG6_STR',
                    'PXI_Trig6',
                    'The trigger is received on PXI trigger line 6.'
                ],
                [
                    'NIRFSG_VAL_PXIE_DSTARC_STR',
                    'PXIe_DStarC',
                    'The signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5840/5841/5842.'
                ],
                [
                    'NIRFSG_VAL_TRIG_OUT_STR',
                    'TrigOut',
                    'TRIG IN/OUT terminal.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'ConfigurationSettledEventExportOutputTerm',
        'lv_property': 'Events:Configuration Settled Event Export Output Terminal',
        'name': 'EXPORTED_CONFIGURATION_SETTLED_EVENT_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150132: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the adjustment for the NIRFSG_ATTR_POWER_LEVEL attribute. This attribute is valid only when you set the NIRFSG_ATTR_POWER_LEVEL_TYPE attribute to NIRFSG_VAL_PEAK_POWER. The value of the NIRFSG_ATTR_PEAK_POWER_ADJUSTMENT attribute adds to the NIRFSG_ATTR_POWER_LEVEL attribute. The NIRFSG_ATTR_PEAK_POWER_ADJUSTMENT attribute typically specifies the peak-to-average power ratio (PAPR) of a waveform. If the PAPR is specified, the specified power level becomes the average power level of the waveform, even if the NIRFSG_ATTR_POWER_LEVEL_TYPE attribute is set to NIRFSG_VAL_PEAK_POWER.\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Assigning Properties or Attributes to a Waveform <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/assigning_properties_or_attributes_to_a_waveform.html>`_—Refer to this topic for more information about using this attribute to associate a peak power adjustment with a waveform.\n            ',
            'note': '- For the PXIe-5673/5673E only, use this attribute to associate a peak power adjustment with a waveform.\n\n - For the PXIe-5645, this attribute is ignored if you are using the I/Q ports.'
        },
        'lv_property': 'RF:Peak Power Adjustment (dB)',
        'name': 'PEAK_POWER_ADJUSTMENT',
        'type': 'ViReal64'
    },
    1150133: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Configures the loop bandwidth of the reference PLL.\n\n                **Default Value:** NIRFSG_VAL_NARROW\n\n                **Supported Devices:** PXIe-5653\n\n                **Related Topics**\n\n                `Phase-Locked Loop Bandwidth <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/phased_lock_loop_bandwidth.html>`_\n            \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_NARROW',
                    'Uses the narrowest loop bandwidth setting for the PLL.'
                ],
                [
                    'NIRFSG_VAL_MEDIUM',
                    'Uses the medium loop bandwidth setting for the PLL.'
                ],
                [
                    'NIRFSG_VAL_WIDE',
                    'Uses the widest loop bandwidth setting for the PLL.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'enum': 'LoopBandwidth',
        'lv_property': 'RF:Advanced:Ref PLL Bandwidth',
        'name': 'REF_PLL_BANDWIDTH',
        'type': 'ViInt32'
    },
    1150134: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the interval at which the RF signal generator issues credits to allow the writer peer to transfer data over the bus into the configured endpoint. This attribute is coerced up by NI-RFSG to the nearest 128-byte boundary. This attribute is endpoint-based.\n\n                **Units**: samples per channel\n\n                **Supported Devices:** PXIe-5673E\n\n                **Related Topics**\n\n                `Configuring a Peer-to-Peer Endpoint <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/p2p_configuring_an_endpoint.html>`_\n\n                `Configuring Flow Control <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/p2p_flow_control.html>`_\n                '
        },
        'lv_property': 'Peer-to-Peer:Data Transfer Permission Interval',
        'name': 'P2P_DATA_TRANSFER_PERMISSION_INTERVAL',
        'type': 'ViInt64'
    },
    1150135: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the initial amount of data that the writer peer can transfer over the bus into the configured endpoint when the peer-to-peer data stream is enabled. If this attribute is not set and the endpoint is empty, credits equal to the full endpoint size are issued to the writer peer. If data is written to the endpoint using the nirfsg_WriteP2pEndpointI16 function prior to enabling the stream, credits equal to the remaining space available in the endpoint are issued to the writer peer. This attribute is coerced up by NI-RFSG to 8-byte boundaries. This attribute is endpoint-based.\n\n                **Units**: samples per channel\n\n                **Default Value:** 1,024\n\n                **Supported Devices:** PXIe-5673E\n\n                **Related Topics**\n\n                `Configuring a Peer-to-Peer Endpoint <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/p2p_configuring_an_endpoint.html>`_\n\n                `Configuring Flow Control <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/p2p_flow_control.html>`_\n                '
        },
        'lv_property': 'Peer-to-Peer:Data Transfer Permission Initial Credits',
        'name': 'P2P_DATA_TRANSFER_PERMISSION_INITIAL_CREDITS',
        'type': 'ViInt64'
    },
    1150136: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Indicates, in degrees Celsius, the temperature of the device at the time of the last self calibration.\n\n                **Supported Devices:** PXIe-5644/5645/5646\n                '
        },
        'lv_property': 'Self Calibration:Last Self Calibration Temperature',
        'name': 'SELF_CALIBRATION_TEMPERATURE',
        'type': 'ViReal64'
    },
    1150137: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Configures the amplitude settling accuracy in decibels. NI-RFSG waits until the RF power settles within the specified accuracy level after calling the nirfsg_Initiate function or nirfsg_WaitUntilSettled function or prior to advancing to next step if using RF list mode.\n\n                Any specified amplitude settling value that is above the acceptable minimum value is coerced down to the closest valid value.\n\n                PXI/PXIe-5650/5651/5652: This attribute is for NI internal use only.\n\n                **Units**: dB\n\n                **Default Value:**\n\n                PXIe-5654: 4\n\n                PXIe-5654 with PXIe-5696 (ALC disabled): 4\n\n                PXIe-5654 with PXIe-5696 (ALC enabled): 0.2\n\n                PXIe-5820/5830/5831/5832/5840/5841/5842/5860: 0.5\n\n                **Valid Values:**\n\n                PXIe-5654: 1.5, 2, 4\n\n                PXIe-5654 with PXIe-5696 (ALC disabled): 1.5, 2, 4\n\n                PXIe-5654 with PXIe-5696 (ALC enabled): 0.2, 0.5\n\n                PXIe-5820/5830/5831/5832/5840/5841/5842/5860: 0.01 to 1\n\n                **Supported Devices:** PXIe-5654/5654 with PXIe-5696, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Amplitude Settling Times <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_amplitude_settling_times.html>`_\n                '
        },
        'lv_property': 'RF:Amplitude Settling',
        'name': 'AMPLITUDE_SETTLING',
        'type': 'ViReal64'
    },
    1150140: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Indicates the maximum amount of time allowed to complete a streaming write operation.\n\n                **Default Value:** 10.0seconds\n\n                **Supported Devices:** PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Streaming <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/streaming.html>`_\n\n                `Streaming Waveform Data <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/streaming_waveform_data.html>`_\n                '
        },
        'lv_property': 'Arb:Data Transfer:Streaming:Streaming Write Timeout',
        'name': 'STREAMING_WRITE_TIMEOUT',
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    1150141: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Determines the inheritance behavior of the NIRFSG_ATTR_PEAK_POWER_ADJUSTMENT attribute when a script inherits values from specified waveforms.\n\n                **Default Value:** NIRFSG_VAL_EXACT_MATCH\n\n                **Supported Devices:** PXIe-5673/5673E\n\n                **Related Topics**\n\n                `Assigning Properties or Attributes to a Waveform <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/assigning_properties_or_attributes_to_a_waveform.html>`_\n            \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_EXACT_MATCH',
                    'Errors out if different values are detected in the script.'
                ],
                [
                    'NIRFSG_VAL_MINIMUM',
                    'Uses the minimum value found in the script.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'enum': 'PpaInheritance',
        'lv_property': 'RF:Peak Power Adjustment Inheritance',
        'name': 'PEAK_POWER_ADJUSTMENT_INHERITANCE',
        'type': 'ViInt32'
    },
    1150142: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies whether the device is the master device when synchronizing the Script Trigger.\n\n                The master device distributes the synchronized Script Trigger to all devices in the system through the Script Trigger distribution line.\n\n                When synchronizing the Script trigger, one device must always be designated as the master. The master device actively drives the Script Trigger distribution line. For slave devices, set the NIRFSG_ATTR_SCRIPT_TRIGGER_TYPE attribute to digital edge, and set the NIRFSG_ATTR_DIGITAL_EDGE_SCRIPT_TRIGGER_SOURCE attribute to sync_script.\n\n                To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                **Default Value:** VI_FALSE\n\n                **Supported Devices:** PXIe-5644/5645/5646\n\n                **Related Topics**\n\n                `Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_\n\n                `Synchronizing Sample Clock and Sampled Reference Clock Signals <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/sample_clock_sync.html>`_\n\n                Refer to the Synchronization Using NI-RFSA and NI-RFSG topic appropriate to your device for more information about device synchronization for vector signal transceivers.\n            \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'VI_TRUE',
                    'The device is the master device for synchronizing the Script Trigger.'
                ],
                [
                    'VI_FALSE',
                    'The device is not the master for synchronizing the Script Trigger.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Triggers:Sync Script Trigger Master',
        'name': 'SYNC_SCRIPT_TRIGGER_MASTER',
        'type': 'ViBoolean'
    },
    1150143: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies which external trigger line distributes the synchronized Script Trigger signal. When synchronizing the Script Trigger, configure all devices to use the same Script Trigger distribution line.\n\n                To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                **Valid Values:** PXI_Trig0, PXI_Trig1, PXI_Trig2, PXI_Trig3, PXI_Trig4, PXI_Trig5, PXI_Trig6, PXI_Trig7, PFI0\n\n                **Default Value:** "" (empty string)\n\n                **Supported Devices:** PXIe-5644/5645/5646\n\n                **Related Topics**\n\n                `Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_\n\n                `Synchronizing Sample Clock and Sampled Reference Clock Signals <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/sample_clock_sync.html>`_\n\n                Refer to the Synchronization Using NI-RFSA and NI-RFSG topic appropriate to your device for more information about device synchronization for vector signal transceivers.\n                '
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Triggers:Sync Script Trigger Dist Line',
        'name': 'SYNC_SCRIPT_TRIGGER_DIST_LINE',
        'type': 'ViString'
    },
    1150144: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the connector(s) to use to generate the signal. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                You must write complex I and Q data for all options. The Q data has no effect if you set this attribute to I Only and set the NIRFSG_ATTR_IQ_OUT_PORT_CARRIER_FREQUENCY attribute to 0. If you set the NIRFSG_ATTR_IQ_OUT_PORT_CARRIER_FREQUENCY attribute to a value other than 0, the onboard signal processing (OSP) frequency shifts I and Q as a complex value and outputs the real portion of the result on the I connector(s) of the device.\n\n                If you set the NIRFSG_ATTR_OUTPUT_PORT attribute to NIRFSG_VAL_I_ONLY\\_ONLY or NIRFSG_VAL_IQ_OUT, the NIRFSG_ATTR_IQ_OUT_PORT_TERMINAL_CONFIGURATION attribute applies.\n\n                **Default Value:**\n\n                PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842/5860: NIRFSG_VAL_RF_OUT\n\n                PXIe-5820: NIRFSG_VAL_IQ_OUT\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n            \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_CAL_OUT',
                    '14002 (0x36b2)',
                    'Enables the CAL OUT port.'
                ],
                [
                    'NIRFSG_VAL_I_ONLY',
                    '14003 (0x36b3)',
                    'Enables the I connectors of the I/Q OUT port. This value is valid on only the PXIe-5645.'
                ],
                [
                    'NIRFSG_VAL_IQ_OUT',
                    '14001 (0x36b1)',
                    'Enables the I/Q OUT port. This value is valid on only the PXIe-5645 and PXIe-5820.'
                ],
                [
                    'NIRFSG_VAL_RF_OUT',
                    '14000 (0x36b0)',
                    'Enables the RF OUT port. This value is not valid for the PXIe-5820.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'OutputPort',
        'lv_property': 'Device Specific:Vector Signal Transceiver:Signal Path:Output Port',
        'name': 'OUTPUT_PORT',
        'type': 'ViInt32'
    },
    1150145: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the frequency of the I/Q OUT port signal. The onboard signal processing (OSP) applies the specified frequency shift to the I/Q data before the data is sent to the digital-to-analog converter (DAC). To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                **Units:** hertz (Hz)\n\n                **Valid Values:**\n\n                PXIe-5645: -60MHz to 60MHz\n\n                PXIe-5820: -500MHz to 500MHz\n\n                **Supported Devices:** PXIe-5645, PXIe-5820\n            ',
            'note': '- For the PXIe-5820, NI recommends using the NIRFSG_ATTR_FREQUENCY attribute.\n\n - For the PXIe-5645, this attribute is ignored if you are using the RF ports.'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:IQ Out Port:Carrier Frequency',
        'name': 'IQ_OUT_PORT_CARRIER_FREQUENCY',
        'type': 'ViReal64'
    },
    1150146: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies whether to use the I/Q OUT port for differential configuration or single-ended configuration. If you set this attribute to NIRFSG_VAL_SINGLE_ENDED, you must terminate the negative I and Q output connectors with a 50 Ohm termination.\n\n                If you set this attribute to NIRFSG_VAL_SINGLE_ENDED, the positive I and Q connectors generate the resulting waveform. If you set this attribute to NIRFSG_VAL_DIFFERENTIAL, both the positive and negative I and Q connectors generate the resulting waveform.\n\n                To use this attribute, you must use the channelName parameter of the nirfsg_SetAttributeViInt32 function to specify the name of the channel you are configuring. For the PXIe-5645, you can configure the I and Q channels by using I or Q as the channel string, or set the channel string to "" (empty string) to configure both channels. For the PXIe-5820, the only valid value for the channel string is "" (empty string).\n\n                To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                **Default Value:** NIRFSG_VAL_DIFFERENTIAL\n\n                PXIe-5820: The only valid value for this attribute is NIRFSG_VAL_DIFFERENTIAL.\n\n                **Supported Devices:** PXIe-5645, PXIe-5820\n\n                **Related Topics**\n\n                `Differential and Single-Ended Operation (I/O Interface) <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/differential_single_ended_operation.html>`_\n            \n            **Defined Values**:\n            ',
            'note': 'For the PXIe-5645, this attribute is ignored if you are using the RF ports.',
            'table_body': [
                [
                    'NIRFSG_VAL_DIFFERENTIAL',
                    '15000 (0x3a98)',
                    'Sets the terminal configuration to differential.'
                ],
                [
                    'NIRFSG_VAL_SINGLE_ENDED',
                    '15001 (0x3a99)',
                    'Sets the terminal configuration to single-ended.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'IQOutPortTermCfg',
        'lv_property': 'Device Specific:Vector Signal Transceiver:IQ Out Port:Terminal Configuration',
        'name': 'IQ_OUT_PORT_TERMINAL_CONFIGURATION',
        'type': 'ViInt32'
    },
    1150147: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the amplitude of the generated signal in volts, peak-to-peak (V). For example, if you set this attribute to 1.0, the output signal ranges from -0.5 volts to 0.5 volts.\n\n                To use this attribute, you must use the channelName parameter of the nirfsg_SetAttributeViReal64 function to specify the name of the channel you are configuring. For the PXIe-5645, you can configure the I and Q channels by using I or Q as the channel string, or set the channel string to "" (empty string) to configure both channels. For the PXIe-5820, the only valid value for the channel string is "" (empty string).\n\n                To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                Refer to the specifications document for your device for allowable output levels.\n\n                **Units:** Volts, peak-to-peak (V\\ :sub:`pk-pk`\\ )\n\n                **Valid Values:**\n\n                PXIe-5645: 1V\\ :sub:`pk-pk`\\  maximum if you set the NIRFSG_ATTR_IQ_OUT_PORT_TERMINAL_CONFIGURATION attribute to NIRFSG_VAL_DIFFERENTIAL, and 0.5V\\ :sub:`pk-pk`\\ \n\nmaximum if you set the NIRFSG_ATTR_IQ_OUT_PORT_TERMINAL_CONFIGURATION attribute to NIRFSG_VAL_SINGLE_ENDED.\n\n                PXIe-5820: 3.4V\\ :sub:`pk-pk`\\ maximum for signal bandwidth less than 160MHz, and 2V\\ :sub:`pk-pk`\\ \n\nmaximum for signal bandwidth greater than 160MHz.\n\n                **Default Value:** 0.5volts\n\n                **Supported Devices:** PXIe-5645, PXIe-5820\n            ',
            'note': '- For the PXIe-5645, this attribute is ignored if you are using the RF ports.\n\n - The valid values are only applicable when you set the NIRFSG_ATTR_IQ_OUT_PORT_LOAD_IMPEDANCE attribute to 50 Ω and when you set the NIRFSG_ATTR_IQ_OUT_PORT_OFFSET attribute to 0.'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:IQ Out Port:Level',
        'name': 'IQ_OUT_PORT_LEVEL',
        'type': 'ViReal64'
    },
    1150148: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the common-mode offset applied to the signals generated at each differential output terminal. This attribute applies only when you set the NIRFSG_ATTR_IQ_OUT_PORT_TERMINAL_CONFIGURATION attribute to NIRFSG_VAL_DIFFERENTIAL. Common-mode offset shifts both positive and negative terminals in the same direction.\n\n                To use this attribute, you must use the channelName parameter of the nirfsg_SetAttributeViReal64 function to specify the name of the channel you are configuring. For the PXIe-5645, you can configure the I and Q channels by using I or Q as the channel string, or set the channel string to "" (empty string) to configure both channels. For the PXIe-5820, the only valid value for the channel string is "" (empty string).\n\n                To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                **Units:** Volts\n\n                **Valid Values:**\n\n                PXIe-5645: -0.8V to 0.8V if you set the NIRFSG_ATTR_IQ_OUT_PORT_LOAD_IMPEDANCE attribute to 50 Ω. The valid values are -1.2V to 1.2V if you set the NIRFSG_ATTR_IQ_OUT_PORT_LOAD_IMPEDANCE attribute to 100 Ω.\n\n                PXIe-5820: -0.25V to 1.5V\n\n                **Supported Devices:** PXIe-5645, PXIe-5820\n            ',
            'note': '- For the PXIe-5645, this attribute is ignored if you are using the RF ports.\n\n - The valid range is dependent on the load impedance.'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:IQ Out Port:Common Mode Offset',
        'name': 'IQ_OUT_PORT_COMMON_MODE_OFFSET',
        'type': 'ViReal64'
    },
    1150149: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the value, in volts, that the signal generator adds to the arbitrary waveform data. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                To use this attribute, you must use the channelName parameter of the nirfsg_SetAttributeViReal64 function to specify the name of the channel you are configuring. For the PXIe-5645, you can configure the I and Q channels by using I or Q as the channel string, or set the channel string to "" (empty string) to configure both channels. For the PXIe-5820, the only valid value for the channel string is "" (empty string).\n\n                PXIe-5645: The waveform may be scaled in DSP prior to adding offset and the device state may be changed in order to accommodate the requested offset.\n\n                PXIe-5820: The waveform is not automatically scaled in DSP. To prevent DSP overflows, use the NIRFSG_ATTR_ARB_PRE_FILTER_GAIN attribute to scale the waveform to provide additional headroom for offsets.\n\n                **Units:** Volts\n\n                **Supported Devices:** PXIe-5645, PXIe-5820\n            ',
            'note': 'For the PXIe-5645, this attribute is ignored if you are using the RF ports.'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:IQ Out Port:Offset',
        'name': 'IQ_OUT_PORT_OFFSET',
        'type': 'ViReal64'
    },
    1150150: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies whether to use the internal or external local oscillator (LO) source. If the NIRFSG_ATTR_LO_SOURCE attribute is set to "" (empty string), NI-RFSG uses the internal LO source. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                To use this attribute for the PXIe-5830/5831/5832, you must use the channelName parameter of the nirfsg_SetAttributeViString function to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).\n\n                **Default Value:** NIRFSG_VAL_LO_SOURCE_ONBOARD_STR\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842\n\n                **Related Topics**\n\n                `PXIe-5830 LO Sharing Using NI-RFSA and NI-RFSG <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/lo_sharing_using_rfsa_rfsg.html>`_\n\n                `PXIe-5831/5832 LO Sharing Using NI-RFSA and NI-RFSG <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/lo_sharing_using_rfsa_rfsg.html>`_\n            \n            **Defined Values**:\n            ',
            'note': 'For the PXIe-5841 with PXIe-5655, RF list mode is not supported when this attribute is set to NIRFSG_VAL_LO_SOURCE_SG_SA_SHARED_STR.',
            'table_body': [
                [
                    'NIRFSG_VAL_LO_SOURCE_AUTOMATIC_SG_SA_SHARED_STR',
                    'Automatic_SG_SA_Shared',
                    'NI-RFSG internally makes the configuration to share the LO between NI-RFSA and NI-RFSG. This value is valid only on the PXIe-5820/5830/5831/5832/5840/5841/5842.'
                ],
                [
                    'NIRFSG_VAL_LO_SOURCE_LO_IN_STR',
                    'LO_In',
                    'Uses an external LO as the LO source. Connect a signal to the LO IN connector on the device and use the NIRFSG_ATTR_UPCONVERTER_CENTER_FREQUENCY attribute to specify the LO frequency.'
                ],
                [
                    'NIRFSG_VAL_LO_SOURCE_ONBOARD_STR',
                    'Onboard',
                    'Uses an internal LO as the LO source. If you specify an internal LO source, the LO is generated inside the device itself.'
                ],
                [
                    'NIRFSG_VAL_LO_SOURCE_SG_SA_SHARED_STR',
                    'SG_SA_Shared',
                    'Uses the same internal LO during NI-RFSA and NI-RFSG sessions. NI-RFSG selects an internal synthesizer and the synthesizer signal is switched to both the RF In and RF Out mixers. This value is valid only on the PXIe-5830/5831/5832/5841 with PXIe-5655/5842.'
                ],
                [
                    'NIRFSG_VAL_LO_SOURCE_SECONDARY_STR',
                    'Secondary',
                    'Uses the PXIe-5831/5840 internal LO as the LO source. This value is valid only on the PXIe-5831 with PXIe-5653 and PXIe-5832 with PXIe-5653.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'LoSource',
        'lv_property': 'Device Specific:Vector Signal Transceiver:Signal Path:LO Source',
        'name': 'LO_SOURCE',
        'type': 'ViString'
    },
    1150151: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the step size for tuning the local oscillator (LO) phase-locked loop (PLL).\n\n                When the NIRFSG_ATTR_LO_PLL_FRACTIONAL_MODE_ENABLED attribute is enabled, the specified step size affects the fractional spur performance of the device. When the NIRFSG_ATTR_LO_PLL_FRACTIONAL_MODE_ENABLED attribute is disabled, the specified step size affects the phase noise performance of the device.\n\n                The valid values for this attribute depend on the NIRFSG_ATTR_LO_PLL_FRACTIONAL_MODE_ENABLED attribute.\n\n                **PXIe-5644/5645/5646**—If you disable the NIRFSG_ATTR_LO_PLL_FRACTIONAL_MODE_ENABLED attribute, the specified value is coerced to the nearest valid value.\n\n                **PXIe-5840/5841**—If you disable the NIRFSG_ATTR_LO_PLL_FRACTIONAL_MODE_ENABLED attribute, the specified value is coerced to the nearest valid value that is less than or equal to the desired step size.\n\n                **Units:** hertz (Hz)\n\n                **Default Values:**\n\n                PXIe-5644/5645/5646: 200kHz\n\n                PXIe-5830: 2MHz\n\n                PXIe-5831/5832 (RF port): 8MHz\n\n                PXIe-5831/5832 (IF port): 2MHz, 4MHz\n\n                PXIe-5840/5841:\n\n                - Fractional mode: 500 kHz\n                - Integer mode: 10 MHz for frequencies less than or equal to 4 GHz. 20 MHz for frequencies greater than 4 GHz.\n\n                PXIe-5841 with PXIe-5655: 500kHz\n\n                PXIe-5842: 1Hz\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842\n\n            ',
            'note': 'Values up to 100 MHz are coerced to 50 MHz.',
            'table_body': [
                [
                    'NIRFSG_ATTR_LO_FREQUENCY_STEP_SIZE Attribute Valid Values on PXIe-5644/5645',
                    '50 kHz to 24 MHz',
                    '4 MHz, 5 MHz, 6 MHz, 12 MHz, or 24 MHz'
                ],
                [
                    'NIRFSG_ATTR_LO_FREQUENCY_STEP_SIZE Attribute Valid Values on PXIe-5646',
                    '50 kHz to 25 MHz',
                    '2 MHz, 5 MHz, 10 MHz, or 25 MHz'
                ],
                [
                    'NIRFSG_ATTR_LO_FREQUENCY_STEP_SIZE Attribute Valid Values on PXIe-5840/5841',
                    '50 kHz to 100 MHz',
                    '1 MHz, 5 MHz, 10 MHz, 25 MHz, 50 MHz, or 100 MHz'
                ],
                [
                    'NIRFSG_ATTR_LO_FREQUENCY_STEP_SIZE Attribute Valid Values on PXIe-5830/5831/ 5832 LO1',
                    '8 Hz to 400 MHz',
                    '—'
                ],
                [
                    'NIRFSG_ATTR_LO_FREQUENCY_STEP_SIZE Attribute Valid Values on PXIe-5830/5831/ 5832 LO2',
                    '4 Hz to 400 MHz',
                    '—'
                ],
                [
                    'NIRFSG_ATTR_LO_FREQUENCY_STEP_SIZE Attribute Valid Values on PXIe-5841 with PXIe-5655/NI PXIe-5842 (See note)',
                    '1 nHz to 100 MHz',
                    '1 nHz to 50 MHz'
                ]
            ],
            'table_header': [
                'NIRFSG_ATTR_LO_PLL_FRACTIONAL_MODE_ENABLED Attribute Setting',
                'NIRFSG_VAL_ENABLE',
                'NIRFSG_VAL_DISABLE'
            ]
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Signal Path:LO Frequency Step Size (Hz)',
        'name': 'LO_FREQUENCY_STEP_SIZE',
        'type': 'ViReal64'
    },
    1150152: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies whether to use fractional mode for the local oscillator (LO) phase-locked loop (PLL). This attribute enables or disables fractional frequency tuning in the LO. Fractional mode provides a finer frequency step resolution and allows smaller values for the NIRFSG_ATTR_LO_FREQUENCY_STEP_SIZE attribute. However, fractional mode may introduce non-harmonic spurs.\n\n                This attribute applies only if you set the NIRFSG_ATTR_LO_SOURCE attribute to NIRFSG_VAL_LO_SOURCE_ONBOARD_STR.\n\n                To use this attribute for the PXIe-5830/5831/5832, you must use the channelName parameter of the nirfsg_SetAttributeViInt32 function to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).\n\n                **Default Value:** NIRFSG_VAL_ENABLE\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842\n\n                **Related Topics**\n\n                Refer to the local oscillators topic appropriate to your device for more information about using fractional mode.\n            \n            **Defined Values**:\n            ',
            'note': 'For the PXIe-5841 with PXIe-5655, this attribute is ignored if the PXIe-5655 is used as the LO source.',
            'table_body': [
                [
                    'NIRFSG_VAL_ENABLE',
                    '0 (0x0)',
                    'Disables fractional mode for the LO PLL.'
                ],
                [
                    'NIRFSG_VAL_DISABLE',
                    '1 (0x1)',
                    'Enables fractional mode for the LO PLL.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'LoPlLfractionalModeEnabled',
        'lv_property': 'Device Specific:Vector Signal Transceiver:Signal Path:LO PLL Fractional Mode Enabled',
        'name': 'LO_PLL_FRACTIONAL_MODE_ENABLED',
        'type': 'ViInt32'
    },
    1150153: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the delay, in seconds, to apply to the I/Q waveform. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                **Units:** Seconds\n\n                **Valid Values:** Plus or minus half of one I/Q sample period\n\n                **Supported Devices:** PXIe-5644/5645/5646\n                '
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Signal Path:Interpolation Delay',
        'name': 'INTERPOLATION_DELAY',
        'type': 'ViReal64'
    },
    1150154: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the delay, in seconds, applied to the Started Event, Done Event, and all Marker Events with respect to the analog output of the RF signal generator. To set this attribute, the NI-RFSG device must be in the Configuration or Generation state.\n\n                By default, markers and events are delayed to align with the waveform data generated from the device. This attribute adds an additional delay to markers and events. Use this attribute to adjust the time delay between events and the corresponding data.\n\n                **Units:** Seconds\n\n                **Valid Values:**\n\n                PXIe-5644/5645: -1.217 μs to 67.050 μs\n\n                PXIe-5646: -0.896 μs to 64.640 μs\n\n                PXIe-5820/5830/5831/5832/5840/5841/5842: 0 μs to 3.276 μs\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842\n\n                **Related Topics**\n\n                `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_\n            ',
            'note': 'If you decrease the event delay during generation, some markers may be dropped.'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Events:Events Delay',
        'name': 'EVENTS_DELAY',
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    1150155: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies whether the device is the master device when synchronizing the Start Trigger. The master device distributes the synchronized Start Trigger to all devices in the system through the Start Trigger distribution line.\n\n                When synchronizing the Start Trigger, one device must always be designated as the master. The master device actively drives the Start Trigger distribution line. For slave devices, set the NIRFSG_ATTR_START_TRIGGER_TYPE attribute to digital edge, and set the NIRFSG_ATTR_DIGITAL_EDGE_START_TRIGGER_SOURCE attribute to sync_script.\n\n                To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                **Default Value:** VI_FALSE\n\n                **Supported Devices:** PXIe-5644/5645/5646\n\n                **Related Topics**\n\n                `Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_\n\n                Refer to the Synchronization Using NI-RFSA and NI-RFSG topic appropriate to your device for more information about device synchronization for vector signal transceivers.\n            \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'VI_TRUE',
                    'The device is the master device for synchronizing the Start Trigger.'
                ],
                [
                    'VI_FALSE',
                    'The device is not the master for synchronizing the Start Trigger.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Triggers:Sync Start Trigger Master',
        'name': 'SYNC_START_TRIGGER_MASTER',
        'type': 'ViBoolean'
    },
    1150156: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies which external trigger line distributes the synchronized Start Trigger signal. When synchronizing the Start Trigger, configure all devices to use the same Start Trigger distribution line.\n\n                To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                **Valid Values:** PXI_Trig0, PXI_Trig1, PXI_Trig2, PXI_Trig3, PXI_Trig4, PXI_Trig5, PXI_Trig6, PXI_Trig7, PFI0\n\n                **Default Value:** "" (empty string)\n\n                **Supported Devices:** PXIe-5644/5645/5646\n\n                **Related Topics**\n\n                `Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_\n\n                Refer to the Synchronization Using NI-RFSA and NI-RFSG topic appropriate to your device for more information about device synchronization for vector signal transceivers.\n                '
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Triggers:Sync Start Trigger Dist Line',
        'name': 'SYNC_START_TRIGGER_DIST_LINE',
        'type': 'ViString'
    },
    1150157: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the repetition mode of a waveform when you set the NIRFSG_ATTR_GENERATION_MODE attribute to NIRFSG_VAL_ARB_WAVEFORM. If you set this attribute to VI_TRUE, the number of repetitions is determined by the NIRFSG_ATTR_ARB_WAVEFORM_REPEAT_COUNT attribute. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                **Default Value:** VI_FALSE\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n            \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'VI_TRUE',
                    'Repeats the waveform a finite number of times.'
                ],
                [
                    'VI_FALSE',
                    'Repeats the waveform continuously until you abort the generation.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'lv_property': 'Arb:Waveform Repeat Count Is Finite',
        'name': 'ARB_WAVEFORM_REPEAT_COUNT_IS_FINITE',
        'type': 'ViBoolean'
    },
    1150158: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the repeat count of a waveform when you set the NIRFSG_ATTR_ARB_WAVEFORM_REPEAT_COUNT_IS_FINITE attribute to VI_TRUE. This attribute is valid only when you set the NIRFSG_ATTR_GENERATION_MODE attribute to NIRFSG_VAL_ARB_WAVEFORM. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                **Default Value:** 1\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n                '
        },
        'lv_property': 'Arb:Waveform Repeat Count',
        'name': 'ARB_WAVEFORM_REPEAT_COUNT',
        'type': 'ViInt32'
    },
    1150160: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                This attribute offsets the NIRFSG_ATTR_UPCONVERTER_CENTER_FREQUENCY from the RF frequency. Use this attribute to keep the local oscillator (LO) leakage at a determined offset from the RF signal.\n\n                **Valid Values:**\n\n                PXIe-5644/5645: -42MHz to +42MHz\n\n                PXIe-5646: -100MHz to +100MHz\n\n                PXIe-5830/5831/5832/5840/5841: -500MHz to +500MHz\n\n                PXI-5842 (500 MHz bandwidth option): -250MHz to +250MHz\n\n                PXI-5842 (1 GHz bandwidth option): -500MHz to +500MHz\n\n                PXI-5842 (2 GHz bandwidth option): -1GHz to +1GHz\n\n                PXIe-5842 (4 GHz bandwidth option) using the Standard personality: -1GHz to +1GHz\n\n                PXIe-5842 (4 GHz bandwidth option) using the 4 GHz Bandwidth personality: -2GHz to +2GHz\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842\n\n                **Related Topics**\n\n                `PXIe-5830 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_selection.html>`_\n\n                `PXIe-5831/5832 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_selection.html>`_\n\n                `PXIe-5841 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_selection.html>`_\n            ',
            'note': '- You cannot set the NIRFSG_ATTR_UPCONVERTER_CENTER_FREQUENCY attribute or the NIRFSG_ATTR_ARB_CARRIER_FREQUENCY attribute at the same time as the NIRFSG_ATTR_UPCONVERTER_FREQUENCY_OFFSET attribute.\n\n - Resetting this attribute disables the upconverter frequency offset.'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Upconverter:Frequency Offset (Hz)',
        'name': 'UPCONVERTER_FREQUENCY_OFFSET',
        'type': 'ViReal64'
    },
    1150161: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns the temperature, in degrees Celsius, of the I/Q Out circuitry on the device.\n\n                **Units:** Degrees Celsius\n\n                **Supported Devices:** PXIe-5645, PXIe-5820\n            ',
            'note': 'If you query this attribute during RF list mode, list steps may take longer to complete during list execution.'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:IQ Out Port:Temperature (Degrees C)',
        'name': 'IQ_OUT_PORT_TEMPERATURE',
        'type': 'ViReal64'
    },
    1150162: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the Marker Event at which RF blanking occurs. RF blanking quickly attenuates the RF OUT signal. Use Marker Events to toggle the state of RF blanking. The RF Output always starts in the unblanked state.\n\n                To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                You can specify Marker Events by using scripts to trigger blanking at a certain point in a waveform. For example, if you set this attribute to marker0 str}, and marker0 occurs on samples 1,000 and 2,000 of a script, then the RF Output will be blanked (attenuated) between samples 1,000 and 2,000.\n\n                PXIe-5645: This attribute is ignored if you are using the I/Q ports.\n\n                PXIe-5840/5841: RF blanking does not occur for frequencies below 120MHz.\n\n                For PXIe-5830/5831/5832: The RF Blanking reserves a PXI trigger line. If you are calling any nirfsg_Reset or `niRFSA_reset <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/cvinirfsa_reset.html>`_ on the same device, NI recommends calling it before committing blanking attributes. Alternatively, you can call nirfsg_ResetWithOptions or `niRFSA_ResetWithOptions <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/cvinirfsa_resetwithoptions.html>`_. Select **Routes** in the **steps to omit**parameter.\n\n                **Default Value:** "" (empty string)\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842\n\n                **Related Topics**\n\n                `Marker Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/marker_events.html>`_\n            \n            **Valid Values**:\n            ',
            'note': 'The shortest supported blanking interval is eight microseconds.',
            'table_body': [
                [
                    '"" (empty string)',
                    'RF blanking is disabled.'
                ],
                [
                    'Marker0',
                    'RF blanking is tied to marker0.'
                ],
                [
                    'Marker1',
                    'RF blanking is tied to marker1.'
                ],
                [
                    'Marker2',
                    'RF blanking is tied to marker2.'
                ],
                [
                    'Marker3',
                    'RF blanking is tied to marker3.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Signal Path:RF Blanking Source',
        'name': 'RF_BLANKING_SOURCE',
        'type': 'ViString'
    },
    1150163: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the load impedance connected to the I/Q OUT port. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                To use this attribute, you must use the channelName parameter of the nirfsg_SetAttributeViReal64 function to specify the name of the channel you are configuring. For the PXIe-5645, you can configure the I and Q channels by using I or Q as the channel string, or set the channel string to "" (empty string) to configure both channels. For the PXIe-5820, the only valid value for the channel string is "" (empty string).\n\n                **Units:** Ohms\n\n                **Valid Values:** Any value greater than 0. Values greater than or equal to 1 megaohms (MΩ) are interpreted as high impedance.\n\n                **Default Value:** 50 Ω if you set the NIRFSG_ATTR_IQ_OUT_PORT_TERMINAL_CONFIGURATION attribute to NIRFSG_VAL_SINGLE_ENDED, and 100 Ω if you set the NIRFSG_ATTR_IQ_OUT_PORT_TERMINAL_CONFIGURATION attribute to NIRFSG_VAL_DIFFERENTIAL.\n\n                **Supported Devices:** PXIe-5645, PXIe-5820\n            ',
            'note': 'For the PXIe-5645, this attribute is ignored if you are using the RF ports.'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:IQ Out Port:Load Impedance',
        'name': 'IQ_OUT_PORT_LOAD_IMPEDANCE',
        'type': 'ViReal64'
    },
    1150165: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the narrowband frequency modulation (FM) range to apply by sending the signal through an integrator.\n\n                This attribute is valid only when you set the NIRFSG_ATTR_ANALOG_MODULATION_TYPE attribute to NIRFSG_VAL_FM and the NIRFSG_ATTR_ANALOG_MODULATION_FM_BAND attribute to NIRFSG_VAL_NARROWBAND.\n                \n                **Default Value:** NIRFSG_VAL_100HZ_TO_1KHZ\n\n                **Supported Devices:** PXIe-5654/5654 with PXIe-5696\n\n                **Related Topics**\n\n                `Frequency Modulation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_5696_frequency_modulation.html>`_\n                \n                **Defined Values**:\n                ',
            'table_body': [
                [
                    'NIRFSG_VAL_100HZ_TO_1KHZ',
                    '18000 (0x4650)',
                    'Specifies a range from 100Â Hz to 1Â kHz.'
                ],
                [
                    'NIRFSG_VAL_10KHZ_TO_100KHZ',
                    '18002 (0x4652)',
                    'Specifies a range from 10Â kHz to 100Â kHz.'
                ],
                [
                    'NIRFSG_VAL_1KHZ_TO_10KHZ',
                    '18001 (0x4651)',
                    'Specifies a range from 1Â kHz to 10Â kHz.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'AnlgModFmNarrowbandIntegrator',
        'lv_property': 'Modulation:Analog:FM Narrowband Integrator',
        'name': 'ANALOG_MODULATION_FM_NARROWBAND_INTEGRATOR',
        'type': 'ViInt32'
    },
    1150166: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies an uncalibrated digital-to-analog converter (DAC) value that scales the input signal before the signal modulates the carrier. A value of 0 completely attenuates the signal, and a value of 100 passes the full-scale signal to the modulator.\n\n                **Default Value:** 100\n\n                **Valid Values:** 0 to 100\n\n                **Supported Devices:** PXIe-5654/5654 with PXIe-5696\n\n                **Related Topics**\n\n                `Frequency Modulation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_5696_frequency_modulation.html>`_\n                '
        },
        'lv_property': 'Modulation:Analog:FM Sensitivity',
        'name': 'ANALOG_MODULATION_FM_SENSITIVITY',
        'type': 'ViReal64'
    },
    1150167: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies an uncalibrated digital-to-analog converter (DAC) value that scales the input signal before the signal modulates the carrier. A value of 0 completely attenuates the signal, and a value of 100 passes the full-scale signal to the modulator.\n\n                When using the PXIe-5654 with PXIe-5696, NI-RFSG may coerce AM sensitivity. Coercing the AM sensitivity prevents overpower conditions at the PXIe-5696 input. Read this attribute to determine the coerced value.\n\n                **Default Value:** 100\n\n                **Valid Values:** 0 to 100\n\n                **Supported Devices:** PXIe-5654/5654 with PXIe-5696\n\n                **Related Topics**\n\n                `Amplitude Modulation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_5696_amplitude_modulation.html>`_\n                '
        },
        'lv_property': 'Modulation:Analog:AM Sensitivity',
        'name': 'ANALOG_MODULATION_AM_SENSITIVITY',
        'type': 'ViReal64'
    },
    1150168: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies an uncalibrated digital-to-analog converter (DAC) value that scales the input signal before the signal modulates the carrier. A value of 0 completely attenuates the signal, and a value of 100 passes the full-scale signal to the modulator.\n\n                **Default Value:** 100\n\n                **Valid Values:** 0 to 100\n\n                **Supported Devices:** PXIe-5654/5654 with PXIe-5696\n\n                **Related Topics**\n\n                `Phase Modulation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_5696_phase_modulation.html>`_\n                '
        },
        'lv_property': 'Modulation:Analog:PM Sensitivity',
        'name': 'ANALOG_MODULATION_PM_SENSITIVITY',
        'type': 'ViReal64'
    },
    1150173: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the level of attenuation in the attenuator path. Setting this attribute overrides the value chosen by NI-RFSG. Not all power levels are achievable if you set this attribute.\n\n                **Units**: dB\n\n                **Valid Values**: 0dB to 110dB in steps of 10\n\n                **Supported Devices:** PXIe-5654 with PXIe-5696\n            ',
            'note': 'Resetting this attribute reverts back to the default unset behavior.'
        },
        'lv_property': 'RF:Attenuator Setting (dB)',
        'name': 'ATTENUATOR_SETTING',
        'type': 'ViReal64'
    },
    1150175: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns whether the configuration list is still running or done. To read this attribute, the device must be in the Generation state.\n\n                **Supported Devices:** PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXIe-5673E\n\n                **Related Topics**\n\n                `RF List Mode <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/rf_list_mode_overview.html>`_\n\n                `Using RF List Mode <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/rf_list_mode.html>`_\n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'VI_TRUE',
                    'The configuration list is done.'
                ],
                [
                    'VI_FALSE',
                    'The configuration list is still running.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'lv_property': 'Configuration List:Configuration List Is Done',
        'name': 'CONFIGURATION_LIST_IS_DONE',
        'type': 'ViBoolean'
    },
    1150180: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies whether the device is the master device when synchronizing the Sample Clock between multiple devices. The master device distributes the Sample Clock sync signal to all devices in the system through the Sample Clock sync distribution line.\n\n                When synchronizing the Sample Clock, one device must always be designated as the master. The master device actively drives the Sample Clock sync distribution line.\n\n                To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                **Default Value:** VI_FALSE\n\n                **Supported Devices:** PXIe-5646\n\n                **Related Topics**\n\n                `Synchronization Using NI-RFSA and NI-RFSG <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/synchronization_rfsa_g.html>`_—Refer to this topic for more information about PXIe-5646 device synchronization.\n            \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'VI_TRUE',
                    'The device is the master device for synchronizing the Sample Clock.'
                ],
                [
                    'VI_FALSE',
                    'The device is not the master for synchronizing the Sample Clock.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Triggers:Sync Sample Clock Master',
        'name': 'SYNC_SAMPLE_CLOCK_MASTER',
        'type': 'ViBoolean'
    },
    1150181: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies which external trigger line distributes the Sample Clock sync signal. When synchronizing the Sample Clock between multiple devices, configure all devices to use the same Sample Clock sync distribution line.\n\n                To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                **Valid Values:** PXI_Trig0, PXI_Trig1, PXI_Trig2, PXI_Trig3, PXI_Trig4, PXI_Trig5, PXI_Trig6, PXI_Trig7, PFI0\n\n                **Default Value:** "" (empty string)\n\n                **Supported Devices:** PXIe-5646\n\n                **Related Topics**\n\n                `Synchronization Using NI-RFSA and NI-RFSG <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/synchronization_rfsa_g.html>`_—Refer to this topic for more information about PXIe-5646 device synchronization.\n                '
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Triggers:Sync Sample Clock Dist Line',
        'name': 'SYNC_SAMPLE_CLOCK_DIST_LINE',
        'type': 'ViString'
    },
    1150182: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns the amplitude extender module temperature in degrees Celsius.\n\n                **Units**: degrees Celsius (°C)\n\n                **Supported Devices:** PXIe-5654 with PXIe-5696\n                '
        },
        'lv_property': 'Device Characteristics:AE Temperature (Degrees C)',
        'name': 'AE_TEMPERATURE',
        'type': 'ViReal64'
    },
    1150185: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the amplification path to use. The low harmonic path provides greater second and third harmonic spurious response, and the high power path provides higher output power.\n\n                NI-RFSG automatically sets the value of this attribute based on power and frequency settings. Setting this attribute overrides the value chosen by NI-RFSG.\n\n                **Default Value:** NIRFSG_VAL_LOW_HARMONIC\n\n                **Supported Devices:** PXIe-5654 with PXIe-5696\n\n                **Related Topics**\n\n                `Low Harmonic Path Versus High Power Path <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/low_harmonic_path_vs_high_power_path.html>`_\n                \n            **Defined Values**:\n            ',
            'note': 'Resetting this attribute reverts back to the default unset behavior.',
            'table_body': [
                [
                    'NIRFSG_VAL_HIGH_POWER',
                    '16000 (0x3e80)',
                    'Sets the amplification path to use the high power path.'
                ],
                [
                    'NIRFSG_VAL_LOW_HARMONIC',
                    '16001 (0x3e81)',
                    'Sets the amplification path to use the low harmonic path.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'AmpPath',
        'lv_property': 'RF:Advanced:Amp Path',
        'name': 'AMP_PATH',
        'type': 'ViInt32'
    },
    1150186: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns a string containing the path to the location of the current NI-RFSG instrument driver FPGA extensions bitfile, a .lvbitx file, that is programmed on the device. You can specify the bitfile location using the Driver Setup string in the **optionString** parameter of the nirfsg_InitWithOptions function.\n\n                NI-RFSG instrument driver FPGA extensions enable you to use pre-compiled FPGA bitfiles to customize the behavior of the vector signal transceiver FPGA while maintaining the functionality of the NI-RFSG instrument driver.\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `NI-RFSG Instrument Driver FPGA Extensions <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/fpga_extensions.html>`_\n                '
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Device Characteristics:FPGA Bitfile Path',
        'name': 'FPGA_BITFILE_PATH',
        'type': 'ViString'
    },
    1150188: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns whether the NI RF signal generator has the fast tuning option available.\n\n                **Supported Devices:** PXIe-5654/5654 with PXIe-5696\n\n                **Related Topics**\n\n                `Frequency Tuning Times <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_tuning_times_5654.html>`_\n\n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'VI_TRUE',
                    'The RF signal generator has the fast 100 µs tuning option.'
                ],
                [
                    'VI_FALSE',
                    'The RF signal generator has the 1 ms tuning option.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'lv_property': 'Device Characteristics:Options:Fast Tuning Option',
        'name': 'FAST_TUNING_OPTION',
        'type': 'ViBoolean'
    },
    1150190: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                PXIe-5654/5654 with PXIe-5696: Specifies the pulse modulation mode to use.\n\n                PXIe-5842: This property allows you to choose a tradeoff between switching speed and On/Off Ratio when using pulse modulation. Refer to the product specifications document for the switching characteristics of each mode. This property is settable while the device is generating, but some output pulses may be dropped.\n\n                **Default Value:** NIRFSG_VAL_ANALOG\n\n                **Supported Devices:** PXIe-5842/5654/5654 with PXIe-5696\n            \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_OPTIMAL_MATCH',
                    'Provides for a more optimal power output match for the device during the off cycle of the pulse mode operation. Not supported on PXIe-5842.'
                ],
                [
                    'NIRFSG_VAL_PULSE_MODULATION_ANALOG_HIGH_ISOLATION',
                    'Allows for the best on/off power ratio of the pulsed signal.'
                ],
                [
                    'NIRFSG_VAL_PULSE_MODULATION_ANALOG',
                    'Analog switch blanking. Balance between switching speed and on/off power ratio of the pulsed signal.'
                ],
                [
                    'NIRFSG_VAL_PULSE_MODULATION_DIGITAL',
                    'Digital only modulation. Provides the best on/off switching speed of the pulsed signal at the cost of signal isolation.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'enum': 'PulseModulationMode',
        'lv_property': 'RF:Advanced:Pulse Modulation Mode',
        'name': 'PULSE_MODULATION_MODE',
        'type': 'ViInt32'
    },
    1150191: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the analog modulation frequency modulation (FM) band to use. Wideband FM allows for modulating signals higher than 100kHz. Narrowband FM allows for modulating lower frequency signals.\n\n                **Default Value:** NIRFSG_VAL_WIDEBAND\n\n                **Supported Devices:** PXIe-5654/5654 with PXIe-5696\n\n                **Related Topics**\n\n                `Frequency Modulation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_5696_frequency_modulation.html>`_\n\n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_NARROWBAND',
                    '17000 (0x4268)',
                    'Specifies narrowband frequency modulation.'
                ],
                [
                    'NIRFSG_VAL_WIDEBAND',
                    '17001 (0x4269)',
                    'Specifies wideband frequency modulation.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'AnlgModFmBand',
        'lv_property': 'Modulation:Analog:FM Band',
        'name': 'ANALOG_MODULATION_FM_BAND',
        'type': 'ViInt32'
    },
    1150192: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the phase modulation (PM) mode to use.\n\n                **Default Value:** NIRFSG_VAL_LOW_PHASE_NOISE\n\n                **Supported Devices:** PXIe-5654/5654 with PXIe-5696\n\n                **Related Topics**\n\n                `Phase Modulation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_5696_phase_modulation.html>`_\n\n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_HIGH_DEVIATION',
                    '19000 (0x4a38)',
                    'Specifies high deviation. High deviation comes at the expense of a higher phase noise.'
                ],
                [
                    'NIRFSG_VAL_LOW_PHASE_NOISE',
                    '19001 (0x4a39)',
                    'Specifies low phase noise. Low phase noise comes at the expense of a lower maximum deviation.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'AnlgModPmMode',
        'lv_property': 'Modulation:Analog:PM Mode',
        'name': 'ANALOG_MODULATION_PM_MODE',
        'type': 'ViInt32'
    },
    1150194: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns the name of the fully qualified signal name as a string.\n\n                **Supported Devices:** PXIe-5654/5654 with PXIe-5696, PXIe-5820/5830/5831/5832/5840/5841/5842\n\n                **Default Values**:\n\n                PXIe-5654/5654 with PXIe-5696: /*ModuleName*/ConfigurationSettledEvent, where *ModuleName* is the name of your device in MAX.\n\n                PXIe-5830/5831/5832: /*BasebandModule*/ao/0/ConfigurationSettledEvent, where *BasebandModule* is the name of the baseband module of your device in MAX.\n\n                PXIe-5820/5840/5841/5842: /*ModuleName*/ao/0/ConfigurationSettledEvent, where *ModuleName* is the name of your device in MAX.\n\n                **Related Topics**\n\n                `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_\n\n                `Syntax for Terminal Names <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/syntax_for_terminal_names.html>`_\n                '
        },
        'lv_property': 'Events:Configuration Settled Event Terminal Name',
        'name': 'CONFIGURATION_SETTLED_EVENT_TERMINAL_NAME',
        'type': 'ViString'
    },
    1150195: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Enables or disables the automatic leveling control (ALC).\n\n                PXIe-5654 with PXIe-5696: If this attribute is enabled, the ALC is closed (closed-loop mode) and allows for better amplitude accuracy and wider amplitude dynamic range. If this attribute is disabled, the ALC is open (open-loop mode), which is ideal when using modulation. Disabling the NIRFSG_ATTR_ALC_CONTROL attribute also allows for NI-RFSG to perform an automatic power search.\n\n                PXIe-5654: NIRFSG_VAL_DISABLE is the only supported value for this device. The PXIe-5654 does not support the ALC when used as a stand-alone device.\n\n                **Default Value:**\n\n                PXIe-5654: NIRFSG_VAL_DISABLE\n\n                PXIe-5654 with PXIe-5696: NIRFSG_VAL_ENABLE\n\n                **Supported Devices:** PXIe-5654/5654 with PXIe-5696\n\n                **Related Topics**\n\n                `Power Level Adjustment <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_power_level_adjustment.html>`_\n\n                `ALC Closed Loop Versus Open Loop <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_alc_closed_loop_vs_open_loop.html>`_\n\n                `Power Search <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_power_search.html>`_\n\n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_DISABLE',
                    '0 (0x0)',
                    'Disables ALC.'
                ],
                [
                    'NIRFSG_VAL_ENABLE',
                    '1 (0x1)',
                    'Enables the ALC.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'AutomaticLevelControl',
        'lv_property': 'RF:ALC Control',
        'name': 'ALC_CONTROL',
        'type': 'ViInt32'
    },
    1150196: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Enables or disables automatic power search. When this attribute is enabled, a power search performs after the device is initiated, after output power is enabled, or when the frequency or power level changes while the device is generating. When this attribute is disabled, NI-RFSG does not perform a power search unless you call the nirfsg_PerformPowerSearch function.\n\n                This attribute is ignored when the NIRFSG_ATTR_ALC_CONTROL attribute is enabled.\n\n                PXIe-5654: NIRFSG_VAL_DISABLE is the only supported value for this device.\n\n                **Default Value:**\n\n                PXIe-5654: NIRFSG_VAL_DISABLE\n\n                PXIe-5654 with PXIe-5696: NIRFSG_VAL_ENABLE\n\n                **Supported Devices:** PXIe-5654/5654 with PXIe-5696\n\n                **Related Topics**\n\n                `Power Search <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_power_search.html>`_\n\n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_DISABLE',
                    '0 (0x0)',
                    'Disables automatic power search.'
                ],
                [
                    'NIRFSG_VAL_ENABLE',
                    '1 (0x1)',
                    'Enables automatic power search.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'AutomaticPowerSearch',
        'lv_property': 'RF:Automatic Power Search',
        'name': 'AUTO_POWER_SEARCH',
        'type': 'ViInt32'
    },
    1150199: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the frequency of the LO source.\n\n                To use this attribute for the PXIe-5830/5831/5832, you must use the channelName parameter of the nirfsg_SetAttributeViReal64 function to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).\n\n                **Supported Devices**: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842\n\n                **Related Topics**\n\n                `PXIe-5830 Frequency and Bandwidth Configuration <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_configuration.html>`_\n\n                `PXIe-5831/5832 Frequency and Bandwidth Configuration <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_configuration.html>`_\n            ',
            'note': 'This attribute is read/write if you are using an external LO. Otherwise, this attribute is read-only.'
        },
        'lv_property': 'RF:LO Frequency (Hz)',
        'name': 'LO_FREQUENCY',
        'type': 'ViReal64'
    },
    1150204: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the digital gain, in decibels. The digital gain is applied to the waveform data after filtering. Use this attribute to adjust the output power of the device while keeping the analog path fixed. This may cause clipping, overflows, or quantization noise if used improperly.\n\n                To set this attribute, the NI-RFSG device must be in the Configuration or Generation state.\n\n                **Default Value:** 0 dB\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n                '
        },
        'name': 'ARB_DIGITAL_GAIN',
        'type': 'ViReal64'
    },
    1150206: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the output behavior for the Marker Event. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                **Default Value:** NIRFSG_VAL_PULSE\n\n                **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842\n\n                **Related Topics**\n\n                `Marker Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/marker_events.html>`_\n            \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_PULSE',
                    '23000 (0x59d8)',
                    'Specifies the Marker Event output behavior as pulse.'
                ],
                [
                    'NIRFSG_VAL_TOGGLE',
                    '23001 (0x59d9)',
                    'Specifies the Marker Event output behavior as toggle.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'MarkerEventOutputBehavior',
        'lv_property': 'Events:Marker:Output Behavior',
        'name': 'MARKER_EVENT_OUTPUT_BEHAVIOR',
        'repeated_capability_type': 'markers',
        'supported_rep_caps': [
            'markers'
        ],
        'type': 'ViInt32'
    },
    1150207: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the pulse width value for the Marker Event. Use the NIRFSG_ATTR_MARKER_EVENT_PULSE_WIDTH_UNITS attribute to set the units for the pulse width value. This attribute is valid only when the NIRFSG_ATTR_MARKER_EVENT_OUTPUT_BEHAVIOR attribute is set to NIRFSG_VAL_PULSE.\n\n                To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                **Default Value:** 200 ns\n\n                **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842\n\n                **Related Topics**\n\n                `Marker Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/marker_events.html>`_\n                '
        },
        'lv_property': 'Events:Marker:Pulse:Width Value',
        'name': 'MARKER_EVENT_PULSE_WIDTH',
        'repeated_capability_type': 'markers',
        'supported_rep_caps': [
            'markers'
        ],
        'type': 'ViReal64'
    },
    1150208: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the pulse width units for the Marker Event. This attribute is valid only when the NIRFSG_ATTR_MARKER_EVENT_OUTPUT_BEHAVIOR attribute is set to NIRFSG_VAL_PULSE.\n\n                To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                **Default Value:** NIRFSG_VAL_SECONDS\n\n                **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842\n\n                **Related Topics**\n\n                `Marker Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/marker_events.html>`_\n            \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_PULSE',
                    '23000 (0x59d8)',
                    'Specifies the Marker Event output behavior as pulse.'
                ],
                [
                    'NIRFSG_VAL_TOGGLE',
                    '23001 (0x59d9)',
                    'Specifies the Marker Event output behavior as toggle.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'MarkerEventPulseWidthUnits',
        'lv_property': 'Events:Marker:Pulse:Width Units',
        'name': 'MARKER_EVENT_PULSE_WIDTH_UNITS',
        'repeated_capability_type': 'markers',
        'supported_rep_caps': [
            'markers'
        ],
        'type': 'ViInt32'
    },
    1150209: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the initial state for the Marker Event when the NIRFSG_ATTR_MARKER_EVENT_OUTPUT_BEHAVIOR attribute is set to NIRFSG_VAL_TOGGLE.\n\n                To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                **Default Value:** NIRFSG_VAL_DIGITAL_LOW\n\n                **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842\n\n                **Related Topics**\n\n                `Marker Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/marker_events.html>`_\n            \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_DIGITAL_HIGH',
                    '21001 (0x5209)',
                    'Specifies the initial state of the Marker Event toggle behavior as digital high.'
                ],
                [
                    'NIRFSG_VAL_DIGITAL_LOW',
                    '21000 (0x5208)',
                    'Specifies the initial state of the Marker Event toggle behavior as digital low.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'MarkerEventToggleInitialState',
        'lv_property': 'Events:Marker:Toggle:Initial State',
        'name': 'MARKER_EVENT_TOGGLE_INITIAL_STATE',
        'repeated_capability_type': 'markers',
        'supported_rep_caps': [
            'markers'
        ],
        'type': 'ViInt32'
    },
    1150210: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns the total power consumption of the device.\n\n                **Units:** watts\n\n                **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n            ',
            'note': 'If you query this attribute during RF list mode, list steps may take longer to complete during list execution.'
        },
        'lv_property': 'Device Characteristics:Module Power Consumption (W)',
        'name': 'MODULE_POWER_CONSUMPTION',
        'type': 'ViReal64'
    },
    1150211: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns the FPGA temperature in degrees Celsius.\n\n                Serial signals between the sensor and the system control unit can potentially modulate the signal being generated, thus causing phase spurs. After the device thoroughly warms up, its temperature varies only slightly (less than 1 degree Celsius) and slowly, and it is not necessary to constantly poll this temperature sensor.\n\n                **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n            ',
            'note': 'If you query this attribute during RF list mode, list steps may take longer to complete during list execution.'
        },
        'lv_property': 'Device Characteristics:FPGA Temperature (Degrees C)',
        'name': 'FPGA_TEMPERATURE',
        'type': 'ViReal64'
    },
    1150212: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the minimum time between temperature sensor readings.\n\n                **Units:** Seconds\n\n                **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n                '
        },
        'lv_property': 'Device Characteristics:Temperature Read Interval',
        'name': 'TEMPERATURE_READ_INTERVAL',
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    1150217: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies whether peer-to-peer should continuously generate data from the peer-to-peer stream or from only a finite number of samples, according to the NIRFSG_ATTR_P2P_NUMBER_OF_SAMPLES_TO_GENERATE attribute. To use this attribute, peer-to-peer must be enabled. This attribute is endpoint-based.\n\n                **Default Value**: VI_FALSE\n\n                **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842\n            \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'VI_TRUE',
                    'Data is generated from only a finite number of samples.'
                ],
                [
                    'VI_FALSE',
                    'Data is continuously generated from the peer-to-peer stream.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'lv_property': 'Peer-to-Peer:Is Finite Generation',
        'name': 'P2P_IS_FINITE_GENERATION',
        'type': 'ViBoolean'
    },
    1150218: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies how many samples are generated from the peer-to-peer subsystem when it is enabled. To use this attribute, peer-to-peer must be enabled and set to finite generation. This attribute is endpoint-based.\n\n                **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842\n\n                **Related Topics**\n\n                `Configuring a Peer-to-Peer Endpoint <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/p2p_configuring_an_endpoint.html>`_\n                '
        },
        'lv_property': 'Peer-to-Peer:Number Of Samples To Generate',
        'name': 'P2P_NUMBER_OF_SAMPLES_TO_GENERATE',
        'type': 'ViInt64'
    },
    1150219: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns how many samples NI-RFSG pulls from the peer-to-peer FIFO per read. You can use this attribute to determine how many samples to send across the peer-to-peer bus to ensure that no samples are ignored. If you send a number of samples that is not a multiple of this value, the remaining samples are not read from the FIFO during generation. This attribute is endpoint-based.\n\n                **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842\n                '
        },
        'lv_property': 'Peer-to-Peer:Generation FIFO Sample Quantum',
        'name': 'P2P_GENERATION_FIFO_SAMPLE_QUANTUM',
        'type': 'ViInt64'
    },
    1150220: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the delay, in seconds, to apply to the I/Q waveform.\n\n                Relative delay allows for delaying the generated signal from one device relative to the generated signal of another device after those devices have been synchronized. You can achieve a negative relative delay by delaying both synchronized devices by the same value (1 μs) before generation begins and then changing the relative delay to a smaller amount than the initial value on only one of the devices.\n\nTo set this attribute, the NI-RFSG device must be in the Configuration or Generation state.\n\n                **Units:** Seconds\n\n                **Valid Values:**\n\n                PXIe-PXIe-5820/5830/5831/5832/5840/5841: 0 μs to 3.2 μs\n\n                PXIe-5842: 0 μs to 6.5 μs\n\n                **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842\n\n                **Related Topics**\n\n                `NI-TClk Overview <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_tclk_help.html>`_\n            ',
            'note': '- To obtain a negative relative delay when synchronizing the PXIe-5840/5841 with a module that does not support this attribute, use the NITCLK_ATTR_SAMPLE_CLOCK_DELAY attribute.\n\n - The resolution of this attribute is a function of the I/Q sample period at 15E(-6) of the sample period but not worse than one Sample Clock period.'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Signal Path:Relative Delay',
        'name': 'RELATIVE_DELAY',
        'type': 'ViReal64'
    },
    1150225: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the sub-Sample Clock delay, in seconds, to apply to the I/Q waveform. Use this attribute to reduce the trigger jitter when synchronizing multiple devices with NI-TClk. This attribute can also help maintain synchronization repeatability by writing the absolute delay value of a previous measurement to the current session.\n\n                To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                **Units:** Seconds\n\n                **Valid Values:** Plus or minus half of one Sample Clock period\n\n                **Supported Devices:** PXIe-5820/5840/5841/5842\n                ',
            'note': '- The resolution of this attribute is a function of the I/Q sample period at 15E(-6) times that sample period.\n\n - If this attribute is set, NI-TClk cannot perform any sub-Sample Clock adjustment.'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Signal Path:Absolute Delay',
        'name': 'ABSOLUTE_DELAY',
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    1150226: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the bandwidth of the device. The instantaneous bandwidth is the effective real-time bandwidth of the signal path for your configuration.\n\n                The NIRFSG_ATTR_SIGNAL_BANDWIDTH centered at the NIRFSG_ATTR_FREQUENCY must fit within the device instantaneous bandwidth, which is centered at the NIRFSG_ATTR_UPCONVERTER_CENTER_FREQUENCY.\n\n                **Units**: Hz\n\n                **Default Value**: N/A\n\n                **Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `PXIe-5830 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_selection.html>`_\n\n                `PXIe-5831/5832 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_selection.html>`_\n\n                `PXIe-5841 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_selection.html>`_\n                '
        },
        'lv_property': 'Arb:Device Instantaneous Bandwidth (Hz)',
        'name': 'DEVICE_INSTANTANEOUS_BANDWIDTH',
        'type': 'ViReal64'
    },
    1150228: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Configures error reporting for onboard signal processing (OSP) overflows. Overflows lead to clipping of the waveform.\n\n                **Default Value:** NIRFSG_VAL_ERROR_REPORTING_WARNING\n\n                **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n            \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_ERROR_REPORTING_DISABLED',
                    '1302 (0x516)',
                    'NI-RFSG does not return an error or a warning when an OSP overflow occurs.'
                ],
                [
                    'NIRFSG_VAL_ERROR_REPORTING_WARNING',
                    '1301 (0x515)',
                    'NI-RFSG returns a warning when an OSP overflow occurs.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'OverflowErrorReporting',
        'lv_property': 'Arb:Advanced:Overflow Error Reporting',
        'name': 'OVERFLOW_ERROR_REPORTING',
        'type': 'ViInt32'
    },
    1150239: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the size of the DMA buffer in computer memory, in bytes. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                A sufficiently large host DMA buffer improves performance by allowing large writes to be transferred more efficiently.\n\n                **Units:** bytes\n\n                **Default Value:** 8MB\n\n                **Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n                '
        },
        'lv_property': 'Arb:Data Transfer:Advanced:Host DMA Buffer Size',
        'name': 'HOST_DMA_BUFFER_SIZE',
        'type': 'ViInt64'
    },
    1150241: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the port to configure.\n\n                **Valid Values**:\n\n                PXIe-5644/5645/5646, PXIe-5820/5840/5841: "" (empty string)\n\n                PXIe-5830: if0, if1\n\n                PXIe-5831/5832: if0, if1, rf*0-1*/port*x*, where *0-1* indicates one (*0*) or two (*1*) mmRH-5582 connections and *x* is the port number on the mmRH-5582 front panel.\n\n                **Default Value:**\n\n                PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842/5860: "" (empty string)\n\n                PXIe-5830/5831/5832: if0\n\n                **Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                NIRFSG_ATTR_AVAILABLE_PORTS\n            ',
            'note': 'When using RF list mode, ports cannot be shared with NI-RFSA.'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Signal Path:Selected Ports',
        'name': 'SELECTED_PORTS',
        'type': 'ViString'
    },
    1150242: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies whether to allow NI-RFSA to control the NI-RFSG LO out export.\n\n                Set this attribute to NIRFSG_VAL_ENABLE to allow NI-RFSA to control the LO out export. Use the RF OUT LO EXPORT ENABLED attribute to control the LO out export from NI-RFSA.\n\n                **Default Value:** NIRFSG_VAL_DISABLE\n\n                **Supported Devices**: PXIe-5840/5841/5842\n            \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_ENABLE',
                    '0 (0x0)',
                    'Do not allow NI-RFSA to control the NI-RFSG local oscillator export.'
                ],
                [
                    'NIRFSG_VAL_DISABLE',
                    '1 (0x1)',
                    'Allow NI-RFSA to control the NI-RFSG local oscillator export.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'LoOutExportConfigureFromRFSaEnable',
        'lv_property': 'RF:LO Out Export Configure From RFSA',
        'name': 'LO_OUT_EXPORT_CONFIGURE_FROM_RFSA',
        'type': 'ViInt32'
    },
    1150243: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies whether to enable the RF IN LO OUT terminal on the PXIe-5840/5841.\n\n                Set this attribute to NIRFSG_VAL_ENABLE to export the LO signal from the RF IN LO OUT terminal.\n\n                When this attribute is enabled, if the NIRFSG_ATTR_LO_SOURCE attribute is set to NIRFSG_VAL_LO_SOURCE_LO_IN_STR and you do not set the NIRFSG_ATTR_LO_FREQUENCY or NIRFSG_ATTR_UPCONVERTER_CENTER_FREQUENCY attributes, NI-RFSG rounds the LO frequency to approximately an LO step size as if the source was NIRFSG_VAL_ONBOARD_CLOCK_STR. This ensures that when you configure NI-RFSA and NI-RFSG with compatible settings that result in the same LO frequency, the rounding also is compatible.\n\n                **Default Value:** NIRFSG_VAL_UNSPECIFIED\n\n                **Supported Devices**: PXIe-5840/5841/5842\n            \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_DISABLE',
                    'The RF In local oscillator signal is not present at the front panel LO OUT connector.'
                ],
                [
                    'NIRFSG_VAL_ENABLE',
                    'The RF In local oscillator signal is present at the front panel LO OUT connector.'
                ],
                [
                    'NIRFSG_VAL_UNSPECIFIED',
                    'The RF IN local oscillator signal may or may not be present at the front panel LO OUT connector, because NI-RFSA may be controlling it.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'enum': 'RFInLoExportEnabled',
        'lv_property': 'RF:RF In LO Export Enabled',
        'name': 'RF_IN_LO_EXPORT_ENABLED',
        'type': 'ViInt32'
    },
    1150244: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the temperature change, in degrees Celsius, that is required before NI-RFSG recalculates the thermal correction settings when entering the Generation state.\n\n                **Units:** degrees Celsius (°C)\n\n                **Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Default Values:**\n\n                PXIe-5830/5831/5832/5842/5860: 0.2\n\n                PXIe-5840/5841: 1.0\n                '
        },
        'lv_property': 'RF:Advanced:Thermal Correction Temperature Resolution (Degrees C)',
        'name': 'THERMAL_CORRECTION_TEMPERATURE_RESOLUTION',
        'type': 'ViReal64'
    },
    1150248: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies whether to allow NI-RFSG to select the upconverter frequency offset. You can either set an offset yourself or let NI-RFSG select one for you.\n\n                Placing the upconverter center frequency outside the bandwidth of your waveform can help avoid issues such as LO leakage.\n\n                To set an offset yourself, set this attribute to NIRFSG_VAL_AUTO or NIRFSG_VAL_USER_DEFINED, and set either the NIRFSG_ATTR_UPCONVERTER_CENTER_FREQUENCY or the NIRFSG_ATTR_UPCONVERTER_FREQUENCY_OFFSET attribute.\n\n                To allow NI-RFSG to automatically select the upconverter frequency offset, set this attribute to NIRFSG_VAL_AUTO or NIRFSG_VAL_ENABLE and set the NIRFSG_ATTR_SIGNAL_BANDWIDTH to describe the bandwidth of your waveform. The signal bandwidth must be no greater than half the value of the NIRFSG_ATTR_DEVICE_INSTANTANEOUS_BANDWIDTH attribute, minus a device-specific guard band. Do not set the NIRFSG_ATTR_UPCONVERTER_CENTER_FREQUENCY or NIRFSG_ATTR_UPCONVERTER_FREQUENCY_OFFSET attributes. If all conditions are met, NI-RFSG places the upconverter center frequency outside the signal bandwidth. Set this attribute to NIRFSG_VAL_ENABLE if you want to receive an error any time NI-RFSG is unable to apply automatic offset.\n\n                When you set an offset yourself or do not use an offset, the reference frequency for gain is near the upconverter center frequency, and NIRFSG_ATTR_UPCONVERTER_FREQUENCY_OFFSET_MODE returns NIRFSG_VAL_USER_DEFINED. When NI-RFSG automatically sets an offset, the reference frequency for gain is near the NIRFSG_ATTR_FREQUENCY and NIRFSG_ATTR_UPCONVERTER_FREQUENCY_OFFSET_MODE returns NIRFSG_VAL_ENABLE.\n\n                **Default Value:** NIRFSG_VAL_AUTO\n\n                **Supported Devices**: PXIe-5830/5831/5832/5841/5842\n\n                **Related Topics**\n\n                `PXIe-5830 Automatic Frequency Offset <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/automatic_frequency_offset.html>`_\n\n                `PXIe-5831/5832 Automatic Frequency Offset <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/automatic_frequency_offset.html>`_\n\n                `PXIe-5841 Automatic Frequency Offset <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/automatic_frequency_offset.html>`_\n            \n            **Defined Values**:\n            ',
            'note': 'Below 120 MHz, the PXIe-5841 does not use an LO and NIRFSG_VAL_ENABLE is unavailable. Refer to the *PXIe-5841 Automatic Frequency Offset* topic for more information about using an automatic offset with an external LO.',
            'table_body': [
                [
                    'NIRFSG_VAL_ENABLE',
                    'NI-RFSG places the upconverter center frequency outside of the signal bandwidth if the NIRFSG_ATTR_SIGNAL_BANDWIDTH attribute has been set and can be avoided. NI-RFSG returns an error if the NIRFSG_ATTR_SIGNAL_BANDWIDTH attribute has not been set, or if the signal bandwidth is too large.'
                ],
                [
                    'NIRFSG_VAL_AUTO',
                    'NI-RFSG places the upconverter center frequency outside of the signal bandwidth if the NIRFSG_ATTR_SIGNAL_BANDWIDTH attribute has been set and can be avoided.'
                ],
                [
                    'NIRFSG_VAL_USER_DEFINED',
                    'NI-RFSG uses the offset that you specified with the NIRFSG_ATTR_UPCONVERTER_FREQUENCY_OFFSET or NIRFSG_ATTR_UPCONVERTER_CENTER_FREQUENCY attributes.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'enum': 'UpconverterFrequencyOffsetMode',
        'lv_property': 'RF:Upconverter:Frequency Offset Mode',
        'name': 'UPCONVERTER_FREQUENCY_OFFSET_MODE',
        'type': 'ViInt32'
    },
    1150249: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns a comma-separated list of the ports available for use based on your instrument configuration.\n\n                **Supported Devices**: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n                '
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Signal Path:Available Ports',
        'name': 'AVAILABLE_PORTS',
        'type': 'ViString'
    },
    1150251: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns a string that contains the name of the FPGA target being used. This name can be used with the RIO open session to open a reference to the FPGA.\n\n                This attribute is channel dependent if multiple FPGA targets are supported.\n\n                **Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n                '
        },
        'lv_property': 'Device Characteristics:FPGA Target Name',
        'name': 'FPGA_TARGET_NAME',
        'type': 'ViString'
    },
    1150252: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the type of de-embedding to apply to measurements on the specified port.\n\n                To use this attribute, you must use the channelName parameter of the nirfsg_SetAttributeViInt32 function to specify the name of the port to configure for de-embedding.\n\n                If you set this attribute to NIRFSG_VAL_DEEMBEDDING_TYPE_SCALAR or NIRFSG_VAL_DEEMBEDDING_TYPE_VECTOR, NI-RFSG adjusts the instrument settings and the returned data to remove the effects of the external network between the instrument and the DUT.\n\n                **Default Value**: NIRFSG_VAL_DEEMBEDDING_TYPE_SCALAR\n\n                **Valid Values for PXIe-5830/5832/5840/5841/5842/5860** : NIRFSG_VAL_DEEMBEDDING_TYPE_SCALAR or NIRFSG_VAL_DEEMBEDDING_TYPE_NONE\n\n                **Valid Values for PXIe-5831** NIRFSG_VAL_DEEMBEDDING_TYPE_SCALAR, NIRFSG_VAL_DEEMBEDDING_TYPE_VECTOR, or NIRFSG_VAL_DEEMBEDDING_TYPE_NONE. NIRFSG_VAL_DEEMBEDDING_TYPE_VECTOR is only supported for TRX Ports in a Semiconductor Test System (STS).\n\n                **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860\n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_DEEMBEDDING_TYPE_NONE',
                    '25000 (0x61a8)',
                    'De-embedding is not applied to the measurement.'
                ],
                [
                    'NIRFSG_VAL_DEEMBEDDING_TYPE_SCALAR',
                    '25001 (0x61a9)',
                    'De-embeds the measurement using only the gain term.'
                ],
                [
                    'NIRFSG_VAL_DEEMBEDDING_TYPE_VECTOR',
                    '25002 (0x61aa)',
                    'De-embeds the measurement using the gain term and the reflection term.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'DeembeddingTypeAttrVals',
        'lv_property': 'De-embedding:Type',
        'name': 'DEEMBEDDING_TYPE',
        'supported_rep_caps': [
            'deembedding_port'
        ],
        'type': 'ViInt32'
    },
    1150253: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Selects the de-embedding table to apply to the measurements on the specified port.\n\n                To use this attribute, you must use the channelName parameter of the nirfsg_SetAttributeViString function to specify the name of the port to configure for de-embedding.\n\n                If de-embedding is enabled, NI-RFSG uses the specified table to remove the effects of the external network between the instrument and the DUT.\n\n                Use the create deembedding sparameter table array function to create tables.\n\n                **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860\n                '
        },
        'lv_property': 'De-embedding:Selected Table',
        'name': 'DEEMBEDDING_SELECTED_TABLE',
        'supported_rep_caps': [
            'deembedding_port'
        ],
        'type': 'ViString'
    },
    1150257: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the step size for tuning the internal voltage-controlled oscillator (VCO) used to generate the LO signal.\n\n                **Valid Values**:\n\n                LO1: 1 Hz to 50 MHz\n\n                LO2: 1 Hz to 100 MHz\n\n                **Default Value**: 1 MHz\n\n                **Supported Devices**: PXIe-5830/5831/5832\n                '
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Signal Path:LO VCO Frequency Step Size (Hz)',
        'name': 'LO_VCO_FREQUENCY_STEP_SIZE',
        'type': 'ViReal64'
    },
    1150258: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the expected thermal operating range of the instrument from the self-calibration temperature, in degrees Celsius, returned from the NIRFSG_ATTR_DEVICE_TEMPERATURE attribute.\n\n                For example, if this property is set to 5.0, and the device is self-calibrated at 35°C, then you can expect to run the device from 30°C to 40°C with corrected accuracy and no overflows. Setting this property with a smaller value can result in improved dynamic range, but you must ensure thermal stability while the instrument is running. Operating the instrument outside of the specified range may cause degraded performance or DSP overflows.\n\n                **Units:** degrees Celsius (°C)\n\n                **Default Value**:\n\n                **PXIe-5830/5831/5832/5842/5860**: 5\n\n                **PXIe-5840/5841**: 10\n\n                **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860\n                '
        },
        'lv_property': 'RF:Advanced:Thermal Correction Headroom Range (Degrees C)',
        'name': 'THERMAL_CORRECTION_HEADROOM_RANGE',
        'type': 'ViReal64'
    },
    1150263: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the I/Q rate of the waveform. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Streaming <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/streaming.html>`_\n\n                `Assigning Properties or Attributes to a Waveform <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/assigning_properties_or_attributes_to_a_waveform.html>`_—Refer to this topic for more information about using this attribute to associate an I/Q rate with a waveform.\n\n                `Digital Upconverter <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/duc.html>`_\n                '
        },
        'lv_property': 'Arb:Waveform Attributes:Waveform IQ Rate (S/s)',
        'name': 'WAVEFORM_IQ_RATE',
        'supported_rep_caps': [
            'waveform'
        ],
        'type': 'ViReal64'
    },
    1150264: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the bandwidth of the arbitrary signal. This value must be less than or equal to (0.8× NIRFSG_ATTR_IQ_RATE).\n\n                **Units**: hertz (Hz)\n\n                **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n                '
        },
        'lv_property': 'Arb:Waveform Attributes:Waveform Signal Bandwidth (Hz)',
        'name': 'WAVEFORM_SIGNAL_BANDWIDTH',
        'supported_rep_caps': [
            'waveform'
        ],
        'type': 'ViReal64'
    },
    1150265: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the waveform runtime scaling. The waveform runtime scaling is applied to the waveform data before any other signal processing.\n\n                **Units**: dB\n\n                **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860, PXIe-5841 with PXIe-5655\n                '
        },
        'lv_property': 'Arb:Waveform Attributes:Waveform Runtime Scaling',
        'name': 'WAVEFORM_RUNTIME_SCALING',
        'supported_rep_caps': [
            'waveform'
        ],
        'type': 'ViReal64'
    },
    1150266: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the peak-to-average power ratio (PAPR).\n\n                **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n                '
        },
        'lv_property': 'Arb:Waveform Attributes:Waveform PAPR (dB)',
        'name': 'WAVEFORM_PAPR',
        'supported_rep_caps': [
            'waveform'
        ],
        'type': 'ViReal64'
    },
    1150271: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies a comma-separated list of ports for which to fix the group delay.\n                \n\n                **Supported Devices:** PXIe-5831/5832\n                '
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Signal Path:Fixed Group Delay Across Ports',
        'name': 'FIXED_GROUP_DELAY_ACROSS_PORTS',
        'type': 'ViString'
    },
    1150273: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Enables the detection of burst start and burst stop locations in the waveform. You can read the detected burst start and burst stop locations using nirfsg_GetWaveformBurstStartLocations and nirfsg_GetWaveformBurstStopLocations functions respectively.\n\n                **Default Value:** NIRFSG_VAL_DISABLE\n\n                **Supported Devices:**PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n            \n            **Defined Values**:\n            ',
            'note': '- When you download a waveform using nirfsg_ReadAndDownloadWaveformFromFileTdms function and if NIRFSG_ATTR_WAVEFORM_RF_BLANKING attribute is enabled, you must set the NIRFSG_ATTR_WRITE_WAVEFORM_BURST_DETECTION attribute to NIRFSG_VAL_DISABLE.\n\n - For PXIe-5830/5831/5832: The RF Blanking reserves a PXI trigger line. If you are calling any nirfsg_Reset or `niRFSA_reset <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/cvinirfsa_reset.html>`_ on the same device, NI recommends calling it before committing blanking attributes. Alternatively, you can call nirfsg_ResetWithOptions or `niRFSA_ResetWithOptions <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/cvinirfsa_resetwithoptions.html>`_. Select **Routes** in the **steps to omit** parameter.',
            'table_body': [
                [
                    'NIRFSG_VAL_ENABLE',
                    'Burst detection is enabled.'
                ],
                [
                    'NIRFSG_VAL_DISABLE',
                    'Burst detection is disabled.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'enum': 'WriteWaveformBurstDetection',
        'lv_property': 'Arb:Write Waveform Burst Detection:Enabled',
        'name': 'WRITE_WAVEFORM_BURST_DETECTION',
        'type': 'ViInt32'
    },
    1150274: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the algorithm that NI-RFSG uses to detect the burst start and burst stop locations in the waveform when burst detection is enabled using the NIRFSG_ATTR_WRITE_WAVEFORM_BURST_DETECTION attribute. When you set NIRFSG_ATTR_WRITE_WAVEFORM_BURST_DETECTION_MODE to NIRFSG_VAL_AUTO, NI-RFSG automatically detects the burst start and burst stop locations by analyzing the waveform. To fine-tune the burst detection process parameters yourself, you can set this attribute to NIRFSG_VAL_MANUAL and specify the burst detection parameters using the write waveform burst detection minimum quiet time, NIRFSG_ATTR_WRITE_WAVEFORM_BURST_DETECTION_POWER_THRESHOLD, write waveform burst detection minimum burst time attributes.\n\n                **Default Value:** NIRFSG_VAL_AUTO\n\n                **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n            \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_AUTO',
                    'NI-RFSG automatically detects the burst start and burst stop locations by analyzing the waveform.'
                ],
                [
                    'NIRFSG_VAL_MANUAL',
                    'User sets the burst detection parameters.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'enum': 'WriteWaveformBurstDetectionMode',
        'lv_property': 'Arb:Write Waveform Burst Detection:Mode',
        'name': 'WRITE_WAVEFORM_BURST_DETECTION_MODE',
        'type': 'ViInt32'
    },
    1150276: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the relative power level at which burst start or stop locations are detected. The threshold is relative to the peak power in the waveform. NI-RFSG detects burst start (or burst stop) locations when the signal exceeds (or falls below) the level specified by this attribute. This attribute is ignored when you disable the NIRFSG_ATTR_WRITE_WAVEFORM_BURST_DETECTION attribute or when you set the NIRFSG_ATTR_WRITE_WAVEFORM_BURST_DETECTION_MODE attribute to NIRFSG_VAL_AUTO.\n\n                **Units:** dB\n\n                **Default Value:** 0\n\n                **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n                '
        },
        'lv_property': 'Arb:Write Waveform Burst Detection:Power Threshold',
        'name': 'WRITE_WAVEFORM_BURST_DETECTION_POWER_THRESHOLD',
        'type': 'ViReal64'
    },
    1150278: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '\n                **Defined Values**:\n\nName (Value): Description\n\nNIRFSG_VAL_DISABLE (0):\tRF blanking is disabled.\n\nNIRFSG_VAL_ENABLE (1):\tRF blanking is enabled.\n\n                **Default Value:** NIRFSG_VAL_DISABLE\n\n                **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842\n\n                **Related Topics**\n\n                `Marker Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/marker_events.html>`_\n            \n            Enables or disables RF blanking.\n            ',
            'note': 'For PXIe-5830/5831/5832: The RF Blanking reserves a PXI trigger line. If you are calling any nirfsg_Reset or `niRFSA_reset <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/cvinirfsa_reset.html>`_ on the same device, NI recommends calling it before committing blanking attributes. Alternatively, you can call nirfsg_ResetWithOptions or `niRFSA_ResetWithOptions <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/cvinirfsa_resetwithoptions.html>`_. Select **Routes** in the **steps to omit** parameter.',
            'table_body': [
                [
                    '"" (empty string)',
                    'NIRFSG_VAL_DISABLE',
                    'No blanking performed.'
                ],
                [
                    '"" (empty string)',
                    'NIRFSG_VAL_ENABLE',
                    'Blanking performed based on burst start and stop values and blanking source set to private marker.'
                ],
                [
                    'NIRFSG_VAL_MARKER0, NIRFSG_VAL_MARKER1, NIRFSG_VAL_MARKER2, or NIRFSG_VAL_MARKER3',
                    'NIRFSG_VAL_DISABLE',
                    'Blanking performed based on the marker locations for the marker that the user set in the blanking source.'
                ],
                [
                    'NIRFSG_VAL_MARKER0, NIRFSG_VAL_MARKER1, NIRFSG_VAL_MARKER2, or NIRFSG_VAL_MARKER3',
                    'NIRFSG_VAL_ENABLE',
                    'Error is shown.'
                ]
            ],
            'table_header': [
                'NIRFSG_ATTR_RF_BLANKING_SOURCE',
                'NIRFSG_ATTR_WAVEFORM_RF_BLANKING',
                'Behaviour'
            ]
        },
        'enum': 'RFBlanking',
        'lv_property': 'Arb:Waveform Attributes:Waveform RF Blanking',
        'name': 'WAVEFORM_RF_BLANKING',
        'supported_rep_caps': [
            'waveform'
        ],
        'type': 'ViInt32'
    },
    1150289: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns the de-embedding gain applied to compensate for the mismatch on the specified port. If de-embedding is enabled, NI-RFSG uses the returned compensation gain to remove the effects of the external network between the instrument and the DUT.\n\n                **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860\n                '
        },
        'lv_property': 'De-embedding:Compensation Gain',
        'name': 'DEEMBEDDING_COMPENSATION_GAIN',
        'supported_rep_caps': [
            'deembedding_port'
        ],
        'type': 'ViReal64'
    },
    1150290: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the configurations to skip while loading from a file.\n\n                **Default Value:**  NIRFSG_VAL_SKIP_NONE\n                \n                **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n            \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_SKIP_NONE',
                    'NI-RFSG loads all the configurations to the session.'
                ],
                [
                    'NIRFSG_VAL_SKIP_WAVEFORM',
                    'NI-RFSG skips loading the waveform configurations to the session.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'enum': 'LoadOptions',
        'lv_property': 'Load Configurations:Load Options',
        'name': 'LOAD_CONFIGURATIONS_FROM_FILE_LOAD_OPTIONS',
        'type': 'ViInt32'
    },
    1150291: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the configurations to skip to reset while loading configurations from a file.\n\n                **Default Value:**  NIRFSG_VAL_SKIP_NONE\n                **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n            \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_SKIP_NONE',
                    'NI-RFSG resets all configurations.'
                ],
                [
                    'NIRFSG_VAL_SKIP_WAVEFORMS',
                    'NI-RFSG skips resetting the waveform configurations.'
                ],
                [
                    'NIRFSG_VAL_SKIP_SCRIPTS',
                    'NI-RFSG skips resetting the scripts.'
                ],
                [
                    'NIRFSG_VAL_SKIP_DEEMBEDDING_TABLES',
                    'NI-RFSG skips resetting the de-embedding tables.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'enum': 'ResetOptions',
        'lv_property': 'Load Configurations:Reset Options',
        'name': 'LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS',
        'type': 'ViInt32'
    },
    1150292: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the Reference Clock Rate, in Hz, of the signal sent to the Reference Clock Export Output Terminal. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                **Default Value:** NIRFSG_VAL_10MHZ\n\n                **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n            \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_10MHZ',
                    '10000000 (0x989680)',
                    'Uses a 10MHz Reference Clock rate.'
                ],
                [
                    'NIRFSG_VAL_100MHZ',
                    '',
                    'Uses a 100MHz Reference Clock rate.'
                ],
                [
                    'NIRFSG_VAL_1GHZ',
                    '',
                    'Uses a 1GHz Reference Clock rate.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'ReferenceClockExportedRate',
        'lv_property': 'Clock:Reference Clock Exported Rate (Hz)',
        'name': 'EXPORTED_REF_CLOCK_RATE',
        'type': 'ViReal64'
    },
    1150293: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies whether to perform the normalization on a waveform.\n\n                **Default Value:** NIRFSG_VAL_DISABLE\n\n                **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n            \n            **Defined Values**:\n            ',
            'note': 'You can not set NIRFSG_ATTR_WRITE_WAVEFORM_NORMALIZATION and NIRFSG_ATTR_POWER_LEVEL_TYPE attributes at the same time.',
            'table_body': [
                [
                    'NIRFSG_VAL_ENABLE',
                    'Enables normalization on a waveform to transform the waveform data so that its maximum is 1.00 and its minimum is -1.00'
                ],
                [
                    'NIRFSG_VAL_DISABLE',
                    'Disables normalization on the waveform.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'enum': 'WriteWaveformNormalization',
        'lv_property': 'Arb:Write Waveform Normalization',
        'name': 'WRITE_WAVEFORM_NORMALIZATION',
        'type': 'ViInt32'
    },
    1150297: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the size of the waveform specified by an active channel.\n\n                **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5841 with PXIe-5655/5842/5860\n                '
        },
        'lv_property': 'Arb:Waveform Attributes:Waveform Size',
        'name': 'WAVEFORM_WAVEFORM_SIZE',
        'supported_rep_caps': [
            'waveform'
        ],
        'type': 'ViInt32'
    },
    1150307: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the active level of the pulse modulation signal when pulse modulation is enabled. To set this property, the NI-RFSG device must be in the Configuration state.\n\n                **Default Value:** NIRFSG_VAL_ACTIVE_HIGH\n\n                **Supported Devices:**  PXIe-5842\n            \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_ACTIVE_HIGH',
                    '9000 (0x2328)',
                    'Trigger when the digital trigger signal is high.'
                ],
                [
                    'NIRFSG_VAL_ACTIVE_LOW',
                    '9001 (0x2329)',
                    'Trigger when the digital trigger signal is low.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'ScriptTrigDigLevelActiveLevel',
        'lv_property': 'RF:Advanced:Pulse Modulation Active Level',
        'name': 'PULSE_MODULATION_ACTIVE_LEVEL',
        'type': 'ViInt32'
    },
    1150308: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the source of the pulse modulation signal. When Pulse In in used, the pulse modulation is applied with the lowest latency and jitter, but is not aligned to any particular waveform sample. When a marker is used, the RF pulse is aligned to a specific sample in the arbitrary waveform. To set this property, the NI-RFSG device must be in the Configuration state.\n\n                **Default Value:** NIRFSG_VAL_PULSE_IN_STR\n\n                **Supported Devices:**  PXIe-5842\n            \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_PULSE_IN_STR',
                    'PulseIn',
                    'The trigger is received on the PULSE IN terminal. This value is valid on only the PXIe-5842.'
                ],
                [
                    'NIRFSG_VAL_MARKER0_STR',
                    '',
                    'The trigger is received from the Marker 0.'
                ],
                [
                    'NIRFSG_VAL_MARKER1_STR',
                    '',
                    'The trigger is received from the Marker 1.'
                ],
                [
                    'NIRFSG_VAL_MARKER2_STR',
                    '',
                    'The trigger is received from the Marker 2.'
                ],
                [
                    'NIRFSG_VAL_MARKER3_STR',
                    '',
                    'The trigger is received from the Marker 3.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'PulseModulationSource',
        'lv_property': 'Modulation:Pulse:Pulse Modulation Source',
        'name': 'PULSE_MODULATION_SOURCE',
        'type': 'ViString'
    },
    1150309: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the destination terminal for exporting the Pulse Modulation Event. The Pulse Modulation Event tracks the RF Envelope when Pulse Modulation is Enabled. If this property is set to a value other than `do not export str`, calling NI-RFSG Commit will cause the output terminal to be pulled to the logic level that is the inverse of `exported pulse modulation event active level`. You can tri-state this terminal by setting this property to `do not export str` or by calling `niRFSG Reset`. To set this property, the NI-RFSG device must be in the Configuration state.\n\n                **Default Value:** NIRFSG_VAL_PULSE_OUT_STR\n\n                **Supported Devices:**  PXIe-5842\n            \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_DO_NOT_EXPORT_STR',
                    '',
                    'yet to be defined'
                ],
                [
                    'NIRFSG_VAL_PULSE_OUT_STR',
                    'PulseOut',
                    'yet to be defined'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'PulseModulationOutputTerm',
        'lv_property': 'Events:Pulse Modulation:Exported Pulse Modulation Event Output Terminal',
        'name': 'EXPORTED_PULSE_MODULATION_EVENT_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150310: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the active level of the exported Pulse Modulation Event. When `attribute pulse modulation enabled` is Enabled, `pulse modulation active level` is `active high`, `exported pulse modulation event output terminal` is `PulseOut`, and this property is `active high`, then the Pulse Modulation Event will transition from Low to High after the the Pulse In signal is set to logic high, and the RF Output has settled. To set this property, the NI-RFSG device must be in the Configuration state.\n\n                **Default Value:** NIRFSG_VAL_ACTIVE_HIGH\n\n                **Supported Devices:**  PXIe-5842\n            \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_ACTIVE_HIGH',
                    '9000 (0x2328)',
                    'Trigger when the digital trigger signal is high.'
                ],
                [
                    'NIRFSG_VAL_ACTIVE_LOW',
                    '9001 (0x2329)',
                    'Trigger when the digital trigger signal is low.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'ScriptTrigDigLevelActiveLevel',
        'lv_property': 'Events:Pulse Modulation:Exported Pulse Modulation Event Active Level',
        'name': 'EXPORTED_PULSE_MODULATION_EVENT_ACTIVE_LEVEL',
        'type': 'ViInt32'
    },
    1150311: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies which path to configure to generate a signal.\n                \n                '
        },
        'lv_property': 'Signal Path:Advanced:Selected Path',
        'name': 'SELECTED_PATH',
        'type': 'ViString'
    },
    1150312: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns a comma separated list of the configurable paths available for use based on your instrument configuration.\n                \n                '
        },
        'lv_property': 'Signal Path:Advanced:Available Paths',
        'name': 'AVAILABLE_PATHS',
        'type': 'ViString'
    },
    1152832: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Enables or disables compensation for filter group delay on the AWG module. This attribute also accounts for the upconverter group delay and aligns the RF output with the Started Event, Done Event, and Marker Events.\n\n                At a low I/Q rate, the group delay can become so large that some devices may not be able to align the events with the RF output, in which case you must increase the I/Q rate or disable this attribute.\n\n                **Default Value:** VI_FALSE\n\n                **Supported Devices:** PXIe-5672\n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'VI_TRUE',
                    'Enables compensation for filter group delay.'
                ],
                [
                    'VI_FALSE',
                    'Disables compensation for filter group delay.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'lv_property': 'Arb:Advanced:Compensate for Filter Group Delay',
        'name': 'COMPENSATE_FOR_FILTER_GROUP_DELAY',
        'type': 'ViBoolean'
    },
    1154097: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the gain the upconverter applies to the signal.\n\n                **Units**: dB\n\n                **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n            ',
            'note': 'This attribute is read/write on the PXI-5610 and PXIe-5611 and is read-only on the PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, and PXIe-5820/5830/5831/5832/5840/5841/5842/5860.'
        },
        'lv_property': 'RF:Upconverter:Gain (dB)',
        'name': 'UPCONVERTER_GAIN',
        'type': 'ViReal64'
    },
    1154098: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Indicates the center frequency of the passband containing the upconverted RF signal. Writing a value to this attribute while using the PXIe-5644/5645/5646, PXIe-5672/5673/5673E, or PXIe-5820/5840/5841 device enables in-band retuning. In-band retuning increases the speed of frequency sweeps by reducing the amount of upconverter retunes.\n\n                **Units**: hertz (Hz)\n\n                **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842\n            ',
            'note': '- This attribute is read/write on the PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXIe-5672/5673/5673E, and PXIe-5820/5830/5831/5832/5840/5841/5842, and is read-only on the PXI-5670/5671.\n\n - Resetting this attribute disables in-band retuning, however, for the PXIe-5820, in-band retuning is always enabled.\n\n - For the PXIe-5820, the only valid value for this attribute is 0.\n\n - Setting this attribute while the PXIe-5644/5645/5646, PXIe-5673/5673E, or PXIe-5820/5830/5831/5832/5840/5841/5842 device is generating has no effect until a dynamic attribute is set.'
        },
        'lv_property': 'RF:Upconverter:Center Frequency (Hz)',
        'name': 'UPCONVERTER_CENTER_FREQUENCY',
        'type': 'ViReal64'
    },
    1250001: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the frequency of the generated RF signal. For arbitrary waveform generation, this attribute specifies the center frequency of the signal.\n\n                The PXI-5670/5671, PXIe-5672, PXIe-5820, and PXIe-5860 must be in the Configuration state to use this attribute. However, the PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXIe-5673/5673E, and PXIe-5830/5831/5832/5840/5841/5842 can be in the Configuration or the Generation state to use this attribute.\n\n                **Units**: hertz (Hz)\n\n                **Defined Values**:\n                Refer to the specifications document for your device allowable frequency settings.\n\n                **Default Value:**\n\n                PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E: 100MHz\n\n                PXIe-5653: 4GHz\n\n                PXIe-5820: 0Hz\n\n                PXIe-5830/5831/5832: 6.5 GHz\n\n                PXIe-5840/5841/5860, PXI-5842 (500 MHz, 1 GHz, and 2 GHz bandwidth options): 1GHz\n\n                PXIe-5842 (4 GHz bandwidth option) using the Standard personality: 1GHz\n\n                PXIe-5842 (4 GHz bandwidth option) using the 4 GHz Bandwidth personality: 6.5GHz\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `NI-RFSG Instrument Driver Programming Flow <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/progflow.html>`_\n                \n                **High-Level Functions**:\n\n                - nirfsg_ConfigureRf\n            ',
            'note': 'For the PXIe-5645, this attribute is ignored if you are using the I/Q ports.'
        },
        'lv_property': 'RF:Frequency (Hz)',
        'name': 'FREQUENCY',
        'type': 'ViReal64'
    },
    1250002: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies either the average power level or peak power level of the generated RF signal, depending on the NIRFSG_ATTR_POWER_LEVEL_TYPE attribute setting.\n\n                The PXI-5670/5671, PXIe-5672, and PXIe-5860 must be in the Configuration state to use this attribute. However, the PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5654/5654 with PXIe-5696, PXIe-5673/5673E and PXIe-5830/5831/5832/5840/5841/5842 can be in the Configuration or the Generation state to use this attribute.\n\n                Refer to the specifications document for your device for allowable power level settings.\n\n                **Units**: dBm\n\n                **Default Values:**\n\n                PXIe-5644/5645/5646, PXIe-5673/5673E: -100\n\n                PXI/PXIe-5650/5651/5652: -90\n\n                PXIe-5654: -7\n\n                PXIe-5654 with PXIe-5696: -110\n\n                PXI-5670/5671, PXIe-5672: -145\n\n                PXIe-5830/5831/5832/5840/5841/5842/5860: -174\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5830/5831/5832/5840/5841/5842/5860\n                **High-Level Functions**:\n\n                - nirfsg_ConfigureRf\n            ',
            'note': '- For the PXIe-5653, this attribute is read-only.\n\n - For the PXIe-5645, this attribute is ignored if you are using the I/Q ports.'
        },
        'lv_property': 'RF:Power Level (dBm)',
        'name': 'POWER_LEVEL',
        'type': 'ViReal64'
    },
    1250004: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies whether signal output is enabled. Setting the NIRFSG_ATTR_OUTPUT_ENABLED attribute to VI_FALSE while in the Generation state stops signal output, although generation continues internally. For the PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653, PXI-5670/5671, and PXIe-5672/5673/5673E, setting the NIRFSG_ATTR_OUTPUT_ENABLED attribute while in the Committed state does not transition the device to the Configuration state, but output changes immediately.\n\n                **Default Value:** VI_TRUE\n\n                **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Output Enabled <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/outputenable.html>`_\n\n                `NI-RFSG Instrument Driver Programming Flow <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/progflow.html>`_\n                \n                **High-Level Functions**:\n\n                - nirfsg_ConfigureOutputEnabled\n            \n            **Defined Values**:\n            ',
            'note': '- For the PXIe-5653, this attribute controls only the LO1 terminal.\n\n - For the PXIe-5645, this attribute is ignored if you are using the I/Q ports.\n\n - When the NIRFSG_ATTR_ACTIVE_CONFIGURATION_LIST attribute is set to a valid list name, setting the NIRFSG_ATTR_OUTPUT_ENABLED attribute transitions the device to the Configuration state.',
            'table_body': [
                [
                    'VI_TRUE',
                    'Enables signal output.'
                ],
                [
                    'VI_FALSE',
                    'Disables signal output.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'lv_property': 'RF:Output Enabled',
        'name': 'OUTPUT_ENABLED',
        'type': 'ViBoolean'
    },
    1250051: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Enables or disables pulse modulation.\n\n                PXIe-5654/5654 with PXIe-5696: If this attribute is enabled and the signal at the PULSEIN front panel connector is high, the device generates a signal. If the signal is low, output generation is disabled.\n\n                PXIe-5673/5673E: If this attribute is enabled and the signal at the PLSMOD front panel connector is high, the device generates a signal. If the signal is low, output generation is disabled.\n\n                PXIe-5842: If this attribute is enabled and the signal at the PULSE IN front panel connector is high, the device generates a signal. If the signal is low, output generation is disabled. This behavior can be modified by setting pulse modulation active level.\n\n                **Default Value:** VI_FALSE\n\n                **Supported Devices:** PXIe-5654/5654 with PXIe-5696, PXIe-5673/5673E\n\n                **Related Topics**\n\n                `Pulse Modulation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/pulse_modulation.html>`_\n            \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'VI_TRUE',
                    'Enables pulse modulation.'
                ],
                [
                    'VI_FALSE',
                    'Disables pulse modulation.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'lv_property': 'Modulation:Pulse:Pulse Modulation Enabled',
        'name': 'PULSE_MODULATION_ENABLED',
        'type': 'ViBoolean'
    },
    1250322: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the Reference Clock rate, in Hz, of the signal present at the REF IN or CLK IN connector. This property is only valid when the NIRFSG_ATTR_REF_CLOCK_SOURCE attribute is set to NIRFSG_VAL_CLK_IN_STR, NIRFSG_VAL_REF_IN_STR, or NIRFSG_VAL_REF_IN_2_STR\n\n                To set this attribute, the NI-RFSG device must be in the Configuration state. If you are using the PXIe-5654/5654 with PXIe-5696, the NI-RFSG device must be in the Committed state to read this attribute. When you read this attribute, it returns the frequency the device is locked to during the Committed state.\n\n                If you set this attribute to NIRFSG_VAL_AUTO, NI-RFSG uses the default Reference Clock rate for the device or automatically detects the Reference Clock rate if automatic detection is supported by the device.\n\n                **Valid Values:**\n\n                PXIe-5654/5654 with PXIe-5696: Values between 1MHz to 20MHz in 1MHz steps are supported in addition to the NIRFSG_VAL_AUTO and NIRFSG_VAL_10MHZ values.\n\n                PXIe-5841 with PXIe-5655, PXIe-5842: 10 MHz, 100 MHz, 270 MHz, and 3.84 MHz \n\n                y, where\n\n                y is 4, 8, 16, 24, 25, or 32.\n\n                PXIe-5860: 10 MHz, 100 MHz\n\n                **Units**: hertz (Hz)\n\n                **Default Value:** NIRFSG_VAL_AUTO\n\n                **Supported Devices:** PXI-5610, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Timing Configurations <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/timing_configurations.html>`_\n                \n                **High-Level Functions**:\n\n                - nirfsg_ConfigureRefClock\n            \n            **Defined Values**:\n            ',
            'note': 'Automatic detection of the Reference Clock rate is supported on only the PXIe-5654/5654 with PXIe-5696. For all other supported devices, NI-RFSG uses the default Reference Clock rate of 10MHz.',
            'table_body': [
                [
                    'NIRFSG_VAL_AUTO',
                    'Uses the default Reference Clock rate for the device or automatically detects the Reference Clock rate if the device supports it.'
                ],
                [
                    'NIRFSG_VAL_10MHZ',
                    'Uses a 10 MHz Reference Clock rate.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'enum': 'ReferenceClockRate',
        'lv_property': 'Clock:Reference Clock Rate (Hz)',
        'name': 'REF_CLOCK_RATE',
        'type': 'ViReal64'
    },
    1250404: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Enables or disables the inverse phase rotation of the I/Q signal by swapping the I and Q inputs.\n\n                To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                **Default Value:** VI_FALSE\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842\n            \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'VI_TRUE',
                    'NI-RFSG device applies noninverse phase rotation of the I/Q signal.'
                ],
                [
                    'VI_FALSE',
                    'NI-RFSG device applies inverse phase rotation of the I/Q signal.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'name': 'IQ_SWAP_ENABLED',
        'type': 'ViBoolean'
    },
    1250451: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the waveform in onboard memory to generate upon calling the nirfsg_Init function when the NIRFSG_ATTR_GENERATION_MODE attribute is set to NIRFSG_VAL_ARB_WAVEFORM. The NIRFSG_ATTR_ARB_SELECTED_WAVEFORM attribute is ignored when the NIRFSG_ATTR_GENERATION_MODE attribute is set to NIRFSG_VAL_SCRIPT or NIRFSG_VAL_CW. To set the NIRFSG_ATTR_ARB_SELECTED_WAVEFORM attribute, the NI-RFSG device must be in the Configuration state.\n\n                **Default Value:** "" (empty string)\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Assigning Properties or Attributes to a Waveform <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/assigning_properties_or_attributes_to_a_waveform.html>`_\n                \n                **High-Level Functions**:\n\n                - nirfsg_SelectArbWaveform'
        },
        'lv_property': 'Arb:Waveform Capabilities:Selected Waveform',
        'name': 'ARB_SELECTED_WAVEFORM',
        'type': 'ViString'
    },
    1250452: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                This attribute specifies the I/Q rate of the arbitrary waveform. The I/Q rate is coerced to a value the hardware can achieve. Read this value back after setting it to see the actual I/Q rate. NI-RFSG internally uses an FIR filter with flat response up to (0.4 × IQ rate). Given a desired signal with the maximum frequency content *f*, sample the signal at an I/Q rate greater than or equal to ( *f*/0.4).\n\n                This attribute applies only when the NIRFSG_ATTR_GENERATION_MODE attribute is set to NIRFSG_VAL_ARB_WAVEFORM or NIRFSG_VAL_SCRIPT.\n\n                To set this attribute, the NI-RFSG device must be in the Configuration state.\n                \n                Setting this attribute to 50 MS/s on the PXI-5670/5671 and PXIe-5672 has the following implications:\n                - NI-RFSG is forced to place the carrier frequency at 18 MHz ± 1 MHz to avoid aliasing. This means that NI-RFSG cannot select a carrier frequency that could optimize waveform size if phase continuity is enabled.  \n                - Output signal bandwidth must be <5 MHz to avoid aliasing.  \n                - Close-in phase noise is higher.\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Streaming <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/streaming.html>`_\n\n                `Assigning Properties or Attributes to a Waveform <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/assigning_properties_or_attributes_to_a_waveform.html>`_—Refer to this topic for more information about using this attribute to associate an I/Q rate with a waveform.\n\n                `Digital Upconverter <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/duc.html>`_\n            **Valid Values**:\n            ',
            'note': 'Use this attribute to associate an I/Q rate with a waveform.',
            'table_body': [
                [
                    'PXIe-5644/5645',
                    'Up to 120 MS/s.'
                ],
                [
                    'PXIe-5646',
                    'Up to 250 MS/s.'
                ],
                [
                    'PXI-5670',
                    '50 MS/s*'
                ],
                [
                    '',
                    '100 MS/s*'
                ],
                [
                    'PXI-5671',
                    '50 MS/s*'
                ],
                [
                    '',
                    '100 MS/s'
                ],
                [
                    '',
                    '*(100 MS/s)/n, where n is divisible by 2 between 12 to 512, and divisible by 4 between 512 to 1,024 (n = 12, 14, 16, ..., 512, 516, 520, ..., 1,024). Setting the I/Q rate to one of these value enables the DUC.'
                ],
                [
                    'PXIe-5672 ',
                    'Up to 100 MS/s.'
                ],
                [
                    'PXIe-5673/5673E',
                    'Up to 200 MS/s. Note that -  If an PXIe-5450 with module revisions A or B is used as part of your PXIe-5673/5673E, the NI-FGEN NIFGEN_ATTR_COMPENSATE_FOR_FILTER_GROUP_DELAY attribute is disabled if the requested I/Q rate is less than 1.5 MS/s.'
                ],
                [
                    'PXIe-5820/5830/5831/5832/5840/5841/5860',
                    'Up to 1.25 GS/s.'
                ],
                [
                    'PXI-5842 (500 MHz, 1 GHz, and 2 GHz bandwidth options)',
                    'Up to 2.5 GS/s'
                ],
                [
                    ' PXIe-5842 (4 GHz bandwidth option) using the Standard personality',
                    'Up to 2.5 GS/s'
                ],
                [
                    'PXIe-5842 (4 GHz bandwidth option) using the 4 GHz Bandwidth personality',
                    '5 GS/s only.'
                ]
            ],
            'table_header': [
                'Device',
                'I/Q Rates'
            ]
        },
        'lv_property': 'Acquisition:IQ',
        'name': 'IQ_RATE',
        'type': 'ViReal64'
    },
    1250454: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns the maximum number of waveforms the device can hold in memory.\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n                \n                **High-Level Functions**:\n\n                - nirfsg_QueryArbWaveformCapabilities'
        },
        'lv_property': 'Arb:Waveform Capabilities:Max Number Waveforms',
        'name': 'ARB_MAX_NUMBER_WAVEFORMS',
        'type': 'ViInt32'
    },
    1250455: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns the waveform quantum for the device. The number of samples in a waveform must be an integer multiple of the waveform quantum. The other restrictions on the length of the waveform are the NIRFSG_ATTR_ARB_WAVEFORM_SIZE_MIN and NIRFSG_ATTR_ARB_WAVEFORM_SIZE_MAX arbitrary waveform sizes.\n\n                PXI-5671, PXIe-5672: The value of this attribute depends on the I/Q rate. Set the NIRFSG_ATTR_IQ_RATE attribute before reading this attribute.\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n                \n                **High-Level Functions**:\n\n                - nirfsg_QueryArbWaveformCapabilities'
        },
        'lv_property': 'Arb:Waveform Capabilities:Waveform Quantum',
        'name': 'ARB_WAVEFORM_QUANTUM',
        'type': 'ViInt32'
    },
    1250456: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns the smallest allowable waveform size. For the PXI-5671 and PXIe-5672, the value of this attribute depends on the I/Q rate. Set the NIRFSG_ATTR_IQ_RATE attribute before reading this attribute.\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n                \n                **High-Level Functions**:\n\n                - nirfsg_QueryArbWaveformCapabilities'
        },
        'lv_property': 'Arb:Waveform Capabilities:Min Waveform Size',
        'name': 'ARB_WAVEFORM_SIZE_MIN',
        'type': 'ViInt32'
    },
    1250457: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Returns the size of the largest waveform that is allowed.\n\n                To read this attribute, the NI-RFSG device must be in the Configuration state.\n\n                For the PXI-5671 and PXIe-5672, the value of this attribute depends on the I/Q rate. Set the NIRFSG_ATTR_IQ_RATE before reading this attribute. For the PXIe-5673/5673E, the maximum waveform size is reduced to account for the amount of device memory currently used.\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n                \n                **High-Level Functions**:\n\n                - nirfsg_QueryArbWaveformCapabilities\n            ',
            'note': 'Not all onboard memory is available for waveform storage. A portion of onboard memory stores scripts that specify how the waveforms are generated. These scripts typically require less than 1KB of onboard memory.'
        },
        'lv_property': 'Arb:Waveform Capabilities:Max Waveform Size',
        'name': 'ARB_WAVEFORM_SIZE_MAX',
        'type': 'ViInt32'
    },
    1250458: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the Start Trigger type. Depending upon the value of this attribute, more attributes may be needed to fully configure the trigger. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n                **Default Value:** NIRFSG_VAL_NONE\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_\n\n                `Trigger Types <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_types.html>`_\n\n                **High-Level Functions**:\n\n                - nirfsg_ConfigureDigitalEdgeStartTrigger\n                - nirfsg_ConfigureSoftwareStartTrigger\n                - nirfsg_DisableStartTrigger\n            \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_NONE',
                    'No trigger is configured.'
                ],
                [
                    'NIRFSG_VAL_DIGITAL_EDGE',
                    'The data operation does not start until a digital edge is detected. The source of the digital edge is specified with the NIRFSG_ATTR_DIGITAL_EDGE_START_TRIGGER_SOURCE attribute, and the active edge is specified in the NIRFSG_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE attribute.'
                ],
                [
                    'NIRFSG_VAL_SOFTWARE',
                    'The data operation does not start until a software event occurs. You may create a software trigger by calling the niRFSG_SendSoftwareEdgeTrigger function.'
                ],
                [
                    'NIRFSG_VAL_P2P_ENDPOINT_FULLNESS',
                    'The data operation does not start until the endpoint reaches the threshold specified in the NIRFSG_ATTR_P2P_ENDPOINT_FULLNESS_START_TRIGGER_LEVEL attribute.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'enum': 'StartTrigType',
        'lv_property': 'Triggers:Start:Type',
        'name': 'START_TRIGGER_TYPE',
        'type': 'ViInt32'
    },
    1250459: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '                Specifies the active edge for the Start Trigger. This attribute is used when the NIRFSG_ATTR_START_TRIGGER_TYPE attribute is set to digital edge. To set the NIRFSG_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE attribute, the NI-RFSG device must be in the Configuration state.\n\n                PXIe-5654/5654 with PXIe-5696: The Start Trigger is valid only with a timer-based list when RF list mode is enabled.\n\n                **Default Value:** NIRFSG_VAL_RISING_EDGE\n\n                **Supported Devices:** PXIe-5644/5645/5646, PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n                **Related Topics**\n\n                `Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_\n\n                `Digital Edge Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_edge.html>`_\n                \n                **High-Level Functions**:\n\n                - nirfsg_ConfigureDigitalEdgeStartTrigger\n                \n            **Defined Values**:\n            ',
            'table_body': [
                [
                    'NIRFSG_VAL_FALLING_EDGE',
                    '1 (0x1)',
                    'Occurs when the signal transitions from high level to low level.'
                ],
                [
                    'NIRFSG_VAL_RISING_EDGE',
                    '0 (0x0)',
                    'Occurs when the signal transitions from low level to high level.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'StartTrigDigEdgeEdge',
        'lv_property': 'Triggers:Start:Digital Edge',
        'name': 'DIGITAL_EDGE_START_TRIGGER_EDGE',
        'type': 'ViInt32'
    }
}
