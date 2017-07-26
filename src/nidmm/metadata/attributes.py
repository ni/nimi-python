# -*- coding: utf-8 -*-
attributes = {
    -2: {
        'access': 'write only',
        'enum': None,
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
        'lv_property': 'Active Channel',
        'name': 'ACTIVE_CHANNEL',
        'shortDescription': '''
Specifies the channel name used to access all subsequent channel-based
properties in this property node. Set the channel before setting
channel-based properties. Pass a name that the instrument driver defines
or a virtual channel name configured in MAX.
''',
        'type': 'ViString',
    },
    1050002: {
        'access': 'read-write',
        'enum': None,
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
        'lv_property': 'Inherent IVI Attributes:User Options:Range Check',
        'name': 'RANGE_CHECK',
        'shortDescription': '''
Specifies whether to validate property values and VI parameters. If
enabled, the instrument driver validates the parameter values passed to
driver VIs. Range checking parameters is very useful for debugging.
After the user program is validated, you can set this property to FALSE
(0) to disable range checking and maximize performance. The default
value is TRUE (1). Use niDMM Initialize With Options to override the
default setting.
''',
        'type': 'ViBoolean',
    },
    1050003: {
        'access': 'read-write',
        'enum': None,
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
        'name': 'QUERY_INSTRUMENT_STATUS',
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
        'type': 'ViBoolean',
    },
    1050004: {
        'access': 'read-write',
        'enum': None,
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
        'lv_property': 'Inherent IVI Attributes:User Options:Cache',
        'name': 'CACHE',
        'shortDescription': '''
Specifies whether to cache the value of properties. When caching is
enabled, the instrument driver keeps track of the current instrument
settings and avoids sending redundant commands to the instrument. Thus,
it significantly increases execution speed. The instrument driver can
choose to always cache or to never cache particular properties
regardless of the setting of this property. The default value is TRUE
(1). Use niDMM Initialize With Options to override the default setting.
''',
        'type': 'ViBoolean',
    },
    1050005: {
        'access': 'read-write',
        'enum': None,
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
        'lv_property': 'Inherent IVI Attributes:User Options:Simulate',
        'name': 'SIMULATE',
        'shortDescription': '''
Specifies whether to simulate instrument driver I/O operations. If
simulation is enabled, instrument driver functions perform range
checking and call IVI Get and Set VIs, but they do not perform
instrument I/O. For output parameters that represent instrument data,
the instrument driver VIs return calculated values. The default value is
FALSE (0). Use niDMM Initialize With Options to override the default
setting.
''',
        'type': 'ViBoolean',
    },
    1050006: {
        'access': 'read-write',
        'enum': None,
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
        'name': 'RECORD_VALUE_COERCIONS',
        'shortDescription': '''
Specifies whether the IVI engine keeps a list of the value coercions it
makes for ViInt32 and ViReal64 properties. The default value is FALSE
(0). Use niDMM Initialize With Options to override the default setting.
Use niDMM Get Next Coercion Record to extract and delete the oldest
coercion record from the list.
''',
        'type': 'ViBoolean',
    },
    1050007: {
        'access': 'read only',
        'enum': None,
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
        'lv_property': 'Inherent IVI Attributes:User Options:Driver Setup',
        'name': 'DRIVER_SETUP',
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
        'type': 'ViString',
    },
    1050021: {
        'access': 'read-write',
        'enum': None,
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
        'name': 'INTERCHANGE_CHECK',
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
        'type': 'ViBoolean',
    },
    1050101: {
        'access': 'read-write',
        'enum': None,
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
        'name': 'PRIMARY_ERROR',
        'shortDescription': '''
A code that describes the first error that occurred since the last call
to niDMM Get Error for the session. The value follows the VXIplug&play
conventions. A negative value describes an error condition. A positive
value describes a warning condition. A zero indicates that no error or
warning occurred. The error and warning values can be status codes
defined by IVI, VISA, class drivers, or specific drivers.
''',
        'type': 'ViInt32',
    },
    1050102: {
        'access': 'read-write',
        'enum': None,
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
        'name': 'SECONDARY_ERROR',
        'shortDescription': '''
An optional code that provides additional information concerning the
primary error condition. The error and warning values can be status
codes defined by IVI, VISA, class drivers, or specific drivers. Zero
indicates no additional information.
''',
        'type': 'ViInt32',
    },
    1050103: {
        'access': 'read-write',
        'enum': None,
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
        'name': 'ERROR_ELABORATION',
        'shortDescription': '''
An optional string that contains additional information concerning the
primary error condition.
''',
        'type': 'ViString',
    },
    1050203: {
        'access': 'read only',
        'enum': None,
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
        'name': 'CHANNEL_COUNT',
        'shortDescription': '''
Indicates the number of channels that the specific instrument driver
supports. For each property for which the IVI\_VAL\_MULTI\_CHANNEL flag
property is set, the IVI engine maintains a separate cache value for
each channel.
''',
        'type': 'ViInt32',
    },
    1050302: {
        'access': 'read only',
        'enum': None,
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
        'name': 'SPECIFIC_DRIVER_PREFIX',
        'shortDescription': '''
The prefix for the specific instrument driver. The name of each
user-callable VI in this driver starts with this prefix. The prefix can
be up to a maximum of eight characters.
''',
        'type': 'ViString',
    },
    1050304: {
        'access': 'read only',
        'enum': None,
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
        'name': 'IO_RESOURCE_DESCRIPTOR',
        'shortDescription': '''
A string containing the resource descriptor of the instrument.
''',
        'type': 'ViString',
    },
    1050305: {
        'access': 'read only',
        'enum': None,
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
        'name': 'LOGICAL_NAME',
        'shortDescription': '''
A string containing the logical name of the instrument.
''',
        'type': 'ViString',
    },
    1050327: {
        'access': 'read only',
        'enum': None,
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
        'name': 'SUPPORTED_INSTRUMENT_MODELS',
        'shortDescription': '''
A string containing the instrument models supported by the specific
driver.
''',
        'type': 'ViString',
    },
    1050401: {
        'access': 'read only',
        'enum': None,
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
        'name': 'GROUP_CAPABILITIES',
        'shortDescription': '''
A string containing the capabilities and extension groups supported by
the specific driver.
''',
        'type': 'ViString',
    },
    1050501: {
        'access': 'read only',
        'enum': None,
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
        'name': 'ENGINE_MAJOR_VERSION',
        'shortDescription': 'The major version number of the IVI engine.',
        'type': 'ViInt32',
    },
    1050502: {
        'access': 'read only',
        'enum': None,
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
        'name': 'ENGINE_MINOR_VERSION',
        'shortDescription': 'The minor version number of the IVI engine.',
        'type': 'ViInt32',
    },
    1050503: {
        'access': 'read only',
        'enum': None,
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
        'name': 'SPECIFIC_DRIVER_MAJOR_VERSION',
        'shortDescription': '''
Returns the major version number of this instrument driver.
''',
        'type': 'ViInt32',
    },
    1050504: {
        'access': 'read only',
        'enum': None,
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
        'name': 'SPECIFIC_DRIVER_MINOR_VERSION',
        'shortDescription': '''
Returns the minor version number of this instrument driver.
''',
        'type': 'ViInt32',
    },
    1050510: {
        'access': 'read only',
        'enum': None,
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
        'name': 'INSTRUMENT_FIRMWARE_REVISION',
        'shortDescription': '''
A string containing the instrument firmware revision number.
''',
        'type': 'ViString',
    },
    1050511: {
        'access': 'read only',
        'enum': None,
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
        'name': 'INSTRUMENT_MANUFACTURER',
        'shortDescription': '''
A string containing the manufacturer of the instrument.
''',
        'type': 'ViString',
    },
    1050512: {
        'access': 'read only',
        'enum': None,
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
        'name': 'INSTRUMENT_MODEL',
        'shortDescription': 'A string containing the instrument model.',
        'type': 'ViString',
    },
    1050513: {
        'access': 'read only',
        'enum': None,
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
        'name': 'SPECIFIC_DRIVER_VENDOR',
        'shortDescription': '''
A string containing the vendor of the specific driver.
''',
        'type': 'ViString',
    },
    1050514: {
        'access': 'read only',
        'enum': None,
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
        'name': 'SPECIFIC_DRIVER_DESCRIPTION',
        'shortDescription': '''
A string containing a description of the specific driver.
''',
        'type': 'ViString',
    },
    1050515: {
        'access': 'read only',
        'enum': None,
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
        'name': 'SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION',
        'shortDescription': '''
The major version number of the class specification for the specific
driver.
''',
        'type': 'ViInt32',
    },
    1050516: {
        'access': 'read only',
        'enum': None,
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
        'name': 'SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION',
        'shortDescription': '''
The minor version number of the class specification for the specific
driver.
''',
        'type': 'ViInt32',
    },
    1050551: {
        'access': 'read only',
        'enum': None,
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
        'name': 'SPECIFIC_DRIVER_REVISION',
        'shortDescription': '''
A string that contains additional version information about this
instrument driver.
''',
        'type': 'ViString',
    },
    1050553: {
        'access': 'read only',
        'enum': None,
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
        'name': 'ENGINE_REVISION',
        'shortDescription': '''
A string that contains additional version information about the IVI
engine.
''',
        'type': 'ViString',
    },
    1150001: {
        'access': 'read only',
        'enum': None,
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
        'lv_property': 'Obsolete:Misc:IDQuery response',
        'name': 'IDQUERY_RESPONSE',
        'shortDescription': '''
A string containing the type of instrument used in the current session.
''',
        'type': 'ViString',
    },
    1150002: {
        'access': 'read-write',
        'enum': 'MeasurementDestinationSlope',
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
        'lv_property': 'Trigger:Measurement Destination Slope',
        'name': 'MEASUREMENT_DESTINATION_SLOPE',
        'shortDescription': '''
Specifies the polarity of the generated measurement complete signal.
''',
        'type': 'ViInt32',
    },
    1150003: {
        'access': 'read-write',
        'enum': None,
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
        'lv_property': 'Configuration:Measurement Options:Shunt Value',
        'name': 'SHUNT_VALUE',
        'shortDescription': '''
For the NI 4050 only, specifies the shunt resistance value.
''',
        'type': 'ViReal64',
    },
    1150010: {
        'access': 'read-write',
        'enum': 'SampleTrigSlope',
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
        'lv_property': 'Multi Point Acquisition:Sample Trig Slope',
        'name': 'SAMPLE_TRIG_SLOPE',
        'shortDescription': '''
Specifies the edge of the signal from the specified sample trigger
source on which the DMM is triggered.
''',
        'type': 'ViInt32',
    },
    1150014: {
        'access': 'read-write',
        'enum': 'OperationMode',
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
        'lv_property': 'Configuration:Advanced:Operation Mode',
        'name': 'OPERATION_MODE',
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
        'type': 'ViInt32',
    },
    1150018: {
        'access': 'read-write',
        'enum': None,
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
        'lv_property': 'Waveform Acquisition:Waveform Rate',
        'name': 'WAVEFORM_RATE',
        'shortDescription': '''
Specifies the rate of the waveform acquisition in samples per second
(S/s). The valid rate is calculated by dividing 1,800,000 by an integer
divisor, and the rate falls between 10 and 1,800,000 samples per second.
The waveform rate is coerced upwards to the next valid rate. The default
value is 1,800,000 samples per second. Not supported by NI 4065.
''',
        'type': 'ViReal64',
    },
    1150019: {
        'access': 'read-write',
        'enum': None,
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
        'lv_property': 'Waveform Acquisition:Waveform Points',
        'name': 'WAVEFORM_POINTS',
        'shortDescription': '''
For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the number of
points to acquire in a waveform acquisition.
''',
        'type': 'ViInt32',
    },
    1150022: {
        'access': 'read-write',
        'enum': 'ADCCalibration',
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
        'lv_property': 'Configuration:Measurement Options:ADC Calibration',
        'name': 'ADC_CALIBRATION',
        'shortDescription': '''
For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the ADC
calibration mode.
''',
        'type': 'ViInt32',
    },
    1150023: {
        'access': 'read-write',
        'enum': 'OffsetCompensatedOhms',
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
        'name': 'OFFSET_COMPENSATED_OHMS',
        'shortDescription': '''
For the NI 4080/4081/4082 and NI 4070/4071/4072, enables or disables
offset compensated ohms.
''',
        'type': 'ViInt32',
    },
    1150025: {
        'access': 'read-write',
        'enum': 'CurrentSource',
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
        'lv_property': 'Configuration:Measurement Options:Current Source',
        'name': 'CURRENT_SOURCE',
        'shortDescription': '''
Specifies the current source provided during diode measurements.

The NI 4050 and NI 4060 are not supported.
''',
        'type': 'ViReal64',
    },
    1150026: {
        'access': 'read-write',
        'enum': 'DCNoiseRejection',
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
        'name': 'DC_NOISE_REJECTION',
        'shortDescription': 'Specifies the DC noise rejection mode.',
        'type': 'ViInt32',
    },
    1150027: {
        'access': 'read-write',
        'enum': 'WaveformCoupling',
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
        'lv_property': 'Waveform Acquisition:Waveform Coupling',
        'name': 'WAVEFORM_COUPLING',
        'shortDescription': '''
For the NI 4080/4081/4082 and NI 4070/4071/4072 only, specifies the
coupling during a waveform acquisition.
''',
        'type': 'ViInt32',
    },
    1150028: {
        'access': 'read-write',
        'enum': None,
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
        'lv_property': 'Configuration:Advanced:Settle Time',
        'name': 'SETTLE_TIME',
        'shortDescription': '''
Specifies the settling time in seconds. Use this property to override
the default settling time. To return to the default, set this property
to Auto (-1).
''',
        'type': 'ViReal64',
    },
    1150029: {
        'access': 'read-write',
        'enum': 'InputResistance',
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
        'name': 'INPUT_RESISTANCE',
        'shortDescription': '''
Specifies the input resistance of the instrument.
''',
        'type': 'ViReal64',
    },
    1150031: {
        'access': 'read-write',
        'enum': None,
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
        'lv_property': 'Multi Point Acquisition:Sample Delay Mode',
        'name': 'SAMPLE_DELAY_MODE',
        'shortDescription': '''
For the NI 4060 only, specifies a delay interval after a sample trigger.
''',
        'type': 'ViInt32',
    },
    1150032: {
        'access': 'read-write',
        'enum': None,
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
        'lv_property': 'Configuration:Advanced:Number Of Averages',
        'name': 'NUMBER_OF_AVERAGES',
        'shortDescription': '''
Specifies the number of averages to perform in a measurement. For the NI
4080/4081/4082 and NI 4070/4071/4072, applies only when the aperture
time is not set to Auto and Auto Zero is ON. The Number of Averages
Property will be ignored otherwise. The default is 4 for 7 1/2 digits;
otherwise, the default is 1.

The NI 4050 and NI 4060 are not supported.
''',
        'type': 'ViInt32',
    },
    1150034: {
        'access': 'read-write',
        'enum': None,
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
        'lv_property': 'Multi Point Acquisition:Advanced:Latency',
        'name': 'LATENCY',
        'shortDescription': '''
Specifies the number of measurements transferred at a time from the
instrument to an internal buffer. When set to Auto (-1), NI-DMM chooses
the transfer size.
''',
        'type': 'ViInt32',
    },
    1150037: {
        'access': 'read-write',
        'enum': None,
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
        'lv_property': 'Multi Point Acquisition:Advanced:Buffer Size',
        'name': 'BUFFER_SIZE',
        'shortDescription': '''
Specifies the size in samples of the internal data buffer. Maximum size
is 134,217,727 (0X7FFFFFF) samples. When set to Auto (-1), NI-DMM
chooses the buffer size.
''',
        'type': 'ViInt32',
    },
    1150044: {
        'access': 'read only',
        'enum': None,
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
        'name': 'FREQUENCY_VOLTAGE_AUTO_RANGE_VALUE',
        'shortDescription': '''
For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the value of
the frequency voltage range. If auto ranging is enabled, shows the
actual value of the active frequency voltage range. If not Auto Ranging,
the value is the same as that of the Frequency Voltage Range property.
''',
        'type': 'ViReal64',
    },
    1150045: {
        'access': 'read-write',
        'enum': 'CableCompensationType',
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
        'name': 'CABLE_COMPENSATION_TYPE',
        'shortDescription': '''
For the NI 4081 and NI 4072 only, specifies the type of cable
compensation that is applied to the current capacitance or inductance
measurement for the current range.
''',
        'type': 'ViInt32',
    },
    1150046: {
        'access': 'read-write',
        'enum': None,
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
        'name': 'REACTANCE',
        'shortDescription': '''
For the NI 4082 and NI 4072 only, represents the reactive part
(reactance) of the short cable compensation. The valid range is any real
number >0. The default value (-1) indicates that compensation has not
taken place.
''',
        'type': 'ViReal64',
    },
    1150047: {
        'access': 'read-write',
        'enum': None,
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
        'name': 'RESISTANCE',
        'shortDescription': '''
For the NI 4082 and NI 4072 only, represents the active part
(resistance) of the short cable compensation. The valid range is any
real number >0. The default value (-1) indicates that compensation has
not taken place.
''',
        'type': 'ViReal64',
    },
    1150048: {
        'access': 'read-write',
        'enum': None,
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
        'name': 'SUSCEPTANCE',
        'shortDescription': '''
For the NI 4082 and NI 4072 only, specifies the reactive part
(susceptance) of the open cable compensation. The valid range is any
real number >0. The default value (-1.0) indicates that compensation has
not taken place.
''',
        'type': 'ViReal64',
    },
    1150049: {
        'access': 'read-write',
        'enum': None,
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
        'name': 'CONDUCTANCE',
        'shortDescription': '''
For the NI 4082 and NI 4072 only, specifies the active part
(conductance) of the open cable compensation. The valid range is any
real number >0. The default value (-1.0) indicates that compensation has
not taken place.
''',
        'type': 'ViReal64',
    },
    1150052: {
        'access': 'read-write',
        'enum': 'LCCalculationModel',
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
        'name': 'LC_CALCULATION_MODEL',
        'shortDescription': '''
For the NI 4082 and NI 4072 only, specifies the type of algorithm that
the measurement processing uses for capacitance and inductance
measurements.
''',
        'type': 'ViInt32',
    },
    1150053: {
        'access': 'read-write',
        'enum': 'DCBias',
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
        'name': 'DC_BIAS',
        'shortDescription': '''
For the NI 4082 and NI 4072 only, controls the available DC bias for
capacitance measurements.
''',
        'type': 'ViInt32',
    },
    1150054: {
        'access': 'read only',
        'enum': None,
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
        'name': 'INSTRUMENT_SERIAL_NUMBER',
        'shortDescription': '''
A string containing the serial number of the instrument. This property
corresponds to the serial number label that is attached to most
products.
''',
        'type': 'ViString',
    },
    1150055: {
        'access': 'read-write',
        'enum': None,
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
        'name': 'NUMBER_OF_LC_MEASUREMENTS_TO_AVERAGE',
        'shortDescription': '''
For the NI 4082 and NI 4072 only, specifies the number of LC
measurements that are averaged to produce one reading.
''',
        'type': 'ViInt32',
    },
    1150061: {
        'access': 'read only',
        'enum': None,
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
        'name': 'INSTRUMENT_PRODUCT_ID',
        'shortDescription': 'The PCI product ID.',
        'type': 'ViInt32',
    },
    1150120: {
        'access': 'read-write',
        'enum': 'RTDType',
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
        'name': 'RTD_TYPE',
        'shortDescription': 'Specifies the RTD type.',
        'type': 'ViInt32',
    },
    1150121: {
        'access': 'read-write',
        'enum': None,
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
        'name': 'RTD_A',
        'shortDescription': '''
Specifies the Callendar-Van Dusen A coefficient for RTD scaling when the
**RTD Type property** is set to Custom.
''',
        'type': 'ViReal64',
    },
    1150122: {
        'access': 'read-write',
        'enum': None,
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
        'name': 'RTD_B',
        'shortDescription': '''
Specifies the Callendar-Van Dusen B coefficient for RTD scaling when the
**RTD Type property** is set to Custom.
''',
        'type': 'ViReal64',
    },
    1150123: {
        'access': 'read-write',
        'enum': None,
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
        'name': 'RTD_C',
        'shortDescription': '''
Specifies the Callendar-Van Dusen C coefficient for RTD scaling when the
**RTD Type property** is set to Custom.
''',
        'type': 'ViReal64',
    },
    1150124: {
        'access': 'read-write',
        'enum': 'ThermistorType',
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
        'name': 'THERMISTOR_TYPE',
        'shortDescription': 'Specifies the thermistor type.',
        'type': 'ViInt32',
    },
    1150125: {
        'access': 'read-write',
        'enum': None,
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
        'name': 'THERMISTOR_A',
        'shortDescription': '''
Specifies the Steinhart-Hart A coefficient for thermistor scaling when
the **Thermistor Type property** is set to Custom.
''',
        'type': 'ViReal64',
    },
    1150126: {
        'access': 'read-write',
        'enum': None,
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
        'name': 'THERMISTOR_B',
        'shortDescription': '''
Specifies the Steinhart-Hart B coefficient for thermistor scaling when
the **Thermistor Type property** is set to Custom.
''',
        'type': 'ViReal64',
    },
    1150127: {
        'access': 'read-write',
        'enum': None,
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
        'name': 'THERMISTOR_C',
        'shortDescription': '''
Specifies the Steinhart-Hart C coefficient for thermistor scaling when
the **Thermistor Type property** is set to Custom.
''',
        'type': 'ViReal64',
    },
    1250001: {
        'access': 'read-write',
        'enum': 'Function',
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
        'lv_property': 'Configuration:Function',
        'name': 'FUNCTION',
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
        'type': 'ViInt32',
    },
    1250002: {
        'access': 'read-write',
        'enum': None,
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
        'lv_property': 'Configuration:Range',
        'name': 'RANGE',
        'shortDescription': '''
Specifies the measurement range. Use positive values to represent the
absolute value of the maximum expected measurement. The value is in
units appropriate for the current value of the Function property. For
example, if the Function property is set to DC Volts, the units are
volts.
''',
        'type': 'ViReal64',
    },
    1250003: {
        'access': 'read-write',
        'enum': 'DigitsResolution',
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
        'lv_property': 'Configuration:Digits Resolution',
        'name': 'DIGITS_RESOLUTION',
        'shortDescription': '''
Specifies the measurement resolution in digits. Setting this property to
higher values increases the measurement accuracy. Setting this property
to lower values increases the measurement speed.
''',
        'type': 'ViReal64',
    },
    1250004: {
        'access': 'read-write',
        'enum': 'TriggerSource',
        'longDescription': '''
Specifies the trigger source. When niDMM Initiate is called, the DMM
waits for the trigger specified with this property. After it receives
the trigger, the DMM waits the length of time specified with the Trigger
Delay property. The DMM then takes a measurement.

To determine which values are supported by each device, refer to the
LabVIEW Trigger Routing section in the *NI Digital Multimeters Help*.

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
        'lv_property': 'Trigger:Trigger Source',
        'name': 'TRIGGER_SOURCE',
        'shortDescription': '''
Specifies the trigger source. When niDMM Initiate is called, the DMM
waits for the trigger specified with this property. After it receives
the trigger, the DMM waits the length of time specified with the Trigger
Delay property. The DMM then takes a measurement.

To determine which values are supported by each device, refer to the
LabVIEW Trigger Routing section in the *NI Digital Multimeters Help*.
''',
        'type': 'ViInt32',
    },
    1250005: {
        'access': 'read-write',
        'enum': None,
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
        'lv_property': 'Trigger:Trigger Delay',
        'name': 'TRIGGER_DELAY',
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
        'type': 'ViReal64',
    },
    1250006: {
        'access': 'read-write',
        'enum': None,
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
        'lv_property': 'Configuration:Measurement Options:Min Frequency',
        'name': 'MIN_FREQUENCY',
        'shortDescription': '''
Specifies the minimum frequency component of the input signal for AC
measurements. This property affects the DMM only when you set the
Function property to AC measurements. The valid range is 1 Hz-300 kHz
for the NI 4080/4081/4082 and NI 4070/4071/4072, 10 Hz-100 Hz for the NI
4065, and 20 Hz-25 kHz for the NI 4050 and NI 4060.
''',
        'type': 'ViReal64',
    },
    1250007: {
        'access': 'read-write',
        'enum': None,
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
        'lv_property': 'Configuration:Measurement Options:Max Frequency',
        'name': 'MAX_FREQUENCY',
        'shortDescription': '''
Specifies the maximum frequency component of the input signal for AC
measurements. This property is used only for error checking and verifies
that the value of this parameter is less than the maximum frequency of
the device. This property affects the DMM only when you set the Function
property to AC measurements.
''',
        'type': 'ViReal64',
    },
    1250008: {
        'access': 'read-write',
        'enum': None,
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
        'lv_property': 'Configuration:Absolute Resolution',
        'name': 'ABSOLUTE_RESOLUTION',
        'shortDescription': '''
Specifies the measurement resolution in absolute units. Setting this
property to higher values increases the measurement accuracy. Setting
this property to lower values increases the measurement speed.
''',
        'type': 'ViReal64',
    },
    1250101: {
        'access': 'read-write',
        'enum': None,
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
        'name': 'FREQUENCY_VOLTAGE_RANGE',
        'shortDescription': '''
For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the maximum
amplitude of the input signal for frequency measurements.
''',
        'type': 'ViReal64',
    },
    1250201: {
        'access': 'read-write',
        'enum': 'TransducerType',
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
        'name': 'TRANSDUCER_TYPE',
        'shortDescription': 'Specifies the transducer type.',
        'type': 'ViInt32',
    },
    1250231: {
        'access': 'read-write',
        'enum': 'ThermocoupleType',
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
        'name': 'THERMOCOUPLE_TYPE',
        'shortDescription': 'Specifies the thermocouple type.',
        'type': 'ViInt32',
    },
    1250232: {
        'access': 'read-write',
        'enum': 'ThermocoupleReferenceJunctionType',
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
        'name': 'TC_REF_JUNCTION_TYPE',
        'shortDescription': '''
Specifies the thermocouple reference junction type.
''',
        'type': 'ViInt32',
    },
    1250233: {
        'access': 'read-write',
        'enum': None,
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
        'name': 'TC_FIXED_REF_JUNCTION',
        'shortDescription': '''
Specifies the value of the fixed reference junction temperature for a
thermocouple in degrees Celsius.
''',
        'type': 'ViReal64',
    },
    1250242: {
        'access': 'read-write',
        'enum': None,
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
        'name': 'RTD_RESISTANCE',
        'shortDescription': '''
Specifies the RTD resistance at 0 degrees Celsius.
''',
        'type': 'ViReal64',
    },
    1250301: {
        'access': 'read-write',
        'enum': None,
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
        'lv_property': 'Multi Point Acquisition:Sample Count',
        'name': 'SAMPLE_COUNT',
        'shortDescription': '''
Specifies the number of measurements the DMM takes each time it receives
a trigger in a multiple point acquisition. Setting Sample Count to 0 on
the NI 4050 and NI 4060 causes the device to take continuous
measurements. Otherwise, setting Sample Count to 0 causes the
conditional statement "Measurements equal to Sample Count" to always
evaluate to False, and causes the DMM to continue taking measurements in
the inner loop.
''',
        'type': 'ViInt32',
    },
    1250302: {
        'access': 'read-write',
        'enum': 'SampleTrigger',
        'longDescription': '''
Specifies the sample trigger source.

To determine which values are supported by each device, refer to the
LabVIEW Trigger Routing section in the *NI Digital Multimeters Help*.

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
        'lv_property': 'Multi Point Acquisition:Sample Trigger',
        'name': 'SAMPLE_TRIGGER',
        'shortDescription': '''
Specifies the sample trigger source.

To determine which values are supported by each device, refer to the
LabVIEW Trigger Routing section in the *NI Digital Multimeters Help*.
''',
        'type': 'ViInt32',
    },
    1250303: {
        'access': 'read-write',
        'enum': None,
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
        'lv_property': 'Multi Point Acquisition:Sample Interval',
        'name': 'SAMPLE_INTERVAL',
        'shortDescription': '''
Specifies the amount of time in seconds the DMM waits between
measurement cycles. This property only applies when the Sample Trigger
property is set to INTERVAL. The default value (-1) ensures that the DMM
settles for a recommended time, which is the same as using an immediate
trigger.
''',
        'type': 'ViReal64',
    },
    1250304: {
        'access': 'read-write',
        'enum': None,
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
        'lv_property': 'Multi Point Acquisition:Trigger Count',
        'name': 'TRIGGER_COUNT',
        'shortDescription': '''
Specifies the number of triggers the DMM receives before returning to
the Idle state. This property can be set to any positive ViInt32 value
for the NI 4065, NI 4070/4071/4072, and NI 4080/4081/4082.

The NI 4050/4060 only support this property being set to 1.

Refer to Multiple Point Acquisitions in the *NI Digital Multimeters
Help* for more information.
''',
        'type': 'ViInt32',
    },
    1250305: {
        'access': 'read-write',
        'enum': 'MeasurementCompleteDest',
        'longDescription': '''
Specifies the destination of the measurement complete (MC) signal.

To determine which values are supported by each device, refer to the
LabVIEW Trigger Routing section in the *NI Digital Multimeters Help*.

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
        'lv_property': 'Trigger:Measurement Complete Dest',
        'name': 'MEASUREMENT_COMPLETDEST',
        'shortDescription': '''
Specifies the destination of the measurement complete (MC) signal.

To determine which values are supported by each device, refer to the
LabVIEW Trigger Routing section in the *NI Digital Multimeters Help*.
''',
        'type': 'ViInt32',
    },
    1250321: {
        'access': 'read-write',
        'enum': None,
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
        'lv_property': 'Configuration:Advanced:Aperture Time',
        'name': 'APERTURE_TIME',
        'shortDescription': '''
Specifies the measurement aperture time for the current configuration.
Aperture time is specified in units set by the Aperture Time Units
property. To override the default aperture, set this property to the
desired aperture time after calling niDMM Config Measurement . To return
to the default, set this property to Aperture Time Auto (-1).
''',
        'type': 'ViReal64',
    },
    1250322: {
        'access': 'read-write',
        'enum': 'ApertureTimeUnits',
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
        'lv_property': 'Configuration:Advanced:Aperture Time Units',
        'name': 'APERTURE_TIME_UNITS',
        'shortDescription': '''
Specifies the units of aperture time for the current configuration.
''',
        'type': 'ViInt32',
    },
    1250331: {
        'access': 'read only',
        'enum': None,
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
        'lv_property': 'Configuration:Auto Range Value',
        'name': 'AUTO_RANGE_VALUE',
        'shortDescription': '''
Specifies the value of the range. If auto ranging is enabled, shows the
actual value of the active range. The value of this property is set
during a read operation.
''',
        'type': 'ViReal64',
    },
    1250332: {
        'access': 'read-write',
        'enum': 'AutoZero',
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
        'lv_property': 'Configuration:Measurement Options:Auto Zero',
        'name': 'AUTO_ZERO',
        'shortDescription': '''
Specifies the AutoZero mode. This property is not supported for the NI
4050.
''',
        'type': 'ViInt32',
    },
    1250333: {
        'access': 'read-write',
        'enum': 'PowerlineFrequency',
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
        'name': 'POWERLINE_FREQUENCY',
        'shortDescription': '''
Specifies the powerline frequency. The NI 4060 and NI 4050 use this
value to select an aperture time to reject powerline noise by selecting
the appropriate internal sample clock and filter. The NI 4065, NI
4070/4071/4072, and NI 4080/4081/4082 use this value to select timebases
for setting the Aperture Time property in powerline cycles.
''',
        'type': 'ViReal64',
    },
    1250334: {
        'access': 'read-write',
        'enum': 'TriggerSlope',
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
        'lv_property': 'Trigger:Trigger Slope',
        'name': 'TRIGGER_SLOPE',
        'shortDescription': '''
Specifies the edge of the signal from the specified trigger source on
which the DMM is triggered.
''',
        'type': 'ViInt32',
    },
}
