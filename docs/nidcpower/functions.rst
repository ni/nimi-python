nidcpower.Session methods
=========================

.. py:currentmodule:: nidcpower

.. function:: commit()

    Vistatus :py:func:`nidcpower.commit`(ViSession vi);

    Applies previously configured settings to the device. Calling this
    function moves the NI-DCPower session from the Uncommitted state into
    the Committed state. After calling this function, modifying any
    attribute reverts the NI-DCPower session to the Uncommitted state. Use
    the
    `:py:func:`nidcpower._initiate` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_Initiate.html')>`__
    function to transition to the Running state. Refer to the `Programming
    States <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/programmingstates/>`__
    topic in the *NI DC Power Supplies and SMUs Help* for details about the
    specific NI-DCPower software states.

    **Related Topics:**

    `Programming
    States <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/programmingstates/>`__

    


.. function:: configure_aperture_time(aperture_time, units)

    Vistatus :py:func:`nidcpower.configure_aperture_time`(ViSession vi, ViConstString
    channelName, ViReal64 apertureTime, ViInt32 units);

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

    `Aperture
    Time <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/aperture/>`__

    

    .. note:: This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'supportedFunctions.html')>`__
        for more information about supported devices.


    :param channel_name:


        Specifies the output channel(s) to which this configuration value
        applies. Specify multiple channels by using a channel list or a channel
        range. A channel list is a comma (,) separated sequence of channel names
        (for example, 0,2 specifies channels 0 and 2). A channel range is a
        lower bound channel followed by a hyphen (-) or colon (:) followed by an
        upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
        In the Running state, multiple output channel configurations are
        performed sequentially based on the order specified in this parameter.

        

    :type channel_name: string
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

    :type units: int

.. function:: configure_digital_edge_measure_trigger(input_terminal, edge)

    Vistatus :py:func:`nidcpower.configure_digital_edge_measure_trigger`(ViSession vi,
    ViConstString inputTerminal, ViInt32 edge);

    Configures the Measure trigger for digital edge triggering.

    

    .. note:: This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'supportedFunctions.html')>`__
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

    :type edge: int

.. function:: configure_digital_edge_pulse_trigger(input_terminal, edge)

    Vistatus :py:func:`nidcpower.configure_digital_edge_pulse_trigger`(ViSession vi,
    ViConstString inputTerminal, ViInt32 edge);

    Configures the Pulse trigger for digital edge triggering.

    

    .. note:: This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'supportedFunctions.html')>`__
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

    :type edge: int

.. function:: configure_digital_edge_sequence_advance_trigger(input_terminal, edge)

    Vistatus :py:func:`nidcpower.configure_digital_edge_sequence_advance_trigger`(ViSession
    vi, ViConstString inputTerminal, ViInt32 edge);

    Configures the Sequence Advance trigger for digital edge triggering.

    

    .. note:: This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'supportedFunctions.html')>`__
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

    :type edge: int

.. function:: configure_digital_edge_source_trigger(input_terminal, edge)

    Vistatus :py:func:`nidcpower.configure_digital_edge_source_trigger`(ViSession vi,
    ViConstString inputTerminal, ViInt32 edge);

    Configures the Source trigger for digital edge triggering.

    

    .. note:: This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'supportedFunctions.html')>`__
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

    :type edge: int

.. function:: configure_digital_edge_start_trigger(input_terminal, edge)

    Vistatus :py:func:`nidcpower.configure_digital_edge_start_trigger`(ViSession vi,
    ViConstString inputTerminal, ViInt32 edge);

    Configures the Start trigger for digital edge triggering.

    

    .. note:: This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'supportedFunctions.html')>`__
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

    :type edge: int

