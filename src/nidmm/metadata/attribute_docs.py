
# -*- coding: utf-8 -*-
attribute_docs = {
    '-2': {
        'shortDescription': '''
Specifies the channel name used to access all subsequent channel-based
properties in this property node. Set the channel before setting
channel-based properties. Pass a name that the instrument driver defines
or a virtual channel name configured in MAX.

''',
        'longDescription': '''
Specifies the channel name used to access all subsequent channel-based
properties in this property node. Set the channel before setting
channel-based properties. Pass a name that the instrument driver defines
or a virtual channel name configured in MAX.

This corresponds to LabVIEW property **Active Channel**

The following table lists the characteristics of this property.

+------------------+--------------+
| Characteristic   | Value        |
+------------------+--------------+
| Datatype         | string       |
+------------------+--------------+
| Permissions      | Write Only   |
+------------------+--------------+
| High Level VI    | N/A          |
+------------------+--------------+
| Channel Based    | False        |
+------------------+--------------+
| Resettable       | No           |
+------------------+--------------+

''',
    },
    '1050002': {
        'shortDescription': '''
Specifies whether to validate property values and VI parameters. If
enabled, the instrument driver validates the parameter values passed to
driver VIs. Range checking parameters is very useful for debugging.
After the user program is validated, you can set this property to FALSE
(0) to disable range checking and maximize performance. The default
value is TRUE (1). Use niDMM Initialize With Options to override the
default setting.

''',
        'longDescription': '''
Specifies whether to validate property values and VI parameters. If
enabled, the instrument driver validates the parameter values passed to
driver VIs. Range checking parameters is very useful for debugging.
After the user program is validated, you can set this property to FALSE
(0) to disable range checking and maximize performance. The default
value is TRUE (1). Use niDMM Initialize With Options to override the
default setting.

This corresponds to LabVIEW property **Inherent IVI Attributes:User
Options:Range Check**

The following table lists the characteristics of this property.

+------------------+--------------+
| Characteristic   | Value        |
+------------------+--------------+
| Datatype         | Boolean      |
+------------------+--------------+
| Permissions      | Read/Write   |
+------------------+--------------+
| High Level VI    | N/A          |
+------------------+--------------+
| Channel Based    | False        |
+------------------+--------------+
| Resettable       | No           |
+------------------+--------------+

''',
    },
    '1050003': {
        'shortDescription': '''
Specifies whether the instrument driver queries the instrument status
after each operation. Querying the instrument status is very useful for
debugging. After the user program is validated, this property can be set
to FALSE (0) to disable status checking and maximize performance. The
instrument driver can choose to ignore status checking for particular
properties regardless of the setting of this property. The default value
is TRUE (1). Use niDMM Initialize With Options to override the default
setting.

''',
        'longDescription': '''
Specifies whether the instrument driver queries the instrument status
after each operation. Querying the instrument status is very useful for
debugging. After the user program is validated, this property can be set
to FALSE (0) to disable status checking and maximize performance. The
instrument driver can choose to ignore status checking for particular
properties regardless of the setting of this property. The default value
is TRUE (1). Use niDMM Initialize With Options to override the default
setting.

This corresponds to LabVIEW property **Inherent IVI Attributes:User
Options:Query Instrument Status**

The following table lists the characteristics of this property.

+------------------+--------------+
| Characteristic   | Value        |
+------------------+--------------+
| Datatype         | Boolean      |
+------------------+--------------+
| Permissions      | Read/Write   |
+------------------+--------------+
| High Level VI    | N/A          |
+------------------+--------------+
| Channel Based    | False        |
+------------------+--------------+
| Resettable       | No           |
+------------------+--------------+

''',
    },
    '1050004': {
        'shortDescription': '''
Specifies whether to cache the value of properties. When caching is
enabled, the instrument driver keeps track of the current instrument
settings and avoids sending redundant commands to the instrument. Thus,
it significantly increases execution speed. The instrument driver can
choose to always cache or to never cache particular properties
regardless of the setting of this property. The default value is TRUE
(1). Use niDMM Initialize With Options to override the default setting.

''',
        'longDescription': '''
Specifies whether to cache the value of properties. When caching is
enabled, the instrument driver keeps track of the current instrument
settings and avoids sending redundant commands to the instrument. Thus,
it significantly increases execution speed. The instrument driver can
choose to always cache or to never cache particular properties
regardless of the setting of this property. The default value is TRUE
(1). Use niDMM Initialize With Options to override the default setting.

This corresponds to LabVIEW property **Inherent IVI Attributes:User
Options:Cache**

The following table lists the characteristics of this property.

+------------------+--------------+
| Characteristic   | Value        |
+------------------+--------------+
| Datatype         | Boolean      |
+------------------+--------------+
| Permissions      | Read/Write   |
+------------------+--------------+
| High Level VI    | N/A          |
+------------------+--------------+
| Channel Based    | False        |
+------------------+--------------+
| Resettable       | No           |
+------------------+--------------+

''',
    },
    '1050005': {
        'shortDescription': '''
Specifies whether to simulate instrument driver I/O operations. If
simulation is enabled, instrument driver functions perform range
checking and call IVI Get and Set VIs, but they do not perform
instrument I/O. For output parameters that represent instrument data,
the instrument driver VIs return calculated values. The default value is
FALSE (0). Use niDMM Initialize With Options to override the default
setting.

''',
        'longDescription': '''
Specifies whether to simulate instrument driver I/O operations. If
simulation is enabled, instrument driver functions perform range
checking and call IVI Get and Set VIs, but they do not perform
instrument I/O. For output parameters that represent instrument data,
the instrument driver VIs return calculated values. The default value is
FALSE (0). Use niDMM Initialize With Options to override the default
setting.

This corresponds to LabVIEW property **Inherent IVI Attributes:User
Options:Simulate**

.. note::
   Simulate can only be set within the niDMM Initialize With Options VI. The property value cannot be changed outside of the VI.  

The following table lists the characteristics of this property.

+------------------+--------------+
| Characteristic   | Value        |
+------------------+--------------+
| Datatype         | Boolean      |
+------------------+--------------+
| Permissions      | Read/Write   |
+------------------+--------------+
| High Level VI    | N/A          |
+------------------+--------------+
| Channel Based    | False        |
+------------------+--------------+
| Resettable       | No           |
+------------------+--------------+

''',
    },
    '1050006': {
        'shortDescription': '''
Specifies whether the IVI engine keeps a list of the value coercions it
makes for ViInt32 and ViReal64 properties. The default value is FALSE
(0). Use niDMM Initialize With Options to override the default setting.
Use niDMM Get Next Coercion Record to extract and delete the oldest
coercion record from the list.

''',
        'longDescription': '''
Specifies whether the IVI engine keeps a list of the value coercions it
makes for ViInt32 and ViReal64 properties. The default value is FALSE
(0). Use niDMM Initialize With Options to override the default setting.
Use niDMM Get Next Coercion Record to extract and delete the oldest
coercion record from the list.

This corresponds to LabVIEW property **Inherent IVI Attributes:User
Options:Record Value Coercions**

The following table lists the characteristics of this property.

+------------------+--------------+
| Characteristic   | Value        |
+------------------+--------------+
| Datatype         | Boolean      |
+------------------+--------------+
| Permissions      | Read/Write   |
+------------------+--------------+
| High Level VI    | N/A          |
+------------------+--------------+
| Channel Based    | False        |
+------------------+--------------+
| Resettable       | No           |
+------------------+--------------+

''',
    },
    '1050007': {
        'shortDescription': '''
This property indicates the Driver Setup string that the user specified
when initializing the driver. Some cases exist where the end-user must
specify instrument driver options at initialization time. An example of
this is specifying a particular instrument model from among a family of
instruments that the driver supports. This is useful when using
simulation. The end-user can specify driver-specific options through the
Driver Setup keyword in the Option String parameter in niDMM Initialize
With Options . If the user does not specify a Driver Setup string, this
property returns an empty string.

''',
        'longDescription': '''
This property indicates the Driver Setup string that the user specified
when initializing the driver. Some cases exist where the end-user must
specify instrument driver options at initialization time. An example of
this is specifying a particular instrument model from among a family of
instruments that the driver supports. This is useful when using
simulation. The end-user can specify driver-specific options through the
Driver Setup keyword in the Option String parameter in niDMM Initialize
With Options . If the user does not specify a Driver Setup string, this
property returns an empty string.

This corresponds to LabVIEW property **Inherent IVI Attributes:User
Options:Driver Setup**

The following table lists the characteristics of this property.

+------------------+-------------+
| Characteristic   | Value       |
+------------------+-------------+
| Datatype         | string      |
+------------------+-------------+
| Permissions      | Read Only   |
+------------------+-------------+
| High Level VI    | N/A         |
+------------------+-------------+
| Channel Based    | False       |
+------------------+-------------+
| Resettable       | No          |
+------------------+-------------+

''',
    },
    '1050021': {
        'shortDescription': '''
Specifies whether to perform interchangeability checking and log
interchangeability warnings when you call niDMM VIs. Interchangeability
warnings indicate that using your application with a different
instrument might cause different behavior. Use niDMM Get Next
Interchange Warning to extract interchange warnings. Use niDMM Clear
Interchange Warnings to clear the list of interchangeability warnings
without reading them. Interchangeability checking examines the
properties in a capability group only if you specify a value for at
least one property within that group. Interchangeability warnings can
occur when a property affects the behavior of the instrument and you
have not set that property, or the property has been invalidated since
you set it.

''',
        'longDescription': '''
Specifies whether to perform interchangeability checking and log
interchangeability warnings when you call niDMM VIs. Interchangeability
warnings indicate that using your application with a different
instrument might cause different behavior. Use niDMM Get Next
Interchange Warning to extract interchange warnings. Use niDMM Clear
Interchange Warnings to clear the list of interchangeability warnings
without reading them. Interchangeability checking examines the
properties in a capability group only if you specify a value for at
least one property within that group. Interchangeability warnings can
occur when a property affects the behavior of the instrument and you
have not set that property, or the property has been invalidated since
you set it.

This corresponds to LabVIEW property **Inherent IVI Attributes:User
Options:Interchange Check**

+---------+-----+
| TRUE    | 1   |
+---------+-----+
| FALSE   | 0   |
+---------+-----+

The following table lists the characteristics of this property.

+------------------+--------------+
| Characteristic   | Value        |
+------------------+--------------+
| Datatype         | Boolean      |
+------------------+--------------+
| Permissions      | Read/Write   |
+------------------+--------------+
| High Level VI    | N/A          |
+------------------+--------------+
| Channel Based    | False        |
+------------------+--------------+
| Resettable       | No           |
+------------------+--------------+

''',
    },
    '1050101': {
        'shortDescription': '''
A code that describes the first error that occurred since the last call
to niDMM Get Error for the session. The value follows the VXIplug&play
conventions. A negative value describes an error condition. A positive
value describes a warning condition. A zero indicates that no error or
warning occurred. The error and warning values can be status codes
defined by IVI, VISA, class drivers, or specific drivers.

''',
        'longDescription': '''
A code that describes the first error that occurred since the last call
to niDMM Get Error for the session. The value follows the VXIplug&play
conventions. A negative value describes an error condition. A positive
value describes a warning condition. A zero indicates that no error or
warning occurred. The error and warning values can be status codes
defined by IVI, VISA, class drivers, or specific drivers.

This corresponds to LabVIEW property **Obsolete:Inherent IVI
Attributes:Error Info:Primary Error**

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1050102': {
        'shortDescription': '''
An optional code that provides additional information concerning the
primary error condition. The error and warning values can be status
codes defined by IVI, VISA, class drivers, or specific drivers. Zero
indicates no additional information.

''',
        'longDescription': '''
An optional code that provides additional information concerning the
primary error condition. The error and warning values can be status
codes defined by IVI, VISA, class drivers, or specific drivers. Zero
indicates no additional information.

This corresponds to LabVIEW property **Obsolete:Inherent IVI
Attributes:Error Info:Secondary Error**

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1050103': {
        'shortDescription': '''
An optional string that contains additional information concerning the
primary error condition.

''',
        'longDescription': '''
An optional string that contains additional information concerning the
primary error condition.

This corresponds to LabVIEW property **Obsolete:Inherent IVI
Attributes:Error Info:Error Elaboration**

The following table lists the characteristics of this property.

+------------------+--------------+
| Characteristic   | Value        |
+------------------+--------------+
| Datatype         | string       |
+------------------+--------------+
| Permissions      | Read/Write   |
+------------------+--------------+
| High Level VI    | N/A          |
+------------------+--------------+
| Channel Based    | False        |
+------------------+--------------+
| Resettable       | No           |
+------------------+--------------+

''',
    },
    '1050203': {
        'shortDescription': '''
Indicates the number of channels that the specific instrument driver
supports. For each property for which the IVI\_VAL\_MULTI\_CHANNEL flag
property is set, the IVI engine maintains a separate cache value for
each channel.

''',
        'longDescription': '''
Indicates the number of channels that the specific instrument driver
supports. For each property for which the IVI\_VAL\_MULTI\_CHANNEL flag
property is set, the IVI engine maintains a separate cache value for
each channel.

This corresponds to LabVIEW property **Inherent IVI
Attributes:Instrument Capabilities:Channel Count**

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read Only               |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1050302': {
        'shortDescription': '''
The prefix for the specific instrument driver. The name of each
user-callable VI in this driver starts with this prefix. The prefix can
be up to a maximum of eight characters.

''',
        'longDescription': '''
The prefix for the specific instrument driver. The name of each
user-callable VI in this driver starts with this prefix. The prefix can
be up to a maximum of eight characters.

This corresponds to LabVIEW property **Inherent IVI
Attributes:Instrument Capabilities:Specific Driver Prefix**

The following table lists the characteristics of this property.

+------------------+-------------+
| Characteristic   | Value       |
+------------------+-------------+
| Datatype         | string      |
+------------------+-------------+
| Permissions      | Read Only   |
+------------------+-------------+
| High Level VI    | N/A         |
+------------------+-------------+
| Channel Based    | False       |
+------------------+-------------+
| Resettable       | No          |
+------------------+-------------+

''',
    },
    '1050304': {
        'shortDescription': '''
A string containing the resource descriptor of the instrument.

''',
        'longDescription': '''
A string containing the resource descriptor of the instrument.

This corresponds to LabVIEW property **Inherent IVI Attributes:Advanced
Session Information:I/O Resource Descriptor**

The following table lists the characteristics of this property.

+------------------+-------------+
| Characteristic   | Value       |
+------------------+-------------+
| Datatype         | string      |
+------------------+-------------+
| Permissions      | Read Only   |
+------------------+-------------+
| High Level VI    | N/A         |
+------------------+-------------+
| Channel Based    | False       |
+------------------+-------------+
| Resettable       | No          |
+------------------+-------------+

''',
    },
    '1050305': {
        'shortDescription': '''
A string containing the logical name of the instrument.

''',
        'longDescription': '''
A string containing the logical name of the instrument.

This corresponds to LabVIEW property **Inherent IVI Attributes:Advanced
Session Information:Logical Name**

The following table lists the characteristics of this property.

+------------------+-------------+
| Characteristic   | Value       |
+------------------+-------------+
| Datatype         | string      |
+------------------+-------------+
| Permissions      | Read Only   |
+------------------+-------------+
| High Level VI    | N/A         |
+------------------+-------------+
| Channel Based    | False       |
+------------------+-------------+
| Resettable       | No          |
+------------------+-------------+

''',
    },
    '1050327': {
        'shortDescription': '''
A string containing the instrument models supported by the specific
driver.

''',
        'longDescription': '''
A string containing the instrument models supported by the specific
driver.

This corresponds to LabVIEW property **Inherent IVI Attributes:Specific
Driver Capabilities:Supported Instrument Models**

The following table lists the characteristics of this property.

+------------------+-------------+
| Characteristic   | Value       |
+------------------+-------------+
| Datatype         | string      |
+------------------+-------------+
| Permissions      | Read Only   |
+------------------+-------------+
| High Level VI    | N/A         |
+------------------+-------------+
| Channel Based    | False       |
+------------------+-------------+
| Resettable       | No          |
+------------------+-------------+

''',
    },
    '1050401': {
        'shortDescription': '''
A string containing the capabilities and extension groups supported by
the specific driver.

''',
        'longDescription': '''
A string containing the capabilities and extension groups supported by
the specific driver.

This corresponds to LabVIEW property **Inherent IVI Attributes:Specific
Driver Capabilities:Group Capabilities**

The following table lists the characteristics of this property.

+------------------+-------------+
| Characteristic   | Value       |
+------------------+-------------+
| Datatype         | string      |
+------------------+-------------+
| Permissions      | Read Only   |
+------------------+-------------+
| High Level VI    | N/A         |
+------------------+-------------+
| Channel Based    | False       |
+------------------+-------------+
| Resettable       | No          |
+------------------+-------------+

''',
    },
    '1050501': {
        'shortDescription': '''
The major version number of the IVI engine.

''',
        'longDescription': '''
The major version number of the IVI engine.

This corresponds to LabVIEW property **Obsolete:Inherent IVI
Attributes:Version Info:Engine Major Version**

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read Only               |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1050502': {
        'shortDescription': '''
The minor version number of the IVI engine.

''',
        'longDescription': '''
The minor version number of the IVI engine.

This corresponds to LabVIEW property **Obsolete:Inherent IVI
Attributes:Version Info:Engine Minor Version**

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read Only               |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1050503': {
        'shortDescription': '''
Returns the major version number of this instrument driver.

''',
        'longDescription': '''
Returns the major version number of this instrument driver.

This corresponds to LabVIEW property **Inherent IVI Attributes:Version
Info:Specific Driver Major Version**

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read Only               |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1050504': {
        'shortDescription': '''
Returns the minor version number of this instrument driver.

''',
        'longDescription': '''
Returns the minor version number of this instrument driver.

This corresponds to LabVIEW property **Inherent IVI Attributes:Version
Info:Specific Driver Minor Version**

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read Only               |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1050510': {
        'shortDescription': '''
A string containing the instrument firmware revision number.

''',
        'longDescription': '''
A string containing the instrument firmware revision number.

This corresponds to LabVIEW property **Inherent IVI
Attributes:Instrument Identification:Instrument Firmware Revision**

The following table lists the characteristics of this property.

+------------------+-------------+
| Characteristic   | Value       |
+------------------+-------------+
| Datatype         | string      |
+------------------+-------------+
| Permissions      | Read Only   |
+------------------+-------------+
| High Level VI    | N/A         |
+------------------+-------------+
| Channel Based    | False       |
+------------------+-------------+
| Resettable       | No          |
+------------------+-------------+

''',
    },
    '1050511': {
        'shortDescription': '''
A string containing the manufacturer of the instrument.

''',
        'longDescription': '''
A string containing the manufacturer of the instrument.

This corresponds to LabVIEW property **Inherent IVI
Attributes:Instrument Identification:Instrument Manufacturer**

The following table lists the characteristics of this property.

+------------------+-------------+
| Characteristic   | Value       |
+------------------+-------------+
| Datatype         | string      |
+------------------+-------------+
| Permissions      | Read Only   |
+------------------+-------------+
| High Level VI    | N/A         |
+------------------+-------------+
| Channel Based    | False       |
+------------------+-------------+
| Resettable       | No          |
+------------------+-------------+

''',
    },
    '1050512': {
        'shortDescription': '''
A string containing the instrument model.

''',
        'longDescription': '''
A string containing the instrument model.

This corresponds to LabVIEW property **Inherent IVI
Attributes:Instrument Identification:Instrument Model**

The following table lists the characteristics of this property.

+------------------+-------------+
| Characteristic   | Value       |
+------------------+-------------+
| Datatype         | string      |
+------------------+-------------+
| Permissions      | Read Only   |
+------------------+-------------+
| High Level VI    | N/A         |
+------------------+-------------+
| Channel Based    | False       |
+------------------+-------------+
| Resettable       | No          |
+------------------+-------------+

''',
    },
    '1050513': {
        'shortDescription': '''
A string containing the vendor of the specific driver.

''',
        'longDescription': '''
A string containing the vendor of the specific driver.

This corresponds to LabVIEW property **Inherent IVI Attributes:Specific
Driver Identification:Specific Driver Vendor**

The following table lists the characteristics of this property.

+------------------+-------------+
| Characteristic   | Value       |
+------------------+-------------+
| Datatype         | string      |
+------------------+-------------+
| Permissions      | Read Only   |
+------------------+-------------+
| High Level VI    | N/A         |
+------------------+-------------+
| Channel Based    | False       |
+------------------+-------------+
| Resettable       | No          |
+------------------+-------------+

''',
    },
    '1050514': {
        'shortDescription': '''
A string containing a description of the specific driver.

''',
        'longDescription': '''
A string containing a description of the specific driver.

This corresponds to LabVIEW property **Inherent IVI Attributes:Specific
Driver Identification:Specific Driver Description**

The following table lists the characteristics of this property.

+------------------+-------------+
| Characteristic   | Value       |
+------------------+-------------+
| Datatype         | string      |
+------------------+-------------+
| Permissions      | Read Only   |
+------------------+-------------+
| High Level VI    | N/A         |
+------------------+-------------+
| Channel Based    | False       |
+------------------+-------------+
| Resettable       | No          |
+------------------+-------------+

''',
    },
    '1050515': {
        'shortDescription': '''
The major version number of the class specification for the specific
driver.

''',
        'longDescription': '''
The major version number of the class specification for the specific
driver.

This corresponds to LabVIEW property **Inherent IVI Attributes:Specific
Driver Identification:Specific Driver Class Spec Major Version**

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read Only               |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1050516': {
        'shortDescription': '''
The minor version number of the class specification for the specific
driver.

''',
        'longDescription': '''
The minor version number of the class specification for the specific
driver.

This corresponds to LabVIEW property **Inherent IVI Attributes:Specific
Driver Identification:Specific Driver Class Spec Minor Version**

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read Only               |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1050551': {
        'shortDescription': '''
A string that contains additional version information about this
instrument driver.

''',
        'longDescription': '''
A string that contains additional version information about this
instrument driver.

This corresponds to LabVIEW property **Inherent IVI Attributes:Version
Info:Specific Driver Revision**

The following table lists the characteristics of this property.

+------------------+-------------+
| Characteristic   | Value       |
+------------------+-------------+
| Datatype         | string      |
+------------------+-------------+
| Permissions      | Read Only   |
+------------------+-------------+
| High Level VI    | N/A         |
+------------------+-------------+
| Channel Based    | False       |
+------------------+-------------+
| Resettable       | No          |
+------------------+-------------+

''',
    },
    '1050553': {
        'shortDescription': '''
A string that contains additional version information about the IVI
engine.

''',
        'longDescription': '''
A string that contains additional version information about the IVI
engine.

This corresponds to LabVIEW property **Obsolete:Inherent IVI
Attributes:Version Info:Engine Revision**

The following table lists the characteristics of this property.

+------------------+-------------+
| Characteristic   | Value       |
+------------------+-------------+
| Datatype         | string      |
+------------------+-------------+
| Permissions      | Read Only   |
+------------------+-------------+
| High Level VI    | N/A         |
+------------------+-------------+
| Channel Based    | False       |
+------------------+-------------+
| Resettable       | No          |
+------------------+-------------+

''',
    },
    '1150001': {
        'shortDescription': '''
A string containing the type of instrument used in the current session.

''',
        'longDescription': '''
A string containing the type of instrument used in the current session.

This corresponds to LabVIEW property **Obsolete:Misc:IDQuery response**

The following table lists the characteristics of this property.

+------------------+-------------+
| Characteristic   | Value       |
+------------------+-------------+
| Datatype         | string      |
+------------------+-------------+
| Permissions      | Read Only   |
+------------------+-------------+
| High Level VI    | N/A         |
+------------------+-------------+
| Channel Based    | False       |
+------------------+-------------+
| Resettable       | No          |
+------------------+-------------+

''',
    },
    '1150002': {
        'shortDescription': '''
Specifies the polarity of the generated measurement complete signal.

''',
        'longDescription': '''
Specifies the polarity of the generated measurement complete signal.

This corresponds to LabVIEW property **Trigger:Measurement Destination
Slope**

+--------------------+------------------------------------------------------------------+
| Name               | Description                                                      |
+--------------------+------------------------------------------------------------------+
| **Positive** (0)   | The driver triggers on the rising edge of the trigger signal.    |
+--------------------+------------------------------------------------------------------+
| **Negative** (1)   | The driver triggers on the falling edge of the trigger signal.   |
+--------------------+------------------------------------------------------------------+

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1150003': {
        'shortDescription': '''
For the NI 4050 only, specifies the shunt resistance value.

''',
        'longDescription': '''
For the NI 4050 only, specifies the shunt resistance value.

This corresponds to LabVIEW property **Configuration:Measurement
Options:Shunt Value**

.. note::
   The NI 4050 requires an external shunt resistor for current measurements. This property should be set to the value of the shunt resistor.  

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 64-bit floating point   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1150010': {
        'shortDescription': '''
Specifies the edge of the signal from the specified sample trigger
source on which the DMM is triggered.

''',
        'longDescription': '''
Specifies the edge of the signal from the specified sample trigger
source on which the DMM is triggered.

This corresponds to LabVIEW property **Multi Point Acquisition:Sample
Trig Slope**

+--------------------+------------------------------------------------------------------+
| Name               | Description                                                      |
+--------------------+------------------------------------------------------------------+
| **Positive** (0)   | The driver triggers on the rising edge of the trigger signal.    |
+--------------------+------------------------------------------------------------------+
| **Negative** (1)   | The driver triggers on the falling edge of the trigger signal.   |
+--------------------+------------------------------------------------------------------+

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1150014': {
        'shortDescription': '''
Specifies how the DMM acquires data.

.. note::
   The NI 4050 and NI 4060 are not supported.  

When you call niDMM Config Measurement , NI-DMM sets this property to
IVIDMM Mode. When you call niDMM Configure Waveform Acquisition , NI-DMM
sets this property to Waveform Mode. If you are programming properties
directly, you must set this property before setting other configuration
properties.

''',
        'longDescription': '''
Specifies how the DMM acquires data.

.. note::
   The NI 4050 and NI 4060 are not supported.  

When you call niDMM Config Measurement , NI-DMM sets this property to
IVIDMM Mode. When you call niDMM Configure Waveform Acquisition , NI-DMM
sets this property to Waveform Mode. If you are programming properties
directly, you must set this property before setting other configuration
properties.

This corresponds to LabVIEW property **Configuration:Advanced:Operation
Mode**

+-------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name                    | Description                                                                                                                                                                                                                                        |
+-------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **IVIDMM Mode** (0)     | Single or multipoint measurements: When the Trigger Count and Sample Count properties are both set to 1, the NI 4065, NI 4070/4071/4072, and NI 4080/4081/4082 take a single-point measurement; otherwise, NI-DMM takes multipoint measurements.   |
+-------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Waveform Mode** (1)   | Configures the NI 4080/4081/4082 and NI 4070/4071/4072 to take waveform measurements.                                                                                                                                                              |
+-------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1150018': {
        'shortDescription': '''
Specifies the rate of the waveform acquisition in samples per second
(S/s). The valid rate is calculated by dividing 1,800,000 by an integer
divisor, and the rate falls between 10 and 1,800,000 samples per second.
The waveform rate is coerced upwards to the next valid rate. The default
value is 1,800,000 samples per second. Not supported by NI 4065.

''',
        'longDescription': '''
Specifies the rate of the waveform acquisition in samples per second
(S/s). The valid rate is calculated by dividing 1,800,000 by an integer
divisor, and the rate falls between 10 and 1,800,000 samples per second.
The waveform rate is coerced upwards to the next valid rate. The default
value is 1,800,000 samples per second. Not supported by NI 4065.

This corresponds to LabVIEW property **Waveform Acquisition:Waveform
Rate**

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 64-bit floating point   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1150019': {
        'shortDescription': '''
For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the number of
points to acquire in a waveform acquisition.

''',
        'longDescription': '''
For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the number of
points to acquire in a waveform acquisition.

This corresponds to LabVIEW property **Waveform Acquisition:Waveform
Points**

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1150022': {
        'shortDescription': '''
For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the ADC
calibration mode.

''',
        'longDescription': '''
For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the ADC
calibration mode.

This corresponds to LabVIEW property **Configuration:Measurement
Options:ADC Calibration**

+-----------------+------------------------------------------------------------------------------------------------+
| Name            | Description                                                                                    |
+-----------------+------------------------------------------------------------------------------------------------+
| **Auto** (-1)   | The DMM enables or disables ADC calibration based on the configured function and resolution.   |
+-----------------+------------------------------------------------------------------------------------------------+
| **Off** (0)     | The DMM does not compensate for changes to the gain.                                           |
+-----------------+------------------------------------------------------------------------------------------------+
| **On** (1)      | The DMM measures an internal reference to calculate the correct gain for the measurement.      |
+-----------------+------------------------------------------------------------------------------------------------+

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1150023': {
        'shortDescription': '''
For the NI 4080/4081/4082 and NI 4070/4071/4072, enables or disables
offset compensated ohms.

''',
        'longDescription': '''
For the NI 4080/4081/4082 and NI 4070/4071/4072, enables or disables
offset compensated ohms.

This corresponds to LabVIEW property **Configuration:Measurement
Options:Offset Compensated Ohms**

+---------------+-------------------------------------+
| Name          | Description                         |
+---------------+-------------------------------------+
| **Off** (0)   | Disables Offset Compensated Ohms.   |
+---------------+-------------------------------------+
| **On** (1)    | Enables Offset Compensated Ohms.    |
+---------------+-------------------------------------+

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1150025': {
        'shortDescription': '''
Specifies the current source provided during diode measurements.

The NI 4050 and NI 4060 are not supported.

''',
        'longDescription': '''
Specifies the current source provided during diode measurements.

The NI 4050 and NI 4060 are not supported.

This corresponds to LabVIEW property **Configuration:Measurement
Options:Current Source**

+----------------------------------+--------------------------------------------------------------------+
| Name                             | Description                                                        |
+----------------------------------+--------------------------------------------------------------------+
| **1 Microamp** (1.000000E-6)     | NI 4070/4071/4072 are supported.                                   |
+----------------------------------+--------------------------------------------------------------------+
| **10 Microamp** (1.000000E-5)    | NI 4080/4081/4082 and NI 4070/4071/4072 are supported.             |
+----------------------------------+--------------------------------------------------------------------+
| **100 Microamp** (1.000000E-4)   | NI 4080/4081/4082, NI 4070/4071/4072, and NI 4065 are supported.   |
+----------------------------------+--------------------------------------------------------------------+
| **1 Milliamp** (1.000000E-3)     | NI 4080/4081/4082, NI 4070/4071/4072, and NI 4065 are supported.   |
+----------------------------------+--------------------------------------------------------------------+

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 64-bit floating point   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1150026': {
        'shortDescription': '''
Specifies the DC noise rejection mode.

''',
        'longDescription': '''
Specifies the DC noise rejection mode.

This corresponds to LabVIEW property **Configuration:Measurement
Options:DC Noise Rejection**

.. note::
   The NI 4050 and NI 4060 are not supported.  

+------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name                   | Description                                                                                                                                                                        |
+------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Auto** (-1)          | The driver chooses the DC noise rejection setting based on the configured function and resolution.                                                                                 |
+------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Normal** (0)         | NI-DMM weighs all samples equally.                                                                                                                                                 |
+------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Second Order** (1)   | NI-DMM weighs the samples taken in the middle of the aperture time more than samples taken at the beginning and the end of the measurement using a triangular weighing function.   |
+------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **High Order** (2)     | NI-DMM weighs the samples taken in the middle of the aperture time more than samples taken at the beginning and the end of the measurement using a bell-curve weighing function.   |
+------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1150027': {
        'shortDescription': '''
For the NI 4080/4081/4082 and NI 4070/4071/4072 only, specifies the
coupling during a waveform acquisition.

''',
        'longDescription': '''
For the NI 4080/4081/4082 and NI 4070/4071/4072 only, specifies the
coupling during a waveform acquisition.

This corresponds to LabVIEW property **Waveform Acquisition:Waveform
Coupling**

+--------------+--------------------------+
| Name         | Description              |
+--------------+--------------------------+
| **AC** (0)   | Specifies AC coupling.   |
+--------------+--------------------------+
| **DC** (1)   | Specifies DC coupling.   |
+--------------+--------------------------+

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1150028': {
        'shortDescription': '''
Specifies the settling time in seconds. Use this property to override
the default settling time. To return to the default, set this property
to Auto (-1).

''',
        'longDescription': '''
Specifies the settling time in seconds. Use this property to override
the default settling time. To return to the default, set this property
to Auto (-1).

This corresponds to LabVIEW property **Configuration:Advanced:Settle
Time**

.. note::
   The NI 4050 and NI 4060 are not supported.  

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 64-bit floating point   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1150029': {
        'shortDescription': '''
Specifies the input resistance of the instrument.

''',
        'longDescription': '''
Specifies the input resistance of the instrument.

This corresponds to LabVIEW property **Configuration:Measurement
Options:Input Resistance**

.. note::
   The NI 4050 and NI 4060 are not supported.  

+--------------------------------------------+------------------------------------------+
| Name                                       | Description                              |
+--------------------------------------------+------------------------------------------+
| **1 M Ohm** (1.000000E+6)                  | Input resistance of 1 M Ohm              |
+--------------------------------------------+------------------------------------------+
| **10 M Ohm** (1.000000E+7)                 | Input resistance of 10 M Ohm             |
+--------------------------------------------+------------------------------------------+
| **Greater Than 10 G Ohm** (1.000000E+10)   | Input resistance greater than 10 G Ohm   |
+--------------------------------------------+------------------------------------------+

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 64-bit floating point   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1150031': {
        'shortDescription': '''
For the NI 4060 only, specifies a delay interval after a sample trigger.

''',
        'longDescription': '''
For the NI 4060 only, specifies a delay interval after a sample trigger.

This corresponds to LabVIEW property **Multi Point Acquisition:Sample
Delay Mode**

+-----+---------------------+-----------------------------------------------------------------------------------------+
| 0   | IVI compliant       | The Sample Interval property is only used when the Sample Trigger is set to Interval.   |
+-----+---------------------+-----------------------------------------------------------------------------------------+
| 1   | Not IVI compliant   | The Sample Interval property is used as a delay after any type of Sample Trigger.       |
+-----+---------------------+-----------------------------------------------------------------------------------------+

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1150032': {
        'shortDescription': '''
Specifies the number of averages to perform in a measurement. For the NI
4080/4081/4082 and NI 4070/4071/4072, applies only when the aperture
time is not set to Auto and Auto Zero is ON. The Number of Averages
Property will be ignored otherwise. The default is 4 for 7 1/2 digits;
otherwise, the default is 1.

The NI 4050 and NI 4060 are not supported.

''',
        'longDescription': '''
Specifies the number of averages to perform in a measurement. For the NI
4080/4081/4082 and NI 4070/4071/4072, applies only when the aperture
time is not set to Auto and Auto Zero is ON. The Number of Averages
Property will be ignored otherwise. The default is 4 for 7 1/2 digits;
otherwise, the default is 1.

The NI 4050 and NI 4060 are not supported.

This corresponds to LabVIEW property **Configuration:Advanced:Number Of
Averages**

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1150034': {
        'shortDescription': '''
Specifies the number of measurements transferred at a time from the
instrument to an internal buffer. When set to Auto (-1), NI-DMM chooses
the transfer size.

''',
        'longDescription': '''
Specifies the number of measurements transferred at a time from the
instrument to an internal buffer. When set to Auto (-1), NI-DMM chooses
the transfer size.

This corresponds to LabVIEW property **Multi Point
Acquisition:Advanced:Latency**

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1150037': {
        'shortDescription': '''
Specifies the size in samples of the internal data buffer. Maximum size
is 134,217,727 (0X7FFFFFF) samples. When set to Auto (-1), NI-DMM
chooses the buffer size.

''',
        'longDescription': '''
Specifies the size in samples of the internal data buffer. Maximum size
is 134,217,727 (0X7FFFFFF) samples. When set to Auto (-1), NI-DMM
chooses the buffer size.

This corresponds to LabVIEW property **Multi Point
Acquisition:Advanced:Buffer Size**

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1150044': {
        'shortDescription': '''
For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the value of
the frequency voltage range. If auto ranging is enabled, shows the
actual value of the active frequency voltage range. If not Auto Ranging,
the value is the same as that of the Frequency Voltage Range property.

''',
        'longDescription': '''
For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the value of
the frequency voltage range. If auto ranging is enabled, shows the
actual value of the active frequency voltage range. If not Auto Ranging,
the value is the same as that of the Frequency Voltage Range property.

This corresponds to LabVIEW property **Configuration:Measurement
Options:Frequency Voltage Auto Range Value**

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 64-bit floating point   |
+------------------+-------------------------+
| Permissions      | Read Only               |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1150045': {
        'shortDescription': '''
For the NI 4081 and NI 4072 only, specifies the type of cable
compensation that is applied to the current capacitance or inductance
measurement for the current range.

''',
        'longDescription': '''
For the NI 4081 and NI 4072 only, specifies the type of cable
compensation that is applied to the current capacitance or inductance
measurement for the current range.

This corresponds to LabVIEW property **Configuration:Measurement
Options:Capacitance and Inductance:Cable Compensation Type**

.. note::
   Changing the function or the range using property nodes or through niDMM Config Measurement resets this property to the default value.  

+----------------------------+--------------------------------------+
| Name                       | Description                          |
+----------------------------+--------------------------------------+
| **None** (0)               | No cable compensation.               |
+----------------------------+--------------------------------------+
| **Open** (1)               | Open cable compensation.             |
+----------------------------+--------------------------------------+
| **Short** (2)              | Short cable compensation.            |
+----------------------------+--------------------------------------+
| **Open\_and\_Short** (3)   | Open and short cable compensation.   |
+----------------------------+--------------------------------------+

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1150046': {
        'shortDescription': '''
For the NI 4082 and NI 4072 only, represents the reactive part
(reactance) of the short cable compensation. The valid range is any real
number >0. The default value (-1) indicates that compensation has not
taken place.

''',
        'longDescription': '''
For the NI 4082 and NI 4072 only, represents the reactive part
(reactance) of the short cable compensation. The valid range is any real
number >0. The default value (-1) indicates that compensation has not
taken place.

This corresponds to LabVIEW property **Configuration:Measurement
Options:Capacitance and Inductance:Short Cable Compensation
Values:Reactance**

.. note::
   Changing the VI or the range through this property or through niDMM Config Measurement resets this property to the default value.  

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 64-bit floating point   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1150047': {
        'shortDescription': '''
For the NI 4082 and NI 4072 only, represents the active part
(resistance) of the short cable compensation. The valid range is any
real number >0. The default value (-1) indicates that compensation has
not taken place.

''',
        'longDescription': '''
For the NI 4082 and NI 4072 only, represents the active part
(resistance) of the short cable compensation. The valid range is any
real number >0. The default value (-1) indicates that compensation has
not taken place.

This corresponds to LabVIEW property **Configuration:Measurement
Options:Capacitance and Inductance:Short Cable Compensation
Values:Resistance**

.. note::
   Changing the VI or the range through this property or through niDMM Config Measurement resets this property to the default value.  

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 64-bit floating point   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1150048': {
        'shortDescription': '''
For the NI 4082 and NI 4072 only, specifies the reactive part
(susceptance) of the open cable compensation. The valid range is any
real number >0. The default value (-1.0) indicates that compensation has
not taken place.

''',
        'longDescription': '''
For the NI 4082 and NI 4072 only, specifies the reactive part
(susceptance) of the open cable compensation. The valid range is any
real number >0. The default value (-1.0) indicates that compensation has
not taken place.

This corresponds to LabVIEW property **Configuration:Measurement
Options:Capacitance and Inductance:Open Cable Compensation
Values:Susceptance**

.. note::
   Changing the function or the range using property nodes or through niDMM Config Measurement resets this property to the default value.  

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 64-bit floating point   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1150049': {
        'shortDescription': '''
For the NI 4082 and NI 4072 only, specifies the active part
(conductance) of the open cable compensation. The valid range is any
real number >0. The default value (-1.0) indicates that compensation has
not taken place.

''',
        'longDescription': '''
For the NI 4082 and NI 4072 only, specifies the active part
(conductance) of the open cable compensation. The valid range is any
real number >0. The default value (-1.0) indicates that compensation has
not taken place.

This corresponds to LabVIEW property **Configuration:Measurement
Options:Capacitance and Inductance:Open Cable Compensation
Values:Conductance**

.. note::
   Changing the function or the range using property nodes or through niDMM Config Measurement resets this property to the default value.  

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 64-bit floating point   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1150052': {
        'shortDescription': '''
For the NI 4082 and NI 4072 only, specifies the type of algorithm that
the measurement processing uses for capacitance and inductance
measurements.

''',
        'longDescription': '''
For the NI 4082 and NI 4072 only, specifies the type of algorithm that
the measurement processing uses for capacitance and inductance
measurements.

This corresponds to LabVIEW property **Configuration:Measurement
Options:Capacitance and Inductance:Advanced:Calculation Model**

+--------------------+--------------------------------------------------------------------------------------+
| Name               | Description                                                                          |
+--------------------+--------------------------------------------------------------------------------------+
| **Auto** (-1)      | NI-DMM chooses the algorithm based on function and range.                            |
+--------------------+--------------------------------------------------------------------------------------+
| **Series** (0)     | NI-DMM uses the series impedance model to calculate capacitance and inductance.      |
+--------------------+--------------------------------------------------------------------------------------+
| **Parallel** (1)   | NI-DMM uses the parallel admittance model to calculate capacitance and inductance.   |
+--------------------+--------------------------------------------------------------------------------------+

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1150053': {
        'shortDescription': '''
For the NI 4082 and NI 4072 only, controls the available DC bias for
capacitance measurements.

''',
        'longDescription': '''
For the NI 4082 and NI 4072 only, controls the available DC bias for
capacitance measurements.

This corresponds to LabVIEW property **Configuration:Measurement
Options:Capacitance and Inductance:Advanced:DC Bias**

+-----------------------+------------------------------------------------------+
| Name                  | Description                                          |
+-----------------------+------------------------------------------------------+
| **DC Bias Off** (0)   | NI-DMM programs the device not to use the DC bias.   |
+-----------------------+------------------------------------------------------+
| **DC Bias On** (1)    | NI-DMM programs the device to use the DC bias.       |
+-----------------------+------------------------------------------------------+

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1150054': {
        'shortDescription': '''
A string containing the serial number of the instrument. This property
corresponds to the serial number label that is attached to most
products.

''',
        'longDescription': '''
A string containing the serial number of the instrument. This property
corresponds to the serial number label that is attached to most
products.

This corresponds to LabVIEW property **Inherent IVI
Attributes:Instrument Identification:Instrument Serial Number**

The following table lists the characteristics of this property.

+------------------+-------------+
| Characteristic   | Value       |
+------------------+-------------+
| Datatype         | string      |
+------------------+-------------+
| Permissions      | Read Only   |
+------------------+-------------+
| High Level VI    | N/A         |
+------------------+-------------+
| Channel Based    | False       |
+------------------+-------------+
| Resettable       | No          |
+------------------+-------------+

''',
    },
    '1150055': {
        'shortDescription': '''
For the NI 4082 and NI 4072 only, specifies the number of LC
measurements that are averaged to produce one reading.

''',
        'longDescription': '''
For the NI 4082 and NI 4072 only, specifies the number of LC
measurements that are averaged to produce one reading.

This corresponds to LabVIEW property **Configuration:Measurement
Options:Capacitance and Inductance:Number of LC Measurements To
Average**

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1150061': {
        'shortDescription': '''
The PCI product ID.

''',
        'longDescription': '''
The PCI product ID.

This corresponds to LabVIEW property **Inherent IVI
Attributes:Instrument Identification:Instrument Product ID**

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read Only               |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1150120': {
        'shortDescription': '''
Specifies the RTD type.

''',
        'longDescription': '''
Specifies the RTD type.

This corresponds to LabVIEW property **Configuration:Measurement
Options:Temperature:Resistance Temperature Detector:RTD Type**

+-------------------+----------------------------------------------------------------------------------------------+
| Name              | Description                                                                                  |
+-------------------+----------------------------------------------------------------------------------------------+
| **Custom** (0)    | Performs Callendar-Van Dusen RTD scaling with the user-specified A, B, and C coefficients.   |
+-------------------+----------------------------------------------------------------------------------------------+
| **Pt 3750** (1)   | Performs scaling for a Pt 3750 RTD.                                                          |
+-------------------+----------------------------------------------------------------------------------------------+
| **Pt 3851** (2)   | Performs scaling for a Pt 3851 RTD.                                                          |
+-------------------+----------------------------------------------------------------------------------------------+
| **Pt 3911** (3)   | Performs scaling for a Pt 3911 RTD.                                                          |
+-------------------+----------------------------------------------------------------------------------------------+
| **Pt 3916** (4)   | Performs scaling for a Pt 3916 RTD.                                                          |
+-------------------+----------------------------------------------------------------------------------------------+
| **Pt 3920** (5)   | Performs scaling for a Pt 3920 RTD.                                                          |
+-------------------+----------------------------------------------------------------------------------------------+
| **Pt 3928** (6)   | Performs scaling for a Pt 3928 RTD.                                                          |
+-------------------+----------------------------------------------------------------------------------------------+

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1150121': {
        'shortDescription': '''
Specifies the Callendar-Van Dusen A coefficient for RTD scaling when the
**RTD Type property** is set to Custom.

''',
        'longDescription': '''
Specifies the Callendar-Van Dusen A coefficient for RTD scaling when the
**RTD Type property** is set to Custom.

This corresponds to LabVIEW property **Configuration:Measurement
Options:Temperature:Resistance Temperature Detector:RTD A**

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 64-bit floating point   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1150122': {
        'shortDescription': '''
Specifies the Callendar-Van Dusen B coefficient for RTD scaling when the
**RTD Type property** is set to Custom.

''',
        'longDescription': '''
Specifies the Callendar-Van Dusen B coefficient for RTD scaling when the
**RTD Type property** is set to Custom.

This corresponds to LabVIEW property **Configuration:Measurement
Options:Temperature:Resistance Temperature Detector:RTD B**

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 64-bit floating point   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1150123': {
        'shortDescription': '''
Specifies the Callendar-Van Dusen C coefficient for RTD scaling when the
**RTD Type property** is set to Custom.

''',
        'longDescription': '''
Specifies the Callendar-Van Dusen C coefficient for RTD scaling when the
**RTD Type property** is set to Custom.

This corresponds to LabVIEW property **Configuration:Measurement
Options:Temperature:Resistance Temperature Detector:RTD C**

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 64-bit floating point   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1150124': {
        'shortDescription': '''
Specifies the thermistor type.

''',
        'longDescription': '''
Specifies the thermistor type.

This corresponds to LabVIEW property **Configuration:Measurement
Options:Temperature:Thermistor:Thermistor Type**

+------------------+------------------------------------------------------------------------------------------------+
| Name             | Description                                                                                    |
+------------------+------------------------------------------------------------------------------------------------+
| **Custom** (0)   | Performs Steinhart-Hart thermistor scaling with the user-specified A, B, and C coefficients.   |
+------------------+------------------------------------------------------------------------------------------------+
| **44004** (1)    | Performs scaling for an Omega Series 44004 thermistor.                                         |
+------------------+------------------------------------------------------------------------------------------------+
| **44006** (2)    | Performs scaling for an Omega Series 44006 thermistor.                                         |
+------------------+------------------------------------------------------------------------------------------------+
| **44007** (3)    | Performs scaling for an Omega Series 44007 thermistor.                                         |
+------------------+------------------------------------------------------------------------------------------------+

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1150125': {
        'shortDescription': '''
Specifies the Steinhart-Hart A coefficient for thermistor scaling when
the **Thermistor Type property** is set to Custom.

''',
        'longDescription': '''
Specifies the Steinhart-Hart A coefficient for thermistor scaling when
the **Thermistor Type property** is set to Custom.

This corresponds to LabVIEW property **Configuration:Measurement
Options:Temperature:Thermistor:Thermistor A**

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 64-bit floating point   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1150126': {
        'shortDescription': '''
Specifies the Steinhart-Hart B coefficient for thermistor scaling when
the **Thermistor Type property** is set to Custom.

''',
        'longDescription': '''
Specifies the Steinhart-Hart B coefficient for thermistor scaling when
the **Thermistor Type property** is set to Custom.

This corresponds to LabVIEW property **Configuration:Measurement
Options:Temperature:Thermistor:Thermistor B**

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 64-bit floating point   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1150127': {
        'shortDescription': '''
Specifies the Steinhart-Hart C coefficient for thermistor scaling when
the **Thermistor Type property** is set to Custom.

''',
        'longDescription': '''
Specifies the Steinhart-Hart C coefficient for thermistor scaling when
the **Thermistor Type property** is set to Custom.

This corresponds to LabVIEW property **Configuration:Measurement
Options:Temperature:Thermistor:Thermistor C**

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 64-bit floating point   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1250001': {
        'shortDescription': '''
Specifies the measurement function. If you are setting this property
directly, you must also set the Operation Mode property, which controls
whether the DMM takes standard single or multipoint measurements, or
acquires a waveform. If you are programming properties directly, you
must set the Operation Mode property before setting other configuration
properties. If the Operation Mode property is set to Waveform Mode, the
only valid function types are Waveform Voltage and Waveform Current. Set
the Operation Mode property to IVIDMM Mode to set all other function
values.

''',
        'longDescription': '''
Specifies the measurement function. If you are setting this property
directly, you must also set the Operation Mode property, which controls
whether the DMM takes standard single or multipoint measurements, or
acquires a waveform. If you are programming properties directly, you
must set the Operation Mode property before setting other configuration
properties. If the Operation Mode property is set to Waveform Mode, the
only valid function types are Waveform Voltage and Waveform Current. Set
the Operation Mode property to IVIDMM Mode to set all other function
values.

This corresponds to LabVIEW property **Configuration:Function**

+----------------------------------+---------------------------------------------+
| Name                             | Description                                 |
+----------------------------------+---------------------------------------------+
| **DC Volts** (1)                 | All devices supported.                      |
+----------------------------------+---------------------------------------------+
| **AC Volts** (2)                 | All devices supported.                      |
+----------------------------------+---------------------------------------------+
| **DC Current** (3)               | All devices supported.                      |
+----------------------------------+---------------------------------------------+
| **AC Current** (4)               | All devices supported.                      |
+----------------------------------+---------------------------------------------+
| **2-Wire Resistance** (5)        | All devices supported.                      |
+----------------------------------+---------------------------------------------+
| **4-Wire Resistance** (101)      | NI 4065, and NI 4070/4071/4072 supported.   |
+----------------------------------+---------------------------------------------+
| **Frequency** (104)              | NI 4070/4071/4072 supported.                |
+----------------------------------+---------------------------------------------+
| **Period** (105)                 | NI 4070/4071/4072 supported.                |
+----------------------------------+---------------------------------------------+
| **AC Volts DC Coupled** (1001)   | NI 4070/4071/4072 supported.                |
+----------------------------------+---------------------------------------------+
| **Diode** (1002)                 | All devices supported.                      |
+----------------------------------+---------------------------------------------+
| **Waveform Voltage** (1003)      | NI 4070/4071/4072 supported.                |
+----------------------------------+---------------------------------------------+
| **Waveform Current** (1004)      | NI 4070/4071/4072 supported.                |
+----------------------------------+---------------------------------------------+
| **Capacitance** (1005)           | NI 4072 supported.                          |
+----------------------------------+---------------------------------------------+
| **Inductance** (1006)            | NI 4072 supported.                          |
+----------------------------------+---------------------------------------------+
| **Temperature** (108)            | NI 4065, and NI 4070/4071/4072 supported.   |
+----------------------------------+---------------------------------------------+

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1250002': {
        'shortDescription': '''
Specifies the measurement range. Use positive values to represent the
absolute value of the maximum expected measurement. The value is in
units appropriate for the current value of the Function property. For
example, if the Function property is set to DC Volts, the units are
volts.

''',
        'longDescription': '''
Specifies the measurement range. Use positive values to represent the
absolute value of the maximum expected measurement. The value is in
units appropriate for the current value of the Function property. For
example, if the Function property is set to DC Volts, the units are
volts.

This corresponds to LabVIEW property **Configuration:Range**

.. note::
   The NI 4050, NI 4060, and NI 4065 only support Auto Range when the trigger and sample trigger are set to Immediate.  

+----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| (-1.0)   | Auto Range On     | NI-DMM performs an Auto Range before acquiring the measurement.                                                                                                                                |
+----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| (-2.0)   | Auto Range Off    | NI-DMM sets the Range to the current Auto Range Value and uses this range for all subsequent measurements until the measurement configuration is changed.                                      |
+----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| (-3.0)   | Auto Range Once   | NI-DMM performs an Auto Range before acquiring the next measurement. The Auto Range Value is stored and used for all subsequent measurements until the measurement configuration is changed.   |
+----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 64-bit floating point   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1250003': {
        'shortDescription': '''
Specifies the measurement resolution in digits. Setting this property to
higher values increases the measurement accuracy. Setting this property
to lower values increases the measurement speed.

''',
        'longDescription': '''
Specifies the measurement resolution in digits. Setting this property to
higher values increases the measurement accuracy. Setting this property
to lower values increases the measurement speed.

This corresponds to LabVIEW property **Configuration:Digits Resolution**

.. note::
   NI-DMM ignores this property for capacitance and inductance measurements on the NI 4082 and NI 4072. To achieve better resolution for such measurements, use the Number of LC Measurements to Average property.  

+--------------------------+------------------------------------+
| Name                     | Description                        |
+--------------------------+------------------------------------+
| **3.5** (3.5000000E+0)   | Specifies 3.5 digits resolution.   |
+--------------------------+------------------------------------+
| **4.5** (4.500000E+0)    | Specifies 4.5 digits resolution.   |
+--------------------------+------------------------------------+
| **5.5** (5.500000E+0)    | Specifies 5.5 digits resolution.   |
+--------------------------+------------------------------------+
| **6.5** (6.500000E+0)    | Specifies 6.5 digits resolution.   |
+--------------------------+------------------------------------+
| **7.5** (7.500000E+0)    | Specifies 7.5 digits resolution.   |
+--------------------------+------------------------------------+

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 64-bit floating point   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1250004': {
        'shortDescription': '''
Specifies the trigger source. When niDMM Initiate is called, the DMM
waits for the trigger specified with this property. After it receives
the trigger, the DMM waits the length of time specified with the Trigger
Delay property. The DMM then takes a measurement.

To determine which values are supported by each device, refer to the
LabVIEW Trigger Routing section in the *NI Digital Multimeters Help* .

''',
        'longDescription': '''
Specifies the trigger source. When niDMM Initiate is called, the DMM
waits for the trigger specified with this property. After it receives
the trigger, the DMM waits the length of time specified with the Trigger
Delay property. The DMM then takes a measurement.

To determine which values are supported by each device, refer to the
LabVIEW Trigger Routing section in the *NI Digital Multimeters Help* .

This corresponds to LabVIEW property **Trigger:Trigger Source**

+--------------------------+-------------------------------------------------------------------------------------------------------------------+
| Name                     | Description                                                                                                       |
+--------------------------+-------------------------------------------------------------------------------------------------------------------+
| **Immediate** (1)        | No trigger specified.                                                                                             |
+--------------------------+-------------------------------------------------------------------------------------------------------------------+
| **External** (2)         | Pin 9 on the AUX Connector                                                                                        |
+--------------------------+-------------------------------------------------------------------------------------------------------------------+
| **Software Trig** (3)    | Waits until \`niDMM Send Software Trigger <dmmviref.chm::/niDMM\_Send\_Software\_Trigger.html>\`\_\_ is called.   |
+--------------------------+-------------------------------------------------------------------------------------------------------------------+
| **TTL 0** (111)          | PXI Trigger Line 0                                                                                                |
+--------------------------+-------------------------------------------------------------------------------------------------------------------+
| **TTL 1** (112)          | PXI Trigger Line 1                                                                                                |
+--------------------------+-------------------------------------------------------------------------------------------------------------------+
| **TTL 2** (113)          | PXI Trigger Line 2                                                                                                |
+--------------------------+-------------------------------------------------------------------------------------------------------------------+
| **TTL 3** (114)          | PXI Trigger Line 3                                                                                                |
+--------------------------+-------------------------------------------------------------------------------------------------------------------+
| **TTL 4** (115)          | PXI Trigger Line 4                                                                                                |
+--------------------------+-------------------------------------------------------------------------------------------------------------------+
| **TTL 5** (116)          | PXI Trigger Line 5                                                                                                |
+--------------------------+-------------------------------------------------------------------------------------------------------------------+
| **TTL 6** (117)          | PXI Trigger Line 6                                                                                                |
+--------------------------+-------------------------------------------------------------------------------------------------------------------+
| **TTL 7** (118)          | PXI Trigger Line 7                                                                                                |
+--------------------------+-------------------------------------------------------------------------------------------------------------------+
| **PXI Star** (131)       | PXI Star Trigger Line                                                                                             |
+--------------------------+-------------------------------------------------------------------------------------------------------------------+
| **LBR Trig 1** (1004)    | Local Bus Right Trigger Line 1 of PXI/SCXI combination chassis                                                    |
+--------------------------+-------------------------------------------------------------------------------------------------------------------+
| **AUX\_Trig 1** (1001)   | Pin 3 on the AUX connector                                                                                        |
+--------------------------+-------------------------------------------------------------------------------------------------------------------+

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1250005': {
        'shortDescription': '''
Specifies the time (in seconds) that the DMM waits after it has received
a trigger before taking a measurement. The default value is Auto Delay
(-1), which means that the DMM waits an appropriate settling time before
taking the measurement.

The NI 4080/4081/4082 uses the value specified in this property as
additional settling time. The valid range for Trigger Delay is Auto
Delay (-1) or 0.0 - 150.0 seconds, and the onboard timing resolution is
10.0 ns.

The NI 4065 and NI 4070/4071/4072 use the value specified in this
property as additional settling time. For these devices, the valid range
for Trigger Delay is Auto Delay (-1) or 0.0 - 149.0 seconds and the
onboard timing resolution is 34.72 ns.

On the NI 4060, if this property is set to 0, the DMM does not settle
before taking the measurement. On the NI 4060, the valid range for
Trigger Delay (-1) is 0.0-12.0 seconds and the onboard timing resolution
is 100 ms.

When using the NI 4050, this property must be set to Auto Delay (-1).

Use positive values to set the trigger delay in seconds.

Valid Range: Auto Delay (-1.0), 0.0-12.0 seconds (NI 4060 only),
0.0-149.0 seconds (NI 4065 and NI 4070/4071/4072)

Default Value: Auto Delay

''',
        'longDescription': '''
Specifies the time (in seconds) that the DMM waits after it has received
a trigger before taking a measurement. The default value is Auto Delay
(-1), which means that the DMM waits an appropriate settling time before
taking the measurement.

The NI 4080/4081/4082 uses the value specified in this property as
additional settling time. The valid range for Trigger Delay is Auto
Delay (-1) or 0.0 - 150.0 seconds, and the onboard timing resolution is
10.0 ns.

The NI 4065 and NI 4070/4071/4072 use the value specified in this
property as additional settling time. For these devices, the valid range
for Trigger Delay is Auto Delay (-1) or 0.0 - 149.0 seconds and the
onboard timing resolution is 34.72 ns.

On the NI 4060, if this property is set to 0, the DMM does not settle
before taking the measurement. On the NI 4060, the valid range for
Trigger Delay (-1) is 0.0-12.0 seconds and the onboard timing resolution
is 100 ms.

When using the NI 4050, this property must be set to Auto Delay (-1).

Use positive values to set the trigger delay in seconds.

Valid Range: Auto Delay (-1.0), 0.0-12.0 seconds (NI 4060 only),
0.0-149.0 seconds (NI 4065 and NI 4070/4071/4072)

Default Value: Auto Delay

This corresponds to LabVIEW property **Trigger:Trigger Delay**

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 64-bit floating point   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1250006': {
        'shortDescription': '''
Specifies the minimum frequency component of the input signal for AC
measurements. This property affects the DMM only when you set the
Function property to AC measurements. The valid range is 1 Hz-300 kHz
for the NI 4080/4081/4082 and NI 4070/4071/4072, 10 Hz-100 Hz for the NI
4065, and 20 Hz-25 kHz for the NI 4050 and NI 4060.

''',
        'longDescription': '''
Specifies the minimum frequency component of the input signal for AC
measurements. This property affects the DMM only when you set the
Function property to AC measurements. The valid range is 1 Hz-300 kHz
for the NI 4080/4081/4082 and NI 4070/4071/4072, 10 Hz-100 Hz for the NI
4065, and 20 Hz-25 kHz for the NI 4050 and NI 4060.

This corresponds to LabVIEW property **Configuration:Measurement
Options:Min Frequency**

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 64-bit floating point   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1250007': {
        'shortDescription': '''
Specifies the maximum frequency component of the input signal for AC
measurements. This property is used only for error checking and verifies
that the value of this parameter is less than the maximum frequency of
the device. This property affects the DMM only when you set the Function
property to AC measurements.

''',
        'longDescription': '''
Specifies the maximum frequency component of the input signal for AC
measurements. This property is used only for error checking and verifies
that the value of this parameter is less than the maximum frequency of
the device. This property affects the DMM only when you set the Function
property to AC measurements.

This corresponds to LabVIEW property **Configuration:Measurement
Options:Max Frequency**

The valid ranges are shown in the following table.

+----------------------------------------+----------------+
| NI 4080/4081/4082, NI 4070/4071/4072   | 1 Hz-300 kHz   |
+----------------------------------------+----------------+
| NI 4065                                | 10 Hz-100 Hz   |
+----------------------------------------+----------------+
| NI 4050/4060                           | 20 Hz-25 kHz   |
+----------------------------------------+----------------+

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 64-bit floating point   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1250008': {
        'shortDescription': '''
Specifies the measurement resolution in absolute units. Setting this
property to higher values increases the measurement accuracy. Setting
this property to lower values increases the measurement speed.

''',
        'longDescription': '''
Specifies the measurement resolution in absolute units. Setting this
property to higher values increases the measurement accuracy. Setting
this property to lower values increases the measurement speed.

This corresponds to LabVIEW property **Configuration:Absolute
Resolution**

.. note::
   NI-DMM ignores this property for capacitance and inductance measurements on the NI 4082 and NI 4072. To achieve better resolution for such measurements, use the Number of LC Measurements to Average property.  

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 64-bit floating point   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1250101': {
        'shortDescription': '''
For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the maximum
amplitude of the input signal for frequency measurements.

''',
        'longDescription': '''
For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the maximum
amplitude of the input signal for frequency measurements.

This corresponds to LabVIEW property **Configuration:Measurement
Options:Frequency Voltage Range**

+------------------+--------+------------------------------------------------------------------------------------------------------------------------------------+
| Auto Range On    | -1.0   | Configures the DMM to take an Auto Range measurement to calculate the voltage range before each frequency or period measurement.   |
+------------------+--------+------------------------------------------------------------------------------------------------------------------------------------+
| Auto Range Off   | -2.0   | Disables Auto Ranging. NI-DMM sets the voltage range to the last calculated voltage range.                                         |
+------------------+--------+------------------------------------------------------------------------------------------------------------------------------------+

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 64-bit floating point   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1250201': {
        'shortDescription': '''
Specifies the transducer type.

''',
        'longDescription': '''
Specifies the transducer type.

This corresponds to LabVIEW property **Configuration:Measurement
Options:Temperature:Transducer Type**

+------------------------+--------------------------------------+
| Name                   | Description                          |
+------------------------+--------------------------------------+
| **Thermocouple** (1)   | Use for thermocouple measurements.   |
+------------------------+--------------------------------------+
| **Thermistor** (2)     | Use for thermistor measurements.     |
+------------------------+--------------------------------------+
| **2-Wire RTD** (3)     | Use for 2-wire RTD measurements.     |
+------------------------+--------------------------------------+
| **4-Wire RTD** (4)     | Use for 4-wire RTD measurements.     |
+------------------------+--------------------------------------+

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1250231': {
        'shortDescription': '''
Specifies the thermocouple type.

''',
        'longDescription': '''
Specifies the thermocouple type.

This corresponds to LabVIEW property **Configuration:Measurement
Options:Temperature:Thermocouple:Thermocouple Type**

+--------------+-----------------------+
| Name         | Description           |
+--------------+-----------------------+
| **B** (1)    | Thermocouple type B   |
+--------------+-----------------------+
| **E** (4)    | Thermocouple type E   |
+--------------+-----------------------+
| **J** (6)    | Thermocouple type J   |
+--------------+-----------------------+
| **K** (7)    | Thermocouple type K   |
+--------------+-----------------------+
| **N** (8)    | Thermocouple type N   |
+--------------+-----------------------+
| **R** (9)    | Thermocouple type R   |
+--------------+-----------------------+
| **S** (10)   | Thermocouple type S   |
+--------------+-----------------------+
| **T** (11)   | Thermocouple type T   |
+--------------+-----------------------+

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1250232': {
        'shortDescription': '''
Specifies the thermocouple reference junction type.

''',
        'longDescription': '''
Specifies the thermocouple reference junction type.

This corresponds to LabVIEW property **Configuration:Measurement
Options:Temperature:Thermocouple:Reference Junction Type**

+-----------------+------------------------------------------------------------------------------+
| Name            | Description                                                                  |
+-----------------+------------------------------------------------------------------------------+
| **Fixed** (2)   | Thermocouple reference juction is fixed at the user-specified temperature.   |
+-----------------+------------------------------------------------------------------------------+

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1250233': {
        'shortDescription': '''
Specifies the value of the fixed reference junction temperature for a
thermocouple in degrees Celsius.

''',
        'longDescription': '''
Specifies the value of the fixed reference junction temperature for a
thermocouple in degrees Celsius.

This corresponds to LabVIEW property **Configuration:Measurement
Options:Temperature:Thermocouple:Fixed Reference Junction**

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 64-bit floating point   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1250242': {
        'shortDescription': '''
Specifies the RTD resistance at 0 degrees Celsius.

''',
        'longDescription': '''
Specifies the RTD resistance at 0 degrees Celsius.

This corresponds to LabVIEW property **Configuration:Measurement
Options:Temperature:Resistance Temperature Detector:RTD Resistance**

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 64-bit floating point   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1250301': {
        'shortDescription': '''
Specifies the number of measurements the DMM takes each time it receives
a trigger in a multiple point acquisition. Setting Sample Count to 0 on
the NI 4050 and NI 4060 causes the device to take continuous
measurements. Otherwise, setting Sample Count to 0 causes the
conditional statement "Measurements equal to Sample Count" to always
evaluate to False, and causes the DMM to continue taking measurements in
the inner loop.

''',
        'longDescription': '''
Specifies the number of measurements the DMM takes each time it receives
a trigger in a multiple point acquisition. Setting Sample Count to 0 on
the NI 4050 and NI 4060 causes the device to take continuous
measurements. Otherwise, setting Sample Count to 0 causes the
conditional statement "Measurements equal to Sample Count" to always
evaluate to False, and causes the DMM to continue taking measurements in
the inner loop.

This corresponds to LabVIEW property **Multi Point Acquisition:Sample
Count**

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1250302': {
        'shortDescription': '''
Specifies the sample trigger source.

To determine which values are supported by each device, refer to the
LabVIEW Trigger Routing section in the *NI Digital Multimeters Help* .

''',
        'longDescription': '''
Specifies the sample trigger source.

To determine which values are supported by each device, refer to the
LabVIEW Trigger Routing section in the *NI Digital Multimeters Help* .

This corresponds to LabVIEW property **Multi Point Acquisition:Sample
Trigger**

+-------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Name                    | Description                                                                                                                            |
+-------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| **Immediate** (1)       | No trigger specified                                                                                                                   |
+-------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| **Interval** (10)       | Interval trigger                                                                                                                       |
+-------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| **External** (2)        | Pin 9 on the AUX Connector                                                                                                             |
+-------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| **Software Trig** (3)   | Configures the DMM to wait until \`niDMM Send Software Trigger <dmmviref.chm::/niDMM\_Send\_Software\_Trigger.html>\`\_\_ is called.   |
+-------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| **TTL 0** (111)         | PXI Trigger Line 0                                                                                                                     |
+-------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| **TTL 1** (112)         | PXI Trigger Line 1                                                                                                                     |
+-------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| **TTL 2** (113)         | PXI Trigger Line 2                                                                                                                     |
+-------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| **TTL 3** (114)         | PXI Trigger Line 3                                                                                                                     |
+-------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| **TTL 4** (115)         | PXI Trigger Line 4                                                                                                                     |
+-------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| **TTL 5** (116)         | PXI Trigger Line 5                                                                                                                     |
+-------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| **TTL 6** (117)         | PXI Trigger Line 6                                                                                                                     |
+-------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| **TTL 7** (118)         | PXI Trigger Line 7                                                                                                                     |
+-------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| **PXI Star** (131)      | PXI Star trigger line                                                                                                                  |
+-------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| **LBR Trig 1** (1004)   | Local Bus Right Trigger Line 1 of PXI/SCXI combination chassis                                                                         |
+-------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| **AUX Trig 1** (1001)   | Pin 3 on the AUX connector                                                                                                             |
+-------------------------+----------------------------------------------------------------------------------------------------------------------------------------+

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1250303': {
        'shortDescription': '''
Specifies the amount of time in seconds the DMM waits between
measurement cycles. This property only applies when the Sample Trigger
property is set to INTERVAL. The default value (-1) ensures that the DMM
settles for a recommended time, which is the same as using an immediate
trigger.

''',
        'longDescription': '''
Specifies the amount of time in seconds the DMM waits between
measurement cycles. This property only applies when the Sample Trigger
property is set to INTERVAL. The default value (-1) ensures that the DMM
settles for a recommended time, which is the same as using an immediate
trigger.

This corresponds to LabVIEW property **Multi Point Acquisition:Sample
Interval**

The NI 4065 and NI 4070/4071/4072 use the value specified in this
property as additional delay. On these devices, the onboard timing
resolution is 34.72 ns and the valid range is 0-149 s.

On the NI 4060, the value for this property is used as the settling
time. When this property is set to 0, the NI 4060 does not settle
between measurement cycles. The onboard timing resolution is 1 micro s
on the NI 4060.

Only positive values are valid when setting the sample interval.

.. note::
   The NI 4080/4081/4082 and NI 4050 are not supported.  

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 64-bit floating point   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1250304': {
        'shortDescription': '''
Specifies the number of triggers the DMM receives before returning to
the Idle state. This property can be set to any positive ViInt32 value
for the NI 4065, NI 4070/4071/4072, and NI 4080/4081/4082.

The NI 4050/4060 only support this property being set to 1.

Refer to Multiple Point Acquisitions in the *NI Digital Multimeters
Help* for more information.

''',
        'longDescription': '''
Specifies the number of triggers the DMM receives before returning to
the Idle state. This property can be set to any positive ViInt32 value
for the NI 4065, NI 4070/4071/4072, and NI 4080/4081/4082.

The NI 4050/4060 only support this property being set to 1.

Refer to Multiple Point Acquisitions in the *NI Digital Multimeters
Help* for more information.

This corresponds to LabVIEW property **Multi Point Acquisition:Trigger
Count**

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1250305': {
        'shortDescription': '''
Specifies the destination of the measurement complete (MC) signal.

To determine which values are supported by each device, refer to the
LabVIEW Trigger Routing section in the *NI Digital Multimeters Help* .

''',
        'longDescription': '''
Specifies the destination of the measurement complete (MC) signal.

To determine which values are supported by each device, refer to the
LabVIEW Trigger Routing section in the *NI Digital Multimeters Help* .

This corresponds to LabVIEW property **Trigger:Measurement Complete
Dest**

.. note::
   The NI 4050 is not supported.  

+-------------------------+------------------------------------------------------------------+
| Name                    | Description                                                      |
+-------------------------+------------------------------------------------------------------+
| **None** (-1)           | No destination specified.                                        |
+-------------------------+------------------------------------------------------------------+
| **External** (2)        | Pin 6 on the AUX Connector                                       |
+-------------------------+------------------------------------------------------------------+
| **TTL 0** (111)         | PXI Trigger Line 0                                               |
+-------------------------+------------------------------------------------------------------+
| **TTL 1** (112)         | PXI Trigger Line 1                                               |
+-------------------------+------------------------------------------------------------------+
| **TL 2** (113)          | PXI Trigger Line 2                                               |
+-------------------------+------------------------------------------------------------------+
| **TTL 3** (114)         | PXI Trigger Line 3                                               |
+-------------------------+------------------------------------------------------------------+
| **TL 4** (115)          | PXI Trigger Line 4                                               |
+-------------------------+------------------------------------------------------------------+
| **TTL 5** (116)         | PXI Trigger Line 5                                               |
+-------------------------+------------------------------------------------------------------+
| **TTL 6** (117)         | PXI Trigger Line 6                                               |
+-------------------------+------------------------------------------------------------------+
| **TTL 7** (118)         | PXI Trigger Line 7                                               |
+-------------------------+------------------------------------------------------------------+
| **LBR Trig 0** (1003)   | Local Bus Right Trigger Line 0 of PXI/SCXI combination chassis   |
+-------------------------+------------------------------------------------------------------+

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1250321': {
        'shortDescription': '''
Specifies the measurement aperture time for the current configuration.
Aperture time is specified in units set by the Aperture Time Units
property. To override the default aperture, set this property to the
desired aperture time after calling niDMM Config Measurement . To return
to the default, set this property to Aperture Time Auto (-1).

''',
        'longDescription': '''
Specifies the measurement aperture time for the current configuration.
Aperture time is specified in units set by the Aperture Time Units
property. To override the default aperture, set this property to the
desired aperture time after calling niDMM Config Measurement . To return
to the default, set this property to Aperture Time Auto (-1).

This corresponds to LabVIEW property **Configuration:Advanced:Aperture
Time**

Any number of powerline cycles (PLCs) within the minimum and maximum
ranges is allowed on the NI 4080/4081/4082 and NI 4070/4071/4072.

On the NI 4065 the minimum aperture time is 333 micro s and the maximum
aperture time is 78.2 s. If setting the number of averages directly, the
total measurement time is aperture time X the number of averages, which
must be less than 72.8 s. The aperture times allowed are 333 micro s,
667 micro s, or multiples of 1.11 ms—for example 1.11 ms, 2.22 ms, 3.33
ms, and so on. If you set an aperture time other than 333 micro s, 667
micro s, or multiples of 1.11 ms, the value will be coerced up to the
next supported aperture time.

On the NI 4060, when the powerline frequency is 60 Hz, the PLCs allowed
are 1 PLC, 6 PLC, 12 PLC, and 120 PLC. When the powerline frequency is
50 Hz, the PLCs allowed are 1 PLC, 5 PLC, 10 PLC, and 100 PLC.

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 64-bit floating point   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1250322': {
        'shortDescription': '''
Specifies the units of aperture time for the current configuration.

''',
        'longDescription': '''
Specifies the units of aperture time for the current configuration.

This corresponds to LabVIEW property **Configuration:Advanced:Aperture
Time Units**

.. note::
   The NI 4060 does not support an aperture time set in seconds.  

+-----------------------------+--------------------------------------+
| Name                        | Description                          |
+-----------------------------+--------------------------------------+
| **Seconds** (0)             | Units are seconds.                   |
+-----------------------------+--------------------------------------+
| **Power Line Cycles** (1)   | Units are powerline cycles (PLCs).   |
+-----------------------------+--------------------------------------+

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1250331': {
        'shortDescription': '''
Specifies the value of the range. If auto ranging is enabled, shows the
actual value of the active range. The value of this property is set
during a read operation.

''',
        'longDescription': '''
Specifies the value of the range. If auto ranging is enabled, shows the
actual value of the active range. The value of this property is set
during a read operation.

This corresponds to LabVIEW property **Configuration:Auto Range Value**

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 64-bit floating point   |
+------------------+-------------------------+
| Permissions      | Read Only               |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1250332': {
        'shortDescription': '''
Specifies the AutoZero mode. This property is not supported for the NI
4050.

''',
        'longDescription': '''
Specifies the AutoZero mode. This property is not supported for the NI
4050.

This corresponds to LabVIEW property **Configuration:Measurement
Options:Auto Zero**

+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name            | Description                                                                                                                                                                                                                                                                                                                         |
+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Auto** (-1)   | NI-DMM chooses the Auto Zero setting based on the configured function and resolution.                                                                                                                                                                                                                                               |
+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Off** (0)     | Disables AutoZero.                                                                                                                                                                                                                                                                                                                  |
+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **On** (1)      | The DMM internally disconnects the input signal following each measurement and takes a zero reading. It then subtracts the zero reading from the preceding reading. For NI 4065 devices, Auto Zero is always ON. Auto Zero is an integral part of the signal measurement phase and adds no extra time to the overall measurement.   |
+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Once** (2)    | The DMM internally disconnects the input signal for the first measurement and takes a zero reading. It then subtracts the zero reading from the first reading and the following readings. The NI 4060/4065 does not support this setting.                                                                                           |
+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1250333': {
        'shortDescription': '''
Specifies the powerline frequency. The NI 4060 and NI 4050 use this
value to select an aperture time to reject powerline noise by selecting
the appropriate internal sample clock and filter. The NI 4065, NI
4070/4071/4072, and NI 4080/4081/4082 use this value to select timebases
for setting the Aperture Time property in powerline cycles.

''',
        'longDescription': '''
Specifies the powerline frequency. The NI 4060 and NI 4050 use this
value to select an aperture time to reject powerline noise by selecting
the appropriate internal sample clock and filter. The NI 4065, NI
4070/4071/4072, and NI 4080/4081/4082 use this value to select timebases
for setting the Aperture Time property in powerline cycles.

This corresponds to LabVIEW property **Configuration:Measurement
Options:Powerline Frequency**

After configuring powerline frequency, set the Aperture Time Units
property to PLCs. When setting the Aperture Time property, select the
number of PLCs for the powerline frequency. For example, if powerline
frequency = 50 Hz (or 20 ms) and aperture time in PLCs = 5, then
aperture time in seconds = 20 ms \* 5 PLCs = 100 ms. Similarly, if
powerline frequency = 60 Hz (or 16.667 ms) and aperture time in PLCs =
6, then aperture time in seconds = 16.667 ms \* 6 PLCs = 100 ms.

.. note::
   For 400 Hz powerline frequency, use the 50 Hz setting.  

+---------------------------+-----------------------------------------------+
| Name                      | Description                                   |
+---------------------------+-----------------------------------------------+
| **50 Hz** (5.000000E+1)   | Specifies the powerline frequency as 50 Hz.   |
+---------------------------+-----------------------------------------------+
| **60 Hz** (6.000000E+1)   | Specifies the powerline frequency as 60 Hz.   |
+---------------------------+-----------------------------------------------+

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 64-bit floating point   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
    '1250334': {
        'shortDescription': '''
Specifies the edge of the signal from the specified trigger source on
which the DMM is triggered.

''',
        'longDescription': '''
Specifies the edge of the signal from the specified trigger source on
which the DMM is triggered.

This corresponds to LabVIEW property **Trigger:Trigger Slope**

+--------------------+------------------------------------------------------------------+
| Name               | Description                                                      |
+--------------------+------------------------------------------------------------------+
| **Positive** (0)   | The driver triggers on the rising edge of the trigger signal.    |
+--------------------+------------------------------------------------------------------+
| **Negative** (1)   | The driver triggers on the falling edge of the trigger signal.   |
+--------------------+------------------------------------------------------------------+

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| High Level VI    | N/A                     |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
    },
}
