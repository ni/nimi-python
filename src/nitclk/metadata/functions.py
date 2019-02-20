# -*- coding: utf-8 -*-
# This file is code generated, do not make changes here
#  If the generated information is not correct for python
#  changes can be made in functions_addon.py and they will be
#  applied at build time


functions = {
    'ConfigureForHomogeneousTriggers': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'sessionCount',
                'type': 'ViUInt32',
'documentation': {
'description': 'Number of elements in the sessions array',
},
            },
            {
                'direction': 'in',
                'name': 'Sessions',
                'type': 'ViSession []',
'documentation': {
'description': 'sessions is an array of sessions that are being synchronized.',
},
            },
        ],
'documentation': {
'description': '''
Configures the attributes commonly required for the TClk synchronization
of device sessions with homogeneous triggers in a single PXI chassis or
a single PC. Use niTClk_ConfigureForHomogeneousTriggers to configure
the attributes for the reference clocks, start triggers, reference
triggers, script triggers, and pause triggers. If
niTClk_ConfigureForHomogeneousTriggers cannot perform all the steps
appropriate for the given sessions, it returns an error. If an error is
returned, use the instrument driver functions and attributes for signal
routing, along with the following NI-TClk attributes:
NITCLK_ATTR_START_TRIGGER_MASTER_SESSION
NITCLK_ATTR_REF_TRIGGER_MASTER_SESSION
NITCLK_ATTR_SCRIPT_TRIGGER_MASTER_SESSION
NITCLK_ATTR_PAUSE_TRIGGER_MASTER_SESSION
niTClk_ConfigureForHomogeneousTriggers affects the following clocks and
triggers: - Reference clocks - Start triggers - Reference triggers -
Script triggers - Pause triggers Reference Clocks
niTClk_ConfigureForHomogeneousTriggers configures the reference clocks
if they are needed. Specifically, if the internal sample clocks or
internal sample clock timebases are used, and the reference clock source
is not configured--or is set to None (no trigger
configured)--niTClk_ConfigureForHomogeneousTriggers configures the
following: PXI--The reference clock source on all devices is set to be
the 10 MHz PXI backplane clock (PXI_CLK10). PCI--One of the devices
exports its 10 MHz onboard reference clock to RTSI 7. The reference
clock source on all devices is set to be RTSI 7. Note: If the reference
clock source is set to a value other than None,
niTClk_ConfigureForHomogeneousTriggers cannot configure the reference
clock source. Start Triggers If the start trigger is set to None (no
trigger configured) for all sessions, the sessions are configured to
share the start trigger. The start trigger is shared by: - Implicitly
exporting the start trigger from one session - Configuring the other
sessions for digital edge start triggers with sources corresponding to
the exported start trigger - Setting
NITCLK_ATTR_START_TRIGGER_MASTER_SESSION to the session that is
exporting the trigger for all sessions If the start triggers are None
for all except one session, niTClk_ConfigureForHomogeneousTriggers
configures the sessions to share the start trigger from the one excepted
session. The start trigger is shared by: - Implicitly exporting start
trigger from the session with the start trigger that is not None -
Configuring the other sessions for digital-edge start triggers with
sources corresponding to the exported start trigger - Setting
NITCLK_ATTR_START_TRIGGER_MASTER_SESSION to the session that is
exporting the trigger for all sessions If start triggers are configured
for all sessions, niTClk_ConfigureForHomogeneousTriggers does not
affect the start triggers. Start triggers are considered to be
configured for all sessions if either of the following conditions is
true: - No session has a start trigger that is None - One session has a
start trigger that is None, and all other sessions have start triggers
other than None. The one session with the None trigger must have
NITCLK_ATTR_START_TRIGGER_MASTER_SESSION set to itself, indicating
that the session itself is the start trigger master Reference Triggers
niTClk_ConfigureForHomogeneousTriggers configures sessions that support
reference triggers to share the reference triggers if the reference
triggers are None (no trigger configured) for all except one session.
The reference triggers are shared by: - Implicitly exporting the
reference trigger from the session whose reference trigger is not None -
Configuring the other sessions that support the reference trigger for
digital-edge reference triggers with sources corresponding to the
exported reference trigger - Setting
NITCLK_ATTR_REF_TRIGGER_MASTER_SESSION to the session that is
exporting the trigger for all sessions that support reference trigger If
the reference triggers are configured for all sessions that support
reference triggers, niTClk_ConfigureForHomogeneousTriggers does not
affect the reference triggers. Reference triggers are considered to be
configured for all sessions if either one or the other of the following
conditions is true: - No session has a reference trigger that is None -
One session has a reference trigger that is None, and all other sessions
have reference triggers other than None. The one session with the None
trigger must have NITCLK_ATTR_REF_TRIGGER_MASTER_SESSION set to
itself, indicating that the session itself is the reference trigger
master Reference Trigger Holdoffs Acquisition sessions may be configured
with the reference trigger. For acquisition sessions, when the reference
trigger is shared, niTClk_ConfigureForHomogeneousTriggers configures
the holdoff attributes (which are instrument driver specific) on the
reference trigger master session so that the session does not recognize
the reference trigger before the other sessions are ready. This
condition is only relevant when the sample clock rates, sample clock
timebase rates, sample counts, holdoffs, and/or any delays for the
acquisitions are different. When the sample clock rates, sample clock
timebase rates, and/or the sample counts are different in acquisition
sessions sharing the reference trigger, you should also set the holdoff
attributes for the reference trigger master using the instrument driver.
Script Triggers niTClk_ConfigureForHomogeneousTriggers configures
sessions that support script triggers to share them, if the script
triggers are None (no trigger configured) for all except one session.
The script triggers are shared in the following ways: - Implicitly
exporting the script trigger from the session whose script trigger is
not None - Configuring the other sessions that support the script
trigger for digital-edge script triggers with sources corresponding to
the exported script trigger - Setting
NITCLK_ATTR_SCRIPT_TRIGGER_MASTER_SESSION to the session that is
exporting the trigger for all sessions that support script triggers If
the script triggers are configured for all sessions that support script
triggers, niTClk_ConfigureForHomogeneousTriggers does not affect script
triggers. Script triggers are considered to be configured for all
sessions if either one or the other of the following conditions are
true: - No session has a script trigger that is None - One session has a
script trigger that is None and all other sessions have script triggers
other than None. The one session with the None trigger must have
NITCLK_ATTR_SCRIPT_TRIGGER_MASTER_SESSION set to itself, indicating
that the session itself is the script trigger master Pause Triggers
niTClk_ConfigureForHomogeneousTriggers configures generation sessions
that support pause triggers to share them, if the pause triggers are
None (no trigger configured) for all except one session. The pause
triggers are shared by: - Implicitly exporting the pause trigger from
the session whose script trigger is not None - Configuring the other
sessions that support the pause trigger for digital-edge pause triggers
with sources corresponding to the exported pause trigger - Setting
NITCLK_ATTR_PAUSE_TRIGGER_MASTER_SESSION to the session that is
exporting the trigger for all sessions that support script triggers If
the pause triggers are configured for all generation sessions that
support pause triggers, niTClk_ConfigureForHomogeneousTriggers does not
affect pause triggers. Pause triggers are considered to be configured
for all sessions if either one or the other of the following conditions
is true: - No session has a pause trigger that is None - One session has
a pause trigger that is None and all other sessions have pause triggers
other than None. The one session with the None trigger must have
NITCLK_ATTR_PAUSE_TRIGGER_MASTER_SESSION set to itself, indicating
that the session itself is the pause trigger master Note: TClk
synchronization is not supported for pause triggers on acquisition
sessions.
''',
},
    },
    'FinishSyncPulseSenderSynchronize': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'sessionCount',
                'type': 'ViUInt32',