.. function:: create_advanced_sequence(sequence_name, attribute_id_count, attribute_ids, set_as_active_sequence)

    Vistatus :py:func:`nidcpower.create_advanced_sequence`(ViSession vi, ViConstString
    sequenceName, ViInt32 attributeIDCount,ViInt32 attributeIDs[], viBoolean
    setAsActiveSequence);

    Creates an empty advanced sequence. Call the
    :py:func:`nidcpower.create_advanced_sequence_step` function to add steps to the
    active advanced sequence.

    **Support for this function**

    You must set the source mode to Sequence to use this function.

    Using the :py:func:`nidcpower.set_sequence` function with Advanced Sequence
    functions is unsupported.

    Use this function in the Uncommitted or Committed programming states.
    Refer to the `Programming
    States <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/programmingstates/>`__
    topic in the *NI DC Power Supplies and SMUs Help* for more information
    about NI-DCPower programming states.

    **Related Topics**:

    `Advanced Sequence
    Mode <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/advancedsequencemode/>`__

    `Programming
    States <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/programmingstates/>`__

    `:py:func:`nidcpower.create_advanced_sequence_step` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_CreateAdvancedSequenceStep.html')>`__

    

    .. note:: This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'supportedFunctions.html')>`__
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

        +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | Attribute                                                                                                                                                                                               | PXIe-4135 | NI 4136 | NI 4137 | NI 4138 | NI 4139 | NI 4140/4142/4144 | NI 4141/4143/4145 | PXIe-4162/4163 |
        +=========================================================================================================================================================================================================+===========+=========+=========+=========+=========+===================+===================+================+
        | `:py:data:`nidcpower.DC\_NOISE\_REJECTION` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_DC_NOISE_REJECTION.html')>`__                         | ✓         | ✕       | ✓       | ✕       | ✓       | ✕                 | ✕                 | ✓              |
        +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | `:py:data:`nidcpower.APERTURE\_TIME` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_APERTURE_TIME.html')>`__                                    | ✓         | ✓       | ✓       | ✓       | ✓       | ✓                 | ✓                 | ✓              |
        +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | `:py:data:`nidcpower.MEASURE\_RECORD\_LENGTH` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_MEASURE_RECORD_LENGTH.html')>`__                   | ✓         | ✓       | ✓       | ✓       | ✓       | ✓                 | ✓                 | ✓              |
        +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | `:py:data:`nidcpower.sense` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_SENSE.html')>`__                                                     | ✓         | ✓       | ✓       | ✓       | ✓       | ✓                 | ✓                 | ✓              |
        +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | `:py:data:`nidcpower.OVP\_ENABLED` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_OVP_ENABLED.html')>`__                                        | ✓         | ✓       | ✓       | ✕       | ✕       | ✕                 | ✕                 | ✕              |
        +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | `:py:data:`nidcpower.OVP\_LIMIT` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_OVP_LIMIT.html')>`__                                            | ✓         | ✓       | ✓       | ✕       | ✕       | ✕                 | ✕                 | ✕              |
        +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | `:py:data:`nidcpower.PULSE\_BIAS\_DELAY` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_PULSE_BIAS_DELAY.html')>`__                             | ✓         | ✓       | ✓       | ✓       | ✓       | ✕                 | ✕                 | ✕              |
        +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | `:py:data:`nidcpower.PULSE\_OFF\_TIME` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_PULSE_OFF_TIME.html')>`__                                 | ✓         | ✓       | ✓       | ✓       | ✓       | ✕                 | ✕                 | ✕              |
        +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | `:py:data:`nidcpower.PULSE\_ON\_TIME` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_PULSE_ON_TIME.html')>`__                                   | ✓         | ✓       | ✓       | ✓       | ✓       | ✕                 | ✕                 | ✕              |
        +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | `:py:data:`nidcpower.SOURCE\_DELAY` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_SOURCE_DELAY.html')>`__                                      | ✓         | ✓       | ✓       | ✓       | ✓       | ✓                 | ✓                 | ✓              |
        +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | `:py:data:`nidcpower.CURRENT\_COMPENSATION\_FREQUENCY` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_CURRENT_COMPENSATION_FREQUENCY.html')>`__ | ✓         | ✕       | ✓       | ✕       | ✓       | ✕                 | ✓                 | ✓              |
        +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | `:py:data:`nidcpower.CURRENT\_GAIN\_BANDWIDTH` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_CURRENT_GAIN_BANDWIDTH.html')>`__                 | ✓         | ✕       | ✓       | ✕       | ✓       | ✕                 | ✓                 | ✓              |
        +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | `:py:data:`nidcpower.CURRENT\_POLE\_ZERO\_RATIO` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_CURRENT_POLE_ZERO_RATIO.html')>`__              | ✓         | ✕       | ✓       | ✕       | ✓       | ✕                 | ✓                 | ✓              |
        +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | `:py:data:`nidcpower.VOLTAGE\_COMPENSATION\_FREQUENCY` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_VOLTAGE_COMPENSATION_FREQUENCY.html')>`__ | ✓         | ✕       | ✓       | ✕       | ✓       | ✕                 | ✓                 | ✓              |
        +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | `:py:data:`nidcpower.VOLTAGE\_GAIN\_BANDWIDTH` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_VOLTAGE_GAIN_BANDWIDTH.html')>`__                 | ✓         | ✕       | ✓       | ✕       | ✓       | ✕                 | ✓                 | ✓              |
        +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | `:py:data:`nidcpower.VOLTAGE\_POLE\_ZERO\_RATIO` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_VOLTAGE_POLE_ZERO_RATIO.html')>`__              | ✓         | ✕       | ✓       | ✕       | ✓       | ✕                 | ✓                 | ✓              |
        +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | `:py:data:`nidcpower.CURRENT\_LEVEL` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_CURRENT_LEVEL.html')>`__                                    | ✓         | ✓       | ✓       | ✓       | ✓       | ✓                 | ✓                 | ✓              |
        +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | `:py:data:`nidcpower.CURRENT\_LEVEL\_RANGE` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_CURRENT_LEVEL_RANGE.html')>`__                       | ✓         | ✓       | ✓       | ✓       | ✓       | ✓                 | ✓                 | ✓              |
        +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | `:py:data:`nidcpower.VOLTAGE\_LIMIT` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_VOLTAGE_LIMIT.html')>`__                                    | ✓         | ✓       | ✓       | ✓       | ✓       | ✓                 | ✓                 | ✓              |
        +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | `:py:data:`nidcpower.VOLTAGE\_LIMIT\_RANGE` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_VOLTAGE_LIMIT_RANGE.html')>`__                       | ✓         | ✓       | ✓       | ✓       | ✓       | ✓                 | ✓                 | ✓              |
        +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | `:py:data:`nidcpower.CURRENT\_LIMIT` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_CURRENT_LIMIT.html')>`__                                    | ✓         | ✓       | ✓       | ✓       | ✓       | ✓                 | ✓                 | ✓              |
        +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | `:py:data:`nidcpower.CURRENT\_LIMIT\_RANGE` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_CURRENT_LIMIT_RANGE.html')>`__                       | ✓         | ✓       | ✓       | ✓       | ✓       | ✓                 | ✓                 | ✓              |
        +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | `:py:data:`nidcpower.VOLTAGE\_LEVEL` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_VOLTAGE_LEVEL.html')>`__                                    | ✓         | ✓       | ✓       | ✓       | ✓       | ✓                 | ✓                 | ✓              |
        +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | `:py:data:`nidcpower.VOLTAGE\_LEVEL\_RANGE` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_VOLTAGE_LEVEL_RANGE.html')>`__                       | ✓         | ✓       | ✓       | ✓       | ✓       | ✓                 | ✓                 | ✓              |
        +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | `:py:data:`nidcpower.OUTPUT\_ENABLED` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_OUTPUT_ENABLED.html')>`__                                  | ✓         | ✓       | ✓       | ✓       | ✓       | ✓                 | ✓                 | ✓              |
        +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | `:py:data:`nidcpower.OUTPUT\_FUNCTION` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_OUTPUT_FUNCTION.html')>`__                                | ✓         | ✓       | ✓       | ✓       | ✓       | ✓                 | ✓                 | ✓              |
        +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | `:py:data:`nidcpower.OUTPUT\_RESISTANCE` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_OUTPUT_RESISTANCE.html')>`__                            | ✓         | ✕       | ✓       | ✕       | ✓       | ✕                 | ✓                 | ✕              |
        +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | `:py:data:`nidcpower.PULSE\_BIAS\_CURRENT\_LEVEL` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LEVEL.html')>`__            | ✓         | ✓       | ✓       | ✓       | ✓       | ✕                 | ✕                 | ✕              |
        +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | `:py:data:`nidcpower.PULSE\_BIAS\_VOLTAGE\_LIMIT` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT.html')>`__            | ✓         | ✓       | ✓       | ✓       | ✓       | ✕                 | ✕                 | ✕              |
        +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | `:py:data:`nidcpower.PULSE\_CURRENT\_LEVEL` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL.html')>`__                       | ✓         | ✓       | ✓       | ✓       | ✓       | ✕                 | ✕                 | ✕              |
        +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | `:py:data:`nidcpower.PULSE\_CURRENT\_LEVEL\_RANGE` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL_RANGE.html')>`__          | ✓         | ✓       | ✓       | ✓       | ✓       | ✕                 | ✕                 | ✕              |
        +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | `:py:data:`nidcpower.PULSE\_VOLTAGE\_LIMIT` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT.html')>`__                       | ✓         | ✓       | ✓       | ✓       | ✓       | ✕                 | ✕                 | ✕              |
        +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | `:py:data:`nidcpower.PULSE\_VOLTAGE\_LIMIT\_RANGE` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_RANGE.html')>`__          | ✓         | ✓       | ✓       | ✓       | ✓       | ✕                 | ✕                 | ✕              |
        +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | `:py:data:`nidcpower.PULSE\_BIAS\_CURRENT\_LIMIT` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT.html')>`__            | ✓         | ✓       | ✓       | ✓       | ✓       | ✕                 | ✕                 | ✕              |
        +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | `:py:data:`nidcpower.PULSE\_BIAS\_VOLTAGE\_LEVEL` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LEVEL.html')>`__            | ✓         | ✓       | ✓       | ✓       | ✓       | ✕                 | ✕                 | ✕              |
        +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | `:py:data:`nidcpower.PULSE\_CURRENT\_LIMIT` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT.html')>`__                       | ✓         | ✓       | ✓       | ✓       | ✓       | ✕                 | ✕                 | ✕              |
        +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | `:py:data:`nidcpower.PULSE\_CURRENT\_LIMIT\_RANGE` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_RANGE.html')>`__          | ✓         | ✓       | ✓       | ✓       | ✓       | ✕                 | ✕                 | ✕              |
        +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | `:py:data:`nidcpower.PULSE\_VOLTAGE\_LEVEL` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL.html')>`__                       | ✓         | ✓       | ✓       | ✓       | ✓       | ✕                 | ✕                 | ✕              |
        +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | `:py:data:`nidcpower.PULSE\_VOLTAGE\_LEVEL\_RANGE` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL_RANGE.html')>`__          | ✓         | ✓       | ✓       | ✓       | ✓       | ✕                 | ✕                 | ✕              |
        +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+
        | `:py:data:`nidcpower.TRANSIENT\_RESPONSE` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_TRANSIENT_RESPONSE.html')>`__                          | ✓         | ✓       | ✓       | ✓       | ✓       | ✓                 | ✓                 | ✓              |
        +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+---------+---------+---------+---------+-------------------+-------------------+----------------+

    :type attribute_ids: list of int
    :param set_as_active_sequence:


        Specifies that this current sequence is active.

        

    :type set_as_active_sequence: bool

