
# -*- coding: utf-8 -*-
# This file is code generated, do not make changes here
#  If the generated information is not correct for python
#  changes can be made in functions_addon.py and they will be
#  applied at build time


functions = {
    'AbortScan': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
        ],
'documentation': {
'description': '''
Aborts the scan in progress. Initiate a scan with
niSwitch\_InitiateScan. If the switch module is not scanning,
NISWITCH\_ERROR\_NO\_SCAN\_IN\_PROGRESS error is returned.
''',
},
    },
    'CanConnect': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channel1',
                'type': 'ViConstString',
'documentation': {
'description': '''
Input one of the channel names of the desired path. Pass the other
channel name as the channel 2 parameter. Refer to Devices Overview for
valid channel names for the switch module. Examples of valid channel
names: ch0, com0, ab0, r1, c2, cjtemp Default value: ""
''',
},
            },
            {
                'direction': 'in',
                'name': 'channel2',
                'type': 'ViConstString',
'documentation': {
'description': '''
Input one of the channel names of the desired path. Pass the other
channel name as the channel 1 parameter. Refer to Devices Overview for
valid channel names for the switch module. Examples of valid channel
names: ch0, com0, ab0, r1, c2, cjtemp Default value: ""
''',
},
            },
            {
                'direction': 'out',
                'name': 'pathCapability',
                'type': 'ViInt32',
'documentation': {
'description': '''
Indicates whether a path is valid. Possible values include:
------------------------------------ NISWITCH\_VAL\_PATH\_AVAILABLE 1
NISWITCH\_VAL\_PATH\_EXISTS 2 NISWITCH\_VAL\_PATH\_UNSUPPORTED 3
NISWITCH\_VAL\_RSRC\_IN\_USE 4 NISWITCH\_VAL\_SOURCE\_CONFLICT 5
NISWITCH\_VAL\_CHANNEL\_NOT\_AVAILABLE 6 Notes: (1)
NISWITCH\_VAL\_PATH\_AVAILABLE indicates that the driver can create the
path at this time. (2) NISWITCH\_VAL\_PATH\_EXISTS indicates that the
path already exists. (3) NISWITCH\_VAL\_PATH\_UNSUPPORTED indicates that
the instrument is not capable of creating a path between the channels
you specify. (4) NISWITCH\_VAL\_RSRC\_IN\_USE indicates that although
the path is valid, the driver cannot create the path at this moment
because the switch device is currently using one or more of the required
channels to create another path. You must destroy the other path before
creating this one. (5) NISWITCH\_VAL\_SOURCE\_CONFLICT indicates that
the instrument cannot create a path because both channels are connected
to a different source channel. (6)
NISWITCH\_VAL\_CHANNEL\_NOT\_AVAILABLE indicates that the driver cannot
create a path between the two channels because one of the channels is a
configuration channel and thus unavailable for external connections.
''',
},
            },
        ],
'documentation': {
'description': '''
Verifies that a path between channel 1 and channel 2 can be created. If
a path is possible in the switch module, the availability of that path
is returned given the existing connections. If the path is possible but
in use, a NISWITCH\_WARN\_IMPLICIT\_CONNECTION\_EXISTS warning is
returned.
''',
},
    },
    'CheckAttributeViBoolean': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Some attributes are unique per channel. For these, pass the name of the
channel. Other attributes are unique per switch device. Pass VI\_NULL or
an empty string for this parameter. Default Value: ""
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': '''
Pass the ID of an attribute. From the function panel window, you can use
this control as follows. - Click on the control or press , , or , to
display a dialog box containing a hierarchical list of the available
attributes. Attributes whose value cannot be set are dim. Help text is
shown for each attribute. Select an attribute by double-clicking on it
or by selecting it and then pressing . Read-only attributes appear dim
in the list box. If you select a read-only attribute, an error message
appears. A ring control at the top of the dialog box allows you to see
all IVI attributes or only the attributes of the ViBoolean type. If you
choose to see all IVI attributes, the data types appear to the right of
the attribute names in the list box. The data types that are not
consistent with this function are dim. If you select an attribute data
type that is dim, LabWindows/CVI transfers you to the function panel for
the corresponding function that is consistent with the data type. - If
you want to enter a variable name, press to change this ring control to
a manual input box. - If the attribute in this ring control has
constants as valid values, you can view the constants by moving to the
Attribute Value control and pressing .
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Pass the value which you want to verify as a valid value for the
attribute. From the function panel window, you can use this control as
follows. - If the attribute currently showing in the Attribute ID ring
control has constants as valid values, you can view a list of the
constants by pressing on this control. Select a value by double-clicking
on it or by selecting it and then pressing . Note: Some of the values
might not be valid depending on the current settings of the instrument
session. Default Value: none
''',
},
            },
        ],
'documentation': {
'description': '''
This function checks the validity of a value you specify for a ViBoolean
attribute.
''',
},
    },
    'CheckAttributeViInt32': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Some attributes are unique per channel. For these, pass the name of the
channel. Other attributes are unique per switch device. Pass VI\_NULL or
an empty string for this parameter. Default Value: ""
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': '''
Pass the ID of an attribute. From the function panel window, you can use
this control as follows. - Click on the control or press , , or , to
display a dialog box containing a hierarchical list of the available
attributes. Attributes whose value cannot be set are dim. Help text is
shown for each attribute. Select an attribute by double-clicking on it
or by selecting it and then pressing . Read-only attributes appear dim
in the list box. If you select a read-only attribute, an error message
appears. A ring control at the top of the dialog box allows you to see
all IVI attributes or only the attributes of the ViInt32 type. If you
choose to see all IVI attributes, the data types appear to the right of
the attribute names in the list box. The data types that are not
consistent with this function are dim. If you select an attribute data
type that is dim, LabWindows/CVI transfers you to the function panel for
the corresponding function that is consistent with the data type. - If
you want to enter a variable name, press to change this ring control to
a manual input box. - If the attribute in this ring control has
constants as valid values, you can view the constants by moving to the
Attribute Value control and pressing .
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViInt32',
'documentation': {
'description': '''
Pass the value which you want to verify as a valid value for the
attribute. From the function panel window, you can use this control as
follows. - If the attribute currently showing in the Attribute ID ring
control has constants as valid values, you can view a list of the
constants by pressing on this control. Select a value by double-clicking
on it or by selecting it and then pressing . Note: Some of the values
might not be valid depending on the current settings of the instrument
session. Default Value: none
''',
},
            },
        ],
'documentation': {
'description': '''
This function checks the validity of a value you specify for a ViInt32
attribute.
''',
},
    },
    'CheckAttributeViReal64': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Some attributes are unique per channel. For these, pass the name of the
channel. Other attributes are unique per switch device. Pass VI\_NULL or
an empty string for this parameter. Default Value: ""
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': '''
Pass the ID of an attribute. From the function panel window, you can use
this control as follows. - Click on the control or press , , or , to
display a dialog box containing a hierarchical list of the available
attributes. Attributes whose value cannot be set are dim. Help text is
shown for each attribute. Select an attribute by double-clicking on it
or by selecting it and then pressing . Read-only attributes appear dim
in the list box. If you select a read-only attribute, an error message
appears. A ring control at the top of the dialog box allows you to see
all IVI attributes or only the attributes of the ViReal64 type. If you
choose to see all IVI attributes, the data types appear to the right of
the attribute names in the list box. The data types that are not
consistent with this function are dim. If you select an attribute data
type that is dim, LabWindows/CVI transfers you to the function panel for
the corresponding function that is consistent with the data type. - If
you want to enter a variable name, press to change this ring control to
a manual input box. - If the attribute in this ring control has
constants as valid values, you can view the constants by moving to the
Attribute Value control and pressing .
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViReal64',
'documentation': {
'description': '''
Pass the value which you want to verify as a valid value for the
attribute. From the function panel window, you can use this control as
follows. - If the attribute currently showing in the Attribute ID ring
control has constants as valid values, you can view a list of the
constants by pressing on this control. Select a value by double-clicking
on it or by selecting it and then pressing . Note: Some of the values
might not be valid depending on the current settings of the instrument
session. Default Value: none
''',
},
            },
        ],
'documentation': {
'description': '''
This function checks the validity of a value you specify for a ViReal64
attribute.
''',
},
    },
    'CheckAttributeViSession': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Some attributes are unique per channel. For these, pass the name of the
channel. Other attributes are unique per switch device. Pass VI\_NULL or
an empty string for this parameter. Default Value: ""
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': '''
Pass the ID of an attribute. From the function panel window, you can use
this control as follows. - Click on the control or press , , or , to
display a dialog box containing a hierarchical list of the available
attributes. Attributes whose value cannot be set are dim. Help text is
shown for each attribute. Select an attribute by double-clicking on it
or by selecting it and then pressing . Read-only attributes appear dim
in the list box. If you select a read-only attribute, an error message
appears. A ring control at the top of the dialog box allows you to see
all IVI attributes or only the attributes of the ViSession type. If you
choose to see all IVI attributes, the data types appear to the right of
the attribute names in the list box. The data types that are not
consistent with this function are dim. If you select an attribute data
type that is dim, LabWindows/CVI transfers you to the function panel for
the corresponding function that is consistent with the data type. - If
you want to enter a variable name, press to change this ring control to
a manual input box. - If the attribute in this ring control has
constants as valid values, you can view the constants by moving to the
Attribute Value control and pressing .
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViSession',
'documentation': {
'description': '''
Pass the value which you want to verify as a valid value for the
attribute. From the function panel window, you can use this control as
follows. - If the attribute currently showing in the Attribute ID ring
control has constants as valid values, you can view a list of the
constants by pressing on this control. Select a value by double-clicking
on it or by selecting it and then pressing . Note: Some of the values
might not be valid depending on the current settings of the instrument
session. Default Value: none
''',
},
            },
        ],
'documentation': {
'description': '''
This function checks the validity of a value you specify for a ViSession
attribute.
''',
},
    },
    'CheckAttributeViString': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Some attributes are unique per channel. For these, pass the name of the
channel. Other attributes are unique per switch device. Pass VI\_NULL or
an empty string for this parameter. Default Value: ""
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': '''
Pass the ID of an attribute. From the function panel window, you can use
this control as follows. - Click on the control or press , , or , to
display a dialog box containing a hierarchical list of the available
attributes. Attributes whose value cannot be set are dim. Help text is
shown for each attribute. Select an attribute by double-clicking on it
or by selecting it and then pressing . Read-only attributes appear dim
in the list box. If you select a read-only attribute, an error message
appears. A ring control at the top of the dialog box allows you to see
all IVI attributes or only the attributes of the ViString type. If you
choose to see all IVI attributes, the data types appear to the right of
the attribute names in the list box. The data types that are not
consistent with this function are dim. If you select an attribute data
type that is dim, LabWindows/CVI transfers you to the function panel for
the corresponding function that is consistent with the data type. - If
you want to enter a variable name, press to change this ring control to
a manual input box. - If the attribute in this ring control has
constants as valid values, you can view the constants by moving to the
Attribute Value control and pressing .
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Pass the value which you want to verify as a valid value for the
attribute. From the function panel window, you can use this control as
follows. - If the attribute currently showing in the Attribute ID ring
control has constants as valid values, you can view a list of the
constants by pressing on this control. Select a value by double-clicking
on it or by selecting it and then pressing . Note: Some of the values
might not be valid depending on the current settings of the instrument
session. Default Value: none
''',
},
            },
        ],
'documentation': {
'description': '''
This function checks the validity of a value you specify for a ViString
attribute.
''',
},
    },
    'ClearError': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
        ],
'documentation': {
'description': '''
This function clears the error code and error description for the IVI
session. If the user specifies a valid IVI session for the
instrument\_handle parameter, this function clears the error information
for the session. If the user passes VI\_NULL for the Vi parameter, this
function clears the error information for the current execution thread.
If the Vi parameter is an invalid session, the function does nothing and
returns an error. The function clears the error code by setting it to
VI\_SUCCESS, If the error description string is non-NULL, the function
deallocates the error description string and sets the address to
VI\_NULL. Maintaining the error information separately for each thread
is useful if the user does not have a session handle to pass to the
niSwitch\_GetError function, which occurs when a call to niSwitch\_init
or niSwitch\_InitWithOptions fails.
''',
},
    },
    'ClearInterchangeWarnings': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
        ],
'documentation': {
'description': 'This function clears the list of current interchange warnings.',
},
    },
    'Commit': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
        ],
'documentation': {
'description': '''
Downloads the configured scan list and trigger settings to hardware.
Calling niSwitch\_Commit optional as it is implicitly called during
niSwitch\_InitiateScan. Use niSwitch\_Commit to arm triggers in a given
order or to control when expensive hardware operations are performed.
''',
},
    },
    'ConfigureScanList': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Scanlist',
                'type': 'ViConstString',
'documentation': {
'description': '''
The scan list to use. The driver uses this value to set the Scan List
attribute. Default value: None
''',
},
            },
            {
                'direction': 'in',
                'name': 'scanMode',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies how the switch module breaks existing connections when
scanning. The driver uses this value to set the Scan Mode attribute.
Refer to scan modes for more information. Default value: Break Before
Make
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the scan list and scan mode used for scanning. Refer to
Devices Overview to determine if the switch module supports scanning.
The scan list is comprised of a list of channel connections separated by
semi-colons. For example, the following scan list will scan the first
three channels of a multiplexer: com0->ch0; com0->ch1; com0->ch2; Refer
to Scan Lists for more information on scan list syntax To see the status
of the scan, call either niSwitch\_IsScanning or
niSwitch\_WaitForScanComplete. Use the niSwitch\_ConfigureScanTrigger
function to configure the scan trigger. Use the niSwitch\_InitiateScan
function to start the scan.
''',
},
    },
    'ConfigureScanTrigger': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
            {
                'direction': 'in',
                'name': 'scanDelay',
                'type': 'ViReal64',
'documentation': {
'description': '''
The minimum length of time you want the switch device to wait after it
creates a path until it asserts a trigger on the scan advanced output
line. The driver uses this value to set the Scan Delay attribute. The
scan delay is in addition to the settling time.The driver uses this
value to set the NISWITCH\_ATTR\_SCAN\_DELAY attribute. Express this
value in seconds. Default value: 0.0 s
''',
},
            },
            {
                'direction': 'in',
                'name': 'triggerInput',
                'type': 'ViInt32',
'documentation': {
'description': '''
Trigger source you want the switch module to use during scanning. The
driver uses this value to set the NISWITCH\_ATTR\_TRIGGER\_INPUT
attribute. The switch device waits for the trigger you specify when it
encounters a semicolon in the scanlist. When the trigger occurs, the
switch device advances to the next entry in the scanlist. Refer to the
NISWITCH\_ATTR\_TRIGGER\_INPUT topic in the NI Switches Help for a list
of valid values.
''',
},
            },
            {
                'direction': 'in',
                'name': 'scanAdvancedOutput',
                'type': 'ViInt32',
'documentation': {
'description': '''
Output destination of the scan advanced trigger signal. The driver uses
this value to set the NISWITCH\_ATTR\_SCAN\_ADVANCED\_OUTPUT attribute.
After the switch processes each entry in the scan list, it waits the
length of time you specify in the Scan Delay parameter and then asserts
a trigger on the line you specify with this parameter. Refer to the
NISWITCH\_ATTR\_SCAN\_ADVANCED\_OUTPUT topic in the NI Switches Help for
a list of valid values.
''',
},
            },
        ],