'documentation': {
'description': 'Number of elements in the sessions array',
},
            },
            {
                'direction': 'in',
                'name': 'Sessions',
                'type': 'ViSession []',
'documentation': {
'description': 'sessions is an array of sessions that are being synchronized.',
},
            },
            {
                'direction': 'in',
                'name': 'minTime',
                'type': 'ViReal64',
'documentation': {
'description': '''
Minimal period of TClk, expressed in seconds. Supported values are
between 0.0 s and 0.050 s (50 ms). Minimal period for a single
chassis/PC is 200 ns. If the specified value is less than 200 ns,
NI-TClk automatically coerces minTime to 200 ns. For multichassis
synchronization, adjust this value to account for propagation delays
through the various devices and cables.
''',
},
            },
        ],

    },
    'GetAttributeViReal64': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'Session',
                'type': 'ViSession',
'documentation': {
'description': 'session references the sessions being synchronized.',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': 'Pass VI_NULL or an empty string',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': '''
The ID of the attribute that you want to get Supported Attribute
NITCLK_ATTR_SAMPLE_CLOCK_DELAY
''',
},
            },
            {
                'direction': 'out',
                'name': 'Value',
                'type': 'ViReal64',
'documentation': {
'description': 'The value that you are getting',
},
            },
        ],