.. function:: create_advanced_sequence_step(set_as_active_step)

    Vistatus :py:func:`nidcpower.create_advanced_sequence_step`(ViSession vi, viBoolean
    setAsActiveSequenceStep);

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
    Mode <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/advancedsequencemode/>`__

    `Programming
    States <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/programmingstates/>`__

    `:py:func:`nidcpower.create_advanced_sequence` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_CreateAdvancedSequence.html')>`__

    

    .. note:: This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'supportedFunctions.html')>`__
        for more information about supported devices.


    :param set_as_active_step:


        Specifies that this current step in the active sequence is active.

        

    :type set_as_active_step: bool

.. function:: delete_advanced_sequence(sequence_name)

    Vistatus :py:func:`nidcpower.delete_advanced_sequence`(ViSession vi, viConstString
    sequenceName);

    Deletes a previously created advanced sequence and all the advanced
    sequence steps in the advanced sequence.

    **Support for this Function**

    You must set the source mode to Sequence to use this function.

    Using the :py:func:`nidcpower.set_sequence` function with Advanced Sequence
    functions is unsupported.

    **Related Topics**:

    `Advanced Sequence
    Mode <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/advancedsequencemode/>`__

    `Programming
    States <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/programmingstates/>`__

    

    .. note:: This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'supportedFunctions.html')>`__
        for more information about supported devices.


    :param sequence_name:


        specifies the name of the sequence to delete.

        

    :type sequence_name: string

