nidcpower.Session methods
=========================

.. py:currentmodule:: nidcpower

.. function:: abort()

    Vistatus :py:func:`nidcpower.abort`(ViSession vi);

    Transitions the NI-DCPower session from the Running state to the
    Committed state. If a sequence is running, it is stopped. Any
    configuration functions called after this function are not applied until
    the
    `:py:func:`nidcpower.initiate` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_Initiate.html')>`__
    function is called. If power output is enabled when you call the
    :py:func:`nidcpower.abort` function, the output channels remain in their current
    state and continue providing power.

    Use the
    `:py:func:`nidcpower.configure_output_enabled` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_ConfigureOutputEnabled.html')>`__
    function to disable power output on a per channel basis. Use the
    `:py:func:`nidcpower.reset` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_reset.html')>`__
    function to disable output on all channels.

    Refer to the `Programming
    States <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/programmingstates/>`__
    topic in the *NI DC Power Supplies and SMUs Help* for information about
    the specific NI-DCPower software states.

    **Related Topics:**

    `Programming
    States <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/programmingstates/>`__

    


.. function:: cal_adjust_current_limit(range, number_of_measurements, requested_outputs, measured_outputs)

    Vistatus :py:func:`nidcpower.cal_adjust_current_limit`(ViSession vi, ViConstString
    channelName, ViReal64 range, ViUInt32 numberOfMeasurements, ViReal64
    requestedOutputs[], ViReal64 measuredOutputs[]);

    Calculates the calibration constants for the current limit for the
    specified output channel and range. This function compares the array in
    **requestedOutputs** to the array in **measuredOutputs** and calculates
    the calibration constants for the current limit returned by the device.
    Refer to the calibration procedure for the device you are calibrating
    for detailed instructions on the appropriate use of this function. This
    function can only be called from an external calibration session.

    

    .. note:: This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'supportedFunctions.html')>`__
        for more information about supported devices.


    :param channel_name:


        Specifies the channel name to which these calibration settings apply.

        

    :type channel_name: int
    :param range:


        Specifies the range to calibrate with these settings. Only one channel
        at a time may be calibrated.

        

    :type range: float
    :param number_of_measurements:


        Specifies the number of elements in **requestedOutputs** and
        **measuredOutputs**.

        

    :type number_of_measurements: int
    :param requested_outputs:


        Specifies an array of the output values that were requested in the
        `:py:func:`nidcpower.configure_current_limit` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_ConfigureCurrentLimit.html')>`__
        function.

        

    :type requested_outputs: float
    :param measured_outputs:


        Specifies an array of the output values measured by an external
        precision digital multimeter.

        

    :type measured_outputs: float

.. function:: cal_adjust_current_measurement(range, number_of_measurements, reported_outputs, measured_outputs)

    Vistatus :py:func:`nidcpower.cal_adjust_current_measurement`(ViSession vi,
    ViConstString channelName, ViReal64 range, ViUInt32
    numberOfMeasurements, ViReal64 reportedOutputs[], ViReal64
    measuredOutputs[]);

    Calibrates the current measurements returned by the
    `:py:func:`nidcpower.measure` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_Measure.html')>`__
    function for the specified output channel. This function calculates new
    calibration coefficients for the specified current measurement range
    based on the **reportedOutputs** and **measuredOutputs**. Refer to the
    calibration procedure for the device you are calibrating for detailed
    instructions about the appropriate use of this function. This function
    can only be called in an external calibration session.

    


    :param channel_name:


        Specifies the output channel name to which these calibration settings
        apply.

        

    :type channel_name: int
    :param range:


        Specifies the range to calibrate with these settings. Only one channel
        at a time may be calibrated.

        

    :type range: float
    :param number_of_measurements:


        Specifies the number of elements in **reportedOutputs** and
        **measuredOutputs**.

        

    :type number_of_measurements: int
    :param reported_outputs:


        Specifies an array of the output values that were returned by the
        `:py:func:`nidcpower.measure` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_Measure.html')>`__
        function.

        

    :type reported_outputs: float
    :param measured_outputs:


        Specifies an array of the output values measured by an external
        precision digital multimeter.

        

    :type measured_outputs: float

.. function:: cal_adjust_internal_reference(internal_reference, adjusted_internal_reference)

    Vistatus :py:func:`nidcpower.cal_adjust_internal_reference`(ViSession vi, ViSession
    vi, ViInt32 internal_reference, ViReal64
    adjusted_internal_reference;

    Programs the adjusted reference value to the device. Refer to the
    calibration procedure for the device you are calibrating for detailed
    instructions on the appropriate use of this function. This function can
    only be called from an external calibration session.

    

    .. note:: This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'supportedFunctions.html')>`__
        for more information about supported devices.


    :param internal_reference:


        Specifies the internal reference to be connected to the calibration pin.
        **Defined Values**:

        +-----------------------------------------------------+---------------------------------------------------------+
        | NIDCPOWER\_VAL\_INTERNAL\_REFERENCE\_5V (1054)      | Calibration pin connected to 5 V internal reference.    |
        +-----------------------------------------------------+---------------------------------------------------------+
        | NIDCPOWER\_VAL\_INTERNAL\_REFERENCE\_100KOHM (1055) | Calibration pin connected to 100 kΩ internal reference. |
        +-----------------------------------------------------+---------------------------------------------------------+

    :type internal_reference: int
    :param adjusted_internal_reference:


        Specifies the updated value of the internal reference that will be
        programmed to the device.

        

    :type adjusted_internal_reference: float

.. function:: cal_adjust_output_resistance(number_of_measurements, requested_outputs, measured_outputs)

    Vistatus :py:func:`nidcpower.cal_adjust_output_resistance`(ViSession vi,
    ViConstString channelName, ViUInt32 numberOfValues, ViReal64
    requestedOutputs[], ViReal64 measuredOutputs[]);

    Compares the array in **requestedOutputs** to the array in
    **measuredOutputs** and calculates the calibration constants for the
    output resistance of the specified channel. Refer to the calibration
    procedure for the device you are calibrating for detailed instructions
    on the appropriate use of this function. This function can only be
    called from an external calibration session.

    

    .. note:: This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'supportedFunctions.html')>`__
        for more information about supported devices.


    :param channel_name:


        Specifies the output channel name to which these calibration settings
        apply. Only one channel at a time can be calibrated.

        

    :type channel_name: int
    :param number_of_measurements:


        Specifies the number of elements in **requestedOutputs** and
        **measuredOutputs**.

        

    :type number_of_measurements: int
    :param requested_outputs:


        Specifies an array of the output values that were requested in the
        `:py:func:`nidcpower.configure_output_resistance` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_ConfigureOutputResistance.html')>`__
        function.

        

    :type requested_outputs: float
    :param measured_outputs:


        Specifies an array of the output values measured by an external
        precision digital multimeter.

        

    :type measured_outputs: float

.. function:: cal_adjust_residual_current_offset()

    Vistatus :py:func:`nidcpower.cal_adjust_residual_current_offset`(ViSession vi,
    ViConstString channelName);

    Calculates the calibration constants for the residual current offsets
    for the specified output channel. Residual offsets account for minor
    offset effects on the device that lie outside of the self-calibration
    circuitry. These offsets can include multiplexer input offsets and
    leakage effects from internal switching.

    This function requires that the output be open prior to it being
    invoked.

    Refer to the calibration procedure for the device you are calibrating
    for detailed instructions on the appropriate use of this function. This
    function can be called only in an external calibration session.

    

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

        

    :type channel_name: int

.. function:: cal_adjust_residual_voltage_offset()

    Vistatus :py:func:`nidcpower.cal_adjust_residual_voltage_offset`(ViSession vi,
    ViConstString channelName);

    Calculates the calibration constants for the residual voltage offsets
    for the specified output channel. Residual offsets account for minor
    offset effects on the device that lie outside of the self-calibration
    circuitry. These offsets can include multiplexer input offsets and
    leakage effects from internal switching.

    This function requires that the output be shorted prior to it being
    invoked.

    Refer to the calibration procedure for the device you are calibrating
    for detailed instructions on the appropriate use of this function. This
    function can be called only in an external calibration session.

    

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

        

    :type channel_name: int

.. function:: cal_adjust_voltage_level(range, number_of_measurements, requested_outputs, measured_outputs)

    Vistatus :py:func:`nidcpower.cal_adjust_voltage_level`(ViSession vi,ViConstString
    channelName, ViReal64 range, ViUInt32 numberOfMeasurements, ViReal64
    requestedOutputs[], ViReal64 measuredOutputs[]);

    Calculates the calibration constants for the voltage level for the
    specified output channel. This function compares the array in
    **requestedOutputs** to the array in **measuredOutputs** and calculates
    the calibration constants for the voltage level of the output channel.
    Refer to the calibration procedure of the device you are calibrating for
    detailed instructions on the appropriate use of this function. This
    function can be called only in an external calibration session.

    

    .. note:: This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'supportedFunctions.html')>`__
        for more information about supported devices.


    :param channel_name:


        Specifies the output channel to which these calibration settings apply.

        

    :type channel_name: int
    :param range:


        Specifies the range to calibrate with these settings. Only one channel
        at a time may be calibrated.

        

    :type range: float
    :param number_of_measurements:


        Specifies the number of elements in **requestedOutputs** and
        **measuredOutputs**.

        

    :type number_of_measurements: int
    :param requested_outputs:


        Specifies an array of the output values requested in the
        `:py:func:`nidcpower.configure_voltage_level` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_ConfigureVoltageLevel.html')>`__
        function.

        

    :type requested_outputs: float
    :param measured_outputs:


        Specifies an array of the output values measured by an external
        precision digital multimeter.

        

    :type measured_outputs: float

.. function:: cal_adjust_voltage_measurement(range, number_of_measurements, reported_outputs, measured_outputs)

    Vistatus :py:func:`nidcpower.cal_adjust_voltage_measurement`(ViSession vi,
    ViConstString channelName, ViReal64 range, ViUInt32
    numberOfMeasurements, ViReal64 reportedOutputs[], ViReal64
    measuredOutputs[]);

    Calculates the calibration constants for the voltage measurements
    returned by the
    `:py:func:`nidcpower.measure` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_Measure.html')>`__
    function for the specified output channel. This function compares the
    array in **reportedOutputs** to the array in **measuredOutputs** and
    calculates the calibration constants for the voltage measurements
    returned by the :py:func:`nidcpower.measure` function. Refer to the calibration
    procedure for the device you are calibrating for detailed instructions
    on the appropriate use of this function. This function can only be
    called in an external calibration session.

    


    :param channel_name:


        Specifies the channel name to which these calibration settings apply.

        

    :type channel_name: int
    :param range:


        Specifies the range to calibrate with these settings. Only one channel
        at a time may be calibrated.

        

    :type range: float
    :param number_of_measurements:


        Specifies the number of elements in **reportedOutputs** and
        **measuredOutputs**.

        

    :type number_of_measurements: int
    :param reported_outputs:


        Specifies an array of the output values that were returned by the
        `:py:func:`nidcpower.measure` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_Measure.html')>`__
        function.

        

    :type reported_outputs: float
    :param measured_outputs:


        Specifies an array of the output values measured by an external
        precision digital multimeter.

        

    :type measured_outputs: float

.. function:: cal_self_calibrate()

    Vistatus :py:func:`nidcpower.cal_self_calibrate`(ViSession vi, ViConstString
    channelName);

    Performs a self-calibration upon the specified channel(s).

    This function disables the output, performs several internal
    calculations, and updates calibration values. The updated calibration
    values are written to the device hardware if the
    :py:data:`nidcpower.SELF\_CALIBRATION\_PERSISTENCE` attribute is set to
    NIDCPOWER\_VAL\_WRITE\_TO\_EEPROM. Refer to the
    `:py:data:`nidcpower.SELF\_CALIBRATION\_PERSISTENCE` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_SELF_CALIBRATION_PERSISTENCE.html')>`__
    attribute topic for more information about the settings for this
    attribute.

    Refer to the
    `Self-Calibration <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/selfcal/>`__
    topic for more information about this function.

    **Related Topics:**

    `Self-Calibration <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/selfcal/>`__

    

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

        

    :type channel_name: int

.. function:: change_ext_cal_password(old_password, new_password)

    Vistatus :py:func:`nidcpower.change_ext_cal_password`(ViSession vi, ViConstString
    oldPassword, ViConstString newPassword);

    Changes the **password** that is required to initialize an external
    calibration session. The **password** can be a maximum of four
    alphanumeric characters. If you call this function in a session,
    **password** is changed immediately. If you call this function in an
    external calibration session, **password** is changed only after you
    close the session using the
    `:py:func:`nidcpower.close_ext_cal` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_CloseExtCal.html')>`__
    function with **action** set to NIDCPOWER\_VAL\_COMMIT.

    


    :param old_password:


        Specifies the previous password used to protect the calibration values.

        

    :type old_password: int
    :param new_password:


        Specifies the new password to use to protect the calibration values.

        

    :type new_password: int

.. function:: clear_error()

    Vistatus :py:func:`nidcpower.clear_error`(ViSession vi);

    | Clears the error code and error description for the IVI session. If
      the user specifies a valid IVI session for **vi**, this function
      clears the error information for the session. If the user passes
      VI\_NULL for **vi**, this function clears the error information for
      the current execution thread. If the ViSession parameter is an invalid
      session, the function does nothing and returns an error.
    | The function clears the error code by setting it to VI\_SUCCESS. If
      the error description string is non-NULL, the function de-allocates
      the error description string and sets the address to VI\_NULL.
    | Maintaining the error information separately for each thread is useful
      if the user does not have a session handle to pass to the
      `:py:func:`nidcpower.get_error` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_GetError.html')>`__
      function, which occurs when a call to
      `:py:func:`nidcpower.initialize_with_channels` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_InitializeWithChannels.html')>`__
      fails.

    


.. function:: clear_interchange_warnings()

    Vistatus :py:func:`nidcpower.clear_interchange_warnings`(ViSession vi);

    Clears the list of current interchange warnings.

    


.. function:: close_ext_cal(action)

    Vistatus :py:func:`nidcpower.close_ext_cal`(ViSession vi, ViInt32 action);

    Closes the session specified in **vi** and deallocates the resources
    that NI-DCPower reserved for calibration. Refer to the calibration
    procedure for the device you are calibrating for detailed instructions
    on the appropriate use of this function.

    


    :param action:


        Specifies how to use the calibration values from this session as the
        session is closed.

        **Defined Values**:

        +-------------------------------+-------------------------------------------------------------------------+
        | NIDCPOWER\_VAL\_COMMIT (1002) | The new calibration constants are stored in the EEPROM.                 |
        +-------------------------------+-------------------------------------------------------------------------+
        | NIDCPOWER\_VAL\_CANCEL (1001) | The old calibration constants are kept, and the new ones are discarded. |
        +-------------------------------+-------------------------------------------------------------------------+

    :type action: int

.. function:: commit()

    Vistatus :py:func:`nidcpower.commit`(ViSession vi);

    Applies previously configured settings to the device. Calling this
    function moves the NI-DCPower session from the Uncommitted state into
    the Committed state. After calling this function, modifying any
    attribute reverts the NI-DCPower session to the Uncommitted state. Use
    the
    `:py:func:`nidcpower.initiate` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_Initiate.html')>`__
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

        

    :type channel_name: int
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

