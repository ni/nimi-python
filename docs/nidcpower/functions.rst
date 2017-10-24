nidcpower.Session methods
=========================

.. py:currentmodule:: nidcpower

.. function:: commit()

    Applies previously configured settings to the device. Calling this
    function moves the NI-DCPower session from the Uncommitted state into
    the Committed state. After calling this function, modifying any
    attribute reverts the NI-DCPower session to the Uncommitted state. Use
    the :py:func:`nidcpower._initiate` function to transition to the Running state.
    Refer to the `Programming
    States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic in
    the *NI DC Power Supplies and SMUs Help* for details about the specific
    NI-DCPower software states.

    **Related Topics:**

    `Programming
    States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

    



.. function:: configure_aperture_time(aperture_time, units=nidcpower.ApertureTimeUnits.SECONDS)

    Configures the aperture time on the specified channel(s).

    The supported values depend on the **units**. Refer to the *Aperture
    Time* topic for your device in the *NI DC Power Supplies and SMUs Help*
    for more information. In general, devices support discrete
    **apertureTime** values, and if you configure **apertureTime** to some
    unsupported value, NI-DCPower coerces it up to the next supported value.

    Refer to the *Measurement Configuration and Timing* or *DC Noise
    Rejection* topic for your device in the *NI DC Power Supplies and SMUs
    Help* for more information about how to configure your measurements.

    **Related Topics:**

    `Aperture Time <REPLACE_DRIVER_SPECIFIC_URL_1(aperture)>`__

    

    .. note:: This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].configure_aperture_time(aperture_time, units=nidcpower.ApertureTimeUnits.SECONDS)


    :param aperture_time:


        Specifies the aperture time. Refer to the *Aperture Time* topic for your
        device in the *NI DC Power Supplies and SMUs Help* for more information.

        


    :type aperture_time: float
    :param units:


        Specifies the units for **apertureTime**.
        **Defined Values**:

        +--------------------------------------------+------------------------------+
        | NIDCPOWER\_VAL\_SECONDS (1028)             | Specifies seconds.           |
        +--------------------------------------------+------------------------------+
        | NIDCPOWER\_VAL\_POWER\_LINE\_CYCLES (1029) | Specifies Power Line Cycles. |
        +--------------------------------------------+------------------------------+


    :type units: :py:data:`nidcpower.ApertureTimeUnits`

.. function:: configure_digital_edge_measure_trigger(input_terminal, edge=nidcpower.DigitalEdge.RISING)

    Configures the Measure trigger for digital edge triggering.

    

    .. note:: This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.



    :param input_terminal:


        Specifies the input terminal for the digital edge Measure trigger.

        You can specify any valid input terminal for this function. Valid
        terminals are listed in MAX under the **Device Routes** tab. For
        PXIe-4162/4163, refer to the Signal Routing topic for the device to
        determine which routes are available. This information is not available
        on a Device Routes tab in MAX.

        Input terminals can be specified in one of two ways. If the device is
        named Dev1 and your terminal is PXI\_Trig0, you can specify the terminal
        with the fully qualified terminal name, /Dev1/PXI\_Trig0, or with the
        shortened terminal name, PXI\_Trig0. The input terminal can also be a
        terminal from another device. For example, you can set the input
        terminal on Dev1 to be /Dev2/SourceCompleteEvent.

        


    :type input_terminal: string
    :param edge:


        Specifies whether to configure the Measure trigger to assert on the
        rising or falling edge.
        **Defined Values:**

        +--------------------------------+----------------------------------------------------------------+
        | NIDCPOWER\_VAL\_RISING (1016)  | Asserts the trigger on the rising edge of the digital signal.  |
        +--------------------------------+----------------------------------------------------------------+
        | NIDCPOWER\_VAL\_FALLING (1017) | Asserts the trigger on the falling edge of the digital signal. |
        +--------------------------------+----------------------------------------------------------------+


    :type edge: :py:data:`nidcpower.DigitalEdge`

.. function:: configure_digital_edge_pulse_trigger(input_terminal, edge=nidcpower.DigitalEdge.RISING)

    Configures the Pulse trigger for digital edge triggering.

    

    .. note:: This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.



    :param input_terminal:


        Specifies the input terminal for the digital edge Pulse trigger.

        You can specify any valid input terminal for this function. Valid
        terminals are listed in MAX under the **Device Routes** tab. For
        PXIe-4162/4163, refer to the Signal Routing topic for the device to
        determine which routes are available. This information is not available
        on a Device Routes tab in MAX.

        Input terminals can be specified in one of two ways. If the device is
        named Dev1 and your terminal is PXI\_Trig0, you can specify the terminal
        with the fully qualified terminal name, /Dev1/PXI\_Trig0, or with the
        shortened terminal name, PXI\_Trig0. The input terminal can also be a
        terminal from another device. For example, you can set the input
        terminal on Dev1 to be /Dev2/SourceCompleteEvent.

        


    :type input_terminal: string
    :param edge:


        Specifies whether to configure the Pulse trigger to assert on the rising
        or falling edge.
        **Defined Values:**

        +--------------------------------+----------------------------------------------------------------+
        | NIDCPOWER\_VAL\_RISING (1016)  | Asserts the trigger on the rising edge of the digital signal.  |
        +--------------------------------+----------------------------------------------------------------+
        | NIDCPOWER\_VAL\_FALLING (1017) | Asserts the trigger on the falling edge of the digital signal. |
        +--------------------------------+----------------------------------------------------------------+


    :type edge: :py:data:`nidcpower.DigitalEdge`

