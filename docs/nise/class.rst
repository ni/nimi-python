.. py:module:: nise

Session
=======

.. py:class:: Session(self, virtual_device_name, options={})

    

    Opens a session to a specified NI Switch Executive virtual device. Opens
    communications with all of the IVI switches associated with the
    specified NI Switch Executive virtual device. Returns a session handle
    that you use to identify the virtual device in all subsequent NI Switch
    Executive method calls. NI Switch Executive uses a reference counting
    scheme to manage open session handles to an NI Switch Executive virtual
    device. Each call to :py:meth:`nise.Session.__init__` must be matched with a subsequent
    call to :py:meth:`nise.Session.close`. Successive calls to :py:meth:`nise.Session.__init__` with
    the same virtual device name always returns the same session handle. NI
    Switch Executive disconnects its communication with the IVI switches
    after all session handles are closed to a given virtual device. The
    session handles may be used safely in multiple threads of an
    application. Sessions may only be opened to a given NI Switch Executive
    virtual device from a single process at a time.

    



    :param virtual_device_name:
        

        The name of the NI Switch Executive virtual device.

        


    :type virtual_device_name: str

    :param options:
        

        Specifies the initial value of certain properties for the session. The
        syntax for **options** is a dictionary of properties with an assigned
        value. For example:

        { 'simulate': False }

        You do not have to specify a value for all the properties. If you do not
        specify a value for a property, the default value is used.

        Advanced Example:
        { 'simulate': True, 'driver_setup': { 'Model': '<model number>',  'BoardType': '<type>' } }

        +-------------------------+---------+
        | Property                | Default |
        +=========================+=========+
        | range_check             | True    |
        +-------------------------+---------+
        | query_instrument_status | False   |
        +-------------------------+---------+
        | cache                   | True    |
        +-------------------------+---------+
        | simulate                | False   |
        +-------------------------+---------+
        | record_value_coersions  | False   |
        +-------------------------+---------+
        | driver_setup            | {}      |
        +-------------------------+---------+


    :type options: str


Methods
=======

close
-----

    .. py:currentmodule:: nise.Session

    .. py:method:: close()

            Reduces the reference count of open sessions by one. If the reference
            count goes to 0, the method deallocates any memory resources the
            driver uses and closes any open IVI switch sessions. After calling the
            :py:meth:`nise.Session.close` method, you should not use the NI Switch Executive
            virtual device again until you call :py:meth:`nise.Session.__init__`.

            

            .. note:: This method is not needed when using the session context manager



connect
-------

    .. py:currentmodule:: nise.Session

    .. py:method:: connect(connect_spec, multiconnect_mode=nise.MulticonnectMode.DEFAULT, wait_for_debounce=True)

            Connects the routes specified by the connection specification. When
            connecting, it may allow for multiconnection based on the
            multiconnection mode. In the event of an error, the call to
            :py:meth:`nise.Session.connect` will attempt to undo any connections made so that the
            system will be left in the same state that it was in before the call was
            made. Some errors can be caught before manipulating hardware, although
            it is feasible that a hardware call could fail causing some connections
            to be momentarily closed and then reopened. If the wait for debounce
            parameter is set, the method will not return until the switch system
            has debounced.

            



            :param connect_spec:


                String describing the connections to be made. The route specification
                strings are best summarized as a series of routes delimited by
                ampersands. The specified routes may be route names, route group names,
                or fully specified route paths delimited by square brackets. Some
                examples of route specification strings are: MyRoute MyRouteGroup
                MyRoute & MyRouteGroup [A->Switch1/r0->B] MyRoute & MyRouteGroup &
                [A->Switch1/r0->B] Refer to Route Specification Strings in the NI Switch
                Executive Help for more information.

                


            :type connect_spec: str
            :param multiconnect_mode:


                This value sets the connection mode for the method. The mode might be
                one of the following: :py:data:`~nise.NISE_VAL_USE_DEFAULT_MODE` (-1) - uses the mode
                selected as the default for the route in the NI Switch Executive virtual
                device configuration. If a mode has not been selected for the route in
                the NI Switch Executive virtual device, this parameter defaults to
                :py:data:`~nise.NISE_VAL_MULTICONNECT_ROUTES`. :py:data:`~nise.MulticonnectMode.NO_MULTICONNECT` (0) -
                routes specified in the connection specification must be disconnected
                before they can be reconnected. Calling Connect on a route that was
                connected using No Multiconnect mode results in an error condition.
                :py:data:`~nise.NISE_VAL_MULTICONNECT_ROUTES` (1)- routes specified in the connection
                specification can be connected multiple times. The first call to Connect
                performs the physical hardware connection. Successive calls to Connect
                increase a connection reference count. Similarly, calls to Disconnect
                decrease the reference count. Once it reaches 0, the hardware is
                physically disconnected. Multiconnecting routes applies to entire routes
                and not to route segments.

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type multiconnect_mode: :py:data:`nise.MulticonnectMode`
            :param wait_for_debounce:


                Waits (if true) for switches to debounce between its connect and
                disconnect operations. If false, it immediately begins the second
                operation after completing the first. The order of connect and
                disconnect operation is set by the Operation Order input.

                


            :type wait_for_debounce: bool