.. function:: disable()

    Vistatus :py:func:`nidcpower.disable`(ViSession vi);

    This function performs the same actions as the
    `:py:func:`nidcpower.reset` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_reset.html')>`__
    function, except that this function also immediately sets the
    `:py:data:`nidcpower.OUTPUT\_ENABLED` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_OUTPUT_ENABLED.html')>`__
    attribute to VI\_FALSE.

    This function opens the output relay on devices that have an output
    relay.

    


.. function:: export_signal(signal, signal_identifier, output_terminal)

    Vistatus :py:func:`nidcpower.export_signal`(ViSession vi, ViInt32 signal,
    ViConstString signalIdentifier, ViConstString outputTerminal);

    Routes signals (triggers and events) to the output terminal you specify.
    The route is created when the session is
    `committed <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_Commit.html')>`__.

    **Related Topics:**

    `Triggers <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/trigger/>`__

    

    .. note:: This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'supportedFunctions.html')>`__
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

    :type signal: int
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

.. function:: fetch_multiple(timeout, count)

    Vistatus :py:func:`nidcpower.fetch_multiple`(ViSession vi, ViConstString
    channelName, ViReal64 timeout, ViInt32 count, ViReal64
    voltageMeasurements[], ViReal64 currentMeasurements[], ViBoolean
    inCompliance[], ViInt32\* actualcount);

    Returns an array of voltage measurements, an array of current
    measurements, and an array of compliance measurements that were
    previously taken and are stored in the NI-DCPower buffer. This function
    should not be used when the
    `:py:data:`nidcpower.MEASURE\_WHEN` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_MEASURE_WHEN.html')>`__
    attribute is set to NIDCPOWER\_VAL\_ON\_DEMAND. You must first call
    `:py:func:`nidcpower._initiate` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_Initiate.html')>`__
    before calling this function.

    Refer to the `Acquiring
    Measurements <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/acquiringmeasurements/>`__
    and
    `Compliance <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/compliance/>`__
    topics in the *NI DC Power Supplies and SMUs Help* for more information
    about configuring this function.

    

    .. note:: This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'supportedFunctions.html')>`__
        for more information about supported devices.


    :param channel_name:


        Specifies the output channel(s) to which this configuration value
        applies. Specify multiple channels by using a channel list or a channel
        range. A channel list is a comma (,) separated sequence of channel names
        (for example, 0,2 specifies channels 0 and 2). A channel range is a
        lower bound channel followed by a hyphen (-) or colon (:) followed by an
        upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
        In the Running state, multiple output channel configurations are
        performed sequentially based on the order specified in this parameter.

        

    :type channel_name: string
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

    ViStatus :py:func:`nidcpower.get_channel_name`(ViSession vi, ViInt32 index, ViInt32
    bufferSize, ViChar channelName[]);

    Retrieves the output **channelName** that corresponds to the requested
    **index**. Use the
    `:py:data:`nidcpower.CHANNEL\_COUNT` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_CHANNEL_COUNT.html')>`__
    attribute to determine the upper bound of valid values for **index**.

    


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

    Vistatus :py:func:`nidcpower.get_self_cal_last_date_and_time`(ViSession vi, ViInt32
    \*year, ViInt32 \*month, ViInt32 \*day, ViInt32 \*hour, ViInt32
    \*minute);

    Returns the date and time of the oldest successful self-calibration from
    among the channels in the session.

    The time returned is 24-hour (military) local time; for example, if you
    have a session using channels 1 and 2, and a self-calibration was
    performed on channel 1 at 2:30 PM, and a self-calibration was performed
    on channel 2 at 3:00 PM on the same day, this function returns 14 for
    **hours** and 30 for **minutes**.

    

    .. note:: This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'supportedFunctions.html')>`__
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

    Vistatus :py:func:`nidcpower.get_self_cal_last_temp`(ViSession vi, ViReal64
    \*temperature);

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
        Device <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'supportedFunctions.html')>`__
        for more information about supported devices.


    :rtype: float
    :return:


            Returns the onboard **temperature** of the device, in degrees Celsius,
            during the oldest successful calibration.

            