.. function:: configure_digital_edge_sequence_advance_trigger(input_terminal, edge=nidcpower.DigitalEdge.RISING)

    Configures the Sequence Advance trigger for digital edge triggering.

    

    .. note:: This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.



    :param input_terminal:


        Specifies the input terminal for the digital edge Sequence Advance
        trigger.

        You can specify any valid input terminal for this function. Valid
        terminals are listed in MAX under the **Device Routes** tab. For
        PXIe-4162/4163, refer to the Signal Routing topic for the device to
        determine which routes are available. This information is not available
        on a Device Routes tab in MAX.

        Input terminals can be specified in one of two ways. If the device is
        named Dev1 and your terminal is PXI\_Trig0, you can specify the terminal
        with the fully qualified terminal name, /Dev1/PXI\_Trig0, or with the
        shortened terminal name, PXI\_Trig0. The input terminal can also be a
        terminal from another device. For example, you can set the input
        terminal on Dev1 to be /Dev2/SourceCompleteEvent.

        


    :type input_terminal: string
    :param edge:


        Specifies whether to configure the Sequence Advance trigger to assert on
        the rising or falling edge.
        **Defined Values:**

        +--------------------------------+----------------------------------------------------------------+
        | NIDCPOWER\_VAL\_RISING (1016)  | Asserts the trigger on the rising edge of the digital signal.  |
        +--------------------------------+----------------------------------------------------------------+
        | NIDCPOWER\_VAL\_FALLING (1017) | Asserts the trigger on the falling edge of the digital signal. |
        +--------------------------------+----------------------------------------------------------------+


    :type edge: :py:data:`nidcpower.DigitalEdge`

.. function:: configure_digital_edge_source_trigger(input_terminal, edge=nidcpower.DigitalEdge.RISING)

    Configures the Source trigger for digital edge triggering.

    

    .. note:: This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.



    :param input_terminal:


        Specifies the input terminal for the digital edge Source trigger.

        You can specify any valid input terminal for this function. Valid
        terminals are listed in MAX under the **Device Routes** tab. For
        PXIe-4162/4163, refer to the Signal Routing topic for the device to
        determine which routes are available. This information is not available
        on a Device Routes tab in MAX.

        Input terminals can be specified in one of two ways. If the device is
        named Dev1 and your terminal is PXI\_Trig0, you can specify the terminal
        with the fully qualified terminal name, /Dev1/PXI\_Trig0, or with the
        shortened terminal name, PXI\_Trig0. The input terminal can also be a
        terminal from another device. For example, you can set the input
        terminal on Dev1 to be /Dev2/SourceCompleteEvent.

        


    :type input_terminal: string
    :param edge:


        Specifies whether to configure the Source trigger to assert on the
        rising or falling edge.
        **Defined Values:**

        +--------------------------------+----------------------------------------------------------------+
        | NIDCPOWER\_VAL\_RISING (1016)  | Asserts the trigger on the rising edge of the digital signal.  |
        +--------------------------------+----------------------------------------------------------------+
        | NIDCPOWER\_VAL\_FALLING (1017) | Asserts the trigger on the falling edge of the digital signal. |
        +--------------------------------+----------------------------------------------------------------+


    :type edge: :py:data:`nidcpower.DigitalEdge`

.. function:: configure_digital_edge_start_trigger(input_terminal, edge=nidcpower.DigitalEdge.RISING)

    Configures the Start trigger for digital edge triggering.

    

    .. note:: This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.



    :param input_terminal:


        Specifies the input terminal for the digital edge Start trigger.

        You can specify any valid input terminal for this function. Valid
        terminals are listed in MAX under the **Device Routes** tab. For
        PXIe-4162/4163, refer to the Signal Routing topic for the device to
        determine which routes are available. This information is not available
        on a Device Routes tab in MAX.

        Input terminals can be specified in one of two ways. If the device is
        named Dev1 and your terminal is PXI\_Trig0, you can specify the terminal
        with the fully qualified terminal name, /Dev1/PXI\_Trig0, or with the
        shortened terminal name, PXI\_Trig0. The input terminal can also be a
        terminal from another device. For example, you can set the input
        terminal on Dev1 to be /Dev2/SourceCompleteEvent.

        


    :type input_terminal: string
    :param edge:


        Specifies whether to configure the Start trigger to assert on the rising
        or falling edge.
        **Defined Values:**

        +--------------------------------+----------------------------------------------------------------+
        | NIDCPOWER\_VAL\_RISING (1016)  | Asserts the trigger on the rising edge of the digital signal.  |
        +--------------------------------+----------------------------------------------------------------+
        | NIDCPOWER\_VAL\_FALLING (1017) | Asserts the trigger on the falling edge of the digital signal. |
        +--------------------------------+----------------------------------------------------------------+


    :type edge: :py:data:`nidcpower.DigitalEdge`