'documentation': {
'description': '''
Configures the scan triggers for the scan list established with
niSwitch\_ConfigureScanList. Refer to Devices Overview to determine if
the switch module supports scanning. niSwitch\_ConfigureScanTrigger sets
the location that the switch expects to receive an input trigger to
advance through the scan list. This function also sets the location
where it outputs a scan advanced signal after it completes an entry in
the scan list.
''',
},
    },
    'Connect': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channel1',
                'type': 'ViConstString',
'documentation': {
'description': '''
Input one of the channel names of the desired path. Pass the other
channel name as the channel 2 parameter. Refer to Devices Overview for
valid channel names for the switch module. Examples of valid channel
names: ch0, com0, ab0, r1, c2, cjtemp Default value: None
''',
},
            },
            {
                'direction': 'in',
                'name': 'channel2',
                'type': 'ViConstString',
'documentation': {
'description': '''
Input one of the channel names of the desired path. Pass the other
channel name as the channel 1 parameter. Refer to Devices Overview for
valid channel names for the switch module. Examples of valid channel
names: ch0, com0, ab0, r1, c2, cjtemp Default value: None
''',
},
            },
        ],
'documentation': {
'description': '''
Creates a path between channel 1 and channel 2. The driver calculates
and uses the shortest path between the two channels. Refer to Immediate
Operations for information about Channel Usage types. If a path is not
available, the function returns one of the following errors: -
NISWITCH\_ERROR\_EXPLICIT\_CONNECTION\_EXISTS, if the two channels are
already explicitly connected by calling either the niSwitch\_Connect or
niSwitch\_SetPath function. -
NISWITCH\_ERROR\_IS\_CONFIGURATION\_CHANNEL, if a channel is a
configuration channel. Error elaboration contains information about
which of the two channels is a configuration channel. -
NISWITCH\_ERROR\_ATTEMPT\_TO\_CONNECT\_SOURCES, if both channels are
connected to a different source. Error elaboration contains information
about sources channel 1 and 2 connect to. -
NISWITCH\_ERROR\_CANNOT\_CONNECT\_TO\_ITSELF, if channels 1 and 2 are
one and the same channel. - NISWITCH\_ERROR\_PATH\_NOT\_FOUND, if the
driver cannot find a path between the two channels. Note: Paths are
bidirectional. For example, if a path exists between channels CH1 and
CH2, then the path also exists between channels CH2 and CH1.
''',
},
    },
    'ConnectMultiple': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
            {
                'direction': 'in',
                'name': 'connectionList',
                'type': 'ViConstString',
'documentation': {
'description': '''
Connection List specifies a list of connections between channels to
make. NI-SWITCH validates the connection list, and aborts execution of
the list if errors are returned. Refer to Connection and Disconnection
List Syntax for valid connection list syntax and examples. Refer to
Devices Overview for valid channel names for the switch module. Example
of a valid connection list: c0 -> r1, [c2 -> r2 -> c3] In this example,
r2 is a configuration channel. Default value: None
''',
},
            },
        ],
'documentation': {
'description': '''
Creates the connections between channels specified in Connection List.
Specify connections with two endpoints only or the explicit path between
two endpoints. NI-SWITCH calculates and uses the shortest path between
the channels. Refer to Setting Source and Configuration Channels for
information about channel usage types. In the event of an error,
connecting stops at the point in the list where the error occurred. If a
path is not available, the function returns one of the following errors:
- NISWITCH\_ERROR\_EXPLICIT\_CONNECTION\_EXISTS, if the two channels are
already explicitly connected. -
NISWITCH\_ERROR\_IS\_CONFIGURATION\_CHANNEL, if a channel is a
configuration channel. Error elaboration contains information about
which of the two channels is a configuration channel. -
NISWITCH\_ERROR\_ATTEMPT\_TO\_CONNECT\_SOURCES, if both channels are
connected to a different source. Error elaboration contains information
about sources channel 1 and 2 to connect. -
NISWITCH\_ERROR\_CANNOT\_CONNECT\_TO\_ITSELF, if channels 1 and 2 are
one and the same channel. - NISWITCH\_ERROR\_PATH\_NOT\_FOUND, if the
driver cannot find a path between the two channels. Note: Paths are
bidirectional. For example, if a path exists between channels ch1 and
ch2, then the path also exists between channels ch1 and ch2.
''',
},
    },
    'Disable': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
        ],
'documentation': {
'description': '''
Places the switch module in a quiescent state where it has minimal or no
impact on the system to which it is connected. All channels are
disconnected and any scan in progress is aborted.
''',
},
    },
    'Disconnect': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channel1',
                'type': 'ViConstString',
'documentation': {
'description': '''
Input one of the channel names of the path to break. Pass the other
channel name as the channel 2 parameter. Refer to Devices Overview for
valid channel names for the switch module. Examples of valid channel
names: ch0, com0, ab0, r1, c2, cjtemp Default value: None
''',
},
            },
            {
                'direction': 'in',
                'name': 'channel2',
                'type': 'ViConstString',
'documentation': {
'description': '''
Input one of the channel names of the path to break. Pass the other
channel name as the channel 1 parameter. Refer to Devices Overview for
valid channel names for the switch module. Examples of valid channel
names: ch0, com0, ab0, r1, c2, cjtemp Default value: None
''',
},
            },
        ],
'documentation': {
'description': '''
This function destroys the path between two channels that you create
with the niSwitch\_Connect or niSwitch\_SetPath function. If a path is
not connected or not available, the function returns the
IVISWTCH\_ERROR\_NO\_SUCH\_PATH error.
''',
},
    },
    'DisconnectAll': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
        ],
'documentation': {
'description': '''
Breaks all existing paths. If the switch module cannot break all paths,
NISWITCH\_WARN\_PATH\_REMAINS warning is returned.
''',
},
    },
    'DisconnectMultiple': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
            {
                'direction': 'in',
                'name': 'disconnectionList',
                'type': 'ViConstString',
'documentation': {
'description': '''
Disconnection List specifies a list of connections between channels to
break. NI-SWITCH validates the disconnection list, and aborts execution
of the list if errors are returned. Refer to Connection and
Disconnection List Syntax for valid disconnection list syntax and
examples. Refer to Devices Overview for valid channel names for the
switch module. Example of a valid disconnection list: c0 -> r1, [c2 ->
r2 -> c3] In this example, r2 is a configuration channel. Default value:
None
''',
},
            },
        ],
'documentation': {
'description': '''
Breaks the connections between channels specified in Disconnection List.
If no connections exist between channels, NI-SWITCH returns an error. In
the event of an error, the VI stops at the point in the list where the
error occurred.
''',
},
    },
    'GetAttributeViBoolean': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Some attributes are unique per channel. For these, pass the name of the
channel. Other attributes are unique per switch device. Pass VI\_NULL or
an empty string for this parameter. Default Value: ""
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': '''
Pass the ID of an attribute. From the function panel window, you can use
this control as follows. - Click on the control or press , , or , to
display a dialog box containing a hierarchical list of the available
attributes. Attributes whose value cannot be set are dim. Help text is
shown for each attribute. Select an attribute by double-clicking on it
or by selecting it and then pressing . A ring control at the top of the
dialog box allows you to see all IVI attributes or only the attributes
of the ViInt32 type. If you choose to see all IVI attributes, the data
types appear to the right of the attribute names in the list box. The
data types that are not consistent with this function are dim. If you
select an attribute data type that is dim, LabWindows/CVI transfers you
to the function panel for the corresponding function that is consistent
with the data type. - If you want to enter a variable name, press to
change this ring control to a manual input box. - If the attribute in
this ring control has constants as valid values, you can view the
constants by moving to the Attribute Value control and pressing .
''',
},
            },
            {
                'direction': 'out',
                'name': 'attributeValue',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Returns the current value of the attribute. Pass the address of a
ViBoolean variable. From the function panel window, you can use this
control as follows. - If the attribute currently showing in the
Attribute ID ring control has constants as valid values, you can view a
list of the constants by pressing on this control. Select a value by
double-clicking on it or by selecting it and then pressing .
''',
},
            },
        ],
'documentation': {
'description': '''
This function queries the value of a ViBoolean attribute. You can use
this function to get the values of instrument specific attributes and
inherent IVI attributes. If the attribute represents an instrument
state, this function performs instrument I/O in the following cases: -
State caching is disabled for the entire session or for the particular
attribute. - State caching is enabled and the currently cached value is
invalid.
''',
},
    },
    'GetAttributeViInt32': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Some attributes are unique per channel. For these, pass the name of the
channel. Other attributes are unique per switch device. Pass VI\_NULL or
an empty string for this parameter. Default Value: ""
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': '''
Pass the ID of an attribute. From the function panel window, you can use
this control as follows. - Click on the control or press , , or , to
display a dialog box containing a hierarchical list of the available
attributes. Attributes whose value cannot be set are dim. Help text is
shown for each attribute. Select an attribute by double-clicking on it
or by selecting it and then pressing . A ring control at the top of the
dialog box allows you to see all IVI attributes or only the attributes
of the ViInt32 type. If you choose to see all IVI attributes, the data
types appear to the right of the attribute names in the list box. The
data types that are not consistent with this function are dim. If you
select an attribute data type that is dim, LabWindows/CVI transfers you
to the function panel for the corresponding function that is consistent
with the data type. - If you want to enter a variable name, press to
change this ring control to a manual input box. - If the attribute in
this ring control has constants as valid values, you can view the
constants by moving to the Attribute Value control and pressing .
''',
},
            },
            {
                'direction': 'out',
                'name': 'attributeValue',
                'type': 'ViInt32',
'documentation': {
'description': '''
Returns the current value of the attribute. Pass the address of a
ViInt32 variable. From the function panel window, you can use this
control as follows. - If the attribute currently showing in the
Attribute ID ring control has constants as valid values, you can view a
list of the constants by pressing on this control. Select a value by
double-clicking on it or by selecting it and then pressing .
''',
},
            },
        ],
'documentation': {
'description': '''
This function queries the value of a ViInt32 attribute. You can use this
function to get the values of instrument specific attributes and
inherent IVI attributes. If the attribute represents an instrument
state, this function performs instrument I/O in the following cases: -
State caching is disabled for the entire session or for the particular
attribute. - State caching is enabled and the currently cached value is
invalid.
''',
},
    },
    'GetAttributeViReal64': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Some attributes are unique per channel. For these, pass the name of the
channel. Other attributes are unique per switch device. Pass VI\_NULL or
an empty string for this parameter. Default Value: ""
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': '''
Pass the ID of an attribute. From the function panel window, you can use
this control as follows. - Click on the control or press , , or , to
display a dialog box containing a hierarchical list of the available
attributes. Attributes whose value cannot be set are dim. Help text is
shown for each attribute. Select an attribute by double-clicking on it
or by selecting it and then pressing . A ring control at the top of the
dialog box allows you to see all IVI attributes or only the attributes
of the ViInt32 type. If you choose to see all IVI attributes, the data
types appear to the right of the attribute names in the list box. The
data types that are not consistent with this function are dim. If you
select an attribute data type that is dim, LabWindows/CVI transfers you
to the function panel for the corresponding function that is consistent
with the data type. - If you want to enter a variable name, press to
change this ring control to a manual input box. - If the attribute in
this ring control has constants as valid values, you can view the
constants by moving to the Attribute Value control and pressing .
''',
},
            },
            {
                'direction': 'out',
                'name': 'attributeValue',
                'type': 'ViReal64',
'documentation': {
'description': '''
Returns the current value of the attribute. Pass the address of a
ViReal64 variable. From the function panel window, you can use this
control as follows. - If the attribute currently showing in the
Attribute ID ring control has constants as valid values, you can view a
list of the constants by pressing on this control. Select a value by
double-clicking on it or by selecting it and then pressing .
''',
},
            },
        ],
'documentation': {
'description': '''
This function queries the value of a ViReal64 attribute. You can use
this function to get the values of instrument specific attributes and
inherent IVI attributes. If the attribute represents an instrument
state, this function performs instrument I/O in the following cases: -
State caching is disabled for the entire session or for the particular
attribute. - State caching is enabled and the currently cached value is
invalid.
''',
},
    },
    'GetAttributeViSession': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Some attributes are unique per channel. For these, pass the name of the
channel. Other attributes are unique per switch device. Pass VI\_NULL or
an empty string for this parameter. Default Value: ""
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': '''
Pass the ID of an attribute. From the function panel window, you can use
this control as follows. - Click on the control or press , , or , to
display a dialog box containing a hierarchical list of the available
attributes. Attributes whose value cannot be set are dim. Help text is
shown for each attribute. Select an attribute by double-clicking on it
or by selecting it and then pressing . A ring control at the top of the
dialog box allows you to see all IVI attributes or only the attributes
of the ViInt32 type. If you choose to see all IVI attributes, the data
types appear to the right of the attribute names in the list box. The
data types that are not consistent with this function are dim. If you
select an attribute data type that is dim, LabWindows/CVI transfers you
to the function panel for the corresponding function that is consistent
with the data type. - If you want to enter a variable name, press to
change this ring control to a manual input box. - If the attribute in
this ring control has constants as valid values, you can view the
constants by moving to the Attribute Value control and pressing .
''',
},
            },
            {
                'direction': 'out',
                'name': 'attributeValue',
                'type': 'ViSession',
'documentation': {
'description': '''
Returns the current value of the attribute. Pass the address of a
ViSession variable. From the function panel window, you can use this
control as follows. - If the attribute currently showing in the
Attribute ID ring control has constants as valid values, you can view a
list of the constants by pressing on this control. Select a value by
double-clicking on it or by selecting it and then pressing .
''',
},
            },
        ],
'documentation': {
'description': '''
This function queries the value of a ViSession attribute. You can use
this function to get the values of instrument specific attributes and
inherent IVI attributes. If the attribute represents an instrument
state, this function performs instrument I/O in the following cases: -
State caching is disabled for the entire session or for the particular
attribute. - State caching is enabled and the currently cached value is
invalid.
''',
},
    },
    'GetAttributeViString': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Some attributes are unique per channel. For these, pass the name of the
channel. Other attributes are unique per switch device. Pass VI\_NULL or
an empty string for this parameter. Default Value: ""
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': '''
Pass the ID of an attribute. From the function panel window, you can use
this control as follows. - Click on the control or press , , or , to
display a dialog box containing a hierarchical list of the available
attributes. Attributes whose value cannot be set are dim. Help text is
shown for each attribute. Select an attribute by double-clicking on it
or by selecting it and then pressing . A ring control at the top of the
dialog box allows you to see all IVI attributes or only the attributes
of the ViInt32 type. If you choose to see all IVI attributes, the data
types appear to the right of the attribute names in the list box. The
data types that are not consistent with this function are dim. If you
select an attribute data type that is dim, LabWindows/CVI transfers you
to the function panel for the corresponding function that is consistent
with the data type. - If you want to enter a variable name, press to
change this ring control to a manual input box. - If the attribute in
this ring control has constants as valid values, you can view the
constants by moving to the Attribute Value control and pressing .
''',
},
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'ViInt32',
'documentation': {
'description': '''
Pass the number of bytes in the ViChar array you specify for the
Attribute Value parameter. If the current value of the attribute,
including the terminating NUL byte, contains more bytes that you
indicate in this parameter, the function copies Array Size-1 bytes into
the buffer, places an ASCII NUL byte at the end of the buffer, and
returns the array size you must pass to get the entire value. For
example, if the value is "123456" and the Array Size is 4, the function
places "123" into the buffer and returns 7. If you pass a negative
number, the function copies the value to the buffer regardless of the
number of bytes in the value. If you pass 0, you can pass VI\_NULL for
the Attribute Value buffer parameter. Default Value:512
''',
},
            },
            {
                'direction': 'out',
                'name': 'attributeValue',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The buffer in which the function returns the current value of the
attribute. The buffer must be of type ViChar and have at least as many
bytes as indicated in the Array Size parameter. If the current value of
the attribute, including the terminating NUL byte, contains more bytes
that you indicate in this parameter, the function copies Array Size-1
bytes into the buffer, places an ASCII NUL byte at the end of the
buffer, and returns the array size you must pass to get the entire
value. For example, if the value is "123456" and the Array Size is 4,
the function places "123" into the buffer and returns 7. If you specify
0 for the Array Size parameter, you can pass VI\_NULL for this
parameter. From the function panel window, you can use this control as
follows. - If the attribute currently showing in the Attribute ID ring
control has constants as valid values, you can view a list of the
constants by pressing on this control. Select a value by double-clicking
on it or by selecting it and then pressing .
''',
},
            },
        ],
