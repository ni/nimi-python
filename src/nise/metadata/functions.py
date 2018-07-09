
# -*- coding: utf-8 -*-
# This file is code generated, do not make changes here
#  If the generated information is not correct for python
#  changes can be made in functions_addon.py and they will be
#  applied at build time


functions = {
    'ClearError': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The Session handle that you obtain from niSE_OpenSession. The handle
identifies a particular session to the virtual switch device.
''',
},
            },
        ],
'documentation': {
'description': '''
This function clears the error information stored on a session. Note
that niSE_GetError actually clears the error information after it is
retrieved. niSE_ClearError is thus only necessary when a call to
niSE_GetError is not being performed.
''',
},
    },
    'CloseSession': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The Session handle that you obtain from niSE_OpenSession. The handle
identifies a particular session to the virtual switch device.
''',
},
            },
        ],
'documentation': {
'description': '''
Reduces the reference count of open sessions by one. If the reference
count goes to 0, the function deallocates any memory resources the
driver uses and closes any open IVI switch sessions. After calling the
niSE_CloseSession function, you should not use the NI Switch Executive
virtual device again until you call niSE_OpenSession.
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
The Session handle that you obtain from niSE_OpenSession. The handle
identifies a particular session to the virtual switch device.
''',
},
            },
            {
                'direction': 'in',
                'name': 'connectSpec',
                'type': 'ViConstString',
'documentation': {
'description': '''
String describing the connections to be made. The route specification
strings are best summarized as a series of routes delimited by
ampersands. The specified routes may be route names, route group names,
or fully specified route paths delimited by square brackets. Some
examples of route specification strings are: MyRoute MyRouteGroup
MyRoute & MyRouteGroup [A->Switch1/r0->B] MyRoute & MyRouteGroup &
[A->Switch1/r0->B] Refer to Route Specification Strings in the NI Switch
Executive Help for more information.
''',
},
            },
            {
                'direction': 'in',
                'name': 'multiconnectMode',
                'type': 'ViInt32',
'documentation': {
'description': '''
This value sets the connection mode for the function. The mode might be
one of the following: NISE_VAL_USE_DEFAULT_MODE (-1) - uses the mode
selected as the default for the route in the NI Switch Executive virtual
device configuration. If a mode has not been selected for the route in
the NI Switch Executive virtual device, this parameter defaults to
NISE_VAL_MULTICONNECT_ROUTES. NISE_VAL_NO_MULTICONNECT (0) -
routes specified in the connection specification must be disconnected
before they can be reconnected. Calling Connect on a route that was
connected using No Multiconnect mode results in an error condition.
NISE_VAL_MULTICONNECT_ROUTES (1)- routes specified in the connection
specification can be connected multiple times. The first call to Connect
performs the physical hardware connection. Successive calls to Connect
increase a connection reference count. Similarly, calls to Disconnect
decrease the reference count. Once it reaches 0, the hardware is
physically disconnected. Multiconnecting routes applies to entire routes
and not to route segments.
''',
},
            },
            {
                'direction': 'in',
                'name': 'waitForDebounce',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Waits (if true) for switches to debounce between its connect and
disconnect operations. If false, it immediately begins the second
operation after completing the first. The order of connect and
disconnect operation is set by the Operation Order input.
''',
},
            },
        ],
'documentation': {
'description': '''
Connects the routes specified by the connection specification. When
connecting, it may allow for multiconnection based on the
multiconnection mode. In the event of an error, the call to
niSE_Connect will attempt to undo any connections made so that the
system will be left in the same state that it was in before the call was
made. Some errors can be caught before manipulating hardware, although
it is feasible that a hardware call could fail causing some connections
to be momentarily closed and then reopened. If the wait for debounce
parameter is set, the function will not return until the switch system
has debounced.
''',
},
    },
    'ConnectAndDisconnect': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The Session handle that you obtain from niSE_OpenSession. The handle
identifies a particular session to the virtual switch device.
''',
},
            },
            {
                'direction': 'in',
                'name': 'connectSpec',
                'type': 'ViConstString',
'documentation': {
'description': '''
String describing the connections to be made. The route specification
strings are best summarized as a series of routes delimited by
ampersands. The specified routes may be route names, route group names,
or fully specified route paths delimited by square brackets. Some
examples of route specification strings are: MyRoute MyRouteGroup
MyRoute & MyRouteGroup [A->Switch1/r0->B] MyRoute & MyRouteGroup &
[A->Switch1/r0->B] Refer to Route Specification Strings in the NI Switch
Executive Help for more information.
''',
},
            },
            {
                'direction': 'in',
                'name': 'disconnectSpec',
                'type': 'ViConstString',
'documentation': {
'description': '''
String describing the disconnections to be made. The route specification
strings are best summarized as a series of routes delimited by
ampersands. The specified routes may be route names, route group names,
or fully specified route paths delimited by square brackets. Some
examples of route specification strings are: MyRoute MyRouteGroup
MyRoute & MyRouteGroup [A->Switch1/r0->B] MyRoute & MyRouteGroup &
[A->Switch1/r0->B] Refer to Route Specification Strings in the NI Switch
Executive Help for more information.
''',
},
            },
            {
                'direction': 'in',
                'name': 'multiconnectMode',
                'type': 'ViInt32',
'documentation': {
'description': '''
This value sets the connection mode for the function. The mode might be
one of the following: NISE_VAL_USE_DEFAULT_MODE (-1) - uses the mode
selected as the default for the route in the NI Switch Executive virtual
device configuration. If a mode has not been selected for the route in
the NI Switch Executive virtual device, this parameter defaults to
NISE_VAL_MULTICONNECT_ROUTES. NISE_VAL_NO_MULTICONNECT (0) -
routes specified in the connection specification must be disconnected
before they can be reconnected. Calling Connect on a route that was
connected using No Multiconnect mode results in an error condition.
NISE_VAL_MULTICONNECT_ROUTES (1) - routes specified in the connection
specification can be connected multiple times. The first call to Connect
performs the physical hardware connection. Successive calls to Connect
increase a connection reference count. Similarly, calls to Disconnect
decrease the reference count. Once it reaches 0, the hardware is
physically disconnected. This behavior is slightly different with SPDT
relays. For more information, refer to the Exclusions and SPDT Relays
topic in the NI Switch Executive Help. Multiconnecting routes applies to
entire routes and not to route segments.
''',
},
            },
            {
                'direction': 'in',
                'name': 'operationOrder',
                'type': 'ViInt32',
'documentation': {
'description': '''
Sets the order of the operation for the function. Defined values are
Break Before Make and Break After Make. NISE_VAL_BREAK_BEFORE_MAKE
(1) - The function disconnects the routes specified in the disconnect
specification before connecting the routes specified in the connect
specification. This is the typical mode of operation.
NISE_VAL_BREAK_AFTER_MAKE (2) - The function connects the routes
specified in the connection specification before connecting the routes
specified in the disconnection specification. This mode of operation is
normally used when you are switching current and want to ensure that a
load is always connected to your source. The order of operation is to
connect first or disconnect first.
''',
},
            },
            {
                'direction': 'in',
                'name': 'waitForDebounce',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Waits (if true) for switches to debounce between its connect and
disconnect operations. If false, it immediately begins the second
operation after completing the first. The order of connect and
disconnect operation is set by the Operation Order input.
''',
},
            },
        ],
'documentation': {
'description': '''
Connects routes and disconnects routes in a similar fashion to
niSE_Connect and niSE_Disconnect except that the operations happen in
the context of a single function call. This function is useful for
switching from one state to another state. niSE_ConnectAndDisconnect
manipulates the hardware connections and disconnections only when the
routes are different between the connection and disconnection
specifications. If any routes are common between the connection and
disconnection specifications, NI Switch Executive determines whether or
not the relays need to be switched. This functionality has the distinct
advantage of increased throughput for shared connections, because
hardware does not have to be involved and potentially increases relay
lifetime by decreasing the number of times that the relay has to be
switched. In the event of an error, the call to
niSE_ConnectAndDisconnect attempts to undo any connections made, but
does not attempt to reconnect disconnections. Some errors can be caught
before manipulating hardware, although it is feasible that a hardware
call could fail causing some connections to be momentarily closed and
then reopened.
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
The Session handle that you obtain from niSE_OpenSession. The handle
identifies a particular session to the virtual switch device.
''',
},
            },
            {
                'direction': 'in',
                'name': 'disconnectSpec',
                'type': 'ViConstString',
'documentation': {
'description': '''
String describing the disconnections to be made. The route specification
strings are best summarized as a series of routes delimited by
ampersands. The specified routes may be route names, route group names,
or fully specified route paths delimited by square brackets. Some
examples of route specification strings are: MyRoute MyRouteGroup
MyRoute & MyRouteGroup [A->Switch1/r0->B] MyRoute & MyRouteGroup &
[A->Switch1/r0->B] Refer to Route Specification Strings in the NI Switch
Executive Help for more information.
''',
},
            },
        ],
'documentation': {
'description': '''
Disconnects the routes specified in the Disconnection Specification. If
any of the specified routes were originally connected in a
multiconnected mode, the call to niSE_Disconnect reduces the reference
count on the route by 1. If the reference count reaches 0, it is
disconnected. If a specified route does not exist, it is an error
condition. In the event of an error, the call to niSE_Disconnect
continues to try to disconnect everything specified by the route
specification string but reports the error on completion.
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
The Session handle that you obtain from niSE_OpenSession. The handle
identifies a particular session to the virtual switch device.
''',
},
            },
        ],
'documentation': {
'description': '''
Disconnects all connections on every IVI switch device managed by the
NISE session reference passed to this function. niSE_DisconnectAll
ignores all multiconnect modes. Calling niSE_DisconnectAll resets all
of the switch states for the system.
''',
},
    },
    'ExpandRouteSpec': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The Session handle that you obtain from niSE_OpenSession. The handle
identifies a particular session to the virtual switch device.
''',
},
            },
            {
                'direction': 'in',
                'name': 'routeSpec',
                'type': 'ViConstString',
'documentation': {
'description': '''
String describing the routes and route groups to expand. The route
specification strings are best summarized as a series of routes
delimited by ampersands. The specified routes may be route names, route
group names, or fully specified route paths delimited by square
brackets. Some examples of route specification strings are: MyRoute
MyRouteGroup MyRoute & MyRouteGroup [A->Switch1/r0->B] MyRoute &
MyRouteGroup & [A->Switch1/r0->B] Refer to Route Specification Strings
in the NI Switch Executive Help for more information.
''',
},
            },
            {
                'direction': 'in',
                'name': 'expandAction',
                'type': 'ViInt32',
'documentation': {
'description': '''
This value sets the expand action for the function. The action might be
one of the following: NISE_VAL_EXPAND_TO_ROUTES (0) - expands the
route spec to routes. Converts route groups to their constituent routes.
NISE_VAL_EXPAND_TO_PATHS (1) - expands the route spec to paths.
Converts routes and route groups to their constituent square bracket
route spec strings. Example: [Dev1/c0->Dev1/r0->Dev1/c1]
''',
},
            },
            {
                'direction': 'out',
                'name': 'expandedRouteSpec',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The expanded route spec. Route specification strings can be directly
passed to niSE_Connect, niSE_Disconnect, or niSE_ConnectAndDisconnect
Refer to Route Specification Strings in the NI Switch Executive Help for
more information. You may pass NULL for this parameter if you are not
interested in the return value. To obtain the route specification
string, you should pass a buffer to this parameter. The size of the
buffer required may be obtained by calling the function with NULL for
this parameter and a valid ViInt32 to routeSpecSize. The routeSpecSize
will contain the size needed to hold the entire route specification
(including the NULL termination character). Common operation is to call
the function twice. The first time you call the function you can
determine the size needed to hold the route specification string.
Allocate a buffer of the appropriate size and then re-call the function
to obtain the entire buffer.
''',
},
            },
            {
                'direction': 'out',
                'name': 'expandedRouteSpecSize',
                'type': 'ViInt32',
'documentation': {
'description': '''
The routeSpecSize is an ViInt32 that is passed by reference into the
function. As an input, it is the size of the route spec string buffer
being passed. If the route spec string is larger than the string buffer
being passed, only the portion of the route spec string that can fit in
the string buffer is copied into it. On return from the function,
routeSpecSize holds the size required to hold the entire route spec
string. Note that this size may be larger than the buffer size as the
function always returns the size needed to hold the entire buffer. You
may pass NULL for this parameter if you are not interested in the return
value for routeSpecSize and routeSpec.
''',
},
            },
        ],
'documentation': {
'description': '''
Expands a route spec string to yield more information about the routes
and route groups within the spec. The route specification string
returned from niSE_ExpandRouteSpec can be passed to other Switch
Executive API functions (such as niSE_Connect, niSE_Disconnect, and
niSE_ConnectAndDisconnect) that use route specification strings.
''',
},
    },
    'FindRoute': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The Session handle that you obtain from niSE_OpenSession. The handle
identifies a particular session to the virtual switch device.
''',
},
            },
            {
                'direction': 'in',
                'name': 'channel1',
                'type': 'ViConstString',
'documentation': {
'description': '''
Channel name of one of the endpoints of the route to find. The channel
name must either be a channel alias name or a name in the
device/ivichannel syntax. Examples: MyChannel Switch1/R0
''',
},
            },
            {
                'direction': 'in',
                'name': 'channel2',
                'type': 'ViConstString',
'documentation': {
'description': '''
Channel name of one of the endpoints of the route to find. The channel
name must either be a channel alias name or a name in the
device/ivichannel syntax. Examples: MyChannel Switch1/R0
''',
},
            },
            {
                'direction': 'out',
                'name': 'routeSpec',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The fully specified route path complete with delimiting square
brackets if the route exists or is possible. An example of a fully
specified route string is: [A->Switch1/r0->B] Route specification
strings can be directly passed to niSE_Connect, niSE_Disconnect, or
niSE_ConnectAndDisconnect Refer to Route Specification Strings in the
NI Switch Executive Help for more information. You may pass NULL for
this parameter if you are not interested in the return value. To obtain
the route specification string, you should pass a buffer to this
parameter. The size of the buffer required may be obtained by calling
the function with NULL for this parameter and a valid ViInt32 to
routeSpecSize. The routeSpecSize will contain the size needed to hold
the entire route specification (including the NULL termination
character). Common operation is to call the function twice. The first
time you call the function you can determine the size needed to hold the
route specification string. Allocate a buffer of the appropriate size
and then re-call the function to obtain the entire buffer.
''',
},
            },
            {
                'direction': 'out',
                'name': 'routeSpecSize',
                'type': 'ViInt32',
'documentation': {
'description': '''
The routeSpecSize is an ViInt32 that is passed by reference into the
function. As an input, it is the size of the route string buffer being
passed. If the route string is larger than the string buffer being
passed, only the portion of the route string that can fit in the string
buffer is copied into it. On return from the function, routeSpecSize
holds the size required to hold the entire route string. Note that this
size may be larger than the buffer size as the function always returns
the size needed to hold the entire buffer. You may pass NULL for this
parameter if you are not interested in the return value for
routeSpecSize and routeSpec.
''',
},
            },
            {
                'direction': 'out',
                'name': 'pathCapability',
                'type': 'ViInt32',
'documentation': {
'description': '''
The return value which expresses the capability of finding a valid route
between Channel 1 and Channel 2. Refer to the table below for value
descriptions. You may pass NULL for this parameter if you are not
interested in the return value. Route capability might be one of the
following: Path Available (1) A path between channel 1 and channel 2 is
available. The route specification parameter returns a string describing
the available path. Path Exists (2) A path between channel 1 and channel
2 already exists. The route specification parameter returns a string
describing the existing path. Path Unsupported (3) There is no potential
path between channel 1 and channel 2 given the current configuration.
Resource In Use (4) There is a potential path between channel 1 and
channel 2, although a resource needed to complete the path is already in
use. Source Conflict (5) Channel 1 and channel 2 cannot be connected
because their connection would result in an exclusion violation. Channel
Not Available (6) One of the channels is not useable as an endpoint
channel. Make sure that it is not marked as a reserved for routing.
Channels Hardwired (7) The two channels reside on the same hardwire. An
implicit path already exists.
''',
},
            },
        ],
'documentation': {
'description': '''
Finds an existing or potential route between channel 1 and channel 2.
The returned route specification contains the route specification and
the route capability determines whether or not the route existed, is
possible, or is not possible for various reasons. The route
specification string returned from niSE_FindRoute can be passed to
other Switch Executive API functions (such as niSE_Connect,
niSE_Disconnect, and niSE_ConnectAndDisconnect) that use route
specification strings.
''',
},
    },
    'GetAllConnections': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The Session handle that you obtain from niSE_OpenSession. The handle
identifies a particular session to the virtual switch device.
''',
},
            },
            {
                'direction': 'out',
                'name': 'routeSpec',
                'type': 'ViChar[]',
'documentation': {
'description': '''
The route spec of all currently connected routes and route groups. Route
specification strings can be directly passed to niSE_Connect,
niSE_Disconnect, niSE_ConnectAndDisconnect, or niSE_ExpandRouteSpec
Refer to Route Specification Strings in the NI Switch Executive Help for
more information. You may pass NULL for this parameter if you are not
interested in the return value. To obtain the route specification
string, you should pass a buffer to this parameter. The size of the
buffer required may be obtained by calling the function with NULL for
this parameter and a valid ViInt32 to routeSpecSize. The routeSpecSize
will contain the size needed to hold the entire route specification
(including the NULL termination character). Common operation is to call
the function twice. The first time you call the function you can
determine the size needed to hold the route specification string.
Allocate a buffer of the appropriate size and then re-call the function
to obtain the entire buffer.
''',
},
            },
            {
                'direction': 'out',
                'name': 'routeSpecSize',
                'type': 'ViInt32',
'documentation': {
'description': '''
The routeSpecSize is an ViInt32 that is passed by reference into the
function. As an input, it is the size of the route spec string buffer
being passed. If the route spec string is larger than the string buffer
being passed, only the portion of the route spec string that can fit in
the string buffer is copied into it. On return from the function,
routeSpecSize holds the size required to hold the entire route spec
string. Note that this size may be larger than the buffer size as the
function always returns the size needed to hold the entire buffer. You
may pass NULL for this parameter if you are not interested in the return
value for routeSpecSize and routeSpec.
''',
},
            },
        ],