.. function:: create_advanced_sequence(sequence_name, attribute_ids, set_as_active_sequence=True)

    Creates an empty advanced sequence. Call the
    :py:func:`nidcpower.create_advanced_sequence_step` function to add steps to the
    active advanced sequence.

    **Support for this function**

    You must set the source mode to Sequence to use this function.

    Using the :py:func:`nidcpower.set_sequence` function with Advanced Sequence
    functions is unsupported.

    Use this function in the Uncommitted or Committed programming states.
    Refer to the `Programming
    States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic in
    the *NI DC Power Supplies and SMUs Help* for more information about
    NI-DCPower programming states.

    **Related Topics**:

    `Advanced Sequence
    Mode <REPLACE_DRIVER_SPECIFIC_URL_1(advancedsequencemode)>`__

    `Programming
    States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

    :py:func:`nidcpower.create_advanced_sequence_step`

    

    .. note:: This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.



    :param sequence_name:


        Specifies the name of the sequence to create.

        


    :type sequence_name: string
    :param attribute_id_count:


        Specifies the number of attributes in the attributeIDs array.

        


    :type attribute_id_count: int
    :param attribute_ids:


        Specifies the attributes you reconfigure per step in the advanced
        sequence. The following table lists which attributes can be configured
        in an advanced sequence for each NI-DCPower device that supports
        advanced sequencing. A ✓ indicates that the attribute can be configured
        in advanced sequencing. An ✕ indicates that the attribute cannot be
        configured in advanced sequencing.

        +-------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | Attribute                                             | PXIe-4135 | NI 4136 | NI 4137 | NI 4138 | NI 4139 | NI 4140/4142/4144 | NI 4141/4143/4145 | PXIe-4162/4163 |
        +=======================================================+===========+=========+=========+=========+=========+===================+===================+================+
        | :py:data:`nidcpower.DC\_NOISE\_REJECTION`             | ✓         | ✕       | ✓       | ✕       | ✓       | ✕                 | ✕                 | ✓              |
        +-------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | :py:data:`nidcpower.APERTURE\_TIME`                   | ✓         | ✓       | ✓       | ✓       | ✓       | ✓                 | ✓                 | ✓              |
        +-------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | :py:data:`nidcpower.MEASURE\_RECORD\_LENGTH`          | ✓         | ✓       | ✓       | ✓       | ✓       | ✓                 | ✓                 | ✓              |
        +-------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | :py:data:`nidcpower.sense`                            | ✓         | ✓       | ✓       | ✓       | ✓       | ✓                 | ✓                 | ✓              |
        +-------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | :py:data:`nidcpower.OVP\_ENABLED`                     | ✓         | ✓       | ✓       | ✕       | ✕       | ✕                 | ✕                 | ✕              |
        +-------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | :py:data:`nidcpower.OVP\_LIMIT`                       | ✓         | ✓       | ✓       | ✕       | ✕       | ✕                 | ✕                 | ✕              |
        +-------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | :py:data:`nidcpower.PULSE\_BIAS\_DELAY`               | ✓         | ✓       | ✓       | ✓       | ✓       | ✕                 | ✕                 | ✕              |
        +-------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | :py:data:`nidcpower.PULSE\_OFF\_TIME`                 | ✓         | ✓       | ✓       | ✓       | ✓       | ✕                 | ✕                 | ✕              |
        +-------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | :py:data:`nidcpower.PULSE\_ON\_TIME`                  | ✓         | ✓       | ✓       | ✓       | ✓       | ✕                 | ✕                 | ✕              |
        +-------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | :py:data:`nidcpower.SOURCE\_DELAY`                    | ✓         | ✓       | ✓       | ✓       | ✓       | ✓                 | ✓                 | ✓              |
        +-------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | :py:data:`nidcpower.CURRENT\_COMPENSATION\_FREQUENCY` | ✓         | ✕       | ✓       | ✕       | ✓       | ✕                 | ✓                 | ✓              |
        +-------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | :py:data:`nidcpower.CURRENT\_GAIN\_BANDWIDTH`         | ✓         | ✕       | ✓       | ✕       | ✓       | ✕                 | ✓                 | ✓              |
        +-------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | :py:data:`nidcpower.CURRENT\_POLE\_ZERO\_RATIO`       | ✓         | ✕       | ✓       | ✕       | ✓       | ✕                 | ✓                 | ✓              |
        +-------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | :py:data:`nidcpower.VOLTAGE\_COMPENSATION\_FREQUENCY` | ✓         | ✕       | ✓       | ✕       | ✓       | ✕                 | ✓                 | ✓              |
        +-------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | :py:data:`nidcpower.VOLTAGE\_GAIN\_BANDWIDTH`         | ✓         | ✕       | ✓       | ✕       | ✓       | ✕                 | ✓                 | ✓              |
        +-------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | :py:data:`nidcpower.VOLTAGE\_POLE\_ZERO\_RATIO`       | ✓         | ✕       | ✓       | ✕       | ✓       | ✕                 | ✓                 | ✓              |
        +-------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | :py:data:`nidcpower.CURRENT\_LEVEL`                   | ✓         | ✓       | ✓       | ✓       | ✓       | ✓                 | ✓                 | ✓              |
        +-------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | :py:data:`nidcpower.CURRENT\_LEVEL\_RANGE`            | ✓         | ✓       | ✓       | ✓       | ✓       | ✓                 | ✓                 | ✓              |
        +-------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | :py:data:`nidcpower.VOLTAGE\_LIMIT`                   | ✓         | ✓       | ✓       | ✓       | ✓       | ✓                 | ✓                 | ✓              |
        +-------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | :py:data:`nidcpower.VOLTAGE\_LIMIT\_RANGE`            | ✓         | ✓       | ✓       | ✓       | ✓       | ✓                 | ✓                 | ✓              |
        +-------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | :py:data:`nidcpower.CURRENT\_LIMIT`                   | ✓         | ✓       | ✓       | ✓       | ✓       | ✓                 | ✓                 | ✓              |
        +-------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | :py:data:`nidcpower.CURRENT\_LIMIT\_RANGE`            | ✓         | ✓       | ✓       | ✓       | ✓       | ✓                 | ✓                 | ✓              |
        +-------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | :py:data:`nidcpower.VOLTAGE\_LEVEL`                   | ✓         | ✓       | ✓       | ✓       | ✓       | ✓                 | ✓                 | ✓              |
        +-------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | :py:data:`nidcpower.VOLTAGE\_LEVEL\_RANGE`            | ✓         | ✓       | ✓       | ✓       | ✓       | ✓                 | ✓                 | ✓              |
        +-------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | :py:data:`nidcpower.OUTPUT\_ENABLED`                  | ✓         | ✓       | ✓       | ✓       | ✓       | ✓                 | ✓                 | ✓              |
        +-------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | :py:data:`nidcpower.OUTPUT\_FUNCTION`                 | ✓         | ✓       | ✓       | ✓       | ✓       | ✓                 | ✓                 | ✓              |
        +-------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | :py:data:`nidcpower.OUTPUT\_RESISTANCE`               | ✓         | ✕       | ✓       | ✕       | ✓       | ✕                 | ✓                 | ✕              |
        +-------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | :py:data:`nidcpower.PULSE\_BIAS\_CURRENT\_LEVEL`      | ✓         | ✓       | ✓       | ✓       | ✓       | ✕                 | ✕                 | ✕              |
        +-------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | :py:data:`nidcpower.PULSE\_BIAS\_VOLTAGE\_LIMIT`      | ✓         | ✓       | ✓       | ✓       | ✓       | ✕                 | ✕                 | ✕              |
        +-------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | :py:data:`nidcpower.PULSE\_CURRENT\_LEVEL`            | ✓         | ✓       | ✓       | ✓       | ✓       | ✕                 | ✕                 | ✕              |
        +-------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | :py:data:`nidcpower.PULSE\_CURRENT\_LEVEL\_RANGE`     | ✓         | ✓       | ✓       | ✓       | ✓       | ✕                 | ✕                 | ✕              |
        +-------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | :py:data:`nidcpower.PULSE\_VOLTAGE\_LIMIT`            | ✓         | ✓       | ✓       | ✓       | ✓       | ✕                 | ✕                 | ✕              |
        +-------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | :py:data:`nidcpower.PULSE\_VOLTAGE\_LIMIT\_RANGE`     | ✓         | ✓       | ✓       | ✓       | ✓       | ✕                 | ✕                 | ✕              |
        +-------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | :py:data:`nidcpower.PULSE\_BIAS\_CURRENT\_LIMIT`      | ✓         | ✓       | ✓       | ✓       | ✓       | ✕                 | ✕                 | ✕              |
        +-------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | :py:data:`nidcpower.PULSE\_BIAS\_VOLTAGE\_LEVEL`      | ✓         | ✓       | ✓       | ✓       | ✓       | ✕                 | ✕                 | ✕              |
        +-------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | :py:data:`nidcpower.PULSE\_CURRENT\_LIMIT`            | ✓         | ✓       | ✓       | ✓       | ✓       | ✕                 | ✕                 | ✕              |
        +-------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | :py:data:`nidcpower.PULSE\_CURRENT\_LIMIT\_RANGE`     | ✓         | ✓       | ✓       | ✓       | ✓       | ✕                 | ✕                 | ✕              |
        +-------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | :py:data:`nidcpower.PULSE\_VOLTAGE\_LEVEL`            | ✓         | ✓       | ✓       | ✓       | ✓       | ✕                 | ✕                 | ✕              |
        +-------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | :py:data:`nidcpower.PULSE\_VOLTAGE\_LEVEL\_RANGE`     | ✓         | ✓       | ✓       | ✓       | ✓       | ✕                 | ✕                 | ✕              |
        +-------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | :py:data:`nidcpower.TRANSIENT\_RESPONSE`              | ✓         | ✓       | ✓       | ✓       | ✓       | ✓                 | ✓                 | ✓              |
        +-------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+


    :type attribute_ids: list of int
    :param set_as_active_sequence:


        Specifies that this current sequence is active.

        


    :type set_as_active_sequence: bool