'documentation': {
'description': 'Gets the value of an NI-TClk ViReal64 attribute.',
},
    },
    'GetAttributeViSession': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'Session',
                'type': 'ViSession',
'documentation': {
'description': 'session references the sessions being synchronized.',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Pass VI_NULL or an empty string, except for
NITCLK_ATTR_SCRIPT_TRIGGER_MASTER_SESSION, for which you should
specify scriptTrigger0, scriptTrigger1, scriptTrigger2, or
scriptTrigger3. VI_NULL and the empty string are treated as
scriptTrigger0 for NITCLK_ATTR_SCRIPT_TRIGGER_MASTER_SESSION.
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': '''
The ID of the attribute that you want to set Supported Attributes
NITCLK_ATTR_START_TRIGGER_MASTER_SESSION
NITCLK_ATTR_REF_TRIGGER_MASTER_SESSION
NITCLK_ATTR_SCRIPT_TRIGGER_MASTER_SESSION
NITCLK_ATTR_PAUSE_TRIGGER_MASTER_SESSION
''',
},
            },
            {
                'direction': 'out',
                'name': 'Value',
                'type': 'ViSession',
'documentation': {
'description': 'The value that you are getting',
},
            },
        ],
'documentation': {
'description': 'Gets the value of an NI-TClk ViSession attribute.',
},
    },
    'GetAttributeViString': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'Session',
                'type': 'ViSession',
'documentation': {
'description': 'session references the sessions being synchronized.',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': 'Pass VI_NULL or an empty string',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': '''
The ID of the attribute that you want to get Supported Attributes
NITCLK_ATTR_SYNC_PULSE_SOURCE
NITCLK_ATTR_SYNC_PULSE_CLOCK_SOURCE
NITCLK_ATTR_EXPORTED_SYNC_PULSE_OUTPUT_TERMINAL
''',
},
            },
            {
                'direction': 'in',
                'name': 'bufSize',
                'type': 'ViInt32',
'documentation': {
'description': '''
The number of bytes in the ViChar array that you specify for the value
parameter
''',
},
            },
            {
                'direction': 'in',
                'name': 'Value',
                'type': 'ViChar []',
'documentation': {
'description': 'The value that you are getting',
},
            },
        ],
'documentation': {
'description': '''
This function queries the value of an NI-TClk ViString attribute. You
must provide a ViChar array to serve as a buffer for the value. You pass
the number of bytes in the buffer as bufSize. If the current value of
the attribute, including the terminating NULL byte, is larger than the
size you indicate in bufSize, the function copies bufSize minus 1 bytes
into the buffer, places an ASCII NULL byte at the end of the buffer, and
returns the array size that you must pass to get the entire value. For
example, if the value is "123456" and bufSize is 4, the function places
"123" into the buffer and returns 7. If you want to call
niTClk_GetAttributeViString just to get the required array size, pass 0
for bufSize and VI_NULL for the value.
''',
},
    },
    'GetExtendedErrorInfo': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'out',
                'name': 'errorString',
                'type': 'ViChar []',
'documentation': {
'description': '''
Extended error description. If errorString is NULL, then it is not large
enough to hold the entire error description. In this case, the return
value of niTClk_GetExtendedErrorInfo is the size that you should use
for niTClk_GetExtendedErrorInfo to return the full error string.
''',
},
            },
            {
                'direction': 'in',
                'name': 'errorStringSize',
                'type': 'ViUInt32',
'documentation': {
'description': '''
Size of the errorString. If errorStringSize is 0, then it is not large
enough to hold the entire error description. In this case, the return
value of niTClk_GetExtendedErrorInfo is the size that you should use
for niTClk_GetExtendedErrorInfo to return the full error string.
''',
},
            },
        ],
'documentation': {
'description': '''
Reports extended error information for the most recent NI-TClk function
that returned an error. To establish the function that returned an
error, use the return values of the individual functions because once
niTClk_GetExtendedErrorInfo reports an errorString, it does not report
an empty string again.
''',
},
    },
    'Initiate': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'sessionCount',
                'type': 'ViUInt32',
'documentation': {
'description': 'Number of elements in the sessions array',
},
            },
            {
                'direction': 'in',
                'name': 'Sessions',
                'type': 'ViSession []',
'documentation': {
'description': 'sessions is an array of sessions that are being synchronized.',
},
            },
        ],
'documentation': {
'description': '''
Initiates the acquisition or generation sessions specified, taking into
consideration any special requirements needed for synchronization. For
example, the session exporting the TClk-synchronized start trigger is
not initiated until after niTClk_Initiate initiates all the sessions
that import the TClk-synchronized start trigger.
''',
},
    },
    'IsDone': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'sessionCount',
                'type': 'ViUInt32',
'documentation': {
'description': 'Number of elements in the sessions array',
},
            },
            {
                'direction': 'in',
                'name': 'Sessions',
                'type': 'ViSession []',
'documentation': {
'description': 'sessions is an array of sessions that are being synchronized.',
},
            },
            {
                'direction': 'out',
                'name': 'Done',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Indicates that the operation is done. The operation is done when each
session has completed without any errors or when any one of the sessions
reports an error.
''',
},
            },
        ],
