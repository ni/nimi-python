nifake.Session methods
======================

.. py:currentmodule:: nifake

.. function:: _abort()

    Aborts a previously initiated thingie.

    


.. function:: _clear_error()

    Clears the error for the current thread and session

    


.. function:: get_a_number(a_number)

    Returns a number.

    

    .. note:: This function rules!


    :rtype: ViInt16


            Contains a number.

            


.. function:: get_a_string_of_fixed_maximum_size(a_string)

    Illustrates resturning a string of fixed size.

    


    :rtype: ViChar


            String comes back here. Buffer must be 256 big.

            


.. function:: get_a_string_with_specified_maximum_size(a_string, buffer_size)

    Illustrates resturning a string where user specifies the size.

    


    :param buffer_size:


        String comes back here. Buffer must be 256 big.

        

    :type buffer_size: int

    :rtype: ViChar


            String comes back here. Buffer must be at least bufferSize big.

            


.. function:: _get_attribute_vi_boolean(channel_name, attribute_id, attribute_value)

    Queries the value of a ViBoolean attribute.

    


    :param channel_name:


        This is the channel(s) that this function will apply to.

        

    :type channel_name: str
    :param attribute_id:


        Pass the ID of an attribute.

        

    :type attribute_id: int

    :rtype: ViBoolean


            Returns the value of the attribute.

            


.. function:: _get_attribute_vi_int32(channel_name, attribute_id, attribute_value)

    Queries the value of a ViInt32 attribute.

    


    :param channel_name:


        This is the channel(s) that this function will apply to.

        

    :type channel_name: str
    :param attribute_id:


        Pass the ID of an attribute.

        

    :type attribute_id: int

    :rtype: ViInt32


            Returns the value of the attribute.

            


.. function:: _get_attribute_vi_real64(channel_name, attribute_id, attribute_value)

    Queries the value of a ViReal attribute.

    


    :param channel_name:


        This is the channel(s) that this function will apply to.

        

    :type channel_name: str
    :param attribute_id:


        Pass the ID of an attribute.

        

    :type attribute_id: int

    :rtype: ViReal64


            Returns the value of the attribute.

            


.. function:: _get_attribute_vi_session(channel_name, attribute_id, attribute_value)

    Queries the value of a ViSession attribute.

    


    :param channel_name:


        This is the channel(s) that this function will apply to.

        

    :type channel_name: str
    :param attribute_id:


        Pass the ID of an attribute.

        

    :type attribute_id: int

    :rtype: ViSession


            Returns the value of the attribute.

            


.. function:: _get_attribute_vi_string(channel_name, attribute_id, buffer_size, attribute_value)

    Queries the value of a ViBoolean attribute.

    


    :param channel_name:


        This is the channel(s) that this function will apply to.

        

    :type channel_name: str
    :param attribute_id:


        Pass the ID of an attribute.

        

    :type attribute_id: int
    :param buffer_size:


        Number of bytes in attributeValue. You can IVI-dance with this.

        

    :type buffer_size: int

.. function:: get_enum_value(a_quantity, a_turtle)

    Returns an enum value

    

    .. note:: Splinter is not supported.


    :rtype: tuple (a_quantity, a_turtle)

        WHERE

        a_quantity (ViInt32): 


            This is an amount.

            

            .. note:: The amount will be between -2^31 and (2^31-1)

        a_turtle (enums.Turtle): 


            Indicates a ninja turtle

            +---+---------------+
            | 0 | Leonardo      |
            +---+---------------+
            | 1 | Donatello     |
            +---+---------------+
            | 2 | Raphael       |
            +---+---------------+
            | 3 | Mich elangelo |
            +---+---------------+


.. function:: _get_error(error_code, buffer_size, description)

    Returns the error information associated with the session.

    


    :param buffer_size:


        Number of bytes in description buffer.

        

    :type buffer_size: int

    :rtype: ViStatus


            Returns errorCode for the session. If you pass 0 for bufferSize, you can pass VI\_NULL for this.

            


.. function:: _get_error_message(error_code, buffer_size, error_message)

    Returns the errorMessage as a user-readable string. Uses IVI-dance

    


    :param error_code:


        The error code returned for which you want to get a string.

        

    :type error_code: int
    :param buffer_size:


        Number of bytes allocated for errorMessage

        

    :type buffer_size: int