connect_and_disconnect
----------------------

    .. py:currentmodule:: nise.Session

    .. py:method:: connect_and_disconnect(connect_spec, disconnect_spec, multiconnect_mode=nise.MulticonnectMode.DEFAULT, operation_order=nise.OperationOrder.AFTER, wait_for_debounce=True)

            Connects routes and disconnects routes in a similar fashion to
            :py:meth:`nise.Session.connect` and :py:meth:`nise.Session.disconnect` except that the operations happen in
            the context of a single method call. This method is useful for
            switching from one state to another state. :py:meth:`nise.Session.connect_and_disconnect`
            manipulates the hardware connections and disconnections only when the
            routes are different between the connection and disconnection
            specifications. If any routes are common between the connection and
            disconnection specifications, NI Switch Executive determines whether or
            not the relays need to be switched. This functionality has the distinct
            advantage of increased throughput for shared connections, because
            hardware does not have to be involved and potentially increases relay
            lifetime by decreasing the number of times that the relay has to be
            switched. In the event of an error, the call to
            :py:meth:`nise.Session.connect_and_disconnect` attempts to undo any connections made, but
            does not attempt to reconnect disconnections. Some errors can be caught
            before manipulating hardware, although it is feasible that a hardware
            call could fail causing some connections to be momentarily closed and
            then reopened.

            



            :param connect_spec:


                String describing the connections to be made. The route specification
                strings are best summarized as a series of routes delimited by
                ampersands. The specified routes may be route names, route group names,
                or fully specified route paths delimited by square brackets. Some
                examples of route specification strings are: MyRoute MyRouteGroup
                MyRoute & MyRouteGroup [A->Switch1/r0->B] MyRoute & MyRouteGroup &
                [A->Switch1/r0->B] Refer to Route Specification Strings in the NI Switch
                Executive Help for more information.

                


            :type connect_spec: str
            :param disconnect_spec:


                String describing the disconnections to be made. The route specification
                strings are best summarized as a series of routes delimited by
                ampersands. The specified routes may be route names, route group names,
                or fully specified route paths delimited by square brackets. Some
                examples of route specification strings are: MyRoute MyRouteGroup
                MyRoute & MyRouteGroup [A->Switch1/r0->B] MyRoute & MyRouteGroup &
                [A->Switch1/r0->B] Refer to Route Specification Strings in the NI Switch
                Executive Help for more information.

                


            :type disconnect_spec: str
            :param multiconnect_mode:


                This value sets the connection mode for the method. The mode might be
                one of the following: :py:data:`~nise.NISE_VAL_USE_DEFAULT_MODE` (-1) - uses the mode
                selected as the default for the route in the NI Switch Executive virtual
                device configuration. If a mode has not been selected for the route in
                the NI Switch Executive virtual device, this parameter defaults to
                :py:data:`~nise.NISE_VAL_MULTICONNECT_ROUTES`. :py:data:`~nise.MulticonnectMode.NO_MULTICONNECT` (0) -
                routes specified in the connection specification must be disconnected
                before they can be reconnected. Calling Connect on a route that was
                connected using No Multiconnect mode results in an error condition.
                :py:data:`~nise.NISE_VAL_MULTICONNECT_ROUTES` (1) - routes specified in the connection
                specification can be connected multiple times. The first call to Connect
                performs the physical hardware connection. Successive calls to Connect
                increase a connection reference count. Similarly, calls to Disconnect
                decrease the reference count. Once it reaches 0, the hardware is
                physically disconnected. This behavior is slightly different with SPDT
                relays. For more information, refer to the Exclusions and SPDT Relays
                topic in the NI Switch Executive Help. Multiconnecting routes applies to
                entire routes and not to route segments.

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type multiconnect_mode: :py:data:`nise.MulticonnectMode`
            :param operation_order:


                Sets the order of the operation for the method. Defined values are
                Break Before Make and Break After Make. :py:data:`~nise.OperationOrder.BEFORE`
                (1) - The method disconnects the routes specified in the disconnect
                specification before connecting the routes specified in the connect
                specification. This is the typical mode of operation.
                :py:data:`~nise.OperationOrder.AFTER` (2) - The method connects the routes
                specified in the connection specification before connecting the routes
                specified in the disconnection specification. This mode of operation is
                normally used when you are switching current and want to ensure that a
                load is always connected to your source. The order of operation is to
                connect first or disconnect first.

                


            :type operation_order: :py:data:`nise.OperationOrder`
            :param wait_for_debounce:


                Waits (if true) for switches to debounce between its connect and
                disconnect operations. If false, it immediately begins the second
                operation after completing the first. The order of connect and
                disconnect operation is set by the Operation Order input.

                


            :type wait_for_debounce: bool