.. function:: configure_auto_zero(auto_zero)

    Vistatus :py:func:`nidcpower.configure_auto_zero`(ViSession vi, ViConstString
    channelName, ViInt32 autoZero);

    Configures auto zero for the device.

    Refer to the `NI PXI-4132 Auto
    Zero <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/4132_autozero/>`__
    and `NI PXI-4132 Measurement Configuration and
    Timing <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/4132_measureconfigtiming/>`__
    topics in the *NI DC Power Supplies and SMUs Help* for more information
    about how to configure your measurements.

    **Related Topics:**

    `Auto
    Zero <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/autozero/>`__

    

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

        

    :type channel_name: int
    :param auto_zero:


        Specifies the auto-zero setting. Refer to the *Measurement Configuration
        and Timing* topic and the *Auto Zero* topic for your device for more
        information about how to configure your measurements.
        **Defined Values:**

        +-----------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | NIDCPOWER\_VAL\_OFF (0)     | Disables auto-zero.                                                                                                                                                                                               |
        +-----------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | NIDCPOWER\_VAL\_ONCE (1024) | Makes zero conversions following the first measurement after initiating the device. The device uses these zero conversions for the preceding measurement and future measurements until the device is reinitiated. |
        +-----------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | NIDCPOWER\_VAL\_ON (1)      | Makes zero conversions for every measurement.                                                                                                                                                                     |
        +-----------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    :type auto_zero: int

.. function:: configure_current_level(level)

    Vistatus :py:func:`nidcpower.configure_current_level`(ViSession vi, ViConstString
    channelName, ViReal64 level);

    Configures the current level the device attempts to generate for the
    specified channel(s). The channel must be enabled for the specified
    current level to take effect. Refer to the
    `:py:func:`nidcpower.configure_output_enabled` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_ConfigureOutputEnabled.html')>`__
    function for more information about enabling the output channel.

    The current level setting is applicable only if the output function of
    the channel is set to NIDCPOWER\_VAL\_DC\_CURRENT. Use
    `:py:func:`nidcpower.configure_output_function` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cvinidcpower_ConfigureOutputFunction.html')>`__
    to set the output function. The device actively regulates the current at
    the specified level unless doing so causes a voltage greater than the
    `voltage
    limit <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigureVoltageLimit.html')>`__
    across the channels' output terminals.

    **Related Topics:**

    `Constant Current
    Mode <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/constant_current/>`__

    


    :param channel_name:


        Specifies the output channel(s) to which this configuration value
        applies. Specify multiple channels by using a channel list or a channel
        range. A channel list is a comma (,) separated sequence of channel names
        (for example, 0,2 specifies channels 0 and 2). A channel range is a
        lower bound channel followed by a hyphen (-) or colon (:) followed by an
        upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
        In the Running state, multiple output channel configurations are
        performed sequentially based on the order specified in this parameter.

        

    :type channel_name: int
    :param level:


        Specifies the current level, in amps, to generate for the specified
        channel(s).
        **Valid Values:**
        The valid values for this parameter are defined by the current level
        range that is configured using the
        `:py:func:`nidcpower.configure_current_level_range` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigureCurrentLevelRange.html')>`__
        function.

        

    :type level: float

.. function:: configure_current_level_range(range)

    Vistatus :py:func:`nidcpower.configure_current_level_range`(ViSession vi,
    ViConstString channelName, ViReal64 range);

    Configures the current level range for the specified channel(s). The
    configured range defines the valid values the current level can be set
    to using the
    `:py:func:`nidcpower.configure_current_level` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_ConfigureCurrentLevel.html')>`__
    function. The current level range setting is applicable only if the
    output function of the channel is set to NIDCPOWER\_VAL\_DC\_CURRENT.
    Use
    `:py:func:`nidcpower.configure_output_function` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cvinidcpower_ConfigureOutputFunction.html')>`__
    to set the output function.

    Use the
    `:py:data:`nidcpower.CURRENT\_LEVEL\_AUTORANGE` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','NIDCPOWER_ATTR_CURRENT_LEVEL_AUTORANGE.html')>`__
    attribute to enable automatic selection of the current level range.

    **Related Topics:**

    `ranges <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/ranges/>`__

    


    :param channel_name:


        Specifies the output channel(s) to which this configuration value
        applies. Specify multiple channels by using a channel list or a channel
        range. A channel list is a comma (,) separated sequence of channel names
        (for example, 0,2 specifies channels 0 and 2). A channel range is a
        lower bound channel followed by a hyphen (-) or colon (:) followed by an
        upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
        In the Running state, multiple output channel configurations are
        performed sequentially based on the order specified in this parameter.

        

    :type channel_name: int
    :param range:


        Specifies the current level range, in amps, for the specified channel.
        For valid ranges, refer to the *ranges* topic for your device in the *NI
        DC Power Supplies and SMUs Help*.

        

    :type range: float

.. function:: configure_current_limit(behavior, limit)

    Vistatus :py:func:`nidcpower.configure_current_limit`(ViSession vi, ViConstString
    channelName, ViInt32 behavior, ViReal64 limit);

    | Configures the current limit for the specified channel(s). The channel
      must be enabled for the specified current limit to take effect. Refer
      to the
      `:py:func:`nidcpower.configure_output_enabled` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_ConfigureOutputEnabled.html')>`__
      function for more information about enabling the output channel.
    | The current limit is the current that the output should not exceed
      when generating the desired `voltage
      level <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_ConfigureVoltageLevel.html')>`__.
      The current limit setting is applicable only if the output function of
      the channel is set to NIDCPOWER\_VAL\_DC\_VOLTAGE. Use
      `:py:func:`nidcpower.configure_output_function` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cvinidcpower_ConfigureOutputFunction.html')>`__
      to set the output function.

    **Related Topics:**

    `Compliance <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/compliance/>`__

    


    :param channel_name:


        Specifies the output channel(s) to which this configuration value
        applies. Specify multiple channels by using a channel list or a channel
        range. A channel list is a comma (,) separated sequence of channel names
        (for example, 0,2 specifies channels 0 and 2). A channel range is a
        lower bound channel followed by a hyphen (-) or colon (:) followed by an
        upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
        In the Running state, multiple output channel configurations are
        performed sequentially based on the order specified in this parameter.

        

    :type channel_name: int
    :param behavior:


        Specifies how the output should behave when the current limit is
        reached.
        **Defined Values:**

        +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | NIDCPOWER\_VAL\_CURRENT\_REGULATE | Controls output current so that it does not exceed the current limit. Power continues to generate even if the current limit is reached. |
        +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | NIDCPOWER\_VAL\_CURRENT\_REGULATE | Controls output current so that it does not exceed the current limit. Power continues to generate even if the current limit is reached. |
        +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+

    :type behavior: int
    :param limit:


        Specifies the current limit, in amps, on the specified channel(s). The
        limit is specified as a positive value, but symmetric positive and
        negative limits are enforced simultaneously.
        **Valid Values:**
        The valid values for this parameter are defined by the current limit
        range that is configured using the
        `:py:func:`nidcpower.configure_current_limit_range` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigureCurrentLimitRange.html')>`__
        function.

        

    :type limit: float

.. function:: configure_current_limit_range(range)

    Vistatus :py:func:`nidcpower.configure_current_limit_range`(ViSession vi,
    ViConstString channelName, ViReal64 range);

    Configures the current limit range for the specified channel(s).The
    configured range defines the valid values the current limit can be set
    to using the
    `:py:func:`nidcpower.configure_current_limit` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_ConfigureCurrentLimit.html')>`__
    function. The current limit range setting is applicable only if the
    output function of the channel is set to NIDCPOWER\_VAL\_DC\_VOLTAGE.
    Use
    `:py:func:`nidcpower.configure_output_function` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cvinidcpower_ConfigureOutputFunction.html')>`__
    to set the output function.

    Use the
    `:py:data:`nidcpower.CURRENT\_LIMIT\_AUTORANGE` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','NIDCPOWER_ATTR_CURRENT_LIMIT_AUTORANGE.html')>`__
    attribute to enable automatic selection of the current limit range.

    **Related Topics:**

    `ranges <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/ranges/>`__

    


    :param channel_name:


        Specifies the output channel(s) to which this configuration value
        applies. Specify multiple channels by using a channel list or a channel
        range. A channel list is a comma (,) separated sequence of channel names
        (for example, 0,2 specifies channels 0 and 2). A channel range is a
        lower bound channel followed by a hyphen (-) or colon (:) followed by an
        upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
        In the Running state, multiple output channel configurations are
        performed sequentially based on the order specified in this parameter.

        

    :type channel_name: int
    :param range:


        Specifies the current limit range, in amps, for the specified channel.
        For valid ranges, refer to the *ranges* topic for your device in the *NI
        DC Power Supplies and SMUs Help*.

        

    :type range: float

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

        

    :type input_terminal: int
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

        

    :type input_terminal: int
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

        

    :type input_terminal: int
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

        

    :type input_terminal: int
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

        

    :type input_terminal: int
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

.. function:: configure_output_enabled(enabled)

    Vistatus :py:func:`nidcpower.configure_output_enabled`(ViSession vi, ViConstString
    channelName, ViBoolean enabled);

    Enables or disables generation on the specified channel(s). Depending on
    the selected output function, the voltage level, current level,or output
    resistance must be set in addition to enabling the output to generate
    the desired level. For more information about configuring the output
    level, refer to
    `:py:func:`nidcpower.configure_output_function` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigureOutputFunction.html')>`__.

    

    .. note:: If the device is in the
        `Uncommitted <javascript:LaunchHelp('NI_DC_Power_Supplies_Help.chm::/programmingStates.html#uncommitted')>`__
        state, enabling the output does not take effect until you call the
        `:py:func:`nidcpower.initiate` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_Initiate.html')>`__
        function.


    :param channel_name:


        Specifies the output channel(s) to which this configuration value
        applies. Specify multiple channels by using a channel list or a channel
        range. A channel list is a comma (,) separated sequence of channel names
        (for example, 0,2 specifies channels 0 and 2). A channel range is a
        lower bound channel followed by a hyphen (-) or colon (:) followed by an
        upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
        In the Running state, multiple output channel configurations are
        performed sequentially based on the order specified in this parameter.

        

    :type channel_name: int
    :param enabled:


        Specifies whether the output is enabled or disabled.
        **Defined Values**:

        +-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | VI\_TRUE  | Enables generation on the specified output channel(s).                                                                                                                                              |
        +-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | VI\_FALSE | Disables generation on the specified output channel(s). This parameter has no effect on the output disconnect relay. To toggle the relay, use the :py:data:`nidcpower.OUTPUT\_CONNECTED` attribute. |
        +-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    :type enabled: bool

.. function:: configure_output_function(function)

    Vistatus :py:func:`nidcpower.configure_output_function`(ViSession vi, ViConstString
    channelName, ViInt32 function);

    Configures the function the device attempts to generate for the
    specified channel(s).

    When NIDCPOWER\_VAL\_DC\_VOLTAGE is selected, the device generates the
    desired voltage level on the output as long as the output current is
    below the current limit. The following functions can be used to
    configure the channel when NIDCPOWER\_VAL\_DC\_VOLTAGE is selected:

    -  `:py:func:`nidcpower.configure_voltage_level` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigureVoltageLevel.html')>`__
    -  `:py:func:`nidcpower.configure_current_limit` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigureCurrentLimit.html')>`__
    -  `:py:func:`nidcpower.configure_voltage_level_range` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigureVoltageLevelRange.html')>`__
    -  `:py:func:`nidcpower.configure_current_limit_range` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigureCurrentLimitRange.html')>`__

    When NIDCPOWER\_VAL\_DC\_CURRENT is selected, the device generates the
    desired current level on the output as long as the output voltage is
    below the voltage limit. The following functions can be used to
    configure the channel when NIDCPOWER\_VAL\_DC\_CURRENT is selected:

    -  `:py:func:`nidcpower.configure_current_level` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigureCurrentLevel.html')>`__
    -  `:py:func:`nidcpower.configure_voltage_limit` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigureVoltageLimit.html')>`__
    -  `:py:func:`nidcpower.configure_current_level_range` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigureCurrentLevelRange.html')>`__
    -  `:py:func:`nidcpower.configure_voltage_limit_range` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigureVoltageLimitRange.html')>`__

    When NIDCPOWER\_VAL\_PULSE\_VOLTAGE is selected, the device generates
    pulses at the desired voltage levels on the output as long as the output
    current is below the current limit. The following VIs can be used to
    configure the channel when NIDCPOWER\_VAL\_PULSE\_VOLTAGE is selected:

    -  `:py:func:`nidcpower.configure_pulse_voltage_level` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigurePulseVoltageLevel.html')>`__
    -  `:py:func:`nidcpower.configure_pulse_bias_voltage_level` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigurePulseBiasVoltageLevel.html')>`__
    -  `:py:func:`nidcpower.configure_pulse_current_limit` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigurePulseCurrentLimit.html')>`__
    -  `:py:func:`nidcpower.configure_pulse_bias_current_limit` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigurePulseBiasCurrentLimit.html')>`__
    -  `:py:func:`nidcpower.configure_pulse_voltage_level_range` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigurePulseVoltageLevelRange.html')>`__
    -  `:py:func:`nidcpower.configure_pulse_current_limit_range` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigurePulseCurrentLimitRange.html')>`__

    When NIDCPOWER\_VAL\_PULSE\_CURRENT is selected, the device generates
    pulses at the desired current levels on the output as long as the output
    voltage is below the voltage limit. The following VIs can be used to
    configure the channel when NIDCPOWER\_VAL\_PULSE\_CURRENT is selected:

    -  `:py:func:`nidcpower.configure_pulse_current_level` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigurePulseCurrentLevel.html')>`__
    -  `:py:func:`nidcpower.configure_pulse_bias_current_level` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigurePulseBiasCurrentLevel.html')>`__
    -  `:py:func:`nidcpower.configure_pulse_voltage_limit` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigurePulseVoltageLimit.html')>`__
    -  `:py:func:`nidcpower.configure_pulse_bias_voltage_limit` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigurePulseBiasVoltageLimit.html')>`__
    -  `:py:func:`nidcpower.configure_pulse_current_level_range` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigurePulseCurrentLevelRange.html')>`__
    -  `:py:func:`nidcpower.configure_pulse_voltage_limit_range` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigurePulseVoltageLimitRange.html')>`__

    **Related Topics:**

    `Constant Voltage
    Mode <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/constant_voltage/>`__

    `Constant Current
    Mode <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/constant_current/>`__

    


    :param channel_name:


        Specifies the output channel(s) to which this configuration value
        applies. Specify multiple channels by using a channel list or a channel
        range. A channel list is a comma (,) separated sequence of channel names
        (for example, 0,2 specifies channels 0 and 2). A channel range is a
        lower bound channel followed by a hyphen (-) or colon (:) followed by an
        upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
        In the Running state, multiple output channel configurations are
        performed sequentially based on the order specified in this parameter.

        

    :type channel_name: int
    :param function:


        Configures the function to generate for the specified channel(s).
        **Defined Values**:

        +---------------------------------------+--------------------------------------------+
        | NIDCPOWER\_VAL\_DC\_VOLTAGE (1006)    | Sets the output function to DC voltage.    |
        +---------------------------------------+--------------------------------------------+
        | NIDCPOWER\_VAL\_DC\_CURRENT (1007)    | Sets the output function to DC current.    |
        +---------------------------------------+--------------------------------------------+
        | NIDCPOWER\_VAL\_PULSE\_VOLTAGE (1049) | Sets the output function to pulse voltage. |
        +---------------------------------------+--------------------------------------------+
        | NIDCPOWER\_VAL\_PULSE\_CURRENT (1050) | Sets the output function to pulse current. |
        +---------------------------------------+--------------------------------------------+

    :type function: int