'documentation': {
'description': '''
Returns the top-level connected routes and route groups. The route
specification string returned from niSE_GetAllConnections can be passed
to other Switch Executive API functions (such as niSE_Connect,
niSE_Disconnect, niSE_ConnectAndDisconnect, and niSE_ExpandRouteSpec)
that use route specification strings.
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
The Session handle that you obtain from niSE_OpenSession. The handle
identifies a particular session to the virtual switch device.
''',
},
            },
            {
                'direction': 'out',
                'name': 'errorNumber',
                'type': 'ViInt32',
'documentation': {
'description': '''
By reference parameter which returns the error number of the first error
which occurred on the session since the error was last cleared. You may
pass NULL for this parameter if you are not interested in the return
value.
''',
},
            },
            {
                'direction': 'out',
                'name': 'errorDescription',
                'type': 'ViChar[]',
'documentation': {
'description': '''
By reference buffer which is to be filled with the error description
string. You may pass NULL for this parameter if you are not interested
in the return value. To obtain the error description string, you should
pass a buffer to this parameter. The size of the buffer required may be
obtained by calling the function with NULL for this parameter and a
valid ViInt32 to the error description size parameter. The error
description size will contain the size needed to hold the entire route
specification (including the NULL termination character). Common
operation is to call the function twice. The first time you call the
function you can determine the size needed to hold the route
specification string. Allocate a buffer of the appropriate size and then
re-call the function to obtain the entire buffer.
''',
},
            },
            {
                'direction': 'out',
                'name': 'errorDescriptionSize',
                'type': 'ViInt32',
'documentation': {
'description': '''
As input, it is the size of the error description string buffer. As
output, it is the Size of the entire error description string (may be
larger than the buffer size as the function always returns the size
needed to hold the entire buffer). This parameter is a ViInt32 that is
passed by reference into the function. As an input, it is the size of
the error description buffer being passed. If the error description
string is larger than the string buffer being passed, only the portion
of the route string that can fit in the string buffer will be copied
into it. On return from the function, it holds the size required to hold
the entire error description string, including the NULL termination
character. Note that this size may be larger than the buffer size as the
function always returns the size needed to hold the entire buffer. You
may pass NULL for this parameter if you are not interested in the return
value for it.
''',
},
            },
        ],