.. function:: create_advanced_sequence_step(set_as_active_step=True)

    Creates a new advanced sequence step in the advanced sequence specified
    by the Active advanced sequence. When you create an advanced sequence
    step, each attribute you passed to the :py:func:`nidcpower.create_advanced_sequence`
    function is reset to its default value for that step unless otherwise
    specified.

    **Support for this Function**

    You must set the source mode to Sequence to use this function.

    Using the :py:func:`nidcpower.set_sequence` function with Advanced Sequence
    functions is unsupported.

    **Related Topics**:

    `Advanced Sequence
    Mode <REPLACE_DRIVER_SPECIFIC_URL_1(advancedsequencemode)>`__

    `Programming
    States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

    :py:func:`nidcpower.create_advanced_sequence`

    

    .. note:: This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.



    :param set_as_active_step:


        Specifies that this current step in the active sequence is active.

        


    :type set_as_active_step: bool

.. function:: delete_advanced_sequence(sequence_name)

    Deletes a previously created advanced sequence and all the advanced
    sequence steps in the advanced sequence.

    **Support for this Function**

    You must set the source mode to Sequence to use this function.

    Using the :py:func:`nidcpower.set_sequence` function with Advanced Sequence
    functions is unsupported.

    **Related Topics**:

    `Advanced Sequence
    Mode <REPLACE_DRIVER_SPECIFIC_URL_1(advancedsequencemode)>`__

    `Programming
    States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

    

    .. note:: This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.



    :param sequence_name:


        specifies the name of the sequence to delete.

        


    :type sequence_name: string