.. function:: measure(measurement_type)

    Vistatus :py:func:`nidcpower.measure`(ViSession vi, ViConstString channelName,
    ViInt32 measurementType, ViReal64 \*measurement)

    Returns the measured value of either the voltage or current on the
    specified output channel. Each call to this function blocks other
    function calls until the hardware returns the **measurement**. To
    measure multiple output channels, use the
    `:py:func:`nidcpower.measure_multiple` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_MeasureMultiple.html')>`__
    function.

    


    :param channel_name:


        Specifies the output channel to measure. Only one measurement at a time
        may be made with the :py:func:`nidcpower.measure` function. Use the
        `:py:func:`nidcpower.measure_multiple` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_MeasureMultiple.html')>`__
        function to measure multiple channels.

        

    :type channel_name: string
    :param measurement_type:


        Specifies whether a voltage or current value is measured.
        **Defined Values**:

        +--------------------------------------+------------------------------+
        | NIDCPOWER\_VAL\_MEASURE\_VOLTAGE (1) | The device measures voltage. |
        +--------------------------------------+------------------------------+
        | NIDCPOWER\_VAL\_MEASURE\_CURRENT (0) | The device measures current. |
        +--------------------------------------+------------------------------+

    :type measurement_type: int

    :rtype: float
    :return:


            Returns the value of the measurement, either in volts for voltage or
            amps for current.

            


