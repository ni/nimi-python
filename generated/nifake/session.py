# -*- coding: utf-8 -*-
# This file was generated
import array  # noqa: F401
import ctypes
import datetime

from nifake import _converters
from nifake import attributes
from nifake import enums
from nifake import errors
from nifake import library_singleton
from nifake import visatype

from nifake import custom_struct  # noqa: F401

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


class _RepeatedCapabilities(object):
    def __init__(self, session, prefix):
        self._session = session
        self._prefix = prefix

    def __getitem__(self, repeated_capability):
        '''Set/get properties or call methods with a repeated capability (i.e. channels)'''
        rep_caps, rep_caps_list = _converters.convert_repeated_capabilities(repeated_capability, self._prefix)

        return _SessionBase(vi=self._session._vi, repeated_capability=rep_caps, repeated_capability_list=rep_caps_list, library=self._session._library, encoding=self._session._encoding, freeze_it=True)


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

    float_enum = attributes.AttributeEnum(attributes.AttributeViReal64, enums.FloatEnum, 1000005)
    '''Type: enums.FloatEnum

    An property with an enum that is also a float
    '''
    read_write_bool = attributes.AttributeViBoolean(1000000)
    '''Type: bool

    An property of type bool with read/write access.
    '''
    read_write_color = attributes.AttributeEnum(attributes.AttributeViInt32, enums.Color, 1000003)
    '''Type: enums.Color

    An property of type Color with read/write access.
    '''
    read_write_double = attributes.AttributeViReal64(1000001)
    '''Type: float

    An property of type float with read/write access.
    '''
    read_write_double_with_converter = attributes.AttributeViReal64TimeDeltaSeconds(1000007)
    '''Type: datetime.timedelta

    Property in seconds
    '''
    read_write_int64 = attributes.AttributeViInt64(1000006)
    '''Type: int

    An property of type 64-bit integer with read/write access.
    '''
    read_write_integer = attributes.AttributeViInt32(1000004)
    '''Type: int

    An property of type integer with read/write access.
    '''
    read_write_integer_with_converter = attributes.AttributeViInt32TimeDeltaMilliseconds(1000008)
    '''Type: datetime.timedelta

    Property in milliseconds
    '''
    read_write_string = attributes.AttributeViString(1000002)
    '''Type: str

    An property of type string with read/write access.
    '''

    def __init__(self, repeated_capability, repeated_capability_list, vi, library, encoding, freeze_it=False):
        self._repeated_capability = repeated_capability
        self._repeated_capability_list = repeated_capability_list
        self._vi = vi
        self._library = library
        self._encoding = encoding

        # Store the parameter list for later printing in __repr__
        param_list = []
        param_list.append("repeated_capability=" + pp.pformat(repeated_capability))
        param_list.append("repeated_capability_list=" + pp.pformat(repeated_capability_list))
        param_list.append("vi=" + pp.pformat(vi))
        param_list.append("library=" + pp.pformat(library))
        param_list.append("encoding=" + pp.pformat(encoding))
        self._param_list = ', '.join(param_list)

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

    def _get_attribute_vi_boolean(self, attribute_id):
        '''_get_attribute_vi_boolean

        Queries the value of a ViBoolean property.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifake.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifake.Session instance, and calling this method on the result.:

            session.channels['0,1']._get_attribute_vi_boolean(attribute_id)

        Args:
            attribute_id (int): Pass the ID of an property.


        Returns:
            attribute_value (bool): Returns the value of the property.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = visatype.ViBoolean()  # case S200
        error_code = self._library.niFake_GetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(attribute_value_ctype.value)

    def _get_attribute_vi_int32(self, attribute_id):
        '''_get_attribute_vi_int32

        Queries the value of a ViInt32 property.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifake.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifake.Session instance, and calling this method on the result.:

            session.channels['0,1']._get_attribute_vi_int32(attribute_id)

        Args:
            attribute_id (int): Pass the ID of an property.


        Returns:
            attribute_value (int): Returns the value of the property.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = visatype.ViInt32()  # case S200
        error_code = self._library.niFake_GetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(attribute_value_ctype.value)

    def _get_attribute_vi_int64(self, attribute_id):
        '''_get_attribute_vi_int64

        Queries the value of a ViInt64 property.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifake.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifake.Session instance, and calling this method on the result.:

            session.channels['0,1']._get_attribute_vi_int64(attribute_id)

        Args:
            attribute_id (int): Pass the ID of an property.


        Returns:
            attribute_value (int): Returns the value of the property.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = visatype.ViInt64()  # case S200
        error_code = self._library.niFake_GetAttributeViInt64(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(attribute_value_ctype.value)

    def _get_attribute_vi_real64(self, attribute_id):
        '''_get_attribute_vi_real64

        Queries the value of a ViReal property.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifake.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifake.Session instance, and calling this method on the result.:

            session.channels['0,1']._get_attribute_vi_real64(attribute_id)

        Args:
            attribute_id (int): Pass the ID of an property.


        Returns:
            attribute_value (float): Returns the value of the property.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = visatype.ViReal64()  # case S200
        error_code = self._library.niFake_GetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(attribute_value_ctype.value)

    def _get_attribute_vi_string(self, attribute_id):
        '''_get_attribute_vi_string

        Queries the value of a ViBoolean property.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifake.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifake.Session instance, and calling this method on the result.:

            session.channels['0,1']._get_attribute_vi_string(attribute_id)

        Args:
            attribute_id (int): Pass the ID of an property.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case S150
        buffer_size_ctype = visatype.ViInt32()  # case S170
        attribute_value_ctype = None  # case C050
        error_code = self._library.niFake_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, buffer_size_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = visatype.ViInt32(error_code)  # case S180
        attribute_value_ctype = (visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niFake_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, buffer_size_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return attribute_value_ctype.value.decode(self._encoding)

    def _get_error(self):
        '''_get_error

        Returns the error information associated with the session.

        Returns:
            error_code (int): Returns errorCode for the session. If you pass 0 for bufferSize, you can pass VI_NULL for this.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        error_code_ctype = visatype.ViStatus()  # case S200
        buffer_size_ctype = visatype.ViInt32()  # case S170
        description_ctype = None  # case C050
        error_code = self._library.niFake_GetError(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), buffer_size_ctype, description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=True)
        buffer_size_ctype = visatype.ViInt32(error_code)  # case S180
        description_ctype = (visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niFake_GetError(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), buffer_size_ctype, description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return int(error_code_ctype.value), description_ctype.value.decode(self._encoding)

    def read_from_channel(self, maximum_time):
        '''read_from_channel

        Acquires a single measurement and returns the measured value.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifake.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifake.Session instance, and calling this method on the result.:

            session.channels['0,1'].read_from_channel(maximum_time)

        Args:
            maximum_time (datetime.timedelta): Specifies the **maximum_time** allowed in microseconds.


        Returns:
            reading (float): The measured value.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        maximum_time_ctype = _converters.convert_timedelta_to_microseconds(maximum_time, visatype.ViInt32)  # case S140
        reading_ctype = visatype.ViReal64()  # case S200
        error_code = self._library.niFake_ReadFromChannel(vi_ctype, channel_name_ctype, maximum_time_ctype, None if reading_ctype is None else (ctypes.pointer(reading_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(reading_ctype.value)

    def _set_attribute_vi_boolean(self, attribute_id, attribute_value):
        '''_set_attribute_vi_boolean

        This method sets the value of a ViBoolean property.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifake.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifake.Session instance, and calling this method on the result.:

            session.channels['0,1']._set_attribute_vi_boolean(attribute_id, attribute_value)

        Args:
            attribute_id (int): Pass the ID of an property.

            attribute_value (bool): Pass the value that you want to set the property to.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = visatype.ViBoolean(attribute_value)  # case S150
        error_code = self._library.niFake_SetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_int32(self, attribute_id, attribute_value):
        '''_set_attribute_vi_int32

        This method sets the value of a ViInt32 property.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifake.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifake.Session instance, and calling this method on the result.:

            session.channels['0,1']._set_attribute_vi_int32(attribute_id, attribute_value)

        Args:
            attribute_id (int): Pass the ID of an property.

            attribute_value (int): Pass the value that you want to set the property to.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = visatype.ViInt32(attribute_value)  # case S150
        error_code = self._library.niFake_SetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_int64(self, attribute_id, attribute_value):
        '''_set_attribute_vi_int64

        This method sets the value of a ViInt64 property.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifake.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifake.Session instance, and calling this method on the result.:

            session.channels['0,1']._set_attribute_vi_int64(attribute_id, attribute_value)

        Args:
            attribute_id (int): Pass the ID of an property.

            attribute_value (int): Pass the value that you want to set the property to.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = visatype.ViInt64(attribute_value)  # case S150
        error_code = self._library.niFake_SetAttributeViInt64(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_real64(self, attribute_id, attribute_value):
        '''_set_attribute_vi_real64

        This method sets the value of a ViReal64 property.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifake.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifake.Session instance, and calling this method on the result.:

            session.channels['0,1']._set_attribute_vi_real64(attribute_id, attribute_value)

        Args:
            attribute_id (int): Pass the ID of an property.

            attribute_value (float): Pass the value that you want to set the property to.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = visatype.ViReal64(attribute_value)  # case S150
        error_code = self._library.niFake_SetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_string(self, attribute_id, attribute_value):
        '''_set_attribute_vi_string

        This method sets the value of a ViString property.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifake.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifake.Session instance, and calling this method on the result.:

            session.channels['0,1']._set_attribute_vi_string(attribute_id, attribute_value)

        Args:
            attribute_id (int): Pass the ID of an property.

            attribute_value (str): Pass the value that you want to set the property to.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = ctypes.create_string_buffer(attribute_value.encode(self._encoding))  # case C020
        error_code = self._library.niFake_SetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _error_message(self, error_code):
        '''_error_message

        Takes the errorCode returned by a functiona and returns it as a user-readable string.

        Args:
            error_code (int): The errorCode returned from the instrument.


        Returns:
            error_message (str): The error information formatted into a string.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        error_code_ctype = visatype.ViStatus(error_code)  # case S150
        error_message_ctype = (visatype.ViChar * 256)()  # case C070
        error_code = self._library.niFake_error_message(vi_ctype, error_code_ctype, error_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return error_message_ctype.value.decode(self._encoding)


class Session(_SessionBase):
    '''An NI-FAKE session to a fake MI driver whose sole purpose is to test nimi-python code generation'''

    def __init__(self, resource_name, options={}, id_query=False, reset_device=False):
        '''An NI-FAKE session to a fake MI driver whose sole purpose is to test nimi-python code generation

        Creates a new IVI instrument driver session.

        Args:
            resource_name (str): Caution: This is just some string.

                Contains the **resource_name** of the device to initialize.

            options (str): Specifies the initial value of certain properties for the session. The
                syntax for **options** is a dictionary of properties with an assigned
                value. For example:

                { 'simulate': False }

                You do not have to specify a value for all the properties. If you do not
                specify a value for an property, the default value is used.

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
        super(Session, self).__init__(repeated_capability='', repeated_capability_list=[], vi=None, library=None, encoding=None, freeze_it=False)
        options = _converters.convert_init_with_options_dictionary(options, self._encoding)
        self._library = library_singleton.get()
        self._encoding = 'windows-1251'

        # Call specified init function
        self._vi = 0  # This must be set before calling _init_with_options().
        self._vi = self._init_with_options(resource_name, options, id_query, reset_device)

        # Instantiate any repeated capability objects
        self.channels = _RepeatedCapabilities(self, '')

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
        return _Acquisition(self)

    def close(self):
        try:
            self._close()
        except errors.Error as e:
            self._vi = 0
            raise
        self._vi = 0

    ''' These are code-generated '''

    def abort(self):
        '''abort

        Aborts a previously initiated thingie.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFake_Abort(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def bool_array_output_function(self, number_of_elements):
        '''bool_array_output_function

        This method returns an array of booleans.

        Args:
            number_of_elements (int): Number of elements in the array.


        Returns:
            an_array (list of bool): Contains an array of booleans

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        number_of_elements_ctype = visatype.ViInt32(number_of_elements)  # case S190
        an_array_size = number_of_elements  # case B600
        an_array_ctype = get_ctypes_pointer_for_buffer(library_type=visatype.ViBoolean, size=an_array_size)  # case B600
        error_code = self._library.niFake_BoolArrayOutputFunction(vi_ctype, number_of_elements_ctype, an_array_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [bool(an_array_ctype[i]) for i in range(number_of_elements_ctype.value)]

    def enum_array_output_function(self, number_of_elements):
        '''enum_array_output_function

        This method returns an array of enums, stored as 16 bit integers under the hood.

        Args:
            number_of_elements (int): Number of elements in the array.


        Returns:
            an_array (list of enums.Turtle): Contains an array of enums, stored as 16 bit integers under the hood

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        number_of_elements_ctype = visatype.ViInt32(number_of_elements)  # case S190
        an_array_size = number_of_elements  # case B600
        an_array_ctype = get_ctypes_pointer_for_buffer(library_type=visatype.ViInt16, size=an_array_size)  # case B600
        error_code = self._library.niFake_EnumArrayOutputFunction(vi_ctype, number_of_elements_ctype, an_array_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [enums.Turtle(an_array_ctype[i]) for i in range(number_of_elements_ctype.value)]

    def enum_input_function_with_defaults(self, a_turtle=enums.Turtle.LEONARDO):
        '''enum_input_function_with_defaults

        This method takes one parameter other than the session, which happens to be an enum and has a default value defined in functions_addon.

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
            raise TypeError('Parameter mode must be of type ' + str(enums.Turtle))
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        a_turtle_ctype = visatype.ViInt16(a_turtle.value)  # case S130
        error_code = self._library.niFake_EnumInputFunctionWithDefaults(vi_ctype, a_turtle_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def fetch_waveform(self, number_of_samples):
        '''fetch_waveform

        Returns waveform data.

        Args:
            number_of_samples (int): Number of samples to return


        Returns:
            waveform_data (array.array("d")): Samples fetched from the device. Array should be numberOfSamples big.

            actual_number_of_samples (int): Number of samples actually fetched.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        number_of_samples_ctype = visatype.ViInt32(number_of_samples)  # case S190
        waveform_data_size = number_of_samples  # case B600
        waveform_data_array = array.array("d", [0] * waveform_data_size)  # case B600
        waveform_data_ctype = get_ctypes_pointer_for_buffer(value=waveform_data_array, library_type=visatype.ViReal64)  # case B600
        actual_number_of_samples_ctype = visatype.ViInt32()  # case S200
        error_code = self._library.niFake_FetchWaveform(vi_ctype, number_of_samples_ctype, waveform_data_ctype, None if actual_number_of_samples_ctype is None else (ctypes.pointer(actual_number_of_samples_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return waveform_data_array

    def fetch_waveform_into(self, waveform_data):
        '''fetch_waveform

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

        vi_ctype = visatype.ViSession(self._vi)  # case S110
        number_of_samples_ctype = visatype.ViInt32(number_of_samples)  # case S190
        waveform_data_ctype = get_ctypes_pointer_for_buffer(value=waveform_data)  # case B510
        actual_number_of_samples_ctype = visatype.ViInt32()  # case S200
        error_code = self._library.niFake_FetchWaveform(vi_ctype, number_of_samples_ctype, waveform_data_ctype, None if actual_number_of_samples_ctype is None else (ctypes.pointer(actual_number_of_samples_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def get_a_boolean(self):
        '''get_a_boolean

        Returns a boolean.

        Note: This method rules!

        Returns:
            a_boolean (bool): Contains a boolean.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        a_boolean_ctype = visatype.ViBoolean()  # case S200
        error_code = self._library.niFake_GetABoolean(vi_ctype, None if a_boolean_ctype is None else (ctypes.pointer(a_boolean_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(a_boolean_ctype.value)

    def get_a_number(self):
        '''get_a_number

        Returns a number.

        Note: This method rules!

        Returns:
            a_number (int): Contains a number.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        a_number_ctype = visatype.ViInt16()  # case S200
        error_code = self._library.niFake_GetANumber(vi_ctype, None if a_number_ctype is None else (ctypes.pointer(a_number_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(a_number_ctype.value)

    def get_a_string_of_fixed_maximum_size(self):
        '''get_a_string_of_fixed_maximum_size

        Illustrates resturning a string of fixed size.

        Returns:
            a_string (str): String comes back here. Buffer must be 256 big.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        a_string_ctype = (visatype.ViChar * 256)()  # case C070
        error_code = self._library.niFake_GetAStringOfFixedMaximumSize(vi_ctype, a_string_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return a_string_ctype.value.decode(self._encoding)

    def get_an_ivi_dance_string(self):
        '''get_an_ivi_dance_string

        Returns a string using the IVI dance.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        buffer_size_ctype = visatype.ViInt32()  # case S170
        a_string_ctype = None  # case C050
        error_code = self._library.niFake_GetAnIviDanceString(vi_ctype, buffer_size_ctype, a_string_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = visatype.ViInt32(error_code)  # case S180
        a_string_ctype = (visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niFake_GetAnIviDanceString(vi_ctype, buffer_size_ctype, a_string_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return a_string_ctype.value.decode(self._encoding)

    def get_array_for_python_code_custom_type(self):
        '''get_array_for_python_code_custom_type

        This method returns an array for use in python-code size mechanism.

        Returns:
            array_out (list of CustomStruct): Array of custom type using puthon-code size mechanism

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        number_of_elements_ctype = visatype.ViInt32(self.get_array_size_for_python_code())  # case S120
        array_out_size = self.get_array_size_for_python_code()  # case B560
        array_out_ctype = get_ctypes_pointer_for_buffer(library_type=custom_struct.custom_struct, size=array_out_size)  # case B560
        error_code = self._library.niFake_GetArrayForPythonCodeCustomType(vi_ctype, number_of_elements_ctype, array_out_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [custom_struct.CustomStruct(array_out_ctype[i]) for i in range(self.get_array_size_for_python_code())]

    def get_array_for_python_code_double(self):
        '''get_array_for_python_code_double

        This method returns an array for use in python-code size mechanism.

        Returns:
            array_out (list of float): Array of double using puthon-code size mechanism

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        number_of_elements_ctype = visatype.ViInt32(self.get_array_size_for_python_code())  # case S120
        array_out_size = self.get_array_size_for_python_code()  # case B560
        array_out_ctype = get_ctypes_pointer_for_buffer(library_type=visatype.ViReal64, size=array_out_size)  # case B560
        error_code = self._library.niFake_GetArrayForPythonCodeDouble(vi_ctype, number_of_elements_ctype, array_out_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(array_out_ctype[i]) for i in range(self.get_array_size_for_python_code())]

    def get_array_size_for_python_code(self):
        '''get_array_size_for_python_code

        This method returns the size of the array for use in python-code size mechanism.

        Returns:
            size_out (int): Size of array

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        size_out_ctype = visatype.ViInt32()  # case S200
        error_code = self._library.niFake_GetArraySizeForPythonCode(vi_ctype, None if size_out_ctype is None else (ctypes.pointer(size_out_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(size_out_ctype.value)

    def get_array_using_ivi_dance(self):
        '''get_array_using_ivi_dance

        This method returns an array of float whose size is determined with the IVI dance.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        array_size_ctype = visatype.ViInt32()  # case S170
        array_out_ctype = None  # case B580
        error_code = self._library.niFake_GetArrayUsingIVIDance(vi_ctype, array_size_ctype, array_out_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        array_size_ctype = visatype.ViInt32(error_code)  # case S180
        array_out_size = array_size_ctype.value  # case B590
        array_out_ctype = get_ctypes_pointer_for_buffer(library_type=visatype.ViReal64, size=array_out_size)  # case B590
        error_code = self._library.niFake_GetArrayUsingIVIDance(vi_ctype, array_size_ctype, array_out_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(array_out_ctype[i]) for i in range(array_size_ctype.value)]

    def _get_cal_date_and_time(self, cal_type):
        '''_get_cal_date_and_time

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
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        cal_type_ctype = visatype.ViInt32(cal_type)  # case S150
        month_ctype = visatype.ViInt32()  # case S200
        day_ctype = visatype.ViInt32()  # case S200
        year_ctype = visatype.ViInt32()  # case S200
        hour_ctype = visatype.ViInt32()  # case S200
        minute_ctype = visatype.ViInt32()  # case S200
        error_code = self._library.niFake_GetCalDateAndTime(vi_ctype, cal_type_ctype, None if month_ctype is None else (ctypes.pointer(month_ctype)), None if day_ctype is None else (ctypes.pointer(day_ctype)), None if year_ctype is None else (ctypes.pointer(year_ctype)), None if hour_ctype is None else (ctypes.pointer(hour_ctype)), None if minute_ctype is None else (ctypes.pointer(minute_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(month_ctype.value), int(day_ctype.value), int(year_ctype.value), int(hour_ctype.value), int(minute_ctype.value)

    def get_custom_type(self):
        '''get_custom_type

        This method returns a custom type.

        Returns:
            cs (CustomStruct): Set using custom type

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        cs_ctype = custom_struct.custom_struct()  # case S200
        error_code = self._library.niFake_GetCustomType(vi_ctype, None if cs_ctype is None else (ctypes.pointer(cs_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return custom_struct.CustomStruct(cs_ctype)

    def get_custom_type_array(self, number_of_elements):
        '''get_custom_type_array

        This method returns a custom type.

        Args:
            number_of_elements (int): Number of elements in the array.


        Returns:
            cs (list of CustomStruct): Get using custom type

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        number_of_elements_ctype = visatype.ViInt32(number_of_elements)  # case S190
        cs_size = number_of_elements  # case B600
        cs_ctype = get_ctypes_pointer_for_buffer(library_type=custom_struct.custom_struct, size=cs_size)  # case B600
        error_code = self._library.niFake_GetCustomTypeArray(vi_ctype, number_of_elements_ctype, cs_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [custom_struct.CustomStruct(cs_ctype[i]) for i in range(number_of_elements_ctype.value)]

    def get_enum_value(self):
        '''get_enum_value

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
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        a_quantity_ctype = visatype.ViInt32()  # case S200
        a_turtle_ctype = visatype.ViInt16()  # case S200
        error_code = self._library.niFake_GetEnumValue(vi_ctype, None if a_quantity_ctype is None else (ctypes.pointer(a_quantity_ctype)), None if a_turtle_ctype is None else (ctypes.pointer(a_turtle_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(a_quantity_ctype.value), enums.Turtle(a_turtle_ctype.value)

    def get_cal_date_and_time(self, cal_type):
        '''get_cal_date_and_time

        Returns the date and time of the last calibration performed.

        Args:
            cal_type (int): Specifies the type of calibration performed (external or self-calibration).


        Returns:
            month (datetime.datetime): Indicates date and time of the last calibration.

        '''
        month, day, year, hour, minute = self._get_cal_date_and_time(cal_type)
        return datetime.datetime(year, month, day, hour, minute)

    def _init_with_options(self, resource_name, option_string, id_query=False, reset_device=False):
        '''_init_with_options

        Creates a new IVI instrument driver session.

        Args:
            resource_name (str): Caution: This is just some string.

                Contains the **resource_name** of the device to initialize.

            option_string (str): Some options

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
        id_query_ctype = visatype.ViBoolean(id_query)  # case S150
        reset_device_ctype = visatype.ViBoolean(reset_device)  # case S150
        option_string_ctype = ctypes.create_string_buffer(option_string.encode(self._encoding))  # case C020
        vi_ctype = visatype.ViSession()  # case S200
        error_code = self._library.niFake_InitWithOptions(resource_name_ctype, id_query_ctype, reset_device_ctype, option_string_ctype, None if vi_ctype is None else (ctypes.pointer(vi_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(vi_ctype.value)

    def _initiate(self):
        '''_initiate

        Initiates a thingie.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFake_Initiate(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def multiple_array_types(self, output_array_size, input_array_of_floats, input_array_of_integers=None):
        '''multiple_array_types

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
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        output_array_size_ctype = visatype.ViInt32(output_array_size)  # case S190
        output_array_size = output_array_size  # case B600
        output_array_ctype = get_ctypes_pointer_for_buffer(library_type=visatype.ViReal64, size=output_array_size)  # case B600
        output_array_of_fixed_length_size = 3  # case B570
        output_array_of_fixed_length_ctype = get_ctypes_pointer_for_buffer(library_type=visatype.ViReal64, size=output_array_of_fixed_length_size)  # case B570
        input_array_sizes_ctype = visatype.ViInt32(0 if input_array_of_floats is None else len(input_array_of_floats))  # case S160
        input_array_of_floats_ctype = get_ctypes_pointer_for_buffer(value=input_array_of_floats, library_type=visatype.ViReal64)  # case B550
        input_array_of_integers_ctype = get_ctypes_pointer_for_buffer(value=input_array_of_integers, library_type=visatype.ViInt16)  # case B550
        error_code = self._library.niFake_MultipleArrayTypes(vi_ctype, output_array_size_ctype, output_array_ctype, output_array_of_fixed_length_ctype, input_array_sizes_ctype, input_array_of_floats_ctype, input_array_of_integers_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(output_array_ctype[i]) for i in range(output_array_size_ctype.value)], [float(output_array_of_fixed_length_ctype[i]) for i in range(3)]

    def one_input_function(self, a_number):
        '''one_input_function

        This method takes one parameter other than the session.

        Args:
            a_number (int): Contains a number

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        a_number_ctype = visatype.ViInt32(a_number)  # case S150
        error_code = self._library.niFake_OneInputFunction(vi_ctype, a_number_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def parameters_are_multiple_types(self, a_boolean, an_int32, an_int64, an_int_enum, a_float, a_float_enum, a_string):
        '''parameters_are_multiple_types

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
            raise TypeError('Parameter mode must be of type ' + str(enums.Turtle))
        if type(a_float_enum) is not enums.FloatEnum:
            raise TypeError('Parameter mode must be of type ' + str(enums.FloatEnum))
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        a_boolean_ctype = visatype.ViBoolean(a_boolean)  # case S150
        an_int32_ctype = visatype.ViInt32(an_int32)  # case S150
        an_int64_ctype = visatype.ViInt64(an_int64)  # case S150
        an_int_enum_ctype = visatype.ViInt16(an_int_enum.value)  # case S130
        a_float_ctype = visatype.ViReal64(a_float)  # case S150
        a_float_enum_ctype = visatype.ViReal64(a_float_enum.value)  # case S130
        string_size_ctype = visatype.ViInt32(0 if a_string is None else len(a_string))  # case S160
        a_string_ctype = ctypes.create_string_buffer(a_string.encode(self._encoding))  # case C020
        error_code = self._library.niFake_ParametersAreMultipleTypes(vi_ctype, a_boolean_ctype, an_int32_ctype, an_int64_ctype, an_int_enum_ctype, a_float_ctype, a_float_enum_ctype, string_size_ctype, a_string_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def simple_function(self):
        '''simple_function

        This method takes no parameters other than the session.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFake_PoorlyNamedSimpleFunction(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def read(self, maximum_time):
        '''read

        Acquires a single measurement and returns the measured value.

        Args:
            maximum_time (datetime.timedelta): Specifies the **maximum_time** allowed in seconds.


        Returns:
            reading (float): The measured value.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        maximum_time_ctype = _converters.convert_timedelta_to_seconds(maximum_time, visatype.ViReal64)  # case S140
        reading_ctype = visatype.ViReal64()  # case S200
        error_code = self._library.niFake_Read(vi_ctype, maximum_time_ctype, None if reading_ctype is None else (ctypes.pointer(reading_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(reading_ctype.value)

    def return_a_number_and_a_string(self):
        '''return_a_number_and_a_string

        Returns a number and a string.

        Note: This method rules!

        Returns:
            a_number (int): Contains a number.

            a_string (str): Contains a string. Buffer must be 256 bytes or larger.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        a_number_ctype = visatype.ViInt16()  # case S200
        a_string_ctype = (visatype.ViChar * 256)()  # case C070
        error_code = self._library.niFake_ReturnANumberAndAString(vi_ctype, None if a_number_ctype is None else (ctypes.pointer(a_number_ctype)), a_string_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(a_number_ctype.value), a_string_ctype.value.decode(self._encoding)

    def return_multiple_types(self, array_size):
        '''return_multiple_types

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

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        a_boolean_ctype = visatype.ViBoolean()  # case S200
        an_int32_ctype = visatype.ViInt32()  # case S200
        an_int64_ctype = visatype.ViInt64()  # case S200
        an_int_enum_ctype = visatype.ViInt16()  # case S200
        a_float_ctype = visatype.ViReal64()  # case S200
        a_float_enum_ctype = visatype.ViReal64()  # case S200
        array_size_ctype = visatype.ViInt32(array_size)  # case S190
        an_array_size = array_size  # case B600
        an_array_ctype = get_ctypes_pointer_for_buffer(library_type=visatype.ViReal64, size=an_array_size)  # case B600
        string_size_ctype = visatype.ViInt32()  # case S170
        a_string_ctype = None  # case C050
        error_code = self._library.niFake_ReturnMultipleTypes(vi_ctype, None if a_boolean_ctype is None else (ctypes.pointer(a_boolean_ctype)), None if an_int32_ctype is None else (ctypes.pointer(an_int32_ctype)), None if an_int64_ctype is None else (ctypes.pointer(an_int64_ctype)), None if an_int_enum_ctype is None else (ctypes.pointer(an_int_enum_ctype)), None if a_float_ctype is None else (ctypes.pointer(a_float_ctype)), None if a_float_enum_ctype is None else (ctypes.pointer(a_float_enum_ctype)), array_size_ctype, an_array_ctype, string_size_ctype, a_string_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        string_size_ctype = visatype.ViInt32(error_code)  # case S180
        a_string_ctype = (visatype.ViChar * string_size_ctype.value)()  # case C060
        error_code = self._library.niFake_ReturnMultipleTypes(vi_ctype, None if a_boolean_ctype is None else (ctypes.pointer(a_boolean_ctype)), None if an_int32_ctype is None else (ctypes.pointer(an_int32_ctype)), None if an_int64_ctype is None else (ctypes.pointer(an_int64_ctype)), None if an_int_enum_ctype is None else (ctypes.pointer(an_int_enum_ctype)), None if a_float_ctype is None else (ctypes.pointer(a_float_ctype)), None if a_float_enum_ctype is None else (ctypes.pointer(a_float_enum_ctype)), array_size_ctype, an_array_ctype, string_size_ctype, a_string_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(a_boolean_ctype.value), int(an_int32_ctype.value), int(an_int64_ctype.value), enums.Turtle(an_int_enum_ctype.value), float(a_float_ctype.value), enums.FloatEnum(a_float_enum_ctype.value), [float(an_array_ctype[i]) for i in range(array_size_ctype.value)], a_string_ctype.value.decode(self._encoding)

    def set_custom_type(self, cs):
        '''set_custom_type

        This method takes a custom type.

        Args:
            cs (CustomStruct): Set using custom type

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        cs_ctype = custom_struct.custom_struct(cs)  # case S150
        error_code = self._library.niFake_SetCustomType(vi_ctype, cs_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_custom_type_array(self, cs):
        '''set_custom_type_array

        This method takes an array of custom types.

        Args:
            cs (list of CustomStruct): Set using custom type

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        number_of_elements_ctype = visatype.ViInt32(0 if cs is None else len(cs))  # case S160
        cs_ctype = get_ctypes_pointer_for_buffer([custom_struct.custom_struct(c) for c in cs], library_type=custom_struct.custom_struct)  # case B540
        error_code = self._library.niFake_SetCustomTypeArray(vi_ctype, number_of_elements_ctype, cs_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def two_input_function(self, a_number, a_string):
        '''two_input_function

        This method takes two parameters other than the session.

        Args:
            a_number (float): Contains a number

            a_string (str): Contains a string

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        a_number_ctype = visatype.ViReal64(a_number)  # case S150
        a_string_ctype = ctypes.create_string_buffer(a_string.encode(self._encoding))  # case C020
        error_code = self._library.niFake_TwoInputFunction(vi_ctype, a_number_ctype, a_string_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def use64_bit_number(self, input):
        '''use64_bit_number

        Returns a number and a string.

        Note: This method rules!

        Args:
            input (int): A big number on its way in.


        Returns:
            output (int): A big number on its way out.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        input_ctype = visatype.ViInt64(input)  # case S150
        output_ctype = visatype.ViInt64()  # case S200
        error_code = self._library.niFake_Use64BitNumber(vi_ctype, input_ctype, None if output_ctype is None else (ctypes.pointer(output_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(output_ctype.value)

    def write_waveform(self, waveform):
        '''write_waveform

        Writes waveform to the driver

        Args:
            waveform (array.array("d")): Waveform data.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        number_of_samples_ctype = visatype.ViInt32(0 if waveform is None else len(waveform))  # case S160
        waveform_array = get_ctypes_and_array(value=waveform, array_type="d")  # case B550
        waveform_ctype = get_ctypes_pointer_for_buffer(value=waveform_array, library_type=visatype.ViReal64)  # case B550
        error_code = self._library.niFake_WriteWaveform(vi_ctype, number_of_samples_ctype, waveform_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def write_waveform_numpy(self, waveform):
        '''write_waveform

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
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        number_of_samples_ctype = visatype.ViInt32(0 if waveform is None else len(waveform))  # case S160
        waveform_ctype = get_ctypes_pointer_for_buffer(value=waveform)  # case B510
        error_code = self._library.niFake_WriteWaveform(vi_ctype, number_of_samples_ctype, waveform_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _close(self):
        '''_close

        Closes the specified session and deallocates resources that it reserved.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFake_close(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return