.. function:: disable()

    This function performs the same actions as the :py:func:`nidcpower.reset`
    function, except that this function also immediately sets the
    :py:data:`nidcpower.OUTPUT\_ENABLED` attribute to VI\_FALSE.

    This function opens the output relay on devices that have an output
    relay.

    



.. function:: export_signal(signal, output_terminal, signal_identifier='')

    Routes signals (triggers and events) to the output terminal you specify.
    The route is created when the session is :py:func:`nidcpower.commit`.

    **Related Topics:**

    `Triggers <REPLACE_DRIVER_SPECIFIC_URL_1(trigger)>`__

    

    .. note:: This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.



    :param signal:


        Specifies which trigger or event to export.
        **Defined Values:**

        +-------------------------------------------------------------+------------------------------------------------+
        | NIDCPOWER\_VAL\_SOURCE\_COMPLETE\_EVENT (1030)              | Exports the Source Complete event.             |
        +-------------------------------------------------------------+------------------------------------------------+
        | NIDCPOWER\_VAL\_MEASURE\_COMPLETE\_EVENT (1031)             | Exports the Measure Complete event.            |
        +-------------------------------------------------------------+------------------------------------------------+
        | NIDCPOWER\_VAL\_SEQUENCE\_ITERATION\_COMPLETE\_EVENT (1032) | Exports the Sequence Iteration Complete event. |
        +-------------------------------------------------------------+------------------------------------------------+
        | NIDCPOWER\_VAL\_SEQUENCE\_ENGINE\_DONE\_EVENT (1033)        | Exports the Sequence Engine Done event.        |
        +-------------------------------------------------------------+------------------------------------------------+
        | NIDCPOWER\_VAL\_PULSE\_COMPLETE\_EVENT (1051)               | Exports the Pulse Complete event.              |
        +-------------------------------------------------------------+------------------------------------------------+
        | NIDCPOWER\_VAL\_READY\_FOR\_PULSE\_TRIGGER\_EVENT (1052)    | Exports the Ready Pulse Trigger event.         |
        +-------------------------------------------------------------+------------------------------------------------+
        | NIDCPOWER\_VAL\_START\_TRIGGER (1034)                       | Exports the Start trigger.                     |
        +-------------------------------------------------------------+------------------------------------------------+
        | NIDCPOWER\_VAL\_SOURCE\_TRIGGER (1035)                      | Exports the Source trigger.                    |
        +-------------------------------------------------------------+------------------------------------------------+
        | NIDCPOWER\_VAL\_MEASURE\_TRIGGER (1036)                     | Exports the Measure trigger.                   |
        +-------------------------------------------------------------+------------------------------------------------+
        | NIDCPOWER\_VAL\_SEQUENCE\_ADVANCE\_TRIGGER (1037)           | Exports the Sequence Advance trigger.          |
        +-------------------------------------------------------------+------------------------------------------------+
        | NIDCPOWER\_VAL\_PULSE\_TRIGGER (1053)                       | Exports the Pulse trigger.                     |
        +-------------------------------------------------------------+------------------------------------------------+


    :type signal: :py:data:`nidcpower.Signals`
    :param signal_identifier:


        Reserved for future use. Pass in an empty string for this parameter.

        


    :type signal_identifier: string
    :param output_terminal:


        Specifies where to export the selected signal.
        **Relative Terminals**:

        +--------------+----------------------+
        | ""           | Do not export signal |
        +--------------+----------------------+
        | "PXI\_Trig0" | PXI trigger line 0   |
        +--------------+----------------------+
        | "PXI\_Trig1" | PXI trigger line 1   |
        +--------------+----------------------+
        | "PXI\_Trig2" | PXI trigger line 2   |
        +--------------+----------------------+
        | "PXI\_Trig3" | PXI trigger line 3   |
        +--------------+----------------------+
        | "PXI\_Trig4" | PXI trigger line 4   |
        +--------------+----------------------+
        | "PXI\_Trig5" | PXI trigger line 5   |
        +--------------+----------------------+
        | "PXI\_Trig6" | PXI trigger line 6   |
        +--------------+----------------------+
        | "PXI\_Trig7" | PXI trigger line 7   |
        +--------------+----------------------+


    :type output_terminal: string

