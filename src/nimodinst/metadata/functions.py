
# -*- coding: utf-8 -*-
# This file is code generated, do not make changes here
#  If the generated information is not correct for python
#  changes can be made in functions_addon.py and they will be
#  applied at build time



functions = {
    'CloseInstalledDevicesSession': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'handle',
                'type': 'ViSession',
'documentation': {
'description': '''
The NI-ModInst session handle created by
niModInst_OpenInstalledDevicesSession.
''',
},
            },
        ],
'documentation': {
'description': '''
Cleans up the NI-ModInst session created by a call to
niModInst_OpenInstalledDevicesSession. Call this function when you are
finished using the session handle and do not use this handle again.
''',
},
    },
    'GetExtendedErrorInfo': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'errorInfoBufferSize',
                'type': 'ViInt32',
'documentation': {
'description': '''
The size of the buffer allocated and passed in as the errorInfo
parameter. The buffer should be large enough to hold the errorInfo
string (including a NULL terminating character). The size of the buffer
allocated and passed in as the errorInfo parameter. The buffer should be
large enough to hold the errorInfo string (including a NULL terminating
character). Refer to the function help to find out how to determine the
exact buffer size required.
''',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'errorInfo',
                'type': 'ViChar[]',
'documentation': {
'description': 'The character buffer into which the error information string is copied.',
},
            },
        ],
'documentation': {
'description': '''
Returns detailed information about the last error that occurred in the
current thread during a call to one of the NI-ModInst functions. When
one of the other functions returns a negative value as its return value,
immediately call this function to get detailed information about the
error. Because error information is stored on a thread-by-thread basis,
be sure to call this function in the same thread that called the
function that returned an error. The extended error information is
returned as a string. To find out the length of the error information
string before you allocate a buffer for it, call this function and pass
0 as the errorInfoBufferSize parameter or NULL as the errorInfo
parameter. When you do this, the function returns the size of the buffer
required to hold the error information string as its return value. You
can then allocate an appropriately sized string character buffer and
call this function again.
''',
},
    },
    'GetInstalledDeviceAttributeViInt32': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'handle',
                'type': 'ViSession',
'documentation': {
'description': '''
The NI-ModInst session handle created by
niModInst_OpenInstalledDevicesSession.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'index',
                'type': 'ViInt32',
'documentation': {
'description': '''
A zero-based index that specifies the device for which you want the
attribute. This index parameter should be between 0 and (deviceCount -
1), inclusive, where deviceCount is the number of installed devices
returned by niModInst_OpenInstalledDevicesSession.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeID',
                'type': 'ViInt32',
'documentation': {
'description': '''
The ID of the integer attribute you want to query. Valid Values Slot
Number--the slot (for example, in a PXI chassis) in which the device is
installed. This attribute can only be queried for PXI devices installed
in a chassis that has been properly identified in MAX. Chassis
Number--the number of the chassis in which the device is installed. This
attribute can only be queried for PXI devices installed in a chassis
that has been properly identified in MAX. Bus Number--the bus on which
the device has been enumerated. Socket Number--the socket number on
which the device has been enumerated. Notes The bus number and socket
number can be used to form a VISA resource string for this device, of
the form "PXI::::INSTR". Traditional NI-DAQ devices do not support the
chassis number, bus number, and socket number attributes.
''',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'attributeValue',
                'type': 'ViInt32',
'documentation': {
'description': '''
A pointer to a signed 32-bit integer variable that receives the value of
the requested attribute.
''',
},
            },
        ],
'documentation': {
'description': '''
Returns an integer attribute specified by the attributeID parameter for
a device specified by the handle and index parameters. The handle
parameter is expected to be a valid handle returned by
niModInst_OpenInstalledDevicesSession. It therefore acts as a handle to
a list of installed devices. The index parameter specifies the device in
the list for which you want the attribute.
''',
},
    },
    'GetInstalledDeviceAttributeViString': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'handle',
                'type': 'ViSession',
'documentation': {
'description': '''
The NI-ModInst session handle created by
niModInst_OpenInstalledDevicesSession.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'index',
                'type': 'ViInt32',
'documentation': {
'description': '''
A zero-based index that specifies the device for which you want the
attribute. This index parameter should be between 0 and (deviceCount -
1), inclusive, where deviceCount is the number of installed devices
returned by niModInst_OpenInstalledDevicesSession.
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeID',
                'type': 'ViInt32',
'documentation': {
'description': '''
The ID of the string attribute you want to query. Valid Values
NIMODINST_ATTR_DEVICE_NAME--the name of the device, which can be used
to open an instrument driver session for that device
NIMODINST_ATTR_DEVICE_MODEL--the model of the device (for example, NI
PXI-5122) NIMODINST_ATTR_SERIAL_NUMBER--the serial number of the
device
''',
},
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'attributeValueBufferSize',
                'type': 'ViInt32',
'documentation': {
'description': '''
The size of the buffer allocated and passed in as the attributeValue
parameter. The buffer should be large enough to hold the attribute value
string (including a NULL terminating character). Refer to the
Description section for information on how to determine the exact buffer
size required.
''',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'attributeValue',
                'type': 'ViChar[]',
'documentation': {
'description': 'The character buffer into which the attribute value string is copied.',
},
            },
        ],
'documentation': {
'description': '''
Returns a string attribute specified by the attributeID parameter for a
device specified by the handle and index parameters. The handle
parameter is expected to be a valid handle returned by
niModInst_OpenInstalledDevicesSession. Therefore, it acts as a handle
to a list of installed devices. The index parameter specifies for which
device in the list you want the attribute. To find out the length of the
device name string before you allocate a buffer for it, simply call this
function and pass 0 as the attributeValueBufferSize parameter or NULL as
the attributeValue parameter. When you do this, the function returns the
size of the buffer required to hold the attribute value string as its
return value. You can then allocate an appropriately sized character
buffer and call this function again.
''',
},
    },
    'OpenInstalledDevicesSession': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'driver',
                'type': 'ViConstString',
'documentation': {
'description': '''
A string specifying the driver whose supported devices you want to find.
This string is not case-sensitive. Some examples are: NI-SCOPE niScope
NI-FGEN niFgen NI-HSDIO niHSDIO NI-DMM niDMM NI-SWITCH niSwitch Note If
you use the empty string for this parameter, NI-ModInst creates a list
of all Modular Instruments devices installed in the system.
''',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'handle',
                'type': 'ViSession',
'documentation': {
'description': '''
A pointer to a ViSession variable that receives the value of the
NI-ModInst session handle. This value acts as a handle to the list of
installed devices and is used in other NI-ModInst functions.
''',
},
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'deviceCount',
                'type': 'ViInt32',
'documentation': {
'description': '''
A pointer to an integer variable that receives the number of devices
found in the system that are supported by the driver specified in the
driver parameter.
''',
},
            },
        ],
'documentation': {
'description': '''
Creates a handle to a list of installed devices supported by the
specified driver. Call this function and pass in the name of a National
Instruments instrument driver, such as "NI-SCOPE". This function
searches the system and constructs a list of all the installed devices
that are supported by that driver, and then returns both a handle to
this list and the number of devices found. The handle is used with other
functions to query for attributes such as device name and model, and to
safely discard the list when finished. Note This handle reflects the
system state when the handle is created (that is, when you call this
function. If you remove devices from the system or rename them in
Measurement & Automation Explorer (MAX), this handle may not refer to an
accurate list of devices. You should destroy the handle using
niModInst_CloseInstalledDevicesSession and create a new handle using
this function.
''',
},
    },
}