.. function:: configure_output_range(range_type, range)

    Vistatus :py:func:`nidcpower.configure_output_range`(ViSession vi, ViConstString
    channelName, ViInt32 rangeType, ViReal64 range);

    Configures either the voltage level range or the current limit range. If
    **range type** is Voltage, the voltage level range is configured. If
    **range type** is Current, the current limit range is configured.

    This function does not configure any of the DC Current output function
    settings. Refer to the
    `:py:func:`nidcpower.configure_output_function` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_ConfigureOutputFunction.html')>`__
    function for more information.

    This is a deprecated function. You must use the following functions
    instead of the:py:func:`nidcpower.configure_output_range` function:

    -  `:py:func:`nidcpower.configure_voltage_level` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_ConfigureVoltageLevel.html')>`__
    -  `:py:func:`nidcpower.configure_voltage_limit` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_ConfigureVoltageLimit.html')>`__
    -  `:py:func:`nidcpower.configure_current_level` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_ConfigureCurrentLevel.html')>`__
    -  `:py:func:`nidcpower.configure_current_limit` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_ConfigureCurrentLimit.html')>`__

    


    :param channel_name:


        Specifies the output channel(s) to which this configuration value
        applies. Specify multiple channels by using a channel list or a channel
        range. A channel list is a comma (,) separated sequence of channel names
        (for example, 0,2 specifies channels 0 and 2). A channel range is a
        lower bound channel followed by a hyphen (-) or colon (:) followed by an
        upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
        In the Running state, multiple output channel configurations are
        performed sequentially based on the order specified in this parameter.

        

    :type channel_name: int
    :param range_type:


        Specifies the type of the range: voltage or current.
        **Defined Values**:

        +------------------------------------+------------------------------------------+
        | NIDCPOWER\_VAL\_RANGE\_CURRENT (0) | NI-DCPower configures the current range. |
        +------------------------------------+------------------------------------------+
        | NIDCPOWER\_VAL\_RANGE\_VOLTAGE (1) | NI-DCPower configures the voltage range. |
        +------------------------------------+------------------------------------------+

    :type range_type: int
    :param range:


        Specifies the range to calibrate with these settings. Only one channel
        at a time may be calibrated.

        

    :type range: float

.. function:: configure_output_resistance(resistance)

    Vistatus :py:func:`nidcpower.configure_output_resistance`(ViSession vi,
    ViConstString channelName, ViReal64 resistance);

    Configures the output resistance that the device attempts to generate
    for the specified channel or channels. The channel must be enabled for
    the specified output resistance to take effect.

    Refer to the
    `:py:func:`nidcpower.configure_output_enabled` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cvinidcpower_ConfigureOutputEnabled.html')>`__
    function for more information about enabling the output channel.

    For NI PXIe-4141/4143/4145 devices, output resistance is only supported
    if the output function of the channel is set to
    NIDCPOWER\_VAL\_DC\_VOLTAGE using the :py:func:`nidcpower.configure_output_function`
    function.

    For PXIe-4135, NI PXIe-4137, and NI PXIe-4139 devices, output resistance
    is supported if the output function of the channel is set to
    NIDCPOWER\_VAL\_DC\_CURRENT or NIDCPOWER\_VAL\_DC\_VOLTAGE using the
    :py:func:`nidcpower.configure_output_function` function.

    The device actively regulates the current and voltage to reach the
    specified output resistance, although in DC Voltage output mode, the
    voltage at the output experiences a "virtual drop" that is proportional
    to its current. In DC Current output mode, the output experiences a
    "virtual leakage current" that is proportional to the output voltage.

    

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

        

    :type channel_name: int
    :param resistance:


        Specifies the output resistance, in ohms, for the specified channel.
        Refer to the `NI PXIe-4141 Programmable Output
        resistance <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/4140_4141_progoutputresist/>`__,
        `NI PXIe-4143 Programmable Output
        resistance <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/4142_4143_progoutputresist/>`__,
        `NI PXIe-4145 Programmable Output
        resistance <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/4144_4145_progoutputresist/>`__,or
        `NI PXIe-4154 Programmable Output
        resistance <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/4154_prog_output_resist/>`__
        topic in the NI DC Power Supplies and SMUs Help for more information
        about configuring output resistance.

        

    :type resistance: float

.. function:: configure_power_line_frequency(powerline_frequency)

    Vistatus :py:func:`nidcpower.configure_power_line_frequency`(ViSession vi, ViReal64
    powerLineFrequency);

    Specifies the power line frequency for specified channel(s). NI-DCPower
    uses this value to select a timebase for setting the
    `:py:func:`nidcpower.configure_aperture_time` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_ConfigureApertureTime.html')>`__
    function in power line cycles (PLCs).

    Refer to the *Measurement Configuration and Timing* topic for your
    device in the *NI DC Power Supplies and SMUs Help* for more information
    about how to configure your measurements.

    **Related Topics:**

    `Measurement Noise
    Rejection <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/noiserejectmeasure/>`__

    

    .. note:: This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'supportedFunctions.html')>`__
        for more information about supported devices.


    :param powerline_frequency:


        Specifies the power line frequency in hertz for specified channel(s).
        NI-DCPower uses this value to select a timebase for the
        `:py:data:`nidcpower.APERTURE\_TIME` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_APERTURE_TIME.html')>`__
        attribute. Refer to the *Measurement Configuration and Timing* topic for
        your device for more information about how to configure your
        measurements.
        **Defined Values**:

        +----------------------------------+------------------+
        | NIDCPOWER\_VAL\_50\_HERTZ (50.0) | Specifies 50 Hz. |
        +----------------------------------+------------------+
        | NIDCPOWER\_VAL\_60\_HERTZ (60.0) | Specifies 60 Hz. |
        +----------------------------------+------------------+

        .. note:: Set this parameter to the frequency of the AC power line.

    :type powerline_frequency: float

.. function:: configure_pulse_bias_current_level(level)

    Vistatus :py:func:`nidcpower.configure_pulse_bias_current_level`(ViSession vi,
    ViConstString channelName, ViReal64 level);

    Configures the pulse bias current level that the device attempts to
    generate for the specified channel(s) during the off phase of a pulse.
    The channel must be enabled for the specified current level to take
    effect.

    Refer to the
    `:py:func:`nidcpower.configure_output_enabled` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigureOutputEnabled.html')>`__
    function for more information about enabling the output channel. The
    pulse current level setting is applicable only if the channel is set to
    the NIDCPOWER\_VAL\_PULSE\_CURRENT output function using the
    `:py:func:`nidcpower.configure_output_function` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigureOutputFunction.html')>`__
    function.

    The device actively regulates the current at the specified level unless
    doing so causes a voltage drop greater than the `pulse bias voltage
    limit <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT.html')>`__
    across the channels' output terminals.

    

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

        

    :type channel_name: int
    :param level:


        Specifies the pulse bias current level, in amps, on the specified
        channel(s).
        **Valid Values:**
        The valid values for this parameter are defined by the pulse current
        level range that is configured using the
        `:py:func:`nidcpower.configure_pulse_current_level_range` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigurePulseCurrentLevelRange.html')>`__
        function.

        

    :type level: float

.. function:: configure_pulse_bias_current_limit(limit)

    Vistatus :py:func:`nidcpower.configure_pulse_bias_current_limit`(ViSession vi,
    ViConstString channelName, ViReal64 limit);

    Configures the pulse bias current limit for the specified channel(s).
    The channel must be enabled for the specified current limit to take
    effect.

    Refer to the
    `:py:func:`nidcpower.configure_output_enabled` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigureOutputEnabled.html')>`__
    function for more information about enabling the output channel. The
    pulse bias current limit is the current that the output must not exceed
    when generating the desired `pulse bias voltage
    level <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_pULSE_bIAS_vOLTAGE_lEVEL.html')>`__.
    The pulse bias current limit setting is only applicable if the channel
    is set to the NIDCPOWER\_VAL\_PULSE\_VOLTAGE output function using the
    `:py:func:`nidcpower.configure_output_function` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigureOutputFunction.html')>`__
    function.

    

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

        

    :type channel_name: int
    :param limit:


        Specifies the pulse bias current limit, in amps, on the specified
        channel(s). The limit is specified as a positive value, but symmetric
        positive and negative limits are enforced simultaneously.
        **Valid Values:**
        The valid values for this parameter are defined by the pulse current
        limit range that is configured using the
        `:py:func:`nidcpower.configure_pulse_current_limit_range` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigurePulseCurrentLimitRange.html')>`__
        function.

        

    :type limit: float

.. function:: configure_pulse_bias_voltage_level(level)

    Vistatus :py:func:`nidcpower.configure_pulse_bias_voltage_level`(ViSession vi,
    ViConstString channelName, ViReal64 level);

    Configures the pulse bias voltage level that the device attempts to
    generate for the specified channel(s) during the off phase of a pulse.
    The channel must be enabled for the specified voltage level to take
    effect.

    Refer to the
    `:py:func:`nidcpower.configure_output_enabled` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigureOutputEnabled.html')>`__
    function for more information about enabling the output channel. The
    pulse bias voltage level setting is applicable only if the channel is
    set to the NIDCPOWER\_VAL\_PULSE\_VOLTAGE output function using the
    `:py:func:`nidcpower.configure_output_function` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigureOutputFunction.html')>`__
    function.

    The device actively regulates the voltage at the specified level unless
    doing so causes a current greater than the `pulse bias current
    limit <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT.html')>`__
    through the channels' output terminals.

    

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

        

    :type channel_name: int
    :param level:


        Specifies the pulse bias voltage level, in volts, for the output channel
        generation.
        **Valid Values**:
        The valid values for this parameter are defined by the pulse voltage
        level range that is selected using the
        `:py:func:`nidcpower.configure_pulse_voltage_level_range` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigurePulseVoltageLevelRange.html')>`__
        function.

        

    :type level: float

.. function:: configure_pulse_bias_voltage_limit(limit)

    Vistatus :py:func:`nidcpower.configure_pulse_bias_voltage_limit`(ViSession vi,
    ViConstString channelName, ViReal64 limit);

    Configures the pulse bias voltage limit for the specified channel(s).
    The channel must be enabled for the specified voltage limit to take
    effect.

    Refer to the
    `:py:func:`nidcpower.configure_output_enabled` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigureOutputEnabled.html')>`__
    function for more information about enabling the output channel. The
    pulse bias voltage limit is the voltage that the output must not exceed
    when generating the desired `pulse bias current
    level <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_PULSE_bIAS_cURRENT_lEVEL.html')>`__.
    The pulse bias voltage limit setting is only applicable if the channel
    is set to the NIDCPOWER\_VAL\_PULSE\_CURRENT output function using the
    `:py:func:`nidcpower.configure_output_function` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigureOutputFunction.html')>`__
    function.

    

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

        

    :type channel_name: int
    :param limit:


        Specifies the pulse bias voltage limit, in volts, on the specified
        channel(s). The limit is specified as a positive value, but symmetric
        positive and negative limits are enforced simultaneously.
        **Valid Values:**
        The valid values for this parameter are defined by the pulse voltage
        limit range that is configured using the
        `:py:func:`nidcpower.configure_pulse_voltage_limit_range` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigurePulseVoltageLimitRange.html')>`__
        function.

        

    :type limit: float

.. function:: configure_pulse_current_level(level)

    Vistatus :py:func:`nidcpower.configure_pulse_current_level`(ViSession vi,
    ViConstString channelName, ViReal64 level);

    Configures the pulse current level that the device attempts to generate
    for the specified channel(s) during the on phase of a pulse. The channel
    must be enabled for the specified current level to take effect.

    Refer to the
    `:py:func:`nidcpower.configure_output_enabled` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm','NIDCPowerCRef.chm','cviniDCPower_ConfigureOutputEnabled.html')>`__
    function for more information about enabling the output channel. The
    pulse current level setting is applicable only if the channel is set to
    the NIDCPOWER\_VAL\_PULSE\_CURRENT output function using the
    `:py:func:`nidcpower.configure_output_enabled` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigureOutputEnabled.html')>`__
    function.

    The device actively regulates the current at the specified level unless
    doing so causes a voltage drop greater than the `pulse voltage
    limit <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_PULSE_VOLTAGE_lIMIT.html')>`__
    across the channels' output terminals.

    

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

        

    :type channel_name: int
    :param level:


        Specifies the pulse current level, in amps, on the specified channel(s).
        **Valid Values:**
        The valid values for this parameter are defined by the pulse current
        level range that is configured using the
        `:py:func:`nidcpower.configure_pulse_current_level_range` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigurePulseCurrentLevelRange.html')>`__
        function.

        

    :type level: float

.. function:: configure_pulse_current_level_range(range)

    Vistatus :py:func:`nidcpower.configure_pulse_current_level_range`(ViSession vi,
    ViConstString channelName, ViReal64 range);

    Configures the pulse current level range for the specified channel(s).

    The configured range defines the valid values to which you can set the
    pulse current level and pulse bias current level using the
    `:py:func:`nidcpower.configure_pulse_current_level` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm','NIDCPowerCRef.chm','cviniDCPower_ConfigurePulseCurrentLevel.html')>`__
    and
    `:py:func:`nidcpower.configure_pulse_bias_current_level` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm','NIDCPowerCRef.chm','cviniDCPower_ConfigurePulseBiasCurrentLevel.html')>`__
    functions. The pulse current level range setting is applicable only if
    the channel is set to the NIDCPOWER\_VAL\_PULSE\_CURRENT output function
    using the
    `:py:func:`nidcpower.configure_output_function` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigureOutputFunction.html')>`__
    function.

    

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

        

    :type channel_name: int
    :param range:


        Specifies the pulse current level range, in amps, on the specified
        channel(s).
        For valid ranges, refer to the *ranges* topic for your device in the *NI
        DC Power Supplies and SMUs Help*.

        

    :type range: float

.. function:: configure_pulse_current_limit(limit)

    Vistatus :py:func:`nidcpower.configure_pulse_current_limit`(ViSession vi,
    ViConstString channelName, ViReal64 limit);

    Configures the pulse current limit for the specified channel(s). The
    channel must be enabled for the specified current limit to take effect.

    Refer to the
    `:py:func:`nidcpower.configure_output_enabled` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigureOutputEnabled.html')>`__
    function for more information about enabling the output channel. The
    pulse current limit is the current that the output must not exceed when
    generating the desired `pulse voltage
    level <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_PULSE_vOLTAGE_lEVEL.html')>`__.
    The pulse current limit setting is only applicable if the channel is set
    to the NIDCPOWER\_VAL\_PULSE\_VOLTAGE output function using the
    `:py:func:`nidcpower.configure_output_function` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigureOutputFunction.html')>`__
    function.

    

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

        

    :type channel_name: int
    :param limit:


        Specifies the pulse current limit, in amps, on the specified channel(s).
        The limit is specified as a positive value, but symmetric positive and
        negative limits are enforced simultaneously.
        **Valid Values:**
        The valid values for this parameter are defined by the pulse current
        limit range that is configured using the
        `:py:func:`nidcpower.configure_pulse_current_limit_range` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigurePulseCurrentLimitRange.html')>`__
        function.

        

    :type limit: float

.. function:: configure_pulse_current_limit_range(range)

    Vistatus :py:func:`nidcpower.configure_pulse_current_limit_range`(ViSession vi,
    ViConstString channelName, ViReal64 range);

    Configures the pulse current limit range for the specified channel(s).

    The configured range defines the valid values to which you can set the
    pulse current limit and pulse bias current limit using the
    `:py:func:`nidcpower.configure_pulse_current_limit` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm','NIDCPowerCRef.chm','cviniDCPower_ConfigurePulseCurrentLimit.html')>`__
    and
    `:py:func:`nidcpower.configure_pulse_bias_current_limit` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm','NIDCPowerCRef.chm','cviniDCPower_ConfigurePulseBiasCurrentLimit.html')>`__
    functions. The pulse current limit range setting is applicable only if
    the channel is set to the NIDCPOWER\_VAL\_PULSE\_VOLTAGE output function
    using the
    `:py:func:`nidcpower.configure_output_function` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigureOutputFunction.html')>`__
    function.

    

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

        

    :type channel_name: int
    :param range:


        Specifies the pulse current limit range, in amps, on the specified
        channel(s).
        For valid ranges, refer to the *ranges* topic for your device in the *NI
        DC Power Supplies and SMUs Help*.

        

    :type range: float