disconnect
----------

    .. py:currentmodule:: nise.Session

    .. py:method:: disconnect(disconnect_spec)

            Disconnects the routes specified in the Disconnection Specification. If
            any of the specified routes were originally connected in a
            multiconnected mode, the call to :py:meth:`nise.Session.disconnect` reduces the reference
            count on the route by 1. If the reference count reaches 0, it is
            disconnected. If a specified route does not exist, it is an error
            condition. In the event of an error, the call to :py:meth:`nise.Session.disconnect`
            continues to try to disconnect everything specified by the route
            specification string but reports the error on completion.

            



            :param disconnect_spec:


                String describing the disconnections to be made. The route specification
                strings are best summarized as a series of routes delimited by
                ampersands. The specified routes may be route names, route group names,
                or fully specified route paths delimited by square brackets. Some
                examples of route specification strings are: MyRoute MyRouteGroup
                MyRoute & MyRouteGroup [A->Switch1/r0->B] MyRoute & MyRouteGroup &
                [A->Switch1/r0->B] Refer to Route Specification Strings in the NI Switch
                Executive Help for more information.

                


            :type disconnect_spec: str

disconnect_all
--------------

    .. py:currentmodule:: nise.Session

    .. py:method:: disconnect_all()

            Disconnects all connections on every IVI switch device managed by the
            NISE session reference passed to this method. :py:meth:`nise.Session.disconnect_all`
            ignores all multiconnect modes. Calling :py:meth:`nise.Session.disconnect_all` resets all
            of the switch states for the system.

            



expand_route_spec
-----------------

    .. py:currentmodule:: nise.Session

    .. py:method:: expand_route_spec(route_spec, expand_action=nise.ExpandAction.ROUTES, expanded_route_spec_size=[1024])

            Expands a route spec string to yield more information about the routes
            and route groups within the spec. The route specification string
            returned from :py:meth:`nise.Session.expand_route_spec` can be passed to other Switch
            Executive API methods (such as :py:meth:`nise.Session.connect`, :py:meth:`nise.Session.disconnect`, and
            :py:meth:`nise.Session.connect_and_disconnect`) that use route specification strings.

            



            :param route_spec:


                String describing the routes and route groups to expand. The route
                specification strings are best summarized as a series of routes
                delimited by ampersands. The specified routes may be route names, route
                group names, or fully specified route paths delimited by square
                brackets. Some examples of route specification strings are: MyRoute
                MyRouteGroup MyRoute & MyRouteGroup [A->Switch1/r0->B] MyRoute &
                MyRouteGroup & [A->Switch1/r0->B] Refer to Route Specification Strings
                in the NI Switch Executive Help for more information.

                


            :type route_spec: str
            :param expand_action:


                This value sets the expand action for the method. The action might be
                one of the following: :py:data:`~nise.ExpandAction.ROUTES` (0) - expands the
                route spec to routes. Converts route groups to their constituent routes.
                :py:data:`~nise.ExpandAction.PATHS` (1) - expands the route spec to paths.
                Converts routes and route groups to their constituent square bracket
                route spec strings. Example: [Dev1/c0->Dev1/r0->Dev1/c1]

                


            :type expand_action: :py:data:`nise.ExpandAction`
            :param expanded_route_spec_size:


                The routeSpecSize is an ViInt32 that is passed by reference into the
                method. As an input, it is the size of the route spec string buffer
                being passed. If the route spec string is larger than the string buffer
                being passed, only the portion of the route spec string that can fit in
                the string buffer is copied into it. On return from the method,
                routeSpecSize holds the size required to hold the entire route spec
                string. Note that this size may be larger than the buffer size as the
                method always returns the size needed to hold the entire buffer. You
                may pass NULL for this parameter if you are not interested in the return
                value for routeSpecSize and routeSpec.

                


            :type expanded_route_spec_size: list of int

            :rtype: str
            :return:


                    The expanded route spec. Route specification strings can be directly
                    passed to :py:meth:`nise.Session.connect`, :py:meth:`nise.Session.disconnect`, or :py:meth:`nise.Session.connect_and_disconnect`
                    Refer to Route Specification Strings in the NI Switch Executive Help for
                    more information. You may pass NULL for this parameter if you are not
                    interested in the return value. To obtain the route specification
                    string, you should pass a buffer to this parameter. The size of the
                    buffer required may be obtained by calling the method with NULL for
                    this parameter and a valid ViInt32 to routeSpecSize. The routeSpecSize
                    will contain the size needed to hold the entire route specification
                    (including the NULL termination character). Common operation is to call
                    the method twice. The first time you call the method you can
                    determine the size needed to hold the route specification string.
                    Allocate a buffer of the appropriate size and then re-call the method
                    to obtain the entire buffer.

                    



