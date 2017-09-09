nifake.Session methods
======================

.. py:currentmodule:: nifake

.. function:: get_a_boolean(a_boolean)

    Returns a boolean.

    

    .. note:: This function rules!


    :rtype: bool
    :return:


            Contains a boolean.

            


.. function:: get_a_number(a_number)

    Returns a number.

    

    .. note:: This function rules!


    :rtype: int
    :return:


            Contains a number.

            


.. function:: get_a_string_of_fixed_maximum_size(a_string)

    Illustrates resturning a string of fixed size.

    


    :rtype: int
    :return:


            String comes back here. Buffer must be 256 big.

            


.. function:: get_a_string_with_specified_maximum_size(a_string, buffer_size)

    Illustrates resturning a string where user specifies the size.

    


    :param buffer_size:


        Buffersize of the string.

        

    :type buffer_size: int

    :rtype: int
    :return:


            String comes back here. Buffer must be at least bufferSize big.

            


.. function:: get_enum_value(a_quantity, a_turtle)

    Returns an enum value

    

    .. note:: Splinter is not supported.


    :rtype: tuple (a_quantity, a_turtle)

        WHERE

        a_quantity (int): 


            This is an amount.

            

            .. note:: The amount will be between -2^31 and (2^31-1)

        a_turtle (:py:data:`nifake.Turtle`): 


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


.. function:: one_input_function(a_number)

    This function takes one parameter other than the session.

    


    :param a_number:


        Contains a number

        

    :type a_number: int

.. function:: read(maximum_time, reading)

    Acquires a single measurement and returns the measured value.

    


    :param maximum_time:


        Specifies the **maximum\_time** allowed in years.

        

    :type maximum_time: int

    :rtype: float
    :return:


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

        reading_array (float): 


            An array of measurement values.

            

            .. note:: The size must be at least arraySize.

        actual_number_of_points (int): 


            Indicates the number of measured values actually retrieved.

            


.. function:: return_a_number_and_a_string(a_number, a_string)

    Returns a number and a string.

    

    .. note:: This function rules!


    :rtype: tuple (a_number, a_string)

        WHERE

        a_number (int): 


            Contains a number.

            

        a_string (int): 


            Contains a string.

            


.. function:: simple_function()

    This function takes no parameters other than the session.

    


.. function:: two_input_function(a_number, a_string)

    This function takes two parameters other than the session.

    


    :param a_number:


        Contains a number

        

    :type a_number: float
    :param a_string:


        Contains a string

        

    :type a_string: int

.. function:: error_message(error_code, error_message)

    Takes the errorCode returned by a functiona and returns it as a user-readable string.

    


    :param error_code:


        The errorCode returned from the instrument.

        

    :type error_code: int

    :rtype: int
    :return:


            The error information formatted into a string.

            



