# -*- coding: utf-8 -*-
attribute_docs = {
    '-2': {
        'longDescription': '''
Specifies the channel name used to access all subsequent channel-based
properties in this property node. Set the channel before setting
channel-based properties. Pass a name that the instrument driver defines
or a virtual channel name configured in MAX.

The following table lists the characteristics of this property.

+------------------+--------------+
| Characteristic   | Value        |
+------------------+--------------+
| Datatype         | string       |
+------------------+--------------+
| Permissions      | Write Only   |
+------------------+--------------+
| Channel Based    | False        |
+------------------+--------------+
| Resettable       | No           |
+------------------+--------------+

''',
        'lv_property': '''
Active Channel
''',
        'shortDescription': '''
Specifies the channel name used to access all subsequent channel-based
properties in this property node. Set the channel before setting
channel-based properties. Pass a name that the instrument driver defines
or a virtual channel name configured in MAX.

''',
    },
    '1050002': {
        'longDescription': '''
Specifies whether to validate property values and VI parameters. If
enabled, the instrument driver validates the parameter values passed to
driver VIs. Range checking parameters is very useful for debugging.
After the user program is validated, you can set this property to FALSE
(0) to disable range checking and maximize performance. The default
value is TRUE (1). Use niDMM Initialize With Options to override the
default setting.

The following table lists the characteristics of this property.

+------------------+--------------+
| Characteristic   | Value        |
+------------------+--------------+
| Datatype         | Boolean      |
+------------------+--------------+
| Permissions      | Read/Write   |
+------------------+--------------+
| Channel Based    | False        |
+------------------+--------------+
| Resettable       | No           |
+------------------+--------------+

''',
        'lv_property': '''
Inherent IVI Attributes:User Options:Range Check
''',
        'shortDescription': '''
Specifies whether to validate property values and VI parameters. If
enabled, the instrument driver validates the parameter values passed to
driver VIs. Range checking parameters is very useful for debugging.
After the user program is validated, you can set this property to FALSE
(0) to disable range checking and maximize performance. The default
value is TRUE (1). Use niDMM Initialize With Options to override the
default setting.

''',
    },
    '1050003': {
        'longDescription': '''
Specifies whether the instrument driver queries the instrument status
after each operation. Querying the instrument status is very useful for
debugging. After the user program is validated, this property can be set
to FALSE (0) to disable status checking and maximize performance. The
instrument driver can choose to ignore status checking for particular
properties regardless of the setting of this property. The default value
is TRUE (1). Use niDMM Initialize With Options to override the default
setting.

The following table lists the characteristics of this property.

+------------------+--------------+
| Characteristic   | Value        |
+------------------+--------------+
| Datatype         | Boolean      |
+------------------+--------------+
| Permissions      | Read/Write   |
+------------------+--------------+
| Channel Based    | False        |
+------------------+--------------+
| Resettable       | No           |
+------------------+--------------+

''',
        'lv_property': '''
Inherent IVI Attributes:User Options:Query Instrument Status
''',
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
    },
    '1050004': {
        'longDescription': '''
Specifies whether to cache the value of properties. When caching is
enabled, the instrument driver keeps track of the current instrument
settings and avoids sending redundant commands to the instrument. Thus,
it significantly increases execution speed. The instrument driver can
choose to always cache or to never cache particular properties
regardless of the setting of this property. The default value is TRUE
(1). Use niDMM Initialize With Options to override the default setting.

The following table lists the characteristics of this property.

+------------------+--------------+
| Characteristic   | Value        |
+------------------+--------------+
| Datatype         | Boolean      |
+------------------+--------------+
| Permissions      | Read/Write   |
+------------------+--------------+
| Channel Based    | False        |
+------------------+--------------+
| Resettable       | No           |
+------------------+--------------+

''',
        'lv_property': '''
Inherent IVI Attributes:User Options:Cache
''',
        'shortDescription': '''
Specifies whether to cache the value of properties. When caching is
enabled, the instrument driver keeps track of the current instrument
settings and avoids sending redundant commands to the instrument. Thus,
it significantly increases execution speed. The instrument driver can
choose to always cache or to never cache particular properties
regardless of the setting of this property. The default value is TRUE
(1). Use niDMM Initialize With Options to override the default setting.

''',
    },
    '1050005': {
        'longDescription': '''
Specifies whether to simulate instrument driver I/O operations. If
simulation is enabled, instrument driver functions perform range
checking and call IVI Get and Set VIs, but they do not perform
instrument I/O. For output parameters that represent instrument data,
the instrument driver VIs return calculated values. The default value is
FALSE (0). Use niDMM Initialize With Options to override the default
setting.

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
| Channel Based    | False        |
+------------------+--------------+
| Resettable       | No           |
+------------------+--------------+

''',
        'lv_property': '''
Inherent IVI Attributes:User Options:Simulate
''',
        'shortDescription': '''
Specifies whether to simulate instrument driver I/O operations. If
simulation is enabled, instrument driver functions perform range
checking and call IVI Get and Set VIs, but they do not perform
instrument I/O. For output parameters that represent instrument data,
the instrument driver VIs return calculated values. The default value is
FALSE (0). Use niDMM Initialize With Options to override the default
setting.

''',
    },
    '1050006': {
        'longDescription': '''
Specifies whether the IVI engine keeps a list of the value coercions it
makes for ViInt32 and ViReal64 properties. The default value is FALSE
(0). Use niDMM Initialize With Options to override the default setting.
Use niDMM Get Next Coercion Record to extract and delete the oldest
coercion record from the list.

The following table lists the characteristics of this property.

+------------------+--------------+
| Characteristic   | Value        |
+------------------+--------------+
| Datatype         | Boolean      |
+------------------+--------------+
| Permissions      | Read/Write   |
+------------------+--------------+
| Channel Based    | False        |
+------------------+--------------+
| Resettable       | No           |
+------------------+--------------+

''',
        'lv_property': '''
Inherent IVI Attributes:User Options:Record Value Coercions
''',
        'shortDescription': '''
Specifies whether the IVI engine keeps a list of the value coercions it
makes for ViInt32 and ViReal64 properties. The default value is FALSE
(0). Use niDMM Initialize With Options to override the default setting.
Use niDMM Get Next Coercion Record to extract and delete the oldest
coercion record from the list.

''',
    },
    '1050007': {
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

The following table lists the characteristics of this property.

+------------------+-------------+
| Characteristic   | Value       |
+------------------+-------------+
| Datatype         | string      |
+------------------+-------------+
| Permissions      | Read Only   |
+------------------+-------------+
| Channel Based    | False       |
+------------------+-------------+
| Resettable       | No          |
+------------------+-------------+

''',
        'lv_property': '''
Inherent IVI Attributes:User Options:Driver Setup
''',
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
    },
    '1050021': {
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
| Channel Based    | False        |
+------------------+--------------+
| Resettable       | No           |
+------------------+--------------+

''',
        'lv_property': '''
Inherent IVI Attributes:User Options:Interchange Check
''',
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
    },
    '1050101': {
        'longDescription': '''
A code that describes the first error that occurred since the last call
to niDMM Get Error for the session. The value follows the VXIplug&play
conventions. A negative value describes an error condition. A positive
value describes a warning condition. A zero indicates that no error or
warning occurred. The error and warning values can be status codes
defined by IVI, VISA, class drivers, or specific drivers.

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Obsolete:Inherent IVI Attributes:Error Info:Primary Error
''',
        'shortDescription': '''
A code that describes the first error that occurred since the last call
to niDMM Get Error for the session. The value follows the VXIplug&play
conventions. A negative value describes an error condition. A positive
value describes a warning condition. A zero indicates that no error or
warning occurred. The error and warning values can be status codes
defined by IVI, VISA, class drivers, or specific drivers.

''',
    },
    '1050102': {
        'longDescription': '''
An optional code that provides additional information concerning the
primary error condition. The error and warning values can be status
codes defined by IVI, VISA, class drivers, or specific drivers. Zero
indicates no additional information.

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Obsolete:Inherent IVI Attributes:Error Info:Secondary Error
''',
        'shortDescription': '''
An optional code that provides additional information concerning the
primary error condition. The error and warning values can be status
codes defined by IVI, VISA, class drivers, or specific drivers. Zero
indicates no additional information.

''',
    },
    '1050103': {
        'longDescription': '''
An optional string that contains additional information concerning the
primary error condition.

The following table lists the characteristics of this property.

+------------------+--------------+
| Characteristic   | Value        |
+------------------+--------------+
| Datatype         | string       |
+------------------+--------------+
| Permissions      | Read/Write   |
+------------------+--------------+
| Channel Based    | False        |
+------------------+--------------+
| Resettable       | No           |
+------------------+--------------+

''',
        'lv_property': '''
Obsolete:Inherent IVI Attributes:Error Info:Error Elaboration
''',
        'shortDescription': '''
An optional string that contains additional information concerning the
primary error condition.

''',
    },
    '1050203': {
        'longDescription': '''
Indicates the number of channels that the specific instrument driver
supports. For each property for which the IVI\_VAL\_MULTI\_CHANNEL flag
property is set, the IVI engine maintains a separate cache value for
each channel.

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read Only               |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Inherent IVI Attributes:Instrument Capabilities:Channel Count
''',
        'shortDescription': '''
Indicates the number of channels that the specific instrument driver
supports. For each property for which the IVI\_VAL\_MULTI\_CHANNEL flag
property is set, the IVI engine maintains a separate cache value for
each channel.

''',
    },
    '1050302': {
        'longDescription': '''
The prefix for the specific instrument driver. The name of each
user-callable VI in this driver starts with this prefix. The prefix can
be up to a maximum of eight characters.

The following table lists the characteristics of this property.

+------------------+-------------+
| Characteristic   | Value       |
+------------------+-------------+
| Datatype         | string      |
+------------------+-------------+
| Permissions      | Read Only   |
+------------------+-------------+
| Channel Based    | False       |
+------------------+-------------+
| Resettable       | No          |
+------------------+-------------+

''',
        'lv_property': '''
Inherent IVI Attributes:Instrument Capabilities:Specific Driver Prefix
''',
        'shortDescription': '''
The prefix for the specific instrument driver. The name of each
user-callable VI in this driver starts with this prefix. The prefix can
be up to a maximum of eight characters.

''',
    },
    '1050304': {
        'longDescription': '''
A string containing the resource descriptor of the instrument.

The following table lists the characteristics of this property.

+------------------+-------------+
| Characteristic   | Value       |
+------------------+-------------+
| Datatype         | string      |
+------------------+-------------+
| Permissions      | Read Only   |
+------------------+-------------+
| Channel Based    | False       |
+------------------+-------------+
| Resettable       | No          |
+------------------+-------------+

''',
        'lv_property': '''
Inherent IVI Attributes:Advanced Session Information:I/O Resource Descriptor
''',
        'shortDescription': '''
A string containing the resource descriptor of the instrument.

''',
    },
    '1050305': {
        'longDescription': '''
A string containing the logical name of the instrument.

The following table lists the characteristics of this property.

+------------------+-------------+
| Characteristic   | Value       |
+------------------+-------------+
| Datatype         | string      |
+------------------+-------------+
| Permissions      | Read Only   |
+------------------+-------------+
| Channel Based    | False       |
+------------------+-------------+
| Resettable       | No          |
+------------------+-------------+

''',
        'lv_property': '''
Inherent IVI Attributes:Advanced Session Information:Logical Name
''',
        'shortDescription': '''
A string containing the logical name of the instrument.

''',
    },
    '1050327': {
        'longDescription': '''
A string containing the instrument models supported by the specific
driver.

The following table lists the characteristics of this property.

+------------------+-------------+
| Characteristic   | Value       |
+------------------+-------------+
| Datatype         | string      |
+------------------+-------------+
| Permissions      | Read Only   |
+------------------+-------------+
| Channel Based    | False       |
+------------------+-------------+
| Resettable       | No          |
+------------------+-------------+

''',
        'lv_property': '''
Inherent IVI Attributes:Specific Driver Capabilities:Supported Instrument Models
''',
        'shortDescription': '''
A string containing the instrument models supported by the specific
driver.

''',
    },
    '1050401': {
        'longDescription': '''
A string containing the capabilities and extension groups supported by
the specific driver.

The following table lists the characteristics of this property.

+------------------+-------------+
| Characteristic   | Value       |
+------------------+-------------+
| Datatype         | string      |
+------------------+-------------+
| Permissions      | Read Only   |
+------------------+-------------+
| Channel Based    | False       |
+------------------+-------------+
| Resettable       | No          |
+------------------+-------------+

''',
        'lv_property': '''
Inherent IVI Attributes:Specific Driver Capabilities:Group Capabilities
''',
        'shortDescription': '''
A string containing the capabilities and extension groups supported by
the specific driver.

''',
    },
    '1050501': {
        'longDescription': '''
The major version number of the IVI engine.

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read Only               |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Obsolete:Inherent IVI Attributes:Version Info:Engine Major Version
''',
        'shortDescription': '''
The major version number of the IVI engine.

''',
    },
    '1050502': {
        'longDescription': '''
The minor version number of the IVI engine.

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read Only               |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Obsolete:Inherent IVI Attributes:Version Info:Engine Minor Version
''',
        'shortDescription': '''
The minor version number of the IVI engine.

''',
    },
    '1050503': {
        'longDescription': '''
Returns the major version number of this instrument driver.

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read Only               |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Inherent IVI Attributes:Version Info:Specific Driver Major Version
''',
        'shortDescription': '''
Returns the major version number of this instrument driver.

''',
    },
    '1050504': {
        'longDescription': '''
Returns the minor version number of this instrument driver.

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read Only               |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Inherent IVI Attributes:Version Info:Specific Driver Minor Version
''',
        'shortDescription': '''
Returns the minor version number of this instrument driver.

''',
    },
    '1050510': {
        'longDescription': '''
A string containing the instrument firmware revision number.

The following table lists the characteristics of this property.

+------------------+-------------+
| Characteristic   | Value       |
+------------------+-------------+
| Datatype         | string      |
+------------------+-------------+
| Permissions      | Read Only   |
+------------------+-------------+
| Channel Based    | False       |
+------------------+-------------+
| Resettable       | No          |
+------------------+-------------+

''',
        'lv_property': '''
Inherent IVI Attributes:Instrument Identification:Instrument Firmware Revision
''',
        'shortDescription': '''
A string containing the instrument firmware revision number.

''',
    },
    '1050511': {
        'longDescription': '''
A string containing the manufacturer of the instrument.

The following table lists the characteristics of this property.

+------------------+-------------+
| Characteristic   | Value       |
+------------------+-------------+
| Datatype         | string      |
+------------------+-------------+
| Permissions      | Read Only   |
+------------------+-------------+
| Channel Based    | False       |
+------------------+-------------+
| Resettable       | No          |
+------------------+-------------+

''',
        'lv_property': '''
Inherent IVI Attributes:Instrument Identification:Instrument Manufacturer
''',
        'shortDescription': '''
A string containing the manufacturer of the instrument.

''',
    },
    '1050512': {
        'longDescription': '''
A string containing the instrument model.

The following table lists the characteristics of this property.

+------------------+-------------+
| Characteristic   | Value       |
+------------------+-------------+
| Datatype         | string      |
+------------------+-------------+
| Permissions      | Read Only   |
+------------------+-------------+
| Channel Based    | False       |
+------------------+-------------+
| Resettable       | No          |
+------------------+-------------+

''',
        'lv_property': '''
Inherent IVI Attributes:Instrument Identification:Instrument Model
''',
        'shortDescription': '''
A string containing the instrument model.

''',
    },
    '1050513': {
        'longDescription': '''
A string containing the vendor of the specific driver.

The following table lists the characteristics of this property.

+------------------+-------------+
| Characteristic   | Value       |
+------------------+-------------+
| Datatype         | string      |
+------------------+-------------+
| Permissions      | Read Only   |
+------------------+-------------+
| Channel Based    | False       |
+------------------+-------------+
| Resettable       | No          |
+------------------+-------------+

''',
        'lv_property': '''
Inherent IVI Attributes:Specific Driver Identification:Specific Driver Vendor
''',
        'shortDescription': '''
A string containing the vendor of the specific driver.

''',
    },
    '1050514': {
        'longDescription': '''
A string containing a description of the specific driver.

The following table lists the characteristics of this property.

+------------------+-------------+
| Characteristic   | Value       |
+------------------+-------------+
| Datatype         | string      |
+------------------+-------------+
| Permissions      | Read Only   |
+------------------+-------------+
| Channel Based    | False       |
+------------------+-------------+
| Resettable       | No          |
+------------------+-------------+

''',
        'lv_property': '''
Inherent IVI Attributes:Specific Driver Identification:Specific Driver Description
''',
        'shortDescription': '''
A string containing a description of the specific driver.

''',
    },
    '1050515': {
        'longDescription': '''
The major version number of the class specification for the specific
driver.

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read Only               |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Inherent IVI Attributes:Specific Driver Identification:Specific Driver Class Spec Major Version
''',
        'shortDescription': '''
The major version number of the class specification for the specific
driver.

''',
    },
    '1050516': {
        'longDescription': '''
The minor version number of the class specification for the specific
driver.

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read Only               |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Inherent IVI Attributes:Specific Driver Identification:Specific Driver Class Spec Minor Version
''',
        'shortDescription': '''
The minor version number of the class specification for the specific
driver.

''',
    },
    '1050551': {
        'longDescription': '''
A string that contains additional version information about this
instrument driver.

The following table lists the characteristics of this property.

+------------------+-------------+
| Characteristic   | Value       |
+------------------+-------------+
| Datatype         | string      |
+------------------+-------------+
| Permissions      | Read Only   |
+------------------+-------------+
| Channel Based    | False       |
+------------------+-------------+
| Resettable       | No          |
+------------------+-------------+

''',
        'lv_property': '''
Inherent IVI Attributes:Version Info:Specific Driver Revision
''',
        'shortDescription': '''
A string that contains additional version information about this
instrument driver.

''',
    },
    '1050553': {
        'longDescription': '''
A string that contains additional version information about the IVI
engine.

The following table lists the characteristics of this property.

+------------------+-------------+
| Characteristic   | Value       |
+------------------+-------------+
| Datatype         | string      |
+------------------+-------------+
| Permissions      | Read Only   |
+------------------+-------------+
| Channel Based    | False       |
+------------------+-------------+
| Resettable       | No          |
+------------------+-------------+

''',
        'lv_property': '''
Obsolete:Inherent IVI Attributes:Version Info:Engine Revision
''',
        'shortDescription': '''
A string that contains additional version information about the IVI
engine.

''',
    },
    '1150001': {
        'longDescription': '''
A string containing the type of instrument used in the current session.

The following table lists the characteristics of this property.

+------------------+-------------+
| Characteristic   | Value       |
+------------------+-------------+
| Datatype         | string      |
+------------------+-------------+
| Permissions      | Read Only   |
+------------------+-------------+
| Channel Based    | False       |
+------------------+-------------+
| Resettable       | No          |
+------------------+-------------+

''',
        'lv_property': '''
Obsolete:Misc:IDQuery response
''',
        'shortDescription': '''
A string containing the type of instrument used in the current session.

''',
    },
    '1150002': {
        'longDescription': '''
Specifies the polarity of the generated measurement complete signal.

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
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Trigger:Measurement Destination Slope
''',
        'shortDescription': '''
Specifies the polarity of the generated measurement complete signal.

''',
    },
    '1150003': {
        'longDescription': '''
For the NI 4050 only, specifies the shunt resistance value.

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
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Configuration:Measurement Options:Shunt Value
''',
        'shortDescription': '''
For the NI 4050 only, specifies the shunt resistance value.

''',
    },
    '1150010': {
        'longDescription': '''
Specifies the edge of the signal from the specified sample trigger
source on which the DMM is triggered.

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
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Multi Point Acquisition:Sample Trig Slope
''',
        'shortDescription': '''
Specifies the edge of the signal from the specified sample trigger
source on which the DMM is triggered.

''',
    },
    '1150014': {
        'longDescription': '''
Specifies how the DMM acquires data.

.. note::
   The NI 4050 and NI 4060 are not supported.  

When you call niDMM Config Measurement , NI-DMM sets this property to
IVIDMM Mode. When you call niDMM Configure Waveform Acquisition , NI-DMM
sets this property to Waveform Mode. If you are programming properties
directly, you must set this property before setting other configuration
properties.

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
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Configuration:Advanced:Operation Mode
''',
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
    },
    '1150018': {
        'longDescription': '''
Specifies the rate of the waveform acquisition in samples per second
(S/s). The valid rate is calculated by dividing 1,800,000 by an integer
divisor, and the rate falls between 10 and 1,800,000 samples per second.
The waveform rate is coerced upwards to the next valid rate. The default
value is 1,800,000 samples per second. Not supported by NI 4065.

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 64-bit floating point   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Waveform Acquisition:Waveform Rate
''',
        'shortDescription': '''
Specifies the rate of the waveform acquisition in samples per second
(S/s). The valid rate is calculated by dividing 1,800,000 by an integer
divisor, and the rate falls between 10 and 1,800,000 samples per second.
The waveform rate is coerced upwards to the next valid rate. The default
value is 1,800,000 samples per second. Not supported by NI 4065.

''',
    },
    '1150019': {
        'longDescription': '''
For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the number of
points to acquire in a waveform acquisition.

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Waveform Acquisition:Waveform Points
''',
        'shortDescription': '''
For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the number of
points to acquire in a waveform acquisition.

''',
    },
    '1150022': {
        'longDescription': '''
For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the ADC
calibration mode.

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
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Configuration:Measurement Options:ADC Calibration
''',
        'shortDescription': '''
For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the ADC
calibration mode.

''',
    },
    '1150023': {
        'longDescription': '''
For the NI 4080/4081/4082 and NI 4070/4071/4072, enables or disables
offset compensated ohms.

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
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Configuration:Measurement Options:Offset Compensated Ohms
''',
        'shortDescription': '''
For the NI 4080/4081/4082 and NI 4070/4071/4072, enables or disables
offset compensated ohms.

''',
    },
    '1150025': {
        'longDescription': '''
Specifies the current source provided during diode measurements.

The NI 4050 and NI 4060 are not supported.

+-----------------------------+--------------------------------------------------------------------+
| Name                        | Description                                                        |
+-----------------------------+--------------------------------------------------------------------+
| **1 Microamp** (1e-06)      | NI 4070/4071/4072 are supported.                                   |
+-----------------------------+--------------------------------------------------------------------+
| **10 Microamp** (1e-05)     | NI 4080/4081/4082 and NI 4070/4071/4072 are supported.             |
+-----------------------------+--------------------------------------------------------------------+
| **100 Microamp** (0.0001)   | NI 4080/4081/4082, NI 4070/4071/4072, and NI 4065 are supported.   |
+-----------------------------+--------------------------------------------------------------------+
| **1 Milliamp** (0.001)      | NI 4080/4081/4082, NI 4070/4071/4072, and NI 4065 are supported.   |
+-----------------------------+--------------------------------------------------------------------+

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 64-bit floating point   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Configuration:Measurement Options:Current Source
''',
        'shortDescription': '''
Specifies the current source provided during diode measurements.

The NI 4050 and NI 4060 are not supported.

''',
    },
    '1150026': {
        'longDescription': '''
Specifies the DC noise rejection mode.

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
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Configuration:Measurement Options:DC Noise Rejection
''',
        'shortDescription': '''
Specifies the DC noise rejection mode.

''',
    },
    '1150027': {
        'longDescription': '''
For the NI 4080/4081/4082 and NI 4070/4071/4072 only, specifies the
coupling during a waveform acquisition.

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
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Waveform Acquisition:Waveform Coupling
''',
        'shortDescription': '''
For the NI 4080/4081/4082 and NI 4070/4071/4072 only, specifies the
coupling during a waveform acquisition.

''',
    },
    '1150028': {
        'longDescription': '''
Specifies the settling time in seconds. Use this property to override
the default settling time. To return to the default, set this property
to Auto (-1).

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
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Configuration:Advanced:Settle Time
''',
        'shortDescription': '''
Specifies the settling time in seconds. Use this property to override
the default settling time. To return to the default, set this property
to Auto (-1).

''',
    },
    '1150029': {
        'longDescription': '''
Specifies the input resistance of the instrument.

.. note::
   The NI 4050 and NI 4060 are not supported.  

+---------------------------------------------+------------------------------------------+
| Name                                        | Description                              |
+---------------------------------------------+------------------------------------------+
| **1 M Ohm** (1000000.0)                     | Input resistance of 1 M Ohm              |
+---------------------------------------------+------------------------------------------+
| **10 M Ohm** (10000000.0)                   | Input resistance of 10 M Ohm             |
+---------------------------------------------+------------------------------------------+
| **Greater Than 10 G Ohm** (10000000000.0)   | Input resistance greater than 10 G Ohm   |
+---------------------------------------------+------------------------------------------+

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 64-bit floating point   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Configuration:Measurement Options:Input Resistance
''',
        'shortDescription': '''
Specifies the input resistance of the instrument.

''',
    },
    '1150031': {
        'longDescription': '''
For the NI 4060 only, specifies a delay interval after a sample trigger.

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
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Multi Point Acquisition:Sample Delay Mode
''',
        'shortDescription': '''
For the NI 4060 only, specifies a delay interval after a sample trigger.

''',
    },
    '1150032': {
        'longDescription': '''
Specifies the number of averages to perform in a measurement. For the NI
4080/4081/4082 and NI 4070/4071/4072, applies only when the aperture
time is not set to Auto and Auto Zero is ON. The Number of Averages
Property will be ignored otherwise. The default is 4 for 7 1/2 digits;
otherwise, the default is 1.

The NI 4050 and NI 4060 are not supported.

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Configuration:Advanced:Number Of Averages
''',
        'shortDescription': '''
Specifies the number of averages to perform in a measurement. For the NI
4080/4081/4082 and NI 4070/4071/4072, applies only when the aperture
time is not set to Auto and Auto Zero is ON. The Number of Averages
Property will be ignored otherwise. The default is 4 for 7 1/2 digits;
otherwise, the default is 1.

The NI 4050 and NI 4060 are not supported.

''',
    },
    '1150034': {
        'longDescription': '''
Specifies the number of measurements transferred at a time from the
instrument to an internal buffer. When set to Auto (-1), NI-DMM chooses
the transfer size.

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Multi Point Acquisition:Advanced:Latency
''',
        'shortDescription': '''
Specifies the number of measurements transferred at a time from the
instrument to an internal buffer. When set to Auto (-1), NI-DMM chooses
the transfer size.

''',
    },
    '1150037': {
        'longDescription': '''
Specifies the size in samples of the internal data buffer. Maximum size
is 134,217,727 (0X7FFFFFF) samples. When set to Auto (-1), NI-DMM
chooses the buffer size.

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Multi Point Acquisition:Advanced:Buffer Size
''',
        'shortDescription': '''
Specifies the size in samples of the internal data buffer. Maximum size
is 134,217,727 (0X7FFFFFF) samples. When set to Auto (-1), NI-DMM
chooses the buffer size.

''',
    },
    '1150044': {
        'longDescription': '''
For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the value of
the frequency voltage range. If auto ranging is enabled, shows the
actual value of the active frequency voltage range. If not Auto Ranging,
the value is the same as that of the Frequency Voltage Range property.

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 64-bit floating point   |
+------------------+-------------------------+
| Permissions      | Read Only               |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Configuration:Measurement Options:Frequency Voltage Auto Range Value
''',
        'shortDescription': '''
For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the value of
the frequency voltage range. If auto ranging is enabled, shows the
actual value of the active frequency voltage range. If not Auto Ranging,
the value is the same as that of the Frequency Voltage Range property.

''',
    },
    '1150045': {
        'longDescription': '''
For the NI 4081 and NI 4072 only, specifies the type of cable
compensation that is applied to the current capacitance or inductance
measurement for the current range.

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
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Configuration:Measurement Options:Capacitance and Inductance:Cable Compensation Type
''',
        'shortDescription': '''
For the NI 4081 and NI 4072 only, specifies the type of cable
compensation that is applied to the current capacitance or inductance
measurement for the current range.

''',
    },
    '1150046': {
        'longDescription': '''
For the NI 4082 and NI 4072 only, represents the reactive part
(reactance) of the short cable compensation. The valid range is any real
number >0. The default value (-1) indicates that compensation has not
taken place.

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
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Configuration:Measurement Options:Capacitance and Inductance:Short Cable Compensation Values:Reactance
''',
        'shortDescription': '''
For the NI 4082 and NI 4072 only, represents the reactive part
(reactance) of the short cable compensation. The valid range is any real
number >0. The default value (-1) indicates that compensation has not
taken place.

''',
    },
    '1150047': {
        'longDescription': '''
For the NI 4082 and NI 4072 only, represents the active part
(resistance) of the short cable compensation. The valid range is any
real number >0. The default value (-1) indicates that compensation has
not taken place.

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
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Configuration:Measurement Options:Capacitance and Inductance:Short Cable Compensation Values:Resistance
''',
        'shortDescription': '''
For the NI 4082 and NI 4072 only, represents the active part
(resistance) of the short cable compensation. The valid range is any
real number >0. The default value (-1) indicates that compensation has
not taken place.

''',
    },
    '1150048': {
        'longDescription': '''
For the NI 4082 and NI 4072 only, specifies the reactive part
(susceptance) of the open cable compensation. The valid range is any
real number >0. The default value (-1.0) indicates that compensation has
not taken place.

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
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Configuration:Measurement Options:Capacitance and Inductance:Open Cable Compensation Values:Susceptance
''',
        'shortDescription': '''
For the NI 4082 and NI 4072 only, specifies the reactive part
(susceptance) of the open cable compensation. The valid range is any
real number >0. The default value (-1.0) indicates that compensation has
not taken place.

''',
    },
    '1150049': {
        'longDescription': '''
For the NI 4082 and NI 4072 only, specifies the active part
(conductance) of the open cable compensation. The valid range is any
real number >0. The default value (-1.0) indicates that compensation has
not taken place.

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
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Configuration:Measurement Options:Capacitance and Inductance:Open Cable Compensation Values:Conductance
''',
        'shortDescription': '''
For the NI 4082 and NI 4072 only, specifies the active part
(conductance) of the open cable compensation. The valid range is any
real number >0. The default value (-1.0) indicates that compensation has
not taken place.

''',
    },
    '1150052': {
        'longDescription': '''
For the NI 4082 and NI 4072 only, specifies the type of algorithm that
the measurement processing uses for capacitance and inductance
measurements.

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
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Configuration:Measurement Options:Capacitance and Inductance:Advanced:Calculation Model
''',
        'shortDescription': '''
For the NI 4082 and NI 4072 only, specifies the type of algorithm that
the measurement processing uses for capacitance and inductance
measurements.

''',
    },
    '1150053': {
        'longDescription': '''
For the NI 4082 and NI 4072 only, controls the available DC bias for
capacitance measurements.

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
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Configuration:Measurement Options:Capacitance and Inductance:Advanced:DC Bias
''',
        'shortDescription': '''
For the NI 4082 and NI 4072 only, controls the available DC bias for
capacitance measurements.

''',
    },
    '1150054': {
        'longDescription': '''
A string containing the serial number of the instrument. This property
corresponds to the serial number label that is attached to most
products.

The following table lists the characteristics of this property.

+------------------+-------------+
| Characteristic   | Value       |
+------------------+-------------+
| Datatype         | string      |
+------------------+-------------+
| Permissions      | Read Only   |
+------------------+-------------+
| Channel Based    | False       |
+------------------+-------------+
| Resettable       | No          |
+------------------+-------------+

''',
        'lv_property': '''
Inherent IVI Attributes:Instrument Identification:Instrument Serial Number
''',
        'shortDescription': '''
A string containing the serial number of the instrument. This property
corresponds to the serial number label that is attached to most
products.

''',
    },
    '1150055': {
        'longDescription': '''
For the NI 4082 and NI 4072 only, specifies the number of LC
measurements that are averaged to produce one reading.

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Configuration:Measurement Options:Capacitance and Inductance:Number of LC Measurements To Average
''',
        'shortDescription': '''
For the NI 4082 and NI 4072 only, specifies the number of LC
measurements that are averaged to produce one reading.

''',
    },
    '1150061': {
        'longDescription': '''
The PCI product ID.

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read Only               |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Inherent IVI Attributes:Instrument Identification:Instrument Product ID
''',
        'shortDescription': '''
The PCI product ID.

''',
    },
    '1150120': {
        'longDescription': '''
Specifies the RTD type.

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
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD Type
''',
        'shortDescription': '''
Specifies the RTD type.

''',
    },
    '1150121': {
        'longDescription': '''
Specifies the Callendar-Van Dusen A coefficient for RTD scaling when the
**RTD Type property** is set to Custom.

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 64-bit floating point   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD A
''',
        'shortDescription': '''
Specifies the Callendar-Van Dusen A coefficient for RTD scaling when the
**RTD Type property** is set to Custom.

''',
    },
    '1150122': {
        'longDescription': '''
Specifies the Callendar-Van Dusen B coefficient for RTD scaling when the
**RTD Type property** is set to Custom.

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 64-bit floating point   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD B
''',
        'shortDescription': '''
Specifies the Callendar-Van Dusen B coefficient for RTD scaling when the
**RTD Type property** is set to Custom.

''',
    },
    '1150123': {
        'longDescription': '''
Specifies the Callendar-Van Dusen C coefficient for RTD scaling when the
**RTD Type property** is set to Custom.

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 64-bit floating point   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD C
''',
        'shortDescription': '''
Specifies the Callendar-Van Dusen C coefficient for RTD scaling when the
**RTD Type property** is set to Custom.

''',
    },
    '1150124': {
        'longDescription': '''
Specifies the thermistor type.

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
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Configuration:Measurement Options:Temperature:Thermistor:Thermistor Type
''',
        'shortDescription': '''
Specifies the thermistor type.

''',
    },
    '1150125': {
        'longDescription': '''
Specifies the Steinhart-Hart A coefficient for thermistor scaling when
the **Thermistor Type property** is set to Custom.

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 64-bit floating point   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Configuration:Measurement Options:Temperature:Thermistor:Thermistor A
''',
        'shortDescription': '''
Specifies the Steinhart-Hart A coefficient for thermistor scaling when
the **Thermistor Type property** is set to Custom.

''',
    },
    '1150126': {
        'longDescription': '''
Specifies the Steinhart-Hart B coefficient for thermistor scaling when
the **Thermistor Type property** is set to Custom.

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 64-bit floating point   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Configuration:Measurement Options:Temperature:Thermistor:Thermistor B
''',
        'shortDescription': '''
Specifies the Steinhart-Hart B coefficient for thermistor scaling when
the **Thermistor Type property** is set to Custom.

''',
    },
    '1150127': {
        'longDescription': '''
Specifies the Steinhart-Hart C coefficient for thermistor scaling when
the **Thermistor Type property** is set to Custom.

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 64-bit floating point   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Configuration:Measurement Options:Temperature:Thermistor:Thermistor C
''',
        'shortDescription': '''
Specifies the Steinhart-Hart C coefficient for thermistor scaling when
the **Thermistor Type property** is set to Custom.

''',
    },
    '1250001': {
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
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Configuration:Function
''',
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
    },
    '1250002': {
        'longDescription': '''
Specifies the measurement range. Use positive values to represent the
absolute value of the maximum expected measurement. The value is in
units appropriate for the current value of the Function property. For
example, if the Function property is set to DC Volts, the units are
volts.

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
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Configuration:Range
''',
        'shortDescription': '''
Specifies the measurement range. Use positive values to represent the
absolute value of the maximum expected measurement. The value is in
units appropriate for the current value of the Function property. For
example, if the Function property is set to DC Volts, the units are
volts.

''',
    },
    '1250003': {
        'longDescription': '''
Specifies the measurement resolution in digits. Setting this property to
higher values increases the measurement accuracy. Setting this property
to lower values increases the measurement speed.

.. note::
   NI-DMM ignores this property for capacitance and inductance measurements on the NI 4082 and NI 4072. To achieve better resolution for such measurements, use the Number of LC Measurements to Average property.  

+-----------------+------------------------------------+
| Name            | Description                        |
+-----------------+------------------------------------+
| **3.5** (3.5)   | Specifies 3.5 digits resolution.   |
+-----------------+------------------------------------+
| **4.5** (4.5)   | Specifies 4.5 digits resolution.   |
+-----------------+------------------------------------+
| **5.5** (5.5)   | Specifies 5.5 digits resolution.   |
+-----------------+------------------------------------+
| **6.5** (6.5)   | Specifies 6.5 digits resolution.   |
+-----------------+------------------------------------+
| **7.5** (7.5)   | Specifies 7.5 digits resolution.   |
+-----------------+------------------------------------+

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 64-bit floating point   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Configuration:Digits Resolution
''',
        'shortDescription': '''
Specifies the measurement resolution in digits. Setting this property to
higher values increases the measurement accuracy. Setting this property
to lower values increases the measurement speed.

''',
    },
    '1250004': {
        'longDescription': '''
Specifies the trigger source. When niDMM Initiate is called, the DMM
waits for the trigger specified with this property. After it receives
the trigger, the DMM waits the length of time specified with the Trigger
Delay property. The DMM then takes a measurement.

To determine which values are supported by each device, refer to the
LabVIEW Trigger Routing section in the *NI Digital Multimeters Help* .

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
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Trigger:Trigger Source
''',
        'shortDescription': '''
Specifies the trigger source. When niDMM Initiate is called, the DMM
waits for the trigger specified with this property. After it receives
the trigger, the DMM waits the length of time specified with the Trigger
Delay property. The DMM then takes a measurement.

To determine which values are supported by each device, refer to the
LabVIEW Trigger Routing section in the *NI Digital Multimeters Help* .

''',
    },
    '1250005': {
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

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 64-bit floating point   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Trigger:Trigger Delay
''',
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
    },
    '1250006': {
        'longDescription': '''
Specifies the minimum frequency component of the input signal for AC
measurements. This property affects the DMM only when you set the
Function property to AC measurements. The valid range is 1 Hz-300 kHz
for the NI 4080/4081/4082 and NI 4070/4071/4072, 10 Hz-100 Hz for the NI
4065, and 20 Hz-25 kHz for the NI 4050 and NI 4060.

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 64-bit floating point   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Configuration:Measurement Options:Min Frequency
''',
        'shortDescription': '''
Specifies the minimum frequency component of the input signal for AC
measurements. This property affects the DMM only when you set the
Function property to AC measurements. The valid range is 1 Hz-300 kHz
for the NI 4080/4081/4082 and NI 4070/4071/4072, 10 Hz-100 Hz for the NI
4065, and 20 Hz-25 kHz for the NI 4050 and NI 4060.

''',
    },
    '1250007': {
        'longDescription': '''
Specifies the maximum frequency component of the input signal for AC
measurements. This property is used only for error checking and verifies
that the value of this parameter is less than the maximum frequency of
the device. This property affects the DMM only when you set the Function
property to AC measurements.

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
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Configuration:Measurement Options:Max Frequency
''',
        'shortDescription': '''
Specifies the maximum frequency component of the input signal for AC
measurements. This property is used only for error checking and verifies
that the value of this parameter is less than the maximum frequency of
the device. This property affects the DMM only when you set the Function
property to AC measurements.

''',
    },
    '1250008': {
        'longDescription': '''
Specifies the measurement resolution in absolute units. Setting this
property to higher values increases the measurement accuracy. Setting
this property to lower values increases the measurement speed.

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
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Configuration:Absolute Resolution
''',
        'shortDescription': '''
Specifies the measurement resolution in absolute units. Setting this
property to higher values increases the measurement accuracy. Setting
this property to lower values increases the measurement speed.

''',
    },
    '1250101': {
        'longDescription': '''
For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the maximum
amplitude of the input signal for frequency measurements.

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
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Configuration:Measurement Options:Frequency Voltage Range
''',
        'shortDescription': '''
For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the maximum
amplitude of the input signal for frequency measurements.

''',
    },
    '1250201': {
        'longDescription': '''
Specifies the transducer type.

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
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Configuration:Measurement Options:Temperature:Transducer Type
''',
        'shortDescription': '''
Specifies the transducer type.

''',
    },
    '1250231': {
        'longDescription': '''
Specifies the thermocouple type.

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
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Configuration:Measurement Options:Temperature:Thermocouple:Thermocouple Type
''',
        'shortDescription': '''
Specifies the thermocouple type.

''',
    },
    '1250232': {
        'longDescription': '''
Specifies the thermocouple reference junction type.

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
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Configuration:Measurement Options:Temperature:Thermocouple:Reference Junction Type
''',
        'shortDescription': '''
Specifies the thermocouple reference junction type.

''',
    },
    '1250233': {
        'longDescription': '''
Specifies the value of the fixed reference junction temperature for a
thermocouple in degrees Celsius.

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 64-bit floating point   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Configuration:Measurement Options:Temperature:Thermocouple:Fixed Reference Junction
''',
        'shortDescription': '''
Specifies the value of the fixed reference junction temperature for a
thermocouple in degrees Celsius.

''',
    },
    '1250242': {
        'longDescription': '''
Specifies the RTD resistance at 0 degrees Celsius.

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 64-bit floating point   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD Resistance
''',
        'shortDescription': '''
Specifies the RTD resistance at 0 degrees Celsius.

''',
    },
    '1250301': {
        'longDescription': '''
Specifies the number of measurements the DMM takes each time it receives
a trigger in a multiple point acquisition. Setting Sample Count to 0 on
the NI 4050 and NI 4060 causes the device to take continuous
measurements. Otherwise, setting Sample Count to 0 causes the
conditional statement "Measurements equal to Sample Count" to always
evaluate to False, and causes the DMM to continue taking measurements in
the inner loop.

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Multi Point Acquisition:Sample Count
''',
        'shortDescription': '''
Specifies the number of measurements the DMM takes each time it receives
a trigger in a multiple point acquisition. Setting Sample Count to 0 on
the NI 4050 and NI 4060 causes the device to take continuous
measurements. Otherwise, setting Sample Count to 0 causes the
conditional statement "Measurements equal to Sample Count" to always
evaluate to False, and causes the DMM to continue taking measurements in
the inner loop.

''',
    },
    '1250302': {
        'longDescription': '''
Specifies the sample trigger source.

To determine which values are supported by each device, refer to the
LabVIEW Trigger Routing section in the *NI Digital Multimeters Help* .

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
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Multi Point Acquisition:Sample Trigger
''',
        'shortDescription': '''
Specifies the sample trigger source.

To determine which values are supported by each device, refer to the
LabVIEW Trigger Routing section in the *NI Digital Multimeters Help* .

''',
    },
    '1250303': {
        'longDescription': '''
Specifies the amount of time in seconds the DMM waits between
measurement cycles. This property only applies when the Sample Trigger
property is set to INTERVAL. The default value (-1) ensures that the DMM
settles for a recommended time, which is the same as using an immediate
trigger.

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
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Multi Point Acquisition:Sample Interval
''',
        'shortDescription': '''
Specifies the amount of time in seconds the DMM waits between
measurement cycles. This property only applies when the Sample Trigger
property is set to INTERVAL. The default value (-1) ensures that the DMM
settles for a recommended time, which is the same as using an immediate
trigger.

''',
    },
    '1250304': {
        'longDescription': '''
Specifies the number of triggers the DMM receives before returning to
the Idle state. This property can be set to any positive ViInt32 value
for the NI 4065, NI 4070/4071/4072, and NI 4080/4081/4082.

The NI 4050/4060 only support this property being set to 1.

Refer to Multiple Point Acquisitions in the *NI Digital Multimeters
Help* for more information.

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 32-bit signed integer   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Multi Point Acquisition:Trigger Count
''',
        'shortDescription': '''
Specifies the number of triggers the DMM receives before returning to
the Idle state. This property can be set to any positive ViInt32 value
for the NI 4065, NI 4070/4071/4072, and NI 4080/4081/4082.

The NI 4050/4060 only support this property being set to 1.

Refer to Multiple Point Acquisitions in the *NI Digital Multimeters
Help* for more information.

''',
    },
    '1250305': {
        'longDescription': '''
Specifies the destination of the measurement complete (MC) signal.

To determine which values are supported by each device, refer to the
LabVIEW Trigger Routing section in the *NI Digital Multimeters Help* .

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
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Trigger:Measurement Complete Dest
''',
        'shortDescription': '''
Specifies the destination of the measurement complete (MC) signal.

To determine which values are supported by each device, refer to the
LabVIEW Trigger Routing section in the *NI Digital Multimeters Help* .

''',
    },
    '1250321': {
        'longDescription': '''
Specifies the measurement aperture time for the current configuration.
Aperture time is specified in units set by the Aperture Time Units
property. To override the default aperture, set this property to the
desired aperture time after calling niDMM Config Measurement . To return
to the default, set this property to Aperture Time Auto (-1).

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
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Configuration:Advanced:Aperture Time
''',
        'shortDescription': '''
Specifies the measurement aperture time for the current configuration.
Aperture time is specified in units set by the Aperture Time Units
property. To override the default aperture, set this property to the
desired aperture time after calling niDMM Config Measurement . To return
to the default, set this property to Aperture Time Auto (-1).

''',
    },
    '1250322': {
        'longDescription': '''
Specifies the units of aperture time for the current configuration.

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
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Configuration:Advanced:Aperture Time Units
''',
        'shortDescription': '''
Specifies the units of aperture time for the current configuration.

''',
    },
    '1250331': {
        'longDescription': '''
Specifies the value of the range. If auto ranging is enabled, shows the
actual value of the active range. The value of this property is set
during a read operation.

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 64-bit floating point   |
+------------------+-------------------------+
| Permissions      | Read Only               |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Configuration:Auto Range Value
''',
        'shortDescription': '''
Specifies the value of the range. If auto ranging is enabled, shows the
actual value of the active range. The value of this property is set
during a read operation.

''',
    },
    '1250332': {
        'longDescription': '''
Specifies the AutoZero mode. This property is not supported for the NI
4050.

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
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Configuration:Measurement Options:Auto Zero
''',
        'shortDescription': '''
Specifies the AutoZero mode. This property is not supported for the NI
4050.

''',
    },
    '1250333': {
        'longDescription': '''
Specifies the powerline frequency. The NI 4060 and NI 4050 use this
value to select an aperture time to reject powerline noise by selecting
the appropriate internal sample clock and filter. The NI 4065, NI
4070/4071/4072, and NI 4080/4081/4082 use this value to select timebases
for setting the Aperture Time property in powerline cycles.

After configuring powerline frequency, set the Aperture Time Units
property to PLCs. When setting the Aperture Time property, select the
number of PLCs for the powerline frequency. For example, if powerline
frequency = 50 Hz (or 20 ms) and aperture time in PLCs = 5, then
aperture time in seconds = 20 ms \* 5 PLCs = 100 ms. Similarly, if
powerline frequency = 60 Hz (or 16.667 ms) and aperture time in PLCs =
6, then aperture time in seconds = 16.667 ms \* 6 PLCs = 100 ms.

.. note::
   For 400 Hz powerline frequency, use the 50 Hz setting.  

+--------------------+-----------------------------------------------+
| Name               | Description                                   |
+--------------------+-----------------------------------------------+
| **50 Hz** (50.0)   | Specifies the powerline frequency as 50 Hz.   |
+--------------------+-----------------------------------------------+
| **60 Hz** (60.0)   | Specifies the powerline frequency as 60 Hz.   |
+--------------------+-----------------------------------------------+

The following table lists the characteristics of this property.

+------------------+-------------------------+
| Characteristic   | Value                   |
+------------------+-------------------------+
| Datatype         | 64-bit floating point   |
+------------------+-------------------------+
| Permissions      | Read/Write              |
+------------------+-------------------------+
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Configuration:Measurement Options:Powerline Frequency
''',
        'shortDescription': '''
Specifies the powerline frequency. The NI 4060 and NI 4050 use this
value to select an aperture time to reject powerline noise by selecting
the appropriate internal sample clock and filter. The NI 4065, NI
4070/4071/4072, and NI 4080/4081/4082 use this value to select timebases
for setting the Aperture Time property in powerline cycles.

''',
    },
    '1250334': {
        'longDescription': '''
Specifies the edge of the signal from the specified trigger source on
which the DMM is triggered.

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
| Channel Based    | False                   |
+------------------+-------------------------+
| Resettable       | No                      |
+------------------+-------------------------+

''',
        'lv_property': '''
Trigger:Trigger Slope
''',
        'shortDescription': '''
Specifies the edge of the signal from the specified trigger source on
which the DMM is triggered.

''',
    },
}
