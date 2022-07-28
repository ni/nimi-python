# -*- coding: utf-8 -*-
# This file was generated
import array  # noqa: F401
import ctypes

import nise._converters as _converters
import nise._library_singleton as _library_singleton
import nise._visatype as _visatype
import nise.enums as enums
import nise.errors as errors

import hightime

# Used for __repr__
import pprint
pp = pprint.PrettyPrinter(indent=4)


# Helper functions for creating ctypes needed for calling into the driver DLL
def get_ctypes_pointer_for_buffer(value=None, library_type=None, size=None):
    if isinstance(value, array.array):
        assert library_type is not None, 'library_type is required for array.array'
        addr, _ = value.buffer_info()
        return ctypes.cast(addr, ctypes.POINTER(library_type))
    elif str(type(value)).find("'numpy.ndarray'") != -1:
        import numpy
        return numpy.ctypeslib.as_ctypes(value)
    elif isinstance(value, bytes):
        return ctypes.cast(value, ctypes.POINTER(library_type))
    elif isinstance(value, list):
        assert library_type is not None, 'library_type is required for list'
        return (library_type * len(value))(*value)
    else:
        if library_type is not None and size is not None:
            return (library_type * size)()
        else:
            return None


def get_ctypes_and_array(value, array_type):
    if value is not None:
        if isinstance(value, array.array):
            value_array = value
        else:
            value_array = array.array(array_type, value)
    else:
        value_array = None

    return value_array