'documentation': {
'description': '''
This function queries the value of a ViString attribute. You can use
this function to get the values of instrument specific attributes and
inherent IVI attributes. If the attribute represents an instrument
state, this function performs instrument I/O in the following cases: -
State caching is disabled for the entire session or for the particular
attribute. - State caching is enabled and the currently cached value is
invalid. You must provide a ViChar array to serve as a buffer for the
value. You pass the number of bytes in the buffer as the Array Size
parameter. If the current value of the attribute, including the
terminating NULL byte, is larger than the size you indicate in the Array
Size parameter, the function copies Array Size-1 bytes into the buffer,
places an ASCII NULL byte at the end of the buffer, and returns the
array size you must pass to get the entire value. For example, if the
value is "123456" and the Array Size is 4, the function places "123"
into the buffer and returns 7. If you want to call this function just to
get the required array size, you can pass 0 for the Array Size and
VI\_NULL for the Attribute Value buffer. If you want the function to
fill in the buffer regardless of the number of bytes in the value, pass
a negative number for the Array Size parameter.
''',
},
    },
    'GetChannelName': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Index',
                'type': 'ViInt32',
'documentation': {
'description': '''
A 1-based index into the channel table. Default value: 1 Maximum value:
Value of Channel Count attribute.
''',
},
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32',
'documentation': {
'description': '''
Pass the number of bytes in the ViChar array you specify for the Channel
Name Buffer parameter. If the channel name string, including the
terminating NUL byte, contains more bytes than you indicate in this
parameter, the function copies Buffer Size - 1 bytes into the buffer,
places an ASCII NUL byte at the end of the buffer, and returns the
buffer size you must pass to get the entire value. For example, if the
value is "123456" and the Buffer Size is 4, the function places "123"
into the buffer and returns 7. If you pass a negative number, the
function copies the value to the buffer regardless of the number of
bytes in the value. If you pass 0, you can pass VI\_NULL for the
Coercion Record buffer parameter. Default Value: None
''',
},
            },
            {
                'direction': 'out',
                'name': 'channelNameBuffer',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Returns the channel name that is in the channel table at the index you
specify.
''',
},
            },
        ],
'documentation': {
'description': '''
Returns the channel string that is in the channel table at the specified
index. Use niSwitch\_GetChannelName in a For Loop to get a complete list
of valid channel names for the switch module. Use the Channel Count
attribute to determine the number of channels.
''',
},
    },
    'GetError': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
            {
                'direction': 'out',
                'name': 'Code',
                'type': 'ViStatus',
'documentation': {
'description': '''
Returns the error code for the session or execution thread. If you pass
0 for the Buffer Size, you can pass VI\_NULL for this parameter.
''',
},
            },
            {
                'direction': 'in',
                'name': 'BufferSize',
                'type': 'ViInt32',
'documentation': {
'description': '''
Pass the number of bytes in the ViChar array you specify for the
Description parameter. If the error description, including the
terminating NUL byte, contains more bytes than you indicate in this
parameter, the function copies buffer\_size - 1 bytes into the buffer,
places an ASCII NUL byte at the end of the buffer, and returns the
buffer size you must pass to get the entire value. For example, if the
value is "123456" and the Buffer Size is 4, the function places "123"
into the buffer and returns 7. If you pass a negative number, the
function copies the value to the buffer regardless of the number of
bytes in the value. If you pass 0, you can pass VI\_NULL for the
Description buffer parameter. Default Value: None
''',
},
            },
            {
                'direction': 'out',
                'name': 'Description',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Returns the error description for the IVI session or execution thread.
If there is no description, the function returns an empty string. The
buffer must contain at least as many elements as the value you specify
with the Buffer Size parameter. If the error description, including the
terminating NUL byte, contains more bytes than you indicate with the
Buffer Size parameter, the function copies Buffer Size - 1 bytes into
the buffer, places an ASCII NUL byte at the end of the buffer, and
returns the buffer size you must pass to get the entire value. For
example, if the value is "123456" and the Buffer Size is 4, the function
places "123" into the buffer and returns 7. If you pass 0 for the Buffer
Size, you can pass VI\_NULL for this parameter.
''',
},
            },
        ],
'documentation': {
'description': '''
This function retrieves and then clears the IVI error information for
the session or the current execution thread. One exception exists: If
the buffer_size parameter is 0, the function does not clear the error
information. By passing 0 for the buffer size, the caller can ascertain
the buffer size required to get the entire error description string and
then call the function again with a sufficiently large buffer. If the
user specifies a valid IVI session for the InstrumentHandle parameter,
Get Error retrieves and then clears the error information for the
session. If the user passes VI\_NULL for the InstrumentHandle parameter,
this function retrieves and then clears the error information for the
current execution thread. If the InstrumentHandle parameter is an
invalid session, the function does nothing and returns an error.
Normally, the error information describes the first error that occurred
since the user last called niSwitch\_GetError or niSwitch\_ClearError.
''',
},
    },
    'GetNextCoercionRecord': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32',
'documentation': {
'description': '''
Pass the number of bytes in the ViChar array you specify for the
Coercion Record parameter. If the next coercion record string, including
the terminating NUL byte, contains more bytes than you indicate in this
parameter, the function copies Buffer Size - 1 bytes into the buffer,
places an ASCII NUL byte at the end of the buffer, and returns the
buffer size you must pass to get the entire value. For example, if the
value is "123456" and the Buffer Size is 4, the function places "123"
into the buffer and returns 7. If you pass a negative number, the
function copies the value to the buffer regardless of the number of
bytes in the value. If you pass 0, you can pass VI\_NULL for the
Coercion Record buffer parameter. Default Value: None
''',
},
            },
            {
                'direction': 'out',
                'name': 'coercionRecord',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Returns the next coercion record for the IVI session. If there are no
coercion records, the function returns an empty string. The buffer must
contain at least as many elements as the value you specify with the
Buffer Size parameter. If the next coercion record string, including the
terminating NUL byte, contains more bytes than you indicate with the
Buffer Size parameter, the function copies Buffer Size - 1 bytes into
the buffer, places an ASCII NUL byte at the end of the buffer, and
returns the buffer size you must pass to get the entire value. For
example, if the value is "123456" and the Buffer Size is 4, the function
places "123" into the buffer and returns 7. This parameter returns an
empty string if no coercion records remain for the session.
''',
},
            },
        ],
'documentation': {
'description': '''
This function returns the coercion information associated with the IVI
session. This function retrieves and clears the oldest instance in which
the instrument driver coerced a value you specified to another value. If
you set the NISWITCH\_ATTR\_RECORD\_COERCIONS attribute to VI\_TRUE, the
instrument driver keeps a list of all coercions it makes on ViInt32 or
ViReal64 values you pass to instrument driver functions. You use this
function to retrieve information from that list. If the next coercion
record string, including the terminating NUL byte, contains more bytes
than you indicate in this parameter, the function copies Buffer Size - 1
bytes into the buffer, places an ASCII NUL byte at the end of the
buffer, and returns the buffer size you must pass to get the entire
value. For example, if the value is "123456" and the Buffer Size is 4,
the function places "123" into the buffer and returns 7. If you pass a
negative number, the function copies the value to the buffer regardless
of the number of bytes in the value. If you pass 0, you can pass
VI\_NULL for the Coercion Record buffer parameter. The function returns
an empty string in the Coercion Record parameter if no coercion records
remain for the session.
''',
},
    },
    'GetNextInterchangeWarning': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32',
'documentation': {
'description': '''
Pass the number of bytes in the ViChar array you specify for the
Interchange Warning parameter. If the next interchangeability warning
string, including the terminating NUL byte, contains more bytes than you
indicate in this parameter, the function copies Buffer Size - 1 bytes
into the buffer, places an ASCII NUL byte at the end of the buffer, and
returns the buffer size you must pass to get the entire value. For
example, if the value is "123456" and the Buffer Size is 4, the function
places "123" into the buffer and returns 7. If you pass a negative
number, the function copies the value to the buffer regardless of the
number of bytes in the value. If you pass 0, you can pass VI\_NULL for
the Interchange Warning buffer parameter. Default Value: None
''',
},
            },
            {
                'direction': 'out',
                'name': 'interchangeWarning',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Returns the next interchange warning for the IVI session. If there are
no interchange warnings, the function returns an empty string. The
buffer must contain at least as many elements as the value you specify
with the Buffer Size parameter. If the next interchangeability warning
string, including the terminating NUL byte, contains more bytes than you
indicate with the Buffer Size parameter, the function copies Buffer Size
- 1 bytes into the buffer, places an ASCII NUL byte at the end of the
buffer, and returns the buffer size you must pass to get the entire
value. For example, if the value is "123456" and the Buffer Size is 4,
the function places "123" into the buffer and returns 7. This parameter
returns an empty string if no interchangeability warnings remain for the
session.
''',
},
            },
        ],
'documentation': {
'description': '''
This function returns the interchangeability warnings associated with
the IVI session. It retrieves and clears the oldest instance in which
the class driver recorded an interchangeability warning.
Interchangeability warnings indicate that using your application with a
different instrument might cause different behavior. You use this
function to retrieve interchangeability warnings. The driver performs
interchangeability checking when the NISWITCH\_ATTR\_INTERCHANGE\_CHECK
attribute is set to VI\_TRUE. The function returns an empty string in
the Interchange Warning parameter if no interchangeability warnings
remain for the session. In general, the instrument driver generates
interchangeability warnings when an attribute that affects the behavior
of the instrument is in a state that you did not specify.
''',
},
    },
    'GetPath': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channel1',
                'type': 'ViConstString',
