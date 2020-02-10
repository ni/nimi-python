# -*- coding: utf-8 -*-
# This file is generated from NI Switch Executive API metadata version 21.0.0d0
functions = {
    'CloseSession': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nReduces the reference count of open sessions by one. If the reference\ncount goes to 0, the function deallocates any memory resources the\ndriver uses and closes any open IVI switch sessions. After calling the\nniSE_CloseSession function, you should not use the NI Switch Executive\nvirtual device again until you call niSE_OpenSession.\n'
        },
        'method_name_for_documentation': 'close',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe Session handle that you obtain from niSE_OpenSession. The handle\nidentifies a particular session to the virtual switch device.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'Connect': {
        'documentation': {
            'description': '\nConnects the routes specified by the connection specification. When\nconnecting, it may allow for multiconnection based on the\nmulticonnection mode. In the event of an error, the call to\nniSE_Connect will attempt to undo any connections made so that the\nsystem will be left in the same state that it was in before the call was\nmade. Some errors can be caught before manipulating hardware, although\nit is feasible that a hardware call could fail causing some connections\nto be momentarily closed and then reopened. If the wait for debounce\nparameter is set, the function will not return until the switch system\nhas debounced.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe Session handle that you obtain from niSE_OpenSession. The handle\nidentifies a particular session to the virtual switch device.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nString describing the connections to be made. The route specification\nstrings are best summarized as a series of routes delimited by\nampersands. The specified routes may be route names, route group names,\nor fully specified route paths delimited by square brackets. Some\nexamples of route specification strings are: MyRoute MyRouteGroup\nMyRoute & MyRouteGroup [A->Switch1/r0->B] MyRoute & MyRouteGroup &\n[A->Switch1/r0->B] Refer to Route Specification Strings in the NI Switch\nExecutive Help for more information.\n'
                },
                'name': 'connectSpec',
                'type': 'ViConstString'
            },
            {
                'default_value': 'MulticonnectMode.DEFAULT',
                'direction': 'in',
                'documentation': {
                    'description': '\nThis value sets the connection mode for the function. The mode might be\none of the following: NISE_VAL_USE_DEFAULT_MODE (-1) - uses the mode\nselected as the default for the route in the NI Switch Executive virtual\ndevice configuration. If a mode has not been selected for the route in\nthe NI Switch Executive virtual device, this parameter defaults to\nNISE_VAL_MULTICONNECT_ROUTES. NISE_VAL_NO_MULTICONNECT (0) -\nroutes specified in the connection specification must be disconnected\nbefore they can be reconnected. Calling Connect on a route that was\nconnected using No Multiconnect mode results in an error condition.\nNISE_VAL_MULTICONNECT_ROUTES (1)- routes specified in the connection\nspecification can be connected multiple times. The first call to Connect\nperforms the physical hardware connection. Successive calls to Connect\nincrease a connection reference count. Similarly, calls to Disconnect\ndecrease the reference count. Once it reaches 0, the hardware is\nphysically disconnected. Multiconnecting routes applies to entire routes\nand not to route segments.\n'
                },
                'enum': 'MulticonnectMode',
                'name': 'multiconnectMode',
                'type': 'ViInt32'
            },
            {
                'default_value': True,
                'direction': 'in',
                'documentation': {
                    'description': '\nWaits (if true) for switches to debounce between its connect and\ndisconnect operations. If false, it immediately begins the second\noperation after completing the first. The order of connect and\ndisconnect operation is set by the Operation Order input.\n'
                },
                'name': 'waitForDebounce',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConnectAndDisconnect': {
        'documentation': {
            'description': '\nConnects routes and disconnects routes in a similar fashion to\nniSE_Connect and niSE_Disconnect except that the operations happen in\nthe context of a single function call. This function is useful for\nswitching from one state to another state. niSE_ConnectAndDisconnect\nmanipulates the hardware connections and disconnections only when the\nroutes are different between the connection and disconnection\nspecifications. If any routes are common between the connection and\ndisconnection specifications, NI Switch Executive determines whether or\nnot the relays need to be switched. This functionality has the distinct\nadvantage of increased throughput for shared connections, because\nhardware does not have to be involved and potentially increases relay\nlifetime by decreasing the number of times that the relay has to be\nswitched. In the event of an error, the call to\nniSE_ConnectAndDisconnect attempts to undo any connections made, but\ndoes not attempt to reconnect disconnections. Some errors can be caught\nbefore manipulating hardware, although it is feasible that a hardware\ncall could fail causing some connections to be momentarily closed and\nthen reopened.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe Session handle that you obtain from niSE_OpenSession. The handle\nidentifies a particular session to the virtual switch device.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nString describing the connections to be made. The route specification\nstrings are best summarized as a series of routes delimited by\nampersands. The specified routes may be route names, route group names,\nor fully specified route paths delimited by square brackets. Some\nexamples of route specification strings are: MyRoute MyRouteGroup\nMyRoute & MyRouteGroup [A->Switch1/r0->B] MyRoute & MyRouteGroup &\n[A->Switch1/r0->B] Refer to Route Specification Strings in the NI Switch\nExecutive Help for more information.\n'
                },
                'name': 'connectSpec',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nString describing the disconnections to be made. The route specification\nstrings are best summarized as a series of routes delimited by\nampersands. The specified routes may be route names, route group names,\nor fully specified route paths delimited by square brackets. Some\nexamples of route specification strings are: MyRoute MyRouteGroup\nMyRoute & MyRouteGroup [A->Switch1/r0->B] MyRoute & MyRouteGroup &\n[A->Switch1/r0->B] Refer to Route Specification Strings in the NI Switch\nExecutive Help for more information.\n'
                },
                'name': 'disconnectSpec',
                'type': 'ViConstString'
            },
            {
                'default_value': 'MulticonnectMode.DEFAULT',
                'direction': 'in',
                'documentation': {
                    'description': '\nThis value sets the connection mode for the function. The mode might be\none of the following: NISE_VAL_USE_DEFAULT_MODE (-1) - uses the mode\nselected as the default for the route in the NI Switch Executive virtual\ndevice configuration. If a mode has not been selected for the route in\nthe NI Switch Executive virtual device, this parameter defaults to\nNISE_VAL_MULTICONNECT_ROUTES. NISE_VAL_NO_MULTICONNECT (0) -\nroutes specified in the connection specification must be disconnected\nbefore they can be reconnected. Calling Connect on a route that was\nconnected using No Multiconnect mode results in an error condition.\nNISE_VAL_MULTICONNECT_ROUTES (1) - routes specified in the connection\nspecification can be connected multiple times. The first call to Connect\nperforms the physical hardware connection. Successive calls to Connect\nincrease a connection reference count. Similarly, calls to Disconnect\ndecrease the reference count. Once it reaches 0, the hardware is\nphysically disconnected. This behavior is slightly different with SPDT\nrelays. For more information, refer to the Exclusions and SPDT Relays\ntopic in the NI Switch Executive Help. Multiconnecting routes applies to\nentire routes and not to route segments.\n'
                },
                'enum': 'MulticonnectMode',
                'name': 'multiconnectMode',
                'type': 'ViInt32'
            },
            {
                'default_value': 'OperationOrder.AFTER',
                'direction': 'in',
                'documentation': {
                    'description': '\nSets the order of the operation for the function. Defined values are\nBreak Before Make and Break After Make. NISE_VAL_BREAK_BEFORE_MAKE\n(1) - The function disconnects the routes specified in the disconnect\nspecification before connecting the routes specified in the connect\nspecification. This is the typical mode of operation.\nNISE_VAL_BREAK_AFTER_MAKE (2) - The function connects the routes\nspecified in the connection specification before connecting the routes\nspecified in the disconnection specification. This mode of operation is\nnormally used when you are switching current and want to ensure that a\nload is always connected to your source. The order of operation is to\nconnect first or disconnect first.\n'
                },
                'enum': 'OperationOrder',
                'name': 'operationOrder',
                'type': 'ViInt32'
            },
            {
                'default_value': True,
                'direction': 'in',
                'documentation': {
                    'description': '\nWaits (if true) for switches to debounce between its connect and\ndisconnect operations. If false, it immediately begins the second\noperation after completing the first. The order of connect and\ndisconnect operation is set by the Operation Order input.\n'
                },
                'name': 'waitForDebounce',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'Disconnect': {
        'documentation': {
            'description': '\nDisconnects the routes specified in the Disconnection Specification. If\nany of the specified routes were originally connected in a\nmulticonnected mode, the call to niSE_Disconnect reduces the reference\ncount on the route by 1. If the reference count reaches 0, it is\ndisconnected. If a specified route does not exist, it is an error\ncondition. In the event of an error, the call to niSE_Disconnect\ncontinues to try to disconnect everything specified by the route\nspecification string but reports the error on completion.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe Session handle that you obtain from niSE_OpenSession. The handle\nidentifies a particular session to the virtual switch device.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nString describing the disconnections to be made. The route specification\nstrings are best summarized as a series of routes delimited by\nampersands. The specified routes may be route names, route group names,\nor fully specified route paths delimited by square brackets. Some\nexamples of route specification strings are: MyRoute MyRouteGroup\nMyRoute & MyRouteGroup [A->Switch1/r0->B] MyRoute & MyRouteGroup &\n[A->Switch1/r0->B] Refer to Route Specification Strings in the NI Switch\nExecutive Help for more information.\n'
                },
                'name': 'disconnectSpec',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisconnectAll': {
        'documentation': {
            'description': '\nDisconnects all connections on every IVI switch device managed by the\nNISE session reference passed to this function. niSE_DisconnectAll\nignores all multiconnect modes. Calling niSE_DisconnectAll resets all\nof the switch states for the system.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe Session handle that you obtain from niSE_OpenSession. The handle\nidentifies a particular session to the virtual switch device.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ExpandRouteSpec': {
        'documentation': {
            'description': '\nExpands a route spec string to yield more information about the routes\nand route groups within the spec. The route specification string\nreturned from niSE_ExpandRouteSpec can be passed to other Switch\nExecutive API functions (such as niSE_Connect, niSE_Disconnect, and\nniSE_ConnectAndDisconnect) that use route specification strings.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe Session handle that you obtain from niSE_OpenSession. The handle\nidentifies a particular session to the virtual switch device.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nString describing the routes and route groups to expand. The route\nspecification strings are best summarized as a series of routes\ndelimited by ampersands. The specified routes may be route names, route\ngroup names, or fully specified route paths delimited by square\nbrackets. Some examples of route specification strings are: MyRoute\nMyRouteGroup MyRoute & MyRouteGroup [A->Switch1/r0->B] MyRoute &\nMyRouteGroup & [A->Switch1/r0->B] Refer to Route Specification Strings\nin the NI Switch Executive Help for more information.\n'
                },
                'name': 'routeSpec',
                'type': 'ViConstString'
            },
            {
                'default_value': 'ExpandAction.ROUTES',
                'direction': 'in',
                'documentation': {
                    'description': '\nThis value sets the expand action for the function. The action might be\none of the following: NISE_VAL_EXPAND_TO_ROUTES (0) - expands the\nroute spec to routes. Converts route groups to their constituent routes.\nNISE_VAL_EXPAND_TO_PATHS (1) - expands the route spec to paths.\nConverts routes and route groups to their constituent square bracket\nroute spec strings. Example: [Dev1/c0->Dev1/r0->Dev1/c1]\n'
                },
                'enum': 'ExpandAction',
                'name': 'expandAction',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe expanded route spec. Route specification strings can be directly\npassed to niSE_Connect, niSE_Disconnect, or niSE_ConnectAndDisconnect\nRefer to Route Specification Strings in the NI Switch Executive Help for\nmore information. You may pass NULL for this parameter if you are not\ninterested in the return value. To obtain the route specification\nstring, you should pass a buffer to this parameter. The size of the\nbuffer required may be obtained by calling the function with NULL for\nthis parameter and a valid ViInt32 to routeSpecSize. The routeSpecSize\nwill contain the size needed to hold the entire route specification\n(including the NULL termination character). Common operation is to call\nthe function twice. The first time you call the function you can\ndetermine the size needed to hold the route specification string.\nAllocate a buffer of the appropriate size and then re-call the function\nto obtain the entire buffer.\n'
                },
                'name': 'expandedRouteSpec',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'expanded_route_spec_size[0]'
                },
                'type': 'ViChar[]'
            },
            {
                'default_value': [
                    1024
                ],
                'direction': 'in',
                'documentation': {
                    'description': '\nThe routeSpecSize is an ViInt32 that is passed by reference into the\nfunction. As an input, it is the size of the route spec string buffer\nbeing passed. If the route spec string is larger than the string buffer\nbeing passed, only the portion of the route spec string that can fit in\nthe string buffer is copied into it. On return from the function,\nrouteSpecSize holds the size required to hold the entire route spec\nstring. Note that this size may be larger than the buffer size as the\nfunction always returns the size needed to hold the entire buffer. You\nmay pass NULL for this parameter if you are not interested in the return\nvalue for routeSpecSize and routeSpec.\n'
                },
                'name': 'expandedRouteSpecSize',
                'size': {
                    'mechanism': 'fixed',
                    'value': 1
                },
                'type': 'ViInt32[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'FindRoute': {
        'documentation': {
            'description': '\nFinds an existing or potential route between channel 1 and channel 2.\nThe returned route specification contains the route specification and\nthe route capability determines whether or not the route existed, is\npossible, or is not possible for various reasons. The route\nspecification string returned from niSE_FindRoute can be passed to\nother Switch Executive API functions (such as niSE_Connect,\nniSE_Disconnect, and niSE_ConnectAndDisconnect) that use route\nspecification strings.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe Session handle that you obtain from niSE_OpenSession. The handle\nidentifies a particular session to the virtual switch device.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nChannel name of one of the endpoints of the route to find. The channel\nname must either be a channel alias name or a name in the\ndevice/ivichannel syntax. Examples: MyChannel Switch1/R0\n'
                },
                'name': 'channel1',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nChannel name of one of the endpoints of the route to find. The channel\nname must either be a channel alias name or a name in the\ndevice/ivichannel syntax. Examples: MyChannel Switch1/R0\n'
                },
                'name': 'channel2',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe fully specified route path complete with delimiting square\nbrackets if the route exists or is possible. An example of a fully\nspecified route string is: [A->Switch1/r0->B] Route specification\nstrings can be directly passed to niSE_Connect, niSE_Disconnect, or\nniSE_ConnectAndDisconnect Refer to Route Specification Strings in the\nNI Switch Executive Help for more information. You may pass NULL for\nthis parameter if you are not interested in the return value. To obtain\nthe route specification string, you should pass a buffer to this\nparameter. The size of the buffer required may be obtained by calling\nthe function with NULL for this parameter and a valid ViInt32 to\nrouteSpecSize. The routeSpecSize will contain the size needed to hold\nthe entire route specification (including the NULL termination\ncharacter). Common operation is to call the function twice. The first\ntime you call the function you can determine the size needed to hold the\nroute specification string. Allocate a buffer of the appropriate size\nand then re-call the function to obtain the entire buffer.\n'
                },
                'name': 'routeSpec',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'route_spec_size[0]'
                },
                'type': 'ViChar[]'
            },
            {
                'default_value': [
                    1024
                ],
                'direction': 'in',
                'documentation': {
                    'description': '\nThe routeSpecSize is an ViInt32 that is passed by reference into the\nfunction. As an input, it is the size of the route string buffer being\npassed. If the route string is larger than the string buffer being\npassed, only the portion of the route string that can fit in the string\nbuffer is copied into it. On return from the function, routeSpecSize\nholds the size required to hold the entire route string. Note that this\nsize may be larger than the buffer size as the function always returns\nthe size needed to hold the entire buffer. You may pass NULL for this\nparameter if you are not interested in the return value for\nrouteSpecSize and routeSpec.\n'
                },
                'name': 'routeSpecSize',
                'size': {
                    'mechanism': 'fixed',
                    'value': 1
                },
                'type': 'ViInt32[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe return value which expresses the capability of finding a valid route\nbetween Channel 1 and Channel 2. Refer to the table below for value\ndescriptions. You may pass NULL for this parameter if you are not\ninterested in the return value. Route capability might be one of the\nfollowing: Path Available (1) A path between channel 1 and channel 2 is\navailable. The route specification parameter returns a string describing\nthe available path. Path Exists (2) A path between channel 1 and channel\n2 already exists. The route specification parameter returns a string\ndescribing the existing path. Path Unsupported (3) There is no potential\npath between channel 1 and channel 2 given the current configuration.\nResource In Use (4) There is a potential path between channel 1 and\nchannel 2, although a resource needed to complete the path is already in\nuse. Source Conflict (5) Channel 1 and channel 2 cannot be connected\nbecause their connection would result in an exclusion violation. Channel\nNot Available (6) One of the channels is not useable as an endpoint\nchannel. Make sure that it is not marked as a reserved for routing.\nChannels Hardwired (7) The two channels reside on the same hardwire. An\nimplicit path already exists.\n'
                },
                'enum': 'PathCapability',
                'name': 'pathCapability',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAllConnections': {
        'documentation': {
            'description': '\nReturns the top-level connected routes and route groups. The route\nspecification string returned from niSE_GetAllConnections can be passed\nto other Switch Executive API functions (such as niSE_Connect,\nniSE_Disconnect, niSE_ConnectAndDisconnect, and niSE_ExpandRouteSpec)\nthat use route specification strings.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe Session handle that you obtain from niSE_OpenSession. The handle\nidentifies a particular session to the virtual switch device.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe route spec of all currently connected routes and route groups. Route\nspecification strings can be directly passed to niSE_Connect,\nniSE_Disconnect, niSE_ConnectAndDisconnect, or niSE_ExpandRouteSpec\nRefer to Route Specification Strings in the NI Switch Executive Help for\nmore information. You may pass NULL for this parameter if you are not\ninterested in the return value. To obtain the route specification\nstring, you should pass a buffer to this parameter. The size of the\nbuffer required may be obtained by calling the function with NULL for\nthis parameter and a valid ViInt32 to routeSpecSize. The routeSpecSize\nwill contain the size needed to hold the entire route specification\n(including the NULL termination character). Common operation is to call\nthe function twice. The first time you call the function you can\ndetermine the size needed to hold the route specification string.\nAllocate a buffer of the appropriate size and then re-call the function\nto obtain the entire buffer.\n'
                },
                'name': 'routeSpec',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'route_spec_size[0]'
                },
                'type': 'ViChar[]'
            },
            {
                'default_value': [
                    1024
                ],
                'direction': 'in',
                'documentation': {
                    'description': '\nThe routeSpecSize is an ViInt32 that is passed by reference into the\nfunction. As an input, it is the size of the route spec string buffer\nbeing passed. If the route spec string is larger than the string buffer\nbeing passed, only the portion of the route spec string that can fit in\nthe string buffer is copied into it. On return from the function,\nrouteSpecSize holds the size required to hold the entire route spec\nstring. Note that this size may be larger than the buffer size as the\nfunction always returns the size needed to hold the entire buffer. You\nmay pass NULL for this parameter if you are not interested in the return\nvalue for routeSpecSize and routeSpec.\n'
                },
                'name': 'routeSpecSize',
                'size': {
                    'mechanism': 'fixed',
                    'value': 1
                },
                'type': 'ViInt32[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetError': {
        'codegen_method': 'private',
        'documentation': {
            'description': "\nGet error information of the first error that occurred. If a valid\npointer is passed to errorDescription or errorNumber, GetError will\nclear the error on completion. errorDescriptionSize is an in/out\nparameter that describes the size of the errorDescription buffer. On the\nway in, it tells the function the size of string. On the way out, it\ndescribes the number of bytes (including the trailing null string)\nneeded to hold the entire error description buffer. If NULL is passed\nfor errorDescription and the errorNumber, the function will not clear\nthe error. Users wanting to dynamically size the errorDescription string\ncan thus call the function twice. On the first call they can pass NULL\nfor the errorDescription and use the returned errorDescriptionSize to\nallocate enough space for the entire errorDescription buffer. Note that\nif a buffer is passed that is not large enough to hold the entire\ndescription string, the portion of of the string that will fit in the\npassed buffer will be returned and the error will still be cleared. All\nof the parameters are NULL tolerant. Note that passing NULL for both\nerrorNumber and errorDescription can change the function's behavior.\n"
        },
        'is_error_handling': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe Session handle that you obtain from niSE_OpenSession. The handle\nidentifies a particular session to the virtual switch device.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nBy reference parameter which returns the error number of the first error\nwhich occurred on the session since the error was last cleared. You may\npass NULL for this parameter if you are not interested in the return\nvalue.\n'
                },
                'name': 'errorNumber',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nBy reference buffer which is to be filled with the error description\nstring. You may pass NULL for this parameter if you are not interested\nin the return value. To obtain the error description string, you should\npass a buffer to this parameter. The size of the buffer required may be\nobtained by calling the function with NULL for this parameter and a\nvalid ViInt32 to the error description size parameter. The error\ndescription size will contain the size needed to hold the entire route\nspecification (including the NULL termination character). Common\noperation is to call the function twice. The first time you call the\nfunction you can determine the size needed to hold the route\nspecification string. Allocate a buffer of the appropriate size and then\nre-call the function to obtain the entire buffer.\n'
                },
                'name': 'errorDescription',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'error_description_size[0]'
                },
                'type': 'ViChar[]'
            },
            {
                'default_value': [
                    1024
                ],
                'direction': 'in',
                'documentation': {
                    'description': '\nAs input, it is the size of the error description string buffer. As\noutput, it is the Size of the entire error description string (may be\nlarger than the buffer size as the function always returns the size\nneeded to hold the entire buffer). This parameter is a ViInt32 that is\npassed by reference into the function. As an input, it is the size of\nthe error description buffer being passed. If the error description\nstring is larger than the string buffer being passed, only the portion\nof the route string that can fit in the string buffer will be copied\ninto it. On return from the function, it holds the size required to hold\nthe entire error description string, including the NULL termination\ncharacter. Note that this size may be larger than the buffer size as the\nfunction always returns the size needed to hold the entire buffer. You\nmay pass NULL for this parameter if you are not interested in the return\nvalue for it.\n'
                },
                'name': 'errorDescriptionSize',
                'size': {
                    'mechanism': 'fixed',
                    'value': 1
                },
                'type': 'ViInt32[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'IsConnected': {
        'documentation': {
            'description': '\nChecks whether the specified routes and routes groups are connected. It\nreturns true if connected.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe Session handle that you obtain from niSE_OpenSession. The handle\nidentifies a particular session to the virtual switch device.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nString describing the connections to check. The route specification\nstrings are best summarized as a series of routes delimited by\nampersands. The specified routes may be route names, route group names,\nor fully specified route paths delimited by square brackets. Some\nexamples of route specification strings are: MyRoute MyRouteGroup\nMyRoute & MyRouteGroup [A->Switch1/r0->B] MyRoute & MyRouteGroup &\n[A->Switch1/r0->B] Refer to Route Specification Strings in the NI Switch\nExecutive Help for more information.\n'
                },
                'name': 'routeSpec',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns TRUE if the routes and routes groups are connected or FALSE if\nthey are not.\n'
                },
                'name': 'isConnected',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'IsDebounced': {
        'documentation': {
            'description': '\nChecks to see if the switching system is debounced or not. This function\ndoes not wait for debouncing to occur. It returns true if the system is\nfully debounced. This function is similar to the IviSwtch specific\nfunction.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe Session handle that you obtain from niSE_OpenSession. The handle\nidentifies a particular session to the virtual switch device.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns TRUE if the system is fully debounced or FALSE if it is still\nsettling.\n'
                },
                'name': 'isDebounced',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'OpenSession': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nOpens a session to a specified NI Switch Executive virtual device. Opens\ncommunications with all of the IVI switches associated with the\nspecified NI Switch Executive virtual device. Returns a session handle\nthat you use to identify the virtual device in all subsequent NI Switch\nExecutive function calls. NI Switch Executive uses a reference counting\nscheme to manage open session handles to an NI Switch Executive virtual\ndevice. Each call to niSE_OpenSession must be matched with a subsequent\ncall to niSE_CloseSession. Successive calls to niSE_OpenSession with\nthe same virtual device name always returns the same session handle. NI\nSwitch Executive disconnects its communication with the IVI switches\nafter all session handles are closed to a given virtual device. The\nsession handles may be used safely in multiple threads of an\napplication. Sessions may only be opened to a given NI Switch Executive\nvirtual device from a single process at a time.\n'
        },
        'method_name_for_documentation': '__init__',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The name of the NI Switch Executive virtual device.'
                },
                'name': 'virtualDeviceName',
                'type': 'ViConstString'
            },
            {
                'default_value': '""',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe option string can be used to pass information to each of the IVI\ndevices on startup. It can be used to set things such as simulation,\nrange checking, etc. Consult your driver documentation for more\ninformation about valid entries for the option string.\n'
                },
                'name': 'optionString',
                'python_api_converter_name': 'convert_init_with_options_dictionary',
                'type': 'ViConstString',
                'type_in_documentation': 'dict'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The session referencing this NI Switch Executive virtual device session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'WaitForDebounce': {
        'documentation': {
            'description': '\nWaits for all of the switches in the NI Switch Executive virtual device\nto debounce. This function does not return until either the switching\nsystem is completely debounced and settled or the maximum time has\nelapsed and the system is not yet debounced. In the event that the\nmaximum time elapses, the function returns an error indicating that a\ntimeout has occurred. To ensure that all of the switches have settled,\nNI recommends calling niSE_WaitForDebounce after a series of connection\nor disconnection operations and before taking any measurements of the\nsignals connected to the switching system.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe Session handle that you obtain from niSE_OpenSession. The handle\nidentifies a particular session to the virtual switch device.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': 'datetime.timedelta(milliseconds=-1)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe amount of time to wait (in milliseconds) for the debounce to\ncomplete. A value of 0 checks for debouncing once and returns an error\nif the system is not debounced at that time. A value of -1 means to\nblock for an infinite period of time until the system is debounced.\n'
                },
                'name': 'maximumTimeMs',
                'python_api_converter_name': 'convert_timedelta_to_milliseconds',
                'type': 'ViInt32',
                'type_in_documentation': 'float in seconds or datetime.timedelta'
            }
        ],
        'returns': 'ViStatus'
    }
}