.. function:: configure_pulse_voltage_level(level)

    Vistatus :py:func:`nidcpower.configure_pulse_voltage_level`(ViSession vi,
    ViConstString channelName, ViReal64 level);

    Configures the pulse voltage level that the device attempts to generate
    for the specified channel(s) during the on phase of a pulse. The channel
    must be enabled for the specified voltage level to take effect.

    Refer to the
    `:py:func:`nidcpower.configure_output_enabled` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigureOutputEnabled.html')>`__
    function for more information about enabling the output channel. The
    pulse voltage level setting is applicable only if the channel is set to
    the NIDCPOWER\_VAL\_PULSE\_VOLTAGE output function using the
    `:py:func:`nidcpower.configure_output_function` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigureOutputFunction.html')>`__
    function.

    The device actively regulates the voltage at the specified level unless
    doing so causes a current greater than the `pulse current
    limit <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_PULSE_cURRENT_lIMIT.html')>`__
    through the channels' output terminals.

    

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

        

    :type channel_name: int
    :param level:


        Specifies the pulse voltage level, in volts, for the output channel
        generation.
        **Valid Values**:
        The valid values for this parameter are defined by the voltage level
        range that is selected using the
        `:py:func:`nidcpower.configure_pulse_voltage_level_range` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigurePulseVoltageLevelRange.html')>`__
        function.

        

    :type level: float

.. function:: configure_pulse_voltage_level_range(range)

    Vistatus :py:func:`nidcpower.configure_pulse_voltage_level_range`(ViSession vi,
    ViConstString channelName, ViReal64 range);

    Configures the pulse voltage level range for the specified channel(s).

    The configured range defines the valid values to which you can set the
    pulse voltage level and pulse bias voltage level using the
    `:py:func:`nidcpower.configure_pulse_voltage_level` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm','NIDCPowerCRef.chm','cviniDCPower_ConfigurePulseVoltageLevel.html')>`__
    and
    `:py:func:`nidcpower.configure_pulse_bias_voltage_level` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm','NIDCPowerCRef.chm','cviniDCPower_ConfigurePulseBiasVoltageLevel.html')>`__
    functions. The pulse voltage level range setting is applicable only if
    the channel is set to the NIDCPOWER\_VAL\_PULSE\_VOLTAGE output function
    using the
    `:py:func:`nidcpower.configure_output_function` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigureOutputFunction.html')>`__
    function.

    

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

        

    :type channel_name: int
    :param range:


        Specifies the pulse voltage level range, in volts, on the specified
        channel(s).
        For valid ranges, refer to the *ranges* topic for your device in the *NI
        DC Power Supplies and SMUs Help*.

        

    :type range: float

.. function:: configure_pulse_voltage_limit(limit)

    Vistatus :py:func:`nidcpower.configure_pulse_voltage_limit`(ViSession vi,
    ViConstString channelName, ViReal64 limit);

    Configures the pulse voltage limit for the specified channel(s). The
    channel must be enabled for the specified voltage limit to take effect.

    Refer to the
    `:py:func:`nidcpower.configure_output_enabled` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigureOutputEnabled.html')>`__
    function for more information about enabling the output channel. The
    pulse voltage limit is the voltage that the output must not exceed when
    generating the desired `pulse current
    level <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_PULSE_cURRENT_lEVEL.html')>`__.
    The pulse voltage limit setting is only applicable if the channel is set
    to the NIDCPOWER\_VAL\_PULSE\_CURRENT output function using the
    `:py:func:`nidcpower.configure_output_function` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigureOutputFunction.html')>`__
    function.

    

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

        

    :type channel_name: int
    :param limit:


        Specifies the pulse voltage limit, in volts, on the specified output
        channel(s). The limit is specified as a positive value, but symmetric
        positive and negative limits are enforced simultaneously.
        **Valid Values:**
        The valid values for this parameter are defined by the pulse voltage
        limit range that is configured using the
        `:py:func:`nidcpower.configure_pulse_voltage_limit_range` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigurePulseVoltageLimitRange.html')>`__
        function.

        

    :type limit: float

.. function:: configure_pulse_voltage_limit_range(range)

    Vistatus :py:func:`nidcpower.configure_pulse_voltage_limit_range`(ViSession vi,
    ViConstString channelName, ViReal64 range);

    Configures the pulse voltage limit range for the specified channel(s).

    The configured range defines the valid values to which you can set the
    pulse voltage limit and pulse bias voltage limit using the
    `:py:func:`nidcpower.configure_pulse_voltage_limit` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm','NIDCPowerCRef.chm','cviniDCPower_ConfigurePulseVoltageLimit.html')>`__
    and
    `:py:func:`nidcpower.configure_pulse_bias_voltage_limit` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm','NIDCPowerCRef.chm','cviniDCPower_ConfigurePulseBiasVoltageLimit.html')>`__
    functions. The pulse voltage limit range setting is applicable only if
    the channel is set to the NIDCPOWER\_VAL\_PULSE\_CURRENT output function
    using the
    `:py:func:`nidcpower.configure_output_function` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigureOutputFunction.html')>`__
    function.

    .

    

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

        

    :type channel_name: int
    :param range:


        Specifies the pulse voltage limit range, in volts, on the specified
        channel(s).
        For valid ranges, refer to the *ranges* topic for your device in the *NI
        DC Power Supplies and SMUs Help*.

        

    :type range: float

.. function:: configure_sense(sense)

    Vistatus :py:func:`nidcpower.configure_sense`(ViSession vi, ViConstString
    channelName, ViInt32 sense);

    Specifies whether to use
    `local <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm','local_and_remote_sense.html')>`__
    or
    `remote <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm','local_and_remote_sense.html')>`__
    sensing of the output voltage on the specified channel(s). Refer to the
    *Devices* topic specific to your device in the *NI DC Power Supplies and
    SMUs* Help for more information about sensing voltage on supported
    channels.

    **Related Topics:**

    `Local and Remote
    sense <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/4112_localandremotesense/>`__

    


    :param channel_name:


        Specifies the output channel(s) to which this configuration value
        applies. Specify multiple channels by using a channel list or a channel
        range. A channel list is a comma (,) separated sequence of channel names
        (for example, 0,2 specifies channels 0 and 2). A channel range is a
        lower bound channel followed by a hyphen (-) or colon (:) followed by an
        upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
        In the Running state, multiple output channel configurations are
        performed sequentially based on the order specified in this parameter.

        

    :type channel_name: int
    :param sense:


        Specifies local or remote sensing on the specified channel(s).
        **Defined Values:**

        +-------------------------------+----------------+
        | NIDCPOWER\_VAL\_LOCAL (1008)  | Local sensing  |
        +-------------------------------+----------------+
        | NIDCPOWER\_VAL\_REMOTE (1009) | Remote sensing |
        +-------------------------------+----------------+

    :type sense: int

.. function:: configure_software_edge_measure_trigger()

    Vistatus :py:func:`nidcpower.configure_software_edge_measure_trigger`(ViSession vi);

    Configures the Measure trigger for software triggering. Use the
    `:py:func:`nidcpower.send_software_edge_trigger` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_SendSoftwareEdgeTrigger.html')>`__
    function to assert the trigger condition.

    

    .. note:: This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'supportedFunctions.html')>`__
        for more information about supported devices.


.. function:: configure_software_edge_pulse_trigger()

    Vistatus :py:func:`nidcpower.configure_software_edge_pulse_trigger`(ViSession vi);

    Configures the Pulse trigger for software triggering. Use the
    `:py:func:`nidcpower.send_software_edge_trigger` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_SendSoftwareEdgeTrigger.html')>`__
    function to assert the trigger condition.

    

    .. note:: This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'supportedFunctions.html')>`__
        for more information about supported devices.


.. function:: configure_software_edge_sequence_advance_trigger()

    Vistatus
    :py:func:`nidcpower.configure_software_edge_sequence_advance_trigger`(ViSession vi);

    Configures the Sequence Advance trigger for software triggering. Use the
    `:py:func:`nidcpower.send_software_edge_trigger` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_SendSoftwareEdgeTrigger.html')>`__
    function to assert the trigger condition.

    

    .. note:: This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'supportedFunctions.html')>`__
        for more information about supported devices.


.. function:: configure_software_edge_source_trigger()

    Vistatus :py:func:`nidcpower.configure_software_edge_source_trigger`(ViSession vi);

    Configures the Source trigger for software triggering. Use the
    `:py:func:`nidcpower.send_software_edge_trigger` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_SendSoftwareEdgeTrigger.html')>`__
    function to assert the trigger condition.

    

    .. note:: This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'supportedFunctions.html')>`__
        for more information about supported devices.


.. function:: configure_software_edge_start_trigger()

    Vistatus :py:func:`nidcpower.configure_software_edge_start_trigger`(ViSession vi);

    Configures the Start trigger for software triggering. Use the
    `:py:func:`nidcpower.send_software_edge_trigger` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_SendSoftwareEdgeTrigger.html')>`__
    function to assert the trigger condition.

    

    .. note:: This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'supportedFunctions.html')>`__
        for more information about supported devices.


.. function:: configure_source_mode(source_mode)

    Vistatus :py:func:`nidcpower.configure_source_mode`(ViSession vi, ViInt32
    sourceMode);

    Configures the
    `:py:data:`nidcpower.SOURCE\_MODE` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_SOURCE_MODE.html')>`__
    attribute. Specifies whether to run a single output point or a sequence.
    Refer to the `Single Point Source
    Mode <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/singlept/>`__
    and `Sequence Source
    Mode <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/sequencing/>`__
    topics in the *NI DC Power Supplies and SMUs Help* for more information
    about using this function.

    


    :param source_mode:


        Specifies the source mode for the NI-DCPower session.
        **Defined Values**:

        +--------------------------------------+-------------------------------------------------------------------+
        | NIDCPOWER\_VAL\_SINGLE\_POINT (1020) | Applies a single source configuration.                            |
        +--------------------------------------+-------------------------------------------------------------------+
        | NIDCPOWER\_VAL\_SEQUENCE (1021)      | Applies a list of voltage or current configurations sequentially. |
        +--------------------------------------+-------------------------------------------------------------------+

    :type source_mode: int

.. function:: configure_voltage_level(level)

    Vistatus :py:func:`nidcpower.configure_voltage_level`(ViSession vi, ViConstString
    channelName, ViReal64 level);

    Configures the voltage level the device attempts to generate for the
    specified channel(s). The channel must be enabled for the specified
    voltage level to take effect. Refer to the
    `:py:func:`nidcpower.configure_output_enabled` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigureOutputEnabled.html')>`__
    function for more information about enabling the output channel.

    The voltage level setting is applicable only if the output function of
    the channel is set to NIDCPOWER\_VAL\_DC\_VOLTAGE. Use
    `:py:func:`nidcpower.configure_output_function` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cvinidcpower_ConfigureOutputFunction.html')>`__
    to set the output function.

    The device actively regulates the voltage at the specified level unless
    doing so causes a current output greater than the `current
    limit <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_CURRENT_LIMIT.html')>`__
    across the channels' output terminals.

    **Related Topics:**

    `Constant Voltage
    Mode <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/constant_voltage/>`__

    


    :param channel_name:


        Specifies the output channel(s) to which this configuration value
        applies. Specify multiple channels by using a channel list or a channel
        range. A channel list is a comma (,) separated sequence of channel names
        (for example, 0,2 specifies channels 0 and 2). A channel range is a
        lower bound channel followed by a hyphen (-) or colon (:) followed by an
        upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
        In the Running state, multiple output channel configurations are
        performed sequentially based on the order specified in this parameter.

        

    :type channel_name: int
    :param level:


        Specifies the voltage level, in volts, for the output channel
        generation.
        **Valid Values**:
        The valid values for this parameter are defined by the voltage level
        range that is selected using the
        `:py:func:`nidcpower.configure_voltage_level_range` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigureVoltageLevelRange.html')>`__
        function.

        

    :type level: float

.. function:: configure_voltage_level_range(range)

    Vistatus :py:func:`nidcpower.configure_voltage_level_range`(ViSession vi,
    ViConstString channelName, ViReal64 range);

    Configures the voltage level range for the specified channel(s). The
    configured range defines the valid values the voltage level can be set
    to using the
    `:py:func:`nidcpower.configure_voltage_level` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_ConfigureVoltageLevel.html')>`__
    function. The voltage level range setting is applicable only if the
    output function of the channel is set to NIDCPOWER\_VAL\_DC\_VOLTAGE.
    Use
    `:py:func:`nidcpower.configure_output_function` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cvinidcpower_ConfigureOutputFunction.html')>`__
    to set the output function.

    Use the
    `:py:data:`nidcpower.VOLTAGE\_LEVEL\_AUTORANGE` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','NIDCPOWER_ATTR_VOLTAGE_LEVEL_AUTORANGE.html')>`__
    attribute to enable automatic selection of the voltage level range.

    **Related Topics:**

    `ranges <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/ranges/>`__

    


    :param channel_name:


        Specifies the output channel(s) to which this configuration value
        applies. Specify multiple channels by using a channel list or a channel
        range. A channel list is a comma (,) separated sequence of channel names
        (for example, 0,2 specifies channels 0 and 2). A channel range is a
        lower bound channel followed by a hyphen (-) or colon (:) followed by an
        upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
        In the Running state, multiple output channel configurations are
        performed sequentially based on the order specified in this parameter.

        

    :type channel_name: int
    :param range:


        Specifies the voltage level range, in volts, on the specified
        channel(s).
        For valid ranges, refer to the *ranges* topic for your device in the *NI
        DC Power Supplies and SMUs Help*.

        

    :type range: float

.. function:: configure_voltage_limit(limit)

    Vistatus :py:func:`nidcpower.configure_voltage_limit`(ViSession vi, ViConstString
    channelName, ViReal64 limit);

    Configures the voltage limit for the specified channel(s). The channel
    must be enabled for the specified voltage limit to take effect. Refer to
    the
    `:py:func:`nidcpower.configure_output_enabled` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_ConfigureOutputEnabled.html')>`__
    function for more information about enabling the output channel.

    The voltage limit is the voltage that the output should not exceed when
    generating the desired `current
    level <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_ConfigureCurrentLevel.html')>`__.
    The voltage limit setting is applicable only if the output function of
    the channel is set to NIDCPOWER\_VAL\_DC\_CURRENT. Use
    `:py:func:`nidcpower.configure_output_function` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cvinidcpower_ConfigureOutputFunction.html')>`__
    to set the output function.

    **Related Topics:**

    `Compliance <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/compliance/>`__

    


    :param channel_name:


        Specifies the output channel(s) to which this configuration value
        applies. Specify multiple channels by using a channel list or a channel
        range. A channel list is a comma (,) separated sequence of channel names
        (for example, 0,2 specifies channels 0 and 2). A channel range is a
        lower bound channel followed by a hyphen (-) or colon (:) followed by an
        upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
        In the Running state, multiple output channel configurations are
        performed sequentially based on the order specified in this parameter.

        

    :type channel_name: int
    :param limit:


        Specifies the voltage limit, in volts, on the specified output
        channel(s). The limit is specified as a positive value, but symmetric
        positive and negative limits are enforced simultaneously.
        **Valid Values:**
        The valid values for this parameter are defined by the voltage limit
        range that is configured using the
        `:py:func:`nidcpower.configure_voltage_limit_range` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','cviniDCPower_ConfigureVoltageLimitRange.html')>`__
        function.

        

    :type limit: float