'documentation': {
'description': '''
Input one of the channel names of the desired path. Pass the other
channel name as the channel 2 parameter. Refer to Devices Overview for
valid channel names for the switch module. Examples of valid channel
names: ch0, com0, ab0, r1, c2, cjtemp Default value: ""
''',
},
            },
            {
                'direction': 'in',
                'name': 'channel2',
                'type': 'ViConstString',
'documentation': {
'description': '''
Input one of the channel names of the desired path. Pass the other
channel name as the channel 1 parameter. Refer to Devices Overview for
valid channel names for the switch module. Examples of valid channel
names: ch0, com0, ab0, r1, c2, cjtemp Default value: ""
''',
},
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32',
'documentation': {
'description': '''
Pass the number of bytes in the ViChar array you specify for the Path
List parameter. If the current value of the attribute, including the
terminating NULL byte, contains more bytes that you indicate in this
parameter, the function copies Buffer Size - 1 bytes into the buffer,
places an ASCII NULL byte at the end of the buffer, and returns the
buffer size you must pass to get the entire value. For example, if the
value is "R1->C1" and the Buffer Size is 4, the function places "R1-"
into the buffer and returns 7. If you pass 0, you can pass VI\_NULL for
the Path parameter. This enables you to find out the path size and to
allocate the buffer of the appropriate size before calling this function
again.
''',
},
            },
            {
                'direction': 'out',
                'name': 'Path',
                'type': 'ViChar[]',
'documentation': {
'description': '''
A string composed of comma-separated paths between channel 1 and channel
2. The first and last names in the path are the endpoints of the path.
All other channels in the path are configuration channels. Examples of
returned paths: ch0->com0, com0->ab0
''',
},
            },
        ],
'documentation': {
'description': '''
Returns a string that identifies the explicit path created with
niSwitch\_Connect. Pass this string to niSwitch\_SetPath to establish
the exact same path in future connections. In some cases, multiple paths
are available between two channels. When you call niSwitch\_Connect, the
driver selects an available path. With niSwitch\_Connect, there is no
guarantee that the driver selected path will always be the same path
through the switch module. niSwitch\_GetPath only returns those paths
explicitly created by niSwitch Connect Channels or niSwitch\_SetPath.
For example, if you connect channels CH1 and CH3,and then channels CH2
and CH3, an explicit path between channels CH1 and CH2 does not exist an
error is returned
''',
},
    },
    'GetRelayCount': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
            {
                'direction': 'in',
                'name': 'relayName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Name of the relay. Default value: None Examples of valid relay names:
ch0, ab0, 1wire, hlselect Refer to Devices Overview for a list of valid
relay names for the switch module.
''',
},
            },
            {
                'direction': 'out',
                'name': 'relayCount',
                'type': 'ViInt32',
'documentation': {
'description': 'The number of relay cycles.',
},
            },
        ],
'documentation': {
'description': '''
Returns the number of times the relay has changed from Closed to Open.
Relay count is useful for tracking relay lifetime and usage. Call
niSwitch\_WaitForDebounce before niSwitch\_GetRelayCount to ensure an
accurate count. Refer to the Relay Count topic in the NI Switches Help
to determine if the switch module supports relay counting.
''',
},
    },
    'GetRelayName': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Index',
                'type': 'ViInt32',
'documentation': {
'description': '''
A 1-based index into the channel table. Default value: 1 Maximum value:
Value of Channel Count attribute.
''',
},
            },
            {
                'direction': 'in',
                'name': 'relayNameBufferSize',
                'type': 'ViInt32',
'documentation': {
'description': '''
Pass the number of bytes in the ViChar array you specify for the Relay
Name Buffer parameter. If the relay name string, including the
terminating NUL byte, contains more bytes than you indicate in this
parameter, the function copies Buffer Size - 1 bytes into the buffer,
places an ASCII NUL byte at the end of the buffer, and returns the
buffer size you must pass to get the entire value. For example, if the
value is "123456" and the Buffer Size is 4, the function places "123"
into the buffer and returns 7. If you pass a negative number, the
function copies the value to the buffer regardless of the number of
bytes in the value. If you pass 0, you can pass VI\_NULL for the
Coercion Record buffer parameter. Default Value: None
''',
},
            },
            {
                'direction': 'out',
                'name': 'relayNameBuffer',
                'type': 'ViChar[]',
'documentation': {
'description': 'Returns the relay name for the index you specify.',
},
            },
        ],
'documentation': {
'description': '''
Returns the relay name string that is in the relay list at the specified
index. Use niSwitch\_GetRelayName in a For Loop to get a complete list
of valid relay names for the switch module. Use the Number of Relays
attribute to determine the number of relays.
''',
},
    },
    'GetRelayPosition': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
            {
                'direction': 'in',
                'name': 'relayName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Name of the relay. Default value: None Examples of valid relay names:
ch0, ab0, 1wire, hlselect Refer to Devices Overview for a list of valid
relay names for the switch module.
''',
},
            },
            {
                'direction': 'out',
                'name': 'relayPosition',
                'type': 'ViInt32',
'documentation': {
'description': '''
Indicates whether the relay is open or closed. NISWITCH\_VAL\_OPEN 10
NIWITCH\_VAL\_CLOSED 11
''',
},
            },
        ],
'documentation': {
'description': '''
Returns the relay position for the relay specified in the Relay Name
parameter.
''',
},
    },
    'InitWithOptions': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'resourceName',
                'type': 'ViRsrc',