.. function:: measure_multiple()

    Vistatus :py:func:`nidcpower.measure_multiple`(ViSession vi, ViConstString
    channelName, ViReal64 voltageMeasurements[], ViReal64
    currentMeasurements[]);

    Returns arrays of the measured voltage and current values on the
    specified output channel(s). Each call to this function blocks other
    function calls until the measurements are returned from the device. The
    order of the measurements returned in the array corresponds to the order
    on the specified output channel(s).

    


    :param channel_name:


        Specifies the output channels to measure. You can specify multiple
        channels by using a channel list or a channel range. A channel list is a
        comma (,) separated sequence of channel names (e.g. 0,2 specifies
        channels 0 and 2). A channel range is a lower bound channel followed by
        a hyphen (-) or colon (:) followed by an upper bound channel (e.g. 0-2
        specifies channels 0, 1, and 2). If you do not specify a channel name,
        the function uses all channels in the session.

        

    :type channel_name: string

    :rtype: tuple (voltage_measurements, current_measurements)

        WHERE

        voltage_measurements (list of float): 


            Returns an array of voltage measurements. The measurements in the array
            are returned in the same order as the channels specified in
            **channelName**. Ensure that sufficient space has been allocated for the
            returned array.

            

        current_measurements (list of float): 


            Returns an array of current measurements. The measurements in the array
            are returned in the same order as the channels specified in
            **channelName**. Ensure that sufficient space has been allocated for the
            returned array.

            


.. function:: query_in_compliance()

    Vistatus :py:func:`nidcpower.query_in_compliance`(ViSession vi, ViConstString
    channelName, ViBoolean \*inCompliance);

    Queries the specified output device to determine if it is operating at
    the
    `compliance <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'compliance.html')>`__
    limit.

    The compliance limit is the current limit when the output function is
    set to NIDCPOWER\_VAL\_DC\_VOLTAGE. If the output is operating at the
    compliance limit, the output reaches the current limit before the
    desired voltage level. Refer to the
    `:py:func:`nidcpower.configure_output_function` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigureOutputFunction.html')>`__
    function and the
    `:py:func:`nidcpower.configure_current_limit` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigureCurrentLimit.html')>`__
    function for more information about output function and current limit,
    respectively.

    The compliance limit is the voltage limit when the output function is
    set to NIDCPOWER\_VAL\_DC\_CURRENT. If the output is operating at the
    compliance limit, the output reaches the voltage limit before the
    desired current level. Refer to the :py:func:`nidcpower.configure_output_function`
    function and the
    `:py:func:`nidcpower.configure_voltage_limit` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigureVoltageLimit.html')>`__
    function for more information about output function and voltage limit,
    respectively.

    **Related Topics:**

    `Compliance <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/compliance/>`__

    


    :param channel_name:


        Specifies the output channel to query. Compliance status can only be
        queried for one channel at a time.

        

    :type channel_name: string

    :rtype: bool
    :return:


            Returns whether the device output channel is in compliance.

            


