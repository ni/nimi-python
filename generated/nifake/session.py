# -*- coding: utf-8 -*-
# This file was generated
import ctypes

from nifake import ctypes_types
from nifake import enums
from nifake import errors
from nifake import library
from nifake import python_types


class AttributeViInt32(object):

    def __init__(self, attribute_id):
        self.attribute_id = attribute_id
        self.channel = ''

    def __get__(self, obj, objtype):
        assert objtype is Session
        return obj._get_attribute_vi_int32(self.channel, self.attribute_id)

    def __set__(self, obj, value):
        obj._set_attribute_vi_int32(self.channel, self.attribute_id, value)


class AttributeViReal64(object):

    def __init__(self, attribute_id):
        self.attribute_id = attribute_id
        self.channel = ''

    def __get__(self, obj, objtype):
        assert objtype is Session
        return obj._get_attribute_vi_real64(self.channel, self.attribute_id)

    def __set__(self, obj, value):
        obj._set_attribute_vi_real64(self.channel, self.attribute_id, value)


class AttributeViString(object):

    def __init__(self, attribute_id):
        self.attribute_id = attribute_id
        self.channel = ''

    def __get__(self, obj, objtype):
        assert objtype is Session
        return obj._get_attribute_vi_string(self.channel, self.attribute_id)

    def __set__(self, obj, value):
        obj._set_attribute_vi_string(self.channel, self.attribute_id, value)


class AttributeViBoolean(object):

    def __init__(self, attribute_id):
        self.attribute_id = attribute_id
        self.channel = ''

    def __get__(self, obj, objtype):
        assert objtype is Session
        return obj._get_attribute_vi_boolean(self.channel, self.attribute_id)

    def __set__(self, obj, value):
        obj._set_attribute_vi_boolean(self.channel, self.attribute_id, value)


class AttributeEnum(object):

    def __init__(self, attribute_id, enum_meta_class):
        self.attribute_id = attribute_id
        self.attribute_type = enum_meta_class
        self.channel = ''

    def __get__(self, obj, objtype):
        assert objtype is Session
        return self.attribute_type(obj._get_attribute_vi_int32(self.channel, self.attribute_id))

    def __set__(self, obj, value):
        if type(value) is not self.attribute_type:
            raise TypeError('Value mode must be of type ' + str(self.attribute_type))
        obj._set_attribute_vi_int32(self.channel, self.attribute_id, value.value)


class Acquisition(object):
    def __init__(self, session):
        self.session = session

    def __enter__(self):
        self.session._initiate()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.session._abort()