'documentation': {
'description': '''
Resource name of the switch module to initialize. Default value: None
Syntax: Optional fields are shown in square brackets ([]). Configured in
MAX Under Valid Syntax Devices and Interfaces DeviceName Traditional
NI-DAQ Devices SCXI[chassis ID]::slot number PXI System PXI[bus
number]::device number TIP: IVI logical names are also valid for the
resource name. Default values for optional fields: chassis ID = 1 bus
number = 0 Example resource names: Resource Name Description SC1Mod3
NI-DAQmx module in chassis "SC1" slot 3 MySwitch NI-DAQmx module renamed
to "MySwitch" SCXI1::3 Traditional NI-DAQ module in chassis 1, slot 3
SCXI::3 Traditional NI-DAQ module in chassis 1, slot 3 PXI0::16 PXI bus
0, device number 16 PXI::16 PXI bus 0, device number 16
''',
},
            },
            {
                'direction': 'in',
                'name': 'idQuery',
                'type': 'ViBoolean',
'documentation': {
'description': '''
This parameter is ignored. Because NI-SWITCH supports multiple switch
modules, it always queries the switch device to determine which device
is installed. For this reason, this VI may return
NISWITCH\_ERROR\_FAIL\_ID\_QUERY even if this parameter is set to
VI\_FALSE. Valid Values: VI\_TRUE - (Default Value) VI\_FALSE -
Currently unsupported.
''',
},
            },
            {
                'direction': 'in',
                'name': 'resetDevice',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether to reset the switch module during the initialization
process. Valid Values: VI\_TRUE - Reset Device (Default Value) VI\_FALSE
- Currently unsupported. The device will not reset.
''',
},
            },
            {
                'direction': 'in',
                'name': 'optionsString',
                'type': 'ViConstString',
'documentation': {
'description': '''
Sets initial values of certain attributes for the NI-SWITCH session.
Default value: Simulate=0,RangeCheck=1,DriverSetup=topology:1127/2-Wire
32x1 Mux The following table lists the attribute string names you can
use: RangeCheck 1 NISWITCH\_ATTR\_RANGE\_CHECK QueryInstrStatus 1
NISWITCH\_ATTR\_QUERY\_INSTRUMENT\_STATUS Cache 1 NISWITCH\_ATTR\_CACHE
Simulate 0 NISWITCH\_ATTR\_SIMULATE RecordCoercions 0
NISWITCH\_ATTR\_RECORD\_COERCIONS DriverSetup topology 1127/2-Wire 32x1
Mux The format of the option string is, "AttributeStringName=Value"
where AttributeStringName is the string name of the attribute shown
above and Value is the value to which the attribute will be set. To set
multiple attributes, separate assignments with a comma. If you pass an
empty string for this parameter, the NI-SWITCH session uses the default
values for the attributes. You can override the default values by
explicitly assigning a value. You do not have to specify all of the
available attributes. If you do not specify an attribute, its default
value is used. Use the DriverSetup attribute to set the topology or the
resource type (DAQmx or Traditional DAQ) of the switch module. This
attribute can contain config token/value pairs within it.
DriverSetup=[config token]:[value];[config token 2]:[value 2] Valid
Config Tokens and Values: Config Token topology - Refer to Device book
for your switch in the NI Switches Help for valid values. You can also
set the value of the topology config token to Configured Topology to
specify the last topology that was configured for the device in MAX.
Default: MAX configured topology for each device. resourcetype - "daqmx"
for devices configured under NI-DAQmx Devices in MAX or "legacy" for
devices configured under Traditional NI-DAQ Devices in MAX. Default:
daqmx For example, use the following string to set an NI SCXI-1127 as a
2-wire 32x1 multiplexer configured in MAX under DAQmx Devices:
"DriverSetup=topology:1127/2-Wire 32x1 Mux;resourcetype:daqmx" The
DriverSetup string is particularly important when using NI-SWITCH
through the IviSwitch class driver. To enable simulation, set simulate
equal to 1 and specify the switch module and topology of the switch
module to simulate. The following string enables simulation for an
SCXI-1127 configured as a 2-wire 32x1 multiplexer. "Simulate=1,
DriverSetup=topology:1127/2-Wire 32x1 Mux" If simulate is set to 1 and
the DriverSetup string specifies a topology, the topology is used to
determine which device to simulate. If the DriverSetup string does not
specify a topology, the device specified in resource name is simulated.
''',
},
            },
            {
                'direction': 'out',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
        ],
'documentation': {
'description': '''
Returns a session handle used to identify the switch module in all
subsequent instrument driver calls and optionally sets the initial state
of the session. niSwitch\_InitWithOptions creates a new IVI instrument
driver session for the switch module specified in the resource name
parameter. If multiple topologies are valid for that device, the driver
uses the default topology specified in MAX. The topology is also
configurable in the options string parameter. Note: When initializing an
NI SwitchBlock device with topology, you must specify the topology
created when you configured the device in MAX, using either Configured
Topology or the topology string of the device. Refer to the Initializing
with Topology for NI SwitchBlock Devices topic in the NI Switches Help
for information about determining the topology string of an NI
SwitchBlock device. By default, the switch module is reset to a known
state. Enable simulation in the options string parameter. An error is
returned if a session to the specified resource exists in another
process. The same session is returned if niSwitch\_InitWithOptions is
called twice in the same process for the same resource with the same
topology.
''',
},
    },
    'InitWithTopology': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'resourceName',
                'type': 'ViRsrc',
'documentation': {
'description': '''
Resource name of the switch module to initialize. Default value: None
Syntax: Optional fields are shown in square brackets ([]). Configured in
MAX Under Valid Syntax Devices and Interfaces DeviceName Traditional
NI-DAQ Devices SCXI[chassis ID]::slot number PXI System PXI[bus
number]::device number TIP: IVI logical names are also valid for the
resource name. Default values for optional fields: chassis ID = 1 bus
number = 0 Example resource names: Resource Name Description SC1Mod3
NI-DAQmx module in chassis "SC1" slot 3 MySwitch NI-DAQmx module renamed
to "MySwitch" SCXI1::3 Traditional NI-DAQ module in chassis 1, slot 3
SCXI::3 Traditional NI-DAQ module in chassis 1, slot 3 PXI0::16 PXI bus
0, device number 16 PXI::16 PXI bus 0, device number 16
''',
},
            },
            {
                'direction': 'in',
                'name': 'Topology',
                'type': 'ViConstString',
'documentation': {
'description': '''
Pass the topology name you want to use for the switch you specify with
Resource Name parameter. You can also pass
NISWITCH\_TOPOLOGY\_CONFIGURED\_TOPOLOGY to use the last topology that
was configured for the device in MAX. Default Value:
NISWITCH\_TOPOLOGY\_CONFIGURED\_TOPOLOGY Valid Values:
NISWITCH\_TOPOLOGY\_1127\_1\_WIRE\_64X1\_MUX
NISWITCH\_TOPOLOGY\_1127\_2\_WIRE\_32X1\_MUX
NISWITCH\_TOPOLOGY\_1127\_2\_WIRE\_4X8\_MATRIX
NISWITCH\_TOPOLOGY\_1127\_4\_WIRE\_16X1\_MUX
NISWITCH\_TOPOLOGY\_1127\_INDEPENDENT
NISWITCH\_TOPOLOGY\_1128\_1\_WIRE\_64X1\_MUX
NISWITCH\_TOPOLOGY\_1128\_2\_WIRE\_32X1\_MUX
NISWITCH\_TOPOLOGY\_1128\_2\_WIRE\_4X8\_MATRIX
NISWITCH\_TOPOLOGY\_1128\_4\_WIRE\_16X1\_MUX
NISWITCH\_TOPOLOGY\_1128\_INDEPENDENT
NISWITCH\_TOPOLOGY\_1129\_2\_WIRE\_16X16\_MATRIX
NISWITCH\_TOPOLOGY\_1129\_2\_WIRE\_8X32\_MATRIX
NISWITCH\_TOPOLOGY\_1129\_2\_WIRE\_4X64\_MATRIX
NISWITCH\_TOPOLOGY\_1129\_2\_WIRE\_DUAL\_8X16\_MATRIX
NISWITCH\_TOPOLOGY\_1129\_2\_WIRE\_DUAL\_4X32\_MATRIX
NISWITCH\_TOPOLOGY\_1129\_2\_WIRE\_QUAD\_4X16\_MATRIX
NISWITCH\_TOPOLOGY\_1130\_1\_WIRE\_256X1\_MUX
NISWITCH\_TOPOLOGY\_1130\_1\_WIRE\_DUAL\_128X1\_MUX
NISWITCH\_TOPOLOGY\_1130\_1\_WIRE\_4X64\_MATRIX
NISWITCH\_TOPOLOGY\_1130\_1\_WIRE\_8x32\_MATRIX
NISWITCH\_TOPOLOGY\_1130\_1\_WIRE\_OCTAL\_32X1\_MUX
NISWITCH\_TOPOLOGY\_1130\_1\_WIRE\_QUAD\_64X1\_MUX
NISWITCH\_TOPOLOGY\_1130\_1\_WIRE\_SIXTEEN\_16X1\_MUX
NISWITCH\_TOPOLOGY\_1130\_2\_WIRE\_4X32\_MATRIX
NISWITCH\_TOPOLOGY\_1130\_2\_WIRE\_128X1\_MUX
NISWITCH\_TOPOLOGY\_1130\_2\_WIRE\_OCTAL\_16X1\_MUX
NISWITCH\_TOPOLOGY\_1130\_2\_WIRE\_QUAD\_32X1\_MUX
NISWITCH\_TOPOLOGY\_1130\_4\_WIRE\_64X1\_MUX
NISWITCH\_TOPOLOGY\_1130\_4\_WIRE\_QUAD\_16X1\_MUX
NISWITCH\_TOPOLOGY\_1130\_INDEPENDENT NISWITCH\_TOPOLOGY\_1160\_16\_SPDT
NISWITCH\_TOPOLOGY\_1161\_8\_SPDT
NISWITCH\_TOPOLOGY\_1163R\_OCTAL\_4X1\_MUX
NISWITCH\_TOPOLOGY\_1166\_16\_DPDT NISWITCH\_TOPOLOGY\_1166\_32\_SPDT
NISWITCH\_TOPOLOGY\_1167\_INDEPENDENT
NISWITCH\_TOPOLOGY\_1169\_100\_SPST NISWITCH\_TOPOLOGY\_1169\_50\_DPST
NISWITCH\_TOPOLOGY\_1175\_1\_WIRE\_196X1\_MUX
NISWITCH\_TOPOLOGY\_1175\_2\_WIRE\_98X1\_MUX
NISWITCH\_TOPOLOGY\_1175\_2\_WIRE\_95X1\_MUX
NISWITCH\_TOPOLOGY\_1190\_QUAD\_4X1\_MUX
NISWITCH\_TOPOLOGY\_1191\_QUAD\_4X1\_MUX
NISWITCH\_TOPOLOGY\_1192\_8\_SPDT NISWITCH\_TOPOLOGY\_1193\_32X1\_MUX
NISWITCH\_TOPOLOGY\_1193\_16X1\_TERMINATED\_MUX
NISWITCH\_TOPOLOGY\_1193\_DUAL\_16X1\_MUX
NISWITCH\_TOPOLOGY\_1193\_DUAL\_8X1\_TERMINATED\_MUX
NISWITCH\_TOPOLOGY\_1193\_QUAD\_8X1\_MUX
NISWITCH\_TOPOLOGY\_1193\_QUAD\_4X1\_TERMINATED\_MUX
NISWITCH\_TOPOLOGY\_1193\_INDEPENDENT
NISWITCH\_TOPOLOGY\_1194\_QUAD\_4X1\_MUX
NISWITCH\_TOPOLOGY\_1195\_QUAD\_4X1\_MUX
NISWITCH\_TOPOLOGY\_2501\_1\_WIRE\_48X1\_MUX
NISWITCH\_TOPOLOGY\_2501\_1\_WIRE\_48X1\_AMPLIFIED\_MUX
NISWITCH\_TOPOLOGY\_2501\_2\_WIRE\_24X1\_MUX
NISWITCH\_TOPOLOGY\_2501\_2\_WIRE\_24X1\_AMPLIFIED\_MUX
NISWITCH\_TOPOLOGY\_2501\_2\_WIRE\_DUAL\_12X1\_MUX
NISWITCH\_TOPOLOGY\_2501\_2\_WIRE\_QUAD\_6X1\_MUX
NISWITCH\_TOPOLOGY\_2501\_2\_WIRE\_4X6\_MATRIX
NISWITCH\_TOPOLOGY\_2501\_4\_WIRE\_12X1\_MUX
NISWITCH\_TOPOLOGY\_2503\_1\_WIRE\_48X1\_MUX
NISWITCH\_TOPOLOGY\_2503\_2\_WIRE\_24X1\_MUX
NISWITCH\_TOPOLOGY\_2503\_2\_WIRE\_DUAL\_12X1\_MUX
NISWITCH\_TOPOLOGY\_2503\_2\_WIRE\_QUAD\_6X1\_MUX
NISWITCH\_TOPOLOGY\_2503\_2\_WIRE\_4X6\_MATRIX
NISWITCH\_TOPOLOGY\_2503\_4\_WIRE\_12X1\_MUX
NISWITCH\_TOPOLOGY\_2510\_INDEPENDENT
NISWITCH\_TOPOLOGY\_2512\_INDEPENDENT
NISWITCH\_TOPOLOGY\_2514\_INDEPENDENT
NISWITCH\_TOPOLOGY\_2515\_INDEPENDENT NISWITCH\_TOPOLOGY\_2520\_80\_SPST
NISWITCH\_TOPOLOGY\_2521\_40\_DPST NISWITCH\_TOPOLOGY\_2522\_53\_SPDT
NISWITCH\_TOPOLOGY\_2523\_26\_DPDT
NISWITCH\_TOPOLOGY\_2524\_1\_WIRE\_128X1\_MUX
NISWITCH\_TOPOLOGY\_2524\_1\_WIRE\_DUAL\_64X1\_MUX
NISWITCH\_TOPOLOGY\_2524\_1\_WIRE\_QUAD\_32X1\_MUX
NISWITCH\_TOPOLOGY\_2524\_1\_WIRE\_OCTAL\_16X1\_MUX
NISWITCH\_TOPOLOGY\_2524\_1\_WIRE\_SIXTEEN\_8X1\_MUX
NISWITCH\_TOPOLOGY\_2525\_2\_WIRE\_64X1\_MUX
NISWITCH\_TOPOLOGY\_2525\_2\_WIRE\_DUAL\_32X1\_MUX
NISWITCH\_TOPOLOGY\_2525\_2\_WIRE\_QUAD\_16X1\_MUX
NISWITCH\_TOPOLOGY\_2525\_2\_WIRE\_OCTAL\_8X1\_MUX
NISWITCH\_TOPOLOGY\_2525\_2\_WIRE\_SIXTEEN\_4X1\_MUX
NISWITCH\_TOPOLOGY\_2526\_1\_WIRE\_158X1\_MUX
NISWITCH\_TOPOLOGY\_2526\_2\_WIRE\_79X1\_MUX
NISWITCH\_TOPOLOGY\_2527\_1\_WIRE\_64X1\_MUX
NISWITCH\_TOPOLOGY\_2527\_1\_WIRE\_DUAL\_32X1\_MUX
NISWITCH\_TOPOLOGY\_2527\_2\_WIRE\_32X1\_MUX
NISWITCH\_TOPOLOGY\_2527\_2\_WIRE\_DUAL\_16X1\_MUX
NISWITCH\_TOPOLOGY\_2527\_4\_WIRE\_16X1\_MUX
NISWITCH\_TOPOLOGY\_2527\_INDEPENDENT
NISWITCH\_TOPOLOGY\_2529\_2\_WIRE\_DUAL\_4X16\_MATRIX
NISWITCH\_TOPOLOGY\_2529\_2\_WIRE\_8X16\_MATRIX
NISWITCH\_TOPOLOGY\_2529\_2\_WIRE\_4X32\_MATRIX
NISWITCH\_TOPOLOGY\_2530\_1\_WIRE\_128X1\_MUX
NISWITCH\_TOPOLOGY\_2530\_1\_WIRE\_DUAL\_64X1\_MUX
NISWITCH\_TOPOLOGY\_2530\_1\_WIRE\_4x32\_MATRIX
NISWITCH\_TOPOLOGY\_2530\_1\_WIRE\_8x16\_MATRIX
NISWITCH\_TOPOLOGY\_2530\_1\_WIRE\_OCTAL\_16X1\_MUX
NISWITCH\_TOPOLOGY\_2530\_1\_WIRE\_QUAD\_32X1\_MUX
NISWITCH\_TOPOLOGY\_2530\_2\_WIRE\_4x16\_MATRIX
NISWITCH\_TOPOLOGY\_2530\_2\_WIRE\_64X1\_MUX
NISWITCH\_TOPOLOGY\_2530\_2\_WIRE\_DUAL\_32X1\_MUX
NISWITCH\_TOPOLOGY\_2530\_2\_WIRE\_QUAD\_16X1\_MUX
NISWITCH\_TOPOLOGY\_2530\_4\_WIRE\_32X1\_MUX
NISWITCH\_TOPOLOGY\_2530\_4\_WIRE\_DUAL\_16X1\_MUX
NISWITCH\_TOPOLOGY\_2530\_INDEPENDENT
NISWITCH\_TOPOLOGY\_2531\_1\_WIRE\_4X128\_MATRIX
NISWITCH\_TOPOLOGY\_2531\_1\_WIRE\_8X64\_MATRIX
NISWITCH\_TOPOLOGY\_2531\_1\_WIRE\_DUAL\_4X64\_MATRIX
NISWITCH\_TOPOLOGY\_2531\_1\_WIRE\_DUAL\_8X32\_MATRIX
NISWITCH\_TOPOLOGY\_2531\_2\_WIRE\_4X64\_MATRIX
NISWITCH\_TOPOLOGY\_2531\_2\_WIRE\_8X32\_MATRIX
NISWITCH\_TOPOLOGY\_2532\_1\_WIRE\_16X32\_MATRIX
NISWITCH\_TOPOLOGY\_2532\_1\_WIRE\_4X128\_MATRIX
NISWITCH\_TOPOLOGY\_2532\_1\_WIRE\_8X64\_MATRIX
NISWITCH\_TOPOLOGY\_2532\_1\_WIRE\_DUAL\_16X16\_MATRIX
NISWITCH\_TOPOLOGY\_2532\_1\_WIRE\_DUAL\_4X64\_MATRIX
NISWITCH\_TOPOLOGY\_2532\_1\_WIRE\_DUAL\_8X32\_MATRIX
NISWITCH\_TOPOLOGY\_2532\_1\_WIRE\_SIXTEEN\_2X16\_MATRIX
NISWITCH\_TOPOLOGY\_2532\_2\_WIRE\_16X16\_MATRIX
NISWITCH\_TOPOLOGY\_2532\_2\_WIRE\_4X64\_MATRIX
NISWITCH\_TOPOLOGY\_2532\_2\_WIRE\_8X32\_MATRIX
NISWITCH\_TOPOLOGY\_2532\_2\_WIRE\_DUAL\_4X32\_MATRIX
NISWITCH\_TOPOLOGY\_2533\_1\_WIRE\_4X64\_MATRIX
NISWITCH\_TOPOLOGY\_2534\_1\_WIRE\_8X32\_MATRIX
NISWITCH\_TOPOLOGY\_2535\_1\_WIRE\_4X136\_MATRIX
NISWITCH\_TOPOLOGY\_2536\_1\_WIRE\_8X68\_MATRIX
NISWITCH\_TOPOLOGY\_2540\_1\_WIRE\_8X9\_MATRIX
NISWITCH\_TOPOLOGY\_2541\_1\_WIRE\_8X12\_MATRIX
NISWITCH\_TOPOLOGY\_2542\_QUAD\_2X1\_TERMINATED\_MUX
NISWITCH\_TOPOLOGY\_2543\_DUAL\_4X1\_TERMINATED\_MUX
NISWITCH\_TOPOLOGY\_2544\_8X1\_TERMINATED\_MUX
NISWITCH\_TOPOLOGY\_2545\_4X1\_TERMINATED\_MUX
NISWITCH\_TOPOLOGY\_2546\_DUAL\_4X1\_MUX
NISWITCH\_TOPOLOGY\_2547\_8X1\_MUX NISWITCH\_TOPOLOGY\_2548\_4\_SPDT
NISWITCH\_TOPOLOGY\_2549\_TERMINATED\_2\_SPDT
NISWITCH\_TOPOLOGY\_2554\_4X1\_MUX
NISWITCH\_TOPOLOGY\_2555\_4X1\_TERMINATED\_MUX
NISWITCH\_TOPOLOGY\_2556\_DUAL\_4X1\_MUX
NISWITCH\_TOPOLOGY\_2557\_8X1\_MUX NISWITCH\_TOPOLOGY\_2558\_4\_SPDT
NISWITCH\_TOPOLOGY\_2559\_TERMINATED\_2\_SPDT
NISWITCH\_TOPOLOGY\_2564\_16\_SPST NISWITCH\_TOPOLOGY\_2564\_8\_DPST
NISWITCH\_TOPOLOGY\_2565\_16\_SPST NISWITCH\_TOPOLOGY\_2566\_16\_SPDT
NISWITCH\_TOPOLOGY\_2566\_8\_DPDT NISWITCH\_TOPOLOGY\_2567\_INDEPENDENT
NISWITCH\_TOPOLOGY\_2568\_15\_DPST NISWITCH\_TOPOLOGY\_2568\_31\_SPST
NISWITCH\_TOPOLOGY\_2569\_100\_SPST NISWITCH\_TOPOLOGY\_2569\_50\_DPST
NISWITCH\_TOPOLOGY\_2570\_20\_DPDT NISWITCH\_TOPOLOGY\_2570\_40\_SPDT
NISWITCH\_TOPOLOGY\_2571\_66\_SPDT
NISWITCH\_TOPOLOGY\_2575\_1\_WIRE\_196X1\_MUX
NISWITCH\_TOPOLOGY\_2575\_2\_WIRE\_98X1\_MUX
NISWITCH\_TOPOLOGY\_2575\_2\_WIRE\_95X1\_MUX
NISWITCH\_TOPOLOGY\_2576\_2\_WIRE\_64X1\_MUX
NISWITCH\_TOPOLOGY\_2576\_2\_WIRE\_DUAL\_32X1\_MUX
NISWITCH\_TOPOLOGY\_2576\_2\_WIRE\_OCTAL\_8X1\_MUX
NISWITCH\_TOPOLOGY\_2576\_2\_WIRE\_QUAD\_16X1\_MUX
NISWITCH\_TOPOLOGY\_2576\_2\_WIRE\_SIXTEEN\_4X1\_MUX
NISWITCH\_TOPOLOGY\_2576\_INDEPENDENT
NISWITCH\_TOPOLOGY\_2584\_1\_WIRE\_12X1\_MUX
NISWITCH\_TOPOLOGY\_2584\_1\_WIRE\_DUAL\_6X1\_MUX
NISWITCH\_TOPOLOGY\_2584\_2\_WIRE\_6X1\_MUX
NISWITCH\_TOPOLOGY\_2584\_INDEPENDENT
NISWITCH\_TOPOLOGY\_2585\_1\_WIRE\_10X1\_MUX
NISWITCH\_TOPOLOGY\_2586\_10\_SPST NISWITCH\_TOPOLOGY\_2586\_5\_DPST
NISWITCH\_TOPOLOGY\_2590\_4X1\_MUX NISWITCH\_TOPOLOGY\_2591\_4X1\_MUX
NISWITCH\_TOPOLOGY\_2593\_16X1\_MUX
NISWITCH\_TOPOLOGY\_2593\_8X1\_TERMINATED\_MUX
NISWITCH\_TOPOLOGY\_2593\_DUAL\_8X1\_MUX
NISWITCH\_TOPOLOGY\_2593\_DUAL\_4X1\_TERMINATED\_MUX
NISWITCH\_TOPOLOGY\_2593\_INDEPENDENT NISWITCH\_TOPOLOGY\_2594\_4X1\_MUX
NISWITCH\_TOPOLOGY\_2595\_4X1\_MUX
NISWITCH\_TOPOLOGY\_2596\_DUAL\_6X1\_MUX
NISWITCH\_TOPOLOGY\_2597\_6X1\_TERMINATED\_MUX
NISWITCH\_TOPOLOGY\_2598\_DUAL\_TRANSFER
NISWITCH\_TOPOLOGY\_2599\_2\_SPDT NISWITCH\_TOPOLOGY\_2720\_INDEPENDENT
NISWITCH\_TOPOLOGY\_2722\_INDEPENDENT
NISWITCH\_TOPOLOGY\_2725\_INDEPENDENT
NISWITCH\_TOPOLOGY\_2727\_INDEPENDENT
NISWITCH\_TOPOLOGY\_2737\_2\_WIRE\_4X64\_MATRIX
NISWITCH\_TOPOLOGY\_2738\_2\_WIRE\_8X32\_MATRIX
NISWITCH\_TOPOLOGY\_2739\_2\_WIRE\_16X16\_MATRIX
NISWITCH\_TOPOLOGY\_2746\_QUAD\_4X1\_MUX
NISWITCH\_TOPOLOGY\_2747\_DUAL\_8X1\_MUX
NISWITCH\_TOPOLOGY\_2748\_16X1\_MUX
NISWITCH\_TOPOLOGY\_2790\_INDEPENDENT
NISWITCH\_TOPOLOGY\_2796\_DUAL\_6X1\_MUX
NISWITCH\_TOPOLOGY\_2797\_6X1\_TERMINATED\_MUX
NISWITCH\_TOPOLOGY\_2798\_DUAL\_TRANSFER
NISWITCH\_TOPOLOGY\_2799\_2\_SPDT
''',
},
            },
            {
                'direction': 'in',
                'name': 'Simulate',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Enables simulation of the switch module specified in the resource name
parameter. Valid Values: VI\_TRUE - simulate VI\_FALSE - Don't simulate
(Default Value)
''',
},
            },
            {
                'direction': 'in',
                'name': 'resetDevice',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether to reset the switch module during the initialization
process. Valid Values: VI\_TRUE - Reset Device (Default Value) VI\_FALSE
- Currently unsupported. The device will not reset.
''',
},
            },
            {
                'direction': 'out',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
        ],
'documentation': {
'description': '''
Returns a session handle used to identify the switch in all subsequent
instrument driver calls and sets the topology of the switch.
niSwitch\_InitWithTopology creates a new IVI instrument driver session
for the switch specified in the resourceName parameter. The driver uses
the topology specified in the topology parameter and overrides the
topology specified in MAX. Note: When initializing an NI SwitchBlock
device with topology, you must specify the toplogy created when you
configured the device in MAX, using either
NISWITCH\_TOPOLOGY\_CONFIGURED\_TOPOLOGY or the toplogy string of the
device. Refer to the Initializing with Toplogy for NI SwitchBlock
Devices topic in the NI Switches Help for information about determining
the topology string of an NI SwitchBlock device. By default, the switch
is reset to a known state. Enable simulation by specifying the topology
and setting the simulate parameter to VI\_TRUE.
''',
},
    },
    'InitiateScan': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
        ],
'documentation': {
'description': '''
Commits the configured scan list and trigger settings to hardware and
initiates the scan. If niSwitch Commit was called earlier, niSwitch
Initiate Scan only initiates the scan and returns immediately. Once the
scanning operation begins, you cannot perform any other operation other
than GetAttribute, AbortScan, or SendSoftwareTrigger. All other
functions return NISWITCH\_ERROR\_SCAN\_IN\_PROGRESS. To stop the
scanning operation, To stop the scanning operation, call
niSwitch\_AbortScan.
''',
},
    },
    'IsDebounced': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
            {
                'direction': 'out',
                'name': 'isDebounced',
                'type': 'ViBoolean',
'documentation': {
'description': '''
VI\_TRUE indicates that all created paths have settled. VI\_FALSE
indicates that all created paths have not settled.
''',
},
            },
        ],
'documentation': {
'description': '''
Indicates if all created paths have settled by returning the value of
the NISWITCH\_ATTR\_IS\_DEBOUNCED attribute.
''',
},
    },
    'IsScanning': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
            {
                'direction': 'out',
                'name': 'isScanning',
                'type': 'ViBoolean',
'documentation': {
'description': '''
The driver returns the value of NISWITCH\_ATTR\_IS\_SCANNING attribute.
VI\_TRUE indicates that the switch device is scanning. VI\_FALSE
indicates that the switch device is idle.
''',
},
            },
        ],
'documentation': {
'description': 'Indicates the status of the scan.',
},
    },
    'LockSession': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
            {
                'direction': 'out',
                'name': 'callerHasLock',
                'type': 'ViBoolean',
'documentation': {
'description': '''
This parameter serves as a convenience. If you do not want to use this
parameter, pass VI\_NULL. Use this parameter in complex functions to
keep track of whether you obtain a lock and therefore need to unlock the
session. Pass the address of a local ViBoolean variable. In the
declaration of the local variable, initialize it to VI\_FALSE. Pass the
address of the same local variable to any other calls you make to
niSwitch\_LockSession or niSwitch\_UnlockSession in the same function.
The parameter is an input/output parameter. niSwitch\_LockSession and
niSwitch\_UnlockSession each inspect the current value and take the
following actions: - If the value is VI\_TRUE, niSwitch\_LockSession
does not lock the session again. If the value is VI\_FALSE,
niSwitch\_LockSession obtains the lock and sets the value of the
parameter to VI\_TRUE. - If the value is VI\_FALSE,
niSwitch\_UnlockSession does not attempt to unlock the session. If the
value is VI\_TRUE, niSwitch\_UnlockSession releases the lock and sets
the value of the parameter to VI\_FALSE. Thus, you can, call
niSwitch\_UnlockSession at the end of your function without worrying
about whether you actually have the lock. Example: ViStatus TestFunc
(ViSession vi, ViInt32 flags) { ViStatus error = VI\_SUCCESS; ViBoolean
haveLock = VI\_FALSE; if (flags & BIT\_1) { viCheckErr(
niSwitch\_LockSession(vi, &haveLock;)); viCheckErr( TakeAction1(vi)); if
(flags & BIT\_2) { viCheckErr( niSwitch\_UnlockSession(vi, &haveLock;));
viCheckErr( TakeAction2(vi)); viCheckErr( niSwitch\_LockSession(vi,
&haveLock;); } if (flags & BIT\_3) viCheckErr( TakeAction3(vi)); }
Error: /\* At this point, you cannot really be sure that you have the
lock. Fortunately, the haveLock variable takes care of that for you. \*/
niSwitch\_UnlockSession(vi, &haveLock;); return error; }
''',
},
            },
        ],
'documentation': {
'description': '''
This function obtains a multithread lock on the instrument session.
Before it does so, it waits until all other execution threads have
released their locks on the instrument session. Other threads might have
obtained a lock on this session in the following ways: - The user's
application called niSwitch\_LockSession. - A call to the instrument
driver locked the session. - A call to the IVI engine locked the
session. After your call to niSwitch\_LockSession returns successfully,
no other threads can access the instrument session until you call
niSwitch\_UnlockSession. Use niSwitch\_LockSession and
niSwitch\_UnlockSession around a sequence of calls to instrument driver
functions if you require that the instrument retain its settings through
the end of the sequence. You can safely make nested calls to
niSwitch\_LockSession within the same thread. To completely unlock the
session, you must balance each call to niSwitch\_LockSession with a call
to niSwitch\_UnlockSession. If, however, you use the Caller Has Lock
parameter in all calls to niSwitch\_LockSession and
niSwitch\_UnlockSession within a function, the IVI Library locks the
session only once within the function regardless of the number of calls
you make to niSwitch\_LockSession. This allows you to call
niSwitch\_UnlockSession just once at the end of the function.
''',
},
    },
    'RelayControl': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
            {
                'direction': 'in',
                'name': 'relayName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Name of the relay. Default value: None Examples of valid relay names:
ch0, ab0, 1wire, hlselect Refer to Devices Overview for a list of valid
relay names for the switch module.
''',
},
            },
            {
                'direction': 'in',
                'name': 'relayAction',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies whether to open or close a given relay. Default value: Relay
Close Defined values: NISWITCH\_VAL\_OPEN\_RELAY
NISWITCH\_VAL\_CLOSE\_RELAY (Default Value)
''',
},
            },
        ],
'documentation': {
'description': '''
Controls individual relays of the switch. When controlling individual
relays, the protection offered by setting the usage of source channels
and configuration channels, and by enabling or disabling analog bus
sharing on the NI SwitchBlock, does not apply. Refer to the device book
for your switch in the NI Switches Help to determine if the switch
supports individual relay control.
''',
},
    },
    'ResetInterchangeCheck': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
        ],
'documentation': {
'description': '''
When developing a complex test system that consists of multiple test
modules, it is generally a good idea to design the test modules so that
they can run in any order. To do so requires ensuring that each test
module completely configures the state of each instrument it uses. If a
particular test module does not completely configure the state of an
instrument, the state of the instrument depends on the configuration
from a previously executed test module. If you execute the test modules
in a different order, the behavior of the instrument and therefore the
entire test module is likely to change. This change in behavior is
generally instrument specific and represents an interchangeability
problem. You can use this function to test for such cases. After you
call this function, the interchangeability checking algorithms in the
specific driver ignore all previous configuration operations. By calling
this function at the beginning of a test module, you can determine
whether the test module has dependencies on the operation of previously
executed test modules. This function does not clear the
interchangeability warnings from the list of previously recorded
interchangeability warnings. If you want to guarantee that the
niSwitch\_GetNextInterchangeWarning function only returns those
interchangeability warnings that are generated after calling this
function, you must clear the list of interchangeability warnings. You
can clear the interchangeability warnings list by repeatedly calling the
niSwitch\_GetNextInterchangeWarning function until no more
interchangeability warnings are returned. If you are not interested in
the content of those warnings, you can call the
niSwitch\_ClearInterchangeWarnings function.
''',
},
    },
    'ResetWithDefaults': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
        ],
'documentation': {
'description': '''
Resets the switch module and applies initial user specified settings
from the logical name used to initialize the session. If the session was
created without a logical name, this function is equivalent to
niSwitch\_reset.
''',
},
    },
    'RouteScanAdvancedOutput': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
            {
                'direction': 'in',
                'name': 'scanAdvancedOutputConnector',
                'type': 'ViInt32',
'documentation': {
'description': '''
The scan advanced trigger destination. Valid locations are the
NISWITCH\_VAL\_FRONTCONNECTOR and NISWITCH\_VAL\_REARCONNECTOR. Default
value: NISWITCH\_VAL\_FRONTCONNECTOR
''',
},
            },
            {
                'direction': 'in',
                'name': 'scanAdvancedOutputBusLine',
                'type': 'ViInt32',
'documentation': {
'description': '''
The trigger line to route the scan advanced output trigger from the
front or rear connector. Select NISWITCH\_VAL\_NONE to break an existing
route. Default value: None Valid Values: NISWITCH\_VAL\_NONE
NISWITCH\_VAL\_TTL0 NISWITCH\_VAL\_TTL1 NISWITCH\_VAL\_TTL2
NISWITCH\_VAL\_TTL3 NISWITCH\_VAL\_TTL4 NISWITCH\_VAL\_TTL5
NISWITCH\_VAL\_TTL6 NISWITCH\_VAL\_TTL7
''',
},
            },
            {
                'direction': 'in',
                'name': 'Invert',
                'type': 'ViBoolean',
'documentation': {
'description': '''
If VI\_TRUE, inverts the input trigger signal from falling to rising or
vice versa. Default value: VI\_FALSE
''',
},
            },
        ],
'documentation': {
'description': '''
Routes the scan advanced output trigger from a trigger bus line (TTLx)
to the front or rear connector.
''',
},
    },
    'RouteTriggerInput': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
            {
                'direction': 'in',
                'name': 'triggerInputConnector',
                'type': 'ViInt32',
'documentation': {
'description': '''
The location of the input trigger source on the switch module. Valid
locations are the NISWITCH\_VAL\_FRONTCONNECTOR and
NISWITCH\_VAL\_REARCONNECTOR. Default value:
NISWITCH\_VAL\_FRONTCONNECTOR
''',
},
            },
            {
                'direction': 'in',
                'name': 'triggerInputBusLine',
                'type': 'ViInt32',
'documentation': {
'description': '''
The trigger line to route the input trigger. Select NISWITCH\_VAL\_NONE
to break an existing route. Default value: None Valid Values:
NISWITCH\_VAL\_NONE NISWITCH\_VAL\_TTL0 NISWITCH\_VAL\_TTL1
NISWITCH\_VAL\_TTL2 NISWITCH\_VAL\_TTL3 NISWITCH\_VAL\_TTL4
NISWITCH\_VAL\_TTL5 NISWITCH\_VAL\_TTL6 NISWITCH\_VAL\_TTL7
''',
},
            },
            {
                'direction': 'in',
                'name': 'Invert',
                'type': 'ViBoolean',
'documentation': {
'description': '''
If VI\_TRUE, inverts the input trigger signal from falling to rising or
vice versa. Default value: VI\_FALSE
''',
},
            },
        ],
'documentation': {
'description': '''
Routes the input trigger from the front or rear connector to a trigger
bus line (TTLx). To disconnect the route, call this function again and
specify None for trigger bus line parameter.
''',
},
    },
    'Scan': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
            {
                'direction': 'in',
                'name': 'Scanlist',
                'type': 'ViConstString',
'documentation': {
'description': '''
Pass the scan list you want the instrument to use. The driver uses this
value to set the NISWITCH\_ATTR\_SCAN\_LIST attribute. The scan list is
a string that specifies channel connections and trigger conditions for
scanning. After you call the niSwitch\_InitiateScan function, the
instrument makes or breaks connections and waits for triggers according
to the instructions in the scan list. The scan list is comprised of
channel names that you separate with special characters. These special
characters determine the operation the scanner performs on the channels
when it executes this scan list. To create a path between two channels,
use '->' (a dash followed by a '>' sign) between the two channel names.
Example: "CH1->CH2" instructs the switch to make a path from channel CH1
to channel CH2. To break or clear a path, use a '~' (tilde) as a prefix
before the path. Example: "~CH1->CH2" instructs the switch to break the
path from channel CH1 to channel CH2. To wait for a trigger event, use a
';' (semicolon) as a separator between paths. Example:
"CH1->CH2;CH3->CH4" instructs the switch to make the path from channel
CH1 to channel CH2, wait for a trigger, and then make the path from CH3
to CH4. To tell the switch device to create multiple paths
simultaneously, use an '&' (ampersand) character as a separator between
the paths. Example: "CH0->CH1; CH1->CH2 & CH3->CH4" instructs the
scanner to make the path between channels CH0 and CH1, wait for a
trigger, and then simultaneously make the paths between channels CH1 and
CH2 and between channels CH3 and CH4. For SCXI use the following syntax
: - For a single channel: sc!md!ch -> com0; For example: for Chassis 1,
module in slot 3, and ch 30 the syntax is: sc1!md3!ch30 ->com0; For
multiple sequential channels: sc!md!ch -> com0; For example: for Chassis
1, module in slot 3, and ch 30 to 19 the syntax is: sc1!md3!ch30:19
->com0; will scan from channel 30 to 19 sequentially. For multiple
randomly ordered channels: sc!md!ch -> com0; sc!md!ch -> com0; For
example: for Chassis 1, module in slot 3 and slot 4, and ch 30 and 5 on
slot 3 and channel 19 on slot 4the syntax is: sc1!md3!ch30 ->com0;
sc1!md4!ch19 ->com0; sc1!md3!ch5 ->com0; This will scan ch30 of slot 3
then ch19 of slot 4 then ch5 of slot3. For more information on scan list
syntax, refer to the NI Switches Help. Default Value: None
''',
},
            },
            {
                'direction': 'in',
                'name': 'Initiation',
                'type': 'ViInt16',
'documentation': {
'description': '''
Use the initiation paramater to specify whether the switch device or the
measurement device will be initiating the scan trigger handshake. This
parameter determines whether to wait for the scan to reach a trigger
point before completing. If the Measurement Device will initiate the
scan, set this parameter to
NISWITCH\_VAL\_MEASUREMENT\_DEVICE\_INITIATED. This function will then
wait until the switch is waiting for a trigger from the measurement
device before completing. If the Switch will initiate the scan, set this
parameter to NISWITCH\_VAL\_SWITCH\_INITIATED. This function will then
complete immediately after initating the scan. You should have already
set up your DMM to wait for a trigger before calling this function with
initiation set to NISWITCH\_VAL\_SWITCH\_INITIATED. Valid values:
NISWITCH\_VAL\_SWITCH\_INITIATED - Switch Initiated
NISWITCH\_VAL\_MEASUREMENT\_DEVICE\_INITIATED - Measurement device
initiated Default value: NISWITCH\_VAL\_MEASUREMENT\_DEVICE\_INITIATED
''',
},
            },
        ],
'documentation': {
'description': '''
This function is a high level operation for scanning. It takes the scan
list provided, programs the switching hardware and initiates the scan.
Once initiation is complete, the operation will return. The scan list
itself is comprised of a list of channel connections separated by
semicolons. For example, the following scan list would scan the first
three channels of a multiplexer. Example: com0->ch0; com0->ch1;
com0->ch2; For more information on scan list syntax, refer to the NI
Switches Help. To see the status of the scan, you can call either
niSwitch\_IsScanning or niSwitch\_WaitForScanComplete. Use the
niSwitch\_ConfigureScanTrigger function to configure the scan trigger.
Use the niSwitch\_AbortScan function to stop the scan if you are in
continuous scan mode (Refer to niSwitch\_SetContinuousScan); otherwise
the scan halts automatically when the end of the scan list is reached.
For reference, this operation is equivalent to calling
niSwitch\_ConfigureScanList and niSwitch\_InitiateScan.
''',
},
    },
    'SendSoftwareTrigger': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
        ],
'documentation': {
'description': '''
Sends a software trigger to the switch module specified in the NI-SWITCH
session. When the trigger input is set to NISWITCH\_VAL\_SOFTWARE\_TRIG
through either the niSwitch\_ConfigureScanTrigger or the
NISWITCH\_ATTR\_TRIGGER\_INPUT attribute, the scan does not proceed from
a semi-colon (wait for trigger) until niSwitch\_SendSoftwareTrigger is
called.
''',
},
    },
    'SetAttributeViBoolean': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Some attributes are unique per channel. For these, pass the name of the
channel. Other attributes are unique per switch device. Pass VI\_NULL or
an empty string for this parameter. Default Value: ""
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': '''
Pass the ID of an attribute. From the function panel window, you can use
this control as follows. - Click on the control or press , , or , to
display a dialog box containing a hierarchical list of the available
attributes. Attributes whose value cannot be set are dim. Help text is
shown for each attribute. Select an attribute by double-clicking on it
or by selecting it and then pressing . Read-only attributes appear dim
in the list box. If you select a read-only attribute, an error message
appears. A ring control at the top of the dialog box allows you to see
all IVI attributes or only the attributes of the ViInt32 type. If you
choose to see all IVI attributes, the data types appear to the right of
the attribute names in the list box. The data types that are not
consistent with this function are dim. If you select an attribute data
type that is dim, LabWindows/CVI transfers you to the function panel for
the corresponding function that is consistent with the data type. - If
you want to enter a variable name, press to change this ring control to
a manual input box. - If the attribute in this ring control has
constants as valid values, you can view the constants by moving to the
Attribute Value control and pressing .
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Pass the value to which you want to set the attribute. From the function
panel window, you can use this control as follows. - If the attribute
currently showing in the Attribute ID ring control has constants as
valid values, you can view a list of the constants by pressing on this
control. Select a value by double-clicking on it or by selecting it and
then pressing . Note: Some of the values might not be valid depending on
the current settings of the instrument session. Default Value: none
''',
},
            },
        ],
'documentation': {
'description': '''
This function sets the value of a ViBoolean attribute. This is a
low-level function that you can use to set the values of
instrument-specific attributes and inherent IVI attributes. If the
attribute represents an instrument state, this function performs
instrument I/O in the following cases: - State caching is disabled for
the entire session or for the particular attribute. - State caching is
enabled and the currently cached value is invalid or is different than
the value you specify. This instrument driver contains high-level
functions that set most of the instrument attributes. It is best to use
the high-level driver functions as much as possible. They handle order
dependencies and multithread locking for you. In addition, they perform
status checking only after setting all of the attributes. In contrast,
when you set multiple attributes using the SetAttribute functions, the
functions check the instrument status after each call. Also, when state
caching is enabled, the high-level functions that configure multiple
attributes perform instrument I/O only for the attributes whose value
you change. Thus, you can safely call the high-level functions without
the penalty of redundant instrument I/O.
''',
},
    },
    'SetAttributeViInt32': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Some attributes are unique per channel. For these, pass the name of the
channel. Other attributes are unique per switch device. Pass VI\_NULL or
an empty string for this parameter. Default Value: ""
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': '''
Pass the ID of an attribute. From the function panel window, you can use
this control as follows. - Click on the control or press , , or , to
display a dialog box containing a hierarchical list of the available
attributes. Attributes whose value cannot be set are dim. Help text is
shown for each attribute. Select an attribute by double-clicking on it
or by selecting it and then pressing . Read-only attributes appear dim
in the list box. If you select a read-only attribute, an error message
appears. A ring control at the top of the dialog box allows you to see
all IVI attributes or only the attributes of the ViInt32 type. If you
choose to see all IVI attributes, the data types appear to the right of
the attribute names in the list box. The data types that are not
consistent with this function are dim. If you select an attribute data
type that is dim, LabWindows/CVI transfers you to the function panel for
the corresponding function that is consistent with the data type. - If
you want to enter a variable name, press to change this ring control to
a manual input box. - If the attribute in this ring control has
constants as valid values, you can view the constants by moving to the
Attribute Value control and pressing .
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViInt32',
'documentation': {
'description': '''
Pass the value to which you want to set the attribute. From the function
panel window, you can use this control as follows. - If the attribute
currently showing in the Attribute ID ring control has constants as
valid values, you can view a list of the constants by pressing on this
control. Select a value by double-clicking on it or by selecting it and
then pressing . Note: Some of the values might not be valid depending on
the current settings of the instrument session. Default Value: none
''',
},
            },
        ],
