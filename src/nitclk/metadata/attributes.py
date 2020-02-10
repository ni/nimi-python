# -*- coding: utf-8 -*-
# This file is generated from NI-TClk API metadata version 255.0.0d0
attributes = {
    1: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': "\nSpecifies the Sync Pulse source. This attribute is most often used when  synchronizing a multichassis system.\nValues\nEmpty string\nPXI Devices -  'PXI_Trig0' through  'PXI_Trig7' and device-specific settings\nPCI Devices -  'RTSI_0' through  'RTSI_7' and device-specific settings\nExamples of Device-Specific Settings\n- NI PXI-5122 supports  'PFI0' and  'PFI1'\n- NI PXI-5421 supports  'PFI0',  'PFI1',  'PFI2', and  'PFI3'\n- NI PXI-6551/6552 supports  'PFI0',  'PFI1',  'PFI2', and  'PFI3'\nDefault Value - Empty string. This default value directs  niTClk_Synchronize to set this attribute when all the synchronized devices  are in one PXI chassis. To synchronize a multichassis system, you must set  this attribute before calling niTClk_Synchronize.\n"
        },
        'lv_property': 'Sync Pulse Source',
        'name': 'SYNC_PULSE_SOURCE',
        'resettable': False,
        'type': 'ViString'
    },
    2: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': "\nSpecifies the destination of the Sync Pulse. This attribute is most often  used when synchronizing a multichassis system.\nValues\nEmpty string. Empty string is a valid value, indicating that the signal is  not exported.\nPXI Devices -  'PXI_Trig0' through  'PXI_Trig7' and device-specific settings\nPCI Devices -  'RTSI_0' through  'RTSI_7' and device-specific settings\nExamples of Device-Specific Settings\n- NI PXI-5122 supports  'PFI0' and  'PFI1'\n- NI PXI-5421 supports  'PFI0',  'PFI1',  'PFI4', and  'PFI5'\n- NI PXI-6551/6552 supports  'PFI0',  'PFI1',  'PFI2', and  'PFI3'\nDefault Value is empty string\n"
        },
        'lv_property': 'Export Sync Pulse Output Terminal',
        'name': 'EXPORTED_SYNC_PULSE_OUTPUT_TERMINAL',
        'resettable': False,
        'type': 'ViString'
    },
    3: {
        'access': 'read-write',
        'attribute_class': 'AttributeSessionReference',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the start trigger master session.\nFor external triggers, the session that originally receives the trigger.  For None (no trigger configured) or software triggers, the session that  originally generates the trigger.\n'
        },
        'lv_property': 'Start Trigger Master Session',
        'name': 'START_TRIGGER_MASTER_SESSION',
        'resettable': False,
        'type': 'ViSession',
        'type_in_documentation': 'Driver Session or nitclk.SessionReference',
    },
    4: {
        'access': 'read-write',
        'attribute_class': 'AttributeSessionReference',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the reference trigger master session.\nFor external triggers, the session that originally receives the trigger.  For None (no trigger configured) or software triggers, the session that  originally generates the trigger.\n'
        },
        'lv_property': 'Reference Trigger Master Session',
        'name': 'REF_TRIGGER_MASTER_SESSION',
        'resettable': False,
        'type': 'ViSession',
        'type_in_documentation': 'Driver Session or nitclk.SessionReference',
    },
    5: {
        'access': 'read-write',
        'attribute_class': 'AttributeSessionReference',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies the script trigger master session.\nFor external triggers, the session that originally receives the trigger.  For None (no trigger configured) or software triggers, the session that  originally generates the trigger.\n'
        },
        'lv_property': 'Script Trigger Master Session',
        'name': 'SCRIPT_TRIGGER_MASTER_SESSION',
        'resettable': False,
        'type': 'ViSession',
        'type_in_documentation': 'Driver Session or nitclk.SessionReference',
    },
    6: {
        'access': 'read-write',
        'attribute_class': 'AttributeSessionReference',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the pause trigger master session.\nFor external triggers, the session that originally receives the trigger.  For None (no trigger configured) or software triggers, the session that  originally generates the trigger.\n'
        },
        'lv_property': 'Pause Trigger Master Session',
        'name': 'PAUSE_TRIGGER_MASTER_SESSION',
        'resettable': False,
        'type': 'ViSession',
        'type_in_documentation': 'Driver Session or nitclk.SessionReference',
    },
    8: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': '\nIndicates the computed TClk period that will be used during the acquisition.\n'
        },
        'lv_property': 'Period',
        'name': 'TCLK_ACTUAL_PERIOD',
        'resettable': False,
        'type': 'ViReal64',
    },
    9: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': "\nSpecifies the destination of the device's TClk signal.\nValues\nEmpty string. Empty string is a valid value, indicating that the signal is  not exported.\nPXI Devices -  'PXI_Trig0' through  'PXI_Trig7' and device-specific settings\nPCI Devices -  'RTSI_0' through  'RTSI_7' and device-specific settings\nExamples of Device-Specific Settings\n- NI PXI-5122 supports  'PFI0' and  'PFI1'\n- NI PXI-5421 supports  'PFI0',  'PFI1',  'PFI4', and  'PFI5'\n- NI PXI-6551/6552 supports  'PFI0',  'PFI1',  'PFI2', and  'PFI3'\nDefault Value is empty string\n"
        },
        'lv_property': 'Output Terminal',
        'name': 'EXPORTED_TCLK_OUTPUT_TERMINAL',
        'resettable': False,
        'type': 'ViString',
    },
    10: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': "\nSpecifies the Sync Pulse Clock source. This attribute is typically used to  synchronize PCI devices when you want to control RTSI 7 yourself. Make  sure that a 10 MHz clock is driven onto RTSI 7.\nValues\nPCI Devices -  'RTSI_7' and  'None'\nPXI Devices -  'PXI_CLK10' and  'None'\nDefault Value -  'None' directs niTClk_Synchronize to create the necessary routes. For  PCI, one of the synchronized devices drives a 10 MHz clock on RTSI 7  unless that line is already being driven.\n"
        },
        'lv_property': 'Sync Pulse Clock Source',
        'name': 'SYNC_PULSE_CLOCK_SOURCE',
        'resettable': False,
        'type': 'ViString'
    },
    11: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the sample clock delay.\nSpecifies the delay, in seconds, to apply to the session sample clock  relative to the other synchronized sessions. During synchronization,  NI-TClk aligns the sample clocks on the synchronized devices. If you want  to delay the sample clocks, set this attribute before calling  niTClk_Synchronize.\nnot supported for acquisition sessions.\nValues - Between minus one and plus one period of the sample clock.\nOne sample clock period is equal to (1/sample clock rate). For example,  for a session with sample rate of 100 MS/s, you can specify sample clock  delays between -10.0 ns and +10.0 ns.\nDefault Value is 0\n',
            'note': 'Sample clock delay is supported for generation sessions only; it is'
        },
        'lv_property': 'Sample Clock Delay',
        'name': 'SAMPLE_CLOCK_DELAY',
        'resettable': False,
        'type': 'ViReal64',
        'type_in_documentation': 'float in seconds or datetime.timedelta',
    },
    13: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': "\nSpecifies the external sync pulse source for the Sync Pulse Sender.  You can use this source to synchronize  the Sync Pulse Sender with an external non-TClk source.\nValues\nEmpty string. Empty string is a valid value, indicating that the signal is  not exported.\nPXI Devices -  'PXI_Trig0' through  'PXI_Trig7' and device-specific settings\nPCI Devices -  'RTSI_0' through  'RTSI_7' and device-specific settings\nExamples of Device-Specific Settings\n- NI PXI-5122 supports  'PFI0' and  'PFI1'\n- NI PXI-5421 supports  'PFI0',  'PFI1',  'PFI4', and  'PFI5'\n- NI PXI-6551/6552 supports  'PFI0',  'PFI1',  'PFI2', and  'PFI3'\nDefault Value is empty string\n"
        },
        'lv_property': 'External Pulse Source',
        'name': 'SYNC_PULSE_SENDER_SYNC_PULSE_SOURCE',
        'resettable': False,
        'type': 'ViString'
    },
    16: {
        'access': 'read-write',
        'attribute_class': 'AttributeSessionReference',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the sequencer flag master session.\nFor external triggers, the session that originally receives the trigger.\nFor None (no trigger configured) or software triggers, the session that\noriginally generates the trigger.\n'
        },
        'lv_property': 'Sequencer Flag Master Session',
        'name': 'SEQUENCER_FLAG_MASTER_SESSION',
        'resettable': False,
        'type': 'ViSession',
        'type_in_documentation': 'Driver Session or nitclk.SessionReference',
    }
}