'documentation': {
'description': '''
Get error information of the first error that occurred. If a valid
pointer is passed to errorDescription or errorNumber, GetError will
clear the error on completion. errorDescriptionSize is an in/out
parameter that describes the size of the errorDescription buffer. On the
way in, it tells the function the size of string. On the way out, it
describes the number of bytes (including the trailing null string)
needed to hold the entire error description buffer. If NULL is passed
for errorDescription and the errorNumber, the function will not clear
the error. Users wanting to dynamically size the errorDescription string
can thus call the function twice. On the first call they can pass NULL
for the errorDescription and use the returned errorDescriptionSize to
allocate enough space for the entire errorDescription buffer. Note that
if a buffer is passed that is not large enough to hold the entire
description string, the portion of of the string that will fit in the
passed buffer will be returned and the error will still be cleared. All
of the parameters are NULL tolerant. Note that passing NULL for both
errorNumber and errorDescription can change the function's behavior.
''',
},
    },
    'GetIviDeviceSession': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The Session handle that you obtain from niSE_OpenSession. The handle
identifies a particular session to the virtual switch device.
''',
},
            },
            {
                'direction': 'in',
                'name': 'iviLogicalName',
                'type': 'ViConstString',
'documentation': {
'description': '''
The IVI logical name of the IVI device for which to retrieve an IVI
session.
''',
},
            },
            {
                'direction': 'out',
                'name': 'iviSessionHandle',
                'type': 'ViSession',
'documentation': {
'description': 'The IVI instrument handle of the specified IVI device.',
},
            },
        ],
'documentation': {
'description': '''
Retrieves an IVI instrument session for an IVI switching device that is
being managed by the NI Switch Executive. The retrieved session handle
can be used to access instrument specific functionality through the
instrument driver. The retrieved handle should not be closed. Note: Use
caution when using the session handle. Calling functions on an
instrument driver can invalidate the NI Switch Executive configuration
and cache. You should not use the retrieved session handle to make or
break connections or modify the configuration channels as this can cause
undefined, and potentially unwanted, behavior.
''',
},
    },
    'IsConnected': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': '''