'documentation': {
'description': '''
This function sets the value of a ViInt32 attribute. This is a low-level
function that you can use to set the values of instrument-specific
attributes and inherent IVI attributes. If the attribute represents an
instrument state, this function performs instrument I/O in the following
cases: - State caching is disabled for the entire session or for the
particular attribute. - State caching is enabled and the currently
cached value is invalid or is different than the value you specify. This
instrument driver contains high-level functions that set most of the
instrument attributes. It is best to use the high-level driver functions
as much as possible. They handle order dependencies and multithread
locking for you. In addition, they perform status checking only after
setting all of the attributes. In contrast, when you set multiple
attributes using the SetAttribute functions, the functions check the
instrument status after each call. Also, when state caching is enabled,
the high-level functions that configure multiple attributes perform
instrument I/O only for the attributes whose value you change. Thus, you
can safely call the high-level functions without the penalty of
redundant instrument I/O.
''',
},
    },
    'SetAttributeViReal64': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Some attributes are unique per channel. For these, pass the name of the
channel. Other attributes are unique per switch device. Pass VI\_NULL or
an empty string for this parameter. Default Value: ""
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': '''
Pass the ID of an attribute. From the function panel window, you can use
this control as follows. - Click on the control or press , , or , to
display a dialog box containing a hierarchical list of the available
attributes. Attributes whose value cannot be set are dim. Help text is
shown for each attribute. Select an attribute by double-clicking on it
or by selecting it and then pressing . Read-only attributes appear dim
in the list box. If you select a read-only attribute, an error message
appears. A ring control at the top of the dialog box allows you to see
all IVI attributes or only the attributes of the ViInt32 type. If you
choose to see all IVI attributes, the data types appear to the right of
the attribute names in the list box. The data types that are not
consistent with this function are dim. If you select an attribute data
type that is dim, LabWindows/CVI transfers you to the function panel for
the corresponding function that is consistent with the data type. - If
you want to enter a variable name, press to change this ring control to
a manual input box. - If the attribute in this ring control has
constants as valid values, you can view the constants by moving to the
Attribute Value control and pressing .
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViReal64',
'documentation': {
'description': '''
Pass the value to which you want to set the attribute. From the function
panel window, you can use this control as follows. - If the attribute
currently showing in the Attribute ID ring control has constants as
valid values, you can view a list of the constants by pressing on this
control. Select a value by double-clicking on it or by selecting it and
then pressing . Note: Some of the values might not be valid depending on
the current settings of the instrument session. Default Value: none
''',
},
            },
        ],