.. function:: configure_voltage_limit_range(range)

    Vistatus :py:func:`nidcpower.configure_voltage_limit_range`(ViSession vi,
    ViConstString channelName, ViReal64 range);

    Configures the voltage limit range for the specified channel(s). The
    configured range defines the valid values the voltage limit can be set
    to using the
    `:py:func:`nidcpower.configure_voltage_limit` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_ConfigureVoltageLimit.html')>`__
    function. The voltage limit range setting is applicable only if the
    output function of the channel is set to NIDCPOWER\_VAL\_DC\_CURRENT.
    Use
    `:py:func:`nidcpower.configure_output_function` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cvinidcpower_ConfigureOutputFunction.html')>`__
    to set the output function.

    Use the
    `:py:data:`nidcpower.VOLTAGE\_LIMIT\_AUTORANGE` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','NIDCPOWER_ATTR_VOLTAGE_LIMIT_AUTORANGE.html')>`__
    attribute to enable automatic selection of the voltage limit range.

    **Related Topics:**

    `ranges <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/ranges/>`__

    


    :param channel_name:


        Specifies the output channel(s) to which this configuration value
        applies. Specify multiple channels by using a channel list or a channel
        range. A channel list is a comma (,) separated sequence of channel names
        (for example, 0,2 specifies channels 0 and 2). A channel range is a
        lower bound channel followed by a hyphen (-) or colon (:) followed by an
        upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
        In the Running state, multiple output channel configurations are
        performed sequentially based on the order specified in this parameter.

        

    :type channel_name: int
    :param range:


        Specifies the voltage limit range, in volts, on the specified
        channel(s).
        For valid ranges, refer to the *ranges* topic for your device in the *NI
        DC Power Supplies and SMUs Help*.

        

    :type range: float

.. function:: connect_internal_reference(internal_reference)

    Vistatus :py:func:`nidcpower.connect_internal_reference`(ViSession vi, ViSession
    vi, ViInt32 internal_reference;

    Routes the internal reference to the calibration pin in preparation for
    adjustment. Refer to the calibration procedure for the device you are
    calibrating for detailed instructions on the appropriate use of this
    function. This function can only be called from an external calibration
    session.

    

    .. note:: This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'supportedFunctions.html')>`__
        for more information about supported devices.


    :param internal_reference:


        Specifies the internal reference to be connected to the calibration pin.
        **Defined Values**:

        +-----------------------------------------------------+---------------------------------------------------------+
        | NIDCPOWER\_VAL\_INTERNAL\_REFERENCE\_5V (1054)      | Calibration pin connected to 5 V internal reference.    |
        +-----------------------------------------------------+---------------------------------------------------------+
        | NIDCPOWER\_VAL\_INTERNAL\_REFERENCE\_100KOHM (1055) | Calibration pin connected to 100 kΩ internal reference. |
        +-----------------------------------------------------+---------------------------------------------------------+
        | NIDCPOWER\_VAL\_INTERNAL\_REFERENCE\_GROUND (1056)  | Calibration pin connected to ground reference.          |
        +-----------------------------------------------------+---------------------------------------------------------+
        | NIDCPOWER\_VAL\_INTERNAL\_REFERENCE\_NONE (1057)    | Calibration pin disconnected from internal reference.   |
        +-----------------------------------------------------+---------------------------------------------------------+

    :type internal_reference: int

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

        

    :type sequence_name: str
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

    :type attribute_ids: int
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

        

    :type sequence_name: str

.. function:: disable()

    Vistatus :py:func:`nidcpower.disable`(ViSession vi);

    This function performs the same actions as the
    `:py:func:`nidcpower.reset` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_reset.html')>`__
    function, except that this function also immediately sets the
    `:py:data:`nidcpower.OUTPUT\_ENABLED` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_OUTPUT_ENABLED.html')>`__
    attribute to VI\_FALSE.

    This function opens the output relay on devices that have an output
    relay.

    


.. function:: disable_pulse_trigger()

    Vistatus :py:func:`nidcpower.disable_pulse_trigger`(ViSession vi);

    Disables the Pulse trigger. The device does not wait for a pulse trigger
    before performing a pulse operation. Refer to `Pulse
    Mode <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/pulsemode/>`__
    and `Sequence Source
    Mode <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/sequencing/>`__
    for more information about the Pulse trigger.

    This function is necessary only if you configured a Pulse trigger in the
    past and now want to disable it.

    

    .. note:: This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'supportedFunctions.html')>`__
        for more information about supported devices.


.. function:: disable_sequence_advance_trigger()

    Vistatus :py:func:`nidcpower.disable_sequence_advance_trigger`(ViSession vi);

    Disables the Sequence Advance trigger. The device does not wait for a
    Sequence Advance trigger before advancing to the next iteration of the
    sequence. Refer to the `Sequence Source
    Mode <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/sequencing/>`__
    topic for more information about the Sequence Advance trigger.

    

    .. note:: This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'supportedFunctions.html')>`__
        for more information about supported devices.


.. function:: disable_source_trigger()

    Vistatus :py:func:`nidcpower.disable_source_trigger`(ViSession vi);

    Disables the Source trigger. The device does not wait for a source
    trigger before performing a source operation. Refer to the `Single Point
    Source
    Mode <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/singlept/>`__
    and `Sequence Source
    Mode <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/sequencing/>`__
    topics for more information about the Source trigger.

    

    .. note:: This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'supportedFunctions.html')>`__
        for more information about supported devices.


.. function:: disable_start_trigger()

    Vistatus :py:func:`nidcpower.disable_start_trigger`(ViSession vi);

    Disables the Start trigger. The device does not wait for a Start trigger
    when starting generation or acquisition.

    

    .. note:: This function is not supported on all devices. Refer to `Supported
        Functions by
        Device <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'supportedFunctions.html')>`__
        for more information about supported devices.


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

        

    :type signal_identifier: int
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

    :type output_terminal: int

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
    `:py:func:`nidcpower.initiate` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_Initiate.html')>`__
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

        

    :type channel_name: int
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

        voltage_measurements (float): 


            Returns an array of voltage measurements. Ensure that sufficient space
            has been allocated for the returned array.

            

        current_measurements (float): 


            Returns an array of current measurements. Ensure that sufficient space
            has been allocated for the returned array.

            

        in_compliance (bool): 


            Returns an array of Boolean values indicating whether the output was in
            compliance at the time the measurement was taken. Ensure that sufficient
            space has been allocated for the returned array.

            

        actual_count (int): 


            Indicates the number of measured values actually retrieved from the
            device.

            


.. function:: get_attribute_vi_boolean(attribute_id)

    Vistatus :py:func:`nidcpower.get_attribute_vi_boolean`(ViSession vi, ViConstString
    channelName, ViAttr attribute, ViBoolean \*value);

    | Queries the value of a ViBoolean attribute.
    | You can use this function to get the values of device-specific
      attributes and inherent IVI attributes.

    


    :param channel_name:


        Specifies the output channel(s) to which this configuration value
        applies. Specify multiple channels by using a channel list or a channel
        range. A channel list is a comma (,) separated sequence of channel names
        (for example, 0,2 specifies channels 0 and 2). A channel range is a
        lower bound channel followed by a hyphen (-) or colon (:) followed by an
        upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
        In the Running state, multiple output channel configurations are
        performed sequentially based on the order specified in this parameter.

        

    :type channel_name: int
    :param attribute_id:


        Specifies the ID of an attribute. From the function panel window, you
        can use this control as follows.

        -  In the function panel window, click on the control or press **Enter**
           or the spacebar to display a dialog box containing hierarchical list
           of the available attributes. Help text is shown for each attribute.
           Select an attribute by double-clicking on it or by selecting it and
           then pressing **Enter**.
        -  A ring control at the top of the dialog box allows you to see all IVI
           attributes or only the attributes of type ViBoolean. If you choose to
           see all IVI attributes, the data types appear to the right of the
           attribute names in the list box. Attributes with data types other
           than ViBoolean are dim. If you select an attribute data type that is
           dim, LabWindows/CVI transfers you to the function panel for the
           corresponding function that is consistent with the data type.
        -  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
           change this ring control to a manual input box. If the attribute in
           this ring control has named constants as valid values, you can view
           the constants by moving to the value control and pressing **Enter**.

        

    :type attribute_id: int

    :rtype: bool
    :return:


            Returns the current value of the attribute. Passes the address of a
            ViBoolean variable.
            If the attribute currently showing in the attribute ring control has
            constants as valid values, you can view a list of the constants by
            pressing **Enter** on this control. Select a value by double-clicking on
            it or by selecting it and then pressing **Enter**.

            


.. function:: get_attribute_vi_int32(attribute_id)

    Vistatus :py:func:`nidcpower.get_attribute_vi_int32`(ViSession vi, ViConstString
    channelName, ViAttr attribute, ViInt32 \*value);

    | Queries the value of a ViInt32 attribute.
    | You can use this function to get the values of device-specific
      attributes and inherent IVI attributes.

    


    :param channel_name:


        Specifies the output channel(s) to which this configuration value
        applies. Specify multiple channels by using a channel list or a channel
        range. A channel list is a comma (,) separated sequence of channel names
        (for example, 0,2 specifies channels 0 and 2). A channel range is a
        lower bound channel followed by a hyphen (-) or colon (:) followed by an
        upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
        In the Running state, multiple output channel configurations are
        performed sequentially based on the order specified in this parameter.

        

    :type channel_name: int
    :param attribute_id:


        Specifies the ID of an attribute. From the function panel window, you
        can use this control as follows.

        -  In the function panel window, click on the control or press **Enter**
           or the spacebar to display a dialog box containing hierarchical list
           of the available attributes. Help text is shown for each attribute.
           Select an attribute by double-clicking on it or by selecting it and
           then pressing **Enter**.
        -  A ring control at the top of the dialog box allows you to see all IVI
           attributes or only the attributes of type ViInt32. If you choose to
           see all IVI attributes, the data types appear to the right of the
           attribute names in the list box. Attributes with data types other
           than ViInt32 are dim. If you select an attribute data type that is
           dim, LabWindows/CVI transfers you to the function panel for the
           corresponding function that is consistent with the data type.
        -  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
           change this ring control to a manual input box. If the attribute in
           this ring control has named constants as valid values, you can view
           the constants by moving to the value control and pressing **Enter**.

        

    :type attribute_id: int

    :rtype: int
    :return:


            Returns the current value of the attribute. Passes the address of a
            ViInt32 variable.
            If the attribute currently showing in the attribute ring control has
            constants as valid values, you can view a list of the constants by
            pressing **Enter** on this control. Select a value by double-clicking on
            it or by selecting it and then pressing **Enter**.

            


.. function:: get_attribute_vi_int64(attribute_id)

    Vistatus :py:func:`nidcpower.get_attribute_vi_int64`(ViSession vi, ViConstString
    channelName, ViAttr attribute, ViInt64 \*value);

    | Queries the value of a ViInt64 attribute.
    | You can use this function to get the values of device-specific
      attributes and inherent IVI attributes.

    


    :param channel_name:


        Specifies the output channel(s) to which this configuration value
        applies. Specify multiple channels by using a channel list or a channel
        range. A channel list is a comma (,) separated sequence of channel names
        (for example, 0,2 specifies channels 0 and 2). A channel range is a
        lower bound channel followed by a hyphen (-) or colon (:) followed by an
        upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
        In the Running state, multiple output channel configurations are
        performed sequentially based on the order specified in this parameter.

        

    :type channel_name: int
    :param attribute_id:


        Specifies the ID of an attribute. From the function panel window, you
        can use this control as follows.

        -  In the function panel window, click on the control or press **Enter**
           or the spacebar to display a dialog box containing hierarchical list
           of the available attributes. Help text is shown for each attribute.
           Select an attribute by double-clicking on it or by selecting it and
           then pressing **Enter**.
        -  A ring control at the top of the dialog box allows you to see all IVI
           attributes or only the attributes of type ViReal64. If you choose to
           see all IVI attributes, the data types appear to the right of the
           attribute names in the list box. Attributes with data types other
           than ViReal64 are dim. If you select an attribute data type that is
           dim, LabWindows/CVI transfers you to the function panel for the
           corresponding function that is consistent with the data type.
        -  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
           change this ring control to a manual input box. If the attribute in
           this ring control has named constants as valid values, you can view
           the constants by moving to the value control and pressing **Enter**.

        

    :type attribute_id: int

    :rtype: int
    :return:


            Returns the current value of the attribute. Passes the address of a
            ViReal64 variable.
            If the attribute currently showing in the attribute ring control has
            constants as valid values, you can view a list of the constants by
            pressing **Enter** on this control. Select a value by double-clicking on
            it or by selecting it and then pressing **Enter**.

            


.. function:: get_attribute_vi_real64(attribute_id)

    Vistatus :py:func:`nidcpower.get_attribute_vi_real64`(ViSession vi, ViConstString
    channelName, ViAttr attribute, ViReal64 \*value);

    | Queries the value of a ViReal64 attribute.
    | You can use this function to get the values of device-specific
      attributes and inherent IVI attributes.

    


    :param channel_name:


        Specifies the output channel(s) to which this configuration value
        applies. Specify multiple channels by using a channel list or a channel
        range. A channel list is a comma (,) separated sequence of channel names
        (for example, 0,2 specifies channels 0 and 2). A channel range is a
        lower bound channel followed by a hyphen (-) or colon (:) followed by an
        upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
        In the Running state, multiple output channel configurations are
        performed sequentially based on the order specified in this parameter.

        

    :type channel_name: int
    :param attribute_id:


        Specifies the ID of an attribute. From the function panel window, you
        can use this control as follows.

        -  In the function panel window, click on the control or press **Enter**
           or the spacebar to display a dialog box containing hierarchical list
           of the available attributes. Help text is shown for each attribute.
           Select an attribute by double-clicking on it or by selecting it and
           then pressing **Enter**.
        -  A ring control at the top of the dialog box allows you to see all IVI
           attributes or only the attributes of type ViReal64. If you choose to
           see all IVI attributes, the data types appear to the right of the
           attribute names in the list box. Attributes with data types other
           than ViReal64 are dim. If you select an attribute data type that is
           dim, LabWindows/CVI transfers you to the function panel for the
           corresponding function that is consistent with the data type.
        -  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
           change this ring control to a manual input box. If the attribute in
           this ring control has named constants as valid values, you can view
           the constants by moving to the value control and pressing **Enter**.

        

    :type attribute_id: int

    :rtype: float
    :return:


            Returns the current value of the attribute. Passes the address of a
            ViReal64 variable.
            If the attribute currently showing in the attribute ring control has
            constants as valid values, you can view a list of the constants by
            pressing **Enter** on this control. Select a value by double-clicking on
            it or by selecting it and then pressing **Enter**.

            


.. function:: get_attribute_vi_session(attribute_id)

    Vistatus :py:func:`nidcpower.get_attribute_vi_session`(ViSession vi, ViConstString
    channelName, ViAttr attribute, ViSession \*value);

    | Queries the value of a ViSession attribute.
    | You can use this function to get the values of device-specific
      attributes and inherent IVI attributes.

    


    :param channel_name:


        Specifies the output channel(s) to which this configuration value
        applies. Specify multiple channels by using a channel list or a channel
        range. A channel list is a comma (,) separated sequence of channel names
        (for example, 0,2 specifies channels 0 and 2). A channel range is a
        lower bound channel followed by a hyphen (-) or colon (:) followed by an
        upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
        In the Running state, multiple output channel configurations are
        performed sequentially based on the order specified in this parameter.

        

    :type channel_name: int
    :param attribute_id:


        Specifies the ID of an attribute. From the function panel window, you
        can use this control as follows.

        -  In the function panel window, click on the control or press **Enter**
           or the spacebar to display a dialog box containing hierarchical list
           of the available attributes. Help text is shown for each attribute.
           Select an attribute by double-clicking on it or by selecting it and
           then pressing **Enter**.
        -  A ring control at the top of the dialog box allows you to see all IVI
           attributes or only the attributes of type ViSession. If you choose to
           see all IVI attributes, the data types appear to the right of the
           attribute names in the list box. Attributes with data types other
           than ViSession are dim. If you select an attribute data type that is
           dim, LabWindows/CVI transfers you to the function panel for the
           corresponding function that is consistent with the data type.
        -  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
           change this ring control to a manual input box. If the attribute in
           this ring control has named constants as valid values, you can view
           the constants by moving to the value control and pressing **Enter**.

        

    :type attribute_id: int

    :rtype: int
    :return:


            Returns the current value of the attribute. Passes the address of a
            ViSession variable.
            If the attribute currently showing in the attribute ring control has
            constants as valid values, you can view a list of the constants by
            pressing **Enter** on this control. Select a value by double-clicking on
            it or by selecting it and then pressing **Enter**.

            


