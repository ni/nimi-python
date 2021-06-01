# -*- coding: utf-8 -*-
# This file was generated
import array  # noqa: F401
import ctypes
# Used by @ivi_synchronized
from functools import wraps

import nifake._attributes as _attributes
import nifake._converters as _converters
import nifake._library_singleton as _library_singleton
import nifake._visatype as _visatype
import nifake.enums as enums
import nifake.errors as errors

import nifake.custom_struct as custom_struct  # noqa: F401

import hightime
import nitclk

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

        return _SessionBase(vi=self._session._vi, repeated_capability_list=complete_rep_cap_list, library=self._session._library, encoding=self._session._encoding, freeze_it=True)


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
    '''

    def __init__(self, repeated_capability_list, vi, library, encoding, freeze_it=False):
        self._repeated_capability_list = repeated_capability_list
        self._repeated_capability = ','.join(repeated_capability_list)
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

        # Instantiate any repeated capability objects
        self.channels = _RepeatedCapabilities(self, '', repeated_capability_list)
        self.sites = _RepeatedCapabilities(self, 'site', repeated_capability_list)
        self.instruments = _RepeatedCapabilities(self, '', repeated_capability_list)

        self._is_frozen = freeze_it

    def __repr__(self):
        return '{0}.{1}({2})'.format('nifake', self.__class__.__name__, self._param_list)

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

    @ivi_synchronized
    def _get_attribute_vi_boolean(self, attribute_id):
        r'''_get_attribute_vi_boolean

        Queries the value of a ViBoolean property.

        Tip:
        This method can be called for specific channels within your :py:class:`nifake.Session` object.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_boolean`

        To call the method for all channels, you can call it directly on the :py:class:`nifake.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_boolean`

        Args:
            attribute_id (int): Pass the ID of a property.


        Returns:
            attribute_value (bool): Returns the value of the property.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niFake_GetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(attribute_value_ctype.value)

    @ivi_synchronized
    def _get_attribute_vi_int32(self, attribute_id):
        r'''_get_attribute_vi_int32

        Queries the value of a ViInt32 property.

        Tip:
        This method can be called for specific channels within your :py:class:`nifake.Session` object.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_int32`

        To call the method for all channels, you can call it directly on the :py:class:`nifake.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_int32`

        Args:
            attribute_id (int): Pass the ID of a property.


        Returns:
            attribute_value (int): Returns the value of the property.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFake_GetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(attribute_value_ctype.value)

    @ivi_synchronized
    def _get_attribute_vi_int64(self, attribute_id):
        r'''_get_attribute_vi_int64

        Queries the value of a ViInt64 property.

        Tip:
        This method can be called for specific channels within your :py:class:`nifake.Session` object.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_int64`

        To call the method for all channels, you can call it directly on the :py:class:`nifake.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_int64`

        Args:
            attribute_id (int): Pass the ID of a property.


        Returns:
            attribute_value (int): Returns the value of the property.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt64()  # case S220
        error_code = self._library.niFake_GetAttributeViInt64(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(attribute_value_ctype.value)

    @ivi_synchronized
    def _get_attribute_vi_real64(self, attribute_id):
        r'''_get_attribute_vi_real64

        Queries the value of a ViReal property.

        Tip:
        This method can be called for specific channels within your :py:class:`nifake.Session` object.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_real64`

        To call the method for all channels, you can call it directly on the :py:class:`nifake.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_real64`

        Args:
            attribute_id (int): Pass the ID of a property.


        Returns:
            attribute_value (float): Returns the value of the property.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niFake_GetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(attribute_value_ctype.value)

    @ivi_synchronized
    def _get_attribute_vi_string(self, attribute_id):
        r'''_get_attribute_vi_string

        Queries the value of a ViBoolean property.

        Tip:
        This method can be called for specific channels within your :py:class:`nifake.Session` object.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_string`

        To call the method for all channels, you can call it directly on the :py:class:`nifake.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_string`

        Args:
            attribute_id (int): Pass the ID of a property.


        Returns:
            attribute_value (str): Returns the value of the property.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        attribute_value_ctype = None  # case C050
        error_code = self._library.niFake_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, buffer_size_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        attribute_value_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niFake_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, buffer_size_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return attribute_value_ctype.value.decode(self._encoding)

    def _get_error(self):
        r'''_get_error

        Returns the error information associated with the session.

        Returns:
            error_code (int): Returns errorCode for the session. If you pass 0 for bufferSize, you can pass VI_NULL for this.

            description (str): At least bufferSize big, string comes out here.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code_ctype = _visatype.ViStatus()  # case S220
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        description_ctype = None  # case C050
        error_code = self._library.niFake_GetError(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), buffer_size_ctype, description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=True)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        description_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niFake_GetError(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), buffer_size_ctype, description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return int(error_code_ctype.value), description_ctype.value.decode(self._encoding)

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
        self._lock_session()  # We do not call _lock_session() in the context manager so that this function can
        # act standalone as well and let the client call unlock() explicitly. If they do use the context manager,
        # that will handle the unlock for them
        return _Lock(self)

    def _lock_session(self):
        '''_lock_session

        Actual call to driver
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFake_LockSession(vi_ctype, None)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return

    @ivi_synchronized
    def read_from_channel(self, maximum_time):
        r'''read_from_channel

        Acquires a single measurement and returns the measured value.

        Tip:
        This method can be called for specific channels within your :py:class:`nifake.Session` object.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].read_from_channel`

        To call the method for all channels, you can call it directly on the :py:class:`nifake.Session`.

        Example: :py:meth:`my_session.read_from_channel`

        Args:
            maximum_time (hightime.timedelta): Specifies the **maximum_time** allowed in milliseconds.


        Returns:
            reading (float): The measured value.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        maximum_time_ctype = _converters.convert_timedelta_to_milliseconds_int32(maximum_time)  # case S140
        reading_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niFake_ReadFromChannel(vi_ctype, channel_name_ctype, maximum_time_ctype, None if reading_ctype is None else (ctypes.pointer(reading_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(reading_ctype.value)

    @ivi_synchronized
    def _set_attribute_vi_boolean(self, attribute_id, attribute_value):
        r'''_set_attribute_vi_boolean

        This method sets the value of a ViBoolean property.

        Tip:
        This method can be called for specific channels within your :py:class:`nifake.Session` object.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_boolean`

        To call the method for all channels, you can call it directly on the :py:class:`nifake.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_boolean`

        Args:
            attribute_id (int): Pass the ID of a property.

            attribute_value (bool): Pass the value that you want to set the property to.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViBoolean(attribute_value)  # case S150
        error_code = self._library.niFake_SetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def _set_attribute_vi_int32(self, attribute_id, attribute_value):
        r'''_set_attribute_vi_int32

        This method sets the value of a ViInt32 property.

        Tip:
        This method can be called for specific channels within your :py:class:`nifake.Session` object.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_int32`

        To call the method for all channels, you can call it directly on the :py:class:`nifake.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_int32`

        Args:
            attribute_id (int): Pass the ID of a property.

            attribute_value (int): Pass the value that you want to set the property to.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt32(attribute_value)  # case S150
        error_code = self._library.niFake_SetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def _set_attribute_vi_int64(self, attribute_id, attribute_value):
        r'''_set_attribute_vi_int64

        This method sets the value of a ViInt64 property.

        Tip:
        This method can be called for specific channels within your :py:class:`nifake.Session` object.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_int64`

        To call the method for all channels, you can call it directly on the :py:class:`nifake.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_int64`

        Args:
            attribute_id (int): Pass the ID of a property.

            attribute_value (int): Pass the value that you want to set the property to.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt64(attribute_value)  # case S150
        error_code = self._library.niFake_SetAttributeViInt64(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def _set_attribute_vi_real64(self, attribute_id, attribute_value):
        r'''_set_attribute_vi_real64

        This method sets the value of a ViReal64 property.

        Tip:
        This method can be called for specific channels within your :py:class:`nifake.Session` object.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_real64`

        To call the method for all channels, you can call it directly on the :py:class:`nifake.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_real64`

        Args:
            attribute_id (int): Pass the ID of a property.

            attribute_value (float): Pass the value that you want to set the property to.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViReal64(attribute_value)  # case S150
        error_code = self._library.niFake_SetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def _set_attribute_vi_string(self, attribute_id, attribute_value):
        r'''_set_attribute_vi_string

        This method sets the value of a ViString property.

        Tip:
        This method can be called for specific channels within your :py:class:`nifake.Session` object.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_string`

        To call the method for all channels, you can call it directly on the :py:class:`nifake.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_string`

        Args:
            attribute_id (int): Pass the ID of a property.

            attribute_value (str): Pass the value that you want to set the property to.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = ctypes.create_string_buffer(attribute_value.encode(self._encoding))  # case C020
        error_code = self._library.niFake_SetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def unlock(self):
        '''unlock

        Releases a lock that you acquired on an device session using
        lock. Refer to lock for additional
        information on session locks.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFake_UnlockSession(vi_ctype, None)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return

    def _error_message(self, error_code):
        r'''_error_message

        Takes the errorCode returned by a functiona and returns it as a user-readable string.

        Args:
            error_code (int): The errorCode returned from the instrument.


        Returns:
            error_message (str): The error information formatted into a string.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code_ctype = _visatype.ViStatus(error_code)  # case S150
        error_message_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library.niFake_error_message(vi_ctype, error_code_ctype, error_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return error_message_ctype.value.decode(self._encoding)


class Session(_SessionBase):
    '''An NI-FAKE session to a fake MI driver whose sole purpose is to test nimi-python code generation'''

    def __init__(self, resource_name, options={}, id_query=False, reset_device=False):
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


        Returns:
            session (nifake.Session): A session object representing the device.

        '''
        super(Session, self).__init__(repeated_capability_list=[], vi=None, library=None, encoding=None, freeze_it=False)
        options = _converters.convert_init_with_options_dictionary(options)
        self._library = _library_singleton.get()
        self._encoding = 'windows-1251'

        # Call specified init function
        self._vi = 0  # This must be set before calling _init_with_options().
        self._vi = self._init_with_options(resource_name, options, id_query, reset_device)

        self.tclk = nitclk.SessionReference(self._vi)

        # Store the parameter list for later printing in __repr__
        param_list = []
        param_list.append("resource_name=" + pp.pformat(resource_name))
        param_list.append("options=" + pp.pformat(options))
        param_list.append("reset_device=" + pp.pformat(reset_device))
        self._param_list = ', '.join(param_list)

        self._is_frozen = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
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
            self._vi = 0
            raise
        self._vi = 0

    ''' These are code-generated '''

    @ivi_synchronized
    def abort(self):
        r'''abort

        Aborts a previously initiated thingie.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFake_Abort(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def accept_list_of_durations_in_seconds(self, delays):
        r'''accept_list_of_durations_in_seconds

        Accepts list of floats or hightime.timedelta instances representing time delays.

        Args:
            delays (hightime.timedelta, datetime.timedelta, or float in seconds): A collection of time delay values.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        count_ctype = _visatype.ViInt32(0 if delays is None else len(delays))  # case S160
        delays_converted = _converters.convert_timedeltas_to_seconds_real64(delays)  # case B520
        delays_ctype = get_ctypes_pointer_for_buffer(value=delays_converted, library_type=_visatype.ViReal64)  # case B520
        error_code = self._library.niFake_AcceptListOfDurationsInSeconds(vi_ctype, count_ctype, delays_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def bool_array_output_function(self, number_of_elements):
        r'''bool_array_output_function

        This method returns an array of booleans.

        Args:
            number_of_elements (int): Number of elements in the array.


        Returns:
            an_array (list of bool): Contains an array of booleans

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        number_of_elements_ctype = _visatype.ViInt32(number_of_elements)  # case S210
        an_array_size = number_of_elements  # case B600
        an_array_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViBoolean, size=an_array_size)  # case B600
        error_code = self._library.niFake_BoolArrayOutputFunction(vi_ctype, number_of_elements_ctype, an_array_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [bool(an_array_ctype[i]) for i in range(number_of_elements_ctype.value)]

    @ivi_synchronized
    def double_all_the_nums(self, numbers):
        r'''double_all_the_nums

        Test for buffer with converter

        Args:
            numbers (list of float): numbers is an array of numbers we want to double.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        number_count_ctype = _visatype.ViInt32(0 if numbers is None else len(numbers))  # case S160
        numbers_converted = _converters.convert_double_each_element(numbers)  # case B520
        numbers_ctype = get_ctypes_pointer_for_buffer(value=numbers_converted, library_type=_visatype.ViReal64)  # case B520
        error_code = self._library.niFake_DoubleAllTheNums(vi_ctype, number_count_ctype, numbers_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def enum_array_output_function(self, number_of_elements):
        r'''enum_array_output_function

        This method returns an array of enums, stored as 16 bit integers under the hood.

        Args:
            number_of_elements (int): Number of elements in the array.


        Returns:
            an_array (list of enums.Turtle): Contains an array of enums, stored as 16 bit integers under the hood

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        number_of_elements_ctype = _visatype.ViInt32(number_of_elements)  # case S210
        an_array_size = number_of_elements  # case B600
        an_array_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViInt16, size=an_array_size)  # case B600
        error_code = self._library.niFake_EnumArrayOutputFunction(vi_ctype, number_of_elements_ctype, an_array_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [enums.Turtle(an_array_ctype[i]) for i in range(number_of_elements_ctype.value)]

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        a_turtle_ctype = _visatype.ViInt16(a_turtle.value)  # case S130
        error_code = self._library.niFake_EnumInputFunctionWithDefaults(vi_ctype, a_turtle_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def export_attribute_configuration_buffer(self):
        r'''export_attribute_configuration_buffer

        Export configuration buffer.

        Returns:
            configuration (bytes):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        size_in_bytes_ctype = _visatype.ViInt32()  # case S170
        configuration_ctype = None  # case B580
        error_code = self._library.niFake_ExportAttributeConfigurationBuffer(vi_ctype, size_in_bytes_ctype, configuration_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        size_in_bytes_ctype = _visatype.ViInt32(error_code)  # case S180
        configuration_size = size_in_bytes_ctype.value  # case B590
        configuration_array = array.array("b", [0] * configuration_size)  # case B590
        configuration_ctype = get_ctypes_pointer_for_buffer(value=configuration_array, library_type=_visatype.ViInt8)  # case B590
        error_code = self._library.niFake_ExportAttributeConfigurationBuffer(vi_ctype, size_in_bytes_ctype, configuration_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return _converters.convert_to_bytes(configuration_array)

    @ivi_synchronized
    def fetch_waveform(self, number_of_samples):
        r'''fetch_waveform

        Returns waveform data.

        Args:
            number_of_samples (int): Number of samples to return


        Returns:
            waveform_data (array.array("d")): Samples fetched from the device. Array should be numberOfSamples big.

            actual_number_of_samples (int): Number of samples actually fetched.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        number_of_samples_ctype = _visatype.ViInt32(number_of_samples)  # case S210
        waveform_data_size = number_of_samples  # case B600
        waveform_data_array = array.array("d", [0] * waveform_data_size)  # case B600
        waveform_data_ctype = get_ctypes_pointer_for_buffer(value=waveform_data_array, library_type=_visatype.ViReal64)  # case B600
        actual_number_of_samples_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFake_FetchWaveform(vi_ctype, number_of_samples_ctype, waveform_data_ctype, None if actual_number_of_samples_ctype is None else (ctypes.pointer(actual_number_of_samples_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return waveform_data_array

    @ivi_synchronized
    def fetch_waveform_into(self, waveform_data):
        r'''fetch_waveform

        Returns waveform data.

        Args:
            waveform_data (numpy.array(dtype=numpy.float64)): Samples fetched from the device. Array should be numberOfSamples big.


        Returns:
            waveform_data (numpy.array(dtype=numpy.float64)): Samples fetched from the device. Array should be numberOfSamples big.

            actual_number_of_samples (int): Number of samples actually fetched.

        '''
        import numpy

        if type(waveform_data) is not numpy.ndarray:
            raise TypeError('waveform_data must be {0}, is {1}'.format(numpy.ndarray, type(waveform_data)))
        if numpy.isfortran(waveform_data) is True:
            raise TypeError('waveform_data must be in C-order')
        if waveform_data.dtype is not numpy.dtype('float64'):
            raise TypeError('waveform_data must be numpy.ndarray of dtype=float64, is ' + str(waveform_data.dtype))
        number_of_samples = len(waveform_data)

        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        number_of_samples_ctype = _visatype.ViInt32(number_of_samples)  # case S210
        waveform_data_ctype = get_ctypes_pointer_for_buffer(value=waveform_data)  # case B510
        actual_number_of_samples_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFake_FetchWaveform(vi_ctype, number_of_samples_ctype, waveform_data_ctype, None if actual_number_of_samples_ctype is None else (ctypes.pointer(actual_number_of_samples_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def get_a_boolean(self):
        r'''get_a_boolean

        Returns a boolean.

        Note: This method rules!

        Returns:
            a_boolean (bool): Contains a boolean.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        a_boolean_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niFake_GetABoolean(vi_ctype, None if a_boolean_ctype is None else (ctypes.pointer(a_boolean_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(a_boolean_ctype.value)

    @ivi_synchronized
    def get_a_number(self):
        r'''get_a_number

        Returns a number.

        Note: This method rules!

        Returns:
            a_number (int): Contains a number.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        a_number_ctype = _visatype.ViInt16()  # case S220
        error_code = self._library.niFake_GetANumber(vi_ctype, None if a_number_ctype is None else (ctypes.pointer(a_number_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(a_number_ctype.value)

    @ivi_synchronized
    def get_a_string_of_fixed_maximum_size(self):
        r'''get_a_string_of_fixed_maximum_size

        Illustrates returning a string of fixed size.

        Returns:
            a_string (str): String comes back here. Buffer must be 256 big.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        a_string_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library.niFake_GetAStringOfFixedMaximumSize(vi_ctype, a_string_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return a_string_ctype.value.decode(self._encoding)

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        a_number_ctype = _visatype.ViInt16(a_number)  # case S150
        a_string_ctype = (_visatype.ViChar * a_number)()  # case C080
        error_code = self._library.niFake_GetAStringUsingPythonCode(vi_ctype, a_number_ctype, a_string_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return a_string_ctype.value.decode(self._encoding)

    @ivi_synchronized
    def get_an_ivi_dance_string(self):
        r'''get_an_ivi_dance_string

        Returns a string using the IVI dance.

        Returns:
            a_string (str): Returns the string.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        a_string_ctype = None  # case C050
        error_code = self._library.niFake_GetAnIviDanceString(vi_ctype, buffer_size_ctype, a_string_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        a_string_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niFake_GetAnIviDanceString(vi_ctype, buffer_size_ctype, a_string_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return a_string_ctype.value.decode(self._encoding)

    @ivi_synchronized
    def get_an_ivi_dance_with_a_twist_string(self):
        r'''get_an_ivi_dance_with_a_twist_string

        TBD

        Returns:
            a_string (str):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        a_string_ctype = None  # case C090
        actual_size_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFake_GetAnIviDanceWithATwistString(vi_ctype, buffer_size_ctype, a_string_ctype, None if actual_size_ctype is None else (ctypes.pointer(actual_size_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(actual_size_ctype.value)  # case S200
        a_string_ctype = (_visatype.ViChar * actual_size_ctype.value)()  # case C100
        error_code = self._library.niFake_GetAnIviDanceWithATwistString(vi_ctype, buffer_size_ctype, a_string_ctype, None if actual_size_ctype is None else (ctypes.pointer(actual_size_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return a_string_ctype.value.decode(self._encoding)

    @ivi_synchronized
    def get_array_for_python_code_custom_type(self):
        r'''get_array_for_python_code_custom_type

        This method returns an array for use in python-code size mechanism.

        Returns:
            array_out (list of CustomStruct): Array of custom type using python-code size mechanism

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        number_of_elements_ctype = _visatype.ViInt32(self.get_array_size_for_python_code())  # case S120
        array_out_size = self.get_array_size_for_python_code()  # case B560
        array_out_ctype = get_ctypes_pointer_for_buffer(library_type=custom_struct.struct_CustomStruct, size=array_out_size)  # case B560
        error_code = self._library.niFake_GetArrayForPythonCodeCustomType(vi_ctype, number_of_elements_ctype, array_out_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [custom_struct.CustomStruct(array_out_ctype[i]) for i in range(self.get_array_size_for_python_code())]

    @ivi_synchronized
    def get_array_for_python_code_double(self):
        r'''get_array_for_python_code_double

        This method returns an array for use in python-code size mechanism.

        Returns:
            array_out (list of float): Array of double using python-code size mechanism

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        number_of_elements_ctype = _visatype.ViInt32(self.get_array_size_for_python_code())  # case S120
        array_out_size = self.get_array_size_for_python_code()  # case B560
        array_out_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=array_out_size)  # case B560
        error_code = self._library.niFake_GetArrayForPythonCodeDouble(vi_ctype, number_of_elements_ctype, array_out_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(array_out_ctype[i]) for i in range(self.get_array_size_for_python_code())]

    @ivi_synchronized
    def get_array_size_for_python_code(self):
        r'''get_array_size_for_python_code

        This method returns the size of the array for use in python-code size mechanism.

        Returns:
            size_out (int): Size of array

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        size_out_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFake_GetArraySizeForPythonCode(vi_ctype, None if size_out_ctype is None else (ctypes.pointer(size_out_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(size_out_ctype.value)

    @ivi_synchronized
    def get_array_using_ivi_dance(self):
        r'''get_array_using_ivi_dance

        This method returns an array of float whose size is determined with the IVI dance.

        Returns:
            array_out (list of float): The array returned by this method

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        array_size_ctype = _visatype.ViInt32()  # case S170
        array_out_ctype = None  # case B580
        error_code = self._library.niFake_GetArrayUsingIviDance(vi_ctype, array_size_ctype, array_out_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        array_size_ctype = _visatype.ViInt32(error_code)  # case S180
        array_out_size = array_size_ctype.value  # case B590
        array_out_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=array_out_size)  # case B590
        error_code = self._library.niFake_GetArrayUsingIviDance(vi_ctype, array_size_ctype, array_out_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(array_out_ctype[i]) for i in range(array_size_ctype.value)]

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        cal_type_ctype = _visatype.ViInt32(cal_type)  # case S150
        month_ctype = _visatype.ViInt32()  # case S220
        day_ctype = _visatype.ViInt32()  # case S220
        year_ctype = _visatype.ViInt32()  # case S220
        hour_ctype = _visatype.ViInt32()  # case S220
        minute_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFake_GetCalDateAndTime(vi_ctype, cal_type_ctype, None if month_ctype is None else (ctypes.pointer(month_ctype)), None if day_ctype is None else (ctypes.pointer(day_ctype)), None if year_ctype is None else (ctypes.pointer(year_ctype)), None if hour_ctype is None else (ctypes.pointer(hour_ctype)), None if minute_ctype is None else (ctypes.pointer(minute_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(month_ctype.value), int(day_ctype.value), int(year_ctype.value), int(hour_ctype.value), int(minute_ctype.value)

    @ivi_synchronized
    def get_cal_interval(self):
        r'''get_cal_interval

        Returns the recommended maximum interval, in **months**, between external calibrations.

        Returns:
            months (hightime.timedelta): Specifies the recommended maximum interval, in **months**, between external calibrations.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        months_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFake_GetCalInterval(vi_ctype, None if months_ctype is None else (ctypes.pointer(months_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return _converters.convert_month_to_timedelta(int(months_ctype.value))

    @ivi_synchronized
    def get_custom_type(self):
        r'''get_custom_type

        This method returns a custom type.

        Returns:
            cs (CustomStruct): Set using custom type

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        cs_ctype = custom_struct.struct_CustomStruct()  # case S220
        error_code = self._library.niFake_GetCustomType(vi_ctype, None if cs_ctype is None else (ctypes.pointer(cs_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return custom_struct.CustomStruct(cs_ctype)

    @ivi_synchronized
    def get_custom_type_array(self, number_of_elements):
        r'''get_custom_type_array

        This method returns a custom type.

        Args:
            number_of_elements (int): Number of elements in the array.


        Returns:
            cs (list of CustomStruct): Get using custom type

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        number_of_elements_ctype = _visatype.ViInt32(number_of_elements)  # case S210
        cs_size = number_of_elements  # case B600
        cs_ctype = get_ctypes_pointer_for_buffer(library_type=custom_struct.struct_CustomStruct, size=cs_size)  # case B600
        error_code = self._library.niFake_GetCustomTypeArray(vi_ctype, number_of_elements_ctype, cs_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [custom_struct.CustomStruct(cs_ctype[i]) for i in range(number_of_elements_ctype.value)]

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        a_quantity_ctype = _visatype.ViInt32()  # case S220
        a_turtle_ctype = _visatype.ViInt16()  # case S220
        error_code = self._library.niFake_GetEnumValue(vi_ctype, None if a_quantity_ctype is None else (ctypes.pointer(a_quantity_ctype)), None if a_turtle_ctype is None else (ctypes.pointer(a_turtle_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(a_quantity_ctype.value), enums.Turtle(a_turtle_ctype.value)

    @ivi_synchronized
    def get_cal_date_and_time(self, cal_type):
        '''get_cal_date_and_time

        Returns the date and time of the last calibration performed.

        Args:
            cal_type (int): Specifies the type of calibration performed (external or self-calibration).


        Returns:
            month (hightime.datetime): Indicates date and time of the last calibration.

        '''
        month, day, year, hour, minute = self._get_cal_date_and_time(cal_type)
        return hightime.datetime(year, month, day, hour, minute)

    @ivi_synchronized
    def import_attribute_configuration_buffer(self, configuration):
        r'''import_attribute_configuration_buffer

        Import configuration buffer.

        Args:
            configuration (bytes):

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        size_in_bytes_ctype = _visatype.ViInt32(0 if configuration is None else len(configuration))  # case S160
        configuration_converted = _converters.convert_to_bytes(configuration)  # case B520
        configuration_ctype = get_ctypes_pointer_for_buffer(value=configuration_converted, library_type=_visatype.ViInt8)  # case B520
        error_code = self._library.niFake_ImportAttributeConfigurationBuffer(vi_ctype, size_in_bytes_ctype, configuration_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

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
        resource_name_ctype = ctypes.create_string_buffer(resource_name.encode(self._encoding))  # case C020
        id_query_ctype = _visatype.ViBoolean(id_query)  # case S150
        reset_device_ctype = _visatype.ViBoolean(reset_device)  # case S150
        option_string_ctype = ctypes.create_string_buffer(_converters.convert_init_with_options_dictionary(option_string).encode(self._encoding))  # case C040
        vi_ctype = _visatype.ViSession()  # case S220
        error_code = self._library.niFake_InitWithOptions(resource_name_ctype, id_query_ctype, reset_device_ctype, option_string_ctype, None if vi_ctype is None else (ctypes.pointer(vi_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(vi_ctype.value)

    @ivi_synchronized
    def _initiate(self):
        r'''_initiate

        Initiates a thingie.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFake_Initiate(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        output_array_size_ctype = _visatype.ViInt32(output_array_size)  # case S210
        output_array_size = output_array_size  # case B600
        output_array_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=output_array_size)  # case B600
        output_array_of_fixed_length_size = 3  # case B570
        output_array_of_fixed_length_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=output_array_of_fixed_length_size)  # case B570
        input_array_sizes_ctype = _visatype.ViInt32(0 if input_array_of_floats is None else len(input_array_of_floats))  # case S160
        if input_array_of_integers is not None and len(input_array_of_integers) != len(input_array_of_floats):  # case S160
            raise ValueError("Length of input_array_of_integers and input_array_of_floats parameters do not match.")  # case S160
        input_array_of_floats_ctype = get_ctypes_pointer_for_buffer(value=input_array_of_floats, library_type=_visatype.ViReal64)  # case B550
        input_array_of_integers_ctype = get_ctypes_pointer_for_buffer(value=input_array_of_integers, library_type=_visatype.ViInt16)  # case B550
        error_code = self._library.niFake_MultipleArrayTypes(vi_ctype, output_array_size_ctype, output_array_ctype, output_array_of_fixed_length_ctype, input_array_sizes_ctype, input_array_of_floats_ctype, input_array_of_integers_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(output_array_ctype[i]) for i in range(output_array_size_ctype.value)], [float(output_array_of_fixed_length_ctype[i]) for i in range(3)]

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        values1_ctype = get_ctypes_pointer_for_buffer(value=values1, library_type=_visatype.ViReal64)  # case B550
        values2_ctype = get_ctypes_pointer_for_buffer(value=values2, library_type=_visatype.ViReal64)  # case B550
        values3_ctype = get_ctypes_pointer_for_buffer(value=values3, library_type=_visatype.ViReal64)  # case B550
        values4_ctype = get_ctypes_pointer_for_buffer(value=values4, library_type=_visatype.ViReal64)  # case B550
        size_ctype = _visatype.ViInt32(0 if values1 is None else len(values1))  # case S160
        if values2 is not None and len(values2) != len(values1):  # case S160
            raise ValueError("Length of values2 and values1 parameters do not match.")  # case S160
        if values3 is not None and len(values3) != len(values1):  # case S160
            raise ValueError("Length of values3 and values1 parameters do not match.")  # case S160
        if values4 is not None and len(values4) != len(values1):  # case S160
            raise ValueError("Length of values4 and values1 parameters do not match.")  # case S160
        error_code = self._library.niFake_MultipleArraysSameSize(vi_ctype, values1_ctype, values2_ctype, values3_ctype, values4_ctype, size_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def one_input_function(self, a_number):
        r'''one_input_function

        This method takes one parameter other than the session.

        Args:
            a_number (int): Contains a number

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        a_number_ctype = _visatype.ViInt32(a_number)  # case S150
        error_code = self._library.niFake_OneInputFunction(vi_ctype, a_number_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        a_boolean_ctype = _visatype.ViBoolean(a_boolean)  # case S150
        an_int32_ctype = _visatype.ViInt32(an_int32)  # case S150
        an_int64_ctype = _visatype.ViInt64(an_int64)  # case S150
        an_int_enum_ctype = _visatype.ViInt16(an_int_enum.value)  # case S130
        a_float_ctype = _visatype.ViReal64(a_float)  # case S150
        a_float_enum_ctype = _visatype.ViReal64(a_float_enum.value)  # case S130
        string_size_ctype = _visatype.ViInt32(0 if a_string is None else len(a_string))  # case S160
        a_string_ctype = ctypes.create_string_buffer(a_string.encode(self._encoding))  # case C020
        error_code = self._library.niFake_ParametersAreMultipleTypes(vi_ctype, a_boolean_ctype, an_int32_ctype, an_int64_ctype, an_int_enum_ctype, a_float_ctype, a_float_enum_ctype, string_size_ctype, a_string_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def simple_function(self):
        r'''simple_function

        This method takes no parameters other than the session.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFake_PoorlyNamedSimpleFunction(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def read(self, maximum_time):
        r'''read

        Acquires a single measurement and returns the measured value.

        Args:
            maximum_time (hightime.timedelta): Specifies the **maximum_time** allowed in seconds.


        Returns:
            reading (float): The measured value.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        maximum_time_ctype = _converters.convert_timedelta_to_seconds_real64(maximum_time)  # case S140
        reading_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niFake_Read(vi_ctype, maximum_time_ctype, None if reading_ctype is None else (ctypes.pointer(reading_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(reading_ctype.value)

    @ivi_synchronized
    def return_a_number_and_a_string(self):
        r'''return_a_number_and_a_string

        Returns a number and a string.

        Note: This method rules!

        Returns:
            a_number (int): Contains a number.

            a_string (str): Contains a string. Buffer must be 256 bytes or larger.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        a_number_ctype = _visatype.ViInt16()  # case S220
        a_string_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library.niFake_ReturnANumberAndAString(vi_ctype, None if a_number_ctype is None else (ctypes.pointer(a_number_ctype)), a_string_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(a_number_ctype.value), a_string_ctype.value.decode(self._encoding)

    @ivi_synchronized
    def return_duration_in_seconds(self):
        r'''return_duration_in_seconds

        Returns a hightime.timedelta instance.

        Returns:
            timedelta (hightime.timedelta): Duration in seconds.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        timedelta_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niFake_ReturnDurationInSeconds(vi_ctype, None if timedelta_ctype is None else (ctypes.pointer(timedelta_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return _converters.convert_seconds_real64_to_timedelta(float(timedelta_ctype.value))

    @ivi_synchronized
    def return_list_of_durations_in_seconds(self, number_of_elements):
        r'''return_list_of_durations_in_seconds

        Returns a list of hightime.timedelta instances.

        Args:
            number_of_elements (int): Number of elements in output.


        Returns:
            timedeltas (hightime.timedelta): Contains a list of hightime.timedelta instances.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        number_of_elements_ctype = _visatype.ViInt32(number_of_elements)  # case S210
        timedeltas_size = number_of_elements  # case B600
        timedeltas_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=timedeltas_size)  # case B600
        error_code = self._library.niFake_ReturnListOfDurationsInSeconds(vi_ctype, number_of_elements_ctype, timedeltas_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return _converters.convert_seconds_real64_to_timedeltas([float(timedeltas_ctype[i]) for i in range(number_of_elements_ctype.value)])

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        a_boolean_ctype = _visatype.ViBoolean()  # case S220
        an_int32_ctype = _visatype.ViInt32()  # case S220
        an_int64_ctype = _visatype.ViInt64()  # case S220
        an_int_enum_ctype = _visatype.ViInt16()  # case S220
        a_float_ctype = _visatype.ViReal64()  # case S220
        a_float_enum_ctype = _visatype.ViReal64()  # case S220
        array_size_ctype = _visatype.ViInt32(array_size)  # case S210
        an_array_size = array_size  # case B600
        an_array_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=an_array_size)  # case B600
        string_size_ctype = _visatype.ViInt32()  # case S170
        a_string_ctype = None  # case C050
        error_code = self._library.niFake_ReturnMultipleTypes(vi_ctype, None if a_boolean_ctype is None else (ctypes.pointer(a_boolean_ctype)), None if an_int32_ctype is None else (ctypes.pointer(an_int32_ctype)), None if an_int64_ctype is None else (ctypes.pointer(an_int64_ctype)), None if an_int_enum_ctype is None else (ctypes.pointer(an_int_enum_ctype)), None if a_float_ctype is None else (ctypes.pointer(a_float_ctype)), None if a_float_enum_ctype is None else (ctypes.pointer(a_float_enum_ctype)), array_size_ctype, an_array_ctype, string_size_ctype, a_string_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        string_size_ctype = _visatype.ViInt32(error_code)  # case S180
        a_string_ctype = (_visatype.ViChar * string_size_ctype.value)()  # case C060
        error_code = self._library.niFake_ReturnMultipleTypes(vi_ctype, None if a_boolean_ctype is None else (ctypes.pointer(a_boolean_ctype)), None if an_int32_ctype is None else (ctypes.pointer(an_int32_ctype)), None if an_int64_ctype is None else (ctypes.pointer(an_int64_ctype)), None if an_int_enum_ctype is None else (ctypes.pointer(an_int_enum_ctype)), None if a_float_ctype is None else (ctypes.pointer(a_float_ctype)), None if a_float_enum_ctype is None else (ctypes.pointer(a_float_enum_ctype)), array_size_ctype, an_array_ctype, string_size_ctype, a_string_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(a_boolean_ctype.value), int(an_int32_ctype.value), int(an_int64_ctype.value), enums.Turtle(an_int_enum_ctype.value), float(a_float_ctype.value), enums.FloatEnum(a_float_enum_ctype.value), [float(an_array_ctype[i]) for i in range(array_size_ctype.value)], a_string_ctype.value.decode(self._encoding)

    @ivi_synchronized
    def set_custom_type(self, cs):
        r'''set_custom_type

        This method takes a custom type.

        Args:
            cs (CustomStruct): Set using custom type

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        cs_ctype = custom_struct.struct_CustomStruct(cs)  # case S150
        error_code = self._library.niFake_SetCustomType(vi_ctype, cs_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def set_custom_type_array(self, cs):
        r'''set_custom_type_array

        This method takes an array of custom types.

        Args:
            cs (list of CustomStruct): Set using custom type

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        number_of_elements_ctype = _visatype.ViInt32(0 if cs is None else len(cs))  # case S160
        cs_ctype = get_ctypes_pointer_for_buffer([custom_struct.struct_CustomStruct(c) for c in cs], library_type=custom_struct.struct_CustomStruct)  # case B540
        error_code = self._library.niFake_SetCustomTypeArray(vi_ctype, number_of_elements_ctype, cs_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        a_mobile_os_name_ctype = ctypes.create_string_buffer(a_mobile_os_name.value.encode(self._encoding))  # case C030
        error_code = self._library.niFake_StringValuedEnumInputFunctionWithDefaults(vi_ctype, a_mobile_os_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def two_input_function(self, a_number, a_string):
        r'''two_input_function

        This method takes two parameters other than the session.

        Args:
            a_number (float): Contains a number

            a_string (str): Contains a string

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        a_number_ctype = _visatype.ViReal64(a_number)  # case S150
        a_string_ctype = ctypes.create_string_buffer(a_string.encode(self._encoding))  # case C020
        error_code = self._library.niFake_TwoInputFunction(vi_ctype, a_number_ctype, a_string_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        input_ctype = _visatype.ViInt64(input)  # case S150
        output_ctype = _visatype.ViInt64()  # case S220
        error_code = self._library.niFake_Use64BitNumber(vi_ctype, input_ctype, None if output_ctype is None else (ctypes.pointer(output_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(output_ctype.value)

    @ivi_synchronized
    def write_waveform(self, waveform):
        r'''write_waveform

        Writes waveform to the driver

        Args:
            waveform (array.array("d")): Waveform data.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        number_of_samples_ctype = _visatype.ViInt32(0 if waveform is None else len(waveform))  # case S160
        waveform_array = get_ctypes_and_array(value=waveform, array_type="d")  # case B550
        waveform_ctype = get_ctypes_pointer_for_buffer(value=waveform_array, library_type=_visatype.ViReal64)  # case B550
        error_code = self._library.niFake_WriteWaveform(vi_ctype, number_of_samples_ctype, waveform_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def write_waveform_numpy(self, waveform):
        r'''write_waveform

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        number_of_samples_ctype = _visatype.ViInt32(0 if waveform is None else len(waveform))  # case S160
        waveform_ctype = get_ctypes_pointer_for_buffer(value=waveform)  # case B510
        error_code = self._library.niFake_WriteWaveform(vi_ctype, number_of_samples_ctype, waveform_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _close(self):
        r'''_close

        Closes the specified session and deallocates resources that it reserved.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFake_close(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

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
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        self_test_result_ctype = _visatype.ViInt16()  # case S220
        self_test_message_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library.niFake_self_test(vi_ctype, None if self_test_result_ctype is None else (ctypes.pointer(self_test_result_ctype)), self_test_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(self_test_result_ctype.value), self_test_message_ctype.value.decode(self._encoding)