'documentation': {
'description': '''
Monitors the progress of the acquisitions and/or generations
corresponding to sessions.
''',
},
    },
    'SetAttributeViReal64': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'Session',
                'type': 'ViSession',
'documentation': {
'description': 'session references the sessions being synchronized.',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': 'Pass VI_NULL or an empty string',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': '''
The ID of the attribute that you want to set Supported Attribute
NITCLK_ATTR_SAMPLE_CLOCK_DELAY
''',
},
            },
            {
                'direction': 'in',
                'name': 'Value',
                'type': 'ViReal64',
'documentation': {
'description': 'The value for the attribute',
},
            },
        ],
'documentation': {
'description': '''
Sets the value of an NI-TClk VIReal64 attribute.
niTClk_SetAttributeViReal64 is a low-level function that you can use to
set the values NI-TClk attributes. NI-TClk contains high-level functions
that set most of the attributes. It is best to use the high-level
functions as much as possible.
''',
},
    },
    'SetAttributeViSession': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'Session',
                'type': 'ViSession',
'documentation': {
'description': 'session references the sessions being synchronized.',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Pass VI_NULL or an empty string, except for
NITCLK_ATTR_SCRIPT_TRIGGER_MASTER_SESSION, for which you should
specify scriptTrigger0, scriptTrigger1, scriptTrigger2, or
scriptTrigger3. VI_NULL and the empty string are treated as
scriptTrigger0 for NITCLK_ATTR_SCRIPT_TRIGGER_MASTER_SESSION.
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': '''
The ID of the attribute that you want to set Supported Attributes
NITCLK_ATTR_START_TRIGGER_MASTER_SESSION
NITCLK_ATTR_REF_TRIGGER_MASTER_SESSION
NITCLK_ATTR_SCRIPT_TRIGGER_MASTER_SESSION
NITCLK_ATTR_PAUSE_TRIGGER_MASTER_SESSION
''',
},
            },
            {
                'direction': 'in',
                'name': 'Value',
                'type': 'ViSession',
'documentation': {
'description': 'The value for the attribute',
},
            },
        ],
'documentation': {
'description': '''
Sets the value of an NI-TClk ViSession attribute.
niTClk_SetAttributeViSession is a low-level function that you can use
to set the values NI-TClk attributes. NI-TClk contains high-level
functions that set most of the attributes. It is best to use the
high-level functions as much as possible.
''',
},
    },
    'SetAttributeViString': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'Session',
                'type': 'ViSession',
'documentation': {
'description': 'session references the sessions being synchronized.',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': 'Pass VI_NULL or an empty string',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': '''
Pass the ID of the attribute that you want to set Supported Attributes
NITCLK_ATTR_SYNC_PULSE_SOURCE
NITCLK_ATTR_SYNC_PULSE_CLOCK_SOURCE
NITCLK_ATTR_EXPORTED_SYNC_PULSE_OUTPUT_TERMINAL
''',
},
            },
            {
                'direction': 'in',
                'name': 'Value',
                'type': 'ViConstString',
'documentation': {
'description': 'Pass the value for the attribute',
},
            },
        ],
'documentation': {
'description': '''
Sets the value of an NI-TClk VIString attribute.
niTClk_SetAttributeViString is a low-level function that you can use to
set the values of NI-TClk attributes. NI-TClk contain high-level
functions that set most of the attributes. It is best to use the
high-level functions as much as possible.
''',
},
    },
    'SetupForSyncPulseSenderSynchronize': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'sessionCount',
                'type': 'ViUInt32',
'documentation': {
'description': 'Number of elements in the sessions array',
},
            },
            {
                'direction': 'in',
                'name': 'Sessions',
                'type': 'ViSession []',
'documentation': {
'description': 'sessions is an array of sessions that are being synchronized.',
},
            },
            {
                'direction': 'in',
                'name': 'minTime',
                'type': 'ViReal64',
'documentation': {
'description': '''
Minimal period of TClk, expressed in seconds. Supported values are
between 0.0 s and 0.050 s (50 ms). Minimal period for a single
chassis/PC is 200 ns. If the specified value is less than 200 ns,
NI-TClk automatically coerces minTime to 200 ns. For multichassis
synchronization, adjust this value to account for propagation delays
through the various devices and cables.
''',
},
            },
        ],

    },
    'Synchronize': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'sessionCount',
                'type': 'ViUInt32',
'documentation': {
'description': 'Number of elements in the sessions array',
},
            },
            {
                'direction': 'in',
                'name': 'Sessions',
                'type': 'ViSession []',
'documentation': {
'description': 'sessions is an array of sessions that are being synchronized.',
},
            },
            {
                'direction': 'in',
                'name': 'minTime',
                'type': 'ViReal64',
'documentation': {
'description': '''
Minimal period of TClk, expressed in seconds. Supported values are
between 0.0 s and 0.050 s (50 ms). Minimal period for a single
chassis/PC is 200 ns. If the specified value is less than 200 ns,
NI-TClk automatically coerces minTime to 200 ns. For multichassis
synchronization, adjust this value to account for propagation delays
through the various devices and cables.
''',
},
            },
        ],
'documentation': {
'description': '''
Synchronizes the TClk signals on the given sessions. After
niTClk_Synchronize executes, TClk signals from all sessions are
synchronized. Note: Before using this NI-TClk function, verify that your
system is configured as specified in the PXI Trigger Lines and RTSI
Lines topic of the NI-TClk Synchronization Help. You can locate this
help file at Start>>Programs>>National Instruments>>NI-TClk.
''',
},
    },
    'SyncronizeToSyncPulseSender': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'sessionCount',
                'type': 'ViUInt32',
'documentation': {
'description': 'Number of elements in the sessions array',
},
            },
            {
                'direction': 'in',
                'name': 'Sessions',
                'type': 'ViSession []',
'documentation': {
'description': 'sessions is an array of sessions that are being synchronized.',
},
            },
            {
                'direction': 'in',
                'name': 'minTime',
                'type': 'ViReal64',
'documentation': {
'description': '''
Minimal period of TClk, expressed in seconds. Supported values are
between 0.0 s and 0.050 s (50 ms). Minimal period for a single
chassis/PC is 200 ns. If the specified value is less than 200 ns,
NI-TClk automatically coerces minTime to 200 ns. For multichassis
synchronization, adjust this value to account for propagation delays
through the various devices and cables.
''',
},
            },
        ],

    },
    'WaitUntilDone': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'sessionCount',
                'type': 'ViUInt32',
'documentation': {
'description': 'Number of elements in the sessions array',
},
            },
            {
                'direction': 'in',
                'name': 'Sessions',
                'type': 'ViSession []',
'documentation': {
'description': 'sessions is an array of sessions that are being synchronized.',
},
            },
            {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'ViReal64',
'documentation': {
'description': '''
The amount of time in seconds that niTClk_WaitUntilDone waits for the
sessions to complete. If timeout is exceeded, niTClk_WaitUntilDone
returns an error.
''',
},
            },
        ],
'documentation': {
'description': '''
Call this function to pause execution of your program until the
acquisitions and/or generations corresponding to sessions are done or
until the function returns a timeout error. niTClk_WaitUntilDone is a
blocking function that periodically checks the operation status. It
returns control to the calling program if the operation completes
successfully or an error occurs (including a timeout error). This
function is most useful for finite data operations that you expect to
complete within a certain time.
''',
},
    },
}