.. function:: get_attribute_vi_string(attribute_id, buffer_size)

    ViStatus :py:func:`nidcpower.get_attribute_vi_string`(ViSession vi, ViConstString
    channelName, ViAttr attribute, ViInt32 bufSize, ViChar value[]);

    | Queries the value of a ViString attribute.
    | You can use this function to get the values of device-specific
      attributes and inherent IVI attributes.

    


    :param channel_name:


        Specifies the output channel(s) to which this configuration value
        applies. Specify multiple channels by using a channel list or a channel
        range. A channel list is a comma (,) separated sequence of channel names
        (for example, 0,2 specifies channels 0 and 2). A channel range is a
        lower bound channel followed by a hyphen (-) or colon (:) followed by an
        upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
        In the Running state, multiple output channel configurations are
        performed sequentially based on the order specified in this parameter.

        

    :type channel_name: int
    :param attribute_id:


        Specifies the ID of an attribute. From the function panel window, you
        can use this control as follows.

        -  In the function panel window, click on the control or press or the
           spacebar to display a dialog box containing hierarchical list of the
           available attributes. Help text is shown for each attribute. Select
           an attribute by double-clicking on it or by selecting it and then
           pressing .
        -  A ring control at the top of the dialog box allows you to see all IVI
           attributes or only the attributes of type ViString. If you choose to
           see all IVI attributes, the data types appear to the right of the
           attribute names in the list box. Attributes with data types other
           than ViString are dimmed. If you select an attribute data type that
           is dimmed, LabWindows/CVI transfers you to the function panel for the
           corresponding function that is consistent with the data type.
        -  If you want to enter a variable name, press to change this ring
           control to a manual input control. If the attribute in this ring
           control has named constants as valid values, you can view the
           constants by moving to the value control and pressing .

        

    :type attribute_id: int
    :param buffer_size:


        Passes the number of bytes in the buffer and specifies the number of
        bytes in the ViChar array you specify for **value**. If the current
        value of **value**, including the terminating NUL byte, is larger than
        the size you indicate in this parameter, the function copies (buffer
        size - 1) bytes into the buffer, places an ASCII NUL byte at the end of
        the buffer, and returns the buffer size you must pass to get the entire
        value. For example, if the value is 123456 and the buffer size is 4, the
        function places 123 into the buffer and returns 7.
        To obtain the required buffer size, you can pass 0 for this attribute
        and VI\_NULL for **value**. If you want the function to fill in the
        buffer regardless of the number of bytes in the value, pass a negative
        number for this attribute.

        

    :type buffer_size: int

    :rtype: int
    :return:


            The buffer in which the function returns the current value of the
            attribute. The buffer must be of type ViChar and have at least as many
            bytes as indicated in **bufSize**.
            If the current value of the attribute, including the terminating NUL
            byte, contains more bytes that you indicate in this attribute, the
            function copies (buffer size -1) bytes into the buffer, places an ASCII
            NUL byte at the end of the buffer, and returns the buffer size you must
            pass to get the entire value. For example, if the value is 123456 and
            the buffer size is 4, the function places 123 into the buffer and
            returns 7.
            If you specify 0 for **bufSize**, you can pass VI\_NULL for this
            attribute.
            If the attribute currently showing in the attribute ring control has
            constants as valid values, you can view a list of the constants by
            pressing on this control. Select a value by double-clicking on it or by
            selecting it and then pressing .

            


.. function:: get_cal_user_defined_info()

    Vistatus :py:func:`nidcpower.get_cal_user_defined_info`(ViSession vi, ViString info);

    Returns the user-defined information in the device onboard EEPROM.

    


    :rtype: int
    :return:


            Returns the user-defined information stored in the device onboard
            EEPROM.

            


.. function:: get_cal_user_defined_info_max_size()

    Vistatus :py:func:`nidcpower.get_cal_user_defined_info_max_size`(ViSession vi,
    ViInt32\*infoSize);

    Returns the maximum number of characters that can be used to store
    user-defined information in the device onboard EEPROM.

    


    :rtype: int
    :return:


            Returns the number of characters that can be stored in the device
            onboard EEPROM.

            


.. function:: get_channel_name(index, buffer_size)

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

    :rtype: int
    :return:


            Returns the output channel name that corresponds to **index**.

            


.. function:: get_error(buffer_size)

    ViStatus :py:func:`nidcpower.get_error`(ViSession vi, ViStatus \*code, ViInt32
    bufferSize, ViChar description[]);

    | Retrieves and then clears the IVI error information for the session or
      the current execution thread unless **bufferSize** is 0, in which case
      the function does not clear the error information. By passing 0 for
      the buffer size, you can ascertain the buffer size required to get the
      entire error description string and then call the function again with
      a sufficiently large buffer size.
    | If the user specifies a valid IVI session for **vi**, this function
      retrieves and then clears the error information for the session. If
      the user passes VI\_NULL for **vi**, this function retrieves and then
      clears the error information for the current execution thread. If
      **vi** is an invalid session, the function does nothing and returns an
      error. Normally, the error information describes the first error that
      occurred since the user last called :py:func:`nidcpower.get_error` or
      `:py:func:`nidcpower.clear_error` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_ClearError.html')>`__.

    


    :param buffer_size:


        Specifies the number of bytes in the ViChar array you specify for
        **description**.
        If the error description, including the terminating NUL byte, contains
        more bytes than you indicate in this attribute, the function copies
        (buffer size - 1) bytes into the buffer, places an ASCII NUL byte at the
        end of the buffer, and returns the buffer size you must pass to get the
        entire value. For example, if the value is 123456 and the buffer size is
        4, the function places 123 into the buffer and returns 7.
        If you pass 0 for this attribute, you can pass VI\_NULL for
        **description**.

        

    :type buffer_size: int

    :rtype: tuple (code, description)

        WHERE

        code (int): 


            Returns the error code for the session or execution thread.

            

        description (int): 


            Returns the error description for the IVI session or execution thread.
            If there is no description, the function returns an empty string.
            The buffer must contain at least as many elements as the value you
            specify with **bufferSize**. If the error description, including the
            terminating NUL byte, contains more bytes than you indicate with
            **bufferSize**, the function copies (buffer size - 1) bytes into the
            buffer, places an ASCII NUL byte at the end of the buffer, and returns
            the buffer size you must pass to get the entire value. For example, if
            the value is 123456 and the buffer size is 4, the function places 123
            into the buffer and returns 7.
            If you pass 0 for **bufferSize**, you can pass VI\_NULL for this
            attribute.

            


.. function:: get_ext_cal_last_date_and_time()

    Vistatus :py:func:`nidcpower.get_ext_cal_last_date_and_time`(ViSession vi, ViInt32
    \*year, ViInt32 \*month, ViInt32 \*day, ViInt32 \*hour, ViInt32
    \*minute);

    Returns the date and time of the last successful calibration. The time
    returned is 24-hour (military) local time; for example, if the device
    was calibrated at 2:30 PM, this function returns 14 for **hours** and 30
    for **minutes**.

    


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

            


.. function:: get_ext_cal_last_temp()

    Vistatus :py:func:`nidcpower.get_ext_cal_last_temp`(ViSession vi, ViReal64
    \*temperature);

    Returns the onboard **temperature** of the device, in degrees Celsius,
    during the last successful external calibration.

    


    :rtype: float
    :return:


            Returns the onboard **temperature** of the device, in degrees Celsius,
            during the last successful external calibration.

            


.. function:: get_ext_cal_recommended_interval()

    Vistatus :py:func:`nidcpower.get_ext_cal_recommended_interval`(ViSession vi, ViInt32
    \*months);

    Returns the recommended maximum interval, in **months**, between
    external calibrations.

    


    :rtype: int
    :return:


            Specifies the recommended maximum interval, in **months**, between
            external calibrations.

            


.. function:: get_next_coercion_record(buffer_size)

    ViStatus :py:func:`nidcpower.get_next_coercion_record`(ViSession vi, ViInt32
    bufferSize, ViChar coercionRecord[]);

    Returns the coercion information associated with the IVI session and
    clears the earliest instance in which NI-DCPower coerced a value you
    specified.

    


    :param buffer_size:


        Specifies the number of bytes in the ViChar array you specify for
        **coercionRecord**. If the next coercion record string, including the
        terminating NUL byte, contains more bytes than you indicate in this
        attribute, the function copies (buffer size - 1) bytes into the buffer,
        places an ASCII NUL byte at the end of the buffer, and returns the
        buffer size you must pass to get the entire value. For example, if the
        value is 123456 and the buffer size is 4, the function places 123 into
        the buffer and returns 7.
        If you pass 0, you can pass VI\_NULL for **coercionRecord**.

        

    :type buffer_size: int

    :rtype: int
    :return:


            Returns the next **coercionRecord** for the IVI session. If there are no
            **coercionRecords**, the function returns an empty string.

            


.. function:: get_next_interchange_warning(buffer_size)

    ViStatus :py:func:`nidcpower.get_next_interchange_warning`(ViSession vi, ViInt32
    bufferSize, ViChar interchangeWarning[]);

    This function returns the interchangeability warning associated with the
    IVI session. It retrieves and clears the earliest instance in which the
    class driver recorded an interchangeability warning. Interchangeability
    warnings indicate that using your application with a different device
    may cause a different behavior.

    NI-DCPower performs interchangeability checking when the
    `:py:data:`nidcpower.INTERCHANGE\_CHECK` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm','NIDCPOWER_ATTR_INTERCHANGE_CHECK.html')>`__
    attribute is set to VI\_TRUE. This function returns an empty string in
    warning if no interchangeability warnings remain for the session. In
    general, NI-DCPower generates interchangeability warnings when an
    attribute that affects the behavior of the device is in a state that you
    did not specify.

    


    :param buffer_size:


        Specifies the number of bytes in the ViChar array you specify for
        **interchangeWarning**. If the next interchangeability warning string,
        including the terminating NUL byte, contains more bytes than you
        indicate in this attribute, the function copies (buffer size - 1) bytes
        into the buffer, places an ASCII NUL byte at the end of the buffer, and
        returns the buffer size you must pass to get the entire value. For
        example, if the value is 123456 and the buffer size is 4, the function
        places 123 into the buffer and returns 7.
        If you pass 0, you can pass VI\_NULL for **interchangeWarning**.

        

    :type buffer_size: int

    :rtype: int
    :return:


            Returns the next interchange warning for the IVI session. If there are
            no interchange warnings, the function returns an empty string.

            


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

            


.. function:: init_ext_cal(resource_name, password)

    Vistatus :py:func:`nidcpower.init_ext_cal`(ViRsrc resourceName, ViConstString
    password, ViSession \*vi);

    If **password** is valid, this function creates a new IVI instrument
    driver session to the device specified in **resourceName** and returns
    an instrument handle you use to identify the device in all subsequent
    NI-DCPower function calls. This function also sends initialization
    commands to set the device to the state necessary for the operation of
    NI-DCPower.

    Opening a calibration session always performs a reset. Refer to the
    calibration procedure for the device you are calibrating for detailed
    instructions on the appropriate use of this function. This function uses
    the `deprecated programming state
    model <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/initializedeprecatedmodel/>`__.

    


    :param resource_name:


        Specifies the **resourceName** assigned by Measurement & Automation
        Explorer (MAX), for example "PXI1Slot3" where "PXI1Slot3" is an
        instrument's **resourceName**. **resourceName** can also be a logical
        IVI name.

        

    :type resource_name: str
    :param password:


        Specifies the **password** for opening a calibration session. The
        initial password is factory configured to "NI". **password** can be a
        maximum of four alphanumeric characters.

        

    :type password: int

    :rtype: int
    :return:


            Returns a handle that you use to identify the session in all subsequent
            NI-DCPower function calls.

            


.. function:: init_with_options(resource_name, id_query, reset_device, option_string)

    Vistatus :py:func:`nidcpower.init_with_options`(ViRsrc resourceName, ViBoolean
    IDQuery, ViBoolean resetDevice, ViString optionString, ViSession \*vi);

    This function is deprecated. Use
    `:py:func:`nidcpower.initialize_with_channels` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_InitializeWithChannels.html')>`__
    instead.

    Creates a new IVI instrument driver session to the device specified in
    **resourceName** and returns a session handle you use to identify the
    device in all subsequent NI-DCPower function calls. With this function,
    you can optionally set the initial state of the following session
    attributes:

    -  `:py:data:`nidcpower.simulate` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_SIMULATE.html')>`__
    -  `:py:data:`nidcpower.DRIVER\_SETUP` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_DRIVER_SETUP.html')>`__
    -  `:py:data:`nidcpower.RANGE\_CHECK` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_RANGE_CHECK.html')>`__
    -  `:py:data:`nidcpower.QUERY\_INSTRUMENT\_STATUS` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_QUERY_INSTRUMENT_STATUS.html')>`__
    -  `:py:data:`nidcpower.cache` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_CACHE.html')>`__
    -  `:py:data:`nidcpower.RECORD\_COERCIONS` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_RECORD_COERCIONS.html')>`__

    This function also sends initialization commands to set the device to
    the state necessary for NI-DCPower to operate.

    To place the device in a known start-up state when creating a new
    session, set **resetDevice** to VI\_TRUE. This action is equivalent to
    using the
    `:py:func:`nidcpower.reset` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_reset.html')>`__
    function.

    To open a session and leave the device in its existing configuration
    without passing through a transitional output state, set **resetDevice**
    to VI\_FALSE, and immediately call the
    `:py:func:`nidcpower.abort` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_Abort.html')>`__
    function. Then configure the device as in the previous session changing
    only the desired settings, and then call the
    `:py:func:`nidcpower.initiate` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_Initiate.html')>`__
    function.

    Refer to the `deprecated programming state
    model <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/initializedeprecatedmodel/>`__
    for information about the specific software states.

    


    :param resource_name:


        Specifies the **resourceName** assigned by Measurement & Automation
        Explorer (MAX), for example "PXI1Slot3" where "PXI1Slot3" is an
        instrument's **resourceName**. **resourceName** can also be a logical
        IVI name.

        

    :type resource_name: str
    :param id_query:


        Specifies whether the device is queried to determine if the device is a
        valid instrument for NI-DCPower.

        

    :type id_query: bool
    :param reset_device:


        Specifies whether to reset the device during the initialization
        procedure.

        

    :type reset_device: bool
    :param option_string:


        Specifies the initial value of certain attributes for the session. The
        syntax for **optionString** is a list of attributes with an assigned
        value where 1 is VI\_TRUE and 0 is VI\_FALSE. Each attribute/value
        combination is delimited with a comma, as shown in the following
        example:

        "Simulate=0,RangeCheck=1,QueryInstrStatus=0,Cache=1"

        If you do not wire this input or pass an empty string, the session
        assigns the default values, shown in the example, for these attributes.
        You do not have to specify a value for all the attributes. If you do not
        specify a value for an attribute, the default value is used.

        For more information about simulating a device, refer to `Simulating a
        Power Supply or
        SMU <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/simulate/>`__.

        

    :type option_string: int

    :rtype: int
    :return:


            Returns a handle that you use to identify the device in all subsequent
            NI-DCPower function calls.

            