.. function:: fetch_multiple(count, timeout=1.0)

    Returns an array of voltage measurements, an array of current
    measurements, and an array of compliance measurements that were
    previously taken and are stored in the NI-DCPower buffer. This function
    should not be used when the :py:data:`nidcpower.MEASURE\_WHEN` attribute is
    set to NIDCPOWER\_VAL\_ON\_DEMAND. You must first call
    :py:func:`nidcpower._initiate` before calling this function.

    Refer to the `Acquiring
    Measurements <REPLACE_DRIVER_SPECIFIC_URL_1(acquiringmeasurements)>`__
    and `Compliance <REPLACE_DRIVER_SPECIFIC_URL_1(compliance)>`__ topics in
    the *NI DC Power Supplies and SMUs Help* for more information about
    configuring this function.

    

    .. note:: This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].fetch_multiple(count, timeout=1.0)


    :param timeout:


        Specifies the maximum time allowed for this function to complete, in
        seconds. If the function does not complete within this time interval,
        NI-DCPower returns an error.

        

        .. note:: When setting the timeout interval, ensure you take into account any
            triggers so that the timeout interval is long enough for your
            application.


    :type timeout: float
    :param count:


        Specifies the number of measurements to fetch.

        


    :type count: int

    :rtype: tuple (voltage_measurements, current_measurements, in_compliance, actual_count)

        WHERE

        voltage_measurements (list of float): 


            Returns an array of voltage measurements. Ensure that sufficient space
            has been allocated for the returned array.

            


        current_measurements (list of float): 


            Returns an array of current measurements. Ensure that sufficient space
            has been allocated for the returned array.

            


        in_compliance (list of bool): 


            Returns an array of Boolean values indicating whether the output was in
            compliance at the time the measurement was taken. Ensure that sufficient
            space has been allocated for the returned array.

            


        actual_count (int): 


            Indicates the number of measured values actually retrieved from the
            device.

            



.. function:: get_channel_name(index)

    Retrieves the output **channelName** that corresponds to the requested
    **index**. Use the :py:data:`nidcpower.CHANNEL\_COUNT` attribute to
    determine the upper bound of valid values for **index**.

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].get_channel_name(index)


    :param index:


        Specifies which output channel name to return. The index values begin at
        1.

        


    :type index: int
    :param buffer_size:


        Specifies the number of bytes in the ViChar array you specify for
        **channelName**. If the **channelName**, including the terminating NUL
        byte, contains more bytes than you indicate in this attribute, the
        function copies (buffer size - 1) bytes into the buffer, places an ASCII
        NUL byte at the end of the buffer, and returns the buffer size you must
        pass to get the entire value. For example, if the value is 123456 and
        the buffer size is 4, the function places 123 into the buffer and
        returns 7.
        If you pass 0, you can pass VI\_NULL for **channelName**.

        


    :type buffer_size: int

.. function:: get_self_cal_last_date_and_time()

    Returns the date and time of the oldest successful self-calibration from
    among the channels in the session.

    The time returned is 24-hour (military) local time; for example, if you
    have a session using channels 1 and 2, and a self-calibration was
    performed on channel 1 at 2:30 PM, and a self-calibration was performed
    on channel 2 at 3:00 PM on the same day, this function returns 14 for
    **hours** and 30 for **minutes**.

    

    .. note:: This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.



    :rtype: tuple (year, month, day, hour, minute)

        WHERE

        year (int): 


            Returns the **year** the device was last calibrated.

            


        month (int): 


            Returns the **month** in which the device was last calibrated.

            


        day (int): 


            Returns the **day** on which the device was last calibrated.

            


        hour (int): 


            Returns the **hour** (in 24-hour time) in which the device was last
            calibrated.

            


        minute (int): 


            Returns the **minute** in which the device was last calibrated.

            



.. function:: get_self_cal_last_temp()

    Returns the onboard temperature of the device, in degrees Celsius,
    during the oldest successful self-calibration from among the channels in
    the session.

    For example, if you have a session using channels 1 and 2, and you
    perform a self-calibration on channel 1 with a device temperature of 25
    degrees Celsius at 2:00, and a self-calibration was performed on channel
    2 at 27 degrees Celsius at 3:00 on the same day, this function returns
    25 for the **temperature** parameter.

    

    .. note:: This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.



    :rtype: float
    :return:


            Returns the onboard **temperature** of the device, in degrees Celsius,
            during the oldest successful calibration.

            



.. function:: measure(measurement_type)

    Returns the measured value of either the voltage or current on the
    specified output channel. Each call to this function blocks other
    function calls until the hardware returns the **measurement**. To
    measure multiple output channels, use the :py:func:`nidcpower.MeasureMultiple`
    function.

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].measure(measurement_type)


    :param measurement_type:


        Specifies whether a voltage or current value is measured.
        **Defined Values**:

        +--------------------------------------+------------------------------+
        | NIDCPOWER\_VAL\_MEASURE\_VOLTAGE (1) | The device measures voltage. |
        +--------------------------------------+------------------------------+
        | NIDCPOWER\_VAL\_MEASURE\_CURRENT (0) | The device measures current. |
        +--------------------------------------+------------------------------+


    :type measurement_type: :py:data:`nidcpower.MeasurementTypes`

    :rtype: float
    :return:


            Returns the value of the measurement, either in volts for voltage or
            amps for current.

            