The Session handle that you obtain from niSE_OpenSession. The handle
identifies a particular session to the virtual switch device.
''',
},
            },
            {
                'direction': 'in',
                'name': 'routeSpec',
                'type': 'ViConstString',
'documentation': {
'description': '''
String describing the connections to check. The route specification
strings are best summarized as a series of routes delimited by
ampersands. The specified routes may be route names, route group names,
or fully specified route paths delimited by square brackets. Some
examples of route specification strings are: MyRoute MyRouteGroup
MyRoute & MyRouteGroup [A->Switch1/r0->B] MyRoute & MyRouteGroup &
[A->Switch1/r0->B] Refer to Route Specification Strings in the NI Switch
Executive Help for more information.
''',
},
            },
            {
                'direction': 'out',
                'name': 'isConnected',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Returns TRUE if the routes and routes groups are connected or FALSE if
they are not.
''',
},
            },
        ],
'documentation': {
'description': '''
Checks whether the specified routes and routes groups are connected. It
returns true if connected.
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
The Session handle that you obtain from niSE_OpenSession. The handle
identifies a particular session to the virtual switch device.
''',
},
            },
            {
                'direction': 'out',
                'name': 'isDebounced',
                'type': 'ViBoolean',
'documentation': {
'description': '''
Returns TRUE if the system is fully debounced or FALSE if it is still
settling.
''',
},
            },
        ],