.. function:: initialize_with_channels(resource_name, channels, reset, option_string)

    Vistatus :py:func:`nidcpower.initialize_with_channels`(ViRsrc resourceName,
    ViConstString channels, ViBoolean reset, ViConstString optionString,
    ViSession \*vi);

    Creates and returns a new NI-DCPower session to the power supply or SMU
    specified in **resource name** to be used in all subsequent NI-DCPower
    function calls. With this function, you can optionally set the initial
    state of the following session attributes:

    -  `:py:data:`nidcpower.simulate` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_SIMULATE.html')>`__
    -  `:py:data:`nidcpower.DRIVER\_SETUP` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'NIDCPOWER_ATTR_DRIVER_SETUP.html')>`__

    After calling this function, the session will be in the Uncommitted
    state. Refer to the `Programming
    States <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/programmingstates/>`__
    topic for details about specific software states.

    To place the device in a known start-up state when creating a new
    session, set **reset** to VI\_TRUE. This action is equivalent to using
    the
    `:py:func:`nidcpower.reset` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_reset.html')>`__
    function immediately after initializing the session.

    To open a session and leave the device in its existing configuration
    without passing through a transitional output state, set **reset** to
    VI\_FALSE. Then configure the device as in the previous session,
    changing only the desired settings, and then call the
    `:py:func:`nidcpower.initiate` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_Initiate.html')>`__
    function.

    **Related Topics:**

    `Programming
    States <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/programmingstates/>`__

    


    :param resource_name:


        Specifies the **resourceName** assigned by Measurement & Automation
        Explorer (MAX), for example "PXI1Slot3" where "PXI1Slot3" is an
        instrument's **resourceName**. **resourceName** can also be a logical
        IVI name.

        

    :type resource_name: str
    :param channels:


        Specifies which output channel(s) to include in a new session. Specify
        multiple channels by using a channel list or a channel range. A channel
        list is a comma (,) separated sequence of channel names (for example,
        0,2 specifies channels 0 and 2). A channel range is a lower bound
        channel followed by a hyphen (-) or colon (:) followed by an upper bound
        channel (for example, 0-2 specifies channels 0, 1, and 2). In the
        Running state, multiple output channel configurations are performed
        sequentially based on the order specified in this parameter. If you do
        not specify any channels, by default all channels on the device are
        included in the session.

        

    :type channels: int
    :param reset:


        Specifies whether to reset the device during the initialization
        procedure.

        

    :type reset: bool
    :param option_string:


        Specifies the initial value of certain attributes for the session. The
        syntax for **optionString** is a list of attributes with an assigned
        value where 1 is VI\_TRUE and 0 is VI\_FALSE. For example:

        "Simulate=0"

        You do not have to specify a value for all the attributes. If you do not
        specify a value for an attribute, the default value is used.

        For more information about simulating a device, refer to `Simulating a
        Power Supply or
        SMU <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/simulate/>`__.

        

    :type option_string: int

    :rtype: int
    :return:


            Returns a session handle that you use to identify the device in all
            subsequent NI-DCPower function calls.

            


.. function:: initiate()

    Vistatus :py:func:`nidcpower.initiate`(ViSession vi);

    Starts generation or acquisition, causing the NI-DCPower session to
    leave the Uncommitted state or Committed state and enter the Running
    state. To return to the Committed state call the
    `:py:func:`nidcpower.abort` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_Abort.html')>`__
    function. Refer to the `Programming
    States <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/programmingstates/>`__
    topic in the *NI DC Power Supplies and SMUs Help* for information about
    the specific NI-DCPower software states.

    **Related Topics:**

    `Programming
    States <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/programmingstates/>`__

    