'documentation': {
'description': '''
This function sets the value of a ViReal64 attribute. This is a
low-level function that you can use to set the values of
instrument-specific attributes and inherent IVI attributes. If the
attribute represents an instrument state, this function performs
instrument I/O in the following cases: - State caching is disabled for
the entire session or for the particular attribute. - State caching is
enabled and the currently cached value is invalid or is different than
the value you specify. This instrument driver contains high-level
functions that set most of the instrument attributes. It is best to use
the high-level driver functions as much as possible. They handle order
dependencies and multithread locking for you. In addition, they perform
status checking only after setting all of the attributes. In contrast,
when you set multiple attributes using the SetAttribute functions, the
functions check the instrument status after each call. Also, when state
caching is enabled, the high-level functions that configure multiple
attributes perform instrument I/O only for the attributes whose value
you change. Thus, you can safely call the high-level functions without
the penalty of redundant instrument I/O.
''',
},
    },
    'SetAttributeViSession': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Some attributes are unique per channel. For these, pass the name of the
channel. Other attributes are unique per switch device. Pass VI\_NULL or
an empty string for this parameter. Default Value: ""
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': '''
Pass the ID of an attribute. From the function panel window, you can use
this control as follows. - Click on the control or press , , or , to
display a dialog box containing a hierarchical list of the available
attributes. Attributes whose value cannot be set are dim. Help text is
shown for each attribute. Select an attribute by double-clicking on it
or by selecting it and then pressing . Read-only attributes appear dim
in the list box. If you select a read-only attribute, an error message
appears. A ring control at the top of the dialog box allows you to see
all IVI attributes or only the attributes of the ViInt32 type. If you
choose to see all IVI attributes, the data types appear to the right of
the attribute names in the list box. The data types that are not
consistent with this function are dim. If you select an attribute data
type that is dim, LabWindows/CVI transfers you to the function panel for
the corresponding function that is consistent with the data type. - If
you want to enter a variable name, press to change this ring control to
a manual input box. - If the attribute in this ring control has
constants as valid values, you can view the constants by moving to the
Attribute Value control and pressing .
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViSession',
'documentation': {
'description': '''
Pass the value to which you want to set the attribute. From the function
panel window, you can use this control as follows. - If the attribute
currently showing in the Attribute ID ring control has constants as
valid values, you can view a list of the constants by pressing on this
control. Select a value by double-clicking on it or by selecting it and
then pressing . Note: Some of the values might not be valid depending on
the current settings of the instrument session. Default Value: none
''',
},
            },
        ],