class _SessionBase(object):
    '''Base class for all NI Switch Executive sessions.'''

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

    def __init__(self, repeated_capability_list, all_channels_in_session, vi, library, encoding, freeze_it=False):
        self._repeated_capability_list = repeated_capability_list
        self._repeated_capability = ','.join(repeated_capability_list)
        self._all_channels_in_session = all_channels_in_session
        self._vi = vi
        self._library = library
        self._encoding = encoding

        # Store the parameter list for later printing in __repr__
        param_list = []
        param_list.append("repeated_capability_list=" + pp.pformat(repeated_capability_list))
        param_list.append("vi=" + pp.pformat(vi))
        param_list.append("library=" + pp.pformat(library))
        param_list.append("encoding=" + pp.pformat(encoding))
        self._param_list = ', '.join(param_list)

        # Finally, set _is_frozen to True which is used to prevent clients from accidentally adding
        # members when trying to set a property with a typo.
        self._is_frozen = freeze_it

    def __repr__(self):
        return '{0}.{1}({2})'.format('nise', self.__class__.__name__, self._param_list)

    def __setattr__(self, key, value):
        if self._is_frozen and key not in dir(self):
            raise AttributeError("'{0}' object has no attribute '{1}'".format(type(self).__name__, key))
        object.__setattr__(self, key, value)

    def _get_error_description(self, error_code):
        '''_get_error_description

        Returns the error description.
        '''
        try:
            _, error_string = self._get_error()
            return error_string
        except errors.Error:
            pass

        try:
            '''
            It is expected for _get_error to raise when the session is invalid
            (IVI spec requires GetError to fail).
            Use _error_message instead. It doesn't require a session.
            '''
            error_string = self._error_message(error_code)
            return error_string
        except errors.Error:
            return "Failed to retrieve error description."

    ''' These are code-generated '''

    def _get_error(self, error_description_size=[1024]):
        r'''_get_error

        Get error information of the first error that occurred. If a valid
        pointer is passed to errorDescription or errorNumber, GetError will
        clear the error on completion. errorDescriptionSize is an in/out
        parameter that describes the size of the errorDescription buffer. On the
        way in, it tells the method the size of string. On the way out, it
        describes the number of bytes (including the trailing null string)
        needed to hold the entire error description buffer. If NULL is passed
        for errorDescription and the errorNumber, the method will not clear
        the error. Users wanting to dynamically size the errorDescription string
        can thus call the method twice. On the first call they can pass NULL
        for the errorDescription and use the returned errorDescriptionSize to
        allocate enough space for the entire errorDescription buffer. Note that
        if a buffer is passed that is not large enough to hold the entire
        description string, the portion of of the string that will fit in the
        passed buffer will be returned and the error will still be cleared. All
        of the parameters are NULL tolerant. Note that passing NULL for both
        errorNumber and errorDescription can change the method's behavior.

        Args:
            error_description_size (list of int): As input, it is the size of the error description string buffer. As
                output, it is the Size of the entire error description string (may be
                larger than the buffer size as the method always returns the size
                needed to hold the entire buffer). This parameter is a ViInt32 that is
                passed by reference into the method. As an input, it is the size of
                the error description buffer being passed. If the error description
                string is larger than the string buffer being passed, only the portion
                of the route string that can fit in the string buffer will be copied
                into it. On return from the method, it holds the size required to hold
                the entire error description string, including the NULL termination
                character. Note that this size may be larger than the buffer size as the
                method always returns the size needed to hold the entire buffer. You
                may pass NULL for this parameter if you are not interested in the return
                value for it.


        Returns:
            error_number (int): By reference parameter which returns the error number of the first error
                which occurred on the session since the error was last cleared. You may
                pass NULL for this parameter if you are not interested in the return
                value.

            error_description (str): By reference buffer which is to be filled with the error description
                string. You may pass NULL for this parameter if you are not interested
                in the return value. To obtain the error description string, you should
                pass a buffer to this parameter. The size of the buffer required may be
                obtained by calling the method with NULL for this parameter and a
                valid ViInt32 to the error description size parameter. The error
                description size will contain the size needed to hold the entire route
                specification (including the NULL termination character). Common
                operation is to call the method twice. The first time you call the
                method you can determine the size needed to hold the route
                specification string. Allocate a buffer of the appropriate size and then
                re-call the method to obtain the entire buffer.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_number_ctype = _visatype.ViInt32()  # case S220
        error_description_ctype = (_visatype.ViChar * error_description_size[0])()  # case C080
        error_description_size_ctype = get_ctypes_pointer_for_buffer(value=error_description_size, library_type=_visatype.ViInt32)  # case B550
        error_code = self._library.niSE_GetError(vi_ctype, None if error_number_ctype is None else (ctypes.pointer(error_number_ctype)), error_description_ctype, error_description_size_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return int(error_number_ctype.value), error_description_ctype.value.decode(self._encoding)


class Session(_SessionBase):
    '''An NI Switch Executive session'''

    def __init__(self, virtual_device_name, options={}):
        r'''An NI Switch Executive session

        Opens a session to a specified NI Switch Executive virtual device. Opens
        communications with all of the IVI switches associated with the
        specified NI Switch Executive virtual device. Returns a session handle
        that you use to identify the virtual device in all subsequent NI Switch
        Executive method calls. NI Switch Executive uses a reference counting
        scheme to manage open session handles to an NI Switch Executive virtual
        device. Each call to __init__ must be matched with a subsequent
        call to close. Successive calls to __init__ with
        the same virtual device name always returns the same session handle. NI
        Switch Executive disconnects its communication with the IVI switches
        after all session handles are closed to a given virtual device. The
        session handles may be used safely in multiple threads of an
        application. Sessions may only be opened to a given NI Switch Executive
        virtual device from a single process at a time.

        Args:
            virtual_device_name (str): The name of the NI Switch Executive virtual device.

            options (dict): Specifies the initial value of certain properties for the session. The
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


        Returns:
            session (nise.Session): A session object representing the device.

        '''
        # Initialize the superclass with default values first, populate them later
        super(Session, self).__init__(
            repeated_capability_list=[],
            vi=None,
            library=None,
            encoding=None,
            freeze_it=False,
            all_channels_in_session=None
        )
        options = _converters.convert_init_with_options_dictionary(options)
        self._library = _library_singleton.get()
        self._encoding = 'windows-1251'

        # Call specified init function
        self._vi = 0  # This must be set before calling _open_session().
        self._vi = self._open_session(virtual_device_name, options)

        # Store the parameter list for later printing in __repr__
        param_list = []
        param_list.append("virtual_device_name=" + pp.pformat(virtual_device_name))
        param_list.append("options=" + pp.pformat(options))
        self._param_list = ', '.join(param_list)

        # Store the list of channels in the Session which is needed by some nimi-python modules.
        # Use try/except because not all the modules support channels.
        # self.get_channel_names() and self.channel_count can only be called after the session
        # handle `self._vi` is set
        try:
            self._all_channels_in_session = self.get_channel_names(range(self.channel_count))
        except AttributeError:
            self._all_channels_in_session = None

        # Finally, set _is_frozen to True which is used to prevent clients from accidentally adding
        # members when trying to set a property with a typo.
        self._is_frozen = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        '''close

        Reduces the reference count of open sessions by one. If the reference
        count goes to 0, the method deallocates any memory resources the
        driver uses and closes any open IVI switch sessions. After calling the
        close method, you should not use the NI Switch Executive
        virtual device again until you call __init__.

        Note:
        This method is not needed when using the session context manager
        '''
        try:
            self._close_session()
        except errors.DriverError:
            self._vi = 0
            raise
        self._vi = 0

    ''' These are code-generated '''

    def _close_session(self):
        r'''_close_session

        Reduces the reference count of open sessions by one. If the reference
        count goes to 0, the method deallocates any memory resources the
        driver uses and closes any open IVI switch sessions. After calling the
        close method, you should not use the NI Switch Executive
        virtual device again until you call __init__.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niSE_CloseSession(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def connect(self, connect_spec, multiconnect_mode=enums.MulticonnectMode.DEFAULT, wait_for_debounce=True):
        r'''connect

        Connects the routes specified by the connection specification. When
        connecting, it may allow for multiconnection based on the
        multiconnection mode. In the event of an error, the call to
        connect will attempt to undo any connections made so that the
        system will be left in the same state that it was in before the call was
        made. Some errors can be caught before manipulating hardware, although
        it is feasible that a hardware call could fail causing some connections
        to be momentarily closed and then reopened. If the wait for debounce
        parameter is set, the method will not return until the switch system
        has debounced.

        Args:
            connect_spec (str): String describing the connections to be made. The route specification
                strings are best summarized as a series of routes delimited by
                ampersands. The specified routes may be route names, route group names,
                or fully specified route paths delimited by square brackets. Some
                examples of route specification strings are: MyRoute MyRouteGroup
                MyRoute & MyRouteGroup [A->Switch1/r0->B] MyRoute & MyRouteGroup &
                [A->Switch1/r0->B] Refer to Route Specification Strings in the NI Switch
                Executive Help for more information.

            multiconnect_mode (enums.MulticonnectMode): This value sets the connection mode for the method. The mode might be
                one of the following: NISE_VAL_USE_DEFAULT_MODE (-1) - uses the mode
                selected as the default for the route in the NI Switch Executive virtual
                device configuration. If a mode has not been selected for the route in
                the NI Switch Executive virtual device, this parameter defaults to
                NISE_VAL_MULTICONNECT_ROUTES. MulticonnectMode.NO_MULTICONNECT (0) -
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

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            wait_for_debounce (bool): Waits (if true) for switches to debounce between its connect and
                disconnect operations. If false, it immediately begins the second
                operation after completing the first. The order of connect and
                disconnect operation is set by the Operation Order input.

        '''
        if type(multiconnect_mode) is not enums.MulticonnectMode:
            raise TypeError('Parameter multiconnect_mode must be of type ' + str(enums.MulticonnectMode))
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        connect_spec_ctype = ctypes.create_string_buffer(connect_spec.encode(self._encoding))  # case C020
        multiconnect_mode_ctype = _visatype.ViInt32(multiconnect_mode.value)  # case S130
        wait_for_debounce_ctype = _visatype.ViBoolean(wait_for_debounce)  # case S150
        error_code = self._library.niSE_Connect(vi_ctype, connect_spec_ctype, multiconnect_mode_ctype, wait_for_debounce_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def connect_and_disconnect(self, connect_spec, disconnect_spec, multiconnect_mode=enums.MulticonnectMode.DEFAULT, operation_order=enums.OperationOrder.AFTER, wait_for_debounce=True):
        r'''connect_and_disconnect

        Connects routes and disconnects routes in a similar fashion to
        connect and disconnect except that the operations happen in
        the context of a single method call. This method is useful for
        switching from one state to another state. connect_and_disconnect
        manipulates the hardware connections and disconnections only when the
        routes are different between the connection and disconnection
        specifications. If any routes are common between the connection and
        disconnection specifications, NI Switch Executive determines whether or
        not the relays need to be switched. This functionality has the distinct
        advantage of increased throughput for shared connections, because
        hardware does not have to be involved and potentially increases relay
        lifetime by decreasing the number of times that the relay has to be
        switched. In the event of an error, the call to
        connect_and_disconnect attempts to undo any connections made, but
        does not attempt to reconnect disconnections. Some errors can be caught
        before manipulating hardware, although it is feasible that a hardware
        call could fail causing some connections to be momentarily closed and
        then reopened.

        Args:
            connect_spec (str): String describing the connections to be made. The route specification
                strings are best summarized as a series of routes delimited by
                ampersands. The specified routes may be route names, route group names,
                or fully specified route paths delimited by square brackets. Some
                examples of route specification strings are: MyRoute MyRouteGroup
                MyRoute & MyRouteGroup [A->Switch1/r0->B] MyRoute & MyRouteGroup &
                [A->Switch1/r0->B] Refer to Route Specification Strings in the NI Switch
                Executive Help for more information.

            disconnect_spec (str): String describing the disconnections to be made. The route specification
                strings are best summarized as a series of routes delimited by
                ampersands. The specified routes may be route names, route group names,
                or fully specified route paths delimited by square brackets. Some
                examples of route specification strings are: MyRoute MyRouteGroup
                MyRoute & MyRouteGroup [A->Switch1/r0->B] MyRoute & MyRouteGroup &
                [A->Switch1/r0->B] Refer to Route Specification Strings in the NI Switch
                Executive Help for more information.

            multiconnect_mode (enums.MulticonnectMode): This value sets the connection mode for the method. The mode might be
                one of the following: NISE_VAL_USE_DEFAULT_MODE (-1) - uses the mode
                selected as the default for the route in the NI Switch Executive virtual
                device configuration. If a mode has not been selected for the route in
                the NI Switch Executive virtual device, this parameter defaults to
                NISE_VAL_MULTICONNECT_ROUTES. MulticonnectMode.NO_MULTICONNECT (0) -
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

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            operation_order (enums.OperationOrder): Sets the order of the operation for the method. Defined values are
                Break Before Make and Break After Make. OperationOrder.BEFORE
                (1) - The method disconnects the routes specified in the disconnect
                specification before connecting the routes specified in the connect
                specification. This is the typical mode of operation.
                OperationOrder.AFTER (2) - The method connects the routes
                specified in the connection specification before connecting the routes
                specified in the disconnection specification. This mode of operation is
                normally used when you are switching current and want to ensure that a
                load is always connected to your source. The order of operation is to
                connect first or disconnect first.

            wait_for_debounce (bool): Waits (if true) for switches to debounce between its connect and
                disconnect operations. If false, it immediately begins the second
                operation after completing the first. The order of connect and
                disconnect operation is set by the Operation Order input.

        '''
        if type(multiconnect_mode) is not enums.MulticonnectMode:
            raise TypeError('Parameter multiconnect_mode must be of type ' + str(enums.MulticonnectMode))
        if type(operation_order) is not enums.OperationOrder:
            raise TypeError('Parameter operation_order must be of type ' + str(enums.OperationOrder))
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        connect_spec_ctype = ctypes.create_string_buffer(connect_spec.encode(self._encoding))  # case C020
        disconnect_spec_ctype = ctypes.create_string_buffer(disconnect_spec.encode(self._encoding))  # case C020
        multiconnect_mode_ctype = _visatype.ViInt32(multiconnect_mode.value)  # case S130
        operation_order_ctype = _visatype.ViInt32(operation_order.value)  # case S130
        wait_for_debounce_ctype = _visatype.ViBoolean(wait_for_debounce)  # case S150
        error_code = self._library.niSE_ConnectAndDisconnect(vi_ctype, connect_spec_ctype, disconnect_spec_ctype, multiconnect_mode_ctype, operation_order_ctype, wait_for_debounce_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disconnect(self, disconnect_spec):
        r'''disconnect

        Disconnects the routes specified in the Disconnection Specification. If
        any of the specified routes were originally connected in a
        multiconnected mode, the call to disconnect reduces the reference
        count on the route by 1. If the reference count reaches 0, it is
        disconnected. If a specified route does not exist, it is an error
        condition. In the event of an error, the call to disconnect
        continues to try to disconnect everything specified by the route
        specification string but reports the error on completion.

        Args:
            disconnect_spec (str): String describing the disconnections to be made. The route specification
                strings are best summarized as a series of routes delimited by
                ampersands. The specified routes may be route names, route group names,
                or fully specified route paths delimited by square brackets. Some
                examples of route specification strings are: MyRoute MyRouteGroup
                MyRoute & MyRouteGroup [A->Switch1/r0->B] MyRoute & MyRouteGroup &
                [A->Switch1/r0->B] Refer to Route Specification Strings in the NI Switch
                Executive Help for more information.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        disconnect_spec_ctype = ctypes.create_string_buffer(disconnect_spec.encode(self._encoding))  # case C020
        error_code = self._library.niSE_Disconnect(vi_ctype, disconnect_spec_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disconnect_all(self):
        r'''disconnect_all

        Disconnects all connections on every IVI switch device managed by the
        NISE session reference passed to this method. disconnect_all
        ignores all multiconnect modes. Calling disconnect_all resets all
        of the switch states for the system.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niSE_DisconnectAll(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def expand_route_spec(self, route_spec, expand_action=enums.ExpandAction.ROUTES, expanded_route_spec_size=[1024]):
        r'''expand_route_spec

        Expands a route spec string to yield more information about the routes
        and route groups within the spec. The route specification string
        returned from expand_route_spec can be passed to other Switch
        Executive API methods (such as connect, disconnect, and
        connect_and_disconnect) that use route specification strings.

        Args:
            route_spec (str): String describing the routes and route groups to expand. The route
                specification strings are best summarized as a series of routes
                delimited by ampersands. The specified routes may be route names, route
                group names, or fully specified route paths delimited by square
                brackets. Some examples of route specification strings are: MyRoute
                MyRouteGroup MyRoute & MyRouteGroup [A->Switch1/r0->B] MyRoute &
                MyRouteGroup & [A->Switch1/r0->B] Refer to Route Specification Strings
                in the NI Switch Executive Help for more information.

            expand_action (enums.ExpandAction): This value sets the expand action for the method. The action might be
                one of the following: ExpandAction.ROUTES (0) - expands the
                route spec to routes. Converts route groups to their constituent routes.
                ExpandAction.PATHS (1) - expands the route spec to paths.
                Converts routes and route groups to their constituent square bracket
                route spec strings. Example: [Dev1/c0->Dev1/r0->Dev1/c1]

            expanded_route_spec_size (list of int): The routeSpecSize is an ViInt32 that is passed by reference into the
                method. As an input, it is the size of the route spec string buffer
                being passed. If the route spec string is larger than the string buffer
                being passed, only the portion of the route spec string that can fit in
                the string buffer is copied into it. On return from the method,
                routeSpecSize holds the size required to hold the entire route spec
                string. Note that this size may be larger than the buffer size as the
                method always returns the size needed to hold the entire buffer. You
                may pass NULL for this parameter if you are not interested in the return
                value for routeSpecSize and routeSpec.


        Returns:
            expanded_route_spec (str): The expanded route spec. Route specification strings can be directly
                passed to connect, disconnect, or connect_and_disconnect
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

        '''
        if type(expand_action) is not enums.ExpandAction:
            raise TypeError('Parameter expand_action must be of type ' + str(enums.ExpandAction))
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        route_spec_ctype = ctypes.create_string_buffer(route_spec.encode(self._encoding))  # case C020
        expand_action_ctype = _visatype.ViInt32(expand_action.value)  # case S130
        expanded_route_spec_ctype = (_visatype.ViChar * expanded_route_spec_size[0])()  # case C080
        expanded_route_spec_size_ctype = get_ctypes_pointer_for_buffer(value=expanded_route_spec_size, library_type=_visatype.ViInt32)  # case B550
        error_code = self._library.niSE_ExpandRouteSpec(vi_ctype, route_spec_ctype, expand_action_ctype, expanded_route_spec_ctype, expanded_route_spec_size_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return expanded_route_spec_ctype.value.decode(self._encoding)

    def find_route(self, channel1, channel2, route_spec_size=[1024]):
        r'''find_route

        Finds an existing or potential route between channel 1 and channel 2.
        The returned route specification contains the route specification and
        the route capability determines whether or not the route existed, is
        possible, or is not possible for various reasons. The route
        specification string returned from find_route can be passed to
        other Switch Executive API methods (such as connect,
        disconnect, and connect_and_disconnect) that use route
        specification strings.

        Args:
            channel1 (str): Channel name of one of the endpoints of the route to find. The channel
                name must either be a channel alias name or a name in the
                device/ivichannel syntax. Examples: MyChannel Switch1/R0

            channel2 (str): Channel name of one of the endpoints of the route to find. The channel
                name must either be a channel alias name or a name in the
                device/ivichannel syntax. Examples: MyChannel Switch1/R0

            route_spec_size (list of int): The routeSpecSize is an ViInt32 that is passed by reference into the
                method. As an input, it is the size of the route string buffer being
                passed. If the route string is larger than the string buffer being
                passed, only the portion of the route string that can fit in the string
                buffer is copied into it. On return from the method, routeSpecSize
                holds the size required to hold the entire route string. Note that this
                size may be larger than the buffer size as the method always returns
                the size needed to hold the entire buffer. You may pass NULL for this
                parameter if you are not interested in the return value for
                routeSpecSize and routeSpec.


        Returns:
            route_spec (str): The fully specified route path complete with delimiting square
                brackets if the route exists or is possible. An example of a fully
                specified route string is: [A->Switch1/r0->B] Route specification
                strings can be directly passed to connect, disconnect, or
                connect_and_disconnect Refer to Route Specification Strings in the
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

            path_capability (enums.PathCapability): The return value which expresses the capability of finding a valid route
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

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel1_ctype = ctypes.create_string_buffer(channel1.encode(self._encoding))  # case C020
        channel2_ctype = ctypes.create_string_buffer(channel2.encode(self._encoding))  # case C020
        route_spec_ctype = (_visatype.ViChar * route_spec_size[0])()  # case C080
        route_spec_size_ctype = get_ctypes_pointer_for_buffer(value=route_spec_size, library_type=_visatype.ViInt32)  # case B550
        path_capability_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niSE_FindRoute(vi_ctype, channel1_ctype, channel2_ctype, route_spec_ctype, route_spec_size_ctype, None if path_capability_ctype is None else (ctypes.pointer(path_capability_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return route_spec_ctype.value.decode(self._encoding), enums.PathCapability(path_capability_ctype.value)

    def get_all_connections(self, route_spec_size=[1024]):
        r'''get_all_connections

        Returns the top-level connected routes and route groups. The route
        specification string returned from get_all_connections can be passed
        to other Switch Executive API methods (such as connect,
        disconnect, connect_and_disconnect, and expand_route_spec)
        that use route specification strings.

        Args:
            route_spec_size (list of int): The routeSpecSize is an ViInt32 that is passed by reference into the
                method. As an input, it is the size of the route spec string buffer
                being passed. If the route spec string is larger than the string buffer
                being passed, only the portion of the route spec string that can fit in
                the string buffer is copied into it. On return from the method,
                routeSpecSize holds the size required to hold the entire route spec
                string. Note that this size may be larger than the buffer size as the
                method always returns the size needed to hold the entire buffer. You
                may pass NULL for this parameter if you are not interested in the return
                value for routeSpecSize and routeSpec.


        Returns:
            route_spec (str): The route spec of all currently connected routes and route groups. Route
                specification strings can be directly passed to connect,
                disconnect, connect_and_disconnect, or expand_route_spec
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

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        route_spec_ctype = (_visatype.ViChar * route_spec_size[0])()  # case C080
        route_spec_size_ctype = get_ctypes_pointer_for_buffer(value=route_spec_size, library_type=_visatype.ViInt32)  # case B550
        error_code = self._library.niSE_GetAllConnections(vi_ctype, route_spec_ctype, route_spec_size_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return route_spec_ctype.value.decode(self._encoding)

    def is_connected(self, route_spec):
        r'''is_connected

        Checks whether the specified routes and routes groups are connected. It
        returns true if connected.

        Args:
            route_spec (str): String describing the connections to check. The route specification
                strings are best summarized as a series of routes delimited by
                ampersands. The specified routes may be route names, route group names,
                or fully specified route paths delimited by square brackets. Some
                examples of route specification strings are: MyRoute MyRouteGroup
                MyRoute & MyRouteGroup [A->Switch1/r0->B] MyRoute & MyRouteGroup &
                [A->Switch1/r0->B] Refer to Route Specification Strings in the NI Switch
                Executive Help for more information.


        Returns:
            is_connected (bool): Returns TRUE if the routes and routes groups are connected or FALSE if
                they are not.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        route_spec_ctype = ctypes.create_string_buffer(route_spec.encode(self._encoding))  # case C020
        is_connected_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niSE_IsConnected(vi_ctype, route_spec_ctype, None if is_connected_ctype is None else (ctypes.pointer(is_connected_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(is_connected_ctype.value)

    def is_debounced(self):
        r'''is_debounced

        Checks to see if the switching system is debounced or not. This method
        does not wait for debouncing to occur. It returns true if the system is
        fully debounced. This method is similar to the IviSwtch specific
        method.

        Returns:
            is_debounced (bool): Returns TRUE if the system is fully debounced or FALSE if it is still
                settling.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        is_debounced_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niSE_IsDebounced(vi_ctype, None if is_debounced_ctype is None else (ctypes.pointer(is_debounced_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(is_debounced_ctype.value)

    def _open_session(self, virtual_device_name, option_string=""):
        r'''_open_session

        Opens a session to a specified NI Switch Executive virtual device. Opens
        communications with all of the IVI switches associated with the
        specified NI Switch Executive virtual device. Returns a session handle
        that you use to identify the virtual device in all subsequent NI Switch
        Executive method calls. NI Switch Executive uses a reference counting
        scheme to manage open session handles to an NI Switch Executive virtual
        device. Each call to __init__ must be matched with a subsequent
        call to close. Successive calls to __init__ with
        the same virtual device name always returns the same session handle. NI
        Switch Executive disconnects its communication with the IVI switches
        after all session handles are closed to a given virtual device. The
        session handles may be used safely in multiple threads of an
        application. Sessions may only be opened to a given NI Switch Executive
        virtual device from a single process at a time.

        Args:
            virtual_device_name (str): The name of the NI Switch Executive virtual device.

            option_string (dict): The option string can be used to pass information to each of the IVI
                devices on startup. It can be used to set things such as simulation,
                range checking, etc. Consult your driver documentation for more
                information about valid entries for the option string.


        Returns:
            vi (int): The session referencing this NI Switch Executive virtual device session.

        '''
        virtual_device_name_ctype = ctypes.create_string_buffer(virtual_device_name.encode(self._encoding))  # case C020
        option_string_ctype = ctypes.create_string_buffer(_converters.convert_init_with_options_dictionary(option_string).encode(self._encoding))  # case C040
        vi_ctype = _visatype.ViSession()  # case S220
        error_code = self._library.niSE_OpenSession(virtual_device_name_ctype, option_string_ctype, None if vi_ctype is None else (ctypes.pointer(vi_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(vi_ctype.value)

    def wait_for_debounce(self, maximum_time_ms=hightime.timedelta(milliseconds=-1)):
        r'''wait_for_debounce

        Waits for all of the switches in the NI Switch Executive virtual device
        to debounce. This method does not return until either the switching
        system is completely debounced and settled or the maximum time has
        elapsed and the system is not yet debounced. In the event that the
        maximum time elapses, the method returns an error indicating that a
        timeout has occurred. To ensure that all of the switches have settled,
        NI recommends calling wait_for_debounce after a series of connection
        or disconnection operations and before taking any measurements of the
        signals connected to the switching system.

        Args:
            maximum_time_ms (hightime.timedelta, datetime.timedelta, or int in milliseconds): The amount of time to wait (in milliseconds) for the debounce to
                complete. A value of 0 checks for debouncing once and returns an error
                if the system is not debounced at that time. A value of -1 means to
                block for an infinite period of time until the system is debounced.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        maximum_time_ms_ctype = _converters.convert_timedelta_to_milliseconds_int32(maximum_time_ms)  # case S140
        error_code = self._library.niSE_WaitForDebounce(vi_ctype, maximum_time_ms_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return