.. function:: query_max_current_limit(voltage_level)

    Vistatus :py:func:`nidcpower.query_max_current_limit`(ViSession vi, ViConstString
    channelName, ViReal64 voltageLevel, ViReal64 \*maxCurrentLimit);

    Queries the maximum current limit on an output channel if the output
    channel is set to the specified **voltageLevel**.

    


    :param channel_name:


        Specifies the output channel to query. The maximum current limit may
        only be queried for one channel at a time.

        

    :type channel_name: string
    :param voltage_level:


        Specifies the voltage level to use when calculating the
        **maxCurrentLimit**.

        

    :type voltage_level: float

    :rtype: float
    :return:


            Returns the maximum current limit that can be set with the specified
            **voltageLevel**.

            


.. function:: query_max_voltage_level(current_limit)

    Vistatus :py:func:`nidcpower.query_max_voltage_level`(ViSession vi, ViConstString
    channelName, ViReal64 currentLimit, ViReal64 \*maxVoltageLevel);

    Queries the maximum voltage level on an output channel if the output
    channel is set to the specified **currentLimit**.

    


    :param channel_name:


        Specifies the output channel to query. The maximum voltage level may
        only be queried for one channel at a time.

        

    :type channel_name: string
    :param current_limit:


        Specifies the current limit to use when calculating the
        **maxVoltageLevel**.

        

    :type current_limit: float

    :rtype: float
    :return:


            Returns the maximum voltage level that can be set on an output channel
            with the specified **currentLimit**.

            


.. function:: query_min_current_limit(voltage_level)

    Vistatus :py:func:`nidcpower.query_min_current_limit`(ViSession vi, ViConstString
    channelName, ViReal64 voltageLevel, ViReal64 \*minCurrentLimit);

    Queries the minimum current limit on an output channel if the output
    channel is set to the specified **voltageLevel**.

    


    :param channel_name:


        Specifies the output channel to query. The minimum current limit may
        only be queried for one channel at a time.

        

    :type channel_name: string
    :param voltage_level:


        Specifies the voltage level to use when calculating the
        **minCurrentLimit**.

        

    :type voltage_level: float

    :rtype: float
    :return:


            Returns the minimum current limit that can be set on an output channel
            with the specified **voltageLevel**.

            


.. function:: query_output_state(output_state)

    Vistatus :py:func:`nidcpower.query_output_state`(ViSession vi, ViConstString
    channelName, ViInt32 outputState, ViBoolean \*inState);

    Queries the specified output channel to determine if the output channel
    is currently in the state specified by **outputState**.

    **Related Topics:**

    `Compliance <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/compliance/>`__

    


    :param channel_name:


        Specifies the output channel to query. The output state may only be
        queried for one channel at a time.

        

    :type channel_name: string
    :param output_state:


        Specifies the output state of the output channel that is being queried.
        **Defined Values**:

        +-----------------------------------------------+-------------------------------------------------------------------+
        | NIDCPOWER\_VAL\_OUTPUT\_CONSTANT\_VOLTAGE (0) | The device maintains a constant voltage by adjusting the current. |
        +-----------------------------------------------+-------------------------------------------------------------------+
        | NIDCPOWER\_VAL\_OUTPUT\_CONSTANT\_CURRENT (1) | The device maintains a constant current by adjusting the voltage. |
        +-----------------------------------------------+-------------------------------------------------------------------+

    :type output_state: int

    :rtype: bool
    :return:


            Returns whether the device output channel is in the specified output
            state.

            


.. function:: read_current_temperature()

    Vistatus :py:func:`nidcpower.read_current_temperature`(ViSession vi, ViReal64
    \*temperature);

    Returns the current onboard **temperature**, in degrees Celsius, of the
    device.

    


    :rtype: float
    :return:


            Returns the onboard **temperature**, in degrees Celsius, of the device.

            


.. function:: reset_device()

    Vistatus :py:func:`nidcpower.reset_device`(ViSession vi);

    Resets the device to a known state. The function disables power
    generation, resets session attributes to their default values, clears
    errors such as overtemperature and unexpected loss of auxiliary power,
    commits the session attributes, and leaves the session in the
    Uncommitted state. This function also performs a hard reset on the
    device and driver software. This function has the same functionality as
    using reset in Measurement & Automation Explorer. Refer to the
    `Programming
    States <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/programmingstates/>`__
    topic for more information about NI-DCPower software states.

    This will also open the output relay on devices that have an output
    relay.

    