find_route
----------

    .. py:currentmodule:: nise.Session

    .. py:method:: find_route(channel1, channel2, route_spec_size=[1024])

            Finds an existing or potential route between channel 1 and channel 2.
            The returned route specification contains the route specification and
            the route capability determines whether or not the route existed, is
            possible, or is not possible for various reasons. The route
            specification string returned from :py:meth:`nise.Session.find_route` can be passed to
            other Switch Executive API methods (such as :py:meth:`nise.Session.connect`,
            :py:meth:`nise.Session.disconnect`, and :py:meth:`nise.Session.connect_and_disconnect`) that use route
            specification strings.

            



            :param channel1:


                Channel name of one of the endpoints of the route to find. The channel
                name must either be a channel alias name or a name in the
                device/ivichannel syntax. Examples: MyChannel Switch1/R0

                


            :type channel1: str
            :param channel2:


                Channel name of one of the endpoints of the route to find. The channel
                name must either be a channel alias name or a name in the
                device/ivichannel syntax. Examples: MyChannel Switch1/R0

                


            :type channel2: str
            :param route_spec_size:


                The routeSpecSize is an ViInt32 that is passed by reference into the
                method. As an input, it is the size of the route string buffer being
                passed. If the route string is larger than the string buffer being
                passed, only the portion of the route string that can fit in the string
                buffer is copied into it. On return from the method, routeSpecSize
                holds the size required to hold the entire route string. Note that this
                size may be larger than the buffer size as the method always returns
                the size needed to hold the entire buffer. You may pass NULL for this
                parameter if you are not interested in the return value for
                routeSpecSize and routeSpec.

                


            :type route_spec_size: list of int

            :rtype: tuple (route_spec, path_capability)

                WHERE

                route_spec (str): 


                    The fully specified route path complete with delimiting square
                    brackets if the route exists or is possible. An example of a fully
                    specified route string is: [A->Switch1/r0->B] Route specification
                    strings can be directly passed to :py:meth:`nise.Session.connect`, :py:meth:`nise.Session.disconnect`, or
                    :py:meth:`nise.Session.connect_and_disconnect` Refer to Route Specification Strings in the
                    NI Switch Executive Help for more information. You may pass NULL for
                    this parameter if you are not interested in the return value. To obtain
                    the route specification string, you should pass a buffer to this
                    parameter. The size of the buffer required may be obtained by calling
                    the method with NULL for this parameter and a valid ViInt32 to
                    routeSpecSize. The routeSpecSize will contain the size needed to hold
                    the entire route specification (including the NULL termination
                    character). Common operation is to call the method twice. The first
                    time you call the method you can determine the size needed to hold the
                    route specification string. Allocate a buffer of the appropriate size
                    and then re-call the method to obtain the entire buffer.

                    


                path_capability (:py:data:`nise.PathCapability`): 


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

                    



