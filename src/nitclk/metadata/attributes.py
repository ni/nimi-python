# -*- coding: utf-8 -*-
# This file is code generated, do not make changes here.
#  If the generated information is not correct for python
#  changes can be made in attributes_addon.py and they will be
#  applied at build time.

attributes = {
    1: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Sync Pulse Source',
        'name': 'SYNC_PULSE_SOURCE',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the Sync Pulse source. This attribute is most often used when  synchronizing a multichassis system.
Values
Empty string
PXI Devices -  'PXI_Trig0' through  'PXI_Trig7' and device-specific settings
PCI Devices -  'RTSI_0' through  'RTSI_7' and device-specific settings
Examples of Device-Specific Settings
- NI PXI-5122 supports  'PFI0' and  'PFI1'
- NI PXI-5421 supports  'PFI0',  'PFI1',  'PFI2', and  'PFI3'
- NI PXI-6551/6552 supports  'PFI0',  'PFI1',  'PFI2', and  'PFI3'
Default Value - Empty string. This default value directs  niTClk_Synchronize to set this attribute when all the synchronized devices  are in one PXI chassis. To synchronize a multichassis system, you must set  this attribute before calling niTClk_Synchronize.
''',
},
    },
    2: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Export Sync Pulse Output Terminal',
        'name': 'EXPORTED_SYNC_PULSE_OUTPUT_TERMINAL',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the destination of the Sync Pulse. This attribute is most often  used when synchronizing a multichassis system.
Values
Empty string. Empty string is a valid value, indicating that the signal is  not exported.
PXI Devices -  'PXI_Trig0' through  'PXI_Trig7' and device-specific settings
PCI Devices -  'RTSI_0' through  'RTSI_7' and device-specific settings
Examples of Device-Specific Settings
- NI PXI-5122 supports  'PFI0' and  'PFI1'
- NI PXI-5421 supports  'PFI0',  'PFI1',  'PFI4', and  'PFI5'
- NI PXI-6551/6552 supports  'PFI0',  'PFI1',  'PFI2', and  'PFI3'
Default Value is empty string
''',
},
    },
    3: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Start Trigger Master Session',
        'name': 'START_TRIGGER_MASTER_SESSION',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the start trigger master session.
For external triggers, the session that originally receives the trigger.  For None (no trigger configured) or software triggers, the session that  originally generates the trigger.
''',
},
    },
    4: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Reference Trigger Master Session',
        'name': 'REF_TRIGGER_MASTER_SESSION',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the reference trigger master session.
For external triggers, the session that originally receives the trigger.  For None (no trigger configured) or software triggers, the session that  originally generates the trigger.
''',
},
    },
    5: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Script Trigger Master Session',
        'name': 'SCRIPT_TRIGGER_MASTER_SESSION',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the script trigger master session.
For external triggers, the session that originally receives the trigger.  For None (no trigger configured) or software triggers, the session that  originally generates the trigger.
''',
},
    },
    6: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Pause Trigger Master Session',
        'name': 'PAUSE_TRIGGER_MASTER_SESSION',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the pause trigger master session.
For external triggers, the session that originally receives the trigger.  For None (no trigger configured) or software triggers, the session that  originally generates the trigger.
''',
},
    },
    8: {
        'access': 'read only',
        'channel_based': 'False',
        'lv_property': 'Period',
        'name': 'TCLK_ACTUAL_PERIOD',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Indicates the computed TClk period that will be used during the acquisition.
''',
},
    },
    9: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Output Terminal',
        'name': 'EXPORTED_TCLK_OUTPUT_TERMINAL',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the destination of the device's TClk signal.
Values
Empty string. Empty string is a valid value, indicating that the signal is  not exported.
PXI Devices -  'PXI_Trig0' through  'PXI_Trig7' and device-specific settings
PCI Devices -  'RTSI_0' through  'RTSI_7' and device-specific settings
Examples of Device-Specific Settings
- NI PXI-5122 supports  'PFI0' and  'PFI1'
- NI PXI-5421 supports  'PFI0',  'PFI1',  'PFI4', and  'PFI5'
- NI PXI-6551/6552 supports  'PFI0',  'PFI1',  'PFI2', and  'PFI3'
Default Value is empty string
''',
},
    },
    10: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Sync Pulse Clock Source',
        'name': 'SYNC_PULSE_CLOCK_SOURCE',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the Sync Pulse Clock source. This attribute is typically used to  synchronize PCI devices when you want to control RTSI 7 yourself. Make  sure that a 10 MHz clock is driven onto RTSI 7.
Values
PCI Devices -  'RTSI_7' and  'None'
PXI Devices -  'PXI_CLK10' and  'None'
Default Value -  'None' directs niTClk_Synchronize to create the necessary routes. For  PCI, one of the synchronized devices drives a 10 MHz clock on RTSI 7  unless that line is already being driven.
''',
},
    },
    11: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Sample Clock Delay',
        'name': 'SAMPLE_CLOCK_DELAY',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the sample clock delay.
Specifies the delay, in seconds, to apply to the session sample clock  relative to the other synchronized sessions. During synchronization,  NI-TClk aligns the sample clocks on the synchronized devices. If you want  to delay the sample clocks, set this attribute before calling  niTClk_Synchronize.
not supported for acquisition sessions.
Values - Between minus one and plus one period of the sample clock.
One sample clock period is equal to (1/sample clock rate). For example,  for a session with sample rate of 100 MS/s, you can specify sample clock  delays between -10.0 ns and +10.0 ns.
Default Value is 0
''',
'note': 'Sample clock delay is supported for generation sessions only; it is',
},
    },
    13: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'External Pulse Source',
        'name': 'SYNC_PULSE_SENDER_SYNC_PULSE_SOURCE',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the external sync pulse source for the Sync Pulse Sender.  You can use this source to synchronize  the Sync Pulse Sender with an external non-TClk source.
Values
Empty string. Empty string is a valid value, indicating that the signal is  not exported.
PXI Devices -  'PXI_Trig0' through  'PXI_Trig7' and device-specific settings
PCI Devices -  'RTSI_0' through  'RTSI_7' and device-specific settings
Examples of Device-Specific Settings
- NI PXI-5122 supports  'PFI0' and  'PFI1'
- NI PXI-5421 supports  'PFI0',  'PFI1',  'PFI4', and  'PFI5'
- NI PXI-6551/6552 supports  'PFI0',  'PFI1',  'PFI2', and  'PFI3'
Default Value is empty string
''',
},
    },
    16: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Sequencer Flag Master Session',
        'name': 'SEQUENCER_FLAG_MASTER_SESSION',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the sequencer flag master session.
For external triggers, the session that originally receives the trigger.
For None (no trigger configured) or software triggers, the session that
originally generates the trigger.
''',
},
    },
}