'documentation': {
'description': '''
This function sets the value of a ViSession attribute. This is a
low-level function that you can use to set the values of
instrument-specific attributes and inherent IVI attributes. If the
attribute represents an instrument state, this function performs
instrument I/O in the following cases: - State caching is disabled for
the entire session or for the particular attribute. - State caching is
enabled and the currently cached value is invalid or is different than
the value you specify. This instrument driver contains high-level
functions that set most of the instrument attributes. It is best to use
the high-level driver functions as much as possible. They handle order
dependencies and multithread locking for you. In addition, they perform
status checking only after setting all of the attributes. In contrast,
when you set multiple attributes using the SetAttribute functions, the
functions check the instrument status after each call. Also, when state
caching is enabled, the high-level functions that configure multiple
attributes perform instrument I/O only for the attributes whose value
you change. Thus, you can safely call the high-level functions without
the penalty of redundant instrument I/O.
''',
},
    },
    'SetAttributeViString': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
'documentation': {
'description': '''
Some attributes are unique per channel. For these, pass the name of the
channel. Other attributes are unique per switch device. Pass VI\_NULL or
an empty string for this parameter. Default Value: ""
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr',
'documentation': {
'description': '''
Pass the ID of an attribute. From the function panel window, you can use
this control as follows. - Click on the control or press , , or , to
display a dialog box containing a hierarchical list of the available
attributes. Attributes whose value cannot be set are dim. Help text is
shown for each attribute. Select an attribute by double-clicking on it
or by selecting it and then pressing . Read-only attributes appear dim
in the list box. If you select a read-only attribute, an error message
appears. A ring control at the top of the dialog box allows you to see
all IVI attributes or only the attributes of the ViInt32 type. If you
choose to see all IVI attributes, the data types appear to the right of
the attribute names in the list box. The data types that are not
consistent with this function are dim. If you select an attribute data
type that is dim, LabWindows/CVI transfers you to the function panel for
the corresponding function that is consistent with the data type. - If
you want to enter a variable name, press to change this ring control to
a manual input box. - If the attribute in this ring control has
constants as valid values, you can view the constants by moving to the
Attribute Value control and pressing .
''',
},
            },
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Pass the value to which you want to set the attribute. From the function
panel window, you can use this control as follows. - If the attribute
currently showing in the Attribute ID ring control has constants as
valid values, you can view a list of the constants by pressing on this
control. Select a value by double-clicking on it or by selecting it and
then pressing . Note: Some of the values might not be valid depending on
the current settings of the instrument session. Default Value: none
''',
},
            },
        ],
'documentation': {
'description': '''
This function sets the value of a ViString attribute. This is a
low-level function that you can use to set the values of
instrument-specific attributes and inherent IVI attributes. If the
attribute represents an instrument state, this function performs
instrument I/O in the following cases: - State caching is disabled for
the entire session or for the particular attribute. - State caching is
enabled and the currently cached value is invalid or is different than
the value you specify. This instrument driver contains high-level
functions that set most of the instrument attributes. It is best to use
the high-level driver functions as much as possible. They handle order
dependencies and multithread locking for you. In addition, they perform
status checking only after setting all of the attributes. In contrast,
when you set multiple attributes using the SetAttribute functions, the
functions check the instrument status after each call. Also, when state
caching is enabled, the high-level functions that configure multiple
attributes perform instrument I/O only for the attributes whose value
you change. Thus, you can safely call the high-level functions without
the penalty of redundant instrument I/O.
''',
},
    },
    'SetContinuousScan': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
            {
                'direction': 'in',
                'name': 'continuousScan',
                'type': 'ViBoolean',
'documentation': {
'description': '''
If VI\_TRUE, loops continuously through the scan list during scanning.
If VI\_FALSE, the scan stops after one pass through the scan list.
Default value: VI\_FALSE
''',
},
            },
        ],
'documentation': {
'description': '''
Sets the to loop continuously through the scan list or to stop scanning
after one pass through the scan list.
''',
},
    },
    'SetPath': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
            {
                'direction': 'in',
                'name': 'pathList',
                'type': 'ViConstString',
'documentation': {
'description': '''
A string composed of comma-separated paths between channel 1 and channel
2. The first and last names in the path are the endpoints of the path.
Every other channel in the path are configuration channels. Example of a
valid path list string: ch0->com0, com0->ab0. In this example, com0 is a
configuration channel. Default value: None Obtain the path list for a
previously created path with niSwitch\_GetPath.
''',
},
            },
        ],
'documentation': {
'description': '''
Connects two channels by specifying an explicit path in the path list
parameter. niSwitch\_SetPath is particularly useful where path
repeatability is important, such as in calibrated signal paths. If this
is not necessary, use niSwitch\_Connect.
''',
},
    },
    'UnlockSession': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
            {
                'direction': 'out',
                'name': 'callerHasLock',
                'type': 'ViBoolean',
'documentation': {
'description': '''
This parameter serves as a convenience. If you do not want to use this
parameter, pass VI\_NULL. Use this parameter in complex functions to
keep track of whether you obtain a lock and therefore need to unlock the
session. Pass the address of a local ViBoolean variable. In the
declaration of the local variable, initialize it to VI\_FALSE. Pass the
address of the same local variable to any other calls you make to
niSwitch\_LockSession or niSwitch\_UnlockSession in the same function.
The parameter is an input/output parameter. niSwitch\_LockSession and
niSwitch\_UnlockSession each inspect the current value and take the
following actions: - If the value is VI\_TRUE, niSwitch\_LockSession
does not lock the session again. If the value is VI\_FALSE,
niSwitch\_LockSession obtains the lock and sets the value of the
parameter to VI\_TRUE. - If the value is VI\_FALSE,
niSwitch\_UnlockSession does not attempt to unlock the session. If the
value is VI\_TRUE, niSwitch\_UnlockSession releases the lock and sets
the value of the parameter to VI\_FALSE. Thus, you can, call
niSwitch\_UnlockSession at the end of your function without worrying
about whether you actually have the lock. Example: ViStatus TestFunc
(ViSession vi, ViInt32 flags) { ViStatus error = VI\_SUCCESS; ViBoolean
haveLock = VI\_FALSE; if (flags & BIT\_1) { viCheckErr(
niSwitch\_LockSession(vi, &haveLock;)); viCheckErr( TakeAction1(vi)); if
(flags & BIT\_2) { viCheckErr( niSwitch\_UnlockSession(vi, &haveLock;));
viCheckErr( TakeAction2(vi)); viCheckErr( niSwitch\_LockSession(vi,
&haveLock;); } if (flags & BIT\_3) viCheckErr( TakeAction3(vi)); }
Error: /\* At this point, you cannot really be sure that you have the
lock. Fortunately, the haveLock variable takes care of that for you. \*/
niSwitch\_UnlockSession(vi, &haveLock;); return error; }
''',
},
            },
        ],
'documentation': {
'description': '''
This function releases a lock that you acquired on an instrument session
using niSwitch\_LockSession. Refer to niSwitch\_LockSession for
additional information on session locks.
''',
},
    },
    'WaitForDebounce': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
            {
                'direction': 'in',
                'name': 'maximumTimeMs',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the maximum length of time to wait for all relays in the
switch module to activate or deactivate. If the specified time elapses
before all relays active or deactivate, a timeout error is returned.
Default Value:5000 ms
''',
},
            },
        ],
'documentation': {
'description': '''
Pauses until all created paths have settled. If the time you specify
with the Maximum Time (ms) parameter elapsed before the switch paths
have settled, this function returns the
NISWITCH\_ERROR\_MAX\_TIME\_EXCEEDED error.
''',
},
    },
    'WaitForScanComplete': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
            {
                'direction': 'in',
                'name': 'maximumTimeMs',
                'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the maximum length of time to wait for the switch module to
stop scanning. If the specified time elapses before the scan ends,
NISWITCH\_ERROR\_MAX\_TIME\_EXCEEDED error is returned. Default
Value:5000 ms
''',
},
            },
        ],
'documentation': {
'description': '''
Pauses until the switch module stops scanning or the maximum time has
elapsed and returns a timeout error. If the time you specify with the
Maximum Time (ms) parameter elapsed before the scanning operation has
finished, this function returns the NISWITCH\_ERROR\_MAX\_TIME\_EXCEEDED
error.
''',
},
    },
    'close': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
        ],
'documentation': {
'description': '''
Terminates the NI-SWITCH session and all of its attributes and
deallocates any memory resources the driver uses. Notes: (1) You must
unlock the session before calling niSwitch\_close. (2) After calling
niSwitch\_close, you cannot use the instrument driver again until you
call niSwitch\_init or niSwitch\_InitWithOptions.
''',
},
    },
    'error_message': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
            {
                'direction': 'in',
                'name': 'errorCode',
                'type': 'ViStatus',
'documentation': {
'description': '''
Status code returned by any NI-SWITCH function. Default Value: 0
(VI\_SUCCESS)
''',
},
            },
            {
                'direction': 'out',
                'name': 'errorMessage',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The error information formatted into a string. You must pass a ViChar
array with at least 256 bytes.
''',
},
            },
        ],
'documentation': {
'description': '''
Converts an error code returned by NI-SWITCH into a user-readable
string. Generally this information is supplied in error out of any
NI-SWITCH VI. Use niSwitch\_error\_message for a static lookup of an
error code description.
''',
},
    },
    'error_query': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
            {
                'direction': 'out',
                'name': 'errorCode',
                'type': 'ViInt32',
'documentation': {
'description': '''
Returns the error code read from the instrument's error queue. NI-SWITCH
does not have an error queue, so this function never returns any errors.
''',
},
            },
            {
                'direction': 'out',
                'name': 'errorMessage',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Returns the error message string read from the instrument's error
message queue. You must pass a ViChar array with at least 256 bytes.
NI-SWITCH does not have an error queue, so this function never returns
anything other than "No error".
''',
},
            },
        ],
'documentation': {
'description': '''
This function reads an error code and a message from the instrument's
error queue. NI-SWITCH does not have an error queue, so this function
never returns any errors.
''',
},
    },
    'init': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'resourceName',
                'type': 'ViRsrc',
'documentation': {
'description': '''
Resource name of the switch module to initialize. Default value: None
Syntax: Optional fields are shown in square brackets ([]). Configured in
MAX Under Valid Syntax Devices and Interfaces DeviceName Traditional
NI-DAQ Devices SCXI[chassis ID]::slot number PXI System PXI[bus
number]::device number TIP: IVI logical names are also valid for the
resource name. Default values for optional fields: chassis ID = 1 bus
number = 0 Example resource names: Resource Name Description SC1Mod3
NI-DAQmx module in chassis "SC1" slot 3 MySwitch NI-DAQmx module renamed
to "MySwitch" SCXI1::3 Traditional NI-DAQ module in chassis 1, slot 3
SCXI::3 Traditional NI-DAQ module in chassis 1, slot 3 PXI0::16 PXI bus
0, device number 16 PXI::16 PXI bus 0, device number 16
''',
},
            },
            {
                'direction': 'in',
                'name': 'idQuery',
                'type': 'ViBoolean',
'documentation': {
'description': '''
This parameter is ignored. Because NI-SWITCH supports multiple switch
modules, it always queries the switch device to determine which device
is installed. For this reason, this VI may return
NISWITCH\_ERROR\_FAIL\_ID\_QUERY even if this parameter is set to
VI\_FALSE. Valid Values: VI\_TRUE - (Default Value) VI\_FALSE -
Currently unsupported.
''',
},
            },
            {
                'direction': 'in',
                'name': 'resetDevice',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether to reset the switch module during the initialization
process. Valid Values: VI\_TRUE - Reset Device (Default Value) VI\_FALSE
- Currently unsupported. The device will not reset.
''',
},
            },
            {
                'direction': 'out',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
        ],
'documentation': {
'description': '''
Returns a session handle used to identify the switch module in all
subsequent instrument driver calls. niSwitch\_init creates a new IVI
instrument driver session for the switch module specified in the
resource name parameter. If multiple topologies are valid for that
device, the driver uses the default topology specified in MAX. By
default, the switch module is reset to a known state. An error is
returned if a session to the specified resource exists in another
process. The same session is returned if niSwitch\_init is called twice
in the same process for the same resource with the same topology.
''',
},
    },
    'reset': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
        ],
'documentation': {
'description': '''
Disconnects all created paths and returns the switch module to the state
at initialization. Configuration channel and source channel settings
remain unchanged.
''',
},
    },
    'revision_query': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
            {
                'direction': 'out',
                'name': 'instrumentDriverRevision',
                'type': 'ViChar[]',
'documentation': {
'description': '''
NI-SWITCH software revision numbers in the form of a string. You must
pass a ViChar array with at least 256 bytes.
''',
},
            },
            {
                'direction': 'out',
                'name': 'firmwareRevision',
                'type': 'ViChar[]',
'documentation': {
'description': 'Currently unsupported.',
},
            },
        ],
'documentation': {
'description': 'Returns the revision of the NI-SWITCH driver.',
},
    },
    'self_test': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
A particular NI-SWITCH session established with
niSwitch\_InitWithTopology, niSwitch\_InitWithOptions, or niSwitch\_init
and used for all subsequent NI-SWITCH calls.
''',
},
            },
            {
                'direction': 'out',
                'name': 'selfTestResult',
                'type': 'ViInt16',
'documentation': {
'description': 'Value returned from the switch device self-test. Passed 0 Failed 1',
},
            },
            {
                'direction': 'out',
                'name': 'selfTestMessage',
                'type': 'ViChar[]',
'documentation': {
'description': '''
Self-test response string from the switch device. You must pass a ViChar
array with at least 256 bytes.
''',
},
            },
        ],
'documentation': {
'description': 'Verifies that the driver can communicate with the switch module.',
},
    },
}