get_all_connections
-------------------

    .. py:currentmodule:: nise.Session

    .. py:method:: get_all_connections(route_spec_size=[1024])

            Returns the top-level connected routes and route groups. The route
            specification string returned from :py:meth:`nise.Session.get_all_connections` can be passed
            to other Switch Executive API methods (such as :py:meth:`nise.Session.connect`,
            :py:meth:`nise.Session.disconnect`, :py:meth:`nise.Session.connect_and_disconnect`, and :py:meth:`nise.Session.expand_route_spec`)
            that use route specification strings.

            



            :param route_spec_size:


                The routeSpecSize is an ViInt32 that is passed by reference into the
                method. As an input, it is the size of the route spec string buffer
                being passed. If the route spec string is larger than the string buffer
                being passed, only the portion of the route spec string that can fit in
                the string buffer is copied into it. On return from the method,
                routeSpecSize holds the size required to hold the entire route spec
                string. Note that this size may be larger than the buffer size as the
                method always returns the size needed to hold the entire buffer. You
                may pass NULL for this parameter if you are not interested in the return
                value for routeSpecSize and routeSpec.

                


            :type route_spec_size: list of int

            :rtype: str
            :return:


                    The route spec of all currently connected routes and route groups. Route
                    specification strings can be directly passed to :py:meth:`nise.Session.connect`,
                    :py:meth:`nise.Session.disconnect`, :py:meth:`nise.Session.connect_and_disconnect`, or :py:meth:`nise.Session.expand_route_spec`
                    Refer to Route Specification Strings in the NI Switch Executive Help for
                    more information. You may pass NULL for this parameter if you are not
                    interested in the return value. To obtain the route specification
                    string, you should pass a buffer to this parameter. The size of the
                    buffer required may be obtained by calling the method with NULL for
                    this parameter and a valid ViInt32 to routeSpecSize. The routeSpecSize
                    will contain the size needed to hold the entire route specification
                    (including the NULL termination character). Common operation is to call
                    the method twice. The first time you call the method you can
                    determine the size needed to hold the route specification string.
                    Allocate a buffer of the appropriate size and then re-call the method
                    to obtain the entire buffer.

                    



is_connected
------------

    .. py:currentmodule:: nise.Session

    .. py:method:: is_connected(route_spec)

            Checks whether the specified routes and routes groups are connected. It
            returns true if connected.

            



            :param route_spec:


                String describing the connections to check. The route specification
                strings are best summarized as a series of routes delimited by
                ampersands. The specified routes may be route names, route group names,
                or fully specified route paths delimited by square brackets. Some
                examples of route specification strings are: MyRoute MyRouteGroup
                MyRoute & MyRouteGroup [A->Switch1/r0->B] MyRoute & MyRouteGroup &
                [A->Switch1/r0->B] Refer to Route Specification Strings in the NI Switch
                Executive Help for more information.

                


            :type route_spec: str

            :rtype: bool
            :return:


                    Returns TRUE if the routes and routes groups are connected or FALSE if
                    they are not.

                    



is_debounced
------------

    .. py:currentmodule:: nise.Session

    .. py:method:: is_debounced()

            Checks to see if the switching system is debounced or not. This method
            does not wait for debouncing to occur. It returns true if the system is
            fully debounced. This method is similar to the IviSwtch specific
            method.

            



            :rtype: bool
            :return:


                    Returns TRUE if the system is fully debounced or FALSE if it is still
                    settling.

                    



wait_for_debounce
-----------------

    .. py:currentmodule:: nise.Session

    .. py:method:: wait_for_debounce(maximum_time_ms=datetime.timedelta(milliseconds=-1))

            Waits for all of the switches in the NI Switch Executive virtual device
            to debounce. This method does not return until either the switching
            system is completely debounced and settled or the maximum time has
            elapsed and the system is not yet debounced. In the event that the
            maximum time elapses, the method returns an error indicating that a
            timeout has occurred. To ensure that all of the switches have settled,
            NI recommends calling :py:meth:`nise.Session.wait_for_debounce` after a series of connection
            or disconnection operations and before taking any measurements of the
            signals connected to the switching system.

            



            :param maximum_time_ms:


                The amount of time to wait (in milliseconds) for the debounce to
                complete. A value of 0 checks for debouncing once and returns an error
                if the system is not debounced at that time. A value of -1 means to
                block for an infinite period of time until the system is debounced.

                


            :type maximum_time_ms: float in seconds or datetime.timedelta



Properties
==========


.. contents:: Session