class Session(object):
    '''An NI-FAKE session to a fake MI driver whose sole purpose is to test nimi-python code generation'''

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

    read_write_bool = AttributeViBoolean(1000000)
    '''
    An attribute of type bool with read/write access.
    '''
    read_write_color = AttributeEnum(1000003, enums.Color)
    '''
    An attribute of type Color with read/write access.
    '''
    read_write_double = AttributeViReal64(1000001)
    '''
    An attribute of type float with read/write access.
    '''
    read_write_string = AttributeViString(1000002)
    '''
    An attribute of type string with read/write access.
    '''

    def __init__(self, resource_name, id_query=0, reset_device=False, options_string=""):
        self.library = library.get_library()
        self.vi = 0  # This must be set before calling _init_with_options.
        self.vi = self._init_with_options(resource_name, id_query, reset_device, options_string)

        self._is_frozen = True

    def __setattr__(self, key, value):
        if self._is_frozen and key not in dir(self):
            raise TypeError("%r is a frozen class" % self)
        object.__setattr__(self, key, value)

    def initiate(self):
        return Acquisition(self)

    def __del__(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        # TODO(marcoskirsch): Should we raise an exception on double close? Look at what File does.
        try:
            self._close()
        except errors.Error:
            # TODO(marcoskirsch): This will occur when session is "stolen". Change to log instead
            print("Failed to close session.")
        self.vi = 0

    # method needed for generic driver exceptions
    def _get_error_description(self, error_code):
        try:
            '''
            Return code > 0 from first call to GetError represents the size of
            the description.  Call it again.
            Ignore incoming IVI error code and return description from the driver
            (trust that the IVI error code was properly stored in the session
            by the driver)
            '''
            # TODO(texasaggie97) This currently does not work - _get_error() will raise
            # an exception that then calls this function, causing infinite recursion.
            # Fix is beyond the scope of this PR
            # Also fix documentation.
            (new_error_code, new_error_string) = self._get_error()
            return new_error_code, new_error_string
        except errors.Error:
            '''
            Return code <= 0 from GetError indicates a problem.  This is expected
            when the session is invalid (IVI spec requires GetError to fail).
            Use GetErrorMessage instead.  It doesn't require a session.

            Call niFake_GetErrorMessage, pass VI_NULL for the buffer in order to retrieve
            the length of the error message.
            '''
            new_error_string = self._get_error_message(error_code)
            return error_code, new_error_string

    ''' These are code-generated '''

    def _abort(self):
        '''_abort

        Aborts a previously initiated thingie.
        '''
        error_code = self.library.niFake_Abort(self.vi)
        errors._handle_error(self, error_code)
        return

    def _clear_error(self):
        '''_clear_error

        Clears the error for the current thread and session
        '''
        error_code = self.library.niFake_ClearError(self.vi)
        errors._handle_error(self, error_code)
        return

    def get_a_number(self):
        '''get_a_number

        Returns a number.

        Note: This function rules!

        Returns:
            a_number (int):Contains a number.
        '''
        a_number_ctype = ctypes_types.ViInt16_ctype(0)
        error_code = self.library.niFake_GetANumber(self.vi, ctypes.pointer(a_number_ctype))
        errors._handle_error(self, error_code)
        return python_types.ViInt16(a_number_ctype.value)

    def get_a_string_of_fixed_maximum_size(self):
        '''get_a_string_of_fixed_maximum_size

        Illustrates resturning a string of fixed size.

        Returns:
            a_string (int):String comes back here. Buffer must be 256 big.
        '''
        a_string_ctype = ctypes_types.ViChar_ctype(0)
        error_code = self.library.niFake_GetAStringOfFixedMaximumSize(self.vi, ctypes.pointer(a_string_ctype))
        errors._handle_error(self, error_code)
        return python_types.ViChar(a_string_ctype.value)

    def get_a_string_with_specified_maximum_size(self, buffer_size):
        '''get_a_string_with_specified_maximum_size

        Illustrates resturning a string where user specifies the size.

        Args:
            buffer_size (int):String comes back here. Buffer must be 256 big.

        Returns:
            a_string (int):String comes back here. Buffer must be at least bufferSize big.
        '''
        a_string_ctype = ctypes_types.ViChar_ctype(0)
        error_code = self.library.niFake_GetAStringWithSpecifiedMaximumSize(self.vi, ctypes.pointer(a_string_ctype), buffer_size)
        errors._handle_error(self, error_code)
        return python_types.ViChar(a_string_ctype.value)

    def _get_attribute_vi_boolean(self, channel_name, attribute_id):
        '''_get_attribute_vi_boolean

        Queries the value of a ViBoolean attribute.

        Args:
            channel_name (str):This is the channel(s) that this function will apply to.
            attribute_id (int):Pass the ID of an attribute.

        Returns:
            attribute_value (bool):Returns the value of the attribute.
        '''
        attribute_value_ctype = ctypes_types.ViBoolean_ctype(0)
        error_code = self.library.niFake_GetAttributeViBoolean(self.vi, channel_name.encode('ascii'), attribute_id, ctypes.pointer(attribute_value_ctype))
        errors._handle_error(self, error_code)
        return python_types.ViBoolean(attribute_value_ctype.value)

    def _get_attribute_vi_int32(self, channel_name, attribute_id):
        '''_get_attribute_vi_int32

        Queries the value of a ViInt32 attribute.

        Args:
            channel_name (str):This is the channel(s) that this function will apply to.
            attribute_id (int):Pass the ID of an attribute.

        Returns:
            attribute_value (int):Returns the value of the attribute.
        '''
        attribute_value_ctype = ctypes_types.ViInt32_ctype(0)
        error_code = self.library.niFake_GetAttributeViInt32(self.vi, channel_name.encode('ascii'), attribute_id, ctypes.pointer(attribute_value_ctype))
        errors._handle_error(self, error_code)
        return python_types.ViInt32(attribute_value_ctype.value)

    def _get_attribute_vi_real64(self, channel_name, attribute_id):
        '''_get_attribute_vi_real64

        Queries the value of a ViReal attribute.

        Args:
            channel_name (str):This is the channel(s) that this function will apply to.
            attribute_id (int):Pass the ID of an attribute.

        Returns:
            attribute_value (float):Returns the value of the attribute.
        '''
        attribute_value_ctype = ctypes_types.ViReal64_ctype(0)
        error_code = self.library.niFake_GetAttributeViReal64(self.vi, channel_name.encode('ascii'), attribute_id, ctypes.pointer(attribute_value_ctype))
        errors._handle_error(self, error_code)
        return python_types.ViReal64(attribute_value_ctype.value)

    def _get_attribute_vi_session(self, channel_name, attribute_id):
        '''_get_attribute_vi_session

        Queries the value of a ViSession attribute.

        Args:
            channel_name (str):This is the channel(s) that this function will apply to.
            attribute_id (int):Pass the ID of an attribute.

        Returns:
            attribute_value (int):Returns the value of the attribute.
        '''
        attribute_value_ctype = ctypes_types.ViSession_ctype(0)
        error_code = self.library.niFake_GetAttributeViSession(self.vi, channel_name.encode('ascii'), attribute_id, ctypes.pointer(attribute_value_ctype))
        errors._handle_error(self, error_code)
        return python_types.ViSession(attribute_value_ctype.value)

    def _get_attribute_vi_string(self, channel_name, attribute_id):
        '''_get_attribute_vi_string

        Queries the value of a ViBoolean attribute.

        Args:
            channel_name (str):This is the channel(s) that this function will apply to.
            attribute_id (int):Pass the ID of an attribute.
            buffer_size (int):Number of bytes in attributeValue. You can IVI-dance with this.
        '''
        buffer_size = 0
        attribute_value_ctype = None
        error_code = self.library.niFake_GetAttributeViString(self.vi, channel_name.encode('ascii'), attribute_id, buffer_size, attribute_value_ctype)
        # Don't use _handle_error, because positive value in error_code means size, not warning.
        if (errors._is_error(error_code)):
            raise errors.Error(self, error_code)
        buffer_size = error_code
        attribute_value_ctype = ctypes.cast(ctypes.create_string_buffer(buffer_size), ctypes_types.ViString_ctype)
        error_code = self.library.niFake_GetAttributeViString(self.vi, channel_name.encode('ascii'), attribute_id, buffer_size, attribute_value_ctype)
        errors._handle_error(self, error_code)
        return attribute_value_ctype.value.decode("ascii")

    def get_enum_value(self):
        '''get_enum_value

        Returns an enum value

        Note: Splinter is not supported.

        Returns:
            a_quantity (int):This is an amount.

                Note: The amount will be between -2^31 and (2^31-1)
            a_turtle (enums.Turtle):Indicates a ninja turtle

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
        a_quantity_ctype = ctypes_types.ViInt32_ctype(0)
        a_turtle_ctype = ctypes_types.ViInt16_ctype(0)
        error_code = self.library.niFake_GetEnumValue(self.vi, ctypes.pointer(a_quantity_ctype), ctypes.pointer(a_turtle_ctype))
        errors._handle_error(self, error_code)
        return python_types.ViInt32(a_quantity_ctype.value), enums.Turtle(a_turtle_ctype.value)

    def _get_error(self):
        '''_get_error

        Returns the error information associated with the session.

        Args:
            buffer_size (int):Number of bytes in description buffer.

        Returns:
            error_code (int):Returns errorCode for the session. If you pass 0 for bufferSize, you can pass VI_NULL for this.
        '''
        error_code_ctype = ctypes_types.ViStatus_ctype(0)
        buffer_size = 0
        description_ctype = None
        error_code = self.library.niFake_GetError(self.vi, ctypes.pointer(error_code_ctype), buffer_size, description_ctype)
        # Don't use _handle_error, because positive value in error_code means size, not warning.
        if (errors._is_error(error_code)):
            raise errors.Error(self, error_code)
        buffer_size = error_code
        description_ctype = ctypes.cast(ctypes.create_string_buffer(buffer_size), ctypes_types.ViString_ctype)
        error_code = self.library.niFake_GetError(self.vi, ctypes.pointer(error_code_ctype), buffer_size, description_ctype)
        errors._handle_error(self, error_code)
        return python_types.ViStatus(error_code_ctype.value), description_ctype.value.decode("ascii")

    def _get_error_message(self, error_code):
        '''_get_error_message

        Returns the errorMessage as a user-readable string. Uses IVI-dance

        Args:
            error_code (int):The error code returned for which you want to get a string.
            buffer_size (int):Number of bytes allocated for errorMessage
        '''
        buffer_size = 0
        error_message_ctype = None
        error_code = self.library.niFake_GetErrorMessage(self.vi, error_code, buffer_size, error_message_ctype)
        # Don't use _handle_error, because positive value in error_code means size, not warning.
        if (errors._is_error(error_code)):
            raise errors.Error(self, error_code)
        buffer_size = error_code
        error_message_ctype = ctypes.cast(ctypes.create_string_buffer(buffer_size), ctypes_types.ViChar_ctype)
        error_code = self.library.niFake_GetErrorMessage(self.vi, error_code, buffer_size, error_message_ctype)
        errors._handle_error(self, error_code)
        return error_message_ctype.value.decode("ascii")

    def _init_with_options(self, resource_name, id_query, reset_device, option_string):
        '''_init_with_options

        Creates a new IVI instrument driver session.

        Args:
            resource_name (str):Caution: This is just some string.

                Contains the **resource_name** of the device to initialize.
            id_query (bool):NI-FAKE is probably not needed.

                +-------------------+---+------------------+
                | VI_TRUE (default) | 1 | Perform ID Query |
                +-------------------+---+------------------+
                | VI_FALSE          | 0 | Skip ID Query    |
                +-------------------+---+------------------+
            reset_device (bool):Specifies whether to reset

                +-------------------+---+--------------+
                | VI_TRUE (default) | 1 | Reset Device |
                +-------------------+---+--------------+
                | VI_FALSE          | 0 | Don't Reset  |
                +-------------------+---+--------------+
            option_string (str):Some options

        Returns:
            vi (int):Returns a ViSession handle that you use.
        '''
        vi_ctype = ctypes_types.ViSession_ctype(0)
        error_code = self.library.niFake_InitWithOptions(resource_name.encode('ascii'), id_query, reset_device, option_string.encode('ascii'), ctypes.pointer(vi_ctype))
        errors._handle_error(self, error_code)
        return python_types.ViSession(vi_ctype.value)

    def _initiate(self):
        '''_initiate

        Initiates a thingie.
        '''
        error_code = self.library.niFake_Initiate(self.vi)
        errors._handle_error(self, error_code)
        return

    def read(self, maximum_time):
        '''read

        Acquires a single measurement and returns the measured value.

        Args:
            maximum_time (int):Specifies the **maximum_time** allowed in years.

        Returns:
            reading (float):The measured value.
        '''
        reading_ctype = ctypes_types.ViReal64_ctype(0)
        error_code = self.library.niFake_Read(self.vi, maximum_time, ctypes.pointer(reading_ctype))
        errors._handle_error(self, error_code)
        return python_types.ViReal64(reading_ctype.value)

    def read_multi_point(self, maximum_time, array_size):
        '''read_multi_point

        Acquires multiple measurements and returns an array of measured values.

        Args:
            maximum_time (int):Specifies the **maximum_time** allowed in years.
            array_size (int):Number of measurements to acquire.

        Returns:
            reading_array (float):An array of measurement values.

                Note: The size must be at least arraySize.
            actual_number_of_points (int):Indicates the number of measured values actually retrieved.
        '''
        reading_array_ctype = (ctypes_types.ViReal64_ctype * array_size)()
        actual_number_of_points_ctype = ctypes_types.ViInt32_ctype(0)
        error_code = self.library.niFake_ReadMultiPoint(self.vi, maximum_time, array_size, ctypes.cast(reading_array_ctype, ctypes.POINTER(ctypes_types.ViReal64_ctype)), ctypes.pointer(actual_number_of_points_ctype))
        errors._handle_error(self, error_code)
        return [python_types.ViReal64(reading_array_ctype[i].value) for i in range(array_size)], python_types.ViInt32(actual_number_of_points_ctype.value)

    def return_a_number_and_a_string(self):
        '''return_a_number_and_a_string

        Returns a number and a string.

        Note: This function rules!

        Returns:
            a_number (int):Contains a number.
            a_string (int):Contains a string.
        '''
        a_number_ctype = ctypes_types.ViInt16_ctype(0)
        a_string_ctype = ctypes_types.ViChar_ctype(0)
        error_code = self.library.niFake_ReturnANumberAndAString(self.vi, ctypes.pointer(a_number_ctype), ctypes.pointer(a_string_ctype))
        errors._handle_error(self, error_code)
        return python_types.ViInt16(a_number_ctype.value), python_types.ViChar(a_string_ctype.value)

    def _set_attribute_vi_boolean(self, channel_name, attribute_id, attribute_value):
        '''_set_attribute_vi_boolean

        This function sets the value of a ViBoolean attribute.

        Args:
            channel_name (str):This is the channel(s) that this function will apply to.
            attribute_id (int):Pass the ID of an attribute.
            attribute_value (bool):Pass the value that you want to set the attribute to.
        '''
        error_code = self.library.niFake_SetAttributeViBoolean(self.vi, channel_name.encode('ascii'), attribute_id, attribute_value)
        errors._handle_error(self, error_code)
        return

    def _set_attribute_vi_int32(self, channel_name, attribute_id, attribute_value):
        '''_set_attribute_vi_int32

        This function sets the value of a ViInt32 attribute.

        Args:
            channel_name (str):This is the channel(s) that this function will apply to.
            attribute_id (int):Pass the ID of an attribute.
            attribute_value (int):Pass the value that you want to set the attribute to.
        '''
        error_code = self.library.niFake_SetAttributeViInt32(self.vi, channel_name.encode('ascii'), attribute_id, attribute_value)
        errors._handle_error(self, error_code)
        return

    def _set_attribute_vi_real64(self, channel_name, attribute_id, attribute_value):
        '''_set_attribute_vi_real64

        This function sets the value of a ViReal64 attribute.

        Args:
            channel_name (str):This is the channel(s) that this function will apply to.
            attribute_id (int):Pass the ID of an attribute.
            attribute_value (float):Pass the value that you want to set the attribute to.
        '''
        error_code = self.library.niFake_SetAttributeViReal64(self.vi, channel_name.encode('ascii'), attribute_id, attribute_value)
        errors._handle_error(self, error_code)
        return

    def _set_attribute_vi_session(self, channel_name, attribute_id, attribute_value):
        '''_set_attribute_vi_session

        This function sets the value of a ViSession attribute.

        Args:
            channel_name (str):This is the channel(s) that this function will apply to.
            attribute_id (int):Pass the ID of an attribute.
            attribute_value (int):Pass the value that you want to set the attribute to.
        '''
        error_code = self.library.niFake_SetAttributeViSession(self.vi, channel_name.encode('ascii'), attribute_id, attribute_value)
        errors._handle_error(self, error_code)
        return

    def _set_attribute_vi_string(self, channel_name, attribute_id, attribute_value):
        '''_set_attribute_vi_string

        This function sets the value of a ViString attribute.

        Args:
            channel_name (str):This is the channel(s) that this function will apply to.
            attribute_id (int):Pass the ID of an attribute.
            attribute_value (str):Pass the value that you want to set the attribute to.
        '''
        error_code = self.library.niFake_SetAttributeViString(self.vi, channel_name.encode('ascii'), attribute_id, attribute_value.encode('ascii'))
        errors._handle_error(self, error_code)
        return

    def simple_function(self):
        '''simple_function

        This function takes no parameters other than the session.
        '''
        error_code = self.library.niFake_SimpleFunction(self.vi)
        errors._handle_error(self, error_code)
        return

    def _close(self):
        '''_close

        Closes the specified session and deallocates resources that it reserved.
        '''
        error_code = self.library.niFake_close(self.vi)
        errors._handle_error(self, error_code)
        return

    def error_message(self, error_code):
        '''error_message

        Takes the errorCode returned by a functiona and returns it as a user-readable string.

        Args:
            error_code (int):The errorCode returned from the instrument.

        Returns:
            error_message (int):The error information formatted into a string.
        '''
        error_message_ctype = ctypes_types.ViChar_ctype(0)
        error_code = self.library.niFake_error_message(self.vi, error_code, ctypes.pointer(error_message_ctype))
        errors._handle_error(self, error_code)
        return python_types.ViChar(error_message_ctype.value)