.. function:: _init_with_options(resource_name, id_query, reset_device, option_string)

    Creates a new IVI instrument driver session.

    


    :param resource_name:


        .. caution:: This is just some string.

        Contains the **resource\_name** of the device to initialize.

        

    :type resource_name: str
    :param id_query:


        NI-FAKE is probably not needed.

        +--------------------+---+------------------+
        | VI\_TRUE (default) | 1 | Perform ID Query |
        +--------------------+---+------------------+
        | VI\_FALSE          | 0 | Skip ID Query    |
        +--------------------+---+------------------+

    :type id_query: bool
    :param reset_device:


        Specifies whether to reset

        +--------------------+---+--------------+
        | VI\_TRUE (default) | 1 | Reset Device |
        +--------------------+---+--------------+
        | VI\_FALSE          | 0 | Don't Reset  |
        +--------------------+---+--------------+

    :type reset_device: bool
    :param option_string:


        Some options

        

    :type option_string: str

    :rtype: ViSession


            Returns a ViSession handle that you use.

            


.. function:: _initiate()

    Initiates a thingie.

    


.. function:: read(maximum_time, reading)

    Acquires a single measurement and returns the measured value.

    


    :param maximum_time:


        Specifies the **maximum\_time** allowed in years.

        

    :type maximum_time: int

    :rtype: ViReal64


            The measured value.

            


.. function:: read_multi_point(maximum_time, array_size, reading_array, actual_number_of_points)

    Acquires multiple measurements and returns an array of measured values.

    


    :param maximum_time:


        Specifies the **maximum\_time** allowed in years.

        

    :type maximum_time: int
    :param array_size:


        Number of measurements to acquire.

        

    :type array_size: int

    :rtype: tuple (reading_array, actual_number_of_points)

        WHERE

        reading_array (ViReal64): 


            An array of measurement values.

            

            .. note:: The size must be at least arraySize.

        actual_number_of_points (ViInt32): 


            Indicates the number of measured values actually retrieved.

            


.. function:: return_a_number_and_a_string(a_number, a_string)

    Returns a number and a string.

    

    .. note:: This function rules!


    :rtype: tuple (a_number, a_string)

        WHERE

        a_number (ViInt16): 


            Contains a number.

            

        a_string (ViChar): 


            Contains a string.

            


.. function:: _set_attribute_vi_boolean(channel_name, attribute_id, attribute_value)

    This function sets the value of a ViBoolean attribute.

    


    :param channel_name:


        This is the channel(s) that this function will apply to.

        

    :type channel_name: str
    :param attribute_id:


        Pass the ID of an attribute.

        

    :type attribute_id: int
    :param attribute_value:


        Pass the value that you want to set the attribute to.

        

    :type attribute_value: bool

.. function:: _set_attribute_vi_int32(channel_name, attribute_id, attribute_value)

    This function sets the value of a ViInt32 attribute.

    


    :param channel_name:


        This is the channel(s) that this function will apply to.

        

    :type channel_name: str
    :param attribute_id:


        Pass the ID of an attribute.

        

    :type attribute_id: int
    :param attribute_value:


        Pass the value that you want to set the attribute to.

        

    :type attribute_value: int

.. function:: _set_attribute_vi_real64(channel_name, attribute_id, attribute_value)

    This function sets the value of a ViReal64 attribute.

    


    :param channel_name:


        This is the channel(s) that this function will apply to.

        

    :type channel_name: str
    :param attribute_id:


        Pass the ID of an attribute.

        

    :type attribute_id: int
    :param attribute_value:


        Pass the value that you want to set the attribute to.

        

    :type attribute_value: float

.. function:: _set_attribute_vi_session(channel_name, attribute_id, attribute_value)

    This function sets the value of a ViSession attribute.

    


    :param channel_name:


        This is the channel(s) that this function will apply to.

        

    :type channel_name: str
    :param attribute_id:


        Pass the ID of an attribute.

        

    :type attribute_id: int
    :param attribute_value:


        Pass the value that you want to set the attribute to.

        

    :type attribute_value: int

.. function:: _set_attribute_vi_string(channel_name, attribute_id, attribute_value)

    This function sets the value of a ViString attribute.

    


    :param channel_name:


        This is the channel(s) that this function will apply to.

        

    :type channel_name: str
    :param attribute_id:


        Pass the ID of an attribute.

        

    :type attribute_id: int
    :param attribute_value:


        Pass the value that you want to set the attribute to.

        

    :type attribute_value: str

.. function:: simple_function()

    This function takes no parameters other than the session.

    


.. function:: _close()

    Closes the specified session and deallocates resources that it reserved.

    


.. function:: error_message(error_code, error_message)

    Takes the errorCode returned by a functiona and returns it as a user-readable string.

    


    :param error_code:


        The errorCode returned from the instrument.

        

    :type error_code: int

    :rtype: ViChar


            The error information formatted into a string.

            