.. function:: query_in_compliance()

    Queries the specified output device to determine if it is operating at
    the `compliance <REPLACE_DRIVER_SPECIFIC_URL_2(compliance)>`__ limit.

    The compliance limit is the current limit when the output function is
    set to NIDCPOWER\_VAL\_DC\_VOLTAGE. If the output is operating at the
    compliance limit, the output reaches the current limit before the
    desired voltage level. Refer to the :py:func:`nidcpower.ConfigureOutputFunction`
    function and the :py:func:`nidcpower.ConfigureCurrentLimit` function for more
    information about output function and current limit, respectively.

    The compliance limit is the voltage limit when the output function is
    set to NIDCPOWER\_VAL\_DC\_CURRENT. If the output is operating at the
    compliance limit, the output reaches the voltage limit before the
    desired current level. Refer to the :py:func:`nidcpower.ConfigureOutputFunction`
    function and the :py:func:`nidcpower.ConfigureVoltageLimit` function for more
    information about output function and voltage limit, respectively.

    **Related Topics:**

    `Compliance <REPLACE_DRIVER_SPECIFIC_URL_1(compliance)>`__

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].query_in_compliance()


    :rtype: bool
    :return:


            Returns whether the device output channel is in compliance.

            



.. function:: query_max_current_limit(voltage_level)

    Queries the maximum current limit on an output channel if the output
    channel is set to the specified **voltageLevel**.

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].query_max_current_limit(voltage_level)


    :param voltage_level:


        Specifies the voltage level to use when calculating the
        **maxCurrentLimit**.

        


    :type voltage_level: float

    :rtype: float
    :return:


            Returns the maximum current limit that can be set with the specified
            **voltageLevel**.

            



.. function:: query_max_voltage_level(current_limit)

    Queries the maximum voltage level on an output channel if the output
    channel is set to the specified **currentLimit**.

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].query_max_voltage_level(current_limit)


    :param current_limit:


        Specifies the current limit to use when calculating the
        **maxVoltageLevel**.

        


    :type current_limit: float

    :rtype: float
    :return:


            Returns the maximum voltage level that can be set on an output channel
            with the specified **currentLimit**.

            



.. function:: query_min_current_limit(voltage_level)

    Queries the minimum current limit on an output channel if the output
    channel is set to the specified **voltageLevel**.

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].query_min_current_limit(voltage_level)


    :param voltage_level:


        Specifies the voltage level to use when calculating the
        **minCurrentLimit**.

        


    :type voltage_level: float

    :rtype: float
    :return:


            Returns the minimum current limit that can be set on an output channel
            with the specified **voltageLevel**.

            



.. function:: query_output_state(output_state)

    Queries the specified output channel to determine if the output channel
    is currently in the state specified by **outputState**.

    **Related Topics:**

    `Compliance <REPLACE_DRIVER_SPECIFIC_URL_1(compliance)>`__

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].query_output_state(output_state)


    :param output_state:


        Specifies the output state of the output channel that is being queried.
        **Defined Values**:

        +-----------------------------------------------+-------------------------------------------------------------------+
        | NIDCPOWER\_VAL\_OUTPUT\_CONSTANT\_VOLTAGE (0) | The device maintains a constant voltage by adjusting the current. |
        +-----------------------------------------------+-------------------------------------------------------------------+
        | NIDCPOWER\_VAL\_OUTPUT\_CONSTANT\_CURRENT (1) | The device maintains a constant current by adjusting the voltage. |
        +-----------------------------------------------+-------------------------------------------------------------------+


    :type output_state: :py:data:`nidcpower.OutputStates`

    :rtype: bool
    :return:


            Returns whether the device output channel is in the specified output
            state.

            



.. function:: read_current_temperature()

    Returns the current onboard **temperature**, in degrees Celsius, of the
    device.

    



    :rtype: float
    :return:


            Returns the onboard **temperature**, in degrees Celsius, of the device.

            



