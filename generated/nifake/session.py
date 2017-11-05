# -*- coding: utf-8 -*-
# This file was generated
import ctypes

from nifake import attributes
from nifake import enums
from nifake import errors
from nifake import library_singleton
from nifake import visatype

from nifake import custom_struct  # noqa: F401


class _Acquisition(object):
    def __init__(self, session):
        self._session = session

    def __enter__(self):
        self._session._initiate()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._session._abort()


class _SessionBase(object):
    '''Base class for all NI-FAKE sessions.'''

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

    float_enum = attributes.AttributeEnum(attributes.AttributeViReal64, enums.FloatEnum, 1000005)
    '''
    An attribute with an enum that is also a float
    '''
    read_write_bool = attributes.AttributeViBoolean(1000000)
    '''
    An attribute of type bool with read/write access.
    '''
    read_write_color = attributes.AttributeEnum(attributes.AttributeViInt32, enums.Color, 1000003)
    '''
    An attribute of type Color with read/write access.
    '''
    read_write_double = attributes.AttributeViReal64(1000001)
    '''
    An attribute of type float with read/write access.
    '''
    read_write_int64 = attributes.AttributeViInt64(1000006)
    '''
    An attribute of type 64-bit integer with read/write access.
    '''
    read_write_integer = attributes.AttributeViInt32(1000004)
    '''
    An attribute of type integer with read/write access.
    '''
    read_write_string = attributes.AttributeViString(1000002)
    '''
    An attribute of type string with read/write access.
    '''

    def __init__(self, repeated_capability):
        self._library = library_singleton.get()
        self._repeated_capability = repeated_capability
        self._encoding = 'windows-1251'

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

        Queries the value of a ViBoolean attribute.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifake.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifake.Session instance, and calling this method on the result.:

            session['0,1']._get_attribute_vi_boolean(attribute_id)

        Args:
            attribute_id (int): Pass the ID of an attribute.

        Returns:
            attribute_value (bool): Returns the value of the attribute.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case 8
        attribute_value_ctype = visatype.ViBoolean()  # case 13
        error_code = self._library.niFake_GetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_id_ctype, ctypes.pointer(attribute_value_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(attribute_value_ctype.value)

    def _get_attribute_vi_int32(self, attribute_id):
        '''_get_attribute_vi_int32

        Queries the value of a ViInt32 attribute.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifake.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifake.Session instance, and calling this method on the result.:

            session['0,1']._get_attribute_vi_int32(attribute_id)

        Args:
            attribute_id (int): Pass the ID of an attribute.

        Returns:
            attribute_value (int): Returns the value of the attribute.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case 8
        attribute_value_ctype = visatype.ViInt32()  # case 13
        error_code = self._library.niFake_GetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_id_ctype, ctypes.pointer(attribute_value_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(attribute_value_ctype.value)

    def _get_attribute_vi_int64(self, attribute_id):
        '''_get_attribute_vi_int64

        Queries the value of a ViInt64 attribute.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifake.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifake.Session instance, and calling this method on the result.:

            session['0,1']._get_attribute_vi_int64(attribute_id)

        Args:
            attribute_id (int): Pass the ID of an attribute.

        Returns:
            attribute_value (int): Returns the value of the attribute.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case 8
        attribute_value_ctype = visatype.ViInt64()  # case 13
        error_code = self._library.niFake_GetAttributeViInt64(vi_ctype, channel_name_ctype, attribute_id_ctype, ctypes.pointer(attribute_value_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(attribute_value_ctype.value)

    def _get_attribute_vi_real64(self, attribute_id):
        '''_get_attribute_vi_real64

        Queries the value of a ViReal attribute.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifake.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifake.Session instance, and calling this method on the result.:

            session['0,1']._get_attribute_vi_real64(attribute_id)

        Args:
            attribute_id (int): Pass the ID of an attribute.

        Returns:
            attribute_value (float): Returns the value of the attribute.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case 8
        attribute_value_ctype = visatype.ViReal64()  # case 13
        error_code = self._library.niFake_GetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_id_ctype, ctypes.pointer(attribute_value_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(attribute_value_ctype.value)

    def _get_attribute_vi_string(self, attribute_id):
        '''_get_attribute_vi_string

        Queries the value of a ViBoolean attribute.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifake.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifake.Session instance, and calling this method on the result.:

            session['0,1']._get_attribute_vi_string(attribute_id)

        Args:
            attribute_id (int): Pass the ID of an attribute.
            buffer_size (int): Number of bytes in attributeValue. You can IVI-dance with this.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case 8
        buffer_size_ctype = visatype.ViInt32()  # case 6
        attribute_value_ctype = None  # case 11
        error_code = self._library.niFake_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, buffer_size_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = visatype.ViInt32(error_code)  # TODO(marcoskirsch): use get_ctype_variable_declaration_snippet()
        attribute_value_ctype = (visatype.ViChar * buffer_size_ctype.value)()  # TODO(marcoskirsch): use get_ctype_variable_declaration_snippet()
        error_code = self._library.niFake_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, buffer_size_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return attribute_value_ctype.value.decode(self._encoding)

    def _get_error(self):
        '''_get_error

        Returns the error information associated with the session.

        Args:
            buffer_size (int): Number of bytes in description buffer.

        Returns:
            error_code (int): Returns errorCode for the session. If you pass 0 for bufferSize, you can pass VI_NULL for this.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        error_code_ctype = visatype.ViStatus()  # case 13
        buffer_size_ctype = visatype.ViInt32()  # case 6
        description_ctype = None  # case 11
        error_code = self._library.niFake_GetError(vi_ctype, ctypes.pointer(error_code_ctype), buffer_size_ctype, description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=True)
        buffer_size_ctype = visatype.ViInt32(error_code)  # TODO(marcoskirsch): use get_ctype_variable_declaration_snippet()
        description_ctype = (visatype.ViChar * buffer_size_ctype.value)()  # TODO(marcoskirsch): use get_ctype_variable_declaration_snippet()
        error_code = self._library.niFake_GetError(vi_ctype, ctypes.pointer(error_code_ctype), buffer_size_ctype, description_ctype)
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

            session['0,1'].read_from_channel(maximum_time)

        Args:
            maximum_time (int): Specifies the **maximum_time** allowed in years.

        Returns:
            reading (float): The measured value.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        maximum_time_ctype = visatype.ViInt32(maximum_time)  # case 8
        reading_ctype = visatype.ViReal64()  # case 13
        error_code = self._library.niFake_ReadFromChannel(vi_ctype, channel_name_ctype, maximum_time_ctype, ctypes.pointer(reading_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(reading_ctype.value)

    def _set_attribute_vi_boolean(self, attribute_id, attribute_value):
        '''_set_attribute_vi_boolean

        This function sets the value of a ViBoolean attribute.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifake.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifake.Session instance, and calling this method on the result.:

            session['0,1']._set_attribute_vi_boolean(attribute_id, attribute_value)

        Args:
            attribute_id (int): Pass the ID of an attribute.
            attribute_value (bool): Pass the value that you want to set the attribute to.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case 8
        attribute_value_ctype = visatype.ViBoolean(attribute_value)  # case 8
        error_code = self._library.niFake_SetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_int32(self, attribute_id, attribute_value):
        '''_set_attribute_vi_int32

        This function sets the value of a ViInt32 attribute.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifake.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifake.Session instance, and calling this method on the result.:

            session['0,1']._set_attribute_vi_int32(attribute_id, attribute_value)

        Args:
            attribute_id (int): Pass the ID of an attribute.
            attribute_value (int): Pass the value that you want to set the attribute to.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case 8
        attribute_value_ctype = visatype.ViInt32(attribute_value)  # case 8
        error_code = self._library.niFake_SetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_int64(self, attribute_id, attribute_value):
        '''_set_attribute_vi_int64

        This function sets the value of a ViInt64 attribute.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifake.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifake.Session instance, and calling this method on the result.:

            session['0,1']._set_attribute_vi_int64(attribute_id, attribute_value)

        Args:
            attribute_id (int): Pass the ID of an attribute.
            attribute_value (int): Pass the value that you want to set the attribute to.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case 8
        attribute_value_ctype = visatype.ViInt64(attribute_value)  # case 8
        error_code = self._library.niFake_SetAttributeViInt64(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_real64(self, attribute_id, attribute_value):
        '''_set_attribute_vi_real64

        This function sets the value of a ViReal64 attribute.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifake.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifake.Session instance, and calling this method on the result.:

            session['0,1']._set_attribute_vi_real64(attribute_id, attribute_value)

        Args:
            attribute_id (int): Pass the ID of an attribute.
            attribute_value (float): Pass the value that you want to set the attribute to.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case 8
        attribute_value_ctype = visatype.ViReal64(attribute_value)  # case 8
        error_code = self._library.niFake_SetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_string(self, attribute_id, attribute_value):
        '''_set_attribute_vi_string

        This function sets the value of a ViString attribute.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifake.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifake.Session instance, and calling this method on the result.:

            session['0,1']._set_attribute_vi_string(attribute_id, attribute_value)

        Args:
            attribute_id (int): Pass the ID of an attribute.
            attribute_value (string): Pass the value that you want to set the attribute to.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case 8
        attribute_value_ctype = ctypes.create_string_buffer(attribute_value.encode(self._encoding))  # case 3
        error_code = self._library.niFake_SetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _error_message(self, error_code):
        '''_error_message

        Takes the errorCode returned by a functiona and returns it as a user-readable string.

        Args:
            error_code (int): The errorCode returned from the instrument.

        Returns:
            error_message (string): The error information formatted into a string.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        error_code_ctype = visatype.ViStatus(error_code)  # case 8
        error_message_ctype = (visatype.ViChar * 256)()  # case 10
        error_code = self._library.niFake_error_message(vi_ctype, error_code_ctype, error_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return error_message_ctype.value.decode(self._encoding)


class _RepeatedCapability(_SessionBase):
    '''Allows for setting/getting properties and calling methods for specific repeated capabilities (such as channels) on your session.'''

    def __init__(self, vi, repeated_capability):
        super(_RepeatedCapability, self).__init__(repeated_capability)
        self._vi = vi
        self._is_frozen = True


class Session(_SessionBase):
    '''An NI-FAKE session to a fake MI driver whose sole purpose is to test nimi-python code generation'''

    def __init__(self, resource_name, id_query=False, reset_device=False, option_string=''):
        super(Session, self).__init__(repeated_capability='')
        self._vi = 0  # This must be set before calling _init_with_options().
        self._vi = self._init_with_options(resource_name, id_query, reset_device, option_string)
        self._is_frozen = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def __getitem__(self, repeated_capability):
        '''Set/get properties or call methods with a repeated capability (i.e. channels)'''
        return _RepeatedCapability(self._vi, repeated_capability)

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

    def _abort(self):
        '''_abort

        Aborts a previously initiated thingie.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        error_code = self._library.niFake_Abort(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def array_input_function(self, an_array):
        '''array_input_function

        This function takes an array parameter.

        Args:
            number_of_elements (int): Number of elements in the array.
            an_array (list of float): Contains an array of float numbers
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        number_of_elements_ctype = visatype.ViInt32(len(an_array))  # case 5
        an_array_ctype = (visatype.ViReal64 * len(an_array))(*an_array)  # case 4
        error_code = self._library.niFake_ArrayInputFunction(vi_ctype, number_of_elements_ctype, an_array_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def bool_array_output_function(self, number_of_elements):
        '''bool_array_output_function

        This function returns an array of booleans.

        Args:
            number_of_elements (int): Number of elements in the array.

        Returns:
            an_array (list of bool): Contains an array of booleans
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        number_of_elements_ctype = visatype.ViInt32(number_of_elements)  # case 7
        an_array_ctype = (visatype.ViBoolean * number_of_elements)()  # case 12
        error_code = self._library.niFake_BoolArrayOutputFunction(vi_ctype, number_of_elements_ctype, an_array_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [bool(an_array_ctype[i]) for i in range(number_of_elements_ctype.value)]

    def enum_array_output_function(self, number_of_elements):
        '''enum_array_output_function

        This function returns an array of enums, stored as 16 bit integers under the hood.

        Args:
            number_of_elements (int): Number of elements in the array.

        Returns:
            an_array (list of enums.Turtle): Contains an array of enums, stored as 16 bit integers under the hood
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        number_of_elements_ctype = visatype.ViInt32(number_of_elements)  # case 7
        an_array_ctype = (visatype.ViInt16 * number_of_elements)()  # case 12
        error_code = self._library.niFake_EnumArrayOutputFunction(vi_ctype, number_of_elements_ctype, an_array_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [enums.Turtle(an_array_ctype[i]) for i in range(number_of_elements_ctype.value)]

    def enum_input_function_with_defaults(self, a_turtle=enums.Turtle.LEONARDO):
        '''enum_input_function_with_defaults

        This function takes one parameter other than the session, which happens to be an enum and has a default value defined in functions_addon.

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
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        a_turtle_ctype = visatype.ViInt16(a_turtle.value)  # case 9
        error_code = self._library.niFake_EnumInputFunctionWithDefaults(vi_ctype, a_turtle_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def get_a_boolean(self):
        '''get_a_boolean

        Returns a boolean.

        Note: This function rules!

        Returns:
            a_boolean (bool): Contains a boolean.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        a_boolean_ctype = visatype.ViBoolean()  # case 13
        error_code = self._library.niFake_GetABoolean(vi_ctype, ctypes.pointer(a_boolean_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(a_boolean_ctype.value)

    def get_a_number(self):
        '''get_a_number

        Returns a number.

        Note: This function rules!

        Returns:
            a_number (int): Contains a number.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        a_number_ctype = visatype.ViInt16()  # case 13
        error_code = self._library.niFake_GetANumber(vi_ctype, ctypes.pointer(a_number_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(a_number_ctype.value)

    def get_a_string_of_fixed_maximum_size(self):
        '''get_a_string_of_fixed_maximum_size

        Illustrates resturning a string of fixed size.

        Returns:
            a_string (string): String comes back here. Buffer must be 256 big.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        a_string_ctype = (visatype.ViChar * 256)()  # case 10
        error_code = self._library.niFake_GetAStringOfFixedMaximumSize(vi_ctype, a_string_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return a_string_ctype.value.decode(self._encoding)

    def get_an_ivi_dance_string(self):
        '''get_an_ivi_dance_string

        Returns a string using the IVI dance.

        Args:
            buffer_size (int): Number of bytes in aString You can IVI-dance with this.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        buffer_size_ctype = visatype.ViInt32()  # case 6
        a_string_ctype = None  # case 11
        error_code = self._library.niFake_GetAnIviDanceString(vi_ctype, buffer_size_ctype, a_string_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = visatype.ViInt32(error_code)  # TODO(marcoskirsch): use get_ctype_variable_declaration_snippet()
        a_string_ctype = (visatype.ViChar * buffer_size_ctype.value)()  # TODO(marcoskirsch): use get_ctype_variable_declaration_snippet()
        error_code = self._library.niFake_GetAnIviDanceString(vi_ctype, buffer_size_ctype, a_string_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return a_string_ctype.value.decode(self._encoding)

    def get_array_using_ivi_dance(self):
        '''get_array_using_ivi_dance

        This function returns an array of float whose size is determined with the IVI dance.

        Args:
            array_size (int): Specifies the size of the buffer for copyint arrayOut onto.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        array_size_ctype = visatype.ViInt32()  # case 6
        array_out_ctype = None  # case 11
        error_code = self._library.niFake_GetArrayUsingIVIDance(vi_ctype, array_size_ctype, array_out_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        array_size_ctype = visatype.ViInt32(error_code)  # TODO(marcoskirsch): use get_ctype_variable_declaration_snippet()
        array_out_ctype = (visatype.ViReal64 * array_size_ctype.value)()  # TODO(marcoskirsch): use get_ctype_variable_declaration_snippet()
        error_code = self._library.niFake_GetArrayUsingIVIDance(vi_ctype, array_size_ctype, array_out_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(array_out_ctype[i]) for i in range(array_size_ctype.value)]

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
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        a_quantity_ctype = visatype.ViInt32()  # case 13
        a_turtle_ctype = visatype.ViInt16()  # case 13
        error_code = self._library.niFake_GetEnumValue(vi_ctype, ctypes.pointer(a_quantity_ctype), ctypes.pointer(a_turtle_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(a_quantity_ctype.value), enums.Turtle(a_turtle_ctype.value)

    def _init_with_options(self, resource_name, id_query=False, reset_device=False, option_string=''):
        '''_init_with_options

        Creates a new IVI instrument driver session.

        Args:
            resource_name (string): Caution: This is just some string.

                Contains the **resource_name** of the device to initialize.
            id_query (bool): NI-FAKE is probably not needed.

                +-------------------+---+------------------+
                | VI_TRUE (default) | 1 | Perform ID Query |
                +-------------------+---+------------------+
                | VI_FALSE          | 0 | Skip ID Query    |
                +-------------------+---+------------------+
            reset_device (bool): Specifies whether to reset

                +-------------------+---+--------------+
                | VI_TRUE (default) | 1 | Reset Device |
                +-------------------+---+--------------+
                | VI_FALSE          | 0 | Don't Reset  |
                +-------------------+---+--------------+
            option_string (string): Some options

        Returns:
            vi (int): Returns a ViSession handle that you use.
        '''
        resource_name_ctype = ctypes.create_string_buffer(resource_name.encode(self._encoding))  # case 3
        id_query_ctype = visatype.ViBoolean(id_query)  # case 8
        reset_device_ctype = visatype.ViBoolean(reset_device)  # case 8
        option_string_ctype = ctypes.create_string_buffer(option_string.encode(self._encoding))  # case 3
        vi_ctype = visatype.ViSession()  # case 13
        error_code = self._library.niFake_InitWithOptions(resource_name_ctype, id_query_ctype, reset_device_ctype, option_string_ctype, ctypes.pointer(vi_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(vi_ctype.value)

    def _initiate(self):
        '''_initiate

        Initiates a thingie.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        error_code = self._library.niFake_Initiate(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def multiple_array_types(self, passed_in_array_size, len_array):
        '''multiple_array_types

        Returns multiple types of arrays.

        Args:
            passed_in_array_size (int): Number of measurements to acquire.
            len_array_size (int): Size of lenArray
            len_array (list of float): Contains an array of float numbers.

        Returns:
            passed_in_array (list of float): An array with size passed in.

                Note: The size must be at least arraySize.
            a_fixed_array (list of float): An array of doubles with fixed size.
        '''
        passed_in_array_size_ctype = visatype.ViInt32(passed_in_array_size)  # case 7
        passed_in_array_ctype = (visatype.ViReal64 * passed_in_array_size)()  # case 12
        a_fixed_array_ctype = (visatype.ViReal64 * 3)()  # case 10
        len_array_size_ctype = visatype.ViInt32(len(len_array))  # case 5
        len_array_ctype = (visatype.ViReal64 * len(len_array))(*len_array)  # case 4
        error_code = self._library.niFake_MultipleArrayTypes(passed_in_array_size_ctype, passed_in_array_ctype, a_fixed_array_ctype, len_array_size_ctype, len_array_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(passed_in_array_ctype[i]) for i in range(passed_in_array_size_ctype.value)], [float(a_fixed_array_ctype[i]) for i in range(3)]

    def one_input_function(self, a_number):
        '''one_input_function

        This function takes one parameter other than the session.

        Args:
            a_number (int): Contains a number
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        a_number_ctype = visatype.ViInt32(a_number)  # case 8
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
            string_size (int): Number of bytes allocated for aString
            a_string (string): An IVI dance string.
        '''
        if type(an_int_enum) is not enums.Turtle:
            raise TypeError('Parameter mode must be of type ' + str(enums.Turtle))
        if type(a_float_enum) is not enums.FloatEnum:
            raise TypeError('Parameter mode must be of type ' + str(enums.FloatEnum))
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        a_boolean_ctype = visatype.ViBoolean(a_boolean)  # case 8
        an_int32_ctype = visatype.ViInt32(an_int32)  # case 8
        an_int64_ctype = visatype.ViInt64(an_int64)  # case 8
        an_int_enum_ctype = visatype.ViInt16(an_int_enum.value)  # case 9
        a_float_ctype = visatype.ViReal64(a_float)  # case 8
        a_float_enum_ctype = visatype.ViReal64(a_float_enum.value)  # case 9
        string_size_ctype = visatype.ViInt32(len(a_string))  # case 5
        a_string_ctype = ctypes.create_string_buffer(a_string.encode(self._encoding))  # case 3
        error_code = self._library.niFake_ParametersAreMultipleTypes(vi_ctype, a_boolean_ctype, an_int32_ctype, an_int64_ctype, an_int_enum_ctype, a_float_ctype, a_float_enum_ctype, string_size_ctype, a_string_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def read(self, maximum_time):
        '''read

        Acquires a single measurement and returns the measured value.

        Args:
            maximum_time (int): Specifies the **maximum_time** allowed in years.

        Returns:
            reading (float): The measured value.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        maximum_time_ctype = visatype.ViInt32(maximum_time)  # case 8
        reading_ctype = visatype.ViReal64()  # case 13
        error_code = self._library.niFake_Read(vi_ctype, maximum_time_ctype, ctypes.pointer(reading_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(reading_ctype.value)

    def read_multi_point(self, maximum_time, array_size):
        '''read_multi_point

        Acquires multiple measurements and returns an array of measured values.

        Args:
            maximum_time (int): Specifies the **maximum_time** allowed in years.
            array_size (int): Number of measurements to acquire.

        Returns:
            reading_array (list of float): An array of measurement values.

                Note: The size must be at least arraySize.
            actual_number_of_points (int): Indicates the number of measured values actually retrieved.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        maximum_time_ctype = visatype.ViInt32(maximum_time)  # case 8
        array_size_ctype = visatype.ViInt32(array_size)  # case 7
        reading_array_ctype = (visatype.ViReal64 * array_size)()  # case 12
        actual_number_of_points_ctype = visatype.ViInt32()  # case 13
        error_code = self._library.niFake_ReadMultiPoint(vi_ctype, maximum_time_ctype, array_size_ctype, reading_array_ctype, ctypes.pointer(actual_number_of_points_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(reading_array_ctype[i]) for i in range(array_size_ctype.value)], int(actual_number_of_points_ctype.value)

    def return_a_number_and_a_string(self):
        '''return_a_number_and_a_string

        Returns a number and a string.

        Note: This function rules!

        Returns:
            a_number (int): Contains a number.
            a_string (string): Contains a string. Buffer must be 256 bytes or larger.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        a_number_ctype = visatype.ViInt16()  # case 13
        a_string_ctype = (visatype.ViChar * 256)()  # case 10
        error_code = self._library.niFake_ReturnANumberAndAString(vi_ctype, ctypes.pointer(a_number_ctype), a_string_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(a_number_ctype.value), a_string_ctype.value.decode(self._encoding)

    def return_multiple_types(self, array_size):
        '''return_multiple_types

        Returns multiple types.

        Args:
            array_size (int): Number of measurements to acquire.
            string_size (int): Number of bytes allocated for aString

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
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        a_boolean_ctype = visatype.ViBoolean()  # case 13
        an_int32_ctype = visatype.ViInt32()  # case 13
        an_int64_ctype = visatype.ViInt64()  # case 13
        an_int_enum_ctype = visatype.ViInt16()  # case 13
        a_float_ctype = visatype.ViReal64()  # case 13
        a_float_enum_ctype = visatype.ViReal64()  # case 13
        array_size_ctype = visatype.ViInt32(array_size)  # case 7
        an_array_ctype = (visatype.ViReal64 * array_size)()  # case 12
        string_size_ctype = visatype.ViInt32()  # case 6
        a_string_ctype = None  # case 11
        error_code = self._library.niFake_ReturnMultipleTypes(vi_ctype, ctypes.pointer(a_boolean_ctype), ctypes.pointer(an_int32_ctype), ctypes.pointer(an_int64_ctype), ctypes.pointer(an_int_enum_ctype), ctypes.pointer(a_float_ctype), ctypes.pointer(a_float_enum_ctype), array_size_ctype, an_array_ctype, string_size_ctype, a_string_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        string_size_ctype = visatype.ViInt32(error_code)  # TODO(marcoskirsch): use get_ctype_variable_declaration_snippet()
        a_string_ctype = (visatype.ViChar * string_size_ctype.value)()  # TODO(marcoskirsch): use get_ctype_variable_declaration_snippet()
        error_code = self._library.niFake_ReturnMultipleTypes(vi_ctype, ctypes.pointer(a_boolean_ctype), ctypes.pointer(an_int32_ctype), ctypes.pointer(an_int64_ctype), ctypes.pointer(an_int_enum_ctype), ctypes.pointer(a_float_ctype), ctypes.pointer(a_float_enum_ctype), array_size_ctype, an_array_ctype, string_size_ctype, a_string_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(a_boolean_ctype.value), int(an_int32_ctype.value), int(an_int64_ctype.value), enums.Turtle(an_int_enum_ctype.value), float(a_float_ctype.value), enums.FloatEnum(a_float_enum_ctype.value), [float(an_array_ctype[i]) for i in range(array_size_ctype.value)], a_string_ctype.value.decode(self._encoding)

    def set_custom_type(self, cs):
        '''set_custom_type

        This function takes a custom type.

        Args:
            cs (custom_struct): Set using custom type
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        cs_ctype = visatype.CustomStruct(cs)  # case 8
        error_code = self._library.niFake_SetCustomType(vi_ctype, cs_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def simple_function(self):
        '''simple_function

        This function takes no parameters other than the session.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        error_code = self._library.niFake_SimpleFunction(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def two_input_function(self, a_number, a_string):
        '''two_input_function

        This function takes two parameters other than the session.

        Args:
            a_number (float): Contains a number
            a_string (int): Contains a string
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        a_number_ctype = visatype.ViReal64(a_number)  # case 8
        a_string_ctype = ctypes.create_string_buffer(a_string.encode(self._encoding))  # case 3
        error_code = self._library.niFake_TwoInputFunction(vi_ctype, a_number_ctype, a_string_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def use64_bit_number(self, input):
        '''use64_bit_number

        Returns a number and a string.

        Note: This function rules!

        Args:
            input (int): A big number on its way in.

        Returns:
            output (int): A big number on its way out.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        input_ctype = visatype.ViInt64(input)  # case 8
        output_ctype = visatype.ViInt64()  # case 13
        error_code = self._library.niFake_Use64BitNumber(vi_ctype, input_ctype, ctypes.pointer(output_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(output_ctype.value)

    def _close(self):
        '''_close

        Closes the specified session and deallocates resources that it reserved.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        error_code = self._library.niFake_close(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return



