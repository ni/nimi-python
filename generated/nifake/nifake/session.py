# -*- coding: utf-8 -*-
# This file was generated
import array  # noqa: F401
# Used by @ivi_synchronized
from functools import wraps

import nifake._attributes as _attributes
import nifake._converters as _converters
import nifake._library_interpreter as _library_interpreter
import nifake.enums as enums
import nifake.errors as errors

import nifake.custom_struct as custom_struct  # noqa: F401

import nifake.custom_struct_typedef as custom_struct_typedef  # noqa: F401

import nifake.custom_struct_nested_typedef as custom_struct_nested_typedef  # noqa: F401

import hightime
import nitclk

# Used for __repr__
import pprint
pp = pprint.PrettyPrinter(indent=4)


class _Acquisition(object):
    def __init__(self, session):
        self._session = session
        self._session._initiate()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._session.abort()


# From https://stackoverflow.com/questions/5929107/decorators-with-parameters
def ivi_synchronized(f):
    @wraps(f)
    def aux(*xs, **kws):
        session = xs[0]  # parameter 0 is 'self' which is the session object
        with session.lock():
            return f(*xs, **kws)
    return aux


class _Lock(object):
    def __init__(self, session):
        self._session = session

    def __enter__(self):
        # _lock_session is called from the lock() function, not here
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._session.unlock()


class _RepeatedCapabilities(object):
    def __init__(self, session, prefix, current_repeated_capability_list):
        self._session = session
        self._prefix = prefix
        # We need at least one element. If we get an empty list, make the one element an empty string
        self._current_repeated_capability_list = current_repeated_capability_list if len(current_repeated_capability_list) > 0 else ['']
        # Now we know there is at lease one entry, so we look if it is an empty string or not
        self._separator = '/' if len(self._current_repeated_capability_list[0]) > 0 else ''

    def __getitem__(self, repeated_capability):
        '''Set/get properties or call methods with a repeated capability (i.e. channels)'''
        rep_caps_list = _converters.convert_repeated_capabilities(repeated_capability, self._prefix)
        complete_rep_cap_list = [current_rep_cap + self._separator + rep_cap for current_rep_cap in self._current_repeated_capability_list for rep_cap in rep_caps_list]

        return _SessionBase(
            repeated_capability_list=complete_rep_cap_list,
            all_channels_in_session=self._session._all_channels_in_session,
            interpreter=self._session._interpreter,
            freeze_it=True
        )


# This is a very simple context manager we can use when we need to set/get attributes
# or call functions from _SessionBase that require no channels. It is tied to the specific
# implementation of _SessionBase and how repeated capabilities are handled.
class _NoChannel(object):
    def __init__(self, session):
        self._session = session

    def __enter__(self):
        self._repeated_capability_cache = self._session._repeated_capability
        self._session._repeated_capability = ''

    def __exit__(self, exc_type, exc_value, traceback):
        self._session._repeated_capability = self._repeated_capability_cache