.. function:: reset_device()

    Resets the device to a known state. The function disables power
    generation, resets session attributes to their default values, clears
    errors such as overtemperature and unexpected loss of auxiliary power,
    commits the session attributes, and leaves the session in the
    Uncommitted state. This function also performs a hard reset on the
    device and driver software. This function has the same functionality as
    using reset in Measurement & Automation Explorer. Refer to the
    `Programming
    States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic for
    more information about NI-DCPower software states.

    This will also open the output relay on devices that have an output
    relay.

    



.. function:: reset_with_defaults()

    Resets the device to a known state. This function disables power
    generation, resets session attributes to their default values, commits
    the session attributes, and leaves the session in the
    `Running <javascript:LaunchHelp('NI_DC_Power_Supplies_Help.chm::/programmingStates.html#running')>`__
    state. In addition to exhibiting the behavior of the :py:func:`nidcpower.reset`
    function, this function can assign user-defined default values for
    configurable attributes from the IVI configuration.

    



.. function:: send_software_edge_trigger(trigger=nidcpower.SendSoftwareEdgeTriggerType.START)

    Asserts the specified trigger. This function can override an external
    edge trigger.

    **Related Topics:**

    `Triggers <REPLACE_DRIVER_SPECIFIC_URL_1(trigger)>`__

    

    .. note:: This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.



    :param trigger:


        Specifies which trigger to assert.
        **Defined Values:**

        +---------------------------------------------------+---------------------------------------+
        | NIDCPOWER\_VAL\_START\_TRIGGER (1034)             | Asserts the Start trigger.            |
        +---------------------------------------------------+---------------------------------------+
        | NIDCPOWER\_VAL\_SOURCE\_TRIGGER (1035)            | Asserts the Source trigger.           |
        +---------------------------------------------------+---------------------------------------+
        | NIDCPOWER\_VAL\_MEASURE\_TRIGGER (1036)           | Asserts the Measure trigger.          |
        +---------------------------------------------------+---------------------------------------+
        | NIDCPOWER\_VAL\_SEQUENCE\_ADVANCE\_TRIGGER (1037) | Asserts the Sequence Advance trigger. |
        +---------------------------------------------------+---------------------------------------+
        | NIDCPOWER\_VAL\_PULSE\_TRIGGER (1053              | Asserts the Pulse trigger.            |
        +---------------------------------------------------+---------------------------------------+


    :type trigger: :py:data:`nidcpower.SendSoftwareEdgeTriggerType`

.. function:: set_sequence(values, source_delays=None)

    Configures a series of voltage or current outputs and corresponding
    source delays. The source mode must be set to
    `Sequence <REPLACE_DRIVER_SPECIFIC_URL_1(sequencing)>`__ for this
    function to take effect.

    Refer to the `Configuring the Source
    Unit <REPLACE_DRIVER_SPECIFIC_URL_1(configuringthesourceunit)>`__ topic
    in the *NI DC Power Supplies and SMUs Help* for more information about
    how to configure your device.

    Use this function in the Uncommitted or Committed programming states.
    Refer to the `Programming
    States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic in
    the *NI DC Power Supplies and SMUs Help* for more information about
    NI-DCPower programming states.

    

    .. note:: This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].set_sequence(values, source_delays=None)


    :param values:


        Specifies the series of voltage levels or current levels, depending on
        the configured `output
        function <REPLACE_DRIVER_SPECIFIC_URL_1(programming_output)>`__.
        **Valid values**:
        The valid values for this parameter are defined by the voltage level
        range or current level range.

        


    :type values: list of float
    :param source_delays:


        Specifies the source delay that follows the configuration of each value
        in the sequence.
        **Valid Values**:
        The valid values are between 0 and 167 seconds.

        


    :type source_delays: list of float
    :param size:


        The number of elements in the Values and the Source Delays arrays. The
        Values and Source Delays arrays should have the same size.

        


    :type size: int

.. function:: wait_for_event(event_id, timeout=10.0)

    Waits until the device has generated the specified event.

    The session monitors whether each type of event has occurred at least
    once since the last time this function or the :py:func:`nidcpower._initiate`
    function were called. If an event has only been generated once and you
    call this function successively, the function times out. Individual
    events must be generated between separate calls of this function.

    

    .. note:: Refer to `Supported Functions by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.



    :param event_id:


        Specifies which event to wait for.
        **Defined Values:**

        +-------------------------------------------------------------+--------------------------------------------------+
        | NIDCPOWER\_VAL\_SOURCE\_COMPLETE\_EVENT (1030)              | Waits for the Source Complete event.             |
        +-------------------------------------------------------------+--------------------------------------------------+
        | NIDCPOWER\_VAL\_MEASURE\_COMPLETE\_EVENT (1031)             | Waits for the Measure Complete event.            |
        +-------------------------------------------------------------+--------------------------------------------------+
        | NIDCPOWER\_VAL\_SEQUENCE\_ITERATION\_COMPLETE\_EVENT (1032) | Waits for the Sequence Iteration Complete event. |
        +-------------------------------------------------------------+--------------------------------------------------+
        | NIDCPOWER\_VAL\_SEQUENCE\_ENGINE\_DONE\_EVENT (1033)        | Waits for the Sequence Engine Done event.        |
        +-------------------------------------------------------------+--------------------------------------------------+
        | NIDCPOWER\_VAL\_PULSE\_COMPLETE\_EVENT (1051 )              | Waits for the Pulse Complete event.              |
        +-------------------------------------------------------------+--------------------------------------------------+
        | NIDCPOWER\_VAL\_READY\_FOR\_PULSE\_TRIGGER\_EVENT (1052)    | Waits for the Ready for Pulse Trigger event.     |
        +-------------------------------------------------------------+--------------------------------------------------+


    :type event_id: :py:data:`nidcpower.Event`
    :param timeout:


        Specifies the maximum time allowed for this function to complete, in
        seconds. If the function does not complete within this time interval,
        NI-DCPower returns an error.

        

        .. note:: When setting the timeout interval, ensure you take into account any
            triggers so that the timeout interval is long enough for your
            application.


    :type timeout: float

.. function:: reset()

    Resets the device to a known state. This function disables power
    generation, resets session attributes to their default values, commits
    the session attributes, and leaves the session in the Uncommitted state.
    Refer to the `Programming
    States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic for
    more information about NI-DCPower software states.

    



.. function:: self_test()

    Performs the device self-test routine and returns the test result(s).
    Calling this function implicitly calls the :py:func:`nidcpower.reset` function.

    



    :rtype: tuple (self_test_result, self_test_message)

        WHERE

        self_test_result (int): 


            Returns the value result from the device self-test.

            +----------------+-------------------+
            | Self-Test Code | Description       |
            +================+===================+
            | 0              | Self test passed. |
            +----------------+-------------------+
            | 1              | Self test failed. |
            +----------------+-------------------+


        self_test_message (string): 


            Returns the self-test result message. The size of this array must be at
            least 256 bytes.

            