.. function:: lock_session()

    Vistatus :py:func:`nidcpower.lock_session`(ViSession vi, ViBoolean
    \*callerHasLock);

    | Obtains a multithread lock on the device session. Before doing so, the
      software waits until all other execution threads release their locks
      on the device session.
    | Other threads may have obtained a lock on this session for the
      following reasons:

    -  The application called the :py:func:`nidcpower.lock_session` function.
    -  A call to NI-DCPower locked the session.
    -  A call to the IVI engine locked the session.
    -  After a call to the :py:func:`nidcpower.lock_session` function returns
       successfully, no other threads can access the device session until
       you call the
       `:py:func:`nidcpower.unlock_session` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_UnlockSession.html')>`__
       function.
    -  Use the :py:func:`nidcpower.lock_session` function and the
       :py:func:`nidcpower.unlock_session` function around a sequence of calls to
       instrument driver functions if you require that the device retain its
       settings through the end of the sequence.

    You can safely make nested calls to the :py:func:`nidcpower.lock_session` function
    within the same thread. To completely unlock the session, you must
    balance each call to the :py:func:`nidcpower.lock_session` function with a call to
    the :py:func:`nidcpower.unlock_session` function. If, however, you use
    **caller_has_lock** in all calls to the :py:func:`nidcpower.lock_session` and
    :py:func:`nidcpower.unlock_session` function within a function, the IVI Library
    locks the session only once within the function regardless of the number
    of calls you make to the :py:func:`nidcpower.lock_session` function. This behavior
    allows you to call the :py:func:`nidcpower.unlock_session` function just once at
    the end of the function.

    


    :rtype: bool
    :return:


            | This parameter is optional. If you do not want to use this parameter,
              pass VI\_NULL.
            | Use this parameter in complex functions to keep track of whether you
              obtain a lock and therefore need to unlock the session. Pass the
              address of a local ViBoolean variable. In the declaration of the local
              variable, initialize it to VI\_FALSE. Pass the address of the same
              local variable to any other calls you make to the
              :py:func:`nidcpower.lock_session` function or the :py:func:`nidcpower.unlock_session`
              function in the same function.
            | The parameter is an input/output parameter. The :py:func:`nidcpower.lock_session`
              and :py:func:`nidcpower.unlock_session` functions each inspect the current value
              and take the following actions.

            -  If the value is VI\_TRUE, the :py:func:`nidcpower.lock_session` function does
               not lock the session again.
            -  If the value is VI\_FALSE, the :py:func:`nidcpower.lock_session` function
               obtains the lock and sets the value of the parameter to VI\_TRUE.
            -  If the value is VI\_FALSE, the :py:func:`nidcpower.unlock_session` function does
               not attempt to unlock the session.
            -  If the value is VI\_TRUE, the :py:func:`nidcpower.unlock_session` function
               releases the lock and sets the value of the parameter to VI\_FALSE.

            | Thus, you can, call the :py:func:`nidcpower.unlock_session` function at the end
              of your function without worrying about whether you actually have the
              lock, as shown in the following example.
            | ViStatus TestFunc (ViSession vi, ViInt32 flags)
              {
              ViStatus error = VI\_SUCCESS;
              ViBoolean haveLock = VI\_FALSE;
              if (flags & BIT\_1)
              {
              viCheckErr( :py:func:`nidcpower.lock_session`(vi, &haveLock;));
              viCheckErr( TakeAction1(vi));
              if (flags & BIT\_2)
              {
              viCheckErr( :py:func:`nidcpower.unlock_session`(vi, &haveLock;));
              viCheckErr( TakeAction2(vi));
              viCheckErr( :py:func:`nidcpower.lock_session`(vi, &haveLock;);
              }
              if (flags & BIT\_3)
              viCheckErr( TakeAction3(vi));
              }
              Error:
              /\*At this point, you cannot really be sure that you have the lock.
              Fortunately, the haveLock variable takes care of that for you.\*/
              :py:func:`nidcpower.unlock_session`(vi, &haveLock;);
              return error;
            | }

            


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

        

    :type channel_name: int
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

        

    :type channel_name: int

    :rtype: tuple (voltage_measurements, current_measurements)

        WHERE

        voltage_measurements (float): 


            Returns an array of voltage measurements. The measurements in the array
            are returned in the same order as the channels specified in
            **channelName**. Ensure that sufficient space has been allocated for the
            returned array.

            

        current_measurements (float): 


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

        

    :type channel_name: int

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

        

    :type channel_name: int
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

        

    :type channel_name: int
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

        

    :type channel_name: int
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

        

    :type channel_name: int
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

    


.. function:: reset_interchange_check()

    Vistatus :py:func:`nidcpower.reset_interchange_check`(ViSession vi);

    When developing a complex test system that consists of multiple test
    modules, it is generally a good idea to design the test modules so that
    they can run in any order. To do so requires ensuring that each test
    module completely configures the state of each instrument it uses. If a
    particular test module does not completely configure the state of an
    instrument, the state of the instrument depends on the configuration
    from a previously executed test module. If you execute the test modules
    in a different order, the behavior of the instrument and therefore the
    entire test module is likely to change. This change in behavior is
    generally instrument specific and represents an interchangeability
    problem.

    You can use this function to test for such cases. After you call this
    function, the interchangeability checking algorithms in the specific
    driver ignore all previous configuration operations. By calling this
    function at the beginning of a test module, you can determine whether
    the test module has dependencies on the operation of previously executed
    test modules.

    This function does not clear the interchangeability warnings from the
    list of previously recorded interchangeability warnings. If you want to
    guarantee that the
    `:py:func:`nidcpower.get_next_interchange_warning` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_GetNextInterchangeWarning.html')>`__
    function only returns those interchangeability warnings that are
    generated after calling this function, you must clear the list of
    interchangeability warnings. You can clear the interchangeability
    warnings list by repeatedly calling the
    :py:func:`nidcpower.get_next_interchange_warning` function until no more
    interchangeability warnings are returned. If you are not interested in
    the content of those warnings, you can call the
    `:py:func:`nidcpower.clear_interchange_warnings` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_ClearInterchangeWarnings.html')>`__
    function.

    

    .. note:: :py:func:`nidcpower.get_next_interchange_warning` does not mark any attributes for
        an interchange check.


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

.. function:: set_attribute_vi_boolean(attribute_id, attribute_value)

    Vistatus :py:func:`nidcpower.set_attribute_vi_boolean`(ViSession vi, ViConstString
    channelName, ViAttr attribute, ViBoolean value);

    | Sets the value of a ViBoolean attribute.
    | This is a low-level function that you can use to set the values of
      device-specific attributes and inherent IVI attributes.

    


    :param channel_name:


        Specifies the output channel(s) to which this configuration value
        applies. Specify multiple channels by using a channel list or a channel
        range. A channel list is a comma (,) separated sequence of channel names
        (for example, 0,2 specifies channels 0 and 2). A channel range is a
        lower bound channel followed by a hyphen (-) or colon (:) followed by an
        upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
        In the Running state, multiple output channel configurations are
        performed sequentially based on the order specified in this parameter.

        

    :type channel_name: int
    :param attribute_id:


        Specifies the ID of an attribute. From the function panel window, you
        can use this control as follows.

        -  In the function panel window, click on the control or press **Enter**
           or the spacebar to display a dialog box containing hierarchical list
           of the available attributes. Attributes whose value cannot be set are
           dim. Help text is shown for each attribute. Select an attribute by
           double-clicking on it or by selecting it and then pressing **Enter**.
        -  Read-only attributes appear dim in the list box. If you select a
           read-only attribute, an error message appears. A ring control at the
           top of the dialog box allows you to see all IVI attributes or only
           the attributes of type ViBoolean. If you choose to see all IVI
           attributes, the data types appear to the right of the attribute names
           in the list box. Attributes with data types other than ViBoolean are
           dim. If you select an attribute data type that is dim, LabWindows/CVI
           transfers you to the function panel for the corresponding function
           that is consistent with the data type.
        -  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
           change this ring control to a manual input box. If the attribute in
           this ring control has named constants as valid values, you can view
           the constants by moving to the value control and pressing **Enter**.

        

    :type attribute_id: int
    :param attribute_value:


        Specifies the value to which you want to set the attribute. If the
        attribute currently showing in the attribute ring control has constants
        as valid values, you can view a list of the constants by pressing
        **Enter** on this control. Select a value by double-clicking on it or by
        selecting it and then pressing **Enter**.

        

        .. note:: Some of the values might not be valid depending upon the current
            settings of the device session.

    :type attribute_value: bool

.. function:: set_attribute_vi_int32(attribute_id, attribute_value)

    Vistatus :py:func:`nidcpower.set_attribute_vi_int32`(ViSession vi, ViConstString
    channelName, ViAttr attribute, ViInt32 value);

    | Sets the value of a ViInt32 attribute.
    | This is a low-level function that you can use to set the values of
      device-specific attributes and inherent IVI attributes.

    


    :param channel_name:


        Specifies the output channel(s) to which this configuration value
        applies. Specify multiple channels by using a channel list or a channel
        range. A channel list is a comma (,) separated sequence of channel names
        (for example, 0,2 specifies channels 0 and 2). A channel range is a
        lower bound channel followed by a hyphen (-) or colon (:) followed by an
        upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
        In the Running state, multiple output channel configurations are
        performed sequentially based on the order specified in this parameter.

        

    :type channel_name: int
    :param attribute_id:


        Specifies the ID of an attribute. From the function panel window, you
        can use this control as follows.

        -  In the function panel window, click on the control or press **Enter**
           or the spacebar to display a dialog box containing hierarchical list
           of the available attributes. Attributes whose value cannot be set are
           dim. Help text is shown for each attribute. Select an attribute by
           double-clicking on it or by selecting it and then pressing **Enter**.
        -  Read-only attributes appear dim in the list box. If you select a
           read-only attribute, an error message appears. A ring control at the
           top of the dialog box allows you to see all IVI attributes or only
           the attributes of type ViInt32. If you choose to see all IVI
           attributes, the data types appear to the right of the attribute names
           in the list box. Attributes with data types other than ViInt32 are
           dim. If you select an attribute data type that is dim, LabWindows/CVI
           transfers you to the function panel for the corresponding function
           that is consistent with the data type.
        -  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
           change this ring control to a manual input box. If the attribute in
           this ring control has named constants as valid values, you can view
           the constants by moving to the value control and pressing **Enter**.

        

    :type attribute_id: int
    :param attribute_value:


        Specifies the value to which you want to set the attribute. If the
        attribute currently showing in the attribute ring control has constants
        as valid values, you can view a list of the constants by pressing
        **Enter** on this control. Select a value by double-clicking on it or by
        selecting it and then pressing **Enter**.

        

        .. note:: Some of the values might not be valid depending upon the current
            settings of the device session.

    :type attribute_value: int

.. function:: set_attribute_vi_int64(attribute_id, attribute_value)

    Vistatus :py:func:`nidcpower.set_attribute_vi_int64`(ViSession vi, ViConstString
    channelName, ViAttr attribute, ViInt64 value);

    | Sets the value of a ViInt64 attribute.
    | This is a low-level function that you can use to set the values of
      device-specific attributes and inherent IVI attributes.

    


    :param channel_name:


        Specifies the output channel(s) to which this configuration value
        applies. Specify multiple channels by using a channel list or a channel
        range. A channel list is a comma (,) separated sequence of channel names
        (for example, 0,2 specifies channels 0 and 2). A channel range is a
        lower bound channel followed by a hyphen (-) or colon (:) followed by an
        upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
        In the Running state, multiple output channel configurations are
        performed sequentially based on the order specified in this parameter.

        

    :type channel_name: int
    :param attribute_id:


        Specifies the ID of an attribute. From the function panel window, you
        can use this control as follows.

        -  In the function panel window, click on the control or press **Enter**
           or the spacebar to display a dialog box containing hierarchical list
           of the available attributes. Attributes whose value cannot be set are
           dim. Help text is shown for each attribute. Select an attribute by
           double-clicking on it or by selecting it and then pressing **Enter**.
        -  Read-only attributes appear dim in the list box. If you select a
           read-only attribute, an error message appears. A ring control at the
           top of the dialog box allows you to see all IVI attributes or only
           the attributes of type ViReal64. If you choose to see all IVI
           attributes, the data types appear to the right of the attribute names
           in the list box. Attributes with data types other than ViReal64 are
           dim. If you select an attribute data type that is dim, LabWindows/CVI
           transfers you to the function panel for the corresponding function
           that is consistent with the data type.
        -  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
           change this ring control to a manual input box. If the attribute in
           this ring control has named constants as valid values, you can view
           the constants by moving to the value control and pressing **Enter**.

        

    :type attribute_id: int
    :param attribute_value:


        Specifies the value to which you want to set the attribute. If the
        attribute currently showing in the attribute ring control has constants
        as valid values, you can view a list of the constants by pressing
        **Enter** on this control. Select a value by double-clicking on it or by
        selecting it and then pressing **Enter**.

        

        .. note:: Some of the values might not be valid depending upon the current
            settings of the device session.

    :type attribute_value: int

.. function:: set_attribute_vi_real64(attribute_id, attribute_value)

    Vistatus :py:func:`nidcpower.set_attribute_vi_real64`(ViSession vi, ViConstString
    channelName, ViAttr attribute, ViReal64 value);

    | Sets the value of a ViReal64 attribute.
    | This is a low-level function that you can use to set the values of
      device-specific attributes and inherent IVI attributes.

    


    :param channel_name:


        Specifies the output channel(s) to which this configuration value
        applies. Specify multiple channels by using a channel list or a channel
        range. A channel list is a comma (,) separated sequence of channel names
        (for example, 0,2 specifies channels 0 and 2). A channel range is a
        lower bound channel followed by a hyphen (-) or colon (:) followed by an
        upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
        In the Running state, multiple output channel configurations are
        performed sequentially based on the order specified in this parameter.

        

    :type channel_name: int
    :param attribute_id:


        Specifies the ID of an attribute. From the function panel window, you
        can use this control as follows.

        -  In the function panel window, click on the control or press **Enter**
           or the spacebar to display a dialog box containing hierarchical list
           of the available attributes. Attributes whose value cannot be set are
           dim. Help text is shown for each attribute. Select an attribute by
           double-clicking on it or by selecting it and then pressing **Enter**.
        -  Read-only attributes appear dim in the list box. If you select a
           read-only attribute, an error message appears. A ring control at the
           top of the dialog box allows you to see all IVI attributes or only
           the attributes of type ViReal64. If you choose to see all IVI
           attributes, the data types appear to the right of the attribute names
           in the list box. Attributes with data types other than ViReal64 are
           dim. If you select an attribute data type that is dim, LabWindows/CVI
           transfers you to the function panel for the corresponding function
           that is consistent with the data type.
        -  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
           change this ring control to a manual input box. If the attribute in
           this ring control has named constants as valid values, you can view
           the constants by moving to the value control and pressing **Enter**.

        

    :type attribute_id: int
    :param attribute_value:


        Specifies the value to which you want to set the attribute. If the
        attribute currently showing in the attribute ring control has constants
        as valid values, you can view a list of the constants by pressing
        **Enter** on this control. Select a value by double-clicking on it or by
        selecting it and then pressing **Enter**.

        

        .. note:: Some of the values might not be valid depending upon the current
            settings of the device session.

    :type attribute_value: float

.. function:: set_attribute_vi_session(attribute_id, attribute_value)

    Vistatus :py:func:`nidcpower.set_attribute_vi_session`(ViSession vi, ViConstString
    channelName, ViAttr attribute, ViSession value);

    | Sets the value of a ViSession attribute.
    | This is a low-level function that you can use to set the values of
      device-specific attributes and inherent IVI attributes.

    


    :param channel_name:


        Specifies the output channel(s) to which this configuration value
        applies. Specify multiple channels by using a channel list or a channel
        range. A channel list is a comma (,) separated sequence of channel names
        (for example, 0,2 specifies channels 0 and 2). A channel range is a
        lower bound channel followed by a hyphen (-) or colon (:) followed by an
        upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
        In the Running state, multiple output channel configurations are
        performed sequentially based on the order specified in this parameter.

        

    :type channel_name: int
    :param attribute_id:


        Specifies the ID of an attribute. From the function panel window, you
        can use this control as follows.

        -  In the function panel window, click on the control or press **Enter**
           or the spacebar to display a dialog box containing hierarchical list
           of the available attributes. Attributes whose value cannot be set are
           dim. Help text is shown for each attribute. Select an attribute by
           double-clicking on it or by selecting it and then pressing **Enter**.
        -  Read-only attributes appear dim in the list box. If you select a
           read-only attribute, an error message appears. A ring control at the
           top of the dialog box allows you to see all IVI attributes or only
           the attributes of type ViSession. If you choose to see all IVI
           attributes, the data types appear to the right of the attribute names
           in the list box. Attributes with data types other than ViSession are
           dim. If you select an attribute data type that is dim, LabWindows/CVI
           transfers you to the function panel for the corresponding function
           that is consistent with the data type.
        -  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
           change this ring control to a manual input box. If the attribute in
           this ring control has named constants as valid values, you can view
           the constants by moving to the value control and pressing **Enter**.

        

    :type attribute_id: int
    :param attribute_value:


        Specifies the value to which you want to set the attribute. If the
        attribute currently showing in the attribute ring control has constants
        as valid values, you can view a list of the constants by pressing
        **Enter** on this control. Select a value by double-clicking on it or by
        selecting it and then pressing **Enter**.

        

        .. note:: Some of the values might not be valid depending upon the current
            settings of the device session.

    :type attribute_value: int

.. function:: set_attribute_vi_string(attribute_id, attribute_value)

    Vistatus :py:func:`nidcpower.set_attribute_vi_string`(ViSession vi, ViConstString
    channelName, ViAttr attribute, ViConstString value);

    | Sets the value of a ViString attribute.
    | This is a low-level function that you can use to set the values of
      device-specific attributes and inherent IVI attributes.

    


    :param channel_name:


        Specifies the output channel(s) to which this configuration value
        applies. Specify multiple channels by using a channel list or a channel
        range. A channel list is a comma (,) separated sequence of channel names
        (for example, 0,2 specifies channels 0 and 2). A channel range is a
        lower bound channel followed by a hyphen (-) or colon (:) followed by an
        upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
        In the Running state, multiple output channel configurations are
        performed sequentially based on the order specified in this parameter.

        

    :type channel_name: int
    :param attribute_id:


        Specifies the ID of an attribute. From the function panel window, you
        can use this control as follows.

        -  In the function panel window, click on the control or press **Enter**
           or the spacebar to display a dialog box containing hierarchical list
           of the available attributes. Attributes whose value cannot be set are
           dim. Help text is shown for each attribute. Select an attribute by
           double-clicking on it or by selecting it and then pressing **Enter**.
        -  Read-only attributes appear dim in the list box. If you select a
           read-only attribute, an error message appears. A ring control at the
           top of the dialog box allows you to see all IVI attributes or only
           the attributes of type ViString. If you choose to see all IVI
           attributes, the data types appear to the right of the attribute names
           in the list box. Attributes with data types other than ViString are
           dim. If you select an attribute data type that is dim, LabWindows/CVI
           transfers you to the function panel for the corresponding function
           that is consistent with the data type.
        -  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
           change this ring control to a manual input box. If the attribute in
           this ring control has named constants as valid values, you can view
           the constants by moving to the value control and pressing **Enter**.

        

    :type attribute_id: int
    :param attribute_value:


        Specifies the value to which you want to set the attribute. If the
        attribute currently showing in the attribute ring control has constants
        as valid values, you can view a list of the constants by pressing
        **Enter** on this control. Select a value by double-clicking on it or by
        selecting it and then pressing **Enter**.

        

        .. note:: Some of the values might not be valid depending upon the current
            settings of the device session.

    :type attribute_value: int

.. function:: set_cal_user_defined_info(info)

    Vistatus :py:func:`nidcpower.set_cal_user_defined_info`(ViSession vi, ViConstString
    info);

    Stores a user-defined string of characters in the device onboard EEPROM.
    If the string is longer than the maximum allowable size, it is
    truncated. This function overwrites any existing user-defined
    information.

    If you call this function in a session, **info** is immediately changed.
    If you call this function in an external calibration session, **info**
    is changed only after you close the session using the
    `:py:func:`nidcpower.close_ext_cal` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_CloseExtCal.html')>`__
    function with **action** set to NIDCPOWER\_VAL\_COMMIT.

    


    :param info:


        Specifies the string to store in the device onboard EEPROM.

        

    :type info: int

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

        

    :type channel_name: int
    :param values:


        Specifies the series of voltage levels or current levels, depending on
        the configured `output
        function <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/programming_output/>`__.
        **Valid values**:
        The valid values for this parameter are defined by the voltage level
        range or current level range.

        

    :type values: float
    :param source_delays:


        Specifies the source delay that follows the configuration of each value
        in the sequence.
        **Valid Values**:
        The valid values are between 0 and 167 seconds.

        

    :type source_delays: float
    :param size:


        The number of elements in the Values and the Source Delays arrays. The
        Values and Source Delays arrays should have the same size.

        

    :type size: int

.. function:: unlock_session()

    Vistatus :py:func:`nidcpower.unlock_session`(ViSession vi, ViBoolean
    \*callerHasLock);

    Releases a lock that you acquired on an device session using
    `:py:func:`nidcpower.lock_session` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_LockSession.html')>`__.
    Refer to :py:func:`nidcpower.lock_session` for additional information on session
    locks.

    


    :rtype: bool
    :return:


            | This attribute is optional. If you do not want to use this attribute,
              pass VI\_NULL.
            | Use this attribute in complex functions to keep track of whether you
              obtain a lock and therefore need to unlock the session.
            | Pass the address of a local ViBoolean variable. In the declaration of
              the local variable, initialize it to VI\_FALSE. Pass the address of
              the same local variable to any other calls you make to
              :py:func:`nidcpower.lock_session` or :py:func:`nidcpower.unlock_session` in the same
              function.
            | The parameter is an input/output parameter. :py:func:`nidcpower.lock_session` and
              :py:func:`nidcpower.unlock_session` each inspect the current value and take the
              following actions.

            -  If the value is VI\_TRUE, :py:func:`nidcpower.lock_session` does not lock the
               session again.
            -  If the value is VI\_FALSE, :py:func:`nidcpower.lock_session` obtains the lock
               and sets the value of the parameter to VI\_TRUE.
            -  If the value is VI\_FALSE, :py:func:`nidcpower.unlock_session` does not attempt
               to unlock the session.
            -  If the value is VI\_TRUE, :py:func:`nidcpower.unlock_session` releases the lock
               and sets the value of the parameter to VI\_FALSE.

            | Thus, you can, call :py:func:`nidcpower.unlock_session` at the end of your
              function without worrying about whether you actually have the lock, as
              the following example shows.
            | ViStatus TestFunc (ViSession vi, ViInt32 flags)
              {
              ViStatus error = VI\_SUCCESS;
              ViBoolean haveLock = VI\_FALSE;
              if (flags & BIT\_1)
              {
              viCheckErr( :py:func:`nidcpower.lock_session`(vi, &haveLock;));
              viCheckErr( TakeAction1(vi));
              if (flags & BIT\_2)
              {
              viCheckErr( :py:func:`nidcpower.unlock_session`(vi, &haveLock;));
              viCheckErr( TakeAction2(vi));
              viCheckErr( :py:func:`nidcpower.lock_session`(vi, &haveLock;);
              }
              if (flags & BIT\_3)
              viCheckErr( TakeAction3(vi));
              }
              Error:
              /\*At this point, you cannot really be sure that you have the lock.
              Fortunately, the haveLock variable takes care of that for you.\*/
              :py:func:`nidcpower.unlock_session`(vi, &haveLock;);
              return error;
              }

            


.. function:: wait_for_event(event_id, timeout)

    Vistatus :py:func:`nidcpower.wait_for_event`(ViSession vi, ViInt32 eventId, ViReal64
    timeout);

    Waits until the device has generated the specified event.

    The session monitors whether each type of event has occurred at least
    once since the last time this function or the
    `:py:func:`nidcpower.initiate` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_Initiate.html')>`__
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

.. function:: close()

    Vistatus :py:func:`nidcpower.close`(ViSession vi);

    Closes the session specified in **vi** and deallocates the resources
    that NI-DCPower reserves. If power output is enabled when you call this
    function, the output channels remain in their existing state and
    continue providing power. Use the
    `:py:func:`nidcpower.configure_output_enabled` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_ConfigureOutputEnabled.html')>`__
    function to disable power output on a per channel basis. Use the
    `:py:func:`nidcpower.reset` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_reset.html')>`__
    function to disable power output on all channel(s).

    **Related Topics:**

    `Programming
    States <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/programmingstates/>`__

    


.. function:: error_message(error_code)

    Vistatus :py:func:`nidcpower.error_message`(ViSession vi, Vistatus errorCode,
    ViChar errorMessage[256]);

    Converts a status code returned by an instrument driver function into a
    user-readable string.

    


    :param error_code:


        Specifies the **status** parameter that is returned from any of the
        NI-DCPower functions.

        

    :type error_code: int

    :rtype: int
    :return:


            Returns the user-readable message string that corresponds to the status
            code you specify.
            You must pass a ViChar array with at least 256 bytes.

            


.. function:: init(resource_name, id_query, reset_device)

    Vistatus :py:func:`nidcpower.init`(ViRsrc resourceName, ViBoolean IDQuery,
    ViBoolean resetDevice, ViSession \*vi);

    This function is deprecated. Use
    `:py:func:`nidcpower.initialize_with_channels` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_InitializeWithChannels.html')>`__
    instead.

    Creates a new IVI instrument driver session to the device specified in
    **resourceName** and returns a session handle you use to identify the
    device in all subsequent NI-DCPower function calls. This function also
    sends initialization commands to set the device to the state necessary
    for the operation of NI-DCPower.

    To place the device in a known start-up state when creating a new
    session, set **resetDevice** to VI\_TRUE. This action is equivalent to
    using the
    `:py:func:`nidcpower.reset` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_reset.html')>`__
    function.

    To open a session and leave the device in its existing configuration
    without passing through a transitional output state, set **resetDevice**
    to VI\_FALSE, and immediately call the
    `:py:func:`nidcpower.abort` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_Abort.html')>`__
    function. Then configure the device as in the previous session, changing
    only the desired settings, and then call the
    `:py:func:`nidcpower.initiate` <javascript:LaunchMergedHelp('NI_DC_Power_Supplies_Help.chm',%20'NIDCPowerCRef.chm',%20'cviniDCPower_Initiate.html')>`__
    function. Refer to the `deprecated programming state
    model <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/initializedeprecatedmodel/>`__
    for information about the specific software states.

    


    :param resource_name:


        Specifies the **resourceName** assigned by Measurement & Automation
        Explorer (MAX), for example "PXI1Slot3" where "PXI1Slot3" is an
        instrument's **resourceName**. **resourceName** can also be a logical
        IVI name.

        

    :type resource_name: str
    :param id_query:


        Specifies whether the device is queried to determine if the device is a
        valid instrument for NI-DCPower.
        **Defined Values**:

        +---------------+--------------------------+
        | VI\_TRUE (1)  | Perform ID query.        |
        +---------------+--------------------------+
        | VI\_FALSE (0) | Do not perform ID query. |
        +---------------+--------------------------+

    :type id_query: bool
    :param reset_device:


        Specifies whether to reset the device during the initialization
        procedure.
        **Defined Values**:

        +---------------+--------------------------+
        | VI\_TRUE (1)  | Reset the device.        |
        +---------------+--------------------------+
        | VI\_FALSE (0) | Do not reset the device. |
        +---------------+--------------------------+

    :type reset_device: bool

    :rtype: int
    :return:


            Returns a session handle that you use to identify the session in all
            subsequent NI-DCPower function calls.

            


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

        instrument_driver_revision (int): 


            Returns the driver revision information for NI-DCPower.

            

        firmware_revision (int): 


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

        self_test_message (int): 


            Returns the self-test result message. The size of this array must be at
            least 256 bytes.

            