'documentation': {
'description': '''
Checks to see if the switching system is debounced or not. This function
does not wait for debouncing to occur. It returns true if the system is
fully debounced. This function is similar to the IviSwtch specific
function.
''',
},
    },
    'OpenSession': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'virtualDeviceName',
                'type': 'ViConstString',
'documentation': {
'description': 'The name of the NI Switch Executive virtual device.',
},
            },
            {
                'direction': 'in',
                'name': 'optionString',
                'type': 'ViConstString',
'documentation': {
'description': '''
The option string can be used to pass information to each of the IVI
devices on startup. It can be used to set things such as simulation,
range checking, etc. Consult your driver documentation for more
information about valid entries for the option string.
''',
},
            },
            {
                'direction': 'out',
                'name': 'vi',
                'type': 'ViSession',
'documentation': {
'description': 'The session referencing this NI Switch Executive virtual device session.',
},
            },
        ],
'documentation': {
'description': '''
Opens a session to a specified NI Switch Executive virtual device. Opens
communications with all of the IVI switches associated with the
specified NI Switch Executive virtual device. Returns a session handle
that you use to identify the virtual device in all subsequent NI Switch
Executive function calls. NI Switch Executive uses a reference counting
scheme to manage open session handles to an NI Switch Executive virtual
device. Each call to niSE_OpenSession must be matched with a subsequent
call to niSE_CloseSession. Successive calls to niSE_OpenSession with
the same virtual device name always returns the same session handle. NI
Switch Executive disconnects its communication with the IVI switches
after all session handles are closed to a given virtual device. The
session handles may be used safely in multiple threads of an
application. Sessions may only be opened to a given NI Switch Executive
virtual device from a single process at a time.
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
The Session handle that you obtain from niSE_OpenSession. The handle
identifies a particular session to the virtual switch device.
''',
},
            },
            {
                'direction': 'in',
                'name': 'maximumTimeMs',
                'type': 'ViInt32',
'documentation': {
'description': '''
The amount of time to wait (in milliseconds) for the debounce to
complete. A value of 0 checks for debouncing once and returns an error
if the system is not debounced at that time. A value of -1 means to
block for an infinite period of time until the system is debounced.
''',
},
            },
        ],
'documentation': {
'description': '''
Waits for all of the switches in the NI Switch Executive virtual device
to debounce. This function does not return until either the switching
system is completely debounced and settled or the maximum time has
elapsed and the system is not yet debounced. In the event that the
maximum time elapses, the function returns an error indicating that a
timeout has occurred. To ensure that all of the switches have settled,
NI recommends calling niSE_WaitForDebounce after a series of connection
or disconnection operations and before taking any measurements of the
signals connected to the switching system.
''',
},
    },
}