.. function:: reset_with_defaults()

    Vistatus :py:func:`nidcpower.reset_with_defaults`(ViSession vi);

    Resets the device to a known state. This function disables power
    generation, resets session attributes to their default values, commits
    the session attributes, and leaves the session in the
    `Running <javascript:LaunchHelp('NI_DC_Power_Supplies_Help.chm::/programmingStates.html#running')>`__
    state. In addition to exhibiting the behavior of the
    `:py:func:`nidcpower.reset` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_reset.html')>`__
    function, this function can assign user-defined default values for
    configurable attributes from the IVI configuration.

    


.. function:: send_software_edge_trigger(trigger)

    Vistatus :py:func:`nidcpower.send_software_edge_trigger`(ViSession vi, ViInt32
    trigger);

    Asserts the specified trigger. This function can override an external
    edge trigger.

    **Related Topics:**

    `triggers <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/trigger/>`__

    

    .. note:: This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'supportedFunctions.html')>`__
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

    :type trigger: int

.. function:: set_sequence(values, source_delays, size)

    Vistatus :py:func:`nidcpower.set_sequence`(ViSession vi, ViConstString channelName,
    ViReal64 values[], ViReal64 sourceDelays[], ViUInt32 size);

    Configures a series of voltage or current outputs and corresponding
    source delays. The source mode must be set to
    `Sequence <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/sequencing/>`__
    for this function to take effect.

    Refer to the `Configuring the Source
    Unit <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/configuringthesourceunit/>`__
    topic in the *NI DC Power Supplies and SMUs Help* for more information
    about how to configure your device.

    Use this function in the Uncommitted or Committed programming states.
    Refer to the `Programming
    States <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/programmingstates/>`__
    topic in the *NI DC Power Supplies and SMUs Help* for more information
    about NI-DCPower programming states.

    

    .. note:: This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'supportedFunctions.html')>`__
        for more information about supported devices.


    :param channel_name:


        Specifies the output channel to which this configuration value applies.
        You can only set a sequence for one channel at a time.

        

    :type channel_name: string
    :param values:


        Specifies the series of voltage levels or current levels, depending on
        the configured `output
        function <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/programming_output/>`__.
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

.. function:: wait_for_event(event_id, timeout)

    Vistatus :py:func:`nidcpower.wait_for_event`(ViSession vi, ViInt32 eventId, ViReal64
    timeout);

    Waits until the device has generated the specified event.

    The session monitors whether each type of event has occurred at least
    once since the last time this function or the
    `:py:func:`nidcpower._initiate` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_Initiate.html')>`__
    function were called. If an event has only been generated once and you
    call this function successively, the function times out. Individual
    events must be generated between separate calls of this function.

    

    .. note:: Refer to `Supported Functions by
        Device <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'supportedFunctions.html')>`__
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

    :type event_id: int
    :param timeout:


        Specifies the maximum time allowed for this function to complete, in
        seconds. If the function does not complete within this time interval,
        NI-DCPower returns an error.

        

        .. note:: When setting the timeout interval, ensure you take into account any
            triggers so that the timeout interval is long enough for your
            application.

    :type timeout: float

.. function:: reset()

    Vistatus :py:func:`nidcpower.reset`(ViSession vi);

    Resets the device to a known state. This function disables power
    generation, resets session attributes to their default values, commits
    the session attributes, and leaves the session in the Uncommitted state.
    Refer to the `Programming
    States <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/programmingstates/>`__
    topic for more information about NI-DCPower software states.

    


.. function:: revision_query()

    Vistatus :py:func:`nidcpower.revision_query`(ViSession vi, ViChar
    instrumentDriverRevision[], ViChar firmwareRevision[]);

    Returns the revision information of NI-DCPower and the device firmware.

    


    :rtype: tuple (instrument_driver_revision, firmware_revision)

        WHERE

        instrument_driver_revision (string): 


            Returns the driver revision information for NI-DCPower.

            

        firmware_revision (string): 


            Returns firmware revision information for the device you are using. The
            size of this array must be at least 256 bytes.

            


.. function:: self_test()

    Vistatus :py:func:`nidcpower.self_test`(ViSession vi, ViInt16 \*selfTestResult,
    ViChar selfTestMessage[]);

    Performs the device self-test routine and returns the test result(s).
    Calling this function implicitly calls the
    `:py:func:`nidcpower.reset` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_reset.html')>`__
    function.

    


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

            