class _SessionBase(object):
    '''Base class for all NI-FAKE sessions.'''

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

    float_enum = _attributes.AttributeEnum(_attributes.AttributeViReal64, enums.FloatEnum, 1000005)
    '''Type: enums.FloatEnum

    A property with an enum that is also a float
    '''
    read_write_bool = _attributes.AttributeViBoolean(1000000)
    '''Type: bool

    A property of type bool with read/write access.
    '''
    read_write_color = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.Color, 1000003)
    '''Type: enums.Color

    A property of type Color with read/write access.
    '''
    read_write_double = _attributes.AttributeViReal64(1000001)
    '''Type: float

    A property of type float with read/write access.
    '''
    read_write_double_with_converter = _attributes.AttributeViReal64TimeDeltaSeconds(1000007)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    Property in seconds
    '''
    read_write_double_with_repeated_capability = _attributes.AttributeViReal64(1000009)
    '''Type: float

    Tip:
    This property can be set/get on specific channels within your :py:class:`nifake.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].read_write_double_with_repeated_capability`

    To set/get on all channels, you can call the property directly on the :py:class:`nifake.Session`.

    Example: :py:attr:`my_session.read_write_double_with_repeated_capability`
    '''
    read_write_enum_with_converter = _attributes.AttributeEnumWithConverter(_attributes.AttributeEnum(_attributes.AttributeViInt32, enums.EnumWithConverter, 1000011), _converters.convert_from_enum_with_converter_enum, _converters.convert_to_enum_with_converter_enum)
    read_write_int64 = _attributes.AttributeViInt64(1000006)
    '''Type: int

    A property of type 64-bit integer with read/write access.
    '''
    read_write_integer = _attributes.AttributeViInt32(1000004)
    '''Type: int

    A property of type integer with read/write access.
    '''
    read_write_integer_with_converter = _attributes.AttributeViInt32TimeDeltaMilliseconds(1000008)
    '''Type: hightime.timedelta, datetime.timedelta, or int in milliseconds

    Property in milliseconds
    '''
    read_write_string = _attributes.AttributeViString(1000002)
    '''Type: str

    A property of type string with read/write access.
    '''
    read_write_string_repeated_capability = _attributes.AttributeViStringRepeatedCapability(1000010)
    '''Type: Any repeated capability type, as defined in nimi-python:
        - str
        - str - Comma delimited list
        - str - Range (using '-' or ':')
        - int
        - Basic sequence types (list, tuple, range, slice) of other supported types

    A property with read/write access, that represents a repeated capability

    Tip:
    This property can be set/get on specific instruments within your :py:class:`nifake.Session` instance.
    Use Python index notation on the repeated capabilities container instruments to specify a subset.

    Example: :py:attr:`my_session.instruments[ ... ].read_write_string_repeated_capability`

    To set/get on all instruments, you can call the property directly on the :py:class:`nifake.Session`.

    Example: :py:attr:`my_session.read_write_string_repeated_capability`
    '''
    sample_count = _attributes.AttributeViInt32(1000012)
    sample_interval = _attributes.AttributeViReal64(1000013)

    def __init__(self, repeated_capability_list, all_channels_in_session, interpreter, freeze_it=False):
        self._repeated_capability_list = repeated_capability_list
        self._repeated_capability = ','.join(repeated_capability_list)
        self._all_channels_in_session = all_channels_in_session
        self._interpreter = interpreter

        # Store the parameter list for later printing in __repr__
        param_list = []
        param_list.append("repeated_capability_list=" + pp.pformat(repeated_capability_list))
        param_list.append("interpreter=" + pp.pformat(interpreter))
        self._param_list = ', '.join(param_list)

        # Instantiate any repeated capability objects
        self.channels = _RepeatedCapabilities(self, '', repeated_capability_list)
        self.sites = _RepeatedCapabilities(self, 'site', repeated_capability_list)
        self.instruments = _RepeatedCapabilities(self, '', repeated_capability_list)

        # Finally, set _is_frozen to True which is used to prevent clients from accidentally adding
        # members when trying to set a property with a typo.
        self._is_frozen = freeze_it

    def __repr__(self):
        return '{0}.{1}({2})'.format('nifake', self.__class__.__name__, self._param_list)

    def __setattr__(self, key, value):
        if self._is_frozen and key not in dir(self):
            raise AttributeError("'{0}' object has no attribute '{1}'".format(type(self).__name__, key))
        object.__setattr__(self, key, value)

    ''' These are code-generated '''

    @ivi_synchronized
    def function_with_repeated_capability_type(self):
        r'''function_with_repeated_capability_type

        A method with a parameter that specifies repeated_capability_type.

        Tip:
        This method can be called on specific sites within your :py:class:`nifake.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ].function_with_repeated_capability_type`

        To call the method on all sites, you can call it directly on the :py:class:`nifake.Session`.

        Example: :py:meth:`my_session.function_with_repeated_capability_type`
        '''
        self._interpreter.function_with_repeated_capability_type(self._repeated_capability)

    @ivi_synchronized
    def _get_attribute_vi_boolean(self, attribute_id):
        r'''_get_attribute_vi_boolean

        Queries the value of a ViBoolean property.

        Tip:
        This method can be called on specific channels within your :py:class:`nifake.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_boolean`

        To call the method on all channels, you can call it directly on the :py:class:`nifake.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_boolean`

        Args:
            attribute_id (int): Pass the ID of a property.


        Returns:
            attribute_value (bool): Returns the value of the property.

        '''
        attribute_value = self._interpreter.get_attribute_vi_boolean(self._repeated_capability, attribute_id)
        return attribute_value

    @ivi_synchronized
    def _get_attribute_vi_int32(self, attribute_id):
        r'''_get_attribute_vi_int32

        Queries the value of a ViInt32 property.

        Tip:
        This method can be called on specific channels within your :py:class:`nifake.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_int32`

        To call the method on all channels, you can call it directly on the :py:class:`nifake.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_int32`

        Args:
            attribute_id (int): Pass the ID of a property.


        Returns:
            attribute_value (int): Returns the value of the property.

        '''
        attribute_value = self._interpreter.get_attribute_vi_int32(self._repeated_capability, attribute_id)
        return attribute_value

    @ivi_synchronized
    def _get_attribute_vi_int64(self, attribute_id):
        r'''_get_attribute_vi_int64

        Queries the value of a ViInt64 property.

        Tip:
        This method can be called on specific channels within your :py:class:`nifake.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_int64`

        To call the method on all channels, you can call it directly on the :py:class:`nifake.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_int64`

        Args:
            attribute_id (int): Pass the ID of a property.


        Returns:
            attribute_value (int): Returns the value of the property.

        '''
        attribute_value = self._interpreter.get_attribute_vi_int64(self._repeated_capability, attribute_id)
        return attribute_value

    @ivi_synchronized
    def _get_attribute_vi_real64(self, attribute_id):
        r'''_get_attribute_vi_real64

        Queries the value of a ViReal property.

        Tip:
        This method can be called on specific channels within your :py:class:`nifake.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_real64`

        To call the method on all channels, you can call it directly on the :py:class:`nifake.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_real64`

        Args:
            attribute_id (int): Pass the ID of a property.


        Returns:
            attribute_value (float): Returns the value of the property.

        '''
        attribute_value = self._interpreter.get_attribute_vi_real64(self._repeated_capability, attribute_id)
        return attribute_value

    @ivi_synchronized
    def _get_attribute_vi_string(self, attribute_id):
        r'''_get_attribute_vi_string

        Queries the value of a ViBoolean property.

        Tip:
        This method can be called on specific channels within your :py:class:`nifake.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_string`

        To call the method on all channels, you can call it directly on the :py:class:`nifake.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_string`

        Args:
            attribute_id (int): Pass the ID of a property.


        Returns:
            attribute_value (str): Returns the value of the property.

        '''
        attribute_value = self._interpreter.get_attribute_vi_string(self._repeated_capability, attribute_id)
        return attribute_value

    @ivi_synchronized
    def _get_channel_names(self, indices):
        r'''_get_channel_names

        Returns a list of channel names for the given channel indices.

        Args:
            indices (basic sequence types or str or int): Index list for the channels in the session. Valid values are from zero to the total number of channels in the session minus one. The index string can be one of the following formats:

                -   A comma-separated list—for example, "0,2,3,1"
                -   A range using a hyphen—for example, "0-3"
                -   A range using a colon—for example, "0:3 "

                You can combine comma-separated lists and ranges that use a hyphen or colon. Both out-of-order and repeated indices are supported ("2,3,0," "1,2,2,3"). White space characters, including spaces, tabs, feeds, and carriage returns, are allowed between characters. Ranges can be incrementing or decrementing.


        Returns:
            names (list of str): The channel name(s) at the specified indices.

        '''
        indices = _converters.convert_repeated_capabilities_without_prefix(indices)
        names = self._interpreter.get_channel_names(indices)
        return _converters.convert_comma_separated_string_to_list(names)

    def lock(self):
        '''lock

        Obtains a multithread lock on the device session. Before doing so, the
        software waits until all other execution threads release their locks
        on the device session.

        Other threads may have obtained a lock on this session for the
        following reasons:

            -  The application called the lock method.
            -  A call to NI-FAKE locked the session.
            -  After a call to the lock method returns
               successfully, no other threads can access the device session until
               you call the unlock method or exit out of the with block when using
               lock context manager.
            -  Use the lock method and the
               unlock method around a sequence of calls to
               instrument driver methods if you require that the device retain its
               settings through the end of the sequence.

        You can safely make nested calls to the lock method
        within the same thread. To completely unlock the session, you must
        balance each call to the lock method with a call to
        the unlock method.

        Returns:
            lock (context manager): When used in a with statement, nifake.Session.lock acts as
            a context manager and unlock will be called when the with block is exited
        '''
        self._interpreter.lock()  # We do not call this in the context manager so that this function can
        # act standalone as well and let the client call unlock() explicitly. If they do use the context manager,
        # that will handle the unlock for them
        return _Lock(self)

    @ivi_synchronized
    def get_channel_names(self, indices):
        '''get_channel_names

        Returns a list of channel names for the given channel indices.

        Args:
            indices (basic sequence types or str or int): Index list for the channels in the session. Valid values are from zero to the total number of channels in the session minus one. The index string can be one of the following formats:

                -   A comma-separated list—for example, "0,2,3,1"
                -   A range using a hyphen—for example, "0-3"
                -   A range using a colon—for example, "0:3 "

                You can combine comma-separated lists and ranges that use a hyphen or colon. Both out-of-order and repeated indices are supported ("2,3,0," "1,2,2,3"). White space characters, including spaces, tabs, feeds, and carriage returns, are allowed between characters. Ranges can be incrementing or decrementing.


        Returns:
            names (list of str): The channel name(s) at the specified indices.

        '''
        return self._get_channel_names(indices)

    @ivi_synchronized
    def read_from_channel(self, maximum_time):
        r'''read_from_channel

        Acquires a single measurement and returns the measured value.

        Tip:
        This method can be called on specific channels within your :py:class:`nifake.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].read_from_channel`

        To call the method on all channels, you can call it directly on the :py:class:`nifake.Session`.

        Example: :py:meth:`my_session.read_from_channel`

        Args:
            maximum_time (hightime.timedelta): Specifies the **maximum_time** allowed in milliseconds.


        Returns:
            reading (float): The measured value.

        '''
        maximum_time = _converters.convert_timedelta_to_milliseconds_int32(maximum_time)
        reading = self._interpreter.read_from_channel(self._repeated_capability, maximum_time)
        return reading

    @ivi_synchronized
    def _set_attribute_vi_boolean(self, attribute_id, attribute_value):
        r'''_set_attribute_vi_boolean

        This method sets the value of a ViBoolean property.

        Tip:
        This method can be called on specific channels within your :py:class:`nifake.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_boolean`

        To call the method on all channels, you can call it directly on the :py:class:`nifake.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_boolean`

        Args:
            attribute_id (int): Pass the ID of a property.

            attribute_value (bool): Pass the value that you want to set the property to.

        '''
        self._interpreter.set_attribute_vi_boolean(self._repeated_capability, attribute_id, attribute_value)

    @ivi_synchronized
    def _set_attribute_vi_int32(self, attribute_id, attribute_value):
        r'''_set_attribute_vi_int32

        This method sets the value of a ViInt32 property.

        Tip:
        This method can be called on specific channels within your :py:class:`nifake.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_int32`

        To call the method on all channels, you can call it directly on the :py:class:`nifake.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_int32`

        Args:
            attribute_id (int): Pass the ID of a property.

            attribute_value (int): Pass the value that you want to set the property to.

        '''
        self._interpreter.set_attribute_vi_int32(self._repeated_capability, attribute_id, attribute_value)

    @ivi_synchronized
    def _set_attribute_vi_int64(self, attribute_id, attribute_value):
        r'''_set_attribute_vi_int64

        This method sets the value of a ViInt64 property.

        Tip:
        This method can be called on specific channels within your :py:class:`nifake.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_int64`

        To call the method on all channels, you can call it directly on the :py:class:`nifake.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_int64`

        Args:
            attribute_id (int): Pass the ID of a property.

            attribute_value (int): Pass the value that you want to set the property to.

        '''
        self._interpreter.set_attribute_vi_int64(self._repeated_capability, attribute_id, attribute_value)

    @ivi_synchronized
    def _set_attribute_vi_real64(self, attribute_id, attribute_value):
        r'''_set_attribute_vi_real64

        This method sets the value of a ViReal64 property.

        Tip:
        This method can be called on specific channels within your :py:class:`nifake.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_real64`

        To call the method on all channels, you can call it directly on the :py:class:`nifake.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_real64`

        Args:
            attribute_id (int): Pass the ID of a property.

            attribute_value (float): Pass the value that you want to set the property to.

        '''
        self._interpreter.set_attribute_vi_real64(self._repeated_capability, attribute_id, attribute_value)

    @ivi_synchronized
    def _set_attribute_vi_string(self, attribute_id, attribute_value):
        r'''_set_attribute_vi_string

        This method sets the value of a ViString property.

        Tip:
        This method can be called on specific channels within your :py:class:`nifake.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_string`

        To call the method on all channels, you can call it directly on the :py:class:`nifake.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_string`

        Args:
            attribute_id (int): Pass the ID of a property.

            attribute_value (str): Pass the value that you want to set the property to.

        '''
        self._interpreter.set_attribute_vi_string(self._repeated_capability, attribute_id, attribute_value)

    def unlock(self):
        '''unlock

        Releases a lock that you acquired on an device session using
        lock. Refer to lock for additional
        information on session locks.
        '''
        self._interpreter.unlock()

    def _error_message(self, error_code):
        r'''_error_message

        Takes the errorCode returned by a functiona and returns it as a user-readable string.

        Args:
            error_code (int): The errorCode returned from the instrument.


        Returns:
            error_message (str): The error information formatted into a string.

        '''
        error_message = self._interpreter.error_message(error_code)
        return error_message


class Session(_SessionBase):
    '''An NI-FAKE session to a fake MI driver whose sole purpose is to test nimi-python code generation'''

    def __init__(self, resource_name, options={}, id_query=False, reset_device=False, *, grpc_options=None):
        r'''An NI-FAKE session to a fake MI driver whose sole purpose is to test nimi-python code generation

        Creates a new IVI instrument driver session.

        Args:
            resource_name (str): Caution: This is just some string.

                Contains the **resource_name** of the device to initialize.

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

            id_query (bool): NI-FAKE is probably not needed.

                +----------------+---+------------------+
                | True (default) | 1 | Perform ID Query |
                +----------------+---+------------------+
                | False          | 0 | Skip ID Query    |
                +----------------+---+------------------+

            reset_device (bool): Specifies whether to reset

                +----------------+---+--------------+
                | True (default) | 1 | Reset Device |
                +----------------+---+--------------+
                | False          | 0 | Don't Reset  |
                +----------------+---+--------------+

            grpc_options (nifake.grpc_session_options.GrpcSessionOptions): MeasurementLink gRPC session options


        Returns:
            session (nifake.Session): A session object representing the device.

        '''
        if grpc_options:
            import nifake._grpc_stub_interpreter as _grpc_stub_interpreter
            interpreter = _grpc_stub_interpreter.GrpcStubInterpreter(grpc_options)
        else:
            interpreter = _library_interpreter.LibraryInterpreter(encoding='windows-1251')

        # Initialize the superclass with default values first, populate them later
        super(Session, self).__init__(
            repeated_capability_list=[],
            interpreter=interpreter,
            freeze_it=False,
            all_channels_in_session=None
        )
        options = _converters.convert_init_with_options_dictionary(options)

        # Call specified init function
        # Note that _interpreter default-initializes the session handle in its constructor, so that
        # if _init_with_options fails, the error handler can reference it.
        # And then here, once _init_with_options succeeds, we call set_session_handle
        # with the actual session handle.
        self._interpreter.set_session_handle(self._init_with_options(resource_name, options, id_query, reset_device))

        # NI-TClk does not work over NI gRPC Device Server
        if not grpc_options:
            self.tclk = nitclk.SessionReference(self._interpreter.get_session_handle())

        # Store the parameter list for later printing in __repr__
        param_list = []
        param_list.append("resource_name=" + pp.pformat(resource_name))
        param_list.append("options=" + pp.pformat(options))
        param_list.append("reset_device=" + pp.pformat(reset_device))
        self._param_list = ', '.join(param_list)

        # Store the list of channels in the Session which is needed by some nimi-python modules.
        # Use try/except because not all the modules support channels.
        # self.get_channel_names() and self.channel_count can only be called after the session
        # handle is set
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
        if self._interpreter._close_on_exit:
            self.close()

    def initiate(self):
        '''initiate

        Initiates a thingie.

        Note:
        This method will return a Python context manager that will initiate on entering and abort on exit.
        '''
        return _Acquisition(self)

    def close(self):
        '''close

        Closes the specified session and deallocates resources that it reserved.

        Note:
        This method is not needed when using the session context manager
        '''
        try:
            self._close()
        except errors.DriverError:
            self._interpreter.set_session_handle()
            raise
        self._interpreter.set_session_handle()

    ''' These are code-generated '''

    @ivi_synchronized
    def abort(self):
        r'''abort

        Aborts a previously initiated thingie.
        '''
        self._interpreter.abort()

    @ivi_synchronized
    def accept_list_of_durations_in_seconds(self, delays):
        r'''accept_list_of_durations_in_seconds

        Accepts list of hightime.timedelta or datetime.timedelta or float instances representing time delays.

        Args:
            delays (hightime.timedelta, datetime.timedelta, or float in seconds): A collection of time delay values.

        '''
        delays = _converters.convert_timedeltas_to_seconds_real64(delays)
        self._interpreter.accept_list_of_durations_in_seconds(delays)

    @ivi_synchronized
    def bool_array_output_function(self, number_of_elements):
        r'''bool_array_output_function

        This method returns an array of booleans.

        Args:
            number_of_elements (int): Number of elements in the array.


        Returns:
            an_array (list of bool): Contains an array of booleans

        '''
        an_array = self._interpreter.bool_array_output_function(number_of_elements)
        return an_array

    @ivi_synchronized
    def configure_abc(self):
        r'''configure_abc

        TBD
        '''
        self._interpreter.configure_abc()

    @ivi_synchronized
    def custom_nested_struct_roundtrip(self, nested_custom_type_in):
        r'''custom_nested_struct_roundtrip

        TBD

        Args:
            nested_custom_type_in (CustomStructNestedTypedef):


        Returns:
            nested_custom_type_out (CustomStructNestedTypedef):

        '''
        nested_custom_type_out = self._interpreter.custom_nested_struct_roundtrip(nested_custom_type_in)
        return nested_custom_type_out

    @ivi_synchronized
    def double_all_the_nums(self, numbers):
        r'''double_all_the_nums

        Test for buffer with converter

        Args:
            numbers (list of float): numbers is an array of numbers we want to double.

        '''
        numbers = _converters.convert_double_each_element(numbers)
        self._interpreter.double_all_the_nums(numbers)

    @ivi_synchronized
    def enum_array_output_function(self, number_of_elements):
        r'''enum_array_output_function

        This method returns an array of enums, stored as 16 bit integers under the hood.

        Args:
            number_of_elements (int): Number of elements in the array.


        Returns:
            an_array (list of enums.Turtle): Contains an array of enums, stored as 16 bit integers under the hood

        '''
        an_array = self._interpreter.enum_array_output_function(number_of_elements)
        return an_array

    @ivi_synchronized
    def enum_input_function_with_defaults(self, a_turtle=enums.Turtle.LEONARDO):
        r'''enum_input_function_with_defaults

        This method takes one parameter other than the session, which happens to be an enum and has a default value.

        Args:
            a_turtle (enums.Turtle): Indicates a ninja turtle

                +---+---------------+
                | 0 | Leonardo      |
                +---+---------------+
                | 1 | Donatello     |
                +---+---------------+
                | 2 | Raphael       |
                +---+---------------+
                | 3 | Mich elangelo |
                +---+---------------+

        '''
        if type(a_turtle) is not enums.Turtle:
            raise TypeError('Parameter a_turtle must be of type ' + str(enums.Turtle))
        self._interpreter.enum_input_function_with_defaults(a_turtle)

    @ivi_synchronized
    def export_attribute_configuration_buffer(self):
        r'''export_attribute_configuration_buffer

        Export configuration buffer.

        Returns:
            configuration (bytes):

        '''
        configuration = self._interpreter.export_attribute_configuration_buffer()
        return _converters.convert_to_bytes(configuration)

    @ivi_synchronized
    def fetch_waveform(self, number_of_samples):
        r'''fetch_waveform

        Returns waveform data.

        Args:
            number_of_samples (int): Number of samples to return


        Returns:
            waveform_data (array.array("d")): Samples fetched from the device. Array should be numberOfSamples big.

        '''
        waveform_data = self._interpreter.fetch_waveform(number_of_samples)
        return waveform_data

    @ivi_synchronized
    def fetch_waveform_into(self, waveform_data):
        r'''fetch_waveform_into

        Returns waveform data.

        Args:
            waveform_data (numpy.array(dtype=numpy.float64)): Samples fetched from the device. Array should be numberOfSamples big.

        '''
        import numpy

        if type(waveform_data) is not numpy.ndarray:
            raise TypeError('waveform_data must be {0}, is {1}'.format(numpy.ndarray, type(waveform_data)))
        if numpy.isfortran(waveform_data) is True:
            raise TypeError('waveform_data must be in C-order')
        if waveform_data.dtype is not numpy.dtype('float64'):
            raise TypeError('waveform_data must be numpy.ndarray of dtype=float64, is ' + str(waveform_data.dtype))
        self._interpreter.fetch_waveform_into(waveform_data)

    @ivi_synchronized
    def get_a_boolean(self):
        r'''get_a_boolean

        Returns a boolean.

        Note: This method rules!

        Returns:
            a_boolean (bool): Contains a boolean.

        '''
        a_boolean = self._interpreter.get_a_boolean()
        return a_boolean

    @ivi_synchronized
    def get_a_number(self):
        r'''get_a_number

        Returns a number.

        Note: This method rules!

        Returns:
            a_number (int): Contains a number.

        '''
        a_number = self._interpreter.get_a_number()
        return a_number

    @ivi_synchronized
    def get_a_string_of_fixed_maximum_size(self):
        r'''get_a_string_of_fixed_maximum_size

        Illustrates returning a string of fixed size.

        Returns:
            a_string (str): String comes back here. Buffer must be 256 big.

        '''
        a_string = self._interpreter.get_a_string_of_fixed_maximum_size()
        return a_string

    @ivi_synchronized
    def get_a_string_using_python_code(self, a_number):
        r'''get_a_string_using_python_code

        Returns a number and a string.

        Note: This method rules!

        Args:
            a_number (int): Contains a number.


        Returns:
            a_string (str): Contains a string of length aNumber.

        '''
        a_string = self._interpreter.get_a_string_using_python_code(a_number)
        return a_string

    @ivi_synchronized
    def get_an_ivi_dance_char_array(self):
        r'''get_an_ivi_dance_char_array

        TBD

        Returns:
            char_array (str):

        '''
        char_array = self._interpreter.get_an_ivi_dance_char_array()
        return char_array

    @ivi_synchronized
    def get_an_ivi_dance_with_a_twist_string(self):
        r'''get_an_ivi_dance_with_a_twist_string

        TBD

        Returns:
            a_string (str):

        '''
        a_string = self._interpreter.get_an_ivi_dance_with_a_twist_string()
        return a_string

    @ivi_synchronized
    def get_array_for_python_code_custom_type(self):
        r'''get_array_for_python_code_custom_type

        This method returns an array for use in python-code size mechanism.

        Returns:
            array_out (list of CustomStruct): Array of custom type using python-code size mechanism

        '''
        array_out = self._interpreter.get_array_for_python_code_custom_type()
        return array_out

    @ivi_synchronized
    def get_array_for_python_code_double(self):
        r'''get_array_for_python_code_double

        This method returns an array for use in python-code size mechanism.

        Returns:
            array_out (list of float): Array of double using python-code size mechanism

        '''
        array_out = self._interpreter.get_array_for_python_code_double()
        return array_out

    @ivi_synchronized
    def get_array_size_for_python_code(self):
        r'''get_array_size_for_python_code

        This method returns the size of the array for use in python-code size mechanism.

        Returns:
            size_out (int): Size of array

        '''
        size_out = self._interpreter.get_array_size_for_python_code()
        return size_out

    @ivi_synchronized
    def get_array_using_ivi_dance(self):
        r'''get_array_using_ivi_dance

        This method returns an array of float whose size is determined with the IVI dance.

        Returns:
            array_out (list of float): The array returned by this method

        '''
        array_out = self._interpreter.get_array_using_ivi_dance()
        return array_out

    @ivi_synchronized
    def _get_cal_date_and_time(self, cal_type):
        r'''_get_cal_date_and_time

        Returns the date and time of the last calibration performed.

        Args:
            cal_type (int): Specifies the type of calibration performed (external or self-calibration).


        Returns:
            month (int): Indicates the **month** of the last calibration.

            day (int): Indicates the **day** of the last calibration.

            year (int): Indicates the **year** of the last calibration.

            hour (int): Indicates the **hour** of the last calibration.

            minute (int): Indicates the **minute** of the last calibration.

        '''
        month, day, year, hour, minute = self._interpreter.get_cal_date_and_time(cal_type)
        return month, day, year, hour, minute

    @ivi_synchronized
    def get_cal_interval(self):
        r'''get_cal_interval

        Returns the recommended maximum interval, in **months**, between external calibrations.

        Returns:
            months (hightime.timedelta): Specifies the recommended maximum interval, in **months**, between external calibrations.

        '''
        months = self._interpreter.get_cal_interval()
        return _converters.convert_month_to_timedelta(months)

    @ivi_synchronized
    def get_custom_type(self):
        r'''get_custom_type

        This method returns a custom type.

        Returns:
            cs (CustomStruct): Set using custom type

        '''
        cs = self._interpreter.get_custom_type()
        return cs

    @ivi_synchronized
    def get_custom_type_array(self, number_of_elements):
        r'''get_custom_type_array

        This method returns a custom type.

        Args:
            number_of_elements (int): Number of elements in the array.


        Returns:
            cs (list of CustomStruct): Get using custom type

        '''
        cs = self._interpreter.get_custom_type_array(number_of_elements)
        return cs

    @ivi_synchronized
    def get_custom_type_typedef(self):
        r'''get_custom_type_typedef

        This method returns a custom type with typedef and a custom type with nested typedef.

        Returns:
            cst (CustomStructTypedef): An object of a custom type with typedef

            csnt (CustomStructNestedTypedef): An object of a custom type with nested typedef

        '''
        cst, csnt = self._interpreter.get_custom_type_typedef()
        return cst, csnt

    @ivi_synchronized
    def get_enum_value(self):
        r'''get_enum_value

        Returns an enum value

        Note: Splinter is not supported.

        Returns:
            a_quantity (int): This is an amount.

                Note: The amount will be between -2^31 and (2^31-1)

            a_turtle (enums.Turtle): Indicates a ninja turtle

                +---+---------------+
                | 0 | Leonardo      |
                +---+---------------+
                | 1 | Donatello     |
                +---+---------------+
                | 2 | Raphael       |
                +---+---------------+
                | 3 | Mich elangelo |
                +---+---------------+

        '''
        a_quantity, a_turtle = self._interpreter.get_enum_value()
        return a_quantity, a_turtle

    @ivi_synchronized
    def get_cal_date_and_time(self, cal_type):
        '''get_cal_date_and_time

        Returns the date and time of the last calibration performed.

        Args:
            cal_type (int): Specifies the type of calibration performed (external or self-calibration).


        Returns:
            last_cal_datetime (hightime.datetime): Indicates date and time of the last calibration.

        '''
        month, day, year, hour, minute = self._get_cal_date_and_time(cal_type)
        return hightime.datetime(year, month, day, hour, minute)

    @ivi_synchronized
    def get_parameter_with_overridden_grpc_name(self, enum_parameter):
        r'''get_parameter_with_overridden_grpc_name

        TBD

        Args:
            enum_parameter (enums.Turtle):


        Returns:
            original_parameter (int):

        '''
        if type(enum_parameter) is not enums.Turtle:
            raise TypeError('Parameter enum_parameter must be of type ' + str(enums.Turtle))
        original_parameter = self._interpreter.get_parameter_with_overridden_grpc_name(enum_parameter)
        return original_parameter

    @ivi_synchronized
    def import_attribute_configuration_buffer(self, configuration):
        r'''import_attribute_configuration_buffer

        Import configuration buffer.

        Args:
            configuration (bytes):

        '''
        configuration = _converters.convert_to_bytes(configuration)
        self._interpreter.import_attribute_configuration_buffer(configuration)

    @ivi_synchronized
    def import_attribute_configuration_buffer_ex(self, configuration):
        r'''import_attribute_configuration_buffer_ex

        TBD

        Args:
            configuration (list of ViAddr):

        '''
        self._interpreter.import_attribute_configuration_buffer_ex(configuration)

    def _init_with_options(self, resource_name, option_string, id_query=False, reset_device=False):
        r'''_init_with_options

        Creates a new IVI instrument driver session.

        Args:
            resource_name (str): Caution: This is just some string.

                Contains the **resource_name** of the device to initialize.

            option_string (dict): Some options

            id_query (bool): NI-FAKE is probably not needed.

                +----------------+---+------------------+
                | True (default) | 1 | Perform ID Query |
                +----------------+---+------------------+
                | False          | 0 | Skip ID Query    |
                +----------------+---+------------------+

            reset_device (bool): Specifies whether to reset

                +----------------+---+--------------+
                | True (default) | 1 | Reset Device |
                +----------------+---+--------------+
                | False          | 0 | Don't Reset  |
                +----------------+---+--------------+


        Returns:
            vi (int): Returns a ViSession handle that you use.

        '''
        option_string = _converters.convert_init_with_options_dictionary(option_string)
        vi = self._interpreter.init_with_options(resource_name, id_query, reset_device, option_string)
        return vi

    @ivi_synchronized
    def _initiate(self):
        r'''_initiate

        Initiates a thingie.
        '''
        self._interpreter.initiate()

    @ivi_synchronized
    def method_using_whole_and_fractional_numbers(self):
        r'''method_using_whole_and_fractional_numbers

        TBD

        Returns:
            whole_number (int):

            fractional_number (float):

        '''
        whole_number, fractional_number = self._interpreter.method_using_whole_and_fractional_numbers()
        return whole_number, fractional_number

    @ivi_synchronized
    def method_with_grpc_only_param(self, simple_param):
        r'''method_with_grpc_only_param

        TBD

        Args:
            simple_param (int):

        '''
        self._interpreter.method_with_grpc_only_param(simple_param)

    @ivi_synchronized
    def method_with_proto_only_parameter(self, attribute_value):
        r'''method_with_proto_only_parameter

        TBD

        Args:
            attribute_value (int):

        '''
        self._interpreter.method_with_proto_only_parameter(attribute_value)

    @ivi_synchronized
    def multiple_array_types(self, output_array_size, input_array_of_floats, input_array_of_integers=None):
        r'''multiple_array_types

        Receives and returns multiple types of arrays.

        Args:
            output_array_size (int): Size of the array that will be returned.

            input_array_of_floats (list of float): Array of floats

            input_array_of_integers (list of int): Array of integers. Optional. If passed in then size must match that of inputArrayOfFloats.


        Returns:
            output_array (list of float): Array that will be returned.

                Note: The size must be at least outputArraySize.

            output_array_of_fixed_length (list of float): An array of doubles with fixed size.

        '''
        if input_array_of_integers is not None and len(input_array_of_integers) != len(input_array_of_floats):  # case S160
            raise ValueError("Length of input_array_of_integers and input_array_of_floats parameters do not match.")  # case S160
        output_array, output_array_of_fixed_length = self._interpreter.multiple_array_types(output_array_size, input_array_of_floats, input_array_of_integers)
        return output_array, output_array_of_fixed_length

    @ivi_synchronized
    def multiple_arrays_same_size(self, values1, values2, values3, values4):
        r'''multiple_arrays_same_size

        Method to test multiple arrays that use the same size

        Args:
            values1 (list of float): Array 1 of same size.

            values2 (list of float): Array 2 of same size.

            values3 (list of float): Array 3 of same size.

            values4 (list of float): Array 4 of same size.

        '''
        if values2 is not None and len(values2) != len(values1):  # case S160
            raise ValueError("Length of values2 and values1 parameters do not match.")  # case S160
        if values3 is not None and len(values3) != len(values1):  # case S160
            raise ValueError("Length of values3 and values1 parameters do not match.")  # case S160
        if values4 is not None and len(values4) != len(values1):  # case S160
            raise ValueError("Length of values4 and values1 parameters do not match.")  # case S160
        self._interpreter.multiple_arrays_same_size(values1, values2, values3, values4)

    @ivi_synchronized
    def one_input_function(self, a_number):
        r'''one_input_function

        This method takes one parameter other than the session.

        Args:
            a_number (int): Contains a number

        '''
        self._interpreter.one_input_function(a_number)

    @ivi_synchronized
    def parameters_are_multiple_types(self, a_boolean, an_int32, an_int64, an_int_enum, a_float, a_float_enum, a_string):
        r'''parameters_are_multiple_types

        Has parameters of multiple types.

        Args:
            a_boolean (bool): Contains a boolean.

            an_int32 (int): Contains a 32-bit integer.

            an_int64 (int): Contains a 64-bit integer.

            an_int_enum (enums.Turtle): Indicates a ninja turtle

                +---+---------------+
                | 0 | Leonardo      |
                +---+---------------+
                | 1 | Donatello     |
                +---+---------------+
                | 2 | Raphael       |
                +---+---------------+
                | 3 | Mich elangelo |
                +---+---------------+

            a_float (float): The measured value.

            a_float_enum (enums.FloatEnum): A float enum.

            a_string (str): An IVI dance string.

        '''
        if type(an_int_enum) is not enums.Turtle:
            raise TypeError('Parameter an_int_enum must be of type ' + str(enums.Turtle))
        if type(a_float_enum) is not enums.FloatEnum:
            raise TypeError('Parameter a_float_enum must be of type ' + str(enums.FloatEnum))
        self._interpreter.parameters_are_multiple_types(a_boolean, an_int32, an_int64, an_int_enum, a_float, a_float_enum, a_string)

    @ivi_synchronized
    def simple_function(self):
        r'''simple_function

        This method takes no parameters other than the session.
        '''
        self._interpreter.simple_function()

    @ivi_synchronized
    def read(self, maximum_time):
        r'''read

        Acquires a single measurement and returns the measured value.

        Args:
            maximum_time (hightime.timedelta): Specifies the **maximum_time** allowed in seconds.


        Returns:
            reading (float): The measured value.

        '''
        maximum_time = _converters.convert_timedelta_to_seconds_real64(maximum_time)
        reading = self._interpreter.read(maximum_time)
        return reading

    @ivi_synchronized
    def return_a_number_and_a_string(self):
        r'''return_a_number_and_a_string

        Returns a number and a string.

        Note: This method rules!

        Returns:
            a_number (int): Contains a number.

            a_string (str): Contains a string. Buffer must be 256 bytes or larger.

        '''
        a_number, a_string = self._interpreter.return_a_number_and_a_string()
        return a_number, a_string

    @ivi_synchronized
    def return_duration_in_seconds(self):
        r'''return_duration_in_seconds

        Returns a hightime.timedelta instance.

        Returns:
            timedelta (hightime.timedelta): Duration in seconds.

        '''
        timedelta = self._interpreter.return_duration_in_seconds()
        return _converters.convert_seconds_real64_to_timedelta(timedelta)

    @ivi_synchronized
    def return_list_of_durations_in_seconds(self, number_of_elements):
        r'''return_list_of_durations_in_seconds

        Returns a list of hightime.timedelta instances.

        Args:
            number_of_elements (int): Number of elements in output.


        Returns:
            timedeltas (hightime.timedelta): Contains a list of hightime.timedelta instances.

        '''
        timedeltas = self._interpreter.return_list_of_durations_in_seconds(number_of_elements)
        return _converters.convert_seconds_real64_to_timedeltas(timedeltas)

    @ivi_synchronized
    def return_multiple_types(self, array_size):
        r'''return_multiple_types

        Returns multiple types.

        Args:
            array_size (int): Number of measurements to acquire.


        Returns:
            a_boolean (bool): Contains a boolean.

            an_int32 (int): Contains a 32-bit integer.

            an_int64 (int): Contains a 64-bit integer.

            an_int_enum (enums.Turtle): Indicates a ninja turtle

                +---+---------------+
                | 0 | Leonardo      |
                +---+---------------+
                | 1 | Donatello     |
                +---+---------------+
                | 2 | Raphael       |
                +---+---------------+
                | 3 | Mich elangelo |
                +---+---------------+

            a_float (float): The measured value.

            a_float_enum (enums.FloatEnum): A float enum.

            an_array (list of float): An array of measurement values.

                Note: The size must be at least arraySize.

            a_string (str): An IVI dance string.

        '''
        a_boolean, an_int32, an_int64, an_int_enum, a_float, a_float_enum, an_array, a_string = self._interpreter.return_multiple_types(array_size)
        return a_boolean, an_int32, an_int64, an_int_enum, a_float, a_float_enum, an_array, a_string

    @ivi_synchronized
    def set_custom_type(self, cs):
        r'''set_custom_type

        This method takes a custom type.

        Args:
            cs (CustomStruct): Set using custom type

        '''
        self._interpreter.set_custom_type(cs)

    @ivi_synchronized
    def set_custom_type_array(self, cs):
        r'''set_custom_type_array

        This method takes an array of custom types.

        Args:
            cs (list of CustomStruct): Set using custom type

        '''
        self._interpreter.set_custom_type_array(cs)

    @ivi_synchronized
    def string_valued_enum_input_function_with_defaults(self, a_mobile_os_name=enums.MobileOSNames.ANDROID):
        r'''string_valued_enum_input_function_with_defaults

        This method takes one parameter other than the session, which happens to be a string-valued enum and has a default value.

        Args:
            a_mobile_os_name (enums.MobileOSNames): Indicates a Mobile OS

                +---------+---------+
                | ANDROID | Android |
                +---------+---------+
                | IOS     | iOS     |
                +---------+---------+
                | NONE    | None    |
                +---------+---------+

        '''
        if type(a_mobile_os_name) is not enums.MobileOSNames:
            raise TypeError('Parameter a_mobile_os_name must be of type ' + str(enums.MobileOSNames))
        self._interpreter.string_valued_enum_input_function_with_defaults(a_mobile_os_name)

    @ivi_synchronized
    def two_input_function(self, a_number, a_string):
        r'''two_input_function

        This method takes two parameters other than the session.

        Args:
            a_number (float): Contains a number

            a_string (str): Contains a string

        '''
        self._interpreter.two_input_function(a_number, a_string)

    @ivi_synchronized
    def use64_bit_number(self, input):
        r'''use64_bit_number

        Returns a number and a string.

        Note: This method rules!

        Args:
            input (int): A big number on its way in.


        Returns:
            output (int): A big number on its way out.

        '''
        output = self._interpreter.use64_bit_number(input)
        return output

    @ivi_synchronized
    def write_waveform(self, waveform):
        r'''write_waveform

        Writes waveform to the driver

        Args:
            waveform (array.array("d")): Waveform data.

        '''
        self._interpreter.write_waveform(waveform)

    @ivi_synchronized
    def write_waveform_numpy(self, waveform):
        r'''write_waveform_numpy

        Writes waveform to the driver

        Args:
            waveform (numpy.array(dtype=numpy.float64)): Waveform data.

        '''
        import numpy

        if type(waveform) is not numpy.ndarray:
            raise TypeError('waveform must be {0}, is {1}'.format(numpy.ndarray, type(waveform)))
        if numpy.isfortran(waveform) is True:
            raise TypeError('waveform must be in C-order')
        if waveform.dtype is not numpy.dtype('float64'):
            raise TypeError('waveform must be numpy.ndarray of dtype=float64, is ' + str(waveform.dtype))
        self._interpreter.write_waveform_numpy(waveform)

    def _close(self):
        r'''_close

        Closes the specified session and deallocates resources that it reserved.
        '''
        self._interpreter.close()

    @ivi_synchronized
    def self_test(self):
        '''self_test

        Performs a self-test
        '''
        code, msg = self._self_test()
        if code:
            raise errors.SelfTestError(code, msg)
        return None

    @ivi_synchronized
    def _self_test(self):
        r'''_self_test

        Performs a self-test.

        Returns:
            self_test_result (int): Contains the value returned from the instrument self-test. Zero indicates success.

            self_test_message (str): This parameter contains the string returned from the instrument self-test. The array must contain at least 256 elements.

        '''
        self_test_result, self_test_message = self._interpreter.self_test()
        return self_test_result, self_test_message
